import codecs
from os.path import dirname, join

from setuptools import setup, find_packages

here = dirname(__file__)


def read(*parts):
    return codecs.open(join(here, *parts), 'r').read()


def find_version(*file_paths):
    version = read(*file_paths).strip()
    if version == '':
        raise RuntimeError('No version found')
    return version


setup(
    name='credsmash',
    version=find_version('credsmash', 'VERSION'),

    maintainer="Nathan Muir",
    maintainer_email="ndmuir@gmail.com",

    url='https://github.com/3stack-software/credsmash',

    license='Apache2',
    description='A utility for managing secrets in the cloud using AWS KMS and DynamoDB',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests',)),

    package_data={
        'credsmash': ['VERSION']
    },

    python_requires=">=3.8",
    install_requires=[
        'cryptography',
        'boto3',
        'click',
        'six',
        'importlib_resources>=5.12',
        'importlib_metadata>=6.5'
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'yaml': ['PyYAML'],
        'templates': ['jinja2'],
        'documentation': [],
        'dev': ['PyYAML', 'jinja2', 'pytest']
    },
    entry_points={
        'console_scripts': [
            'credsmash = credsmash.cli:main'
        ],
        'credsmash.key_service': [
            'kms = credsmash.kms_key_service:KmsKeyService',
        ],
        'credsmash.storage_service': [
            'dynamodb = credsmash.dynamodb_storage_service:DynamoDbStorageService',
        ],
        'credsmash.cli': [
            'templates = credsmash.templates',
            'dynamodb = credsmash.cli_dynamodb'
        ]
    },

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
