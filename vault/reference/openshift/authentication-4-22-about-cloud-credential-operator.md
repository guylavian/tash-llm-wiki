---
title: "About the Cloud Credential Operator"
type: reference
domain: openshift
slug: authentication-4-22-about-cloud-credential-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/about-cloud-credential-operator
version: 4.22
family: authentication
documentKind: "Documentation"
---

# About the Cloud Credential Operator

[id="about-cloud-credential-operator"]
= About the Cloud Credential Operator

The Cloud Credential Operator (CCO) manages cloud provider credentials as  custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

[id="about-cloud-credential-operator-modes_{context}"]
== Modes

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in _mint_, _passthrough_, or _manual_ mode. These options provide transparency and flexibility in how the CCO uses cloud credentials to process `CredentialsRequest` CRs in the cluster, and allow the CCO to be configured to suit the security requirements of your organization. Not all CCO modes are supported for all cloud providers.

* **Mint**: In mint mode, the CCO uses the provided admin-level cloud credential to create new credentials for components in the cluster with only the specific permissions that are required.

* **Passthrough**: In passthrough mode, the CCO passes the provided cloud credential to the components that request cloud credentials.

* **Manual mode with long-term credentials for components**: In manual mode, you can manage long-term cloud credentials instead of the CCO.

* **Manual mode with short-term credentials for components**: For some providers, you can use the CCO utility (`ccoctl`) during installation to implement short-term credentials for individual components. These credentials are created and managed outside the OpenShift Container Platform cluster.

.CCO mode support matrix
[cols="<.^2,^.^1,^.^1,^.^1,^.^1"]
|====
|Cloud provider |Mint |Passthrough |Manual with long-term credentials |Manual with short-term credentials

|Amazon Web Services (AWS)
|X
|X
|X
|X

|Global Microsoft Azure
|
|X
|X
|X

|Microsoft Azure Stack Hub
|
|
|X
|

|{gcp-first}
|X
|X
|X
|X

|{ibm-cloud-name}
|
|
|X ^[1]^
|

|Nutanix
|
|
|X ^[1]^
|

|{rh-openstack-first}
|
|X
|
|

|VMware vSphere
|
|X
|
|

|====
[.small]
--
1. This platform uses the `ccoctl` utility during installation to configure long-term credentials.
--

[id="cco-determine-mode_{context}"]
== Determining the Cloud Credential Operator mode

For platforms that support using the CCO in multiple modes, you can determine what mode the CCO is configured to use by using the web console or the CLI.

.Determining the CCO configuration
image::334_OpenShift_cluster_updating_and_CCO_workflows_0923_4.11_A_AliCloud_patch.png[Decision tree showing how to determine the configured CCO credentials mode for your cluster.]

//Determining the Cloud Credential Operator mode by using the web console
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
// * authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.adoc

[id="cco-determine-mode-gui_{context}"]
= Determining the Cloud Credential Operator mode by using the web console

You can determine what mode the Cloud Credential Operator (CCO) is configured to use by using the web console.

[NOTE]
====
Only Amazon Web Services (AWS), global Microsoft Azure, and {gcp-first} clusters support multiple CCO modes.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator permissions.

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Navigate to *Administration* -> *Cluster Settings*.

. On the *Cluster Settings* page, select the *Configuration* tab.

. Under *Configuration resource*, select *CloudCredential*.

. On the *CloudCredential details* page, select the *YAML* tab.

. In the YAML block, check the value of `spec.credentialsMode`. The following values are possible, though not all are supported on all platforms:
+
--
* `''`: The CCO is operating in the default mode. In this configuration, the CCO operates in mint or passthrough mode, depending on the credentials provided during installation.
* `Mint`: The CCO is operating in mint mode.
* `Passthrough`: The CCO is operating in passthrough mode.
* `Manual`: The CCO is operating in manual mode.
--
+
[IMPORTANT]
====
To determine the specific configuration of an AWS, {gcp-short}, or global Microsoft Azure cluster that has a `spec.credentialsMode` of `''`, `Mint`, or `Manual`, you must investigate further.

AWS and {gcp-short} clusters support using mint mode with the root secret deleted.
If the cluster is specifically configured to use mint mode or uses mint mode by default, you must determine if the root secret is present on the cluster before updating.

An AWS, {gcp-short}, or global Microsoft Azure cluster that uses manual mode might be configured to create and manage cloud credentials from outside of the cluster with AWS STS, {gcp-short} Workload Identity, or {entra-first}. You can determine whether your cluster uses this strategy by examining the cluster `Authentication` object.
====

. AWS or {gcp-short} clusters that use the default (`''`) only: To determine whether the cluster is operating in mint or passthrough mode, inspect the annotations on the cluster root secret:

.. Navigate to *Workloads* -> *Secrets* and look for the root secret for your cloud provider.
+
[NOTE]
====
Ensure that the *Project* dropdown is set to *All Projects*.
====
+
[cols=2,options=header]
|===
|Platform
|Secret name

|AWS
|`aws-creds`

|{gcp-short}
|`gcp-credentials`

|===

.. To view the CCO mode that the cluster is using, click `1 annotation` under *Annotations*, and check the value field. The following values are possible:
+
--
* `Mint`: The CCO is operating in mint mode.
* `Passthrough`: The CCO is operating in passthrough mode.
--
+
If your cluster uses mint mode, you can also determine whether the cluster is operating without the root secret.

. AWS or {gcp-short} clusters that use mint mode only: To determine whether the cluster is operating without the root secret, navigate to *Workloads* -> *Secrets* and look for the root secret for your cloud provider.
+
[NOTE]
====
Ensure that the *Project* dropdown is set to *All Projects*.
====
+
[cols=2,options=header]
|===
|Platform
|Secret name

|AWS
|`aws-creds`

|{gcp-short}
|`gcp-credentials`

|===
+
--
* If you see one of these values, your cluster is using mint or passthrough mode with the root secret present.
* If you do not see these values, your cluster is using the CCO in mint mode with the root secret removed.
--

. AWS, {gcp-short}, or global Microsoft Azure clusters that use manual mode only: To determine whether the cluster is configured to create and manage cloud credentials from outside of the cluster, you must check the cluster `Authentication` object YAML values.

.. Navigate to *Administration* -> *Cluster Settings*.

.. On the *Cluster Settings* page, select the *Configuration* tab.

.. Under *Configuration resource*, select *Authentication*.

.. On the *Authentication details* page, select the *YAML* tab.

.. In the YAML block, check the value of the `.spec.serviceAccountIssuer` parameter.
+
--
* A value that contains a URL that is associated with your cloud provider indicates that the CCO is using manual mode with short-term credentials for components. These clusters are configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* An empty value (`''`) indicates that the cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility.
--

.Next steps

* If you are updating a cluster that has the CCO operating in mint or passthrough mode and the root secret is present, you do not need to update any cloud provider resources and can continue to the next part of the update process.

* If your cluster is using the CCO in mint mode with the root secret removed, you must reinstate the credential secret with the administrator-level credential before continuing to the next part of the update process.

* If your cluster was configured using the CCO utility (`ccoctl`), you must take the following actions:

.. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

.. Configure the `ccoctl` utility for the new release and use it to update the cloud provider resources.

.. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.

* If your cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility, you must take the following actions:

.. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

.. Manually update the cloud provider resources for the new release.

.. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.

//Determining the Cloud Credential Operator mode by using the CLI
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
// * authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.adoc

[id="cco-determine-mode-cli_{context}"]
= Determining the Cloud Credential Operator mode by using the CLI

You can determine what mode the Cloud Credential Operator (CCO) is configured to use by using the CLI.

[NOTE]
====
Only Amazon Web Services (AWS), global Microsoft Azure, and {gcp-first} clusters support multiple CCO modes.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator permissions.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Log in to `oc` on the cluster as a user with the `cluster-admin` role.

. To determine the mode that the CCO is configured to use, enter the following command:
+
[source,terminal]
----
$ oc get cloudcredentials cluster \
  -o=jsonpath={.spec.credentialsMode}
----
+
The following output values are possible, though not all are supported on all platforms:
+
--
* `''`: The CCO is operating in the default mode. In this configuration, the CCO operates in mint or passthrough mode, depending on the credentials provided during installation.
* `Mint`: The CCO is operating in mint mode.
* `Passthrough`: The CCO is operating in passthrough mode.
* `Manual`: The CCO is operating in manual mode.
--
+
[IMPORTANT]
====
To determine the specific configuration of an AWS, {gcp-short}, or global Microsoft Azure cluster that has a `spec.credentialsMode` of `''`, `Mint`, or `Manual`, you must investigate further.

AWS and {gcp-short} clusters support using mint mode with the root secret deleted.
If the cluster is specifically configured to use mint mode or uses mint mode by default, you must determine if the root secret is present on the cluster before updating.

An AWS, {gcp-short}, or global Microsoft Azure cluster that uses manual mode might be configured to create and manage cloud credentials from outside of the cluster with AWS STS, {gcp-short} Workload Identity, or {entra-first}. You can determine whether your cluster uses this strategy by examining the cluster `Authentication` object.
====

. AWS or {gcp-short} clusters that use the default (`''`) only: To determine whether the cluster is operating in mint or passthrough mode, run the following command:
+
[source,terminal]
----
$ oc get secret <secret_name> \
  -n kube-system \
  -o jsonpath \
  --template '{ .metadata.annotations }'
----
+
where `<secret_name>` is `aws-creds` for AWS or `gcp-credentials` for {gcp-short}.
+
This command displays the value of the `.metadata.annotations` parameter in the cluster root secret object. The following output values are possible:
+
--
* `Mint`: The CCO is operating in mint mode.
* `Passthrough`: The CCO is operating in passthrough mode.
--
+
If your cluster uses mint mode, you can also determine whether the cluster is operating without the root secret.

. AWS or {gcp-short} clusters that use mint mode only: To determine whether the cluster is operating without the root secret, run the following command:
+
[source,terminal]
----
$ oc get secret <secret_name> \
  -n=kube-system
----
+
where `<secret_name>` is `aws-creds` for AWS or `gcp-credentials` for {gcp-short}.
+
If the root secret is present, the output of this command returns information about the secret. An error indicates that the root secret is not present on the cluster.

. AWS, {gcp-short}, or global Microsoft Azure clusters that use manual mode only: To determine whether the cluster is configured to create and manage cloud credentials from outside of the cluster, run the following command:
+
[source,terminal]
----
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
----
+
This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object.
+
--
* An output of a URL that is associated with your cloud provider indicates that the CCO is using manual mode with short-term credentials for components. These clusters are configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* An empty output indicates that the cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility.
--

.Next steps

* If you are updating a cluster that has the CCO operating in mint or passthrough mode and the root secret is present, you do not need to update any cloud provider resources and can continue to the next part of the update process.

* If your cluster is using the CCO in mint mode with the root secret removed, you must reinstate the credential secret with the administrator-level credential before continuing to the next part of the update process.

* If your cluster was configured using the CCO utility (`ccoctl`), you must take the following actions:

.. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

.. Configure the `ccoctl` utility for the new release and use it to update the cloud provider resources.

.. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.

* If your cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility, you must take the following actions:

.. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

.. Manually update the cloud provider resources for the new release.

.. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.

[id="about-cloud-credential-operator-default_{context}"]
== Default behavior
For platforms on which multiple modes are supported (AWS, Azure, and {gcp-short}), when the CCO operates in its default mode, it checks the provided credentials dynamically to determine for which mode they are sufficient to process `CredentialsRequest` CRs.

By default, the CCO determines whether the credentials are sufficient for mint mode, which is the preferred mode of operation, and uses those credentials to create appropriate credentials for components in the cluster. If the credentials are not sufficient for mint mode, it determines whether they are sufficient for passthrough mode. If the credentials are not sufficient for passthrough mode, the CCO cannot adequately process `CredentialsRequest` CRs.

If the provided credentials are determined to be insufficient during installation, the installation fails. For AWS, the installation program fails early in the process and indicates which required permissions are missing. Other providers might not provide specific information about the cause of the error until errors are encountered.

If the credentials are changed after a successful installation and the CCO determines that the new credentials are insufficient, the CCO puts conditions on any new `CredentialsRequest` CRs to indicate that it cannot process them because of the insufficient credentials.

To resolve insufficient credentials issues, provide a credential with sufficient permissions. If an error occurred during installation, try installing again. For issues with new `CredentialsRequest` CRs, wait for the CCO to try to process the CR again. As an alternative, you can configure your cluster to use a different CCO mode that is supported for your cloud provider.

[role="_additional-resources"]
[id="additional-resources_about-cloud-credential-operator_{context}"]
== Additional resources

* Cluster Operators reference page for the Cloud Credential Operator
