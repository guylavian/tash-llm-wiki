---
title: "Migrating FRR-K8s resources"
type: reference
domain: openshift
slug: networking-4-22-migrating-frr-k8s-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/migrating-frr-k8s-resources
version: 4.22
family: networking
documentKind: "Documentation"
---

# Migrating FRR-K8s resources

[id="migrating-frr-k8s-resources"]
= Migrating FRR-K8s resources

[role="_abstract"]
Migrating FRR-K8s custom resources is required when upgrading from OpenShift Container Platform 4.17 or earlier with the MetalLB Operator deployed. Existing FRRConfiguration resources in the `metallb-system` namespace must be moved to the `openshift-frr-k8s` namespace to align with the updated architecture. Learn how to migrate these resources using the CLI and how to verify that the migration completed successfully.

All user-created FRR-K8s custom resources (CRs) in the `metallb-system` namespace under OpenShift Container Platform 4.17 and earlier releases must be migrated to the `openshift-frr-k8s` namespace. As a cluster administrator, you can migrate your FRR-K8s custom resources to the `openshift-frr-k8s` namespace using the CLI.

// Module included in the following assemblies:
//
// * networking/bgp_routing/migrating-frr-k8s-resources.adoc

[id="nw-bgp-frr-k8s-migration_{context}"]
= Migrating FRR-K8s resources

[role="_abstract"]
You can migrate the FRR-K8s `FRRConfiguration` custom resources from the `metallb-system` namespace to the `openshift-frr-k8s` namespace.

When upgrading from an earlier version of OpenShift Container Platform with the Metal LB Operator deployed, you must manually migrate your custom `FRRConfiguration` configurations from the `metallb-system` namespace to the `openshift-frr-k8s` namespace.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in to the cluster as a user with the `cluster-admin` role.

.Procedure

. To create the `openshift-frr-k8s` namespace, enter the following command:
+
[source,terminal]
----
$ oc create namespace openshift-frr-k8s
----

. To automate the migration, create a shell script named `migrate.sh` with the following contents:
+
[source,bash]
----
#!/bin/bash
OLD_NAMESPACE="metallb-system"
NEW_NAMESPACE="openshift-frr-k8s"
FILTER_OUT="metallb-"
oc get frrconfigurations.frrk8s.metallb.io -n "${OLD_NAMESPACE}" -o json |\
  jq -r '.items[] | select(.metadata.name | test("'"${FILTER_OUT}"'") | not)' |\
  jq -r '.metadata.namespace = "'"${NEW_NAMESPACE}"'"' |\
  oc create -f -
----

. To execute the migration, run the following command:
+
[source,terminal]
----
$ bash migrate.sh
----

.Verification

* To confirm that the migration succeeded, run the following command:
+
[source,terminal]
----
$ oc get frrconfigurations.frrk8s.metallb.io -n openshift-frr-k8s
----

After the migration is complete, you can remove the `FRRConfiguration` custom resources from the `metallb-system` namespace.
