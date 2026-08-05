---
title: "Configuring role-based permissions"
type: reference
domain: openshift
slug: ai-workloads-4-22-rbac-permissions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/rbac-permissions
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Configuring role-based permissions

[id="rbac-permissions"]
= Configuring role-based permissions

The following procedures provide information about how you can configure role-based access control (RBAC) for your {kueue-name} deployment. These RBAC permissions determine which types of users can create which types of {kueue-name} objects.

[id="authentication-clusterroles"]
== Cluster roles

The {kueue-name} Operator deploys `kueue-batch-admin-role` and `kueue-batch-user-role` cluster roles by default.

kueue-batch-admin-role:: This cluster role includes the permissions to manage cluster queues, local queues, workloads, and resource flavors.
kueue-batch-user-role:: This cluster role includes the permissions to manage jobs and to view local queues and workloads.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/rbac-permissions.adoc

[id="configure-rbac-batch-admins_{context}"]
= Configuring permissions for batch administrators

You can configure permissions for batch administrators by binding the `kueue-batch-admin-role` cluster role to a user or group of users.

.Prerequisites

.Procedure

. Create a `ClusterRoleBinding` object as a YAML file:
+
.Example `ClusterRoleBinding` object
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kueue-admins <1>
subjects: <2>
- kind: User
  name: admin@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef: <3>
  kind: ClusterRole
  name: kueue-batch-admin-role
  apiGroup: rbac.authorization.k8s.io
----
<1> Provide a name for the `ClusterRoleBinding` object.
<2> Add details about which user or group of users you want to provide user permissions for.
<3> Add details about the `kueue-batch-admin-role` cluster role.

. Apply the `ClusterRoleBinding` object:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

* You can verify that the `ClusterRoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-admin-role` cluster role:
+
[source,yaml]
----
$ oc describe clusterrolebinding.rbac
----
+
.Example output
[source,terminal]
----
...
Name:         kueue-batch-admin-role
Labels:       app.kubernetes.io/name=kueue
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  kueue-batch-admin-role
Subjects:
  Kind            Name                      Namespace
  ----            ----                      ---------
  User            admin@example.com         admin-namespace
...
----

// Module included in the following assemblies:
//
// * ai_workloads/kueue/rbac-permissions.adoc

[id="configure-rbac-batch-users_{context}"]
= Configuring permissions for users

You can configure permissions for {kueue-name} users by binding the `kueue-batch-user-role` cluster role to a user or group of users.

.Prerequisites

.Procedure

. Create a `RoleBinding` object as a YAML file:
+
.Example `ClusterRoleBinding` object
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: kueue-users <1>
  namespace: user-namespace <2>
subjects: <3>
- kind: Group
  name: team-a@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef: <4>
  kind: ClusterRole
  name: kueue-batch-user-role
  apiGroup: rbac.authorization.k8s.io

----
<1> Provide a name for the `RoleBinding` object.
<2> Add details about which namespace the `RoleBinding` object applies to.
<3> Add details about which user or group of users you want to provide user permissions for.
<4> Add details about the `kueue-batch-user-role` cluster role.

. Apply the `RoleBinding` object:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

* You can verify that the `RoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-user-role` cluster role:
+
[source,yaml]
----
$ oc describe rolebinding.rbac
----
+
.Example output
[source,terminal]
----
...
Name:         kueue-users
Labels:       app.kubernetes.io/name=kueue
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  kueue-batch-user-role
Subjects:
  Kind            Name                      Namespace
  ----            ----                      ---------
  Group           team-a@example.com        user-namespace
...
----

[role="_additional-resources"]
== Additional resources
* Using RBAC to define and apply permissions
* Glossary of common terms for OpenShift Container Platform authentication and authorization
