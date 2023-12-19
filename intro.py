import pyfiglet

# import portscanner
from security_headings import headercheck
from portscanner import port

print('''                                        
                 .:--:.                 
             .+#@@@@@@@@#+.             
            *@@@%+=--=+%@@@*            
          .%@@#:        :#@@%.          
          #@@#            **=.          
          @@@-                          
          @@@-                          
          @@@#________________   
     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     
     @@@@@@@@@@@@@@%%@@@@@@@@@@@@@@     
     @@@@@@@@@@@@=    =@@@@@@@@@@@@     
     @@@@@@@@@@@#      #@@@@@@@@@@@     
     @@@@@@@@@@@@=    =@@@@@@@@@@@@     
     @@@@@@@@@@@@@-  -@@@@@@@@@@@@@     
     @@@@@@@@@@@@@=..=@@@@@@@@@@@@@     
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
     =@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     
       :------------------------:       
                                        
''')
result = pyfiglet.figlet_format("WebGuardian")
print(result)
print("Scanning Vulnerabilities One at a time\n\n")
# print()
a = "http://testphp.vulnweb.com"
headercheck.headerchecker(a)
port.portscan(a)