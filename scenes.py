import cv2
import numpy
from skimage import measure

WIDTH = 1920
HEIGHT = 1124
SCENES = {
    "tower-select": {
        "score": 0,
        "key_sequence": ["y"],
        "range_x": slice(400, WIDTH - 400),
        "range_y": slice(0, HEIGHT),
    },
    "tower-continue": {
        "score": 0,
        "key_sequence": ["y"],
        "range_x": slice(0, int((WIDTH / 3) * 2)),
        "range_y": slice(400, HEIGHT),
    },
    "tower-continue-fatality": {
        "score": 0,
        "key_sequence": ["y"],
        "range_x": slice(0, int((WIDTH / 3) * 2)),
        "range_y": slice(400, HEIGHT),
    },
    "tower-continue-brutality": {
        "score": 0,
        "key_sequence": ["y"],
        "range_x": slice(0, int((WIDTH / 3) * 2)),
        "range_y": slice(400, HEIGHT),
    },
    "tower-lose": {
        "score": 0,
        "key_sequence": ["y", "d", "y"],
        "range_x": slice(0, int((WIDTH / 3) * 2)),
        "range_y": slice(400, HEIGHT),
    },
    "tower-difficulty": {
        "score": 0,
        "key_sequence": ["y"],
        "range_x": slice(400, WIDTH - 400),
        "range_y": slice(400, HEIGHT),
    },
    "tower-character": {
        "score": 0,
        "key_sequence": ["d", "y"],
        "range_x": slice(0, int(WIDTH / 2)),
        "range_y": slice(0, HEIGHT),
    },
    "tower-variation": {
        "score": 0,
        "key_sequence": ["u", "a", "y"],
        "range_x": slice(0, int(WIDTH / 2)),
        "range_y": slice(0, HEIGHT),
    },
}


class Scenes:
    @staticmethod
    def load_image(image_name):
        return cv2.imread("./{}".format(image_name))

    @staticmethod
    def guess_scene():
        screenshot = Scenes.load_image("screenshot.jpg")
        imhsv = screenshot
        (h, s, v) = cv2.split(imhsv)
        
        # stack = numpy.hstack([h,s,v])
        # cv2.imshow("stack hsv", cv2.resize(stack, (480*3, 281)))
        # cv2.waitKey(0)
        # cv2.imshow("test",screenshot)
        # cv2.waitKey(0)

        for scene in SCENES:
            scene_screenshot = Scenes.load_image("./dataset/{}.jpg".format(scene))
            imhsv2 = scene_screenshot

            (h2, s2, v2) = cv2.split(imhsv2)

            range_x = SCENES[scene]["range_x"]
            range_y = SCENES[scene]["range_y"]

            (score, diff) = measure.compare_ssim(
                s[range_y, range_x],
                s2[range_y, range_x],
                full=True,
            )
            SCENES[scene]["score"] = score

        return max(SCENES, key=lambda key: SCENES[key]["score"])
