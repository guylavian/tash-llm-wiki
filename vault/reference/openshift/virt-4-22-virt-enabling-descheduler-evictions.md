---
title: "Enabling descheduler evictions on virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-enabling-descheduler-evictions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-enabling-descheduler-evictions
version: 4.22
family: virt
documentKind: "Documentation"
---

# Enabling descheduler evictions on virtual machines

[id="virt-enabling-descheduler-evictions"]
= Enabling descheduler evictions on virtual machines

[role="_abstract"]
You can use the descheduler to evict pods so that the pods can be rescheduled onto more appropriate nodes. If the pod is a virtual machine, the pod eviction causes the virtual machine to be live migrated to another node.

// Module included in the following assemblies:
//
// * nodes/scheduling/descheduler/index.adoc

[id="nodes-descheduler-profiles_{context}"]
= Descheduler profiles

[role="_abstract"]
Use descheduler profiles to enable specific eviction strategies that rebalance your cluster based on criteria such as pod lifecycle or node utilization.

The following descheduler profiles are available:

`AffinityAndTaints`:: This profile evicts pods that violate inter-pod anti-affinity, node affinity, and node taints.
+
It enables the following strategies:
+
* `RemovePodsViolatingInterPodAntiAffinity`: removes pods that are violating inter-pod anti-affinity.
* `RemovePodsViolatingNodeAffinity`: removes pods that are violating node affinity.
* `RemovePodsViolatingNodeTaints`: removes pods that are violating `NoSchedule` taints on nodes.
+
Pods with a node affinity type of `requiredDuringSchedulingIgnoredDuringExecution` are removed.

`TopologyAndDuplicates`:: This profile evicts pods in an effort to evenly spread similar pods, or pods of the same topology domain, among nodes.
+
It enables the following strategies:
+
--
* `RemovePodsViolatingTopologySpreadConstraint`: finds unbalanced topology domains and tries to evict pods from larger ones when `DoNotSchedule` constraints are violated.
* `RemoveDuplicates`: ensures that there is only one pod associated with a replica set, replication controller, deployment, or job running on same node. If there are more, those duplicate pods are evicted for better pod distribution in a cluster.
--
+
[WARNING]
====
Do not enable `TopologyAndDuplicates` with any of the following profiles: `SoftTopologyAndDuplicates` or `CompactAndScale`. Enabling these profiles together results in a conflict.
====

`LifecycleAndUtilization`:: This profile evicts long-running pods and balances resource usage between nodes.
+
It enables the following strategies:
+
--
* `RemovePodsHavingTooManyRestarts`: removes pods whose containers have been restarted too many times.
+
Pods where the sum of restarts over all containers (including Init Containers) is more than 100.

* `LowNodeUtilization`: finds nodes that are underutilized and evicts pods, if possible, from overutilized nodes in the hope that recreation of evicted pods will be scheduled on these underutilized nodes.

** A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods).

** A node is considered overutilized if its usage is above 50% for any of the thresholds (CPU, memory, and number of pods).

+
Optionally, you can adjust these underutilized/overutilized threshold percentages by setting the Technology Preview field `devLowNodeUtilizationThresholds` to one the following values: `Low` for 10%/30%, `Medium` for 20%/50%, or `High` for 40%/70%. The default value is `Medium`.

* `PodLifeTime`: evicts pods that are too old.
+
By default, pods that are older than 24 hours are removed. You can customize the pod lifetime value.
--
+
[WARNING]
====
Do not enable `LifecycleAndUtilization` with any of the following profiles: `LongLifecycle` or `CompactAndScale`. Enabling these profiles together results in a conflict.
====

`SoftTopologyAndDuplicates`:: This profile is the same as `TopologyAndDuplicates`, except that pods with soft topology constraints, such as `whenUnsatisfiable: ScheduleAnyway`, are also considered for eviction.
+
[WARNING]
====
Do not enable both `SoftTopologyAndDuplicates` and `TopologyAndDuplicates`. Enabling both results in a conflict.
====

`EvictPodsWithLocalStorage`:: This profile allows pods with local storage to be eligible for eviction.

`EvictPodsWithPVC`:: This profile allows pods with persistent volume claims to be eligible for eviction. If you are using `Kubernetes NFS Subdir External Provisioner`, you must add an excluded namespace for the namespace where the provisioner is installed.

`CompactAndScale`:: This profile enables the `HighNodeUtilization` strategy, which attempts to evict pods from underutilized nodes to allow a workload to run on a smaller set of nodes. A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods).
+
Optionally, you can adjust the underutilized percentage by setting the Technology Preview field `devHighNodeUtilizationThresholds` to one the following values: `Minimal` for 10%, `Modest` for 20%, or `Moderate` for 30%. The default value is `Modest`.
+
[WARNING]
====
Do not enable `CompactAndScale` with any of the following profiles: `LifecycleAndUtilization`, `LongLifecycle`, or `TopologyAndDuplicates`. Enabling these profiles together results in a conflict.
====

Use the `KubeVirtRelieveAndMigrate` or `LongLifecycle` profile to enable the descheduler on a virtual machine.

[IMPORTANT]
====
You cannot have both `KubeVirtRelieveAndMigrate` and `LongLifeCycle` enabled at the same time.
====

`KubeVirtRelieveAndMigrate`:: This profile is an enhanced version of the `LongLifeCycle` profile.
+
The `KubeVirtRelieveAndMigrate` profile evicts pods from high-cost nodes to reduce overall resource expenses and enable workload migration. It also periodically rebalances workloads to help maintain similar spare capacity across nodes, which supports better handling of sudden workload spikes. Nodes can experience the following costs:
+
--
* **Resource utilization**: Increased resource pressure raises the overhead for running applications.
* **Node maintenance**: A higher number of containers on a node increases resource consumption and maintenance costs.
--
+
The profile enables the `LowNodeUtilization` strategy with the alpha-level `EvictionsInBackground` feature. By default, the profile uses the `PrometheusCPUMemoryCombinedProfile` utilization metric. This metric combines CPU and memory utilization with pressure stall information (PSI) for both dimensions for comprehensive node load balancing.
+
The profile also exposes the following customization fields:
+
--
* `devActualUtilizationProfile`: Enables load-aware descheduling. You can configure the following utilization profiles:
+
** `PrometheusCPUMemoryCombinedProfile` (default): Balances nodes based on CPU utilization, CPU PSI pressure, memory utilization, and memory PSI pressure. This profile is ideal for environments with memory overcommit enabled, as it spreads the load and prevents resource contention.
** `PrometheusCPUCombined`: Balances nodes based on CPU utilization and CPU PSI pressure only. Use this profile in environments without memory overcommit, where memory allocations are strictly guaranteed and CPU pressure is the primary driver for workload distribution.
* `devLowNodeUtilizationThresholds`: Sets experimental thresholds for the `LowNodeUtilization` strategy. Do not use this field with `devDeviationThresholds`.
* `devDeviationThresholds`: Treats nodes with below-average resource usage as underutilized to help redistribute workloads from overutilized nodes. Do not use this field with `devLowNodeUtilizationThresholds`. Supported values are: `Low` (10%:10%), `Medium` (20%:20%), `High` (30%:30%), `AsymmetricLow` (0%:10%), `AsymmetricMedium` (0%:20%), `AsymmetricHigh` (0%:30%).
* `devEnableSoftTainter`: Enables the soft-tainting component to dynamically apply or remove soft taints as scheduling hints.
--
+
.Example configuration
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  managementState: Managed
  deschedulingIntervalSeconds: 30
  mode: "Automatic"
  profiles:
    - KubeVirtRelieveAndMigrate
  profileCustomizations:
    devEnableSoftTainter: true
    devDeviationThresholds: AsymmetricLow
    devActualUtilizationProfile: PrometheusCPUMemoryCombinedProfile
----
+
The `KubeVirtRelieveAndMigrate` profile requires PSI metrics to be enabled on all worker nodes. You can enable this by applying the following `MachineConfig` custom resource (CR):
+
.Example `MachineConfig` CR
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-openshift-machineconfig-worker-psi-karg
spec:
  kernelArguments:
    - psi=1
----
+
[NOTE]
====
The name of the `MachineConfig` object is significant because machine configs are processed in lexicographical order. By default, a config that starts with `98-` disables PSI. To ensure that PSI is enabled, name your config with a higher prefix, such as `99-openshift-machineconfig-worker-psi-karg`.
====
+
You can use this profile with the `SoftTopologyAndDuplicates` profile to also rebalance pods based on soft topology constraints, which can be useful in hosted control plane environments.

// Show LongLifecycle profile both for virt and nodes
`LongLifecycle`:: This profile balances resource usage between nodes and enables the following strategies:
+
--
* `RemovePodsHavingTooManyRestarts`: removes pods whose containers have been restarted too many times and pods where the sum of restarts over all containers (including Init Containers) is more than 100. Restarting the VM guest operating system does not increase this count.
* `LowNodeUtilization`: evicts pods from overutilized nodes when there are any underutilized nodes. The destination node for the evicted pod will be determined by the scheduler.
** A node is considered underutilized if its usage is below 20% for all thresholds (CPU, memory, and number of pods).
** A node is considered overutilized if its usage is above 50% for any of the thresholds (CPU, memory, and number of pods).
--
+
[WARNING]
====
Do not enable `LongLifecycle` with any of the following profiles: `LifecycleAndUtilization` or `CompactAndScale`. Enabling these profiles together results in a conflict.
====

// Module included in the following assemblies:
//
// * nodes/scheduling/descheduler/nodes-descheduler-configuring.adoc

[id="nodes-descheduler-installing_{context}"]
= Installing the descheduler

[role="_abstract"]
The descheduler is not available by default. To enable the descheduler, you must install the {descheduler-operator} from the software catalog and enable one or more descheduler profiles.

By default, the descheduler runs in predictive mode, which means that it only simulates pod evictions. You must change the mode to automatic for the descheduler to perform the pod evictions.

[IMPORTANT]
====
If you have enabled {hcp} in your cluster, set a custom priority threshold to lower the chance that pods in the hosted control plane namespaces are evicted. Set the priority threshold class name to `hypershift-control-plane`, because it has the lowest priority value (`100000000`) of the hosted control plane priority classes.
====

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* Access to the OpenShift Container Platform web console.
* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in _Configuring OpenShift Container Platform to use Red Hat Operators_.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Create the required namespace for the {descheduler-operator}.
.. Navigate to *Administration* -> *Namespaces* and click *Create Namespace*.
.. Enter `openshift-kube-descheduler-operator` in the *Name* field, enter `openshift.io/cluster-monitoring=true` in the *Labels* field to enable descheduler metrics, and click *Create*.
. Install the {descheduler-operator}.
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. Type *{descheduler-operator}* into the filter box.
.. Select the *{descheduler-operator}* and click *Install*.
.. On the *Install Operator* page, select *A specific namespace on the cluster*. Select *openshift-kube-descheduler-operator* from the drop-down menu.
.. Adjust the values for the *Update Channel* and *Approval Strategy* to the desired values.
.. Click *Install*.
. Create a descheduler instance.
.. From the *Ecosystem* -> *Installed Operators* page, click the *{descheduler-operator}*.
.. Select the *Kube Descheduler* tab and click *Create KubeDescheduler*.
.. Edit the settings as necessary.
... To evict pods instead of simulating the evictions, change the *Mode* field to *Automatic*.

... Expand the *Profiles* section and select `LongLifecycle`. The `AffinityAndTaints` profile is enabled by default.
+
[IMPORTANT]
====
The only profile currently available for {VirtProductName} is `LongLifecycle`.
====
+
You can also configure the profiles and settings for the descheduler later using the OpenShift CLI (`oc`).
... Expand the *Profiles* section to select one or more profiles to enable. The `AffinityAndTaints` profile is enabled by default. Click *Add Profile* to select additional profiles.
+
[NOTE]
====
Do not enable both `TopologyAndDuplicates` and `SoftTopologyAndDuplicates`. Enabling both results in a conflict.
====
... Optional: Expand the *Profile Customizations* section to set optional configurations for the descheduler.
**** Set a custom pod lifetime value for the `LifecycleAndUtilization` profile. Use the *podLifetime* field to set a numerical value and a valid unit (`s`, `m`, or `h`). The default pod lifetime is 24 hours (`24h`).

**** Set a custom priority threshold to consider pods for eviction only if their priority is lower than a specified priority level. Use the *thresholdPriority* field to set a numerical priority threshold or use the *thresholdPriorityClassName* field to specify a certain priority class name.
+
[NOTE]
====
Do not specify both *thresholdPriority* and *thresholdPriorityClassName* for the descheduler.
====

**** Set specific namespaces to exclude or include from descheduler operations. Expand the *namespaces* field and add namespaces to the *excluded* or *included* list. You can only either set a list of namespaces to exclude or a list of namespaces to include. Note that protected namespaces (`openshift-*`, `kube-system`, `hypershift`) are excluded by default.

**** Experimental: Set thresholds for underutilization and overutilization for the `LowNodeUtilization` strategy. Use the *devLowNodeUtilizationThresholds* field to set one of the following values:
+
--
***** `Low`: 10% underutilized and 30% overutilized
***** `Medium`: 20% underutilized and 50% overutilized (Default)
***** `High`: 40% underutilized and 70% overutilized
--
+
[NOTE]
====
This setting is experimental and should not be used in a production environment.
====

... Optional: Use the *Descheduling Interval Seconds* field to change the number of seconds between descheduler runs. The default is `3600` seconds.
.. Click *Create*.

+
You can also configure the profiles and settings for the descheduler later using the OpenShift CLI (`oc`). If you did not adjust the profiles when creating the descheduler instance from the web console, the `AffinityAndTaints` profile is enabled by default.

// Module included in the following assemblies:
//
// virt/virtual_machines/advanced_vm_management/virt-enabling-descheduler-evictions.adoc

[id="virt-configuring-descheduler-evictions_{context}"]
= Configuring descheduler evictions for virtual machines

[role="_abstract"]
After the descheduler is installed and configured, all migratable virtual machines (VMs) are eligible for eviction by default. You can configure the descheduler to manage VM evictions across the cluster and optionally exclude specific VMs from eviction.

.Prerequisites

* Install the descheduler in the OpenShift Container Platform web console or OpenShift CLI (`oc`).

.Procedure

. Stop the VM.

. Configure the `KubeDescheduler` object with the `KubeVirtRelieveAndMigrate` profile and enable background evictions for improved VM eviction stability during live migration:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 60
  profiles:
  - KubeVirtRelieveAndMigrate
  mode: Automatic
----
+
. Optional: To evict pods, set the `mode` field value to `Automatic`. By default, the descheduler does not evict pods.

. Optional: Configure limits for the number of parallel evictions to improve stability in large clusters.
+
The descheduler can limit the number of concurrent evictions per node and across the cluster by using the `evictionLimits` field. Set these limits to match the migration limits configured in the `HyperConverged` custom resource (CR).
+
[source,yaml]
----
spec:
  evictionLimits:
    node: 2
    total: 5
----
+
Set values that correspond to the migration limits in the `HyperConverged` CR:
+
[source,yaml]
----
spec:
  liveMigrationConfig:
    parallelMigrationsPerCluster: 5
    parallelOutboundMigrationsPerNode: 2
----

. Optional: To exclude the VM from eviction, add the `descheduler.alpha.kubernetes.io/prefer-no-eviction` annotation to the `spec.template.metadata.annotations` field. The change is applied dynamically and is propagated to the `VirtualMachineInstance` (VMI) object and the `virt-launcher` pod.
+
Only the presence of the annotation is checked. The value is not evaluated, so `"true"` and `"false"` have the same effect.
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  template:
    metadata:
      annotations:
        descheduler.alpha.kubernetes.io/prefer-no-eviction: "true"
----

. Start the VM.

.Result

The VM is now configured according to the descheduler settings.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Descheduler overview
