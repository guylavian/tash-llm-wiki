---
title: "Configuring an {ibm-cloud-title} account"
type: reference
domain: openshift
slug: installing-4-22-installing-ibm-cloud-account-power-vs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-ibm-cloud-account-power-vs
version: 4.22
family: installing
documentKind: "Documentation"
---

# Configuring an {ibm-cloud-title} account

[id="installing-ibm-cloud-account-power-vs"]
= Configuring an {ibm-cloud-title} account

Before you can install OpenShift Container Platform, you must configure an {ibm-cloud-name} account.

[id="prerequisites_installing-ibm-cloud-account-power-vs"]
== Prerequisites

* You have an {ibm-cloud-name} account with a subscription. You cannot install OpenShift Container Platform on a free or on a trial {ibm-cloud-name} account.

// Module included in the following assemblies:
//
// installing/installing_ibm_powervs/installing-ibm-cloud-account-power-vs.adoc

[id="quotas-and-limits-ibm-power-vs_{context}"]
= Quotas and limits on {ibm-power-server-title}

The OpenShift Container Platform cluster uses several {ibm-cloud-name} and {ibm-power-server-name} components, and the default quotas and limits affect your ability to install OpenShift Container Platform clusters. If you use certain cluster configurations, deploy your cluster in certain regions, or run multiple clusters from your account, you might need to request additional resources for your {ibm-cloud-name} account.

For a comprehensive list of the default {ibm-cloud-name} quotas and service limits, see the {ibm-cloud-name} documentation for Quotas and service limits.

== Virtual Private Cloud

Each OpenShift Container Platform cluster creates its own Virtual Private Cloud (VPC). The default quota of VPCs per region is 10. If you have 10 VPCs created, you will need to increase your quota before attempting an installation.

== Application load balancer

By default, each cluster creates two application load balancers (ALBs):

* Internal load balancer for the control plane API server
* External load balancer for the control plane API server

You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs are 50 per region. To have more than 50 ALBs, you must increase this quota.

VPC ALBs are supported. Classic ALBs are not supported for {ibm-power-server-name}.

== Transit Gateways

Each OpenShift Container Platform cluster creates its own Transit Gateway to enable communication with a VPC. The default quota of transit gateways per account is 10. If you have 10 transit gateways created, you will need to increase your quota before attempting an installation.

== Dynamic Host Configuration Protocol Service

There is a limit of one Dynamic Host Configuration Protocol (DHCP) service per {ibm-power-server-name} instance.

== Virtual Server Instances

By default, a cluster creates server instances with the following resources :

* 0.5 CPUs
* 32 GB RAM
* System Type: `s922`
* Processor Type: `uncapped`, `shared`
* Storage Tier: `Tier-3`

The following nodes are created:

* One bootstrap machine, which is removed after the installation is complete
* Three control plane nodes
* Three compute nodes

For more information, see Creating a Power Systems Virtual Server in the {ibm-cloud-name} documentation.

[id="configuring-dns-resolution-powervs"]
== Configuring DNS resolution

How you configure DNS resolution depends on the type of OpenShift Container Platform cluster you are installing:

* If you are installing a public cluster, you use {ibm-cloud-name} Internet Services (CIS).
* If you are installing a private cluster, you use {ibm-cloud-name} DNS Services (DNS Services).

// Module included in the following assemblies:
//
// installing/installing_ibm_cloud/installing-ibm-cloud-account.adoc
// installing/installing_ibm_powervs/installing-ibm-cloud-account-power-vs.adoc

[id="installation-cis-ibm-cloud_{context}"]
= Using {ibm-cloud-title} Internet Services for DNS resolution

The installation program uses {ibm-cloud-name} Internet Services (CIS) to configure cluster DNS resolution and provide name lookup for a public cluster.

[NOTE]
====
This offering does not support IPv6, so dual stack or IPv6 environments are not possible.
====

You must create a domain zone in CIS in the same account as your cluster. You must also ensure the zone is authoritative for the domain. You can do this using a root domain or subdomain.

.Prerequisites

* You have installed the {ibm-cloud-name} CLI.
* You have an existing domain and registrar. For more information, see the {ibm-name} documentation.

.Procedure

. Create a CIS instance to use with your cluster:

.. Install the CIS plugin:
+
[source,terminal]
----
$ ibmcloud plugin install cis
----

.. Log in to {ibm-cloud-name} by using the CLI:
+
[source,terminal]
----
$ ibmcloud login
----

.. Create the CIS instance:
+
[source,terminal]
----
$ ibmcloud cis instance-create <instance_name> standard-next <1>
----
<1> At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records.
+
[NOTE]
====
After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect.
====

. Connect an existing domain to your CIS instance:

.. Set the context instance for CIS:
+
[source,terminal]
----
$ ibmcloud cis instance-set <instance_name> <1>
----
<1> The instance cloud resource name.
+
[source,terminal]
----
$ ibmcloud cis instance-set <instance_CRN> <1>
----
<1> The instance CRN (Cloud Resource Name).
For example: `ibmcloud cis instance-set crn:v1:bluemix:public:power-iaas:osa21:a/65b64c1f1c29460d8c2e4bbfbd893c2c:c09233ac-48a5-4ccb-a051-d1cfb3fc7eb5::`

.. Add the domain for CIS:
+
[source,terminal]
----
$ ibmcloud cis domain-add <domain_name> <1>
----
<1> The fully qualified domain name. You can use either the root domain or subdomain value as the domain name, depending on which you plan to configure.
+
[NOTE]
====
A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`.
====

. Open the CIS web console, navigate to the *Overview* page, and note your CIS name servers. These name servers will be used in the next step.

. Configure the name servers for your domains or subdomains at the domain's registrar or DNS provider. For more information, see the {ibm-cloud-name} documentation.

// Module included in the following assemblies:
//
// installing/installing_ibm_cloud/installing-ibm-cloud-account.adoc
// installing/installing_ibm_powervs/installing-ibm-cloud-account-power-vs.adoc

[id="installation-ibm-cloud-iam-policies-api-key_{context}"]
= {ibm-cloud-title} IAM Policies and API Key

To install OpenShift Container Platform into your {ibm-cloud-name} account, the installation program requires an IAM API key, which provides authentication and authorization to access {ibm-cloud-name} service APIs. You can use an existing IAM API key that contains the required policies or create a new one.

For an {ibm-cloud-name} IAM overview, see the {ibm-cloud-name} documentation.

[id="required-access-policies-ibm-cloud_{context}"]
== Required access policies

You must assign the required access policies to your {ibm-cloud-name} account.

.Required access policies
[cols="1,2,2,2,3",options="header"]
|===
|Service type |Service |Access policy scope |Platform access |Service access

|Account management
|IAM Identity Service
|All resources or a subset of resources ^[1]^
|Editor, Operator, Viewer, Administrator
|Service ID creator

|Account management ^[2]^
|Identity and Access Management
|All resources
|Editor, Operator, Viewer, Administrator
|

|Account management
|Resource group only
|All resource groups in the account
|Administrator
|

|IAM services
|Cloud Object Storage
|All resources or a subset of resources ^[1]^
|Editor, Operator, Viewer, Administrator
|Reader, Writer, Manager, Content Reader, Object Reader, Object Writer

|IAM services
|Internet Services
|All resources or a subset of resources ^[1]^
|Editor, Operator, Viewer, Administrator
|Reader, Writer, Manager

|IAM services
|DNS Services
|All resources or a subset of resources ^[1]^
|Editor, Operator, Viewer, Administrator
|Reader, Writer, Manager

|IAM services
|VPC Infrastructure Services
|All resources or a subset of resources ^[1]^
|Editor, Operator, Viewer, Administrator
|Reader, Writer, Manager
|===
[.small]
--
1. The policy access scope should be set based on how granular you want to assign access. The scope can be set to *All resources* or *Resources based on selected attributes*.
2. Optional: This access policy is only required if you want the installation program to create a resource group. For more information about resource groups, see the {ibm-name} documentation.
--
//TODO: IBM confirmed current values in the table above. They hope to provide more guidance on possibly scoping down the permissions (related to resource group actions).

[id="pre-requisite-permissions-ibm-cloud_{context}"]
== Pre-requisite permissions

.Pre-requisite permissions
[cols="1,2",options="header"]
|===
|Role |Access

|Viewer, Operator, Editor, Administrator, Reader, Writer, Manager
|Internet Services service in <resource_group> resource group

|Viewer, Operator, Editor, Administrator, User API key creator, Service ID creator
|IAM Identity Service service

|Viewer, Operator, Administrator, Editor, Reader, Writer, Manager, Console Administrator
|VPC Infrastructure Services service in <resource_group> resource group

|Viewer
|Resource Group: Access to view the resource group itself. The resource type should equal `Resource group`, with a value of <your_resource_group_name>.
|===

[id="cluster-creation-permissions-ibm-cloud_{context}"]
== Cluster-creation permissions

.Cluster-creation permissions
[cols="1,2",options="header"]
|===
|Role |Access

|Viewer
|<resource_group> (Resource Group Created for Your Team)

|Viewer, Operator, Editor, Reader, Writer, Manager
|All Identity and IAM enabled services in Default resource group

|Viewer, Reader
|Internet Services service

|Viewer, Operator, Reader, Writer, Manager, Content Reader, Object Reader, Object Writer, Editor
|Cloud Object Storage service

|Viewer
|Default resource group: The resource type should equal `Resource group`, with a value of `Default`. If your account administrator changed your account's default resource group to something other than Default, use that value instead.

|Viewer, Operator, Editor, Reader, Manager
|Workspace for {ibm-power-server-name} service in <resource_group> resource group

|Viewer, Operator, Editor, Reader, Writer, Manager, Administrator
|Internet Services service in <resource_group> resource group: CIS functional scope string equals reliability

|Viewer, Operator, Editor
|Transit Gateway service

|Viewer, Operator, Editor, Administrator, Reader, Writer, Manager, Console Administrator
|VPC Infrastructure Services service <resource_group> resource group
|===

[id="access-policy-assignment-ibm-cloud_{context}"]
== Access policy assignment

In {ibm-cloud-name} IAM, access policies can be attached to different subjects:
In {ibm-cloud-name} IAM, access policies can be attached to different subjects:

* Access group (Recommended)
* Service ID
* User

[NOTE]
====
The recommended method is to define IAM access policies in an access group. This helps organize all the access required for OpenShift Container Platform and enables you to onboard users and service IDs to this group. You can also assign access to users and service IDs directly, if desired.
====

// Module included in the following assemblies:
//
// installing/installing_ibm_cloud/installing-ibm-cloud-account.adoc
// installing/installing_ibm_powervs/installing-ibm-cloud-account-power-vs.adoc

[id="installation-ibm-cloud-creating-api-key_{context}"]
= Creating an API key

You must create a user API key or a service ID API key for your {ibm-cloud-name} account.

.Prerequisites

* You have assigned the required access policies to your {ibm-cloud-name} account.
* You have attached you IAM access policies to an access group, or other appropriate resource.

.Procedure

* Create an API key, depending on how you defined your IAM access policies.
+
For example, if you assigned your access policies to a user, you must create a user API key. If you assigned your access policies to a service ID, you must create a service ID API key. If your access policies are assigned to an access group, you can use either API key type. For more information on {ibm-cloud-name} API keys, see Understanding API keys.

// Module included in the following assemblies:
//
// installing/installing_ibm_cloud/installing-ibm-cloud-account.adoc
// installing/installing_ibm_powervs/installing-ibm-cloud-account-power-vs.adoc

[id="installation-ibm-cloud-regions_{context}"]
= Supported {ibm-cloud-title} regions

[id="installation-ibm-power-vs-regions_{context}"]
= Supported {ibm-power-server-title} regions and zones

You can deploy an OpenShift Container Platform cluster to the following regions:

//Not listed for openshift-install: br-sao, in-che, kr-seo

* `au-syd` (Sydney, Australia)
* `br-sao` (Sao Paulo, Brazil)
* `ca-tor` (Toronto, Canada)
* `eu-de` (Frankfurt, Germany)
* `eu-gb` (London, United Kingdom)
* `eu-es` (Madrid, Spain)
* `jp-osa` (Osaka, Japan)
* `jp-tok` (Tokyo, Japan)
* `us-east` (Washington DC, United States)
* `us-south` (Dallas, United States)

[NOTE]
====
Deploying your cluster in the `eu-es` (Madrid, Spain) region is not supported for OpenShift Container Platform 4.14.6 and earlier versions.
====

* `tor` (Toronto, Canada)
** `tor01`
* `dal` (Dallas, USA)
** `dal10`
** `dal12`
* `eu-de` (Frankfurt, Germany)
** `eu-de-1`
** `eu-de-2`
* `lon` (London, UK)
** `lon04`
** `lon06`
* `mad` (Madrid, Spain)
** `mad02`
** `mad04`
* `osa` (Osaka, Japan)
** `osa21`
* `sao` (Sao Paulo, Brazil)
** `sao01`
** `sao04`
* `syd` (Sydney, Australia)
** `syd04`
** `syd05`
* `wdc` (Washington DC, USA)
** `wdc06`
** `wdc07`
* `us-east` (Washington DC, United States)
** `us-east`
* `us-south` (Dallas, United States)
** `us-south`

You might optionally specify the {ibm-cloud-name} region in which the installation program creates any VPC components.

[NOTE]
====
If you do not specify the region, the installation program selects the region closest to {ibm-power-server-title} zone you are deploying to.
====

{ibm-cloud-name} supports the following regions:

* `us-east`
* `us-south`
* `eu-de`
* `eu-es`
* `eu-gb`
* `jp-osa`
* `au-syd`
* `br-sao`
* `ca-tor`
* `jp-tok`

[id="next-steps_installing-ibm-cloud-account-power-vs"]
== Next steps
* Creating an {ibm-power-server-name} workspace
