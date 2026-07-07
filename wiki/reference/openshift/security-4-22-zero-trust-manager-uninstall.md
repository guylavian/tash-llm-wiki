---
title: "Uninstalling the {zero-trust-full}"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-uninstall
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the {zero-trust-full}

[id="zero-trust-manager-uninstall_{context}"]
= Uninstalling the {zero-trust-full}

[role="_abstract"]
To remove the {zero-trust-full} from OpenShift Container Platform, uninstall the Operator and delete its related resources. This process removes the component from your cluster.

// Uninstalling the {zero-trust-full}
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-uninstall.adoc

[id="zero-trust-manager-uninstall-console_{context}"]
= Uninstalling the {zero-trust-full}

[role="_abstract"]
To remove the {zero-trust-full} from your cluster, uninstall the Operator using the web console. This helps you clean up resources and delete the service from your environment.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have access to the OpenShift Container Platform web console.

* The {zero-trust-full} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Uninstall the {zero-trust-full}.

.. Go to *Ecosystem* -> *Installed Operators*.

.. Click the *Options* menu next to the *{zero-trust-full}* entry, and then click *Uninstall Operator*.

.. In the confirmation dialog, click *Uninstall*.

.Verification

* Verify that the {zero-trust-full} Operator is uninstalled.
+
[source,terminal]
----
$ oc get csv -n openshift-zero-trust-workload-identity
----
+
.Example output
[source,terminal]
----
No resources found in openshift-zero-trust-workload-identity namespace.
----

// Removing {zero-trust-full} resources
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-uninstall.adoc

[id="zero-trust-manager-uninstall-resources_{context}"]
= Uninstalling {zero-trust-full} resources by using the CLI

[role="_abstract"]
Remove {zero-trust-full} resources from your cluster using the CLI. This deletes the remaining operands and definitions to help ensure a clean environment after you uninstall the product.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Uninstall the operands by running each of the following commands:

.. Delete the `SpireOIDCDiscoveryProvider` cluster by running the following command:
+
[source,terminal]
----
$ oc delete SpireOIDCDiscoveryProvider cluster
----

.. Delete the `SpiffeCSIDriver` cluster by running the following command:
+
[source,terminal]
----
$ oc delete SpiffeCSIDriver cluster -l
----

.. Delete the `SpireAgent` cluster by running the following command:
+
[source,terminal]
----
$ oc delete SpireAgent cluster
----

.. Delete the `SpireServer` cluster by running the following command:
+
[source,terminal]
----
$ oc delete SpireServer cluster
----

.. Delete the `ZeroTrustWorkloadIdentityManager` cluster by running the following command:
+
[source,terminal]
----
$ oc delete ZeroTrustWorkloadIdentityManager cluster
----

.. Delete the persistent volume claim (PVC) by running the following command:
+
[source,terminal]
----
$ oc delete pvc -l=app.kubernetes.io/name=spire-server
----

.. Delete the service by running the following command:
+
[source,terminal]
----
$ oc delete service -l=app.kubernetes.io/name=zero-trust-workload-identity-manager -n zero-trust-workload-identity-manager
----

.. Delete the namespace by running the following command:
+
[source,terminal]
----
$ oc delete ns zero-trust-workload-identity-manager
----

.. Delete the cluster role by running the following command:
+
[source,terminal]
----
$ oc delete clusterrole -l=app.kubernetes.io/name=zero-trust-workload-identity-manager
----

.. Delete the admission webhook configuration by running the following command:
+
[source,terminal]
----
$ oc delete validatingwebhookconfigurations -l=app.kubernetes.io/name=zero-trust-workload-identity-manager
----

. Delete the custom resource definitions (CRDs) by running each of the following commands:

.. Delete the SPIRE Server CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd spireservers.operator.openshift.io
----

.. Delete the SPIRE Agent CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd spireagents.operator.openshift.io
----

.. Delete the SPIFFEE CSI Drivers CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd spiffecsidrivers.operator.openshift.io
----

.. Delete the SPIRE OIDC Discovery Provider CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd spireoidcdiscoveryproviders.operator.openshift.io
----

.. Delete the SPIRE and SPIFFE cluster federated trust domains CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd clusterfederatedtrustdomains.spire.spiffe.io
----

.. Delete the cluster SPIFFE IDs CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd clusterspiffeids.spire.spiffe.io
----

.. Delete the SPIRE and SPIFFE cluster static entries CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd clusterstaticentries.spire.spiffe.io
----

.. Delete the {zero-trust-full} CRD by running the following command:
+
[source,terminal]
----
$ oc delete crd zerotrustworkloadidentitymanagers.operator.openshift.io
----

.Verification

To verify that the resources have been deleted, replace each `oc delete` command with `oc get`, and then run the command. If no resources are returned, the deletion was successful.
