import pathlib
from setuptools import setup, find_packages

ROOT = pathlib.Path(__file__).parent
README = (ROOT / "README.md").read_text()

setup(
    name='docxlatex',
    version='0.1.6',
    description='Extract text from .docx files with support for inserted equations',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/hrushikeshrv/docxlatex',
    author='Hrushikesh Vaidya',
    author_email='hrushikeshrv@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(exclude=('docx',)),
    # py_modules=['docxlatex'],
    include_package_data=True,
    install_requires=['defusedxml'],
)
