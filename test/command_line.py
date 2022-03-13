import json
import subprocess
from pathlib import Path
from unittest import TestCase


class CommandLineTest(TestCase):
    BASE = 'https://raw.githubusercontent.com/egemenzeytinci'
    VALID_URL = f'{BASE}/readmrz/master/images/example.jpg'

    def test_valid_file(self):
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

        cmd = f'readmrz -f {full_path}'

        with subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True) as proc:
            res = proc.stdout.read()

        self.assertDictEqual(expected, json.loads(res))

    def test_valid_url(self):
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

        cmd = f'readmrz -u {self.VALID_URL}'

        with subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True) as proc:
            res = proc.stdout.read()

        self.assertDictEqual(expected, json.loads(res))
