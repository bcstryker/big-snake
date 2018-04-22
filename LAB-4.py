import paramiko
import sys
import time

ip = "10.10.10.1"
enable = "enable"
conf = "configure terminal"
host = "hostname R1"
shrun = "show run"
termlength = "terminal length 0"
abs_path = "/home/student/Desktop/PYTHON/TEST/tst.txt"
username = "cisco"
password1 = raw_input("Please provide the password to connect:\t")
password = "cisco"

class REPLACE():
	
	def __init__(self, ipaddr):
		self.ipaddr = ipaddr
		#maybe remote_conn_pre and remote_conn should be defined as self.vars
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(self.ipaddr, username = username, password = password1, 
								look_for_keys= False, allow_agent= False)
		print "SSH connection established to %s" % self.ipaddr
		remote_conn = remote_conn_pre.invoke_shell()
		remote_conn.send(termlength + "\r")
		remote_conn.send(enable + "\r")
		remote_conn.send(password + "\r")
		time.sleep(1)
		remote_conn.recv(1000)
		remote_conn.send(shrun + "\r")
		time.sleep(2)
		self.output = remote_conn.recv(100000)
	
	def Replace_IP(self):
		f = open(abs_path, "w")
		f.write(self.output.replace("192.168.12.1" , "10.10.100.1"))
		f.close()
    
change = REPLACE(sys.argv[1]) 
change.Replace_IP()
sys.exit("operation completed")
