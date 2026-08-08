---
title: "Configuring OAuth clients"
type: reference
domain: openshift
slug: authentication-4-22-configuring-oauth-clients
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-oauth-clients
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring OAuth clients

[id="configuring-oauth-clients"]
= Configuring OAuth clients

[role="_abstract"]
OpenShift Container Platform includes default OAuth clients for platform authentication. You can register additional OAuth clients to integrate third-party applications and configure token inactivity timeouts to enhance security.

// Default OAuth clients
// Module included in the following assemblies:
//
// * authentication/configuring-oauth-clients.adoc

[id="oauth-default-clients_{context}"]
= Default OAuth clients

[role="_abstract"]
OpenShift Container Platform automatically creates OAuth clients for browser-based logins, CLI authentication, and challenge-based authentication when the API starts.

The following OAuth clients are created:

[cols="2,3",options="header"]
|===

|OAuth client |Usage

|`openshift-browser-client`
|Requests tokens at `<namespace_route>/oauth/token/request` with a user-agent that can handle interactive logins.

|`openshift-challenging-client`
|Requests tokens with a user-agent that can handle `WWW-Authenticate` challenges.

|`openshift-cli-client`
|Requests tokens by using a local HTTP server fetching an authorization code grant.

|===

where:

`<namespace_route>`:: Specifies the namespace route. Find this value by running the following command:
+
[source,terminal]
----
$ oc get route oauth-openshift -n openshift-authentication -o json | jq .spec.host
----

// Register an additional OAuth client
// Module included in the following assemblies:
//
// * authentication/configuring-oauth-clients.adoc

[id="oauth-register-additional-client_{context}"]
= Registering an additional OAuth client

[role="_abstract"]
Register additional OAuth clients to manage authentication for applications that need to interact with your OpenShift Container Platform cluster.

.Procedure

* To register additional OAuth clients:
+
[source,terminal]
----
$ oc create -f <(echo '
kind: OAuthClient
apiVersion: oauth.openshift.io/v1
metadata:
 name: demo
secret: "..."
redirectURIs:
 - "http://www.example.com/"
grantMethod: prompt
')
----
+
where:

`metadata.name`:: Specifies the OAuth client name. This value is used as the `client_id` parameter when making requests to `<namespace_route>/oauth/authorize` and `<namespace_route>/oauth/token`.
`secret`:: Specifies the secret value used as the `client_secret` parameter when making requests to `<namespace_route>/oauth/token`.
`redirectURIs`:: Specifies the list of valid redirect URIs. The `redirect_uri` parameter specified in requests to `<namespace_route>/oauth/authorize` and `<namespace_route>/oauth/token` must be equal to or prefixed by one of these URIs.
`grantMethod`:: Specifies the action to take when this client requests tokens and has not yet been granted access by the user. Use `auto` to automatically approve the grant and retry the request, or `prompt` to prompt the user to approve or deny the grant.

// Configuring token inactivity timeout for OAuth clients
// Module included in the following assemblies:
//
// * authentication/configuring-oauth-clients.adoc

[id="oauth-token-inactivity-timeout_{context}"]
= Configuring token inactivity timeout for an OAuth client

[role="_abstract"]
Configure OAuth clients to expire tokens after a set period of inactivity, improving security by automatically invalidating idle sessions.

By default, no token inactivity timeout is set.

[NOTE]
====
If the token inactivity timeout is also configured in the internal OAuth server configuration, the timeout that is set in the OAuth client overrides that value.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have configured an identity provider (IDP).

.Procedure

* Update the `OAuthClient` configuration to set a token inactivity timeout.

.. Edit the `OAuthClient` object:
+
[source,terminal]
----
$ oc edit oauthclient <oauth_client>
----
+
Replace `<oauth_client>` with the OAuth client to configure, for example, `console`.
+
Add the `accessTokenInactivityTimeoutSeconds` field and set your timeout value:
+
[source,yaml]
----
apiVersion: oauth.openshift.io/v1
grantMethod: auto
kind: OAuthClient
metadata:
...
accessTokenInactivityTimeoutSeconds: 600
----
+
where:

`accessTokenInactivityTimeoutSeconds`:: Specifies the token inactivity timeout in seconds. The minimum allowed value is `300`.

.. Save the file to apply the changes.

.Verification

. Log in to the cluster with an identity from your IDP. Be sure to use the OAuth client that you just configured.

. Perform an action and verify that it was successful.

. Wait longer than the configured timeout without using the identity. In this procedure's example, wait longer than 600 seconds.

. Try to perform an action from the same identity's session.
+
This attempt should fail because the token should have expired due to inactivity longer than the configured timeout.

[role="_additional-resources"]
== Additional resources

* OAuthClient [oauth.openshift.io/v1]
