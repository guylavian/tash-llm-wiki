---
title: "Selecting a cluster installation method and preparing it for users"
type: reference
domain: openshift
slug: installing-4-22-installing-preparing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-preparing
version: 4.22
family: installing
documentKind: "Documentation"
---

# Selecting a cluster installation method and preparing it for users

[id="installing-preparing"]
= Selecting a cluster installation method and preparing it for users

[role=”_abstract”]
Before you install OpenShift Container Platform, decide what kind of installation process to follow and verify that you have all of the required resources to prepare the cluster for users.

[id="installing-preparing-selecting-cluster-type"]
== Selecting a cluster installation type
Before you install an OpenShift Container Platform cluster, you need to select the best installation instructions to follow. Think about your answers to the following questions to select the best option.

[id="installing-preparing-install-manage"]
=== Do you want to install and manage an OpenShift Container Platform cluster yourself?

If you want to install and manage OpenShift Container Platform yourself, you can install it on the following platforms:

* Amazon Web Services (AWS) on 64-bit x86 instances
* Amazon Web Services (AWS) on 64-bit ARM instances
* Microsoft Azure on 64-bit x86 instances
* Microsoft Azure on 64-bit ARM instances
* Microsoft Azure Stack Hub
* {gcp-first} on 64-bit x86 instances
* {gcp-first} on 64-bit ARM instances
* {rh-openstack-first}
* {ibm-cloud-name}
* {ibm-z-name} or {ibm-linuxone-name} with z/VM
* {ibm-z-name} or {ibm-linuxone-name} with {op-system-base-full} KVM
* {ibm-z-name} or {ibm-linuxone-name} in an LPAR
* {ibm-power-name}
* {ibm-power-server-name}
* Nutanix
* VMware vSphere
* Bare metal or other platform agnostic infrastructure
// might want a note about single node here

You can deploy an OpenShift Container Platform 4 cluster to both on-premise hardware and to cloud hosting services, but all of the machines in a cluster must be in the same data center or cloud hosting service.

If you want to use OpenShift Container Platform but you do not want to manage the cluster yourself, you can choose from several managed service options. If you want a cluster that is fully managed by Red Hat, you can use OpenShift Dedicated. You can also use OpenShift as a managed service on {azure-short}, {aws-short}, {ibm-cloud-name}, or {gcp-full}. For more information about managed services, see the OpenShift Products page. If you install an OpenShift Container Platform cluster with a cloud virtual machine as a virtual bare metal, the corresponding cloud-based storage is not supported.

[id="installing-preparing-migrate"]
=== Have you used OpenShift Container Platform 3 and want to use OpenShift Container Platform 4?

If you used OpenShift Container Platform 3 and want to try OpenShift Container Platform 4, you need to understand how different OpenShift Container Platform 4 is. OpenShift Container Platform 4 weaves the Operators that package, deploy, and manage Kubernetes applications and the operating system that the platform runs on, {op-system-first}, together seamlessly. Instead of deploying machines and configuring their operating systems so that you can install OpenShift Container Platform on them, the {op-system} operating system is an integral part of the OpenShift Container Platform cluster. Deploying the operating system for the cluster machines is part of the installation process for OpenShift Container Platform. See Differences between OpenShift Container Platform 3 and 4.

Because you need to provision machines as part of the OpenShift Container Platform cluster installation process, you cannot upgrade an OpenShift Container Platform 3 cluster to OpenShift Container Platform 4. Instead, you must create a new OpenShift Container Platform 4 cluster and migrate your OpenShift Container Platform 3 workloads to them. For more information about migrating, see Migrating from OpenShift Container Platform 3 to 4 overview. Because you must migrate to OpenShift Container Platform 4, you can use any type of production cluster installation process to create your new cluster.

[id="installing-preparing-existing-components"]
=== Do you want to use existing components in your cluster?

Because the operating system is integral to OpenShift Container Platform, it is easier to let the installation program for OpenShift Container Platform stand up all of the infrastructure. These are called _installer provisioned infrastructure_ installations. In this type of installation, you can provide some existing infrastructure to the cluster, but the installation program deploys all of the machines that your cluster initially needs.

You can deploy an installer-provisioned infrastructure cluster without specifying any customizations to the cluster or its underlying machines to AWS, Azure, Azure Stack Hub, {gcp-short}, Nutanix.

If you need to perform basic configuration for your installer-provisioned infrastructure cluster, such as the instance type for the cluster machines, you can customize an installation for AWS, Azure, {gcp-short}, Nutanix.

For installer-provisioned infrastructure installations, you can use an existing VPC in AWS, vNet in Azure, or VPC in {gcp-short}. You can also reuse part of your networking infrastructure so that your cluster in AWS, Azure, {gcp-short} can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. If you have existing accounts and credentials on these clouds, you can re-use them, but you might need to modify the accounts to have the required permissions to install OpenShift Container Platform clusters on them.

You can use the installer-provisioned infrastructure method to create appropriate machine instances on your hardware for vSphere, and bare metal. Additionally, for vSphere, you can also customize additional network parameters during installation.

For some installer-provisioned infrastructure installations, for example on the {vmw-first} and bare metal platforms, the external traffic that reaches the ingress virtual IP (VIP) is not balanced between the default `IngressController` replicas. For {vmw-short}  and bare metal installer-provisioned infrastructure installations where exceeding the baseline `IngressController` router performance is expected, you must configure an external load balancer. Configuring an external load balancer achieves the performance of multiple `IngressController` replicas. For more information about the baseline `IngressController` performance, see Baseline Ingress Controller (router) performance. For more information about configuring an external load balancer, see Configuring a user-managed load balancer.

If you want to reuse extensive cloud infrastructure, you can complete a _user-provisioned infrastructure_ installation. With these installations, you manually deploy the machines that your cluster requires during the installation process. If you perform a user-provisioned infrastructure installation on AWS, Azure, Azure Stack Hub, you can use the provided templates to help you stand up all of the required components. You can also reuse a shared VPC on {gcp-short}. Otherwise, you can use the provider-agnostic installation method to deploy a cluster into other clouds.

You can also complete a user-provisioned infrastructure installation on your existing hardware. If you use {rh-openstack}, {ibm-z-name} or {ibm-linuxone-name}, {ibm-z-name} and {ibm-linuxone-name} with {op-system-base} KVM, {ibm-z-name} and {ibm-linuxone-name} in an LPAR, {ibm-power-title}, or vSphere, use the specific installation instructions to deploy your cluster. If you use other supported hardware, follow the bare metal installation procedure. For some of these platforms, such as vSphere and bare metal, you can also customize additional network parameters during installation.

[id="installing-preparing-security"]
=== Do you need extra security for your cluster?

If you use a user-provisioned installation method, you can configure a proxy for your cluster. The instructions are included in each installation procedure.

If you want to prevent your cluster on a public cloud from exposing endpoints externally, you can deploy a private cluster with installer-provisioned infrastructure on AWS, Azure, or {gcp-short}.

If you need to install your cluster that has limited access to the internet, such as a disconnected or restricted network cluster, you can mirror the installation packages and install the cluster from them. Follow detailed instructions for user-provisioned infrastructure installations into restricted networks for AWS, {gcp-short}, {ibm-z-name} or {ibm-linuxone-name}, {ibm-z-name} or {ibm-linuxone-name} with {op-system-base} KVM, {ibm-z-name} or {ibm-linuxone-name} in an LPAR, {ibm-power-name}, vSphere, or bare metal. You can also install a cluster into a restricted network using installer-provisioned infrastructure by following detailed instructions for AWS, {gcp-short}, {ibm-cloud-name}, Nutanix, {rh-openstack}, and vSphere.

If you need to deploy your cluster to an AWS GovCloud region, AWS China region, or Azure government region, you can configure those custom regions during an installer-provisioned infrastructure installation.

You can also configure the cluster machines to use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation during installation.

[IMPORTANT]
====
When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.
====

[id="installing-preparing-single-node"]
=== Are you installing single-node clusters at the edge?

You can use the assisted installer to deploy single node clusters for edge workloads.

[id="installing-preparing-cluster-for-users"]
== Preparing your cluster for users after installation

Some configuration is not required to install the cluster but recommended before your users access the cluster. You can customize the cluster itself by customizing the Operators that make up your cluster and integrate you cluster with other required systems, such as an identity provider.
//This link will change when we consolidate the customizations page with the postinstallation activities.

For a production cluster, you must configure the following integrations:

* Persistent storage
* An identity provider
* Monitoring core OpenShift Container Platform components

[id="installing-preparing-cluster-for-workloads"]
== Preparing your cluster for workloads

Depending on your workload needs, you might need to take extra steps before you begin deploying applications. For example, after you prepare infrastructure to support your application build strategy, you might need to make provisions for low-latency workloads or to protect sensitive workloads. You can also configure monitoring for application workloads.

Hiding until WMCO 10.19.0 GAs
If you plan to run ../../windows_containers/enabling-windows-container-workloads.adoc#enabling-windows-container-workloads[Windows workloads], you must enable hybrid networking with OVN-Kubernetes during the installation process; hybrid networking cannot be enabled after your cluster is installed.

[id="supported-installation-methods-for-different-platforms"]
== Supported installation methods for different platforms

You can perform different types of installations on different platforms.

[NOTE]
====
Not all installation options are supported for all platforms, as shown in the following tables. A checkmark indicates that the option is supported and links to the relevant section.
====

.Installer-provisioned infrastructure options
//This table is for all flavors of OpenShift, except OKD. A separate table is required because OKD does not support multiple AWS architecture types. Trying to maintain one table using conditions, while convenient, is very fragile and prone to publishing errors.
|===
||AWS (64-bit x86) |AWS (64-bit ARM) |Azure (64-bit x86) |Azure (64-bit ARM)|Azure Stack Hub |GCP (64-bit x86) |GCP (64-bit ARM) |Nutanix |{rh-openstack} |Bare metal (64-bit x86) |Bare metal (64-bit ARM) |vSphere |{ibm-cloud-name} |{ibm-z-name} |{ibm-power-name} |{ibm-power-server-name}

|Default
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|
|

|Custom
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|
|&#10003;
|&#10003;
|
|
|&#10003;

|Network customization
|&#10003;
|&#10003;
|&#10003;
|&#10003;

|&#10003;
|&#10003;
|&#10003;
|
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|
|

|Restricted network
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|
|&#10003;

|Private clusters
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|
|
|
|
|
|&#10003;
|
|
|&#10003;

|Existing virtual private networks
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|
|
|
|
|
|&#10003;
|
|
|&#10003;

|Government regions
|&#10003;
|
|&#10003;
|
|
|
|
|
|
|
|
|
|
|
|
|

|Secret regions
|&#10003;
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

|China regions
|&#10003;
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|===

//This table is for OKD only. A separate table is required because OKD does not support multiple AWS architecture types. Trying to maintain one table using conditions, while convenient, is very fragile and prone to publishing errors.
|===
||AWS |Azure |Azure Stack Hub |GCP |Nutanix |{rh-openstack} |Bare metal |vSphere |{ibm-cloud-name} |{ibm-z-name} |{ibm-power-name}

|Default
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|
|

|Custom
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|
|

|Network customization
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|
|
|&#10003;
|&#10003;
|
|

|Restricted network
|&#10003;
|
|
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|
|

|Private clusters
|&#10003;
|&#10003;
|
|&#10003;
|
|
|
|
|&#10003;
|
|

|Existing virtual private networks
|&#10003;
|&#10003;
|
|&#10003;
|
|
|
|
|&#10003;
|
|

|Government regions
|&#10003;
|&#10003;
|
|
|
|
|
|
|
|
|

|Secret regions
|&#10003;
|
|
|
|
|
|
|
|
|
|

|China regions
|&#10003;
|
|
|
|
|
|
|
|
|
|
|===

.User-provisioned infrastructure options
//This table is for all flavors of OpenShift, except OKD. A separate table is required because OKD does not support multiple AWS architecture types. Trying to maintain one table using conditions, while convenient, is very fragile and prone to publishing errors.
|===
||AWS (64-bit x86) |AWS (64-bit ARM) |Azure (64-bit x86) |Azure (64-bit ARM) |Azure Stack Hub |GCP (64-bit x86) |GCP (64-bit ARM) |Nutanix |{rh-openstack} |Bare metal (64-bit x86) |Bare metal (64-bit ARM) |vSphere |{ibm-cloud-name} |{ibm-z-name} |{ibm-z-name} with {op-system-base} KVM |{ibm-power-name} |Platform agnostic

|Custom
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;

|Network customization
|
|
|
|
|
|
|
|
|
|&#10003;
|&#10003;
|&#10003;
|
|
|
|
|

|Restricted network
|&#10003;
|&#10003;
|
|
|
|&#10003;
|&#10003;
|
|
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|

|Shared VPC hosted outside of cluster project
|
|
|
|
|
|&#10003;
|&#10003;
|
|
|
|
|
|
|
|
|
|
|
|===

//This table is for OKD only. A separate table is required because OKD does not support multiple AWS architecture types. Trying to maintain one table using conditions, while convenient, is very fragile and prone to publishing errors.
|===
||AWS |Azure |Azure Stack Hub |GCP |Nutanix |{rh-openstack}|Bare metal |vSphere |{ibm-cloud-name} |{ibm-z-name} |{ibm-z-name} with {op-system-base} KVM |{ibm-power-name} |Platform agnostic

|Custom
|&#10003;
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|&#10003;

|Network customization
|
|
|
|
|
|
|&#10003;
|&#10003;
|
|
|
|
|

|Restricted network
|&#10003;
|
|
|&#10003;
|
|
|&#10003;
|&#10003;
|
|&#10003;
|&#10003;
|&#10003;
|

|Shared VPC hosted outside of cluster project
|
|
|
|&#10003;
|
|
|
|
|
|
|
|
|
|===

.Special use cases
|===
|Single Node

|&#10003;

|===
// sync
