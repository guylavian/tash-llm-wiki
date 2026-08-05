---
title: "Collecting debugging data for a support case"
type: reference
domain: openshift
slug: cicd-4-22-collecting-debugging-data-for-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/collecting-debugging-data-for-support
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Collecting debugging data for a support case

[id="collecting-debugging-data-for-support"]
= Collecting debugging data for a support case

When you open a support case, you must provide debugging information about your cluster to the Red Hat Support team. You can use the `must-gather` tool to collect diagnostic information for project-level resources, cluster-level resources, and {gitops-title} components.

[NOTE]
====
For prompt support, provide diagnostic information for both OpenShift Container Platform and {gitops-title}.
====

// Module included in the following assemblies:
//
// * sandboxed_containers/troubleshooting-sandboxed-containers.adoc
// * virt/support/virt-collecting-virt-data.adoc
// * support/gathering-cluster-data.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * serverless/serverless-support.adoc

[id="about-must-gather_{context}"]
= About the must-gather tool

[role="_abstract"]
The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including:

* Resource definitions
* Service logs

By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`.

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections:

* To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section.
+
For example:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----

* To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section.
+

For example:
+
[source,terminal]
----
$ oc adm must-gather -- /usr/bin/gather_audit_logs
----
+
[NOTE]
====
- Audit logs are not collected as part of the default set of information to reduce the size of the files.
- On a Windows operating system, install the `cwRsync` client and add to the `PATH`  variable for use with the `oc rsync` command.
====

When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local` in the current working directory.

For example:

[source,terminal]
----
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
----
// todo: table or ref module listing available images?
Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option.

For example:

[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --run-namespace <namespace> \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----
// Module included in the following assembly:
//
// * cicd/gitops/collecting-debugging-data-for-support.adoc

[id="collecting-debugging-data-for-gitops_{context}"]
= Collecting debugging data for {gitops-title}

Use the `oc adm must-gather` CLI command to collect the following details about the cluster that is associated with {gitops-title}:

* The subscription and namespace of the {gitops-title} Operator.
* The namespaces where ArgoCD objects are available and the objects in those namespaces, such as `ArgoCD`, `Applications`, `ApplicationSets`, `AppProjects`, and `configmaps`.
* A list of the namespaces that are managed by the {gitops-title} Operator, and resources from those namespaces.
* All {gitops-shortname}-related custom resource objects and definitions.
* Operator and Argo CD logs.
* Warning and error-level events.

.Prerequisites
* You have logged in to the OpenShift Container Platform cluster as an administrator.
* You have installed the OpenShift Container Platform CLI (`oc`).
* You have installed the {gitops-title} Operator.

.Procedure

. Navigate to the directory where you want to store the debugging information.
. Run the `oc adm must-gather` command with the {gitops-title} `must-gather` image:
+
[source,terminal]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/gitops-must-gather-rhel8:v1.9.0
----
+
The `must-gather` tool creates a new directory that starts with `./must-gather.local` in the current directory. For example, `./must-gather.local.4157245944708210399`.

. Create a compressed file from the directory that was just created. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar -cvaf must-gather.tar.gz must-gather.local.4157245944708210399
----

. Attach the compressed file to your support case on the Red Hat Customer Portal.
