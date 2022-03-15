#!/usr/bin/env python
import os,time
from threading import Timer

##########net device variables##########
net_seq = [2,3]
net_dev = ["wlp1s0","wlp4s0"]
net_band = [36,48]

###########main function###############
print("preparing...")
os.system("sudo airmon-ng check kill")
for i,j,k in zip(net_seq,net_dev,net_band):	
	os.system("sudo rfkill unblock {}".format(i))
	os.system("sudo airmon-ng start {} {}".format(j,k))
#print("restoring networking service to provide wired network")
#os.system("sudo service network-manager start")
print("start capture packet!")
try :
	while 1:
		print("capturing",end='',flush=True)
		for i in range(1,25):
			print(".",end='',flush=True)
			time.sleep(1)
		print()
except KeyboardInterrupt:
		print("\nctrl c detected, restore to managed mode!!")
		for i in net_dev:
			os.system("sudo airmon-ng stop {}mon".format(i))
		exit()
