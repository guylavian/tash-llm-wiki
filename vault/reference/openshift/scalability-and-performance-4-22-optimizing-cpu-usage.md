---
title: "Optimizing CPU usage with mount namespace encapsulation"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-optimizing-cpu-usage
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/optimizing-cpu-usage
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Optimizing CPU usage with mount namespace encapsulation

[id="optimizing-cpu-usage"]
= Optimizing CPU usage with mount namespace encapsulation

[role="_abstract"]
You can optimize CPU usage in OpenShift Container Platform clusters by using mount namespace encapsulation to provide a private namespace for kubelet and CRI-O processes. This reduces the cluster CPU resources used by systemd with no difference in functionality.

// Module included in the following assemblies:
//
// * scalability_and_performance/optimization/optimizing-cpu-usage.adoc

[id="optimizing-cpu-usage_{context}"]
= Encapsulating mount namespaces

[role="_abstract"]
You can encapsulate mount namespaces to isolate mount points so that processes in different namespaces cannot view each others' files. Encapsulation is the process of moving Kubernetes mount namespaces to an alternative location where they do not get constantly scanned by the host operating system.

The host operating system uses systemd to constantly scan all mount namespaces: both the standard Linux mounts and the numerous mounts that Kubernetes uses to operate. The current implementation of kubelet and CRI-O both use the top-level namespace for all container runtime and kubelet mount points. However, encapsulating these container-specific mount points in a private namespace reduces systemd overhead with no difference in functionality. Using a separate mount namespace for both CRI-O and kubelet can encapsulate container-specific mounts from any systemd or other host operating system interaction.

This ability to potentially achieve major CPU optimization is now available to all OpenShift Container Platform administrators. Encapsulation can also improve security by storing Kubernetes-specific mount points in a location safe from inspection by unprivileged users.

The following diagrams illustrate a Kubernetes installation before and after encapsulation. Both scenarios show example containers which have mount propagation settings of bidirectional, host-to-container, and none.

image::before-k8s-mount-propagation.png[Before encapsulation]

The diagram shows systemd, host operating system processes, kubelet, and the container runtime sharing a single mount namespace.

* systemd, host operating system processes, kubelet, and the container runtime each have access to and visibility of all mount points.

* Container 1, configured with bidirectional mount propagation, can access systemd and host mounts, kubelet and CRI-O mounts. A mount originating in Container 1, such as `/run/a` is visible to systemd, host operating system processes, kubelet, container runtime, and other containers with host-to-container or bidirectional mount propagation configured (as in Container 2).

* Container 2, configured with host-to-container mount propagation, can access systemd and host mounts, kubelet and CRI-O mounts. A mount originating in Container 2, such as `/run/b`, is not visible to any other context.

* Container 3, configured with no mount propagation, has no visibility of external mount points. A mount originating in Container 3, such as `/run/c`, is not visible to any other context.

The following diagram illustrates the system state after encapsulation.

image::after-k8s-mount-propagation.png[After encapsulation]

* The main systemd process is no longer devoted to unnecessary scanning of Kubernetes-specific mount points. It only monitors systemd-specific and host mount points.

* The host operating system processes can access only the systemd and host mount points.

* Using a separate mount namespace for both CRI-O and kubelet completely separates all container-specific mounts away from any systemd or other host operating system interaction whatsoever.

* The behavior of Container 1 is unchanged, except a mount it creates such as `/run/a` is no longer visible to systemd or host operating system processes. It is still visible to kubelet, CRI-O, and other containers with host-to-container or bidirectional mount propagation configured (like Container 2).

* The behavior of Container 2 and Container 3 is unchanged.

// Module included in the following assemblies:
//
// * scalability_and_performance/optimization/optimizing-cpu-usage.adoc

[id="enabling-encapsulation_{context}"]
= Configuring mount namespace encapsulation

[role="_abstract"]
You can configure mount namespace encapsulation so that a cluster runs with less resource overhead.

[NOTE]
====
Mount namespace encapsulation is a Technology Preview feature and the feature is disabled by default. To use the feature, you must enable the feature manually.
====

.Prerequisites

* You have installed the {oc-first}.
* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Create a file called `mount_namespace_config.yaml` with the following YAML:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-kubens-master
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
      - enabled: true
        name: kubens.service
---
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-kubens-worker
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
      - enabled: true
        name: kubens.service
----

. Apply the mount namespace `MachineConfig` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f mount_namespace_config.yaml
----
+
.Example output
[source,terminal]
----
machineconfig.machineconfiguration.openshift.io/99-kubens-master created
machineconfig.machineconfiguration.openshift.io/99-kubens-worker created
----

. The `MachineConfig` CR can take up to thirty minutes to finish being applied in the cluster. You can check the status of the `MachineConfig` CR by running the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-03d4bc4befb0f4ed3566a2c8f7636751   False     True       False      3              0                   0                     0                      45m
worker   rendered-worker-10577f6ab0117ed1825f8af2ac687ddf   False     True       False      3              1                   1
----

. Wait for the `MachineConfig` CR to be applied successfully across all control plane and worker nodes after running the following command:
+
[source,terminal]
----
$ oc wait --for=condition=Updated mcp --all --timeout=30m
----
+
.Example output
[source,terminal]
----
machineconfigpool.machineconfiguration.openshift.io/master condition met
machineconfigpool.machineconfiguration.openshift.io/worker condition met
----

.Verification

. Open a debug shell to the cluster host:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Open a `chroot` session:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. Check the systemd mount namespace:
+
[source,terminal]
----
sh-4.4# readlink /proc/1/ns/mnt
----
+
.Example output
[source,terminal]
----
mnt:[4026531953]
----

. Check kubelet mount namespace:
+
[source,terminal]
----
sh-4.4# readlink /proc/$(pgrep kubelet)/ns/mnt
----
+
.Example output
[source,terminal]
----
mnt:[4026531840]
----

. Check the CRI-O mount namespace:
+
[source,terminal]
----
sh-4.4# readlink /proc/$(pgrep crio)/ns/mnt
----
+
.Example output
[source,terminal]
----
mnt:[4026531840]
----
+
These commands return the mount namespaces associated with systemd, kubelet, and the container runtime. In OpenShift Container Platform, the container runtime is CRI-O.
+
Encapsulation is in effect if systemd is in a different mount namespace from kubelet and CRI-O as in the previous output example. Encapsulation is not in effect if all three processes are in the same mount namespace.

// Module included in the following assemblies:
//
// * scalability_and_performance/optimization/optimizing-cpu-usage.adoc

[id="supporting-encapsulation_{context}"]
= Inspecting encapsulated namespaces

[role="_abstract"]
You can inspect Kubernetes-specific mount points in the cluster host operating system for debugging or auditing purposes by using the `kubensenter` script that is available in {op-system-first}.

SSH shell sessions to the cluster host are in the default namespace. To inspect Kubernetes-specific mount points in an SSH shell prompt, you need to run the `kubensenter` script as root. The `kubensenter` script is aware of the state of the mount encapsulation, and the script is safe to run even if encapsulation is not enabled.

[NOTE]
====
`oc debug` remote shell sessions start inside the Kubernetes namespace by default. You do not need to run `kubensenter` to inspect mount points when you use `oc debug`.
====

If the encapsulation feature is not enabled, the `kubensenter findmnt` and `findmnt` commands return the same output, regardless of whether they are run in an `oc debug` session or in an SSH shell prompt.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in as a user with `cluster-admin` privileges.
* You have configured SSH access to the cluster host.

.Procedure

. Open a remote SSH shell to the cluster host. For example:
+
[source,terminal]
----
$ ssh core@<node_name>
----

. Run commands using the provided `kubensenter` script as the root user. To run a single command inside the Kubernetes namespace, provide the command and any arguments to the `kubensenter` script. For example, to run the `findmnt` command inside the Kubernetes namespace, run the following command:
+
[source,terminal]
----
[core@control-plane-1 ~]$ sudo kubensenter findmnt
----
+
.Example output
[source,terminal]
----
kubensenter: Autodetect: kubens.service namespace found at /run/kubens/mnt
TARGET                                SOURCE                 FSTYPE     OPTIONS
/                                     /dev/sda4[/ostree/deploy/rhcos/deploy/32074f0e8e5ec453e56f5a8a7bc9347eaa4172349ceab9c22b709d9d71a3f4b0.0]
|                                                            xfs        rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota
                                      shm                    tmpfs
...
----

. To start a new interactive shell inside the Kubernetes namespace, run the `kubensenter` script without any arguments:
+
[source,terminal]
----
[core@control-plane-1 ~]$ sudo kubensenter
----
+
.Example output
[source,terminal]
----
kubensenter: Autodetect: kubens.service namespace found at /run/kubens/mnt
----

// Module included in the following assemblies:
//
// * scalability_and_performance/optimization/optimizing-cpu-usage.adoc
[id="running-services-with-encapsulation_{context}"]
= Running additional services in the encapsulated namespace

[role="_abstract"]
You can adapt any existing tools by using the `kubensenter` script that is provided with OpenShift Container Platform to execute an additional command inside the Kubernetes mount point.

Any monitoring tool that relies on the ability to run in the host operating system and have visibility of mount points created by kubelet, CRI-O, or containers themselves, must enter the container mount namespace to see these mount points.

The `kubensenter` script is aware of the state of the mount encapsulation feature status, and is safe to run even if encapsulation is not enabled. In that case the script executes the provided command in the default mount namespace.

For example, if a systemd service needs to run inside the new Kubernetes mount namespace, edit the service file and use the `ExecStart=` command line with `kubensenter`.

[source,terminal]
----
[Unit]
Description=Example service
[Service]
ExecStart=/usr/bin/kubensenter /path/to/original/command arg1 arg2
----

[role="_additional-resources"]
[id="optimizing-cpu-usage-additional-resources"]
== Additional resources

* What are namespaces

* Manage containers in namespaces by using nsenter

* MachineConfig
