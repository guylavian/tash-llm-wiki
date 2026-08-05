---
title: "Configuring a basic authentication identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-basic-authentication-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-basic-authentication-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring a basic authentication identity provider

[id="configuring-basic-authentication-identity-provider"]
= Configuring a basic authentication identity provider

Configure the `basic-authentication` identity provider for users to log in to OpenShift Container Platform with credentials validated against a remote identity provider. Basic authentication is a generic back-end integration mechanism.

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
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc

[id="identity-provider-about-basic-authentication_{context}"]
= About basic authentication

Basic authentication is a generic back-end integration mechanism that allows
users to log in to OpenShift Container Platform with credentials validated against a remote
identity provider.

Because basic authentication is generic, you can use this identity
provider for advanced authentication configurations.

[IMPORTANT]
====
Basic authentication must use an HTTPS connection to the remote server to
prevent potential snooping of the user ID and password and man-in-the-middle
attacks.
====

With basic authentication configured, users send their user name
and password to OpenShift Container Platform, which then validates those credentials against
a remote server by making a server-to-server request, passing the credentials as
a basic authentication header. This requires users to send their credentials to
OpenShift Container Platform during login.

[NOTE]
====
This only works for user name/password login mechanisms, and OpenShift Container Platform must
be able to make network requests to the remote authentication server.
====

User names and passwords are validated against a remote URL that is protected
by basic authentication and returns JSON.

A `401` response indicates failed authentication.

A non-`200` status, or the presence of a non-empty "error" key, indicates an
error:

[source,terminal]
----
{"error":"Error message"}
----

A `200` status with a `sub` (subject) key indicates success:

[source,terminal]
----
{"sub":"userid"} <1>
----
<1> The subject must be unique to the authenticated user and must not be able to
be modified.

A successful response can optionally provide additional data, such as:

* A display name using the `name` key. For example:
+
[source,terminal]
----
{"sub":"userid", "name": "User Name", ...}
----
+
* An email address using the `email` key. For example:
+
[source,terminal]
----
{"sub":"userid", "email":"user@example.com", ...}
----
+
* A preferred user name using the `preferred_username` key. This is useful when
the unique, unchangeable subject is a database key or UID, and a more
human-readable name exists. This is used as a hint when provisioning the
OpenShift Container Platform user for the authenticated identity. For example:
+
[source,terminal]
----
{"sub":"014fbff9a07c", "preferred_username":"bob", ...}
----

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
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc

[id="identity-provider-basic-authentication-CR_{context}"]
= Sample basic authentication CR

The following custom resource (CR) shows the parameters and acceptable values for a
basic authentication identity provider.

.Basic authentication CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: basicidp <1>
    mappingMethod: claim <2>
    type: BasicAuth
    basicAuth:
      url: https://www.example.com/remote-idp <3>
      ca: <4>
        name: ca-config-map
      tlsClientCert: <5>
        name: client-cert-secret
      tlsClientKey: <6>
        name: client-key-secret
----
<1> This provider name is prefixed to the returned user ID to form an identity
name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> URL accepting credentials in Basic authentication headers.
<4> Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the
PEM-encoded certificate authority bundle to use in validating server
certificates for the configured URL.
<5> Optional: Reference to an OpenShift Container Platform `Secret` object containing the client
certificate to present when making requests to the configured URL.
<6> Reference to an OpenShift Container Platform `Secret` object containing the key for the
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

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc

[id="example-apache-httpd-configuration_{context}"]
= Example Apache HTTPD configuration for basic identity providers

The basic identify provider (IDP) configuration in OpenShift Container Platform 4 requires
that the IDP server respond with JSON for success and failures. You can use CGI
scripting in Apache HTTPD to accomplish this. This section provides examples.

.Example `/etc/httpd/conf.d/login.conf`
----
<VirtualHost *:443>
  # CGI Scripts in here
  DocumentRoot /var/www/cgi-bin

  # SSL Directives
  SSLEngine on
  SSLCipherSuite PROFILE=SYSTEM
  SSLProxyCipherSuite PROFILE=SYSTEM
  SSLCertificateFile /etc/pki/tls/certs/localhost.crt
  SSLCertificateKeyFile /etc/pki/tls/private/localhost.key

  # Configure HTTPD to execute scripts
  ScriptAlias /basic /var/www/cgi-bin

  # Handles a failed login attempt
  ErrorDocument 401 /basic/fail.cgi

  # Handles authentication
  <Location /basic/login.cgi>
    AuthType Basic
    AuthName "Please Log In"
    AuthBasicProvider file
    AuthUserFile /etc/httpd/conf/passwords
    Require valid-user
  </Location>
</VirtualHost>
----

.Example `/var/www/cgi-bin/login.cgi`
----
#!/bin/bash
echo "Content-Type: application/json"
echo ""
echo '{"sub":"userid", "name":"'$REMOTE_USER'"}'
exit 0
----

.Example `/var/www/cgi-bin/fail.cgi`
----
#!/bin/bash
echo "Content-Type: application/json"
echo ""
echo '{"error": "Login failure"}'
exit 0
----

== File requirements

These are the requirements for the files you create on an Apache HTTPD web
server:

* `login.cgi` and `fail.cgi` must be executable (`chmod +x`).
* `login.cgi` and `fail.cgi` must have proper SELinux contexts if SELinux is
enabled: `restorecon -RFv /var/www/cgi-bin`, or ensure that the context is
`httpd_sys_script_exec_t` using `ls -laZ`.
* `login.cgi` is only executed if your user successfully logs in per `Require
and Auth` directives.
* `fail.cgi` is executed if the user fails to log in, resulting in an `HTTP 401`
response.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc

[id="identity-provider-basic-authentication-troubleshooting_{context}"]
= Basic authentication troubleshooting

The most common issue relates to network connectivity to the backend server. For
simple debugging, run `curl` commands on the master. To test for a successful
login, replace the `<user>` and `<password>` in the following example command
with valid credentials. To test an invalid login, replace them with false
credentials.

[source,terminal]
----
$ curl --cacert /path/to/ca.crt --cert /path/to/client.crt --key /path/to/client.key -u <user>:<password> -v https://www.example.com/remote-idp
----

*Successful responses*

A `200` status with a `sub` (subject) key indicates success:

[source,terminal]
----
{"sub":"userid"}
----
The subject must be unique to the authenticated user, and must not be able to
be modified.

A successful response can optionally provide additional data, such as:

* A display name using the `name` key:
+
[source,terminal]
----
{"sub":"userid", "name": "User Name", ...}
----
* An email address using the `email` key:
+
[source,terminal]
----
{"sub":"userid", "email":"user@example.com", ...}
----
* A preferred user name using the `preferred_username` key:
+
[source,terminal]
----
{"sub":"014fbff9a07c", "preferred_username":"bob", ...}
----
+
The `preferred_username` key is useful when
the unique, unchangeable subject is a database key or UID, and a more
human-readable name exists. This is used as a hint when provisioning the
OpenShift Container Platform user for the authenticated identity.

*Failed responses*

- A `401` response indicates failed authentication.
- A non-`200` status or the presence of a non-empty "error" key indicates an
error: `{"error":"Error message"}`
