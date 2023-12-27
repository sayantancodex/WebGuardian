from ftplib import FTP
import socket

def ftpscan(universal_link):
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
	print("Testing FTP")
	target = socket.gethostbyname(universal_link)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
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

# universal_link = 'www.google.com'
# ftpscan(universal_link)
