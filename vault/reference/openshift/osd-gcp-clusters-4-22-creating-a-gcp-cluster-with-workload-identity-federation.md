---
title: "Creating a cluster on {gcp-short} with Workload Identity Federation authentication"
type: reference
domain: openshift
slug: osd-gcp-clusters-4-22-creating-a-gcp-cluster-with-workload-identity-federation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_gcp_clusters/creating-a-gcp-cluster-with-workload-identity-federation
version: 4.22
family: osd_gcp_clusters
documentKind: "Documentation"
---

# Creating a cluster on {gcp-short} with Workload Identity Federation authentication

[id="osd-creating-a-cluster-on-gcp-with-workload-identity-federation"]
= Creating a cluster on {gcp-short} with Workload Identity Federation authentication

[role="_abstract"]
As a system administrator or cloud engineer, you can provision an OpenShift Container Platform cluster on {GCP} using Workload Identity Federation (WIF). This feature establishes a trust relationship that allows your cluster's control plane and workloads to securely assume the necessary {GCP} roles and access required services. This approach eliminates the security risk and operational overhead associated with managing and rotating long-lived {GCP} service account keys.

// Module included in the following assemblies:
//
// *osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="workload-identity-federation-overview_{context}"]
= Workload Identity Federation overview

[role="_abstract"]
Workload Identity Federation (WIF) is a {GCP} Identity and Access Management (IAM) feature that provides third parties a secure method to access resources on a customer's cloud account. WIF eliminates the need for service account keys, and is {gcp-full}'s preferred method of credential authentication.

While service account keys can provide powerful access to your {gcp-full} resources, they must be maintained by the user and can be a security risk if they are not managed properly. WIF does not use service keys as an access method for your {gcp-full} resources. Instead, WIF grants access by using credentials from external identity providers to generate short-lived credentials for workloads. The workloads can then use these credentials to temporarily impersonate service accounts and access {gcp-full} resources. This removes the burden of having to properly maintain service account keys, and removes the risk of unauthorized users gaining access to service account keys.

The following bulleted items provides a basic overview of the Workload Identity Federation process:

* The owner of the {GCP} project configures a workload identity pool with an identity provider, allowing OpenShift Container Platform to  access the project's associated service accounts using short-lived credentials.
* This workload identity pool is configured to authenticate requests using an Identity Provider (IP) that the user defines.
* For applications to get access to cloud resources, they first pass credentials to Google's Security Token Service (STS). STS uses the specified identity provider to verify the credentials.
* Once the credentials are verified, STS returns a temporary access token to the caller, giving the application the ability to impersonate the service account bound to that identity.

Operators also need access to cloud resources. By using WIF instead of service account keys to grant this access, cluster security is further strengthened, as service account keys are no longer stored in the cluster. Instead, operators are given temporary access tokens that impersonate the service accounts. These tokens are short-lived and regularly rotated.

// * External applications authenticate to the identity provider.
// * The external application calls Google Security Token Service to exchange the account credentials for a short-lived Google Cloud access token.
// * The token can then be used to impersonate a service account and access Google Cloud resources.

For more information about Workload Identity Federation, see the {gcp-full} documentation.

[IMPORTANT]
====
Workload Identity Federation (WIF) is only available on OpenShift Container Platform version 4.17 and later, and is only supported by the Customer Cloud Subscription (CCS) infrastructure type.
====

[id="osd-creating-a-cluster-on-gcp-prerequisites1_{context}"]
== Prerequisites

* You have confirmed your {gcp-full} account has the necessary resource quotas and limits to support your desired cluster size according to the cluster resource requirements. For more information regarding resource quotas and limits, see _Additional resources_.
* You have reviewed the introduction to OpenShift Container Platform and the documentation on architecture concepts.
* You have reviewed the OpenShift Container Platform cloud deployment options.
* You have read and completed the Required customer procedure.
* You have downloaded the latest version of the {cluster-manager} CLI (`ocm`) for your operating system from the Downloads page on {cluster-manager}.
+
[IMPORTANT]
====
[subs="attributes+"]
The `ocm` is a Developer Preview feature only.
For more information about the support scope of Red Hat Developer Preview features, see Developer Preview Support Scope.
====
+
* You have created a Workload Identity Federation configuration. For more information, see _Creating a Workload Identity Federation configuration_.

[NOTE]
====
WIF supports the deployment of a private OpenShift Container Platform on {GCP} cluster with Private Service Connect (PSC). Red{nbsp}Hat recommends using PSC when deploying private clusters.
For more information about the prerequisites for PSC, see Prerequisites for Private Service Connect.
====

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="create-wif-configuration_{context}"]
= Creating a Workload Identity Federation configuration

[role="_abstract"]
You can create a WIF configuration using the `auto` mode or the `manual` mode in the `ocm` CLI.

The `auto` mode enables you to automatically create the service accounts for OpenShift Container Platform components as well as other IAM resources.

Alternatively, you can use the `manual` mode. In `manual` mode, you are provided with commands within a `script.sh` file which you use to manually create the service accounts for OpenShift Container Platform components as well as other IAM resources.

.Procedure

* Based on your mode preference, run one of the following commands to create a WIF configuration:

** Create a WIF configuration in auto mode by running the following command:
+
[source,terminal]
----
$ ocm gcp create wif-config --name <wif_name> \ <1>
  --project <gcp_project_id> \ <2>
  --version <osd_version> <3>
  --federated-project <gcp_project_id> <4>
----
<1> Replace `<wif_name>` with the name of your WIF configuration.
<2> Replace `<gcp_project_id>` with the ID of the {GCP} project where the WIF configuration will be implemented.
<3> Optional: Replace `<osd_version>` with the desired OpenShift Container Platform version the wif-config will need to support. If you do not specify a version, the wif-config will support the latest OpenShift Container Platform y-stream version as well as the last three supported OpenShift Container Platform y-stream versions (beginning with version 4.17).
<4> Optional: Replace `<gcp_project_id>` with the ID of the dedicated project where the workload identity pools and providers will be created and managed. If the `--federated-project` flag is not specified, the workload identity pools and providers will be created and managed in the project specified by the `--project` flag.
+
[IMPORTANT]
=====
Using a dedicated project to create and manage workload identity pools and providers is recommended by {GCP}.
Using a dedicated project helps you to establish centralized governance over the configuration of workload identity pools and providers, enforce uniform attribute mappings and conditions throughout all projects and applications, and ensure that only authorized identity providers can authenticate with WIF.

Creating and managing workload identity pools and providers in a dedicated project is only allowed during initial WIF configuration creation. The `--federated-project` flag cannot be applied to existing `wif-configs`.

For more information, see Use a dedicated project to manage workload identity pools and providers.
=====
+
--
**Example output**
[source,terminal]
----
2024/09/26 13:05:41 Creating workload identity configuration...
2024/09/26 13:05:47 Workload identity pool created with name 2e1kcps6jtgla8818vqs8tbjjls4oeub
2024/09/26 13:05:47 workload identity provider created with name oidc
2024/09/26 13:05:48 IAM service account osd-worker-oeub created
2024/09/26 13:05:49 IAM service account osd-control-plane-oeub created
2024/09/26 13:05:49 IAM service account openshift-gcp-ccm-oeub created
2024/09/26 13:05:50 IAM service account openshift-gcp-pd-csi-driv-oeub created
2024/09/26 13:05:50 IAM service account openshift-image-registry-oeub created
2024/09/26 13:05:51 IAM service account openshift-machine-api-gcp-oeub created
2024/09/26 13:05:51 IAM service account osd-deployer-oeub created
2024/09/26 13:05:52 IAM service account cloud-credential-operator-oeub created
2024/09/26 13:05:52 IAM service account openshift-cloud-network-c-oeub created
2024/09/26 13:05:53 IAM service account openshift-ingress-gcp-oeub created
2024/09/26 13:05:55 Role "osd_deployer_v4.19" updated
----
--
+
** Create a WIF configuration in manual mode by running the following command:
+
[source,terminal]
----
$ ocm gcp create wif-config --name <wif_name> \ <1>
  --project <gcp_project_id> \ <2>
  --mode=manual
----
<1> Replace `<wif_name>` with the name of your WIF configuration.
<2> Replace `<gcp_project_id>` with the ID  of the {GCP} project where the WIF configuration will be implemented.
+
Once the WIF is configured, the following service accounts, roles, and groups are created.
+
[NOTE]
====
Red{nbsp}Hat custom roles are versioned with every OpenShift y-stream release, for example 4.19.
====
+
.WIF configuration service accounts, group and roles
[cols="2a,3a",options="header"]
|===

|Service Account/Group
|{gcp-short} pre-defined roles and Red Hat custom roles

|osd-deployer
|osd_deployer_v<y-stream-version>

|osd-control-plane
|- compute.instanceAdmin
- compute.networkAdmin
- compute.securityAdmin
- compute.storageAdmin

|osd-worker
|- compute.storageAdmin
- compute.viewer

|cloud-credential-operator-gcp-ro-creds
|cloud_credential_operator_gcp_ro_creds_v<y-stream-version>

|openshift-cloud-network-config-controller-gcp
|openshift_cloud_network_config_controller_gcp_v<y-stream-version>

|openshift-gcp-ccm
|openshift_gcp_ccm_v<y-stream-version>

|openshift-gcp-pd-csi-driver-operator
|- compute.storageAdmin
- iam.serviceAccountUser
- resourcemanager.tagUser
- openshift_gcp_pd_csi_driver_operator_v<y-stream-version>

|openshift-image-registry-gcp
|openshift_image_registry_gcs_v<y-stream-version>

|openshift-ingress-gcp
|openshift_ingress_gcp_v<y-stream-version>

|openshift-machine-api-gcp
|openshift_machine_api_gcp_v<y-stream-version>

|Access via SRE group:sd-sre-platform-gcp-access
|sre_managed_support
|===
+
For the complete list of WIF configuration roles and their assigned permissions, see managed-cluster-config.

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="create-wif-cluster-ocm_{context}"]
= Creating a Workload Identity Federation cluster using {cluster-manager}

[role="_abstract"]
Follow the steps in this procedure to create an OpenShift Container Platform cluster on {gcp-full} using Workload Identity Federation (WIF) for authentication through the {cluster-manager} web console

.Prerequisites

* You have created a WIF configuration. For more information, see "Creating a Workload Identity Federation configuration".
* You have access to the {cluster-manager} web console. For more information, see _Accessing {cluster-manager}_ in the _Additional resources_ section.

.Procedure

. Log in to {cluster-manager-url} and click *Create cluster* on the OpenShift Container Platform card.

. Under *Billing model*, configure the subscription type and infrastructure type.

.. Select a subscription type. For information about OpenShift Container Platform subscription options, see Cluster subscriptions and registration in the {cluster-manager} documentation.
+

.. Select the *Customer cloud subscription* infrastructure type.

.. Click *Next*.
. Select *Run on {gcp-full}*.
. Select *Workload Identity Federation* as the Authentication type.
//Add back in default authentication type when feature goes live.
+
[NOTE]
====
Workload Identity Federation (WIF) is {gcp-full}'s recommended method of authentication for OpenShift Container Platform installation. It greatly improves a cluster's resilience by using short-lived, least-privilege credentials and eliminates the need for static service account keys.
====
+
.. Read and complete all the required prerequisites.

.. Click the checkbox indicating that you have read and completed all the required prerequisites.
. Select a configured WIF configuration from the *WIF configuration* drop-down list.
. Click *Next*.
. On the *Details* page, provide a name for your cluster and specify the cluster details:
.. In the *Cluster name* field, enter a name for your cluster.
.. Optional: Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated as a 15-character string.
+
To customize the subdomain prefix, select the *Create custom domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field. The domain prefix cannot be longer than 15 characters, must be unique within your organization, and cannot be changed after cluster creation. If you plan to install the cluster into a Shared VPC and select a managed DNS zone in a later step, the *DNS Zone* list is filtered to show only zones that begin with this domain prefix; ensure the prefix matches the managed DNS zones you have created or intend to use.
.. Select a cluster version from the *Version* drop-down menu.
+
[NOTE]
====
Workload Identity Federation (WIF) is only supported on OpenShift Container Platform version 4.17 and later.
====
+
.. Select a channel from the *Channel* drop-down menu.
+
--
--
+
.. Select a cloud provider region from the *Region* drop-down menu.
.. Select a *Single zone* or *Multi-zone* configuration.
+
.. Optional: Select *Enable Secure Boot support for Shielded VMs* to use Shielded VMs when installing your cluster. Once you create your cluster, the *Enable Secure Boot support for Shielded VMs* setting cannot be changed. For more information, see Shielded VMs.
+
[IMPORTANT]
====
To successfully create a cluster, you must select *Enable Secure Boot support for Shielded VMs* if your organization has the policy constraint `constraints/compute.requireShieldedVm` enabled. For more information regarding {gcp-short} organizational policy constraints, see Organization policy constraints.
====
+
[IMPORTANT]
====
*Enable Secure Boot support for Shielded VMs* is not supported for OpenShift Container Platform on {GCP} clusters created using bare-metal instance types. For more information, see Limitations in the {gcp-full} documentation.
====
+
.. Leave *Enable user workload monitoring* selected to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics. This option is enabled by default.

. Optional: Expand *Advanced Encryption* to make changes to encryption settings.

.. Select *Use custom KMS keys* to use custom KMS keys. If you prefer not to use custom KMS keys, leave the default setting *Use default KMS Keys*.

.. With *Use Custom KMS keys* selected:

... Select a key ring location from the *Key ring location* drop-down menu.
... Select a key ring from the *Key ring* drop-down menu.
... Select a key name from the *Key name* drop-down menu.
... Provide the *KMS Service Account*.

.. Optional: Select *Enable FIPS cryptography* if you require your cluster to be FIPS validated.
+
[NOTE]
====
If *Enable FIPS cryptography* is selected, *Enable additional etcd encryption* is enabled by default and cannot be disabled. You can select *Enable additional etcd encryption* without selecting *Enable FIPS cryptography*.
====
+
.. Optional: Select *Enable additional etcd encryption* if you require etcd key value encryption.
With this option, the etcd key values are encrypted, but not the keys. This option is in addition to the control plane storage encryption that encrypts the etcd volumes in OpenShift Container Platform clusters by default.
+
[NOTE]
====
By enabling etcd encryption for the key values in etcd, you incur a performance overhead of approximately 20%. The overhead is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Consider enabling etcd encryption only if you specifically require it for your use case.
====
+
. Click *Next*.

. On the *Machine pool* page, select a *Compute node instance type* and a *Compute node count*. The number and types of nodes that are available depend on your OpenShift Container Platform subscription. If you are using multiple availability zones, the compute node count is per zone.

. Optional: Expand *Add node labels* to add labels to your nodes. Click *Add additional label* to add more node labels.
+
[IMPORTANT]
====
This step refers to labels within Kubernetes, not {gcp-full}. For more information regarding Kubernetes labels, see Labels and Selectors.
====
+
. Click *Next*.

. In the *Cluster privacy* dialog, select *Public* or *Private* to use either public or private API endpoints and application routes for your cluster. If you select *Private*, *Use Private Service Connect* is selected by default, and cannot be disabled. Private Service Connect (PSC) is {gcp-full}’s security-enhanced networking feature.

. Optional: To install the cluster in an existing {gcp-short} Virtual Private Cloud (VPC):
.. Select *Install into an existing VPC*.
+
[IMPORTANT]
====
Private Service Connect is supported only with *Install into an existing VPC*.
====
+
.. If you are installing into an existing VPC and you want to enable an HTTP or HTTPS proxy for your cluster, select *Configure a cluster-wide proxy*.
+
. Accept the default application ingress settings, or to create your own custom settings, select *Custom Settings*. All of the custom settings are optional.
.. In *Route selector*, enter a comma-separated list of `key=value` pairs to limit which routes this ingress exposes.
Leave the field empty if all routes should remain eligible based on your other choices.
.. In *Excluded namespaces*, enter a comma-separated list of namespace names whose routes must not use this ingress.
.. In *Exclude namespace selectors*, specify one or more label selectors. For each selector, provide a label key and a comma-separated list of label values. The default Ingress Controller does not apply to namespaces whose labels satisfy any of the configured selectors.
+
[IMPORTANT]
====
Do not include spaces around commas, for example, use `finance,HR,legal`, and not `finance, HR, legal`.
====
+
.. Set *Namespace ownership policy* for route admission when namespaces share hostnames, for example, select *Strict* for restrictive admission.
.. Set *Wildcard policy* to allow or disallow wildcard patterns in route hostnames, for example, select *Disallowed* to block wildcard host routes.
+
For more information about custom application ingress settings, click on the information icon provided for each setting.

. Click *Next*.

. Optional: To install the cluster into a {gcp-short} Shared VPC, follow these steps.
+
--
--
.. Select *Install into {gcp-short} Shared VPC*.
.. Specify the *Host project ID*. If the specified host project ID is incorrect, cluster creation fails.
+
[NOTE]
====
In a typical Shared VPC deployment, the following {gcp-short} roles are required on the project hosting the VPC:

* `roles/compute.networkAdmin`
* `roles/compute.securityAdmin`
* `roles/dns.admin`

If you use a managed DNS zone (by selecting a zone from the *DNS Zone* list), the `roles/dns.admin` role is not required on the host project.
====
+
.. Optional. To use a pre-created DNS zone and reduce host project permissions, complete the following actions:
... View the provided CLI command instructions to create a zone if you have not already done so. For more information about creating a DNS zone using the ocm CLI, see _Creating a managed DNS zone_ in the _Additional resources_ section.
... Click the **Refresh** button to update the list of available zones.
... Select your preferred zone from the **DNS Zone** list. The list displays the zone ID alongside the {GCP} project and managed zone ID for easy identification.
+
[NOTE]
====
A custom domain prefix must be specified on a previous step  on the *Details* page before zones appear in the *DNS Zone* list. The *DNS Zone* list is filtered to show only zones that begin with the domain prefix you specified. The list may be empty if no matching DNS zones exist, or if the domain prefix was entered incorrectly. If the list is empty, verify your domain prefix and ensure you have created a managed DNS zone with a matching prefix.
====
+
If no zone is selected, the installer will attempt to create one automatically, which requires higher-level permissions in the host project.

+
. If you opted to install the cluster in an existing {GCP} VPC, provide your VPC subnet settings and select *Next*. You must ensure that your VPC is configured to allow outbound internet access to the domains required for the OpenShift Container Platform service. This outbound access is required for the OpenShift Container Platform service to communicate with Red{nbsp}Hat's management plane and SRE tooling via secure and encrypted endpoints over the public internet.
+
[NOTE]
====
If you are installing a cluster into a Shared VPC, the VPC name and subnets are shared from the host project.
====
. Click *Next*.
. If you opted to configure a cluster-wide proxy, provide your proxy configuration details on the *Cluster-wide proxy* page:
+
.. Enter a value in at least one of the following fields:
** Specify a valid *HTTP proxy URL*.
** Specify a valid *HTTPS proxy URL*.
** In the *Additional trust bundle* field, provide a PEM encoded X.509 certificate bundle. The bundle is added to the trusted certificate store for the cluster nodes. An additional trust bundle file is required if you use a TLS-inspecting proxy unless the identity certificate for the proxy is signed by an authority from the {op-system-first} trust bundle. This requirement applies regardless of whether the proxy is transparent or requires explicit configuration using the `http-proxy` and `https-proxy` arguments.
+
.. Click *Next*.
+
For more information about configuring a proxy with OpenShift Container Platform, see _Configuring a cluster-wide proxy_.

. Accept the default application ingress settings, or to create your own custom settings, select *Custom Settings*. All of the custom settings are optional.
.. In *Route selector*, enter a comma-separated list of `key=value` pairs to limit which routes this ingress exposes.
Leave the field empty if all routes should remain eligible based on your other choices.
.. In *Excluded namespaces*, enter a comma-separated list of namespace names whose routes must not use this ingress.
.. In *Exclude namespace selectors*, specify one or more label selectors. For each selector, provide a label key and a comma-separated list of label values. The default Ingress Controller does not apply to namespaces whose labels satisfy any of the configured selectors.
+
[IMPORTANT]
====
Do not include spaces around commas, for example, use `finance,HR,legal`, and not `finance, HR, legal`.
====
+
.. Set *Namespace ownership policy* for route admission when namespaces share hostnames, for example, select *Strict* for restrictive admission.
.. Set *Wildcard policy* to allow or disallow wildcard patterns in route hostnames, for example, select *Disallowed* to block wildcard host routes.
+
For more information about custom application ingress settings, click the information icon provided for each setting.

. In the *CIDR ranges* dialog, configure custom classless inter-domain routing (CIDR) ranges or use the defaults that are provided.
+
[IMPORTANT]
====
CIDR configurations cannot be changed later. Confirm your selections with your network administrator before proceeding.

If the cluster privacy is set to *Private*, you cannot access your cluster until you configure private connections in your cloud provider.
====

. On the *Cluster update strategy* page, configure your update preferences:
.. Choose a cluster update method:
** Select *Individual updates* if you want to schedule each update individually. This is the default option.
** Select *Recurring updates* to update your cluster on your preferred day and start time, when updates are available.
+
[NOTE]
====
You can review the end-of-life dates in the update lifecycle documentation for OpenShift Container Platform. For more information, see OpenShift Dedicated update life cycle.
====
+
.. Provide administrator approval based on your cluster update method:
** Individual updates: If you select an update version that requires approval, provide an administrator’s acknowledgment and click *Approve and continue*.
** Recurring updates: If you selected recurring updates for your cluster, provide an administrator’s acknowledgment and click *Approve and continue*. {cluster-manager} does not start scheduled y-stream updates for minor versions without receiving an administrator’s acknowledgment.
+
.. If you opted for recurring updates, select a preferred day of the week and upgrade start time in UTC from the drop-down menus.
.. Optional: You can set a grace period for *Node draining* during cluster upgrades. A *1 hour* grace period is set by default.
.. Click *Next*.
+
[NOTE]
====
In the event of critical security concerns that significantly impact the security or stability of a cluster, Red Hat Site Reliability Engineering (SRE) might schedule automatic updates to the latest z-stream version that is not impacted. The updates are applied within 48 hours after customer notifications are provided. For a description of the critical impact security rating, see Understanding Red Hat security ratings.
====

. Review the summary of your selections and click *Create cluster* to start the cluster installation. The installation takes approximately 30-40 minutes to complete.
+
. Optional: On the *Overview* tab, you can enable the delete protection feature by selecting *Enable*, which is located directly under *Delete Protection: Disabled*. This will prevent your cluster from being deleted. To disable delete protection, select *Disable*.
By default, clusters are created with the delete protection feature disabled.

.Verification

* You can monitor the progress of the installation in the *Overview* page for your cluster. You can view the installation logs on the same page. Your cluster is ready when the *Status* in the *Details* section of the page is listed as *Ready*.

[IMPORTANT]
====
If your cluster deployment fails during installation, certain resources created during the installation process are not automatically removed from your {GCP} account. To remove these resources from your {gcp-short} account, you must delete the failed cluster.
====

.Additional resources

* Accessing {cluster-manager}

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="create-wif-cluster-cli_{context}"]
= Creating a Workload Identity Federation cluster using the {cluster-manager} CLI

[role="_abstract"]
You can create an OpenShift Container Platform on {GCP} cluster with Workload Identity Federation (WIF) using the {cluster-manager} CLI (`ocm`) in interactive or noninteractive mode.

.Prerequisites

* You have created a WIF configuration. For more information, see "Creating a Workload Identity Federation configuration".
* You have downloaded the latest version of the {cluster-manager} CLI (`ocm`) for your operating system from the Downloads page on {cluster-manager}.

.Procedure
. Create a WIF cluster using the `interactive` or the `non-interactive` mode.

.. In `interactive` mode, cluster attributes are displayed automatically as prompts during the creation of the cluster. Enter the values for those prompts based on specified requirements in the fields provided.

.. In `non-interactive` mode, specify the values for specific parameters within the command.

* Based on your mode preference, run one of the following commands to create an OpenShift Container Platform cluster on {gcp-short} with WIF configuration:

** Create a cluster in interactive mode by running the following command:
+
[source,terminal]
----
$ ocm create cluster --interactive
----
+
where:

`--interactive`:: Specifies that the cluster is created in interactive mode. This mode prompts you to enter the required configuration options during cluster creation. If you do not include this parameter, the cluster is created in `non-interactive` mode by default.
+
** Create a cluster in noninteractive mode by running the following command.
The following example is made up of optional and required parameters and might differ from your noninteractive mode command. Parameters not identified as optional are required. For additional details about these and other parameters, run the `ocm create cluster --help flag` command in your terminal window.
+
[source,terminal]
----
$ ocm create cluster <cluster_name> \
--provider=gcp \
--ccs=true \
--wif-config <wif_name> \
--dns-zone-id <dns_zone_id> \
--region <gcp_region> \
--subscription-type=marketplace-gcp \
--marketplace-gcp-terms=true \
--version <version> \
--multi-az=true  \
--enable-autoscaling=true \
--min-replicas=3 \
--max-replicas=6 \
--secure-boot-for-shielded-vms=true
--channel <channel_name>
----
+
where:

`<cluster_name>`:: Specifies the name of the cluster. Replace `<cluster_name>` with a name for your cluster.

`--provider=gcp`:: Specifies the cloud provider for the cluster.

`--ccs=true`:: Specifies that the cluster is a Customer Cloud Subscription (CCS) cluster.

`--wif-config <wif_name>`:: Specifies the name of the WIF configuration to assign to the cluster. Replace `<wif_name>` with the name of your WIF configuration.

`--dns-zone-id <dns_zone_id>`:: Optional. Specifies the DNS zone ID to use for the cluster. Replace `<dns_zone_id>` with the ID of your DNS zone. For more information about this parameter, see _Creating a managed DNS zone_ in the _Additional resources_ section.

`--region <gcp_region>`:: Specifies the {GCP} region where the new cluster will be deployed. Replace `<gcp_region>` with the required {GCP} region.

`--subscription-type=marketplace-gcp`:: Optional. Specifies the subscription billing model for the cluster.

`--marketplace-gcp-terms=true`:: Confirms that you have accepted the {GCP} Marketplace terms and agreements for the OpenShift Dedicated product listing. This parameter is required if you provided a value of `marketplace-gcp` for the `subscription-type` parameter.

`--version <version>`:: Specifies the required OpenShift Container Platform version. This parameter is optional. However, if an OpenShift Container Platform version is specified, the version must also be supported by the assigned WIF configuration. If a version is specified that is not supported by the assigned WIF configuration, cluster creation will fail.
If this occurs, update the assigned WIF configuration to the required version or create a new WIF configuration with the required version. If you do not specify a version, the cluster is created with the default version for the assigned WIF configuration.
+
For more information about supported versions for WIF configurations, see "Creating a Workload Identity Federation configuration".

`--multi-az=true`:: Specifies that the cluster is deployed to multiple data centers. This parameter is optional.

`--enable-autoscaling=true`:: Enables autoscaling of compute nodes. This parameter is optional.

`--min-replicas=3`:: Specifies the minimum number of compute nodes. This parameter is optional.

`--max-replicas=6`:: Specifies the maximum number of compute nodes. This parameter is optional.

`--secure-boot-for-shielded-vms=true`:: Enables Secure Boot, which allows the use of Shielded VMs in the {gcp-full}. This parameter is optional.

`--channel <channel_name>`:: Specifies the name of the channel you want to assign the cluster to. Channel options include `stable-4.y`, `fast-4.y`, and `eus-4.y`. Replace `<channel_name>` with the required channel. This parameter is optional.

.Verification

* To verify that the cluster was created successfully, run the following command:
+
[source,terminal]
----
$ ocm get cluster <cluster_name>
----
+
If the cluster was created successfully, the output displays the cluster state as `ready`.

[IMPORTANT]
====
If your cluster deployment fails during installation, certain resources created during the installation process are not automatically removed from your {GCP} account. To remove these resources from your {gcp-short} account, you must delete the failed cluster. For more information, see "Deleting an OpenShift Container Platform cluster on {GCP}".
====
// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="ocm-cli-list-wif-commands_{context}"]
= Listing Workload Identity Federation clusters

[role="_abstract"]
You can list OpenShift Container Platform clusters that have been deployed using Workload Identity Federation (WIF) authentication by using the {cluster-manager} CLI (`ocm`).

.Procedure

* To list all of your OpenShift Container Platform clusters that have been deployed using the WIF authentication type, run one of the following commands:
+
** Using the `--parameter` flag with the `search` option:
+
[source,terminal]
----
$ ocm list clusters --parameter search="gcp.authentication.wif_config_id != ''"
----
+
** Using a specific wif-config ID to filter the clusters associated with that configuration, replacing `<wif_config_id>` with the ID of the WIF configuration:
+
[source,terminal]
----
$ ocm list clusters --parameter search="gcp.authentication.wif_config_id = '<wif_config_id>'"
----

// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="wif-configuration-update_{context}"]
= Updating a Workload Identity Federation configuration

[role="_abstract"]
You can update an existing Workload Identity Federation (WIF) configuration to support newer OpenShift Container Platform y-stream versions and to align with the latest security best practices.

[NOTE]
====
Updating a WIF configuration is only applicable for y-stream updates. For an overview of the update process, including details regarding version semantics, see The Ultimate Guide to OpenShift Release and Upgrade Process for Cluster Administrators.
====
Before upgrading a WIF-enabled OpenShift Container Platform cluster to a newer version, you must update the wif-config to that version as well. If you do not update the wif-config version before attempting to upgrade the cluster version, the cluster version upgrade will fail.

As part of Red{nbsp}Hat's ongoing commitment to the principle of least privilege, certain permissions previously assigned to the `osd-deployer` service account in WIF configurations have been removed. These changes help enhance the security of your clusters by ensuring that service accounts have only the permissions they need to perform their functions.

For the complete list of WIF configuration roles and their assigned permissions, see managed-cluster-config.

To align your existing WIF configurations with these updated permissions, you can run the `ocm gcp update wif-config` command. This command updates the WIF configuration to include the latest permissions and roles required for optimal operation.

When you update a wif-config or create a new one, ensure your {cluster-manager} CLI (`ocm`) is up to date. Not updating to the latest version of the `ocm` can result in error messages and service disruptions.

**Example output**
[source,text]
----
Error: failed to create wif-config: failed to create wif-config: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-10-06T15:18:37Z' and operation identifier is 'f9551d63-a58a-4e3c-b847-5f99ba1b0b74': Client version is out of date for WIF operations. Please update from vOCM-CLI/1.0.7 to v1.0.8 and try again.
----

You can also update an existing OpenShift Container Platform cluster that is already using WIF by adding a dedicated project to manage workload identity pools and providers using the `--federated-project` flag. This best-practice model separates the workload identity pools and providers into a dedicated, centralized {GCP} project.

When you update the configuration using the `--federated-project` flag, any associated workload identity pools move to the new federated project you specify, while the existing IAM service accounts and custom roles remain in the original cluster-associated project.

.Procedure
. To check the version of your `ocm`, run the following command:
+
[source,terminal]
----
$ ocm version
----
+
. Optional: If your `ocm` version is not the latest available, download and install the latest version from the Downloads page on {cluster-manager}.
+
. Update a wif-config to a specific OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
ocm gcp update wif-config <wif_name> \
--version <version>
--federated-project <gcp_project_id>
----
+
where:

`<wif_name>`:: The name of the WIF configuration you want to update.

`<version>`:: Optional: The OpenShift Container Platform y-stream version you plan to update the cluster to. If you do not specify a version, the wif-config will be updated to support the latest OpenShift Container Platform y-stream version as well as the last three OpenShift Container Platform supported y-stream versions (beginning with version 4.17).

`--federated-project <gcp_project_id>`:: Optional: A flag to specify a new dedicated project where the workload identity pools and providers will be created and managed. If this flag is not included, the workload identity pools and providers will remain in the project associated with the cluster.

.Next steps

The stale set of permissions previously assigned to the `osd-deployer` service account will remain on the account after updating the wif-config. You need to manually access the roles and remove these stale permissions from them.

Follow the instructions in the "Removing stale deployer permissions from service accounts managed by a WIF configuration" and "Removing stale support permissions from service accounts managed by a WIF configuration" guides to remove these stale permissions.

In addition, if you used the `--federated-project` flag to move the workload identity pool to a new dedicated project, you can manually remove the stale workload identity pool from the original cluster-associated project.
For more information, see Delete a pool in the {GCP} documentation.
// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="wif-removing-stale-deployer-permissions_{context}"]
= Removing stale deployer permissions from service accounts managed by a WIF configuration

[role="_abstract"]
To remove the stale deployer permissions from service accounts managed by a WIF configuration, run the following commands on a terminal with access to the {gcp-full} project hosting the service accounts.

.Procedure

. Retrieve the existing role definition, ensuring the `PROJECT_ID` environment variable points to your {gcp-full} project:
+
[source,terminal]
----
$ gcloud iam roles describe \
  osd_deployer_v4.18 \
  --project $PROJECT_ID \
  --format=yaml > /tmp/role.yaml
----
+
. Remove the unwanted permissions. You can do this by filtering out the unwanted permissions from the role definition file and saving the updated definition to a new file:
+
[source,terminal]
----
$ cat /tmp/role.yaml | \
grep -v "resourcemanager.projects.setIamPolicy" | \
grep -v "iam.serviceAccounts.signBlob" | \
grep -v "iam.serviceAccounts.actAs" > /tmp/updated_role.yaml
----
+
. Review the changes in the output between the original and updated role definitions to ensure only the unwanted permissions have been removed:
+
[source,terminal]
----
$ diff /tmp/role.yaml /tmp/updated_role.yaml
----
+
. Update the role in {gcp-full} with the updated role definition file, ensuring the `PROJECT_ID` environment variable points to your {gcp-full} project:
+
[source,terminal]
----
$ gcloud iam roles update \
  osd_deployer_v4.18 \
  --project=$PROJECT_ID \
  --file=/tmp/updated_role.yaml
----
// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="wif-removing-stale-support-permissions_{context}"]
= Removing stale support permissions from service accounts managed by a WIF configuration

[role="_abstract"]
To remove stale support permissions, run the following commands on a terminal with access to the {gcp-full} project hosting the service accounts.

.Procedure

. Retrieve the existing role definition, ensuring the `PROJECT_ID` environment variable points to your {gcp-full} project:
+
[source,terminal]
----
$ gcloud iam roles describe sre_managed_support --project $PROJECT_ID --format=yaml > /tmp/role.yaml
----
+
. Remove the unwanted permissions. You can do this by filtering out the unwanted permissions from the role definition file and saving the updated definition to a new file:
+
[source,terminal]
----
$ cat /tmp/role.yaml | grep -v "compute.firewalls.create"  > /tmp/updated_role.yaml
----
+
. Review the changes in the output between the original and updated role definitions to ensure only the unwanted permissions have been removed:
+
[source,terminal]
----
$ diff /tmp/role.yaml /tmp/updated_role.yaml
----
+
. Update the role in {gcp-full} with the updated role definition file, ensuring the `PROJECT_ID` environment variable points to your {gcp-full} project:
+
[source,terminal]
----
$ gcloud iam roles update sre_managed_support --project $PROJECT_ID --file=/tmp/updated_role.yaml
----
// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-creating-a-cluster-on-gcp-with-workload-identity-federation.adoc

[id="ocm-cli-verify-wif-commands_{context}"]
= Verifying a Workload Identity Federation configuration

[role="_abstract"]
You can verify that the configuration of resources associated with a WIF configuration are correct by running the `ocm gcp verify wif-config` command. If a misconfiguration is found, the output provides details about the misconfiguration and recommends that you update the WIF configuration.

You need the name and ID of the WIF configuration you want to verify before verification.
To obtain the name and ID of your active WIF configurations, run the following command:

[source,terminal]
----
$ ocm gcp list wif-configs
----

To determine if the WIF configuration you want to verify is configured correctly, run the following command:

[source,terminal]
----
$ ocm gcp verify wif-config <wif_config_name>|<wif_config_id> <1>
----
<1> Replace `<wif_config_name>` and `<wif_config_id>` with the name and ID of your WIF configuration, respectively.

--
**Example output**
[source,terminal]
----
Error: verification failed with error: missing role 'compute.storageAdmin'.
Running 'ocm gcp update wif-config' may fix errors related to cloud resource misconfiguration.
exit status 1.
----
--

[role="_additional-resources"]
== Additional resources

* Customer requirements
* Resource quotas per project
* {gcp-short} account limits
* Required customer procedure
* Manage workload identity pools and providers
* Roles and permissions
* Cluster maximums
* Configuring identity providers
* Revoking privileges and access to an OpenShift Container Platform cluster
* Creating a managed DNS zone
