---
title: "Replacing an unhealthy etcd member"
type: reference
domain: openshift
slug: etcd-4-22-replace-unhealthy-etcd-member
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/replace-unhealthy-etcd-member
version: 4.22
family: etcd
documentKind: "Documentation"
---

# Replacing an unhealthy etcd member

//NOTE TO CONTRIBUTORS:
//
//If you update any of the content in this assembly file, be sure to also make the same changes in the assemblies in the following file: backup_and_restore/control_plane_backup_and_restore/replacing-unhealthy-etcd-member.adoc.

[id="replace-unhealthy-etcd-member"]
= Replacing an unhealthy etcd member

The process to replace a single unhealthy etcd member depends on whether the etcd member is unhealthy because the machine is not running or the node is not ready, or because the etcd pod is crashlooping.

[NOTE]
====
If you have lost the majority of your control plane hosts, follow the disaster recovery procedure to restore to a previous cluster state instead of this procedure.

If the control plane certificates are not valid on the member being replaced, then you must follow the procedure to recover from expired control plane certificates instead of this procedure.

If a control plane node is lost and a new one is created, the etcd cluster Operator handles generating the new TLS certificates and adding the node as an etcd member.
====

// Identifying an unhealthy etcd member
// Module included in the following assemblies:
//
// * backup_and_restore/replacing-unhealthy-etcd-member.adoc
// * etcd/etcd-backup-restore/replace-unhealthy-etcd-member.adoc

[id="restore-identify-unhealthy-etcd-member_{context}"]
= Identifying an unhealthy etcd member

You can identify if your cluster has an unhealthy etcd member.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup. For more information, see "Backing up etcd data".

.Procedure

. Check the status of the `EtcdMembersAvailable` status condition using the following command:
+
[source,terminal]
----
$ oc get etcd -o=jsonpath='{range .items[0].status.conditions[?(@.type=="EtcdMembersAvailable")]}{.message}{"\n"}{end}'
----

. Review the output:
+
[source,terminal]
----
2 of 3 members are available, ip-10-0-131-183.ec2.internal is unhealthy
----
+
This example output shows that the `ip-10-0-131-183.ec2.internal` etcd member is unhealthy.

// Determining the state of the unhealthy etcd member
// Module included in the following assemblies:
//
// * backup_and_restore/replacing-unhealthy-etcd-member.adoc
// * etcd/etcd-backup-restore/replace-unhealthy-etcd-member.adoc

[id="restore-determine-state-etcd-member_{context}"]
= Determining the state of the unhealthy etcd member

The steps to replace an unhealthy etcd member depend on which of the following states your etcd member is in:

* The machine is not running or the node is not ready
* The etcd pod is crashlooping

This procedure determines which state your etcd member is in. This enables you to know which procedure to follow to replace the unhealthy etcd member.

[NOTE]
====
If you are aware that the machine is not running or the node is not ready, but you expect it to return to a healthy state soon, then you do not need to perform a procedure to replace the etcd member. The etcd cluster Operator will automatically sync when the machine or node returns to a healthy state.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have identified an unhealthy etcd member.

.Procedure

. Determine if the *machine is not running*:
+
[source,terminal]
----
$ oc get machines -A -ojsonpath='{range .items[*]}{@.status.nodeRef.name}{"\t"}{@.status.providerStatus.instanceState}{"\n"}' | grep -v running
----
+
.Example output
[source,terminal]
----
ip-10-0-131-183.ec2.internal  stopped <1>
----
<1> This output lists the node and the status of the node's machine. If the status is anything other than `running`, then the *machine is not running*.
+
// TODO: xref
If the *machine is not running*, then follow the _Replacing an unhealthy etcd member whose machine is not running or whose node is not ready_ procedure.

. Determine if the *node is not ready*.
+
If either of the following scenarios are true, then the *node is not ready*.

** If the machine is running, then check whether the node is unreachable:
+
[source,terminal]
----
$ oc get nodes -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{"\t"}{range .spec.taints[*]}{.key}{" "}' | grep unreachable
----
+
.Example output
[source,terminal]
----
ip-10-0-131-183.ec2.internal	node-role.kubernetes.io/master node.kubernetes.io/unreachable node.kubernetes.io/unreachable <1>
----
<1> If the node is listed with an `unreachable` taint, then the *node is not ready*.

** If the node is still reachable, then check whether the node is listed as `NotReady`:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/master | grep "NotReady"
----
+
.Example output
[source,terminal]
----
ip-10-0-131-183.ec2.internal   NotReady   master   122m   v1.35.4 <1>
----
<1> If the node is listed as `NotReady`, then the *node is not ready*.

+
// TODO: xref
If the *node is not ready*, then follow the _Replacing an unhealthy etcd member whose machine is not running or whose node is not ready_ procedure.

. Determine if the *etcd pod is crashlooping*.
+
If the machine is running and the node is ready, then check whether the etcd pod is crashlooping.

.. Verify that all control plane nodes are listed as `Ready`:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/master
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES    AGE     VERSION
ip-10-0-131-183.ec2.internal   Ready    master   6h13m   v1.35.4
ip-10-0-164-97.ec2.internal    Ready    master   6h13m   v1.35.4
ip-10-0-154-204.ec2.internal   Ready    master   6h13m   v1.35.4
----

.. Check whether the status of an etcd pod is either `Error` or `CrashloopBackoff`:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd
----
+
.Example output
[source,terminal]
----
etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m <1>
etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
----
<1> Since this status of this pod is `Error`, then the *etcd pod is crashlooping*.

+
// TODO: xref
If the *etcd pod is crashlooping*, then follow the _Replacing an unhealthy etcd member whose etcd pod is crashlooping_ procedure.

== Replacing the unhealthy etcd member

Depending on the state of your unhealthy etcd member, use one of the following procedures:

* Replacing an unhealthy etcd member whose machine is not running or whose node is not ready
* Replacing a control plane node on an unhealthy cluster
* Replacing an unhealthy etcd member whose etcd pod is crashlooping
* Replacing an unhealthy stopped baremetal etcd member

// Replacing an unhealthy etcd member whose machine is not running or whose node is not ready
// Module included in the following assemblies:
//
// * backup_and_restore/control_plane_backup_and_restore/modules/restore-replace-stopped-etcd-member.adoc
// * etcd/etcd-backup-restore/replace-unhealthy-etcd-member.adoc

[id="restore-replace-stopped-etcd-member_{context}"]
= Replacing an unhealthy etcd member whose machine is not running or whose node is not ready

This procedure details the steps to replace an etcd member that is unhealthy either because the machine is not running or because the node is not ready.

[NOTE]
====
If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in "Troubleshooting the control plane machine set" for an etcd recovery procedure.
====

.Prerequisites

* You have identified the unhealthy etcd member.
* You have verified that either the machine is not running or the node is not ready.
+
[IMPORTANT]
====
You must wait if you power off other control plane nodes. The control plane nodes must remain powered off until the replacement of an unhealthy etcd member is complete.
====
+
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup.
+
[IMPORTANT]
====
Before you perform this procedure, take an etcd backup so that you can restore your cluster if you experience any issues.
====

.Procedure

. Remove the unhealthy member.

.. Choose a pod that is not on the affected node:
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd
----
+
.Example output
[source,terminal]
----
etcd-ip-10-0-131-183.ec2.internal                3/3     Running     0          123m
etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
----

.. Connect to the running etcd container, passing in the name of a pod that is not on the affected node:
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
----

.. View the member list:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 6fc1e7c9db35841d | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
| 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
| ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
Take note of the ID and the name of the unhealthy etcd member because these values are needed later in the procedure. The `$ etcdctl endpoint health` command will list the removed member until the procedure of replacement is finished and a new member is added.

.. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:
+
[source,terminal]
----
sh-4.2# etcdctl member remove 6fc1e7c9db35841d
----
+
.Example output
[source,terminal]
----
Member 6fc1e7c9db35841d removed from cluster ead669ce1fbfb346
----

.. View the member list again and verify that the member was removed:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
| ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
You can now exit the node shell.

. Turn off the quorum guard by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----
+
This command ensures that you can successfully re-create secrets and roll out the static pods.
+
[IMPORTANT]
====
After you turn off the quorum guard, the cluster might be unreachable for a short time while the remaining etcd instances reboot to reflect the configuration change.
====
+
[NOTE]
====
etcd cannot tolerate any additional member failure when running with two members. Restarting either remaining member breaks the quorum and causes downtime in your cluster. The quorum guard protects etcd from restarts due to configuration changes that could cause downtime, so it must be disabled to complete this procedure.
====

. Delete the affected node by running the following command:
+
[source,terminal]
----
$ oc delete node <node_name>
----
+
.Example command
[source,terminal]
----
$ oc delete node ip-10-0-131-183.ec2.internal
----

. Remove the old secrets for the unhealthy etcd member that was removed.

.. List the secrets for the unhealthy etcd member that was removed.
+
[source,terminal]
----
$ oc get secrets -n openshift-etcd | grep ip-10-0-131-183.ec2.internal <1>
----
<1> Pass in the name of the unhealthy etcd member that you took note of earlier in this procedure.
+
There is a peer, serving, and metrics secret as shown in the following output:
+
.Example output
[source,terminal]
----
etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
----

.. Delete the secrets for the unhealthy etcd member that was removed.

... Delete the peer secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
----

... Delete the serving secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
----

... Delete the metrics secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
----

. Check whether a control plane machine set exists by entering the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get controlplanemachineset
----

* If the control plane machine set exists, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically. For more information, see "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready".
+
If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.

.. Obtain the machine for the unhealthy member.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped <1>
clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
----
<1> This is the control plane machine for the unhealthy node, `ip-10-0-131-183.ec2.internal`.

.. Delete the machine of the unhealthy member:
+
[source,terminal]
----
$ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0 <1>
----
<1> Specify the name of the control plane machine for the unhealthy node.
+
A new machine is automatically provisioned after deleting the machine of the unhealthy member.

.. Verify that a new machine was created:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running <1>
clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
----
<1> The new machine, `clustername-8qw5l-master-3` is being created and is ready once the phase changes from `Provisioning` to `Running`.
+
It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.
+
[NOTE]
====
Verify the subnet IDs that you are using for your machine sets to ensure that they end up in the correct availability zone.
====

* If the control plane machine set does not exist, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically.
+
If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.

.. Obtain the machine for the unhealthy member.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped <1>
clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
----
<1> This is the control plane machine for the unhealthy node, `ip-10-0-131-183.ec2.internal`.

.. Save the machine configuration to a file on your file system:
+
[source,terminal]
----
$ oc get machine clustername-8qw5l-master-0 \ <1>
    -n openshift-machine-api \
    -o yaml \
    > new-master-machine.yaml
----
<1> Specify the name of the control plane machine for the unhealthy node.

.. Edit the `new-master-machine.yaml` file that was created in the previous step to assign a new name and remove unnecessary fields.

... Remove the entire `status` section:
+
[source,yaml]
----
status:
  addresses:
  - address: 10.0.131.183
    type: InternalIP
  - address: ip-10-0-131-183.ec2.internal
    type: InternalDNS
  - address: ip-10-0-131-183.ec2.internal
    type: Hostname
  lastUpdated: "2020-04-20T17:44:29Z"
  nodeRef:
    kind: Node
    name: ip-10-0-131-183.ec2.internal
    uid: acca4411-af0d-4387-b73e-52b2484295ad
  phase: Running
  providerStatus:
    apiVersion: awsproviderconfig.openshift.io/v1beta1
    conditions:
    - lastProbeTime: "2020-04-20T16:53:50Z"
      lastTransitionTime: "2020-04-20T16:53:50Z"
      message: machine successfully created
      reason: MachineCreationSucceeded
      status: "True"
      type: MachineCreation
    instanceId: i-0fdb85790d76d0c3f
    instanceState: stopped
    kind: AWSMachineProviderStatus
----

... Change the `metadata.name` field to a new name.
+
Keep the same base name as the old machine and change the ending number to the next available number. In this example, `clustername-8qw5l-master-0` is changed to `clustername-8qw5l-master-3`.
+
For example:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
  name: clustername-8qw5l-master-3
  ...
----

... Remove the `spec.providerID` field:
+
[source,yaml]
----
  providerID: aws:///us-east-1a/i-0fdb85790d76d0c3f
----

.. Delete the machine of the unhealthy member:
+
[source,terminal]
----
$ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0 <1>
----
<1> Specify the name of the control plane machine for the unhealthy node.

.. Verify that the machine was deleted:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
----

.. Create the new machine by using the `new-master-machine.yaml` file:
+
[source,terminal]
----
$ oc apply -f new-master-machine.yaml
----

.. Verify that the new machine was created:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running <1>
clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
----
<1> The new machine, `clustername-8qw5l-master-3` is being created and is ready once the phase changes from `Provisioning` to `Running`.
+
It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

. Turn the quorum guard back on by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

. You can verify that the `unsupportedConfigOverrides` section is removed from the object by entering this command:
+
[source,terminal]
----
$ oc get etcd/cluster -oyaml
----

. If you are using {sno}, restart the node. Otherwise, you might experience the following error in the etcd cluster Operator:
+
.Example output
[source,terminal]
----
EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
----

.Verification

. Verify that all etcd pods are running properly.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd
----
+
.Example output
[source,terminal]
----
etcd-ip-10-0-133-53.ec2.internal                 3/3     Running     0          7m49s
etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
----
+
If the output from the previous command only lists two pods, you can manually force an etcd redeployment. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge <1>
----
<1> The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.

. Verify that there are exactly three etcd members.

.. Connect to the running etcd container, passing in the name of a pod that was not on the affected node:
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
----

.. View the member list:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 5eb0d6b8ca24730c | started |  ip-10-0-133-53.ec2.internal |  https://10.0.133.53:2380 |  https://10.0.133.53:2379 |
| 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
| ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.
+
[WARNING]
====
Be sure to remove the correct etcd member; removing a good etcd member might lead to quorum loss.
====

[role="_additional-resources"]
.Additional resources
* Recovering a degraded etcd Operator
* Replacing a control plane node on an unhealthy cluster

// Replacing an unhealthy etcd member whose etcd pod is crashlooping
// Module included in the following assemblies:
//
// * backup_and_restore/replacing-unhealthy-etcd-member.adoc
// * etcd/etcd-backup-restore/replace-unhealthy-etcd-member.adoc

[id="restore-replace-crashlooping-etcd-member_{context}"]
= Replacing an unhealthy etcd member whose etcd pod is crashlooping

This procedure details the steps to replace an etcd member that is unhealthy because the etcd pod is crashlooping.

.Prerequisites

* You have identified the unhealthy etcd member.
* You have verified that the etcd pod is crashlooping.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup.
+
[IMPORTANT]
====
It is important to take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.
====

.Procedure

. Stop the crashlooping etcd pod.

.. Debug the node that is crashlooping.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc debug node/ip-10-0-131-183.ec2.internal <1>
----
<1> Replace this with the name of the unhealthy node.

.. Change your root directory to `/host`:
+
[source,terminal]
----
sh-4.2# chroot /host
----

.. Move the existing etcd pod file out of the kubelet manifest directory:
+
[source,terminal]
----
sh-4.2# mkdir /var/lib/etcd-backup
----
+
[source,terminal]
----
sh-4.2# mv /etc/kubernetes/manifests/etcd-pod.yaml /var/lib/etcd-backup/
----

.. Move the etcd data directory to a different location:
+
[source,terminal]
----
sh-4.2# mv /var/lib/etcd/ /tmp
----
+
You can now exit the node shell.

. Remove the unhealthy member.

.. Choose a pod that is _not_ on the affected node.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd
----
+
.Example output
[source,terminal]
----
etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m
etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
----

.. Connect to the running etcd container, passing in the name of a pod that is not on the affected node.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
----

.. View the member list:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| 62bcf33650a7170a | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
| b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
| d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
Take note of the ID and the name of the unhealthy etcd member, because these values are needed later in the procedure.

.. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:
+
[source,terminal]
----
sh-4.2# etcdctl member remove 62bcf33650a7170a
----
+
.Example output
[source,terminal]
----
Member 62bcf33650a7170a removed from cluster ead669ce1fbfb346
----

.. View the member list again and verify that the member was removed:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+------------------------------+---------------------------+---------------------------+
|        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
+------------------+---------+------------------------------+---------------------------+---------------------------+
| b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
| d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
+------------------+---------+------------------------------+---------------------------+---------------------------+
----
+
You can now exit the node shell.

. Turn off the quorum guard by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----
+
This command ensures that you can successfully re-create secrets and roll out the static pods.

. Remove the old secrets for the unhealthy etcd member that was removed.

.. List the secrets for the unhealthy etcd member that was removed.
+
[source,terminal]
----
$ oc get secrets -n openshift-etcd | grep ip-10-0-131-183.ec2.internal <1>
----
<1> Pass in the name of the unhealthy etcd member that you took note of earlier in this procedure.
+
There is a peer, serving, and metrics secret as shown in the following output:
+
.Example output
[source,terminal]
----
etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
----

.. Delete the secrets for the unhealthy etcd member that was removed.

... Delete the peer secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
----

... Delete the serving secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
----

... Delete the metrics secret:
+
[source,terminal]
----
$ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
----

. Force etcd redeployment.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "single-master-recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge <1>
----
<1> The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.
+
When the etcd cluster Operator performs a redeployment, it ensures that all control plane nodes have a functioning etcd pod.

. Turn the quorum guard back on by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

. You can verify that the `unsupportedConfigOverrides` section is removed from the object by entering this command:
+
[source,terminal]
----
$ oc get etcd/cluster -oyaml
----

. If you are using {sno}, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:
+
.Example output
[source,terminal]
----
EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
----

.Verification

* Verify that the new member is available and healthy.

.. Connect to the running etcd container again.
+
In a terminal that has access to the cluster as a cluster-admin user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
----

.. Verify that all members are healthy:
+
[source,terminal]
----
sh-4.2# etcdctl endpoint health
----
+
.Example output
[source,terminal]
----
https://10.0.131.183:2379 is healthy: successfully committed proposal: took = 16.671434ms
https://10.0.154.204:2379 is healthy: successfully committed proposal: took = 16.698331ms
https://10.0.164.97:2379 is healthy: successfully committed proposal: took = 16.621645ms
----

// Replacing an unhealthy baremetal stopped etcd member
// Module included in the following assemblies:
//
// * /backup_and_restore/control_plane_backup_and_restore/replacing-unhealthy-etcd-member.adoc
// * etcd/etcd-backup-restore/replace-unhealthy-etcd-member.adoc

[id="restore-replace-stopped-baremetal-etcd-member_{context}"]
= Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready

This procedure details the steps to replace a bare metal etcd member that is unhealthy either because the machine is not running or because the node is not ready.

If you are running installer-provisioned infrastructure or you used the Machine API to create your machines, follow these steps. Otherwise you must create the new control plane node using the same method that was used to originally create it.

.Prerequisites

* You have identified the unhealthy bare metal etcd member.
* You have verified that either the machine is not running or the node is not ready.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup.
+
[IMPORTANT]
====
You must take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.
====

.Procedure

. Verify and remove the unhealthy member.

.. Choose a pod that is _not_ on the affected node:
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
----
+
.Example output
[source,terminal]
----
etcd-openshift-control-plane-0   5/5   Running   11   3h56m   192.168.10.9   openshift-control-plane-0  <none>           <none>
etcd-openshift-control-plane-1   5/5   Running   0    3h54m   192.168.10.10   openshift-control-plane-1   <none>           <none>
etcd-openshift-control-plane-2   5/5   Running   0    3h58m   192.168.10.11   openshift-control-plane-2   <none>           <none>
----
.. Connect to the running etcd container, passing in the name of a pod that is not on the affected node:
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
----

.. View the member list:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
| ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
+------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
| 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
| 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
| cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380/ | https://192.168.10.9:2379/   | false |
+------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
----
+
Take note of the ID and the name of the unhealthy etcd member, because these values are required later in the procedure. The `etcdctl endpoint health` command will list the removed member until the replacement procedure is completed and the new member is added.

.. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:
+
[WARNING]
====
Be sure to remove the correct etcd member; removing a good etcd member might lead to quorum loss.
====
+
[source,terminal]
----
sh-4.2# etcdctl member remove 7a8197040a5126c8
----
+
.Example output
[source,terminal]
----
Member 7a8197040a5126c8 removed from cluster b23536c33f2cdd1b
----

.. View the member list again and verify that the member was removed:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
| ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
+------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
| cc3830a72fc357f9 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
| 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
+------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
----
+
You can now exit the node shell.
+
[IMPORTANT]
====
After you remove the member, the cluster might be unreachable for a short time while the remaining etcd instances reboot.
====

. Turn off the quorum guard by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----
+
This command ensures that you can successfully re-create secrets and roll out the static pods.

. Remove the old secrets for the unhealthy etcd member that was removed by running the following commands.

.. List the secrets for the unhealthy etcd member that was removed.
+
[source,terminal]
----
$ oc get secrets -n openshift-etcd | grep openshift-control-plane-2
----
Pass in the name of the unhealthy etcd member that you took note of earlier in this procedure.
+
There is a peer, serving, and metrics secret as shown in the following output:
+

[source,terminal]
----
etcd-peer-openshift-control-plane-2             kubernetes.io/tls   2   134m
etcd-serving-metrics-openshift-control-plane-2  kubernetes.io/tls   2   134m
etcd-serving-openshift-control-plane-2          kubernetes.io/tls   2   134m
----

.. Delete the secrets for the unhealthy etcd member that was removed.

... Delete the peer secret:
+
[source,terminal]
----
$ oc delete secret etcd-peer-openshift-control-plane-2 -n openshift-etcd

secret "etcd-peer-openshift-control-plane-2" deleted
----

... Delete the serving secret:
+
[source,terminal]
----
$ oc delete secret etcd-serving-metrics-openshift-control-plane-2 -n openshift-etcd

secret "etcd-serving-metrics-openshift-control-plane-2" deleted
----

... Delete the metrics secret:
+
[source,terminal]
----
$ oc delete secret etcd-serving-openshift-control-plane-2 -n openshift-etcd

secret "etcd-serving-openshift-control-plane-2" deleted
----

. Obtain the machine for the unhealthy member.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                               PROVIDERID                                                                                              STATE
examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned <1>
examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
examplecluster-control-plane-2    Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
----
<1> This is the control plane machine for the unhealthy node, `examplecluster-control-plane-2`.

. Ensure that the Bare Metal Operator is available by running the following command:
+
[source,terminal]
----
$ oc get clusteroperator baremetal
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
baremetal   .0    True        False         False      3d15h
----

. Remove the old `BareMetalHost` object by running the following command:
+
[source,terminal]
----
$ oc delete bmh openshift-control-plane-2 -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
baremetalhost.metal3.io "openshift-control-plane-2" deleted
----

. Delete the machine of the unhealthy member by running the following command:
+
[source,terminal]
----
$ oc delete machine -n openshift-machine-api examplecluster-control-plane-2
----
+
After you remove the `BareMetalHost` and `Machine` objects, then the `Machine` controller automatically deletes the `Node` object.
+
If deletion of the machine is delayed for any reason or the command is obstructed and delayed, you can force deletion by removing the machine object finalizer field.
+
[IMPORTANT]
====
Do not interrupt machine deletion by pressing `Ctrl+c`. You must allow the command to proceed to completion. Open a new terminal window to edit and delete the finalizer fields.
====
+
A new machine is automatically provisioned after deleting the machine of the unhealthy member.
+
.. Edit the machine configuration by running the following command:
+
[source,terminal]
----
$ oc edit machine -n openshift-machine-api examplecluster-control-plane-2
----
+
.. Delete the following fields in the `Machine` custom resource, and then save the updated file:
+
[source,yaml]
----
finalizers:
- machine.machine.openshift.io
----
+
.Example output
[source,terminal]
----
machine.machine.openshift.io/examplecluster-control-plane-2 edited
----

. Verify that the machine was deleted by running the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                                 PROVIDERID                                                                                       STATE
examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
----
+
. Verify that the node has been deleted by running the following command:
+
[source,terminal]
----
$ oc get nodes

NAME                     STATUS ROLES   AGE   VERSION
openshift-control-plane-0 Ready master 3h24m v1.35.4
openshift-control-plane-1 Ready master 3h24m v1.35.4
openshift-compute-0       Ready worker 176m v1.35.4
openshift-compute-1       Ready worker 176m v1.35.4
----

. Create the new `BareMetalHost` object and the secret to store the BMC credentials:

+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: openshift-control-plane-2-bmc-secret
  namespace: openshift-machine-api
data:
  password: <password>
  username: <username>
type: Opaque
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: openshift-control-plane-2
  namespace: openshift-machine-api
spec:
  automatedCleaningMode: disabled
  bmc:
    address: redfish://10.46.61.18:443/redfish/v1/Systems/1
    credentialsName: openshift-control-plane-2-bmc-secret
    disableCertificateVerification: true
  bootMACAddress: 48:df:37:b0:8a:a0
  bootMode: UEFI
  externallyProvisioned: false
  online: true
  rootDeviceHints:
    deviceName: /dev/disk/by-id/scsi-<serial_number>
  userData:
    name: master-user-data-managed
    namespace: openshift-machine-api
EOF
----
+
[NOTE]
====
The username and password can be found from the other bare metal host's secrets. The protocol to use in `bmc:address` can be taken from other bmh objects.
====
+
[IMPORTANT]
====
If you reuse the `BareMetalHost` object definition from an existing control plane host, do not leave the `externallyProvisioned` field set to `true`.

Existing control plane `BareMetalHost` objects may have the `externallyProvisioned` flag set to `true` if they were provisioned by the OpenShift Container Platform installation program.
====
+
After the inspection is complete, the `BareMetalHost` object is created and available to be provisioned.

. Verify the creation process using available `BareMetalHost` objects:
+
[source,terminal]

----
$ oc get bmh -n openshift-machine-api

NAME                      STATE                  CONSUMER                      ONLINE ERROR   AGE
openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
openshift-control-plane-2 available              examplecluster-control-plane-3 true         47m
openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
----

.. Verify that a new machine has been created:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api -o wide
----
+
.Example output
[source,terminal]
----
NAME                                   PHASE     TYPE   REGION   ZONE   AGE     NODE                              PROVIDERID                                                                                            STATE
examplecluster-control-plane-0         Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned <1>
examplecluster-control-plane-1         Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
examplecluster-control-plane-2         Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
examplecluster-compute-0               Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
examplecluster-compute-1               Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
----
<1> The new machine, `clustername-8qw5l-master-3` is being created and is ready after the phase changes from `Provisioning` to `Running`.
+
It should take a few minutes for the new machine to be created. The etcd cluster Operator will automatically sync when the machine or node returns to a healthy state.

.. Verify that the bare metal host becomes provisioned and no error reported by running the following command:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
$ oc get bmh -n openshift-machine-api
NAME                      STATE                  CONSUMER                       ONLINE ERROR AGE
openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
openshift-control-plane-2 provisioned            examplecluster-control-plane-3 true          47m
openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
----

.. Verify that the new node is added and in a ready state by running this command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
$ oc get nodes
NAME                     STATUS ROLES   AGE   VERSION
openshift-control-plane-0 Ready master 4h26m v1.35.4
openshift-control-plane-1 Ready master 4h26m v1.35.4
openshift-control-plane-2 Ready master 12m   v1.35.4
openshift-compute-0       Ready worker 3h58m v1.35.4
openshift-compute-1       Ready worker 3h58m v1.35.4
----

. Turn the quorum guard back on by entering the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

. You can verify that the `unsupportedConfigOverrides` section is removed from the object by entering this command:
+
[source,terminal]
----
$ oc get etcd/cluster -oyaml
----

. If you are using {sno}, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:
+
.Example output
[source,terminal]
----
EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
----

.Verification

. Verify that all etcd pods are running properly.
+
In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc -n openshift-etcd get pods -l k8s-app=etcd
----
+
.Example output
[source,terminal]
----
etcd-openshift-control-plane-0      5/5     Running     0     105m
etcd-openshift-control-plane-1      5/5     Running     0     107m
etcd-openshift-control-plane-2      5/5     Running     0     103m
----
+
If the output from the previous command only lists two pods, you can manually force an etcd redeployment. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge <1>
----
+
<1> The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.
+
To verify there are exactly three etcd members, connect to the running etcd container, passing in the name of a pod that was not on the affected node. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:
+
[source,terminal]
----
$ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
----
+
. View the member list:
+
[source,terminal]
----
sh-4.2# etcdctl member list -w table
----
+
.Example output
[source,terminal]
----
+------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
|        ID        | STATUS  |        NAME        |        PEER ADDRS         |       CLIENT ADDRS        |    IS LEARNER    |
+------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
| 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380 | https://192.168.10.11:2379 |   false |
| 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380 | https://192.168.10.10:2379 |   false |
| cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380 | https://192.168.10.9:2379 |     false |
+------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
----
+
[NOTE]
====
If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.
====
+

. Verify that all etcd members are healthy by running the following command:

+
[source,terminal]
----
# etcdctl endpoint health --cluster
----
+
.Example output
[source,terminal]
----
https://192.168.10.10:2379 is healthy: successfully committed proposal: took = 8.973065ms
https://192.168.10.9:2379 is healthy: successfully committed proposal: took = 11.559829ms
https://192.168.10.11:2379 is healthy: successfully committed proposal: took = 11.665203ms
----
+
. Validate that all nodes are at the latest revision by running the following command:
+
[source,terminal]
----
$ oc get etcd -o=jsonpath='{range.items[0].status.conditions[?(@.type=="NodeInstallerProgressing")]}{.reason}{"\n"}{.message}{"\n"}'
----
+
----
AllNodesAtLatestRevision
----

[role="_additional-resources"]
.Additional resources
* Quorum protection with machine lifecycle hooks
