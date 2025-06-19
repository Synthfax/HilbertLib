from setuptools import setup, find_packages

setup(
    name='hilbertlib',
    version='6.17.25',
    description='An all-in-one Python library for bots, math, and more',
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
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)