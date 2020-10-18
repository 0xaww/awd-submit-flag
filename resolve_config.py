import ConfigParser

class submits:
    def __init__(self,name):
        self.name= __name__

class configs:
    def __init__(self,name):
        self.name= __name__
        self.submit = submits("")

def main():
    con = configs("config")
    config=ConfigParser.ConfigParser()
    config.read("./config.conf")
    con.ip_list = config.get("config","ip_list").split(",")


    con.script_function = config.get("config","script_function")
    con.round_time = int(config.get("config","round_time"))
    con.rounds = int(config.get("config","rounds"))
    con.submit_wait = int(config.get("config","submit_wait"))


    flag_file = config.get("config","flag_file")
    con.flag_list = open(flag_file , "r").read().splitlines()


    #con.submit
    con.submit.submit_method = config.get("config","submit_method")
    con.submit.submit_addr = config.get("config","submit_addr")
    con.submit.token = config.get("config","token")
    con.submit.success_request = config.get("config","success_request")
    con.submit.failed_request = config.get("config","failed_request")

    return con

if __name__ == '__main__':
    main()
