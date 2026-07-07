---
title: "Provisioning real-time and low latency workloads"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-cnf-provisioning-low-latency-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-provisioning-low-latency-workloads
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Provisioning real-time and low latency workloads

[id="cnf-provisioning-low-latency-workloads"]
= Provisioning real-time and low latency workloads

[role="_abstract"]
If your organization needs high performance computing and low, predictable latency, especially in the financial and telecommunications industries, you can use the Node Tuning Operator to implement automatic tuning to achieve low latency performance and consistent response time for OpenShift Container Platform applications.

You use the performance profile configuration to make these changes.

You can update the kernel to kernel-rt, reserve CPUs for cluster and operating system housekeeping duties, including pod infra containers, isolate CPUs for application containers to run the workloads, and disable unused CPUs to reduce power consumption.

[NOTE]
====
When writing your applications, follow the general recommendations described in RHEL for Real Time processes and threads.
====

[role="_additional-resources"]
.Additional resources

* Creating a performance profile

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-scheduling-workload-onto-worker-with-real-time-capabilities_{context}"]
= Scheduling a low latency workload onto a compute node

[role="_abstract"]
You can schedule low latency workloads onto a compute node where a performance profile that configures real-time capabilities is applied.

[NOTE]
====
To schedule a workload on specific nodes, use label selectors in the `Pod` custom resource (CR). The label selectors must match the nodes that are attached to the machine config pool that was configured for low latency by the Node Tuning Operator.
====

.Prerequisites

* You have installed the {oc-first}.
* You have logged in as a user with `cluster-admin` privileges.
* You have applied a performance profile in the cluster that tunes compute nodes for low latency workloads.

.Procedure

. Create a `Pod` CR for the low latency workload and apply it in the cluster, for example:
+
.Example `Pod` spec configured to use real-time processing
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: dynamic-low-latency-pod
  annotations:
    cpu-quota.crio.io: "disable"
    cpu-load-balancing.crio.io: "disable"
    irq-load-balancing.crio.io: "disable"
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: dynamic-low-latency-pod
    image: "registry.redhat.io/openshift4/cnf-tests-rhel8:v"
    command: ["sleep", "10h"]
    resources:
      requests:
        cpu: 2
        memory: "200M"
      limits:
        cpu: 2
        memory: "200M"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  runtimeClassName: performance-dynamic-low-latency-profile <5>
# ...
----
+
--
where

`metadata.annotations.cpu-quota.crio.io`:: Disables the CPU completely fair scheduler (CFS) quota at the pod run time.

`metadata.annotations.cpu-load-balancing.crio.io`:: Disables CPU load balancing.

`metadata.annotations.irq-load-balancing.crio.io`:: Opts the pod out of interrupt handling on the node.

`spec.nodeSelector.node-role.kubernetes.io/worker-cnf`:: The `nodeSelector` label must match the label that you specify in the `Node` CR.

`spec.runtimeClassName`:: `runtimeClassName` must match the name of the performance profile configured in the cluster.
--

. Enter the pod `runtimeClassName` in the form performance-<profile_name>, where <profile_name> is the `name` from the `PerformanceProfile` YAML. In the previous YAML example, the `name` is `performance-dynamic-low-latency-profile`.

. Ensure the pod is running correctly. Status should be `running`, and the correct `cnf-worker` node should be set.
+
[source,terminal]
----
$ oc get pod -o wide
----
+
.Expected output
[source,terminal]
----
NAME                     READY   STATUS    RESTARTS   AGE     IP           NODE
dynamic-low-latency-pod  1/1     Running   0          5h33m   10.131.0.10  cnf-worker.example.com
----

. Get the CPUs that the pod configured for IRQ dynamic load balancing runs on:
+
[source,terminal]
----
$ oc exec -it dynamic-low-latency-pod -- /bin/bash -c "grep Cpus_allowed_list /proc/self/status | awk '{print $2}'"
----
+
.Expected output
[source,terminal]
----
Cpus_allowed_list:  2-3
----

.Verification

. Log in to the node to verify the configuration.
+
[source,terminal]
----
$ oc debug node/<node-name>
----

. Verify that you can use the node file system:
+
[source,terminal]
----
sh-4.4# chroot /host
----
+
.Expected output
[source,terminal]
----
sh-4.4#
----

. Ensure the default system CPU affinity mask does not include the `dynamic-low-latency-pod` CPUs, for example, CPUs 2 and 3.
+
[source,terminal]
----
sh-4.4# cat /proc/irq/default_smp_affinity
----
+
.Example output
[source,terminal]
----
33
----

. Ensure the system IRQs are not configured to run on the `dynamic-low-latency-pod` CPUs:
+
[source,terminal]
----
sh-4.4# find /proc/irq/ -name smp_affinity_list -exec sh -c 'i="$1"; mask=$(cat $i); file=$(echo $i); echo $file: $mask' _ {} \;
----
+
.Example output
[source,terminal]
----
/proc/irq/0/smp_affinity_list: 0-5
/proc/irq/1/smp_affinity_list: 5
/proc/irq/2/smp_affinity_list: 0-5
/proc/irq/3/smp_affinity_list: 0-5
/proc/irq/4/smp_affinity_list: 0
/proc/irq/5/smp_affinity_list: 0-5
/proc/irq/6/smp_affinity_list: 0-5
/proc/irq/7/smp_affinity_list: 0-5
/proc/irq/8/smp_affinity_list: 4
/proc/irq/9/smp_affinity_list: 4
/proc/irq/10/smp_affinity_list: 0-5
/proc/irq/11/smp_affinity_list: 0
/proc/irq/12/smp_affinity_list: 1
/proc/irq/13/smp_affinity_list: 0-5
/proc/irq/14/smp_affinity_list: 1
/proc/irq/15/smp_affinity_list: 0
/proc/irq/24/smp_affinity_list: 1
/proc/irq/25/smp_affinity_list: 1
/proc/irq/26/smp_affinity_list: 1
/proc/irq/27/smp_affinity_list: 5
/proc/irq/28/smp_affinity_list: 1
/proc/irq/29/smp_affinity_list: 0
/proc/irq/30/smp_affinity_list: 0-5
----
+
[WARNING]
====
When you tune nodes for low latency, the usage of execution probes in conjunction with applications that require guaranteed CPUs can cause latency spikes. Use other probes, such as a properly configured set of network probes, as an alternative.
====

[role="_additional-resources"]
.Additional resources

* Placing pods on specific nodes using node selectors

* Assigning pods to nodes

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-node-tuning-operator-creating-pod-with-guaranteed-qos-class_{context}"]
= Creating a pod with a guaranteed QoS class

[role="_abstract"]
You can create a pod with a quality of service (QoS) class of `Guaranteed` for high-performance workloads. Configuring a pod with a QoS class of `Guaranteed` ensures that the pod has priority access to the specified CPU and memory resources.

To create a pod with a QoS class of `Guaranteed`, you must apply the following specifications:

* Set identical values for the memory limit and memory request fields for each container in the pod.
* Set identical values for CPU limit and CPU request fields for each container in the pod.

In general, a pod with a QoS class of `Guaranteed` will not be evicted from a node. One exception is during resource contention caused by system daemons exceeding reserved resources. In this scenario, the `kubelet` might evict pods to preserve node stability, starting with the lowest priority pods.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.
* The {oc-first}.

.Procedure

. Create a namespace for the pod by running the following command:
+
[source,terminal]
----
$ oc create namespace qos-example
----
** qos-example: Specifies a `qos-example` example namespace.
+
.Example output
[source,terminal]
----
namespace/qos-example created
----

. Create the `Pod` resource:
+
.. Create a YAML file that defines the `Pod` resource:
+
.Example `qos-example.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: qos-demo
  namespace: qos-example
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: qos-demo-ctr
    image: quay.io/openshifttest/hello-openshift:openshift
    resources:
      limits:
        memory: "200Mi"
        cpu: "1"
      requests:
        memory: "200Mi"
        cpu: "1"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
----
+
--
where:

`spec.containers.image`:: Specifies public image, such as the `hello-openshift` image.

`spec.containers.resources.limits.memory`:: Specifies a memory limit of 200 MB.

`spec.containers.resources.limits.cpu`:: Specifies a CPU limit of 1 CPU.

`spec.containers.resources.requests.memory`:: Specifies a memory request of 200 MB.

`spec.containers.resources.requests.cpu`:: Specifies a CPU request of 1 CPU.
+
[NOTE]
====
If you specify a memory limit for a container, but do not specify a memory request, OpenShift Container Platform automatically assigns a memory request that matches the limit. Similarly, if you specify a CPU limit for a container, but do not specify a CPU request, OpenShift Container Platform automatically assigns a CPU request that matches the limit.
====
--
+
.. Create the `Pod` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f qos-example.yaml --namespace=qos-example
----
+
.Example output
[source,terminal]
----
pod/qos-demo created
----

.Verification

* View the `qosClass` value for the pod by running the following command:
+
[source,terminal]
----
$ oc get pod qos-demo --namespace=qos-example --output=yaml | grep qosClass
----
+
.Example output
[source,yaml]
----
    qosClass: Guaranteed
----

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-node-tuning-operator-disabling-cpu-load-balancing-for-dpdk_{context}"]
= Disabling CPU load balancing in a Pod

[role="_abstract"]
Functionality to disable or enable CPU load balancing is implemented on the CRI-O level. Before CRI-O disables or enables CPU load balancing, you must ensure certain prerequisites are met.

The pod must use the `performance-<profile-name>` runtime class. You can get the proper name by looking at the status of the performance profile, as shown here:

[source,yaml]
----
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
...
status:
  ...
  runtimeClass: performance-manual
----

The Node Tuning Operator is responsible for the creation of the high-performance runtime handler config snippet under relevant nodes and for creation of the high-performance runtime class under the cluster. It will have the same content as the default runtime handler except that it enables the CPU load balancing configuration functionality.

To disable the CPU load balancing for the pod, the `Pod` specification must include the following fields:

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  #...
  annotations:
    #...
    cpu-load-balancing.crio.io: "disable"
    #...
  #...
spec:
  #...
  runtimeClassName: performance-<profile_name>
  #...
----

[NOTE]
====
Only disable CPU load balancing when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. Otherwise, disabling CPU load balancing can affect the performance of other containers in the cluster.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-configuring-high-priority-workload-pods_{context}"]
= Disabling power saving mode for high priority pods

[role="_abstract"]
To protect high priority workloads when using power saving configurations on a node, apply performance settings at the pod level. This ensures that the configuration applies to all cores used by the pod, maintaining performance stability.

By disabling P-states and C-states at the pod level, you can configure high priority workloads for best performance and lowest latency.

.Configuration for high priority workloads
[cols="1,2,3", options="header"]

|===
| Annotation | Possible Values | Description

|`cpu-c-states.crio.io:` a|  * `"enable"`
* `"disable"`
* `"max_latency:microseconds"` | This annotation allows you to enable or disable C-states for each CPU. Alternatively, you can also specify a maximum latency in microseconds for the C-states. For example, enable C-states with a maximum latency of 10 microseconds with the setting `cpu-c-states.crio.io`: `"max_latency:10"`. Set the value to `"disable"` to provide the best performance for a pod.

| `cpu-freq-governor.crio.io:` | Any supported `cpufreq governor`. | Sets the `cpufreq` governor for each CPU. The `"performance"` governor is recommended for high priority workloads.
|===

.Prerequisites

* You have configured power saving in the performance profile for the node where the high priority workload pods are scheduled.

.Procedure

. Add the required annotations to your high priority workload pods. The annotations override the `default` settings.
+
.Example high priority workload annotation
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  #...
  annotations:
    #...
    cpu-c-states.crio.io: "disable"
    cpu-freq-governor.crio.io: "performance"
    #...
  #...
spec:
  #...
  runtimeClassName: performance-<profile_name>
  #...
----

. Restart the pods to apply the annotation.

[role="_additional-resources"]
.Additional resources

* Configuring power saving for nodes that run colocated high and low priority workloads

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-disabling-cpu-cfs-quota_{context}"]
= Disabling CPU CFS quota

[role="_abstract"]
To eliminate CPU throttling for pinned pods, create a pod with the `cpu-quota.crio.io: "disable"` annotation. This annotation disables the CPU completely fair scheduler (CFS) quota when the pod runs.

.Procedure

* To eliminate CPU throttling for pinned pods, create a pod with the `cpu-quota.crio.io: "disable"` annotation. This annotation disables the CPU completely fair scheduler (CFS) quota when the pod runs.
+
.Example pod specification with `cpu-quota.crio.io` disabled
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
      cpu-quota.crio.io: "disable"
spec:
    runtimeClassName: performance-<profile_name>
#...
----
+
[NOTE]
====
Only disable CPU CFS quota when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. For example, pods that contain CPU-pinned containers. Otherwise, disabling CPU CFS quota can affect the performance of other containers in the cluster.
====

[role="_additional-resources"]
.Additional resources

* Recommended firmware configuration for vDU cluster hosts

// Module included in the following assemblies:
//
// * scalability_and_performance/low_latency_tuning/cnf-provisioning-low-latency-workloads.adoc

[id="cnf-disabling-interrupt-processing-for-individual-pods_{context}"]
= Configuring interrupt processing for individual pods

[role="_abstract"]
To achieve low latency for workloads, some containers require that the CPUs they are pinned to do not process device interrupts. You can use the `irq-load-balancing.crio.io` pod annotation to control whether device interrupts are processed on CPUs where the pinned containers are running.

The annotation supports the following values:

`disable`:: Disables IRQ load balancing for all CPUs allocated to the container. Use this value for latency-sensitive workloads when you want to exclude container CPUs from interrupt handling.

`housekeeping`:: Preserves IRQ handling on the first CPU that is allocated to the container, including that CPU's thread siblings. The subsequent CPUs allocated to the container are excluded from interrupt processing. This configuration also injects the `OPENSHIFT_HOUSEKEEPING_CPUS` environment variable into the container. Use this variable to see which CPUs are designated for housekeeping tasks.

You can use the `housekeeping` value to reduce the overall CPU footprint by allowing a small subset of container CPUs to handle both application housekeeping work and system interrupts.

[NOTE]
====
When using the `housekeeping` value, the CPUs designated for housekeeping handle interrupts for the entire system.
====

.Prerequisites

* You configured a performance profile for the node.
* You set the `globallyDisableIrqLoadBalancing` field to `false` in the performance profile.

.Procedure

. Create the `Pod` resource and configure the `irq-load-balancing.crio.io` annotation:
+
.Example pod specification
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-workload
  annotations:
    irq-load-balancing.crio.io: "disable"
spec:
  runtimeClassName: performance-<profile_name>
  containers:
  - name: app
    image: example-image
    resources:
      requests:
        cpu: "8"
        memory: "4Gi"
      limits:
        cpu: "8"
        memory: "4Gi"
----
+
** `metadata.annotations.irq-load-balancing.crio.io`: Specifies if device interrupts are processed on the container CPUs. Set to `disable` to prevent all container CPUs from handling IRQs, or set to `housekeeping` to allow the first allocated CPU and its thread siblings to handle IRQs while excluding the remaining CPUs from IRQ handling.
** `spec.runtimeClassName`: Specifies the runtime class for the performance profile. Replace `<profile_name>` with the name of your performance profile.

. Apply the `Pod` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f pod.yaml
----

.Verification

. Verify the CPUs assigned to the pod:
+
[source,terminal]
----
$ oc exec <pod_name> -- cat /sys/fs/cgroup/cpuset.cpus
----

. For pods using the `housekeeping` annotation, verify the housekeeping CPU environment variable:
+
[source,terminal]
----
$ oc exec <pod_name> -- printenv OPENSHIFT_HOUSEKEEPING_CPUS
----
+
Replace `<pod_name>` with the name of the pod.

. On the worker node, verify the CPUs excluded from IRQ handling:
+
[source,terminal]
----
$ grep IRQBALANCE_BANNED_CPUS /etc/sysconfig/irqbalance
----
+
The output is a hexadecimal bitmask representing the CPUs excluded from IRQ handling.

[role="_additional-resources"]
.Additional resources

* Managing device interrupt processing for guaranteed pod isolated CPUs
