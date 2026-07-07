---
title: "Machine phases and lifecycle"
type: reference
domain: openshift
slug: machine-management-4-22-machine-phases-lifecycle
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/machine-phases-lifecycle
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Machine phases and lifecycle

[id="machine-phases-lifecycle"]
= Machine phases and lifecycle

[role="_abstract"]
Machines move through a _lifecycle_ that has several defined phases. Understanding the machine lifecycle and its phases can help you verify whether a procedure is complete or troubleshoot undesired behavior. In OpenShift Container Platform, the machine lifecycle is consistent across all supported cloud providers.

//Machine phases
// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

[id="machine-about-phases_{context}"]
= Machine phases

[role="_abstract"]
Understanding machine lifecycle phases can help you troubleshoot machine issues. As a machine moves through its lifecycle, it passes through different phases. Each phase is a basic representation of the state of the machine.

`Provisioning`:: There is a request to provision a new machine. The machine does not yet exist and does not have an instance, a provider ID, or an address.

`Provisioned`:: The machine exists and has a provider ID or an address. The cloud provider has created an instance for the machine. The machine has not yet become a node and the `status.nodeRef` section of the machine object is not yet populated.

`Running`:: The machine exists and has a provider ID or address. Ignition has run successfully and the cluster machine approver has approved a certificate signing request (CSR). The machine has become a node and the `status.nodeRef` section of the machine object contains node details.

`Deleting`:: There is a request to delete the machine. The machine object has a `DeletionTimestamp` field that indicates the time of the deletion request.

`Failed`:: There is an unrecoverable problem with the machine. This can happen, for example, if the cloud provider deletes the instance for the machine.

//The machine lifecycle
// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

[id="machine-about-lifecycle_{context}"]
= The machine lifecycle

[role="_abstract"]
Understanding the machine lifecycle can help you troubleshoot machine issues. The lifecycle begins with the request to provision a machine and continues until the machine no longer exists.

//.Machine lifecycle
//image::to-do-machine-lifecycle.png["The sequence of events in the machine lifecycle."]

The machine lifecycle proceeds in the following order. Interruptions due to errors or lifecycle hooks are not included in this overview.

. There is a request to provision a new machine for one of the following reasons:
** A cluster administrator scales a machine set such that it requires additional machines.
** An autoscaling policy scales machine set such that it requires additional machines.
** A machine that is managed by a machine set fails or is deleted and the machine set creates a replacement to maintain the required number of machines.

. The machine enters the `Provisioning` phase.

. The infrastructure provider creates an instance for the machine.

. The machine has a provider ID or address and enters the `Provisioned` phase.

. The Ignition configuration file is processed.

. The kubelet issues a certificate signing request (CSR).

. The cluster machine approver approves the CSR.

. The machine becomes a node and enters the `Running` phase.

. An existing machine is slated for deletion for one of the following reasons:
** A user with `cluster-admin` permissions uses the `oc delete machine` command.
** The machine gets a `machine.openshift.io/delete-machine` annotation.
** The machine set that manages the machine marks it for deletion to reduce the replica count as part of reconciliation.
** The cluster autoscaler identifies a node that is unnecessary to meet the deployment needs of the cluster.
** A machine health check is configured to replace an unhealthy machine.

. The machine enters the `Deleting` phase, in which it is marked for deletion but is still present in the API.

. The machine controller removes the instance from the infrastructure provider.

. The machine controller deletes the `Node` object.

//Determining the phase of a machine by using the CLI
// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

[id="machine-determine-phase-cli_{context}"]
= Determining the phase of a machine by using the CLI

[role="_abstract"]
To troubleshoot issues with a machine, you can find the phase of a machine by using the {oc-first}.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed the `oc` CLI.

.Procedure

* List the machines on the cluster by running the following command:
+
[source,terminal]
----
$ oc get machine -n openshift-machine-api
----
+
.Example output
+
[source,text]
----
NAME                                      PHASE     TYPE         REGION      ZONE         AGE
mycluster-5kbsp-master-0                  Running   m6i.xlarge   us-west-1   us-west-1a   4h55m
mycluster-5kbsp-master-1                  Running   m6i.xlarge   us-west-1   us-west-1b   4h55m
mycluster-5kbsp-master-2                  Running   m6i.xlarge   us-west-1   us-west-1a   4h55m
mycluster-5kbsp-worker-us-west-1a-fmx8t   Running   m6i.xlarge   us-west-1   us-west-1a   4h51m
mycluster-5kbsp-worker-us-west-1a-m889l   Running   m6i.xlarge   us-west-1   us-west-1a   4h51m
mycluster-5kbsp-worker-us-west-1b-c8qzm   Running   m6i.xlarge   us-west-1   us-west-1b   4h51m
----
+
The `PHASE` column of the output contains the phase of each machine.

//Determining the phase of a machine by using the web console
// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

[id="machine-determine-phase-gui_{context}"]
= Determining the phase of a machine by using the web console

[role="_abstract"]
To troubleshoot issues with a machine, you can find the phase of a machine by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

.Procedure

. Log in to the web console as a user with the `cluster-admin` role.

. Navigate to *Compute* -> *Machines*.

. On the *Machines* page, select the name of the machine that you want to find the phase of.

. On the *Machine details* page, select the *YAML* tab.

. In the YAML block, find the value of the `status.phase` field.
+
.Example YAML snippet
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  name: mycluster-5kbsp-worker-us-west-1a-fmx8t
# ...
status:
  phase: Running
----
+
In this example, the phase is `Running`.

[role="_additional-resources"]
== Additional resources

* Lifecycle hooks for the machine deletion phase
