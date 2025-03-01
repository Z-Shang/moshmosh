from setuptools import setup, find_packages
from datetime import datetime

with open('README.md') as readme:
    readme = readme.read()

version = "0.1.1"

setup(
    name='moshmosh-syntax',
    version=version if isinstance(version, str) else str(version),
    keywords="syntax extension, macro, pattern matching", # keywords of your project separated by comma ","
    description="A hygienic syntax extension system for Python", # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    url='https://github.com/thautwarm/moshmosh',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    python_requires='>=3',
    entry_points={"console_scripts": []},
    # above option specifies commands to be installed,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd.compiler"]}
    install_requires=["uncompyle6"],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)