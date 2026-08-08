---
title: "Uninstalling a cluster on {aws-short}"
type: reference
domain: openshift
slug: installing-4-22-uninstalling-cluster-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/uninstalling-cluster-aws
version: 4.22
family: installing
documentKind: "Documentation"
---

# Uninstalling a cluster on {aws-short}

[id="uninstalling-cluster-aws"]
= Uninstalling a cluster on {aws-short}

[role="_abstract"]
You can remove a cluster that you deployed to {aws-first}.

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

// Module included in the following assemblies:
//
// * installing/installing_aws/uninstalling-cluster-aws.adoc
// * installing/installing_gcp/uninstalling-cluster-gcp.adoc
// * installing/installing_azure/uninstalling-cluster-azure.adoc

[id="cco-ccoctl-deleting-sts-resources_{context}"]
= Deleting {cp-first} resources with the Cloud Credential Operator utility

[role="_abstract"]
After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the CCO utility (`ccoctl`) to remove the {cp-first} resources that `ccoctl` created during installation.

.Prerequisites

* Extract and prepare the `ccoctl` binary.
* Uninstall an OpenShift Container Platform cluster on {cp} that uses short-term credentials.

.Procedure
//GCP has extra prep steps
. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --to=<path_to_directory_for_credentials_requests>
----
+
where:

`--included`:: The parameter includes only the manifests that your specific cluster configuration requires.
`<path_to_directory_for_credentials_requests>`:: Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

. Delete the {cp} resources that `ccoctl` created by running the following command:
* Delete the {cp} resources that `ccoctl` created by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ ccoctl {cp-name} delete \
  --name=<name> \
  --project=<{cp-name}_project_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --force-delete-custom-roles
  --region=<{cp-name}_region> \
  --subscription-id=<{cp-name}_subscription_id> \
  --delete-oidc-resource-group
----
+
where:

`<name>`:: Matches the name that was originally used to create and tag the cloud resources.
`<{cp-name}_project_id>`:: The {cp} project ID in which to delete cloud resources.
`force-delete-custom-roles`:: Optional: This parameter deletes the custom roles that the `ccoctl` utility creates during installation. {gcp-short} does not permanently delete custom roles immediately. For more information, see {gcp-short} documentation about deleting a custom role.
+
.Example output
[source,text]
----
2021/04/08 17:50:41 Identity Provider object .well-known/openid-configuration deleted from the bucket <name>-oidc
2021/04/08 17:50:42 Identity Provider object keys.json deleted from the bucket <name>-oidc
2021/04/08 17:50:43 Identity Provider bucket <name>-oidc deleted
2021/04/08 17:51:05 Policy <name>-openshift-cloud-credential-operator-cloud-credential-o associated with IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:05 IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:07 Policy <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials associated with IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:07 IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:08 Policy <name>-openshift-image-registry-installer-cloud-credentials associated with IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:08 IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:09 Policy <name>-openshift-ingress-operator-cloud-credentials associated with IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:10 IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:11 Policy <name>-openshift-machine-api-aws-cloud-credentials associated with IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:11 IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:39 Identity Provider with ARN arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com deleted
----
//Would love a GCP and Azure version of the above output.

.Verification

* To verify that the resources are deleted, query {cp}. For more information, refer to {cp} documentation.

// Module included in the following assemblies:
//
// * installing/installing_aws/uninstalling-cluster-aws.adoc

[id="installation-aws-delete-cluster"]
= Deleting a cluster with a configured {aws-short} Local Zone infrastructure

[role="_abstract"]
After you install a cluster on {aws-first} into an existing Virtual Private Cloud (VPC), and you set subnets for each Local Zone location, you can delete the cluster and any {aws-short} resources associated with it.

The example in the procedure assumes that you created a VPC and its subnets by using a CloudFormation template.

.Prerequisites

* You know the name of the CloudFormation stacks, `<local_zone_stack_name>` and `<vpc_stack_name>`, that were used during the creation of the network. You need the name of the stack to delete the cluster.
* You have access rights to the directory that contains the installation files that were created by the installation program.
* Your account includes a policy that provides you with permissions to delete the CloudFormation stack.

.Procedure

. Change to the directory that contains the stored installation program, and delete the cluster by using the `destroy cluster` command:
+
[source,terminal]
----
$ ./openshift-install destroy cluster --dir <installation_directory> \
   --log-level=debug
----
+
where:

`<installation_directory>`:: Specify the directory that stored any files created by the installation program.
`--log-level=debug`:: To view different log details, specify `error`, `info`, or `warn` instead of `debug`.

. Delete the CloudFormation stack for the Local Zone subnet:
+
[source,terminal]
----
$ aws cloudformation delete-stack --stack-name <local_zone_stack_name>
----

. Delete the stack of resources that represent the VPC:
+
[source,terminal]
----
$ aws cloudformation delete-stack --stack-name <vpc_stack_name>
----

.Verification

* Check that you removed the stack resources by issuing the following commands in the {aws-short} CLI. The AWS CLI outputs that no template component exists.
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <local_zone_stack_name>
----
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <vpc_stack_name>
----

[role="_additional-resources"]
[id="installing-localzone-additional-resources"]
== Additional resources

* Working with stacks({aws-short} documentation)
* Opt into AWS Local Zones({aws-short} documentation)
* AWS Local Zones available locations({aws-short} documentation)
* AWS Local Zones features({aws-short} documentation)
