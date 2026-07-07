---
title: "Configuring a Keystone identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-keystone-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-keystone-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring a Keystone identity provider

[id="configuring-keystone-identity-provider"]
= Configuring a Keystone identity provider

Configure the `keystone` identity provider to integrate your OpenShift Container Platform cluster with Keystone to enable shared authentication with an OpenStack Keystone v3 server configured to store users in an internal database. This configuration allows users to log in to OpenShift Container Platform with their Keystone credentials.

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
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc

[id="identity-provider-keystone-about_{context}"]
= About Keystone authentication

Keystone is an OpenStack project that provides identity, token, catalog, and policy services.

You can configure the integration with Keystone so that the new OpenShift Container Platform users are based on either the Keystone user names or unique Keystone IDs. With both methods, users log in by entering their Keystone user name and password. Basing the OpenShift Container Platform users on the Keystone ID is more secure because if you delete a Keystone user and create a new Keystone user with that user name, the new user might have access to the old user's resources.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc

[id="identity-provider-creating-secret-tls_{context}"]
= Creating the secret

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

.Procedure

* Create a `Secret` object that contains the key and certificate by using the following command:
+
[source,terminal]
----
$ oc create secret tls <secret_name> --key=key.pem --cert=cert.pem -n openshift-config
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
type: kubernetes.io/tls
data:
  tls.crt: <base64_encoded_cert>
  tls.key: <base64_encoded_key>
----
====

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
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc

[id="identity-provider-keystone-CR_{context}"]
= Sample Keystone CR

The following custom resource (CR) shows the parameters and acceptable values for a
Keystone identity provider.

.Keystone CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: keystoneidp <1>
    mappingMethod: claim <2>
    type: Keystone
    keystone:
      domainName: default <3>
      url: https://keystone.example.com:5000 <4>
      ca: <5>
        name: ca-config-map
      tlsClientCert: <6>
        name: client-cert-secret
      tlsClientKey: <7>
        name: client-key-secret
----
<1> This provider name is prefixed to provider user names to form an identity name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> Keystone domain name. In Keystone, usernames are domain-specific. Only a single domain is supported.
<4> The URL to use to connect to the Keystone server (required). This must
use https.
<5> Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the
PEM-encoded certificate authority bundle to use in validating server
certificates for the configured URL.
<6> Optional: Reference to an OpenShift Container Platform `Secret` object containing the client
certificate to present when making requests to the configured URL.
<7> Reference to an OpenShift Container Platform `Secret` object containing the key for the
client certificate. Required if `tlsClientCert` is specified.

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
