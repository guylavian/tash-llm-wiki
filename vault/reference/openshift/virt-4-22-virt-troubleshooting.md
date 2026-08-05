---
title: "Troubleshooting"
type: reference
domain: openshift
slug: virt-4-22-virt-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-troubleshooting
version: 4.22
family: virt
documentKind: "Documentation"
---

# Troubleshooting

[id="virt-troubleshooting"]
= Troubleshooting

[role="_abstract"]
To diagnose and resolve issues with virtual machine (VM) and cluster components, you can troubleshoot {VirtProductName} by using the web console or the {oc-first}. These practices help ensure your virtualized infrastructure remains healthy.

//First new module
// Module included in the following assemblies:
//
// * virt/support/virt-support-troubleshooting.adoc

[id="virt-troubleshooting-events_{context}"]
= Events

[role="_abstract"]
To monitor and troubleshoot virtual machine (VM), namespace, and resource issues, you can review OpenShift Container Platform events. Tracking this life-cycle information helps ensure you maintain a healthy cluster environment.

.Procedure

* To view VM events, go to *VirtualMachine details* -> *Events* in the web console.

* To view namespace events, run the following command:
+
[source,terminal]
----
$ oc get events -n <namespace>
----

* To view resource events, run the following command:
+
[source,terminal]
----
$ oc describe <resource> <resource_name>
----

//Second new module
// Module included in the following assemblies:
//
// * virt/support/virt-support-troubleshooting.adoc

[id="virt-troubleshooting-pod-logs_{context}"]
= Pod logs

[role="_abstract"]
To diagnose issues and monitor {VirtProductName} pods, you can view logs using the web console or the CLI. You can also view aggregated logs using the LokiStack in the web console.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-configuring-pod-log-verbosity_{context}"]
= Configuring {VirtProductName} pod log verbosity

[role="_abstract"]
To gather more detailed diagnostic information for troubleshooting, you can configure the verbosity level of {VirtProductName} pod logs. Edit the `HyperConverged` custom resource (CR) to configure this setting.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. To set log verbosity for specific components, open the `HyperConverged` CR in your default text editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Set the log level for one or more components by editing the `spec.logVerbosityConfig` stanza. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  logVerbosityConfig:
    kubevirt:
      virtAPI: 5
      virtController: 4
      virtHandler: 3
      virtLauncher: 2
      virtOperator: 6
----
+
The log verbosity value must be an integer in the range `1–9`, where a higher number indicates a more detailed log. In this example, the `virtAPI` component logs are exposed if their priority level is `5` or higher.

. Apply your changes by saving and exiting the editor.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-viewing-virt-launcher-pod-logs-web_{context}"]
= Viewing virt-launcher pod logs with the web console

[role="_abstract"]
To diagnose and troubleshoot virtual machine issues, you can view the `virt-launcher` pod logs by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.

. Select a virtual machine to open the *VirtualMachine details* page.

. On the *General* tile, click the pod name to open the *Pod details* page.

. Click the *Logs* tab to view the logs.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-viewing-logs-cli_{context}"]
= Viewing {VirtProductName} pod logs with the CLI

[role="_abstract"]
To diagnose issues and monitor {VirtProductName} pods, you can view logs by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. View a list of pods in the {VirtProductName} namespace by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {CNVNamespace}
----
+
Example output:
+
[%collapsible]
[source,terminal]
----
NAME                               READY   STATUS    RESTARTS   AGE
disks-images-provider-7gqbc        1/1     Running   0          32m
disks-images-provider-vg4kx        1/1     Running   0          32m
virt-api-57fcc4497b-7qfmc          1/1     Running   0          31m
virt-api-57fcc4497b-tx9nc          1/1     Running   0          31m
virt-controller-76c784655f-7fp6m   1/1     Running   0          30m
virt-controller-76c784655f-f4pbd   1/1     Running   0          30m
virt-handler-2m86x                 1/1     Running   0          30m
virt-handler-9qs6z                 1/1     Running   0          30m
virt-operator-7ccfdbf65f-q5snk     1/1     Running   0          32m
virt-operator-7ccfdbf65f-vllz8     1/1     Running   0          32m
----

. View the pod log by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc logs -n {CNVNamespace} <pod_name>
----
+
[NOTE]
====
If a pod fails to start, you can use the `--previous` option to view logs from the last attempt.

To monitor log output in real time, use the `-f` option.
====
+
Example output:
+
[%collapsible]
[source,terminal]
----
{"component":"virt-handler","level":"info","msg":"set verbosity to 2","pos":"virt-handler.go:453","timestamp":"2022-04-17T08:58:37.373695Z"}
{"component":"virt-handler","level":"info","msg":"set verbosity to 2","pos":"virt-handler.go:453","timestamp":"2022-04-17T08:58:37.373726Z"}
{"component":"virt-handler","level":"info","msg":"setting rate limiter to 5 QPS and 10 Burst","pos":"virt-handler.go:462","timestamp":"2022-04-17T08:58:37.373782Z"}
{"component":"virt-handler","level":"info","msg":"CPU features of a minimum baseline CPU model: map[apic:true clflush:true cmov:true cx16:true cx8:true de:true fpu:true fxsr:true lahf_lm:true lm:true mca:true mce:true mmx:true msr:true mtrr:true nx:true pae:true pat:true pge:true pni:true pse:true pse36:true sep:true sse:true sse2:true sse4.1:true ssse3:true syscall:true tsc:true]","pos":"cpu_plugin.go:96","timestamp":"2022-04-17T08:58:37.390221Z"}
{"component":"virt-handler","level":"warning","msg":"host model mode is expected to contain only one model","pos":"cpu_plugin.go:103","timestamp":"2022-04-17T08:58:37.390263Z"}
{"component":"virt-handler","level":"info","msg":"node-labeller is running","pos":"node_labeller.go:94","timestamp":"2022-04-17T08:58:37.391011Z"}
----

//Third new module
// Module included in the following assemblies:
//
// * virt/support/virt-support-troubleshooting.adoc

[id="virt-troubleshooting-guest-system-logs_{context}"]
= Guest system logs

[role="_abstract"]
To diagnose issues with virtual machine (VM) guests, you can configure access to and view their boot logs using the OpenShift Container Platform web console or the {oc-first}.

If the guest VM has no network, you can access it using its VNC or serial console.

This feature is disabled by default. If a VM does not explicitly have this setting enabled or disabled, it inherits the cluster-wide default setting.

[IMPORTANT]
====
If sensitive information such as credentials or other personally identifiable information (PII) is written to the serial console, it is logged with all other visible text. Use SSH to send sensitive data.
====

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-enable-guest-log-default-web_{context}"]
= Enabling default access to guest system logs with the web console

[role="_abstract"]
To troubleshoot issues more easily, you can enable default access to virtual machine (VM) guest system logs by using the web console.

.Procedure

. From the side menu, click *Virtualization* -> *Settings*.

. Click *Cluster* -> *Guest management*.

. Set *Enable guest system log access* to on.

. Optional: If you want to hide the VM user credentials that were set by using cloud-init, set *Hide guest credentials for non-privileged users* to on.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-enable-guest-log-default-cli_{context}"]
= Enabling default access to guest system logs with the CLI

[role="_abstract"]
To troubleshoot issues more easily, you can enable default access to virtual machine (VM) guest system logs by editing the `HyperConverged` custom resource (CR).

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Update the `disableSerialConsoleLog` value. For example:
+
[source,yaml]
----
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  virtualMachineOptions:
    disableSerialConsoleLog: true
#...
----
+
Set the value of `disableSerialConsoleLog` to `false` if you want serial console access to be enabled on VMs by default.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-set-guest-log-single-vm-web_{context}"]
= Setting guest system log access for a single VM with the web console

[role="_abstract"]
To troubleshoot a specific virtual machine (VM) without changing global settings, you can configure the guest system log access by using the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. Set *Guest system log access* to on or off.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-set-guest-log-single-vm-cli_{context}"]
= Setting guest system log access for a single VM with the CLI

[role="_abstract"]
To troubleshoot a specific virtual machine (VM) without changing global settings, you can configure the guest system log access by editing the `VirtualMachine` CR.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the virtual machine manifest by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name>
----

. Update the value of the `logSerialConsole` field. For example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      domain:
        devices:
          logSerialConsole: true
#...
----
+
To enable access to the guest serial console log, set the `logSerialConsole` value to `true`.

. Apply the new configuration to the VM by running the following command:
+
[source,terminal]
----
$ oc apply vm <vm_name>
----

. Optional: If you edited a running VM, restart the VM to apply the new configuration. For example:
+
[source,terminal]
----
$ virtctl restart <vm_name> -n <namespace>
----

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-view-guest-system-logs-web_{context}"]
= Viewing guest system logs with the web console

[role="_abstract"]
To diagnose and troubleshoot issues with a virtual machine (VM) guest operating system, you can view the guest system logs by using the web console.

.Prerequisites

* Guest system log access is enabled.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Diagnostics* tab.

. Click *Guest system logs* to load the serial console.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-view-guest-system-logs-cli_{context}"]
= Viewing guest system logs with the CLI

[role="_abstract"]
To diagnose and troubleshoot issues with a virtual machine (VM) guest operating system, you can view the guest system logs by running the `oc logs` command.

.Prerequisites

* Guest system log access is enabled.
* You have installed the {oc-first}.

.Procedure

* View the logs by running the following command, substituting your own values for `<namespace>` and `<vm_name>`:
+
[source,terminal]
----
$ oc logs -n <namespace> -l kubevirt.io/domain=<vm_name> --tail=-1 -c guest-console-log
----

//Fourth new module
// Module included in the following assemblies:
//
// * virt/support/virt-support-troubleshooting.adoc

[id="virt-troubleshooting-log-aggregation_{context}"]
= Log aggregation

[role="_abstract"]
To more easily diagnose and troubleshoot issues, you can aggregate and filter your logs.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-viewing-logs-loki_{context}"]
= Viewing aggregated {VirtProductName} logs with Loki

[role="_abstract"]
To troubleshoot issues and monitor the health of your virtualization environment, you can view aggregated logs for {VirtProductName} pods and containers in the web console. This process requires Loki, a logging component that provides a short-term, horizontally scalable log store and log aggregation. For more information about Loki, see "Additional resources".

.Prerequisites

* You have installed the {loki-op} and deployed the `LokiStack` custom resource (CR).

.Procedure

. Navigate to *Observe* -> *Logs* in the web console.
. Select *application*, for `virt-launcher` pod logs, or *infrastructure*, for {VirtProductName} control plane pods and containers, from the log type list.
. Click *Show Query* to display the query field.
. Enter the LogQL query in the query field and click *Run Query* to display the filtered logs.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-loki-log-queries_{context}"]
= {VirtProductName} LogQL queries

[role="_abstract"]
To diagnose issues and monitor {VirtProductName} components, you can view and filter aggregated logs by running Loki Query Language (LogQL) queries on the *Observe* -> *Logs* page in the web console.

The default log type is _infrastructure_. The `virt-launcher` log type is _application_.

Optional: You can include or exclude strings or regular expressions by using line filter expressions.

[NOTE]
====
If the query matches a large number of logs, the query might time out.
====

.{VirtProductName} LogQL example queries
[cols="1a,6a",options="header"]
|====
|Component
|LogQL query

|All
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
----

|`cdi-apiserver`

`cdi-deployment`

`cdi-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="storage"
----

|`hco-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="deployment"
----

|`kubemacpool`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="network"
----

|`virt-api`

`virt-controller`

`virt-handler`

`virt-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="compute"
----

|`ssp-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="schedule"
----

|Container|[source,text]
----
{log_type=~".+",kubernetes_container_name=~"<container>\|<container>"}
\|json\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
----

Specify one or more containers separated by a pipe (`\|`).

|`virt-launcher`
|You must select *application* from the log type list before running this query.

[source,text]
----
{log_type=~".+", kubernetes_container_name="compute"}\|json
\|!= "custom-ga-command"
----

`\|!= "custom-ga-command"` excludes libvirt logs that contain the string `custom-ga-command`. (https://bugzilla.redhat.com/show_bug.cgi?id=2177684[*BZ#2177684*])
|====

You can filter log lines to include or exclude strings or regular expressions by using line filter expressions.

.Line filter expressions
[cols="1a,2",options="header"]
|====
|Line filter expression|Description
|`\|= "<string>"` |Log line contains string
|`!= "<string>"` |Log line does not contain string
|`\|~ "<regex>"` |Log line contains regular expression
|`!~ "<regex>"` |Log line does not contain regular expression
|====

.Example line filter expression
====
[source,text]
----
{log_type=~".+"}|json
|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
|= "error" != "timeout"
----
====

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-common-error-messages_{context}"]
= Common error messages

[role="_abstract"]
Troubleshoot {VirtProductName} by reviewing common error messages found in the logs.

`ErrImagePull` or `ImagePullBackOff`:: Indicates an incorrect deployment configuration or problems with the images that are referenced.

//Fifth
// Module included in the following assemblies:
//
// * virt/support/virt-support-troubleshooting.adoc

[id="virt-troubleshooting-data-volumes_{context}"]
= Troubleshooting data volumes

[role="_abstract"]
To analyze and resolve issues, you can check the `Conditions` and `Events` sections of the `DataVolume` object.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-about-dv-conditions-and-events_{context}"]
= About data volume conditions and events

[role="_abstract"]
To diagnose data volume issues, you can examine the `Conditions` and `Events` sections of the `oc describe` command output.

Run the following command to inspect the data volume:

[source,terminal]
----
$ oc describe dv <DataVolume>
----

The `Conditions` section displays the following `Types`:

* `Bound`
* `Running`
* `Ready`

The `Events` section provides the following additional information:

* `Type` of event
* `Reason` for logging
* `Source` of the event
* `Message` containing additional diagnostic information.

The output from `oc describe` does not always contains `Events`.

An event is generated when the `Status`, `Reason`, or `Message` changes.
Both conditions and events react to changes in the state of the data volume.

For example, if you misspell the URL during an import operation, the import
generates a 404 message. That message change generates an event with a reason.
The output in the `Conditions` section is updated as well.

// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

[id="virt-analyzing-datavolume-conditions-and-events_{context}"]
= Analyzing data volume conditions and events

[role="_abstract"]
To determine the state of a data volume in relation to a Persistent Volume Claim (PVC) and whether or not an operation is actively running on the data volume, inspect the `Conditions` and `Events` section of the `oc describe` command output.

You might also receive messages
that offer specific details about the status of the data volume, and how
it came to be in its current state.

There are many different combinations of conditions. Each must be evaluated in its unique context.

Examples of various combinations follow.

* `Bound` - A successfully bound PVC displays in this example.
+
Note that the `Type` is `Bound`, so the `Status` is `True`.
If the PVC is not bound, the `Status` is `False`.
+
When the PVC is bound, an event is generated stating that the PVC is bound.
In this case, the `Reason` is `Bound` and `Status` is `True`.
The `Message` indicates which PVC owns the data volume.
+
`Message`, in the `Events` section, provides further details including how
long the PVC has been bound (`Age`) and by what resource (`From`),
in this case `datavolume-controller`.
+
Example output:
+
[source,terminal]
----
Status:
  Conditions:
    Last Heart Beat Time:  2020-07-15T03:58:24Z
    Last Transition Time:  2020-07-15T03:58:24Z
    Message:               PVC win10-rootdisk Bound
    Reason:                Bound
    Status:                True
    Type:                  Bound
...
  Events:
    Type     Reason     Age    From                   Message
    ----     ------     ----   ----                   -------
    Normal   Bound      24s    datavolume-controller  PVC example-dv Bound
----

* `Running` - In this case, note that `Type` is `Running` and `Status` is `False`,
indicating that an event has occurred that caused an attempted
operation to fail, changing the Status from `True` to `False`.
+
However, note that `Reason` is `Completed` and the `Message` field indicates
`Import Complete`.
+
In the `Events` section, the `Reason` and `Message` contain additional
troubleshooting information about the failed operation. In this example,
the `Message` displays an inability to connect due to a `404`, listed in the
`Events` section's first `Warning`.
+
From this information, you conclude that an import operation was running,
creating contention for other operations that are
attempting to access the data volume.
+
Example output:
+
[source,terminal]
----
Status:
  Conditions:
    Last Heart Beat Time:  2020-07-15T04:31:39Z
    Last Transition Time:  2020-07-15T04:31:39Z
    Message:               Import Complete
    Reason:                Completed
    Status:                False
    Type:                  Running
...
  Events:
    Type     Reason       Age                From                   Message
    ----     ------       ----               ----                   -------
    Warning  Error        12s (x2 over 14s)  datavolume-controller  Unable to connect
    to http data source: expected status code 200, got 404. Status: 404 Not Found
----

* `Ready` – If `Type` is `Ready` and `Status` is `True`, then the data volume is ready
to be used, as in the following example. If the data volume is not ready to be
used, the `Status` is `False`.
+
Example output:
+
[source,terminal]
----
Status:
  Conditions:
    Last Heart Beat Time: 2020-07-15T04:31:39Z
    Last Transition Time:  2020-07-15T04:31:39Z
    Status:                True
    Type:                  Ready
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* OpenShift Container Platform events
* List of events
* Aggregated logs
* Connecting to virtual machine consoles
* LogQL log queries
