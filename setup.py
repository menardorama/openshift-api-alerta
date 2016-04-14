
import setuptools

ALERTA_SERVER_VERSION = '4.7.10'
ALERTA_CLIENT_VERSION = '4.7.9'

setuptools.setup(
    name='openshift-api-alerta',
    version='%s' % ALERTA_SERVER_VERSION,
    description='Alerta API on OpenShift',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    install_requires=[
        'alerta-server==%s' % ALERTA_SERVER_VERSION,
        'alerta==%s' % ALERTA_CLIENT_VERSION
    ],
    dependency_links=[
        'https://github.com/guardian/alerta/tarball/master#egg=alerta-server-%s' % ALERTA_SERVER_VERSION,
        'https://github.com/alerta/python-alerta-client/tarball/master#egg=alerta-%s' % ALERTA_CLIENT_VERSION
    ],
    keywords='alert monitoring system openshift paas'
)
