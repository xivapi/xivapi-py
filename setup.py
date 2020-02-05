import pathlib
import re

import setuptools


ROOT = pathlib.Path(__file__).parent

with open(ROOT / 'requirements.txt', encoding='utf-8') as f:
    REQUIREMENTS = f.readlines()

with open(ROOT / 'README.md', encoding='utf-8') as f:
    README = f.read()

with open(ROOT / 'xivapi' / '__init__.py', encoding='utf-8') as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name='xivapi-py',
    author='Lethys',
    url='https://github.com/xivapi/xivapi-py',
    version=VERSION,
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
