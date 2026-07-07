---
title: "Troubleshooting Windows container workload issues"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-windows-container-workload-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-windows-container-workload-issues
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting Windows container workload issues

[id="troubleshooting-windows-container-workload-issues"]
= Troubleshooting Windows container workload issues

[role="_abstract"]
Use the following sections to troubleshoot Windows container workload issues.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="wmco-does-not-install_{context}"]
= Windows Machine Config Operator does not install

[role="_abstract"]
If you have completed the process of installing the Windows Machine Config Operator (WMCO), but the Operator is stuck in the `InstallWaiting` phase, your issue is likely caused by a networking issue.

The WMCO requires your OpenShift Container Platform cluster to be configured with hybrid networking using OVN-Kubernetes; the WMCO cannot complete the installation process without hybrid networking available. This is necessary to manage nodes on multiple operating systems (OS) and OS variants. This must be completed during the installation of your cluster.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="investigating-why-windows-machine-compute-node_{context}"]
= Investigating why Windows Machine does not become compute node

[role="_abstract"]
There are various reasons why a Windows Machine does not become a compute node. The best way to investigate this problem is to collect the Windows Machine Config Operator (WMCO) logs.

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

.Procedure

* Run the following command to collect the WMCO logs:
+
[source,terminal]
----
$ oc logs -f deployment/windows-machine-config-operator -n openshift-windows-machine-config-operator
----

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="accessing-windows-node_{context}"]
= Accessing a Windows node

[role="_abstract"]
Windows nodes cannot be accessed using the `oc debug node` command; the command requires running a privileged pod on the node, which is not yet supported for Windows. Instead, a Windows node can be accessed using a secure shell (SSH) or Remote Desktop Protocol (RDP). An SSH bastion is required for both methods.
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="accessing-windows-node-using-ssh_{context}"]
= Accessing a Windows node using SSH

[role="_abstract"]
You can access a Windows node by using a secure shell (SSH).

.Prerequisites

* You have installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.
* You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use.
* You have connected to the Windows node using an `ssh-bastion` pod.

.Procedure

* Access the Windows node by running the following command:
+
[source,terminal]
----
$ ssh -t -o StrictHostKeyChecking=no -o ProxyCommand='ssh -A -o StrictHostKeyChecking=no \
    -o ServerAliveInterval=30 -W %h:%p core@$(oc get service --all-namespaces -l run=ssh-bastion \
    -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")' <username>@<windows_node_internal_ip>
----
+
where::
* Specify the cloud provider username, such as `Administrator` for Amazon Web Services (AWS) or `capi` for Microsoft Azure.
* Specify the internal IP address of the node, which can be discovered by running the following command:
+
[source,terminal]
----
$ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
----
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="accessing-windows-node-using-rdp_{context}"]
= Accessing a Windows node using RDP

[role="_abstract"]
You can access a Windows node by using a Remote Desktop Protocol (RDP).

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.
* You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use.
* You have connected to the Windows node using an `ssh-bastion` pod.

.Procedure

. Run the following command to set up an SSH tunnel:
+
[source,terminal]
----
$ ssh -L 2020:<windows_node_internal_ip>:3389 \
    core@$(oc get service --all-namespaces -l run=ssh-bastion -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")
----
+
where::
* Specify the internal IP address of the node, which can be discovered by running the following command:
+
[source,terminal]
----
$ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
----

. From within the resulting shell, SSH into the Windows node and run the following command to create a password for the user:
+
[source,terminal]
----
C:\> net user <username> *
----
+
Specify the cloud provider user name, such as `Administrator` for AWS or `capi` for Azure. You can now remotely access the Windows node at `localhost:2020` using an RDP client.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="collecting-kube-node-logs-windows_{context}"]
= Collecting Kubernetes node logs for Windows containers

[role="_abstract"]
Windows container logging works differently from Linux container logging; the Kubernetes node logs for Windows workloads are streamed to the `C:\var\logs` directory by default. Therefore, you must gather the Windows node logs from that directory.

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

.Procedure

. To view the logs under all directories in `C:\var\logs`, run the following command:
+
[source,terminal]
----
$ oc adm node-logs -l kubernetes.io/os=windows --path= \
    /ip-10-0-138-252.us-east-2.compute.internal containers \
    /ip-10-0-138-252.us-east-2.compute.internal hybrid-overlay \
    /ip-10-0-138-252.us-east-2.compute.internal kube-proxy \
    /ip-10-0-138-252.us-east-2.compute.internal kubelet \
    /ip-10-0-138-252.us-east-2.compute.internal pods
----

. You can now list files in the directories using the same command and view the individual log files. For example, to view the kubelet logs, run the following command:
+
[source,terminal]
----
$ oc adm node-logs -l kubernetes.io/os=windows --path=/kubelet/kubelet.log
----
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="collecting-windows-application-event-logs_{context}"]
= Collecting Windows application event logs

[role="_abstract"]
The `Get-WinEvent` shim on the kubelet `logs` endpoint can be used to collect application event logs from Windows machines.

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

.Procedure

* To view logs from all applications logging to the event logs on the Windows machine, run:
+
[source,terminal]
----
$ oc adm node-logs -l kubernetes.io/os=windows --path=journal
----
+
The same command is executed when collecting logs with `oc adm must-gather`.
+
Other Windows application logs from the event log can also be collected by specifying the respective service with a `-u` flag. For example, you can run the following command to collect logs for the containerd container runtime service:
+
[source,terminal]
----
$ oc adm node-logs -l kubernetes.io/os=windows --path=journal -u containerd
----
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-windows-container-workload-issues.adoc

[id="collecting-docker-logs-windows_{context}"]
= Collecting containerd logs for Windows containers

[role="_abstract"]
The Windows containerd container service does not stream log data to stdout, but instead, it stream log data to the Windows event log. You can view the containerd event logs to investigate issues you think might be caused by the Windows containerd container service.

.Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

.Procedure

* View the containerd logs by running the following command:
+
[source,terminal]
----
$ oc adm node-logs -l kubernetes.io/os=windows --path=containerd
----

[role="_additional-resources"]
== Additional resources

* Configuring hybrid networking
* Containers on Windows troubleshooting
* Troubleshoot host and container image mismatches
* Common Kubernetes problems with Windows
