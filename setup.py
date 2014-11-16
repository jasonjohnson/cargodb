from setuptools import setup

setup(
    name='CargoDB',
    version='0.0.1',
    description='A simple document-oriented databse.',
    author='Jason Johnson',
    author_email='spligak@gmail.com',
    license='MIT',
    packages=[
        'cargo'
    ],
    entry_points={
        'console_scripts': [
            'cargodb-wsgiref = cargo.wsgi.application:main',
            'cargodb-storage = cargo.storage.application:main'
        ]
    }
)
