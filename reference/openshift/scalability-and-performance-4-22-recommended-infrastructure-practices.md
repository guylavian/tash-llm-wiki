---
title: "Recommended infrastructure practices"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-recommended-infrastructure-practices
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/recommended-infrastructure-practices
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Recommended infrastructure practices

[id="recommended-infrastructure-practices"]
= Recommended infrastructure practices

This topic provides recommended performance and scalability practices for infrastructure in OpenShift Container Platform.

// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-infrastructure-practices.adoc

[id="infrastructure-node-sizing_{context}"]
=  Infrastructure node sizing

_Infrastructure nodes_ are nodes that are labeled to run pieces of the OpenShift Container Platform environment. The infrastructure node resource requirements depend on the cluster age, nodes, and objects in the cluster, as these factors can lead to an increase in the number of metrics or time series in Prometheus. The following infrastructure node size recommendations are based on the results observed in cluster-density testing detailed in the *Control plane node sizing* section, where the monitoring stack and the default ingress-controller were moved to these nodes.

[options="header",cols="4*"]
|===
| Number of worker nodes |Cluster density, or number of namespaces |CPU cores |Memory (GB)

| 27
| 500
| 4
| 24

| 120
| 1000
| 8
| 48

| 252
| 4000
| 16
| 128

| 501
| 4000
| 32
| 128

|===

In general, three infrastructure nodes are recommended per cluster.

[IMPORTANT]
====
These sizing recommendations should be used as a guideline. Prometheus is a highly memory intensive application; the resource usage depends on various factors including the number of nodes, objects, the Prometheus metrics scraping interval, metrics or time series, and the age of the cluster. In addition, the router resource usage can also be affected by the number of routes and the amount/type of inbound requests.

These recommendations apply only to infrastructure nodes hosting Monitoring, Ingress and Registry infrastructure components installed during cluster creation.
====

[NOTE]
====
In OpenShift Container Platform , half of a CPU core (500 millicore) is now reserved by the system by default compared to OpenShift Container Platform 3.11 and previous versions. This influences the stated sizing recommendations.
====

[id="scaling-cluster-monitoring-operator_{context}"]
== Scaling the {cmo-full}

OpenShift Container Platform exposes metrics that the {cmo-first} collects and stores in the Prometheus-based monitoring stack. As an administrator, you can view dashboards for system resources, containers, and components metrics in the OpenShift Container Platform web console by navigating to *Observe* -> *Dashboards*.

// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-infrastructure-practices.adoc
// * installing-byoh/installing-existing-hosts.adoc

[id="prometheus-database-storage-requirements_{context}"]
= Prometheus database storage requirements

Red{nbsp}Hat performed various tests for different scale sizes.

[NOTE]
====
* The following Prometheus storage requirements are not prescriptive and should be used as a reference. Higher resource consumption might be observed in your cluster depending on workload activity and resource density, including the number of pods, containers, routes, or other resources exposing metrics collected by Prometheus.

* You can configure the size-based data retention policy to suit your storage requirements.
====

.Prometheus Database storage requirements based on number of nodes/pods in the cluster
[options="header"]
|===
|Number of nodes |Number of pods (2 containers per pod) |Prometheus storage growth per day |Prometheus storage growth per 15 days |Network (per tsdb chunk)

|50
|1800
|6.3 GB
|94 GB
|16 MB

|100
|3600
|13 GB
|195 GB
|26 MB

|150
|5400
|19 GB
|283 GB
|36 MB

|200
|7200
|25 GB
|375 GB
|46 MB
|===

Approximately 20 percent of the expected size was added as overhead to ensure that the storage requirements do not exceed the calculated value.

The above calculation is for the default OpenShift Container Platform {cmo-full}.

[NOTE]
====
CPU utilization has minor impact. The ratio is approximately 1 core out of 40 per 50 nodes and 1800 pods.
====

*Recommendations for OpenShift Container Platform*

* Use at least two infrastructure (infra) nodes.
* Use at least three *openshift-container-storage* nodes with non-volatile memory express (SSD or NVMe) drives.

// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-infrastructure-practices.adoc

[id="configuring-cluster-monitoring_{context}"]
= Configuring cluster monitoring

[role="_abstract"]
You can increase the storage capacity for the Prometheus component in the cluster monitoring stack.

.Procedure

To increase the storage capacity for Prometheus:

. Create a YAML configuration file, `cluster-monitoring-config.yaml`. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
data:
  config.yaml: |
    prometheusK8s:
      retention: {{PROMETHEUS_RETENTION_PERIOD}} <1>
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      volumeClaimTemplate:
        spec:
          storageClassName: {{STORAGE_CLASS}} <2>
          resources:
            requests:
              storage: {{PROMETHEUS_STORAGE_SIZE}} <3>
    alertmanagerMain:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      volumeClaimTemplate:
        spec:
          storageClassName: {{STORAGE_CLASS}} <2>
          resources:
            requests:
              storage: {{ALERTMANAGER_STORAGE_SIZE}} <4>
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
----
<1> The default value of Prometheus retention is `PROMETHEUS_RETENTION_PERIOD=15d`. Units are measured in time using one of these suffixes: s, m, h, d.
<2> The storage class for your cluster.
<3> A typical value is `PROMETHEUS_STORAGE_SIZE=2000Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.
<4> A typical value is `ALERTMANAGER_STORAGE_SIZE=20Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.

. Add values for the retention period, storage class, and storage sizes.

. Save the file.

. Apply the changes by running:
+
[source,terminal]
----
$ oc create -f cluster-monitoring-config.yaml
----

[role="_additional-resources"]
== Additional resources

* Infrastructure Nodes in OpenShift 4
* OpenShift Container Platform cluster maximums
* Creating infrastructure machine sets
