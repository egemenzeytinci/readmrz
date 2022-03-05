import os
import pytesseract
import re


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
