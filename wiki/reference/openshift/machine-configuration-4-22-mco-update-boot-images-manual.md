---
title: "Manually updating the boot image"
type: reference
domain: openshift
slug: machine-configuration-4-22-mco-update-boot-images-manual
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/mco-update-boot-images-manual
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Manually updating the boot image

[id="mco-update-boot-images-manual"]
= Manually updating the boot image

[role="_abstract"]
For OpenShift Container Platform platforms that do not support automatic boot image updating or for clusters configured with the boot image management feature disabled, you can manually update the boot image used by the compute nodes in your cluster. By updating the boot image, you can ensure that newly scaled up nodes are able to successfully use the latest {op-system-first} version and join the cluster.

[NOTE]
====
Red{nbsp}Hat does not support manually updating the boot image in control plane nodes.
====

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-azure_{context}"]
= Manually updating the boot image on an {azure-short} cluster

[role="_abstract"]
You can manually update the boot image for your {azure-first} cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

[NOTE]
====
Boot image updates are not supported for Azure confidential virtual machines and Azure Stack Hub clusters. Contact Red Hat Support for these cases.
====

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your compute machine sets to use that image.

The process requires you to determine the product variant and Hyper-V generation of your Azure boot image. The following procedure helps determine both values, which you need in order to look up the target image.

[NOTE]
====
For clusters that use a default {op-system-first}, Azure Red Hat OpenShift (ARO), or Azure Marketplace image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have installed the {oc-first}.

* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".

* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".

* You have downloaded the latest version of the OpenShift Container Platform installation program from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

* You have installed the `jq` program.

.Procedure

. Set an environment variable with your cluster architecture by running the following command:
+
[source,terminal]
----
$ export ARCH=<architecture_type>
----
+
Replace `<architecture_type>` with one of the following values:
+
--
* Use `aarch64` for the AArch64 or ARM64 architecture.
* Use `x86_64` for the x86_64 or AMD64 architecture.
--
+
You can find the architecture as a label in any `MachineSet` object.
+
.Example machine set with an architecture label
[source,terminal]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
# ...
----

. Determine your Azure image variant and Hyper-V generation:

.. Obtain the required values from your machine set by running the following command:
+
[source,terminal]
----
$ oc get machineset <machineset-name> -n openshift-machine-api \
  -o jsonpath='{.spec.template.spec.providerSpec.value.image}'
----
+
.Example output
[source,terminal]
----
{"offer":"rh-ocp-worker","publisher":"redhat","resourceID":"","sku":"rh-ocp-worker","type":"MarketplaceWithPlan","version":"4.16.20231023"}
----

.. Determine your image variant by comparing the output to the entries in the following table:
+
[cols="1,1",options="header"]
|===
| Output parmeters | Variant
| `resourceID` is non-empty | `no-purchase-plan`
| `publisher` is `azureopenshift` | `no-purchase-plan`
| `publisher` is `redhat` and `offer` is `rh-ocp-worker` | `ocp`
| `publisher` is `redhat` and `offer` is `rh-opp-worker` | `opp`
| `publisher` is `redhat` and `offer` is `rh-oke-worker` | `oke`
| `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `ocp-emea`
| `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `opp-emea`
| `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `oke-emea`
|===
+
Make note of the variant for later use.

.. Determine your image Hyper-V generation by comparing the output to the entries in the following table:
+
[cols="1,1,1",options="header"]
|===
|Output | Image type  | Hyper-V generation
| `resourceID` is non-empty | Legacy uploaded  a| * `hyperVGen2` if the `resourceID` value contains `gen2`
* `hyperVGen1`  if the `resourceID` value does not contain `gen2`
| `publisher` is `azureopenshift` | Unpaid marketplace  a| * `hyperVGen2` if `sku` contains `v2` or the cluster architecture is AArch64 or ARM64
* `hyperVGen1` for all other images
| `publisher` is `redhat` or `redhat-limited`. | Paid marketplace  a| * `hyperVGen1` if `sku` contains `-gen1`
* `hyperVGen2` for all other images
|===
+
Make note of the generation for later use.

.. Optional: You can compare the output of the `version` parameter against the output of the following command to determine if your boot image needs updating.
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
----
+
`ARCH` is the environment variable you created in a previous step.
+
In the output of the command, locate your variant and generation as shown in the following example:
+
.Example output
[source,terminal]
----
  "ocp": {
# ...
    "hyperVGen2": {
      "publisher": "redhat",
      "offer": "rh-ocp-worker",
      "sku": "rh-ocp-worker",
      "version": "4.18.2025031114"
----
+
If the boot image referenced in the `version` parameter of your machine set matches or is later than the version in this output, no further action on your part is required to update the boot image. If not, continue with this procedure.

. Obtain the values needed to identify the new boot image and set the values as environment variables:

.. Obtain the values required for the new boot image by running the following command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
----
+
`ARCH` is the environment variable you created in a previous step.

.. In the output of the command, locate your variant and generation as shown in the following example:
+
.Example output
[source,terminal]
----
  "ocp": {
  # ...
    "hyperVGen2": {
      "publisher": "redhat",
      "offer": "rh-ocp-worker",
      "sku": "rh-ocp-worker",
      "version": "9.6.20251015"
----

.. Set an environment variable with your image variant by running the following command:
+
[source,terminal]
----
$ export VARIANT=<variant>
----
+
Replace `<variant>` with the variant of your image, one of the following vales: `no-purchase-plan`, `ocp`, `opp`, `oke`, `ocp-emea`, `opp-emea`, or `oke-emea`.

.. Set an environment variable with your image generation by running the following command:
+
[source,terminal]
----
$ export GEN=<generation>
----
+
Replace `<generation>` with the generation of your image, one of the following vales: `hyperVGen1` or `hyperVGen2`.

.. Set environment variables for the `publisher`, `offer`, `sku`, and `version` fields based on the `openshift-install` output for your variant and generation by running the following commands:
+
[source,terminal]
----
$ export PUBLISHER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".publisher')
----
+
`ARCH`, `VARIANT`, and `GEN` are environment variables you created in a previous step.
+
[source,terminal]
----
$ export OFFER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".offer')
----
+
[source,terminal]
----
$ export SKU=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".sku')
----
+
[source,terminal]
----
$ export VERSION=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".version')
----

.. Obtain the {op-system} version by running the following command:
+
[source,terminal]
----
$ echo $VERSION
----
+
.Example output
[source,terminal]
----
9.6.20251015
----
+
Make note of the {op-system} version for later use.

.. Set an environment variable with the type of your image by running the following command:
+
[source,terminal]
----
$ export IMAGE_TYPE=<image_type>
----
+
Replace `<image_type>` with one of the following values based on the variant of your image:
+
--
* For the `no-purchase-plan` variant, use `MarketplaceNoPlan`.
* For all other variants, use `MarketplaceWithPlan`.
--

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus21   1         1         1       1           135m
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus22   1         1         1       1           135m
ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus23   1         1         1       1           135m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
  -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"publisher":"'${PUBLISHER}'","offer":"'${OFFER}'","sku":"'${SKU}'","version":"'${VERSION}'","resourceID":"","type":"'${IMAGE_TYPE}'"}}}}}}}'
----
+
`PUBLISHER`, `OFFER`, `SKU`, `VERSION`, and `IMAGE_TYPE` are environment variables you created in previous steps.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-ostree.x86_64.ociarchive",
    "version": "9.6.20251015"
}
----
where:

`version`:: Specifies the boot image version.

. Verify that the boot image is the same the {op-system} version as the image you noted in a previous step by running the following command:
+
[source,terminal]
----
$ echo $VERSION
----
+
.Example output
[source,terminal]
----
9.6.20251015
----

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-aws_{context}"]
= Manually updating the boot image on an {aws-short} cluster

[role="_abstract"]
You can manually update the boot image for your {aws-first} cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct Amazon Machine Image (AMI) to use as the new boot image, and modify your compute machine sets to use that image.

The process differs for clusters that use a default {op-system-first} image and clusters that use a custom {op-system} image from the {aws-short} Marketplace. The following procedure helps determine which type of image you use.

[NOTE]
====
For clusters that use a default {op-system} image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have installed the {oc-first}.

* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".

* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".

* You have installed the {aws-short} CLI.

* You configured an AWS account to host the cluster. For information, see "Configuring an AWS account".

* For a cluster that uses a default {op-system} image, ensure you have met the following additional prerequisites:

** You have downloaded the latest version of the OpenShift Container Platform installation program from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

** For a cluster that uses a default {op-system} image, you have installed the `jq` program.

.Procedure

. Determine if your cluster uses a default {op-system} image or a custom {op-system} image from the {aws-short} Marketplace image:

.. Obtain the current {aws-short} region where the cluster is installed and set the value in an environment variable by running the following command:
+
[source,terminal]
----
$ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}')
----

.. Obtain the current Amazon Machine Image (AMI) ID for your region and set the value in an environment variable by running the following command:
+
[source,terminal]
----
$ export CURRENT_AMI=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.ami.id}')
----

.. Obtain the product ID for your AMI and set the value in an environment variable by running the following command:
+
[source,terminal]
----
$ export PRODUCT_ID=$(aws ec2 describe-images --image-ids "$CURRENT_AMI" --region "$REGION" \
  --query 'Images[0].Name' --output text | \
  grep -oE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
----
+
`CURRENT_AMI` and `REGION` are environment variables you created in previous steps.

.. Display the contents of the `PRODUCT_ID` environment variable by running the following command:
+
[source,terminal]
----
$ echo $PRODUCT_ID
----
+
* If the output for the `PRODUCT_ID` environment variable is empty, as shown in the following example, your cluster uses a standard OpenShift Container Platform image.
+
.Example with empty output
[source,terminal]
----

----
+
* If the output for the `PRODUCT_ID` environment variable is not empty, as shown in the following example, your cluster uses an {aws-short} Marketplace image.
+
.Example with non-empty output
[source,terminal]
----
59ead7de-2540-4653-a8b0-fa7926d5c845
----
+
* If the command returns an error, and you are unable to determine your cluster variant, contact Red Hat Support. If Red Hat Support determines that your cluster uses an {aws-short} Marketplace image, you can set the `PRODUCT_ID` environment variable with the appropriate product ID from the following table.
+
[source,terminal]
----
$ export PRODUCT_ID=<Product_ID_from_table>
----
+
[cols="1,1",options="header"]
|===
| Variant | Product ID
| OpenShift Container Platform on x86 - NA| `59ead7de-2540-4653-a8b0-fa7926d5c845`
| {oke} on x86 - NA| `963b36c3-de6f-48ed-b802-2b38b2a2cdeb`
| {opp} on x86 - NA| `f5da01a6-d046-487c-9072-42fe53b1cad4`
| OpenShift Container Platform on ARM - NA| `abc249f8-7440-45f7-a4b1-c026baff64c1`
| {oke} on ARM - NA| `d2d3ebcd-c1ca-43d8-bf0a-530433200f35`
| {opp} on ARM - NA| `be6d3e94-c8dc-4a3e-9218-4b449b11f06f`
| OpenShift Container Platform on x86 - EU, ME and Africa| `962791c7-3ae5-46d1-ba62-c7a5ebac54fd`
| {oke} on x86 - EU, ME and Africa| `7026c8d7-392c-4010-b93c-f93f7bc5495f`
| {opp} on x86 - EU, ME and Africa| `628c9df3-0254-4f91-bc1f-8619d1b8eaa8`
|===

. Determine the AMI for the new boot image by using one of the following steps, depending upon the type of image used in your cluster:

* For a cluster that uses a default {op-system} image, perform the following steps:
+
.. Set an environment variable with your cluster architecture by running the following command:
+
[source,terminal]
----
$ export ARCH=<architecture_type>
----
+
Replace `<architecture_type>` with one of the following values:
+
--
* Specify `aarch64` for the AArch64 or ARM64 architecture.
* Specify `ppc64le` for the {ibm-power-name} (ppc64le) architecture.
* Specify `s390x` for the {ibm-z-name} and {ibm-linuxone-name} (s390x) architecture.
* Specify `x86_64` for the x86_64 or AMD64 architecture.
--
+
You can find the architecture as a label in any `MachineSet` object.
+
.Example machine set with an architecture label
[source,terminal]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
# ...
----

.. Obtain the AMI for the new boot image and set an environment variable with the AMI by running the following command:
+
[source,terminal]
----
$ export AMI_ID=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".image")
----
+
`ARCH` and `REGION` are environment variables you created in previous steps.

.. View the {op-system} version of the new boot image by running the following command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".release"
----
+
.Example output
[source,terminal]
----
9.6.20251212-1
----
+
Make note of the {op-system} version for later use.

* For a cluster that uses a custom {op-system} image, perform the following steps:
+
.. Obtain a list of valid AMI images by running the following command:
+
[source,terminal]
----
$ aws ec2 describe-images --region "${REGION}" --filters "Name=name,Values=*${PRODUCT_ID}*" \
  --query 'reverse(sort_by(Images, &CreationDate))[].[CreationDate,ImageId,Name]' --output table
----
+
`REGION` and `PRODUCT_ID` are environment variables you created in previous steps.
+
This command returns the AMIs ordered by creation date, with the latest images first. The {op-system} version of each AMI is contained in the AMI name. Choose the latest image version available.
+
Make note of the {op-system-first} version for later use.

.. Set an environment variable with the AMI of the new boot image by running the following command:
+
[source,terminal]
----
$ export AMI_ID=<ami-value>
----

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"ami":{"id":"'${AMI_ID}'"}}}}}}}'
----
+
Replace `<machineset_name>` with the name of your machine set.
+
`AMI_ID` is the environment variable you created in a previous step.

. If boot image skew enforcement in your cluster is set to the manual mode, update the boot image version in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version."

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`version`:: Specifies the boot image version.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-gcp_{context}"]
= Manually updating the boot image on an {gcp-short} cluster

[role="_abstract"]
You can manually update the boot image for your {gcp-first} cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your machine sets to use that image.

The process differs for clusters that use a default {op-system-first} image, clusters that use a custom {op-system-first} image from the {gcp-short} Marketplace, and user-provisioned infrastructure clusters. The following procedure helps determine which type of cluster you have.

For user-provisioned infrastructure {gcp-short} clusters, which typically have no Machine API compute machine sets, you can provision new nodes based on the new boot image by updating the underlying {gcp-short} infrastructure with the new boot image, such as instance templates, Deployment Manager templates, or Terraform configuration. For more information, see "Creating additional worker machines in {gcp-short}".

[NOTE]
====
For clusters that use a default {op-system-first} image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have installed the {oc-first}.

* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".

* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".

* For a cluster that uses a default {op-system} image, ensure that your cluster meets the following additional prerequisites:

** You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

** You have installed the `jq` program.

* For a user-provisioned infrastructure cluster, ensure that your cluster meets the following additional prerequisites:

** You have downloaded the latest version of the OpenShift Container Platform installation program from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

** You have installed the {gcp-short} CLI.

** You have created a {gcp-short} service account.

.Procedure

. Determine which image in the machine set is the boot image and set the value in an environment variable:

.. Set the boot image value in an environment variable by running the following command:
+
[source,terminal]
----
$ export BOOT_DISK_INDEX=$(oc get machineset -n openshift-machine-api -o json | \
  jq '.items[0].spec.template.spec.providerSpec.value.disks | map(.boot == true) | index(true)')
----

.. Display the contents of the `BOOT_DISK_INDEX` environment variable by running the following command:
+
[source,terminal]
----
$ echo $BOOT_DISK_INDEX
----
+
.Example output
[source,terminal]
----
0
----
+
If the output for the `BOOT_DISK_INDEX` environment variable is `null`, none of the disks in the machine set has the `boot` field explicitly set. In this case, the boot disk is typically the first disk.
+
.Example null output
[source,terminal]
----
null
----

.. If the  `BOOT_DISK_INDEX` output is `null`, set the boot image to the first image by running the following command:
+
[source,terminal]
----
$ export BOOT_DISK_INDEX=0
----

. Determine if your cluster uses a default {op-system} image or a GCP Marketplace {op-system} image from the {gcp-short} Marketplace, or is a user-provisioned infrastructure cluster:

.. Obtain the name of the current boot image and set the name as an environment variable by running the following command:
+
[source,terminal]
----
$ export CURRENT_IMAGE=$(oc get machineset -n openshift-machine-api -o json | \
  jq -r ".items[0].spec.template.spec.providerSpec.value.disks[${BOOT_DISK_INDEX}].image")
----
+
`BOOT_DISK_INDEX` is the environment variable you created in a previous step.

.. View the name of the image by running the following command:
+
[source,terminal]
----
$ echo $CURRENT_IMAGE
----
+
.Example output
[source,terminal]
----
projects/rhcos-cloud/global/images/rhcos-416-94-202510081640-0-gcp-x86-64
----

.. Compare the prefix of the image name to the entries in the following table:
+
[cols="1,1",options="header"]
|===
| Current image prefix | Variant
| `projects/rhcos-cloud/global/images/` | Default
| `projects/redhat-marketplace-public/global/images/` | GCP Marketplace {op-system} image
| No machine set present/custom prefix | User-provisioned infrastructure
|===
+
Default {op-system} clusters use images from the `rhcos-cloud` project in the `rhcos-<version>-<platform>-<arch>` format.
+
GCP Marketplace {op-system} clusters use images from the `redhat-marketplace-public` project in the `redhat-coreos-<offering>-<version>-<arch>-<date>` format.
+
[NOTE]
====
The following images are the latest {gcp-short} Marketplace images for the OpenShift Container Platform:

OpenShift Container Platform:: `redhat-coreos-ocp-413-x86-64-202305021736`
{opp}:: `redhat-coreos-opp-413-x86-64-202305021736`
{oke}:: `redhat-coreos-oke-413-x86-64-202305021736`

Red Hat has not published Marketplace images for OpenShift Container Platform later than these OpenShift Container Platform 4.13 images. If the current boot image in your cluster matches one of the listed images, no further action is necessary.
====
. Obtain the name of the new boot image by using one of the following steps, depending upon your cluster:

* For a cluster that uses a default {op-system} image, perform the following steps:
+
.. Set an environment variable with your cluster architecture by running the following command:
+
[source,terminal]
----
$ export ARCH=<architecture_type>
----
+
Replace `<architecture_type>` with one of the following values:
+
--
* Specify `aarch64` for the AArch64 or ARM64 architecture.
* Specify `ppc64le` for the {ibm-power-name} (ppc64le) architecture.
* Specify `s390x` for the {ibm-z-name} and {ibm-linuxone-name} (s390x) architecture.
* Specify `x86_64` for the x86_64 or AMD64 architecture.
--
+
You can find the architecture as a label in any `MachineSet` object.
+
.Example machine set with an architecture label
[source,terminal]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
# ...
----

.. Set an environment variable with the name of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
----
+
`ARCH` is the environment variable you created in a previous step.

.. Set an environment variable with the {gcp-short} project of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
----
+
`ARCH` is the environment variable you created in a previous step.

.. View the {op-system-first} version of the new boot image by running the following command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.release"
----
+
.Example output
[source,terminal]
----
9.6.20251212-1
----
+
Make note of the {op-system} version for later use.

* For a cluster that uses a GCP Marketplace {op-system} image that is earlier than the 4.13 images listed above, perform the following steps:

.. Set an environment variable with the name of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_IMAGE=<image_name>
----
+
Replace `<image_name>` with one of the following values:
+
--
* Specify `redhat-coreos-ocp-413-x86-64-202305021736` for an OpenShift Container Platform cluster.
* Specify `redhat-coreos-opp-413-x86-64-202305021736` for an {opp} cluster.
* Specify `redhat-coreos-oke-413-x86-64-202305021736` for an {oke} cluster.
--

.. Set an environment variable with the {gcp-short} project of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_PROJECT=redhat-marketplace-public
----

* For a user-provisioned infrastructure cluster, perform the following steps:

.. Set an environment variable with your cluster architecture by running the following command:
+
[source,terminal]
----
$ export ARCH=<architecture_type>
----
+
Replace `<architecture_type>` with one of the following values:
+
--
* Specify `aarch64` for the AArch64 or ARM64 architecture.
* Specify `ppc64le` for the {ibm-power-name} (ppc64le) architecture.
* Specify `s390x` for the {ibm-z-name} and {ibm-linuxone-name} (s390x) architecture.
* Specify `x86_64` for the x86_64 or AMD64 architecture.
--

.. Set an environment variable with the name of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
----
+
`ARCH` is the environment variable you created in a previous step.

.. Set an environment variable with the {gcp-short} project of the new boot image in your cluster by running the following command:
+
[source,terminal]
----
$ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
----
+
`ARCH` is the environment variable you created in a previous step.
+
If the default {op-system} image is not accessible in your environment, for example in a restricted or disconnected environment, you could download the new boot image tar file and upload the file as a custom image to your own {gcp-short} project before updating your {gcp-short} instance templates.
+
Update your {gcp-short} instance template(s) to reference the new image, then create new instances from the updated template. The exact steps depend on how your infrastructure was provisioned. For more information, see "Creating additional worker machines in {gcp-short}".
+
After creating the new instances, you can proceed to the verification steps, unless your user-provisioned infrastructure cluster has any Machine API machine sets, such as for Day-2 scaling. You can update those machine sets as described in the following steps.
. Set an environment variable with the name of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_IMAGE=<osd_image_name>
----
+
Replace `osd_image_name` with the name of the new boot image.
+
[NOTE]
====
The `redhat-marketplace-public` project does not grant image list permissions to external users. You must obtain the {product-dedicated} image name Red Hat from support or release documentation.
====

. Set an environment variable with the project of the new boot image by running the following command:
+
[source,terminal]
----
$ export GCP_PROJECT=redhat-marketplace-public
----

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
ci-ln-xw7zmyt-72292-x7nqv-worker-b   1         1         1       1           53m
ci-ln-xw7zmyt-72292-x7nqv-worker-c   1         1         1       1           53m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
  -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/disks/'${BOOT_DISK_INDEX}'/image", "value": "projects/'${GCP_PROJECT}'/global/images/'${GCP_IMAGE}'"}]'
----
+
Replace `<machineset_name>` with the name of your machine set.
+
`BOOT_DISK_INDEX`, `GCP_PROJECT`, and `GCP_IMAGE` are environment variables you created in previous steps.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`version`:: Specifies the boot image version.

. Verify that the boot image is the same the {op-system} version as the image you noted in a previous step by running the following command:
+
[source,terminal]
----
$ echo $GCP_IMAGE
----
+
`RHCOS_URL` is the environment variable you created in a previous step.
+
.Example output
[source,terminal]
----
https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
----

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-ibm-bare-metal_{context}"]
= Manually updating the boot image on a bare-metal cluster

[role="_abstract"]
For a bare-metal cluster that was installed with OpenShift Container Platform version 4.9 or earlier, you need to change how the cluster provisions new nodes in order to update the boot image used with those nodes. Using an up-to-date boot image ensures that any new nodes can scale up properly.

[NOTE]
====
The standard boot image management feature is not supported for bare-metal clusters.
====

If your bare-metal cluster was installed with OpenShift Container Platform version 4.10 or later, boot images are kept current by the Cluster Version Operator (CVO) and are not at risk of boot image skew. Skew enforcement is disabled for the cluster by default. No further action on your part is required to maintain the boot image versioning.

If your bare-metal cluster was installed with OpenShift Container Platform version 4.9 or earlier, the cluster is using the legacy qcow2-based provisioning method. Boot images in these clusters are not managed by the CVO and could be significantly out of date. Follow the steps below to migrate the cluster to use the `machine-os-images` provisioning method, which was introduced in OpenShift Container Platform 4.10. This migration ensures that the cluster always uses the release version as the boot image when a scale-up is taking place.

Use the following procedure to enable the `install_coreos` deployment method and disable the qcow2 image cache. With these changes, the Cluster Baremetal Operator (CBO) will use the `machine-os-images` container from the release payload for new node provisioning. The cluster will have no skew risk, the same as a cluster at version 4.10 or later. Skew enforcement is automatically disabled after the migration is complete.

[NOTE]
====
Boot image updates are not required for Agent-based Installer clusters. The boot image for Agent-based Installer nodes is generated from the current release payload through the `oc adm node-image create` command and does not have skew issues.
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have the {oc-first} installed.

* A new physical host must be registered and in the `available` state and an associated `BareMetalHost` object must be present in the `openshift-machine-api` namespace so that you can scale a new machine to verify the procedure.

.Procedure

. Check whether your cluster is using the legacy boot image provisioning path by running the following command:
+
[source,terminal]
----
$ oc get provisioning provisioning-configuration \
  -o jsonpath='{.spec.provisioningOSDownloadURL}'
----
+
* If the output is non-empty, your cluster was installed with OpenShift Container Platform version 4.9 or earlier. Boot images are not managed by the Cluster Version Operator (CVO) and could be significantly out of date. Follow the steps in this procedure to migrate to the current provisioning path.
+
* If the output is empty, your cluster was installed with OpenShift Container Platform version 4.10 or later. Boot images are kept current by the Cluster Version Operator (CVO) and are not at risk of skew. Skew enforcement is disabled for this cluster. No further action on your part is required to maintain the boot image versioning.

. Clear the legacy image fields and enable the `install_coreos` deployment method:

.. Migrate each machine set to the `machine-os-images` provisioning path by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge \
  -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"customDeploy":{"method":"install_coreos"},"image":{"url":"","checksum":""}}}}}}}'
----
+
Replace `<machineset_name>` with the name of your machine set.

.. Clear the legacy download URL by running the following command:
+
[source,terminal]
----
$ oc patch provisioning provisioning-configuration --type=merge -p '{"spec":{"provisioningOSDownloadURL":""}}'
----
+
This process migrates the cluster to the `machine-os-images` provisioning method, which ensures that the latest boot image is used for scaling nodes.

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`version`:: Specifies the boot image version.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-ibm-cloud_{context}"]
= Manually updating the boot image on an {ibm-cloud-name} cluster

[role="_abstract"]
For an {ibm-cloud-title} cluster, you can manually update the boot image for the compute nodes in your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

[NOTE]
====
The standard boot image management feature is not supported for {ibm-cloud-title} clusters.
====

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain {ibm-cloud-title} authentication credentials, download a boot image, upload that image to the {ibm-cloud-title} image service, and modify your compute machine sets to use the new boot image.

This procedure uses the default {ibm-cloud-title} Cloud Object Storage (COS) bucket in your cluster, which was created during cluster installation. Each COS bucket has a specific Cloud Resource Name (CRN), which the {ibm-cloud-title} CLI uses the to select the correct COS bucket. The following procedure shows how to obtain the CRN for the default COS bucket. For more information on the CRN, see Cloud Resource Names in the {ibm-cloud-title} documentation.

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

* You have the {oc-first} installed.

* You have the {ibm-cloud-title} CLI installed.

* You have installed the {ibm-cloud-title} Virtual Private Cloud (VPC) CLI plugin.

* You have installed the {ibm-cloud-title} Object Storage plugin.

.Procedure

. Obtain the resource group and region from the `infrastructure` object and set the values in an environment variable by running the following commands:
+
[source,terminal]
----
$ export RESOURCE_GROUP=$(oc get infrastructure cluster -o jsonpath='{.status.infrastructureName}')
----
+
[source,terminal]
----
$ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.ibmcloud.location}')
----

. Generate an {ibm-cloud-title} API key and log in to your {ibm-cloud-title}:

.. Follow the instructions in Creating your {ibm-cloud-title} API key in the {ibm-cloud-title} documentation to generate the API key.
+
To ensure that the key has the appropriate permissions, you must use the same {ibm-cloud-title} account used to create the OpenShift Container Platform cluster when generating the key.

.. Set the API key in an environment variable by running the following command:
+
[source,terminal]
----
$ export IBM_API_KEY=<Your_IBM_Cloud_API_Key>
----

.. Log in to your {ibm-cloud-title} by running the following command:
+
[source,terminal]
----
$ ibmcloud login --apikey ${IBM_API_KEY} -r ${REGION} -g ${RESOURCE_GROUP}
----
+
`IBM_API_KEY`, `REGION`, and `RESOURCE_GROUP` are environment variables you created in previous steps.
+
.Example output
[source,terminal]
----
API endpoint: https://cloud.ibm.com
Authenticating...
Retrieving API key token...
OK

Targeted account OpenShift-QE (xxxxxxxxxxxxxxxx) <-> xxxxxx

Targeted resource group xxxxxxx-ibm3h-9pbgg

Targeted region eu-gb

API endpoint:     https://cloud.ibm.com
Region:           eu-gb
User:             xxxxx
Account:          xxxxx
Resource group:   xxxxx
----

. Obtain the URL of the {op-system} image to use as the boot image and set the location in an environment variable by running one of the following commands, based on your cluster architecture:
+
* Linux (x86_64, amd64):
+
[source,terminal]
----
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
----
+
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x):
+
[source,terminal]
----
export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.s390x.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
----

. Obtain the boot image:

.. Download the image by using the following command:
+
[source,terminal]
----
$ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
----
+
`RHCOS_URL` is the environment variable you created in a previous step.

.. Decompress the downloaded image by running the following command:
+
[source,terminal]
----
$ gunzip /tmp/rhcos-new.qcow2.gz
----

. Upload the boot image to the default {ibm-cloud-title} Cloud Object Storage (COS) bucket:

.. Obtain the CRN for your COS bucket and set the CRN in an environment variable by running the following command:
+
[source,terminal]
----
$ export COS_CRN=$(ibmcloud resource service-instance "${RESOURCE_GROUP}-cos" --output json | jq -r '.[0].crn')
----

.. Optional: Check that the CRN is correct by running the following command:
+
[source,terminal]
----
$ echo ${COS_CRN}
----

.. Configure the default COS bucket with the CRN by running the following command:
+
[source,terminal]
----
$ ibmcloud cos config crn --crn "${COS_CRN}"
----
+
`COS_CRN` is the environment variable you created in a previous step.

.. Upload the boot image to the COS bucket by running the following command:
+
[source,terminal]
----
$ ibmcloud cos object-put --bucket "${RESOURCE_GROUP}-vsi-image" --key "rhcos-new.qcow2" --body /tmp/rhcos-new.qcow2 --region "${REGION}"
----
+
`RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps.

.. Optional: Check that image was uploaded to the COS bucket by running the following command:
+
[source,terminal]
----
$ ibmcloud cos objects --bucket "${RESOURCE_GROUP}-vsi-image" --region "${REGION}"
----
+
`RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps.
+
.Example output
[source,terminal]
----
OK
Found 2 objects in bucket 'xxxxxx-ibm3h-9pbgg-vsi-image':
----

.. Set an environment variable to create a descriptive name for your boot image:
+
[source,terminal]
----
$ export IMAGE_NAME="<descriptive_image_name>"
----
+
Setting a descriptive name for your boot image, such as using the {op-system-first} version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.

.. Create a custom image for your {ibm-cloud-title} Virtual Private Cloud (VPC) from the uploaded boot image by running one of the following commands, based on your cluster architecture:
+
--
* Linux (x86_64, amd64):
+
[source,terminal]
----
$ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name rhel-coreos-stable-amd64 --resource-group-name "${RESOURCE_GROUP}"
----
+
You must set  the `--os-name` argument to `rhel-coreos-stable-amd64` as shown. This parameter configures several {op-system-first} default values that are required.
+
`RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps.
+
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x):
+
[source,terminal]
----
$ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name red-8-s390x-byol --resource-group-name "${RESOURCE_GROUP}"
----
+
You must set  the `--os-name` argument to `red-8-s390x-byol` as shown. This parameter configures several {op-system-first} default values that are required.
+
`RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps.
--

.. Optional: Observe the new image being uploaded until its status changes from `pending` to `available`.
+
[source,terminal]
----
$ watch ibmcloud is image "${RESOURCE_GROUP}-${IMAGE_NAME}"
----
+
`RESOURCE_GROUP` and `IMAGE_NAME` are environment variables you created in previous steps.

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
  -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${RESOURCE_GROUP}'-'${IMAGE_NAME}'"}}}}}}'
----
+
Replace `<machineset_name>` with the name of your machine set.
+
`IMAGE_NAME` is the environment variable you created in a previous step.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:
+
--
.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command.
+
[source,terminal]
----
$ oc get nodes
----

.. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`<version>`:: Specifies the boot image version.
--
+
After you migrate all machine sets to the new boot image, the old boot image is no longer needed. You can remove the old boot image from your COS bucket.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-nutanix_{context}"]
= Manually updating the boot image on a Nutanix cluster

[role="_abstract"]
You can manually update the boot image for your Nutanix cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

[NOTE]
====
The standard boot image management feature is not supported for Nutanix clusters.
====

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain Nutanix authentication credentials, download a boot image, upload that image to the Nutanix Prism Central, and modify your compute machine sets to use the new boot image.

This procedure requires Nutanix authentication credentials, which you need to access Prism Central. If you need to recover your credentials, you can get them from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure.

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

* You have installed the {oc-first}.

* You have installed the `jq` program.

.Procedure

. If you need to recover your Nutanix authentication credentials, perform the following steps:

.. Obtain the name of the secret that contains your credentials by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api -o yaml | grep credentialsSecret -A 1
----
+
.Example output
[source,terminal]
----
    credentialsSecret:
      name: nutanix-credentials
----

.. Decrypt the secret by running the following command:
+
[source,terminal]
----
$ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.credentials}' | base64 -d
----
+
Replace `<secret_name>` with the name of the secret, which you obtained in the previous step.
+
.Example output
[source,terminal]
----
[{"type":"basic_auth","data":{"prismCentral":{"username":"","password":""},"prismElements":null}}]
----

. Set an environment variable for the Nutanix username by running the following command:
+
[source,terminal]
----
$ export USER="<username>"
----

. Set an environment variable for the Nutanix password by running the following command:
+
[source,terminal]
----
$ export PASS="<password>"
----

. If you need to recover your IP address for Prism Central, run the following command:
+
[source,terminal]
----
$ oc get configmap cloud-provider-config -n openshift-config -o jsonpath='{.data.config}' | grep prismCentral -A 8
----
+
.Example output
[source,terminal]
----
    "prismCentral": {
        "address": "",
        "port": 9440,
        "credentialRef": {
            "kind": "Secret",
            "name": "nutanix-credentials",
            "namespace": "openshift-cloud-controller-manager"
        }
    },
----
where:

`prismCentral.address`:: Specifies the Prism Central IP address.

. Set an environment variables for the Prism Central IP address by running the following command:
+
[source,terminal]
----
$ export PC_IP="<prism_central_ip_address>"
----

. Obtain the boot image and upload the image to Prism Central:

.. Obtain the URL of the {op-system} image you want to use as the boot image and set the location in an environment variable by running the following command:
+
[source,terminal]
----
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.nutanix.formats.qcow2.disk.location')
----

.. Set an environment variable to create a descriptive name for your boot image in Prism Central by running the following command:
+
[source,terminal]
----
$ export IMAGE_NAME="<descriptive_image_name>"
----
+
Setting a descriptive name for your boot image in Prism Central, such as using the {op-system-first} version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.
+
.Example command
[source,terminal]
----
$ export IMAGE_NAME="rhcos-9.6-boot-image"
----

.. Upload the image to Prism Central by running the following command:
+
[source,terminal]
----
$ curl -k -u "$USER:$PASS" \
  -X POST "https://$PC_IP:9440/api/nutanix/v3/images" \
  -H "Content-Type: application/json" \
  -d '{
    "spec": {
      "name": "'"$IMAGE_NAME"'",
      "resources": {
        "image_type": "DISK_IMAGE",
        "source_uri": "'"$RHCOS_URL"'"
      }
    },
    "metadata": {
      "kind": "image"
    }
  }'
----
+
`USER`,`PASS`, `IMAGE_NAME`, and `RHCOS_URL` are environment variables you created in previous steps.

.. Optional: Verify that the image is uploaded by running the following command:
+
[source,terminal]
----
$ curl -k -u "$USER:$PASS" \
  -X POST "https://$PC_IP:9440/api/nutanix/v3/images/list" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "image",
    "filter": "name=='"$IMAGE_NAME"'"
  }'
----
+
.Example output
[source,terminal]
----
{
  "name": "<image-name>",
  "state": "COMPLETE"
}
----

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"type":"name","name":"'${IMAGE_NAME}'"}}}}}}}'
----
+
Replace `<machineset_name>` with the name of your machine set.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`version`:: Specifies the boot image version.

. Verify that the boot image is the same version as the image you uploaded in a previous step by running the following command:
+
[source,terminal]
----
$ echo ${RHCOS_URL}
----
+
.Example output
[source,terminal]
----
https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
----
+
After you migrate all machine sets to the new boot image, you can remove the old boot image from Prism Central.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-openstack_{context}"]
= Manually updating the boot image on an {rh-openstack} cluster

[role="_abstract"]
For a {rh-openstack-first} cluster, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

[NOTE]
====
The standard boot image management feature is not supported for {rh-openstack} clusters.
====

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain {rh-openstack} authentication credentials, download a boot image, upload that image to the {rh-openstack} image service (Glance), and modify your worker machine sets to use the new boot image.

This procedure requires the `clouds.yaml` file, which is needed by the OpenStackClient CLI to connect to your {rh-openstack} cloud. If you need to re-create this file, you can get the {rh-openstack} credentials from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure.

[NOTE]
====
Updating control plane machine sets is not supported in {rh-openstack}.
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the Prerequisites section of OpenShift Container Platform Boot Image Updates.

* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

* You have installed the {oc-first} installed.

* You have installed the OpenStackClient ({op-system} documentation).

* You have installed the `jq` program.

.Procedure

. If you need to re-create the `clouds.yaml` file, perform the following steps:

.. Obtain the name of the secret that contains your credentials by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api -o yaml | grep cloudsSecret -A 1
----
+
.Example output
[source,terminal]
----
cloudsSecret:
  name: openstack-cloud-credentials
----

.. Decrypt the secret and add the contents to the `clouds.yaml` file by running the following command:
+
[source,terminal]
----
$ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.clouds\.yaml}' | base64 -d > <file_path>/clouds.yaml
----
+
Replace `<secret_name>` with the name of the secret, which you obtained in the previous step, and `<file_path>` with the path to the `clouds.yaml` file.

.. Optional: Verify the contents of the `clouds.yaml` file by running the following command:
+
[source,terminal]
----
$ cat <file_path>/clouds.yaml
----
+
Replace `<file_path>` with the path to the `clouds.yaml` file.
+
.Example output
[source,terminal]
----
clouds:
  openstack:
    auth:
      auth_url: https://your-openstack-url:13000
      username: "your-username"
      password: "your-password"
      project_name: "your-project"
      user_domain_name: "Default"
      project_domain_name: "Default"
----

. Set an environment variable for the location of the `clouds.yaml` file by running the following command:
+
[source,terminal]
----
$ export OS_CLIENT_CONFIG_FILE=<file_path>/clouds.yaml
----
+
Replace `<file_path>` with the path to the `clouds.yaml` file.
+
The OpenStackClient CLI uses this environment variable to locate the `clouds.yaml` file.

. Obtain the name of your {rh-openstack} cloud from the default compute machine set and set the name in an environment variable by running the following command:
+
[source,terminal]
----
$ export CLOUD_NAME=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.cloudName}')
----

. Obtain the URL of the {op-system} image you want to use as the boot image and set the location in an environment variable by running one of the following commands, based on cluster architecture:
+
* Linux (x86_64, amd64):
+
[source,terminal]
----
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.x86_64.artifacts.openstack.formats."qcow2.gz".disk.location')
----
+
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x):
+
[source,terminal]
----
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.s390x.artifacts.openstack.formats."qcow2.gz".disk.location')
----
+
* Linux on ARM (aarch64, arm64)
+
[source,terminal]
----
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
  '.architectures.aarch64.artifacts.openstack.formats."qcow2.gz".disk.location')
----

. Obtain the boot image and upload the image to the {rh-openstack} image service (Glance):

.. Download the image by using the following command:
+
[source,terminal]
----
$ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
----
+
`RHCOS_URL` is the URL environment variables you created in a previous step.

.. Decompress the downloaded image by using the following command:
+
[source,terminal]
----
$ gunzip <file_path>/rhcos-new.qcow2.gz
----
+
Replace `<file_path>` with the path to the location for the image.

.. Set an environment variable to create a descriptive name for your boot image in Glance by running the following command:
+
[source,terminal]
----
$ export IMAGE_NAME="<descriptive_image_name>"
----
+
Setting a descriptive name for your boot image, such as using the {op-system-first} version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.
+
.Example command
[source,terminal]
----
$ export IMAGE_NAME="rhcos 9.6 boot image"
----

.. Upload the image to Glance by using the following command:
+
[source,terminal]
----
$ openstack --os-cloud "${CLOUD_NAME}" image create "${IMAGE_NAME}" \
  --disk-format qcow2 \
  --container-format bare \
  --file <file_path>/rhcos-new.qcow2 \
  --property os_type=linux \
  --property os_distro=rhcos
----
+
Replace `<file_path>` with the path to the location for the image.
+
`CLOUD_NAME` and `IMAGE_NAME` are environment variables you created in previous steps.
+
It might take several minutes for the image to upload. When the upload is complete, details on the image displays, similar to the following example:
+
.Example output
[source,terminal]
----
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field            | Value                                                                                                                                                                               |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| checksum         | 469fa549f706617ff15b41bd2a919679                                                                                                                                                    |
# ...                                                                                                                                                         |
| disk_format      | qcow2                                                                                                                                                                               |
# ...
| name             | rhcos 9.6 boot image
----

.. Optional: Verify that the image has uploaded and is in active state by running the following command:
+
[source,terminal]
----
$ openstack --os-cloud "${CLOUD_NAME}" image show "${IMAGE_NAME}" -f json | jq '{name: .name, status: .status}'
----
+
.Example output
[source,terminal]
----
{
  "name": "rhcos 9.6 boot image",
  "status": "active"
}
----

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p \
  '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${IMAGE_NAME}'"}}}}}}'
----
+
Replace `<machineset_name>` with the name of your machine set.
+
`IMAGE_NAME` is the environment variable you created in a previous step.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:
+
.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:
+
--
`version`:: Specifies the boot image version.
--
+
After you migrate all machine sets to the new boot image, you can remove the old boot image from Glance.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-vsphere_{context}"]
= Manually updating the boot image on a {vmw-short} cluster

[role="_abstract"]
You can manually update the boot image for your {vmw-first} cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

{vmw-short} boot images use a template that you create by uploading a {op-system-first} OVA image to the {vmw-short} vCenter. The template image is used by all machine sets as the boot image. Use the following procedure to identify the correct boot image to use as the new boot image, create the template from the image in vCenter, and modify your compute machine sets to use that template image.

[NOTE]
====
For clusters that use a default {op-system} image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".
====

.Prerequisites

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the OpenShift Container Platform Boot Image Updates knowledgebase article.

* You have installed the {oc-first}.

* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".

* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".

* You have downloaded the latest version of the OpenShift Container Platform installation program from the {cluster-manager-url}. For more information, see "Obtaining the installation program."

// The vSphere steps are copied from installation-vsphere-machines.adoc and tweaked based on the KB; last two steps from KB

.Procedure

. Obtain the latest boot image to use as the new boot image:

.. Obtain the name of the new boot image by running the following command:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq '.architectures.x86_64.artifacts.vmware'
----
+
.Example output
[source,terminal]
----
{
  "release": "9.6.20251023-0",
  "formats": {
    "ova": {
      "disk": {
        "location": "https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251023-0/x86_64/rhcos-9.6.20251023-0-vmware.x86_64.ova",
        "sha256": "14fa549bb83b2e730de22312419b503bc1ce85adf72269582f0af60e366d87ff"
      }
    }
  }
}
----

.. Use the URL in the `location` field to download the image.

. In the vSphere Client, create a template for the OVA image:
.. From the *Hosts and Clusters* tab, right-click your cluster name and select *Deploy OVF Template*.
.. On the *Select an OVF* tab, specify the name of the {op-system} OVA file that you downloaded.
.. On the *Select a name and folder* tab, set a *Virtual machine name* for your template, such as using the {op-system} version number in the image name. Click the name of your vSphere cluster and select the folder.
.. On the *Select a compute resource* tab, click the name of your vSphere cluster.
.. On the *Select storage* tab, configure the storage options for your VM.
*** Select *Thin Provision* or *Thick Provision*, based on your storage preferences.
*** Select the data store that you specified in your `install-config.yaml` file.
*** If you want to encrypt your virtual machines, select *Encrypt this virtual machine*. See "Requirements for encrypting virtual machines" for more information.
.. On the *Select network* tab, specify the network that you configured for the cluster, if available.
.. When creating the OVF template, do not specify values on the *Customize template* tab or configure the template any further.
.. On the *Ready to complete* tab, verify your settings and click *Finish*.
+
The vSphere Client uploads the boot image to create the OVF template. This can take a few minutes depending on network speeds. You can keep track of this process in the task tab under _Deploy OVF template_.
.. After the upload is complete, click the new virtual machine and click *Template* -> *Convert to template* -> *Yes*.
+
You now have a VM template based on the new boot image, which you can use to update the machine set objects.

. Update each of your compute machine sets to include the new boot image:

.. Obtain the name of your machine sets for use in the following step by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
----

.. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:
+
[source,terminal]
----
$ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
  -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/template", "value": "ci-ln-6vjqx8t-c1627-bwxkr-rhcos-generated-region-generated-zone"}]'
----
+
Replace `<machineset_name>` with the name of your machine set.

. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

.Verification

. Scale up a machine set to check that the new node is using the new boot image:

.. Increase the machine set replicas by one to trigger a new machine by running the following command:
+
[source,terminal]
----
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
----
where:

`<count>`:: Specifies the total number of replicas, including any existing replicas, that you want for this machine set.
`<machineset_name>`:: Specifies the name of the machine set to scale.

.. Optional: View the status of the machine set as it provisions by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
----
+
It can take several minutes for the machine set to achieve the `Running` state.

.. Verify that the new node has been created and is in the `Ready` state by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the new node is using the new boot image by running the following command:
+
[source,terminal]
----
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
Replace `<new_node>` with the name of your new node.
+
.Example output
[source,terminal]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
----
where:

`version`:: Specifies the boot image version.

// Module included in the following assemblies:
//
// * machine_configuration/mco-update-boot-images-manual.adoc

[id="mco-update-boot-images-plat-none_{context}"]
= Manually updating the boot image on a platform none or external cluster

[role="_abstract"]
For `platform: None` and `platform: External` clusters, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

For these clusters, OpenShift Container Platform does not manage node provisioning or {op-system-first} boot images. These clusters do not use Machine API machine sets.

[NOTE]
====
The standard boot image management feature is not supported for `platform: None` or `platform: External` clusters.
====

The method for updating boot images depends on how nodes are added to your cluster as a day-2 operation.

[cols="1,1",options="header"]
|===
| Method | Description
| User-provisioned infrastructure clusters | Nodes are provisioned manually by a user-managed infrastructure.
| {rh-rhacm-first}-managed clusters | Nodes are added by using a discovery ISO managed by an `InfraEnv` object on the hub cluster.
| External provider clusters | Nodes are provisioned by using provider-specific tooling with a user-uploaded {op-system} image.
|===

User-provisioned infrastructure::
For user-provisioned infrastructure clusters, you manage boot images as part of your infrastructure. To update the boot image, download the latest {op-system} image for your architecture from mirror.openshift.com and update your infrastructure to serve the new image.
+
For the full procedure, see the section for your platform in "Adding compute machines to clusters with user-provisioned infrastructure manually".

{rh-rhacm}-managed clusters::
For clusters managed by {rh-rhacm}, the boot image used to generate the discovery ISO image is controlled by the `spec.osImageVersion` parameter in the `InfraEnv` object on the hub cluster. After an OpenShift Container Platform upgrade, you need to update the existing `InfraEnv` object to add or update `spec.osImageVersion` field, specifying the OpenShift Container Platform version of the new boot image.

External provider clusters::
For clusters managed by an external infrastructure provider, such as Oracle Cloud Infrastructure (OCI), you must upload the new boot image to the provider's image store and update your node provisioning configuration to reference the new image when creating new nodes. The exact steps are provider-specific.

If boot image skew enforcement in your cluster is set to the manual mode, after updating the boot image, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Boot image management
* Updating the boot image skew enforcement version
* Manually updating the boot image
* Obtaining the installation program
* Adding compute machines to bare metal
* Configuring an AWS account
* Creating additional worker machines in {gcp-short}
* Requirements for encrypting virtual machines
* Adding compute machines to clusters with user-provisioned infrastructure manually
