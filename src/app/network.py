import network
import time


def connect_wifi(ssid: str, password:str, hostname:str):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname=hostname)
    wlan.config(reconnects=3)
    print((str('Connecting wlan with  ') + str((wlan.config('mac')))))
    wlan.connect(ssid, password)
    while not (wlan.isconnected()):
        time.sleep(1)
        if wlan.isconnected():
            return
    print((str('IP Address: ') + str((wlan.ifconfig()[0]))))
    print((str('Subnet: ') + str((wlan.ifconfig()[1]))))
    print((str('Gateway: ') + str((wlan.ifconfig()[2]))))
    print((str('DNS: ') + str((wlan.ifconfig()[3]))))
    print((str('RX Power: ') + str((wlan.config('txpower')))))
