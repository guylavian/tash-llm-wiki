---
title: "Creating custom machine config pools"
type: reference
domain: openshift
slug: machine-configuration-4-22-machine-config-custom-mcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-config-custom-mcp
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Creating custom machine config pools

[id="machine-config-creating-custom-mcp"]
= Creating custom machine config pools

[role="_abstract"]
You can create custom machine config pools (MCP) to manage compute nodes for custom use cases that extend outside of the default node types. By using a custom machine config pool, you can deploy changes targeted only at nodes in the custom pool.

Custom machine config pools inherit their configurations from the `worker` machine config pool. Changes made to the `worker` machine config pool apply to nodes in the custom pool. However, changes made to the custom machine config pool apply only to the nodes in the custom pool. For more information on custom machine config pools, see "Node configuration management with machine config pools".

[NOTE]
====
Custom machine config pools for the control plane nodes are not supported.
====

For example, you could use a custom machine config pool to create an _infrastructure_ node. Components that you move to an infrastructure node do not need to be accounted for during sizing. For more information on infrastructure nodes, see "Creating infrastructure machine sets".

After you create the custom machine config pool, you can boot new nodes directly to the pool by creating a new machine set. Or, you can add existing nodes to the custom pool by using labels.

// Module included in the following assemblies:
//
// * machine_configuration/machine-config-creating-custom-mcp.adoc

[id="machine-config-custom-mcp-automatic_{context}"]
= Creating a custom machine config pool with a new node

[role="_abstract"]
You can create a custom machine config pool (MCP) and launch a new node directly into that pool. By launching the node directly into the new pool, you save a node reboot cycle that would be required when moving the nodes from the worker machine config pool to the custom pool.

Use the `userDataSecret` parameter in the machine set to instruct the Machine Config Operator (MCO) to add the node to a specific machine config pool. The secret contains the endpoint of the custom machine config pool. You must prefix the name of this new secret with the name of the custom machine config pool.

The following procedure shows you how to create a new custom machine config pool and launch a new node into that pool.

.Procedure

. Create a custom machine config pool:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: custom
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [custom,worker]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/custom: ""
----
where:
+
--
`metadata.name`:: Specifies a name for the custom machine config pool.
`spec.machineConfigSelector.matchExpressions`:: Specifies the node roles for the new node. This must include the `worker` role and the custom role.
`spec.nodeSelector.matchLabels`:: Specifies a node selector to use when adding nodes to this pool.
--

.. Create the machine config pool by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. Create a new machine set that creates a new node in the new custom machine config pool:

.. Create a YAML file, for example by making a copy of an existing compute machine set YAML and making the following changes:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
# ...
  name: <machineset_name>
  namespace: openshift-machine-api
# ...
spec:
# ...
  template:
# ...
    spec:
# ...
      providerSpec:
# ...
        value:
# ...
          userDataSecret:
            name: <mcp_name>-user-data-managed
# ...
----
+
where:
+
--
`metadata.name`:: Specifies a name for the machine set.
`metadata.namespace`:: Specifies a namespace for the machine set. This must be `openshift-machine-api`.
`spec.template.spec.providerSpec.value.userDataSecret`:: Specifies a name for the user data secret that is created. The name of the secret must start with the name of the custom machine config pool and end with `-user-data-managed`. For example `custom-user-data-managed`.
--
+
These are the minimum changes required to create the new machine set. For more configuration options or to configure an all-new machine set, see "Creating infrastructure machine sets" for your platform.
+
[NOTE]
====
When creating a new machine set, you should specify the latest image to use for the boot image. For more information about configuring the boot image on your cluster, see "Manually updating the boot image" for your platform. The method to specify the image varies by provider.
====

.. Create the machine set by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
+
The MCO creates a new node in the new custom machine config pool.

.Verification

. Check to see that the MCO created the new machine config pool by running the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output
[source,terminal]
----
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
custom    rendered-custom-72be15c95699b6d39f70fce525f51bb2    True      False      False      1              1                   1                     0                      12s
master    rendered-master-9e25b616b551d6c77f490191f45161d7    True      False      False      3              3                   3                     0                      32m
worker    rendered-worker-72be15c95699b6d39f70fce525f51bb2    True      False      False      2              2                   2                     0                      32m
----
+
In this example, `custom` is the new machine config pool.

. Check to see that the MCO created the new machine set by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                  DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-7x179fk-72292-tc5qz-custom-a    1         1         1       1           62s
ci-ln-7x179fk-72292-tc5qz-worker-a    1         1         1       1           91m
ci-ln-7x179fk-72292-tc5qz-worker-b    1         1         1       1           91m
ci-ln-7x179fk-72292-tc5qz-worker-f    1         1         1       1           91m
----
+
In this example, `ci-ln-7x179fk-72292-tc5qz-custom-a` is the new machine set.

. Check that the MCO created the required secret by running the following command:
+
[source,terminal]
----
$ oc get secrets -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                                  TYPE                      DATA   AGE
# ...
custom-user-data-managed                              Opaque                    2      9m
# ...
----

. Check to see that the node is in the new custom machine config pool by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                        STATUS   ROLES                    AGE   VERSION
ci-ln-i61xqwb-72292-hz2mw-custom-9r496      Ready    custom,worker             9m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-master-0          Ready    control-plane,master     42m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-master-1          Ready    control-plane,master     44m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-master-2          Ready    control-plane,master     43m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-worker-c-2lhcl    Ready    worker                   36m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-worker-f-qgdb7    Ready    worker                   36m   v1.35.3
----
+
In this example, the `ci-ln-i61xqwb-72292--hz2mw-custom-9r496` is a new node that was added to the `custom` machine config pool.
// Module included in the following assemblies:
//
// * machine_configuration/machine-config-creating-custom-mcp.adoc

[id="machine-config-custom-mcp-existing_{context}"]
= Creating a custom machine config pool for an existing node

[role="_abstract"]
You can create custom machine config pools (MCP) and manually add an existing node into that pool. With custom machine config pools, you can deploy changes targeted at the nodes in the custom pool.

The following procedure shows you how to create a new custom machine config pool and add an existing node into that pool.

.Procedure

. Create a custom machine config pool:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: custom
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [custom,worker]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/custom: ""
----
+
where:

`metadata.name`:: Specifies a name for the machine config pool.
`spec.machineConfigSelector.matchExpressions`:: Specifies the node roles for the new node. This must include the `worker` role and the custom role.
`spec.nodeSelector.matchLabels`:: Specifies a node selector to use when adding nodes to this pool.

.. Create the machine config pool by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. Add a label to the worker nodes that you want to move to the new custom pool by running the following command:
+
[source,terminal]
----
$ oc label node <node_name> <node_selector>
----
+
Replace `<node_name>` with the name of the node that you want to move and replace `<node-selector>` with the node selector you added to the machine config pool.
+
.Example command
[source,terminal]
----
$ oc label node ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh node-role.kubernetes.io/custom=""
----

.Verification

. Check to see that the MCO created the new machine config pool by running the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output
[source,terminal]
----
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
custom    rendered-custom-72be15c95699b6d39f70fce525f51bb2    True      False      False      1              1                   1                     0                      12s
master    rendered-master-9e25b616b551d6c77f490191f45161d7    True      False      False      3              3                   3                     0                      32m
worker    rendered-worker-72be15c95699b6d39f70fce525f51bb2    True      False      False      2              2                   2                     0                      32m
----
+
In this example, `custom` is the new machine config pool.

. Check to see if the node is in that pool by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                       STATUS   ROLES                  AGE   VERSION
ci-ln-i61xqwb-72292-ftjn8-master-0         Ready    control-plane,master   42m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-master-1         Ready    control-plane,master   44m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-master-2         Ready    control-plane,master   43m   v1.35.3
ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh   Ready    custom,worker          36m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-worker-c-2lhcl   Ready    worker                 36m   v1.35.3
ci-ln-i61xqwb-72292-ftjn8-worker-f-qgdb7   Ready    worker                 36m   v1.35.3
----
+
In this example, the `ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh` node is an existing node that was moved to the `custom` machine config pool.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Node configuration management with machine config pools
* Manually updating the boot image
* Creating infrastructure machine sets
