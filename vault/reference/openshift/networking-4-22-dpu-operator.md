---
title: "DPU Operator"
type: reference
domain: openshift
slug: networking-4-22-dpu-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/dpu-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# DPU Operator

[id="dpu-operator"]
= DPU Operator

[role="_abstract"]
As a cluster administrator, you can add the Data Processing Unit (DPU) Operator to your cluster to manage DPU devices and network attachments.

--

--

// About DPU and the DPU Operator
// Module included in the following assemblies:
//
// * networking/metallb/about-dpu.adoc

[id="nw-about-dpu_{context}"]
= Orchestrating DPUs with the DPU Operator

[role="_abstract"]
You can use the Data Processing Unit (DPU) Operator to manage DPUs that offload networking, storage, and security workloads from host CPUs to improve cluster performance and efficiency.

A DPU is a type of programmable processor that represents one of the three fundamental pillars of computing, alongside CPUs and GPUs. While CPUs handle general computing tasks and GPUs accelerate specific workloads, the primary role of the DPU is to offload and accelerate data-centric workloads, such as networking, storage, and security functions.

DPUs are typically used in data centers and cloud environments to improve performance, reduce latency, and enhance security by offloading these tasks from the CPU. You can also use DPUs to create a more efficient and flexible infrastructure by enabling the deployment of specialized workloads closer to the data source.

The DPU Operator is responsible for managing the DPU devices and network attachments. The DPU Operator deploys the DPU daemon onto OpenShift Container Platform compute nodes that interface through an API controlling the DPU daemon running on the DPU. The DPU Operator is responsible for the life-cycle management of the `ovn-kube` components and the necessary host network initialization on the DPU.

The following table describes the currently supported DPU devices.

.Supported devices
[cols="1,1,1,2", options="header"]
|===
| Vendor | Device | Firmware | Description

| Intel | IPU E2100 | Version 2.0.0.11126 or later | A DPU designed to offload networking, storage, and security tasks from host CPUs in data centers, improving efficiency and performance. For instructions on deploying a full end-to-end solution, see the Red{nbsp}Hat Knowledgebase solution Accelerating Confidential AI on OpenShift with the Intel E2100 IPU, DPU Operator, and F5 NGINX.
| Senao | SX904 | 35.23.47.0008 or later | A SmartNIC designed to offload compute and network services from the host CPUs in data centers and edge computing environments, improving efficiency and isolation of workloads.
| Marvell | Marvell Octeon 10 CN106 | SDK12.25.01 or later | A DPU designed to offload workloads that require high speed data processing from host CPUs in data centers and edge computing environments, improving performance and energy efficiency
|===
[NOTE]
====
The NVIDIA BlueField-3 is not supported.
====

// Installing the DPU Operator
// Module included in the following assemblies:
//
// * networking/networking_operators/installing-dpu-operator.adoc

[id="overview-installing-dpu-operator_{context}"]
= Installing the DPU Operator

[role="_abstract"]
You can install the Data Processing Unit (DPU) Operator on both host and DPU clusters to manage device lifecycle and network attachments by using the CLI or web console.

Cluster administrators can install the DPU Operator on the host cluster and all DPU clusters by using the OpenShift Container Platform CLI or the web console. The DPU Operator manages the lifecycle, DPU devices, and network attachments for all supported DPUs.

[NOTE]
====
You need to install the DPU Operator on the host cluster and each of the DPU clusters.
====

// Module included in the following assemblies:
//
// * networking/networking_operators/installing-dpu-operator.adoc

[id="nw-dpu-installing-operator-cli_{context}"]
= Installing the DPU Operator by using the CLI

[role="_abstract"]
You can install the DPU Operator by using the CLI. You can use the DPU Operator to simplify the installation process when setting up DPU device management on host clusters.

As a cluster administrator, you can install the DPU Operator by using the CLI.

[NOTE]
====
The CLI must be used to install the DPU Operator on the DPU cluster.
====

.Prerequisites

* Install the OpenShift CLI (`oc`).
* An account with `cluster-admin` privileges.

.Procedure

. Create the `openshift-dpu-operator` namespace by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-dpu-operator
  annotations:
    workload.openshift.io/allowed: management
EOF
----

. Create an `OperatorGroup` custom resource (CR) by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: dpu-operators
  namespace: openshift-dpu-operator
spec:
  targetNamespaces:
  - openshift-dpu-operator
EOF
----

. Create a `Subscription` CR for the DPU Operator by entering the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-dpu-operator-subscription
  namespace: openshift-dpu-operator
spec:
  channel: stable
  name: dpu-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
----

.Verification

. To verify that the Operator is installed, enter the following command and then check that output shows `Succeeded` for the Operator:
+
[source,terminal]
----
$ oc get csv -n openshift-dpu-operator \
  -o custom-columns=Name:.metadata.name,Phase:.status.phase
----

. Change to the `openshift-dpu-operator` project:
+
[source,terminal]
----
$ oc project openshift-dpu-operator
----

. Verify the DPU Operator is running by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-dpu-operator
----
+
.Example output
[source,terminal]
----
NAME                                               READY   STATUS    RESTARTS   AGE
dpu-operator-controller-manager-6b7bbb5db8-7lvkj   2/2     Running   0          2m9s
----

// Module included in the following assemblies:
//
// * networking/networking_operators/installing-dpu-operator.adoc

[id="nw-dpu-installing-operator-ui_{context}"]
= Installing the DPU Operator using the web console

[role="_abstract"]
You can install the DPU Operator by using the web console. You can use the DPU Operator to simplify the installation process when setting up DPU device management on host clusters.

As a cluster administrator, you can install the DPU Operator by using the web console.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* An account with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

. Select *DPU Operator* from the list of available Operators, and then click *Install*.

. On the *Install Operator* page, under *Installed Namespace*, the *Operator recommended Namespace* option is preselected by default. No action is required.

.. Click *Install*.

.Verification

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Ensure that the *openshift-dpu-operator* project lists *DPU Operator* with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status.
If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

.Troubleshooting

* Inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.

* Navigate to the *Workloads* -> *Pods* page and check the logs for pods in the `openshift-dpu-operator` project.

* Check the namespace of the YAML file. If the annotation is missing, you can add the annotation `workload.openshift.io/allowed=management` to the Operator namespace with the following command:
+
[source,terminal]
----
$ oc annotate ns/openshift-dpu-operator workload.openshift.io/allowed=management
----
+
[NOTE]
====
For {sno} clusters, the annotation `workload.openshift.io/allowed=management` is required for the namespace.
====

// Module included in the following assemblies:
//
// * networking/networking_operators/configuring-dpu-operator.adoc

[id="nw-dpu-configuring-operator_{context}"]
= Configuring the DPU Operator

[role="_abstract"]
You can configure the DPU Operator after installation to enable management of DPU devices and network attachments in both dual cluster and single cluster deployment modes.

You can configure the DPU Operator to manage the DPU devices and network attachments in your cluster.

To configure the DPU Operator follow these steps:

.Procedure

. Create the `DpuOperatorConfig` Custom Resource (CR) based on your deployment mode:

* Dual Cluster Deployment: You must create the `DpuOperatorConfig` CR on both the host OpenShift Container Platform cluster and on each of the {ms} DPU clusters.
* Single Cluster Deployment: This deployment uses a standard OpenShift Container Platform cluster. You only need to create the `DpuOperatorConfig` CR once on this cluster.
+
The content of the CR is the same for all clusters.

. Create a file named `dpu-operator-config.yaml` by using the following YAML:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DpuOperatorConfig
metadata:
 name: dpu-operator-config
spec:
 logLevel: 0
----
+
* `metadata.name`: Specifies the name of the Custom Resource, which must be `dpu-operator-config`.
* `spec.logLevel`: Sets the required logging verbosity in the Operator container logs. The value `0` is the default setting.

. Create the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f dpu-operator-config.yaml
----

. Label all nodes that either have an attached DPU or are functioning as a DPU. You can apply this label by running the following command:
+
[source,terminal]
----
$ oc label node <node_name> dpu=true
----
+
where:
+
`node_name`:: Refers to the name of your node, such as `worker-1`.
+
[NOTE]
====
There are two ways to deploy clusters that are compatible with DPUs:

* Dual cluster deployment: This consists of OpenShift Container Platform running on the hosts and {ms} running on the DPU. In this mode, the {ms} instance also needs to deploy the DPU Operator, and you must set the label `dpu=true` on the node.
* Single cluster deployment: This consists of only OpenShift Container Platform running on hosts, where the DPUs are integrated into the main cluster. DPUs just require the label `dpu=true` for both the host nodes with DPUs installed and the DPU nodes themselves. The DPU Operator automatically detects the role of the node whether it is running as a DPU or a host with an attached DPU.
====

// Running workloads on the DPU Operator
// Module included in the following assemblies:
//
// * networking/networking_operators/nw-dpu-running-workloads.adoc

[id="nw-running-workloads-dpu_{context}"]
= Running a workload on the host with DPU

[role="_abstract"]
You can deploy workloads on the host with DPU to offload specialized infrastructure tasks and improve performance while freeing up host CPU resources.

Running workloads on a DPU enables offloading specialized infrastructure tasks such as networking, security, and storage to a dedicated processing unit. This improves performance, enforces a stronger security boundary between infrastructure and application workloads, and frees up host CPU resources.

Follow these steps to deploy a workload on the host with DPU. This is the standard deployment model where the application runs on the host's x86 CPU but utilizes the DPU for network acceleration and offload.

.Prerequisites

* The OpenShift CLI (`oc`) is installed.
* An account with `cluster-admin` privileges is available.
* The DPU Operator is installed.

.Procedure

. Create a sample workload designed to run on the host-side worker node by using the following YAML. Save the file as `workload-host.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: default-sriov-net
spec:
  nodeSelector:
    kubernetes.io/hostname: worker-237
  containers:
  - name: appcntr1
    image: registry.access.redhat.com/ubi9/ubi:latest
    command: ['/bin/sh', '-c', 'sleep infinity']
    imagePullPolicy: Always
    securityContext:
      priviledged: true
      runAsNonRoot: false
      runAsUser: 0
      seccompProfile:
        type: RuntimeDefault
    resources:
      requests:
        openshift.io/dpu: '1'
      limits:
        openshift.io/dpu: '1'
----
+
`spec.nodeSelector`: The node selector schedules the pod on the node with the DPU resource. You can use any standard Kubernetes selector for this, such as `kubernetes.io/hostname`, to target a specific node as shown in the example YAML.
+
[NOTE]
====
For flexible scheduling, the DPU Operator creates the label dpu.config.openshift.io/dpuside: "dpu-host". This label enables the default scheduler to place the workload on any host with a DPU. The workload automatically joins that DPU secondary network.
When the label on the node is `dpu.config.openshift.io/dpuside: "dpu"`, this signifies that the node is the DPU itself. The DPU Operator creates and manages the `dpu.config.openshift.io/dpuside` label .
====

. Create the workload by running the following command:
+
[source,terminal]
----
$ oc apply -f workload-host.yaml
----

// Module included in the following assemblies:
//
// * networking/networking_operators/nw-dpu-running-workloads.adoc

[id="nw-dpu-creating-a-sfc_{context}"]
= Running a workload on the DPU

[role="_abstract"]
You can deploy network workloads directly on the DPU to improve performance, enhance security isolation, and reduce host CPU usage.

The DPU offloads network workloads, such as security functions or virtualized appliances, to improve performance, enhance security isolation, and free host CPU resources.

Follow this procedure to deploy a simple pod directly onto the DPU.

.Prerequisites

* Install the {oc-first}.
* An account with `cluster-admin` privileges.
* Install the DPU Operator.

.Procedure

. Save the following YAML file example as `dpu-pod.yaml`. This is an example of a simple pod that will be scheduled directly onto a DPU node by the Kubernetes default scheduler.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: "my-network-function"
  namespace: openshift-dpu-operator
  annotations:
    k8s.v1.cni.cncf.io/networks: dpunfcni-conf, dpunfcni-conf
spec:
  nodeSelector:
    dpu.config.openshift.io/dpuside: "dpu"
  containers:
    - name: "my-network-function"
      image: "quay.io/example-org/my-network-function:latest"
      resources:
        requests:
          openshift.io/dpu: "2"
        limits:
          openshift.io/dpu: "2"
      securityContext:
        privileged: true
        capabilities:
          drop:
            - ALL
          add:
            - NET_RAW
            - NET_ADMIN
----
+
* `metadata.name.annotations.k8s.v1.cni.cncf.io/networks`: The value `dpunfcni-conf` specifies the name of the `NetworkAttachmentDefinition` resource. The DPU Operator creates this resource during installation to configure the DPU networking.
* `spec.nodeSelector`: The `nodeSelector` is the primary mechanism for scheduling this workload. The DPU Operator creates and maintains the label: `dpu.config.openshift.io/dpuside: "dpu"`. This label ensures the pod is scheduled directly onto the DPU processing unit.
* `spec.containers.name`: The name of the container.
* `spec.containers.image`: The container image to pull and run.

. Create the pod by running the following command:
+
[source,terminal]
----
$ oc apply -f dpu-pod.yaml
----

. Verify the pod status by running the following command:
+
[source,bash]
----
$ oc get pods -n openshift-dpu-operator
----
+
Ensure the pod's status is `Running`.

// Module included in the following assemblies:
//
// * networking/networking_operators/nw-dpu-running-workloads.adoc

[id="nw-dpu-monitoring-status_{context}"]
= Monitoring the status of DPU

[role="_abstract"]
You can monitor the DPU infrastructure status to check the current state and health of your DPU devices across the cluster.

You can monitor the DPU status to see the current state of the DPU infrastructure.

The `oc get dpu` command shows the current state of the DPU infrastructure. Follow this procedure to monitor the status of various cards.

.Prerequisites

* The OpenShift CLI (`oc`) is installed.
* An account with `cluster-admin` privileges is available.
* The DPU Operator is installed.

.Procedure

. Run the following command to check the overall health of your nodes:
+
[source,terminal]
----
$ oc get nodes
----
+
The example output provides a list of all nodes in the cluster along with their status. Ensure that all nodes are in the `Ready` state before proceeding.
+
[source,terminal]
----
NAME                           STATUS   ROLES    AGE    VERSION
ocpcluster-master-1            Ready    master   10d    v1.32.9
ocpcluster-master-2            Ready    master   10d    v1.32.9
ocpcluster-master-3            Ready    master   10d    v1.32.9
ocpcluster-dpu-ipu-219         Ready    worker   42h    v1.32.9
ocpcluster-dpu-marvell-41      Ready    worker   3d23h  v1.32.9
ocpcluster-dpu-ptl-243         Ready    worker   3d23h  v1.32.9
worker-host-ipu-219            Ready    worker   3d19h  v1.32.9
worker-host-marvell-41         Ready    worker   4d     v1.32.9
worker-host-ptl-243            Ready    worker   3d23h  v1.32.9
----
+
This output shows three control plane nodes, and three worker nodes identified by the worker-host prefix, for example, `worker-host-ipu-219`. Each worker node has a DPU identified by the ocpcluster-dpu prefix, for example, `ocpcluster-dpu-ipu-219`.

. Run the following command to report on the status of the DPUs:
+
[source,terminal]
----
$ oc get dpu
----
+
The example output provides a list of detected DPUs.
+
[source,terminal]
----
NAME                                 DPU PRODUCT                    DPU SIDE        MODE NAME               STATUS
030001163eec00ff-host                Intel Netsec Accelerator       false           worker-host-ptl-243     True
d4-e5-c9-00-ec-3v-dpu                Intel Netsec Accelerator       true            worker-dpu-ptl-243      True
intel-ipu-0000-06-00.0-host          Intel IPU E2100                false           worker-host-ipu-219     False
intel-ipu-dpu                        Intel IPU E2100                true            worker-dpu-ipu-219      False
marvell-dpu-0000-87-00.0-host        Marvell DPU                    false           worker-host-marvell-41  True
marvell-dpu-ipu                      Marvell DPU                    true            worker-dpu-marvell-41   True
----
where:

`DPU PRODUCT`:: Displays the vendor or type of DPU, for example, Intel or Marvell.
`DPU SIDE`:: Indicates whether the DPU is operating on the host side (`false`) or the DPU side (`true`). Each physical DPU is represented twice.
`MODE NAME`:: The name of the node where the DPU is located. This is the host worker node for `false` entries and the DPU node for `true` entries.
`STATUS`:: Indicates whether the DPU is functioning correctly (`True`) or has issues (`False`).
+
[NOTE]
====
Run `oc get dpu -o yaml` to get more details about the status.
====

// Module included in the following assemblies:
//
// * networking/networking_operators/uninstalling-dpu-operator.adoc

[id="nw-dpu-operator-uninstall_{context}"]
= Uninstalling the DPU Operator

[role="_abstract"]
You can uninstall the DPU Operator from your cluster when you no longer need DPU device management, ensuring all workloads are deleted first.

To uninstall the DPU Operator, you must first delete any running DPU workloads. Follow this procedure to uninstall the DPU Operator.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have the DPU Operator installed.

.Procedure

. Delete the `DpuOperatorConfig` CR by running the following command:
+
[source,terminal]
----
$ oc delete DpuOperatorConfig dpu-operator-config
----

. Delete the subscription that was used to install the DPU Operator by running the following command:
+
[source,terminal]
----
$ oc delete Subscription openshift-dpu-operator-subscription -n openshift-dpu-operator
----

. Remove the `OperatorGroup` resource that was created by running the following command:
+
[source,terminal]
----
$ oc delete OperatorGroup dpu-operators -n openshift-dpu-operator
----

. Uninstall the DPU Operator as follows:

.. Check the installed Operators by running the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-dpu-operator
----
+
The following example shows the output:
+
[source,terminal]
----
NAME                                DISPLAY        VERSION               REPLACES   PHASE
dpu-operator.v4.22.0-202503130333   DPU Operator   4.22.0-202503130333              Failed
----

.. Delete the DPU Operator by running the following command:
+
[source,terminal]
----
$ oc delete csv dpu-operator.v4.22.0-202503130333 -n openshift-dpu-operator
----

. Delete the namespace that was created for the DPU Operator by running the following command:
+
[source,terminal]
----
$ oc delete namespace openshift-dpu-operator
----

.Verification

. Verify that the DPU Operator is uninstalled by running the following command. An example of successful command output is `No resources found in openshift-dpu-operator namespace`.
+
[source,terminal]
----
$ oc get csv -n openshift-dpu-operator
----

[role="_additional-resources"]
.Additional resources

* Deleting Operators from a cluster
