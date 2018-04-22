import paramiko
import sys
import time
import getpass


ip_list = [	'10.10.10.1',
			'10.10.10.2',
			'10.10.10.3',
			'10.10.10.4'
		  ]

enable = "enable\n"
conf = "configure terminal\n"
termlength = "terminal length 0\n"
my_password = getpass.getpass()
my_username = "cisco"

def Session(ipaddr, name):
	remote_conn_pre = paramiko.SSHClient()  
	remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	remote_conn_pre.connect(ipaddr, username = my_username, password = my_password, 
							look_for_keys = False, allow_agent = False)
	print "SSH connection established to %s" % ipaddr
	remote_conn = remote_conn_pre.invoke_shell()
	print "Interactive SSH session established"
	old_hostname = remote_conn.recv(1000)[:-1].strip()
	print old_hostname
	remote_conn.send(termlength)
	remote_conn.send(enable)
	remote_conn.send(my_password + "\r")
	remote_conn.send(conf)
	time.sleep(1)	
	remote_conn.recv(10000)
	remote_conn.send('hostname {}\n'.format(name))
	time.sleep(1)
	new_hostname = remote_conn.recv(1000)[-9-len(name):-9]
	print new_hostname
	if old_hostname != new_hostname:
		print 'Hostname changed from {old} to {new}'.format(old = old_hostname,
															new = new_hostname)



for ip in ip_list:
	Session(ip, 'R' + str(ip_list.index(ip) + 1))

sys.exit("operation completed")


