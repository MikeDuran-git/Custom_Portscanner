import socket # procures communication using TCP and UDP

#base function to scan
def scan_port(ipadress, port):
	try:
		sock = socket.socket()
		sock.connect((ipadress,port))
		print("[+] Port Open: "+ str(port))
		sock.close()
	except:
		pass

#check port for a single target
def scan(target, ports):
	print("\nStart of Scan for "+ str(target))
	for port in range(1,ports):
		scan_port(target, port)


#main
targets= input("[*] Enter Targets To Scan (split them by ','): ")
ports= int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
	print("[*] Scanning multiple Targets")
	for ipaddr in targets.split(','):
		scan(ipaddr.strip(' '), ports)
		print("Scanning of "+ str(ipaddr)+ " done")
else:
	scan(targets,ports)
