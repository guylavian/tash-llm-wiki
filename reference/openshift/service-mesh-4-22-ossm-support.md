---
title: "Getting support"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-support
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Getting support

[id="ossm-support"]
= Getting support

// Module included in the following assemblies:
//
// * security/compliance_operator/co-support.adoc
// * support/getting-support.adoc
// * distr_tracing/distributed-tracing-release-notes.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * osd_architecture/osd-support.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-0.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-1.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-2.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-3.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-4.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-5.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-6.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-7.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-8.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-9.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-3-0.adoc
// * microshift_support/microshift-getting-support.adoc

[id="support_{context}"]
= Getting support

[role="_abstract"]
If you experience difficulty with a procedure described in this documentation, or with OpenShift Container Platform in general, visit the Red Hat Customer Portal.

From the Customer Portal, you can:

* Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.
* Submit a support case to Red Hat Support.
* Access other product documentation.

To identify issues with your cluster, you can use {red-hat-lightspeed} in {cluster-manager-url}. {red-hat-lightspeed} provides details about issues and, if available, information on how to solve a problem.

// TODO: verify that these settings apply for Service Mesh and OpenShift virtualization, etc.
If you have a suggestion for improving this documentation or have found an
error, submit a Jira issue for the most relevant documentation component. Please provide specific details, such as the section name and OpenShift Container Platform version.

The `must-gather` tool enables you to collect diagnostic information about your
OpenShift Container Platform cluster, including virtual machines and other data related to
{SMProductName}. You can send that diagnostic information to support for both OpenShift Container Platform and {SMProductName}.

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

=== Prerequisites

* Access to the cluster as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

* The OpenShift Container Platform CLI (`oc`) installed.

// Module included in the following assemblies:
//
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * service_mesh/v2x/servicemesh-release-notes.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc

[id="ossm-about-collecting-ossm-data_{context}"]
= About collecting service mesh data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, including features and objects associated with {SMProductName}.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

* The OpenShift Container Platform CLI (`oc`) installed.

.Procedure

. To collect {SMProductName} data with `must-gather`, you must specify the {SMProductName} image.
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:{MaistraVersion}
----
+
. To collect {SMProductName} data for a specific {SMProductShortName} control plane namespace with `must-gather`, you must specify the {SMProductName} image and namespace. In this example, after `gather,` replace `<namespace>` with your {SMProductShortName} control plane namespace, such as `istio-system`.
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:{MaistraVersion} gather <namespace>
----
+
This creates a local directory that contains the following items:

* The Istio Operator namespace and its child objects
* All control plane namespaces and their children objects
* All namespaces and their children objects that belong to any service mesh
* All Istio custom resource definitions (CRD)
* All Istio CRD objects, such as VirtualServices, in a given namespace
* All Istio webhooks
