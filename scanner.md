# Web Security Scanner
- A small python project made by me using the knowledge of python and websecurity. 
- This scanner takes a websites URL sends a request and checks some basic security related data.

## Requirements
- Python 3
- `requests` library
Install `requests` with:
```bash
pip install requests
```

## How to Run
- open the project folder in vs code and run

- step 1 python scanner.py

- step 2 The program will ask:
  "Enter a website URL:" enter a URL you wanna check

 - step 3 run the program and then the code will start checking stuff and will return output as

    --- Security Scan ---
    Target: https://example.com
    Status Code: 200
     HSTS: Present
     X-Frame-Options: Missing
     CSP: Present




## What It Checks
- HSTS: 'Strict-Transport-Security' helps tell browsers to use HTTPS when connecting to a website.
- X-Frame-Options: Controls whether a webpage can be displayed inside a frame or iframe and can help reduce certain clickjacking risks.
-  Content-Security-Policy: CSP allows a website to define restrictions on the types and sources of content that browsers can load, helping reduce certain types      of attacks such as XSS.CSP allows a website to define restrictions on the types and sources of content that browsers can load, helping reduce certain types of     attacks such as XSS.
     (helped by AI for definations)
## Important
- This is a basic learning project, not a complete security scanner.
- Only test websites that you own or have permission to test. 

## Project Status
 - Still learning and improving this project.
 - More checks and features will be added as I learn more Python, networking, and web security.
## DATE 21-09-2026
