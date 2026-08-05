---
title: "Getting started with {product-title}"
type: reference
domain: openshift
slug: osd-getting-started-4-22-osd-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_getting_started/osd-getting-started
version: 4.22
family: osd_getting_started
documentKind: "Documentation"
---

# Getting started with {product-title}

[id="osd-getting-started"]
= Getting started with OpenShift Container Platform

[role="_abstract"]
Follow this getting started document to create a OpenShift Container Platform cluster, grant user access, deploy your first application, and learn how to scale and delete your cluster.

For OpenShift Container Platform clusters deployed on {gcp-short}, Red Hat recommends using {gcp-short} Workload Identity Federation (WIF) as the authentication type for installing and interacting with the OpenShift Container Platform cluster deployed on {gcp-short} because it provides enhanced security.

Red Hat also recommends creating an OpenShift Container Platform cluster deployed on {gcp-short} in Private cluster mode with Private Service Connect (PSC) to manage and monitor a cluster to avoid all public ingress network traffic.

[id="osd-getting-started-prerequisites"]
== Prerequisites

* You reviewed the introduction to OpenShift Container Platform and the documentation on architecture concepts.
* You reviewed the OpenShift Container Platform cloud deployment options.

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
// * osd_install_access_delete_cluster/creating-an-aws-cluster.adoc

[id="osd-create-aws-cluster-ccs_{context}"]
= Creating a cluster on AWS

[role="_abstract"]
Deploy a OpenShift Container Platform cluster with the Customer Cloud Subscription (CCS) or Red{nbsp}Hat cloud account billing model to get more financial control. By configuring AWS Identity and Access Management (IAM) roles, Virtual Private Clouds (VPC) networking, and PrivateLink, you integrate your clusters into existing infrastructure while ensuring security.

.Prerequisites

You have completed the following tasks:

* Configure your AWS account for use with OpenShift Container Platform.
* Ensure that you have not deployed any services in your AWS account.
* Configure the AWS account quotas and limits required to support the specified cluster size.
* Create an `osdCcsAdmin` AWS Identity and Access Management (IAM) user with the `AdministratorAccess` policy attached.
* Set up a service control policy (SCP) in your AWS organization. For more information, see _Minimum required service control policy (SCP)_.
* Consider having *Business Support* or higher from AWS.
* If you are configuring a cluster-wide proxy, verify that the proxy is accessible from the VPC where you installed the cluster.
* Ensure that you can access the proxy from the private subnets of the VPC.

.Procedure

. Log in to {cluster-manager-url}.

. On the *Overview* page, select *Create cluster* in the *Red{nbsp}Hat OpenShift Container Platform* card.

. Under *Billing model*, configure the subscription type and infrastructure type:
.. Select a subscription type. For information about OpenShift Container Platform subscription options, see Cluster subscriptions and registration in the {cluster-manager} documentation.
+
[NOTE]
====
The subscription types that are available to you depend on your OpenShift Container Platform subscriptions and resource quotas. For more information, contact your sales representative or Red Hat support.
====
+
.. Select the *Customer Cloud Subscription* infrastructure type to deploy OpenShift Container Platform in an existing cloud provider account that you own or select *Red Hat cloud account* infrastructure type to deploy OpenShift Container Platform in a Red Hat cloud provider account.
.. Click *Next*.
. Select *Run on Amazon Web Services*. If you are provisioning your cluster in an AWS account, complete the following substeps:
.. Review and complete the listed *Prerequisites*.
.. Select the checkbox to acknowledge that you have read and completed all of the prerequisites.
.. Give your AWS account details:
... Enter your *AWS account ID*.
... Enter your *AWS access key ID* and *AWS secret access key* for your AWS IAM user account.
+
[NOTE]
====
Revoking these credentials in AWS results in a loss of access to any cluster created with these credentials.
====
... Optional: You can select *Bypass AWS service control policy (SCP) checks* to disable the SCP checks.
+
[NOTE]
====
Some AWS SCPs can cause the installation to fail, even if you have the required permissions. Disabling the SCP checks allows an installation to proceed. Even when you bypass the checks, the SCP still runs.
====
. Click *Next* to validate your cloud provider account and go to the *Cluster details* page.

. On the *Cluster details* page, give a name for your cluster and specify the cluster details:
.. Add a *Cluster name*.
.. Optional: Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, then the domain prefix uses that name. If the cluster name is longer than 15 characters, the domain prefix is randomly generated to a 15 character string.
+
To customize the subdomain, select the *Create customize domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field. The domain prefix cannot be longer than 15 characters, must be unique within your organization, and cannot be changed after cluster creation.
.. Select a cluster version from the *Version* drop-down menu.
.. Select a cloud provider region from the *Region* drop-down menu.
.. Select a *Single zone* or *Multi-zone* configuration.
+
.. Leave *Enable user workload monitoring* selected to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics. This option is enabled by default.
.. Optional: Expand *Advanced Encryption* to make changes to encryption settings.
... Accept the default setting *Use default KMS Keys* to use your default AWS KMS key, or select *Use Custom KMS keys* to use a custom KMS key.
.... With *Use Custom KMS keys* selected, enter the AWS Key Management Service (KMS) custom key Amazon Resource Name (ARN) ARN in the *Key ARN* field.
Use the key to encrypt all control plane, infrastructure, worker node root volumes, and persistent volumes in your cluster.
+
... Optional: Select *Enable FIPS cryptography* if you require your cluster to be FIPS validated.
+
[NOTE]
====
If you select  *Enable FIPS cryptography*, then by default, you enable  *Enable additional etcd encryption* and you cannot disable this feature. You can select *Enable additional etcd encryption* without selecting *Enable FIPS cryptography*.
====
+
... Optional: Select *Enable additional etcd encryption* if you require etcd key value encryption. With this option, the etcd key values are encrypted, but the keys are not. This option is in addition to the control plane storage encryption that encrypts the etcd volumes in OpenShift Container Platform clusters by default.
+
[NOTE]
====
By enabling etcd encryption for the key values in etcd, you increase the performance impact on your workloads by about 20%. The workload increase is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Consider enabling etcd encryption only if you specifically require it for your use case.
====
+
.. Click *Next*.

. On the *Default machine pool* page, select a *Compute node instance type* from the drop-down menu.
. Optional: Select the *Enable autoscaling* checkbox to enable autoscaling.
.. Click *Edit cluster autoscaling settings* to make changes to the autoscaling settings.
.. After you make your changes, click *Close*.
.. Select a minimum and maximum node count. Select the node counts by engaging the available plus and minus signs or inputting the node count into the number input field.
. Select a *Compute node count* from the drop-down menu.
+
[NOTE]
====
After you create your cluster, you can change the number of compute nodes in it, but you cannot change the compute node instance type in a machine pool. The number and types of nodes available to you depend on your OpenShift Container Platform subscription.
====

. Choose your preference for the Instance Metadata Service (IMDS) type, either using both IMDSv1 and IMDSv2 types or requiring your EC2 instances to use only IMDSv2. You can access instance metadata from a running instance in two ways:
+
* Instance Metadata Service Version 1 (IMDSv1) - a request/response method
* Instance Metadata Service Version 2 (IMDSv2) - a session-oriented method
+
[IMPORTANT]
====
After you create your cluster, you cannot change the Instance Metadata Service settings.
====
+
[NOTE]
====
IMDSv2 uses session-oriented requests. With session-oriented requests, you create a session token that defines the session duration, which can range from a minimum of one second to a maximum of six hours. During the specified duration, you can use the same session token for future requests. After the specified duration expires, you must create a new session token to use for future requests.
====
+
For more information regarding IMDS, see Instance metadata and user data in the AWS documentation.

. Optional: Expand *Edit node labels* to add labels to your nodes. Click *Add label* to add more node labels and select *Next*.
. On the *Network configuration* page, select *Public* or *Private* to use either public or private API endpoints and application routes for your cluster.
+
[IMPORTANT]
====
If you are using private API endpoints, you cannot access your cluster until you update the network settings in your cloud provider account.
====
+
. Optional: To install the cluster in an existing AWS Virtual Private Cloud (VPC):
+
--

.. Select *Install into an existing VPC*.
.. If you are installing into an existing VPC and opted to use private API endpoints, you can select *Use a PrivateLink*. This option enables connections to the cluster by Red Hat Site Reliability Engineering (SRE) using only AWS PrivateLink endpoints.
+
[NOTE]
====
You cannot change the *Use a PrivateLink* option after you create a cluster.
====
+
.. If you are installing into an existing VPC and you want to enable an HTTP or HTTPS proxy for your cluster, select *Configure a cluster-wide proxy*.
--
. If you opted to install the cluster in an existing AWS VPC, give your *Virtual Private Cloud (VPC) subnet settings* and select *Next*.
You must have created the Cloud network address translation (NAT) and a Cloud router. See the "Additional resources" section for information about Cloud NATs and Google VPCs.
+
[NOTE]
====
Ensure that you configure the VPC with a public and a private subnet for each availability zone that you want the cluster installed into. If you opted to use PrivateLink, you only need private subnets.
====
+
.. Optional: Expand *Additional security groups* and select additional custom security groups to apply to nodes in the default machine pools. You must have already created the security groups and associated them with the VPC that you selected for this cluster. You cannot add or edit security groups to the default machine pools after you create the cluster.
+
By default, the security groups you specify are added for all node types. Clear the *Apply the same security groups to all node types* checkbox to apply different security groups for each node type.
+
For more information, see the requirements for _Security groups_ under _Additional resources_.
. Accept the default application ingress settings, or to create your own custom settings, select *Custom Settings*.
.. Optional: Give route selector.
.. Optional: Give excluded namespaces.
.. Select a namespace ownership policy.
.. Select a wildcard policy.
+
For more information about custom application ingress settings, click the information icon for each setting.
+
. If you opted to configure a cluster-wide proxy, give your proxy configuration details on the *Cluster-wide proxy* page:
.. Enter a value in at least one of the following fields:
** Specify a valid *HTTP proxy URL*.
** Specify a valid *HTTPS proxy URL*.
** In the *Additional trust bundle* field, give a PEM encoded X.509 certificate bundle. The bundle is added to the trusted certificate store for the cluster nodes. You need an additional trust bundle file if you use a TLS-inspecting proxy unless you have an identity certificate for the proxy, signed by an authority from the {op-system-first} trust bundle. This requirement applies regardless of whether the proxy is transparent or requires explicit configuration using the `http-proxy` and `https-proxy` arguments.
+
.. Click *Next*.
+
For more information about configuring a proxy with OpenShift Container Platform, see _Configuring a cluster-wide proxy_.

. In the *CIDR ranges* dialog, configure custom classless inter-domain routing (CIDR) ranges or use the designated defaults.
+
[NOTE]
====
If you are installing into a VPC, the *Machine CIDR* range must match the VPC subnets.
====
+
[IMPORTANT]
====
You cannot change CIDR configurations. Confirm your selections with your network administrator before proceeding.
====
+
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
.. If you opted for recurring updates, select a preferred day of the week and upgrade start time in UTC from the drop-down menus.
.. Optional: You can set a grace period for *Node draining* during cluster upgrades. By default, you get a *1 hour* grace period.
.. Click *Next*.
+
[NOTE]
====
If critical security concerns that significantly impact the security or stability of a cluster occur, Red Hat Site Reliability Engineering (SRE) might schedule automatic updates to the latest z-stream version that is not impacted. The updates apply within 48 hours after you get customer notifications. For a description of the critical impact security rating, see Understanding Red Hat security ratings.
====

. Review the summary of your selections and click *Create cluster* to start the cluster installation. The installation takes approximately 30-40 minutes to complete.
+
. Optional: On the *Overview* tab, you can enable the delete protection feature by going to  *Delete Protection: Disabled* and selecting *Enable*. This feature gives your cluster delete protection. To disable delete protection, select *Disable*.
By default, clusters are created with the delete protection feature disabled.

.Verification

* You can monitor the progress of the installation in the *Overview* page for your cluster. You can view the installation logs on the same page. Your cluster is ready when the *Status* in the *Details* section of the page is listed as *Ready*.

// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/creating-a-gcp-cluster.adoc

[id="osd-create-gcp-cluster-ccs_{context}"]
= Creating a cluster on {gcp-short} with a Red Hat cloud account using {cluster-manager}

[role="_abstract"]
Through {cluster-manager-url}, you can create an OpenShift Container Platform cluster on {GCP} using a standard cloud provider account owned by Red Hat.

[NOTE]
====
If you want to create an OpenShift Container Platform cluster on {GCP} with the {cluster-manager-first} command-line interface (`ocm`), see the instructions for configuring machine pool root disk sizes for clusters
====

.Procedure

. Log in to {cluster-manager-url} and click *Create cluster*.

. In the *Cloud* tab, click *Create cluster* in the *Red Hat OpenShift Container Platform* row.

. Under *Billing model*, configure the subscription type and infrastructure type:
.. Select the *Annual* subscription type. Only the *Annual* subscription type is available when you deploy a cluster using a Red Hat cloud account.
+
For information about OpenShift Container Platform subscription options, see Cluster subscriptions and registration in the {cluster-manager} documentation.
+
[NOTE]
====
You must have the required resource quota for the *Annual* subscription type to be available. For more information, contact your sales representative or Red Hat support.
====
+
.. Select the *Red Hat cloud account* infrastructure type to deploy OpenShift Container Platform in a cloud provider account that is owned by Red Hat.
.. Click *Next*.
. Select *Run on {gcp-full}* and click *Next*.
. On the *Cluster details* page, provide a name for your cluster and specify the cluster details:
.. Add a *Cluster name*.
.. Optional: Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated as a 15-character string.
+
To customize the subdomain, select the *Create custom domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field. The domain prefix cannot be longer than 15 characters, must be unique within your organization, and cannot be changed after cluster creation.
.. Select a cluster version from the *Version* drop-down menu.
.. Select a channel from the *Channel* drop-down menu.
+
--
--
+
.. Select a cloud provider region from the *Region* drop-down menu.
.. Select a *Single zone* or *Multi-zone* configuration.
.. Select a *Persistent storage* capacity for the cluster. For more information, see the _Storage_ section in the OpenShift Container Platform service definition.
.. Specify the number of *Load balancers* that you require for your cluster. For more information, see the _Load balancers_ section in the OpenShift Container Platform service definition.
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
+
.. Optional: Select *Enable FIPS cryptography* if you require your cluster to be FIPS validated.
+
[NOTE]
====
If *Enable FIPS cryptography* is selected, *Enable additional etcd encryption* is enabled by default and cannot be disabled. You can select *Enable additional etcd encryption* without selecting *Enable FIPS cryptography*.
====

.. Optional: Select *Enable additional etcd encryption* if you require etcd key value encryption. With this option, the etcd key values are encrypted, but not the keys. This option is in addition to the control plane storage encryption that encrypts the etcd volumes in OpenShift Container Platform clusters by default.
+
[NOTE]
====
By enabling etcd encryption for the key values in etcd, you increase the performance impact on your workloads by about 20%. This increase is a result of introducing this second layer of encryption, in addition to the default control plane storage encryption that encrypts the etcd volumes. Consider enabling etcd encryption only if you specifically require it for your use case.
====
+
.. Click *Next*.

. On the *Default machine pool* page, select a *Compute node instance type* and a *Compute node count*. The number and types of nodes that are available depend on your OpenShift Container Platform subscription. If you are using multiple availability zones, the compute node count is per zone.
+
[NOTE]
====
After your cluster is created, you can change the number of compute nodes, but you cannot change the compute node instance type in a machine pool. For clusters that use the CCS model, you can add machine pools after installation that use a different instance type. The number and types of nodes available to you depend on your OpenShift Container Platform subscription.
====

. Optional: Expand *Edit node labels* to add labels to your nodes. Click *Add label* to add more node labels and select *Next*.

. In the *Cluster privacy* dialog, select *Public* or *Private* to use either public or private API endpoints and application routes for your cluster.

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

. Click *Next*.

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
** Individual updates: If you select an update version that requires approval, provide an administrator's acknowledgment and click *Approve and continue*.
** Recurring updates: If you selected recurring updates for your cluster, provide an administrator's acknowledgment and click *Approve and continue*. {cluster-manager} does not start scheduled y-stream updates for minor versions without receiving an administrator's acknowledgment.
+
.. If you opted for recurring updates, select a preferred day of the week and upgrade start time in UTC from the drop-down menus.
.. Optional: You can set a grace period for *Node draining* during cluster upgrades. A *1 hour* grace period is set by default.
.. Click *Next*.
+
[NOTE]
====
If there are critical security concerns that significantly impact the security or stability of a cluster, Red Hat Site Reliability Engineering (SRE) might schedule automatic updates to the latest z-stream version that is not impacted. The updates are applied within 48 hours after customer notifications are provided. For a description of the critical impact security rating, see Understanding Red Hat security ratings.
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
// Module included in the following assemblies:
//
// * osd_getting_started/osd-getting-started.adoc

[id="config-idp_{context}"]
= Configuring an identity provider

[role="_abstract"]
After you have installed OpenShift Container Platform, you must configure your cluster to use an identity provider. You can then add members to your identity provider to grant them access to your cluster.

You can configure different identity provider types for your OpenShift Container Platform cluster. Supported types include GitHub, GitHub Enterprise, GitLab, Google, LDAP, OpenID Connect, and htpasswd identity providers.

[IMPORTANT]
====
The htpasswd identity provider option is included only to enable the creation of a single, static administration user. htpasswd is not supported as a general-use identity provider for OpenShift Container Platform.
====

The following procedure configures a GitHub identity provider as an example.

[WARNING]
====
Configuring GitHub authentication allows users to log in to OpenShift Container Platform with their GitHub credentials. To prevent anyone with any GitHub user ID from logging in to your OpenShift Container Platform cluster, you must restrict access to only those in specific GitHub organizations or teams.
====

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You have a GitHub user account.
* You created a GitHub organization in your GitHub account. For more information, see Creating a new organization from scratch in the GitHub documentation.
* If you are restricting user access to a GitHub team, you have created a team within your GitHub organization. For more information, see Creating a team in the GitHub documentation.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Select *Access control* -> *Identity providers*.

. Select the *GitHub* identity provider type from the *Add identity provider* drop-down menu.

. Enter a unique name for the identity provider. The name cannot be changed later.

. Register an OAuth application in your GitHub organization by following the steps in the GitHub documentation.
+
[NOTE]
====
You must register the OAuth app under your GitHub organization. If you register an OAuth application that is not owned by the organization that contains your cluster users or teams, then user authentication to the cluster will not succeed.
====

* For the homepage URL in your GitHub OAuth app configuration, specify the `\https://oauth-openshift.apps.<cluster_name>.<cluster_domain>` portion of the *OAuth callback URL* that is automatically generated in the *Add a GitHub identity provider* page on {cluster-manager}.
+
The following is an example of a homepage URL for a GitHub identity provider:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com
----

* For the authorization callback URL in your GitHub OAuth app configuration, specify the full *OAuth callback URL* that is automatically generated in the *Add a GitHub identity provider* page on {cluster-manager}. The full URL has the following syntax:
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----

. Return to the *Edit identity provider: GitHub* dialog in {cluster-manager-url} and select *Claim* from the *Mapping method* drop-down menu.

. Enter the *Client ID* and *Client secret* for your GitHub OAuth application. The GitHub page for your OAuth app provides the ID and secret.

. Optional: Enter a *hostname*.
+
[NOTE]
====
A hostname must be entered when using a hosted instance of GitHub Enterprise.
====

. Optional: You can specify a certificate authority (CA) file to validate server certificates for a configured GitHub Enterprise URL. Click *Browse* to locate and attach a *CA file* to the identity provider.

. Select *Use organizations* or *Use teams* to restrict access to a GitHub organization or a GitHub team within an organization.

. Enter the name of the organization or team you want to restrict access to. Click *Add more* to specify multiple organizations or teams.
+
[NOTE]
====
Specified organizations must own an OAuth app that was registered by using the preceding steps. If you specify a team, it must exist within an organization that owns an OAuth app that was registered by using the preceding steps.
====

. Click *Add* to apply the identity provider configuration.
+
[NOTE]
====
It might take approximately two minutes for the identity provider configuration to become active.
====

.Verification

* After the configuration becomes active, the identity provider is listed under *Access control* -> *Identity providers* on the {cluster-manager-url} page for your cluster.
// Module included in the following assemblies:
//
// * osd_getting_started/osd-getting-started.adoc
// * using-rbac.adoc

[id="osd-grant-admin-privileges_{context}"]
= Granting administrator privileges to a user

[role="_abstract"]
After you have configured an identity provider for your cluster and added a user to the identity provider, you can grant `dedicated-admin` cluster privileges to the user.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Click the *Access control* tab.

. In the *Cluster Roles and Access* tab, click *Add user*.

. Enter the user ID of an identity provider user.

. Click *Add user* to grant `dedicated-admin` cluster privileges to the user.

.Verification

* After granting the privileges, the user is listed as part of the `dedicated-admins` group under *Access control* -> *Cluster Roles and Access* on the {cluster-manager} page for your cluster.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="access-cluster_{context}"]
= Accessing your cluster

[role="_abstract"]
After you have configured your identity providers, users can access the cluster from {cluster-manager-first}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.
* You added your user account to the configured identity provider.

.Procedure

. From {cluster-manager-url}, select the cluster you want to access.

. Click *Open console* to open the web console for your cluster.

. Select your identity provider and enter your credentials to log in to the cluster. Complete any authorization requests from your provider.
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="deploy-app_{context}"]
= Deploy an application from the Developer Catalog

[role="_abstract"]
From the OpenShift Container Platform web console, you can deploy a test application from the Developer Catalog and expose it with a route.

.Prerequisites

* You logged in to the {hybrid-console-url}.
* You created a OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.
* You added your user account to the configured identity provider.

.Procedure

. Go to the *Cluster List* page in {cluster-manager-url}, click the options icon (&#8942;) next to your cluster, and select *Open console*. Log in to your Red{nbsp}Hat account with your configured identity provider credentials.

. In the *Administrator* perspective, select *Home* -> *Projects* -> *Create Project*, enter a name for your project, and click *Create*. Optional: Add a *Display Name* and *Description*.

. Switch to the *Developer* perspective and select *+Add*. Verify that the selected *Project* is the one you created.

. In the *Developer Catalog* dialog, select *All services*, then select *Languages* -> *JavaScript* from the menu and click *Node.js*.
+
[NOTE]
====
You might need to click *Clear All Filters* to display the *Node.js* option.
====

. To open the *Create Source-to-Image application* page, click *Create*.

. In the *Git* section, click *Try sample*, add a unique name in the *Name* field, and confirm that *Deployment* and *Create a route* are selected.

. Click *Create* to deploy the application. It takes a few minutes for the pods to deploy.

. Optional: Monitor the deployment status in the *Topology* pane by selecting your *Node.js* app and reviewing its sidebar. Wait for the `nodejs` build to complete and for the `nodejs` pod to be in a *Running* state.

. Access the deployed application by clicking the route URL, which has a format similar to:
+
----
https://nodejs-<project>.<cluster_name>.<hash>.<region>.openshiftapps.com/
----
+
A new browser tab opens displaying a message similar to:
+
----
Welcome to your Node.js application on OpenShift
----

. Optional: In the *Administrator* perspective, navigate to *Home* -> *Projects*, click the action menu for your project, and select *Delete Project* to clean up resources.

.Verification

* Verify that the application is running:
+
[source,terminal]
----
$ oc get pods -n <project_name>
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS      RESTARTS   AGE
nodejs-1-build             0/1     Completed   0          5m
nodejs-5d9c6c7d9c-kghq2   1/1     Running     0          2m
----

* Access the application route to verify it responds correctly.

[role="_additional-resources"]
.Additional resources

* Creating applications by using the CLI
* Creating applications by using the web console
* Understanding deployments

// Module included in the following assemblies:
//
// * osd_getting_started/osd-getting-started.adoc

[id="scaling-cluster_{context}"]
= Scaling your cluster

[role="_abstract"]
You can scale the number of load balancers, the persistent storage capacity, and the node count for your OpenShift Container Platform cluster from {cluster-manager}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.

.Procedure

* To scale the number of load balancers or the persistent storage capacity:
. Navigate to {cluster-manager-url} and select your cluster.
. Select *Edit load balancers and persistent storage* from the *Actions* drop-down menu.
. Select how many *Load balancers* that you want to scale to.
. Select the *Persistent storage* capacity that you want to scale to.
. Click *Apply*. Scaling occurs automatically.

* To scale the node count:
. Navigate to {cluster-manager-url} and select your cluster.
. Select *Edit node count* from the *Actions* drop-down menu.
. Select a *Machine pool*.
. Select a *Node count* per zone.
. Click *Apply*. Scaling occurs automatically.

.Verification

* In the *Overview* tab under the *Details* heading, you can review the load balancer configuration, persistent storage details, and actual and required node counts.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/osd-revoking-cluster-privileges.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="osd-revoke-admin-privileges_{context}"]
= Revoking administrator privileges from a user

[role="_abstract"]
After you have granted `dedicated-admin` privileges to a user, you can revoke those privileges when they are no longer needed.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.
* You granted `dedicated-admin` privileges to a user.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Click the *Access control* tab.

. In the *Cluster Roles and Access* tab, select {kebab} next to a user and click *Delete*.

.Verification

* After revoking the privileges, the user is no longer listed as part of the `dedicated-admins` group under *Access control* -> *Cluster Roles and Access* on the {cluster-manager} page for your cluster.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/osd-revoking-cluster-privileges.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="osd-revoke-user-access_{context}"]
= Revoking user access to a cluster

[role="_abstract"]
You can revoke cluster access from an identity provider user by removing them from your configured identity provider.

You can configure different types of identity providers for your OpenShift Container Platform cluster. The following example procedure revokes cluster access for a member of a GitHub organization or team that is configured for identity provision to the cluster.

.Prerequisites

* You have an OpenShift Container Platform cluster.
* You have a GitHub user account.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.

.Procedure

. Navigate to github.com and log in to your GitHub account.

. Remove the user from your GitHub organization or team:
* If your identity provider configuration uses a GitHub organization, follow the steps in Removing a member from your organization in the GitHub documentation.
* If your identity provider configuration uses a team within a GitHub organization, follow the steps in Removing organization members from a team in the GitHub documentation.

.Verification

* After removing the user from your identity provider, the user cannot authenticate into the cluster.
// Module included in the following assemblies:
//
// * osd_gcp_clusters/osd-deleting-a-cluster.adoc
// * osd_aws_clusters/osd-deleting-a-cluster.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="deleting-cluster_{context}"]
= Deleting your cluster

[role="_abstract"]
You can delete your OpenShift Container Platform cluster in {cluster-manager-first}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.

.Procedure

. From {cluster-manager-url}, select the cluster you want to delete.

. Select *Delete cluster* from the *Actions* drop-down menu.

. Type the name of the cluster highlighted in bold, then click *Delete*. Cluster deletion occurs automatically.

+
[NOTE]
====
If you delete a cluster that was installed into a {gcp-short} Shared VPC, inform the VPC owner of the host project to remove the IAM policy roles granted to the service account that was referenced during cluster creation.
====

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* Adding services to a cluster using the {cluster-manager} console
* Creating a Workload Identity Federation configuration
* Private Service Connect overview
* About machine pools
* Preparing to configure the user workload monitoring stack
* About autoscaling nodes on a cluster
* Customer administrator user
* Configuring identity providers
* OpenShift Container Platform update life cycle
* OpenShift Container Platform cluster upgrades
