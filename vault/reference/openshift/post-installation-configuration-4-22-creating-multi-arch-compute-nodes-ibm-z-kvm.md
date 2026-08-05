---
title: "Creating a cluster with multi-architecture compute machines on {ibm-z-title} and {ibm-linuxone-title} with {op-system-base} KVM"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-creating-multi-arch-compute-nodes-ibm-z-kvm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/creating-multi-arch-compute-nodes-ibm-z-kvm
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Creating a cluster with multi-architecture compute machines on {ibm-z-title} and {ibm-linuxone-title} with {op-system-base} KVM

[id="creating-multi-arch-compute-nodes-ibm-z-kvm"]
= Creating a cluster with multi-architecture compute machines on {ibm-z-title} and {ibm-linuxone-title} with {op-system-base} KVM

To create a cluster with multi-architecture compute machines on {ibm-z-name} and {ibm-linuxone-name} (`s390x`) with {op-system-base} KVM, you must have an existing single-architecture `x86_64` cluster. You can then add `s390x` compute machines to your OpenShift Container Platform cluster.

Before you can add `s390x` nodes to your cluster, you must upgrade your cluster to one that uses the multi-architecture payload. For more information on migrating to the multi-architecture payload, see Migrating to a cluster with multi-architecture compute machines.

The following procedures explain how to create a {op-system} compute machine using a {op-system-base} KVM instance. This will allow you to add `s390x` nodes to your cluster and deploy a cluster with multi-architecture compute machines.

To create an {ibm-z-name} or {ibm-linuxone-name} (`s390x`) cluster with multi-architecture compute machines on `x86_64`, follow the instructions for
Installing a cluster on {ibm-z-name} and {ibm-linuxone-name}. You can then add `x86_64` compute machines as described in Creating a cluster with multi-architecture compute machines on bare metal, {ibm-power-title}, or {ibm-z-title}.

[NOTE]
====
Before adding a secondary architecture node to your cluster, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` object. For more information, see Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-z-kvm.adoc

[id="machine-user-infra-machines-ibm-z-kvm_{context}"]
= Creating {op-system} machines using `virt-install`

You can create more {op-system-first} compute machines for your cluster by using `virt-install`.

.Prerequisites

* You have at least one LPAR running on {op-system-base} 8.7 or later with KVM, referred to as {op-system-base} KVM host in this procedure.
* The KVM/QEMU hypervisor is installed on the {op-system-base} KVM host.
* You have a domain name server (DNS) that can perform hostname and reverse lookup for the nodes.
* An HTTP or HTTPS server is set up.

.Procedure

. Extract the Ignition config file from the cluster by running the following command:
+
[source,terminal]
----
$ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
----

. Upload the `worker.ign` Ignition config file you exported from your cluster to your HTTP server. Note the URL of this file.

. You can validate that the Ignition file is available on the URL. The following example gets the Ignition config file for the compute node:
+
[source,terminal]
----
$ curl -k http://<HTTP_server>/worker.ign
----

. Download the {op-system-base} live `kernel`, `initramfs`, and `rootfs` files by running the following commands:
+
[source,terminal]
----
 $ curl -LO $(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' \
| jq -r '.architectures.s390x.artifacts.metal.formats.pxe.kernel.location')
----
+
[source,terminal]
----
$ curl -LO $(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' \
| jq -r '.architectures.s390x.artifacts.metal.formats.pxe.initramfs.location')
----
+
[source,terminal]
----
$ curl -LO $(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' \
| jq -r '.architectures.s390x.artifacts.metal.formats.pxe.rootfs.location')
----

. Move the downloaded {op-system-base} live `kernel`, `initramfs`, and `rootfs` files to an HTTP or HTTPS server before you launch `virt-install`.

. Create the new KVM guest nodes using the {op-system-base} `kernel`, `initramfs`, and Ignition files; the new disk image; and adjusted parm line arguments.
+
--
[source,terminal]
----
$ virt-install \
   --connect qemu:///system \
   --name <vm_name> \
   --autostart \
   --os-variant rhel9.4 \ <1>
   --cpu host \
   --vcpus <vcpus> \
   --memory <memory_mb> \
   --disk <vm_name>.qcow2,size=<image_size> \
   --network network=<virt_network_parm> \
   --location <media_location>,kernel=<rhcos_kernel>,initrd=<rhcos_initrd> \ <2>
   --extra-args "rd.neednet=1" \
   --extra-args "coreos.inst.install_dev=/dev/vda" \
   --extra-args "coreos.inst.ignition_url=http://<http_server>/worker.ign " \ <3>
   --extra-args "coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img" \ <4>
   --extra-args "ip=<ip>::<gateway>:<netmask>:<hostname>::none" \ <5>
   --extra-args "nameserver=<dns>" \
   --extra-args "console=ttysclp0" \
   --noautoconsole \
   --wait
----
<1> For `os-variant`, specify the {op-system-base} version for the {op-system} compute machine. `rhel9.4` is the recommended version. To query the supported {op-system-base} version of your operating system, run the following command:
+
[source,terminal]
----
$ osinfo-query os -f short-id
----
+
[NOTE]
====
The `os-variant` is case sensitive.
====
+
<2> For `--location`, specify the location of the kernel/initrd on the HTTP or HTTPS server.
<3> Specify the location of the `worker.ign` config file. Only HTTP and HTTPS protocols are supported.
<4> Specify the location of the `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported
<5> Optional: For `hostname`, specify the fully qualified hostname of the client machine.
--
+
[NOTE]
====
If you are using HAProxy as a load balancer, update your HAProxy rules for `ingress-router-443` and `ingress-router-80` in the `/etc/haproxy/haproxy.cfg` configuration file.
====

. Continue to create more compute machines for your cluster.

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
