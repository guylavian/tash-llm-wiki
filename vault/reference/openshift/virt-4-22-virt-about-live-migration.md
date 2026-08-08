---
title: "About live migration"
type: reference
domain: openshift
slug: virt-4-22-virt-about-live-migration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-about-live-migration
version: 4.22
family: virt
documentKind: "Documentation"
---

# About live migration

[id="virt-about-live-migration"]
= About live migration

[role="_abstract"]
Live migration is the process of moving a running virtual machine (VM) to another node in the cluster without interrupting the virtual workload. Live migration enables smooth transitions during cluster upgrades or any time a node needs to be drained for maintenance or configuration changes. By default, live migration traffic is encrypted using Transport Layer Security (TLS).

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc
// * virt/install/virt-requirements.adoc

[id="virt-live-migration-requirements_{context}"]
= Live migration requirements

[role="_abstract"]
Live migration requires shared storage, sufficient resources, and compatible CPUs across nodes.

Live migration requirements::

* Shared storage that supports live migration.
* Shared storage with `ReadWriteMany` (RWX) access mode.
* Sufficient RAM and network bandwidth.
+
[NOTE]
====
You must ensure that there is enough memory request capacity in the cluster to support node drains that result in live migrations. You can determine the approximate required spare memory by using the following calculation:

----
Product of (Maximum number of nodes that can drain in parallel) and (Highest total VM memory request allocations across nodes)
----

The default number of migrations that can run in parallel in the cluster is 5. For more information, see "Configuring live migration" in the Additional resources section.
====

* If the virtual machine uses a host model CPU, the nodes must support the virtual machine's host model CPU.

[NOTE]
====
A dedicated Multus network for live migration is highly recommended. For more information, see
"Using a dedicated network for live migration" in the Additional resources section. A dedicated network minimizes the effects of network saturation on tenant workloads during migration.
====

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc

[id="virt-about-live-migration-permissions_{context}"]
= About live migration permissions

[role="_abstract"]
In {VirtProductName} 4.19 and later, live migration operations are restricted to users who are explicitly granted the `kubevirt.io:migrate` cluster role. Users with this role can create, delete, and update virtual machine (VM) live migration requests.

The live migration requests are represented by `VirtualMachineInstanceMigration` (VMIM) custom resources. Cluster administrators can bind the `kubevirt.io:migrate` role to trusted users or groups at either the namespace or cluster level.

Before {VirtProductName} 4.19, namespace administrators had live migration permissions by default. This behavior changed in version 4.19 to prevent unintended or malicious disruptions to infrastructure-critical migration operations.

As a cluster administrator, you can preserve the old behavior by creating a temporary cluster role before updating. After assigning the new role to users, delete the temporary role to enforce the more restrictive permissions. If you have already updated, you can still revert to the old behavior by aggregating the `kubevirt.io:migrate` role into the `admin` cluster role.

//TODO: Remove transition-to-lm-role module in 4.21; relevant in 4.20 due to EUS
// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc

[id="virt-preserving-lm-perms_{context}"]
= Preserving pre-4.19 live migration permissions during update

[role="_abstract"]
Before you update to {VirtProductName} {VirtVersion}, you can create a temporary cluster role to preserve the previous live migration permissions until you are ready for the more restrictive default permissions to take effect.

.Prerequisites

* The {oc-first} is installed.
* You have cluster administrator permissions.

.Procedure

. Before updating to {VirtProductName} {VirtVersion}, create a temporary `ClusterRole` object. For example:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    rbac.authorization.k8s.io/aggregate-to-admin=true
  name: kubevirt.io:upgrademigrate
rules:
- apiGroups:
  - subresources.kubevirt.io
  resources:
  - virtualmachines/migrate
  verbs:
  - update
- apiGroups:
  - kubevirt.io
  resources:
  - virtualmachineinstancemigrations
  verbs:
  - get
  - delete
  - create
  - update
  - patch
  - list
  - watch
  - deletecollection
----
+
This cluster role is aggregated into the `admin` role before you update {VirtProductName}. The update process does not modify it, ensuring the previous behavior is maintained.

. Add the cluster role manifest to the cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f <cluster_role_file_name>.yaml
----

. Update {VirtProductName} to version {VirtVersion}.

. Bind the `kubevirt.io:migrate` cluster role to trusted users or groups by running one of the following commands, replacing `<namespace>`, `<first_user>`, `<second_user>`, and `<group_name>` with your own values.
** To bind the role at the namespace level, run the following command:
+
[source,terminal]
----
$ oc create -n <namespace> rolebinding kvmigrate --clusterrole=kubevirt.io:migrate --user=<first_user> --user=<second_user> --group=<group_name>
----
** To bind the role at the cluster level, run the following command:
+
[source,terminal]
----
$ oc create clusterrolebinding kvmigrate --clusterrole=kubevirt.io:migrate --user=<first_user> --user=<second_user> --group=<group_name>
----

. When you have bound the `kubevirt.io:migrate` role to all necessary users, delete the temporary `ClusterRole` object by running the following command:
+
[source,terminal]
----
$ oc delete clusterrole kubevirt.io:upgrademigrate
----
+
After you delete the temporary cluster role, only users with the `kubevirt.io:migrate` role can create, delete, and update live migration requests.

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc

[id="virt-granting-live-migration-permissions_{context}"]
= Granting live migration permissions

[role="_abstract"]
You can grant trusted users or groups the ability to create, delete, and update live migration instances.

.Prerequisites

* The {oc-first} is installed.
* You have cluster administrator permissions.

.Procedure

* (Optional) To change the default behavior so that namespace administrators always have permission to create, delete, and update live migrations, aggregate the `kubevirt.io:migrate` role into the `admin` cluster role by running the following command:
+
[source,terminal]
----
$ oc label --overwrite clusterrole kubevirt.io:migrate rbac.authorization.k8s.io/aggregate-to-admin=true
----

* Bind the `kubevirt.io:migrate` cluster role to trusted users or groups by running one of the following commands, replacing `<namespace>`, `<first_user>`, `<second_user>`, and `<group_name>` with your own values.
** To bind the role at the namespace level, run the following command:
+
[source,terminal]
----
$ oc create -n <namespace> rolebinding kvmigrate --clusterrole=kubevirt.io:migrate --user=<first_user> --user=<second_user> --group=<group_name>
----
** To bind the role at the cluster level, run the following command:
+
[source,terminal]
----
$ oc create clusterrolebinding kvmigrate --clusterrole=kubevirt.io:migrate --user=<first_user> --user=<second_user> --group=<group_name>
----

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc

[id="virt-vm-migration-tuning_{context}"]
= VM migration tuning

[role="_abstract"]
You can adjust your cluster-wide live migration settings based on the type of workload and migration scenario.

This enables you to control how many VMs migrate at the same time, the network bandwidth you want to use for each migration, and how long {VirtProductName} attempts to complete the migration before canceling the process. Configure these settings in the `HyperConverged` custom resource (CR).

If you are migrating multiple VMs per node at the same time, set a `bandwidthPerMigration` limit to prevent a large or busy VM from using a large portion of the node's network bandwidth. By default, the `bandwidthPerMigration` value is `0`, which means unlimited.

A large VM running a heavy workload (for example, database processing), with higher memory dirty rates, requires a higher bandwidth to complete the migration.

[NOTE]
====
Post copy mode, when enabled, triggers if the initial pre-copy phase does not complete within the defined timeout. During post copy, the VM CPUs pause on the source host while transferring the minimum required memory pages. Then the VM CPUs activate on the destination host, and the remaining memory pages transfer into the destination node at runtime. This can impact performance during the transfer.

Post copy mode should not be used for critical data, or with unstable networks.
====

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-live-migration.adoc

[id="virt-vm-migration-dual-stream_{context}"]
= VM migration support for {op-system} 10.x

[role="_abstract"]

{VirtProductName} 4.22 and later versions supports live migration with {op-system} 10.x worker nodes as a Technology Preview feature.

For information on configuring your cluster to use {op-system} 10.x, refer to the OpenShift Container Platform documentation.

When performing live migration on a cluster using {op-system} 10.x, the migration does not complete successfully when the migration policy uses the attribute `allowPostCopy: true`. This is a known limitation.

Live migration is supported across both {op-system} 9.x and 10.x worker nodes when both versions are present in a cluster. Any VM live migration from {op-system} 10.x to {op-system} 9.x and from {op-system} 9.x to {op-system} 10.x worker nodes, is a Technology Preview feature in OpenShift Container Platform 4.22.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Default cluster roles for {VirtProductName}
* Prometheus queries for live migration
* Configure eviction and run strategies
