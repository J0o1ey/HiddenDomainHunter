## HiddenDomainHunter

### Design ideas

In the process of attack surface mining and vulnerability mining, we encounter some large targets often in ** domain name ** shows a certain rule

It makes us feel like there's a trail

For example, many manufacturers use various keywords to express the nature of the domain name in the business, such as:

```
Test environment:
uat
test

Development environment:
dev

api system:
api

Gateway:
gataway

Pre-launch environment:
pre
pro
```



There are also many of the manufacturer's own system keywords, such as


```
oa
erp
drc
bigdata

And some with Chinese characteristics... For example

ceshi // test
cs // Test
sc // production
```

So the vendor's final Big Data Test System domain name might look something like this

```
bigdata-test.example.com
bigdatatest.example.com
test-bigdata.example.com
uat-bigdata.example.com
sc.bigdata.example.com
ceshi.bigdata.example.com
```

Then we open our mind, if we can extract the keywords of each part, adopt

```
Direct splicing
Splicing the front and back of short slashes
Subdomain concatenation
```

**a variety of ways to arrange the combination of domain keywords and test live, whether the formation of a new attack surface discovery point?** 

So I initially implemented the idea in code and named it HiddenDamainHunter

![image-20230415134634275](https://s2.loli.net/2023/04/15/fdKgsmFPETX2M3I.png)



## Usage

 ```
 Directory structure
 -- HiddenDomainHunter.py // Main program
 └ ── domain.txt // Store a good collection of domain names
 └ ── domain_prefix.txt // program to extract the keywords in the existing domain name
 └ ── key.txt // custom keywords, such as admin,test, uat, dev such a class
 └ ── root_domain.txt // The root of the domain name to pop up is example.com
 └ ─ ─ subdomains. TXT / / the resulting subdomain list
 ```

Command line

```
pip3 install requests
python3 HiddenDomainHunter.py -f domain.txt -rd root_domain.txt
```

**Example** 

```
For example, you want to collect the deeply hidden assets of example.com and example2.com

Then you should write the subdomains of example1.com and example2.com that you have collected in domain.txt (via subdomain blasting, certificate transparency, google dork, various interfaces, etc.)

In root_domain.txt write example.com and example2.com

python3 HiddenDomainHunter.py -f domain.txt -rd root_domain.txt is fine
```



## Effect picture

![image-20230415134634275](https://s2.loli.net/2023/04/15/fdKgsmFPETX2M3I.png)

![image-20230415143415781](https://s2.loli.net/2023/04/15/NoFviXA4hwS12JE.png)



## Actual combat case

### ** Uses target domain features to mine around a new SRC

https://github.com/J0o1ey/BountyHunterInChina/blob/main/%E9%87%8D%E7%94%9F%E4%B9%8B%E6%88%91%E6%98%AF%E8%B5%8F%E9%87%91%E7%8C%8E%E4%BA%BA(%E5%8D%81%E5%9B%9B)-%E5%B7%A7%E7%94%A8%E7%9B%AE%E6%A0%87%E5%9F%9F%E5%90%8D%E7%89%B9%E7%82%B9%E6%8C%96%E6%8E%98%E6%9F%90%E6%96%B0%E4%B8%8ASRC%E5%9B%9B%E5%A4%84RCE.pdf