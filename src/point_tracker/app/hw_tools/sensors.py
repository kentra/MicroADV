from unit import ENVPROUnit
from hardware import I2C as i2c
from hardware import Pin


class I2C:
    def __init__(self, scl: int, sda: int, freq: int = 100000):
        self.i2c0 = i2c(0, scl=scl, sda=sda, freq=freq)

    def m5_env_pro(self):
        return ENVPROUnit(self.i2c0)
