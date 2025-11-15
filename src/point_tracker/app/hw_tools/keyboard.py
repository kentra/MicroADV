from hardware import MatrixKeyboard
from udataclasses import dataclass, field
from app.gui.ui_elements import UIStates
from unit import KeyCode


# States
@dataclass
class KBStates:
    kb_buf: int | str | None = None


class KeyboardTools:
    def __init__(self):
        # key buffer
        # Setup Keyboard
        self.kb: MatrixKeyboard = MatrixKeyboard()
        self.kb.set_callback(self.kb_pressed_event)

    def kb_pressed_event(self, kb_0):
        kb_buf = self.kb.get_key()
        if UIStates.point_tracker_state:
            print(f"Keyboard NAV mode - {chr(kb_buf)}")
            print(kb_buf)
            self.kb_nav_mode()
        else:
            print(f"Keyboard typing mode - {chr(kb_buf)}")
            self.kb_type_mode()

    def kb_nav_mode(self):
        if KBStates.kb_buf == 59:
            print("UP")
            # update_points("+", 1)
            pass
        elif KBStates.kb_buf == 46:
            print("DOWN")
            # update_points("-", 1)
            pass
        elif KBStates.kb_buf == 44:
            print("LEFT")
            # update_points("-", 5)
            pass
        elif KBStates.kb_buf == 47:
            print("RIGHT")
            # update_points("+", 5)
            pass

    def kb_type_mode(self):
        if UIStates.kb_buf == (KeyCode.KEYCODE_BACKSPACE):
            print("BACKSPACE")
            self.update_nickname(chr(kb_buf), True)
        elif self.kb_buf == (KeyCode.KEYCODE_ENTER):
            self.statusbar_buf = str(">") + str(self.nickname)
            self.show_nickname_popup(False)
            self.show_point_tracker(True)
        else:
            self.update_nickname(chr(kb_buf), False)
