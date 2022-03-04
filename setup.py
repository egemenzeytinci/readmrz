import setuptools

with open('README.md', 'r') as f:
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
    package_dir={'': 'src'},
    packages=['readmrz'],
    install_requires=[
        'opencv-python',
    ],
)
