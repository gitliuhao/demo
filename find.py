import subprocess
import time

r_log = "xxx.log"


def find_log_list():
    cmd = "ls -a {log_path}".format(log_path='/home/vagrant/demo')
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line = popen.stdout.readlines()
    if line:
        log_list = [i.decode().replace('\n', '') for i in line if '.log' in i.decode()]
        return log_list
    return []


print(find_log_list()
)