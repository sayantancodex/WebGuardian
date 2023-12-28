import pyfiglet
import colorama
from security_headings import headercheck
from portscanner import port
from ftp import ftp
from adminpanel import adminpanel
from xss import xss_sc
from sqli import sqli

colorama.init()
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.MAGENTA

print('''                                                                                    
              .-=*#%%%%+..:---.                                
           :+%@@@@@@@@@@@@@@@@@#:                              
         -%@@@@@@@@@@@@@@*#**#*@@=                             
      .+@@%*+*@@@@@@@@@@@=@@@@=@@@-                            
     :+=:.-#@@@@@@@%#%@@@=@@@@=@@@#                            
      :+#@@@@@@@@#:   -@@*#%%*#@@@*                            
    +@@@@@@@@@#==*%#*%.#@@@@@@@@@-.                            
  .%@@@@@%*=::+@@@@@##*-%%%###**+.                             
 .@@@#*=.:==*%%%%%%%#****+******#=                             
 %@%: .+%@%@@%%%%%@%@@@@@@@@@@@@@*                             
-@@..#@%*#@@@@@@@@@@@@@@@@@%*+-%@%                             
:#: -@@#   :+@@@@@@@@@@@%=.   .@@@                             
    =@@@*.   .+@@@@@@@@=    .=@@@@                             
    :@@@@@%+-..=@@@@@@+.:-+%@@@@@+                             
     -#@@@@@@@@@@@-.%@@@@@@@@@%=.                              
       .+#@@@@@@@+..:@@@@@@@**=                                
       .@@=@@@@@@@@%@@@@@@@*%@*                                
       .@@#*%@@@@@@@@@@@@@+#@@:                                
        -@@@=+=-==-++-=-:-*@%:                                 
         .@@*+-----=+--=+:%@.                                  
          #@@@@@@@@@@@@@@@@@.                                  
         .%@@@@@@@@@@@@@@@@*.                                  
           ***++==------=++                                    
''')
print(RESET)

result = pyfiglet.figlet_format("WebGuardian")
print(f"{result}")
print(f"{GREEN}Scanning Vulnerabilities One at a time{RESET}")
print(f"{YELLOW}BROUGHT TO YOU BY 📷 @the_eager_wolverine\n\n{RESET}")
# print()
universal_link = input("Enter URL: ")
if universal_link[-1] == '/':
    universal_link = universal_link[0:len(universal_link)-1]
    print(universal_link)
print(f"\n{GREEN}[*]CHECKING WEBSITE SECURITY HEADERS{RESET}\n")
headercheck.headerchecker(universal_link)
print(f"\n{GREEN}[*]CHECKING OPEN PORTS{RESET}\n")
port.portscan(universal_link)
print(f"\n{GREEN}[*]CHECKING FOR VULNERABLE FTP ACCESS{RESET}\n")
ftp.ftpscan(universal_link)
print(f"\n{GREEN}[*]CHECKING FOR ADMIN PANELS. this might take few minutes...{RESET}\n")
adminpanel.adminpanelscanner(universal_link)
print(f"\n{GREEN}[*]CHECKING FOR CROSS SITE SCRIPTING VULNERABILITY{RESET}\n")
xss_sc.xss_scan(universal_link)
sqlchoice = input("\nDo you want to check for SQL injection vulnerability? (Y/N): ")

if sqlchoice == "Y" or sqlchoice == "y":
    sqlilink = input("Enter the full link to scan for SQL injection with php ids: ")
    sqli.sqliscanner(sqlilink)
elif sqlchoice == "N" or sqlchoice == "n":
    pass
else:
    pass
