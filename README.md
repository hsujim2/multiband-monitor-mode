# multiband-monitor-mode
cha_hop using iw and ifconfig, with signal Wi-Fi adapter and switching band quickly.<br>
multibandmon needs multiple Wi-Fi adapter, and perform in difference to capture multiple band.
# depedencies
> sudo apt install net-tools aircrack-ng python3

# usage
Use ifconfig to find net device's name, modify the net_dev name in python code.
> python3 multibandmon.py

or
> python3 cha_hop.py

Use ctrl+c can leave and will restore Wi-Fi adapter to managed mode.
> sudo wireshark

Go to interface, turn on monitor mode.<br>
Multibandmon needs to select all adapter before start capturing packet.
