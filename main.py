from setuptools import setup, find_packages

setup(
    name='reCaptchaV3Bypass',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A library to bypass reCAPTCHA v3 challenges',
    author='rdwxth',
    author_email='your.email@example.com',
    url='https://github.com/rdwxth/reCaptchaV3Bypass',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
