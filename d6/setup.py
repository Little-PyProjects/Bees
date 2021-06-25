from setuptools import setup

setup(
    name='d6',
    version='0.0.2',
    py_modules=['d6'],
    install_requires=[
        'Click',
    ],
    entry_points=""""
        [console_scripts]
        d6 = d6:cli
    """,
)
