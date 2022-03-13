from readmrz import MrzDetector, MrzReader
from unittest import TestCase


class ReadFromUrlTest(TestCase):
    BASE = 'https://canadapassporthelp.ca/wp-content/uploads/2009/11'
    VALID_URL = f'{BASE}/1599px-JTK_Stearne_Passport-1024x727.jpg'

    def test_valid(self):
        detector = MrzDetector()

        reader = MrzReader()

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

        # read image from given url
        image = detector.read_from_url(self.VALID_URL)

        # crop machine readable zone
        cropped = detector.crop_area(image)

        # extract mrz code
        result = reader.process(cropped)

        self.assertDictEqual(expected, result)

    def test_invalid_url(self):
        detector = MrzDetector()

        # if the url is not valid
        with self.assertRaises(Exception) as context:
            detector.read_from_url(self.VALID_URL[:-1])

        self.assertTrue('HTTP Error 404: Not Found' in str(context.exception))
