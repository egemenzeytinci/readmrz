import setuptools

with open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()


setuptools.setup(
    name='readmrz',
    version='0.0.2',
    author='Egemen Zeytinci',
    author_email='egemenzeytinci@gmail.com',
    description='Machine readable zone reader on ID cards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/egemenzeytinci/readmrz',
    packages=['readmrz'],
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'pytesseract',
    ],
)