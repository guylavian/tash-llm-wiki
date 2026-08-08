---
title: "Scheduling Windows container workloads"
type: reference
domain: openshift
slug: windows-containers-4-22-scheduling-windows-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/scheduling-windows-workloads
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Scheduling Windows container workloads

[id="scheduling-windows-workloads"]
= Scheduling Windows container workloads

[role="_abstract"]
You can use the Windows Machine Config Operator (WMCO) to schedule Windows workloads to Windows compute nodes.

== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a Windows container as the OS image.
* You have created a Windows compute machine set.

// Module included in the following assemblies:
//
// * windows_containers/scheduling-windows-workloads.adoc

[id="windows-pod-placement_{context}"]
= Windows pod placement

[role="_abstract"]
Before deploying your Windows workloads to the cluster, you must configure your Windows node scheduling so pods are assigned correctly.

The machine hosting your Windows node is managed the same as a Linux-based node. Likewise, scheduling a Windows pod to the appropriate Windows node is completed similarly, using mechanisms like taints, tolerations, and node selectors.

With multiple operating systems, and the ability to run multiple Windows OS variants in the same cluster, you must map your Windows pods to a base Windows OS variant by using a `RuntimeClass` object. For example, if you have multiple Windows nodes running on different Windows Server container versions, the cluster could schedule your Windows pods to an incompatible Windows OS variant. You must have `RuntimeClass` objects configured for each Windows OS variant on your cluster. Using a `RuntimeClass` object is also recommended if you have only one Windows OS variant available in your cluster.

For more information, see "Host and container version compatibility" in the Microsoft Windows documentation, which is linked in the "Additional resources" section.

Also, it is recommended that you set the `spec.os.name.windows` parameter in your workload pods. The Windows Machine Config Operator (WMCO) uses this field to authoritatively identify the pod operating system for validation and is used to enforce Windows-specific pod security context constraints (SCCs). Currently, this parameter has no effect on pod scheduling. For more information about this parameter, see the Kubernetes Pod OS documentation.

[IMPORTANT]
====
The container base image must be the same Windows OS version and build number that is running on the node where the conainer is to be scheduled.

Also, if you upgrade the Windows nodes from one version to another, for example going from 2022 to 2025, you must upgrade your container base image to match the new version. For more information, see Windows container version compatibility in the Microsoft Windows documentation.
====

// Module included in the following assemblies:
//
// * windows_containers/scheduling-windows-workloads.adoc

[id="creating-runtimeclass_{context}"]
= Creating a RuntimeClass object to encapsulate scheduling mechanisms

// Wording taken from Windows pod placement module
[role="_abstract"]
To deploy Windows workloads, you must create a `RuntimeClass` object to map your Windows pods to a base Windows OS variant.

Using a `RuntimeClass` object simplifies the use of scheduling mechanisms like taints and tolerations; you deploy a runtime class that encapsulates your taints and tolerations and then apply it to your pods to schedule them to the appropriate node.

Creating a runtime class is also necessary in clusters that support multiple operating system variants.

.Procedure

. Create a `RuntimeClass` object YAML file. For example, `runtime-class.yaml`:
+
[source,yaml]
----
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: windows2025
handler: 'runhcs-wcow-process'
scheduling:
  nodeSelector:
    kubernetes.io/os: 'windows'
    kubernetes.io/arch: 'amd64'
    node.kubernetes.io/windows-build: '10.0.26100'
  tolerations:
  - effect: NoSchedule
    key: os
    operator: Equal
    value: "windows"
  - effect: NoSchedule
    key: os
    operator: Equal
    value: "Windows"
----
where:

`metadata.name`:: Specifies the `RuntimeClass` object name, which is defined in the pods you want to be managed by this runtime class.
`scheduling.nodeSelector`:: Specifies labels that must be present on nodes that support this runtime class. Pods using this runtime class can only be scheduled to a node matched by this selector. The node selector of the runtime class is merged with the existing node selector of the pod. Any conflicts prevent the pod from being scheduled to the node.
* For Windows 2025, specify the `node.kubernetes.io/windows-build: '10.0.26100'` label.
* For Windows 2022, specify the `node.kubernetes.io/windows-build: '10.0.20348'` label.
* For Windows 2019, specify the `node.kubernetes.io/windows-build: '10.0.17763'` label.
`scheduling.tolerations`:: Specifies tolerations to append to pods, excluding duplicates, running with this runtime class during admission. This combines the set of nodes tolerated by the pod and the runtime class.

. Create the `RuntimeClass` object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f runtime-class.yaml
----

. Apply the `RuntimeClass` object to your pod to ensure it is scheduled to the appropriate operating system variant:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-windows-pod
spec:
  runtimeClassName: windows2025
# ...
----
where:

`spec.runtimeClassName`:: Specifies the runtime class to manage the scheduling of your pod.

// Module included in the following assemblies:
//
// * windows_containers/scheduling-windows-workloads.adoc

[id="sample-windows-workload-deployment_{context}"]
= Sample Windows container workload deployment

[role="_abstract"]
You can deploy Windows container workloads to your cluster after you have a Windows compute node available.

[NOTE]
====
This sample deployment is provided for reference only.
====

.Example `Service` object
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: win-webserver
  labels:
    app: win-webserver
spec:
  ports:
    # the port that this service should serve on
  - port: 80
    targetPort: 80
  selector:
    app: win-webserver
  type: LoadBalancer
----

.Example `Deployment` object
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: win-webserver
  name: win-webserver
spec:
  selector:
    matchLabels:
      app: win-webserver
  replicas: 1
  template:
    metadata:
      labels:
        app: win-webserver
      name: win-webserver
    spec:
      containers:
      - name: windowswebserver
        image: mcr.microsoft.com/windows/servercore:ltsc2025
        imagePullPolicy: IfNotPresent
        command:
        - powershell.exe
        - -command
        - $listener = New-Object System.Net.HttpListener; $listener.Prefixes.Add('http://*:80/'); $listener.Start();Write-Host('Listening at http://*:80/'); while ($listener.IsListening) { $context = $listener.GetContext(); $response = $context.Response; $content='<html><body><H1>Red Hat OpenShift + Windows Container Workloads</H1></body></html>'; $buffer = [System.Text.Encoding]::UTF8.GetBytes($content); $response.ContentLength64 = $buffer.Length; $response.OutputStream.Write($buffer, 0, $buffer.Length); $response.Close(); };
        securityContext:
          runAsNonRoot: false
          windowsOptions:
            runAsUserName: "ContainerAdministrator"
      os:
        name: "windows"
      runtimeClassName: windows2025
----
where:

`spec.template.spec.containers.image`:: Specifies the container image to use: `mcr.microsoft.com/powershell:<tag>` or `mcr.microsoft.com/windows/servercore:<tag>`. The container image must match the Windows version running on the node.
* For Windows 2025, use the `ltsc2025` tag.
* For Windows 2022, use the `ltsc2022` tag.
* For Windows 2019, use the `ltsc2019` tag.
`spec.template.spec.containers.command`:: Specifies the commands to execute on the container.
* For the `mcr.microsoft.com/powershell:<tag>` container image, you must define the command as `pwsh.exe`.
* For the `mcr.microsoft.com/windows/servercore:<tag>` container image, you must define the command as `powershell.exe`.
`spec.template.spec.runtimeClassName`:: Specifies the runtime class you created for the Windows operating system variant on your cluster.

// Module included in the following assemblies:
//
// * windows_containers/scheduling-windows-workloads.adoc

[id="wmco-supported-csi-drivers_{context}"]
= Support for Windows CSI drivers

[role="_abstract"]
You can use the CSI PROXY plug-in to perform storage operations on the nodes in your cluster.

{productwinc} installs CSI Proxy, which is a plug-in that enables CSI drivers for performing storage operations, on all Windows nodes in the cluster. For more information, see the CSI Proxy link in the "Additional resources" section.

To use persistent storage with Windows workloads, you must deploy a specific Windows CSI driver daemon set, as described in your storage provider's documentation. By default, the WMCO does not automatically create the Windows CSI driver daemon set. See the list of production drivers in the Kubernetes CSI Developer Documentation by using the link in the "Additional resources" section.

[NOTE]
====
Red{nbsp}Hat does not provide support for the third-party production drivers listed in the Kubernetes CSI Developer Documentation.
====

// Module included in the following assemblies:
//
// * machine_management/manually-scaling-machineset.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * windows_containers/scheduling-windows-workloads.adoc

[id="machineset-manually-scaling_{context}"]
= Scaling a compute machine set manually

[role="_abstract"]
To add or remove an instance of a machine in a compute machine set, you can manually scale the compute machine set.

This guidance is relevant to fully automated, installer-provisioned infrastructure installations. Customized, user-provisioned infrastructure installations do not have compute machine sets.

.Prerequisites

* Install an OpenShift Container Platform cluster and the `oc` command line.
* Log in to  `oc` as a user with `cluster-admin` permission.

.Procedure

. View the compute machine sets that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
The compute machine sets are listed in the form of `<clusterid>-worker-<aws-region-az>`.

. View the compute machines that are in the cluster by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io -n openshift-machine-api
----

. Set the annotation on the compute machine that you want to delete by running the following command:
+
[source,terminal]
----
$ oc annotate machines.machine.openshift.io/<machine_name> -n openshift-machine-api machine.openshift.io/delete-machine="true"
----

. Scale the compute machine set by running one of the following commands:
+
[source,terminal]
----
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
Or:
+
[source,terminal]
----
$ oc edit machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----
+
[TIP]
====
You can alternatively apply the following YAML to scale the compute machine set:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 2
----
====
+
You can scale the compute machine set up or down. It takes several minutes for the new machines to be available.
+
[IMPORTANT]
====
By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.
====

.Verification

* Verify the deletion of the intended machine by running the following command:
+
[source,terminal]
----
$ oc get machines.machine.openshift.io
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Host and container version compatibility (Microsoft Windows documentation)
* Pod OS (Kubernetes documentation)
* Windows container version compatibility (Microsoft Windows documentation)
* Production Drivers (Kubernetes CSI Developer Documentation)
* Controlling pod placement using the scheduler
* Controlling pod placement using node taints
* Placing pods on specific nodes using node selectors
