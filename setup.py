from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='Qantani',
    version='0.1.0b1',
    url='http://github.com/bpeschier/qantani',
    author="Bas Peschier",
    author_email="bas.peschier@gmail.com",
    packages=['qantani', ],
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'requests',
    ],
)