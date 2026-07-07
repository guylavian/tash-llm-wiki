---
title: "Installing a cluster on AWS in a disconnected environment with user-provisioned infrastructure"
type: reference
domain: openshift
slug: installing-4-22-installing-restricted-networks-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-restricted-networks-aws
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on AWS in a disconnected environment with user-provisioned infrastructure

[id="installing-restricted-networks-aws"]
= Installing a cluster on AWS in a disconnected environment with user-provisioned infrastructure

In OpenShift Container Platform version , you can install a
cluster on Amazon Web Services (AWS) using infrastructure that you provide and
an internal mirror of the installation release content.

[IMPORTANT]
====
While you can install an OpenShift Container Platform cluster by using mirrored installation
release content, your cluster still requires internet access to use the AWS APIs.
====

One way to create this infrastructure is to use the provided
CloudFormation templates. You can modify the templates to customize your
infrastructure or use the information that they contain to create AWS objects
according to your company's policies.

[IMPORTANT]
====
The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several CloudFormation templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.
====

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You created a mirror registry on your mirror host and obtained the `imageContentSources` data for your version of OpenShift Container Platform.
+
[IMPORTANT]
====
Because the installation media is on the mirror host, you can use that computer to complete all installation steps.
====
* You configured an AWS account to host the cluster.
+
[IMPORTANT]
====
If you have an AWS profile stored on your computer, it must not use a temporary session token that you generated while using a multi-factor authentication device. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials. To generate appropriate keys, see Managing Access Keys for IAM Users in the AWS documentation. You can supply the keys when you run the installation program.
====
* You prepared the user-provisioned infrastructure.
* You downloaded the AWS CLI and installed it on your computer. See Install the AWS CLI Using the Bundled Installer (Linux, macOS, or UNIX) in the AWS documentation.
* If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can manually create and maintain long-term credentials.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc

[id="installation-about-restricted-networks_{context}"]
= About installations in restricted networks

In OpenShift Container Platform , you can perform an installation that does not
require an active connection to the internet to obtain software components. Restricted network installations can be completed using installer-provisioned infrastructure or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you choose to perform a restricted network installation on a cloud platform, you
still require access to its cloud APIs. Some cloud functions, like
Amazon Web Service's Route 53 DNS and IAM services, require internet access.
//behind a proxy
Depending on your network, you might require less internet
access for an installation on bare metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that
mirrors the contents of the {product-registry} and contains the
installation media. You can create this registry on a mirror host, which can
access both the internet and your closed network, or by using other methods
that meet your restrictions.

[IMPORTANT]
====
Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you attempt a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network.
====

[id="required-internet-access-and-an-installation-host_{context}"]
== Required internet access and an installation host

You complete the installation using a bastion host or portable device that can access both the internet and your closed network. You must use a host with internet access to:

* Download the installation program, the OpenShift CLI (`oc`), and the CCO utility (`ccoctl`).
* Use the installation program to locate the {op-system-first} image and create the installation configuration file.
* Use `oc` to extract `ccoctl` from the CCO container image.
* Use `oc` and `ccoctl` to configure IAM for {ibm-cloud-name}.

[id="access-to-a-mirror-registry_{context}"]
== Access to a mirror registry

To complete a restricted network installation, you must create a registry that
mirrors the contents of the {product-registry} and contains the installation media.

You can create this registry on a mirror host, which can access both the internet and your restricted network, or by using other methods that meet your organization's security restrictions.

For more information on mirroring images for a disconnected installation, see "Additional resources".

[id="access-to-ibm-service-endpoints_{context}"]
== Access to IBM service endpoints

The installation program requires access to the following {ibm-cloud-name} service endpoints:

* Cloud Object Storage
* DNS Services
* Global Search
* Global Tagging
* Identity Services
* Resource Controller
* Resource Manager
* VPC

[NOTE]
====
If you are specifying an {ibm-name} Key Protect for {ibm-cloud-name} root key as part of the installation process, the service endpoint for Key Protect is also required.
====

By default, the public endpoint is used to access the service. If network restrictions limit access to public service endpoints, you can override the default behavior.

Before deploying the cluster, you can update the installation configuration file (`install-config.yaml`) to specify the URI of an alternate service endpoint. For more information on usage, see "Additional resources".

[id="installation-restricted-network-limits_{context}"]
== Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates`
error.
//* The authentication Operator might randomly fail.
* By default, you cannot use the contents of the Developer Catalog because
 you cannot access the required image stream tags.
//* The `TelemeterClientDown` and `Watchdog` alerts from the monitoring Operator always display.

//You extract the installation program from the mirrored content.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installaing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-generate_{context}"]
= Creating the installation files for {cp}

To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You manually create the `install-config.yaml` file, and then generate and customize the Kubernetes manifests and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.
To install OpenShift Container Platform on {cp-first} into a shared VPC, you must generate the `install-config.yaml` file and modify it so that the cluster uses the correct VPC networks, DNS zones, and project names.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

// Similar content to what is in this module is also present in modules/installation-disk-partitioning.adoc. <-- This module is in use with the following vSphere assemblies:
//    * installing-vsphere.adoc
//    * installing-vsphere-network-customizations.adoc
//    * installing-restricted-networks-vsphere.adoc

// Similar content to what is in this module is also present in modules/installation-user-infra-machines-advanced.adoc. <-- This module is in use with the following bare metal assemblies:
//    * installing-bare-metal-network-customizations.adoc
//    * installing-bare-metal.adoc
//    * installing-restricted-networks-bare-metal.adoc

[id="installation-disk-partitioning-upi-templates_{context}"]
= Optional: Creating a separate `/var` partition

It is recommended that disk partitioning for OpenShift Container Platform be left to the installer. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of {op-system-first}, the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation.

[IMPORTANT]
====
If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section.
====

.Procedure

. Create a directory to hold the OpenShift Container Platform installation files:
+
[source,terminal]
----
$ mkdir $HOME/clusterconfig
----

. Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted:
+
[source,terminal]
----
$ openshift-install create manifests --dir $HOME/clusterconfig
----
+
.Example output
+
[source,terminal]
----
? SSH Public Key ...
INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
INFO Consuming Install Config from target directory
INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
----

. Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory:
+
[source,terminal]
----
$ ls $HOME/clusterconfig/openshift/
----
+
.Example output
+
[source,terminal]
----
99_kubeadmin-password-secret.yaml
99_openshift-cluster-api_master-machines-0.yaml
99_openshift-cluster-api_master-machines-1.yaml
99_openshift-cluster-api_master-machines-2.yaml
...
----

. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-var-partition
storage:
  disks:
  - device: /dev/disk/by-id/<device_name> <1>
    partitions:
    - label: var
      start_mib: <partition_start_offset> <2>
      size_mib: <partition_size> <3>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota] <4>
      with_mount_unit: true
----
+
<1> The storage device name of the disk that you want to partition.
<2> When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of {op-system} might overwrite the beginning of the data partition.
<3> The size of the data partition in mebibytes.
<4> The `prjquota` mount option must be enabled for filesystems used for container storage.
+
[NOTE]
====
When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name.
====

. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
----

. Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories:
+
[source,terminal]
----
$ openshift-install create ignition-configs --dir $HOME/clusterconfig
----
+
[source,terminal]
----
$ ls $HOME/clusterconfig/
auth  bootstrap.ign  master.ign  metadata.json  worker.ign
----
+
You can now use the Ignition config files as input to the installation procedures to install {op-system-first} systems.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-generate-aws-user-infra-install-config_{context}"]
= Creating the installation configuration file

Generate and customize the installation configuration file that the
installation program needs to deploy your cluster.

.Prerequisites

* You obtained the OpenShift Container Platform installation program
for user-provisioned infrastructure
and the pull secret for your cluster.
For a restricted network installation, these files are on your mirror host.
* You checked that you are deploying your cluster to an AWS Region with an accompanying {op-system-first} AMI published by Red Hat. If you are deploying to an AWS Region that requires a custom AMI, such as an AWS GovCloud Region, you must create the `install-config.yaml` file manually.

.Procedure

. Create the `install-config.yaml` file.
.. Change to the directory that contains the installation program and run the following command:
+
[source,terminal]
----
$ ./openshift-install create install-config --dir <installation_directory> <1>
----
<1> For `<installation_directory>`, specify the directory name to store the
files that the installation program creates.
+
[IMPORTANT]
====
Specify an empty directory. Some installation assets, like bootstrap X.509
certificates have short expiration intervals, so you must not reuse an
installation directory. If you want to reuse individual files from another
cluster installation, you can copy them into your directory. However, the file
names for the installation assets might change between releases. Use caution
when copying installation files from an earlier OpenShift Container Platform version.
====
.. At the prompts, provide the configuration details for your cloud:
... Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
... Select *aws* as the platform to target.
... If you do not have an AWS profile stored on your computer, enter the AWS
access key ID and secret access key for the user that you configured to run the
installation program.
+
[NOTE]
====
The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file.
====
... Select the AWS Region to deploy the cluster to.
... Select the base domain for the Route 53 service that you configured for your cluster.
... Enter a descriptive name for your cluster.
... Paste the {cluster-manager-url-pull}.
This field is optional.

. Edit the `install-config.yaml` file to give the additional information that
is required for an installation in a restricted network.
.. Update the `pullSecret` value to contain the authentication information for
your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<local_registry>`, specify the registry domain name, and optionally the
port, that your mirror registry uses to serve content. For example
`registry.example.com` or `registry.example.com:5000`. For `<credentials>`,
specify the base64-encoded user name and password for your mirror registry.
.. Add the `additionalTrustBundle` parameter and value. The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
+
[source,yaml]
----
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
----
.. Add the image content resources:
+
[source,yaml]
----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----
+
Use the `imageContentSources` section from the output of the command to mirror the repository or the values that you used when you mirrored the content from the media that you brought into your restricted network.

.. Optional: Set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.

. If you are installing a three-node cluster, modify the `install-config.yaml` file by setting the `compute.replicas` parameter to `0`. This ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on AWS".

. Optional: Back up the `install-config.yaml` file.
+
[IMPORTANT]
====
The `install-config.yaml` file is consumed during the installation process. If
you want to reuse the file, you must back it up now.
====

[role="_additional-resources"]
.Additional resources

* See Configuration and credential file settings in the AWS documentation for more information about AWS profile and credential configuration.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing_aws-customizations.adoc
// * installing/installing_aws/installing_aws-private.adoc
// * installing/installing_aws/installing_aws-vpc.adoc
// * installing/installing_aws/installing_aws-china.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/
//installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * networking/configuring-a-custom-pki.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-configure-proxy_{context}"]
= Configuring the cluster-wide proxy during installation

[role="_abstract"]
Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform
cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

[NOTE]
====
For bare-metal installations, if you do not assign node IP addresses from the range that is specified in the `networking.machineNetwork[].cidr` field in the `install-config.yaml` file, you must include them in the `proxy.noProxy` field.
====

.Prerequisites
* You have an existing `install-config.yaml` file.

* You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object's `spec.noProxy` field to bypass the proxy if necessary.
+
[NOTE]
====
The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.

For installations on Amazon Web Services (AWS), {gcp-first}, Microsoft Azure, and {rh-openstack-first}, the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).
====

.Procedure

. Edit your `install-config.yaml` file and add the proxy settings. For example:
+
[source,yaml]
----
apiVersion: v1
baseDomain: my.domain.com
proxy:
  httpProxy: http://<username>:<pswd>@<ip>:<port>
  httpsProxy: https://<username>:<pswd>@<ip>:<port>
  noProxy: example.com
  noProxy: ec2.<aws_region>.amazonaws.com,elasticloadbalancing.<aws_region>.amazonaws.com,s3.<aws_region>.amazonaws.com
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
# ...
----
+
where:
+
`proxy.httpProxy`:: Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.
`proxy.httpsProxy`:: Specifies a proxy URL to use for creating HTTPS connections outside the cluster.
`proxy.noProxy`:: Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.
If you have added the Amazon `EC2`, `Elastic Load Balancing`, and `S3` VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.
You must include vCenter's IP address and the IP range that you use for its machines.
`additionalTrustBundle`:: If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the {op-system} trust bundle. The `additionalTrustBundle` field is required unless the proxy's identity certificate is signed by an authority from the {op-system} trust bundle.
`additionalTrustBundlePolicy`:: Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.
+
[NOTE]
====
The installation program does not support the proxy `readinessEndpoints` field.
====
+
[NOTE]
====
If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

[source,terminal]
----
$ ./openshift-install wait-for install-complete --log-level debug
----
====

. Save the file and reference it when installing OpenShift Container Platform.
+
The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.
+
[NOTE]
====
Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.
====

//include::modules/installation-three-node-cluster.adoc[leveloffset=+2]

// Creating the Kubernetes manifest and Ignition config files
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-generate-k8s-manifest-ignition_{context}"]
= Creating the Kubernetes manifest and Ignition config files

[role="_abstract"]
To customize cluster definitions and manually start machines, generate the Kubernetes manifest and Ignition config files.

The installation configuration file transforms into the Kubernetes manifests. The manifests wrap into the Ignition configuration files, which are later used to configure the cluster machines.

[IMPORTANT]
====
* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program runs on s390x only. This installer program is also available as a macOS version.
====
[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installer program is also available as a macOS version.
====

.Prerequisites

* You obtained the OpenShift Container Platform installation program.
For a restricted network installation, these files are on your mirror host.
* You created the `install-config.yaml` installation configuration file.

.Procedure

. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
where
+
`<installation_directory>`:: Specifies the installation directory that contains the `install-config.yaml` file you created.

. Remove the Kubernetes manifest files that define the control plane machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
----
+
By removing these files, you prevent the cluster from automatically generating control plane machines.

. Remove the Kubernetes manifest files that define the control plane machine set:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----

. Optional: If you do not want the cluster to provision compute machines, remove
the Kubernetes manifest files that define the worker machines:
. Remove the Kubernetes manifest files that define the worker machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
----
+
[IMPORTANT]
====
If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.
====
+
Because you create and manage the worker machines yourself, you do not need to initialize these machines.

. Remove the Kubernetes manifest files that define the control plane machines, compute machine sets, and control plane machine sets:
+
[source,terminal]
----
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----
+
Because you create and manage these resources yourself, you do not have to initialize them. You can preserve the compute machine set files to create compute machines by using the machine API, but you must update references to them to match your environment.
+
[WARNING]
====
If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.
====
+
[IMPORTANT]
====
When you configure control plane nodes from the default unschedulable to schedulable, additional subscriptions are required. This is because control plane nodes then become compute nodes.
====

. Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:
+
.. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
+
.. Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.
+
.. Save and exit the file.

. Optional: If you do not want
the Ingress Operator
to create DNS records on your behalf, remove the `privateZone` and `publicZone`
sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
. Remove the `privateZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: null
  name: cluster
spec:
  baseDomain: example.openshift.com
  privateZone:
    id: mycluster-100419-private-zone
  publicZone: <1>
    id: example.openshift.com
status: {}
----
`spec.privateZone`: Remove this section completely.
+
If you do so, you must add ingress DNS records manually in a later step.

. Configure the cloud provider for your VPC.
+
.. Open the `<installation_directory>/manifests/cloud-provider-config.yaml` file.
+
.. Add the `network-project-id` parameter and set its value to the ID of project that hosts the shared VPC network.
+
.. Add the `network-name` parameter and set its value to the name of the shared VPC network that hosts the OpenShift Container Platform cluster.
+
.. Replace the value of the `subnetwork-name` parameter with the value of the shared VPC subnet that hosts your compute machines.
+
The contents of the `<installation_directory>/manifests/cloud-provider-config.yaml` resemble the following example:
+
[source,yaml]
----
config: |+
  [global]
  project-id      = example-project
  regional        = true
  multizone       = true
  node-tags       = opensh-ptzzx-master
  node-tags       = opensh-ptzzx-worker
  node-instance-prefix = opensh-ptzzx
  external-instance-groups-prefix = opensh-ptzzx
  network-project-id = example-shared-vpc
  network-name    = example-network
  subnetwork-name = example-worker-subnet
----

. If you deploy a cluster that is not on a private network, open the `<installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml` file and replace the value of the `scope` parameter with `External`. The contents of the file resemble the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
    type: LoadBalancerService
status:
  availableReplicas: 0
  domain: ''
  selector: ''
----

. Optional: If your Azure Stack Hub environment uses an internal certificate authority (CA), you must update the `.spec.trustedCA.name` field in the `<installation_directory>/manifests/cluster-proxy-01-config.yaml` file to use `user-ca-bundle`:
+
[source,yaml]
----
...
spec:
  trustedCA:
    name: user-ca-bundle
...
----
+
Later, you must update your bootstrap ignition to include the CA.

. When configuring Azure on user-provisioned infrastructure, you must export
some common variables defined in the manifest files to use later in the Azure
Resource Manager (ARM) templates:
+
.. Export the infrastructure ID by using the following command:
+
[source,terminal]
----
$ export INFRA_ID=<infra_id>
----
+
where:
+
`<infra_id>`:: Specifies that the OpenShift Container Platform cluster has been assigned an identifier (`INFRA_ID`) in the form of `<cluster_name>-<random_string>`. This identifier is used as the base name for most resources created using the provided ARM templates. This is the value of the `.status.infrastructureName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.
+
.. Export the resource group by using the following command:
+
[source,terminal]
----
$ export RESOURCE_GROUP=<resource_group>
----
+
where:
+
`<resource_group>`:: All resources created in this Azure deployment exists as part of a resource group. The resource group name is also based on the `INFRA_ID`, in the form of `<cluster_name>-<random_string>-rg`. This is the value of the `.status.platformStatus.azure.resourceGroupName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.

. Manually create your cloud credentials.
+
.. From the directory that contains the installation program, obtain details of the OpenShift Container Platform release image that your `openshift-install` binary is built to use:
+
[source,terminal]
----
$ openshift-install version
----
+
.Example output
[source,text]
----
release image quay.io/openshift-release-dev/ocp-release:4.y.z-x86_64
----
+
.. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
+
.. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \//
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \//
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`::  Specifies to include only the manifests that your specific cluster configuration requires.
`<path_to_directory_with_installation_configuration>`:: Specifies the location of the `install-config.yaml` file.
`<path_to_directory_for_credentials_requests>`:: Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
This command creates a YAML file for each `CredentialsRequest` object.
+
.Sample `CredentialsRequest` object
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  labels:
    controller-tools.k8s.io: "1.0"
  name: openshift-image-registry-azure
  namespace: openshift-cloud-credential-operator
spec:
  secretRef:
    name: installer-cloud-credentials
    namespace: openshift-image-registry
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
----
+
.. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. The format for the secret data varies for each cloud provider.
+
.Sample `secrets.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
    name: ${secret_name}
    namespace: ${secret_namespace}
stringData:
  azure_subscription_id: ${subscription_id}
  azure_client_id: ${app_id}
  azure_client_secret: ${client_secret}
  azure_tenant_id: ${tenant_id}
  azure_resource_prefix: ${cluster_name}
  azure_resourcegroup: ${resource_group}
  azure_region: ${azure_region}
----
+
.. Create a `cco-configmap.yaml` file in the manifests directory with the Cloud Credential Operator (CCO) disabled:
+
.Sample `ConfigMap` object
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
name: cloud-credential-operator-config
namespace: openshift-cloud-credential-operator
  annotations:
    release.openshift.io/create-only: "true"
data:
  disabled: "true"
----

. To create the Ignition configuration files, run the following command from the directory that contains the installation program:
+
[source,terminal]
----
$ ./openshift-install create ignition-configs --dir <installation_directory>
----
+
where:
+
`<installation_directory>`:: Specifies the same installation directory.
+
Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory. The `kubeadmin-password` and `kubeconfig` files are created in the `./<installation_directory>/auth` directory:
+
----
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
----

. Export the metadata file's `infraID` key as an environment variable:
+
[source,terminal]
----
$ export INFRA_ID=$(jq -r .infraID metadata.json)
----
+
[TIP]
Extract the `infraID` key from `metadata.json` and use it as a prefix for all of the {rh-openstack} resources that you create. By doing so, you avoid name conflicts when making multiple deployments in the same project.

[role="_additional-resources"]
.Additional resources
* Manually creating long-term credentials

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc

[id="installation-extracting-infraid_{context}"]
= Extracting the infrastructure name

[role="_abstract"]
The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in {cp-first}. The infrastructure name is also used to locate the appropriate {cp} resources during an OpenShift Container Platform installation.
The provided {cp-template} templates contain references to this infrastructure name, so you must extract it.

The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in {cp-first}. The provided {cp-template-first} ({cp-template}) templates contain references to this infrastructure name, so you must extract it.

The Ignition config files contain a unique cluster identifier that you can use to
uniquely identify your cluster in {cp-first}. If you plan to use the cluster identifier as the name of your virtual machine folder, you must extract it.

[WARNING]
====
Do not run the `openshift-install create manifests` command again after creating any {gcp-short} resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any {gcp-short} resources you created and recreate them with the new cluster identifier.
====

.Prerequisites
* You obtained the OpenShift Container Platform installation program and the pull secret for your cluster.
* You generated the Ignition config files for your cluster.
* You installed the `jq` package.

.Procedure

* To extract and view the infrastructure name from the Ignition config file
metadata, run the following command:
+
[source,terminal]
----
$ jq -r .infraID <installation_directory>/metadata.json
----
+
For `<installation_directory>`, specify the path to the directory that you stored the installation files in.
+
.Example output
[source,terminal]
----
$ openshift-vw9j6
----
+
The output of this command is your cluster name and a random string.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-vpc_{context}"]
= Creating a VPC in AWS

You must create a Virtual Private Cloud (VPC) in Amazon Web Services (AWS) for your OpenShift Container Platform
cluster to use. You can customize the VPC to meet your requirements, including
VPN and route tables.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent the VPC.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS
infrastructure, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You added your AWS keys and region to your local AWS profile by running `aws configure`.

.Procedure

. Create a JSON file that contains the parameter values that the template
requires:
+
[source,json]
----
[
  {
    "ParameterKey": "VpcCidr", <1>
    "ParameterValue": "10.0.0.0/16" <2>
  },
  {
    "ParameterKey": "AvailabilityZoneCount", <3>
    "ParameterValue": "1" <4>
  },
  {
    "ParameterKey": "SubnetBits", <5>
    "ParameterValue": "12" <6>
  }
]
----
<1> The CIDR block for the VPC.
<2> Specify a CIDR block in the format `x.x.x.x/16-24`.
<3> The number of availability zones to deploy the VPC in.
<4> Specify an integer between `1` and `3`.
<5> The size of each subnet in each availability zone.
<6> Specify an integer between  `5` and `13`, where `5` is `/27` and `13` is `/19`.

. Copy the template from the *CloudFormation template for the VPC*
section of this topic and save it as a YAML file on your computer. This template
describes the VPC that your cluster requires.

. Launch the CloudFormation template to create a stack of AWS resources that represent the VPC:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-vpc`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-vpc/dbedae40-2fd3-11eb-820e-12a48460849f
----

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values
for the following parameters. You must provide these parameter values to
the other CloudFormation templates that you run to create your cluster:
[horizontal]
`VpcId`:: The ID of your VPC.
`PublicSubnetIds`:: The IDs of the new public subnets.
`PrivateSubnetIds`:: The IDs of the new private subnets.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-vpc_{context}"]
= CloudFormation template for the VPC

You can use the following CloudFormation template to deploy the VPC that
you need for your OpenShift Container Platform cluster.

.CloudFormation template for the VPC
[%collapsible]
====
[source,yaml]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-dns_{context}"]
= Creating networking and load balancing components in AWS

You must configure networking and classic or network load balancing in Amazon Web Services (AWS) that your OpenShift Container Platform cluster can use.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources. The stack represents the networking and load balancing components that your OpenShift Container Platform cluster requires. The template also creates a hosted zone and subnet tags.

You can run the template multiple times within a single Virtual Private Cloud (VPC).

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS
infrastructure, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You created and configured a VPC and associated subnets in AWS.

.Procedure

. Obtain the hosted zone ID for the Route 53 base domain that you specified in the
`install-config.yaml` file for your cluster. You can obtain details about your hosted zone by running the following command:
+
[source,terminal]
----
$ aws route53 list-hosted-zones-by-name --dns-name <route53_domain> <1>
----
<1> For the `<route53_domain>`, specify the Route 53 base domain that you used
when you generated the `install-config.yaml` file for the cluster.
+
.Example output
[source,terminal]
----
mycluster.example.com.	False	100
HOSTEDZONES	65F8F38E-2268-B835-E15C-AB55336FCBFA	/hostedzone/Z21IXYZABCZ2A4	mycluster.example.com.	10
----
+
In the example output, the hosted zone ID is `Z21IXYZABCZ2A4`.

. Create a JSON file that contains the parameter values that the template
requires:
+
[source,json]
----
[
  {
    "ParameterKey": "ClusterName", <1>
    "ParameterValue": "mycluster" <2>
  },
  {
    "ParameterKey": "InfrastructureName", <3>
    "ParameterValue": "mycluster-<random_string>" <4>
  },
  {
    "ParameterKey": "HostedZoneId", <5>
    "ParameterValue": "<random_string>" <6>
  },
  {
    "ParameterKey": "HostedZoneName", <7>
    "ParameterValue": "example.com" <8>
  },
  {
    "ParameterKey": "PublicSubnets", <9>
    "ParameterValue": "subnet-<random_string>" <10>
  },
  {
    "ParameterKey": "PrivateSubnets", <11>
    "ParameterValue": "subnet-<random_string>" <12>
  },
  {
    "ParameterKey": "VpcId", <13>
    "ParameterValue": "vpc-<random_string>" <14>
  }
]
----
<1> A short, representative cluster name to use for hostnames, etc.
<2> Specify the cluster name that you used when you generated the
`install-config.yaml` file for the cluster.
<3> The name for your cluster infrastructure that is encoded in your Ignition
config files for the cluster.
<4> Specify the infrastructure name that you extracted from the Ignition config
file metadata, which has the format `<cluster-name>-<random-string>`.
<5> The Route 53 public zone ID to register the targets with.
<6> Specify the Route 53 public zone ID, which as a format similar to
`Z21IXYZABCZ2A4`. You can obtain this value from the AWS console.
<7> The Route 53 zone to register the targets with.
<8> Specify the Route 53 base domain that you used when you generated the
`install-config.yaml` file for the cluster. Do not include the trailing period
(.) that is displayed in the AWS console.
<9> The public subnets that you created for your VPC.
<10> Specify the `PublicSubnetIds` value from the output of the CloudFormation
template for the VPC.
<11> The private subnets that you created for your VPC.
<12> Specify the `PrivateSubnetIds` value from the output of the CloudFormation
template for the VPC.
<13> The VPC that you created for the cluster.
<14> Specify the `VpcId` value from the output of the CloudFormation template
for the VPC.

. Copy the template from the *CloudFormation template for the network and load balancers*
section of this topic and save it as a YAML file on your computer. This template
describes the networking and load balancing objects that your cluster requires.
+
[IMPORTANT]
====
If you are deploying your cluster to an AWS government or secret region, you must update the `InternalApiServerRecord` in the CloudFormation template to use `CNAME` records. Records of type `ALIAS` are not supported for AWS government regions.
====

. Launch the CloudFormation template to create a stack of AWS resources that provide the networking and load balancing components:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
     --capabilities CAPABILITY_NAMED_IAM <4>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-dns`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
<4> You must explicitly declare the `CAPABILITY_NAMED_IAM` capability because the provided template creates some `AWS::IAM::Role` resources.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-dns/cd3e5de0-2fd4-11eb-5cf0-12be5c33a183
----

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values
for the following parameters. You must provide these parameter values to
the other CloudFormation templates that you run to create your cluster:
[horizontal]
`PrivateHostedZoneId`:: Hosted zone ID for the private DNS.
`ExternalApiLoadBalancerName`:: Full name of the external API load balancer.
`InternalApiLoadBalancerName`:: Full name of the internal API load balancer.
`ApiServerDnsName`:: Full hostname of the API server.
`RegisterNlbIpTargetsLambda`:: Lambda ARN useful to help register/deregister IP
targets for these load balancers.
`ExternalApiTargetGroupArn`:: ARN of external API target group.
`InternalApiTargetGroupArn`:: ARN of internal API target group.
`InternalServiceTargetGroupArn`:: ARN of internal service target group.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-dns_{context}"]
= CloudFormation template for the network and load balancers

You can use the following CloudFormation template to deploy the networking
objects and load balancers that you need for your OpenShift Container Platform cluster.

.CloudFormation template for the network and load balancers
[%collapsible]
====
[source,yaml]
----

----
====

[IMPORTANT]
====
If you are deploying your cluster to an AWS government or secret region, you must update the `InternalApiServerRecord` to use `CNAME` records. Records of type `ALIAS` are not supported for AWS government regions. For example:

[source,yaml]
----
Type: CNAME
TTL: 10
ResourceRecords:
- !GetAtt IntApiElb.DNSName
----
====

[role="_additional-resources"]
.Additional resources

* Listing public hosted zones({aws-short} documentation)

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-security_{context}"]
= Creating security group and roles in AWS

You must create security groups and roles in Amazon Web Services (AWS) for your OpenShift Container Platform cluster to use.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources. The stack represents the security groups and roles that your OpenShift Container Platform cluster requires.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS
infrastructure, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Procedure

. Create a JSON file that contains the parameter values that the template
requires:
+
[source,json]
----
[
  {
    "ParameterKey": "InfrastructureName", <1>
    "ParameterValue": "mycluster-<random_string>" <2>
  },
  {
    "ParameterKey": "VpcCidr", <3>
    "ParameterValue": "10.0.0.0/16" <4>
  },
  {
    "ParameterKey": "PrivateSubnets", <5>
    "ParameterValue": "subnet-<random_string>" <6>
  },
  {
    "ParameterKey": "VpcId", <7>
    "ParameterValue": "vpc-<random_string>" <8>
  }
]
----
<1> The name for your cluster infrastructure that is encoded in your Ignition
config files for the cluster.
<2> Specify the infrastructure name that you extracted from the Ignition config
file metadata, which has the format `<cluster-name>-<random-string>`.
<3> The CIDR block for the VPC.
<4> Specify the CIDR block parameter that you used for the VPC that you defined
in the form `x.x.x.x/16-24`.
<5> The private subnets that you created for your VPC.
<6> Specify the `PrivateSubnetIds` value from the output of the CloudFormation
template for the VPC.
<7> The VPC that you created for the cluster.
<8> Specify the `VpcId` value from the output of the CloudFormation template for
the VPC.

. Copy the template from the *CloudFormation template for security objects*
section of this topic and save it as a YAML file on your computer. This template
describes the security groups and roles that your cluster requires.

. Launch the CloudFormation template to create a stack of AWS resources that represent the security groups and roles:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
     --capabilities CAPABILITY_NAMED_IAM <4>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-sec`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
<4> You must explicitly declare the `CAPABILITY_NAMED_IAM` capability because the provided template creates some `AWS::IAM::Role` and `AWS::IAM::InstanceProfile` resources.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-sec/03bd4210-2ed7-11eb-6d7a-13fc0b61e9db
----

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values
for the following parameters. You must provide these parameter values to
the other CloudFormation templates that you run to create your cluster:
[horizontal]
`MasterSecurityGroupId`:: Master Security Group ID
`WorkerSecurityGroupId`:: Worker Security Group ID
`MasterInstanceProfile`:: Master IAM Instance Profile
`WorkerInstanceProfile`:: Worker IAM Instance Profile

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-security_{context}"]
= CloudFormation template for security objects

You can use the following CloudFormation template to deploy the security objects
that you need for your OpenShift Container Platform cluster.

.CloudFormation template for security objects
[%collapsible]
====
[source,yaml]
----

----
====

//TODO: Add the module include to the following assemblies
//TODO: Create related modules for OpenStack (QCOW2) and Bare Metal (ISO)

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-ami-stream-metadata_{context}"]
= Accessing {op-system} AMIs with stream metadata

In OpenShift Container Platform, _stream metadata_ provides standardized metadata about {op-system} in the JSON format and injects the metadata into the cluster. Stream metadata is a stable format that supports multiple architectures and is intended to be self-documenting for maintaining automation.

You can use the `coreos print-stream-json` sub-command of `openshift-install` to access information about the boot images in the stream metadata format. This command provides a method for printing stream metadata in a scriptable, machine-readable format.

For user-provisioned installations, the `openshift-install` binary contains references to the version of {op-system} boot images that are tested for use with OpenShift Container Platform, such as the AWS AMI.

.Procedure

To parse the stream metadata, use one of the following methods:

* From a Go program, use the official `stream-metadata-go` library at https://github.com/coreos/stream-metadata-go. You can also view example code in the library.

* From another programming language, such as Python or Ruby, use the JSON library of your preferred programming language.

* From a command-line utility that handles JSON data, such as `jq`:

** Print the current `x86_64`
or `aarch64`
AMI for an AWS region, such as `us-west-1`:
+
.For x86_64
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.aws.regions["us-west-1"].image'
----
+
.Example output
[source,terminal]
----
ami-0d3e625f84626bbda
----
+
.For aarch64
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq -r '.architectures.aarch64.images.aws.regions["us-west-1"].image'
----
+
.Example output
[source,terminal]
----
ami-0af1d3b7fa5be2131
----
+
The output of this command is the AWS AMI ID for your designated architecture and the `us-west-1` region. The AMI must belong to the same region as the cluster.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-user-infra-rhcos-ami_{context}"]
= {op-system} AMIs for the AWS infrastructure

[role="_abstract"]
Red{nbsp}Hat provides {op-system-first} AMIs that are valid for the various AWS regions and instance architectures that you can manually specify for your OpenShift Container Platform nodes. {op-system} AMIs are available based on RHEL 9 and RHEL 10.

[NOTE]
====
By importing your own AMI, you can also install to regions that do not have published {op-system} AMIs.
====

.x86_64 {op-system} AMIs

[cols="2a,2a,2a",options="header"]
|===

|AWS zone
|RHEL 9 AMI
|RHEL 10 AMI

|`af-south-1`
|`ami-0e09db1a117f89982`
|`ami-00b9419956a1b8301`

|`ap-east-1`
|`ami-0f3883046e2b590c4`
|`ami-093ce74a7831d5796`

|`ap-east-2`
|`ami-05fda30c28d357b97`
|`ami-0f1f5f78fad6126f3`

|`ap-northeast-1`
|`ami-0acebf7451fbed435`
|`ami-0b1305ab18da2b503`

|`ap-northeast-2`
|`ami-07e85fe3474ab6f53`
|`ami-089d5b21fb5472656`

|`ap-northeast-3`
|`ami-0bf06ecbd16316390`
|`ami-08b988fa11f0772c3`

|`ap-south-1`
|`ami-001b087fae6b102a2`
|`ami-030c986c15d7d21fe`

|`ap-south-2`
|`ami-02e59bb73395086de`
|`ami-0baf89a420726a0c9`

|`ap-southeast-1`
|`ami-07e0e4d66f0276e33`
|`ami-07db2a2569bf635d5`

|`ap-southeast-2`
|`ami-0656ee074d43ebeb9`
|`ami-0c66ca97b4cb72a96`

|`ap-southeast-3`
|`ami-0b8ac3107bf7b8091`
|`ami-0ea4633b5accce1cc`

|`ap-southeast-4`
|`ami-06a85e79ca82e97d3`
|`ami-0b9a19c6d404ebe82`

|`ap-southeast-5`
|`ami-068e811f466ce5eec`
|`ami-0860196faab6d36f5`

|`ap-southeast-6`
|`ami-01801dc800c336d1f`
|`ami-05391d944831d449c`

|`ap-southeast-7`
|`ami-01b449b1bf9c95caf`
|`ami-0ea7c99fe14478e31`

|`ca-central-1`
|`ami-016a214bc34aed24c`
|`ami-01a1c5433b11c6040`

|`ca-west-1`
|`ami-0279542db8d76fe7c`
|`ami-0aaec38c9c3c18973`

|`eu-central-1`
|`ami-02b4be39da643ac06`
|`ami-050a2036417aa85c9`

|`eu-central-2`
|`ami-09e9173753792f284`
|`ami-0dc1cab1a5a382089`

|`eu-north-1`
|`ami-0b4a484d5db49d4a5`
|`ami-0ebb900e33852ac20`

|`eu-south-1`
|`ami-02f2692568ca70d48`
|`ami-06794550da69b4d4f`

|`eu-south-2`
|`ami-0777de9170dd480a0`
|`ami-09b9b2363f8b9bf79`

|`eu-west-1`
|`ami-0754b5979bce4f62f`
|`ami-00277e2896ce030cd`

|`eu-west-2`
|`ami-05a2b3abb8cf0cc92`
|`ami-06c08d05f6a1085e5`

|`eu-west-3`
|`ami-01ba91ba1e67b52fa`
|`ami-0c94bd2324f9a7dc4`

|`il-central-1`
|`ami-0be1e841b9475abc2`
|`ami-090c5d273c266bcb1`

|`mx-central-1`
|`ami-04e5e190abb398aef`
|`ami-0127400b1a4f4d8a8`

|`sa-east-1`
|`ami-09b6c03d247ba3007`
|`ami-0d636038b33e48e74`

|`us-east-1`
|`ami-09a04cae40b5df1b1`
|`ami-06c799e44545e8040`

|`us-east-2`
|`ami-008f91aec6651d818`
|`ami-0b56c6461b8dfea32`

|`us-gov-east-1`
|`ami-083a079a4e93810d0`
|`ami-00a5a8f684bfe21a4`

|`us-gov-west-1`
|`ami-03c270b5f712d93c5`
|`ami-0ee3e9e7a587954c3`

|`us-west-1`
|`ami-000065c53330c76d2`
|`ami-0ceb35adb65ceb3ee`

|`us-west-2`
|`ami-0106a1d635d4a36c0`
|`ami-0a8a99e4004c7938d`

|===

.aarch64 {op-system} AMIs

[cols="2a,2a,2a",options="header"]
|===

|AWS zone
|RHEL 9 AMI
|RHEL 10 AMI

|`af-south-1`
|`ami-09b3b126662fe7a18`
|`ami-07c2492a6e610eb29`

|`ap-east-1`
|`ami-009fe8f4f06381d2e`
|`ami-0c081ca051d9066c3`

|`ap-east-2`
|`ami-0403657dcda8a5e9c`
|`ami-016834812d68d485e`

|`ap-northeast-1`
|`ami-0f9d02af671b8f84e`
|`ami-0a93317cde971c817`

|`ap-northeast-2`
|`ami-09fb79703d81dad43`
|`ami-008d018630379e1eb`

|`ap-northeast-3`
|`ami-038a507ec93b04ce1`
|`ami-016bf4359ca8f9ea2`

|`ap-south-1`
|`ami-0eb4f5b5dbaa33c62`
|`ami-01c3da87c9088e490`

|`ap-south-2`
|`ami-0d0f18aae857f459b`
|`ami-089e3dc824dfc53cc`

|`ap-southeast-1`
|`ami-0519530b4a949ac79`
|`ami-047501898db0e6004`

|`ap-southeast-2`
|`ami-029b0ef4d6d0872e6`
|`ami-00aa2f8c59143b0ae`

|`ap-southeast-3`
|`ami-0e04bab1932cc8079`
|`ami-001bd2512362e7b35`

|`ap-southeast-4`
|`ami-03b0fdc3fbc4a0fa4`
|`ami-0c3a562ba17fcc7fe`

|`ap-southeast-5`
|`ami-046fecd472297b7c4`
|`ami-0abc0ee6a009667b2`

|`ap-southeast-6`
|`ami-088024b57838dfd53`
|`ami-0c8b6c104987a0fc3`

|`ap-southeast-7`
|`ami-00c84a187abf62194`
|`ami-0fbf9de5c1828e872`

|`ca-central-1`
|`ami-0f65ba965f0cdf25b`
|`ami-06be00da14f45f988`

|`ca-west-1`
|`ami-0ce3bfdc385214b60`
|`ami-0260b4a668a59a922`

|`eu-central-1`
|`ami-077c9e69aa2a7442b`
|`ami-001fdc3025ce50006`

|`eu-central-2`
|`ami-0843ce8434ed947e0`
|`ami-0443b053f6e845524`

|`eu-north-1`
|`ami-047f81c57b0567e80`
|`ami-06bc091c0435adf6f`

|`eu-south-1`
|`ami-048742ddf9599b9a3`
|`ami-02ee91218bdc1bb3a`

|`eu-south-2`
|`ami-0385fbca30108a3a9`
|`ami-0b8943a7a26627b01`

|`eu-west-1`
|`ami-04631bbd6c1be5b55`
|`ami-064942d9b57521cf3`

|`eu-west-2`
|`ami-0915a41744ba40397`
|`ami-0e13b80ab624fc7d3`

|`eu-west-3`
|`ami-09fd8d0e79f45b71a`
|`ami-0b1bd601d3ecde37d`

|`il-central-1`
|`ami-0853f94ef8841751a`
|`ami-0073de64ca6a1189b`

|`mx-central-1`
|`ami-039d2c56cbe869df0`
|`ami-03bf73795d8dfac51`

|`sa-east-1`
|`ami-0915393860fee75df`
|`ami-0f8e239c3eb87df2b`

|`us-east-1`
|`ami-0e3af3b58f5710e43`
|`ami-04ec52f48c28d001d`

|`us-east-2`
|`ami-017020cb8aeeda203`
|`ami-0469df626c198243e`

|`us-gov-east-1`
|`ami-014a147dae2cf3359`
|`ami-03557a94deb16be46`

|`us-gov-west-1`
|`ami-07113f5ee8cde6fb3`
|`ami-06460c1920305cf08`

|`us-west-1`
|`ami-09ca10147735afd05`
|`ami-0cd45be3140b38916`

|`us-west-2`
|`ami-00e116f16409da3de`
|`ami-03206cc79683aa1a6`

|===

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-bootstrap_{context}"]
= Creating the bootstrap node in AWS

You must create the bootstrap node in Amazon Web Services (AWS) to use during OpenShift Container Platform cluster initialization. You do this by:

* Providing a location to serve the `bootstrap.ign` Ignition config file to your cluster. This file is located in your installation directory. The provided CloudFormation Template assumes that the Ignition config files for your cluster are served from an S3 bucket. If you choose to serve the files from another location, you must modify the templates.
* Using the provided CloudFormation template and a custom parameter file to create a stack of AWS resources. The stack represents the bootstrap node that your OpenShift Container Platform installation requires.

[NOTE]
====
If you do not use the provided CloudFormation template to create your bootstrap
node, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You created and configured DNS, load balancers, and listeners in AWS.
* You created the security groups and roles required for your cluster in AWS.

.Procedure

. Create the bucket by running the following command:
+
[source,terminal]
----
$ aws s3 mb s3://<cluster-name>-infra <1>
----
<1> `<cluster-name>-infra` is the bucket name. When creating the `install-config.yaml` file, replace `<cluster-name>` with the name specified for the cluster.
+
You must use a presigned URL for your S3 bucket, instead of the `s3://` schema, if you are:
** Deploying to a region that has endpoints that differ from the AWS SDK.
** Deploying a proxy.
** Providing your own custom endpoints.

. Upload the `bootstrap.ign` Ignition config file to the bucket by running the following command:
+
[source,terminal]
----
$ aws s3 cp <installation_directory>/bootstrap.ign s3://<cluster-name>-infra/bootstrap.ign <1>
----
<1> For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

. Verify that the file uploaded by running the following command:
+
[source,terminal]
----
$ aws s3 ls s3://<cluster-name>-infra/
----
+
.Example output
[source,terminal]
----
2019-04-03 16:15:16     314878 bootstrap.ign
----
+
[NOTE]
====
The bootstrap Ignition config file does contain secrets, like X.509 keys. The following steps provide basic security for the S3 bucket. To provide additional security, you can enable an S3 bucket policy to allow only certain users, such as the OpenShift IAM user, to access objects that the bucket contains. You can avoid S3 entirely and serve your bootstrap Ignition config file from any address that the bootstrap machine can reach.
====

. Create a JSON file that contains the parameter values that the template requires:
+
[source,json]
----
[
  {
    "ParameterKey": "InfrastructureName", <1>
    "ParameterValue": "mycluster-<random_string>" <2>
  },
  {
    "ParameterKey": "RhcosAmi", <3>
    "ParameterValue": "ami-<random_string>" <4>
  },
  {
    "ParameterKey": "AllowedBootstrapSshCidr", <5>
    "ParameterValue": "0.0.0.0/0" <6>
  },
  {
    "ParameterKey": "PublicSubnet", <7>
    "ParameterValue": "subnet-<random_string>" <8>
  },
  {
    "ParameterKey": "MasterSecurityGroupId", <9>
    "ParameterValue": "sg-<random_string>" <10>
  },
  {
    "ParameterKey": "VpcId", <11>
    "ParameterValue": "vpc-<random_string>" <12>
  },
  {
    "ParameterKey": "BootstrapIgnitionLocation", <13>
    "ParameterValue": "s3://<bucket_name>/bootstrap.ign" <14>
  },
  {
    "ParameterKey": "AutoRegisterELB", <15>
    "ParameterValue": "yes" <16>
  },
  {
    "ParameterKey": "RegisterNlbIpTargetsLambdaArn", <17>
    "ParameterValue": "arn:aws:lambda:<aws_region>:<account_number>:function:<dns_stack_name>-RegisterNlbIpTargets-<random_string>" <18>
  },
  {
    "ParameterKey": "ExternalApiTargetGroupArn", <19>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Exter-<random_string>" <20>
  },
  {
    "ParameterKey": "InternalApiTargetGroupArn", <21>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>" <22>
  },
  {
    "ParameterKey": "InternalServiceTargetGroupArn", <23>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>" <24>
  }
]

----
<1> The name for your cluster infrastructure that is encoded in your Ignition
config files for the cluster.
<2> Specify the infrastructure name that you extracted from the Ignition config
file metadata, which has the format `<cluster-name>-<random-string>`.
<3> Current {op-system-first} AMI to use for the bootstrap node based on your selected architecture.
<4> Specify a valid `AWS::EC2::Image::Id` value.
<5> CIDR block to allow SSH access to the bootstrap node.
<6> Specify a CIDR block in the format `x.x.x.x/16-24`.
<7> The public subnet that is associated with your VPC to launch the bootstrap
node into.
<8> Specify the `PublicSubnetIds` value from the output of the CloudFormation
template for the VPC.
<9> The master security group ID (for registering temporary rules)
<10> Specify the `MasterSecurityGroupId` value from the output of the
CloudFormation template for the security group and roles.
<11> The VPC created resources will belong to.
<12> Specify the `VpcId` value from the output of the CloudFormation template
for the VPC.
<13> Location to fetch bootstrap Ignition config file from.
<14> Specify the S3 bucket and file name in the form
`s3://<bucket_name>/bootstrap.ign`.
<15> Whether or not to register a network load balancer (NLB).
<16> Specify `yes` or `no`. If you specify `yes`, you must provide a Lambda
Amazon Resource Name (ARN) value.
<17> The ARN for NLB IP target registration lambda group.
<18> Specify the `RegisterNlbIpTargetsLambda` value from the output of the
CloudFormation template for DNS and load balancing. Use `arn:aws-us-gov` if
deploying the cluster to an AWS GovCloud region.
<19> The ARN for external API load balancer target group.
<20> Specify the `ExternalApiTargetGroupArn` value from the output of the
CloudFormation template for DNS and load balancing. Use `arn:aws-us-gov` if
deploying the cluster to an AWS GovCloud region.
<21> The ARN for internal API load balancer target group.
<22> Specify the `InternalApiTargetGroupArn` value from the output of the
CloudFormation template for DNS and load balancing. Use `arn:aws-us-gov` if
deploying the cluster to an AWS GovCloud region.
<23> The ARN for internal service load balancer target group.
<24> Specify the `InternalServiceTargetGroupArn` value from the output of the
CloudFormation template for DNS and load balancing. Use `arn:aws-us-gov` if
deploying the cluster to an AWS GovCloud region.

. Copy the template from the *CloudFormation template for the bootstrap machine*
section of this topic and save it as a YAML file on your computer. This template
describes the bootstrap machine that your cluster requires.

. Optional: If you are deploying the cluster with a proxy, you must update the ignition in the template to add the  `ignition.config.proxy` fields. Additionally, If you have added the Amazon EC2, Elastic Load Balancing, and S3 VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.

. Launch the CloudFormation template to create a stack of AWS resources that represent the bootstrap node:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
     --capabilities CAPABILITY_NAMED_IAM <4>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-bootstrap`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
<4> You must explicitly declare the `CAPABILITY_NAMED_IAM` capability because the provided template creates some `AWS::IAM::Role` and `AWS::IAM::InstanceProfile` resources.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-bootstrap/12944486-2add-11eb-9dee-12dace8e3a83
----

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values
for the following parameters. You must provide these parameter values to
the other CloudFormation templates that you run to create your cluster:
[horizontal]
`BootstrapInstanceId`:: The bootstrap Instance ID.
`BootstrapPublicIp`:: The bootstrap node public IP address.
`BootstrapPrivateIp`:: The bootstrap node private IP address.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-bootstrap_{context}"]
= CloudFormation template for the bootstrap machine

You can use the following CloudFormation template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster.

.CloudFormation template for the bootstrap machine
[%collapsible]
====
[source,yaml]
----

----
====

[role="_additional-resources"]
.Additional resources

* {op-system} AMIs for the AWS infrastructure({aws-short} documentation)

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-control-plane_{context}"]
= Creating the control plane machines in AWS

You must create the control plane machines in Amazon Web Services (AWS) that your cluster will use.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent the control plane nodes.

[IMPORTANT]
====
The CloudFormation template creates a stack that represents three control plane nodes.
====

[NOTE]
====
If you do not use the provided CloudFormation template to create your control plane
nodes, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You created the bootstrap machine.

.Procedure

. Create a JSON file that contains the parameter values that the template
requires:
+
[source,json]
----
[
  {
    "ParameterKey": "InfrastructureName", <1>
    "ParameterValue": "mycluster-<random_string>" <2>
  },
  {
    "ParameterKey": "RhcosAmi", <3>
    "ParameterValue": "ami-<random_string>" <4>
  },
  {
    "ParameterKey": "AutoRegisterDNS", <5>
    "ParameterValue": "yes" <6>
  },
  {
    "ParameterKey": "PrivateHostedZoneId", <7>
    "ParameterValue": "<random_string>" <8>
  },
  {
    "ParameterKey": "PrivateHostedZoneName", <9>
    "ParameterValue": "mycluster.example.com" <10>
  },
  {
    "ParameterKey": "Master0Subnet", <11>
    "ParameterValue": "subnet-<random_string>" <12>
  },
  {
    "ParameterKey": "Master1Subnet", <11>
    "ParameterValue": "subnet-<random_string>" <12>
  },
  {
    "ParameterKey": "Master2Subnet", <11>
    "ParameterValue": "subnet-<random_string>" <12>
  },
  {
    "ParameterKey": "MasterSecurityGroupId", <13>
    "ParameterValue": "sg-<random_string>" <14>
  },
  {
    "ParameterKey": "IgnitionLocation", <15>
    "ParameterValue": "https://api-int.<cluster_name>.<domain_name>:22623/config/master" <16>
  },
  {
    "ParameterKey": "CertificateAuthorities", <17>
    "ParameterValue": "data:text/plain;charset=utf-8;base64,ABC...xYz==" <18>
  },
  {
    "ParameterKey": "MasterInstanceProfileName", <19>
    "ParameterValue": "<roles_stack>-MasterInstanceProfile-<random_string>" <20>
  },
  {
    "ParameterKey": "MasterInstanceType", <21>
    "ParameterValue": "" <22>
  },
  {
    "ParameterKey": "AutoRegisterELB", <23>
    "ParameterValue": "yes" <24>
  },
  {
    "ParameterKey": "RegisterNlbIpTargetsLambdaArn", <25>
    "ParameterValue": "arn:aws:lambda:<aws_region>:<account_number>:function:<dns_stack_name>-RegisterNlbIpTargets-<random_string>" <26>
  },
  {
    "ParameterKey": "ExternalApiTargetGroupArn", <27>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Exter-<random_string>" <28>
  },
  {
    "ParameterKey": "InternalApiTargetGroupArn", <29>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>" <30>
  },
  {
    "ParameterKey": "InternalServiceTargetGroupArn", <31>
    "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>" <32>
  }
]
----
<1> The name for your cluster infrastructure that is encoded in your Ignition
config files for the cluster.
<2> Specify the infrastructure name that you extracted from the Ignition config
file metadata, which has the format `<cluster-name>-<random-string>`.
<3> Current {op-system-first} AMI to use for the control plane machines based on your selected architecture.
<4> Specify an `AWS::EC2::Image::Id` value.
<5> Whether or not to perform DNS etcd registration.
<6> Specify `yes` or `no`. If you specify `yes`, you must provide hosted zone
information.
<7> The Route 53 private zone ID to register the etcd targets with.
<8> Specify the `PrivateHostedZoneId` value from the output of the
CloudFormation template for DNS and load balancing.
<9> The Route 53 zone to register the targets with.
<10> Specify `<cluster_name>.<domain_name>` where `<domain_name>` is the Route 53
base domain that you used when you generated `install-config.yaml` file for the
cluster. Do not include the trailing period (.) that is
displayed in the AWS console.
<11> A subnet, preferably private, to launch the control plane machines on.
<12> Specify a subnet from the `PrivateSubnets` value from the output of the
CloudFormation template for DNS and load balancing.
<13> The master security group ID to associate with control plane nodes.
<14> Specify the `MasterSecurityGroupId` value from the output of the
CloudFormation template for the security group and roles.
<15> The location to fetch control plane Ignition config file from.
<16> Specify the generated Ignition config file location,
`https://api-int.<cluster_name>.<domain_name>:22623/config/master`.
<17> The base64 encoded certificate authority string to use.
<18> Specify the value from the `master.ign` file that is in the installation
directory. This value is the long string with the format
`data:text/plain;charset=utf-8;base64,ABC...xYz==`.
<19> The IAM profile to associate with control plane nodes.
<20> Specify the `MasterInstanceProfile` parameter value from the output of
the CloudFormation template for the security group and roles.
<21> The type of AWS instance to use for the control plane machines based on your selected architecture.
<22> The instance type value corresponds to the minimum resource requirements for
control plane machines. For example `m6i.xlarge` is a type for AMD64
and `m6g.xlarge` is a type for ARM64.
<23> Whether or not to register a network load balancer (NLB).
<24> Specify `yes` or `no`. If you specify `yes`, you must provide a Lambda
Amazon Resource Name (ARN) value.
<25> The ARN for NLB IP target registration lambda group.
<26> Specify the `RegisterNlbIpTargetsLambda` value from the output of the CloudFormation template for DNS
and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS
GovCloud region.
<27> The ARN for external API load balancer target group.
<28> Specify the `ExternalApiTargetGroupArn` value from the output of the CloudFormation template for DNS
and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS
GovCloud region.
<29> The ARN for internal API load balancer target group.
<30> Specify the `InternalApiTargetGroupArn` value from the output of the CloudFormation template for DNS
and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS
GovCloud region.
<31> The ARN for internal service load balancer target group.
<32> Specify the `InternalServiceTargetGroupArn` value from the output of the CloudFormation template for DNS
and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS
GovCloud region.

. Copy the template from the *CloudFormation template for control plane machines*
section of this topic and save it as a YAML file on your computer. This template
describes the control plane machines that your cluster requires.

. If you specified an `m5` instance type as the value for `MasterInstanceType`,
add that instance type to the `MasterInstanceType.AllowedValues` parameter
in the CloudFormation template.

. Launch the CloudFormation template to create a stack of AWS resources that represent the control plane nodes:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml <2>
     --parameters file://<parameters>.json <3>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-control-plane`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-control-plane/21c7e2b0-2ee2-11eb-c6f6-0aa34627df4b
----
+
[NOTE]
====
The CloudFormation template creates a stack that represents three control plane nodes.
====

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-control-plane_{context}"]
= CloudFormation template for control plane machines

You can use the following CloudFormation template to deploy the control plane
machines that you need for your OpenShift Container Platform cluster.

.CloudFormation template for control plane machines
[%collapsible]
====
[source,yaml]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-creating-aws-worker_{context}"]
= Creating the worker nodes in AWS

If you do not plan to automatically create worker nodes by using a MachineSet,

You can create worker nodes in Amazon Web Services (AWS) for your cluster to use.

[NOTE]
====
If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.
====

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent a worker node.

[IMPORTANT]
====
The CloudFormation template creates a stack that represents one worker node.
You must create a stack for each worker node.
====

[NOTE]
====
If you do not use the provided CloudFormation template to create your worker
nodes, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You created the control plane machines.

.Procedure

. Create a JSON file that contains the parameter values that the CloudFormation
template requires:
+
[source,json]
----
[
  {
    "ParameterKey": "InfrastructureName", <1>
    "ParameterValue": "mycluster-<random_string>" <2>
  },
  {
    "ParameterKey": "RhcosAmi", <3>
    "ParameterValue": "ami-<random_string>" <4>
  },
  {
    "ParameterKey": "Subnet", <5>
    "ParameterValue": "subnet-<random_string>" <6>
  },
  {
    "ParameterKey": "WorkerSecurityGroupId", <7>
    "ParameterValue": "sg-<random_string>" <8>
  },
  {
    "ParameterKey": "IgnitionLocation", <9>
    "ParameterValue": "https://api-int.<cluster_name>.<domain_name>:22623/config/worker" <10>
  },
  {
    "ParameterKey": "CertificateAuthorities", <11>
    "ParameterValue": "data:text/plain;charset=utf-8;base64,ABC...xYz==" <12>
  },
  {
    "ParameterKey": "WorkerInstanceProfileName", <13>
    "ParameterValue": "<roles_stack>-WorkerInstanceProfile-<random_string>" <14>
  },
  {
    "ParameterKey": "WorkerInstanceType", <15>
    "ParameterValue": "" <16>
  }
]
----
<1> The name for your cluster infrastructure that is encoded in your Ignition
config files for the cluster.
<2> Specify the infrastructure name that you extracted from the Ignition config
file metadata, which has the format `<cluster-name>-<random-string>`.
<3> Current {op-system-first} AMI to use for the worker nodes based on your selected architecture.
<4> Specify an `AWS::EC2::Image::Id` value.
<5> A subnet, preferably private, to start the worker nodes on.
<6> Specify a subnet from the `PrivateSubnets` value from the output of the
CloudFormation template for DNS and load balancing.
<7> The worker security group ID to associate with worker nodes.
<8> Specify the `WorkerSecurityGroupId` value from the output of the
CloudFormation template for the security group and roles.
<9> The location to fetch the bootstrap Ignition config file from.
<10> Specify the generated Ignition config location,
`https://api-int.<cluster_name>.<domain_name>:22623/config/worker`.
<11> Base64 encoded certificate authority string to use.
<12> Specify the value from the `worker.ign` file that is in the installation
directory. This value is the long string with the format
`data:text/plain;charset=utf-8;base64,ABC...xYz==`.
<13> The IAM profile to associate with worker nodes.
<14> Specify the `WorkerInstanceProfile` parameter value from the output of
the CloudFormation template for the security group and roles.
<15> The type of AWS instance to use for the compute machines based on your selected architecture.
<16> The instance type value corresponds to the minimum resource requirements
for compute machines. For example `m6i.large` is a type for AMD64
 and `m6g.large` is a type for ARM64.
. Copy the template from the *CloudFormation template for worker machines*
section of this topic and save it as a YAML file on your computer. This template
describes the networking objects and load balancers that your cluster requires.

. Optional: If you specified an `m5` instance type as the value for `WorkerInstanceType`, add that instance type to the `WorkerInstanceType.AllowedValues` parameter in the CloudFormation template.

. Optional: If you are deploying with an AWS Marketplace image, update the `Worker0.type.properties.ImageID` parameter with the AMI ID that you obtained from your subscription.

. Use the CloudFormation template to create a stack of AWS resources that represent a worker node:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> <1>
     --template-body file://<template>.yaml \ <2>
     --parameters file://<parameters>.json <3>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-worker-1`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path to and name of the CloudFormation
parameters JSON file.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-worker-1/729ee301-1c2a-11eb-348f-sd9888c65b59
----
+
[NOTE]
====
The CloudFormation template creates a stack that represents one worker node.
====

. Confirm that the template components exist:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----

. Continue to create worker stacks until you have created enough worker machines for your cluster. You can create additional worker stacks by referencing the same template and parameter files and specifying a different stack name.
+
[IMPORTANT]
====
You must create at least two worker machines, so you must create at least
two stacks that use this CloudFormation template.
====

[id="installing-workers-aws-user-infra"]
== Creating worker nodes

You can either manually create worker nodes or use a MachineSet to create worker nodes after the cluster deploys. If you use a MachineSet to create and maintain the workers, you can allow the cluster to manage them. This allows you to easily scale, manage, and upgrade your workers.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-cloudformation-worker_{context}"]
= CloudFormation template for compute machines

You can deploy the compute machines that you need for your OpenShift Container Platform cluster by using the following CloudFormation template.

.CloudFormation template for compute machines
[%collapsible]
====
[source,yaml]
----

----
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-creating-cloudformation-stack_{context}"]
= Creating the CloudFormation stack for compute machines

You can create a stack of {aws-short} resources for the compute machines by using the CloudFormation template that was previously shared.

[IMPORTANT]
====
When you use the CloudFormation template for the control plane machines, the template provisions all three control plane machines with a single stack; however, when you use the CloudFormation template to deploy the compute machines, you must create the number of stacks based on the number that you defined in the `install-config.yaml` file. Each stack is provisioned once for each machine. To provision a new compute machine, you must change the stack name.
====

.Procedure
* To create the CloudFormation stack for compute machines, run the following command:
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> \// <1>
     --template-body file://<template>.yaml \// <2>
     --parameters file://<parameters>.json <3>
----
<1> Specify the `<name>` with the name for the CloudFormation stack, such as `cluster-worker-1`. You need the name of this stack if you remove the cluster.
<2> Specify the relative path and the name of the CloudFormation template YAML file that you saved.
<3> Specify the relative path and the name of the JSON file for the CloudFormation parameters.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-worker-1/729ee301-1c2a-11eb-348f-sd9888c65b59
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-user-infra-bootstrap_{context}"]
= Initializing the bootstrap sequence on AWS with user-provisioned infrastructure

After you create all of the required infrastructure in Amazon Web Services (AWS),
you can start the bootstrap sequence that initializes the OpenShift Container Platform control plane.

.Prerequisites

* You created the worker nodes.

.Procedure

. Change to the directory that contains the installation program and start the bootstrap process that initializes the OpenShift Container Platform control plane:
+
[source,terminal]
----
$ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \ <1>
    --log-level=info <2>
----
<1> For `<installation_directory>`, specify the path to the directory that you
stored the installation files in.
<2> To view different installation details, specify `warn`, `debug`, or
`error` instead of `info`.
+
.Example output
[source,terminal]
----
INFO Waiting up to 20m0s for the Kubernetes API at https://api.mycluster.example.com:6443...
INFO API v1.35.4 up
INFO Waiting up to 30m0s for bootstrapping to complete...
INFO It is now safe to remove the bootstrap resources
INFO Time elapsed: 1s
----
+
If the command exits without a `FATAL` warning, your OpenShift Container Platform control plane
has initialized.
+
[NOTE]
====
After the control plane initializes, it sets up the compute nodes and installs additional services in the form of Operators.
====

[role="_additional-resources"]
.Additional resources

* See Monitoring installation progress for details about monitoring the installation, bootstrap, and control plane logs as an OpenShift Container Platform installation progresses.

* See Gathering bootstrap node diagnostic data for information about troubleshooting issues related to the bootstrap process.

//You can install the CLI on the mirror host.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-restricted-networks.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/adding-rhel-compute.adoc
// * machine_management/more-rhel-compute.adoc
// * machine_management/user_provisioned/adding-aws-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-bare-metal-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-vsphere-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="installation-approve-csrs_{context}"]
= Approving the certificate signing requests for your machines

[role="_abstract"]
When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

.Prerequisites

* You added machines to your cluster.

.Procedure

. Confirm that the cluster recognizes the machines:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.35.4
master-1  Ready     master  63m  v1.35.4
master-2  Ready     master  64m  v1.35.4
----
+
The output lists all of the machines that you created.
+
[NOTE]
====
The preceding output might not include the compute nodes, also known as worker nodes, until some CSRs are approved.
====

. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
...
----
+
In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
[source,terminal]
----
$ oc get csr
----
+
[source,terminal]
.Example output
----
NAME        AGE   REQUESTOR                                   CONDITION
csr-mddf5   20m   system:node:master-01.example.com   Approved,Issued
csr-z5rln   16m   system:node:worker-21.example.com   Approved,Issued
----

. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:
+
[NOTE]
====
You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. Then, subsequent serving certificate renewal requests are automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.
====
+
[NOTE]
====
For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.
====
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
----
+
[NOTE]
====
Some Operators might not become available until some CSRs are approved.
Each node submits two CSRs, so you may need to run the command to approve CSRs multiple times.
====

. Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
...
----

. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
----

. After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  73m  v1.35.4
master-1  Ready     master  73m  v1.35.4
master-2  Ready     master  74m  v1.35.4
worker-0  Ready     worker  11m  v1.35.4
worker-1  Ready     worker  11m  v1.35.4
----
.Example output
[source,terminal]
----
NAME               STATUS   ROLES                  AGE   VERSION   INTERNAL-IP      EXTERNAL-IP   OS-IMAGE                                                       KERNEL-VERSION                  CONTAINER-RUNTIME
worker-0-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.21   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.20   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-0-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.38      10.248.0.38   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-1-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.39      10.248.0.39   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-2-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.40      10.248.0.40   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-0-x86       Ready    worker                 75d   v1.35.4   10.248.0.43      10.248.0.43   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-x86       Ready    worker                 75d   v1.35.4   10.248.0.44      10.248.0.44   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
----
+
[NOTE]
====
It can take a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-operators-config_{context}"]
= Initial Operator configuration

[role="_abstract"]
After the control plane initializes, you must immediately configure some Operators so that they all become available.

.Prerequisites

* Your control plane has initialized.

.Procedure

. Watch the cluster components come online:
+
[source,terminal]
----
$ watch -n5 oc get clusteroperators
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             .0    True        False         False      19m
baremetal                                  .0    True        False         False      37m
cloud-credential                           .0    True        False         False      40m
cluster-autoscaler                         .0    True        False         False      37m
config-operator                            .0    True        False         False      38m
console                                    .0    True        False         False      26m
csi-snapshot-controller                    .0    True        False         False      37m
dns                                        .0    True        False         False      37m
etcd                                       .0    True        False         False      36m
image-registry                             .0    True        False         False      31m
ingress                                    .0    True        False         False      30m
insights                                   .0    True        False         False      31m
kube-apiserver                             .0    True        False         False      26m
kube-controller-manager                    .0    True        False         False      36m
kube-scheduler                             .0    True        False         False      36m
kube-storage-version-migrator              .0    True        False         False      37m
machine-api                                .0    True        False         False      29m
machine-approver                           .0    True        False         False      37m
machine-config                             .0    True        False         False      36m
marketplace                                .0    True        False         False      37m
monitoring                                 .0    True        False         False      29m
network                                    .0    True        False         False      38m
node-tuning                                .0    True        False         False      37m
openshift-apiserver                        .0    True        False         False      32m
openshift-controller-manager               .0    True        False         False      30m
openshift-samples                          .0    True        False         False      32m
operator-lifecycle-manager                 .0    True        False         False      37m
operator-lifecycle-manager-catalog         .0    True        False         False      37m
operator-lifecycle-manager-packageserver   .0    True        False         False      32m
service-ca                                 .0    True        False         False      38m
storage                                    .0    True        False         False      37m
----

. Configure the Operators that are not available.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * operators/admin/olm-restricted-networks.adoc
// * operators/admin/olm-managing-custom-catalogs.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="olm-restricted-networks-operatorhub_{context}"]
= Disabling the default software catalog sources

Operator catalogs that source content provided by Red Hat and community projects are configured for the software catalog by default during an OpenShift Container Platform installation.
In a restricted network environment, you must disable the default catalogs as a cluster administrator.
You can then configure the OperatorHub custom resource definition (CRD) to use local catalog sources for the software catalog.
As a cluster administrator, you can disable the set of default catalogs.

.Procedure

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:
+
[source,terminal]
----
$ oc patch OperatorHub cluster --type json \
    -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
----

[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page, click the *Sources* tab, where you can create, update, delete, disable, and enable individual sources.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-config_{context}"]
= Image registry storage configuration

[role="_abstract"]
Amazon Web Services provides default storage, which means the Image Registry Operator is available after installation. However, if the Registry Operator cannot create an S3 bucket and automatically configure storage, you must manually configure registry storage.
[role="_abstract"]
The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * registry/configuring_registry_storage-aws-user-infrastructure.adoc

[id="registry-configuring-storage-aws-user-infra_{context}"]
= Configuring registry storage for AWS with user-provisioned infrastructure

[role="_abstract"]
During installation, your cloud credentials are sufficient to create an Amazon S3 bucket and the Registry Operator will automatically configure storage.

If the Registry Operator cannot create an S3 bucket and automatically configure storage, you can create an S3 bucket and configure storage with the following procedure.

[WARNING]
====
To secure your registry images in AWS, block public access
to the S3 bucket.
====

.Prerequisites

* You have a cluster on AWS with user-provisioned infrastructure.
* For Amazon S3 storage, the secret is expected to contain two keys:
** `REGISTRY_STORAGE_S3_ACCESSKEY`
** `REGISTRY_STORAGE_S3_SECRETKEY`

.Procedure

. Set up a Bucket Lifecycle Policy
to abort incomplete multipart uploads that are one day old.

. Fill in the storage configuration in
`configs.imageregistry.operator.openshift.io/cluster`:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----
+
.Example configuration
[source,yaml]
----
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  storage:
    s3:
      bucket: <bucket_name>
      region: <region_name>
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-registry-storage-non-production_{context}"]
= Configuring storage for the image registry in non-production clusters

[role="_abstract"]
You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory. If you do so, all images are lost if you restart the registry.

.Procedure

* To set the image registry storage to an empty directory:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
----
+
[WARNING]
====
Configure this option only for non-production clusters.
====
+
If you run this command before the Image Registry Operator initializes its
components, the `oc patch` command fails with the following error:
+
[source,terminal]
----
Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
----
+
Wait a few minutes and run the command again.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-user-infra-delete-bootstrap_{context}"]
= Deleting the bootstrap resources

After you complete the initial Operator configuration for the cluster, remove the bootstrap resources from Amazon Web Services (AWS).

.Prerequisites

* You completed the initial Operator configuration for your cluster.

.Procedure

. Delete the bootstrap resources. If you used the CloudFormation template,
delete its stack:
** Delete the stack by using the AWS CLI:
+
[source,terminal]
----
$ aws cloudformation delete-stack --stack-name <name> <1>
----
<1> `<name>` is the name of your bootstrap stack.
** Delete the stack by using the AWS CloudFormation console.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-create-ingress-dns-records_{context}"]
= Creating the Ingress DNS Records

If you removed the DNS Zone configuration, manually create DNS records that point to the Ingress load balancer.
You can create either a wildcard record or specific records. While the following procedure uses A records, you can use other record types that you require, such as CNAME or alias.

.Prerequisites

* You deployed an OpenShift Container Platform cluster on Amazon Web Services (AWS) that uses infrastructure that you provisioned.
* You installed the OpenShift CLI (`oc`).
* You installed the `jq` package.
* You downloaded the AWS CLI and installed it on your computer. See
Install the AWS CLI Using the Bundled Installer (Linux, macOS, or Unix).

.Procedure

. Determine the routes to create.
** To create a wildcard record, use `*.apps.<cluster_name>.<domain_name>`, where `<cluster_name>` is your cluster name, and `<domain_name>` is the Route 53 base domain for your OpenShift Container Platform cluster.
** To create specific records, you must create a record for each route that your cluster uses, as shown in the output of the following command:
+
[source,terminal]
----
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
----
+
.Example output
[source,terminal]
----
oauth-openshift.apps.<cluster_name>.<domain_name>
console-openshift-console.apps.<cluster_name>.<domain_name>
downloads-openshift-console.apps.<cluster_name>.<domain_name>
alertmanager-main-openshift-monitoring.apps.<cluster_name>.<domain_name>
prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<domain_name>
----

. Retrieve the Ingress Operator load balancer status and note the value of the external IP address that it uses, which is shown in the `EXTERNAL-IP` column:
+
[source,terminal]
----
$ oc -n openshift-ingress get service router-default
----
+
.Example output
[source,terminal]
----
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP                            PORT(S)                      AGE
router-default   LoadBalancer   172.30.62.215   ab3...28.us-east-2.elb.amazonaws.com   80:31499/TCP,443:30693/TCP   5m
----

. Locate the hosted zone ID for the load balancer:
+
[source,terminal]
----
$ aws elb describe-load-balancers | jq -r '.LoadBalancerDescriptions[] | select(.DNSName == "<external_ip>").CanonicalHostedZoneNameID' <1>
----
<1> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer that you obtained.
+
.Example output
[source,terminal]
----
Z3AADJGX6KTTL2
----

+
The output of this command is the load balancer hosted zone ID.

. Obtain the public hosted zone ID for your cluster's domain:
+
[source,terminal]
----
$ aws route53 list-hosted-zones-by-name \
            --dns-name "<domain_name>" \ <1>
            --query 'HostedZones[? Config.PrivateZone != `true` && Name == `<domain_name>.`].Id' <1>
            --output text
----
<1> For `<domain_name>`, specify the Route 53 base domain for your OpenShift Container Platform cluster.
+
.Example output
[source,terminal]
----
/hostedzone/Z3URY6TWQ91KVV
----
+
The public hosted zone ID for your domain is shown in the command output. In this example, it is `Z3URY6TWQ91KVV`.

. Add the alias records to your private zone:
+
[source,terminal]
----
$ aws route53 change-resource-record-sets --hosted-zone-id "<private_hosted_zone_id>" --change-batch '{ <1>
>   "Changes": [
>     {
>       "Action": "CREATE",
>       "ResourceRecordSet": {
>         "Name": "\\052.apps.<cluster_domain>", <2>
>         "Type": "A",
>         "AliasTarget":{
>           "HostedZoneId": "<hosted_zone_id>", <3>
>           "DNSName": "<external_ip>.", <4>
>           "EvaluateTargetHealth": false
>         }
>       }
>     }
>   ]
> }'
----
<1> For `<private_hosted_zone_id>`, specify the value from the output of the CloudFormation template for DNS and load balancing.
<2> For `<cluster_domain>`, specify the domain or subdomain that you use with your OpenShift Container Platform cluster.
<3> For `<hosted_zone_id>`, specify the public hosted zone ID for the load balancer that you obtained.
<4> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.

. Add the records to your public zone:
+
[source,terminal]
----
$ aws route53 change-resource-record-sets --hosted-zone-id "<public_hosted_zone_id>"" --change-batch '{ <1>
>   "Changes": [
>     {
>       "Action": "CREATE",
>       "ResourceRecordSet": {
>         "Name": "\\052.apps.<cluster_domain>", <2>
>         "Type": "A",
>         "AliasTarget":{
>           "HostedZoneId": "<hosted_zone_id>", <3>
>           "DNSName": "<external_ip>.", <4>
>           "EvaluateTargetHealth": false
>         }
>       }
>     }
>   ]
> }'
----
<1> For `<public_hosted_zone_id>`, specify the public hosted zone for your domain.
<2> For `<cluster_domain>`, specify the domain or subdomain that you use with your OpenShift Container Platform cluster.
<3> For `<hosted_zone_id>`, specify the public hosted zone ID for the load balancer that you obtained.
<4> For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-user-infra-installation_{context}"]
= Completing an AWS installation on user-provisioned infrastructure

After you start the OpenShift Container Platform installation on Amazon Web Service (AWS)
user-provisioned infrastructure, monitor the deployment to completion.

.Prerequisites

* You removed the bootstrap node for an OpenShift Container Platform cluster on user-provisioned AWS infrastructure.
* You installed the `oc` CLI.

.Procedure

. From the directory that contains the installation program, complete
* From the directory that contains the installation program, complete
the cluster installation:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for install-complete <1>
----
<1> For `<installation_directory>`, specify the path to the directory that you
stored the installation files in.
+
.Example output
[source,terminal]
----
INFO Waiting up to 40m0s for the cluster at https://api.mycluster.example.com:6443 to initialize...
INFO Waiting up to 10m0s for the openshift-console route to be created...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 1s
----
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

. Register your cluster on the Cluster registration page.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp_user_infra/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="cli-logging-in-kubeadmin_{context}"]
= Logging in to the cluster by using the CLI

[role="_abstract"]
To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

.Prerequisites
* You deployed an OpenShift Container Platform cluster.
* You installed the {oc-first}.
* Ensure the bootstrap process completed successfully.

.Procedure

. Export the `kubeadmin` credentials by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that stores the installation files.

. Verify you can run `oc` commands successfully using the exported configuration by running the following command:
+
[source,terminal]
----
$ oc whoami
----
+
.Example output
[source,terminal]
----
system:admin
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-china.adoc.
// * installing/installing_aws/installing-aws-secret-region.adoc
// *installing/validation_and_troubleshooting/validating-an-installation.adoc
// *installing/installing_aws/installing-aws-user-infra.adoc
// *installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// *installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-wavelength-zone.adoc

[id="logging-in-by-using-the-web-console_{context}"]
= Logging in to the cluster by using the web console

The `kubeadmin` user exists by default after an OpenShift Container Platform installation. You can log in to your cluster as the `kubeadmin` user by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the installation host.
* You completed a cluster installation and all cluster Operators are available.

.Procedure

. Obtain the password for the `kubeadmin` user from the `kubeadmin-password` file on the installation host:
+
[source,terminal]
----
$ cat <installation_directory>/auth/kubeadmin-password
----
+
[NOTE]
====
Alternatively, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====

. List the OpenShift Container Platform web console route:
+
[source,terminal]
----
$ oc get routes -n openshift-console | grep 'console-openshift'
----
+
[NOTE]
====
Alternatively, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====
+
.Example output
[source,terminal]
----
console     console-openshift-console.apps.<cluster_name>.<base_domain>            console     https   reencrypt/Redirect   None
----

. Navigate to the route detailed in the output of the preceding command in a web browser and log in as the `kubeadmin` user.

[role="_additional-resources"]
.Additional resources

* Accessing the web console

[role="_additional-resources"]
.Additional resources

* See About remote health monitoring for more information about the Telemetry service

[role="_additional-resources"]
[id="installing-restricted-networks-aws-additional-resources"]
== Additional resources

* Working with stacks ({aws-short} documentation)

[id="installing-restricted-networks-aws-next-steps"]
== Next steps

* Validate an installation.
* Customize your cluster.
* Configure image streams for the Cluster Samples Operator and the `must-gather` tool.
* Learn how to use Operator Lifecycle Manager in disconnected environments.
* If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by configuring additional trust stores.
* If necessary, you can Remote health reporting.
* If necessary, see Registering your disconnected cluster
* If necessary, you can remove cloud provider credentials.
