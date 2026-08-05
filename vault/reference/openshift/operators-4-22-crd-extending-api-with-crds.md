---
title: "Extending the Kubernetes API with custom resource definitions"
type: reference
domain: openshift
slug: operators-4-22-crd-extending-api-with-crds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/crd-extending-api-with-crds
version: 4.22
family: operators
documentKind: "Documentation"
---

# Extending the Kubernetes API with custom resource definitions

[id="crd-extending-api-with-crds"]
= Extending the Kubernetes API with custom resource definitions

Operators use the Kubernetes extension mechanism, custom resource definitions (CRDs), so that custom objects managed by the Operator look and act just like the built-in, native Kubernetes objects. This guide describes how cluster administrators can extend their OpenShift Container Platform cluster by creating and managing CRDs.

// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-custom-resource-definitions_{context}"]
= Custom resource definitions

In the Kubernetes API, a _resource_ is an endpoint that stores a collection of API objects of a certain kind. For example, the built-in `Pods` resource contains a collection of `Pod` objects.

A _custom resource definition_ (CRD) object defines a new, unique object type, called a _kind_, in the cluster and lets the Kubernetes API server handle its entire lifecycle.

_Custom resource_ (CR) objects are created from CRDs that have been added to the cluster by a cluster administrator, allowing all cluster users to add the new resource type into projects.

When a cluster administrator adds a new CRD to the cluster, the Kubernetes API server reacts by creating a new RESTful resource path that can be accessed by the entire cluster or a single project (namespace) and begins serving the specified CR.

Cluster administrators that want to grant access to the CRD to other users can use cluster role aggregation to grant access to users with the `admin`, `edit`, or `view` default cluster roles. Cluster role aggregation allows the insertion of custom policy rules into these cluster roles. This behavior integrates the new resource into the RBAC policy of the cluster as if it was a built-in resource.

Operators in particular make use of CRDs by packaging them with any required RBAC policy and other software-specific logic.
Cluster administrators can also add CRDs manually to the cluster outside of the lifecycle of an Operator, making them available to all users.

[NOTE]
====
While only cluster administrators can create CRDs, developers can create the CR from an existing CRD if they have read and write permission to it.
====

// Module included in the following assemblies:
//
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-creating-custom-resources-definition_{context}"]
= Creating a custom resource definition

To create custom resource (CR) objects, cluster administrators must first create a custom resource definition (CRD).

.Prerequisites

- Access to an OpenShift Container Platform cluster with `cluster-admin` user privileges.

.Procedure

To create a CRD:

. Create a YAML file that contains the following field types:
+
.Example YAML file for a CRD
[source,yaml]
----
apiVersion: apiextensions.k8s.io/v1 <1>
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com <2>
spec:
  group: stable.example.com <3>
  versions:
    - name: v1 <4>
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  scope: Namespaced <5>
  names:
    plural: crontabs <6>
    singular: crontab <7>
    kind: CronTab <8>
    shortNames:
    - ct <9>
----
<1> Use the `apiextensions.k8s.io/v1` API.
<2> Specify a name for the definition. This must be in the `<plural-name>.<group>` format using the values from the `group` and `plural` fields.
<3> Specify a group name for the API. An API group is a collection of objects that are logically related. For example, all batch objects like `Job` or `ScheduledJob` could be in the batch API group (such as `batch.api.example.com`). A good practice is to use a fully-qualified-domain name (FQDN) of your organization.
<4> Specify a version name to be used in the URL. Each API group can exist in multiple versions, for example `v1alpha`, `v1beta`, `v1`.
<5> Specify whether the custom objects are available to a project (`Namespaced`) or all projects in the cluster (`Cluster`).
<6> Specify the plural name to use in the URL. The `plural` field is the same as a resource in an API URL.
<7> Specify a singular name to use as an alias on the CLI and for display.
<8> Specify the kind of objects that can be created. The type can be in CamelCase.
<9> Specify a shorter string to match your resource on the CLI.
+
[NOTE]
====
By default, a CRD is cluster-scoped and available to all projects.
====

. Create the CRD object:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
+
A new RESTful API endpoint is created at:
+
[source,terminal]
----
/apis/<spec:group>/<spec:version>/<scope>/*/<names-plural>/...
----
+
For example, using the example file, the following endpoint is created:
+
[source,terminal]
----
/apis/stable.example.com/v1/namespaces/*/crontabs/...
----
+
You can now use this endpoint URL to create and manage CRs. The object kind is based on the `spec.kind` field of the CRD object you created.

// Module included in the following assemblies:
//
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-creating-aggregated-cluster-role_{context}"]
= Creating cluster roles for custom resource definitions

Cluster administrators can grant permissions to existing cluster-scoped custom resource definitions (CRDs). If you use the `admin`, `edit`, and `view` default cluster roles, you can take advantage of cluster role aggregation for their rules.

[IMPORTANT]
====
You must explicitly assign permissions to each of these roles. The roles with more permissions do not inherit rules from roles with fewer permissions. If you assign a rule to a role, you must also assign that verb to roles that have more permissions. For example, if you grant the `get crontabs` permission to the view role, you must also grant it to the `edit` and `admin` roles. The `admin` or `edit` role is usually assigned to the user that created a project through the project template.
====

.Prerequisites

- Create a CRD.

.Procedure

. Create a cluster role definition file for the CRD. The cluster role definition is a YAML file that contains the rules that apply to each cluster role. An OpenShift Container Platform controller adds the rules that you specify to the default cluster roles.
+
.Example YAML file for a cluster role definition
[source,yaml]
----
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1 <1>
metadata:
  name: aggregate-cron-tabs-admin-edit <2>
  labels:
    rbac.authorization.k8s.io/aggregate-to-admin: "true" <3>
    rbac.authorization.k8s.io/aggregate-to-edit: "true" <4>
rules:
- apiGroups: ["stable.example.com"] <5>
  resources: ["crontabs"] <6>
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete", "deletecollection"] <7>
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: aggregate-cron-tabs-view <2>
  labels:
    # Add these permissions to the "view" default role.
    rbac.authorization.k8s.io/aggregate-to-view: "true" <8>
    rbac.authorization.k8s.io/aggregate-to-cluster-reader: "true" <9>
rules:
- apiGroups: ["stable.example.com"] <5>
  resources: ["crontabs"] <6>
  verbs: ["get", "list", "watch"] <7>
----
<1> Use the `rbac.authorization.k8s.io/v1` API.
<2> Specify a name for the definition.
<3> Specify this label to grant permissions to the admin default role.
<4> Specify this label to grant permissions to the edit default role.
<5> Specify the group name of the CRD.
<6> Specify the plural name of the CRD that these rules apply to.
<7> Specify the verbs that represent the permissions that are granted to the role. For example, apply read and write permissions to the `admin` and `edit` roles and only read permission to the `view` role.
<8> Specify this label to grant permissions to the `view` default role.
<9> Specify this label to grant permissions to the `cluster-reader` default role.

. Create the cluster role:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

// Useful paired with modules/crd-inspecting-custom-resources.adoc
//
// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-creating-custom-resources-from-file_{context}"]
= Creating custom resources from a file

After a custom resource definition (CRD) has been added to the cluster, custom resources (CRs) can be created with the CLI from a file using the CR specification.

.Prerequisites

- CRD added to the cluster by a cluster administrator.

.Procedure

. Create a YAML file for the CR. In the following example definition, the `cronSpec` and `image` custom fields are set in a CR of `Kind: CronTab`. The `Kind` comes from the `spec.kind` field of the CRD object:
+
.Example YAML file for a CR
[source,yaml]
----
apiVersion: "stable.example.com/v1" <1>
kind: CronTab <2>
metadata:
  name: my-new-cron-object <3>
  finalizers: <4>
  - finalizer.stable.example.com
spec: <5>
  cronSpec: "* * * * /5"
  image: my-awesome-cron-image
----
+
<1> Specify the group name and API version (name/version) from the CRD.
<2> Specify the type in the CRD.
<3> Specify a name for the object.
<4> Specify the finalizers for the object, if any. Finalizers allow controllers to implement conditions that must be completed before the object can be deleted.
<5> Specify conditions specific to the type of object.

. After you create the file, create the object:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

// Useful paired with modules/crd-creating-custom-resources-from-file.adoc
//
// Module included in the following assemblies:
//
// * operators/understanding/crds/crd-managing-resources-from-crds.adoc
// * operators/understanding/crds/extending-api-with-crds.adoc

[id="crd-inspecting-custom-resources_{context}"]
= Inspecting custom resources

You can inspect custom resource (CR) objects that exist in your cluster using the CLI.

.Prerequisites

* A CR object exists in a namespace to which you have access.

.Procedure

. To get information on a specific kind of a CR, run:
+
[source,terminal]
----
$ oc get <kind>
----
+
For example:
+
[source,terminal]
----
$ oc get crontab
----
+
.Example output
[source,terminal]
----
NAME                 KIND
my-new-cron-object   CronTab.v1.stable.example.com
----
+
Resource names are not case-sensitive, and you can use either the singular or plural forms defined in the CRD, as well as any short name. For example:
+
[source,terminal]
----
$ oc get crontabs
----
+
[source,terminal]
----
$ oc get crontab
----
+
[source,terminal]
----
$ oc get ct
----

. You can also view the raw YAML data for a CR:
+
[source,terminal]
----
$ oc get <kind> -o yaml
----
+
For example:
+
[source,terminal]
----
$ oc get ct -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: v1
items:
- apiVersion: stable.example.com/v1
  kind: CronTab
  metadata:
    clusterName: ""
    creationTimestamp: 2017-05-31T12:56:35Z
    deletionGracePeriodSeconds: null
    deletionTimestamp: null
    name: my-new-cron-object
    namespace: default
    resourceVersion: "285"
    selfLink: /apis/stable.example.com/v1/namespaces/default/crontabs/my-new-cron-object
    uid: 9423255b-4600-11e7-af6a-28d2447dc82b
  spec:
    cronSpec: '* * * * /5' <1>
    image: my-awesome-cron-image <1>
----
<1> Custom data from the YAML that you used to create the object displays.
