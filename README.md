# awd-submit-flag

---
## 依赖

* urllib2

* requests

* pwntools(pwn题)


## 说明

该模块主要是用来ctf AWD比赛时批量自动提交flag时使用的

---



## 使用方法

配置好`config.conf`之后，直接`python automatic.py`即可。

---

## 文件调用
|文件名    |用途|
|:---   |:---   |
|config.conf    |配置文件，所有的参数配置|
|resolve_config.py  |解析config|
|pwn_flag.py    |调用pwn攻击获取flag|
|web_flag.py    |通过web访问获取flag|
|local_flag.py  |通过本地文件批量提交flag|
|target.py  |获取所有ip段|
|submit.py  |向平台提交flag（具体要看平台的提交方式）|
|log.py |生成日志|
|automatic.py   |主要运行文件|


## config.conf 详解

#### ip module

* ip_mode ip具体网段

* start_ip 攻击开始ip
* end_ip 攻击结束ip
* skip_ip 跳过ip（有些比赛提交自己的flag会扣分）

#### script_function_module
* script_function 脚本功能(web & pwn & local)  
  |___ local:从本地的flag文件中获取flag提交(用于攻击脚本无法自动化的情况)  
  |___ web:根据url进行攻击，并访问获取flag  
  |___ pwn:根据ip与port，利用exp批量攻击获取flag

#### submit_module
* submit_addr 平台提交flag的地址（可以通过curl或urllib来进行提交，看比赛运维平台，详细在submit.py里修改）
* token 队伍token
* success_request 判断提交的flag正确与否的字段(根据curl结果来确定)
* failed_request 判断提交的flag正确与否的字段(根据curl结果来确定)
* round_time 比赛每轮时间，单位秒

#### local_flag module
* flag_file 本地flag文件

#### web_flag symbol
* url web攻击的url，ip用%s来替代
* flag_start 查找web访问response中的flag开头
* flag_end 查找web访问response中的flag结尾

#### pwn_flag module
* port 题目端口

---

## 备注
* 友情提醒，使用前最好`git pull`一下，代码会不定期更新。
* 当使用`web`模块时，一定要修改相应的`header`和`data`。
* 当使用`pwn`模块时，一定要修改相应的`exp`脚本。

---

## 后续计划

* 将urllib2替换成requests.post，增加cookies配置
* 将config配置集成到web.py里
* 对每个后台进程进行监控

---

## 更新说明：

>v1.1
>
>
>* 修改了target ip的生成方式，来适应不同的网段；
>
>  ip_mode:"172.19.%d.30"
>  start_ip:1
>  end_ip:8
>  skip_ip:3,5
>
>  ==>['172.19.1.30', '172.19.2.30', '172.19.4.30', '172.19.6.30', '172.19.7.30', '172.19.8.30']
>
>  ip_mode:"172.19.30.%d"
>  start_ip:1
>  end_ip:8
>  skip_ip:3,5
>
>  ==>['172.19.30.1', '172.19.30.2', '172.19.30.4', '172.19.30.6', '172.19.30.7', '172.19.30.8']
>
>* 将web_flag.py的url调用进行了优化，不再采用url.txt