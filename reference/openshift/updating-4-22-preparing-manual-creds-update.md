---
title: "Preparing to update a cluster with manually maintained credentials"
type: reference
domain: openshift
slug: updating-4-22-preparing-manual-creds-update
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/updating/preparing-manual-creds-update
version: 4.22
family: updating
documentKind: "Documentation"
---

# Preparing to update a cluster with manually maintained credentials

[id="preparing-manual-creds-update"]
= Preparing to update a cluster with manually maintained credentials

WARNING: This assembly has been moved into a subdirectory for 4.14+. Changes to this assembly for earlier versions should be done in separate PRs based off of their respective version branches. Otherwise, your cherry picks may fail.

To do: Remove this comment once 4.13 docs are EOL.

The Cloud Credential Operator (CCO) `Upgradable` status for a cluster with manually maintained credentials is `False` by default.

* For minor releases, for example, from 4.12 to 4.13, this status prevents you from updating until you have addressed any updated permissions and annotated the `CloudCredential` resource to indicate that the permissions are updated as needed for the next version. This annotation changes the `Upgradable` status to `True`.

* For z-stream releases, for example, from 4.13.0 to 4.13.1, no permissions are added or changed, so the update is not blocked.

Before updating a cluster with manually maintained credentials, you must accommodate any new or changed credentials in the release image for the version of OpenShift Container Platform you are updating to.

//Upgrading clusters with manually maintained credentials
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc

[id="about-manually-maintained-credentials-upgrade_{context}"]
= Update requirements for clusters with manually maintained credentials

Before you update a cluster that uses manually maintained credentials with the Cloud Credential Operator (CCO), you must update the cloud provider resources for the new release.

If the cloud credential management for your cluster was configured using the CCO utility (`ccoctl`), use the `ccoctl` utility to update the resources. Clusters that were configured to use manual mode without the `ccoctl` utility require manual updates for the resources.

After updating the cloud provider resources, you must update the `upgradeable-to` annotation for the cluster to indicate that it is ready to update.

[NOTE]
====
The process to update the cloud provider resources and the `upgradeable-to` annotation can only be completed by using command-line tools.
====

[id="cco-platform-options_{context}"]
== Cloud credential configuration options and update requirements by platform type

Some platforms only support using the CCO in one mode. For clusters that are installed on those platforms, the platform type determines the credentials update requirements.

For platforms that support using the CCO in multiple modes, you must determine which mode the cluster is configured to use and take the required actions for that configuration.

.Credentials update requirements by platform type
image::334_OpenShift_cluster_updating_and_CCO_workflows_0523_4.11_B_AliCloud_patch.png[Decision tree showing the possible update paths for your cluster depending on the configured CCO credentials mode.]

{rh-openstack-first} and VMware vSphere::
These platforms do not support using the CCO in manual mode. Clusters on these platforms handle changes in cloud provider resources automatically and do not require an update to the `upgradeable-to` annotation.
+
Administrators of clusters on these platforms should skip the manually maintained credentials section of the update process.

{ibm-cloud-title} and Nutanix::
Clusters installed on these platforms are configured using the `ccoctl` utility.
+
Administrators of clusters on these platforms must take the following actions:
+
. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
. Configure the `ccoctl` utility for the new release and use it to update the cloud provider resources.
. Indicate that the cluster is ready to update with the `upgradeable-to` annotation.

Microsoft Azure Stack Hub::
These clusters use manual mode with long-term credentials and do not use the `ccoctl` utility.
+
Administrators of clusters on these platforms must take the following actions:
+
. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
. Manually update the cloud provider resources for the new release.
. Indicate that the cluster is ready to update with the `upgradeable-to` annotation.

Amazon Web Services (AWS), global Microsoft Azure, and {gcp-first}::
Clusters installed on these platforms support multiple CCO modes.
+
The required update process depends on the mode that the cluster is configured to use. If you are not sure what mode the CCO is configured to use on your cluster, you can use the web console or the CLI to determine this information.

[role="_additional-resources"]
.Additional resources
* Determining the Cloud Credential Operator mode by using the web console
* Determining the Cloud Credential Operator mode by using the CLI
* Extracting and preparing credentials request resources
* About the Cloud Credential Operator

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

[role="_additional-resources"]
.Additional resources
* Extracting and preparing credentials request resources

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

[role="_additional-resources"]
.Additional resources
* Extracting and preparing credentials request resources

//Extracting and preparing credentials request resources
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc

[id="cco-ccoctl-upgrading-extracting_{context}"]
= Extracting and preparing credentials request resources

Before updating a cluster that uses the Cloud Credential Operator (CCO) in manual mode, you must extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

.Prerequisites

* Install the {oc-first} that matches the version for your updated version.
* Log in to the cluster as user with `cluster-admin` privileges.

.Procedure

. Obtain the pull spec for the update that you want to apply by running the following command:
+
[source,terminal]
----
$ oc adm upgrade
----
+
The output of this command includes pull specs for the available updates similar to the following:
+
.Partial example output
[source,text]
----
...
Recommended updates:

VERSION IMAGE
4.22.0  quay.io/openshift-release-dev/ocp-release@sha256:6a899c54dda6b844bb12a247e324a0f6cde367e880b73ba110c056df6d018032
...
----

. Set a `$RELEASE_IMAGE` variable with the release image that you want to use by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=<update_pull_spec>
----
+
where `<update_pull_spec>` is the pull spec for the release image that you want to use. For example:
+
[source,text]
----
quay.io/openshift-release-dev/ocp-release@sha256:6a899c54dda6b844bb12a247e324a0f6cde367e880b73ba110c056df6d018032
----

. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \// <1>
  --to=<path_to_directory_for_credentials_requests> <2>
----
<1> The `--included` parameter includes only the manifests that your specific cluster configuration requires for the target release.
<2> Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
This command creates a YAML file for each `CredentialsRequest` object.

. For each `CredentialsRequest` CR in the release image, ensure that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster. This field is where the generated secrets that hold the credentials configuration are stored.
+
.Sample AWS `CredentialsRequest` object
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: cloud-credential-operator-iam-ro
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - iam:GetUser
      - iam:GetUserPolicy
      - iam:ListAccessKeys
      resource: "*"
  secretRef:
    name: cloud-credential-operator-iam-ro-creds
    namespace: openshift-cloud-credential-operator <1>
----
<1> This field indicates the namespace which must exist to hold the generated secret.
+
The `CredentialsRequest` CRs for other platforms have a similar format with different platform-specific values.

. For any `CredentialsRequest` CR for which the cluster does not already have a namespace with the name specified in `spec.secretRef.namespace`, create the namespace by running the following command:
+
[source,terminal]
----
$ oc create namespace <component_namespace>
----

.Next steps

* If the cloud credential management for your cluster was configured using the CCO utility (`ccoctl`), configure the `ccoctl` utility for a cluster update and use it to update your cloud provider resources.

* If your cluster was not configured with the `ccoctl` utility, manually update your cloud provider resources.

[role="_additional-resources"]
.Additional resources
* Configuring the Cloud Credential Operator utility for a cluster update
* Manually updating cloud provider resources

//Configuring the Cloud Credential Operator utility for a cluster update
// Module included in the following assemblies:
//
//Postinstall and update content
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
//
//Platforms that must use `ccoctl` and update content
// * installing/installing_ibm_cloud/configuring-iam-ibm-cloud.adoc
// * installing/installing_ibm_powervs/preparing-to-install-on-ibm-power-vs.doc
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Postinstall  and update content

//Platforms that must use `ccoctl`

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-configuring_{context}"]

[role="_abstract"]
//Nutanix-only intro because it needs context in its install procedure.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on {ibm-power-server-name}, you must set the CCO to `manual` mode as part of the installation process.

//The upgrade and postinstall procs also have a different intro, so they are excluded here.
To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

//Intro for the postinstall procs.
To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary.

//Intro for the upgrade procs.
To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

[NOTE]
====
The `ccoctl` utility is a Linux binary that must run in a Linux environment.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the {oc-first}.

//Upgrade prereqs
* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

//Permissions requirements (per platform, for install and key rotation)

.Procedure

. Set a variable for the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
----
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
----

. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
----
+
[NOTE]
====
Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
====

. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
----
+
For `<rhel_version>`, specify the value that corresponds to the version of {op-system-base-full} that the host uses.
If no value is specified, `ccoctl.rhel8` is used by default.
The following values are valid:
+
* `rhel8`: Specify this value for hosts that use {op-system-base} 8.
* `rhel9`: Specify this value for hosts that use {op-system-base} 9.

+
[NOTE]
====
The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
====

. Change the permissions to make `ccoctl` executable by running the following command:
+
[source,terminal]
----
$ chmod 775 ccoctl
----

.Verification

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:
+
[source,terminal]
----
$ ./ccoctl
----
+
.Example output
[source,terminal]
----
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
----

//Postinstall and update content

//Platforms that must use `ccoctl` and update content

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Updating cloud provider resources with the Cloud Credential Operator utility
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc

[id="cco-ccoctl-upgrading_{context}"]
= Updating cloud provider resources with the Cloud Credential Operator utility

[role="_abstract"]
Update the cloud provider resources for your OpenShift Container Platform cluster by using the CCO utility (`ccoctl`). The process for upgrading these resources is similar to creating the resources during installation.

[NOTE]
====
On AWS clusters, some `ccoctl` commands make AWS API calls to create or modify AWS resources. You can use the `--dry-run` flag to avoid making API calls. Using this flag creates JSON files on the local file system instead. You can review and modify the JSON files and then apply them with the AWS CLI tool using the `--cli-input-json` parameters.
====

.Prerequisites

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

* You have extracted and configured the `ccoctl` binary from the release image.

.Procedure

. Create the output directory if it does not already exist by running the following command:
+
[source,terminal]
----
$ mkdir -p <path_to_ccoctl_output_dir>
----

. Extract the bound service account signing key from the cluster and save it to the output directory by running the following command:
+
[source,terminal]
----
$ oc get secret bound-service-account-signing-key \
  -n openshift-kube-apiserver \
  -ojsonpath='{ .data.service-account\.pub }' | base64 \
  -d > <path_to_ccoctl_output_dir>/serviceaccount-signer.public
----

. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the command for your cloud provider. The following commands process `CredentialsRequest` objects:
+
.Amazon Web Services (AWS)
[%collapsible]
====
[source,terminal]
----
$ ccoctl aws create-all \// <1>
  --name=<name> \// <2>
  --region=<aws_region> \// <3>
  --credentials-requests-dir=<path_to_credentials_requests_directory> \// <4>
  --output-dir=<path_to_ccoctl_output_dir> \// <5>
  --public-key-file=<path_to_ccoctl_output_dir>/serviceaccount-signer.public \// <6>
  --create-private-s3-bucket \// <7>
  --permissions-boundary-arn=<policy_arn> <8>
----
<1> To create the AWS resources individually, use the "Creating AWS resources individually" procedure in the "Installing a cluster on AWS with customizations" content. This option might be useful if you need to review the JSON files that the `ccoctl` tool creates before modifying AWS resources, or if the process the `ccoctl` tool uses to create AWS resources automatically does not meet the requirements of your organization.
<2> Specify the name used to tag any cloud resources that are created for tracking.
<3> Specify the AWS region in which cloud resources will be created.
<4> Specify the directory containing the files for the component `CredentialsRequest` objects.
<5> Specify the path to the output directory.
<6> Specify the path to the `serviceaccount-signer.public` file that you extracted from the cluster.
<7> Optional: By default, the `ccoctl` utility stores the OpenID Connect (OIDC) configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. To store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL instead, use the `--create-private-s3-bucket` parameter.
<8> Optional: Specify the Amazon Resource Name (ARN) of the {aws-short} IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility.
====
+
.{gcp-first}
[%collapsible]
====
[source,terminal]
----
$ ccoctl gcp create-all \
  --name=<name> \// <1>
  --region=<gcp_region> \// <2>
  --project=<gcp_project_id> \// <3>
  --credentials-requests-dir=<path_to_credentials_requests_directory> \// <4>
  --output-dir=<path_to_ccoctl_output_dir> \// <5>
  --public-key-file=<path_to_ccoctl_output_dir>/serviceaccount-signer.public \// <6>
  --key-storage-method=<key_storage_method> <7>
----
<1> Specify the user-defined name for all created {gcp-short} resources used for tracking.
<2> Specify the {gcp-short} region in which cloud resources will be created.
<3> Specify the {gcp-short} project ID in which cloud resources will be created.
<4> Specify the directory containing the files of `CredentialsRequest` manifests to create {gcp-short} service accounts.
<5> Specify the path to the output directory.
<6> Specify the path to the `serviceaccount-signer.public` file that you extracted from the cluster.
<7> Optional: Specify the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket.
+
[NOTE]
=====
If your cluster was previously configured with the `public-bucket` method and you switch to `pool-jwk-file`, the existing GCS bucket is no longer used. You can delete the old `<name>-oidc` bucket from your {gcp-short} project to avoid retaining an unnecessary public resource.
=====
====
+
.{ibm-cloud-title}
[%collapsible]
====
[source,terminal]
----
$ ccoctl ibmcloud create-service-id \
  --credentials-requests-dir=<path_to_credential_requests_directory> \// <1>
  --name=<cluster_name> \// <2>
  --output-dir=<installation_directory> \// <3>
  --resource-group-name=<resource_group_name> <4>
----
<1> Specify the directory containing the files for the component `CredentialsRequest` objects.
<2> Specify the name of the OpenShift Container Platform cluster.
<3> Optional: Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.
<4> Optional: Specify the name of the resource group used for scoping the access policies.
====
+
.{azure-first}
[%collapsible]
====
[source,terminal]
----
$ ccoctl azure create-managed-identities \
  --name <azure_infra_name> \// <1>
  --output-dir=<path_to_ccoctl_output_dir> \// <2>
  --region <azure_region> \// <3>
  --subscription-id <azure_subscription_id> \// <4>
  --credentials-requests-dir <path_to_directory_for_credentials_requests> \// <5>
  --issuer-url "${OIDC_ISSUER_URL}" \// <6>
  --dnszone-resource-group-name <azure_dns_zone_resourcegroup_name> \// <7>
  --installation-resource-group-name "${AZURE_INSTALL_RG}" \// <8>
  --preserve-existing-roles <9>
----
<1> The value of the `name` parameter is used to create an Azure resource group.
To use an existing Azure resource group instead of creating a new one, specify the `--oidc-resource-group-name` argument with the existing group name as its value.
<2> Specify the path to the output directory.
<3> Specify the region of the existing cluster.
<4> Specify the subscription ID of the existing cluster.
<5> Specify the directory containing the files for the component `CredentialsRequest` objects.
<6> Specify the OIDC issuer URL from the existing cluster.
You can obtain this value by running the following command:
+
[source,terminal]
----
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
----
<7> Specify the name of the resource group that contains the DNS zone.
<8> Specify the {azure-short} resource group name.
You can obtain this value by running the following command:
+
[source,terminal]
----
$ oc get infrastructure cluster \
  -o jsonpath \
  --template '{ .status.platformStatus.azure.resourceGroupName }'
----
<9> Optional: Specify this flag to ensure that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates.
====
+
.Nutanix
[%collapsible]
====
[source,terminal]
----
$ ccoctl nutanix create-shared-secrets \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \// <1>
  --output-dir=<ccoctl_output_dir> \// <2>
  --credentials-source-filepath=<path_to_credentials_file> <3>
----
<1> Specify the path to the directory that contains the files for the component `CredentialsRequests` objects.
<2> Optional: Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.
<3> Optional: Specify the directory that contains the credentials data YAML file. By default, `ccoctl` expects this file to be in `<home_directory>/.nutanix/credentials`.
====
+
For each `CredentialsRequest` object, `ccoctl` creates the required provider resources and a permissions policy as defined in each `CredentialsRequest` object from the OpenShift Container Platform release image.

. Apply the secrets to your cluster by running the following command:
+
[source,terminal]
----
$ ls <path_to_ccoctl_output_dir>/manifests/*-credentials.yaml | xargs -I{} oc apply -f {}
----

.Verification

You can verify that the required provider resources and permissions policies are created by querying the cloud provider. For more information, refer to your cloud provider documentation on listing roles or service accounts.

.Next steps

* Update the `upgradeable-to` annotation to indicate that the cluster is ready to upgrade.

[role="_additional-resources"]
.Additional resources
* Indicating that the cluster is ready to upgrade

//Manually updating cloud provider resources
// Module included in the following assemblies:
//
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc

[id="manually-maintained-credentials-upgrade_{context}"]
= Manually updating cloud provider resources

Before upgrading a cluster with manually maintained credentials, you must create secrets for any new credentials for the release image that you are upgrading to. You must also review the required permissions for existing credentials and accommodate any new permissions requirements in the new release for those components.

.Prerequisites

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

.Procedure

. Create YAML files with secrets for any `CredentialsRequest` custom resources that the new release image adds. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.
+
.Sample AWS YAML files
[%collapsible]
====
.Sample AWS `CredentialsRequest` object with secrets
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - s3:CreateBucket
      - s3:DeleteBucket
      resource: "*"
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
----

.Sample AWS `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  aws_access_key_id: <base64_encoded_aws_access_key_id>
  aws_secret_access_key: <base64_encoded_aws_secret_access_key>
----
====
+
.Sample Azure YAML files
[%collapsible]
====
[NOTE]
=====
Global Azure and Azure Stack Hub use the same `CredentialsRequest` object and secret formats.
=====
.Sample Azure `CredentialsRequest` object with secrets
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
----

.Sample Azure `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  azure_subscription_id: <base64_encoded_azure_subscription_id>
  azure_client_id: <base64_encoded_azure_client_id>
  azure_client_secret: <base64_encoded_azure_client_secret>
  azure_tenant_id: <base64_encoded_azure_tenant_id>
  azure_resource_prefix: <base64_encoded_azure_resource_prefix>
  azure_resourcegroup: <base64_encoded_azure_resourcegroup>
  azure_region: <base64_encoded_azure_region>
----
====
+
.Sample {gcp-short} YAML files
[%collapsible]
====
.Sample {gcp-short} `CredentialsRequest` object with secrets
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: GCPProviderSpec
      predefinedRoles:
      - roles/iam.securityReviewer
      - roles/iam.roleViewer
      skipServiceCheck: true
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
----

.Sample {gcp-short} `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  service_account.json: <base64_encoded_gcp_service_account_file>
----
====

. If the `CredentialsRequest` custom resources for any existing credentials that are stored in secrets have changed permissions requirements, update the permissions as required.

.Next steps
* Update the `upgradeable-to` annotation to indicate that the cluster is ready to upgrade.

[role="_additional-resources"]
.Additional resources
* Manually creating long-term credentials for AWS
* Manually creating long-term credentials for Azure
* Manually creating long-term credentials for Azure Stack Hub
* Manually creating long-term credentials for {gcp-short}
* Indicating that the cluster is ready to upgrade

//Indicating that the cluster is ready to upgrade
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-mode-manual.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc

[id="cco-manual-upgrade-annotation_{context}"]
= Indicating that the cluster is ready to upgrade

The Cloud Credential Operator (CCO) `Upgradable` status for a cluster with manually maintained credentials is `False` by default.

.Prerequisites

* For the release image that you are upgrading to, you have processed any new credentials manually or by using the Cloud Credential Operator utility (`ccoctl`).
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Log in to `oc` on the cluster as a user with the `cluster-admin` role.

. Edit the `CloudCredential` resource to add an `upgradeable-to` annotation within the `metadata` field by running the following command:
+
[source,terminal]
----
$ oc edit cloudcredential cluster
----
+
.Text to add
+
[source,yaml]
----
...
  metadata:
    annotations:
      cloudcredential.openshift.io/upgradeable-to: <version_number>
...
----
+
Where `<version_number>` is the version that you are upgrading to, in the format `x.y.z`. For example, use `4.12.2` for OpenShift Container Platform 4.12.2.
+
It may take several minutes after adding the annotation for the upgradeable status to change.

.Verification

//Would like to add CLI steps for same
. In the *Administrator* perspective of the web console, navigate to *Administration* -> *Cluster Settings*.

. To view the CCO status details, click *cloud-credential* in the *Cluster Operators* list.
+
--
* If the *Upgradeable* status in the *Conditions* section is *False*, verify that the `upgradeable-to` annotation is free of typographical errors.
--

. When the *Upgradeable* status in the *Conditions* section is *True*, begin the OpenShift Container Platform upgrade.
