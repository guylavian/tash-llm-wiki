---
title: "User access to extension resources"
type: reference
domain: openshift
slug: extensions-4-22-user-access-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/user-access-resources
version: 4.22
family: extensions
documentKind: "Documentation"
---

# User access to extension resources

[id="user-access-resources"]
= User access to extension resources

After a cluster extension has been installed and is being managed by {olmv1-first}, the extension can often provide `CustomResourceDefinition` objects (CRDs) that expose new API resources on the cluster. Cluster administrators typically have full management access to these resources by default, whereas non-cluster administrator users, or _regular users_, might lack sufficient permissions.

{olmv1} does not automatically configure or manage role-based access control (RBAC) for regular users to interact with the APIs provided by installed extensions. Cluster administrators must define the required RBAC policy to create, view, or edit these custom resources (CRs) for such users.

[NOTE]
====
The RBAC permissions described for user access to extension resources are different from the permissions that must be added to a service account to enable {olmv1}-based initial installation of a cluster extension itself. For more on RBAC requirements while installing an extension, see "Cluster extension permissions" in "Managing extensions".
====

[role="_additional-resources"]
.Additional resources
* "Managing extensions" -> "Cluster extension permissions"

// Module included in the following assemblies:
//
// * extensions/ce/user-access-resources.adoc

[id="olmv1-default-cluster-roles-users_{context}"]
= Common default cluster roles for users

An installed cluster extension might include default cluster roles to determine role-based access control (RBAC) for regular users to API resources provided by the extension. A common set of cluster roles can resemble the following policies:

`view` cluster role:: Grants read-only access to all custom resource (CR) objects of specified API resources across the cluster. Intended for regular users who require visibility into the resources without any permissions to modify them. Ideal for monitoring purposes and limited access viewing.
`edit` cluster role:: Allows users to modify all CR objects within the cluster. Enables users to create, update, and delete resources, making it suitable for team members who must manage resources but should not control RBAC or manage permissions for others.
`admin` cluster role:: Provides full permissions, including `create`, `update`, and `delete` verbs, over all custom resource objects for the specified API resources across the cluster.

[role="_additional-resources"]
.Additional resources
* User-facing roles (Kubernetes documentation)

// Module included in the following assemblies:
//
// * extensions/ce/user-access-resources.adoc

[id="olmv1-finding-ce-resources_{context}"]
= Finding API groups and resources exposed by a cluster extension

To create appropriate RBAC policies for granting user access to cluster extension resources, you must know which API groups and resources are exposed by the installed extension. As an administrator, you can inspect custom resource definitions (CRDs) installed on the cluster by using {oc-first}.

.Prerequisites

* A cluster extension has been installed on your cluster.

.Procedure

* To list installed CRDs while specifying a label selector targeting a specific cluster extension by name to find only CRDs owned by that extension, run the following command:
+
[source,terminal]
----
$ oc get crds -l 'olm.operatorframework.io/owner-kind=ClusterExtension,olm.operatorframework.io/owner-name=<cluster_extension_name>'
----

* Alternatively, you can search through all installed CRDs and individually inspect them by CRD name:

.. List all available custom resource definitions (CRDs) currently installed on the cluster by running the following command:
+
[source,terminal]
----
$ oc get crds
----
+
Find the CRD you are looking for in the output.

.. Inspect the individual CRD further to find its API groups by running the following command:
+
[source,terminal]
----
$ oc get crd <crd_name> -o yaml
----

// Module included in the following assemblies:
//
// * extensions/ce/user-access-resources.adoc

[id="olmv1-granting-user-access-binding_{context}"]
= Granting user access to extension resources by using custom role bindings

As a cluster administrator, you can manually create and configure role-based access control (RBAC) policies to grant user access to extension resources by using custom role bindings.

.Prerequisites

* A cluster extension has been installed on your cluster.
* You have a list of API groups and resource names, as described in "Finding API groups and resources exposed by a cluster extension".

.Procedure

. If the installed cluster extension does not provide default cluster roles, manually create one or more roles:

.. Consider the use cases for the set of roles described in "Common default cluster roles for users".
+
For example, create one or more of the following `ClusterRole` object definitions, replacing `<cluster_extension_api_group>` and `<cluster_extension_custom_resource>` with the actual API group and resource names provided by the installed cluster extension:
+
.Example `view-custom-resource.yaml` file
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: view-custom-resource
rules:
- apiGroups:
  - <cluster_extension_api_group>
  resources:
  - <cluster_extension_custom_resources>
  verbs:
  - get
  - list
  - watch
----
+
.Example `edit-custom-resource.yaml` file
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: edit-custom-resource
rules:
- apiGroups:
  - <cluster_extension_api_group>
  resources:
  - <cluster_extension_custom_resources>
  verbs:
  - get
  - list
  - watch
  - create
  - update
  - patch
  - delete
----
+
.Example `admin-custom-resource.yaml` file
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: admin-custom-resource
rules:
- apiGroups:
  - <cluster_extension_api_group>
  resources:
  - <cluster_extension_custom_resources>
  verbs:
  - '*' <1>
----
<1> Setting a wildcard (`*`) in `verbs` allows all actions on the specified resources.

.. Create the cluster roles by running the following command for any YAML files you created:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. Associate a cluster role to specific users or groups to grant them the necessary permissions for the resource by binding the cluster roles to individual user or group names:

.. Create an object definition for either a _cluster role binding_ to grant access across all namespaces or a _role binding_ to grant access within a specific namespace:
+
--
*** The following example cluster role bindings grant read-only `view` access to the custom resource across all namespaces:
+
.Example `ClusterRoleBinding` object for a user
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: view-custom-resource-binding
subjects:
- kind: User
  name: <user_name>
roleRef:
  kind: ClusterRole
  name: view-custom-resource
  apiGroup: rbac.authorization.k8s.io
----
+
.Example `ClusterRoleBinding` object for a user
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: view-custom-resource-binding
subjects:
- kind: Group
  name: <group_name>
roleRef:
  kind: ClusterRole
  name: view-custom-resource
  apiGroup: rbac.authorization.k8s.io
----

*** The following role binding restricts `edit` permissions to a specific namespace:
+
.Example `RoleBinding` object for a user
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: edit-custom-resource-edit-binding
  namespace: <namespace>
subjects:
- kind: User
  name: <username>
roleRef:
  kind: Role
  name: custom-resource-edit
  apiGroup: rbac.authorization.k8s.io
----
--

.. Save your object definition to a YAML file.

.. Create the object by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * extensions/ce/user-access-resources.adoc

[id="olmv1-granting-user-access-aggregated_{context}"]
= Granting user access to extension resources by using aggregated cluster roles

As a cluster administrator, you can configure role-based access control (RBAC) policies to grant user access to extension resources by using aggregated cluster roles.

To automatically extend existing default cluster roles, you can add _aggregation labels_ by adding one or more of the following labels to a `ClusterRole` object:

.Aggregation labels in a `ClusterRole` object
[source,yaml]
----
# ..
metadata:
  labels:
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
    rbac.authorization.k8s.io/aggregate-to-view: "true"
# ..
----

This allows users who already have `view`, `edit`, or `admin` roles to interact with the  custom resource specified by the `ClusterRole` object without requiring additional role or cluster role bindings to specific users or groups.

.Prerequisites

* A cluster extension has been installed on your cluster.
* You have a list of API groups and resource names, as described in "Finding API groups and resources exposed by a cluster extension".

.Procedure

. Create an object definition for a cluster role that specifies the API groups and resources provided by the cluster extension and add an aggregation label to extend one or more existing default cluster roles:
+
.Example `ClusterRole` object with an aggregation label
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: view-custom-resource-aggregated
  labels:
    rbac.authorization.k8s.io/aggregate-to-view: "true"
rules:
  - apiGroups:
      - <cluster_extension_api_group>
    resources:
      - <cluster_extension_custom_resource>
    verbs:
      - get
      - list
      - watch
----
+
You can create similar `ClusterRole` objects for `edit` and `admin` with appropriate verbs, such as `create`, `update`, and `delete`. By using aggregation labels, the permissions for the custom resources are added to the default roles.

. Save your object definition to a YAML file.

. Create the object by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

[role="_additional-resources"]
.Additional resources
* Aggregated ClusterRoles (Kubernetes documentation)
