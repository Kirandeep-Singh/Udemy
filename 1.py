'''
import subprocess

cmd = ('sh p1.sh','sh p2.sh','sh p3.sh')
processes = []
print (subprocess.Popen(['pwd']))
for i in cmd:
    process = subprocess.Popen(i, shell=True)
    processes.append(process)

print (processes[0])
print (processes[1])
print (processes[2])

output = [p.wait() for p in processes]

'''

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('10.184.44.61',22,'root','Automation@1234')
    k = ssh.exec_command('ls -lrth /opt/temp')
    print(k[1].read())
except paramiko.AuthenticationException:
    print ("Incorrect password Has been Supplied")


import math
