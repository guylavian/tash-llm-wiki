---
title: "Viewing Operator status"
type: reference
domain: openshift
slug: operators-4-22-olm-status
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-status
version: 4.22
family: operators
documentKind: "Documentation"
---

# Viewing Operator status

[id="olm-status"]
= Viewing Operator status

Understanding the state of the system in Operator Lifecycle Manager (OLM) is important for making decisions about and debugging problems with installed Operators. OLM provides insight into subscriptions and related catalog sources regarding their state and actions performed. This helps users better understand the healthiness of their Operators.

// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-status-conditions_{context}"]
= Operator subscription condition types

[role="_abstract"]
Subscriptions can report the following condition types:

.Subscription condition types
[cols="1,2",options="header"]
|===
|Condition |Description

|`CatalogSourcesUnhealthy`
|Some or all of the catalog sources to be used in resolution are unhealthy.

|`InstallPlanMissing`
|An install plan for a subscription is missing.

|`InstallPlanPending`
|An install plan for a subscription is pending installation.

|`InstallPlanFailed`
|An install plan for a subscription has failed.

|`ResolutionFailed`
|The dependency resolution for a subscription has failed.

|===

[NOTE]
====
Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====

[role="_additional-resources"]
.Additional resources

* Refreshing failing subscriptions

// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-status-viewing-cli_{context}"]
= Viewing Operator subscription status by using the CLI

[role="_abstract"]
You can view Operator subscription status by using the CLI.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List Operator subscriptions:
+
[source,terminal]
----
$ oc get subs -n <operator_namespace>
----

. Use the `oc describe` command to inspect a `Subscription` resource:
+
[source,terminal]
----
$ oc describe sub <subscription_name> -n <operator_namespace>
----

. In the command output, find the `Conditions` section for the status of Operator subscription condition types. In the following example, the `CatalogSourcesUnhealthy` condition type has a status of `false` because all available catalog sources are healthy:
+
.Example output
[source,terminal]
----
Name:         cluster-logging
Namespace:    openshift-logging
Labels:       operators.coreos.com/cluster-logging.openshift-logging=
Annotations:  <none>
API Version:  operators.coreos.com/v1alpha1
Kind:         Subscription
# ...
Conditions:
   Last Transition Time:  2019-07-29T13:42:57Z
   Message:               all available catalogsources are healthy
   Reason:                AllCatalogSourcesHealthy
   Status:                False
   Type:                  CatalogSourcesUnhealthy
# ...
----
+
[NOTE]
====
Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====

// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-cs-status-cli_{context}"]
= Viewing Operator catalog source status by using the CLI

[role="_abstract"]
You can view the status of an Operator catalog source by using the CLI.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List the catalog sources in a namespace. For example, you can check the `{global_ns}` namespace, which is used for cluster-wide catalog sources:
+
[source,terminal,subs="attributes+"]
----
$ oc get catalogsources -n {global_ns}
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY               TYPE   PUBLISHER   AGE
certified-operators   Certified Operators   grpc   Red Hat     55m
community-operators   Community Operators   grpc   Red Hat     55m
example-catalog       Example Catalog       grpc   Example Org 2m25s
redhat-operators      Red Hat Operators     grpc   Red Hat     55m
----

. Use the `oc describe` command to get more details and status about a catalog source:
+
[source,terminal,subs="attributes+"]
----
$ oc describe catalogsource example-catalog -n {global_ns}
----
+
.Example output
[source,terminal,subs="attributes+"]
----
Name:         example-catalog
Namespace:    {global_ns}
Labels:       <none>
Annotations:  operatorframework.io/managed-by: marketplace-operator
              target.workload.openshift.io/management: {"effect": "PreferredDuringScheduling"}
API Version:  operators.coreos.com/v1alpha1
Kind:         CatalogSource
# ...
Status:
  Connection State:
    Address:              example-catalog.{global_ns}.svc:50051
    Last Connect:         2021-09-09T17:07:35Z
    Last Observed State:  TRANSIENT_FAILURE
  Registry Service:
    Created At:         2021-09-09T17:05:45Z
    Port:               50051
    Protocol:           grpc
    Service Name:       example-catalog
    Service Namespace:  {global_ns}
# ...
----
+
In the preceding example output, the last observed state is `TRANSIENT_FAILURE`. This state indicates that there is a problem establishing a connection for the catalog source.

. List the pods in the namespace where your catalog source was created:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {global_ns}
----
+
.Example output
[source,terminal]
----
NAME                                    READY   STATUS             RESTARTS   AGE
certified-operators-cv9nn               1/1     Running            0          36m
community-operators-6v8lp               1/1     Running            0          36m
marketplace-operator-86bfc75f9b-jkgbc   1/1     Running            0          42m
example-catalog-bwt8z                   0/1     ImagePullBackOff   0          3m55s
redhat-operators-smxx8                  1/1     Running            0          36m
----
+
When a catalog source is created in a namespace, a pod for the catalog source is created in that namespace. In the preceding example output, the status for the `example-catalog-bwt8z` pod is `ImagePullBackOff`. This status indicates that there is an issue pulling the catalog source's index image.

. Use the `oc describe` command to inspect a pod for more detailed information:
+
[source,terminal,subs="attributes+"]
----
$ oc describe pod example-catalog-bwt8z -n {global_ns}
----
+
.Example output
[source,terminal,subs="attributes+"]
----
Name:         example-catalog-bwt8z
Namespace:    {global_ns}
Priority:     0
Node:         ci-ln-jyryyg2-f76d1-ggdbq-worker-b-vsxjd/10.0.128.2
...
Events:
  Type     Reason          Age                From               Message
  ----     ------          ----               ----               -------
  Normal   Scheduled       48s                default-scheduler  Successfully assigned {global_ns}/example-catalog-bwt8z to ci-ln-jyryyf2-f76d1-fgdbq-worker-b-vsxjd
  Normal   AddedInterface  47s                multus             Add eth0 [10.131.0.40/23] from openshift-sdn
  Normal   BackOff         20s (x2 over 46s)  kubelet            Back-off pulling image "quay.io/example-org/example-catalog:v1"
  Warning  Failed          20s (x2 over 46s)  kubelet            Error: ImagePullBackOff
  Normal   Pulling         8s (x3 over 47s)   kubelet            Pulling image "quay.io/example-org/example-catalog:v1"
  Warning  Failed          8s (x3 over 47s)   kubelet            Failed to pull image "quay.io/example-org/example-catalog:v1": rpc error: code = Unknown desc = reading manifest v1 in quay.io/example-org/example-catalog: unauthorized: access to the requested resource is not authorized
  Warning  Failed          8s (x3 over 47s)   kubelet            Error: ErrImagePull
----
+
In the preceding example output, the error messages indicate that the catalog source's index image is failing to pull successfully because of an authorization issue. For example, the index image might be stored in a registry that requires login credentials.

[role="_additional-resources"]
.Additional resources

* Operator Lifecycle Manager concepts and resources -> Catalog source
* gRPC documentation: States of Connectivity
* Accessing images for Operators from private registries
