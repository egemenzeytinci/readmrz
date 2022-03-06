# readmrz

`readmrz` detects the machine readable zone on ID cards and extracts the text in that zone. 

This zone contains the name, surname, date of birth, etc. of the person to whom the identity card was issued. 
It has universal standards in new generation identity cards and passports.

## Install

Latest release on PyPI:

```zsh
$ pip install readmrz
```

## Usage

```python
>>> import json
>>> from readmrz import MrzDetector, MrzReader

>>> detector = MrzDetector()
>>> reader = MrzReader()

>>> image = detector.crop_area('/path/to/file')
>>> result = reader.process(image)
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

The result is returned as json so it's easy to access the fields. You can also use command-line,

```zsh
$ readmrz -p /path/to/file
```

## Example

![example](/images/flow.jpg)

Please check to the [notebook](https://github.com/egemenzeytinci/readmrz/blob/master/notebook/example.ipynb) to see the results step by step.


## Contribution

Please check to the pylint and flake8 steps in workflow before contribution.
