from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='kindle-clippings-parser',
    version='0.1.0',
    author='Andrew Dang-Tran',
    author_email='andrewdt1506@gmail.com',
    description='A python library for extracting highlights from a kindle clippings text file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AndrewDang-Tran/kindle-clippings-parser',
    packages=[
        'kindle_clippings_parser',
        'kindle_clippings_parser.models',
    ],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
