import re

import setuptools

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as f:
    README = f.read()

with open('restcord/__init__.py') as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name='restcord.py',
    author='Lethys',
    url='https://github.com/Yandawl/restcord.py',
    version=VERSION,
    packages=['restcord'],
    license='MIT',
    description='An asynchronous Python client for Discord\'s API',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords='discord rest api python asynchronous',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
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
