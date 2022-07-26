from setuptools import setup

VERSION = '0.0.1'


setup(
    nam='cloudpayments-client-charge',
    packages=['cloudpayments-client-charge'],

    description='Client Library for method charge through Cloudpayments',
    long_description="",

    version=VERSION,

    author='Antonida Medvedeva',
    author_email='antonida619@gmail.com',
    license='MIT license',

    url='https://github.com/Rainbow42/client-cloudpayments-charge',
    download_url='https://github.com/Rainbow42/client-cloudpayments-charge/%s' % VERSION,

    requires=[
        'requests (>=2.28.1)',
        'marshmallow (>=3.17.0)',
        'aiohttp (>=3.8.1)',
        'marshmallow-dataclass (>=8.5.8)'
    ],

    install_requires=[
        'requests (>=2.28.1)',
        'marshmallow (>=3.17.0)',
        'aiohttp (>=3.8.1)',
        'marshmallow-dataclass (>=8.5.8)'
    ],

    classifiers=[
        'Development Status ::',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',

        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    zip_safe=False
)
