# readmrz

`readmrz` detects the machine readable zone on ID cards and extracts the text in that zone.

This zone contains the name, surname, date of birth, etc. of the person to whom the identity card was issued.
It has universal standards in new generation identity cards and passports.

In conclusion, `readmrz` is a tool to read mrz code on identity cards and passports.

## Install

Please install `tesseract` before installing the package,

On macOS,

```zsh
$ brew install tesseract
```

On Ubuntu,

```zsh
$ sudo apt-get install -y tesseract-ocr
```

On Windows,

```zsh
$ choco install tesseract
```

Then you can install the latest release,

```zsh
$ pip install readmrz
```

## Usage

```python
>>> import json
>>> from readmrz import MrzDetector, MrzReader

>>> detector = MrzDetector()
>>> reader = MrzReader()

>>> image = detector.read('/path/to/file')
>>> cropped = detector.crop_area(image)
>>> result = reader.process(cropped)
>>> print(json.dumps(result))
{
    "surname": "STEARNE",
    "name": "JOHN TIMOTHY KELLY",
    "country": "CAN",
    "nationality": "CAN",
    "birth_date": "580702",
    "expiry_date": "240904",
    "sex": "M",
    "document_type": "P",
    "document_number": "GA302922",
    "optional_data": "",
    "birth_date_hash": "0",
    "expiry_date_hash": "3",
    "document_number_hash": "0",
    "final_hash": "2"
}
```

or using url,

```python
>>> import json
>>> from readmrz import MrzDetector, MrzReader

>>> detector = MrzDetector()
>>> reader = MrzReader()

>>> image = detector.read_from_url('/url/to/image')
>>> cropped = detector.crop_area(image)
>>> result = reader.process(cropped)
>>> print(json.dumps(result))
{
    "surname": "STEARNE",
    "name": "JOHN TIMOTHY KELLY",
    "country": "CAN",
    "nationality": "CAN",
    "birth_date": "580702",
    "expiry_date": "240904",
    "sex": "M",
    "document_type": "P",
    "document_number": "GA302922",
    "optional_data": "",
    "birth_date_hash": "0",
    "expiry_date_hash": "3",
    "document_number_hash": "0",
    "final_hash": "2"
}
```

The result is returned as a dict so it's easy to access the fields. You can also use command-line,

```zsh
$ readmrz -f /path/to/file
```

or using url,

```zsh
$ readmrz -u /url/to/image
```

## Example

![example](/images/flow.jpg)

Please check to the [notebook](https://github.com/egemenzeytinci/readmrz/blob/master/notebook/example.ipynb) to see the results step by step.

## Contribution

Please check to the pylint and flake8 steps in workflow before contribution.
