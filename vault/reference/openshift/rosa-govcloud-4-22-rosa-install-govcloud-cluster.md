---
title: "Installing a {product-title} cluster in AWS GovCloud"
type: reference
domain: openshift
slug: rosa-govcloud-4-22-rosa-install-govcloud-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_govcloud/rosa-install-govcloud-cluster
version: 4.22
family: rosa_govcloud
documentKind: "Documentation"
---

# Installing a {product-title} cluster in AWS GovCloud

[id="rosa-install-govcloud-cluster"]
= Installing a OpenShift Container Platform cluster in AWS GovCloud

[role="_abstract"]
You can install a OpenShift Container Platform cluster in AWS GovCloud with or without AWS PrivateLink. Before you begin, ensure that you meet the requirements to access AWS GovCloud, you have prepared to access OpenShift Container Platform in AWS GovCloud, and you have signed up for a Red{nbsp}Hat FedRAMP account.

// Module included in the following assemblies:
// * rosa_govcloud/rosa-install-govcloud-cluster.adoc

[id="rosa-govcloud-deploy-cluster_{context}"]
= Preparing to deploy a OpenShift Container Platform cluster in AWS GovCloud

[role="_abstract"]
To deploy a OpenShift Container Platform cluster in AWS GovCloud, you must be logged in to your Red{nbsp}Hat FedRAMP account.

.Prerequisites

* You have configured your AWS CLI to use GovCloud.
* You are logged into your government region.

.Procedure

. Navigate to https://console.openshiftusgov.com/openshift/token.
. Sign in with your Red{nbsp}Hat FedRAMP account credentials where you will see a screen with your token.
. Copy your token for the next step.
+
. In your terminal:
+
.. Run `rosa login` and paste your copied token to log in to the service.
+
[source,terminal]
----
$ rosa login --govcloud --token=<TOKEN>
----
+
[NOTE]
====
Depending on your AWS CLI configuration, you might need to add a government region to the end of the command string, such as `--region us-gov-west-1`.
====
+
.. Run `rosa whoami` to confirm all information is correct ensuring that you are using the AWS Gov region and the {cluster-manager-first} API is “https://api.openshiftusgov.com”..
+
[source,terminal]
----
$ rosa whoami
----
+
.Example output

[source,text]
----
AWS ARN:                                 arn:aws-us-gov:iam::00000000000:user/rosa-gov-user
AWS Account ID:                       00000000000
AWS Default Region:                 us-gov-east-1
OCM API:                                   https://api.openshiftusgov.com
OCM Account Email:                  rosa-gov-user@redhat.com
OCM Account ID:                       3ZXXXXXXXXXXXXXXXXXXXXXXXXX
OCM Account Name:                 Rosa Gov
OCM Account Username:          rosa-gov-user
OCM Organization External ID:  rosa-gov-user
OCM Organization ID:                3ZXXXXXXXXXXXXXXXXXXXXXXXXX
OCM Organization Name:          rosa-gov-user
----
+
. You must create a VPC where OpenShift Container Platform will be deployed.
For instructions on setting up a VPC, see Amazon VPC architecture for the AWS PrivateLink use case.

// Module included in the following assemblies:
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc

[id="rosa-aws-privatelink-create-cluster_{context}"]
= Creating an AWS PrivateLink cluster

[role="_abstract"]
You can create an AWS PrivateLink cluster by using the {rosa-cli-first}.

[NOTE]
====
AWS PrivateLink is supported on existing VPCs only.
====

.Prerequisites

* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli}, on your installation host.
* For GovCloud, you have enabled the OpenShift Container Platform service in the AWS Console on the linked commercial account because it is inside the commercial account that you enable OpenShift Container Platform for GovCloud. For more information, see Enable ROSA and configure AWS prerequisites.
* For Private Marketplace, you have enabled the OpenShift Container Platform service in the AWS Console.
For more information, see AWS Marketplace listings for ROSA.
For more information, see AWS Marketplace listings for ROSA.

.Procedure

. With AWS PrivateLink, you can create a cluster with a single availability zone (Single-AZ) or many availability zones (Multi-AZ). In either case, your machine's classless inter-domain routing (CIDR) must match your virtual private cloud's CIDR. See Requirements for using your own VPC and VPC validation for more information.
+
[IMPORTANT]
====
If you use a firewall, you must configure it so that OpenShift Container Platform can access the sites that it requires to function.

For more information, see the AWS PrivateLink firewall prerequisites section.
====
+
[NOTE]
====
If your cluster name is longer than 15 characters, it will contain an automatically generated domain prefix as a sub-domain for your provisioned cluster on `*.openshiftapps.com`.

To customize the subdomain, use the `--domain-prefix` flag. The domain prefix cannot be longer than 15 characters, must be unique, and cannot be changed after cluster creation.
====
+
** To create a Single-AZ cluster:
+
[source,terminal]
----
$ rosa create cluster --private-link --cluster-name=<cluster-name> [--machine-cidr=<VPC CIDR>/16] --subnet-ids=<private-subnet-id>
----
** To create a Multi-AZ cluster:
+
[source,terminal]
----
$ rosa create cluster --private-link --multi-az --cluster-name=<cluster-name> [--machine-cidr=<VPC CIDR>/16] --subnet-ids=<private-subnet-id1>,<private-subnet-id2>,<private-subnet-id3>
----

. Enter the following command to check the status of your cluster. During cluster creation, the `State` field from the output changesfrom `pending` to `installing`, and finally to `ready`.
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
[NOTE]
====
If installation fails or the `State` field does not change to `ready` after 40 minutes, check the installation troubleshooting documentation for more details.
====

. Enter the following command to follow the OpenShift installer logs to track the progress of your cluster:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----

[role="_additional-resources"]
.Additional resources
* Getting started with OpenShift Container Platform in AWS GovCloud
