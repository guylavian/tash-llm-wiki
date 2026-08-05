---
title: "Understanding and creating service accounts"
type: reference
domain: openshift
slug: authentication-4-22-understanding-and-creating-service-accounts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-and-creating-service-accounts
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Understanding and creating service accounts

[id="understanding-and-creating-service-accounts"]
= Understanding and creating service accounts

// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-overview_{context}"]
= Service accounts overview

A service account is an OpenShift Container Platform account that allows a component to
directly access the API. Service accounts are API objects that exist within each project.
Service accounts provide a flexible way to control API
access without sharing a regular user's credentials.

When you use the OpenShift Container Platform CLI or web console, your API token
authenticates you to the API. You can associate a component with a service account
so that they can access the API without using a regular user's credentials.

For example, service accounts can allow:

* Replication controllers to make API calls to create or delete pods
* Applications inside containers to make API calls for discovery purposes
* External applications to make API calls for monitoring or integration purposes

Each service account's user name is derived from its project and name:

[source,text]
----
system:serviceaccount:<project>:<name>
----

Every service account is also a member of two groups:

[cols="1,2",options="header"]
|===

|Group
|Description

|system:serviceaccounts
|Includes all service accounts in the system.

|system:serviceaccounts:<project>
|Includes all service accounts in the
specified project.

|===

// Module included in the following assemblies:
//
// * authentication/using-service-accounts-in-applications.adoc
// * pods/nodes-pods-secrets.adoc

[id="auto-generated-sa-token-secrets_{context}"]
= Automatically generated image pull secrets

[role="_abstract"]
OpenShift Container Platform automatically creates image pull secrets for each service account to integrate the internal image registry with user authentication.

[NOTE]
====
Prior to OpenShift Container Platform 4.16, a long-lived service account API token secret was also generated for each service account that was created. Starting with OpenShift Container Platform 4.16, this service account API token secret is no longer created.

After upgrading to , any existing long-lived service account API token secrets are not deleted and will continue to function. For information about detecting long-lived API tokens that are in use in your cluster or deleting them if they are not needed, see "Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase)".
====

This image pull secret is necessary to integrate the {product-registry} into the cluster's user authentication and authorization system.

However, if you do not enable the `ImageRegistry` capability or if you disable the integrated {product-registry} in the Cluster Image Registry Operator's configuration, an image pull secret is not generated for each service account.

When the integrated {product-registry} is disabled on a cluster that previously had it enabled, the previously generated image pull secrets are deleted automatically.

// include::modules/service-accounts-enabling-authentication.adoc[leveloffset=+1]

// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-managing_{context}"]
= Creating service accounts

You can create a service account in a project and grant it permissions by
binding it to a role.

.Procedure

. Optional: To view the service accounts in the current project:
+
[source,terminal]
----
$ oc get sa
----
+
.Example output
[source,terminal]
----
NAME       SECRETS   AGE
builder    1         2d
default    1         2d
deployer   1         2d
----

. To create a new service account in the current project:
+
[source,terminal]
----
$ oc create sa <service_account_name> <1>
----
<1> To create a service account in a different project, specify `-n <project_name>`.
+
.Example output
[source,terminal]
----
serviceaccount "robot" created
----
+
[TIP]
====
You can alternatively apply the following YAML to create the service account:

[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name>
  namespace: <current_project>
----
====

. Optional: View the secrets for the service account:
+
[source,terminal]
----
$ oc describe sa robot
----
+
.Example output
[source,terminal]
----
Name:                robot
Namespace:           project1
Labels:              <none>
Annotations:         openshift.io/internal-registry-pull-secret-ref: robot-dockercfg-qzbhb
Image pull secrets:  robot-dockercfg-qzbhb
Mountable secrets:   robot-dockercfg-qzbhb
Tokens:              <none>
Events:              <none>
----

// include::modules/service-accounts-configuration-parameters.adoc[leveloffset=+1]

// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-granting-roles_{context}"]
= Granting roles to service accounts

You can grant roles to service accounts in the same way that you grant roles
to a regular user account.

.Procedure

. You can modify the service accounts for the current project. For example, to add
the `view` role to the `robot` service account in the `top-secret` project:
+
[source,terminal]
----
$ oc policy add-role-to-user view system:serviceaccount:top-secret:robot
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: view
  namespace: top-secret
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: view
subjects:
- kind: ServiceAccount
  name: robot
  namespace: top-secret
----
====

. You can also grant access to a specific service account in a project. For
example, from the project to which the service account belongs, use
the `-z` flag and specify the `<service_account_name>`
+
[source,terminal]
----
$ oc policy add-role-to-user <role_name> -z <service_account_name>
----
+
[IMPORTANT]
====
If you want to grant access to a specific service account in a project, use the
`-z` flag. Using this flag helps prevent typos and ensures that access
is granted to only the specified service account.
====
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: <rolebinding_name>
  namespace: <current_project_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: <role_name>
subjects:
- kind: ServiceAccount
  name: <service_account_name>
  namespace: <current_project_name>
----
====

. To modify a different namespace, you can use the `-n` option to indicate the
project namespace it applies to, as shown in the following examples.
+
** For example, to allow all service accounts in all projects to view resources in
the `my-project` project:
+
[source,terminal]
----
$ oc policy add-role-to-group view system:serviceaccounts -n my-project
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: view
  namespace: my-project
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: view
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:serviceaccounts
----
====
+
** To allow all service accounts in the `managers` project to edit resources in the
`my-project` project:
+
[source,terminal]
----
$ oc policy add-role-to-group edit system:serviceaccounts:managers -n my-project
----
+
[TIP]
====
You can alternatively apply the following YAML to add the role:

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: edit
  namespace: my-project
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: edit
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:serviceaccounts:managers
----
====
