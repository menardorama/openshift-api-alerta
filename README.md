Alerta API on OpenShift
=======================

[Alerta](http://alerta.io) is an alerting server based on Flask with an AngularJS web front-end.

RedHat [OpenShift](https://www.openshift.com/products/online) is a PaaS that can be used to run web applications like [Flask apps](https://developers.openshift.com/en/python-flask.html) for [free](https://www.openshift.com/products/pricing). 

Installation
------------

To deploy the Alerta API to RedHat Openshift, sign-up for free, install the [rhc](https://developers.openshift.com/en/getting-started-osx.html#client-tools) tool and run:

    $ rhc app create alerta python-2.7 mongodb-2.4 \
    AUTH_REQUIRED=False \
    --from-code=git://github.com/alerta/openshift-api-alerta.git

The Alerta API should be available at http://alerta-$namespace.rhcloud.com

To deploy with authentication enforced set `AUTH_REQUIRED` to `True`. To use OAuth credentials for user logins set the `CLIENT_ID` and `CLIENT_SECRET` as supplied by the OAuth provider, or just leave blank for `Basic Auth`:

    $ rhc app create alerta python-2.7 mongodb-2.4 \
    AUTH_REQUIRED=True \
    CLIENT_ID=379647311730-6tfdcopl5fodke08el52nnoj3x8mpl3.apps.googleusercontent.com \
    CLIENT_SECRET=UpJxs02c_bx9GlI3X8MPL3-p \
    --from-code=git://github.com/alerta/openshift-api-alerta.git

Configuration
-------------

Show current environment variable settings:

    $ rhc env list -a alerta
    ALLOWED_EMAIL_DOMAIN=example.com
    AUTH_REQUIRED=True
    CLIENT_ID=foo
    CLIENT_SECRET=bar

Change an environment variable for running app:

    $ rhc set-env 

Troubleshooting
---------------

To display application information and log files:

    $ rhc show-app alerta

    $ rhc tail alerta


If problems persist, try deleting the app and recreating:

    $ rhc app delete -a alerta

License
-------

Copyright (c) 2015-2016 Nick Satterly. Available under the MIT License.

