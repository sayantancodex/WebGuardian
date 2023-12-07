import requests
import colorama
import time

def headerchecker(link):
    colorama.init()
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    RESET = colorama.Fore.RESET
    YELLOW = colorama.Fore.YELLOW
    try:
        r = requests.get(link).headers
        vuln = list(r)
        
        try:
            ser = r.get('Server')
            if ser != None:
                print(f"{GREEN}[+] SERVER: {ser}{RESET}")
            else:
                print(f"{YELLOW}[X] Could not detect server!{RESET}")
            
            time.sleep(1)
        except:
            pass
        security_score = 0
        if "Strict-Transport-Security" not in vuln:
            print(f"{RED}[!] Missing Strict-Transport-Security {RESET}")
            security_score +=1
            time.sleep(1)

        if "Content-Security-Policy" not in vuln:
            print(f"{RED}[!] Missing Content-Security-Policy{RESET}")
            security_score +=1
            time.sleep(1)

        if "X-Frame-Options" not in vuln:
            print(f"{RED}[!] Missing X-Frame-Options{RESET}")
            security_score +=1
            time.sleep(1)

        if "X-Content-Type-Options" not in vuln:
            print(f"{RED}[!] Missing X-Content-Type-Options {RESET}")
            security_score +=1
            time.sleep(1)

        if "Referrer-Policy" not in vuln:
            print(f"{RED}[!] Missing Referrer-Policy{RESET}")
            security_score +=1
            time.sleep(1)

        if "Permissions-Policy" not in vuln:
            print(f"{RED}[!] Missing Permissions-Policy{RESET}")
            security_score +=1
            time.sleep(1)

        if "X-XSS-Protection" not in vuln:
            print(f"{RED}[!] Missing X-XSS-Protection{RESET}")
            security_score +=1
            time.sleep(1)
            
        # print(security_score)
        if security_score > 5:
            print(f"{YELLOW}[*] Likely Vulnerable and outdated Site{RESET}")
    except Exception as e:
        print(e)



link = "http://testphp.vulnweb.com"
headerchecker(link)