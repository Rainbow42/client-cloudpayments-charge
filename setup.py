import setuptools
from setuptools import setup

VERSION = '0.0.1'

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    nam='cloudpayments-client-charge',
    version=VERSION,
    author='Antonida Medvedeva',
    author_email='antonida619@gmail.com',
    license='MIT license',

    packages=setuptools.find_packages(),
    description='Client Library for method charge through Cloudpayments',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/Rainbow42/client-cloudpayments-charge',
    download_url='https://github.com/Rainbow42/client-cloudpayments-charge/%s' % VERSION,

    requires=[
        'requests (>=2.28.1)',
        'marshmallow (>=3.17.0)',
        'aiohttp (>=3.8.1)',
        'parameterized (>=0.8.1)'
    ],

    install_requires=[
        'requests (>=2.28.1)',
        'marshmallow (>=3.17.0)',
        'aiohttp (>=3.8.1)',
        'parameterized (>=0.8.1)'
    ],

    classifiers=[
        'Development Status ::',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Office/Business',
        "Topic :: Internet :: WWW/HTTP",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
