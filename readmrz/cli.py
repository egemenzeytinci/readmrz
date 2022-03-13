import argparse
import json
from .detector import MrzDetector
from .reader import MrzReader


def main():
    parser = argparse.ArgumentParser(
        prog='readmrz', description='Read mrz code on ID cards'
    )

    parser.add_argument(
        '-f', '--file', help='The image file path to read mrz code'
    )

    parser.add_argument(
        '-u', '--url', help='The image url to read mrz code'
    )

    args = parser.parse_args()

    if args.file and args.url:
        raise Exception('File path and url cannot be pass at the same time.')

    detector = MrzDetector()

    reader = MrzReader()

    if args.file:
        image = detector.read(args.file)
    elif args.url:
        image = detector.read_from_url(args.url)

    cropped = detector.crop_area(image)

    result = reader.process(cropped)

    print(json.dumps(result, indent=4))
