
import setuptools

setuptools.setup(
    name='alerta',
    version='2.0.48',
    description='Alerta monitoring framework',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    packages=setuptools.find_packages(exclude=['bin', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'pymongo',
        'stomp.py',
        'PyYAML',
        'pytz'
    ],
    entry_points={
        'console_scripts': [
            'alerta = wsgi.alerta.server.shell:main',
        ]
    },
    keywords='alert monitoring system'
)
