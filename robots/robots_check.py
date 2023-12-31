import subprocess

def curl_and_print(universal_link):
	
    try:
        url = universal_link+"/robots.txt"
        result = subprocess.run(['curl', url], capture_output=True, text=True, check=True)
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that may occur
        print(f"Error: {e}")
        print("Curl Error Output:")
        print(e.stderr)

