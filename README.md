Alerta API on OpenShift
=======================

[Alerta](http://alerta.io) is a alerting server based on Flask with an AngularJS web front-end for alert visualisation and built-in support for many monitoring tools that is also easily extensible using a command-line tool or API.

RedHat [Openshift](https://www.openshift.com/products/online) is a PaaS that can be used to run web applications like [Flask apps](https://developers.openshift.com/en/python-flask.html) for [free](https://www.openshift.com/products/pricing). 

Installation
------------

To deploy the Alerta API to RedHat Openshift, sign-up for free, install the [rhc](https://developers.openshift.com/en/getting-started-osx.html#client-tools) tool and run:

	$ rhc app create alerta python-2.7 mongodb-2.4 --from-code=https://github.com/alerta/openshift-api-alerta.git


Configuration
-------------

TBC

License
-------

Copyright (c) 2015 Nick Satterly. Available under the MIT License.
