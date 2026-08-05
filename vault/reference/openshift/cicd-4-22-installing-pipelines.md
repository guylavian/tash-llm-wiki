---
title: "Installing {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-installing-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/installing-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Installing {pipelines-shortname}

[id="installing-pipelines"]
= Installing {pipelines-shortname}

[role="_abstract"]
This guide walks cluster administrators through the process of installing the {pipelines-title} Operator to an OpenShift Container Platform cluster.

// Prerequisites for installing OpenShift Operator
[discrete]
== Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed `oc` CLI.
* You have installed {pipelines-shortname} (`tkn`) CLI on your local system.
* Your cluster has the Marketplace capability enabled or the Red Hat Operator catalog source configured manually.

* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in the Obtaining the installation program to install this Operator.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in Configuring OpenShift Container Platform to use Red Hat Operators.

//Installing pipelines Operator using web console

// Module included in the following assemblies:
//
// */openshift_pipelines/installing-pipelines.adoc
[id="op-installing-pipelines-operator-in-web-console_{context}"]
= Installing the {pipelines-title} Operator in web console

You can install {pipelines-title} using the Operator listed in the OpenShift Container Platform software catalog. When you install the {pipelines-title} Operator, the custom resources (CRs) required for the pipelines configuration are automatically installed along with the Operator.

The default Operator custom resource definition (CRD) `config.operator.tekton.dev` is now replaced by `tektonconfigs.operator.tekton.dev`.  In addition, the Operator provides the following additional CRDs to individually manage {pipelines-shortname} components:
 `tektonpipelines.operator.tekton.dev`, `tektontriggers.operator.tekton.dev` and `tektonaddons.operator.tekton.dev`.

If you have {pipelines-shortname} already installed on your cluster, the existing installation is seamlessly upgraded. The Operator will replace the instance of `config.operator.tekton.dev` on your cluster with an instance of `tektonconfigs.operator.tekton.dev` and additional objects of the other CRDs as necessary.

[WARNING]
====
If you manually changed your existing installation, such as, changing the target namespace in the `config.operator.tekton.dev` CRD instance by making changes to the `resource name - cluster` field, then the upgrade path is not smooth. In such cases, the recommended workflow is to uninstall your installation and reinstall the {pipelines-title} Operator.
====

The {pipelines-title} Operator now provides the option to choose the components that you want to install by specifying profiles as part of the `TektonConfig` custom resource (CR). The `TektonConfig` CR is automatically installed when the Operator is installed.
The supported profiles are:

* Lite: This installs only Tekton Pipelines.
* Basic: This installs Tekton Pipelines, Tekton Triggers, and Tekton Chains.
* All: This is the default profile used when the `TektonConfig` CR is installed. This profile installs all of the Tekton components, including Tekton Pipelines, Tekton Triggers, Tekton Chains, {pac}, and Tekton Addons. Tekton Addons includes the `ClusterTasks`, `ClusterTriggerBindings`, `ConsoleCLIDownload`, `ConsoleQuickStart`, and `ConsoleYAMLSample` resources.

[discrete]
.Procedure

. In the *Administrator* perspective of the web console, navigate to *Ecosystem* -> *Software Catalog*.

. Use the *Filter by keyword* box to search for `{pipelines-title}` Operator in the catalog. Click the *{pipelines-title}* Operator tile.

. Read the brief description about the Operator on the *{pipelines-title}* Operator page. Click *Install*.

. On the *Install Operator* page:
+
.. Select *All namespaces on the cluster (default)* for the *Installation Mode*. This mode installs the Operator in the default `openshift-operators` namespace, which enables the Operator to watch and be made available to all namespaces in the cluster.

.. Select *Automatic* for the *Approval Strategy*. This ensures that the future upgrades to the Operator are handled automatically by the Operator Lifecycle Manager (OLM). If you select the *Manual* approval strategy, OLM creates an update request. As a cluster administrator, you must then manually approve the OLM update request to update the Operator to the new version.

.. Select an *Update Channel*.

*** The `latest` channel enables installation of the most recent stable version of the {pipelines-title} Operator. Currently, it is the default channel for installing the {pipelines-title} Operator.
*** To install a specific version of the {pipelines-title} Operator, cluster administrators can use the corresponding `pipelines-<version>` channel. For example, to install the {pipelines-title} Operator version `1.8.x`, you can use the `pipelines-1.8` channel.
+
[NOTE]
====
Starting with OpenShift Container Platform 4.11, the `preview` and `stable` channels for installing and upgrading the {pipelines-title} Operator are not available. However, in OpenShift Container Platform 4.10 and earlier versions, you can use the `preview` and `stable` channels for installing and upgrading the Operator.
====

. Click *Install*. You will see the Operator listed on the *Installed Operators* page.
+
[NOTE]
====
The Operator is installed automatically into the `openshift-operators` namespace.
====
+
. Verify that the *Status* is set to *Succeeded Up to date*  to confirm successful installation of {pipelines-title} Operator.
+
[WARNING]
====
The success status may show as *Succeeded Up to date* even if installation of other components is in-progress. Therefore, it is important to verify the installation manually in the terminal.
====
+
. Verify that all components of the {pipelines-title} Operator were installed successfully. Login to the cluster on the terminal, and run the following command:
+

[source,terminal]
----
$ oc get tektonconfig config
----
+
.Example output
----
NAME     VERSION   READY   REASON
config   1.11.0     True
----
+
If the *READY* condition is *True*, the Operator and its components have been installed successfully.
+
Additonally, check the components' versions by running the following command:
+
[source,terminal]
----
$ oc get tektonpipeline,tektontrigger,tektonchain,tektonaddon,pac
----
+
.Example output
----
NAME                                          VERSION   READY   REASON
tektonpipeline.operator.tekton.dev/pipeline   v0.47.0   True

NAME                                        VERSION   READY   REASON
tektontrigger.operator.tekton.dev/trigger   v0.23.1   True

NAME                                    VERSION   READY   REASON
tektonchain.operator.tekton.dev/chain   v0.16.0   True

NAME                                    VERSION   READY   REASON
tektonaddon.operator.tekton.dev/addon   1.11.0     True

NAME                                                             VERSION   READY   REASON
openshiftpipelinesascode.operator.tekton.dev/pipelines-as-code   v0.19.0   True
----

// Installing pipelines Operator using CLI

// Module included in the following assemblies:
//
// * openshift_pipelines/installing-pipelines.adoc

[id="op-installing-pipelines-operator-using-the-cli_{context}"]
= Installing the {pipelines-shortname} Operator using the CLI

You can install {pipelines-title} Operator from the software catalog using the CLI.

[discrete]
.Procedure

. Create a Subscription object YAML file to subscribe a namespace to the {pipelines-title} Operator,
for example, `sub.yaml`:
+
.Example Subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-pipelines-operator
  namespace: openshift-operators
spec:
  channel:  <channel name> <1>
  name: openshift-pipelines-operator-rh <2>
  source: redhat-operators <3>
  sourceNamespace: openshift-marketplace <4>
----
<1> The channel name of the Operator. The `pipelines-<version>` channel is the default channel. For example, the default channel for {pipelines-title} Operator version `1.7` is `pipelines-1.7`. The `latest` channel enables installation of the most recent stable version of the {pipelines-title} Operator.
<2> Name of the Operator to subscribe to.
<3> Name of the CatalogSource that provides the Operator.
<4> Namespace of the CatalogSource. Use `openshift-marketplace` for the default software catalog sources.

. Create the Subscription object:
+
----
$ oc apply -f sub.yaml
----
+
The {pipelines-title} Operator is now installed in the default target namespace `openshift-operators`.

// {pipelines-title} Operator in a restricted environment

// Module included in the following assemblies:
//
// */openshift_pipelines/installing-pipelines.adoc
[id="op-pipelines-operator-in-restricted-environment_{context}"]
= {pipelines-title} Operator in a restricted environment

The {pipelines-title} Operator enables support for installation of pipelines in a restricted network environment.

The Operator installs a proxy webhook that sets the proxy environment variables in the containers of the pod created by tekton-controllers based on the `cluster` proxy object. It also sets the proxy environment variables in the `TektonPipelines`, `TektonTriggers`, `Controllers`, `Webhooks`, and `Operator Proxy Webhook` resources.

By default, the proxy webhook is disabled for the `openshift-pipelines` namespace. To disable it for any other namespace, you can add the `operator.tekton.dev/disable-proxy: true` label to the `namespace` object.

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-performance-tuning-using-tektonconfig-cr_{context}"]
= Performance tuning using TektonConfig CR

You can modify the fields under the `.spec.pipeline.performance` parameter in the `TektonConfig` custom resource (CR) to change high availability (HA) support and performance configuration for the {pipelines-shortname} controller.

.Example TektonConfig performance fields
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    performance:
      disable-ha: false
      buckets: 1
      threads-per-controller: 2
      kube-api-qps: 5.0
      kube-api-burst: 10
----

The fields are optional. If you set them, the {pipelines-title} Operator includes most of the fields as arguments in the `openshift-pipelines-controller` deployment under the `openshift-pipelines-controller` container. The {pipelines-shortname} Operator also updates the `buckets` field in the `config-leader-election` configuration map under the `openshift-pipelines` namespace.

If you do not specify the values, the {pipelines-shortname} Operator does not update those fields and applies the default values for the {pipelines-shortname} controller.

[NOTE]
====
If you modify or remove any of the performance fields, the {pipelines-shortname} Operator updates the `openshift-pipelines-controller` deployment and the `config-leader-election` configuration map (if the `buckets` field changed) and re-creates `openshift-pipelines-controller` pods.
====

.Modifiable fields for tuning {pipelines-shortname} performance
[options="header"]
|===

| Name | Description | Default value for the {pipelines-shortname} controller

| `disable-ha` | Enable or disable the high availability (HA) support. By default, the HA support is enabled. | `false`

| `buckets` | The number of buckets used to partition the key space for each reconciler.

Each of the replicas uses these buckets. The instance that owns a bucket reconciles the keys partitioned into that bucket. The maximum value is `10` | `1`

| `threads-per-controller` | The number of threads (workers) to use when the work queue of the {pipelines-shortname} controller is processed. | `2`

| `kube-api-qps` | The maximum queries per second (QPS) to the cluster master from the REST client. | `5.0`

| `kube-api-burst` | The maximum burst for a throttle. | `10`

|===

[NOTE]
====
The {pipelines-shortname} Operator does not control the number of replicas of the {pipelines-shortname} controller. The `replicas` setting of the deployment determines the number of replicas. For example, to change the number of replicas to 3, enter the following command:

[source,terminal]
----
$ oc --namespace openshift-pipelines scale deployment openshift-pipelines-controller --replicas=3
----
====

[IMPORTANT]
====
The `kube-api-qps` and `kube-api-burst` fields are multiplied by 2 in the {pipelines-shortname} controller. For example, if the `kube-api-qps` and `kube-api-burst` values are `10`, the actual QPS and burst values become `20`.
====

[role="_additional-resources"]
== Additional resources

* You can learn more about installing Operators on OpenShift Container Platform in the adding Operators to a cluster section.

* To install {tekton-chains} using the {pipelines-title} Operator, see Using {tekton-chains} for {pipelines-title} supply chain security.

* To install and deploy in-cluster {tekton-hub}, see Using {tekton-hub} with {pipelines-title}.

* For more information on using pipelines in a restricted environment, see:

** Mirroring images to run pipelines in a restricted environment

** Configuring Samples Operator for a restricted cluster

** Creating a cluster with a mirrored registry
