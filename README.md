# awd-submit-flag

---
## 说明
该模块主要是用来ctf AWD比赛时批量提交flag时使用的

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
* start_ip 攻击开始ip
* end_ip 攻击结束ip
* skip_ip 跳过ip（有些比赛提交自己的flag会扣分）

#### script_function_module
* script_function 脚本功能(web & pwn & local)  
  |____ local:从本地的flag文件中获取flag提交(用于攻击脚本无法自动化的情况)  
  |____ web:从本地的url.txt中批量获取url，并访问获取flag  
  |____ pwn:根据ip与port，利用exp批量攻击获取flag

#### submit_module
* submit_addr 平台提交flag的地址（可以通过curl或urllib来进行提交，看比赛运维平台）
* token 队伍token
* success_request 判断提交的flag正确与否的字段(根据curl结果来确定)
* failed_request 判断提交的flag正确与否的字段(根据curl结果来确定)
* round_time 比赛每轮时间，单位秒

#### local_flag module
* flag_file 本地flag文件

#### web_flag symbol
* url_file web攻击url的文件
* flag_start 查找web访问response中的flag开头
* flag_end 查找web访问response中的flag结尾

#### pwn_flag module
* port 题目端口

---

## 备注
* 友情提醒，使用前最好`git pull`一下，代码会不定期更新。
* 当使用`web`模块时，一定要修改相应的`header`和`data`。
* 当使用`pwn`模块时，一定要修改相应的`exp`脚本。