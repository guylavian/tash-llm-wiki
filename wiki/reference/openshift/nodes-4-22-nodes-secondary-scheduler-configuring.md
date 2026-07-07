---
title: "Scheduling pods using a secondary scheduler"
type: reference
domain: openshift
slug: nodes-4-22-nodes-secondary-scheduler-configuring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-secondary-scheduler-configuring
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Scheduling pods using a secondary scheduler

[id="secondary-scheduler-configuring"]
= Scheduling pods using a secondary scheduler

[role="_abstract"]
You can run a custom secondary scheduler in OpenShift Container Platform by installing the {secondary-scheduler-operator}, deploying the secondary scheduler, and setting the secondary scheduler in the pod definition.

// Installing the {secondary-scheduler-operator}
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-configuring.adoc

[id="nodes-secondary-scheduler-install-console_{context}"]
= Installing the {secondary-scheduler-operator}

[role="_abstract"]
You can install the {secondary-scheduler-operator-full} through the OpenShift Container Platform web console to configure a secondary scheduler.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Create the required namespace for the {secondary-scheduler-operator-full}.
.. Navigate to *Administration* -> *Namespaces* and click *Create Namespace*.
.. Enter `openshift-secondary-scheduler-operator` in the *Name* field and click *Create*.
+
// There are no metrics to collect for the secondary scheduler operator as of now, so no need to add the metrics label

. Install the {secondary-scheduler-operator-full}.
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. Enter *{secondary-scheduler-operator-full}* into the filter box.
.. Select the *{secondary-scheduler-operator-full}* and click *Install*.
.. On the *Install Operator* page:
... The *Update channel* is set to *stable*, which installs the latest stable release of the {secondary-scheduler-operator-full}.
... Select *A specific namespace on the cluster* and select *openshift-secondary-scheduler-operator* from the drop-down menu.
... Select an *Update approval* strategy.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.
... Click *Install*.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.
. Verify that *{secondary-scheduler-operator-full}* is listed with a *Status* of *Succeeded*.

// Deploying a secondary scheduler
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-configuring.adoc

[id="nodes-secondary-scheduler-configuring-console_{context}"]
= Deploying a secondary scheduler

[role="_abstract"]
After you have installed the {secondary-scheduler-operator}, you can deploy a secondary scheduler to apply custom placement logic for specific pods.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* You have access to the OpenShift Container Platform web console.
* The {secondary-scheduler-operator-full} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Create config map to hold the configuration for the secondary scheduler.
.. Navigate to *Workloads* -> *ConfigMaps*.
.. Click *Create ConfigMap*.
.. In the YAML editor, enter the config map definition that contains the necessary `KubeSchedulerConfiguration` configuration. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: "secondary-scheduler-config"
  namespace: "openshift-secondary-scheduler-operator"
data:
  "config.yaml": |
    apiVersion: kubescheduler.config.k8s.io/v1
    kind: KubeSchedulerConfiguration
    leaderElection:
      leaderElect: false
    profiles:
      - schedulerName: secondary-scheduler
        plugins:
          score:
            disabled:
              - name: NodeResourcesBalancedAllocation
              - name: NodeResourcesLeastAllocated
----
+
where:

`metadata.name`:: Specifies the name of the config map. This is used in the *Scheduler Config* field when creating the `SecondaryScheduler` CR.
`metadata.namespace`:: Specifies the namespace to create the config map in. The namespace must be `openshift-secondary-scheduler-operator`.
`data."config.yaml".kind`:: Specifies the `KubeSchedulerConfiguration` resource for the secondary scheduler. For more information, see `KubeSchedulerConfiguration` in the Kubernetes API documentation.
`data."config.yaml".profiles.schedulerName`:: Specifies the name of the secondary scheduler. Pods that set their `spec.schedulerName` field to this value are scheduled with this secondary scheduler.
`data."config.yaml".profiles.plugins`:: Specifies the plugins to enable or disable for the secondary scheduler. For a list default scheduling plugins, see Scheduling plugins in the Kubernetes documentation.

.. Click *Create*.

. Create the `SecondaryScheduler` CR:
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Select *{secondary-scheduler-operator-full}*.
.. Select the *Secondary Scheduler* tab and click *Create SecondaryScheduler*.
.. The *Name* field defaults to `cluster`; do not change this name.
.. The *schedulerConfig* field defaults to `secondary-scheduler-config`. Ensure that this value matches the name of the config map created earlier in this procedure.
.. In the *schedulerImage* field, enter the image name for your custom scheduler.
+
[IMPORTANT]
====
Red Hat does not directly support the functionality of your custom secondary scheduler.
====

.. Optional: To enable high availability for the secondary scheduler, configure the following settings:
+
--
... Expand the *topology* section.
... In the *mode* field, select *HighlyAvailable*.
... In the *maxReplicas* field, enter the maximum number of secondary scheduler replicas to deploy. If unset, the maximum number of replicas is `3`.
... In the *tolerations* field, enter tolerations to allow scheduler replicas on tainted nodes. If unset, no taints are tolerated.
--
+
[NOTE]
====
To configure node selectors, use the *YAML view* option. Add the `spec.topology.highlyAvailableTopology.nodeSelector` field and enter the necessary node labels to target a specific group of nodes for scheduler replica placement. If unset, all nodes are considered.
====

.. Click *Create*.

// Scheduling a pod using the secondary scheduler
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-configuring.adoc

[id="nodes-secondary-scheduler-pod-console_{context}"]
= Scheduling a pod using the secondary scheduler

[role="_abstract"]
To schedule a pod by using the secondary scheduler, set the `schedulerName` field in the pod definition.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* You have access to the OpenShift Container Platform web console.
* The {secondary-scheduler-operator-full} is installed.
* A secondary scheduler is configured.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Navigate to *Workloads* -> *Pods*.
. Click *Create Pod*.
. In the YAML editor, enter the desired pod configuration and add the `schedulerName` field:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: default
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: nginx
      image: nginx:1.14.2
      ports:
        - containerPort: 80
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  schedulerName: secondary-scheduler
----
+
The `spec.schedulerName` field must match the name that is defined in the config map when you configured the secondary scheduler.

. Click *Create*.

.Verification

. Log in to the OpenShift CLI.
. Describe the pod using the following command:
+
[source,terminal]
----
$ oc describe pod nginx -n default
----
+
.Example output
[source,text]
----
Name:         nginx
Namespace:    default
Priority:     0
Node:         ci-ln-t0w4r1k-72292-xkqs4-worker-b-xqkxp/10.0.128.3
...
Events:
  Type    Reason          Age   From                 Message
  ----    ------          ----  ----                 -------
  Normal  Scheduled       12s   secondary-scheduler  Successfully assigned default/nginx to ci-ln-t0w4r1k-72292-xkqs4-worker-b-xqkxp
...
----

. In the events table, find the event with a message similar to `Successfully assigned <namespace>/<pod_name> to <node_name>`.
. In the "From" column, verify that the event was generated from the secondary scheduler and not the default scheduler.
+
[NOTE]
====
You can also check the `secondary-scheduler-*` pod logs in the `openshift-secondary-scheduler-namespace` to verify that the pod was scheduled by the secondary scheduler.
====

Due to a UI bug, can't verify via console. Bug should be fixed in 4.11 hopefully, and if so, update to use the console steps:

.Verification
. Navigate to the *Events* tab for the pod.
. Find the event with a message similar to `Successfully assigned <namespace>/<pod_name> to <node_name>`.
. Verify that the event was generated from the secondary scheduler and not the default scheduler.
