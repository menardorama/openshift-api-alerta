
import setuptools

setuptools.setup(
    name='openshift-api-alerta',
    version='3.2.4',
    description='Alerta API on OpenShift',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    install_requires=[
        'alerta-server==3.2.4',
        'alerta==3.2.4'
    ],
    dependency_links=[
        'https://github.com/guardian/alerta/tarball/release/3.2#egg=alerta-server-3.2.6',
        'https://github.com/alerta/python-alerta-client/tarball/master#egg=alerta-3.2.6'
    ],
    keywords='alert monitoring system openshift paas'
)
