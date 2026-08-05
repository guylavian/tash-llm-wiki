---
title: "Creating a cluster on {gcp-short} with Service Account authentication"
type: reference
domain: openshift
slug: osd-gcp-clusters-4-22-creating-a-gcp-cluster-sa
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_gcp_clusters/creating-a-gcp-cluster-sa
version: 4.22
family: osd_gcp_clusters
documentKind: "Documentation"
---

# Creating a cluster on {gcp-short} with Service Account authentication

[id="osd-creating-a-cluster-on-gcp-sa"]
= Creating a cluster on {gcp-short} with Service Account authentication

[role="_abstract"]

// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/creating-a-gcp-cluster-with-workload-identity-federation.adoc

[id="service-account-auth-overview_{context}"]
= Service Account authentication overview

[role="_abstract"]
The Service Account authentication type allows you to authenticate your OpenShift Container Platform cluster on {GCP} using a private key for authentication purposes.

Service accounts use RSA key pairs, which consist of a public and private key, with the private key being the service account key. The public portion of the key pair is stored on {gcp-full}, while the private key is kept by the user. The private key allows users to authenticate as a service account and gain access to assets and resources associated with that service account.

Service account keys are a security risk if not managed carefully. Users should routinely rotate their service account keys to reduce the risk of leaked or stolen keys.

[IMPORTANT]
=====
Because of the potential security risk when using the Service Account authentication type, Red Hat recommends using {gcp-short} Workload Identity Federation (WIF) as the authentication type for installing and interacting with the OpenShift Dedicated cluster deployed on {gcp-first} because it provides enhanced security. For more information, see _Creating a cluster on {gcp-short} with Workload Identity Federation authentication_ in the _Additional resources_ section.
=====

[id="osd-creating-a-cluster-on-gcp-sa-prerequisites_{context}"]
== Prerequisites

* You reviewed the introduction to OpenShift Container Platform and the documentation on architecture concepts.
* You reviewed the OpenShift Container Platform cloud deployment options.
* You reviewed and completed the Required customer procedure.

// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/creating-a-gcp-cluster.adoc

[id="osd-create-gcp-cluster-ccs1_{context}"]
= Creating a cluster with Service Account authentication using {cluster-manager}

[role="_abstract"]
Through {cluster-manager-url}, you can create an OpenShift Container Platform cluster on {GCP} using a cloud provider account that you own with the Service Account authentication type.

.Procedure

. Log in to {cluster-manager-url} and click *Create cluster*.
. On the *Create an OpenShift cluster* page, select *Create cluster* in the *Red Hat OpenShift Dedicated* row.
. Under *Billing model*, configure the subscription type and infrastructure type:
.. Select a subscription type. For information about OpenShift Container Platform subscription options, see Cluster subscriptions and registration in the {cluster-manager} documentation.
+
[NOTE]
====
The subscription types that are available to you depend on your OpenShift Container Platform subscriptions and resource quotas.
Red Hat recommends deploying your cluster with the On-Demand subscription type purchased through the {GCP} Marketplace. This option provides flexible, consumption-based billing, consuming additional capacity is frictionless, and no Red Hat intervention is required.

For more information, contact your sales representative or Red Hat support.
====
+
.. Select the *Customer Cloud Subscription* infrastructure type to deploy OpenShift Container Platform in an existing cloud provider account that you own.
.. Click *Next*.
. Select *Run on {gcp-full}*.
. Select *Service Account*  as the Authentication type.
+
[NOTE]
====
Red Hat recommends using Workload Identity Federation as the Authentication type. For more information, see _Creating a cluster on {gcp-short} with Workload Identity Federation authentication_ in the _Additional resources_ section.
====
+

. Review and complete the listed *Prerequisites*.
. Select the checkbox to acknowledge that you have read and completed all of the prerequisites.
. Provide your {gcp-short} service account private key in JSON format. You can either click *Browse* to locate and attach a JSON file or add the details in the *Service account JSON* field.

. Click *Next* to validate your cloud provider account and go to the *Cluster details* page.

. On the *Cluster details* page, provide a name for your cluster and specify the cluster details:
.. Add a *Cluster name*.
.. Optional: Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated to a 15 character string.
+
To customize the subdomain, select the *Create customize domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field. The domain prefix cannot be longer than 15 characters, must be unique within your organization, and cannot be changed after cluster creation.
.. Select a cluster version from the *Version* drop-down menu.
+
[IMPORTANT]
====
Clusters configured with Private Service Connect (PSC) are only supported on OpenShift Dedicated version 4.17 and later. For more information regarding PSC, see _Private Service Overview_ in the _Additional resources_ section.
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

.. Optional: Select *Enable Secure Boot for Shielded VMs* to use Shielded VMs when installing your cluster. Once you create your cluster, the *Enable Secure Boot for Shielded VMs* setting cannot be changed. For more information, see Shielded VMs.
+
[IMPORTANT]
====
To successfully create a cluster, you must select *Enable Secure Boot support for Shielded VMs* if your organization has the policy constraint `constraints/compute.requireShieldedVm` enabled. For more information regarding {gcp-short} organizational policy constraints, see Organization policy constraints.
====
// +
// [IMPORTANT]
// ====
// Once a machine pool is saved, the *Enable Secure Boot support for Shielded VMs* setting cannot be changed.
// ====
+
[IMPORTANT]
====
*Enable Secure Boot support for Shielded VMs* is not supported for OpenShift Container Platform on {GCP} clusters created using bare-metal instance types. For more information, see Limitations in the {gcp-full} documentation.
====
+
.. Leave *Enable user workload monitoring* selected to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics. This option is enabled by default.

. Optional: Expand *Advanced Encryption* to make changes to encryption settings.

.. Select *Use custom KMS keys* to use custom KMS keys. If you prefer not to use custom KMS keys, leave the default setting *Use default KMS Keys*.

+

[IMPORTANT]
====
To use custom KMS keys, the IAM service account `osd-ccs-admin` must be granted the *Cloud KMS CryptoKey Encrypter/Decrypter* role. For more information about granting roles on a resource, see Granting roles on a resource.
====

+

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
By enabling additional etcd encryption, you will incur a performance overhead of approximately 20%. The overhead is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Consider enabling etcd encryption only if you specifically require it for your use case.
====
+
.. Click *Next*.

. On the *Default machine pool* page, select a *Compute node instance type* from the drop-down menu.
. Optional: Select the *Enable autoscaling* checkbox to enable autoscaling.
.. Click *Edit cluster autoscaling settings* to make changes to the autoscaling settings.
.. Once you have made your desired changes, click *Close*.
.. Select a minimum and maximum node count. Node counts can be selected by engaging the available plus and minus signs or inputting the desired node count into the number input field.
. Select a *Compute node count* from the drop-down menu.
+
[NOTE]
====
If you are using multiple availability zones, the compute node count is per zone. After your cluster is created, you can change the number of compute nodes in your cluster, but you cannot change the compute node instance type in a machine pool. The number and types of nodes available to you depend on your OpenShift Container Platform subscription.
====
+

. Optional: Expand *Add node labels* to add labels to your nodes. Click *Add additional label* to add an additional node label and select *Next*.

+
[IMPORTANT]
====
This step refers to labels within Kubernetes, not {gcp-full}. For more information regarding Kubernetes labels, see Labels and Selectors.
====
+

. On the *Network configuration* page, select *Public* or *Private* to use either public or private API endpoints and application routes for your cluster.
+
If you select *Private* and selected OpenShift Container Platform version 4.17 or later as your cluster version, *Use Private Service Connect* is selected by default. Private Service Connect (PSC) is {gcp-full}’s security-enhanced networking feature. You can disable PSC by clicking the *Use Private Service Connect* checkbox.
+
[NOTE]
====
Red Hat recommends using Private Service Connect when deploying a private OpenShift Container Platform cluster on {gcp-full}. Private Service Connect ensures there is a secured, private connectivity between Red Hat infrastructure, Site Reliability Engineering (SRE) and private OpenShift Container Platform clusters.
====
+
[IMPORTANT]
====
If you are using private API endpoints, you cannot access your cluster until you update the network settings in your cloud provider account.
====
+

. Optional: To install the cluster in an existing {gcp-short} Virtual Private Cloud (VPC):
+
--

.. Select *Install into an existing VPC*.
+
[IMPORTANT]
====
Private Service Connect is supported only with *Install into an existing VPC*.
====
+
.. If you are installing into an existing VPC and you want to enable an HTTP or HTTPS proxy for your cluster, select *Configure a cluster-wide proxy*.
+
[IMPORTANT]
====
In order to configure a cluster-wide proxy for your cluster, you must first create the Cloud network address translation (NAT) and a Cloud router. See the _Additional resources_ section for more information.
====
--
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

+
. Click *Next*.

. Optional: To install the cluster into a {gcp-short} Shared VPC:
+
[IMPORTANT]
====

To install a cluster into a Shared VPC, you must use OpenShift Container Platform version 4.13.15 or later. Additionally, the VPC owner of the host project must enable a project as a host project in their {gcp-full} console. For more information, see Enable a host project.
====

.. Select *Install into {gcp-short} Shared VPC*.
.. Specify the *Host project ID*. If the specified host project ID is incorrect, cluster creation fails.
+
[IMPORTANT]
====
Once you complete the steps within the cluster configuration wizard and click *Create Cluster*, the cluster will go into the "Installation Waiting" state. At this point, you must contact the VPC owner of the host project, who must assign the dynamically-generated service account the following roles: *Compute Network Administrator*, *Compute Security Administrator*, *Project IAM Admin*, and *DNS Administrator*.
The VPC owner of the host project has 30 days to grant the listed permissions before the cluster creation fails.
For information about Shared VPC permissions, see Provision Shared VPC.
====

+
. If you opted to install the cluster in an existing {gcp-short} VPC, provide your *Virtual Private Cloud (VPC) subnet settings* and select *Next*. You must ensure that your VPC is configured to allow outbound internet access to the domains required for the OpenShift Container Platform service. This outbound access is required for the OpenShift Container Platform service to communicate with Red{nbsp}Hat's management plane and SRE tooling via secure and encrypted endpoints over the public internet.
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

. In the *CIDR ranges* dialog, configure custom classless inter-domain routing (CIDR) ranges or use the defaults that are provided.
+
[NOTE]
====
If you are installing into a VPC, the *Machine CIDR* range must match the VPC subnets.
====
+
[IMPORTANT]
====
CIDR configurations cannot be changed later. Confirm your selections with your network administrator before proceeding.
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
+

[NOTE]
====
If you delete a cluster that was installed into a {gcp-short} Shared VPC, inform the VPC owner of the host project to remove the IAM policy roles granted to the service account that was referenced during cluster creation.
====

.Verification

* You can monitor the progress of the installation in the *Overview* page for your cluster. You can view the installation logs on the same page. Your cluster is ready when the *Status* in the *Details* section of the page is listed as *Ready*.

[IMPORTANT]
====
If your cluster deployment fails during installation, certain resources created during the installation process are not automatically removed from your {GCP} account. To remove these resources from your {gcp-short} account, you must delete the failed cluster.
====

// include::modules/osd-create-cluster-red-hat-account.adoc[leveloffset=+1]
[id="additional-resources_{context}"]
== Additional resources

* Creating a cluster on {gcp-short} with Workload Identity Federation authentication
* Private Service Connect overview
* Configuring a cluster-wide proxy
* Storage OpenShift Container Platform service definition
* Load balancers OpenShift Container Platform service definition
* etcd encryption service definition
* OpenShift Container Platform update life cycle
* Cloud NAT overview in the Google documentation
* Cloud Router overview in the Google documentation
* Create and manage VPC networks in the Google documentation
* Configuring identity providers
* Revoking privileges and access to an OpenShift Container Platform cluster
