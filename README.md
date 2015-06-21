Alerta API on OpenShift
=======================

[Alerta](http://alerta.io) is a alerting server based on Flask with an AngularJS web front-end for alert visualisation and built-in support for many monitoring tools that is also easily extensible using a command-line tool or API.

RedHat [OpenShift](https://www.openshift.com/products/online) is a PaaS that can be used to run web applications like [Flask apps](https://developers.openshift.com/en/python-flask.html) for [free](https://www.openshift.com/products/pricing). 

Installation
------------

To deploy the Alerta API to RedHat Openshift, sign-up for free, install the [rhc](https://developers.openshift.com/en/getting-started-osx.html#client-tools) tool and run:

    $ rhc app create alerta python-2.7 mongodb-2.4 --from-code=git://github.com/alerta/openshift-api-alerta.git

The Alerta API should be available at http://alerta-$namespace.rhcloud.com


Configuration
-------------

Show current environment variable settings:

    $ rhc env

Set environment variable for running app:

    $ rhc set-env 

Troubleshooting
---------------

Show all apps running in OpenShift:

    $ rhc show-app alerta

    $ rhc tail 


If problems persist, try deleting the app and recreating:

    $ rhc app delete -a alerta

TBC

License
-------

Copyright (c) 2015 Nick Satterly. Available under the MIT License.

