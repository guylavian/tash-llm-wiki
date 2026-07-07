---
title: "Using the Node Tuning Operator"
type: reference
domain: openshift
slug: nodes-4-22-nodes-node-tuning-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-node-tuning-operator
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Using the Node Tuning Operator

[id="nodes-node-tuning-operator"]
= Using the Node Tuning Operator

[role="_abstract"]
The Node Tuning Operator in OpenShift Container Platform helps you manage node-level tuning by orchestrating the TuneD daemon. You can use this unified interface to apply custom tuning specifications and achieve low latency performance for high-performance applications.

OpenShift Container Platform supports the Node Tuning Operator to improve performance of your nodes on your clusters. The Node Tuning Operator in OpenShift Container Platform helps you manage node-level tuning by orchestrating the TuneD daemon. You can use this unified interface to apply custom tuning specifications and achieve low latency performance for high-performance applications.

Before creating a node tuning configuration, you must create a custom tuning specification.

// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * operators/operator-reference.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="about-node-tuning-operator_{context}"]
= Node Tuning Operator

= About the Node Tuning Operator

[role="_abstract"]
The Node Tuning Operator provides features for the `NodeTuning` capability.

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs.

If you disable the NodeTuning capability, some default tuning settings will not be applied to the control-plane nodes. This might limit the scalability and performance of large clusters with over 900 nodes or 900 routes.

The Operator manages the containerized TuneD daemon for OpenShift Container Platform as a Kubernetes daemon set. It ensures the custom tuning specification is passed to all containerized TuneD daemons running in the cluster in the format that the daemons understand. The daemons run on all nodes in the cluster, one per node.

Node-level settings applied by the containerized TuneD daemon are rolled back on an event that triggers a profile change or when the containerized TuneD daemon is terminated gracefully by receiving and handling a termination signal.

The Node Tuning Operator uses the Performance Profile controller to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications.

The cluster administrator configures a performance profile to define node-level settings such as the following:

* Updating the kernel to kernel-rt.
* Choosing CPUs for housekeeping.
* Choosing CPUs for running workloads.

The Node Tuning Operator is part of a standard OpenShift Container Platform installation in version 4.1 and later.

[NOTE]
====
In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.
====

Project::
+
`cluster-node-tuning-operator`

// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="accessing-an-example-node-tuning-operator-specification_{context}"]
= Accessing an example Node Tuning Operator specification

[role="_abstract"]
Use this process to access an example Node Tuning Operator specification.

.Procedure

 * Run the following command to access an example Node Tuning Operator specification:
+
[source,terminal]
----
oc get tuned.tuned.openshift.io/default -o yaml -n openshift-cluster-node-tuning-operator
----
+
The default CR is meant for delivering standard node-level tuning for the OpenShift Container Platform platform and it can only be modified to set the Operator Management state. Any other custom changes to the default CR will be overwritten by the Operator. For custom tuning, create your own Tuned CRs. Newly created CRs will be combined with the default CR and custom tuning applied to OpenShift Container Platform nodes based on node or pod labels and profile priorities.
+
[WARNING]
====
While in certain situations the support for pod labels can be a convenient way of automatically delivering required tuning, this practice is discouraged and strongly advised against, especially in large-scale clusters. The default Tuned CR ships without pod label matching. If a custom profile is created with pod label matching, then the functionality will be enabled at that time. The pod label functionality will be deprecated in future versions of the Node Tuning Operator.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="custom-tuning-specification_{context}"]
= Custom tuning specification

[role="_abstract"]
The custom resource (CR) for the Operator has two major sections. The first section, `profile:`, is a list of TuneD profiles and their names. The second, `recommend:`, defines the profile selection logic.

Multiple custom tuning specifications can co-exist as multiple CRs in the Operator's namespace. The existence of new CRs or the deletion of old CRs is detected by the Operator. All existing custom tuning specifications are merged and appropriate objects for the containerized TuneD daemons are updated.

*Management state*

The Operator Management state is set by adjusting the default Tuned CR. By default, the Operator is in the Managed state and the `spec.managementState` field is not present in the default Tuned CR. Valid values for the Operator Management state are as follows:

  * Managed: the Operator will update its operands as configuration resources are updated
  * Unmanaged: the Operator will ignore changes to the configuration resources
  * Removed: the Operator will remove its operands and resources the Operator provisioned

*Profile data*

The `profile:` section lists TuneD profiles and their names.

[source,yaml]
----
profile:
- name: tuned_profile_1
  data: |
    # TuneD profile specification
    [main]
    summary=Description of tuned_profile_1 profile

    [sysctl]
    net.ipv4.ip_forward=1
    # ... other sysctl's or other TuneD daemon plugins supported by the containerized TuneD

# ...

- name: tuned_profile_n
  data: |
    # TuneD profile specification
    [main]
    summary=Description of tuned_profile_n profile

    # tuned_profile_n profile settings
----
[source,json]
----
{
  "profile": [
    {
      "name": "tuned_profile_1",
      "data": "# TuneD profile specification\n[main]\nsummary=Description of tuned_profile_1 profile\n\n[sysctl]\nnet.ipv4.ip_forward=1\n# ... other sysctl's or other TuneD daemon plugins supported by the containerized TuneD\n"
    },
    {
      "name": "tuned_profile_n",
      "data": "# TuneD profile specification\n[main]\nsummary=Description of tuned_profile_n profile\n\n# tuned_profile_n profile settings\n"
    }
  ]
}
----

*Recommended profiles*

The `profile:` selection logic is defined by the `recommend:` section of the CR. The `recommend:` section is a list of items to recommend the profiles based on a selection criteria.

[source,yaml]
----
recommend:
<recommend-item-1>
# ...
<recommend-item-n>
----
[source,json]
----
"recommend": [
    {
      "recommend-item-1": details_of_recommendation,
      # ...
      "recommend-item-n": details_of_recommendation,
    }
  ]
----

The individual items of the list:

[source,yaml]
----
- machineConfigLabels:
    <mcLabels>
  match:
    <match>
  priority: <priority>
  profile: <tuned_profile_name>
  operand:
    debug: <bool>
    tunedConfig:
      reapply_sysctl: <bool>
----

where:

* `machineConfigLabels`: Optional.
* `<mcLabels>`: A dictionary of key/value `MachineConfig` labels. The keys must be unique.
* `match`: If omitted, profile match is assumed unless a profile with a higher priority matches first or `machineConfigLabels` is set.
* `<match>`: An optional list.
* `<priority>`: Profile ordering priority. Lower numbers mean higher priority (`0` is the highest priority).
* `<tuned_profile_name>`: A TuneD profile to apply on a match. For example `tuned_profile_1`.
* `operand`: Optional operand configuration.
* `debug`: Turn debugging on or off for the TuneD daemon. Options are `true` for on or `false` for off. The default is `false`.
* `reapply_sysctl`: Turn `reapply_sysctl` functionality on or off for the TuneD daemon. Options are `true` for on and `false` for off.

[source,json]
----
{
  "profile": [
    {
    # ...
    }
  ],
  "recommend": [
    {
      "profile": <tuned_profile_name>,
      "priority":{ <priority>,
      },
      "match": [
        {
          "label": <label_information>
        },
      ]
    },
  ]
}
----

where:

* `<tuned_profile_name>`: A TuneD profile to apply on a match. For example `tuned_profile_1`.
* `<priority>`: Profile ordering priority. Lower numbers mean higher priority (`0` is the highest priority).
* `match`: If omitted, profile match is assumed unless a profile with a higher priority matches first.
* `<label_information>`: The label for the profile matched items.

`<match>` is an optional list recursively defined as follows:

[source,yaml]
----
- label: <label_name>
  value: <label_value>
  type: <label_type>
    <match>
----

where:

* `<label_name>`: Node or pod label name.
* `<label_value>`: Optional node or pod label value. If omitted, the presence of `<label_name>` is enough to match.
* `<label_type>`: Optional object type (`node` or `pod`). If omitted, `node` is assumed.
* `<match>`: An optional `<match>` list.

[source,yaml]
----
"match": [
        {
          "label": <label_name>
        },
]
----

where:

* `<label_name>`: Node or pod label name.

If `<match>` is not omitted, all nested `<match>` sections must also evaluate to `true`. Otherwise, `false` is assumed and the profile with the respective `<match>` section will not be applied or recommended. Therefore, the nesting (child `<match>` sections) works as logical AND operator. Conversely, if any item of the `<match>` list matches, the entire `<match>` list evaluates to `true`. Therefore, the list acts as logical OR operator.

If `machineConfigLabels` is defined, machine config pool based matching is turned on for the given `recommend:` list item. `<mcLabels>` specifies the labels for a machine config. The machine config is created automatically to apply host settings, such as kernel boot parameters, for the profile `<tuned_profile_name>`. This involves finding all machine config pools with machine config selector matching `<mcLabels>` and setting the profile `<tuned_profile_name>` on all nodes that are assigned the found machine config pools. To target nodes that have both master and worker roles, you must use the master role.

The list items `match` and `machineConfigLabels` are connected by the logical OR operator. The `match` item is evaluated first in a short-circuit manner. Therefore, if it evaluates to `true`, the `machineConfigLabels` item is not considered.

[IMPORTANT]
====
When using machine config pool based matching, it is advised to group nodes with the same hardware configuration into the same machine config pool. Not following this practice might result in TuneD operands calculating conflicting kernel parameters for two or more nodes sharing the same machine config pool.
====
.Example: Node or pod label based matching

[source,yaml]
----
- match:
  - label: tuned.openshift.io/elasticsearch
    match:
    - label: node-role.kubernetes.io/master
    - label: node-role.kubernetes.io/infra
    type: pod
  priority: 10
  profile: openshift-control-plane-es
- match:
  - label: node-role.kubernetes.io/master
  - label: node-role.kubernetes.io/infra
  priority: 20
  profile: openshift-control-plane
- priority: 30
  profile: openshift-node
----
[source,JSON]
----
[
  {
    "match": [
      {
        "label": "tuned.openshift.io/elasticsearch",
        "match": [
          {
            "label": "node-role.kubernetes.io/master"
          },
          {
            "label": "node-role.kubernetes.io/infra"
          }
        ],
        "type": "pod"
      }
    ],
    "priority": 10,
    "profile": "openshift-control-plane-es"
  },
  {
    "match": [
      {
        "label": "node-role.kubernetes.io/master"
      },
      {
        "label": "node-role.kubernetes.io/infra"
      }
    ],
    "priority": 20,
    "profile": "openshift-control-plane"
  },
  {
    "priority": 30,
    "profile": "openshift-node"
  }
]
----

The CR above is translated for the containerized TuneD daemon into its `recommend.conf` file based on the profile priorities. The profile with the highest priority (`10`) is `openshift-control-plane-es` and, therefore, it is considered first. The containerized TuneD daemon running on a given node looks to see if there is a pod running on the same node with the `tuned.openshift.io/elasticsearch` label set. If not, the entire `<match>` section evaluates as `false`. If there is such a pod with the label, in order for the `<match>` section to evaluate to `true`, the node label also needs to be `node-role.kubernetes.io/master` or `node-role.kubernetes.io/infra`.

If the labels for the profile with priority `10` matched, `openshift-control-plane-es` profile is applied and no other profile is considered. If the node/pod label combination did not match, the second highest priority profile (`openshift-control-plane`) is considered. This profile is applied if the containerized TuneD pod runs on a node with labels `node-role.kubernetes.io/master` or `node-role.kubernetes.io/infra`.

Finally, the profile `openshift-node` has the lowest priority of `30`. It lacks the `<match>` section and, therefore, will always match. It acts as a profile catch-all to set `openshift-node` profile, if no other profile with higher priority matches on a given node.

image::node-tuning-operator-workflow-revised.png[Decision workflow]

.Example: Machine config pool based matching
[source,yaml]
----
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: openshift-node-custom
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom OpenShift node profile with an additional kernel parameter
      include=openshift-node
      [bootloader]
      cmdline_openshift_node_custom=+skew_tick=1
    name: openshift-node-custom

  recommend:
  - machineConfigLabels:
      machineconfiguration.openshift.io/role: "worker-custom"
    priority: 20
    profile: openshift-node-custom
----
.Example: Machine pool based matching
[source,JSON]
----
{
  "apiVersion": "tuned.openshift.io/v1",
  "kind": "Tuned",
  "metadata": {
    "name": "openshift-node-custom",
    "namespace": "openshift-cluster-node-tuning-operator"
  },
  "spec": {
    "profile": [
      {
        "data": "[main]\nsummary=Custom OpenShift node profile with an additional kernel parameter\ninclude=openshift-node\n[bootloader]\ncmdline_openshift_node_custom=+skew_tick=1\n",
        "name": "openshift-node-custom"
      }
    ],
    "recommend": [
      {
        "priority": 20,
        "profile": "openshift-node-custom"
      }
    ]
  }
}
----

To minimize node reboots, label the target nodes with a label the machine config pool's node selector will match, then create the Tuned CR above and finally create the custom machine config pool itself.
// $ oc label node <node> node-role.kubernetes.io/worker-custom=
// $ oc create -f <tuned-cr-above>
// $ oc create -f- <<EOF
// apiVersion: machineconfiguration.openshift.io/v1
// kind: MachineConfigPool
// metadata:
//   name: worker-custom
//   labels:
//     worker-custom: ""
// spec:
//   machineConfigSelector:
//     matchExpressions:
//       - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker-custom]}
//   nodeSelector:
//     matchLabels:
//       node-role.kubernetes.io/worker-custom: ""
// EOF

*Cloud provider-specific TuneD profiles*

With this functionality, all Cloud provider-specific nodes can conveniently be assigned a TuneD profile specifically tailored to a given Cloud provider on a OpenShift Container Platform cluster. This can be accomplished without adding additional node labels or grouping nodes into
machine config pools.
machine pools.

This functionality takes advantage of `spec.providerID` node object values in the form of `<cloud-provider>://<cloud-provider-specific-id>` and writes the file `/var/lib/ocp-tuned/provider` with the value `<cloud-provider>` in NTO operand containers. The content of this file is then used by TuneD to load `provider-<cloud-provider>` profile if such profile exists.

The `openshift` profile that both `openshift-control-plane` and `openshift-node` profiles inherit settings from is now updated to use this functionality through the use of conditional profile loading. Neither NTO nor TuneD currently include any Cloud provider-specific profiles. However, it is possible to create a custom profile `provider-<cloud-provider>` that will be applied to all Cloud provider-specific cluster nodes.

.Example GCE Cloud provider profile
[source,yaml]
----
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: provider-gce
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=GCE Cloud provider-specific profile
      # Your tuning for GCE Cloud provider goes here.
    name: provider-gce
----
[source,JSON]
----
{
  "apiVersion": "tuned.openshift.io/v1",
  "kind": "Tuned",
  "metadata": {
    "name": "provider-gce",
    "namespace": "openshift-cluster-node-tuning-operator"
  },
  "spec": {
    "profile": [
      {
        "data": "[main]\nsummary=GCE Cloud provider-specific profile\n# Your tuning for GCE Cloud provider goes here.\n",
        "name": "provider-gce"
      }
    ]
  }
}
----

[NOTE]
====
Due to profile inheritance, any setting specified in the `provider-<cloud-provider>` profile will be overwritten by the `openshift` profile and its child profiles.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="custom-tuning-default-profiles-set_{context}"]
= Default profiles set on a cluster

[role="_abstract"]
The following are the default profiles set on a cluster.

[source,yaml]
----
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: default
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Optimize systems running OpenShift (provider specific parent profile)
      include=-provider-${f:exec:cat:/var/lib/ocp-tuned/provider},openshift
    name: openshift
  recommend:
  - profile: openshift-control-plane
    priority: 30
    match:
    - label: node-role.kubernetes.io/master
    - label: node-role.kubernetes.io/infra
  - profile: openshift-node
    priority: 40
----

Starting with OpenShift Container Platform 4.9, all OpenShift TuneD profiles are shipped with
the TuneD package. You can use the `oc exec` command to view the contents of these profiles:

[source,terminal]
----
$ oc exec $tuned_pod -n openshift-cluster-node-tuning-operator -- find /usr/lib/tuned/openshift{,-control-plane,-node} -name tuned.conf -exec grep -H ^ {} \;
----

// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="supported-tuned-daemon-plug-ins_{context}"]
= Supported TuneD daemon plugins

[role="_abstract"]
Excluding the `[main]` section, the following TuneD plugins are supported when
using custom profiles defined in the `profile:` section of the Tuned CR:

* audio
* cpu
* disk
* eeepc_she
* modules
* mounts
* net
* scheduler
* scsi_host
* selinux
* sysctl
* sysfs
* usb
* video
* vm
* bootloader

There is some dynamic tuning functionality provided by some of these plugins
that is not supported. The following TuneD plugins are currently not supported:

* script
* systemd

[NOTE]
====
The TuneD bootloader plugin only supports {op-system-first} worker nodes.
====

.Additional resources

* Available TuneD Plugins

* Getting Started with TuneD

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-tuning-config.adoc

[id="rosa-creating-node-tuning_{context}"]
= Create node tuning configurations

[role="_abstract"]
Create node tuning configurations to optimize node-level performance for your workloads by using the {rosa-cli-first}.

.Prerequisites

* You have downloaded the latest version of the {rosa-cli}.
* You have a cluster on the latest version.
* You have a specification file configured for node tuning.

.Procedure

* Run the following command to create your tuning configuration:
+
[source,terminal]
----
$ rosa create tuning-config -c <cluster_id> --name <name_of_tuning> --spec-path <path_to_spec_file>
----
+
You must supply the path to the `spec.json` file, or the command returns an error.
+
[source,terminal]
----
$ I: Tuning config 'sample-tuning' has been created on cluster 'cluster-example'.
----
+
[source,terminal]
----
$ I: To view all tuning configs, run 'rosa list tuning-configs -c cluster-example'
----

.Verification

* You can verify the existing tuning configurations by running the following command:
+
[source,terminal]
----
$ rosa list tuning-configs -c <cluster_name> [-o json]
----
+
You can specify the type of output you want for the configuration list.

** Without specifying the output type, you see the ID and name of the tuning configuration:
+
*Example output without specifying output type*
+
[source,terminal]
----
ID                                    NAME
20468b8e-edc7-11ed-b0e4-0a580a800298  sample-tuning
----

** If you specify an output type, such as `json`, you receive the tuning configuration as JSON text:
+
[NOTE]
====
The following JSON output has hard line-returns for the sake of reading clarity. This JSON output is invalid unless you remove the newlines in the JSON strings.
====
+
*Example output specifying JSON output*
+
[source,terminal]
----
[
  {
    "kind": "TuningConfig",
    "id": "20468b8e-edc7-11ed-b0e4-0a580a800298",
    "href": "/api/clusters_mgmt/v1/clusters/23jbsevqb22l0m58ps39ua4trff9179e/tuning_configs/20468b8e-edc7-11ed-b0e4-0a580a800298",
    "name": "sample-tuning",
    "spec": {
      "profile": [
        {
          "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"55\"\n",
          "name": "tuned-1-profile"
        }
      ],
      "recommend": [
        {
          "priority": 20,
          "profile": "tuned-1-profile"
        }
      ]
    }
  }
]
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-tuning-config.adoc

[id="rosa-modifying-node-tuning_{context}"]
= Modify node tuning configurations

[role="_abstract"]
View and update node tuning configurations to adjust performance settings for your cluster by using the {rosa-cli-first}.

.Prerequisites

* You have downloaded the latest version of the {rosa-cli}.
* You have a cluster on the latest version.
* Your cluster has a node tuning configuration added to it.

.Procedure

. View the tuning configurations with the `rosa describe` command:
+
[source,terminal]
----
$ rosa describe tuning-config -c <cluster_id> \
       --name <name_of_tuning> \
       [-o json]
----
where:
+
--
`<cluster_id>`:: Specifies the cluster ID for the cluster that you own that you want to apply a node tuning configuration.
`<name_of_tuning>`:: Specifies the name of your tuning configuration.
`-o json`:: Specifies the output type. This parameter is optional. If you do not specify any outputs, you see only the ID and name of the tuning configuration.
--
+
*Example output without specifying output type*
+
[source,terminal]
----
Name:    sample-tuning
ID:      20468b8e-edc7-11ed-b0e4-0a580a800298
Spec:    {
            "profile": [
              {
                "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"55\"\n",
                "name": "tuned-1-profile"
              }
            ],
            "recommend": [
              {
                 "priority": 20,
                 "profile": "tuned-1-profile"
              }
            ]
         }

----
+
*Example output specifying JSON output*
+
[source,terminal]
----
{
  "kind": "TuningConfig",
  "id": "20468b8e-edc7-11ed-b0e4-0a580a800298",
  "href": "/api/clusters_mgmt/v1/clusters/23jbsevqb22l0m58ps39ua4trff9179e/tuning_configs/20468b8e-edc7-11ed-b0e4-0a580a800298",
  "name": "sample-tuning",
  "spec": {
    "profile": [
      {
        "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"55\"\n",
        "name": "tuned-1-profile"
      }
    ],
    "recommend": [
      {
        "priority": 20,
        "profile": "tuned-1-profile"
      }
    ]
  }
}
----

. After verifying the tuning configuration, edit the existing configuration with the `rosa edit` command:
+
[source,terminal]
----
$ rosa edit tuning-config -c <cluster_id> --name <name_of_tuning> --spec-path <path_to_spec_file>
----
+
In this command, you use the `spec.json` file to edit your configurations.

.Verification

* Run the `rosa describe` command again to see that the changes you made to the `spec.json` file are updated in the tuning configurations:
+
[source,terminal]
----
$ rosa describe tuning-config -c <cluster_id> --name <name_of_tuning>
----
+
*Example output*
+
[source,terminal]
----
Name:  sample-tuning
ID:    20468b8e-edc7-11ed-b0e4-0a580a800298
Spec:  {
           "profile": [
             {
              "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"55\"\n",
              "name": "tuned-2-profile"
             }
           ],
           "recommend": [
             {
              "priority": 10,
              "profile": "tuned-2-profile"
             }
           ]
       }
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-tuning-config.adoc

[id="rosa-deleting-node-tuning_{context}"]
= Delete node tuning configurations

[role="_abstract"]
Remove unused node tuning configurations from your cluster to simplify management by using the {rosa-cli-first}.

[NOTE]
====
You cannot delete a tuning configuration referenced in a machine pool. You must remove the tuning configuration from all machine pools before you can delete it.
====

.Prerequisites

* You have downloaded the latest version of the {rosa-cli}.
* You have a cluster on the latest version.
* Your cluster has a node tuning configuration that you want to delete.

.Procedure

* To delete a tuning configuration, run the following command:
+
[source,terminal]
----
$ rosa delete tuning-config -c <cluster_id> <name_of_tuning>
----
+
The tuning configuration on the cluster is deleted.
+
*Example output*
+
[source,terminal]
----
? Are you sure you want to delete tuning config sample-tuning on cluster sample-cluster? Yes
I: Successfully deleted tuning config 'sample-tuning' from cluster 'sample-cluster'
----
