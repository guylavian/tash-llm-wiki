---
title: "Configuring a request header identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-request-header-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-request-header-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring a request header identity provider

[id="configuring-request-header-identity-provider"]
= Configuring a request header identity provider

Configure the `request-header` identity provider to identify users from request header values, such as `X-Remote-User`. It is typically used in combination with an authenticating proxy, which sets the request header value.

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
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-about-request-header_{context}"]
= About request header authentication

A request header identity provider identifies users from request
header values, such as `X-Remote-User`. It is typically used in combination with
an authenticating proxy, which sets the request header value. The
request header identity provider cannot be combined with other identity providers
that use direct password logins, such as htpasswd, Keystone, LDAP or basic authentication.

[NOTE]
====
You can also use the request header identity provider for advanced configurations
such as the community-supported SAML authentication.
Note that this solution is not supported by Red Hat.
====

For users to authenticate using this identity provider, they must access
`https://_<namespace_route>_/oauth/authorize` (and subpaths) via an authenticating proxy.
To accomplish this, configure the OAuth server to redirect unauthenticated
requests for OAuth tokens to the proxy endpoint that proxies to
`https://_<namespace_route>_/oauth/authorize`.

To redirect unauthenticated requests from clients expecting browser-based login flows:

* Set the `provider.loginURL` parameter to the authenticating proxy URL that
will authenticate interactive clients and then proxy the request to
`https://_<namespace_route>_/oauth/authorize`.

To redirect unauthenticated requests from clients expecting `WWW-Authenticate` challenges:

* Set the `provider.challengeURL` parameter to the authenticating proxy URL that
will authenticate clients expecting `WWW-Authenticate` challenges and then proxy
the request to `https://_<namespace_route>_/oauth/authorize`.

The `provider.challengeURL` and `provider.loginURL` parameters can include
the following tokens in the query portion of the URL:

* `${url}` is replaced with the current URL, escaped to be safe in a query parameter.
+
For example: [x-]`https://www.example.com/sso-login?then=${url}`

* `${query}` is replaced with the current query string, unescaped.
+
For example: [x-]`https://www.example.com/auth-proxy/oauth/authorize?${query}`

[IMPORTANT]
====
As of OpenShift Container Platform 4.1, your proxy must support mutual TLS.
====

[id="sspi-windows_{context}"]
== SSPI connection support on Microsoft Windows

The OpenShift CLI (`oc`) supports the Security Support Provider Interface (SSPI) to allow for SSO
flows on Microsft Windows. If you use the request header identity provider with a
GSSAPI-enabled proxy to connect an Active Directory server to OpenShift Container Platform,
users can automatically authenticate to OpenShift Container Platform by using the `oc`  command
line interface from a domain-joined Microsoft Windows computer.

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
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-request-header-CR_{context}"]
= Sample request header CR

The following custom resource (CR) shows the parameters and
acceptable values for a request header identity provider.

.Request header CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: requestheaderidp <1>
    mappingMethod: claim <2>
    type: RequestHeader
    requestHeader:
      challengeURL: "https://www.example.com/challenging-proxy/oauth/authorize?${query}" <3>
      loginURL: "https://www.example.com/login-proxy/oauth/authorize?${query}" <4>
      ca: <5>
        name: ca-config-map
      clientCommonNames: <6>
      - my-auth-proxy
      headers: <7>
      - X-Remote-User
      - SSO-User
      emailHeaders: <8>
      - X-Remote-User-Email
      nameHeaders: <9>
      - X-Remote-User-Display-Name
      preferredUsernameHeaders: <10>
      - X-Remote-User-Login
----
<1> This provider name is prefixed to the user name in the request header to
form an identity name.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> Optional: URL to redirect unauthenticated `/oauth/authorize` requests to,
that will authenticate browser-based clients and then proxy their request to
`https://_<namespace_route>_/oauth/authorize`.
The URL that proxies to `https://_<namespace_route>_/oauth/authorize` must end with `/authorize` (with no trailing slash),
and also proxy subpaths, in order for OAuth approval flows to work properly.
`${url}` is replaced with the current URL, escaped to be safe in a query parameter.
`${query}` is replaced with the current query string.
If this attribute is not defined, then `loginURL` must be used.
<4> Optional: URL to redirect unauthenticated `/oauth/authorize` requests to,
that will authenticate clients which expect `WWW-Authenticate` challenges, and
then proxy them to `https://_<namespace_route>_/oauth/authorize`.
`${url}` is replaced with the current URL, escaped to be safe in a query parameter.
`${query}` is replaced with the current query string.
If this attribute is not defined, then `challengeURL` must be used.
<5> Reference to an OpenShift Container Platform `ConfigMap` object containing a PEM-encoded
certificate bundle. Used as a trust anchor to validate the TLS
certificates presented by the remote server.
+
[IMPORTANT]
====
As of OpenShift Container Platform 4.1, the `ca` field is required for this identity
provider. This means that your proxy must support mutual TLS.
====
<6> Optional: list of common names (`cn`). If set, a valid client certificate with
a Common Name (`cn`) in the specified list must be presented before the request headers
are checked for user names. If empty, any Common Name is allowed. Can only be used in combination
with `ca`.
<7> Header names to check, in order, for the user identity. The first header containing
a value is used as the identity. Required, case-insensitive.
<8> Header names to check, in order, for an email address. The first header containing
a value is used as the email address. Optional, case-insensitive.
<9> Header names to check, in order, for a display name. The first header containing
a value is used as the display name. Optional, case-insensitive.
<10> Header names to check, in order, for a preferred user name, if different than the immutable
identity determined from the headers specified in `headers`. The first header containing
a value is used as the preferred user name when provisioning. Optional, case-insensitive.

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

[id="example-apache-auth-config-using-request-header"]
== Example Apache authentication configuration using request header

This example configures an Apache authentication proxy for the OpenShift Container Platform
using the request header identity provider.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-apache-custom-proxy-configuration_{context}"]
= Custom proxy configuration

Using the `mod_auth_gssapi` module is a popular way to configure the Apache
authentication proxy using the request header identity provider; however, it is
not required. Other proxies can easily be used if the following requirements are
met:

* Block the `X-Remote-User` header from client requests to prevent spoofing.
* Enforce client certificate authentication in the `RequestHeaderIdentityProvider`
configuration.
* Require the `X-Csrf-Token` header be set for all authentication requests using
the challenge flow.
* Make sure only the `/oauth/authorize` endpoint and its subpaths are proxied;
redirects must be rewritten to allow the backend server to send the client to
the correct location.
* The URL that proxies to `\https://<namespace_route>/oauth/authorize` must end
with `/authorize` with no trailing slash. For example, `\https://proxy.example.com/login-proxy/authorize?...`
must proxy to `\https://<namespace_route>/oauth/authorize?...`.
+
* Subpaths of the URL that proxies to `\https://<namespace_route>/oauth/authorize`
must proxy to subpaths of `\https://<namespace_route>/oauth/authorize`. For
example, `\https://proxy.example.com/login-proxy/authorize/approve?...` must
proxy to `\https://<namespace_route>/oauth/authorize/approve?...`.

[NOTE]
====
The `\https://<namespace_route>` address is the route to the OAuth server and
can be obtained by running `oc get route -n openshift-authentication`.
====

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-configuring-apache-request-header_{context}"]
= Configuring Apache authentication using request header

This example uses the `mod_auth_gssapi` module to configure an Apache
authentication proxy using the request header identity provider.

.Prerequisites

* Obtain the `mod_auth_gssapi` module from the
Optional channel.
You must have the following packages installed on your local machine:
+
** `httpd`
** `mod_ssl`
** `mod_session`
** `apr-util-openssl`
** `mod_auth_gssapi`

* Generate a CA for validating requests that submit the trusted header. Define
an OpenShift Container Platform `ConfigMap` object containing the CA. This is done by running:
+
[source,terminal]
----
$ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config <1>
----
<1> The CA must be stored in the `ca.crt` key of the `ConfigMap` object.
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

* Generate a client certificate for the proxy. You can generate this certificate
by using any x509 certificate tooling. The client certificate must be signed by
the CA you generated for validating requests that submit the trusted header.

* Create the custom resource (CR) for your identity providers.

.Procedure

This proxy uses a client certificate to connect to the OAuth server, which
is configured to trust the `X-Remote-User` header.

. Create the certificate for the Apache configuration. The certificate that you
specify as the `SSLProxyMachineCertificateFile` parameter value is the proxy's
client certificate that is used to authenticate the proxy to the server. It must
use `TLS Web Client Authentication` as the extended key type.

. Create the Apache configuration. Use the following template to provide your
required settings and values:
+
[IMPORTANT]
====
Carefully review the template and customize its contents to fit your
environment.
====
+
----
LoadModule request_module modules/mod_request.so
LoadModule auth_gssapi_module modules/mod_auth_gssapi.so
# Some Apache configurations might require these modules.
# LoadModule auth_form_module modules/mod_auth_form.so
# LoadModule session_module modules/mod_session.so

# Nothing needs to be served over HTTP.  This virtual host simply redirects to
# HTTPS.
<VirtualHost *:80>
  DocumentRoot /var/www/html
  RewriteEngine              On
  RewriteRule     ^(.*)$     https://%{HTTP_HOST}$1 [R,L]
</VirtualHost>

<VirtualHost *:443>
  # This needs to match the certificates you generated.  See the CN and X509v3
  # Subject Alternative Name in the output of:
  # openssl x509 -text -in /etc/pki/tls/certs/localhost.crt
  ServerName www.example.com

  DocumentRoot /var/www/html
  SSLEngine on
  SSLCertificateFile /etc/pki/tls/certs/localhost.crt
  SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
  SSLCACertificateFile /etc/pki/CA/certs/ca.crt

  SSLProxyEngine on
  SSLProxyCACertificateFile /etc/pki/CA/certs/ca.crt
  # It is critical to enforce client certificates. Otherwise, requests can
  # spoof the X-Remote-User header by accessing the /oauth/authorize endpoint
  # directly.
  SSLProxyMachineCertificateFile /etc/pki/tls/certs/authproxy.pem

  # To use the challenging-proxy, an X-Csrf-Token must be present.
  RewriteCond %{REQUEST_URI} ^/challenging-proxy
  RewriteCond %{HTTP:X-Csrf-Token} ^$ [NC]
  RewriteRule ^.* - [F,L]

  <Location /challenging-proxy/oauth/authorize>
      # Insert your backend server name/ip here.
      ProxyPass https://<namespace_route>/oauth/authorize
      AuthName "SSO Login"
      # For Kerberos
      AuthType GSSAPI
      Require valid-user
      RequestHeader set X-Remote-User %{REMOTE_USER}s

      GssapiCredStore keytab:/etc/httpd/protected/auth-proxy.keytab
      # Enable the following if you want to allow users to fallback
      # to password based authentication when they do not have a client
      # configured to perform kerberos authentication.
      GssapiBasicAuth On

      # For ldap:
      # AuthBasicProvider ldap
      # AuthLDAPURL "ldap://ldap.example.com:389/ou=People,dc=my-domain,dc=com?uid?sub?(objectClass=*)"
    </Location>

    <Location /login-proxy/oauth/authorize>
    # Insert your backend server name/ip here.
    ProxyPass https://<namespace_route>/oauth/authorize

      AuthName "SSO Login"
      AuthType GSSAPI
      Require valid-user
      RequestHeader set X-Remote-User %{REMOTE_USER}s env=REMOTE_USER

      GssapiCredStore keytab:/etc/httpd/protected/auth-proxy.keytab
      # Enable the following if you want to allow users to fallback
      # to password based authentication when they do not have a client
      # configured to perform kerberos authentication.
      GssapiBasicAuth On

      ErrorDocument 401 /login.html
    </Location>

</VirtualHost>

RequestHeader unset X-Remote-User
----
+
[NOTE]
====
The `\https://<namespace_route>` address is the route to the OAuth server and
can be obtained by running `oc get route -n openshift-authentication`.
====

. Update the `identityProviders` stanza in the custom resource (CR):
+
[source,yaml]
----
identityProviders:
  - name: requestheaderidp
    type: RequestHeader
    requestHeader:
      challengeURL: "https://<namespace_route>/challenging-proxy/oauth/authorize?${query}"
      loginURL: "https://<namespace_route>/login-proxy/oauth/authorize?${query}"
      ca:
        name: ca-config-map
        clientCommonNames:
        - my-auth-proxy
        headers:
        - X-Remote-User
----

. Verify the configuration.

.. Confirm that you can bypass the proxy by requesting a token by supplying the
correct client certificate and header:
+
[source,terminal]
----
# curl -L -k -H "X-Remote-User: joe" \
   --cert /etc/pki/tls/certs/authproxy.pem \
   https://<namespace_route>/oauth/token/request
----

.. Confirm that requests that do not supply the client certificate fail by
requesting a token without the certificate:
+
[source,terminal]
----
# curl -L -k -H "X-Remote-User: joe" \
   https://<namespace_route>/oauth/token/request
----

.. Confirm that the `challengeURL` redirect is active:
+
[source,terminal]
----
# curl -k -v -H 'X-Csrf-Token: 1' \
   https://<namespace_route>/oauth/authorize?client_id=openshift-challenging-client&response_type=token
----
+
Copy the `challengeURL` redirect to use in the next step.

.. Run this command to show a `401` response with a `WWW-Authenticate` basic
challenge, a negotiate challenge, or both challenges:
+
[source,terminal]
----
# curl -k -v -H 'X-Csrf-Token: 1' \
   <challengeURL_redirect + query>
----

.. Test logging in to the OpenShift CLI (`oc`) with and without using a Kerberos
ticket:
... If you generated a Kerberos ticket by using `kinit`, destroy it:
+
[source,terminal]
----
# kdestroy -c cache_name <1>
----
+
<1> Make sure to provide the name of your Kerberos cache.
... Log in to the `oc` tool by using your Kerberos credentials:
+
[source,terminal]
----
# oc login -u <username>
----
+
Enter your Kerberos password at the prompt.
... Log out of the `oc` tool:
+
[source,terminal]
----
# oc logout
----
... Use your Kerberos credentials to get a ticket:
+
[source,terminal]
----
# kinit
----
+
Enter your Kerberos user name and password at the prompt.
... Confirm that you can log in to the `oc` tool:
+
[source,terminal]
----
# oc login
----
+
If your configuration is correct, you are logged in without entering separate
credentials.
