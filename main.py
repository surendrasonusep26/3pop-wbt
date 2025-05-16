import requests
from bs4 import BeautifulSoup
import subprocess
import platform 
import os
def webscraping(url):

    try:
        response = requests.get(url)
        response.raise_for_status()  # This raise exception on bad code

        soup = BeautifulSoup(response.content, 'html5lib')
        print(soup.prettify()) # It will print that web url into html format

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

def network_tools():

    target = input("Enter the target IP or hostname: ")

    # Using system executable ping to perform ping operation
    print("\n--- Ping ---")
    if platform.system().lower() == "windows":
        ping_command = ["ping", "-n", "4", target]  # We gave default value for count as 4
    else:
        ping_command = ["ping", "-c", "4", target]  # We gave default value for count as 4

    try:
        ping_result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        print(ping_result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ping failed: {e.stderr}")

def traceroute(nanu):

    print("\n--- Traceroute --- {Be patient!}")
    if platform.system().lower() == "windows":
        traceroute_command = ["tracert", nanu]
    else:
        traceroute_command = ["traceroute", nanu]

    try:
        traceroute_result = subprocess.run(traceroute_command, capture_output=True, text=True, check=True)
        print(traceroute_result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Traceroute failed: {e.stderr}")

if __name__ == "__main__":
    art=r"""

██████╗ ██████╗  ██████╗ ██████╗       ██╗    ██╗██████╗ ████████╗
╚════██╗██╔══██╗██╔═══██╗██╔══██╗      ██║    ██║██╔══██╗╚══██╔══╝
 █████╔╝██████╔╝██║   ██║██████╔╝█████╗██║ █╗ ██║██████╔╝   ██║   
 ╚═══██╗██╔═══╝ ██║   ██║██╔═══╝ ╚════╝██║███╗██║██╔══██╗   ██║   
██████╔╝██║     ╚██████╔╝██║           ╚███╔███╔╝██████╔╝   ██║   
╚═════╝ ╚═╝      ╚═════╝ ╚═╝            ╚══╝╚══╝ ╚═════╝    ╚═╝   
                                                                  
        •  ┏          •           ┓     •           ┓
        ┓┏┓╋┏┓┏┓┏┳┓┏┓╋┓┏┓┏┓  ┏┓┏┓╋┣┓┏┓┏┓┓┏┓┏┓  ╋┏┓┏┓┃
        ┗┛┗┛┗┛┛ ┛┗┗┗┻┗┗┗┛┛┗  ┗┫┗┻┗┛┗┗ ┛ ┗┛┗┗┫  ┗┗┛┗┛┗
                              ┛             ┛        
        Programmed By Surendra.S

Note : This program is intended to run on Windows ,Mac ,Linux/Unix based Operating systems.
1) Webscraping - Provide the complete url       (Ex: https://example.com)
2) Ping - Provide the correct ip/hostname       (Ex: 192.168.*.* or arkacybercrew@raspberrypi:192.168.1.1)
3) Traceroute - Provide the correct ip or url   (Ex: www.google.com or 8.8.8.8)

Modules required to run the code (requests,bs4,html5lib Install if Required : subprocess,platform)
!run the code again if error.

    """
    print(art)
    art2="""1: Webscraping"""
    print(art2)
    url = input("Enter the URL to scrape: ")
    webscraping(url)
    art3="""2: Ping Tool"""
    print(art3)
    network_tools()
    art4="""3: Traceroute Tool"""
    print(art4)
    nanu = input("Enter the Url/Ip/Hostname: ")
    traceroute(nanu)
    print("Thank you for using")
