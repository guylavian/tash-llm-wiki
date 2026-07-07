---
title: "Evicting pods using the descheduler"
type: reference
domain: openshift
slug: nodes-4-22-nodes-descheduler-configuring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-descheduler-configuring
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Evicting pods using the descheduler

[id="nodes-descheduler-configuring"]
= Evicting pods using the descheduler

[role="_abstract"]
You can run the descheduler in OpenShift Container Platform by installing the {descheduler-operator} and setting the required profiles and other customizations.

// Installing the descheduler
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

// Configuring the descheduler profiles
// Module included in the following assemblies:
//
// * nodes/scheduling/descheduler/nodes-descheduler-configuring.adoc

[id="nodes-descheduler-configuring-profiles_{context}"]
= Configuring descheduler profiles

[role="_abstract"]
To manage cluster pod eviction behavior, select which descheduler profiles to enable.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Edit the `KubeDescheduler` object:
+
[source,terminal]
----
$ oc edit kubedeschedulers.operator.openshift.io cluster -n openshift-kube-descheduler-operator
----

. Specify one or more profiles in the `spec.profiles` section.
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 3600
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
  mode: Predictive
  profileCustomizations:
    namespaces:
      excluded:
      - my-namespace
    podLifetime: 48h
    thresholdPriorityClassName: my-priority-class-name
  evictionLimits:
    total: 20
  profiles:
  - AffinityAndTaints
  - TopologyAndDuplicates
  - LifecycleAndUtilization
  - EvictPodsWithLocalStorage
  - EvictPodsWithPVC
----
+
where:

`spec.mode`:: Specifies the eviction mode. By default, the descheduler does not evict pods. To evict pods, set `mode` to `Automatic`.
`spec.profileCustomizations.namespaces`:: Specifies a list of user-created namespaces to include or exclude from descheduler operations. Use `excluded` to set a list of namespaces to exclude or use `included` to set a list of namespaces to include. Note that protected namespaces (`openshift-*`, `kube-system`, `hypershift`) are excluded by default. This value is optional.
`spec.profileCustomizations.podLifetime`:: Specifies a custom pod lifetime value for the `LifecycleAndUtilization` profile. Valid units are `s`, `m`, or `h`. The default pod lifetime is 24 hours. This value is optional.
`spec.profileCustomizations.thresholdPriorityClassName`:: Specifies a priority threshold to consider pods for eviction only if their priority is lower than the specified level. Use the `thresholdPriority` field to set a numerical priority threshold (for example, `10000`) or use the `thresholdPriorityClassName` field to specify a certain priority class name (for example, `my-priority-class-name`). If you specify a priority class name, it must already exist or the descheduler will throw an error. Do not set both `thresholdPriority` and `thresholdPriorityClassName`. This value is optional.
`spec.evictionLimits.total`:: Specifies the maximum number of pods to evict during each descheduler run. This value is optional.
`spec.profiles`:: Specifies one or more profiles to enable. Available profiles: `AffinityAndTaints`, `TopologyAndDuplicates`, `LifecycleAndUtilization`, `SoftTopologyAndDuplicates`, `EvictPodsWithLocalStorage`, `EvictPodsWithPVC`, `CompactAndScale`, and `LongLifecycle`. You can enable multiple profiles, but ensure that you do not enable profiles that conflict with each other. The order of the list of profiles is not important.

. Save the file to apply the changes.

// Configuring the descheduler interval
// Module included in the following assemblies:
//
// * nodes/scheduling/descheduler/nodes-descheduler-configuring.adoc

[id="nodes-descheduler-configuring-interval_{context}"]
= Configuring the descheduler interval

[role="_abstract"]
You can configure the amount of time between descheduler runs. The default is 3600 seconds (one hour).

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Edit the `KubeDescheduler` object:
+
[source,terminal]
----
$ oc edit kubedeschedulers.operator.openshift.io cluster -n openshift-kube-descheduler-operator
----

. Update the `deschedulingIntervalSeconds` field to the required value:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 3600
...
----
+
Set the `spec.deschedulingIntervalSeconds` field to the number of seconds you want between descheduler runs. A value of `0` in this field runs the descheduler once and exits.

. Save the file to apply the changes.
