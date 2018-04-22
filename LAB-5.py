import paramiko
import sys
import time

enable = "enable"
conf = "configure terminal"
shrun = "show run"
termlength = "terminal length 0"
username = "cisco"
password = "cisco" 

filenames = open("/home/student/Desktop/PYTHON/TEST/FILES.txt")

class Session(object):  
	def Getrun(self, ip):
		self.ip = ip
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(self.ip, username=username, password=password, look_for_keys= False, allow_agent= False)
		print "SSH connection established to %s" % self.ip
		remote_conn = remote_conn_pre.invoke_shell()
		remote_conn.send(termlength + "\r")
		remote_conn.send(enable + "\r")
		remote_conn.send(password + "\r")
		time.sleep(1)
		remote_conn.recv(10000)
		remote_conn.send(shrun + "\r")
		time.sleep(.5)
		run_cfg = ''
		while not run_cfg.endswith('#'):
			run_cfg += remote_conn.recv(100)
		return run_cfg
		
	def Postrun(self, filename, run_cfg):
		path = "/home/student/Desktop/PYTHON/TEST/Routers/%s" %(filename)
		f = open(path.strip(), "w")
		f.write(run_cfg)
		f.close()

ips = {1:"10.10.10.1", 2:"10.10.10.2", 3:"10.10.10.3", 4:"10.10.10.4"}
                
ssh = Session()

running_configs = []
for ip in ips:
	running_configs.append(ssh.Getrun(ips[ip]))

for i in zip(filenames, running_configs):
        ssh.Postrun(*i)

sys.exit("operation completed")
