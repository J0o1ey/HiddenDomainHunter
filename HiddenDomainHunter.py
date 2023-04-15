import itertools
import re
import argparse
import threading
import requests

def get_subdomains_prefix(filename):
    with open(filename, 'r') as f:
        domains = f.read().splitlines()

    subdomains = []
    pattern = r'(?:^|\.)((?:\w+\-)?\w+)\.(?:\w+\.)*(\w+\.\w{2,})$'
    for domain in domains:
        match = re.search(pattern, domain)
        if match:
            # 获取所有匹配项并去重
            matches = set(match.groups())
            subdomains.extend(matches)
    # 去重
    subdomains = list(set(subdomains))
    for subdomain_prefix in subdomains:
        with open("domain_prefix.txt","a") as subdomain_prefix_file:
            subdomain_prefix_file.write(subdomain_prefix+ "\n")
    print("[*] Subdomain_prefix has been written to doman_prefix.txt ")


def combine_domain(root_domain):
    with open("domain_prefix.txt", "r") as f:
        prefixes = f.read().splitlines()
    with open("key.txt", "r") as f:
        keywords = f.read().splitlines()
    with open("root_domain.txt", "r") as f:
        root_domains = f.read().splitlines()

    # 笛卡尔积生成所有可能的排列组合
    subdomains = []
    for prefix in prefixes:
        for keyword in keywords:
            subdomains.append(prefix + keyword)
        for keyword in keywords:
            subdomains.append(prefix + "-" + keyword)
    for subdomain in itertools.product(subdomains, root_domains):
        subdomain = ".".join(subdomain)
        with open("subdomains.txt", "a") as f:
            f.write(subdomain + "\n")
    print("[+] Based on the existing information, all possible subdomain information has been generated to subdomains.txt")

class CheckUrlThread(threading.Thread):
    def __init__(self, url):
        super(CheckUrlThread, self).__init__()
        self.url = url

    def run(self):
        try:
            res = requests.head(self.url, timeout=3)
            if res.status_code < 400:
                #print(f"{self.url} is alive")
                res = requests.get(self.url, timeout=3)
                title = re.search('<title>(.*?)</title>', res.text)
                if title:
                    print(f"{self.url} title: {title.group(1)}")
                else:
                    print(f"{self.url} title: null")
        except:
            pass


def main():
    parser = argparse.ArgumentParser(description="Combined with the existing network asset information，to discover the hidden assets of the manufacturer")

    parser.add_argument('-f', '--file', dest='filename', required=True,
                        help='the name of the file containing the list of domains')
    parser.add_argument('-rd', '--root-domain', dest='root_domain_file', required=False,
                        help='root domain file')
    args = parser.parse_args()

    print("""
     _   _ _     _     _            ____                        _       _   _             _            
    | | | (_) __| | __| | ___ _ __ |  _ \  ___  _ __ ___   __ _(_)_ __ | | | |_   _ _ __ | |_ ___ _ __ 
    | |_| | |/ _` |/ _` |/ _ \ '_ \| | | |/ _ \| '_ ` _ \ / _` | | '_ \| |_| | | | | '_ \| __/ _ \ '__|
    |  _  | | (_| | (_| |  __/ | | | |_| | (_) | | | | | | (_| | | | | |  _  | |_| | | | | ||  __/ |   
    |_| |_|_|\__,_|\__,_|\___|_| |_|____/ \___/|_| |_| |_|\__,_|_|_| |_|_| |_|\__,_|_| |_|\__\___|_|   
                                                                                       Author:J0o1ey
       """)

    get_subdomains_prefix(args.filename)
    combine_domain(args.root_domain_file)
    with open("subdomains.txt", "r") as f:
        urls = f.read().splitlines()

    threads = []
    for url in urls:
        if not url.startswith("http"):
            url = f"http://{url}"
        threads.append(CheckUrlThread(url))
        if not url.startswith("https"):
            url = f"https://{url}"
        threads.append(CheckUrlThread(url))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()