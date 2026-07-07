---
title: "Using DPDK with SR-IOV"
type: reference
domain: openshift
slug: virt-4-22-virt-using-dpdk-with-sriov
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-dpdk-with-sriov
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using DPDK with SR-IOV

[id="virt-using-dpdk-with-sriov"]
= Using DPDK with SR-IOV

[role="_abstract"]
The Data Plane Development Kit (DPDK) provides a set of libraries and drivers for fast packet processing. You can configure clusters and virtual machines (VMs) to run ultra-low latency packet processing workloads by using DPDK drivers with SR-IOV hardware.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-dpdk-with-sriov.adoc

[id="virt-configuring-cluster-dpdk_{context}"]
= Configuring a cluster for DPDK workloads

[role="_abstract"]
You can configure an OpenShift Container Platform cluster to run Data Plane Development Kit (DPDK) workloads for improved network performance.

.Prerequisites
* You have access to the cluster as a user with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have installed the SR-IOV Network Operator.
* You have installed the Node Tuning Operator.

.Procedure
// Cannot label nodes in ROSA/OSD, but can edit machine pools
. Map your compute nodes topology to determine which Non-Uniform Memory Access (NUMA) CPUs are isolated for DPDK applications and which ones are reserved for the operating system (OS).
. If your OpenShift Container Platform cluster uses separate control plane and compute nodes for high-availability:

.. Label a subset of the compute nodes with a custom role; for example, `worker-dpdk`:
+
[source,terminal]
----
$ oc label node <node_name> node-role.kubernetes.io/worker-dpdk=""
----
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> <machinepool_ID> node-role.kubernetes.io/worker-dpdk=""
----

.. Create a new `MachineConfigPool` manifest that contains the `worker-dpdk` label in the `spec.machineConfigSelector` object.
+
Example `MachineConfigPool` manifest:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker-dpdk
  labels:
    machineconfiguration.openshift.io/role: worker-dpdk
spec:
  machineConfigSelector:
    matchExpressions:
      - key: machineconfiguration.openshift.io/role
        operator: In
        values:
          - worker
          - worker-dpdk
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker-dpdk: ""
----

. Create a `PerformanceProfile` manifest that applies to the labeled nodes and the machine config pool that you created in the previous steps. The performance profile specifies the CPUs that are isolated for DPDK applications and the CPUs that are reserved for house keeping.
+
Example `PerformanceProfile` manifest:
+
[source,yaml]
----
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: profile-1
spec:
  cpu:
    isolated: 4-39,44-79
    reserved: 0-3,40-43
  globallyDisableIrqLoadBalancing: true
  hugepages:
    defaultHugepagesSize: 1G
    pages:
    - count: 8
      node: 0
      size: 1G
  net:
    userLevelNetworking: true
  nodeSelector:
    node-role.kubernetes.io/worker-dpdk: ""
  numa:
    topologyPolicy: single-numa-node
----
+
[NOTE]
====
The compute nodes automatically restart after you apply the `MachineConfigPool` and `PerformanceProfile` manifests.
====

. Retrieve the name of the generated `RuntimeClass` resource from the `status.runtimeClass` field of the `PerformanceProfile` object:
+
[source,terminal]
----
$ oc get performanceprofiles.performance.openshift.io profile-1 -o=jsonpath='{.status.runtimeClass}{"\n"}'
----

. Set the previously obtained `RuntimeClass` name as the default container runtime class for the `virt-launcher` pods by editing the `HyperConverged` custom resource (CR):
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
    --type='json' -p='[{"op": "add", "path": "/spec/defaultRuntimeClass", "value":"<runtimeclass-name>"}]'
----
+
[NOTE]
====
Editing the `HyperConverged` CR changes a global setting that affects all VMs that are created after the change is applied.
====

. If your DPDK-enabled compute nodes use Simultaneous multithreading (SMT), enable the `AlignCPUs` enabler by editing the `HyperConverged` CR:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
    --type='json' -p='[{"op": "replace", "path": "/spec/featureGates/alignCPUs", "value": true}]'
----
+
[NOTE]
====
Enabling `AlignCPUs` allows {VirtProductName} to request up to two additional dedicated CPUs to bring the total CPU count to an even parity when using
emulator thread isolation.
====

. Create an `SriovNetworkNodePolicy` object with the `spec.deviceType` field set to `vfio-pci`.
+
Example `SriovNetworkNodePolicy` manifest:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policy-1
  namespace: openshift-sriov-network-operator
spec:
  resourceName: intel_nics_dpdk
  deviceType: vfio-pci
  mtu: 9000
  numVfs: 4
  priority: 99
  nicSelector:
    vendor: "8086"
    deviceID: "1572"
    pfNames:
      - eno3
    rootDevices:
      - "0000:19:00.2"
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-dpdk-with-sriov.adoc

[id="virt-removing-custom-mcp_{context}"]
= Removing a custom machine config pool for high-availability clusters

[role="_abstract"]
You can delete a custom machine config pool that you previously created for your high-availability cluster.

.Prerequisites
* You have access to the cluster as a user with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have created a custom machine config pool by labeling a subset of the compute nodes with a custom role and creating a `MachineConfigPool` manifest with that label.

.Procedure

. Remove the `worker-dpdk` label from the compute nodes by running the following command:
+
[source,terminal]
----
$ oc label node <node_name> node-role.kubernetes.io/worker-dpdk-
----

. Delete the `MachineConfigPool` manifest that contains the `worker-dpdk` label by entering the following command:
+
[source,terminal]
----
$ oc delete mcp worker-dpdk
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-dpdk-with-sriov.adoc

[id="virt-configuring-vm-project-dpdk_{context}"]
= Configuring a project for DPDK workloads

[role="_abstract"]
You can configure the project to run DPDK workloads on SR-IOV hardware.

.Prerequisites

* Your cluster is configured to run DPDK workloads.
* You have installed the {oc-first}.

.Procedure

. Create a namespace for your DPDK applications:
+
[source,terminal]
----
$ oc create ns dpdk-ns
----

. Create an `SriovNetwork` object that references the `SriovNetworkNodePolicy` object. When you create an `SriovNetwork` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.
+
Example `SriovNetwork` manifest:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-sriovnetwork
  namespace: openshift-sriov-network-operator
spec:
  ipam: |
    {
      "type": "host-local",
      "subnet": "10.56.217.0/24",
      "rangeStart": "10.56.217.171",
      "rangeEnd": "10.56.217.181",
      "routes": [{
        "dst": "0.0.0.0/0"
      }],
      "gateway": "10.56.217.1"
    }
  networkNamespace: dpdk-ns
  resourceName: intel_nics_dpdk
  spoofChk: "off"
  trust: "on"
  vlan: 1019
----
+
* `spec.networkNamespace` defines the namespace where the `NetworkAttachmentDefinition` object is deployed.
* `spec.resourceName` defines the value of the `spec.resourceName` attribute of the `SriovNetworkNodePolicy` object that was created when configuring the cluster for DPDK workloads.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-sriov.adoc

[id="virt-configuring-vm-dpdk_{context}"]
= Configuring a virtual machine for DPDK workloads

[role="_abstract"]
You can run Data Packet Development Kit (DPDK) workloads on virtual machines (VMs) to achieve lower latency and higher throughput for faster packet processing in the user space. DPDK uses the SR-IOV network for hardware-based I/O sharing.

.Prerequisites
* Your cluster is configured to run DPDK workloads.
* You have created and configured the project in which the VM will run.
* You have installed the {oc-first}.

.Procedure
. Edit the `VirtualMachine` manifest to include information about the SR-IOV network interface, CPU topology, CRI-O annotations, and huge pages.
+
Example `VirtualMachine` manifest:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: rhel-dpdk-vm
spec:
  runStrategy: Always
  template:
    metadata:
      annotations:
        cpu-load-balancing.crio.io: disable
        cpu-quota.crio.io: disable
        irq-load-balancing.crio.io: disable
    spec:
      domain:
        cpu:
          sockets: 1
          cores: 5
          threads: 2
          dedicatedCpuPlacement: true
          isolateEmulatorThread: true
        interfaces:
          - masquerade: {}
            name: default
          - model: virtio
            name: nic-east
            pciAddress: '0000:07:00.0'
            sriov: {}
          networkInterfaceMultiqueue: true
          rng: {}
      memory:
        hugepages:
          pageSize: 1Gi
          guest: 8Gi
      networks:
        - name: default
          pod: {}
        - multus:
            networkName: dpdk-net
          name: nic-east
# ...
----
+
* `spec.template.metadata.annotations.cpu-load-balancing.crio.io` specifies that load balancing is disabled for CPUs that are used by the container.
* `spec.template.metadata.annotations.cpu-quota.crio.io` specifies that the CPU quota is disabled for CPUs that are used by the container.
* `spec.template.metadata.annotations.irq-load-balancing.crio.io` specifies that Interrupt Request (IRQ) load balancing is disabled for CPUs that are used by the container.
* `spec.template.spec.domain.cpu.sockets` defines the number of sockets inside the VM. This field must be set to `1` for the CPUs to be scheduled from the same Non-Uniform Memory Access (NUMA) node.
* `spec.template.spec.domain.cpu.cores` defines the number of cores inside the VM. This must be a value greater than or equal to `1`. In this example, the VM is scheduled with 5 hyper-threads or 10 CPUs.
* `spec.template.spec.domain.memory.hugepages.pageSize` defines the size of the huge pages. The possible values for x86-64 architecture are 1Gi and 2Mi. In this example, the request is for 8 huge pages of size 1Gi.
* `spec.template.spec.networks.multus.networkName` defines the name of the SR-IOV `NetworkAttachmentDefinition` object.

. Save and exit the editor.
. Apply the `VirtualMachine` manifest:
+
[source,terminal]
----
$ oc apply -f <file_name>.yaml
----

. Configure the guest operating system. The following example shows the configuration steps for {op-system-base} 9 operating system:
.. Configure huge pages by using the GRUB bootloader command-line interface. In the following example, 8 1G huge pages are specified.
+
[source,terminal]
----
$ grubby --update-kernel=ALL --args="default_hugepagesz=1GB hugepagesz=1G hugepages=8"
----

.. To achieve low-latency tuning by using the `cpu-partitioning` profile in the TuneD application, run the following commands:
+
[source,terminal]
----
$ dnf install -y tuned-profiles-cpu-partitioning
----
+
[source,terminal]
----
$ echo isolated_cores=2-9 > /etc/tuned/cpu-partitioning-variables.conf
----
The first two CPUs (0 and 1) are set aside for house keeping tasks and the rest are isolated for the DPDK application.
+
[source,terminal]
----
$ tuned-adm profile cpu-partitioning
----

.. Override the SR-IOV NIC driver by using the `driverctl` device driver control utility:
+
[source,terminal]
----
$ dnf install -y driverctl
----
+
[source,terminal]
----
$ driverctl set-override 0000:07:00.0 vfio-pci
----

. Restart the VM to apply the changes.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Using CPU Manager and Topology Manager
* Optimizing memory management for workloads by using huge pages
* Creating a custom machine config pool
* Working with projects
