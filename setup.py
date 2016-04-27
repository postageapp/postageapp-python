from setuptools import setup

setup(
    name='postageapp',
    version='0.1.0',
    description='Library for sending email via the PostageApp service',
    url='http://github.com/postageapp/postageapp-python',
    author='Scott Tadman',
    author_email='tadman@postageapp.com',
    license='MIT',
    packages=['postageapp'],
    install_requires=[
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
