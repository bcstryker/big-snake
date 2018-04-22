import paramiko
import sys
import time

my_username = "cisco"
my_password = "cisco"
ipaddr1 ='10.10.10.1'
ipaddr2 ='10.10.10.2'
ipaddr3 ='10.10.10.3'
ipaddr4 ='10.10.10.4'
enable = "enable"
conf = "configure terminal"

def Session(ip, hostname):
	print '---Attempting to connect to', ip
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ip, username = my_username, password = my_password, 
							look_for_keys = False, allow_agent = False)
	remote_conn = remote_conn_pre.invoke_shell()
	print '---Connection established'
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(1)	
	print '---Attempting to change hostname to', hostname
	remote_conn.send("hostname {}\r".format(hostname))
	remote_conn.close()
	print '~'*50
	
Session(ipaddr1, 'R1')	
Session(ipaddr2, 'R2')	
Session(ipaddr3, 'R3')	
Session(ipaddr4, 'R4')	

	
'''
def Session2():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr2, username=username, password=password, look_for_keys= False, allow_agent= False)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R2\r")
	remote_conn.close()

def Session3():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr3, username=username, password=password, look_for_keys= False, allow_agent= False)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R3\r")
	remote_conn.close()

def Session4():
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr4, username=username, password=password, look_for_keys= False, allow_agent= False)
	remote_conn = remote_conn_pre.invoke_shell()
	remote_conn.send("terminal length 0\n")
	remote_conn.send("enable\r")
	remote_conn.send("cisco\r")
	remote_conn.send("conf t\r")
	time.sleep(2)
	remote_conn.send("hostname R4\r")
	remote_conn.close()

print "Connecting to TEST1"
Session1()
print "Connecting to TEST2"
Session2()
print "Connecting to TEST3"
Session3()
print "Connecting to TEST4"
Session4()

sys.exit("operation completed")

'''
