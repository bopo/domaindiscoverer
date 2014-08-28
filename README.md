# README #

基于中文拼音的域名 Whois 查询工具

输入从互联网或输入法内获得的中文词频词库，按词频扫描 .COM/.CN 域名是否存在。

如词库内包含［上海］一词，会记录 SHANGHAI.COM、SHANGHAI.CN 注册状态及有效期。

### 特性 ###

* 基于 Python 2.7 开发, 数据存入 SQLite3
* 默认可查询 .COM、.CN 域名是否存在
* 记录已注册域名的有效期

### 如何使用?

* 建立 data.sqlite 数据库, 表结构见 pinyin_domains.txt
* 默认已包含 sougouDic.txt，执行 init_sogou_dic.py 写入默认数据库
* 执行 domain_discoverer.py 开始扫描, 记录会源源不断写入 SQLite

### 等待你参与的特性...

* 多线程查询以获得更快的扫描速度
* 改善 Whois 服务器地址, 以提升查询成功率
* 阿拉伯数字域名的扫描

### 参考资料 ###

参考词库: 

* http://www.sogou.com/labs/dl/w.html

参考资源:

* https://packages.debian.org/wheezy/whois
* https://github.com/joepie91/python-whois
* https://sqlite.org/docs.html
* https://github.com/OldhamMade/pywhois
* https://github.com/lxneng/xpinyin
* https://wiki.python.org/moin/SQLite
* http://www.opensource.apple.com/source/adv_cmds/adv_cmds-138.1/whois/whois.c