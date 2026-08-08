---
title: "Configuring a dedicated network for live migration"
type: reference
domain: openshift
slug: virt-4-22-virt-dedicated-network-live-migration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-dedicated-network-live-migration
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring a dedicated network for live migration

[id="virt-dedicated-network-live-migration"]
= Configuring a dedicated network for live migration

[role="_abstract"]
You can configure a dedicated secondary network for live migration. A dedicated network minimizes the effects of network saturation on tenant workloads during live migration.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-dedicated-network-live-migration.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="virt-configuring-secondary-network-vm-live-migration_{context}"]
= Configuring a dedicated secondary network for live migration

[role="_abstract"]
After you have configured a Linux bridge network, you can configure a dedicated network for live migration. A dedicated network minimizes the effects of network saturation on tenant workloads during live migration.

To configure a dedicated secondary network for live migration, you must first create a bridge network attachment definition (NAD) by using the CLI. You can then add the name of the `NetworkAttachmentDefinition` object to the `HyperConverged` custom resource (CR).

.Prerequisites

* You installed the {oc-first}.
* You logged in to the cluster as a user with the `cluster-admin` role.
* Each node has at least two Network Interface Cards (NICs).
* The NICs for live migration are connected to the same VLAN.

.Procedure

. Create a `NetworkAttachmentDefinition` manifest according to the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: my-secondary-network
  namespace: {CNVNamespace}
spec:
  config: '{
    "cniVersion": "0.3.1",
    "name": "migration-bridge",
    "type": "macvlan",
    "master": "eth1",
    "mode": "bridge",
    "ipam": {
      "type": "whereabouts",
      "range": "10.200.5.0/24"
    }
  }'
----
** `metadata.name` defines the name of the `NetworkAttachmentDefinition` object.
** `config.master` defines the name of the NIC to be used for live migration.
** `config.type` defines the name of the CNI plugin that provides the network for the NAD.
** `config.range` defines an IP address range for the secondary network. This range must not overlap the IP addresses of the main network.

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the name of the `NetworkAttachmentDefinition` object to the `spec.liveMigrationConfig` stanza of the `HyperConverged` CR.
+
Example `HyperConverged` manifest:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  liveMigrationConfig:
    completionTimeoutPerGiB: 800
    network: <network>
    parallelMigrationsPerCluster: 5
    parallelOutboundMigrationsPerNode: 2
    progressTimeout: 150
# ...
----
** `spec.liveMigrationConfig.network` defines the name of the Multus `NetworkAttachmentDefinition` object to be used for live migrations.

. Save your changes and exit the editor. The `virt-handler` pods restart and connect to the secondary network.

.Verification

* When the node that the virtual machine runs on is placed into maintenance mode, the VM automatically migrates to another node in the cluster. You can verify that the migration occurred over the secondary network and not the default pod network by checking the target IP address in the virtual machine instance (VMI) metadata.
+
[source,terminal]
----
$ oc get vmi <vmi_name> -o jsonpath='{.status.migrationState.targetNodeAddress}'
----

// Module included in the following assemblies:
//
// * virt/live_migration/virt-migrating-vm-on-secondary-network.adoc
// * virt/post_installation_configuration/virt-post-install-network-config.adoc

[id="virt-selecting-migration-network-ui_{context}"]
= Selecting a dedicated network by using the web console

[role="_abstract"]
You can select a dedicated network for live migration by using the OpenShift Container Platform web console.

.Prerequisites

* You configured a Multus network for live migration.
* You created a network attachment definition for the network.

.Procedure

. Go to *Virtualization -> Settings* in the OpenShift Container Platform web console.
. On the *Cluster* tab, click *General settiings*.
. Click *Live Migration*.
. Select the network from the *Live migration network* list.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring live migration limits and timeouts
* Connecting a VM to a Linux bridge network
