import paramiko
import sys
import time
import socket

enable = "enable"
disable = 'disable'
conf = "configure terminal"
shrun = "show run"
termlength = "terminal length 0"
username = "cisco"
password = "cisco"

filelist = open("/home/student/Desktop/PYTHON/Python-Scripts/MPLS3.txt")

class Session(object): 

	def SSHConnect(self, ip):
		self.ip = ip
		try:
			ssh_prep = paramiko.SSHClient()
			ssh_prep.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_prep.connect(self.ip, username=username, password=password, look_for_keys= False, allow_agent= False)
			conn = ssh_prep.invoke_shell()
		except socket.error:
			print "Cannot connect"
		else:
			print "SSH connection established to %s" % self.ip
			conn.send(termlength + "\r")
			time.sleep(1)
			output = conn.recv(1000)
			conn.send(enable + "\r")
			conn.send(password + "\r")
			conn.send(shrun + "\r")
			time.sleep(3)
			output = conn.recv(65534)
			return output
		
	def Postrun(self, filename, run_cfg):
		HOME = "/home/student/Desktop/PYTHON/TEST/Routers-2/%s" %(filename)
		f = open(HOME.strip(), "w")
		f.write(run_cfg)
		f.close()
   
  
ssh = Session()
runfiles = []
y = 1
while y < 5:
	print "\nGetting Running Config for R%s" % y
	running_config = ssh.SSHConnect("10.10.10.%s" % y)
	runfiles.append(running_config)
	y += 1
	
for i in zip(filelist, runfiles):
	ssh.Postrun(*i)
		
sys.exit("operation completed") 
