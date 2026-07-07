---
title: "Configuring an htpasswd identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-htpasswd-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-htpasswd-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring an htpasswd identity provider

[id="configuring-htpasswd-identity-provider"]
= Configuring an htpasswd identity provider

Configure the `htpasswd` identity provider to allow users to log in to OpenShift Container Platform with credentials from an htpasswd file.

To define an htpasswd identity provider, perform the following tasks:

. Create an `htpasswd` file to store the user and password information.
. Create
a secret to represent the `htpasswd` file.
. Define an htpasswd identity provider resource that references the secret.
. Apply the resource to
the default OAuth configuration to add the identity provider.

// Module included in the following assemblies:
//
// * authentication/configuring-identity-provider.adoc
// * authentication/identity_providers/configuring-allow-all-identity-provider.adoc
// * authentication/identity_providers/configuring-deny-all-identity-provider.adoc
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-overview_{context}"]
= About identity providers in OpenShift Container Platform

By default, only a `kubeadmin` user exists on your cluster. To specify an
identity provider, you must create a custom resource (CR) that describes
that identity provider and add it to the cluster.

[NOTE]
====
OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.
====

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-htpasswd-about_{context}"]
= About htpasswd authentication

Using htpasswd authentication in OpenShift Container Platform allows you to identify users based on an htpasswd file. An htpasswd file is a flat file that contains the user name and hashed password for each user. You can use the `htpasswd` utility to create this file.

[WARNING]
====
Do not use htpasswd authentication in OpenShift Container Platform for production environments. Use htpasswd authentication only for development environments.
====

[id="creating-htpasswd-file"]
== Creating the htpasswd file

See one of the following sections for instructions about how to create the htpasswd file:

* Creating an htpasswd file using Linux
* Creating an htpasswd file using Windows

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-creating-htpasswd-file-linux_{context}"]
= Creating an htpasswd file using Linux

To use the htpasswd identity provider, you must generate a flat file that
contains the user names and passwords for your cluster by using
`htpasswd`.

.Prerequisites

* Have access to the `htpasswd` utility. On Red Hat Enterprise Linux
this is available by installing the `httpd-tools` package.

.Procedure

. Create or update your flat file with a user name and hashed password:
+
[source,terminal]
----
$ htpasswd -c -B -b </path/to/users.htpasswd> <username> <password>
----
+
The command generates a hashed version of the password.
+
For example:
+
[source,terminal]
----
$ htpasswd -c -B -b users.htpasswd <username> <password>
----
+
.Example output
[source,terminal]
----
Adding password for user user1
----

. Continue to add or update credentials to the file:
+
[source,terminal]
----
$ htpasswd -B -b </path/to/users.htpasswd> <user_name> <password>
----

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-creating-htpasswd-file-windows_{context}"]
= Creating an htpasswd file using Windows

To use the htpasswd identity provider, you must generate a flat file that
contains the user names and passwords for your cluster by using
`htpasswd`.

.Prerequisites

* Have access to `htpasswd.exe`. This file is included in the `\bin`
directory of many Apache httpd distributions.

.Procedure

. Create or update your flat file with a user name and hashed password:
+
[source,terminal]
----
> htpasswd.exe -c -B -b <\path\to\users.htpasswd> <username> <password>
----
+
The command generates a hashed version of the password.
+
For example:
+
[source,terminal]
----
> htpasswd.exe -c -B -b users.htpasswd <username> <password>
----
+
.Example output
[source,terminal]
----
Adding password for user user1
----

. Continue to add or update credentials to the file:
+
[source,terminal]
----
> htpasswd.exe -b <\path\to\users.htpasswd> <username> <password>
----

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-creating-htpasswd-secret_{context}"]
= Creating the htpasswd secret

To use the htpasswd identity provider, you must define a secret that
contains the htpasswd user file.

.Prerequisites

* Create an htpasswd file.

.Procedure

* Create a `Secret` object that contains the htpasswd users file:
+
[source,terminal]
----
$ oc create secret generic htpass-secret --from-file=htpasswd=<path_to_users.htpasswd> -n openshift-config <1>
----
<1> The secret key containing the users file for the `--from-file` argument must be named `htpasswd`, as shown in the above command.
+
[TIP]
====
You can alternatively apply the following YAML to create the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: htpass-secret
  namespace: openshift-config
type: Opaque
data:
  htpasswd: <base64_encoded_htpasswd_file_contents>
----
====

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-htpasswd-CR_{context}"]
= Sample htpasswd CR

The following custom resource (CR) shows the parameters and acceptable values for an
htpasswd identity provider.

.htpasswd CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_htpasswd_provider <1>
    mappingMethod: claim <2>
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret <3>
----
<1> This provider name is prefixed to provider user names to form an identity
name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> An existing secret containing a file generated using
`htpasswd`.

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See Identity provider parameters for information on parameters, such as `mappingMethod`, that are common to all identity providers.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-allow-all-identity-provider.adoc
// * authentication/identity_providers/configuring-deny-all-identity-provider.adoc
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

// GitHub and Google IDPs do not support username/password login commands
// Only some OIDC IDPs support username/password login commands

[id="add-identity-provider_{context}"]
= Adding an identity provider to your cluster

After you install your cluster, add an identity provider to it so your
users can authenticate.

.Prerequisites

* Create an OpenShift Container Platform cluster.
* Create the custom resource (CR) for your identity providers.
* You must be logged in as an administrator.

.Procedure

. Apply the defined CR:
+
[source,terminal]
----
$ oc apply -f </path/to/CR>
----
+
[NOTE]
====
If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.
====

. Log in to the cluster as a user from your identity provider, entering the
password when prompted.
+
[source,terminal]
----
$ oc login -u <username>
----

. Obtain a token from the OAuth server.
+
As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.
+
You can also access this page from the web console by navigating to *(?) Help* -> *Command Line Tools* -> *Copy Login Command*.

. Log in to the cluster, passing in the token to authenticate.
+
[source,terminal]
----
$ oc login --token=<token>
----
+
[NOTE]
====
If your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, you can log in with a user name and password. You might need to take steps to enable the ROPC grant flow for your identity provider.

After the OIDC identity provider is configured in OpenShift Container Platform, you can log in by using the following command, which prompts for your user name and password:

[source,terminal]
----
$ oc login -u <identity_provider_username> --server=<api_server_url_and_port>
----

This identity provider does not support logging in with a user name and password.
====

. Confirm that the user logged in successfully, and display the user name.
+
[source,terminal]
----
$ oc whoami
----

// Undefining attributes

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc

[id="identity-provider-htpasswd-update-users_{context}"]
= Updating users for an htpasswd identity provider

You can add or remove users from an existing htpasswd identity provider.

.Prerequisites

* You have created a `Secret` object that contains the htpasswd user file. This procedure assumes that it is named `htpass-secret`.
* You have configured an htpasswd identity provider. This procedure assumes that it is named `my_htpasswd_provider`.
* You have access to the `htpasswd` utility. On Red Hat Enterprise Linux this is available by installing the `httpd-tools` package.
* You have cluster administrator privileges.

.Procedure

. Retrieve the htpasswd file from the `htpass-secret` `Secret` object and save the file to your file system:
+
[source,terminal]
----
$ oc get secret htpass-secret -ojsonpath={.data.htpasswd} -n openshift-config | base64 --decode > users.htpasswd
----

. Add or remove users from the `users.htpasswd` file.

** To add a new user:
+
[source,terminal]
----
$ htpasswd -bB users.htpasswd <username> <password>
----
+
.Example output
[source,terminal]
----
Adding password for user <username>
----

** To remove an existing user:
+
[source,terminal]
----
$ htpasswd -D users.htpasswd <username>
----
+
.Example output
[source,terminal]
----
Deleting password for user <username>
----

. Replace the `htpass-secret` `Secret` object with the updated users in the `users.htpasswd` file:
+
[source,terminal]
----
$ oc create secret generic htpass-secret --from-file=htpasswd=users.htpasswd --dry-run=client -o yaml -n openshift-config | oc replace -f -
----
+
[TIP]
====
You can alternatively apply the following YAML to replace the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: htpass-secret
  namespace: openshift-config
type: Opaque
data:
  htpasswd: <base64_encoded_htpasswd_file_contents>
----
====

. If you removed one or more users, you must additionally remove existing resources for each user.

.. Delete the `User` object:
+
[source,terminal]
----
$ oc delete user <username>
----
+
.Example output
[source,terminal]
----
user.user.openshift.io "<username>" deleted
----
+
Be sure to remove the user, otherwise the user can continue using their token as long as it has not expired.

.. Delete the `Identity` object for the user:
+
[source,terminal]
----
$ oc delete identity my_htpasswd_provider:<username>
----
+
.Example output
[source,terminal]
----
identity.user.openshift.io "my_htpasswd_provider:<username>" deleted
----

// Module included in the following assemblies:
//
//* authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
//* authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-configuring-using-the-web-console_{context}"]
= Configuring identity providers using the web console

Configure your identity provider (IDP) through the web console instead of the CLI.

.Prerequisites

* You must be logged in to the web console as a cluster administrator.

.Procedure

. Navigate to *Administration* -> *Cluster Settings*.
. Under the *Configuration* tab, click *OAuth*.
. Under the *Identity Providers* section, select your identity provider from the
*Add* drop-down menu.

[NOTE]
====
You can specify multiple IDPs through the web console without overwriting
existing IDPs.
====
