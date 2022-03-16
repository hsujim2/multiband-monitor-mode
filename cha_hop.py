#!/usr/bin/env python
import os,time,threading,sys
from threading import Timer
print("preparing...")
wlan_name = "wlp2s0"
band = ["5180","5240"]
bandw = ["HT40+", "HT40-"]
os.system("sudo iw phy phy0 interface add mon0 type monitor")
os.system("sudo iw dev {} del".format(wlan_name))
os.system("sudo ifconfig mon0 up")
print("start capture packet!")
global conti
def channel_hopping():
	global conti
	while conti:
		for i,j in zip(band,bandw):
			os.system("sudo iw dev mon0 set freq {} {}".format(i,j))
			time.sleep(0.001)
		
conti = True
c = Timer(0.001,channel_hopping)

try :
	c.start()
	while 1:
		print("capturing",end='',flush=True)
		for i in range(1,25):
			print(".",end='',flush=True)
			time.sleep(1)
		print()
except KeyboardInterrupt:
	conti = False
	print("\nctrl c detected, restore to managed mode!!")
	os.system("sudo iw phy phy0 interface add {} type managed".format(wlan_name))
	os.system("sudo iw dev mon0 del")
	exit()


		
