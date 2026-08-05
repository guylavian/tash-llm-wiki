---
title: "Creating a ROSA cluster without AWS STS"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-creating-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-creating-cluster
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Creating a ROSA cluster without AWS STS

[id="rosa-creating-cluster"]
= Creating a ROSA cluster without AWS STS

[role="_abstract"]
After you set up your environment and install OpenShift Container Platform, create a cluster. For additional security, you can create a OpenShift Container Platform cluster with AWS PrivateLink instead.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-creating-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

[id="rosa-classic-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster, you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-creating-cluster.adoc

[id="rosa-creating-cluster_{context}"]
= Creating your cluster

[role="_abstract"]
You can create a OpenShift Container Platform cluster using the OpenShift Container Platform CLI (`rosa`).

.Prerequisites

* You have installed the {rosa-cli-first}.

[NOTE]
====
AWS Shared VPCs are not currently supported for ROSA installs.
====

.Procedure

. You can create a cluster using the default settings or by specifying custom settings using the interactive mode. To view other options when creating a cluster, enter the `rosa create cluster --help` command.
+
Creating a cluster can take up to 40 minutes.
+
[NOTE]
====
Multiple availability zones (AZ) are recommended for production workloads. The default is a single availability zone. Use `--help` for an example of how to set this option manually or use interactive mode to be prompted for this setting.
====
+
* To create your cluster with the default cluster settings:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name>
----
+
.Example output
[source,terminal]
----
I: Creating cluster with identifier '1de87g7c30g75qechgh7l5b2bha6r04e' and name 'rh-rosa-test-cluster1'
I: To view list of clusters and their status, run `rosa list clusters`
I: Cluster 'rh-rosa-test-cluster1' has been created.
I: Once the cluster is 'Ready' you will need to add an Identity Provider and define the list of cluster administrators. See `rosa create idp --help` and `rosa create user --help` for more information.
I: To determine when your cluster is Ready, run `rosa describe cluster rh-rosa-test-cluster1`.
----
* To create a cluster using interactive prompts:
+
[source,terminal]
----
$ rosa create cluster --interactive
----
* To configure your networking IP ranges, you can use the following default ranges. For more information when using manual mode, use the `rosa create cluster --help | grep cidr` command. In interactive mode, you are prompted for the settings.
+
** Node CIDR: 10.0.0.0/16
** Service CIDR: 172.30.0.0/16
** Pod CIDR: 10.128.0.0/14

. Enter the following command to check the status of your cluster. During cluster creation, the `State` field from the output will transition from `pending` to `installing`, and finally to `ready`.
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
Name: rh-rosa-test-cluster1
OpenShift Version: 4.6.8
DNS: *.example.com
ID: uniqueidnumber
External ID: uniqueexternalidnumber
AWS Account: 123456789101
API URL: https://api.rh-rosa-test-cluster1.example.org:6443
Console URL: https://console-openshift-console.apps.rh-rosa-test-cluster1.example.or
Nodes: Master: 3, Infra: 2, Compute: 2
Region: us-west-2
Multi-AZ: false
State: ready
Channel Group: stable
Private: No
Created: Jan 15 2021 16:30:55 UTC
Details Page: https://console.redhat.com/examplename/details/idnumber
----
+
[NOTE]
====
If installation fails or the `State` field does not change to `ready` after 40 minutes, check the installation troubleshooting documentation for more details.
====

. Track the progress of the cluster creation by watching the OpenShift installer logs:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----

.Next steps

* Configure identity providers.

[role="_additional-resources"]
== Additional resources

* Understanding the ROSA deployment workflow
* Deleting a ROSA cluster
* ROSA architecture models
