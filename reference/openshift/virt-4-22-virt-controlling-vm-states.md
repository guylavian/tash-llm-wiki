---
title: "Control virtual machine states"
type: reference
domain: openshift
slug: virt-4-22-virt-controlling-vm-states
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-controlling-vm-states
version: 4.22
family: virt
documentKind: "Documentation"
---

# Control virtual machine states

[id="virt-controlling-vm-states"]
= Control virtual machine states

[role="_abstract"]
You can use `virtctl` to manage virtual machine states and perform other actions from the CLI. For example, you can use `virtctl` to force stop a VM or expose a port.

You can stop, start, restart, reset, pause, and unpause virtual machines from the web console.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-controlling-vm-states.adoc

[id="virt-configure-rbac-console-subresources-api_{context}"]
= Configuring RBAC permissions for managing VM states by using the web console

[role="_abstract"]
To allow users to manage virtual machine (VM) states by using the OpenShift Container Platform web console, you must create an RBAC cluster role and cluster role binding.
The cluster role uses the `subresources.kubevirt.io` API to define which resources can be controlled by certain users or groups.

.Prerequisites

* You have cluster administrator access to an OpenShift Container Platform cluster where {VirtProductName} is installed.
* You have installed the {oc-first}.

.Procedure

. Create a `ClusterRole` object that allows the target user or group to manage VM states:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: vm-manager-access
rules:
  - apiGroups:
      - subresources.kubevirt.io
    resources:
      - virtualmachines/start
      - virtualmachines/stop
    verbs:
      - update
# ...
----

. Run the following command to apply the cluster role:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Confirm that the cluster role was created by running the following command and observing the output:
+
[source,terminal]
----
$ oc get clusterrole <name>
----
+
Example output:
+
[source,terminal]
----
NAME                AGE
vm-manager-access   15s
----

. Inspect the details of the cluster role, and ensure the intended rules for `subresources.kubevirt.io` are present, specifically the `virtualmachines/start` and `virtualmachines/stop` subresources.
+
Run the following command and observe the output:
+
[source,terminal]
----
$ oc describe clusterrole <name>
----
+
Example output:
+
[source,terminal]
----
Name:         vm-manager-access
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  virtualmachines/start, virtualmachines/stop with subresources.kubevirt.io group  []  []  [update]
----

. Create a `ClusterRoleBinding` object to bind the cluster role you have created to the target user or group:
+
[source,yaml,subs="attributes+"]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vm-manager-access-binding
subjects:
  - kind: User
    name: test-user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: vm-manager-access
  apiGroup: rbac.authorization.k8s.io
----

. Run the following command to apply the cluster role binding:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Confirm that the cluster role binding was created by running the following command and observing the output:
+
[source,terminal]
----
$ oc get clusterrolebinding <name>
----
+
Example output:
+
[source,terminal]
----
NAME                        AGE
vm-manager-access-binding   15s
----

.Verification

. Check if the user can start a VM by running the following command:
+
[source,terminal]
----
$ oc auth can-i update virtualmachines/start --namespace=<namespace> --as=<user_name> --subresource=subresources.kubevirt.io
----
+
Example output:
+
[source,terminal]
----
yes
----

. Check if the user can stop a VM by running the following command:
+
[source,terminal]
----
$ oc auth can-i update virtualmachines/stop --namespace=<namespace> --as=<user_name> --group=subresources.kubevirt.io
----
+
Example output:
+
[source,terminal]
----
yes
----

// Module included in the following assemblies:
//
// * virt/managing-vms/virt-controlling-vm-states.adoc

[id="virt-enable-vm-action-confirmation-web_{context}"]
= Enabling confirmations of virtual machine actions

[role="_abstract"]
The *Stop*, *Restart*, and *Pause* actions can display confirmation dialogs if confirmation is enabled. By default, confirmation is disabled.

.Procedure

. Click *Virtualization* -> *Settings* -> *Cluster* -> *General settings*.

. Click *VirtualMachine actions confirmation*.

. Toggle the *VirtualMachine actions confirmation* setting to *On*.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-starting-vm-web_{context}"]
= Starting a virtual machine

[role="_abstract"]
You can start a virtual machine (VM) from the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to start.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Start VirtualMachine*.

* To start the VM from the tree view:

.. Click the *>* icon next to the project name to open the list of VMs.

.. Right-click the name of the VM and select *Control* -> *Start*.

* To view comprehensive information about the selected VM before you start it:

.. Access the *VirtualMachine details* page by clicking the name of the VM.

.. Click *Actions* -> *Control* -> *Start*.
+
[NOTE]
====
When you start VM that is provisioned from a `URL` source for the first time, the VM has a status of *Importing* while {VirtProductName} imports the container from the URL endpoint. Depending on the size of the image, this process might take several minutes.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-stopping-vm-web_{context}"]
= Stopping a virtual machine

[role="_abstract"]
You can stop a virtual machine (VM) from the web console.

.Procedure

. Click *Virtualization* ->  *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to stop.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Stop VirtualMachine*.
.. If action confirmation is enabled, click *Stop* in the confirmation dialog.
* To stop the VM from the tree view:

.. Click the *>* icon next to the project name to open the list of VMs.

.. Right-click the name of the VM and select *Control* -> *Stop*.
.. If action confirmation is enabled, click *Stop* in the confirmation dialog.
* To view comprehensive information about the selected VM before you stop it:

.. Access the *VirtualMachine details* page by clicking the name of the VM.

.. Click *Actions* → *Control* -> *Stop*.
.. If action confirmation is enabled, click *Stop* in the confirmation dialog.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-restarting-vm-web_{context}"]
= Restarting a virtual machine

[role="_abstract"]
You can restart a running virtual machine (VM) from the web console.

[IMPORTANT]
====
The *Restart* action shuts down the VM and starts a new pod. This action removes all related resources including the `virt-launcher` pod and recreates them.

To avoid errors, do not restart a VM while it has a status of *Importing*.
====

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to restart.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Restart*.
.. If action confirmation is enabled, click *Restart* in the confirmation dialog.

* To restart the VM from the tree view:

.. Click the *>* icon next to the project name to open the list of VMs.

.. Right-click the name of the VM and select *Control* -> *Restart*.
.. If action confirmation is enabled, click *Restart* in the confirmation dialog.

* To view comprehensive information about the selected VM before
you restart it:

.. Access the *VirtualMachine details* page by clicking the name of the virtual
machine.

.. Click *Actions* -> *Restart*.
.. If action confirmation is enabled, click *Restart* in the confirmation dialog.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-resetting-vm-web_{context}"]
= Resetting a virtual machine

[role="_abstract"]
Unlike the *Restart* action, the *Reset* action preserves the pod in which the virtual machine (VM) is running and just hard resets the same VM inside it. When a VM is unresponsive or failed to boot, you can use the *Reset* action to bring it back immediately.

You can reset a VM from the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to restart.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Reset*.
.. If action confirmation is enabled, click *Reset* in the confirmation dialog.

* To reset the VM from the tree view:

.. Click the *>* icon next to the project name to open the list of VMs.

.. Right-click the name of the VM and select *Control* -> *Reset*.
.. If action confirmation is enabled, click *Reset* in the confirmation dialog.

* To view comprehensive information about the selected VM before
you reset it:

.. Access the *VirtualMachine details* page by clicking the name of the virtual
machine.

.. Click *Actions* -> *Control* -> *Reset*.
.. If action confirmation is enabled, click *Reset* in the confirmation dialog.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-pausing-vm-web_{context}"]
= Pausing a virtual machine

[role="_abstract"]
You can pause a virtual machine (VM) from the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to pause.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Pause VirtualMachine*.
.. If action confirmation is enabled, click *Pause* in the confirmation dialog.

* To pause the VM from the tree view:
.. Click the *>* icon next to the project name to open the list of VMs.
.. Right-click the name of the VM and select *Control* -> *Pause*.
.. If action confirmation is enabled, click *Pause* in the confirmation dialog.
* To view comprehensive information about the selected VM before you pause it:

.. Access the *VirtualMachine details* page by clicking the name of the VM.

.. Click *Actions* -> *Control* -> *Pause*.
.. If action confirmation is enabled, click *Pause* in the confirmation dialog.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-controlling-vm-states.adoc

[id="virt-unpausing-vm-web_{context}"]
= Unpausing a virtual machine

[role="_abstract"]
You can unpause a paused virtual machine (VM) from the web console.

.Prerequisites

* At least one of your VMs must have a status of *Paused*.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. In the tree view, select the project that contains the VM that you want to unpause.

. Navigate to the appropriate menu for your use case:

* To stay on this page, where you can perform actions on multiple VMs:

.. Click the Options menu {kebab} located at the far right end of the row and click *Control* -> *Unpause VirtualMachine*.

* To unpause the VM from the tree view:

.. Click the *>* icon next to the project name to open the list of VMs.

.. Right-click the name of the VM and select *Control* -> *Unpause*.

* To view comprehensive information about the selected VM before
you unpause it:

.. Access the *VirtualMachine details* page by clicking the name of the virtual
machine.

.. Click *Actions* → *Control* -> *Unpause*.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-controlling-vm-states.adoc

[id="virt-controlling-multiple-vms-web_{context}"]
= Controlling the state of multiple virtual machines

[role="_abstract"]
You can start, stop, restart, pause, and unpause multiple virtual machines (VMs) from the web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.

. Optional: Enable the *Show only projects with VirtualMachines* option above the tree view to limit the displayed projects.

. Select a relevant project from the tree view.

. Navigate to the appropriate menu for your use case:

* To change the state of all VMs in the selected project:

.. Right-click the name of the project in the tree view and select the intended action from the menu.
.. If action confirmation is enabled, confirm the action in the confirmation dialog.
* To change the state of specific VMs:

.. Select a checkbox next to the VMs you want to work with. To select all VMs, click the checkbox in the *VirtualMachines* table header.
.. Click *Actions* and select the intended action from the menu.
.. If action confirmation is enabled, confirm the action in the confirmation dialog.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Using the CLI tools
