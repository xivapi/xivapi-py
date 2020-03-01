import re

import setuptools

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as f:
    README = f.read()

with open('xivapi/__init__.py') as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name='xivapi',
    author='Lethys',
    author_email='seraymericbot@gmail.com',
    url='https://github.com/xivapi/xivapi-py',
    version=VERSION,
    packages=['xivapi'],
    license='MIT',
    description='An asynchronous Python client for XIVAPI',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords='ffxiv xivapi',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
