
from hardware import I2C
from hardware import Pin
from unit import ENVPROUnit
from app.network import connect_wifi




i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
envpro_0 = ENVPROUnit(i2c0)
time.timezone('GMT+1')
battery_label.setText(str(Power.getBatteryLevel()))
connect_wifi('private.kentra.org', 'kakekjeks', 'M5CardputerADV')
buf = ''
