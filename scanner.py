#WEBSITE SCANNER 
# FIRST WE WILL USE 'import' TO BRING THE MODULE 'request' WHICH LETS PYTHON SEND  HTTP REQ
import requests
url = input('Enter the URL of the website: ')
response = requests.get(url)
#Python, send a GET request to the website stored in url
print(response.status_code)
#if the code comes as 200
print(response.headers) 
if"Strict-transport-security" in response.headers:
    print('HSTS is present')
else:
    print('_________HSTS is not present _________')
# we ask python if this header exists in the response header if yes print present else print not present

