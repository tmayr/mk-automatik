import os
import osascript
import pyautogui

from time import sleep
from screenshot import screencapture

WIDTH = 1920
HEIGHT = 1124


class Window:
    def __init__(self, app):
        self.app = app

    def position_window(self, x=0, y=0):
        script = """
            tell application "System Events" \n
                set position of first window of application process "%s" to {%s, %s} \n
            end tell
        """
        osascript.run(script % (self.app, x, y))

    def focus_window(self):
        osascript.run('activate application "{}"'.format(self.app))

    def take_screenshot(self):
        os.system(
            'screenshot -o jpg -f "screenshot.jpg" "{}" >/dev/null'.format(self.app)
        )

    def press_sequence(self, sequence):
        for key in sequence:
            pyautogui.press(key)
            sleep(1)
        return

