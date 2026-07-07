---
title: "Adding compute machines to vSphere manually"
type: reference
domain: openshift
slug: machine-management-4-22-adding-vsphere-compute-user-infra
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/adding-vsphere-compute-user-infra
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Adding compute machines to vSphere manually

[id="adding-vsphere-compute-user-infra"]
= Adding compute machines to vSphere manually

You can add more compute machines to your OpenShift Container Platform cluster on VMware vSphere manually.

[NOTE]
====
You can also use compute machine sets to automate the creation of additional VMware vSphere compute machines for your cluster.
====

== Prerequisites

* You installed a cluster on vSphere.

* You have installation media and {op-system-first} images that you used to create your cluster. If you do not have these files, you must obtain them by following the instructions in the installation procedure.

[IMPORTANT]
====
If you do not have access to the {op-system-first} images that were used to create your cluster, you can add more compute machines to your OpenShift Container Platform cluster with newer versions of {op-system-first} images. For instructions, see Adding new nodes to UPI cluster fails after upgrading to OpenShift 4.6+.
====

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/user_infra/adding-vsphere-compute-user-infra.adoc

[id="machine-vsphere-machines_{context}"]
= Adding more compute machines to a cluster in vSphere

You can add more compute machines to a user-provisioned OpenShift Container Platform cluster on VMware vSphere.

After your vSphere template deploys in your OpenShift Container Platform cluster, you can deploy a virtual machine (VM) for a machine in that cluster.

[NOTE]
====
If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.
====

.Prerequisites

* Obtain the base64-encoded Ignition file for your compute machines.
* You have access to the vSphere template that you created for your cluster.

.Procedure

. Right-click the template's name and click *Clone* -> *Clone to Virtual Machine*.

. On the *Select a name and folder* tab, specify a name for the VM. You might include the machine type in the name, such as `compute-1`.
+
[NOTE]
====
Ensure that all virtual machine names across a vSphere installation are unique.
====

. On the *Select a name and folder* tab, select the name of the folder that you created for the cluster.

. On the *Select a compute resource* tab, select the name of a host in your data center.

. On the *Select storage* tab, select storage for your configuration and disk files.

. On the *Select clone options* tab, select *Customize this virtual machine's hardware*.

. On the *Customize hardware* tab, click *Advanced Parameters*.
** Add the following configuration parameter names and values by specifying data in the *Attribute* and *Values* fields. Ensure that you select the *Add* button for each parameter that you create.
*** `guestinfo.ignition.config.data`: Paste the contents of the base64-encoded compute Ignition config file for this machine type.
*** `guestinfo.ignition.config.data.encoding`: Specify `base64`.
*** `disk.EnableUUID`: Specify `TRUE`.

. In the *Virtual Hardware* panel of the *Customize hardware* tab, modify the specified values as required. Ensure that the amount of RAM, CPU, and disk storage meets the minimum requirements for the machine type. If many networks exist, select *Add New Device* > *Network Adapter*, and then enter your network information in the fields provided by the *New Network* menu item.

. Complete the remaining configuration steps. On clicking the *Finish* button, you have completed the cloning operation.

. From the *Virtual Machines* tab, right-click on your VM and then select *Power* -> *Power On*.

.Next steps

* Continue to create more compute machines for your cluster.

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
