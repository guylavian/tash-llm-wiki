---
title: "Installing Logging"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-deploying
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-deploying
version: 4.22
family: observability
documentKind: "Documentation"
---

# Installing Logging

[id="cluster-logging-deploying"]
= Installing Logging

{Product-title} Operators use custom resources (CR) to manage applications and their components. High-level configuration and settings are provided by the user within a CR. The Operator translates high-level directives into low-level actions, based on best practices embedded within the Operator’s logic. A custom resource definition (CRD) defines a CR and lists all the configurations available to users of the Operator. Installing an Operator creates the CRDs, which are then used to generate CRs.

[IMPORTANT]
====
You must install the {clo} *after* the log store Operator.
====

You deploy {logging} by installing the {loki-op} or {es-op} to manage your log store, followed by the {clo} to manage the components of logging. You can use either the OpenShift Container Platform web console or the OpenShift Container Platform CLI to install or configure {logging}.

[TIP]
====
You can alternatively apply all example objects.
====

[id="prerequisites_cluster-logging-deploying"]
== Prerequisites
* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in _Configuring OpenShift Container Platform to use Red{nbsp}Hat Operators_.

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying.adoc

[id="logging-es-deploy-console_{context}"]
= Installing {logging-uc} with Elasticsearch using the web console

You can use the OpenShift Container Platform web console to install the OpenShift Elasticsearch and Red Hat OpenShift Logging Operators. Elasticsearch is a memory-intensive application. By default, OpenShift Container Platform installs three Elasticsearch nodes with memory requests and limits of 16 GB. This initial set of three OpenShift Container Platform nodes might not have enough memory to run Elasticsearch within your cluster. If you experience memory issues that are related to Elasticsearch, add more Elasticsearch nodes to your cluster rather than increasing the memory on existing nodes.

[NOTE]
====
If you do not want to use the default Elasticsearch log store, you can remove the internal Elasticsearch `logStore` and Kibana `visualization` components from the `ClusterLogging` custom resource (CR). Removing these components is optional but saves resources.
====

.Prerequisites

* Ensure that you have the necessary persistent storage for Elasticsearch. Note that each Elasticsearch node
requires its own storage volume.
+
[NOTE]
====
If you use a local volume for persistent storage, do not use a raw block volume, which is described with `volumeMode: block` in the `LocalVolume` object. Elasticsearch cannot use raw block volumes.
====

* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in _Configuring OpenShift Container Platform to use Red Hat Operators_.

.Procedure

To install the OpenShift Elasticsearch Operator and Red Hat OpenShift Logging Operator using the OpenShift Container Platform web console:

. Install the OpenShift Elasticsearch Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Choose  *OpenShift Elasticsearch Operator* from the list of available Operators, and click *Install*.

.. Ensure that the *All namespaces on the cluster* is selected under *Installation Mode*.

.. Ensure that *openshift-operators-redhat* is selected under *Installed Namespace*.
+
You must specify the `openshift-operators-redhat` namespace. The `openshift-operators`
namespace might contain Community Operators, which are untrusted and could publish
a metric with the same name as an OpenShift Container Platform metric, which would cause
conflicts.

.. Select *Enable Operator recommended cluster monitoring on this namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object. You must select this option to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

.. Select *stable-5.y* as the *Update Channel*.
+
--
--
+
.. Select an *Approval Strategy*.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

.. Verify that the OpenShift Elasticsearch Operator installed by switching to the *Ecosystem* -> *Installed Operators* page.

.. Ensure that *OpenShift Elasticsearch Operator* is listed in all projects with a *Status* of *Succeeded*.

. Install the Red Hat OpenShift Logging Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Choose  *Red Hat OpenShift Logging* from the list of available Operators, and click *Install*.

.. Ensure that the *A specific namespace on the cluster* is selected under *Installation Mode*.

.. Ensure that *Operator recommended namespace* is *openshift-logging* under *Installed Namespace*.

.. Select *Enable Operator recommended cluster monitoring on this namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object.
You must select this option to ensure that cluster monitoring
scrapes the `openshift-logging` namespace.

.. Select *stable-5.y* as the *Update Channel*.

.. Select an *Approval Strategy*.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

.. Verify that the Red Hat OpenShift Logging Operator installed by switching to the *Ecosystem* -> *Installed Operators* page.

.. Ensure that *Red Hat OpenShift Logging* is listed in the *openshift-logging* project with a *Status* of *Succeeded*.
+
If the Operator does not appear as installed, to troubleshoot further:
+
* Switch to the *Ecosystem* -> *Installed Operators* page and inspect
the *Status* column for any errors or failures.
* Switch to the *Workloads* → *Pods* page and check the logs in any pods in the
`openshift-logging` project that are reporting issues.

. Create an OpenShift Logging instance:

.. Switch to the *Administration* -> *Custom Resource Definitions* page.

.. On the *Custom Resource Definitions* page, click *ClusterLogging*.

.. On the *Custom Resource Definition details* page, select *View Instances* from the *Actions* menu.

.. On the *ClusterLoggings* page, click *Create ClusterLogging*.
+
You might have to refresh the page to load the data.

.. In the YAML field, replace the code with the following:
+
[NOTE]
====
This default OpenShift Logging configuration should support a wide array of environments. Review the topics on tuning and
configuring {logging} components for information on modifications you can make to your OpenShift Logging cluster.
====
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance <1>
  namespace: openshift-logging
spec:
  managementState: Managed <2>
  logStore:
    type: elasticsearch <3>
    retentionPolicy: <4>
      application:
        maxAge: 1d
      infra:
        maxAge: 7d
      audit:
        maxAge: 7d
    elasticsearch:
      nodeCount: 3 <5>
      storage:
        storageClassName: <storage_class_name> <6>
        size: 200G
      resources: <7>
          limits:
            memory: 16Gi
          requests:
            memory: 16Gi
      proxy: <8>
        resources:
          limits:
            memory: 256Mi
          requests:
            memory: 256Mi
      redundancyPolicy: SingleRedundancy
  visualization:
    type: kibana <9>
    kibana:
      replicas: 1
  collection:
    type: fluentd <10>
    fluentd: {}
----
<1> The name must be `instance`.
<2> The OpenShift Logging management state. In some cases, if you change the OpenShift Logging defaults, you must set this to `Unmanaged`.
However, an unmanaged deployment does not receive updates until OpenShift Logging is placed back into a managed state.
<3> Settings for configuring Elasticsearch. Using the CR, you can configure shard replication policy and persistent storage.
<4> Specify the length of time that Elasticsearch should retain each log source. Enter an integer and a time designation: weeks(w), hours(h/H), minutes(m) and seconds(s). For example, `7d` for seven days. Logs older than the `maxAge` are deleted. You must specify a retention policy for each log source or the Elasticsearch indices will not be created for that source.
<5> Specify the number of Elasticsearch nodes. See the note that follows this list.
<6> Enter the name of an existing storage class for Elasticsearch storage. For best performance, specify a storage class that allocates block storage. If you do not specify a storage class, OpenShift Logging uses ephemeral storage.
<7> Specify the CPU and memory requests for Elasticsearch as needed. If you leave these values blank, the OpenShift Elasticsearch Operator sets default values that should be sufficient for most deployments. The default values are `16Gi` for the memory request and `1` for the CPU request.
<8> Specify the CPU and memory requests for the Elasticsearch proxy as needed. If you leave these values blank, the OpenShift Elasticsearch Operator sets default values that should be sufficient for most deployments. The default values are `256Mi` for the memory request and `100m` for the CPU request.
<9> Settings for configuring Kibana. Using the CR, you can scale Kibana for redundancy and configure the CPU and memory for your Kibana nodes. For more information, see *Configuring the log visualizer*.
<10> Settings for configuring Fluentd. Using the CR, you can configure Fluentd CPU and memory limits. For more information, see "Configuring Fluentd".
+
[NOTE]
+
====
The maximum number of master nodes is three. If you specify a `nodeCount` greater than `3`, OpenShift Container Platform creates three Elasticsearch nodes that are Master-eligible nodes, with the master, client, and data roles. The additional Elasticsearch nodes are created as Data-only nodes, using client and data roles. Master nodes perform cluster-wide actions such as creating or deleting an index, shard allocation, and tracking nodes. Data nodes hold the shards and perform data-related operations such as CRUD, search, and aggregations. Data-related operations are I/O-, memory-, and CPU-intensive. It is important to monitor these resources and to add more Data nodes if the current nodes are overloaded.

For example, if `nodeCount=4`, the following nodes are created:

[source,terminal]
----
$ oc get deployment
----

.Example output
[source,terminal]
----
cluster-logging-operator-66f77ffccb-ppzbg       1/1    Running 0 7m
elasticsearch-cd-tuhduuw-1-f5c885dbf-dlqws      1/1    Running 0 2m4s
elasticsearch-cdm-ftuhduuw-1-ffc4b9566-q6bhp    2/2    Running 0 2m40s
elasticsearch-cdm-ftuhduuw-2-7b4994dbfc-rd2gc   2/2    Running 0 2m36s
elasticsearch-cdm-ftuhduuw-3-84b5ff7ff8-gqnm2   2/2    Running 0 2m4s
----
====

.. Click *Create*. This creates the {logging} components, the `Elasticsearch` custom resource and components, and the Kibana interface.

. Verify the install:

.. Switch to the *Workloads* -> *Pods* page.

.. Select the *openshift-logging* project.
+
You should see several pods for OpenShift Logging, Elasticsearch, your collector, and Kibana similar to the following list:
+
.Example output
[source,terminal]
----
cluster-logging-operator-66f77ffccb-ppzbg       1/1     Running   0          7m
elasticsearch-cdm-ftuhduuw-1-ffc4b9566-q6bhp    2/2     Running   0          2m40s
elasticsearch-cdm-ftuhduuw-2-7b4994dbfc-rd2gc   2/2     Running   0          2m36s
elasticsearch-cdm-ftuhduuw-3-84b5ff7ff8-gqnm2   2/2     Running   0          2m4s
collector-587vb                                   1/1     Running   0          2m26s
collector-7mpb9                                   1/1     Running   0          2m30s
collector-flm6j                                   1/1     Running   0          2m33s
collector-gn4rn                                   1/1     Running   0          2m26s
collector-nlgb6                                   1/1     Running   0          2m30s
collector-snpkt                                   1/1     Running   0          2m28s
kibana-d6d5668c5-rppqm                          2/2     Running   0          2m39s
----

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying.adoc

[id="logging-es-deploy-cli_{context}"]
= Installing {logging-uc} with Elasticsearch using the CLI

Elasticsearch is a memory-intensive application. By default, OpenShift Container Platform installs three Elasticsearch nodes with memory requests and limits of 16 GB. This initial set of three OpenShift Container Platform nodes might not have enough memory to run Elasticsearch within your cluster. If you experience memory issues that are related to Elasticsearch, add more Elasticsearch nodes to your cluster rather than increasing the memory on existing nodes.

.Prerequisites

* Ensure that you have the necessary persistent storage for Elasticsearch. Note that each Elasticsearch node requires its own storage volume.
+
[NOTE]
====
If you use a local volume for persistent storage, do not use a raw block volume, which is described with `volumeMode: block` in the `LocalVolume` object. Elasticsearch cannot use raw block volumes.
====

* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in *Configuring OpenShift Container Platform to use Red{nbsp}Hat Operators*.

.Procedure

. Create a `Namespace` object for the {es-op}:
+
.Example `Namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-operators-redhat # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true" # <2>
----
<1> You must specify the `openshift-operators-redhat` namespace. The `openshift-operators`
namespace might contain Community Operators, which are untrusted and could publish
a metric with the same name as an OpenShift Container Platform metric, which would cause
conflicts.
<2> A string value that specifies the label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Namespace` object for the {clo}:
+
.Example `Namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-logging # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true"
----
<1> You must specify `openshift-logging` as the namespace for logging versions 5.7 and earlier. For logging 5.8 and later, you can use any namespace.

. Apply the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create an `OperatorGroup` object for the {es-op}:
+
.Example `OperatorGroup` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-operators-redhat
  namespace: openshift-operators-redhat # <1>
spec: {}
----
<1> You must specify the `openshift-operators-redhat` namespace.

. Apply the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object to subscribe a namespace to the {es-op}:
+
--
--
+
.Example `Subscription` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: elasticsearch-operator
  namespace: openshift-operators-redhat # <1>
spec:
  channel: <channel> # <2>
  installPlanApproval: Automatic # <3>
  source: redhat-operators # <4>
  sourceNamespace: openshift-marketplace
  name: elasticsearch-operator
----
<1> You must specify the `openshift-operators-redhat` namespace.
<2> Specify `stable`, or `stable-<x.y>` as the channel.
<3> `Automatic` allows the Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. `Manual` requires a user with appropriate credentials to approve the Operator update.
<4> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator Lifecycle Manager (OLM)

. Apply the subscription by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Verify the Operator installation by running the following command:
+
[source,terminal]
----
$ oc get csv --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE                                          NAME                            DISPLAY                            VERSION          REPLACES                        PHASE
default                                            elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
kube-node-lease                                    elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
kube-public                                        elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
kube-system                                        elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-apiserver-operator                       elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-apiserver                                elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-authentication-operator                  elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-authentication                           elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-cloud-controller-manager-operator        elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-cloud-controller-manager                 elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
openshift-cloud-credential-operator                elasticsearch-operator.v5.8.3   OpenShift Elasticsearch Operator   5.8.3            elasticsearch-operator.v5.8.2   Succeeded
----

. Create an `OperatorGroup` object for the {clo}:
+
.Example `OperatorGroup` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  targetNamespaces:
  - openshift-logging # <2>
----
<1> You must specify `openshift-logging` as the namespace for logging versions 5.7 and earlier. For logging 5.8 and later, you can use any namespace.
<2> You must specify `openshift-logging` as the namespace for logging versions 5.7 and earlier. For logging 5.8 and later, you can use any namespace.

. Apply the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object to subscribe the namespace to the {clo}:
+
.Example `Subscription` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  channel: stable # <2>
  name: cluster-logging
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-logging` namespace for logging versions 5.7 and older. For logging 5.8 and later versions, you can use any namespace.
<2> Specify `stable` or `stable-x.y` as the channel.
<3> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator Lifecycle Manager (OLM).

. Apply the `subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `ClusterLogging` object as a YAML file:
+
--
.Example `ClusterLogging` object
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance # <1>
  namespace: openshift-logging
spec:
  managementState: Managed # <2>
  logStore:
    type: elasticsearch # <3>
    retentionPolicy: # <4>
      application:
        maxAge: 1d
      infra:
        maxAge: 7d
      audit:
        maxAge: 7d
    elasticsearch:
      nodeCount: 3 # <5>
      storage:
        storageClassName: <storage_class_name> # <6>
        size: 200G
      resources: # <7>
          limits:
            memory: 16Gi
          requests:
            memory: 16Gi
      proxy: # <8>
        resources:
          limits:
            memory: 256Mi
          requests:
            memory: 256Mi
      redundancyPolicy: SingleRedundancy
  visualization:
    type: kibana # <9>
    kibana:
      replicas: 1
  collection:
    type: fluentd # <10>
    fluentd: {}
----
<1> The name must be `instance`.
<2> The OpenShift Logging management state. In some cases, if you change the OpenShift Logging defaults, you must set this to `Unmanaged`.
However, an unmanaged deployment does not receive updates until OpenShift Logging is placed back into a managed state.
<3> Settings for configuring Elasticsearch. Using the CR, you can configure shard replication policy and persistent storage.
<4> Specify the length of time that Elasticsearch should retain each log source. Enter an integer and a time designation: weeks(w), hours(h/H), minutes(m) and seconds(s). For example, `7d` for seven days. Logs older than the `maxAge` are deleted. You must specify a retention policy for each log source or the Elasticsearch indices will not be created for that source.
<5> Specify the number of Elasticsearch nodes.
<6> Enter the name of an existing storage class for Elasticsearch storage. For best performance, specify a storage class that allocates block storage. If you do not specify a storage class, OpenShift Logging uses ephemeral storage.
<7> Specify the CPU and memory requests for Elasticsearch as needed. If you leave these values blank, the OpenShift Elasticsearch Operator sets default values that should be sufficient for most deployments. The default values are `16Gi` for the memory request and `1` for the CPU request.
<8> Specify the CPU and memory requests for the Elasticsearch proxy as needed. If you leave these values blank, the OpenShift Elasticsearch Operator sets default values that should be sufficient for most deployments. The default values are `256Mi` for the memory request and `100m` for the CPU request.
<9> Settings for configuring Kibana. Using the CR, you can scale Kibana for redundancy and configure the CPU and memory for your Kibana nodes.
<10> Settings for configuring Fluentd. Using the CR, you can configure Fluentd CPU and memory limits.
--
+
[NOTE]
====
The maximum number of master nodes is three. If you specify a `nodeCount` greater than `3`, OpenShift Container Platform creates three Elasticsearch nodes that are Master-eligible nodes, with the master, client, and data roles. The additional Elasticsearch nodes are created as Data-only nodes, using client and data roles. Master nodes perform cluster-wide actions such as creating or deleting an index, shard allocation, and tracking nodes. Data nodes hold the shards and perform data-related operations such as CRUD, search, and aggregations. Data-related operations are I/O-, memory-, and CPU-intensive. It is important to monitor these resources and to add more Data nodes if the current nodes are overloaded.

For example, if `nodeCount=4`, the following nodes are created:

[source,terminal]
----
$ oc get deployment
----

.Example output
[source,terminal]
----
cluster-logging-operator-66f77ffccb-ppzbg       1/1     Running   0          7m
elasticsearch-cdm-ftuhduuw-1-ffc4b9566-q6bhp    2/2     Running   0          2m40s
elasticsearch-cdm-ftuhduuw-2-7b4994dbfc-rd2gc   2/2     Running   0          2m36s
elasticsearch-cdm-ftuhduuw-3-84b5ff7ff8-gqnm2   2/2     Running   0          2m4s
----
====

. Apply the `ClusterLogging` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Verify the installation by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-logging
----
+
.Example output
[source,terminal]
----
NAME                                            READY   STATUS    RESTARTS   AGE
cluster-logging-operator-66f77ffccb-ppzbg       1/1     Running   0          7m
elasticsearch-cdm-ftuhduuw-1-ffc4b9566-q6bhp    2/2     Running   0          2m40s
elasticsearch-cdm-ftuhduuw-2-7b4994dbfc-rd2gc   2/2     Running   0          2m36s
elasticsearch-cdm-ftuhduuw-3-84b5ff7ff8-gqnm2   2/2     Running   0          2m4s
collector-587vb                                 1/1     Running   0          2m26s
collector-7mpb9                                 1/1     Running   0          2m30s
collector-flm6j                                 1/1     Running   0          2m33s
collector-gn4rn                                 1/1     Running   0          2m26s
collector-nlgb6                                 1/1     Running   0          2m30s
collector-snpkt                                 1/1     Running   0          2m28s
kibana-d6d5668c5-rppqm                          2/2     Running   0          2m39s
----

--
--

// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-cli-install_{context}"]
= Installing {logging-uc} and the {loki-op} using the CLI

To install and configure logging on your OpenShift Container Platform cluster, an Operator such as {loki-op} for log storage must be installed first. This can be done from the OpenShift Container Platform CLI.

.Prerequisites

* You have administrator permissions.
* You installed the {oc-first}.
* You have access to a supported object store. For example: AWS S3, {gcp-full} Storage, Azure, Swift, Minio, or {rh-storage}.

.Procedure

--
--

. Create a `Namespace` object for {loki-op}:
+
.Example `Namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-operators-redhat # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true" # <2>
----
<1> You must specify the `openshift-operators-redhat` namespace. To prevent possible conflicts with metrics, you should configure the Prometheus Cluster Monitoring stack to scrape metrics from the `openshift-operators-redhat` namespace and not the `openshift-operators` namespace. The `openshift-operators` namespace might contain community Operators, which are untrusted and could publish a metric with the same name as an OpenShift Container Platform metric, which would cause conflicts.
<2> A string value that specifies the label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object for {loki-op}:
+
.Example `Subscription` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: loki-operator
  namespace: openshift-operators-redhat # <1>
spec:
  channel: stable # <2>
  name: loki-operator
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-operators-redhat` namespace.
<2> Specify `stable`, or `stable-5.<y>` as the channel.
<3> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator Lifecycle Manager (OLM).

. Apply the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `namespace` object for the {clo}:
+
.Example `namespace` object
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-logging # <1>
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-logging: "true"
    openshift.io/cluster-monitoring: "true" # <2>
----
<1> The Red{nbsp}Hat OpenShift Logging Operator is only deployable to the `openshift-logging` namespace.
<2> A string value that specifies the label as shown to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. Apply the `namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create an `OperatorGroup` object
+
.Example `OperatorGroup` object
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  targetNamespaces:
  - openshift-logging
----
<1> You must specify the `openshift-logging` namespace.

. Apply the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `Subscription` object:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  channel: stable # <2>
  name: cluster-logging
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-logging` namespace.
<2> Specify `stable`, or `stable-5.<y>` as the channel.
<3> Specify `redhat-operators`. If your OpenShift Container Platform cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the CatalogSource object you created when you configured the Operator Lifecycle Manager (OLM).

. Apply the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `LokiStack` CR:
+
.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging # <2>
spec:
  size: 1x.small # <3>
  storage:
    schemas:
    - version: v13
      effectiveDate: "<yyyy>-<mm>-<dd>"
    secret:
      name: logging-loki-s3 # <4>
      type: s3 # <5>
      credentialMode: # <6>
  storageClassName: <storage_class_name> # <7>
  tenants:
    mode: openshift-logging # <8>
----
<1> Use the name `logging-loki`.
<2> You must specify the `openshift-logging` namespace.
<3> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<4> Specify the name of your log store secret.
<5> Specify the corresponding storage type.
<6> Optional field, logging 5.9 and later. Supported user configured values are as follows: `static` is the default authentication mode available for all supported object storage types using credentials stored in a Secret. `token` for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. `token-cco` is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<7> Specify the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
<8> LokiStack defaults to running in multi-tenant mode, which cannot be modified. One tenant is provided for each log type: audit, infrastructure, and application logs. This enables access control for individual users and user groups to different log streams.

. Apply the `LokiStack CR` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Create a `ClusterLogging` CR object:
+
.Example ClusterLogging CR object
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance # <1>
  namespace: openshift-logging # <2>
spec:
  collection:
    type: vector
  logStore:
    lokistack:
      name: logging-loki
    retentionPolicy:
      application:
        maxAge: 7d
      audit:
        maxAge: 7d
      infra:
        maxAge: 7d
    type: lokistack
  visualization:
    type: ocp-console
    ocpConsole:
      logsLimit: 15
  managementState: Managed
----
<1> Name must be `instance`.
<2> Namespace must be `openshift-logging`.

. Apply the `ClusterLogging CR` object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Verify the installation by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-logging
----
+
.Example output
[source,terminal]
----
$ oc get pods -n openshift-logging
NAME                                               READY   STATUS    RESTARTS   AGE
cluster-logging-operator-fb7f7cf69-8jsbq           1/1     Running   0          98m
collector-222js                                    2/2     Running   0          18m
collector-g9ddv                                    2/2     Running   0          18m
collector-hfqq8                                    2/2     Running   0          18m
collector-sphwg                                    2/2     Running   0          18m
collector-vv7zn                                    2/2     Running   0          18m
collector-wk5zz                                    2/2     Running   0          18m
logging-view-plugin-6f76fbb78f-n2n4n               1/1     Running   0          18m
lokistack-sample-compactor-0                       1/1     Running   0          42m
lokistack-sample-distributor-7d7688bcb9-dvcj8      1/1     Running   0          42m
lokistack-sample-gateway-5f6c75f879-bl7k9          2/2     Running   0          42m
lokistack-sample-gateway-5f6c75f879-xhq98          2/2     Running   0          42m
lokistack-sample-index-gateway-0                   1/1     Running   0          42m
lokistack-sample-ingester-0                        1/1     Running   0          42m
lokistack-sample-querier-6b7b56bccc-2v9q4          1/1     Running   0          42m
lokistack-sample-query-frontend-84fb57c578-gq2f7   1/1     Running   0          42m
----

// Module is included in the following assemblies:
//
// * observability/logging/log_storage/installing-log-storage.adoc

[id="logging-loki-gui-install_{context}"]
= Installing {logging-uc} and the {loki-op} using the web console

To install and configure logging on your OpenShift Container Platform cluster, an Operator such as {loki-op} for log storage must be installed first. This can be done from the software catalog within the web console.

.Prerequisites

* You have access to a supported object store (AWS S3, {gcp-full} Storage, Azure, Swift, Minio, {rh-storage}).
* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, go to *Ecosystem* -> *Software Catalog*.

. Type {loki-op} in the *Filter by keyword* field. Click *{loki-op}* in the list of available Operators, and then click *Install*.
+
[IMPORTANT]
====
The Community {loki-op} is not supported by Red{nbsp}Hat.
====

. Select *stable* or *stable-x.y* as the *Update channel*.
+
--
--
+
The {loki-op} must be deployed to the global operator group namespace `openshift-operators-redhat`, so the *Installation mode* and *Installed Namespace* are already selected. If this namespace does not already exist, it is created for you.

. Select *Enable Operator-recommended cluster monitoring on this namespace.*
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the `Namespace` object. You must select this option to ensure that cluster monitoring scrapes the `openshift-operators-redhat` namespace.

. For *Update approval* select *Automatic*, then click *Install*.
+
If the approval strategy in the subscription is set to *Automatic*, the update process initiates as soon as a new Operator version is available in the selected channel. If the approval strategy is set to *Manual*, you must manually approve pending updates.

. Install the Red{nbsp}Hat OpenShift Logging Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Choose  *Red{nbsp}Hat OpenShift Logging* from the list of available Operators, and click *Install*.

.. Ensure that the *A specific namespace on the cluster* is selected under *Installation Mode*.

.. Ensure that *Operator recommended namespace* is *openshift-logging* under *Installed Namespace*.

.. Select *Enable Operator recommended cluster monitoring on this namespace*.
+
This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object.
You must select this option to ensure that cluster monitoring
scrapes the `openshift-logging` namespace.

.. Select *stable-5.y* as the *Update Channel*.

.. Select an *Approval Strategy*.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

. Go to the *Ecosystem* -> *Installed Operators* page. Click the *All instances* tab.

. From the *Create new* drop-down list, select *LokiStack*.

. Select *YAML view*, and then use the following template to create a `LokiStack` CR:
+
--
.Example `LokiStack` CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki # <1>
  namespace: openshift-logging # <2>
spec:
  size: 1x.small # <3>
  storage:
    schemas:
    - version: v13
      effectiveDate: "<yyyy>-<mm>-<dd>"
    secret:
      name: logging-loki-s3 # <4>
      type: s3 # <5>
      credentialMode: # <6>
  storageClassName: <storage_class_name> # <7>
  tenants:
    mode: openshift-logging # <8>
----
<1> Use the name `logging-loki`.
<2> You must specify the `openshift-logging` namespace.
<3> Specify the deployment size. In the {logging} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
<4> Specify the name of your log store secret.
<5> Specify the corresponding storage type.
<6> Optional field, logging 5.9 and later. Supported user configured values are as follows: static is the default authentication mode available for all supported object storage types using credentials stored in a Secret. token for short-lived tokens retrieved from a credential source. In this mode the static configuration does not contain credentials needed for the object storage. Instead, they are generated during runtime using a service, which allows for shorter-lived credentials and much more granular control. This authentication mode is not supported for all object storage types. token-cco is the default value when Loki is running on managed STS mode and using CCO on STS/WIF clusters.
<7> Specify the name of a storage class for temporary storage. For best performance, specify a storage class that allocates block storage. Available storage classes for your cluster can be listed by using the `oc get storageclasses` command.
<8> LokiStack defaults to running in multi-tenant mode, which cannot be modified. One tenant is provided for each log type: audit, infrastructure, and application logs. This enables access control for individual users and user groups to different log streams.
--
+
[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====

. Click *Create*.

. Create an OpenShift Logging instance:

.. Switch to the *Administration* -> *Custom Resource Definitions* page.

.. On the *Custom Resource Definitions* page, click *ClusterLogging*.

.. On the *Custom Resource Definition details* page, select *View Instances* from the *Actions* menu.

.. On the *ClusterLoggings* page, click *Create ClusterLogging*.
+
You might have to refresh the page to load the data.

.. In the YAML field, replace the code with the following:
+
--
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance # <1>
  namespace: openshift-logging # <2>
spec:
  collection:
    type: vector
  logStore:
    lokistack:
      name: logging-loki
    retentionPolicy:
      application:
        maxAge: 7d
      audit:
        maxAge: 7d
      infra:
        maxAge: 7d
    type: lokistack
  visualization:
    type: ocp-console
    ocpConsole:
      logsLimit: 15

  managementState: Managed
----
<1> Name must be `instance`.
<2> Namespace must be `openshift-logging`.
--

.Verification

. Go to *Ecosystem* -> *Installed Operators*.
. Make sure the *openshift-logging* project is selected.
. In the *Status* column, verify that you see green checkmarks with *InstallSucceeded* and the text *Up to date*.

[NOTE]
====
An Operator might display a `Failed` status before the installation finishes. If the Operator install completes with an `InstallSucceeded` message, refresh the page.
====

[role="_additional-resources"]
.Additional resources

* About OVN-Kubernetes network policy
* About the OVN-Kubernetes default Container Network Interface (CNI) network provider
