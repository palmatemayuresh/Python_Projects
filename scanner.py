#WEBSITE SCANNER 
# FIRST WE WILL USE 'import' TO BRING THE MODULE 'request' WHICH LETS PYTHON SEND  HTTP REQ
import requests
url = input('Enter the URL of the website: ')
response = requests.get(url)
print("\n--- Security Scan ---")
print("Target:", url)
#Python, send a GET request to the website stored in url
print("Status Code:", response.status_code)
#if the code comes as 200 it means its executed succsessfully
if"Strict-transport-security" in response.headers:
    print('HSTS is present')
else:
    print('HSTS is not present')
# we ask python if this header exists in the response header if yes print present else print not present
if "X-Frame-Options" in response.headers:
    print("X-Frame-Options: Present")
else:
    print("X-Frame-Options: NOT Present")
# WE again ask python if the above header is there
if "Content-Security-Policy" in response.headers:
    print("Content-Security-Policy: Present")
else:
    print("Content-Security-Policy: NOT Present")
