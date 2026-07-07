---
title: "Removing the kubeadmin user"
type: reference
domain: openshift
slug: authentication-4-22-remove-kubeadmin
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/remove-kubeadmin
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Removing the kubeadmin user

[id="removing-kubeadmin"]
= Removing the kubeadmin user

// Module included in the following assemblies:
//
// * authentication/removing-kubeadmin.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="understanding-kubeadmin_{context}"]
= The kubeadmin user

OpenShift Container Platform creates a cluster administrator, `kubeadmin`, after the
installation process completes.

This user has the `cluster-admin` role automatically applied and is treated
as the root user for the cluster. The password is dynamically generated
and unique to your OpenShift Container Platform environment. After installation
completes the password is provided in the installation program's output.
For example:

[source,terminal]
----
INFO Install complete!
INFO Run 'export KUBECONFIG=<your working directory>/auth/kubeconfig' to manage the cluster with 'oc', the OpenShift CLI.
INFO The cluster is ready when 'oc login -u kubeadmin -p <provided>' succeeds (wait a few minutes).
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.demo1.openshift4-beta-abcorp.com
INFO Login to the console with user: kubeadmin, password: <provided>
----

// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc
// * authentication/understanding-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="removing-kubeadmin_{context}"]
= Removing the kubeadmin user

After you define an identity provider and create a new `cluster-admin`
user, you can remove the `kubeadmin` to improve cluster security.

[WARNING]
====
If you follow this procedure before another user is a `cluster-admin`,
then OpenShift Container Platform must be reinstalled. It is not possible to undo
this command.
====

.Prerequisites

* You must have configured at least one identity provider.
* You must have added the `cluster-admin` role to a user.
* You must be logged in as an administrator.

.Procedure

* Remove the `kubeadmin` secrets:
+
[source,terminal]
----
$ oc delete secrets kubeadmin -n kube-system
----
