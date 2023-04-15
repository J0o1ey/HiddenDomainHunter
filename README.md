## HiddenDomainHunter

English Docuemnt:

https://github.com/J0o1ey/HiddenDomainHunter/blob/main/README_EN.md

### 设计思想

在攻击面发掘与漏洞挖掘的过程中，我们遇到的一些大型目标往往在**域名命名**中呈现出某种规律

让我们感觉到似乎有迹可循

比如很多厂商用各种关键词来表示该域名在业务中的性质，比如：

```
测试环境：
uat
test

开发环境：
dev

api系统:
api

网关:
gataway

上线前环境：
pre
pro

...
```

还有厂商很多自有系统的关键词，诸如

```
oa
erp
drc
bigdata

还有一些有中国特色的...比如

ceshi  //测试
cs    //测试
sc		//生产
```

所以厂商最终的"大数据测试系统"域名可能是这样的

```
bigdata-test.example.com
bigdatatest.example.com
test-bigdata.example.com
uat-bigdata.example.com
sc.bigdata.example.com
ceshi.bigdata.example.com
....
```

那么我们思维打开，如果可以将各部分关键词提取出来，采用

```
直接拼接
短斜线前后拼接
子域名拼接
```

**多种方式排列组合域名关键词并测活，是否就形成了一个新的攻击面发现点呢？**

于是我初步将想法用代码实现了出来，命名为HiddenDamainHunter

![image-20230415134634275](https://s2.loli.net/2023/04/15/fdKgsmFPETX2M3I.png)



## 用法

```
目录结构
── HiddenDomainHunter.py  //主程序
├── domain.txt  //存放已收集好的域名
├── domain_prefix.txt  //程序提取的已有域名中的关键词
├── key.txt  //自定义的关键词，诸如admin,test，uat，dev这类
├── root_domain.txt  //最终要爆破域名的根域名example.com
└── subdomains.txt  //最终生成的子域列表
```

命令行

```
pip3 install requests
python3 HiddenDomainHunter.py -f domain.txt -rd root_domain.txt
```



**举个栗子**

```
比如您要收集example.com和example2.com的深度隐藏资产

那么您应该在domain.txt中写入您已经收集好的example1.com和example2.com的子域(通过子域爆破，证书透明，google dork，各大接口等)

在root_domain.txt中写入example.com和example2.com

然后python3 HiddenDomainHunter.py -f domain.txt -rd root_domain.txt就可以啦
```



## 效果图

![image-20230415134634275](https://s2.loli.net/2023/04/15/fdKgsmFPETX2M3I.png)

![image-20230415143415781](https://s2.loli.net/2023/04/15/NoFviXA4hwS12JE.png)



## 实战案例

### **巧用目标域名特点挖掘某新上SRC四处RCE.pdf**

https://github.com/J0o1ey/BountyHunterInChina/blob/main/%E9%87%8D%E7%94%9F%E4%B9%8B%E6%88%91%E6%98%AF%E8%B5%8F%E9%87%91%E7%8C%8E%E4%BA%BA(%E5%8D%81%E5%9B%9B)-%E5%B7%A7%E7%94%A8%E7%9B%AE%E6%A0%87%E5%9F%9F%E5%90%8D%E7%89%B9%E7%82%B9%E6%8C%96%E6%8E%98%E6%9F%90%E6%96%B0%E4%B8%8ASRC%E5%9B%9B%E5%A4%84RCE.pdf
