# awd-submit-flag

---

## 调用
config.conf 配置文件，所有的参数配置
exp.py 攻击脚本
exploit.py 批量攻击
resolve_config.py 解析config
log.py 生成日志
submit.py 向平台提交flag（具体要看平台的提交方式）
web_flag.py 通过web访问获取flag
local_flag.py 通过本地文件获取flag
target.py 获取所有ip段
automatic.py 主要运行文件

---

## 使用方法
配置好config.conf之后，直接python automatic.py即可。

---

## 备注

当使用web模块时，一定要修改相应的header和data。
