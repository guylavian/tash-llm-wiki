---
title: "Allocate physical cores for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-physical-cores-allocation-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-physical-cores-allocation-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Allocate physical cores for virtual machines

[id="virt-physical-cores-allocation-vms"]
= Allocate physical cores for virtual machines

[role="_abstract"]
As a cluster administrator, you can allocate a full physical core to a specific virtual machine (VM), instead of allowing different VMs to share the same physical core.
Configuring your VMs to use only full physical cores can optimize performance for high-throughput or latency-critical VMs.

Allocating only full physical cores is important on simultaneous multi-threading (SMT) enabled systems because it offers the following benefits:

* Prevents noisy neighbors and resource contention
* Mitigates performance degradation
* Offers predictable latency
* Guarantees exclusive CPU resources

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-physical-cores-allocation-vms.adoc

[id="virt-CPU-manager-policy_{context}"]
= Configure full physical core allocation for virtual machines

[role="_abstract"]
You can configure full physical core allocation by modifying the `cpuManagerPolicy` and `cpuManagerPolicyOptions` settings in the `KubeletConfig` custom resource (CR).

.Prerequisites

* You have cluster administrator access to a OpenShift Container Platform cluster with {VirtProductName} installed.
* You have installed the {oc-first}.
* You have enabled CPU Manager on the node where your VM runs.

.Procedure

. Edit the `KubeletConfig` CR to add the required `cpuManagerPolicy` and `cpuManagerPolicyOptions` configurations:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
# ...
cpuManagerPolicy: static
cpuManagerPolicyOptions:
  full-pcpus-only: true
kubeReserved:
  cpu: "1"
# ...
----
+
* You must set the `cpuManagerPolicy: static` policy to enable exclusive CPU allocation. This setting is a prerequisite for configuring the `cpuManagerPolicyOptions` settings.
* You must set the `full-pcpus-only: true` policy option so that the static CPU Manager policy only allocates full physical cores.
* You must reserve 1 CPU for the system by setting `cpu: "1"` in the `kubeReserved` settings. This ensures that the cluster remains stable, by requiring that the system's core functions always have access to the CPU that they need to work correctly.

. Run the following command to apply the changes to the `KubeletConfig` CR:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

* Inspect the kubelet configuration on a node where the change you applied the change, by running the following command and inspecting the output:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host cat /etc/kubernetes/kubelet.conf | grep -E -A 2 'cpuManagerPolicy|kubeReserved'
----
+
Example output:
+
[source,YAML]
----
cpuManagerPolicy: static
cpuManagerPolicyOptions:
  full-pcpus-only: true
--
kubeReserved:
  cpu: "1"
----
