import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint
import colorama

# initialize an HTTP session & set the browser
def sqliscanner(sqlilink):
    colorama.init()
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    BLUE = colorama.Fore.BLUE
    RESET = colorama.Fore.RESET
    YELLOW = colorama.Fore.MAGENTA 
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

    def get_all_forms(url):
        soup = bs(s.get(url).content, "html.parser")
        return soup.find_all("form")


    def form_details(form):
        details = {}

        try:
            action = form.attrs.get("action").lower()
        except:
            action = None

        method = form.attrs.get("method", "get").lower()
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

    def vulnerable_it_is(response):
        errors = {
            # MySQL
            "you have an error in your sql syntax;",
            "warning: mysql",
            # SQL Server
            "unclosed quotation mark after the character string",
            # Oracle
            "quoted string not properly terminated",
        }
        for error in errors:
            
            if error in response.content.decode().lower():
                return True
        
        return False

    def scan_sql_injection(url):
        # test on URL
        for c in "\"'":
            # add quote/double quote character to the URL
            new_url = f"{url}{c}"
            print("[!] Trying", new_url)
            # make the HTTP request
            res = s.get(new_url)
            if vulnerable_it_is(res):
                # SQL Injection detected on the URL itself, 
                # no need to preceed for extracting forms and submitting them
                print("[+] SQL Injection vulnerability detected, link:", new_url)
                return
        # test on HTML forms
        forms = get_all_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")
        for form in forms:
            form_details = form_details(form)
            for c in "\"'":
                # the data body we want to submit
                data = {}
                for input_tag in form_details["inputs"]:
                    if input_tag["type"] == "hidden" or input_tag["value"]:
                        
                        try:
                            data[input_tag["name"]] = input_tag["value"] + c
                        except:
                            pass
                    elif input_tag["type"] != "submit":
                        data[input_tag["name"]] = f"test{c}"
                # join the url with the action (form request URL)
                url = urljoin(url, form_details["action"])
                if form_details["method"] == "post":
                    res = s.post(url, data=data)
                elif form_details["method"] == "get":
                    res = s.get(url, params=data)
                # test whether the resulting page is vulnerable
                if vulnerable_it_is(res):
                    print(f"{GREEN}[+] SQL Injection vulnerability detected, link: {url}{RESET}")
                    print("[+] Form:")
                    pprint(form_details)
                    break

    
        
    url = sqlilink
    scan_sql_injection(url)