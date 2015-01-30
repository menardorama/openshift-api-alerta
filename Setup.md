Alerta API on OpenShift
=======================

    $ git clone git@github.com:alerta/openshift-api-alerta.git
    $ cd openshift-api-alerta
    $ git config --local -e

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = false
[remote "all"]
        url = git@github.com:alerta/openshift-api-alerta.git
        url = ssh://524f1c565973cae4d5000053@api-alerta.rhcloud.com/~/git/api.git/
[remote "origin"]
        url = git@github.com:alerta/openshift-api-alerta.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[remote "openshift"]
        url = ssh://<sha1-hash>@api-alerta.rhcloud.com/~/git/api.git/
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
```

To merge this repo with a new OpenShift repo:

    $ git clone git@github.com:alerta/openshift-api-alerta.git
    $ cd openshift-api-alerta
    $ git remote add openshift ssh://<sha1-hash>@api-alerta.rhcloud.com/~/git/api.git/
    $ git fetch openshift
    $ git merge openshift/master -s recursive -X ours

To deploy following a git repo change:

    $ git pull openshift master
    $ git push
    $ git push openshift

To deploy without a git repo change:
    $ rhc ssh api
    > ctl_app deploy
