---
title: "{product-title} with STS deployment workflow"
type: reference
domain: openshift
slug: rosa-getting-started-4-22-rosa-sts-getting-started-workflow
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_getting_started/rosa-sts-getting-started-workflow
version: 4.22
family: rosa_getting_started
documentKind: "Documentation"
---

# {product-title} with STS deployment workflow

[id="rosa-sts-understanding-the-deployment-workflow"]
= OpenShift Container Platform with STS deployment workflow

[role="_abstract"]
The OpenShift Container Platform with STS deployment workflow guides you through prerequisite verification, environment setup, cluster creation options, access configuration, user management, and cluster lifecycle operations.

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-sts-getting-started-workflow.adoc

[id="rosa-sts-overview-of-the-deployment-workflow_{context}"]
= Overview of the OpenShift Container Platform with STS deployment workflow

[role="_abstract"]
The AWS Security Token Service (STS) is a global web service that provides short-term credentials for IAM or federated users. You can use AWS STS with OpenShift Container Platform to allocate temporary, limited-privilege credentials for component-specific IAM roles. The service enables cluster components to make AWS API calls using secure cloud resource management practices.

You can follow the workflow stages to set up and access a OpenShift Container Platform cluster that uses STS.

. *Complete the AWS prerequisites for OpenShift Container Platform with STS*. To deploy a OpenShift Container Platform cluster with STS, your AWS account must meet the prerequisite requirements.
. *Review the required AWS service quotas*. To prepare for your cluster deployment, review the AWS service quotas that are required to run a OpenShift Container Platform cluster.
. *Set up the environment and install OpenShift Container Platform using STS*. Before you create a OpenShift Container Platform with STS cluster, you must enable OpenShift Container Platform in your AWS account, install and configure the required CLI tools, and verify the configuration of the CLI tools. You must also verify that the AWS Elastic Load Balancing (ELB) service role exists and that the required AWS resource quotas are available.
. *Create a OpenShift Container Platform cluster with STS quickly or create a cluster using customizations*. Use the {rosa-cli} (`rosa`) or {cluster-manager-first} to create a cluster with STS. You can create a cluster quickly by using the default options, or you can apply customizations to suit the needs of your organization.
. *Access your cluster*. You can configure an identity provider and grant cluster administrator privileges to the identity provider users as required. You can also access a newly-deployed cluster quickly by configuring a `cluster-admin` user.
. *Revoke access to a OpenShift Container Platform cluster for a user*. You can revoke access to a OpenShift Container Platform with STS cluster from a user by using the {rosa-cli} or the web console.
. *Delete a OpenShift Container Platform cluster*. You can delete a OpenShift Container Platform with STS cluster by using the {rosa-cli} (`rosa`). After deleting a cluster, you can delete the STS resources by using the AWS Identity and Access Management (IAM) Console.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* AWS prerequisites for OpenShift Container Platform with STS
* Required AWS service quotas
* Setting up the environment and installing OpenShift Container Platform using STS
* Creating a OpenShift Container Platform cluster with STS quickly
* Creating a cluster using customizations
* Accessing your cluster
* Revoking access to a OpenShift Container Platform cluster for a user
* Deleting a OpenShift Container Platform cluster
* Understanding the OpenShift Container Platform deployment workflow
