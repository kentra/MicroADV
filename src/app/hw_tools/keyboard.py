from hardware import MatrixKeyboard


class KeyboardTools:
    def __init__(self):
        # Setup Keyboard
        self.kb = MatrixKeyboard()
        self.kb.set_callback(self.kb_pressed_event)

    def kb_pressed_event(self, kb_0):
        keyCode = self.kb.get_key()
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
