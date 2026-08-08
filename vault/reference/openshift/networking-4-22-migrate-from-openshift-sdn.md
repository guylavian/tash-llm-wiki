---
title: "Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin"
type: reference
domain: openshift
slug: networking-4-22-migrate-from-openshift-sdn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/migrate-from-openshift-sdn
version: 4.22
family: networking
documentKind: "Documentation"
---

# Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin

[id="migrate-from-openshift-sdn"]
= Migrating from OpenShift SDN network plugin to OVN-Kubernetes network plugin

As a OpenShift Container Platform cluster administrator, you can initiate the migration from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin and verify the migration status using the ROSA CLI.

Some considerations before starting migration initiation are:

* The cluster version must be 4.16.43 and above.

* The migration process cannot be interrupted.

* Migrating back to the SDN network plugin is not possible.

* Cluster nodes will be rebooted during migration.

* There will be no impact to workloads that are resilient to node disruptions.

* Migration time can vary between several minutes and hours, depending on the cluster size and workload configurations.

// Module included in the following assemblies:
//networking/ovn_kubernetes_network_provider/migrate-from-openshift-sdn.adoc

[id="migrate-sdn-ovn-cli_{context}"]
= Starting migration by using the ROSA CLI

[role="_abstract"]
You can start the migration from the OpenShift SDN network plugin to the OVN-Kubernetes network plugin by using the ROSA CLI.

[WARNING]
====
You can only start migration on clusters that are version 4.16.43 and above.
====

.Procedure

* Start the migration by running the following command. Replace `<cluster_id>` with the ID of the cluster you want to migrate to the OVN-Kubernetes network plugin:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_id>
  --network-type OVNKubernetes
  --ovn-internal-subnets <configuration>
----
+
Optional: You can create key-value pairs to configure internal subnets by using any or all of the options `join, masquerade, transit` along with a single CIDR per option. For example, `--ovn-internal-subnets="join=0.0.0.0/24,transit=0.0.0.0/24,masquerade=0.0.0.0/24"`.
+
[IMPORTANT]
====
You cannot include the optional flag `--ovn-internal-subnets` in the command unless you define a value for the flag `--network-type`.
====

.Verification

* To check the status of the migration, run the following command. Replace `<cluster_id>` with the ID of the cluster to check the migration status:
+
[source,terminal]
----
$ rosa describe cluster -c <cluster_id>
----
