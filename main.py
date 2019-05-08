import subprocess
import os
import sys

from shutil import copyfile
from datetime import datetime
from time import sleep

from window import Window
from scenes import Scenes, SCENES

CONFIDENCE_TRESHOLD = 0.70
APP_NAME = "PS4 Remote Play"


def main(window):
    window.take_screenshot()
    scene = Scenes.guess_scene()
    print("found scene {}".format(scene))
    print(SCENES[scene])
    
    if SCENES[scene]["score"] > CONFIDENCE_TRESHOLD:
        print("found scene {}".format(scene))
        print(SCENES[scene])
        print("\n")
        window.press_sequence(SCENES[scene]["key_sequence"])
        return

    # if SCENES[scene]["score"] < CONFIDENCE_TRESHOLD and SCENES[scene]["score"] > (
    #     CONFIDENCE_TRESHOLD - 0.05
    # ):
    #     copyfile("./screenshot.jpg", "./low-confidence-screenshots/screenshot-{}.jpg".format(datetime.now()))
    #     print("found scene {}".format(scene))
    #     print(SCENES[scene])
    #     print("\n\n")
    #     print(
    #         "scene was identified with low confidence, pressing default buttons and saving screenshot"
    #     )

    print("sending default y")
    window.press_sequence(["y"])


if __name__ == "__main__":
    window = Window(APP_NAME)
    # window.focus_window()
    # window.position_window()

    while True:
        main(window)
