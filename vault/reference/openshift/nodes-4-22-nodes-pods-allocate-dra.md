---
title: "Allocating GPUs to pods by using DRA"
type: reference
domain: openshift
slug: nodes-4-22-nodes-pods-allocate-dra
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-pods-allocate-dra
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Allocating GPUs to pods by using DRA

[id="nodes-pods-allocate-dra"]
= Allocating GPUs to pods by using DRA

// Taken from https://issues.redhat.com/browse/OCPSTRAT-1756
// Naming taken from https://issues.redhat.com/browse/OCPSTRAT-2384. Is this correct?

[role="_abstract"]
You can use {attribute-based-full} to enable fine-tuned control over graphics processing unit (GPU) resource allocation in OpenShift Container Platform, allowing pods to request GPUs based on specific device attributes, including product name, GPU memory capacity, compute capability, vendor name and driver version. Having access to these attributes, which are exposed by a third-party Dynamic Resource Allocation (DRA) driver, allows OpenShift Container Platform to schedule a pod on a node that has the specific devices that the workload needs.

This workflow provides significant improvement in the device allocation workflow when compared to device plugins, which require per-container device requests, do not support device sharing, and do not support expression-based device filtering.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-allocate-dra.adoc

[id="nodes-pods-allocate-dra-about_{context}"]
= About GPU attributes

// Taken from https://issues.redhat.com/browse/OCPSTRAT-1756
[role="_abstract"]
You can use {attribute-based-full} to enable pods to be scheduled on nodes that have specific graphics processing units (GPU). These attributes are advertised to the cluster by using a Dynamic Resource Allocation (DRA) driver, a third-party application that runs on each node in your cluster.

The DRA driver manages and exposes specialized resources within your cluster by interacting with the underlying hardware and advertising it to the OpenShift Container Platform control plane. You must install a DRA driver in your cluster. Installation of the DRA driver is beyond the scope of this documentation. Some DRA device drivers can also slice GPU memory, making it available to multiple workloads.

The DRA driver advertises several GPU device attributes that OpenShift Container Platform can use for precise GPU selection, including the following attributes:

Product Name::
Pods can request an exact GPU model based on performance requirements or compatibility with applications. This ensures that workloads leverage the best-suited hardware for their tasks.

GPU Memory Capacity::
Pods can request GPUs with a minimum or maximum memory capacity, such as 8 GB, 16 GB, or 40 GB. This is helpful with memory-intensive workloads such as large AI model training or data processing. This attribute enables applications to allocate GPUs that meet memory needs without overcommitting or underutilizing resources.

Compute Capability::
Pods can request GPUs based on the compute capabilities of the GPU, such as the CUDA versions supported. Pods can target GPUs that are compatible with the application’s framework and leverage optimized processing capabilities.

Power and Thermal Profiles::
Pods can request GPUs based on power usage or thermal characteristics, enabling power-sensitive or temperature-sensitive applications to operate efficiently. This is particularly useful in high-density environments where energy or cooling constraints are factors.

Device ID and Vendor ID::
Pods can request GPUs based on the GPU's hardware specifics, which allows applications that require specific vendors or device types to make targeted requests.

Driver Version::
Pods can request GPUs that run a specific driver version, ensuring compatibility with application dependencies and maximizing GPU feature access.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-allocate-dra.adoc

[id="nodes-pods-allocate-dra-configure-about_{context}"]
= About GPU allocation objects and concepts

// Taken from https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#terminology
[role="_abstract"]
You can use the following {attribute-based-full} objects and concepts to ensure that a workload is scheduled on a node with the graphics processing unit (GPU) specifications it needs. You should be familiar with these objects before proceeding.

Device class::
A device class is a category of devices that pods can claim. Some device drivers contain their own device class. Alternatively, an administrator can create device classes. A device class contains a device selector, which is a common expression language (CEL) expression that must evaluate to true if a device satisfies the request.
+
The following example `DeviceClass` object selects any device that is managed by the `driver.example.com` device driver:
+
.Example device class object
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: DeviceClass
metadata:
  name: example-device-class
spec:
  selectors:
  - cel:
      expression: |-
        device.driver == "driver.example.com"
----
+
--
where:

`spec.selectors`:: Specifies a CEL expression for selecting a device.
--

Resource slice::
The DRA driver on each node creates and manages _resource slices_, which describe what resources are available in that cluster. A resource slice represents one or more GPU resources that are attached to nodes. The DRA can allocate either a full device or fixed-size partitions of full devices.
+
A partitionable device is a single physical hardware device that can be split into smaller, logical instances, such as Multi-Instance GPUs, based on workload demands. By partitioning devices, you can safely and efficiently share expensive accelerators across multiple pods.
+
--
--
+
To allocate partitions, the DRA creates a _counter set_, which is a set of named _counters_. The counters represent the resources available on the physical device that are used by the logical devices advertised through DRA.
+
Logical devices can specify the `consumesCounters` list in a resource slice. Each entry contains a reference to a counter set and a set of named counters with the amounts they can consume.
+
When a resource claim is created and used in a pod, OpenShift Container Platform uses the resource slices to find nodes that have the requested resources. After finding an eligible resource slice for the resource claim, the OpenShift Container Platform scheduler updates the resource claim with the allocation details, allocates resources to the resource claim, and schedules the pod onto a node that can access the resources.
+
.Example resource slice object for a device
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: resource.k8s.io/v1
  kind: ResourceSlice
# ...
spec:
  driver: driver.example.com
  nodeName: dra-example-driver
  pool:
    generation: 0
    name: dra-example-driver
    resourceSliceCount: 1
  devices:
  - attributes:
      driverVersion:
        version: 1.0.0
      index:
        int: 0
      model:
        string: LATEST-GPU-MODEL
      uuid:
        string: gpu-18db0e85-99e9-c746-8531-ffeb86328b39
    capacity:
      memory:
        value: 10Gb
    name: 2g-10gb
# ...
----
+
--
where:

`spec.driver`:: Specifies the name of the DRA driver, which you can specify in a device class.

`spec.devices.attributes`:: Specifies a device that you can allocate by using a resource claim or resource claim template.
--
+
.Example resource slice object for a partitionable device
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: counter-slice
spec:
  driver: "resource-driver.example.com"
  nodeName: dra-example-driver
  pool:
    generation: 1
    name: "my-pool"
    resourceSliceCount: 2
  sharedCounters:
  - name: gpu-0-counter-set
    counters:
      memory:
        value: 40Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: device-slice
spec:
  driver: "resource-driver.example.com"
  pool:
    generation: 1
    name: "my-pool"
    resourceSliceCount: 2
  nodeName: "my-node"
  devices:
  - name: gpu-0
    capacity:
      memory:
        value: 40Gi
    consumesCounters:
    - counterSet: gpu-0-counter-set
      counters:
        memory:
          value: 40Gi
  - name: gpu-0-partition-0
    capacity:
      memory:
        value: 20Gi
    consumesCounters:
    - counterSet: gpu-0-counter-set
      counters:
        memory:
          value: 20Gi
  - name: gpu-0-partition-1
    capacity:
      memory:
        value: 20Gi
    consumesCounters:
    - counterSet: gpu-0-counter-set
      counters:
        memory:
          value: 20Gi
----
+
--
where:

`spec.driver`:: Specifies the name of the DRA driver, which you can specify in a device class.

`spec.sharedCounters`:: Specifies the counter set and counters.

`spec.devices`:: Specifies a list of devices that can be requested by pods.

`spec.devices.name`:: Specifies the details of a single device.

`spec.devices.consumesCounters`:: Specifies how much of a shared counter set the device consumes if allocated.
--
+
In this example, the `resource-driver.example.com` DRA driver is sharing 40Gi of memory through the `gpu-0-counter-set` counter set in the `counter-slice` object. The `device-slice` object makes this memory available as a full device named _gpu-0_ or either of two partitioned devices named _gpu-0-partition-0_ and _gpu-0-partition-1_. Each device has a capacity and declares how much it consumes from the counter when allocated, either 40Gi for the full device or 20Gi of memory for each partition. You can allocate the memory by using either the full device or the partitions, but not both, enforcing mutual exclusivity between a full device and its partitions. When _gpu-0_ is allocated, the GPU consumes all 40Gi from the counter set, leaving 0Gi for the partitions.

Resource claim template::
Cluster administrators and operators can create a _resource claim template_, which describes the GPU resource that a pod requires. The administrator or operator adds the resource claim to a pod specification. OpenShift Container Platform uses the resource claim template to generate the resource claim for the pod. The OpenShift Container Platform scheduler then schedules that pod on a node in the cluster that has the requested GPU.
+
Each resource claim that OpenShift Container Platform generates from the template is bound that specific pod. A such, the GPU cannot be used simultaneously by another workload. When the pod terminates, OpenShift Container Platform deletes the corresponding resource claim.
+
You must specify either a request for a specific device that the scheduler must meet, or a provide a prioritized list of devices for the scheduler to choose from.
+
The following example resource claim template contains two sub-requests. Of these sub-requests, only one is selected by the scheduler. The scheduler tries to satisfy the sub-requests in the order in which they are listed. A CEL expression is used inside the sub-request for selecting a device.
+
.Example resource claim template object
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  namespace: gpu-claim
  name: gpu-devices
spec:
  spec:
    devices:
      requests:
      - name: req-0
        firstAvailable:
        - name: 2g-10gb
          deviceClassName: example-device-class
          selectors:
          - cel:
              expression: "device.attributes['driver.example.com'].profile == '2g.10gb'"
        - name: 3g-20gb
          deviceClassName: example-device-class
          selectors:
          - cel:
              expression: "device.attributes['driver.example.com'].profile == '3g.20gb'"
----
+
--
where:

`spec.spec.devices.requests`:: Specifies a list of one or more requests for devices. The sub-request must include either `exactly` or `firstAvailable`.
+
* `exactly`: Specifies a request for one or more identical devices. The devices must match the request exactly for the request to be satisfied. If the requested device is not available, the scheduler cannot create the pod.
* `firstAvailable`: Specifies multiple requests for a device, of which only one device needs to be available before the scheduler can create the requesting pod. The scheduler checks the availability of the devices in the order listed and selects the first available device. The scheduler can create the pod if one requested devices is available.

`spec.devices.requests.exactly.deviceClassName` or `spec.devices.requests.firstAvailable.deviceClassName`:: Specifies which device class to use with this request.

`spec.devices.requests.exactly.selectors` or `spec.devices.requests.firstAvailable.selectors`:: Specifies CEL expressions to request specific devices from the specified device class.
--

Resource claim::
Admins and operators can create a _resource claim_, which describes the GPU resource that a pod requires. The administrator or operator adds the resource claim to a pod specification. The OpenShift Container Platform scheduler then schedules that pod on a node in the cluster that has the requested GPU.
+
A resource claim can be used in multiple pod specifications, which allows you to share GPUs with multiple workloads. Resource claims are not deleted when a requesting pod is terminated.
+
For the device request in a resource claim, you must specify either a list of one or more device requests that the scheduler must meet, or a provide a prioritized list of requests for the scheduler to choose from.
+
The following example resource claim uses a CEL expression to request one device in the `example-device-class` device class. Here, the `exactly` parameter indicates that a node with the specific requested device must be available before the scheduler can create the pod.
+
.Example resource claim object
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  namespace: gpu-claim
  name: gpu-devices
spec:
  devices:
    requests:
    - name: req-0
      exactly:
        name: 2g-10gb
        deviceClassName: example-device-class
        selectors:
        - cel:
            expression: "device.attributes['driver.example.com'].profile == '2g.10gb'"
----

Admin access::
A cluster administrator can gain privileged access to a device that is in use by other users. This enables administrators to perform tasks such as monitoring the health and status of devices while ensuring that users can continue to use these devices with their workloads.
+
To gain admin access, an administrator must create a resource claim or resource claim template with the `adminAccess: true` parameter in a namespace that includes the `resource.kubernetes.io/admin-access: "true"` label. Non-administrator users cannot access namespaces with this label.
+
.Example namespace with admin access label
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    resource.kubernetes.io/admin-access: "true"
# ...
----
+
In the following example, the administrator is granted access to the `2g-10gb` device:
+
.Example resource claim object with admin access
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: large-black-cat-claim-template
spec:
  devices:
    requests:
    - name: req-0
      exactly:
        allocationMode: All
        adminAccess: true
        deviceClassName: example-device-class
        selectors:
        - cel:
            expression: "device.attributes['driver.example.com'].profile == '2g.10gb'"
----
+
--
where:

`spec.devices.requests.exactly.adminAccess.true` or `spec.devices.requests.firstAvailable.adminAccess.true`:: Specifies that the admin access mode is enabled for the specified device.
--

For information on adding resource claims to pods, see "Adding resource claims to pods".

// Module included in the following assemblies:
//
// * nodes/nodes-pods-allocate-dra.adoc

[id="nodes-pods-allocate-dra-configure_{context}"]
= Adding resource claims to pods

[role="_abstract"]
You can use resource claims and resource claim templates with {attribute-based-full} to allow you to request your workloads to be scheduled on nodes with specific graphics processing units (GPU).

Resource claims can be used with multiple pods, but resource claim templates can be used with only one pod. For more information, see "About GPU allocation objects and concepts".

The example in the following procedure creates a resource claim to schedule a pod on a node with the assign a specific GPU to  and a resource claim to share a GPU between `container1` and `container2`.

.Prerequisites

* A Dynamic Resource Allocation (DRA) driver is installed. For more information on DRA, see "Dynamic Resource Allocation" (Kubernetes documentation).
* A resource slice has been created.
* If your resource slice is allocating a partitioned device, you enabled the required Technology Preview features for your cluster by adding the `TechPreviewNoUpgrade` feature set to the `FeatureGate` CR named `cluster`. For information about enabling Feature Gates, see "Enabling features using feature gates".
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them. Do not enable this feature set on production clusters.
====

* A resource claim and/or resource claim template has been created.
+
.Example resource claim object
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  namespace: gpu-claim
  name: gpu-devices
spec:
  devices:
    requests:
    - name: req-0
      exactly:
        name: 2g-10gb
        deviceClassName: example-device-class
        selectors:
        - cel:
            expression: "device.attributes['driver.example.com'].profile == '2g.10gb'"
----
+
.Example resource claim template object
[source,yaml]
----
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  namespace: gpu-claim
  name: gpu-devices
spec:
  spec:
    devices:
      requests:
      - name: req-0
        firstAvailable:
        - name: 2g-10gb
          deviceClassName: example-device-class
          selectors:
          - cel:
              expression: "device.attributes['driver.example.com'].profile == '2g.10gb'"
        - name: 3g-20gb
          deviceClassName: example-device-class
          selectors:
          - cel:
              expression: "device.attributes['driver.example.com'].profile == '3g.20gb'"
----

.Procedure

. Create a pod by creating a YAML file similar to the following:
+
.Example pod that is requesting resources
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  namespace: gpu-allocate
  name: pod1
  labels:
    app: pod
spec:
  restartPolicy: Never
  containers:
  - name: container0
    image: ubuntu:24.04
    command: ["sleep", "9999"]
    resources:
      claims:
      - name: gpu-claim-template
  - name: container1
    image: ubuntu:24.04
    command: ["sleep", "9999"]
    resources:
      claims:
      - name: gpu-claim
  - name: container2
    image: ubuntu:24.04
    command: ["sleep", "9999"]
    resources:
      claims:
      - name: gpu-claim
  resourceClaims:
  - name: gpu-claim-template
    resourceClaimTemplateName: gpu-devices-template
  - name: gpu-claim
    resourceClaimName: gpu-devices
----
+
--
where:

`spec.container.resource.claims`:: Specifies one or more resource claims to use with this container.

`spec.resourceClaims`:: Specifies the resource claims that are required for the containers to start. Include an arbitrary name for the resource claim request and a resource claim, resource claim template, or both.
--

. Create the CRD object:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
+
For more information on configuring pod resource requests, see "Dynamic Resource Allocation" (Kubernetes documentation).

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* Enabling features using feature gates
