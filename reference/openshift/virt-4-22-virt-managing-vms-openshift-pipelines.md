---
title: "Manage virtual machines with {pipelines-shortname}"
type: reference
domain: openshift
slug: virt-4-22-virt-managing-vms-openshift-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-managing-vms-openshift-pipelines
version: 4.22
family: virt
documentKind: "Documentation"
---

# Manage virtual machines with {pipelines-shortname}

[id="virt-managing-vms-openshift-pipelines"]
= Manage virtual machines with {pipelines-shortname}

[role="_abstract"]
Automate virtual machine (VM) provisioning and management in your CI/CD workflows with {pipelines-shortname} tasks designed for virtualization. These tasks allow you to create, configure, and manipulate VMs and their disks as part of your automated deployment pipelines, streamlining VM lifecycle management.

{pipelines-title} is a Kubernetes-native CI/CD framework that allows developers to design and run each step of the CI/CD pipeline in its own container.

By using {pipelines-shortname} tasks and the example pipeline, you can do the following:

* Create and manage virtual machines (VMs), persistent volume claims (PVCs), data volumes, and data sources.
* Run commands in VMs.
* Manipulate disk images with `libguestfs` tools.

The tasks are located in the task catalog (ArtifactHub).

The example Windows pipeline is located in the pipeline catalog (ArtifactHub).

[id="prerequisites_virt-managing-vms-openshift-pipelines"]
== Prerequisites

* You have access to an OpenShift Container Platform cluster with `cluster-admin` permissions.
* You have installed the {oc-first}.
* You have installed {pipelines-shortname}.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-managing-vms-openshift-pipelines.adoc

[id="virt-supported-ssp-tasks_{context}"]
= Supported virtual machine tasks

[role="_abstract"]
The following table shows the supported tasks.

.Supported virtual machine tasks
[cols="1,1",options="header"]
|===
| Task | Description

| `create-vm-from-manifest`
| Create a virtual machine from a provided manifest or with `virtctl`.

| `create-vm-from-template`
| Create a virtual machine from a template.

| `copy-template`
| Copy a virtual machine template.

| `modify-vm-template`
| Modify a virtual machine template.

| `modify-data-object`
| Create or delete data volumes or data sources.

| `cleanup-vm`
| Run a script or a command in a virtual machine and stop or delete the virtual machine afterward.

| `disk-virt-customize`
| Use the `virt-customize` tool to run a customization script on a target PVC.

| `disk-virt-sysprep`
| Use the `virt-sysprep` tool to run a sysprep script on a target PVC.

| `wait-for-vmi-status`
| Wait for a specific status of a virtual machine instance and fail or succeed based on the status.
|===

[NOTE]
====
Virtual machine creation in pipelines now utilizes `ClusterInstanceType` and `ClusterPreference` instead of template-based tasks, which have been deprecated. The `create-vm-from-template`, `copy-template`, and `modify-vm-template` commands remain available but are not used in default pipeline tasks.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-managing-vms-openshift-pipelines.adoc

[id="virt-windows-efi-installer-pipeline_{context}"]
= Windows EFI installer pipeline

[role="_abstract"]
You can run the Windows EFI installer pipeline by using the web console or CLI.

The Windows EFI installer pipeline installs Windows 10, Windows 11, or Windows Server 2022 into a new data volume from a Windows installation image (ISO file). A custom answer file is used to run the installation process.

[NOTE]
====
The Windows EFI installer pipeline uses a config map file with `sysprep` predefined by OpenShift Container Platform and suitable for Microsoft ISO files. For ISO files pertaining to different Windows editions, it may be necessary to create a new config map file with a system-specific `sysprep` definition.
====

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-managing-vms-openshift-pipelines.adoc

[id="virt-running-tto-pipeline-web_{context}"]
= Running the example pipelines using the web console

[role="_abstract"]
You can run the example pipelines from the *Pipelines* menu in the web console.

.Procedure

. Click *Pipelines* -> *Pipelines* in the side menu.

. Select a pipeline to open the *Pipeline details* page.

. From the *Actions* list, select *Start*. The *Start Pipeline* dialog is displayed.

. Keep the default values for the parameters and then click *Start* to run the pipeline. The *Details* tab tracks the progress of each task and displays the pipeline status.

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-managing-vms-openshift-pipelines.adoc

[id="virt-running-tto-pipeline-cli_{context}"]
= Running the example pipelines using the CLI

[role="_abstract"]
Use a `PipelineRun` resource to run the example pipelines. A `PipelineRun` object is the running instance of a pipeline. It instantiates a pipeline for execution with specific inputs, outputs, and execution parameters on a cluster. It also creates a `TaskRun` object for each task in the pipeline.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. To run the Microsoft Windows 11 installer pipeline, create the following `PipelineRun` manifest:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1
kind: PipelineRun
metadata:
  generateName: windows11-installer-run-
  labels:
    pipelinerun: windows11-installer-run
spec:
    params:
    -   name: winImageDownloadURL
        value: <windows_image_download_url>
    -   name: acceptEula
        value: false
    pipelineRef:
        params:
        -   name: catalog
            value: redhat-pipelines
        -   name: type
            value: artifact
        -   name: kind
            value: pipeline
        -   name: name
            value: windows-efi-installer
        -   name: version
            value: 
        resolver: hub
    taskRunSpecs:
    -   pipelineTaskName: modify-windows-iso-file
        PodTemplate:
            securityContext:
                fsGroup: 107
                runAsUser: 107
----
** For `<windows_image_download_url>`, specify the URL for the Windows 11 64-bit ISO file. The product's language must be English (United States).
** Example `PipelineRun` objects have a special parameter, `acceptEula`. By setting this parameter, you are agreeing to the applicable Microsoft user license agreements for each deployment or installation of the Microsoft products. If you set it to false, the pipeline exits at the first task.

. Apply the `PipelineRun` manifest:
+
[source,terminal]
----
$ oc apply -f windows11-customize-run.yaml
----

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-deprecated-tasks.adoc

[id="virt-deprecated-tasks.web_{context}"]
= Removing deprecated or unused resources

[role="_abstract"]
You can clean up deprecated or unused resources associated with the {pipelines-title} Operator.

.Procedure

* Remove any remaining {pipelines-shortname} resources from the cluster by running the following command:
+
[source,terminal]
----
$ oc delete clusterroles,rolebindings,serviceaccounts,configmaps,pipelines,tasks \
  --selector 'app.kubernetes.io/managed-by=ssp-operator' \
  --selector 'app.kubernetes.io/component in (tektonPipelines,tektonTasks)' \
  --selector 'app.kubernetes.io/name in (tekton-pipelines,tekton-tasks)' \
  --ignore-not-found \
  --all-namespaces
----
+
If the {pipelines-title} Operator custom resource definitions (CRDs) have already been removed, the command may return an error. You can safely ignore this, as all other matching resources will still be deleted.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Understanding {pipelines-shortname}
* Task catalog (ArtifactHub)
* Windows EFI installer pipeline (ArtifactHub)
* Installing {pipelines-shortname}
* Creating CI/CD solutions for applications using {pipelines-title}
* Creating a Windows VM
