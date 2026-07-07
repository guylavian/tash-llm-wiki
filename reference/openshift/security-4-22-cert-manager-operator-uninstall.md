---
title: "Uninstalling the {cert-manager-operator}"
type: reference
domain: openshift
slug: security-4-22-cert-manager-operator-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-operator-uninstall
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the {cert-manager-operator}

[id="cert-manager-operator-uninstall"]
= Uninstalling the {cert-manager-operator}

[role="_abstract"]
You can remove the {cert-manager-operator} from OpenShift Container Platform by uninstalling the Operator and removing its related resources.

// Uninstalling the {cert-manager-operator}
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-operator-uninstall.adoc

[id="cert-manager-uninstall-console_{context}"]
= Uninstalling the {cert-manager-operator}

[role="_abstract"]
You can uninstall the {cert-manager-operator} by using the web console.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* The {cert-manager-operator} is installed.
// TODO: Any other prereqs, like removing anything that is using it?

.Procedure

. Log in to the OpenShift Container Platform web console.
. Uninstall the {cert-manager-operator} Operator.
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{cert-manager-operator}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

// Removing {cert-manager-operator} resources
// Module included in the following assemblies:
//
// * security/cert-manager-operator-uninstall.adoc

[id="cert-manager-remove-resources-console_{context}"]
= Removing {cert-manager-operator} resources

[role="_abstract"]
Once you have uninstalled the {cert-manager-operator}, you have the option to eliminate its associated resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove the deployments of the cert-manager components, such as `cert-manager`, `cainjector`, and `webhook`, present in the `cert-manager` namespace.

.. Click the *Project* drop-down menu to see a list of all available projects, and select the *cert-manager* project.

.. Navigate to *Workloads* -> *Deployments*.

.. Select the deployment that you want to delete.

.. Click the *Actions* drop-down menu, and select *Delete Deployment* to see a confirmation dialog box.

.. Click *Delete* to delete the deployment.

.. Alternatively, delete deployments of the cert-manager components such as `cert-manager`, `cainjector` and `webhook` present in the `cert-manager` namespace by using the command-line interface (CLI).
+
[source,terminal]
----
$ oc delete deployment -n cert-manager -l app.kubernetes.io/instance=cert-manager
----

. Optional: Remove the custom resource definitions (CRDs) that were installed by the {cert-manager-operator}:

.. Remove the finalizers from the `CertManager` custom resource (CR) by running the following command:
+
[source,terminal]
----
$ oc patch certmanagers.operator cluster --type=merge -p='{"metadata":{"finalizers":null}}'
----

.. Navigate to *Administration* -> *CustomResourceDefinitions*.

.. Enter `certmanager` in the *Name* field to filter the CRDs.

.. Click the Options menu {kebab} next to each of the following CRDs, and select *Delete Custom Resource Definition*:

*** `Certificate`
*** `CertificateRequest`
*** `CertManager` (`operator.openshift.io`)
*** `Challenge`
*** `ClusterIssuer`
*** `Issuer`
*** `Order`

. Optional: Remove the `cert-manager-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Click the Options menu {kebab} next to the *cert-manager-operator* and select *Delete Namespace*.
.. In the confirmation dialog, enter `cert-manager-operator` in the field and click *Delete*.
