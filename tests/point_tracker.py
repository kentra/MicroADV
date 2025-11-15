import os, sys, io
import M5
from M5 import *
from hardware import MatrixKeyboard
from unit import KeyCode
import network


oponent_point_label = None
my_points_label = None
nickname_popup = None
nickname_title = None
nickname_input_bg = None
nickname_prompt = None
nickname_input = None
statusbar = None
statusbar_line = None
shield = None
kb = None
wlan = None


operator = None
value = None
text = None
show = None
input_value = None
backspace = None
buf_key_int = None
my_points = None
statusbar_buf = None
nickname_popup_state = None
point_tracker_state = None
nickname = None
my_points_startup = None


# Describe this function...
def update_points(operator, value):
    global text, show, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if operator == "+":
        my_points = my_points + value
        my_points_label.setText(str(my_points))
    elif operator == "-" and my_points > 0:
        my_points = my_points - value
        my_points_label.setText(str(my_points))
    elif operator == "=":
        my_points = my_points_startup
        my_points_label.setText(str(my_points))


# Describe this function...
def refresh_statusbar():
    global operator, value, text, show, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    statusbar.setText(statusbar_buf)
    statusbar.setVisible(True)
    statusbar_line.setVisible(True)


# Describe this function...
def print_debug(text):
    global operator, value, show, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    print(text)


# Describe this function...
def show_nickname_popup(show):
    global operator, value, text, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if show:
        nickname_popup_state = True
        nickname_popup.setVisible(True)
        nickname_input_bg.setVisible(True)
        nickname_title.setVisible(True)
        nickname_input.setVisible(True)
        nickname_prompt.setVisible(True)
    else:
        nickname_popup_state = False
        nickname_popup.setVisible(False)
        nickname_input_bg.setVisible(False)
        nickname_title.setVisible(False)
        nickname_input.setVisible(False)
        nickname_prompt.setVisible(False)
    refresh_statusbar()


# Describe this function...
def show_point_tracker(show):
    global operator, value, text, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if show:
        point_tracker_state = True
        shield.setVisible(True)
        my_points_label.setVisible(True)
        oponent_point_label.setVisible(True)
    else:
        point_tracker_state = False
        shield.setVisible(False)
        my_points_label.setVisible(False)
        oponent_point_label.setVisible(False)
    refresh_statusbar()


# Describe this function...
def kb_nav_mode():
    global operator, value, text, show, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if buf_key_int == 59:
        print("UP")
        update_points("+", 1)
    elif buf_key_int == 46:
        print("DOWN")
        update_points("-", 1)
    elif buf_key_int == 44:
        update_points("-", 5)
    elif buf_key_int == 47:
        update_points("+", 5)


# Describe this function...
def kb_type_mode():
    global operator, value, text, show, input_value, backspace, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if buf_key_int == (KeyCode.KEYCODE_BACKSPACE):
        print("BACKSPACE")
        update_nickname(chr(buf_key_int), True)
    elif buf_key_int == (KeyCode.KEYCODE_ENTER):
        statusbar_buf = str(">") + str(nickname)
        show_nickname_popup(False)
        show_point_tracker(True)
    else:
        update_nickname(chr(buf_key_int), False)


# Describe this function...
def update_nickname(input_value, backspace):
    global operator, value, text, show, buf_key_int, my_points, statusbar_buf, nickname_popup_state, point_tracker_state, nickname, my_points_startup, oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan
    if backspace:
        nickname = nickname[: int(len(nickname) - 1)]
    else:
        if len(nickname) <= 7:
            nickname = str(nickname) + str(input_value)
    nickname_input.setText(str(nickname))


def kb_pressed_event(kb_0):
    global oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan, buf_key_int, my_points, statusbar_buf, text, show, nickname_popup_state, point_tracker_state, backspace, nickname, operator, my_points_startup, value, input_value
    buf_key_int = kb.get_key()
    if point_tracker_state:
        print("Keyboard NAV mode")
        print_debug(buf_key_int)
        kb_nav_mode()
    else:
        print("Keyboard typing mode")
        print_debug(chr(buf_key_int))
        kb_type_mode()


def setup():
    global oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan, buf_key_int, my_points, statusbar_buf, text, show, nickname_popup_state, point_tracker_state, backspace, nickname, operator, my_points_startup, value, input_value

    M5.begin()
    Widgets.fillScreen(0x222222)
    oponent_point_label = Widgets.Label(
        "50", 179, 83, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu40
    )
    my_points_label = Widgets.Label(
        "50", 92, 50, 1.0, 0x000000, 0x75D414, Widgets.FONTS.DejaVu40
    )
    nickname_popup = Widgets.Rectangle(43, 48, 149, 60, 0x8CFF00, 0x000000)
    nickname_title = Widgets.Label(
        "Enter Nickname:", 47, 52, 1.0, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu12
    )
    nickname_input_bg = Widgets.Rectangle(46, 70, 143, 35, 0x3B3B3B, 0xFFFFFF)
    nickname_prompt = Widgets.Label(
        ">", 53, 77, 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu18
    )
    nickname_input = Widgets.Label(
        " ", 74, 74, 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu24
    )
    statusbar = Widgets.Title("Title", 3, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu18)
    statusbar_line = Widgets.Line(0, 18, 245, 18, 0xB81785)
    shield = Widgets.Image(
        "/flash/res/img/shield_crop.png", 71, 7, scale_x=0.7, scale_y=0.7
    )

    kb = MatrixKeyboard()
    kb.set_callback(kb_pressed_event)
    wlan = network.WLAN(network.STA_IF)
    wlan.connect("private.kentra.org", "kakekjeks")
    print(wlan.isconnected())
    my_points_startup = 50
    my_points = my_points_startup
    nickname = ""
    statusbar_buf = "Setup"
    statusbar.setText(statusbar_buf)
    show_point_tracker(False)
    show_nickname_popup(True)


def loop():
    global oponent_point_label, my_points_label, nickname_popup, nickname_title, nickname_input_bg, nickname_prompt, nickname_input, statusbar, statusbar_line, shield, kb, wlan, buf_key_int, my_points, statusbar_buf, text, show, nickname_popup_state, point_tracker_state, backspace, nickname, operator, my_points_startup, value, input_value
    M5.update()
    kb.tick()


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
