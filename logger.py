import datetime

class logger():
    def __init__(self,n):
        self.n = n

    def log1(self, info):
        self.info = info
        #print ("entered log1")
        now = datetime.datetime.now()
        with open(self.n, 'a') as logfile:
            logfile.writelines('\n')
            logfile.writelines(str(now) + '\t' + self.info)

def log(info,n):
    return logger(n).log1(info)