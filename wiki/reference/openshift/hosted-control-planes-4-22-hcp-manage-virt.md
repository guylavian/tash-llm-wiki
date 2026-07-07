---
title: "Managing {hcp} on {VirtProductName}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-manage-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-manage-virt
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Managing {hcp} on {VirtProductName}

[id="hcp-manage-virt"]
= Managing {hcp} on {VirtProductName}

After you deploy a hosted cluster on {VirtProductName}, you can manage the cluster by completing the following procedures.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-access_{context}"]
= Accessing the hosted cluster

You can access the hosted cluster by either getting the `kubeconfig` file and `kubeadmin` credential directly from resources, or by using the `hcp` command-line interface to generate a `kubeconfig` file.

.Prerequisites

To access the hosted cluster by getting the `kubeconfig` file and credentials directly from resources, you must be familiar with the access secrets for hosted clusters. The _hosted cluster (hosting)_ namespace contains hosted cluster resources and the access secrets. The _hosted control plane_ namespace is where the hosted control plane runs.

The secret name formats are as follows:

** `kubeconfig` secret: `<hosted_cluster_namespace>-<name>-admin-kubeconfig` (clusters-hypershift-demo-admin-kubeconfig)
** `kubeadmin` password secret: `<hosted_cluster_namespace>-<name>-kubeadmin-password` (clusters-hypershift-demo-kubeadmin-password)

The `kubeconfig` secret contains a Base64-encoded `kubeconfig` field, which you can decode and save into a file to use with the following command:

[source,terminal]
----
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
----

The `kubeadmin` password secret is also Base64-encoded. You can decode it and use the password to log in to the API server or console of the hosted cluster.

.Procedure

* To access the hosted cluster by using the `hcp` CLI to generate the `kubeconfig` file, take the following steps:

. Generate the `kubeconfig` file by entering the following command:
+
[source,terminal]
----
$ hcp create kubeconfig --namespace <hosted_cluster_namespace> \
  --name <hosted_cluster_name> > <hosted_cluster_name>.kubeconfig
----

. After you save the `kubeconfig` file, you can access the hosted cluster by entering the following example command:
+
[source,terminal]
----
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-bm.adoc
// * hosted_control_planes/hcp-manage/hcp-manage-non-bm.adoc
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-bm-autoscale_{context}"]
= Enabling node auto-scaling for the hosted cluster

When you need more capacity in your hosted cluster and spare agents are available, you can enable auto-scaling to install new worker nodes.

.Procedure

. To enable auto-scaling, enter the following command:
+
[source,terminal]
----
$ oc -n <hosted_cluster_namespace> patch nodepool <hosted_cluster_name> \
  --type=json \
  -p '[{"op": "remove", "path": "/spec/replicas"},{"op":"add", "path": "/spec/autoScaling", "value": { "max": 5, "min": 2 }}]'
----
+
[NOTE]
====
In the example, the minimum number of nodes is 2, and the maximum is 5. The maximum number of nodes that you can add might be bound by your platform. For example, if you use the Agent platform, the maximum number of nodes is bound by the number of available agents.
====

. Create a workload that requires a new node.

.. Create a YAML file that contains the workload configuration, by using the following example:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: reversewords
  name: reversewords
  namespace: default
spec:
  replicas: 40
  selector:
    matchLabels:
      app: reversewords
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: reversewords
    spec:
      containers:
      - image: quay.io/mavazque/reversewords:latest
        name: reversewords
        resources:
          requests:
            memory: 2Gi
status: {}
----

.. Save the file as `workload-config.yaml`.

.. Apply the YAML by entering the following command:
+
[source,terminal]
----
$ oc apply -f workload-config.yaml
----

. Extract the `admin-kubeconfig` secret by entering the following command:
+
[source,terminal]
----
$ oc extract -n <hosted_cluster_namespace> \
  secret/<hosted_cluster_name>-admin-kubeconfig \
  --to=./hostedcluster-secrets --confirm
----
+
.Example output
----
hostedcluster-secrets/kubeconfig
----

. You can check if new nodes are in the `Ready` status by entering the following command:
+
[source,terminal]
----
$ oc --kubeconfig ./hostedcluster-secrets get nodes
----

. To remove the node, delete the workload by entering the following command:
+
[source,terminal]
----
$ oc --kubeconfig ./hostedcluster-secrets -n <namespace> \
  delete deployment <deployment_name>
----

. Wait for several minutes to pass without requiring the additional capacity. On the Agent platform, the agent is decommissioned and can be reused. You can confirm that the node was removed by entering the following command:
+
[source,terminal]
----
$ oc --kubeconfig ./hostedcluster-secrets get nodes
----
+
[NOTE]
====
For {ibm-z-name} agents, if you are using an OSA network device in Processor Resource/Systems Manager (PR/SM) mode, auto scaling is not supported. You must delete the old agent manually and scale up the node pool because the new agent joins during the scale down process.
====

[id="hcp-virt-storage"]
== Configuring storage for {hcp} on {VirtProductName}

If you do not provide any advanced storage configuration, the default storage class is used for the KubeVirt virtual machine (VM) images, the KubeVirt Container Storage Interface (CSI) mapping, and the etcd volumes.

The following table lists the capabilities that the infrastructure must provide to support persistent storage in a hosted cluster:

.Persistent storage modes in a hosted cluster
|===
| Infrastructure CSI provider | Hosted cluster CSI provider | Hosted cluster capabilities

| Any RWX `Block` CSI provider
| `kubevirt-csi`
a|

--
- Basic RWO `Block` and `File`
- Basic RWX `Block` and `Snapshot`
- CSI volume cloning
--

| Any RWX `Block` CSI provider
| {rh-storage-first}
| {rh-storage-first} feature set. External mode has a smaller footprint and uses a standalone Red{nbsp}Hat Ceph Storage. Internal mode has a larger footprint, but is self-contained and suitable for use cases that require expanded capabilities such as RWX `File`.
|===

[NOTE]
====
{VirtProductName} handles storage on hosted clusters, which especially helps customers whose requirements are limited to block storage.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-map-storage_{context}"]
= Mapping KubeVirt CSI storage classes

KubeVirt CSI supports mapping a infrastructure storage class that is capable of `ReadWriteMany` (RWX) access. You can map the infrastructure storage class to hosted storage class during cluster creation.

.Procedure

* To map the infrastructure storage class to the hosted storage class, use the `--infra-storage-class-mapping` argument by running the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class> \ <6>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Replace `<infrastructure_storage_class>` with the infrastructure storage class name and `<hosted_storage_class>` with the hosted cluster storage class name. You can use the `--infra-storage-class-mapping` argument multiple times within the `hcp create cluster` command.

After you create the hosted cluster, the infrastructure storage class is visible within the hosted cluster. When you create a Persistent Volume Claim (PVC) within the hosted cluster that uses one of those storage classes, KubeVirt CSI provisions that volume by using the infrastructure storage class mapping that you configured during cluster creation.

[NOTE]
====
KubeVirt CSI supports mapping only an infrastructure storage class that is capable of RWX access.
====

The following table shows how volume and access mode capabilities map to KubeVirt CSI storage classes:

.Mapping KubeVirt CSI storage classes to access and volume modes
|===
| Infrastructure CSI capability | Hosted cluster CSI capability | VM live migration support | Notes

| RWX: `Block` or `Filesystem`
| `ReadWriteOnce` (RWO) `Block` or `Filesystem` RWX `Block` only
| Supported
| Use `Block` mode because `Filesystem` volume mode results in degraded hosted `Block` mode performance. RWX `Block` volume mode is supported only when the hosted cluster is OpenShift Container Platform 4.16 or later.

| RWO `Block` storage
| RWO `Block` storage or `Filesystem`
| Not supported
| Lack of live migration support affects the ability to update the underlying infrastructure cluster that hosts the KubeVirt VMs.

| RWO `FileSystem`
| RWO `Block` or `Filesystem`
| Not supported
| Lack of live migration support affects the ability to update the underlying infrastructure cluster that hosts the KubeVirt VMs. Use of the infrastructure `Filesystem` volume mode results in degraded hosted `Block` mode performance.

|===

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-csi-snapshot_{context}"]
= Mapping a single KubeVirt CSI volume snapshot class

You can expose your infrastructure volume snapshot class to the hosted cluster by using KubeVirt CSI.

.Procedure

* To map your volume snapshot class to the hosted cluster, use the `--infra-volumesnapshot-class-mapping` argument when creating a hosted cluster. Run the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class> \ <6>
  --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class> <7>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Replace `<infrastructure_storage_class>` with the storage class present in the infrastructure cluster. Replace `<hosted_storage_class>` with the storage class present in the hosted cluster.
<7> Replace `<infrastructure_volume_snapshot_class>` with the volume snapshot class present in the infrastructure cluster. Replace `<hosted_volume_snapshot_class>` with the volume snapshot class present in the hosted cluster.
+
[NOTE]
====
If you do not use the `--infra-storage-class-mapping` and `--infra-volumesnapshot-class-mapping` arguments, a hosted cluster is created with the default storage class and the volume snapshot class. Therefore, you must set the default storage class and the volume snapshot class in the infrastructure cluster.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-multiple-snapshots_{context}"]
= Mapping multiple KubeVirt CSI volume snapshot classes

You can map multiple volume snapshot classes to the hosted cluster by assigning them to a specific group. The infrastructure storage class and the volume snapshot class are compatible with each other only if they belong to a same group.

.Procedure

* To map multiple volume snapshot classes to the hosted cluster, use the `group` option when creating a hosted cluster. Run the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \ <6>
  --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \
  --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \
  --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class>,group=<group_name> \ <7>
  --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class>,group=<group_name>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Replace `<infrastructure_storage_class>` with the storage class present in the infrastructure cluster. Replace `<hosted_storage_class>` with the storage class present in the hosted cluster. Replace `<group_name>` with the group name. For example, `infra-storage-class-mygroup/hosted-storage-class-mygroup,group=mygroup` and `infra-storage-class-mymap/hosted-storage-class-mymap,group=mymap`.
<7> Replace `<infrastructure_volume_snapshot_class>` with the volume snapshot class present in the infrastructure cluster. Replace `<hosted_volume_snapshot_class>` with the volume snapshot class present in the hosted cluster. For example, `infra-vol-snap-mygroup/hosted-vol-snap-mygroup,group=mygroup` and `infra-vol-snap-mymap/hosted-vol-snap-mymap,group=mymap`.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-root-volume_{context}"]
= Configuring KubeVirt VM root volume

At cluster creation time, you can configure the storage class that is used to host the KubeVirt VM root volumes by using the `--root-volume-storage-class` argument.

.Procedure

* To set a custom storage class and volume size for KubeVirt VMs, run the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --root-volume-storage-class <root_volume_storage_class> \ <6>
  --root-volume-size <volume_size> <7>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Specify a name of the storage class to host the KubeVirt VM root volumes, for example, `ocs-storagecluster-ceph-rbd`.
<7> Specify the volume size, for example, `64`.
+
As a result, you get a hosted cluster created with VMs hosted on PVCs.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-image-caching_{context}"]
= Enabling KubeVirt VM image caching

You can use KubeVirt VM image caching to optimize both cluster startup time and storage usage. KubeVirt VM image caching supports the use of a storage class that is capable of smart cloning and the `ReadWriteMany` access mode. For more information about smart cloning, see _Cloning a data volume using smart-cloning_.

Image caching works as follows:

. The VM image is imported to a PVC that is associated with the hosted cluster.
. A unique clone of that PVC is created for every KubeVirt VM that is added as a worker node to the cluster.

Image caching reduces VM startup time by requiring only a single image import. It can further reduce overall cluster storage usage when the storage class supports copy-on-write cloning.

.Procedure

* To enable image caching, during cluster creation, use the `--root-volume-cache-strategy=PVC` argument by running the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --root-volume-cache-strategy=PVC <6>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Specify a strategy for image caching, for example, `PVC`.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-storage-security-isolation_{context}"]
= KubeVirt CSI storage security and isolation

KubeVirt Container Storage Interface (CSI) extends the storage capabilities of the underlying infrastructure cluster to hosted clusters. The CSI driver ensures secure and isolated access to the infrastructure storage classes and hosted clusters by using the following security constraints:

* The storage of a hosted cluster is isolated from the other hosted clusters.

* Worker nodes in a hosted cluster do not have a direct API access to the infrastructure cluster. The hosted cluster can provision storage on the infrastructure cluster only through the controlled KubeVirt CSI interface.

* The hosted cluster does not have access to the KubeVirt CSI cluster controller. As a result, the hosted cluster cannot access arbitrary storage volumes on the infrastructure cluster that are not associated with the hosted cluster. The KubeVirt CSI cluster controller runs in a pod in the hosted control plane namespace.

* Role-based access control (RBAC) of the KubeVirt CSI cluster controller limits the persistent volume claim (PVC) access to only the hosted control plane namespace. Therefore, KubeVirt CSI components cannot access storage from the other namespaces.

[role="_additional-resources"]
.Additional resources

* Cloning a data volume using smart-cloning

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-etcd-storage_{context}"]
= Configuring etcd storage

At cluster creation time, you can configure the storage class that is used to host etcd data by using the `--etcd-storage-class` argument.

.Procedure

* To configure a storage class for etcd, run the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \ <1>
  --node-pool-replicas <worker_node_count> \ <2>
  --pull-secret <path_to_pull_secret> \ <3>
  --memory <memory> \ <4>
  --cores <cpu> \ <5>
  --etcd-storage-class=<etcd_storage_class_name> <6>
----
+
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `2`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `8Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Specify the etcd storage class name, for example, `lvm-storageclass`. If you do not provide an `--etcd-storage-class` argument, the default storage class is used.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-attach-nvidia-gpus_{context}"]
= Attaching NVIDIA GPU devices by using the hcp CLI

You can attach one or more NVIDIA graphics processing unit (GPU) devices to node pools by using the `hcp` command-line interface (CLI) in a hosted cluster on {VirtProductName}.

.Prerequisites

* You have exposed the NVIDIA GPU device as a resource on the node where the GPU device resides. For more information, see NVIDIA GPU Operator with {VirtProductName}.

* You have exposed the NVIDIA GPU device as an extended resource on the node to assign it to node pools.

.Procedure

* You can attach the GPU device to node pools during cluster creation by running the following command:
+
[source,terminal]
----
$ hcp create cluster kubevirt \
  --name <hosted_cluster_name> \// <1>
  --node-pool-replicas <worker_node_count> \// <2>
  --pull-secret <path_to_pull_secret> \// <3>
  --memory <memory> \// <4>
  --cores <cpu> \// <5>
  --host-device-name="<gpu_device_name>,count:<value>" <6>
----
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the worker count, for example, `3`.
<3> Specify the path to your pull secret, for example, `/user/name/pullsecret`.
<4> Specify a value for memory, for example, `16Gi`.
<5> Specify a value for CPU, for example, `2`.
<6> Specify the GPU device name and the count, for example, `--host-device-name="nvidia-a100,count:2"`. The `--host-device-name` argument takes the name of the GPU device from the infrastructure node and an optional count that represents the number of GPU devices you want to attach to each virtual machine (VM) in node pools. The default count is `1`. For example, if you attach 2 GPU devices to 3 node pool replicas, all 3 VMs in the node pool are attached to the 2 GPU devices.
+
[TIP]
====
You can use the `--host-device-name` argument multiple times to attach multiple devices of different types.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-attach-nvidia-gpus-np-api_{context}"]
= Attaching NVIDIA GPU devices by using the NodePool resource

You can attach one or more NVIDIA graphics processing unit (GPU) devices to node pools by configuring the `nodepool.spec.platform.kubevirt.hostDevices` field in the `NodePool` resource.

.Procedure

* Attach one or more GPU devices to node pools:

** To attach a single GPU device, configure the `NodePool` resource by using the following example configuration:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: <hosted_cluster_name> <1>
  namespace: <hosted_cluster_namespace> <2>
spec:
  arch: amd64
  clusterName: <hosted_cluster_name>
  management:
    autoRepair: false
    upgradeType: Replace
  nodeDrainTimeout: 0s
  nodeVolumeDetachTimeout: 0s
  platform:
    kubevirt:
      attachDefaultNetwork: true
      compute:
        cores: <cpu> <3>
        memory: <memory> <4>
      hostDevices: <5>
      - count: <count> <6>
        deviceName: <gpu_device_name> <7>
      networkInterfaceMultiqueue: Enable
      rootVolume:
        persistent:
          size: 32Gi
        type: Persistent
    type: KubeVirt
  replicas: <worker_node_count> <8>
----
<1> Specify the name of your hosted cluster, for instance, `example`.
<2> Specify the name of the hosted cluster namespace, for example, `clusters`.
<3> Specify a value for CPU, for example, `2`.
<4> Specify a value for memory, for example, `16Gi`.
<5> The `hostDevices` field defines a list of different types of GPU devices that you can attach to node pools.
<6> Specify the number of GPU devices you want to attach to each virtual machine (VM) in node pools. For example, if you attach 2 GPU devices to 3 node pool replicas, all 3 VMs in the node pool are attached to the 2 GPU devices. The default count is `1`.
<7> Specify the GPU device name, for example,`nvidia-a100`.
<8> Specify the worker count, for example, `3`.

** To attach multiple GPU devices, configure the `NodePool` resource by using the following example configuration:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  arch: amd64
  clusterName: <hosted_cluster_name>
  management:
    autoRepair: false
    upgradeType: Replace
  nodeDrainTimeout: 0s
  nodeVolumeDetachTimeout: 0s
  platform:
    kubevirt:
      attachDefaultNetwork: true
      compute:
        cores: <cpu>
        memory: <memory>
      hostDevices:
      - count: <count>
        deviceName: <gpu_device_name>
      - count: <count>
        deviceName: <gpu_device_name>
      - count: <count>
        deviceName: <gpu_device_name>
      - count: <count>
        deviceName: <gpu_device_name>
      networkInterfaceMultiqueue: Enable
      rootVolume:
        persistent:
          size: 32Gi
        type: Persistent
    type: KubeVirt
  replicas: <worker_node_count>
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-virt-evict-vms_{context}"]
= Evicting KubeVirt virtual machines

In cases where KubeVirt virtual machines (VMs) cannot be live migrated, such as when you use GPU passthrough, the VMs must be evicted at the same time as the `NodePool` resource of the hosted cluster. Otherwise, the compute nodes might be shut down without being drained from the workload. This might also happen when you are upgrading the {VirtProductName} Operator. To achieve a synchronized restart, you can set the `evictionStrategy` parameter on the `hyperconverged` resource to ensure that only VMs that are drained from workloads are rebooted.

.Procedure

. To learn more about the `hyperconverged` resource and the allowed values for the `evictionStrategy` parameter, enter the following command:
+
[source,terminal]
----
$ oc explain --api-version=hco.kubevirt.io/v1beta1 hyperconverged.spec.evictionStrategy
----

. Patch the `hyperconverged` resource by entering the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc patch -n {CNVNamespace} {HCOCliKind} kubevirt-hyperconverged \
  --type=merge \
  -p '{"spec": {"evictionStrategy": "External"}}'
----

. Patch the workload update strategy and the workload update methods by entering the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc patch -n {CNVNamespace} {HCOCliKind} kubevirt-hyperconverged \
  --type=merge \
  -p '{"spec": {"workloadUpdateStrategy": {"workloadUpdateMethods": ["LiveMigrate","Evict"]}}}'
----
+
By applying this patch, you specify that VMs should be live-migrated if possible, and that only the VMs that cannot be live-migrated should be evicted.

.Verification

* Check whether the patch command was applied properly by entering the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get -n {CNVNamespace} {HCOCliKind} kubevirt-hyperconverged -ojsonpath='{.spec.evictionStrategy}'
----
+
.Example output
[source,terminal]
----
External
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

[id="hcp-topology-spread-constraint_{context}"]
= Spreading node pool VMs by using topologySpreadConstraint

By default, KubeVirt virtual machines (VMs) created by a node pool are scheduled on any available nodes that have the capacity to run the VMs. By default, the `topologySpreadConstraint` constraint is set to schedule VMs on multiple nodes.

In some scenarios, node pool VMs might run on the same node, which can cause availability issues. To avoid distribution of VMs on a single node, use the descheduler to continuously honor the `topologySpreadConstraint` constraint to spread VMs on multiple nodes.

.Prerequisites

* You installed the {descheduler-operator}. For more information, see "Installing the descheduler".

.Procedure

* Open the `KubeDescheduler` custom resource (CR) by entering the following command, and then modify the `KubeDescheduler` CR to use the `SoftTopologyAndDuplicates` and `KubeVirtRelieveAndMigrate` profiles so that you maintain the `topologySpreadConstraint` constraint settings.
+
The `KubeDescheduler` CR named `cluster` runs in the `openshift-kube-descheduler-operator` namespace.
+
[source,terminal]
----
$ oc edit kubedescheduler cluster -n openshift-kube-descheduler-operator
----
+
.Example `KubeDescheduler` configuration
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  mode: Automatic
  managementState: Managed
  deschedulingIntervalSeconds: 30 # <1>
  profiles:
  - SoftTopologyAndDuplicates   # <2>
  - KubeVirtRelieveAndMigrate          # <3>
  profileCustomizations:
    devDeviationThresholds: AsymmetricLow
    devActualUtilizationProfile: PrometheusCPUCombined
# ...
----
<1> Sets the number of seconds between the descheduler running cycles.
<2> This profile evicts pods that follow the soft topology constraint: `whenUnsatisfiable: ScheduleAnyway`.
<3> This profile balances resource usage between nodes and enables the strategies, such as `RemovePodsHavingTooManyRestarts` and `LowNodeUtilization`.

[role="_additional-resources"]
.Additional resources

* Installing the descheduler
