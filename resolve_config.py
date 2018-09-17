import ConfigParser
def main():
    config=ConfigParser.ConfigParser()
    config.read("./config.conf")
    start_ip = config.get("config","start_ip")
    end_ip = config.get("config","end_ip")
    skip_ip = config.get("config","skip_ip")
    skip_ip = skip_ip.split(',')
    port = config.get("config","port")
    submit_addr = config.get("config","submit_addr")
    script_function = config.get("config","script_function")
    round_time = int(config.get("config","round_time"))
    url_file = config.get("config","url_file")
    url_file = open(url_file , "rw").read().splitlines()
    flag_file = config.get("config","flag_file")
    flag_file = open(flag_file , "rw").read().splitlines()
    token = config.get("config","token")
    success_request = config.get("config","success_request")
    failed_request = config.get("config","failed_request")
    flag_start = config.get("config","flag_start")
    flag_end = config.get("config", "flag_end")
    return start_ip,end_ip,skip_ip,port,submit_addr,script_function,url_file,flag_file,round_time,token,success_request,failed_request,flag_start,flag_end

if __name__ == '__main__':
    main()
