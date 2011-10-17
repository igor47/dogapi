from setuptools import setup, find_packages
import sys

reqs = []
reqs.append("sphinx>=1.1.0")
reqs.append("simplejson>=2.2.1")
reqs.append("decorator>=3.3.2")
if sys.version_info < (2, 7):
    reqs.append("argparse>=1.2")

setup(
    name = "dogapi",
    version = "0.1.0",
    packages = find_packages("src"),
    package_dir = {'':'src'},
    author = "Datadog, Inc.",
    author_email = "packages@datadoghq.com",
    description = "Python bindings to Datadog's API and a user-facing command line tool.",
    license = "BSD",
    keywords = "datadog data",
    url = "http://datadoghq.com",
    install_requires= reqs,
    entry_points={
        'console_scripts': [
            'dog = dogshell:main',
        ],
    },
)
