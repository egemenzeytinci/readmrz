import os
import pytesseract
import re
from mrz.checker.td1 import TD1CodeChecker
from mrz.checker.td3 import TD3CodeChecker


class MrzReader:
    def __init__(self):
        # find root directory
        root = os.path.abspath(os.path.dirname(__file__))

        # get full path of language directory
        mrz_trained = os.path.join(root, 'language')

        # set tessdata prefix to language folder
        os.environ['TESSDATA_PREFIX'] = mrz_trained

        # set white list chars to config
        white_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<'

        self._config = f'tessedit_char_whitelist={white_list}'

        self._fields = [
            'surname',
            'name',
            'country',
            'nationality',
            'birth_date',
            'expiry_date',
            'sex',
            'document_type',
            'document_number',
            'optional_data',
            'birth_date_hash',
            'expiry_date_hash',
            'document_number_hash',
            'final_hash',
        ]

    def read_mrz(self, image):
        """
        Read mrz code from cropped image

        :param np.ndarray image: cropped image
        :return: extracted text
        :rtype: str
        """
        # extracted text from image
        extracted = pytesseract.image_to_string(
            image,
            lang='mrz',
            config=self._config
        )

        # split by enter char
        lines = extracted.split('\n')

        # pattern to find text between `<` chars
        pattern = '^.*?[<]{1,3}([0-9]{1,6}|[<]{1,2})$'

        codes = []

        # remove text if line does not match pattern
        for line in lines:
            if re.match(pattern, line):
                codes.append(line.replace(' ', ''))

        return '\n'.join(codes)

    def get_fields(self, code):
        """
        Extract identity fields from string

        :param str code: code contains identity fields
        :return: extracted fields
        :rtype: dict
        """
        result = {}

        try:
            # validate code
            # 92 characters -> ID card
            # 89 characters -> Passport
            if len(code) == 92:
                checker = TD1CodeChecker(code)
            elif len(code) == 89:
                checker = TD3CodeChecker(code)
            else:
                raise Exception('The MRZ code could not be detected.')

            # extract fields
            fields = checker.fields()

            # add field to result dict
            for field in self._fields:
                val = getattr(fields, field)
                result[field] = val
        except Exception as e:
            raise Exception(e) from e

        return result

    def process(self, image):
        """
        Extract identity fields from cropped image

        :param np.ndarray image: cropped image
        :return: identity fields as json format
        :rtype: json
        """
        # get text from cropped image
        code = self.read_mrz(image)

        # get identity fields from text
        return self.get_fields(code)
