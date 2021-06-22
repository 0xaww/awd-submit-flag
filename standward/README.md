# awd-submit-flag



## 依赖

* python2

* requests（pip安装即可）

* ConfigParser（pip安装即可）

* pwntools（pwn题依赖，pip安装即可）



## 说明

该项目主要是用来在AWD比赛中批量自动提交flag时使用的。



## 使用方法

配置好`config.conf`之后，根据脚本的功能，修改`pwn_attack.py` 或 `web_attack.py`或`flag.txt`，之后直接`python automatic.py`即可。

提前使用`env_test`环境来进行本地测试。

运行效果：

![image-20201019005944352](pic/1.png)

![2](pic/2.png)

## 文件调用
|文件名    |用途|
|:---   |:---   |
|config.conf    |配置文件，所有的参数配置|
|resolve_config.py  |解析config|
|pwn_attack.py    |调用pwn攻击获取flag|
|web_attack.py    |通过web访问获取flag|
|submit.py  |向平台提交flag|
|log.py |生成日志|
|automatic.py   |主要运行文件|



## config.conf 详解

#### ip module

* `ip_list` 所有靶机的ip列表（因为现在很多比赛的ip非常乱，所以自行生成列表使用比较稳妥，注意别加入自己的靶机地址）

#### script_function_module
* `script_function` 脚本功能(web & pwn & local)
  - `local`: 从本地的flag文件中读取flag提交(用于攻击脚本无法自动化的情况)
  - `web`: 根据url进行攻击，并访问获取flag
  - `pwn`: 根据ip与port，利用exp批量攻击获取flag


#### submit_module
* `submit_method` 可以通过curl或requests来进行提交，看比赛运维平台，详细在submit.py里修改
  - `curl`: 使用curl提交flag
  - `requests`: 使用requests模拟web访问提交flag

* `submit_addr` 平台提交flag的地址

* `token` 队伍token

* `success_request` 判断提交的flag正确的字段(需要根据手动提交的结果来确定，或根据官方文档来确定)

* `failed_request` 判断提交的flag错误或其他故障的字段(需要根据手动提交的结果来确定，或根据官方文档来确定)

* `round_time` 比赛每轮时间，单位秒

* `rounds` 比赛总轮次（可以不配置，意义不大）

* `submit_wait` 每次提交flag之间的停顿间隔（秒），部分平台会是提交间隔，没有就写0

#### local_flag module
* `flag_file` 本地`flag`列表文件保存的位置

#### web && PWN
* 到`web_attack.py`或`pwn_attack.py`中进行修改






## 单次运行

当需要单次运行或进行单次测试时，可以对各个模块独立进行单次测试：
`pwn`:`python pwn_attack.py 10.10.10.10` (测试ip是否能够拿到flag)
`web`:`python web_attack.py 10.10.10.10` (测试ip是否能够拿到flag)
`submit`:`python submit.py flag{123123}` (测试提交flag是否成功，需要在config.conf中先配置好submit地址等)





## 备注

* 最好提前使用`env_test`环境进行测试一下，熟悉一下使用方法。`env_test`的使用方法在`env_test/README.md`中
* 友情提醒，使用前`git pull`一下，代码会不定期更新。
* 当使用`web`模块时，一定要修改相应的`header`和`data`。
* 当使用`pwn`模块时，一定要修改相应的`exp`脚本。





## 后续计划

* 兼容`python2`及`python3`
* 将`config`配置集成到`web.py`里
* 对每个后台进程进行监控
* 生成图形化配置界面





## 更新说明：

`v1.2`

>完善了env_test测试环境，用于测试脚本的运行
>
>删除了原有的ip生成方式，改用了固定的ip列表，以应对复杂的ip环境
>
>抛弃了urllib2，改用requests
>
>submit新增了curl的提交方式
>
>优化了submit、web、pwn的脚本
>
>添加了单次测试的功能
>
>

`v1.1`

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

## 已完成计划

* 将urllib2替换成requests.post，增加cookies配置