import os, sys, io
import M5
# from M5 import *
from M5 import Widgets
import asyncio
import network
import time



async def GUI():
    M5.begin()
    Widgets.fillScreen(0x000000)
    line0 = Widgets.Line(0, 20, 240, 20, 0x4e523e)
    rect0 = Widgets.Rectangle(17, 31, 80, 80, 0x232323, 0x191919)
    label0 = Widgets.Label("MicroPython", 23, 62, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
    label1 = Widgets.Label("Cardputer", 29, 36, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
    label2 = Widgets.Label("UIFlow2", 34, 91, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu9)
    bar = Widgets.Rectangle(0, 0, 240, 15, 0xffffff, 0xa4ff00)
    battery_label = Widgets.Label("%", 208, 4, 1.0, 0x000000, 0xafff00, Widgets.FONTS.DejaVu9)

