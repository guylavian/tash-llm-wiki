---
title: "Scoping tokens"
type: reference
domain: openshift
slug: authentication-4-22-tokens-scoping
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/tokens-scoping
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Scoping tokens

[id="tokens-scoping"]
= Scoping tokens

[role="_abstract"]
You can create scoped tokens to delegate specific permissions to users or service accounts, and configure cluster role bindings for unauthenticated users when required.

// Module included in the following assemblies:
//
// * authentication/tokens-scoping.adoc

[id="tokens-scoping-about_{context}"]
= About scoping tokens

[role="_abstract"]
You can create scoped tokens to delegate some of your permissions to another
user or service account. For example, a project administrator might want to delegate the
power to create pods.

A scoped token is a token that identifies as a given user but is limited to
certain actions by its scope.
Only a user with the `cluster-admin` role can create scoped tokens.
Only a user with the `dedicated-admin` role can create scoped tokens.

Scopes are evaluated by converting the set of scopes for a token into a set of
`PolicyRules`. Then, the request is matched against those rules. The request
attributes must match at least one of the scope rules to be passed to the
"normal" authorizer for further authorization checks.

[id="scoping-tokens-user-scopes_{context}"]
== User scopes

User scopes are focused on getting information about a given user. They are
intent-based, so the rules are automatically created for you:

* `user:full` - Allows full read/write access to the API with all of the user's permissions.
* `user:info` - Allows read-only access to information about the user, such as name and groups.
* `user:check-access` - Allows access to `self-localsubjectaccessreviews` and `self-subjectaccessreviews`.
    These are the variables where you pass an empty user and groups in your request object.
* `user:list-projects` - Allows read-only access to list the projects the user has access to.

[id="scoping-tokens-role-scope_{context}"]
== Role scope
The role scope allows you to have the same level of access as a given role
filtered by namespace.

* `role:<cluster-role name>:<namespace or * for all>` - Limits the scope to the
rules specified by the cluster-role, but only in the specified namespace .
+
[NOTE]
====
Caveat: This prevents escalating access. Even if the role allows access to
resources like secrets, rolebindings, and roles, this scope will deny access
to those resources. This helps prevent unexpected escalations. Many people do
not think of a role like `edit` as being an escalating role, but with access to
a secret it is.
====

* `role:<cluster-role name>:<namespace or * for all>:!` -  This is similar to the
example above, except that including the bang causes this scope to allow
escalating access.

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
