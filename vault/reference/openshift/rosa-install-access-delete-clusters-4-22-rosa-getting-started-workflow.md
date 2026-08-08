---
title: "Understanding the ROSA deployment workflow"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-getting-started-workflow
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-getting-started-workflow
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Understanding the ROSA deployment workflow

[id="rosa-understanding-the-deployment-workflow"]
= Understanding the ROSA deployment workflow

[role="_abstract"]
Before you create a OpenShift Container Platform cluster, you must complete the AWS prerequisites, verify that the required AWS service quotas are available, and set up your environment.

The OpenShift Container Platform workflow consists of several stages, with detailed resources available for each phase of the process.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-getting-started-workflow.adoc

[id="rosa-overview-of-the-deployment-workflow_{context}"]
= Overview of the OpenShift Container Platform deployment workflow

[role="_abstract"]
You can follow the workflow stages outlined in this section to set up and access a OpenShift Container Platform cluster.

. Perform the AWS prerequisites. To deploy a OpenShift Container Platform cluster, your AWS account must meet the prerequisite requirements.

. Review the required AWS service quotas. To prepare for your cluster deployment, review the AWS service quotas that are required to run a OpenShift Container Platform cluster.

. Configure your AWS account. Before you create a OpenShift Container Platform cluster, you must enable OpenShift Container Platform in your AWS account, install and configure the AWS CLI (`aws`) tool, and verify the AWS CLI tool configuration.

. Install the OpenShift Container Platform and OpenShift CLI tools and verify the AWS servce quotas. Install and configure the {rosa-cli-first} and the {oc-first}. You can verify if the required AWS resource quotas are available by using the {rosa-cli}.

. Create a OpenShift Container Platform cluster or Create a ROSA cluster using AWS PrivateLink. Use the ROSA CLI (`rosa`) to create a cluster. You can optionally create a ROSA cluster with AWS PrivateLink.

. Access a cluster. You can configure an identity provider and grant cluster administrator privileges to the identity provider users as required. You can also access a newly deployed cluster quickly by configuring a `cluster-admin` user.

. Revoke access to a ROSA cluster for a user. You can revoke access to a OpenShift Container Platform cluster from a user by using the {rosa-cli} or the web console.

. Delete a ROSA cluster. You can delete a OpenShift Container Platform cluster by using the {rosa-cli}.

[id="additional_resources_{context}"]
[role="_additional-resources"]
== Additional resources

* Understanding the OpenShift Container Platform with STS deployment workflow
* Configuring identity providers
* Deleting a cluster
* Deleting access to a cluster
* Command quick reference for creating clusters and users
