---
title: "Installation methods"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-aws
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installation methods

[id="installing-methods-aws"]
= Installation methods

[role="_abstract"]
You can install OpenShift Container Platform on {aws-full} using installer-provisioned, user-provisioned infrastructure, or on a single node, depending on the needs of your use case.

The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster.

You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

You can also install OpenShift Container Platform on a single node, which is a specialized installation method that is ideal for edge computing environments.

[id="choosing-an-method-to-install-ocp-on-aws-installer-provisioned_{context}"]
= Installing a cluster on installer-provisioned infrastructure

[role="_abstract"]
You can install a cluster on {aws-short} infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

You can install OpenShift Container Platform on {aws-short} infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options.

You can install a customized cluster on {aws-short} infrastructure that the installation program provisions. You can also customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available post-installation.

You can install OpenShift Container Platform on {aws-short} on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

You can install OpenShift Container Platform on an existing {aws-short} Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

You can install a private cluster on an existing {aws-short} VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

OpenShift Container Platform can be deployed into {aws-short} regions that are specifically designed for US government agencies at the federal, state, and local level, as well as contractors, educational institutions, and other US customers that must run sensitive workloads in the cloud.

[id="choosing-an-method-to-install-ocp-on-aws-user-provisioned-provisioned_{context}"]
= Installing a cluster on user-provisioned infrastructure

[role="_abstract"]
You can install a cluster on {aws-short} in one of two ways: on infrastructure that you provide or infrastructure that you provide by using an internal mirror of the installation release content.

To install OpenShift Container Platform on {aws-short} infrastructure that you provide, you can use the provided CloudFormation templates to create stacks of {aws-short} resources that represent each of the components required for an OpenShift Container Platform installation.

To install a cluster that does not require an active internet connection to obtain the software components, install OpenShift Container Platform on {aws-short} infrastructure that you provide by using an internal mirror of the installation release content. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the {aws-short} APIs.

[id="choosing-an-method-to-install-ocp-on-aws-single-node"_{context}"]
= Installing a cluster on a single node

[role="_abstract"]
Installing OpenShift Container Platform on a single node alleviates some of the requirements for high availability and large scale clusters. However, you must address requirements for installing on a single node, and the additional requirements for installing {sno} on a cloud provider.

After addressing the requirements for single node installation, use the installing a customized cluster on AWS procedure to install the cluster. The installing single-node OpenShift manually section contains an exemplary `install-config.yaml` file when installing an OpenShift Container Platform cluster on a single node.

[role="_additional-resources"]
[id="installing-methods-aws-ipi-additional-resources"]
== Additional resources
* Installing a cluster quickly on AWS
* Installing a customized cluster on AWS
* Post-installation
* Installing a cluster on AWS in a restricted network
* Installing a cluster on an existing Virtual Private Cloud
* Installing a private cluster on an existing VPC
* Installing a cluster on AWS into a government or secret region
* Installing a cluster on AWS infrastructure that you provide
* Installing a cluster on AWS in a restricted network with user-provisioned infrastructure
* Installation process
