from ftplib import FTP
# import 
import socket

def ftpscan(universal_link):
	print("Testing FTP")
	target = socket.gethostbyname(universal_link)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
			
			# returns an error indicator
	result = s.connect_ex((target,21))
	if result == 0:
		try:
			ftp = FTP(target)
			a = ftp.login()
			if '230' in a:
				print("Anonymous Login Available")
			else:
				pass
		except:
			print("Exception occured")
	else:
		print("FTP port did not respond or is not active")

universal_link = 'www.google.com'
ftpscan(universal_link)
