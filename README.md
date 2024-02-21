# Auth Bypass in ConnectWise ScreenConnect

Exploit for bypassing authentication in ConnectWise ScreenConnect.

![Screenshot 2024-02-21 at 14 36 12](https://github.com/jhonnybonny/auth_bypass_connectwise_screenconnect/assets/87495218/e4ddc4da-8e41-4d26-ad51-1df73d9ab726)

## Usage
```bash
python3 bypass.py --url http://IP --username USER --password PASS
```

## Request for search engines
```
- FOFA: "ScreenConnect" && country="RU" 
- HHOW: web.body="ScreenConnect" and ip.country=="Russia"
- Shodan: ScreenConnect country:"RU"
```

## Requirements
- Python 3
- `requests`
- `re`
- `argparse`
- `colorama`

## Description
This script automates the process of bypassing authentication in ConnectWise ScreenConnect by exploiting a vulnerability. It allows the addition of a new user without proper authentication.

## Script Execution
The script takes three command-line arguments:
- `--url`: Target URL in the format http://IP.
- `--username`: Username to add.
- `--password`: Password to add (must be at least 8 characters in length).

After executing the script, it sends requests to the target URL to exploit the vulnerability and adds the specified username and password as a new user.

