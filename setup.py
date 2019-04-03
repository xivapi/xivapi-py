import setuptools

setuptools.setup(
    name="xivapi.py",
    version="0.1.1",
    author="Lethys",
    author_email="seraymericbot@gmail.com",
    license="MIT",
    description="An asynchronous Python client for XIVAPI",
    keywords='ffxiv xivapi',
    long_description_content_type="text/markdown",
    url="https://github.com/Yandawl/xivapi.py",
    packages=setuptools.find_packages(),
    install_requires=['asyncio', 'aiohttp'],
    python_requires='>=3.6.0',
)