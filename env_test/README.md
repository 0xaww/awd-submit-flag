# env_test

## 用途

用于赛前测试脚本的使用，防止在正式比赛中，因为断网而无法运行脚本。

## 使用方法

* 安装docker及docker-compose
* 在env_test文件夹中运行`docker-compose up -d`
* 没有docker-compose的话运行docker_run.sh
* 之后，在相应的网址及端口即可访问相对于的服务

## 服务

* 9999端口:
  |__ pwn题的端口
* 8888端口:
  |__ `http://127.0.0.1:8888/task_submit.html` web题的网址
  |__ `http://127.0.0.1:8888/flag_submit.html` flag测试提交的地址

上述pwn题、web题对应的exp在pwn_attack.py及web_attack.py中
