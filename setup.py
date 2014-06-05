
import setuptools

setuptools.setup(
    name='openshift-api-alerta',
    version='3.1.0',
    description='Alerta monitoring framework on OpenShift',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    url='http://github.com/guardian/alerta',
    license='Apache License 2.0',
    packages=setuptools.find_packages(exclude=['bin', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'alerta-app==3.1.0'
    ],
    dependency_links = [
        'https://github.com/guardian/alerta/tarball/feature/login-oauth#egg=alerta-app-3.1.0'
    ],
    keywords='alert monitoring system openshift paas'
)
