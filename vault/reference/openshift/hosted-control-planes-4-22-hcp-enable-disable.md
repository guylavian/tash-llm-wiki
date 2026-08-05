---
title: "Enabling or disabling the {hcp} feature"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-enable-disable
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-enable-disable
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Enabling or disabling the {hcp} feature

[id="hcp-enable-disable"]
= Enabling or disabling the {hcp} feature

[role="_abstract"]
The {hcp} feature, as well as the `hypershift-addon` managed cluster add-on, are enabled by default. If needed, you can disable the feature, or if you disabled it, you can manually enable it.

You can uninstall the HyperShift Operator and disable the {hcp} feature. When you disable the {hcp} feature, you must destroy the hosted cluster and the managed cluster resource on {mce-short}, as described in the _Destroying a hosted cluster_ section.

[role="_additional-resources"]
.Additional resources

* Destroying a hosted cluster

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-enable-disable.adoc

[id="hcp-enable-manual_{context}"]
= Manually enabling the {hcp} feature

[role="_abstract"]
If the {hcp} feature is disabled, you can manually enable it.

.Procedure

. Run the following command to enable the feature:
+
[source,terminal]
----
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift","enabled": true}]}}}'
----
+
The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`.

. Run the following command to verify that the `hypershift` and `hypershift-local-hosting` features are enabled in the `MultiClusterEngine` custom resource:
+
[source,terminal]
----
$ oc get mce multiclusterengine -o yaml
----
The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`.
+
.Example output
[source,yaml]
----
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: hypershift
      enabled: true
    - name: hypershift-local-hosting
      enabled: true
----

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-enable-disable.adoc

[id="hcp-enable-manual-addon_{context}"]
= Manually enabling the hypershift-addon managed cluster add-on for local-cluster

[role="_abstract"]
Enabling the {hcp} feature automatically enables the `hypershift-addon` managed cluster add-on. If you need to enable the `hypershift-addon` managed cluster add-on manually, use the `hypershift-addon` to install the HyperShift Operator on `local-cluster`.

.Procedure

. Create the `ManagedClusterAddon` add-on named `hypershift-addon` by creating a file that resembles the following example:
+
[source,yaml]
----
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: hypershift-addon
  namespace: local-cluster
spec:
  installNamespace: open-cluster-management-agent-addon
----

. Apply the file by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----
+
Replace `filename` with the name of the file that you created.

. Confirm that the `hypershift-addon` managed cluster add-on is installed by running the following command:
+
[source,terminal]
----
$ oc get managedclusteraddons -n local-cluster hypershift-addon
----
+
If the add-on is installed, the output resembles the following example:
+
[source,terminal]
----
NAME               AVAILABLE   DEGRADED   PROGRESSING
hypershift-addon   True
----
+
Your `hypershift-addon` managed cluster add-on is installed and the hosting cluster is available to create and manage hosted clusters.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-enable-disable.adoc

[id="hcp-uninstall-operator_{context}"]
= Uninstalling the HyperShift Operator

[role="_abstract"]
Before you can disable the {hcp} feature, you need to uninstall the HyperShift Operator and disable the `hypershift-addon` from the `local-cluster`.

.Procedure

. Run the following command to ensure that there is no hosted cluster running:
+
[source,terminal]
----
$ oc get hostedcluster -A
----
+
[IMPORTANT]
====
If a hosted cluster is running, the HyperShift Operator does not uninstall, even if the `hypershift-addon` is disabled.
====

. Disable the `hypershift-addon` by running the following command:
+
[source,terminal]
----
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift-local-hosting","enabled": false}]}}}'
----
+
The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`.
+
[NOTE]
====
You can also disable the `hypershift-addon` for the `local-cluster` from the {mce-short} console after disabling the `hypershift-addon`.
====

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-enable-disable.adoc

[id="hcp-disable-feature_{context}"]
= Disabling the {hcp} feature

[role="_abstract"]
If you no longer use the {hcp} feature, you can disable it.

.Prerequisites

* You uninstalled the HyperShift Operator. For more information, see "Uninstalling the HyperShift Operator".

.Procedure

. Run the following command to disable the {hcp} feature:
+
[source,terminal]
----
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift","enabled": false}]}}}'
----
+
The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`.

. You can verify that the `hypershift` and `hypershift-local-hosting` features are disabled in the `MultiClusterEngine` custom resource by running the following command:
+
[source,terminal]
----
$ oc get mce multiclusterengine -o yaml
----
+
The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`.
+
See the following example where `hypershift` and `hypershift-local-hosting` have their `enabled:` flags set to `false`:
+
[source,yaml]
----
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: hypershift
      enabled: false
    - name: hypershift-local-hosting
      enabled: false
----
