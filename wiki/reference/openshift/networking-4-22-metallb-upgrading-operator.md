---
title: "Upgrading the MetalLB Operator"
type: reference
domain: openshift
slug: networking-4-22-metallb-upgrading-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/metallb-upgrading-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Upgrading the MetalLB Operator

[id="metallb-upgrading-operator"]
= Upgrading the MetalLB Operator

[role="_abstract"]
The `Subscription` custom resource (CR) for the MetalLB Operator is used to manage whether the Operator is upgraded automatically or manually.

By default, the `Subscription` CR assigns the namespace to `metallb-system` and automatically sets the `installPlanApproval` parameter to `Automatic`. This means that when Red{nbsp}Hat-provided Operator catalogs include a newer version of the MetalLB Operator, the MetalLB Operator is automatically upgraded.

If you need to manually control upgrading the MetalLB Operator, set the `installPlanApproval` parameter to `Manual`.

// Manually upgrading the MetalLB Operator
// Module included in the following assemblies:
//
// * networking/metallb/metallb-upgrading-operator.adoc

[id="upgrading-metallb-operator_{context}"]
= Manually upgrading the MetalLB Operator

[role="_abstract"]
To manually control when the MetalLB Operator upgrades in OpenShift Container Platform, you set `installPlanApproval` to Manual in the Subscription custom resource and approve the install plan. You then verify the upgrade by using the `ClusterServiceVersion` status.

.Prerequisites

* You updated your cluster to the latest z-stream release.
* You used the software catalog to install the MetalLB Operator.
* Access the cluster as a user with the `cluster-admin` role.

.Procedure

. Get the YAML definition of the `metallb-operator` subscription in the `metallb-system` namespace by entering the following command:
+
[source,terminal]
----
$ oc -n metallb-system get subscription metallb-operator -o yaml
----

. Edit the `Subscription` CR by setting the `installPlanApproval` parameter to `Manual`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metallb-operator
  namespace: metallb-system
# ...
spec:
   channel: stable
   installPlanApproval: Manual
   name: metallb-operator
   source: redhat-operators
   sourceNamespace: openshift-marketplace
# ...
----

. Find the latest OpenShift Container Platform  version of the MetalLB Operator by entering the following command:
+
[source,terminal]
----
$ oc -n metallb-system get csv
----

. Check the install plan that exists in the namespace by entering the following command.
+
[source,terminal]
----
$ oc -n metallb-system get installplan
----
+
.Example output that shows install-tsz2g as a manual install plan
[source,terminal,subs="attributes+"]
----
NAME            CSV                                     APPROVAL    APPROVED
install-shpmd   metallb-operator.v.0-202502261233   Automatic   true
install-tsz2g   metallb-operator.v.0-202503102139   Manual      false
----

. Edit the install plan that exists in the namespace by entering the following command. Ensure that you replace `<name_of_installplan>` with the name of the install plan, such as `install-tsz2g`.
+
[source,terminal]
----
$ oc edit installplan <name_of_installplan> -n metallb-system
----
+
.. With the install plan open in your editor, set the `spec.approval` parameter to `Manual` and set the `spec.approved` parameter to `true`.
+
[NOTE]
====
After you edit the install plan, the upgrade operation starts. If you enter the `oc -n metallb-system get csv` command during the upgrade operation, the output might show the `Replacing` or the `Pending` status.
====

.Verification

* To verify that the Operator is upgraded, enter the following command and then check that output shows `Succeeded` for the Operator:
+
[source,terminal]
----
$ oc -n metallb-system get csv
----

[id="additional-resources"]
== Additional resources

* Introduction to OpenShift updates

* Installing the MetalLB Operator
