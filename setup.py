from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='hilbertlib',
    version='6.19.25.2',
    description='HilbertLib is a Python library providing modular tools for bot development, mathematical operations, web utilities, color manipulation, and database management.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Synthfax',
    author_email='synthfax@gmail.com',
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot",
        "discord.py",
        "rapidfuzz",
        "mysql-connector-python"
    ],
    python_requires='>=3.7',
    url='https://github.com/Synthfax/HilbertLib',
    license='MIT',
    license_files=('LICENSE',),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
