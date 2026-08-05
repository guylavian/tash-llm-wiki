---
title: "Understanding node rebooting"
type: reference
domain: openshift
slug: nodes-4-22-nodes-nodes-rebooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-nodes-rebooting
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Understanding node rebooting

[id="nodes-nodes-rebooting"]
= Understanding node rebooting

[role="_abstract"]
Review the following information to learn about rebooting a node without causing an outage for applications running on the
platform by first evacuating the pods on the node.

For pods that are made highly available by the routing tier, nothing
else needs to be done. For other pods needing storage, typically databases, it
is critical to ensure that they can remain in operation with one pod
temporarily going offline. While implementing resiliency for stateful pods
is different for each application, in all cases it is important to configure
the scheduler to use node anti-affinity to
ensure that the pods are properly spread across available nodes.

Another challenge is how to handle nodes that are running critical
infrastructure such as the router or the registry. The same node evacuation
process applies, though it is important to understand certain edge cases.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

[id="nodes-nodes-rebooting-infrastructure_{context}"]
= About rebooting nodes running critical infrastructure

[role="_abstract"]
When rebooting nodes that host critical OpenShift Container Platform infrastructure components, such as router pods, registry pods, and monitoring pods, ensure that there are at least three nodes available to run these components.

The following scenario demonstrates how service interruptions can occur with applications running on OpenShift Container Platform when only two nodes are available:

- Node A is marked unschedulable and all pods are evacuated.
- The registry pod running on that node is now redeployed on node B. Node B is now running both registry pods.
- Node B is now marked unschedulable and is evacuated.
- The service exposing the two pod endpoints on node B loses all endpoints, for a brief period of time, until they are redeployed to node A.

When using three nodes for infrastructure components, this process does not result in a service disruption. However, due to pod scheduling, the last node that is evacuated and brought back into rotation does not have a registry pod. One of the other nodes has two registry pods. To schedule the third registry pod on the last node, use pod anti-affinity to prevent the scheduler from locating two registry pods on the same node.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

[id="nodes-nodes-rebooting-affinity_{context}"]
= Rebooting a node using pod anti-affinity

[role="_abstract"]
You can use pod anti-affinity to spread the workloads on a node to other nodes before performing a graceful node restart.

Pod anti-affinity is slightly different from node anti-affinity. Node anti-affinity can be
violated if there are no other suitable locations to deploy a pod. Pod
anti-affinity can be set to either required or preferred.

With this in place, if only two infrastructure nodes are available and one is rebooted, the container image registry
pod is prevented from running on the other node. `*oc get pods*` reports the pod as unready until a suitable node is available.
Once a node is available and all pods are back in ready state, the next node can be restarted.

The following procedure demonstrates how to reboot a node by using pod anti-affinity.

.Procedure

. Edit the node specification to configure pod anti-affinity:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: with-pod-antiaffinity
spec:
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: registry
              operator: In
              values:
              - default
          topologyKey: kubernetes.io/hostname
#...
----
where:

`spec.affinity.podAntiAffinity`:: Specifies the stanza to configure pod anti-affinity.
`spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`:: Specifies a preferred rule.
`spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`:: Specifies a weight for a preferred rule. The node with the highest weight is preferred.
`spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`:: Specifies a pod label that determines when the anti-affinity rule applies. Define a key and value for the label.
`spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`:: Specifies the relationship between the label on the existing pod and the set of values in the `matchExpression` parameters in the specification for the new pod. Can be `In`, `NotIn`, `Exists`, or `DoesNotExist`.
+
This example assumes the container image registry pod has a label of
`registry=default`. Pod anti-affinity can use any Kubernetes match
expression.

. Enable the `MatchInterPodAffinity` scheduler predicate in the scheduling policy file.
. Perform a graceful restart of the node.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

[id="nodes-nodes-rebooting-router_{context}"]
= Understanding how to reboot nodes running routers

[role="_abstract"]
Review the following information to learn how to reboot a node that hosts a router pod.

In most cases, a pod running an OpenShift Container Platform router exposes a host port.

The `PodFitsPorts` scheduler predicate ensures that no router pods using the
same port can run on the same node, and pod anti-affinity is achieved. If the
routers are relying on IP failover for high availability, there is nothing else that is needed.

For router pods relying on an external service such as AWS Elastic Load Balancing for high
availability, it is that service's responsibility to react to router pod restarts.

In rare cases, a router pod may not have a host port configured. In those cases,
it is important to follow the recommended restart process for infrastructure nodes.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-rebooting.adoc

[id="nodes-nodes-rebooting-gracefully_{context}"]
= Rebooting a node gracefully

[role="_abstract"]
You can perform a graceful restart of a node, where all workloads are moved to other nodes, without data loss or service disruption.

The Windows Machine Config Operator (WMCO) minimizes node reboots whenever possible. However, certain operations and updates require a reboot to ensure that changes are applied correctly and securely. To safely reboot your Windows nodes, use the graceful reboot process. For information on gracefully rebooting a standard OpenShift Container Platform node, see "Rebooting a node gracefully" in the Nodes documentation.

Before rebooting a node, it is recommended to backup etcd data to avoid any data loss on the node.

[NOTE]
====
For {sno} clusters that require users to perform the `oc login` command rather than having the certificates in `kubeconfig` file to manage the cluster, the `oc adm` commands might not be available after cordoning and draining the node. This is because the `openshift-oauth-apiserver` pod is not running due to the cordon. You can use SSH to access the nodes as indicated in the following procedure.

In a {sno} cluster, pods cannot be rescheduled when cordoning and draining. However, doing so gives the pods, especially your workload pods, time to properly stop and release associated resources.
====

The following procedure demonstrates how to perform a graceful restart of a node.

.Procedure

. Mark the node as unschedulable:
+
[source,terminal]
----
$ oc adm cordon <node1>
----

. Drain the node to remove all the running pods:
+
[source,terminal]
----
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force
----
+
You might receive errors that pods associated with custom pod disruption budgets (PDB) cannot be evicted.
+
.Example error
[source,terminal]
----
error when evicting pods/"rails-postgresql-example-1-72v2w" -n "rails" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
----
+
In this case, run the drain command again, adding the `disable-eviction` flag, which bypasses the PDB checks:
+
[source,terminal]
----
$ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
----

. Access the node in debug mode:
+
[source,terminal]
----
$ oc debug node/<node1>
----

. Change your root directory to `/host`:
+
[source,terminal]
----
$ chroot /host
----

. Restart the node:
+
[source,terminal]
----
$ systemctl reboot
----
+
In a moment, the node enters the `NotReady` state.
+
[NOTE]
====
With some {sno} clusters, the `oc` commands might not be available after you cordon and drain the node because the `openshift-oauth-apiserver` pod is not running. You can use SSH to connect to the node and perform the reboot.

[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain>
----

[source,terminal]
----
$ sudo systemctl reboot
----
====
. SSH into the Windows node and enter PowerShell by running the following command:
+
[source,terminal]
----
C:\> powershell
----

. Restart the node by running the following command:
+
[source,terminal]
----
C:\>  Restart-Computer -Force
----

. Windows nodes on Amazon Web Services (AWS) do not return to `READY` state after a graceful reboot due to an inconsistency with the EC2 instance metadata routes and the Host Network Service (HNS) networks.
+
After the reboot, SSH into any Windows node on AWS and add the route by running the following command in a shell prompt:
+
[source,terminal]
----
C:\> route add 169.254.169.254 mask 255.255.255.0 <gateway_ip>
----
+
where:
+
--
`169.254.169.254`:: Specifies the address of the EC2 instance metadata endpoint.
`255.255.255.255`:: Specifies the network mask of the EC2 instance metadata endpoint.
`<gateway_ip>`:: Specifies the corresponding IP address of the gateway in the Windows instance, which you can find by running the following command:
+
[source,terminal]
----
C:\> ipconfig | findstr /C:"Default Gateway"
----
--

. After the reboot is complete, mark the node as schedulable by running the following command:
+
[source,terminal]
----
$ oc adm uncordon <node1>
----
+
[NOTE]
====
With some {sno} clusters, the `oc` commands might not be available after you cordon and drain the node because the `openshift-oauth-apiserver` pod is not running. You can use SSH to connect to the node and uncordon it.

[source,terminal]
----
$ ssh core@<target_node>
----

[source,terminal]
----
$ sudo oc adm uncordon <node> --kubeconfig /etc/kubernetes/static-pod-resources/kube-apiserver-certs/secrets/node-kubeconfigs/localhost.kubeconfig
----
====

. Verify that the node is ready:
+
[source,terminal]
----
$ oc get node <node1>
----
+
.Example output
[source,terminal]
----
NAME    STATUS  ROLES    AGE     VERSION
<node1> Ready   worker   6d22h   v1.18.3+b0068a8
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Placing pods relative to other pods using affinity and anti-affinity rules
* Backing up etcd data
