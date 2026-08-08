---
title: "Managing bare-metal hosts"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-managing-bare-metal-hosts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/managing-bare-metal-hosts
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Managing bare-metal hosts

[id="managing-bare-metal-hosts"]
= Managing bare-metal hosts

[role="_abstract"]
You can configure bare-metal hosts directly within OpenShift Container Platform. To provision and manage nodes in a bare-metal cluster, use `Machine` and `MachineSet` custom resources (CRs).

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="about-bare-metal-hosts-and-nodes_{context}"]
= About bare metal hosts and nodes

[role="_abstract"]
To provision a {op-system-first} bare-metal host as a node in your cluster, first create a `MachineSet` custom resource (CR) object that corresponds to bare-metal host hardware.

Bare-metal host compute machine sets describe infrastructure components specific to your configuration. You apply specific Kubernetes labels to these compute machine sets and then update the infrastructure components to run on only those machines.

When you scale up the relevant `MachineSet` CR that contains a `metal3.io/autoscale-to-hosts` annotation, `Machine` CRs are created automatically. OpenShift Container Platform uses `Machine` CRs to provision the bare-metal node that corresponds to the host as specified in the `MachineSet` CR.

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="maintaining-bare-metal-hosts_{context}"]
= Maintaining bare metal hosts

[role="_abstract"]
You can maintain the details of the bare metal hosts in your cluster from the OpenShift Container Platform web console.

.Procedure

. From the web console, comlete the following steps:
+
.. Navigate to *Compute* -> *Bare Metal Hosts*.
+
.. Select a task from the *Actions* drop-down menu.
+
.. Manage items such as baseboard management controller (BMC) details, boot MAC address for the host, enable power management, and so on. You can also review the details of the network interfaces and drives for the host.

. Move a bare-metal host into maintenance mode. When you move a host into maintenance mode, the scheduler moves all managed workloads off the corresponding bare-metal node. No new workloads are scheduled while in maintenance mode.

. Deprovision a bare-metal host in the web console. Deprovisioning a host does the following actions:
+
.. Annotates the bare-metal host CR with `cluster.k8s.io/delete-machine: true`.
+
.. Scales down the related compute machine set.
+
[NOTE]
====
Powering off the host without first moving the daemon set and unmanaged static pods to another node can cause service disruption and loss of data.
====

[role="_additional-resources"]
.Additional resources

* Adding compute machines to bare metal

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="adding-bare-metal-host-to-cluster-using-web-console_{context}"]
= Adding a bare metal host to the cluster using the web console

[role="_abstract"]
You can add bare-metal hosts to the cluster by using the web console.

.Prerequisites

* Install an {op-system} cluster on bare metal.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. In the web console, navigate to *Compute* -> *Bare Metal Hosts*.

. Select *Add Host* -> *New with Dialog*.

. Specify a unique name for the new bare-metal host.

. Set the *Boot MAC address*.

. Set the *Baseboard Management Console (BMC) Address*.

. Enter the user credentials for the baseboard management controller (BMC) of the host.

. Select to power on the host after creation, and select *Create*.

. Scale up the number of replicas to match the number of available bare metal hosts. Navigate to *Compute* -> *MachineSets*, and increase the number of machine replicas in the cluster by selecting *Edit Machine count* from the *Actions* drop-down menu.
+
[NOTE]
====
You can also manage the number of bare-metal nodes by using the `oc scale` command and the appropriate bare-metal compute machine set.
====

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="adding-bare-metal-host-to-cluster-using-yaml_{context}"]
= Adding a bare-metal host to the cluster using YAML in the web console

[role="_abstract"]
You can add bare-metal hosts to the cluster in the web console by using a YAML file that describes the bare-metal host.

.Prerequisites

* Install a {op-system} compute machine on bare-metal infrastructure for use in the cluster.
* Log in as a user with `cluster-admin` privileges.
* Create a `Secret` CR for the bare-metal host.

.Procedure

. In the web console, navigate to *Compute* -> *Bare Metal Hosts*.

. Select *Add Host* -> *New from YAML*.

. Copy and paste the below YAML, modifying the relevant fields with the details of your host:
+
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: <bare_metal_host_name>
spec:
  online: true
  bmc:
    address: <bmc_address>
    credentialsName: <secret_credentials_name>
    disableCertificateVerification: True
  bootMACAddress: <host_boot_mac_address>
# ...
----
+
where:

`spec.bmc.credentialsName`:: Specifies a reference to a valid `Secret` CR. The Bare Metal Operator cannot manage the bare-metal host without a valid `Secret` referenced in the `credentialsName`. For more information about secrets and how to create them, see "Understanding secrets".

`spec.bmc.disableCertificateVerification`:: Specifies whether to require TLS host validation between the cluster and the baseboard management controller (BMC). When this field is set to `true`, TLS host validation is disabled.

. Select *Create* to save the YAML and create the new bare-metal host.

. Scale up the number of replicas to match the number of available bare-metal hosts. Navigate to *Compute* -> *MachineSets*, and increase the number of machines in the cluster by selecting *Edit Machine count* from the *Actions* drop-down menu.
+
[NOTE]
====
You can also manage the number of bare-metal nodes by using the `oc scale` command and the appropriate bare-metal compute machine set.
====

[role="_additional-resources"]
.Additional resources

* Understanding secrets

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="automatically-scaling-machines-to-available-bare-metal-hosts_{context}"]
= Automatically scaling machines to the number of available bare-metal hosts

[role="_abstract"]
To automatically create the number of `Machine` objects that matches the number of available `BareMetalHost` objects, add a `metal3.io/autoscale-to-hosts` annotation to the `MachineSet` object.

.Prerequisites

* Install {op-system} bare-metal compute machines for use in the cluster, and create corresponding `BareMetalHost` objects.
* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. To configure automatic scaling for a compute machine set, annotate the compute machine set by running the following command:
+
[source,terminal]
----
$ oc annotate machineset <machineset> -n openshift-machine-api 'metal3.io/autoscale-to-hosts=<any_value>'
----
** `<machineset>`: Specifies the name of the compute machine set that you want to configure for automatic scaling.
** `<any_value>` Specifies is a value, such as `true` or `""`.

. Wait for the new scaled machines to start.
+
[NOTE]
====
The `BareMetalHost` object continues to be counted against the `MachineSet` that the `Machine` object was created from when the following conditions are met:

* You use a `BareMetalHost` object to create a machine in the cluster.
* You subsequently change labels or selectors on the `BareMetalHost`.
====

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="removing-bare-metal-hosts-from-provisioner_{context}"]
= Removing bare-metal hosts from the provisioner node

[role="_abstract"]
In certain circumstances, you might want to temporarily remove bare-metal hosts from the provisioner node. For example, to prevent the management of the number of `Machine` objects that matches the number of available `BareMetalHost` objects, add a `baremetalhost.metal3.io/detached` annotation to the `MachineSet` object.

Consider an example during provisioning when a bare-metal host reboot is triggered by using the OpenShift Container Platform administration console or as a result of a Machine Config Pool update. In this case, OpenShift Container Platform logs into the integrated Dell Remote Access Controller (iDRAC) and issues a delete of the job queue.

[NOTE]
====
This annotation has an effect for only `BareMetalHost` objects that are in either `Provisioned`, `ExternallyProvisioned`, or `Ready/Available` states.
====

.Prerequisites

* Install {op-system} bare-metal compute machines for use in the cluster and create corresponding `BareMetalHost` objects.
* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. To configure automatic scaling for a compute machine set, annotate the compute machine set by running the following command:
+
[source,terminal]
----
$ oc annotate machineset <machineset> -n openshift-machine-api 'baremetalhost.metal3.io/detached'
----
+
Wait for the new machines to start.
+
[NOTE]
====
When you use a `BareMetalHost` object to create a machine in the cluster and labels or selectors are subsequently changed on the `BareMetalHost`, the `BareMetalHost` object continues to be counted against the `MachineSet` that the `Machine` object was created from.
====

. In the provisioning use case, remove the annotation after the reboot is complete by using the following command:
+
[source,terminal]
----
$ oc annotate machineset <machineset> -n openshift-machine-api 'baremetalhost.metal3.io/detached-'
----

[role="_additional-resources"]
.Additional resources

* Expanding the cluster
* MachineHealthChecks on bare metal

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="powering-off-bare-metal-hosts-web-console_{context}"]
= Powering off bare-metal hosts by using the web console

[role="_abstract"]
You can power off bare-metal cluster hosts in the web console. Before you power off a host, mark the node as unschedulable and drain all pods and workloads from the node.

.Prerequisites

* You have installed a {op-system} compute machine on bare-metal infrastructure for use in the cluster.
* You have logged in as a user with `cluster-admin` privileges.
* You have configured the host to be managed and have added Baseboard Management Console credentials for the cluster host. You can add BMC credentials by applying a `Secret` custom resource (CR) in the cluster or by logging in to the web console and configuring the bare-metal host to be managed.

.Procedure

. Navigate to *Nodes* and select the node that you want to power off. Expand the *Actions* menu and select *Mark as unschedulable*.

. Manually delete or relocate running pods on the node by adjusting the pod deployments or scaling down workloads on the node to zero. Wait for the drain process to complete.

. Navigate to *Compute* -> *Bare Metal Hosts*.

. Expand the *Options menu* for the bare-metal host that you want to power off, and select *Power Off*.

. Select *Immediate power off*.

// Module included in the following assemblies:
//
// scalability_and_performance/managing-bare-metal-hosts.adoc

[id="powering-off-bare-metal-hosts-cli_{context}"]
= Powering off bare-metal hosts by using the CLI

[role="_abstract"]
You can power off bare-metal cluster hosts by applying a patch in the cluster by using the {oc-first}. Before you power off a host, mark the node as unschedulable and drain all pods and workloads from the node.

.Prerequisites

* You have installed a {op-system} compute machine on bare-metal infrastructure for use in the cluster.
* You have logged in as a user with `cluster-admin` privileges.
* You have configured the host to be managed and have added Baseboard Management Console credentials for the cluster host. You can add BMC credentials by applying a `Secret` custom resource (CR) in the cluster or by logging in to the web console and configuring the bare-metal host to be managed.

.Procedure

. Get the name of the managed bare-metal host by entering the following command:
+
[source,terminal]
----
$ oc get baremetalhosts -n openshift-machine-api -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.provisioning.state}{"\n"}{end}'
----
+
.Example output
[source,terminal]
----
master-0.example.com  managed
master-1.example.com  managed
master-2.example.com  managed
worker-0.example.com  managed
worker-1.example.com  managed
worker-2.example.com  managed
----

. Mark the node as unschedulable by entering the following command:
+
[source,terminal]
----
$ oc adm cordon <bare_metal_host>
----
** `<bare_metal_host>`: Specifies the name of the host that you want to shut down. For example, `worker-2.example.com`.

. Drain all pods on the node by entering the following command:
+
[source,terminal]
----
$ oc adm drain <bare_metal_host> --force=true
----
+
Pods that are backed by replication controllers are rescheduled to other available nodes in the cluster.

. Safely power off the bare-metal host by entering the following command:
+
[source,terminal]
----
$ oc patch <bare_metal_host> --type json -p '[{"op": "replace", "path": "/spec/online", "value": false}]'
----

. After you power on the host, make the node schedulable for workloads by entering the following command:
+
[source,terminal]
----
$ oc adm uncordon <bare_metal_host>
----
