---
title: "Connect to a virtual machine console"
type: reference
domain: openshift
slug: virt-4-22-virt-accessing-vm-consoles
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-accessing-vm-consoles
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connect to a virtual machine console

[id="virt-accessing-vm-consoles"]
= Connect to a virtual machine console

[role="_abstract"]
By using VNC, serial, or desktop viewer consoles, you can access the console of your virtual machine for troubleshooting when the VM does not have network connectivity.

[NOTE]
====
Connecting to a guest VM through the VNC or serial console does not provide a full set of access features and cannot replace the Virtual Desktop Infrastructure (VDI) access. However, these consoles are useful for troubleshooting, as they allow access even if the guest VM has no network.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-vnc-console-considerations_{context}"]
= Considerations for accessing the VNC console

[role="_abstract"]
You can connect to the VNC console of a VM by using the OpenShift Container Platform web console or the `virtctl` command-line tool.

Take into account the following considerations:

* Using the VNC console is recommended for troubleshooting VMs.
* Using the VNC console is not recommended for high-traffic applications, such as Virtual Desktop Infrastructure (VDI), because of the burden on the API server.
* The API server must be able to handle the traffic load.
* The clients must be able to access the API server.
* The clients must have access credentials for the cluster.
* The VNC connection is expected to disconnect during live migration of a VM to another node.
* Using the VNC console allows only a single connection per VM at a time.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-connecting-vnc-console-web_{context}"]
= Connect to the VNC console by using the web console

[role="_abstract"]
You can connect to the VNC console of a virtual machine (VM) by using the OpenShift Container Platform web console.

[NOTE]
====
If you connect to a Windows VM with a vGPU assigned as a mediated device, you can switch between the default display and the vGPU display.
====

.Procedure

. On the *Virtualization* -> *VirtualMachines* page, click a VM to open the *VirtualMachine details* page.
. In the navigation panel, right-click the virtual machine and select *Open Console*.
. Click the *Console* tab. The VNC console session starts automatically.
+
[IMPORTANT]
====
Only one connection to the VNC console is possible at a time. If you try to create a second connection to the same VNC console, a warning is displayed. You must disconnect the existing session before you create the new session.
====

. Optional: To switch to the vGPU display of a Windows VM, select *Ctl + Alt + 2* from the *Send key* list.
+
* Select *Ctl + Alt + 1* from the *Send key* list to restore the default display.

. To end the console session, click outside the console pane and then click *Disconnect*.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-connecting-vnc-console-virtctl_{context}"]
= Connect to the VNC console by using virtctl

[role="_abstract"]
You can use the `virtctl` command-line tool to connect to the VNC console of a running virtual machine.

[NOTE]
====
If you run the `virtctl vnc` command on a remote machine over an SSH connection, you must forward the X session to your local machine by running the `ssh` command with the `-X` or `-Y` flags.
====

.Prerequisites

* You installed the `virt-viewer` package.

.Procedure

. Run the following command to start the console session:
+
[source,terminal]
----
$ virtctl vnc <vm_name> -n <namespace> --preserve-session
----
+
where:
+
<vm_name>:: The name of the VM.
+
<namespace>:: The namespace that contains the VM.
+
--preserve-session:: Prevents an existing VNC console connection from being disconnected if you try to start a new session.
+
[IMPORTANT]
====
Only one connection to the VNC console is possible at a time. If you try to create a second connection to the same VNC console, an error is displayed and the connection fails. If you try to create a second connection to the same VNC console without using the `--preserve-session` flag, this forces the existing connection to disconnect to allow the new connection.
====

. If the connection fails, run the following command to collect troubleshooting information:
+
[source,terminal]
----
$ virtctl vnc <vm_name> -v 4
----

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-grant-token-generation-permission-VNC_{context}"]
= Grant token generation permission for the VNC console by using the cluster role

[role="_abstract"]
As a cluster administrator, you can install a cluster role and bind it to a user or service account to allow access to the endpoint that generates tokens for the VNC console.

.Procedure

* Choose to bind the cluster role to either a user or service account.

** Run the following command to bind the cluster role to a user:
+
[source,terminal]
----
$ kubectl create rolebinding "${ROLE_BINDING_NAME}" --clusterrole="token.kubevirt.io:generate" --user="${USER_NAME}"
----

** Run the following command to bind the cluster role to a service account:
+
[source,terminal]
----
$ kubectl create rolebinding "${ROLE_BINDING_NAME}" --clusterrole="token.kubevirt.io:generate" --serviceaccount="${SERVICE_ACCOUNT_NAME}"
----

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-generate-temporary-token-VNC_{context}"]
= Generate a temporary token for the VNC console

[role="_abstract"]
To access the VNC of a virtual machine (VM), generate a temporary authentication bearer token for the Kubernetes API.

[NOTE]
====
Kubernetes also supports authentication using client certificates, instead of a bearer token, by modifying the curl command.
====

.Prerequisites

* A running VM with {VirtProductName} 4.14 or later and `ssp-operator` 4.14 or later.
* You have installed the {oc-first}.

.Procedure

. Set the `deployVmConsoleProxy` field value in the `HyperConverged` (`HCO`) custom resource (CR) to `true`:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} --type json -p '[{"op": "replace", "path": "/spec/deployVmConsoleProxy", "value": true}]'
----

. Generate a token by entering the following command:
+
[source,terminal]
----
$ curl --header "Authorization: Bearer ${TOKEN}" \
     "https://api.<cluster_fqdn>/apis/token.kubevirt.io/v1alpha1/namespaces/<namespace>/virtualmachines/<vm_name>/vnc?duration=<duration>"
----
+
You can set the `<duration>` parameter in hours and minutes, with a minimum duration of 10 minutes. For example: `5h30m`. If you do not set this parameter, the token is valid for 10 minutes by default.
+
Sample output:
+
[source,terminal]
----
{ "token": "eyJhb..." }
----

. Optional: Use the token provided in the output to create a variable:
+
[source,terminal]
----
$ export VNC_TOKEN="<token>"
----
+
You can now use the token to access the VNC console of a VM.

.Verification

.  Log in to the cluster by entering the following command:
+
[source,terminal]
----
$ oc login --token ${VNC_TOKEN}
----

.  Test access to the VNC console of the VM by using the `virtctl` command:
+
[source,terminal]
----
$ virtctl vnc <vm_name> -n <namespace>
----

[WARNING]
====
You cannot currently revoke a specific token.

To revoke a token, you must delete the service account that you used to create it. However, this also revokes all other tokens that you created by using the service account. Use the following command with caution:

[source,terminal]
----
$ virtctl delete serviceaccount --namespace "<namespace>" "<vm_name>-vnc-access"
----
====

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-serial-console-considerations_{context}"]
= Considerations for accessing the serial console

[role="_abstract"]
You can connect to the serial console of a virtual machine (VM) by using the OpenShift Container Platform web console or the `virtctl` command-line tool.

Take into account the following considerations:

* The clients must be able to access the API server.
* The clients must have access credentials for the cluster.
* The API server must be able to handle the traffic load.
* The serial connection is expected to disconnect during live migration of a VM to another node.
* Using the serial console allows only a single connection per VM at a time.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-connecting-serial-console-web_{context}"]
= Connect to the serial console by using the web console

[role="_abstract"]
You can connect to the serial console of a virtual machine (VM) by using the OpenShift Container Platform web console. If you connect to a Windows VM with a vGPU assigned as a mediated device, you can switch between the default display and the vGPU display.

[NOTE]
====
Running concurrent VNC connections to a single virtual machine is not currently supported.
====

.Procedure

. On the *Virtualization* -> *VirtualMachines* page, click a VM to open the *VirtualMachine details* page.
. In the navigation panel, right-click the virtual machine and select *Open Console*.
. Click the *Console* tab. The VNC console session starts automatically.
+
[IMPORTANT]
====
Only one connection to the VNC console is possible at a time. If you try to create a second connection to the same VNC console, a warning is displayed. You must disconnect the existing session before you create the new session.
====

. Click *Disconnect* to end the VNC console session. Otherwise, the VNC console session continues to run in the background.
. Select *Serial console* from the console list.
. Optional: To switch to the vGPU display of a Windows VM, select *Ctl + Alt + 2* from the *Send key* list.
+
* Select *Ctl + Alt + 1* from the *Send key* list to restore the default display.
. To end the console session, click outside the console pane and then click *Disconnect*.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-connecting-serial-console-virtctl_{context}"]
= Connect to the serial console by using virtctl

[role="_abstract"]
You can use the `virtctl` command-line tool to connect to the serial console of a running virtual machine.

[NOTE]
====
If you run the `virtctl vnc` command on a remote machine over an SSH connection, you must forward the X session to your local machine by running the `ssh` command with the `-X` or `-Y` flags.
====

.Prerequisites
* You installed the `virt-viewer` package.

.Procedure

. Run the following command to start the console session:
+
[source,terminal]
----
$ virtctl console <vm_name>
----

. Press `Ctrl+]` to end the console session.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-accessing-vm-consoles.adoc

[id="virt-connecting-desktop-viewer-web_{context}"]
= Connect to the desktop viewer by using the web console

[role="_abstract"]
You can connect to the desktop viewer of a Windows virtual machine (VM) by using the OpenShift Container Platform web console.

.Prerequisites

* You installed the QEMU guest agent on the Windows VM.
* You have an RDP client installed.

.Procedure

. On the *Virtualization* -> *VirtualMachines* page, click a VM to open the *VirtualMachine details* page.
. In the navigation panel, right-click the virtual machine and select *Open Console*.
. Click the *Console* tab. The VNC console session starts automatically.
+
[IMPORTANT]
====
Only one connection to the VNC console is possible at a time. If you try to create a second connection to the same VNC console, a warning is displayed. You must disconnect the existing session before you create the new session.
====

. Click *Disconnect* to end the VNC console session. Otherwise, the VNC console session continues to run in the background.
. Select *Desktop viewer* from the console list.
. Click *Create RDP Service* to open the *RDP Service* dialog.
. Select *Expose RDP Service* and click *Save* to create a node port service.
. Click *Launch Remote Desktop* to download an `.rdp` file and launch the desktop viewer.
. Optional: To switch to the vGPU display of a Windows VM, select *Ctl + Alt + 2* from the *Send key* list.
+
* Select *Ctl + Alt + 1* from the *Send key* list to restore the default display.
. To end the console session, click outside the console pane and then click *Disconnect*.

[id="_additional-resources_{context}"]
== Additional resources

* About the Scheduling, Scale, and Performance (SSP) Operator
* Connect to the serial console by using the web console
* Connect to the VNC console by using virtctl
* Installing virtctl
