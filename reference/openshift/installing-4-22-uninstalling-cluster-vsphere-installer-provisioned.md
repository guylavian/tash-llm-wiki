---
title: "Uninstalling a cluster on vSphere that uses installer-provisioned infrastructure"
type: reference
domain: openshift
slug: installing-4-22-uninstalling-cluster-vsphere-installer-provisioned
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/uninstalling-cluster-vsphere-installer-provisioned
version: 4.22
family: installing
documentKind: "Documentation"
---

# Uninstalling a cluster on vSphere that uses installer-provisioned infrastructure

[id="uninstalling-cluster-vsphere-installer-provisioned"]
= Uninstalling a cluster on vSphere that uses installer-provisioned infrastructure

You can remove a cluster that you deployed in your VMware vSphere instance by using installer-provisioned infrastructure.

// Module included in the following assemblies:
//
// * installing/installing_aws/uninstalling-cluster-aws.adoc
// * installing/installing_azure/uninstalling-cluster-azure.adoc
// * installing/installing_azure/uninstalling-cluster-azure-stack-hub.adoc
// * installing/installing_gcp/uninstalling-cluster-gcp.adoc
// * installing/installing_ibm_cloud/uninstalling-cluster-ibm-cloud.adoc
// * installing/installing_ibm_powervs/uninstalling-cluster-ibm-power-vs.adoc
// * installing/installing_osp/uninstalling-cluster-openstack.adoc
// * installing/installing_vmc/uninstalling-cluster-vmc.adoc
// * installing/installing_vsphere/uninstalling-cluster-vsphere-installer-provisioned.adoc
// * installing/installing_nutanix/uninstalling-cluster-nutanix.adoc

[id="installation-uninstall-clouds_{context}"]
= Removing a cluster that uses installer-provisioned infrastructure

[role="_abstract"]
You can remove a cluster that uses installer-provisioned infrastructure that you provisioned from your cloud platform.

[NOTE]
====
If you deployed your cluster to the AWS C2S Secret Region, the installation program does not support destroying the cluster; you must manually remove the cluster resources.
====

[NOTE]
====
After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource.
For example, some {gcp-full} resources require IAM permissions in shared VPC host projects, or there might be unused health checks that must be deleted.
====

.Prerequisites

* You have a copy of the installation program that you used to deploy the cluster.
* You have the files that the installation program generated when you created your
cluster.
* You installed the `core-installer` tool by entering the `sudo dnf install coreos-installer` command in your CLI.
* You have configured the `ccoctl` binary.
* You have installed the {ibm-cloud-name} CLI and installed or updated the VPC infrastructure service plugin. For more information see "Prerequisites" in the {ibm-cloud-name} CLI documentation.

.Procedure
. If the following conditions are met, this step is required:
** The installer created a resource group as part of the installation process.
** You or one of your applications created persistent volume claims (PVCs) after the cluster was deployed.
+
In which case, the PVCs are not removed when uninstalling the cluster, which might prevent the resource group from being successfully removed. To prevent a failure:
+
.. Log in to the {ibm-cloud-name} using the CLI.
+
.. To list the PVCs, run the following command:
+
[source,terminal]
----
$ ibmcloud is volumes --resource-group-name <infrastructure_id>
----
+
For more information about listing volumes, see the {ibm-cloud-name} CLI documentation.
+
.. To delete the PVCs, run the following command:
+
[source,terminal]
----
$ ibmcloud is volume-delete --force <volume_id>
----
+
For more information about deleting volumes, see the {ibm-cloud-name} CLI documentation.

. Export the API key that was created as part of the installation process.
+
[source,terminal]
----
$ export IC_API_KEY=<api_key>
----
+
+
[source,terminal]
----
$ export IBMCLOUD_API_KEY=<api_key>
----
+
[NOTE]
====
You must set the variable name exactly as specified. The installation program expects the variable name to be present to remove the service IDs that were created when the cluster was installed.
====

. From the directory that has the installation program on the computer that you used to install the cluster, run the following command:
+
[source,terminal]
----
$ ./openshift-install destroy cluster \
--dir <installation_directory> --log-level info
----
+
where:

<installation_directory>:: Specify the path to the directory that you stored the installation files in.
--log-level info:: To view different details, specify `warn`, `debug`, or `error` instead of `info`.
+
[NOTE]
====
You must specify the directory that includes the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.
====
+
[NOTE]
====
* You must specify the directory that has the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.

* You might have to run the `openshift-install destroy` command up to three times to ensure a proper cleanup.
====

. Remove the manual CCO credentials that were created for the cluster:
+
[source,terminal]
----
$ ccoctl ibmcloud delete-service-id \
    --credentials-requests-dir <path_to_credential_requests_directory> \
    --name <cluster_name>
----
+
--
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
--

. Optional: Use the `coreos-installer` tool to add the `coreos.inst.wipe=yes` flag to the Preboot Execution Environment (PXE) boot configuration. This operation wipes the disk on your system so that if you create a new cluster, you have a clean installation environment. For more detailed instructions, see How to wipe OpenStack disks in OpenShift Container Platform 4 reinstallation (Knowledgebase article).

. Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.

// The above CCO credential removal for {ibm-cloud-title} is only necessary for manual mode. Future releases that support other credential methods will not require this step.
