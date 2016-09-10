
import setuptools

ALERTA_SERVER_VERSION = '4.8.3'
ALERTA_CLIENT_VERSION = '4.8.1'

setuptools.setup(
    name='openshift-api-alerta',
    version='%s' % ALERTA_SERVER_VERSION,
    description='Alerta API on OpenShift',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    install_requires=[
        'Flask>=0.10.1',
        'alerta-server==%s' % ALERTA_SERVER_VERSION,
        'alerta==%s' % ALERTA_CLIENT_VERSION,
        'alerta-geoip'
    ],
    dependency_links=[
        'https://github.com/guardian/alerta/tarball/master#egg=alerta-server-%s' % ALERTA_SERVER_VERSION,
        'https://github.com/alerta/python-alerta/tarball/master#egg=alerta-%s' % ALERTA_CLIENT_VERSION,
        'https://github.com/alerta/alerta-contrib.git#subdirectory=plugins/geoip'
    ],
    keywords='alert monitoring system openshift paas'
)
