## Tools

```

    "adafruit-ampy>=1.1.0",
    "esptool>=5.1.0",
    "micropy-cli>=3.6.0",
    "mpremote>=1.26.1",
    "mpy-cross>=1.26.1.post2",
    "pyright>=1.1.407",
    "rshell>=0.0.36",
    "setuptools>=80.9.0",
    "ty>=0.0.1a25",

```


## Included Resources





**Checkout local copy here:**
- [Cardputer ADV](/Users/daniko/Documents/Code/MCU/Micropython/MicroADV/tests/uiflow-micropython/m5stack/fs/system/cardputeradv)
- [Common](/Users/daniko/Documents/Code/MCU/Micropython/MicroADV/tests/uiflow-micropython/m5stack/fs/system/common)

### Cardputer ADV specific

```
Path /system/cardputeradv

├── applist.jpeg
├── apprun
│   ├── run_always_select.jpeg
│   ├── run_always_unselect.jpeg
│   ├── run_info.jpeg
│   ├── run_once_select.jpeg
│   └── run_once_unselect.jpeg
├── apprun.jpeg
├── common
│   ├── card_228x32_select.jpeg
│   └── card_228x32_unselect.jpeg
├── develop
│   ├── private.jpeg
│   └── public.jpeg
├── develop.jpeg
├── ezdata.jpeg
├── ico
│   ├── a.jpeg
│   ├── b.jpeg
│   ├── c.jpeg
│   ├── d.jpeg
│   ├── e.jpeg
│   ├── f.jpeg
│   ├── g.jpeg
│   ├── h.jpeg
│   ├── i.jpeg
│   ├── j.jpeg
│   ├── k.jpeg
│   ├── l.jpeg
│   ├── m.jpeg
│   ├── n.jpeg
│   ├── o.jpeg
│   ├── p.jpeg
│   ├── q.jpeg
│   ├── r.jpeg
│   ├── s.jpeg
│   ├── t.jpeg
│   ├── u.jpeg
│   ├── v.jpeg
│   ├── w.jpeg
│   ├── x.jpeg
│   ├── y.jpeg
│   └── z.jpeg
├── left.jpeg
├── right.jpeg
├── setting
│   ├── caret_right.jpeg
│   ├── general
│   │   ├── disable.jpeg
│   │   └── enable.jpeg
│   ├── general.jpeg
│   ├── wlan
│   │   ├── input_default.jpeg
│   │   ├── input_psk.jpeg
│   │   ├── input_server.jpeg
│   │   ├── input_ssid.jpeg
│   │   ├── submit_select.jpeg
│   │   └── submit_unselect.jpeg
│   └── wlan.jpeg
├── setting.jpeg
├── sidebar
│   ├── Aa.jpeg
│   ├── Aa0.jpeg
│   ├── alt.jpeg
│   ├── alt0.jpeg
│   ├── ctrl.jpeg
│   ├── ctrl0.jpeg
│   ├── fn.jpeg
│   ├── fn0.jpeg
│   ├── opt.jpeg
│   └── opt0.jpeg
└── statusbar
    ├── battery
    │   ├── black.jpeg
    │   ├── black_charge.jpeg
    │   ├── green.jpeg
    │   ├── green_charge.jpeg
    │   ├── red.jpeg
    │   └── red_charge.jpeg
    ├── cloud
    │   ├── empty.jpeg
    │   ├── error.jpeg
    │   └── green.jpeg
    ├── title_blue.jpeg
    └── wifi
        ├── disconnected.jpeg
        ├── empty.jpeg
        ├── good.jpeg
        ├── mid.jpeg
        └── worse.jpeg

13 directories, 78 files

```

### Common
```
Path /system/common

├── font
│   ├── Montserrat-Medium-10.vlw
│   ├── Montserrat-Medium-12.vlw
│   ├── Montserrat-Medium-14.vlw
│   ├── Montserrat-Medium-16.vlw
│   └── Montserrat-Medium-18.vlw
├── img
│   └── avatar.jpg
└── wav
    ├── bg.wav
    ├── click.wav
    ├── insert.wav
    └── remove.wav

4 directories, 10 files
```



## Screen
```
    Widgets.setBrightness(100)
    Widgets.fillScreen(0x6600CC)
    Widgets.setRotation(0)
```


## MQTT
```python
import os, sys, io
import M5
from M5 import *
from unit import MQTTUnit
import time


mqtt_0 = None


def mqtt_0_SubTopic_event(data):  # noqa: N802
    global mqtt_0
    print(data[0])
    print(data[1])


def setup():
    global mqtt_0

    M5.begin()
    Widgets.fillScreen(0x222222)

    mqtt_0 = MQTTUnit(port=(18, 17))
    mqtt_0.set_client("m5-mqtt-xxx", "mqtt.m5stack.com", 1883, "", "", 120)
    mqtt_0.set_subscribe("SubTopic", mqtt_0_SubTopic_event, 0)
    mqtt_0.set_connect()


def loop():
    global mqtt_0
    M5.update()
    mqtt_0.check_msg()
    time.sleep_ms(50)


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
```


## Widget

### Image


```
    image0 = Widgets.Image("res/img/SCR-20240902-itcy.png", 71, 64)
    title0 = Widgets.Title("Image CoreS3 Example", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)

    image0.setImage("res/img/default.png")
    image0.setImage("res/img/SCR-20240902-itcy.png")
    image0.setCursor(x=0, y=0)
    image0.setVisible(True)
```

### Image Plus

```
    Widgets.fillScreen(0x222222)
    title0 = Widgets.Title("Image+ CoreS3 Example", 3, 0xFFFFFF, 0x0000FF, Widgets.FONTS.DejaVu18)
    image_plus0 = ImagePlus(
        "https://static-cdn.m5stack.com/resource/public/assets/aboutus/m5logo2022.png",
        43,
        51,
        True,
        3000,
        default_img="res/img/default.png",
    )

    image_plus0.setVisible(True)
    image_plus0.set_update_period(5000)
    image_plus0.set_update_enable(True)
```


### Label Pluss

```

def btnPWR_wasClicked_event(state):  # noqa: N802
    global label_plus0, en
    en = not en
    if en:
        label_plus0.set_update_enable(True)
    else:
        label_plus0.set_update_enable(False)


def setup():
    global label_plus0, en

    M5.begin()
    Widgets.setRotation(1)
    Widgets.fillScreen(0x222222)
    label_plus0 = LabelPlus(
        "label_plus0",
        24,
        31,
        1.0,
        0xFFFFFF,
        0x222222,
        Widgets.FONTS.DejaVu18,
        "http://192.168.8.200:8000/data",
        3000,
        True,
        "data",
        "error",
        0xFF0000,
    )

    BtnPWR.setCallback(type=BtnPWR.CB_TYPE.WAS_CLICKED, cb=btnPWR_wasClicked_event)

    en = True

```


## Audio

### Play amr file

```
from audio import Recorder
from audio import Player


recorder = None
player = None


def setup():
    global recorder, player

    M5.begin()
    Widgets.fillScreen(0x222222)

    recorder = Recorder(8000, 16, True)
    recorder.record("file://flash/res/audio/test.amr", 5, True)
    player = Player(None)
    player.play("file://flash/res/audio/test.amr", pos=0, volume=100, sync=True)
```



## M5 LCD
```
    M5.Lcd.setFont(Widgets.FONTS.DejaVu12)
    M5.Lcd.setTextColor(0xFFFFFF, 0x000000)
    M5.Lcd.setCursor(0, 0)
    M5.Lcd.printf(">>> ")
```


## WIFI Tips

```
# Connect to existing WiFi and display IP
wlan = network.WLAN(network.STA_IF)
if wlan.isconnected():
    ip_info = wlan.ifconfig()
    ip_addr = ip_info[0]
    print("Local IP Address:", ip_addr)
    print("\nPlease open your browser and visit http://%s:8080 to view the stream.\n" % ip_addr)
else:
    print("WiFi not connected.")
```



## SDCARD

```
from hardware import sdcard

sdcard.SDCard(slot=3, width=1, sck=40, miso=39, mosi=14, cs=12, freq=20000000)
```


## Audio - Speakers
| Parameter        | Type      | Description                                                                |
| ---------------- | --------- | -------------------------------------------------------------------------- |
| pin_data_out     | (integer) | Serial data line of I2S, representing audio data in binary complement.     |
| pin_bck          | (integer) | Serial clock line of I2S, corresponding to each bit of digital audio data. |
| pin_ws           | (integer) | Frame clock of I2S, used to switch left and right channel data.            |
| sample_rate      | (integer) | Target sampling rate of output audio.                                      |
| stereo           | (boolean) | Use stereo output.                                                         |
| buzzer           | (boolean) | Use single GPIO buzzer.                                                    |
| use_dac          | (boolean) | Use DAC speaker.                                                           |
| dac_zero_level   | (integer) | Zero level reference value when using DAC.                                 |
| magnification    | (integer) | Multiplier of the input value.                                             |
| dma_buf_len      | (integer) | DMA buffer length of I2S.                                                  |
| dma_buf_count    | (integer) | Number of DMA buffers of I2S.                                              |
| task_priority    | (integer) | Priority of background tasks.                                              |
| task_pinned_core | (integer) | CPU used by background tasks.                                              |
| i2s_port         | (integer) | I2S port.                                                                  |





| Stamp-S3A (ESP32-S3 GPIO) | ES8311 Pin | Function & Explanation                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| G8(GPIO8)                 | SDA        | I2C Data Line - Part of the I2C (Inter-Integrated Circuit) bus used to configure the ES8311 (e.g., set volume, gain, or modes). - SDA carries bidirectional data between the ESP32-S3 (master) and ES8311 (slave). - Requires a pull-up resistor (typically 4.7kΩ to 3.3V). In MicroPython: Use machine.I2C(0, scl=Pin(9), sda=Pin(8)). |
| G9(GPIO9)                 | SCL        | I2C Clock Line - The clock signal for the I2C bus, synchronizing data transfer. - Generated by the ESP32-S3; typical speed is 100–400 kHz. - Also needs a pull-up resistor. Common for codec setup before I2S audio streaming.                                                                                                          |
| G41(GPIO41)               | SCLK       | I2S Serial Clock (Bit Clock) - Provides the clock for serial data transfer in I2S (Inter-IC Sound) protocol. - Determines the sample rate (e.g., 44.1 kHz audio needs ~2.8 MHz SCLK). - Output from ESP32-S3 to ES8311; essential for timing audio bits. In MicroPython: Configured via machine.I2S.                                    |
| G46(GPIO46)               | ASDOUT     | I2S Serial Data Out (Playback) - Carries digital audio data from the ESP32-S3 to the ES8311 for output (e.g., to speakers). - Supports stereo PCM audio up to 24-bit/192 kHz. - This is the "TX" line for audio playback.                                                                                                               |
| G43(GPIO43)               | LRCK       | I2S Word Select (Left/Right Clock) - Also called WS or BCLK (but here it's LRCK for Left/Right channel select). - Switches between left and right audio channels (e.g., high for left, low for right). - Runs at the sample rate (e.g., 48 kHz). Critical for stereo audio.                                                             |
| G42(GPIO42)               | DSDIN      | I2S Data In (Record) - Carries digital audio data from the ES8311 to the ESP32-S3 for input (e.g., from a microphone). - This is the "RX" line for audio recording. Supports high SNR (signal-to-noise ratio) for clear voice capture.                                                                                                  |



| Stamp-S3A | G8  | G9  | G41  | G46    | G43  | G42   |
|-----------|-----|-----|------|--------|------|-------|
| ES8311    | SDA | SCL | SCLK | ASDOUT | LRCK | DSDIN |

