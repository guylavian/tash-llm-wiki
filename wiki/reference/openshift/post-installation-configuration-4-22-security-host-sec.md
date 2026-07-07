---
title: "Host security"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-security-host-sec
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/security-host-sec
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Host security

[id="security-host-sec"]
= Host security

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/security/security-host-sec.adoc

[id="security-rhcos-overview_{context}"]
= {op-system-first}

[role="_abstract"]
{op-system-first} is different from {op-system-base-full} in key areas. For more information, see "About {op-system}".

A major distinction is the control of `rpm-ostree`, which is updated through the Machine Config Operator.

{op-system} follows the same immutable design used for pods in OpenShift Container Platform. This ensures that the operating system remains consistent across the cluster. For information about {op-system} architecture, see "{op-system-first}".

To manage hosts effectively while maintaining security, avoid direct access whenever possible. Instead, you can use the following methods for host management:

* Debug pod
* Direct SSH
* Console access

Review the following {op-system} security mechanisms that are integral to maintaining host security:

Linux namespaces:: Provide isolation for processes and resources. Each container keeps its processes and files within its own namespace. If a user escapes from the container namespace, they could gain access to the host operating system, potentially compromising security.

Security-Enhanced Linux (SELinux):: Enforces mandatory access controls to restrict access to files and directories by processes. SELinux adds an extra layer of security by preventing unauthorized access to files if a process tries to break its confinement.
+
SELinux follows the security policy of denying everything unless explicitly allowed. If a process attempts to modify or access a file without permission, SELinux denies access. For more information, see Introduction to SELinux.

Linux capabilities:: Assign specific privileges to processes at a granular level, minimizing the need for full root permissions. For more information, see "Linux capabilities".

Control groups (cgroups):: Allocate and manage system resources, such as CPU and memory for processes and containers, ensuring efficient usage. As of OpenShift Container Platform 4.16, there are two versions of cgroups. cgroup v2 is now configured by default.

CRI-O:: Serves as a lightweight container runtime that enforces security boundaries and manages container workloads.

[role="_additional-resources"]
.Additional resources

* About RHCOS

* Red Hat Enterprise Linux CoreOS (RHCOS)

* Linux capabilities

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/security/security-host-sec.adoc

[id="security-command-line-host-access_{context}"]
= Command-line host access

[role="_abstract"]
Configure an external authenticator to restrict direct access and prevent unauthorized modifications. The Machine Config Operator (MCO) manages these logins and maintains consistency across your cluster.

Examples of external authenticators include lightweight directory access protocol (LDAP) and System Security Services Daemon (SSSD). If a node reboot leads to timeout issues, create a node disruption policy. With this policy, you can configure an external authenticator on a host without requiring a node reboot. For more information, see "Using node disruption policies to minimize disruption from machine config changes" in the _Additional resources_ section.

[IMPORTANT]
====
Do not configure direct access to the root ID on any OpenShift Container Platform cluster server.
====

You can connect to a node in the cluster by using the following methods:

Using debug pod:: Red{nbsp}Hat recommends this method to access a node. To debug or connect to a node, run the following command:
+
[source,terminal]
----
$ oc debug node/<worker_node_name>
----
+
After connecting to the node, run the following command to get access to the root file system:
+
[source,terminal]
----
# chroot /host
----
+
This gives you root access within a debug pod on the node. For more information, see "Starting debug pods with root access".

Direct SSH:: Avoid using the root user. Instead, use the core user ID (or your own ID). To connect to the node by using SSH, run the following command:
+
[source,terminal]
----
$ ssh core@<worker_node_name>
----
+
[IMPORTANT]
====
The core user ID is initially given `sudo` privileges within the cluster.
====
+
If you cannot connect to a node by using SSH, add your SSH key to the core user. For more information, see "How to connect to OpenShift Container Platform 4.x Cluster nodes using SSH bastion pod" in the _Additional resources_ section.
+
After connecting to the node using SSH, run the following command to get access to the root shell:
+
[source,terminal]
----
$ sudo -i
----

Console Access:: Ensure that consoles are secure. Do not allow direct login with the root ID, instead use individual IDs.
+
[NOTE]
====
Follow the best practices of your organization for securing console access.
====

[role="_additional-resources"]
.Additional resources

* Using node disruption policies to minimize disruption from machine config changes

* Starting debug pods with root access

* How to connect to OpenShift Container Platform 4.x Cluster nodes using SSH bastion pod

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/security/security-host-sec.adoc

[id="security-linux-capabilities-overview_{context}"]
= Linux capabilities

[role="_abstract"]
Linux capabilities define the actions a process can perform on the host system. By default, pods are granted several capabilities unless security measures are applied. These default capabilities are as follows:

* `CHOWN`
* `DAC_OVERRIDE`
* `FSETID`
* `FOWNER`
* `SETGID`
* `SETUID`
* `SETPCAP`
* `NET_BIND_SERVICE`
* `KILL`

You can modify which capabilities that a pod can receive by configuring Security Context Constraints (SCCs).

[IMPORTANT]
====
You must not assign the following capabilities to a pod:

* `SYS_ADMIN`: A powerful capability that grants elevated privileges. Allowing this capability can break security boundaries and pose a significant security risk.
* `NET_ADMIN`: Allows control over networking, like SR-IOV ports, but can be replaced with alternative solutions in modern setups.

For more information about Linux capabilities, see the Linux capabilities man page.
====
