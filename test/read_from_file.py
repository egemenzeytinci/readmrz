from pathlib import Path
from readmrz import MrzDetector, MrzReader
from unittest import TestCase


class ReadFromFileTest(TestCase):
    def test_valid(self):
        detector = MrzDetector()

        reader = MrzReader()

        cd = Path('.')

        # get base project directory
        p = cd.parent.parent.absolute()

        # full path of the image
        full_path = f'{p}/images/example.jpg'

        # expected result as a dict
        expected = {
            'surname': 'STEARNE',
            'name': 'JOHN TIMOTHY KELLY',
            'country': 'CAN',
            'nationality': 'CAN',
            'birth_date': '580702',
            'expiry_date': '240904',
            'sex': 'M',
            'document_type': 'P',
            'document_number': 'GA302922',
            'optional_data': '',
            'birth_date_hash': '0',
            'expiry_date_hash': '3',
            'document_number_hash': '0',
            'final_hash': '2'
        }

        # read image
        image = detector.read(full_path)

        # crop machine readable zone
        cropped = detector.crop_area(image)

        # extract mrz code
        result = reader.process(cropped)

        self.assertDictEqual(expected, result)

    def test_invalid_image(self):
        detector = MrzDetector()

        reader = MrzReader()

        cd = Path('.')

        # get base project directory
        p = cd.parent.parent.absolute()

        # full path of the image
        full_path = f'{p}/images/invalid_example.jpg'

        # read image
        image = detector.read(full_path)

        # crop machine readable zone
        cropped = detector.crop_area(image)

        # but mrz not exist in image
        with self.assertRaises(Exception) as context:
            reader.process(cropped)

        error = 'The MRZ code could not be detected.'

        self.assertTrue(error in str(context.exception))

    def test_invalid_type(self):
        detector = MrzDetector()

        cd = Path('.')

        # get base project directory
        p = cd.parent.parent.absolute()

        # full path of the image
        full_path = f'{p}/setup.py'

        # ivalid file type
        self.assertRaises(TypeError, detector.read, full_path)
