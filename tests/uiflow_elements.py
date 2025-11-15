import os, sys, io
import M5
from M5 import *
import asyncio
from hardware import MatrixKeyboard
import network
from hardware import I2C
from hardware import Pin
from unit import ENVPROUnit
import time



line0 = None
rect0 = None
label0 = None
label1 = None
label2 = None
bar = None
battery_label = None
kb = None
wlan = None
i2c0 = None
envpro_0 = None


ssid = None
password = None
hostname = None
keyCode = None
key = None
buf = None

# Describe this function...
def connect_wifi(ssid, password, hostname):
  global keyCode, key, buf, line0, rect0, label0, label1, label2, bar, battery_label, kb, wlan, i2c0, envpro_0
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


def kb_pressed_event(kb_0):
  global line0, rect0, label0, label1, label2, bar, battery_label, kb, wlan, i2c0, envpro_0, keyCode, hostname, key, buf, ssid, password
  keyCode = kb.get_key()
  print(keyCode)
  if keyCode:
    if keyCode >= 0x20 and keyCode <= 0x7e:
      key = chr(keyCode)
      buf = (str(buf) + str(key))
      print(key)
      print(buf)
      print(keyCode)
    else:
      pass


async def main():
  global line0, rect0, label0, label1, label2, bar, battery_label, kb, wlan, i2c0, envpro_0, keyCode, hostname, key, buf, ssid, password

  M5.begin()
  Widgets.fillScreen(0x000000)
  line0 = Widgets.Line(0, 20, 240, 20, 0x4e523e)
  rect0 = Widgets.Rectangle(17, 31, 80, 80, 0x232323, 0x191919)
  label0 = Widgets.Label("MicroPython", 23, 62, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
  label1 = Widgets.Label("Cardputer", 29, 36, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
  label2 = Widgets.Label("UIFlow2", 34, 91, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
  bar = Widgets.Rectangle(0, 0, 240, 15, 0xffffff, 0xa4ff00)
  battery_label = Widgets.Label("%", 208, 4, 1.0, 0x000000, 0xafff00, Widgets.FONTS.DejaVu9)

  kb = MatrixKeyboard()
  kb.set_callback(kb_pressed_event)
  i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
  envpro_0 = ENVPROUnit(i2c0)
  time.timezone('GMT+1')
  battery_label.setText(str(Power.getBatteryLevel()))
  connect_wifi('private.kentra.org', 'kakekjeks', 'M5CardputerADV')
  buf = ''


  while True:
    await asyncio.sleep_ms(10)
    M5.update()
    kb.tick()
    print((str('Temperature: ') + str((envpro_0.get_temperature()))))
    print((str('Pressure: ') + str((envpro_0.get_pressure()))))
    print((str('Humidity: ') + str((envpro_0.get_humidity()))))
    print((str('Gas Res: ') + str((envpro_0.get_gas_resistance()))))
    time.sleep(1)
  

if __name__ == '__main__':
  try:
    asyncio.run(main())
  except (asyncio.CancelledError, KeyboardInterrupt) as e:
    from utility import print_error_msg
    print_error_msg(e)
  except ImportError:
    print("please update to latest firmware")
  finally:
    pass