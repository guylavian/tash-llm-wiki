---
title: "Configuring a GitLab identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-gitlab-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-gitlab-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring a GitLab identity provider

[id="configuring-gitlab-identity-provider"]
= Configuring a GitLab identity provider

Configure the `gitlab` identity provider using GitLab.com or any other GitLab instance as an identity provider.

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
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc

[id="identity-provider-gitlab-about_{context}"]
= About GitLab authentication

Configuring GitLab authentication allows users to log in to OpenShift Container Platform with their GitLab credentials.

If you use GitLab version 7.7.0 to 11.0, you connect using the OAuth integration. If you use GitLab version 11.1 or later, you can use OpenID Connect (OIDC) to connect instead of OAuth.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-creating-secret_{context}"]
= Creating the secret

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

.Procedure

* Create a `Secret` object containing a string by using the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name>
  namespace: openshift-config
type: Opaque
data:
  clientSecret: <base64_encoded_client_secret>
----
====

* You can define a `Secret` object containing the contents of a file by using the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
----

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-creating-configmap_{context}"]
= Creating a config map

Identity providers use OpenShift Container Platform `ConfigMap` objects in the `openshift-config`
namespace to contain the certificate authority bundle. These are primarily
used to contain certificate bundles needed by the identity provider.

[NOTE]
====
This procedure is only required for GitHub Enterprise.
====

.Procedure

* Define an OpenShift Container Platform `ConfigMap` object containing the
certificate authority by using the following command. The certificate
authority must be stored in the `ca.crt` key of the `ConfigMap` object.
+
[source,terminal]
----
$ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the config map:

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: ca-config-map
  namespace: openshift-config
data:
  ca.crt: |
    <CA_certificate_PEM>
----
====

// Undefining attributes

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc

[id="identity-provider-gitlab-CR_{context}"]
= Sample GitLab CR

The following custom resource (CR) shows the parameters and acceptable values for a
GitLab identity provider.

.GitLab CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: gitlabidp <1>
    mappingMethod: claim <2>
    type: GitLab
    gitlab:
      clientID: {...} <3>
      clientSecret: <4>
        name: gitlab-secret
      url: https://gitlab.com <5>
      ca: <6>
        name: ca-config-map
----
<1> This provider name is prefixed to the GitLab numeric user ID to form an
identity name. It is also used to build the callback URL.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> The client ID of a
registered GitLab OAuth application.
The application must be configured with a callback URL of
`\https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.
<4> Reference to an OpenShift Container Platform `Secret` object containing the client secret
issued by GitLab.
<5> The host URL of a GitLab provider. This could either be `\https://gitlab.com/`
or any other self hosted instance of GitLab.
<6> Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the
PEM-encoded certificate authority bundle to use in validating server
certificates for the configured URL.

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
