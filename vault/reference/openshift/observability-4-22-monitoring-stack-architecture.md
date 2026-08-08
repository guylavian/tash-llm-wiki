---
title: "Monitoring stack architecture"
type: reference
domain: openshift
slug: observability-4-22-monitoring-stack-architecture
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/monitoring-stack-architecture
version: 4.22
family: observability
documentKind: "Documentation"
---

# Monitoring stack architecture

[id="monitoring-stack-architecture"]
= Monitoring stack architecture

The OpenShift Container Platform monitoring stack is based on the Prometheus open source project and its wider ecosystem.
You can learn about the monitoring stack architecture, which includes default monitoring components and components for monitoring user-defined projects.

// Understanding the monitoring stack
// Module included in the following assemblies:
//
// * virt/support/virt-openshift-cluster-monitoring.adoc
// * observability/monitoring/monitoring-overview.adoc

[id="understanding-the-monitoring-stack_{context}"]
= Understanding the monitoring stack

The monitoring stack includes the following components:

Default platform monitoring components::
A set of platform monitoring components are installed in the `openshift-monitoring` project by default during an OpenShift Container Platform installation. This provides monitoring for core cluster components including Kubernetes services. The default monitoring stack also enables remote health monitoring for clusters.
A set of platform monitoring components are installed in the `openshift-monitoring` project by default during a OpenShift Container Platform installation. Red{nbsp}Hat Site Reliability Engineers (SRE) use these components to monitor core cluster components including Kubernetes services. This includes critical metrics, such as CPU and memory, collected from all of the workloads in every namespace.
+
You can see these components in the *Installed by default* section in the following diagram.

Components for monitoring user-defined projects::
If you enable monitoring for user-defined projects, additional monitoring components are installed in the `openshift-user-workload-monitoring` project. This provides optional monitoring for user-defined projects.
A set of user-defined project monitoring components are installed in the `openshift-user-workload-monitoring` project by default during a OpenShift Container Platform installation. You can use these components to monitor services and pods in user-defined projects.
+
You can see these components in the *User* section in the following diagram.

image:monitoring-architecture.png[OpenShift Container Platform monitoring architecture]

//Default monitoring components
// Module included in the following assemblies:
//
// * observability/monitoring/monitoring-overview.adoc

[id="default-monitoring-components_{context}"]
= Default monitoring components

By default, the OpenShift Container Platform  monitoring stack includes the following components:

.Default monitoring stack components
[options="header"]
|===

|Component|Description

|{cmo-full}
|The {cmo-first} is a central component of the monitoring stack. It deploys, manages, and automatically updates Prometheus and Alertmanager instances, Thanos Querier, Telemeter Client, and metrics targets. The {cmo-short} is deployed by the Cluster Version Operator (CVO).

|Prometheus Operator
|The Prometheus Operator in the `openshift-monitoring` project creates, configures, and manages platform Prometheus instances and Alertmanager instances. It also automatically generates monitoring target configurations based on Kubernetes label queries.

|Prometheus
|The OpenShift Container Platform monitoring stack is based on the Prometheus monitoring system. Prometheus is a time-series database and a rule evaluation engine for metrics. Prometheus sends alerts to Alertmanager for processing.

|Metrics Server
|The Metrics Server component (MS in the preceding diagram) collects resource metrics and exposes them in the `metrics.k8s.io` Metrics API service for use by other tools and APIs, which frees the core platform Prometheus stack from handling this functionality. Note that with the OpenShift Container Platform 4.16 release, Metrics Server replaces Prometheus Adapter.

|Alertmanager
|The Alertmanager service handles alerts received from Prometheus. Alertmanager is also responsible for sending the alerts to external notification systems.

|kube-state-metrics agent
|The kube-state-metrics exporter agent (KSM in the preceding diagram) converts Kubernetes objects to metrics that Prometheus can use.

|monitoring-plugin
|The monitoring-plugin dynamic plugin component deploys the monitoring pages in the *Observe* section of the OpenShift Container Platform web console.
You can use {cmo-full} config map settings to manage monitoring-plugin resources for the web console pages.

|openshift-state-metrics agent
|The openshift-state-metrics exporter (OSM in the preceding diagram) expands upon kube-state-metrics by adding metrics for OpenShift Container Platform-specific resources.

|node-exporter agent
|The node-exporter agent (NE in the preceding diagram) collects metrics about every node in a cluster. The node-exporter agent is deployed on every node.

|Thanos Querier
|Thanos Querier aggregates and optionally deduplicates core OpenShift Container Platform metrics and metrics for user-defined projects under a single, multi-tenant interface.

|Telemeter Client
|Telemeter Client sends a subsection of the data from platform Prometheus instances to Red{nbsp}Hat to enable remote health monitoring for clusters.

|===

The monitoring stack monitors all components within the stack. The components are automatically updated when OpenShift Container Platform is updated.

// Module included in the following assemblies:
//
// * observability/monitoring/monitoring-overview.adoc

[id="default-monitoring-targets_{context}"]
= Default monitoring targets

In addition to the components of the stack itself, the default monitoring stack monitors additional platform components.

The following are examples of monitoring targets:

The following are examples of targets monitored by Red{nbsp}Hat Site Reliability Engineers (SRE) in your OpenShift Container Platform cluster:

* CoreDNS
* etcd
* HAProxy
* Image registry
* Kubelets
* Kubernetes API server
* Kubernetes controller manager
* Kubernetes scheduler
* OpenShift API server
* OpenShift Controller Manager
* Operator Lifecycle Manager (OLM)

[NOTE]
====
The exact list of targets can vary depending on your cluster capabilities and installed components.
====

[NOTE]
====
* The exact list of targets can vary depending on your cluster capabilities and installed components.

* Each OpenShift Container Platform component is responsible for its monitoring configuration. For problems with the monitoring of an OpenShift Container Platform component, open a
Jira issue against that component, not against the general monitoring component.
====

Other OpenShift Container Platform framework components might be exposing metrics as well. For details, see their respective documentation.

[role="_additional-resources"]
.Additional resources
* Getting detailed information about a metrics target

//Components for monitoring user-defined projects
// Module included in the following assemblies:
//
// * observability/monitoring/monitoring-overview.adoc

[id="components-for-monitoring-user-defined-projects_{context}"]
= Components for monitoring user-defined projects

OpenShift Container Platform

includes an optional enhancement to the monitoring stack that helps you monitor services and pods in user-defined projects. This feature includes the following components:

.Components for monitoring user-defined projects
[options="header"]
|===

|Component|Description

|Prometheus Operator
|The Prometheus Operator in the `openshift-user-workload-monitoring` project creates, configures, and manages Prometheus and Thanos Ruler instances in the same project.

|Prometheus
|Prometheus is the monitoring system that provides monitoring for user-defined projects. Prometheus sends alerts to Alertmanager for processing.

|Thanos Ruler
|The Thanos Ruler is a rule evaluation engine for Prometheus that is deployed as a separate process. In OpenShift Container Platform

, Thanos Ruler provides rule and alerting evaluation for the monitoring of user-defined projects.

|Alertmanager
|The Alertmanager service handles alerts received from Prometheus and Thanos Ruler. Alertmanager is also responsible for sending user-defined alerts to external notification systems. Deploying this service is optional.

|===

[NOTE]
====
The components in the preceding table are deployed after you enable monitoring for user-defined projects.
====

The monitoring stack monitors all components for user-defined projects. The components are automatically updated when OpenShift Container Platform is updated.

// Module included in the following assemblies:
//
// * observability/monitoring/monitoring-overview.adoc

[id="monitoring-targets-for-user-defined-projects_{context}"]
= Monitoring targets for user-defined projects

When monitoring is enabled for user-defined projects, you can monitor:

Monitoring is enabled by default for OpenShift Container Platform user-defined projects. You can monitor:

* Metrics provided through service endpoints in user-defined projects.
* Pods running in user-defined projects.

//The monitoring stack in high-availability clusters
// Module included in the following assembly:
//
// * observability/monitoring/monitoring-overview.adoc

[id="monitoring-stack-in-ha-clusters_{context}"]
= The monitoring stack in high-availability clusters

By default, in multi-node clusters, the following components run in high-availability (HA) mode to prevent data loss and service interruption:

* Prometheus
* Alertmanager
* Thanos Ruler
* Thanos Querier
* Metrics Server
* Monitoring plugin

The component is replicated across two pods, each running on a separate node. This means that the monitoring stack can tolerate the loss of one pod.

Prometheus in HA mode::

* Both replicas independently scrape the same targets and evaluate the same rules.
* The replicas do not communicate with each other. Therefore, data might differ between the pods.

Alertmanager in HA mode::

* The two replicas synchronize notification and silence states with each other. This ensures that each notification is sent at least once.
* If the replicas fail to communicate or if there is an issue on the receiving side, notifications are still sent, but they might be duplicated.

[IMPORTANT]
====
Prometheus, Alertmanager, and Thanos Ruler are stateful components. To ensure high availability, you must configure them with persistent storage.
====

[role="_additional-resources"]
.Additional resources

* Configuring persistent storage
* Configuring performance and scalability

* Configuring persistent storage
* Configuring performance and scalability

//TLS security and rotation in the monitoring stack
// Module included in the following assembly:
//
// * observability/monitoring/monitoring-stack-architecture.adoc

[id="tls-security-and-rotation_{context}"]
= TLS security and rotation in the monitoring stack

[role="_abstract"]
Learn how TLS profiles and certificate rotation work in the OpenShift Container Platform monitoring stack to keep communication secure.

TLS security profiles for monitoring components::
All components of the monitoring stack use the TLS security profile settings that are centrally configured by a cluster administrator.
The monitoring stack component uses the TLS security profile settings that already exist in the `tlsSecurityProfile` field in the global OpenShift Container Platform `apiservers.config.openshift.io/cluster` resource.

TLS certificate rotation and automatic restarts::
The {cmo-full} manages the internal TLS certificate lifecycle for the monitoring components. These certificates secure the internal communication between the monitoring components.
+
During certificate rotation, the {cmo-short} updates secrets and config maps, which triggers automatic restarts of affected pods. This is an expected behavior, and the pods recover automatically.
+
The following example shows events that occur during certificate rotation:
+
[source,terminal]
----
$ oc get events -n openshift-monitoring

LAST SEEN   TYPE      REASON              OBJECT                                   MESSAGE
2h39m       Normal    SecretUpdated       deployment/cluster-monitoring-operator   Updated Secret/grpc-tls -n openshift-monitoring because it changed
2h39m       Normal    SecretCreated       deployment/cluster-monitoring-operator   Created Secret/prometheus-user-workload-grpc-tls -n openshift-user-workload-monitoring because it was missing
2h39m       Normal    SecretCreated       deployment/cluster-monitoring-operator   Created Secret/thanos-querier-grpc-tls -n openshift-monitoring because it was missing
2h39m       Normal    SecretCreated       deployment/cluster-monitoring-operator   Created Secret/thanos-ruler-grpc-tls -n openshift-user-workload-monitoring because it was missing
2h39m       Normal    SecretCreated       deployment/cluster-monitoring-operator   Created Secret/prometheus-k8s-grpc-tls -n openshift-monitoring because it was missing
2h38m       Warning   FailedMount         pod/prometheus-k8s-0                     MountVolume.SetUp failed for volume "secret-grpc-tls" : secret "prometheus-k8s-grpc-tls" not found
2h39m       Normal    Created             pod/prometheus-k8s-0                     Created container kube-rbac-proxy-thanos
2h39m       Normal    Started             pod/prometheus-k8s-0                     Started container kube-rbac-proxy-thanos
2h39m       Normal    SuccessfulDelete    statefulset/prometheus-k8s               delete Pod prometheus-k8s-0 in StatefulSet prometheus-k8s successful
2h39m       Normal    SuccessfulCreate    statefulset/prometheus-k8s               create Pod prometheus-k8s-0 in StatefulSet prometheus-k8s successful
----

[role="_additional-resources"]
.Additional resources
* Configuring TLS security profiles

//Glossary of common terms for OCP monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/monitoring-overview.adoc

[id="monitoring-common-terms_{context}"]
= Glossary of common terms for OpenShift Container Platform monitoring

This glossary defines common terms that are used in OpenShift Container Platform architecture.

Alertmanager::
Alertmanager handles alerts received from Prometheus. Alertmanager is also responsible for sending the alerts to external notification systems.

Alerting rules::
Alerting rules contain a set of conditions that outline a particular state within a cluster. Alerts are triggered when those conditions are true. An alerting rule can be assigned a severity that defines how the alerts are routed.

{cmo-full}::
The {cmo-first} is a central component of the monitoring stack. It deploys and manages Prometheus instances such as, the Thanos Querier, the Telemeter Client, and metrics targets to ensure that they are up to date. The {cmo-short} is deployed by the Cluster Version Operator (CVO).

Cluster Version Operator::
The Cluster Version Operator (CVO) manages the lifecycle of cluster Operators, many of which are installed in OpenShift Container Platform by default.

config map::
A config map provides a way to inject configuration data into pods. You can reference the data stored in a config map in a volume of type `ConfigMap`. Applications running in a pod can use this data.

Container::
A container is a lightweight and executable image that includes software and all its dependencies. Containers virtualize the operating system. As a result, you can run containers anywhere from a data center to a public or private cloud as well as a developer's laptop.

custom resource (CR)::
A CR is an extension of the Kubernetes API. You can create custom resources.

etcd::
etcd is the key-value store for OpenShift Container Platform, which stores the state of all resource objects.

Kubelets::
Runs on nodes and reads the container manifests. Ensures that the defined containers have started and are running.

Kubernetes API server::
Kubernetes API server validates and configures data for the API objects.

Kubernetes controller manager::
Kubernetes controller manager governs the state of the cluster.

Kubernetes scheduler::
Kubernetes scheduler allocates pods to nodes.

labels::
Labels are key-value pairs that you can use to organize and select subsets of objects such as a pod.

Metrics Server::
The Metrics Server monitoring component collects resource metrics and exposes them in the `metrics.k8s.io` Metrics API service for use by other tools and APIs, which frees the core platform Prometheus stack from handling this functionality.

node::
A compute machine in the OpenShift Container Platform cluster. A node is either a virtual machine (VM) or a physical machine.

Operator::
The preferred method of packaging, deploying, and managing a Kubernetes application in your OpenShift Container Platform cluster. An Operator takes human operational knowledge and encodes it into software that is packaged and shared with customers.

Operator Lifecycle Manager (OLM)::
OLM helps you install, update, and manage the lifecycle of Kubernetes native applications. OLM is an open source toolkit designed to manage Operators in an effective, automated, and scalable way.

Persistent storage::
Stores the data even after the device is shut down. Kubernetes uses persistent volumes to store the application data.

Persistent volume claim (PVC)::
You can use a PVC to mount a PersistentVolume into a Pod. You can access the storage without knowing the details of the cloud environment.

pod::
The pod is the smallest logical unit in Kubernetes. A pod is comprised of one or more containers to run in a worker node.

Prometheus::
Prometheus is the monitoring system on which the OpenShift Container Platform monitoring stack is based. Prometheus is a time-series database and a rule evaluation engine for metrics. Prometheus sends alerts to Alertmanager for processing.

Prometheus Operator::
The Prometheus Operator in the `openshift-monitoring` project creates, configures, and manages platform Prometheus and Alertmanager instances. It also automatically generates monitoring target configurations based on Kubernetes label queries.

Silences::
A silence can be applied to an alert to prevent notifications from being sent when the conditions for an alert are true. You can mute an alert after the initial notification, while you work on resolving the underlying issue.

storage::
OpenShift Container Platform supports many types of storage, both for on-premise and cloud providers.
OpenShift Container Platform supports many types of storage on AWS and {gcp-short}.
OpenShift Container Platform supports many types of storage on AWS.
You can manage container storage for persistent and non-persistent data in your OpenShift Container Platform cluster.

Thanos Ruler::
The Thanos Ruler is a rule evaluation engine for Prometheus that is deployed as a separate process. In OpenShift Container Platform, Thanos Ruler provides rule and alerting evaluation for the monitoring of user-defined projects.

Vector::
Vector is a log collector that deploys to each OpenShift Container Platform node. It collects log data from each node, transforms the data, and forwards it to configured outputs.

web console::
A user interface (UI) to manage OpenShift Container Platform.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* About remote health monitoring
* Granting users permissions for monitoring for user-defined projects
* Configuring TLS security profiles
