import paramiko
import time
import re

class CISCO():
	
	def __init__(self, ip, usr, pw, privileged = False):
		self.remote_conn_pre = paramiko.SSHClient()  
		self.remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.remote_conn_pre.connect(ip, username = usr, password = pw, look_for_keys = False, allow_agent = False)
		self.remote_conn = self.remote_conn_pre.invoke_shell()
		self.remote_conn.send('term len 0\n')
		self.remote_conn.send('en\n')
		self.remote_conn.send('cisco\n')
		if privileged:
			self.remote_conn.send('conf t\n')
			time.sleep(1)
		else:
			time.sleep(.5)
		self.remote_conn.recv(1000)

	def get_version_string(self):
		self.remote_conn.send('show version\n')
		time.sleep(3)
		version = self.remote_conn.recv(10000)
		return version
	
	def get_config_register(self, version):
		re_conf_reg = re.search(r'Configuration register is (.*)', version)
		return re_conf_reg.group(1)
		
	def get_inventory_string(self):
		self.remote_conn.send('show inventory\n')
		time.sleep(3)
		inventory = self.remote_conn.recv(10000)
		return inventory
		
	def get_serial_of_chassis(self, inventory):
		re_serial = re.search(r'Chassis.*\n.*SN: (\d+)', inventory)
		return re_serial.group(1)
						
	def get_log_string(self):
		self.remote_conn.send('sh log\n')
		time.sleep(3)
		log = self.remote_conn.recv(10000)
		return log
		
	def get_deny_entries(self, log):
		denies = re.findall(r'.*denied.*', log)
		x = len(denies)
		prompt = 'There is/are {} deny entries. Would you like to see?: (y/n):'
		if x > 0:
			resp = raw_input(prompt.format(x))
			if resp.lower() == 'y':
				for deny in denies:
					print deny
		else:
			print 'There are no deny entries'
	
	def Get_IP_Int_Brief(self):
		self.remote_conn.send('sh ip int brief\n')
		time.sleep(3)
		self.ip_int_br = self.remote_conn.recv(10000)
		return self.ip_int_br
		
		
R1 = CISCO('10.10.10.1', 'cisco', 'cisco')

print R1.get_config_register(R1.get_version_string())
print R1.get_serial_of_chassis(R1.get_inventory_string())
R1.get_deny_entries(R1.get_log_string())
