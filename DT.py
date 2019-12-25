import re

f = open("Network.txt" , "r+")

kd = '<access address="10.184.41.245" connection="SSH" name="ogw" password="Ericsson@123456" username="ogw"/>'

kd1 = re.match(r"(.*)ogw(.*)", kd, re.M|re.I)

print(kd1.group().split('"')[1],)




for kd in f:
    if re.match(r"(.*)username(.*)", kd) is not None:
        #print(kd)
        if re.match(r"(.*)sysadmin(.*)", kd) is not None:
            #print(kd.split('"'))
            ip = kd.split('"')[1]
            pswd = kd.split('"')[7]
            user = kd.split('"')[9]
            print (ip, user, pswd)
