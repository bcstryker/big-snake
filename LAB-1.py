#imports
import paramiko
import sys
import time
from getpass import getpass as gp

#declare and define vars
ipaddr ='10.10.10.2'
username = "cisco"
password = "cisco"
en = "enable\n"
conf = "configure terminal"
host = "hostname R2"
remote_conn_pre = paramiko.SSHClient()  
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ipaddr, username=username, password=password, 
						look_for_keys= False, allow_agent= False)
remote_conn = remote_conn_pre.invoke_shell()


#functions
def COMMONBEGIN():
    print "Interactive SSH session established"
    output = remote_conn.recv(1000)
    print output
    remote_conn.send("terminal length 0\n")
    remote_conn.send(en)
    remote_conn.send(gp('Enter password for 10.10.10.2: ') + '\n')
    remote_conn.send("conf t\r")
    time.sleep(2)

def COMMONEND():
    remote_conn.send("end\r")
    remote_conn.send("disable\r")
    remote_conn.close()

#execution
print "SSH connection established to 10.10.10.2"
COMMONBEGIN()
remote_conn.send("hostname {}\r".format('R2'))
print 'Operation Completed'
'''
COMMONEND()
sys.exit("operation completed")
'''
