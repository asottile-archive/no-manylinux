from setuptools import setup

setup(
    name='no-manylinux1',
    description=(
        'Install this package to disable manylinux1 wheels when dowloading '
        'from pip.'
    ),
    url='https://github.com/asottile/no-manylinux1',
    version='1.0.0',
    author='Anthony Sottile',
    author_email='asottile@umich.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    py_modules=['_manylinux'],
)
