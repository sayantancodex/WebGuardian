import pyfiglet
import sys
import socket
from datetime import datetime
from ftplib import FTP


# Defining a target
def portscan(universal_link):
	if "https://" in universal_link:
		universal_link = universal_link.replace("https://","")
	elif "http://" in universal_link:
		universal_link = universal_link.replace("http://","")
	if '/' in universal_link:
		universal_link = universal_link.replace('/','')
	target = socket.gethostbyname(universal_link)

	if '?' in universal_link:
		universal_link = universal_link.replace('?','')
	target = socket.gethostbyname(universal_link)

	if '=' in universal_link:
		universal_link = universal_link.replace('=','')
	target = socket.gethostbyname(universal_link) 
	# if len(sys.argv) == 2:
		
	# 	# translate hostname to IPv4
	# 	target = socket.gethostbyname(sys.argv[1]) 
	# else:
	# 	print("Invalid amount of Argument")

	# Add Banner 
	print("-" * 50)
	print("Scanning Target: " + target)
	print("-" * 50)
	#aserver_ports = [20,21,22,23,25,53,80,110,119,123,143,161,194,443]
	server_ports = {
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    23: "Telnet",
    3306: "MySQL",
    5432: "PostgreSQL",
    3389: "RDP",
    143: "IMAP",
    110: "POP3",
    389: "LDAP",
    8443: "HTTPS (Alternative)",
    123: "NTP",
    161: "SNMP",
    8080: "HTTP Proxy",
    8443: "HTTPS Proxy",
    27017: "MongoDB",
    1521: "Oracle Database",
	}


# Example of accessing a specific port

	a = list(server_ports.keys())

	try:
		
		# will scan ports between 1 to 65,535
		for port in range(len(a)):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)

			result = s.connect_ex((target,a[port]))
			# print(result)
			if result == 0:
				print(f"[+] Port {a[port]} {server_ports[a[port]]} is open")


			# s.close()
			

	except KeyboardInterrupt:
			print("\n Exiting Program !!!!")
			# sys.exit()
	except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
			# sys.exit()
	except socket.error:
			print("\n Server not responding !!!!")
			# sys.exit()

