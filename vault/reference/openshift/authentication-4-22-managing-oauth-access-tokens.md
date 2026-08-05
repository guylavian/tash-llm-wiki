---
title: "Managing user-owned OAuth access tokens"
type: reference
domain: openshift
slug: authentication-4-22-managing-oauth-access-tokens
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/managing-oauth-access-tokens
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Managing user-owned OAuth access tokens

[id="managing-oauth-access-tokens"]
= Managing user-owned OAuth access tokens

Users can review their own OAuth access tokens and delete any that are no longer needed.

// Listing user-owned OAuth access tokens
// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

[id="oauth-list-tokens_{context}"]
= Listing user-owned OAuth access tokens

You can list your user-owned OAuth access tokens. Token names are not sensitive and cannot be used to log in.

.Procedure

* List all user-owned OAuth access tokens:
+
[source,terminal]
----
$ oc get useroauthaccesstokens
----
+
.Example output
[source,terminal]
----
NAME       CLIENT NAME                    CREATED                EXPIRES                         REDIRECT URI                                                       SCOPES
<token1>   openshift-challenging-client   2021-01-11T19:25:35Z   2021-01-12 19:25:35 +0000 UTC   https://oauth-openshift.apps.example.com/oauth/token/implicit      user:full
<token2>   openshift-browser-client       2021-01-11T19:27:06Z   2021-01-12 19:27:06 +0000 UTC   https://oauth-openshift.apps.example.com/oauth/token/display       user:full
<token3>   console                        2021-01-11T19:26:29Z   2021-01-12 19:26:29 +0000 UTC   https://console-openshift-console.apps.example.com/auth/callback   user:full
----

* List user-owned OAuth access tokens for a particular OAuth client:
+
[source,terminal]
----
$ oc get useroauthaccesstokens --field-selector=clientName="console"
----
+
.Example output
[source,terminal]
----
NAME       CLIENT NAME                    CREATED                EXPIRES                         REDIRECT URI                                                       SCOPES
<token3>   console                        2021-01-11T19:26:29Z   2021-01-12 19:26:29 +0000 UTC   https://console-openshift-console.apps.example.com/auth/callback   user:full
----

// Viewing the details of a user-owned OAuth access token
// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

[id="oauth-view-details-tokens_{context}"]
= Viewing the details of a user-owned OAuth access token

You can view the details of a user-owned OAuth access token.

.Procedure

* Describe the details of a user-owned OAuth access token:
+
[source,terminal]
----
$ oc describe useroauthaccesstokens <token_name>
----
+
.Example output
[source,terminal]
----
Name:                        <token_name> <1>
Namespace:
Labels:                      <none>
Annotations:                 <none>
API Version:                 oauth.openshift.io/v1
Authorize Token:             sha256~Ksckkug-9Fg_RWn_AUysPoIg-_HqmFI9zUL_CgD8wr8
Client Name:                 openshift-browser-client <2>
Expires In:                  86400 <3>
Inactivity Timeout Seconds:  317 <4>
Kind:                        UserOAuthAccessToken
Metadata:
  Creation Timestamp:  2021-01-11T19:27:06Z
  Managed Fields:
    API Version:  oauth.openshift.io/v1
    Fields Type:  FieldsV1
    fieldsV1:
      f:authorizeToken:
      f:clientName:
      f:expiresIn:
      f:redirectURI:
      f:scopes:
      f:userName:
      f:userUID:
    Manager:         oauth-server
    Operation:       Update
    Time:            2021-01-11T19:27:06Z
  Resource Version:  30535
  Self Link:         /apis/oauth.openshift.io/v1/useroauthaccesstokens/<token_name>
  UID:               f9d00b67-ab65-489b-8080-e427fa3c6181
Redirect URI:        https://oauth-openshift.apps.example.com/oauth/token/display
Scopes:
  user:full <5>
User Name:  <user_name> <6>
User UID:   82356ab0-95f9-4fb3-9bc0-10f1d6a6a345
Events:     <none>
----
<1> The token name, which is the sha256 hash of the token. Token names are not sensitive and cannot be used to log in.
<2> The client name, which describes where the token originated from.
<3> The value in seconds from the creation time before this token expires.
<4> If there is a token inactivity timeout set for the OAuth server, this is the value in seconds from the creation time before this token can no longer be used.
<5> The scopes for this token.
<6> The user name associated with this token.

// Deleting user-owned OAuth access tokens
// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

[id="oauth-delete-tokens_{context}"]
= Deleting user-owned OAuth access tokens

The `oc logout` command only invalidates the OAuth token for the active session. You can use the following procedure to delete any user-owned OAuth tokens that are no longer needed.

Deleting an OAuth access token logs out the user from all sessions that use the token.

.Procedure

* Delete the user-owned OAuth access token:
+
[source,terminal]
----
$ oc delete useroauthaccesstokens <token_name>
----
+
.Example output
[source,terminal]
----
useroauthaccesstoken.oauth.openshift.io "<token_name>" deleted
----

// Adding unauthenticated groups to ClusterRoleBindings
// Module included in the following assemblies:
//
// * authentication/impersonating-system-admin.adoc
// * authentication/tokens-scoping.adoc
// * authentication/managing-oauth-access-tokens.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="unauthenticated-users-cluster-role-bindings_{context}"]
= Adding unauthenticated groups to cluster roles

[role="_abstract"]
As a cluster administrator, you can add unauthenticated users to the following cluster roles in OpenShift Container Platform by creating a cluster role binding. Unauthenticated users do not have access to non-public cluster roles. This should only be done in specific use cases when necessary.

You can add unauthenticated users to the following cluster roles:

* `system:scope-impersonation`
* `system:webhook`
* `system:oauth-token-deleter`
* `self-access-reviewer`

[IMPORTANT]
====
Always verify compliance with your organization's security standards when modifying unauthenticated access.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file named `add-<cluster_role>-unauth.yaml` and add the following content:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 annotations:
   rbac.authorization.kubernetes.io/autoupdate: "true"
 name: <cluster_role>access-unauthenticated
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: <cluster_role>
subjects:
 - apiGroup: rbac.authorization.k8s.io
   kind: Group
   name: system:unauthenticated
----
. Apply the configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f add-<cluster_role>.yaml
----
