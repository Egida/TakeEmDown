# Knock Em 2.0

     /$$   /$$                     /$$             /$$$$$$$$              
    | $$$ | $$                    | $$            | $$_____/              
    | $$$$| $$  /$$$$$$   /$$$$$$$| $$   /$$      | $$       /$$$$$$/$$$$ 
    | $$ $$ $$ /$$__  $$ /$$_____/| $$  /$$/      | $$$$$   | $$_  $$_  $$
    | $$  $$$$| $$  \ $$| $$      | $$$$$$/       | $$__/   | $$ \ $$ \ $$
    | $$\  $$$| $$  | $$| $$      | $$_  $$       | $$      | $$ | $$ | $$
    | $$ \  $$|  $$$$$$/|  $$$$$$$| $$ \  $$      | $$$$$$$$| $$ | $$ | $$
    |__/  \__/ \______/  \_______/|__/  \__/      |________/|__/ |__/ |__/
    ______________________________________________________________________

    #################### Predator or pray, predator or pray
    # BossFight 2017   # Nock em out
    # Sweden           # Nock em out
    #################### Predator or pray, predator or pray
    
    
    Music: https://www.youtube.com/watch?v=F0PUVKfxkTM


requirements:


python3, and the following moduels, cloudscraper, random, sys, webbrowser, and scapy.



Usage:


sudo python3 DDoS.py URL/IP/WIFINAME Networks-to-make (for ssid spam)



Ex:


sudo python3 DDoS.py https://www.target.com 1

sudo python3 DDoS.py 1.1.1.1 4

sudo python3 DDoS.py wifiname 9 100



Methods:


Nginx (experimental), uses keep alive and agent user spoof to bypass nginx. (may not work)
 
Cloudfare, uses cloudscraper to send packets to cloudfare protected websites.
 
GET, kinda fast, could stop a normal website really fast.
 
TCP, uses syn attack, kinda powerfull. 
 
NTP, sends packets to a website/ip using there own server (a ntp packet).
 
UDP, sends UDP packets, really fast, kinda laggy. 
 
DNS (memcached packet), sends packets to a website/ip using there own server, it shows as dns but has memcached payload in it. 
 
ICMP, just your good old ping of death.
 
OVH/NFO bypass, same as TCP, has a payload in it, could be more effective sometimes. 
 
SSID spam, spams ssid names, could crash anything that scans for wifi networks if enough are made. Does NOT need a usb plugin thing (unlike most ssid spammers).
 
Website checker, checks if a website is online.
