import time
import random
log_path = 'xxx.log'
while 1:
    with open(log_path,'a') as f:
        f.write('[%s]   %s \n' % (time.ctime(),random.random()))
    time.sleep(1)