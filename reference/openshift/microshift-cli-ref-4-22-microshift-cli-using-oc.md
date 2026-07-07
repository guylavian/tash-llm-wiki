---
title: "Using the oc tool"
type: reference
domain: openshift
slug: microshift-cli-ref-4-22-microshift-cli-using-oc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_cli_ref/microshift-cli-using-oc
version: 4.22
family: microshift_cli_ref
documentKind: "Documentation"
---

# Using the oc tool

[id="microshift-cli-using-oc"]
= Using the oc tool

[role="_abstract"]
The optional {oc-first} tool provides a subset of `oc` commands for {microshift-short} deployments. Using `oc` is convenient if you are familiar with {OCP} and Kubernetes.

// Module included in the following assemblies:
//
// * microshift-cli_ref/microshift-cli-using-oc.adoc

[id="microshift-cli-oc-about_{context}"]
= About the OpenShift CLI

[role="_abstract"]
With the OpenShift command-line interface (CLI), the `oc` command, you can deploy and manage {microshift-short} projects from a terminal. The CLI `oc` tool is ideal in the following situations:

* Working directly with project source code
* Scripting OpenShift Container Platform operations
* Managing projects while restricted by bandwidth resources

[NOTE]
====
A `kubeconfig` file must exist for the node to be accessible. The values are applied from built-in default values or a `config.yaml`, if you created one.
====

// Module included in the following assemblies:
//
// * microshift-cli-using-oc/microshift-oc-apis-errors.adoc

[id="cli-using-cli_{context}"]
= Using oc with a {microshift-short} node

[role="_abstract"]
You can complete common tasks in {microshift-short} by using the `oc` CLI.

[NOTE]
====
When you run `oc` inside a pod and do not specify a namespace, the namespace of the pod is used by default.
====

* To view the pods for the current project, run the `oc get pods` command:
+
[source,terminal]
----
$ oc get pods -o wide
----
+
.Example output
[source,terminal]
----
NAME                  READY   STATUS      RESTARTS   AGE     IP            NODE                           NOMINATED NODE
cakephp-ex-1-build    0/1     Completed   0          5m45s   10.131.0.10   ip-10-0-141-74.ec2.internal    <none>
cakephp-ex-1-deploy   0/1     Completed   0          3m44s   10.129.2.9    ip-10-0-147-65.ec2.internal    <none>
cakephp-ex-1-ktz97    1/1     Running     0          3m33s   10.128.2.11   ip-10-0-168-105.ec2.internal   <none>
----

* To view logs for a particular pod, run the `oc logs` command:
+
[source,terminal]
----
$ oc logs cakephp-ex-1-deploy
----
+
.Example output
[source,terminal]
----
--> Scaling cakephp-ex-1 to 1
--> Success
----

* To view the list of supported API resources on the server, run the `oc api-resources` command:
+
[source,terminal]
----
$ oc api-resources
----
+
.Example output
[source,terminal]
----
NAME                                  SHORTNAMES       APIGROUP                              NAMESPACED   KIND
bindings                                                                                     true         Binding
componentstatuses                     cs                                                     false        ComponentStatus
configmaps                            cm                                                     true         ConfigMap
...
----

// Getting help
// Module included in the following assemblies:
//
// * microshift_cli_ref/microshift_cli_getting_help.adoc

[id="cli-getting-help_{context}"]
= Getting help

[role="_abstract"]
You can get help with CLI commands and {microshift-short} resources in the following ways.

* Use `oc help --flag` to get information about a specific CLI command:
+
.Example: Get help for the `oc create` command
[source,terminal]
----
$ oc create --help
----
+
.Example output
[source,terminal]
----
Create a resource by filename or stdin

JSON and YAML formats are accepted.

Usage:
  oc create -f FILENAME [flags]

...
----

* Use the `oc explain` command to view the description and fields for a particular resource:
+
.Example: View documentation for the `Pod` resource
[source,terminal]
----
$ oc explain pods
----
+
.Example output
[source,terminal]
----
KIND:     Pod
VERSION:  v1

DESCRIPTION:
     Pod is a collection of containers that can run on a host. This resource is
     created by clients and scheduled onto hosts.

FIELDS:
   apiVersion	<string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

...
----

//Errors when using oc commands not enabled in MicroShift
// Module included in the following assemblies:
//
// * microshift-cli-using-oc/microshift-oc-apis-errors.adoc

[id="microshift-oc-apis-errors_{context}"]
= oc command errors in {microshift-short}

[role="_abstract"]
Not all {oc-first} commands are relevant for {microshift-short} deployments. When you use `oc` to make a request call against an unsupported API, the `oc` binary usually generates an error message about a resource that cannot be found.

* For example, when you run the following `new-project` command:
+
[source,terminal]
----
$ oc new-project test
----
+
The following error message can be generated:
+
[source,terminal]
----
Error from server (NotFound): the server could not find the requested resource (get projectrequests.project.openshift.io)
----

* When you run the `get projects` command, another error can be generated as follows:
+
[source,terminal]
----
$ oc get projects
----
+
The following error message can be generated:
+
[source,terminal]
----
error: the server doesn't have a resource type "projects"
----
