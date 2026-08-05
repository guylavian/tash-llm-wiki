---
title: "Uninstalling the External Secrets Operator for Red Hat OpenShift"
type: reference
domain: openshift
slug: security-4-22-external-secrets-operator-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-operator-uninstall
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the External Secrets Operator for Red Hat OpenShift

[id="external-secrets-operator-uninstall"]
= Uninstalling the External Secrets Operator for Red Hat OpenShift

[role="_abstract"]
You can remove the {external-secrets-operator} from OpenShift Container Platform by uninstalling the Operator and removing its related resources.

// Uninstalling the {external-secrets-operator-short}
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-uninstall.adoc

[id="external-secrets-operator-uninstall-console_{context}"]
= Uninstalling the {external-secrets-operator} using the web console

[role="_abstract"]
You can uninstall the {external-secrets-operator} from your cluster using the OpenShift Container Platform web console. Uninstalling the Operator does not automatically delete the `ExternalSecrets` custom resources or the running `external-secrets` application workload. These resources remain in the cluster to prevent accidental data loss and must be removed manually if they are no longer needed.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* The {external-secrets-operator-short} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Uninstall the {external-secrets-operator} using the following steps:

.. Navigate to *Ecosystem* -> *Installed Operators*.

.. Click the Options menu {kebab} next to the *{external-secrets-operator}* entry and click *Uninstall Operator*.

.. In the confirmation dialog, click *Uninstall*.

// Removing {external-secrets-operator-short}
// Module included in the following assemblies:
//
// * security/external-secrets-operator-uninstall.adoc

[id="external-secrets-remove-resources_{context}"]
= Removing {external-secrets-operator} resources by using the web console

[role="_abstract"]
After you have uninstalled the {external-secrets-operator}, you can optionally eliminate its associated resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove the deployments of the `external-secrets` application components in the `external-secrets` namespace:

.. Click the *Project* drop-down menu to see a list of all available projects, and select the *external-secrets* project.

.. Navigate to *Workloads* -> *Deployments*.

.. Select the deployment that you want to delete.

.. Click the *Actions* drop-down menu, and select *Delete Deployment* to see a confirmation dialog box.

.. Click *Delete* to delete the deployment.

. Remove the custom resource definitions (CRDs) that were installed by the {external-secrets-operator-short} using the following steps:

.. Navigate to *Administration* -> *CustomResourceDefinitions*.

.. Choose `external-secrets.io/component: controller` from the suggestions in the *Label* field to filter the CRDs.

.. Click the Options menu {kebab} next to each of the following CRDs, and select *Delete Custom Resource Definition*:

*** ACRAccessToken
*** ClusterExternalSecret
*** ClusterGenerator
*** ClusterPushSecret
*** ClusterSecretStore
*** ECRAuthorizationToken
*** ExternalSecret
*** GCRAccessToken
*** GeneratorState
*** GithubAccessToken
*** Grafana
*** MFA
*** Password
*** PushSecret
*** QuayAccessToken
*** SecretStore
*** SSHKey
*** STSSessionToken
*** UUID
*** VaultDynamicSecret
*** Webhook

. Remove the `external-secrets-operator` namespace using the following steps:

.. Navigate to *Administration* -> *Namespaces*.

.. Click the Options menu {kebab} next to the *{external-secrets-operator-short}* and select *Delete Namespace*.

.. In the confirmation dialog, enter `external-secrets-operator` in the field and click *Delete*.

// Removing {external-secrets-operator-short} using CLI
// Module included in the following assemblies:
//
// * security/external-secrets-operator-uninstall.adoc

[id="external-secrets-remove-resources-cli_{context}"]
= Removing {external-secrets-operator} resources by using the CLI

[role="_abstract"]
After you have uninstalled the {external-secrets-operator}, you can optionally eliminate its associated resources from your cluster by using the command-line interface (CLI).

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Delete the deployments of the `external-secrets` application components in the `external-secrets` namespace by running the following command:
+
[source,terminal]
----
$ oc delete deployment -n external-secrets -l app=external-secrets
----

. Delete the custom resource definitions (CRDs) that were installed by the {external-secrets-operator-short} by running the following command:
+
[source,terminal]
----
$ oc delete customresourcedefinitions.apiextensions.k8s.io -l external-secrets.io/component=controller
----

. Delete the `external-secrets-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc delete project external-secrets-operator
----
