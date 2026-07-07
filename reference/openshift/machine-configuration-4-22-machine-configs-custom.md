---
title: "Configuring MCO-related custom resources"
type: reference
domain: openshift
slug: machine-configuration-4-22-machine-configs-custom
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-configs-custom
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Configuring MCO-related custom resources

[id="machine-configs-custom"]
= Configuring MCO-related custom resources

Besides managing `MachineConfig` objects, the MCO manages two custom resources (CRs): `KubeletConfig` and `ContainerRuntimeConfig`. Those CRs let you change node-level settings impacting how the kubelet and CRI-O container runtime services behave.

// Module included in the following assemblies:
//
// * post_installation_configuration/node-tasks.adoc
// * machine_configuration/machine-configs-custom.adoc

[id="create-a-kubeletconfig-crd-to-edit-kubelet-parameters_{context}"]
= Creating a KubeletConfig CR to edit kubelet parameters

The kubelet configuration is currently serialized as an Ignition configuration, so it can be directly edited. However, there is also a new `kubelet-config-controller` added to the Machine Config Controller (MCC). This lets you use a `KubeletConfig` custom resource (CR) to edit the kubelet parameters.

[NOTE]
====
As the fields in the `kubeletConfig` object are passed directly to the kubelet from upstream Kubernetes, the kubelet validates those values directly. Invalid values in the `kubeletConfig` object might cause cluster nodes to become unavailable. For valid values, see the Kubernetes documentation.
====

Consider the following guidance:

* Edit an existing `KubeletConfig` CR to modify existing settings or add new settings, instead of creating a CR for each change. It is recommended that you create a CR only to modify a different machine config pool, or for changes that are intended to be temporary, so that you can revert the changes.

* Create one `KubeletConfig` CR for each machine config pool with all the config changes you want for that pool.

* As needed, create multiple `KubeletConfig` CRs with a limit of 10 per cluster. For the first `KubeletConfig` CR, the Machine Config Operator (MCO) creates a machine config appended with `kubelet`. With each subsequent CR, the controller creates another `kubelet` machine config with a numeric suffix. For example, if you have a `kubelet` machine config with a `-2` suffix, the next `kubelet` machine config is appended with `-3`.

[NOTE]
====
If you are applying a kubelet or container runtime config to a custom machine config pool, the custom role in the `machineConfigSelector` must match the name of the custom machine config pool.

For example, because the following custom machine config pool is named `infra`, the custom role must also be `infra`:

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: infra
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
# ...
----
====

If you want to delete the machine configs, delete them in reverse order to avoid exceeding the limit. For example, you delete the `kubelet-3` machine config before deleting the `kubelet-2` machine config.

[NOTE]
====
If you have a machine config with a `kubelet-9` suffix, and you create another `KubeletConfig` CR, a new machine config is not created, even if there are fewer than 10 `kubelet` machine configs.
====

.Example `KubeletConfig` CR
[source,terminal]
----
$ oc get kubeletconfig
----

[source,terminal]
----
NAME                      AGE
set-kubelet-config        15m
----

.Example showing a `KubeletConfig` machine config
[source,terminal]
----
$ oc get mc | grep kubelet
----

[source,terminal]
----
...
99-worker-generated-kubelet-1                  b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             26m
...
----

The following procedure is an example to show how to configure the maximum number of pods per node, the maximum PIDs per node, and the maximum container log size size on the worker nodes.

.Prerequisites

. Obtain the label associated with the static `MachineConfigPool` CR for the type of node you want to configure.
Perform one of the following steps:

.. View the machine config pool:
+
[source,terminal]
----
$ oc describe machineconfigpool <name>
----
+
For example:
+
[source,terminal]
----
$ oc describe machineconfigpool worker
----
+
.Example output
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  creationTimestamp: 2019-02-08T14:52:39Z
  generation: 1
  labels:
    custom-kubelet: set-kubelet-config <1>
----
<1> If a label has been added it appears under `labels`.

.. If the label is not present, add a key/value pair:
+
[source,terminal]
----
$ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
----

.Procedure

. View the available machine configuration objects that you can select:
+
[source,terminal]
----
$ oc get machineconfig
----
+
By default, the two kubelet-related configs are `01-master-kubelet` and `01-worker-kubelet`.

. Check the current value for the maximum pods per node:
+
[source,terminal]
----
$ oc describe node <node_name>
----
+
For example:
+
[source,terminal]
----
$ oc describe node ci-ln-5grqprb-f76d1-ncnqq-worker-a-mdv94
----
+
Look for `value: pods: <value>` in the `Allocatable` stanza:
+
.Example output
[source,terminal]
----
Allocatable:
 attachable-volumes-aws-ebs:  25
 cpu:                         3500m
 hugepages-1Gi:               0
 hugepages-2Mi:               0
 memory:                      15341844Ki
 pods:                        250
----

. Configure the worker nodes as needed:

.. Create a YAML file similar to the following that contains the kubelet configuration:
+
[IMPORTANT]
====
Kubelet configurations that target a specific machine config pool also affect any dependent pools. For example, creating a kubelet configuration for the pool containing worker nodes will also apply to any subset pools, including the pool containing infrastructure nodes. To avoid this, you must create a new machine config pool with a selection expression that only includes worker nodes, and have your kubelet configuration target this new pool.
====
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: set-kubelet-config
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config <1>
  kubeletConfig: <2>
      podPidsLimit: 8192
      containerLogMaxSize: 50Mi
      maxPods: 500
----
<1> Enter the label from the machine config pool.
<2> Add the kubelet configuration. For example:
+
--
* Use `podPidsLimit` to set the maximum number of PIDs in any pod.
* Use `containerLogMaxSize` to set the maximum size of the container log file before it is rotated.
* Use `maxPods` to set the maximum pods per node.
+
[NOTE]
====
The rate at which the kubelet talks to the API server depends on queries per second (QPS) and burst values. The default values, `50` for `kubeAPIQPS` and `100` for `kubeAPIBurst`, are sufficient if there are limited pods running on each node. It is recommended to update the kubelet QPS and burst rates if there are enough CPU and memory resources on the node.

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: set-kubelet-config
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config
  kubeletConfig:
    maxPods: <pod_count>
    kubeAPIBurst: <burst_rate>
    kubeAPIQPS: <QPS>
----
====

--

.. Update the machine config pool for workers with the label:
+
[source,terminal]
----
$ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
----

.. Create the `KubeletConfig` object:
+
[source,terminal]
----
$ oc create -f change-maxPods-cr.yaml
----

.Verification

. Verify that the `KubeletConfig` object is created:
+
[source,terminal]
----
$ oc get kubeletconfig
----
+
.Example output
[source,terminal]
----
NAME                      AGE
set-kubelet-config        15m
----
+
Depending on the number of worker nodes in the cluster, wait for the worker nodes to be rebooted one by one. For a cluster with 3 worker nodes, this could take about 10 to 15 minutes.

. Verify that the changes are applied to the node:

.. Check on a worker node that the `maxPods` value changed:
+
[source,terminal]
----
$ oc describe node <node_name>
----

.. Locate the `Allocatable` stanza:
+
[source,terminal]
----
 ...
Allocatable:
  attachable-volumes-gce-pd:  127
  cpu:                        3500m
  ephemeral-storage:          123201474766
  hugepages-1Gi:              0
  hugepages-2Mi:              0
  memory:                     14225400Ki
  pods:                       500 <1>
 ...
----
<1> In this example, the `pods` parameter should report the value you set in the `KubeletConfig` object.

. Verify the change in the `KubeletConfig` object:
+
[source,terminal]
----
$ oc get kubeletconfigs set-kubelet-config -o yaml
----
+
This should show a status of `True` and `type:Success`, as shown in the following example:
+
[source,yaml]
----
spec:
  kubeletConfig:
    containerLogMaxSize: 50Mi
    maxPods: 500
    podPidsLimit: 8192
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: set-kubelet-config
status:
  conditions:
  - lastTransitionTime: "2021-06-30T17:04:07Z"
    message: Success
    status: "True"
    type: Success
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-custom.adoc

[id="create-a-containerruntimeconfig_{context}"]
= Creating a ContainerRuntimeConfig CR to edit CRI-O parameters

You can change some of the settings associated with the OpenShift Container Platform CRI-O runtime for the nodes associated with a specific machine config pool (MCP). Using a `ContainerRuntimeConfig` custom resource (CR), you set the configuration values and add a label to match the MCP. The MCO then rebuilds the `crio.conf` and `storage.conf` configuration files on the associated nodes with the updated values.

[NOTE]
====
To revert the changes implemented by using a `ContainerRuntimeConfig` CR, you must delete the CR. Removing the label from the machine config pool does not revert the changes.
====

You can modify the following settings by using a `ContainerRuntimeConfig` CR:

* **Log level**: The `logLevel` parameter sets the CRI-O `log_level` parameter, which is the level of verbosity for log messages. The default is `info` (`log_level = info`). Other options include `fatal`, `panic`, `error`, `warn`, `debug`, and `trace`.
* **Overlay size**: The `overlaySize` parameter sets the CRI-O Overlay storage driver `size` parameter, which is the maximum size of a container image.
* **Container runtime**: The `defaultRuntime` parameter sets the container runtime to either `crun` or `runc`. The default is `crun`.

You should have one `ContainerRuntimeConfig` CR for each machine config pool with all the config changes you want for that pool. If you are applying the same content to all the pools, you only need one `ContainerRuntimeConfig` CR for all the pools.

You should edit an existing `ContainerRuntimeConfig` CR to modify existing settings or add new settings instead of creating a new CR for each change. It is recommended to create a new `ContainerRuntimeConfig` CR only to modify a different machine config pool, or for changes that are intended to be temporary so that you can revert the changes.

You can create multiple `ContainerRuntimeConfig` CRs, as needed, with a limit of 10 per cluster. For the first `ContainerRuntimeConfig` CR, the MCO creates a machine config appended with `containerruntime`. With each subsequent CR, the controller creates a new `containerruntime` machine config with a numeric suffix. For example, if you have a `containerruntime` machine config with a `-2` suffix, the next `containerruntime` machine config is appended with `-3`.

If you want to delete the machine configs, you should delete them in reverse order to avoid exceeding the limit. For example, you should delete the `containerruntime-3` machine config before deleting the `containerruntime-2` machine config.

[NOTE]
====
If you have a machine config with a `containerruntime-9` suffix, and you create another `ContainerRuntimeConfig` CR, a new machine config is not created, even if there are fewer than 10 `containerruntime` machine configs.
====

.Example showing multiple `ContainerRuntimeConfig` CRs
[source,terminal]
----
$ oc get ctrcfg
----

.Example output
[source,terminal]
----
NAME         AGE
ctr-overlay  15m
ctr-level    5m45s
----

.Example showing multiple `containerruntime` machine configs
[source,terminal]
----
$ oc get mc | grep container
----

.Example output
[source,terminal]
----
...
01-master-container-runtime                        b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             57m
...
01-worker-container-runtime                        b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             57m
...
99-worker-generated-containerruntime               b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             26m
99-worker-generated-containerruntime-1             b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             17m
99-worker-generated-containerruntime-2             b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             7m26s
...
----

The following example sets the `log_level` field to `debug`, sets the overlay size to 8 GB, and configures runC as the container runtime:

.Example `ContainerRuntimeConfig` CR
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: overlay-size
spec:
 machineConfigPoolSelector:
   matchLabels:
     pools.operator.machineconfiguration.openshift.io/worker: '' <1>
 containerRuntimeConfig:
   logLevel: debug <2>
   overlaySize: 8G <3>
   defaultRuntime: "runc" <4>
----
<1> Specifies the machine config pool label. For a container runtime config, the role must match the name of the associated machine config pool.
<2> Optional: Specifies the level of verbosity for log messages.
<3> Optional: Specifies the maximum size of a container image.
<4> Optional: Specifies the container runtime to deploy to new containers, either `crun` or `runc`. The default value is `crun`.

.Procedure

To change CRI-O settings using the `ContainerRuntimeConfig` CR:

. Create a YAML file for the `ContainerRuntimeConfig` CR:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: overlay-size
spec:
 machineConfigPoolSelector:
   matchLabels:
     pools.operator.machineconfiguration.openshift.io/worker: '' <1>
 containerRuntimeConfig: <2>
   logLevel: debug
   overlaySize: 8G
   defaultRuntime: "runc"
----
<1> Specify a label for the machine config pool that you want you want to modify.
<2> Set the parameters as needed.

. Create the `ContainerRuntimeConfig` CR:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. Verify that the CR is created:
+
[source,terminal]
----
$ oc get ContainerRuntimeConfig
----
+
.Example output
[source,terminal]
----
NAME           AGE
overlay-size   3m19s
----

. Check that a new `containerruntime` machine config is created:
+
[source,terminal]
----
$ oc get machineconfigs | grep containerrun
----
+
.Example output
[source,terminal]
----
99-worker-generated-containerruntime   2c9371fbb673b97a6fe8b1c52691999ed3a1bfc2  3.5.0  31s
----

. Monitor the machine config pool until all are shown as ready:
+
[source,terminal]
----
$ oc get mcp worker
----
+
.Example output
+
[source,terminal]
----
NAME    CONFIG               UPDATED  UPDATING  DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT  DEGRADEDMACHINECOUNT  AGE
worker  rendered-worker-169  False    True      False     3             1                  1                    0                     9h
----

. Verify that the settings were applied in CRI-O:

.. Open an `oc debug` session to a node in the machine config pool and run `chroot /host`.
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
[source,terminal]
----
sh-4.4# chroot /host
----

.. Verify the changes in the `crio.conf` file:
+
[source,terminal]
----
sh-4.4# crio config | grep 'log_level'
----
+
.Example output
+
[source,terminal]
----
log_level = "debug"
----

.. Verify the changes in the `storage.conf` file:
+
[source,terminal]
----
sh-4.4# head -n 7 /etc/containers/storage.conf
----
+
.Example output
[source,terminal]
----
[storage]
  driver = "overlay"
  runroot = "/var/run/containers/storage"
  graphroot = "/var/lib/containers/storage"
  [storage.options]
    additionalimagestores = []
    size = "8G"
----

.. Verify the changes in the `crio/crio.conf.d/01-ctrcfg-defaultRuntime` file:
+
[source,terminal]
----
sh-5.1# cat /etc/crio/crio.conf.d/01-ctrcfg-defaultRuntime
----
+
.Example output
[source,terminal]
----
[crio]
  [crio.runtime]
    default_runtime = "runc"
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-custom.adoc

[id="config-container-runtime_{context}"]
= Configuring the container runtime

[role="_abstract"]
You can configure the container runtime used with new workloads on your nodes, based on which runtime you or your organization prefers. You can use either crun, which is considered a faster and more lightweight runtime, or runC, which is more widely used than crun.

For information on crun and runC, see "About the container engine and container runtime".

[WARNING]
====
Starting in OpenShift Container Platform 4.22, the runC container runtime is deprecated.
====

Starting in OpenShift Container Platform 4.18, crun is the default container runtime for new installations. You can change between the runtimes by using a `ContainerRuntimeConfig` object, as described in the following procedure. Changing the container runtime affects new workloads only. Existing workloads continue to use their existing container runtime.

If you updated your cluster from OpenShift Container Platform 4.17, the runC container runtime remains unchanged as the default. During the upgrade, two `MachineConfig` objects, one for the control plane nodes and one for the worker nodes, were created to override the new default runtime. You can migrate the container runtime to crun, on a schedule of your choosing, by removing either or both of the `MachineConfig` objects.

.Procedure

* If your cluster is updated from OpenShift Container Platform 4.17, you can use the crun container runtime by deleting the following `MachineConfig` objects:

** Migrate your worker nodes to crun by running the following command:
+
[source,terminal]
----
$ oc delete machineconfig 00-override-worker-generated-crio-default-container-runtime
----

** Migrate your control plane nodes to crun by running the following command:
+
[source,terminal]
----
$ oc delete machineconfig 00-override-master-generated-crio-default-container-runtime
----

* For any OpenShift Container Platform 4.18 or greater cluster, you can configure crun or runC as the container runtime for specific nodes by creating a container runtime configuration:

. Create a YAML file for the `ContainerRuntimeConfig` CR:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: configure-runc
spec:
 machineConfigPoolSelector:
   matchLabels:
     pools.operator.machineconfiguration.openshift.io/worker: ''
 containerRuntimeConfig:
   defaultRuntime: "runc"
----
where:
+
--
* `spec.machineConfigPoolSelector.matchLabels`:: Specifies a label for the machine config pool that you want you want to modify.
* `spec.containerRuntimeConfig.defaultRuntime`:: Specifies the container runtime to use with new workloads on the nodes in the specified machine config pool, either `crun` or `runc`.
--

. Create the `ContainerRuntimeConfig` CR:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

.Verification

. After the nodes return to a ready state, open an `oc debug` session to a node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
. Set `/host` as the root directory within the debug shell by running the following command:
+
[source,terminal]
----
sh-5.1# chroot /host
----

. Check the container runtime by using the following command:
+
[source,terminal]
----
sh-5.1# crio status config | grep default_runtime
----
+
.Example output
[source,terminal]
----
INFO[2026-01-27 23:09:18.413462914Z] Starting CRI-O, version: 1.30.14-6.rhaos4.17.gitfa27f6f.el9, git: unknown(clean)
    default_runtime = "runc"
----
+
The `default_runtime` parameter specifies the container runtime that OpenShift Container Platform uses for new workloads on this node, either `crun` or `runc`, depending on what you have configured.

// Module included in the following assemblies:
//
// machine_configuration/machine-configs-custom.adoc

[id="set-the-default-max-container-root-partition-size-for-overlay-with-crio_{context}"]
= Setting the default maximum container root partition size for Overlay with CRI-O

The root partition of each container shows all of the available disk space of the underlying host. Follow this guidance to set a maximum partition size for the root disk of all containers.

To configure the maximum Overlay size, as well as other CRI-O options like the log level, you can create the following `ContainerRuntimeConfig` custom resource definition (CRD):

[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: overlay-size
spec:
 machineConfigPoolSelector:
   matchLabels:
     custom-crio: overlay-size
 containerRuntimeConfig:
   logLevel: debug
   overlaySize: 8G
----

.Procedure

. Create the configuration object:
+
[source,terminal]
----
$ oc apply -f overlaysize.yml
----

. To apply the new CRI-O configuration to your worker nodes, edit the worker machine config pool:
+
[source,terminal]
----
$ oc edit machineconfigpool worker
----

. Add the `custom-crio` label based on the `matchLabels` name you set in the `ContainerRuntimeConfig` CRD:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  creationTimestamp: "2020-07-09T15:46:34Z"
  generation: 3
  labels:
    custom-crio: overlay-size
    machineconfiguration.openshift.io/mco-built-in: ""
----

. Save the changes, then view the machine configs:
+
[source,terminal]
----
$ oc get machineconfigs
----
+
New `99-worker-generated-containerruntime` and `rendered-worker-xyz` objects are created:
+
.Example output
[source,terminal]
----
99-worker-generated-containerruntime  4173030d89fbf4a7a0976d1665491a4d9a6e54f1   3.5.0             7m42s
rendered-worker-xyz                   4173030d89fbf4a7a0976d1665491a4d9a6e54f1   3.5.0             7m36s
----

. After those objects are created, monitor the machine config pool for the changes to be applied:
+
[source,terminal]
----
$ oc get mcp worker
----
+
The worker nodes show `UPDATING` as `True`, as well as the number of machines, the number updated, and other details:
+
.Example output
[source,terminal]
----
NAME   CONFIG              UPDATED   UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
worker rendered-worker-xyz False True False     3             2                   2                    0                      20h
----
+
When complete, the worker nodes transition back to `UPDATING` as `False`, and the `UPDATEDMACHINECOUNT` number matches the `MACHINECOUNT`:
+
.Example output
[source,terminal]
----
NAME   CONFIG              UPDATED   UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
worker   rendered-worker-xyz   True      False      False      3         3            3             0           20h
----
+
Looking at a worker machine, you see that the new 8 GB max size configuration is applied to all of the workers:
+
.Example output
[source,terminal]
----
head -n 7 /etc/containers/storage.conf
[storage]
  driver = "overlay"
  runroot = "/var/run/containers/storage"
  graphroot = "/var/lib/containers/storage"
  [storage.options]
    additionalimagestores = []
    size = "8G"
----
+
Looking inside a container, you see that the root partition is now 8 GB:
+
.Example output
[source,terminal]
----
~ $ df -h
Filesystem                Size      Used Available Use% Mounted on
overlay                   8.0G      8.0K      8.0G   0% /
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-custom.adoc

[id="create-crio-default-capabilities_{context}"]
= Creating a drop-in file for the default CRI-O capabilities

You can change some of the settings associated with the OpenShift Container Platform CRI-O runtime for the nodes associated with a specific machine config pool (MCP). By using a controller custom resource (CR), you set the configuration values and add a label to match the MCP. The Machine Config Operator (MCO) then rebuilds the `crio.conf` and `default.conf` configuration files on the associated nodes with the updated values.

Earlier versions of OpenShift Container Platform included specific machine configs by default. If you updated to a later version of OpenShift Container Platform, those machine configs were retained to ensure that clusters running on the same OpenShift Container Platform version have the same machine configs.

You can create multiple `ContainerRuntimeConfig` CRs, as needed, with a limit of 10 per cluster. For the first `ContainerRuntimeConfig` CR, the MCO creates a machine config appended with `containerruntime`. With each subsequent CR, the controller creates a `containerruntime` machine config with a numeric suffix. For example, if you have a `containerruntime` machine config with a `-2` suffix, the next `containerruntime` machine config is appended with `-3`.

If you want to delete the machine configs, delete them in reverse order to avoid exceeding the limit. For example, delete the `containerruntime-3` machine config before you delete the `containerruntime-2` machine config.

[NOTE]
====
If you have a machine config with a `containerruntime-9` suffix and you create another `ContainerRuntimeConfig` CR, a new machine config is not created, even if there are fewer than 10 `containerruntime` machine configs.
====

.Example of multiple ContainerRuntimeConfig CRs
[source,terminal]
----
$ oc get ctrcfg
----

.Example output
[source,terminal]
----
NAME         AGE
ctr-overlay  15m
ctr-level    5m45s
----

.Example showing multiple containerruntime related system configs
[source,terminal]
----
$ cat /proc/1/status | grep Cap
----

[source,terminal]
----
$ capsh --decode=<decode_CapBnd_value> <1>
----
<1> Replace `<decode_CapBnd_value>` with the specific value you want to decode.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About the container engine and container runtime
