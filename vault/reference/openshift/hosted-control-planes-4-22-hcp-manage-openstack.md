---
title: "Managing {hcp} on OpenStack"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-manage-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-manage-openstack
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Managing {hcp} on OpenStack

[id="hcp-manage-openstack"]
= Managing {hcp} on OpenStack

After you deploy {hcp} on {rh-openstack-first} agent machines, you can manage a hosted cluster by completing the
following tasks.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hcp-openstack-accessing_{context}"]
= Accessing the hosted cluster

You can access hosted clusters on {rh-openstack-first} by extracting the kubeconfig secret directly from resources by using the `oc` CLI.

The _hosted cluster (hosting)_ namespace contains hosted cluster resources and the access secrets. The _hosted control plane_ namespace is where the hosted control plane runs.

The secret name formats are as follows:

** `kubeconfig` secret: `<hosted_cluster_namespace>-<name>-admin-kubeconfig`. For example, `clusters-hypershift-demo-admin-kubeconfig`.
** `kubeadmin` password secret: `<hosted_cluster_namespace>-<name>-kubeadmin-password`. For example, `clusters-hypershift-demo-kubeadmin-password`.

The `kubeconfig` secret contains a Base64-encoded `kubeconfig` field. The `kubeadmin` password secret is also Base64-encoded; you can extract it and then use the password to log in to the API server or console of the hosted cluster.

.Prerequisites

* The `oc` CLI is installed.

.Procedure

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

. View a list of nodes of the hosted cluster to verify your access by entering the following command:
+
[source,terminal]
----
$ oc --kubeconfig ./hostedcluster-secrets/kubeconfig get nodes
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hcp-openstack-autoscale_{context}"]
= Enabling node auto-scaling for the hosted cluster

When you need more capacity in your hosted cluster on {rh-openstack-first} and spare agents are available, you can enable auto-scaling to install new worker nodes.

.Procedure

. To enable auto-scaling, enter the following command:
+
[source,terminal]
----
$ oc -n <hosted_cluster_namespace> patch nodepool <hosted_cluster_name> \
  --type=json \
  -p '[{"op": "remove", "path": "/spec/replicas"},{"op":"add", "path": "/spec/autoScaling", "value": { "max": 5, "min": 2 }}]'
----

. Create a workload that requires a new node.

.. Create a YAML file that contains the workload configuration, by using the following example:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: reversewords
  name: reversewords
  namespace: default
spec:
  replicas: 40
  selector:
    matchLabels:
      app: reversewords
  template:
    metadata:
      labels:
        app: reversewords
    spec:
      containers:
      - image: quay.io/mavazque/reversewords:latest
        name: reversewords
        resources:
          requests:
            memory: 2Gi
----

.. Save the file with the name `workload-config.yaml`.

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

. Wait for several minutes to pass without requiring the additional capacity. You can confirm that the node was removed by entering the following command:
+
[source,terminal]
----
$ oc --kubeconfig ./hostedcluster-secrets get nodes
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hcp-manage-openstack-az_{context}"]
= Configuring node pools for availability zones

You can distribute node pools across multiple {rh-openstack-first} Nova availability zones to improve the high availability of your hosted cluster.

NOTE: Availability zones do not necessarily correspond to fault domains and do not inherently provide high availability benefits.

.Prerequisites

* You created a hosted cluster.
* You have access to the management cluster.
* The `hcp` and `oc` CLIs are installed.

.Procedure

. Set environment variables that are appropriate for your needs. For example, if you want to create two additional machines in the `az1` availability zone, you could enter:
+
[source,terminal]
----
$ export NODEPOOL_NAME="${CLUSTER_NAME}-az1" \
  && export WORKER_COUNT="2" \
  && export FLAVOR="m1.xlarge" \
  && export AZ="az1"
----

. Create the node pool by using your environment variables by entering the following command:
+
[source,terminal]
----
$ hcp create nodepool openstack \
  --cluster-name <cluster_name> \
  --name $NODEPOOL_NAME \
  --replicas $WORKER_COUNT \
  --openstack-node-flavor $FLAVOR \
  --openstack-node-availability-zone $AZ
----
+
--
where:

`<cluster_name>`:: Specifies the name of your hosted cluster.
--

. Check the status of the node pool by listing `nodepool` resources in the clusters namespace by running the following command:
+
[source,terminal]
----
$ oc get nodepools --namespace clusters
----
+
.Example output
[source,terminal]
----
NAME                      CLUSTER         DESIRED NODES   CURRENT NODES   AUTOSCALING   AUTOREPAIR   VERSION   UPDATINGVERSION   UPDATINGCONFIG   MESSAGE
example                   example         5               5               False         False        4.17.0
example-az1               example         2                               False         False                  True              True             Minimum availability requires 2 replicas, current 0 available
----

. Observe the notes as they start on your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig $CLUSTER_NAME-kubeconfig get nodes
----
+
.Example output
[source,terminal]
----
NAME                      STATUS   ROLES    AGE     VERSION
...
example-extra-az-zh9l5    Ready    worker   2m6s    v1.27.4+18eadca
example-extra-az-zr8mj    Ready    worker   102s    v1.27.4+18eadca
...
----

. Verify that the node pool is created by running the following command:
+
[source,terminal]
----
$ oc get nodepools --namespace clusters
----
+
.Example output
[source,terminal]
----
NAME              CLUSTER         DESIRED   CURRENT   AVAILABLE   PROGRESSING   MESSAGE
<node_pool_name>  <cluster_name>  2         2         2           False         All replicas are available
----

[id="hosted-clusters-openstack-additional-ports"]
== Configuring additional ports for node pools

You can configure additional ports for node pools to support advanced networking scenarios, such as SR-IOV or multiple networks.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hosted-clusters-openstack-addl-ports-cases_{context}"]
= Use cases for additional ports for node pools

Common reasons to configure additional ports for node pools include the following:

SR-IOV (Single Root I/O Virtualization):: Enables a physical network device to appear as multiple virtual functions (VFs). By attaching additional ports to node pools, workloads can use SR-IOV interfaces to achieve low-latency, high-performance networking.

DPDK (Data Plane Development Kit):: Provides fast packet processing in user space, bypassing the kernel. Node pools with additional ports can expose interfaces for workloads that use DPDK to improve network performance.

Manila RWX volumes on NFS:: Supports `ReadWriteMany` (RWX) volumes over NFS, allowing multiple nodes to access shared storage. Attaching additional ports to node pools enables workloads to reach the NFS network used by Manila.

Multus CNI:: Enables pods to connect to multiple network interfaces. Node pools with additional ports support use cases that require secondary network interfaces, including dual-stack connectivity and traffic separation.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hosted-clusters-openstack-addl-ports-options_{context}"]
= Options for additional ports for node pools

You can use the `--openstack-node-additional-port` flag to attach additional ports to nodes in a hosted cluster on OpenStack. The flag takes a list of comma-separated parameters. Parameters can be used multiple times to attach multiple additional ports to the nodes.

The parameters are:

|===
|Parameter|Description|Required|Default

|`network-id`
|The ID of the network to attach to the node.
|Yes
|N/A

|`vnic-type`
|The VNIC type to use for the port. If not specified, Neutron uses the default type `normal`.
|No
|N/A

|`disable-port-security`
|Whether to disable port security for the port. If not specified, Neutron enables port security unless it is explicitly disabled at the network level.
|No
|N/A

|`address-pairs`
|A list of IP address pairs to assign to the port. The format is `ip_address=mac_address`. Multiple pairs can be provided, separated by a hyphen (`-`). The `mac_address` portion is optional.
|No
|N/A
|===

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

[id="hosted-clusters-openstack-addl-ports_{context}"]
= Creating additional ports for node pools

You can configure additional ports for node pools for hosted clusters that run on {rh-openstack-first}.

.Prerequisites

* You created a hosted cluster.
* You have access to the management cluster.
* The `hcp` CLI is installed.
* Additional networks are created in {rh-openstack}.
* The project that is used by the hosted cluster must have access to the additional networks.
* You reviewed the options that are listed in "Options for additional ports for node pools".

.Procedure

* Create a hosted cluster with additional ports attached to it by running the `hcp create nodepool openstack` command with the `--openstack-node-additional-port` options. For example:
+
[source,terminal]
----
$ hcp create nodepool openstack \
  --cluster-name <cluster_name> \
  --name <nodepool_name> \
  --replicas <replica_count> \
  --openstack-node-flavor <flavor> \
  --openstack-node-additional-port "network-id=<sriov_net_id>,vnic-type=direct,disable-port-security=true" \
  --openstack-node-additional-port "network-id=<lb_net_id>,address-pairs:192.168.0.1-192.168.0.2"
----
+
--
where:

`<cluster_name>`:: Specifies the name of the hosted cluster.
`<nodepool_name>`:: Specifies the name of the node pool.
`<replica_count>`:: Specifies the desired number of replicas.
`<flavor>`:: Specifies the {rh-openstack} flavor to use.
`<sriov_net_id>`:: Specifies a SR-IOV network ID.
`<lb_net_id>`:: Specifies a load balancer network ID.
--

[id="hosted-clusters-openstack-performance"]
== Configuring additional ports for node pools

You can tune hosted cluster node performance on {rh-openstack} for high-performance workloads, such as cloud-native network functions (CNFs). Performance tuning includes configuring {rh-openstack} resources, creating a performance profile, deploying a tuned `NodePool` resource, and enabling SR-IOV device support.

CNFs are designed to run in cloud-native environments. They can provide network services such as routing, firewalling, and load balancing. You can configure the node pool to use high-performance computing and networking devices to run CNFs.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack

[id="hosted-clusters-openstack-performance-tuning_{context}"]
= Tuning performance for hosted cluster nodes

Create a performance profile and deploy a tuned `NodePool` resource to run high-performance workloads on {rh-openstack-first} {hcp}.

.Prerequisites

* You have {rh-openstack} flavor that has the necessary resources to run your workload, including dedicated CPU, memory, and host aggregate information.
* You have an {rh-openstack} network that is attached to SR-IOV or DPDK-capable NICs. The network must be available to the project used by hosted clusters.

.Procedure

. Create a performance profile that meets your requirements in a file called `perfprofile.yaml`. For example:
+
.Example performance profile in a config map
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: perfprof-1
  namespace: clusters
data:
  tuning: |
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cnf-performanceprofile
      namespace: "${HYPERSHIFT_NAMESPACE}"
    data:
      tuning: |
        apiVersion: performance.openshift.io/v2
        kind: PerformanceProfile
        metadata:
          name: cnf-performanceprofile
        spec:
          additionalKernelArgs:
            - nmi_watchdog=0
            - audit=0
            - mce=off
            - processor.max_cstate=1
            - idle=poll
            - intel_idle.max_cstate=0
            - amd_iommu=on
          cpu:
            isolated: "${CPU_ISOLATED}"
            reserved: "${CPU_RESERVED}"
          hugepages:
            defaultHugepagesSize: "1G"
            pages:
              - count: ${HUGEPAGES}
                node: 0
                size: 1G
          nodeSelector:
            node-role.kubernetes.io/worker: ''
          realTimeKernel:
            enabled: false
          globallyDisableIrqLoadBalancing: true
----
+
IMPORTANT: If you do not already have environment variables set for the HyperShift Operator namespace, isolated and reserved CPUs, and huge pages count, create them before applying the performance profile.

. Apply the performance profile configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f perfprof.yaml
----

. If you do not already have a `CLUSTER_NAME` environment variable set for the name of your cluster, define it.

. Set a node pool name environment variable by running the following command:
+
[source,terminal]
----
$ export NODEPOOL_NAME=$CLUSTER_NAME-cnf
----

. Set a flavor environment variable by running the following command:
+
[source,terminal]
----
$ export FLAVOR="m1.xlarge.nfv"
----

. Create a node pool that uses the performance profile by running the following command:
+
[source,terminal]
----
$ hcp create nodepool openstack \
  --cluster-name $CLUSTER_NAME \
  --name $NODEPOOL_NAME \
  --node-count 0 \
  --openstack-node-flavor $FLAVOR
----

. Patch the node pool to reference the `PerformanceProfile` resource by running the following command:
+
[source,terminal]
----
$ oc patch nodepool -n ${HYPERSHIFT_NAMESPACE} ${CLUSTER_NAME} \
  -p '{"spec":{"tuningConfig":[{"name":"cnf-performanceprofile"}]}}' --type=merge
----

. Scale the node pool by running the following command:
+
[source,terminal]
----
$ oc scale nodepool/$CLUSTER_NAME --namespace ${HYPERSHIFT_NAMESPACE} --replicas=1
----

. Wait for the nodes to be ready:

.. Wait for the nodes to be ready by running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=UpdatingConfig=True nodepool \
  -n ${HYPERSHIFT_NAMESPACE} ${CLUSTER_NAME} \
  --timeout=5m
----

.. Wait for the configuration update to finish by running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=UpdatingConfig=False nodepool \
  -n ${HYPERSHIFT_NAMESPACE} ${CLUSTER_NAME} \
  --timeout=30m
----

.. Wait until all nodes are healthy by running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=AllNodesHealthy nodepool \
  -n ${HYPERSHIFT_NAMESPACE} ${CLUSTER_NAME} \
  --timeout=5m
----

NOTE: You can make an SSH connection into the nodes or use the `oc debug` command to verify performance configurations.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-openstack

[id="hosted-clusters-openstack-performance-enabling_{context}"]
= Enabling the SR-IOV Network Operator in a hosted cluster

You can enable the SR-IOV Network Operator to manage SR-IOV-capable devices on nodes deployed by the `NodePool` resource. The operator runs in the hosted cluster and requires labeled worker nodes.

.Procedure

. Generate a `kubeconfig` file for the hosted cluster by running the following command:
+
[source,terminal]
----
$ hcp create kubeconfig --name $CLUSTER_NAME > $CLUSTER_NAME-kubeconfig
----

. Create a `kubeconfig` resource environment variable by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=$CLUSTER_NAME-kubeconfig
----

. Label each worker node to indicate SR-IOV capability by running the following command:
+
[source,terminal]
----
$ oc label node <worker_node_name> feature.node.kubernetes.io/network-sriov.capable=true
----
+
--
where:

`<worker_node_name>`:: Specifies the name of a worker node in the hosted cluster.
--

. Install the SR-IOV Network Operator in the hosted cluster by following the instructions in "Installing the SR-IOV Network Operator".

. After installation, configure SR-IOV workloads in the hosted cluster by using the same process as for a standalone cluster.

[role="_additional-resources"]
.Additional resources

* Installing the SR-IOV Network Operator
