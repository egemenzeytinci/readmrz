from .detector import MrzDetector
from .reader import MrzReader
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog='readmrz', description='Read mrz code on ID cards'
    )

    parser.add_argument(
        '-p', '--path', help='The image path to read mrz code'
    )

    args = parser.parse_args()

    detector = MrzDetector()

    image = detector.crop_area(args.path)

    reader = MrzReader()

    result = reader.process(image)

    print(json.dumps(result, indent=4))
