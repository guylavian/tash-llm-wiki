---
title: "Using feature gates in a hosted cluster"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-using-feature-gates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-using-feature-gates
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Using feature gates in a hosted cluster

[id="hcp-using-feature-gates"]
= Using feature gates in a hosted cluster

You can use feature gates in a hosted cluster to enable features that are not part of the default set of features. You can enable the `TechPreviewNoUpgrade` feature set by using feature gates in your hosted cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-using-feature-gates.adoc

[id="hcp-enable-feature-sets_{context}"]
= Enabling feature sets by using feature gates

You can enable the `TechPreviewNoUpgrade` feature set in a hosted cluster by editing the `HostedCluster` custom resource (CR) with the OpenShift CLI.

.Prerequisites

* You installed the OpenShift CLI (`oc`).

.Procedure

. Open the `HostedCluster` CR for editing on the hosting cluster by running the following command:
+
[source,terminal]
----
$ oc edit hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace>
----

. Define the feature set by entering a value in the `featureSet` field. For example:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name> <1>
  namespace: <hosted_cluster_namespace> <2>
spec:
  configuration:
    featureGate:
      featureSet: TechPreviewNoUpgrade <3>
----
<1> Specifies your hosted cluster name.
<2> Specifies your hosted cluster namespace.
<3> This feature set is a subset of the current Technology Preview features.
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them. Do not enable this feature set on production clusters.
====

. Save the file to apply the changes.

.Verification

* Verify that the `TechPreviewNoUpgrade` feature gate is enabled in your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get featuregate cluster -o yaml
----

[role="_additional-resources"]
.Additional resources

* FeatureGate [config.openshift.io/v1]
