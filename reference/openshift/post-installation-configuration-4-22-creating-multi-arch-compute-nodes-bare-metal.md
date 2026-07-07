---
title: "Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-creating-multi-arch-compute-nodes-bare-metal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/creating-multi-arch-compute-nodes-bare-metal
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}

[id="creating-multi-arch-compute-nodes-bare-metal"]
= Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}

[role="_abstract"]
You can create a cluster with multi-architecture compute machines on bare metal (`x86_64` or `aarch64`), {ibm-power-name} (`ppc64le`), or {ibm-z-name} (`s390x`). To do this, you must have an existing single-architecture cluster on one of these platforms.

See the following installation procedures for your platform:

* Bare metal with user-provisioned infrastructure: See "Installing a user-provisioned cluster on bare metal". You can then add 64-bit ARM compute machines to your OpenShift Container Platform cluster on bare metal.
* {ibm-power-name}: See "Installing on {ibm-power-name}". You can then add `x86_64` compute machines to your OpenShift Container Platform cluster on {ibm-power-name}.
* {ibm-z-name} and {ibm-linuxone-name}: See "Installing on {ibm-z-name} and {ibm-linuxone-name}". You can then add `x86_64` compute machines to your OpenShift Container Platform cluster on {ibm-z-name} and {ibm-linuxone-name}.

[IMPORTANT]
====
The bare metal installer-provisioned infrastructure and the Bare Metal Operator do not support adding secondary architecture nodes during the initial cluster setup. You can add secondary architecture nodes manually only after the initial cluster setup.
====

Before you can add additional compute nodes to your cluster, you must upgrade your cluster to one that uses the multi-architecture payload. For more information about migrating to the multi-architecture payload, see "Migrating to a cluster with multi-architecture compute machines".

The following procedures explain how to create a {op-system} compute machine by using an ISO image or network PXE booting. This allows you to add additional nodes to your cluster and deploy a cluster with multi-architecture compute machines.

[NOTE]
====
Before adding a secondary architecture node to your cluster, you must install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` object. For more information, see "Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator".
====

//Creating {op-system} machines using an ISO image
// Module included in the following assemblies:
//
// * machine_management/user_infra/adding-bare-metal-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="machine-user-infra-machines-iso_{context}"]
= Creating {op-system} machines using an ISO image

[role="_abstract"]
You can create more {op-system-first} compute machines for your bare metal cluster by using an ISO image to create the machines.
You can create more {op-system-first} compute machines for your cluster by using an ISO image to create the machines.

.Prerequisites

* Obtain the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation.
* You must have the OpenShift CLI (`oc`)  installed.

.Procedure

. Extract the Ignition config file from the cluster by running the following command:
+
[source,terminal]
----
$ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
----

. Upload the `worker.ign` Ignition config file you exported from your cluster to your HTTP server. Note the URLs of these files.

. You can validate that the ignition files are available on the URLs. The following example gets the Ignition config files for the compute node:
+
[source,terminal]
----
$ curl -k http://<HTTP_server>/worker.ign
----

. You can access the ISO image for booting your new machine by running to following command:
+
[source,terminal]
----
RHCOS_VHD_ORIGIN_URL=$(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' | jq -r '.architectures.<architecture>.artifacts.metal.formats.iso.disk.location')
----

. Use the ISO file to install {op-system} on more compute machines. Use the same method that you used when you created machines before you installed the cluster:
** Burn the ISO image to a disk and boot it directly.
** Use ISO redirection with a LOM interface.

. Boot the {op-system} ISO image without specifying any options, or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the {op-system} live environment.
+
[NOTE]
====
You can interrupt the {op-system} installation boot process to add kernel arguments. However, for this ISO procedure you must use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.
====

. Run the `coreos-installer` command by using `sudo`. The `core` user does not have the root privileges required to perform the installation. Specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to.
+
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> --ignition-hash=sha512-<digest>
----
+
where:
+
`<digest>`:: Specifies the Ignition config file SHA512 digest obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node.
+
[NOTE]
====
If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.
====
+
The following example initializes a compute node installation to the `/dev/sda` device. The Ignition config file for the compute node is obtained from an HTTP web server with the IP address 192.168.1.2:
+
[source,terminal]
----
$ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/worker.ign /dev/sda --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
----

. Monitor the progress of the {op-system} installation on the console of the machine.
+
[IMPORTANT]
====
Ensure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of {op-system} installation issues that might arise.
====

. Continue to create more compute machines for your cluster.

//Creating {op-system} machines by PXE or iPXE booting
// Module included in the following assemblies:
//
// * machine_management/user_infra/adding-bare-metal-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * post_installation_configuration/multi-architecture-configuration.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="machine-user-infra-machines-pxe_{context}"]
= Creating {op-system} machines by PXE or iPXE booting

[role="_abstract"]
You can create more {op-system-first} compute machines for your bare metal cluster by using PXE or iPXE booting.

.Prerequisites

* Obtain the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation.
* Obtain the URLs of the {op-system} ISO image, compressed metal BIOS, `kernel`, and `initramfs` files that you uploaded to your HTTP server during cluster installation.
* You have access to the PXE booting infrastructure that you used to create the machines for your OpenShift Container Platform cluster during installation. The machines must boot from their local disks after {op-system} is installed on them.
* If you use UEFI, you have access to the `grub.conf` file that you modified during OpenShift Container Platform installation.

.Procedure

. Confirm that your PXE or iPXE installation for the {op-system} images is correct.

** For PXE:
+
----
DEFAULT pxeboot
TIMEOUT 20
PROMPT 0
LABEL pxeboot
    KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
    APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img
----
+
where:
+
`KERNEL`:: Specifies the location of the live `kernel` file that you uploaded to your HTTP server.
`APPEND`:: Specifies the locations of the {op-system} files that you uploaded to your HTTP server:
`initrd`:: Specifies the location of the live `initramfs` file.
`coreos.inst.ignition_url`:: Specifies the location of the worker Ignition config file. This parameter supports only HTTP and HTTPS.
`coreos.live.rootfs_url`:: Specifies the location of the live `rootfs` file. This parameter supports only HTTP and HTTPS.
+
[NOTE]
====
This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in {op-system}, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?".
====

** For iPXE (`x86_64` + `aarch64`):
** For iPXE (`x86_64` + `ppc64le`):
+
----
kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
boot
----
+
where:
+
`kernel`:: Specifies the location of the `kernel` file that you uploaded to your HTTP server.
`initrd=main`:: Specifies an argument that is required for booting on UEFI systems.
`coreos.live.rootfs_url`:: Specifies the location of the `rootfs` file that you uploaded to your HTTP server.
`coreos.inst.ignition_url`:: Specifies the location of the worker Ignition config file that you uploaded to your HTTP server.
`initrd --name main`:: Specifies the location of the `initramfs` file that you uploaded to your HTTP server.
+
[NOTE]
====
* If you use multiple NICs, specify a single interface in the `ip` option.
For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`.
+
* This configuration does not enable serial console access on machines with a graphical console To configure a different console, add one or more `console=` arguments to the `kernel` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in {op-system}, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?" in the Additional resources section and "Enabling the serial console for PXE and ISO installation" in the "Advanced {op-system} installation configuration" section.
====
+
[NOTE]
====
To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. For more information, see "IMAGE_GZIP option in iPXE".
To network boot the CoreOS `kernel` on `ppc64le` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. For more information, see "IMAGE_GZIP option in iPXE".
====

** For PXE (with UEFI and GRUB as second stage) on `aarch64`:
** For PXE (with UEFI and GRUB as second stage) on `ppc64le`:
+
----
menuentry 'Install CoreOS' {
    linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
    initrd rhcos-<version>-live-initramfs.<architecture>.img
}
----
+
where:
+
`linux`:: Specifies the location of the live `kernel` file on your TFTP server.
`coreos.live.rootfs_url`:: Specifies the location of the live `rootfs` file.
`coreos.inst.ignition_url`:: Specifies the location of the worker Ignition config file.
`initrd`:: Specifies the location of the live `initramfs` file on your TFTP server.
+
[NOTE]
====
If you use multiple NICs, specify a single interface in the `ip` option.
For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`.
====
+
. Use the PXE or iPXE infrastructure to create the required compute machines for your cluster.

[role="_additional-resources"]
.Additional resources

* How does one set up a serial terminal and/or console in Red Hat Enterprise Linux? (Red{nbsp}Hat Knowledgebase article)

* `IMAGE_GZIP` option in iPXE (iPXE documentation)

//Approving the certificate signing requests for your machines
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

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Installing a user provisioned cluster on bare metal

* Installing a cluster on {ibm-power-name}

* Installing a cluster on {ibm-z-name} and {ibm-linuxone-name}

* Migrating to a cluster with multi-architecture compute machines

* Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator
