---
title: "Tutorial: {product-title} with AWS STS explained"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-rosa-sts-explained
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-rosa-sts-explained
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: {product-title} with AWS STS explained

[id="cloud-experts-rosa-sts-explained"]
= Tutorial: OpenShift Container Platform with AWS STS explained

[role="_abstract"]
This tutorial outlines the two options for allowing OpenShift Container Platform to interact with resources in a user's Amazon Web Service (AWS) account. It details the components and processes that OpenShift Container Platform with Security Token Service (STS) uses to obtain the necessary credentials. It also reviews why OpenShift Container Platform with STS is the more secure, preferred method.

[NOTE]
====
This content currently covers OpenShift Container Platform Classic with AWS STS.
For OpenShift Container Platform with hosted control planes (HCP) with AWS STS, see AWS STS and OpenShift Container Platform with HCP explained.
====

This tutorial will:

* Enumerate two of the deployment options:
** OpenShift Container Platform with IAM Users
** OpenShift Container Platform with STS
* Explain the differences between the two options
* Explain why OpenShift Container Platform with STS is more secure and the preferred option
* Explain how OpenShift Container Platform with STS works

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-rosa-sts-explained.adoc

[id="cloud-experts-rosa-different-credential-methods-rosa_{context}"]
= Different credential methods to deploy OpenShift Container Platform

[role="_abstract"]
As part of OpenShift Container Platform, Red{nbsp}Hat manages infrastructure resources in your AWS account and must be granted the necessary permissions. There are currently two supported methods for granting those permissions:

* Using static IAM user credentials with an `AdministratorAccess` policy
+
This is referred to as "OpenShift Container Platform with IAM Users" in this tutorial. It is not the preferred credential method.
+
* Using AWS STS with short-lived, dynamic tokens
+
This is referred to as “OpenShift Container Platform with STS” in this tutorial. It is the preferred credential method.

[id="different-credential-methods-rosa-iam-users_{context}"]
== Rosa with IAM Users

When OpenShift Container Platform was first released, the only credential method was OpenShift Container Platform with IAM Users. This method grants IAM users with an `AdministratorAccess` policy full access to create the necessary resources in the AWS account that uses OpenShift Container Platform. The cluster can then create and expand its credentials as needed.

[id="different-credential-methods-rosa-sts_{context}"]
== OpenShift Container Platform with STS

OpenShift Container Platform with STS grants users limited, short-term access to resources in your AWS account. The STS method uses predefined roles and policies to grant temporary, least-privilege permissions to IAM users or authenticated federated users. The credentials typically expire an hour after being requested. Once expired, they are no longer recognized by AWS and no longer have account access from API requests made with them. For more information, see the AWS documentation. While both OpenShift Container Platform with IAM Users and OpenShift Container Platform with STS are currently enabled, OpenShift Container Platform with STS is the preferred and recommended option.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-rosa-sts-explained.adoc

[id="cloud-experts-rosa-sts-security_{context}"]
= OpenShift Container Platform with STS security

[role="_abstract"]
Several crucial components make OpenShift Container Platform with STS more secure than OpenShift Container Platform with IAM Users:

* An explicit and limited set of roles and policies that the user creates ahead of time. The user knows every requested permission and every role used.
* The service cannot do anything outside of those permissions.
* Whenever the service needs to perform an action, it obtains credentials that expire in one hour or less. This means that there is no need to rotate or revoke credentials. Additionally, credential expiration reduces the risks of credentials leaking and being reused.

[id="cloud-experts-sts-explained_{context}"]
== AWS STS explained

OpenShift Container Platform uses AWS STS to grant least-privilege permissions with short-term security credentials to specific and segregated IAM roles. The credentials are associated with IAM roles specific to each component and cluster that makes AWS API calls. This method aligns with principles of least-privilege and secure practices in cloud service resource management. The OpenShift Container Platform command-line interface (CLI) tool manages the STS roles and policies that are assigned for unique tasks and takes action upon AWS resources as part of OpenShift functionality.

STS roles and policies must be created for each OpenShift Container Platform cluster. To make this easier, the installation tools provide all the commands and files needed to create the roles as policies and an option to allow the CLI to automatically create the roles and policies. See "Creating a OpenShift Container Platform cluster with STS using customizations" in the _Additional resource_ for more information about the different `--mode` options.

[id="cloud-experts-sts-process_{context}"]
== OpenShift Container Platform with STS workflow
The user creates the required account-wide roles and account-wide policies. For more information, see the components section in this tutorial. During role creation, a trust policy, known as a cross-account trust policy, is created which allows a Red{nbsp}Hat-owned role to assume the roles. Trust policies are also created for the EC2 service, which allows workloads on EC2 instances to assume roles and obtain credentials. The user can then assign a corresponding permissions policy to each role.

After the account-wide roles and policies are created, the user can create a cluster. Once cluster creation is initiated, the Operator roles are created so that cluster Operators can make AWS API calls. These roles are then assigned to the corresponding permission policies that were created earlier and a trust policy with an OIDC provider. The Operator roles differ from the account-wide roles in that they ultimately represent the pods that need access to AWS resources. Because a user cannot attach IAM roles to pods, they must create a trust policy with an OIDC provider so that the Operator, and therefore the pods, can access the roles they need.

Once the user assigns the roles to the corresponding policy permissions, the final step is creating the OIDC provider.

image::cloud-experts-sts-explained_creation_flow.png[]

When a new role is needed, the workload currently using the Red{nbsp}Hat role will assume the role in the AWS account, obtain temporary credentials from AWS STS, and begin performing the actions using API calls within the customer's AWS account as permitted by the assumed role's permissions policy. The credentials are temporary and have a maximum duration of one hour.

image::cloud-experts-sts-explained_highlevel.png[]

The entire workflow is depicted in the following graphic:

image::cloud-experts-sts-explained_entire_flow.png[]

Operators use the following process to obtain the requisite credentials to perform their tasks. Each Operator is assigned an Operator role, a permissions policy, and a trust policy with an OIDC provider. The Operator will assume the role by passing a JSON web token that contains the role and a token file (`web_identity_token_file`) to the OIDC provider, which then authenticates the signed key with a public key. The public key is created during cluster creation and stored in an S3 bucket. The Operator then confirms that the subject in the signed token file matches the role in the role trust policy which ensures that the OIDC provider can only obtain the allowed role. The OIDC provider then returns the temporary credentials to the Operator so that the Operator can make AWS API calls. For a visual representation, see below:

image::cloud-experts-sts-explained_oidc_op_roles.png[]

[id="cloud-experts-sts-use-cases_{context}"]
== OpenShift Container Platform with STS use cases

Creating nodes at cluster install: The Red{nbsp}Hat installation program uses the `RH-Managed-OpenShift-Installer` role and a trust policy to assume the `Managed-OpenShift-Installer-Role` role in the customer's account. This process returns temporary credentials from AWS STS. The installation program begins making the required API calls with the temporary credentials just received from STS. The installation program creates the required infrastructure in AWS. The credentials expire within an hour and the installation program no longer has access to the customer's account.

The same process also applies for support cases. In support cases, a Red{nbsp}Hat site reliability engineer (SRE) replaces the installation program.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-rosa-sts-explained.adoc

[id="cloud-experts-components-specific-to-rosa-with-sts_{context}"]
= Components specific to OpenShift Container Platform with STS

[role="_abstract"]
* *AWS infrastructure* - This provides the infrastructure required for the cluster. It contains the actual EC2 instances, storage, and networking components.
* *AWS STS* - See the credential method section above.
* *OpenID Connect (OIDC)* - This provides a mechanism for cluster Operators to authenticate with AWS, assume the cluster roles through a trust policy, and obtain temporary credentials from STS to make the required API calls.
* *Roles and policies* - The roles and policies are one of the main differences between OpenShift Container Platform with STS and OpenShift Container Platform with IAM Users. For OpenShift Container Platform with STS, the roles and policies used by OpenShift Container Platform are broken into account-wide roles and policies and Operator roles and policies.
+
The policies determine the allowed actions for each of the roles. See the _Additional resources_ for more details about the individual roles and policies.
+
** The following account-wide roles are required:
+
*** ManagedOpenShift-Installer-Role
*** ManagedOpenShift-ControlPlane-Role
*** ManagedOpenShift-Worker-Role
*** ManagedOpenShift-Support-Role
+
** The following account-wide policies are required:
+
*** ManagedOpenShift-Installer-Role-Policy
*** ManagedOpenShift-ControlPlane-Role-Policy
*** ManagedOpenShift-Worker-Role-Policy
*** ManagedOpenShift-Support-Role-Policy
*** ManagedOpenShift-openshift-ingress-operator-cloud-credentials ^[1]^
*** ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credent ^[1]^
*** ManagedOpenShift-openshift-cloud-network-config-controller-cloud ^[1]^
*** ManagedOpenShift-openshift-machine-api-aws-cloud-credentials ^[1]^
*** ManagedOpenShift-openshift-cloud-credential-operator-cloud-crede ^[1]^
*** ManagedOpenShift-openshift-image-registry-installer-cloud-creden ^[1]^
+
[.small]
--
1. This policy is used by the cluster Operator roles, listed below. The Operator roles are created in a second step because they are dependent on an existing cluster name and cannot be created at the same time as the account-wide roles.
--
+
** The Operator roles are:
+
*** <cluster-name\>-xxxx-openshift-cluster-csi-drivers-ebs-cloud-credent
*** <cluster-name\>-xxxx-openshift-cloud-network-config-controller-cloud
*** <cluster-name\>-xxxx-openshift-machine-api-aws-cloud-credentials
*** <cluster-name\>-xxxx-openshift-cloud-credential-operator-cloud-crede
*** <cluster-name\>-xxxx-openshift-image-registry-installer-cloud-creden
*** <cluster-name\>-xxxx-openshift-ingress-operator-cloud-credentials
+
** Trust policies are created for each account-wide and Operator role.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-rosa-sts-explained.adoc

[id="cloud-experts-deploying-rosa-with-sts-cluster_{context}"]
= Deploying a OpenShift Container Platform STS cluster

[role="_abstract"]
You are not expected to create the resources listed in the below steps from scratch. The OpenShift Container Platform CLI creates the required JSON files for you and outputs the commands you need. The OpenShift Container Platform CLI can also take this a step further and run the commands for you, if desired.

.Procedure
. Steps to deploy a OpenShift Container Platform with STS cluster
. Create the account-wide roles and policies.
. Assign the permissions policy to the corresponding account-wide role.
. Create the cluster.
. Create the Operator roles and policies.
. Assign the permission policy to the corresponding Operator role.
. Create the OIDC provider.
+
The roles and policies can be created automatically by the OpenShift Container Platform CLI, or they can be manually created by utilizing the `--mode manual` or `--mode auto` flags in the {rosa-cli}.
. Scaling the cluster: The `machine-api-operator` uses AssumeRoleWithWebIdentity to assume the `machine-api-aws-cloud-credentials` role. This launches the sequence for the cluster Operators to receive the credentials. The `machine-api-operator` role can now make the relevant API calls to add more EC2 instances to the cluster.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Creating a OpenShift Container Platform cluster with STS using customizations
* AWS compute types to see supported instance types for compute nodes
* Provisioned AWS infrastructure for control plane and infrastructure node configuration
* Creating a cluster with customizations
* Deploying the cluster tutorial
* About IAM resources
