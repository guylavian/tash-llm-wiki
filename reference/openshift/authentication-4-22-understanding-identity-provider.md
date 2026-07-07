---
title: "Understanding identity provider configuration"
type: reference
domain: openshift
slug: authentication-4-22-understanding-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Understanding identity provider configuration

[id="understanding-identity-provider"]
= Understanding identity provider configuration

The OpenShift Container Platform master includes a built-in OAuth server. Developers and
administrators obtain OAuth access tokens to authenticate themselves to the API.

As an administrator, you can configure OAuth to specify an identity provider
after you install your cluster.

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

[id="supported-identity-providers"]
== Supported identity providers

You can configure the following types of identity providers:

[cols="2a,8a",options="header"]
|===

|Identity provider
|Description

|htpasswd
|Configure the `htpasswd` identity provider to validate user names and passwords
against a flat file generated using
`htpasswd`.

|Keystone
|Configure the `keystone` identity provider to integrate
your OpenShift Container Platform cluster with Keystone to enable shared authentication with
an OpenStack Keystone v3 server configured to store users in an internal
database.

|LDAP
|Configure the `ldap` identity provider to validate user names and passwords
against an LDAPv3 server, using simple bind authentication.

|Basic authentication
|Configure a `basic-authentication` identity provider for users to log in to
OpenShift Container Platform with credentials validated against a remote identity provider.
Basic authentication is a generic backend integration mechanism.

|Request header
|Configure a `request-header` identity provider to identify users from request
header values, such as `X-Remote-User`. It is typically used in combination with
an authenticating proxy, which sets the request header value.

|GitHub or GitHub Enterprise
|Configure a `github` identity provider to validate user names and passwords
against GitHub or GitHub Enterprise's OAuth authentication server.

|GitLab
|Configure a `gitlab` identity provider to use
GitLab.com or any other GitLab instance as an identity
provider.

|Google
|Configure a `google` identity provider using
Google's OpenID Connect integration.

|OpenID Connect
|Configure an `oidc` identity provider to integrate with an OpenID Connect
identity provider using an
Authorization Code Flow.

|===

Once an identity provider has been defined, you can
use RBAC to define and apply permissions.

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

// Module included in the following assemblies:
//
// * authentication/understanding-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-parameters_{context}"]
= Identity provider parameters

[role="_abstract"]
The following parameters are common to all identity providers:

[cols="2a,8a",options="header"]
|===
|Parameter     | Description
|`name`      | The provider name is prefixed to provider user names to form an
identity name.

|`mappingMethod`  | Defines how new identities are mapped to users when they log in.
Enter one of the following values:

claim:: The default value. Provisions a user with the identity's preferred
user name. Fails if a user with that user name is already mapped to another
identity.
lookup:: Looks up an existing identity, user identity mapping, and user,
but does not automatically provision users or identities. This allows cluster
administrators to set up identities and users manually, or using an external
process. Using this method requires you to manually provision users.
add:: Provisions a user with the identity's preferred user name. If a user
with that user name already exists, the identity is mapped to the existing user,
adding to any existing identity mappings for the user. Required when multiple
identity providers are configured that identify the same set of users and map to
the same user names.
|===

[NOTE]
When adding or changing identity providers, you can map identities from the new
provider to existing users by setting the `mappingMethod` parameter to
`add`.

// Module included in the following assemblies:
//
// * authentication/understanding-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-default-CR_{context}"]
= Sample identity provider CR

The following custom resource (CR) shows the parameters and default
values that you use to configure an identity provider. This example
uses the htpasswd identity provider.

.Sample identity provider CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider <1>
    mappingMethod: claim <2>
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret <3>
----
<1> This provider name is prefixed to provider user names to form an
identity name.
<2> Controls how mappings are established between this provider's
identities and `User` objects.
<3> An existing secret containing a file generated using
`htpasswd`.

// Module included in the following assemblies:
//
// * authentication/understanding-identity-provider.adoc

[id="identity-provider-provisioning-user-lookup-mapping_{context}"]
= Manually provisioning a user when using the lookup mapping method

Typically, identities are automatically mapped to users during login. The `lookup` mapping method disables this automatic mapping, which requires you to provision users manually. If you are using the `lookup` mapping method, use the following procedure for each user after configuring the identity provider.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Create an OpenShift Container Platform user:
+
[source,terminal]
----
$ oc create user <username>
----

. Create an OpenShift Container Platform identity:
+
[source,terminal]
----
$ oc create identity <identity_provider>:<identity_provider_user_id>
----
+
Where `<identity_provider_user_id>` is a name that uniquely represents the user in the identity provider.

. Create a user identity mapping for the created user and identity:
+
[source,terminal]
----
$ oc create useridentitymapping <identity_provider>:<identity_provider_user_id> <username>
----

[role="_additional-resources"]
.Additional resources
* How to create user, identity and map user and identity in LDAP authentication for `mappingMethod` as `lookup` inside the OAuth manifest
* How to create user, identity and map user and identity in OIDC authentication for `mappingMethod` as `lookup`
