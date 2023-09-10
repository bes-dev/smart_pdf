"""
Copyright 2023 by Sergei Belousov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import setup, find_packages

readme = open('README.md').read()

VERSION = '2023.09.11.1'

requirements = [
    'openai==0.27.6',
    'langchain==0.0.285',
    'pypdf==3.16.0',
    'tiktoken==0.4.0',
    'faiss-cpu==1.7.3'
]

setup(
    # Metadata
    name='smart_pdf',
    version=VERSION,
    author='Sergei Belousov aka BeS',
    author_email='sergei.o.belousov@gmail.com',
    description='SmartPDF: AI powered pdf reader.',
    long_description=readme,
    long_description_content_type='text/markdown',

    # Package info
    packages=find_packages(exclude=('*test*',)),

    #
    zip_safe=True,
    install_requires=requirements,

    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
