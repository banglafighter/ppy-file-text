from setuptools import setup, find_packages
import os
import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
README = (CURRENT_DIR / "README.md").read_text()

env = os.environ.get('source')


def get_dependencies():
    dependency = []

    if env and env == "code":
        return dependency

    return dependency + ["ppy-common"]


setup(
    name='ppy-file-text',
    version='0.0.2',
    url='https://github.com/banglafighter/ppy-file-text',
    license='Apache 2.0',
    author='Bangla Fighter',
    author_email='banglafighter.com@gmail.com',
    description='PWeb Python File & Text is a library which help to perform text read write operation with file directory manipulation',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ]
)
