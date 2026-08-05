---
title: "Configuring an LDAP identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-ldap-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-ldap-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring an LDAP identity provider

[id="configuring-ldap-identity-provider"]
= Configuring an LDAP identity provider

Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication.

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
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc

[id="identity-provider-about-ldap_{context}"]
= About LDAP authentication

During authentication, the LDAP directory is searched for an entry that matches
the provided user name. If a single unique match is found, a simple bind is
attempted using the distinguished name (DN) of the entry plus the provided
password.

These are the steps taken:

. Generate a search filter by combining the attribute and filter in the
configured `url` with the user-provided user name.
. Search the directory using the generated filter. If the search does not return
exactly one entry, deny access.
. Attempt to bind to the LDAP server using the DN of the entry retrieved from
the search, and the user-provided password.
. If the bind is unsuccessful, deny access.
. If the bind is successful, build an identity using the configured attributes
as the identity, email address, display name, and preferred user name.

The configured `url` is an RFC 2255 URL, which specifies the LDAP host and
search parameters to use. The syntax of the URL is:

----
ldap://host:port/basedn?attribute?scope?filter
----

For this URL:

[cols="2a,8a",options="header"]
|===
|URL component | Description
.^|`ldap`      | For regular LDAP, use the string `ldap`. For secure LDAP
(LDAPS), use `ldaps` instead.
.^|`host:port` | The name and port of the LDAP server. Defaults to
`localhost:389` for ldap and `localhost:636` for LDAPS.
.^|`basedn`    | The DN of the branch of the directory where all searches should
start from. At the very least, this must be the top of your directory tree, but
it could also specify a subtree in the directory.
.^|`attribute` | The attribute to search for. Although RFC 2255 allows a
comma-separated list of attributes, only the first attribute will be used, no
matter how many are provided. If no attributes are provided, the default is to
use `uid`. It is recommended to choose an attribute that will be unique across
all entries in the subtree you will be using.
.^|`scope`     | The scope of the search. Can be either `one` or `sub`.
If the scope is not provided, the default is to use a scope of `sub`.
.^|`filter`    | A valid LDAP search filter. If not provided, defaults to
`(objectClass=*)`
|===

When doing searches, the attribute, filter, and provided user name are combined
to create a search filter that looks like:

----
(&(<filter>)(<attribute>=<username>))
----

For example, consider a URL of:

----
ldap://ldap.example.com/o=Acme?cn?sub?(enabled=true)
----

When a client attempts to connect using a user name of `bob`, the resulting
search filter will be `(&(enabled=true)(cn=bob))`.

If the LDAP directory requires authentication to search, specify a `bindDN` and
`bindPassword` to use to perform the entry search.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc

[id="identity-provider-creating-ldap-secret_{context}"]
= Creating the LDAP secret

To use the identity provider, you must define an OpenShift Container Platform `Secret` object that contains the `bindPassword` field.

.Procedure

* Create a `Secret` object that contains the `bindPassword` field:
+
[source,terminal]
----
$ oc create secret generic ldap-secret --from-literal=bindPassword=<secret> -n openshift-config <1>
----
<1> The secret key containing the bindPassword for the `--from-literal` argument must be called `bindPassword`.
+
[TIP]
====
You can alternatively apply the following YAML to create the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: ldap-secret
  namespace: openshift-config
type: Opaque
data:
  bindPassword: <base64_encoded_bind_password>
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
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc

[id="identity-provider-ldap-CR_{context}"]
= Sample LDAP CR

The following custom resource (CR) shows the parameters and acceptable values for an
LDAP identity provider.

.LDAP CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: ldapidp <1>
    mappingMethod: claim <2>
    type: LDAP
    ldap:
      attributes:
        id: <3>
        - dn
        email: <4>
        - mail
        name: <5>
        - cn
        preferredUsername: <6>
        - uid
      bindDN: "" <7>
      bindPassword: <8>
        name: ldap-secret
      ca: <9>
        name: ca-config-map
      insecure: false <10>
      url: "ldaps://ldaps.example.com/ou=users,dc=acme,dc=com?uid" <11>
----
<1> This provider name is prefixed to the returned user ID to form an identity
name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> List of attributes to use as the identity. First non-empty attribute is
used. At least one attribute is required. If none of the listed attribute
have a value, authentication fails. Defined attributes are retrieved as raw,
allowing for binary values to be used.
<4> List of attributes to use as the email address. First non-empty
attribute is used.
<5> List of attributes to use as the display name. First non-empty
attribute is used.
<6> List of attributes to use as the preferred user name when provisioning a
user for this identity. First non-empty attribute is used.
<7> Optional DN to use to bind during the search phase. Must be set if
`bindPassword` is defined.
<8> Optional reference to an OpenShift Container Platform `Secret` object containing the bind
password. Must be set if `bindDN` is defined.
<9> Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the
PEM-encoded certificate authority bundle to use in validating server
certificates for the configured URL. Only used when `insecure` is `false`.
<10> When `true`, no TLS connection is made to the server. When `false`,
`ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to TLS.
This must be set to `false` when `ldaps://` URLs are in use, as these
URLs always attempt to connect using TLS.
<11> An RFC 2255 URL which specifies the LDAP host and search parameters to use.

[NOTE]
====
To whitelist users for an LDAP integration, use the `lookup` mapping method.
Before a login from LDAP would be allowed, a cluster administrator must create
an `Identity` object and a `User` object for each LDAP user.
====

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
