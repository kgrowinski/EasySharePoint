from distutils.core import setup

setup(
    name='easy_sharepoint',
    version='0.1',
    packages=['easy_sharepoint'],
    url='',
    license='MIT',
    author='Krzysztof Growinski',
    author_email='k.growisnski@outlook.com',
    description='Sharepoint List Operations Python Library',
    requires=[
        "requests",
        "requests_ntlm"
    ]
)
