
import setuptools

setuptools.setup(
    name='alerta',
    version='2.0.48',
    description='Alerta monitoring framework',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    include_package_data=True,
    install_requires=[
        'Flask',
        'pymongo',
        'stomp.py',
        'PyYAML',
        'pytz'
    ],
    keywords='alert monitoring system'
)
