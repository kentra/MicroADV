import M5
from M5 import Widgets
import asyncio
from udataclasses import dataclass, field


# States
@dataclass
class UIStates:
    state_one: str = field()
    state_two: bool = True
    nickname_popup_state: bool = True
    point_tracker_state: bool = False
    my_points: int = 50
    my_points_startup: int = 50
    statusbar_buf: str = "Setup"
    nickname: str = ""


# UI Elements
@dataclass
class UIElement:
    oponent_point_label: Widgets = Widgets.Label(
        "50", 179, 83, 1.0, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu40
    )
    my_points_label: Widgets = Widgets.Label(
        "50", 92, 50, 1.0, 0x000000, 0x75D414, Widgets.FONTS.DejaVu40
    )
    nickname_popup: Widgets = Widgets.Rectangle(43, 48, 149, 60, 0x8CFF00, 0x000000)
    nickname_title: Widgets = Widgets.Label(
        "Enter Nickname:", 47, 52, 1.0, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu12
    )
    nickname_input_bg: Widgets = Widgets.Rectangle(46, 70, 143, 35, 0x3B3B3B, 0xFFFFFF)
    nickname_prompt: Widgets = Widgets.Label(
        ">", 53, 77, 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu18
    )
    nickname_input: Widgets = Widgets.Label(
        " ", 74, 74, 1.0, 0x000000, 0xFFFFFF, Widgets.FONTS.DejaVu24
    )
    statusbar: Widgets = Widgets.Title(
        "Title", 3, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu18
    )
    statusbar_line: Widgets = Widgets.Line(0, 18, 245, 18, 0xB81785)
    shield: Widgets = Widgets.Image(
        "/flash/res/img/shield_crop.png", 71, 7, scale_x=0.7, scale_y=0.7
    )


class UI:
    def __init__(self) -> None:

        # Init M5UI
        self.M5 = M5.begin()
        self.Widgets = Widgets
        # Set bacground color
        self.Widgets.fillScreen(0x222222)

        # Set statusbar title
        # UIElement.statusbar.setText(UIStates.statusbar_buf)

    def show_nickname_popup(self, show) -> None:
        if show:
            UIStates.nickname_popup_state = True
            UIElement.nickname_popup.setVisible(True)
            UIElement.nickname_input_bg.setVisible(True)
            UIElement.nickname_title.setVisible(True)
            UIElement.nickname_input.setVisible(True)
            UIElement.nickname_prompt.setVisible(True)
        else:
            UIStates.nickname_popup_state = False
            UIElement.nickname_popup.setVisible(False)
            UIElement.nickname_input_bg.setVisible(False)
            UIElement.nickname_title.setVisible(False)
            UIElement.nickname_input.setVisible(False)
            UIElement.nickname_prompt.setVisible(False)
        self.refresh_statusbar()

    # Describe this function...
    def show_point_tracker(self, show) -> None:
        if show:
            UIStates.point_tracker_state = True
            UIElement.shield.setVisible(True)
            UIElement.my_points_label.setVisible(True)
            UIElement.oponent_point_label.setVisible(True)
        else:
            UIStates.point_tracker_state = False
            UIElement.shield.setVisible(False)
            UIElement.my_points_label.setVisible(False)
            UIElement.oponent_point_label.setVisible(False)
        self.refresh_statusbar()

    # Describe this function...
    def update_points(self, operator, value) -> None:
        if operator == "+":
            UIStates.my_points = UIStates.my_points + value
            UIElement.my_points_label.setText(str(UIStates.my_points))
        elif operator == "-" and UIStates.my_points > 0:
            UIStates.my_points = UIStates.my_points - value
            UIElement.my_points_label.setText(str(UIStates.my_points))
        elif operator == "=":
            UIStates.my_points = UIStates.my_points_startup
            UIElement.my_points_label.setText(str(UIStates.my_points))

    # Describe this function...
    def refresh_statusbar(self) -> None:
        UIElement.statusbar.setText(UIStates.statusbar_buf)
        UIElement.statusbar.setVisible(True)
        UIElement.statusbar_line.setVisible(True)
