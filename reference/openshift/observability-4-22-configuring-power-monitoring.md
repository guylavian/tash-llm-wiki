---
title: "Configuring {PM-shortname}"
type: reference
domain: openshift
slug: observability-4-22-configuring-power-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-power-monitoring
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring {PM-shortname}

[id="configuring-power-monitoring"]
= Configuring {PM-shortname}

The `PowerMonitor` resource is a Kubernetes custom resource definition (CRD) that enables you to configure the deployment and monitor the status of the `PowerMonitor` resource.

// Module included in the following assemblies:

// * power_monitoring/power-monitoring-configuration.adoc

[id="power-monitoring-kepler-configuration_{context}"]
= The {PM-kepler} configuration

You can configure {PM-kepler} with the `spec` field of the `PowerMonitor` resource.

[IMPORTANT]
====
Ensure that the name of your `PowerMonitor` instance is `power-monitor`. All other instances are rejected by the {PM-operator} Webhook.
====

The following is the list of configuration options:

.PowerMonitor configuration options
[cols="1,3,2", options="header"]
|===
| Name
| Description
| Default Behavior

| deployment.nodeSelector
| The nodes on which Kepler (created by PowerMonitor) pods are scheduled.
| kubernetes.io/os: linux

| deployment.tolerations
| The tolerations for Power Monitor that allow the pods to be scheduled on nodes with specific characteristics.
| - operator: "Exists"

| deployment.security.mode
| Security mode can be set to either `none`, allowing unrestricted access to Kepler's metrics by any entity, or `rbac`, securing the metrics endpoint with TLS encryption and restricting access to authorized service accounts listed in `allowedSANames`.
| Set to `rbac` by default and only user workload prometheus is allowed access.

| deployment.security.allowedSANames
| A list of Service Account Names that can access Kepler’s metrics endpoint when security mode is `rbac`.
| In OpenShift, set to `openshift-user-workload-monitoring:prometheus-user-workload` to allow user workload monitoring to scrape Kepler.

| config.logLevel
| The level of logs to expose by Kepler.
| Set to info.

| config.metricLevels
| A list of energy metric levels to expose. Possible values include `node`, `process`, `container`, `vm`, and `pod`.
| The default list includes `node`, `pod`, and `vm`.

| config.staleness
| Specifies how long to wait before considering calculated power values as stale.
| 500ms (500 milliseconds).

| config.sampleRate
| Specifies the interval for monitoring resources such as processes, containers, and VMs.
| 5s (5 seconds).

| config.maxTerminated
| Controls terminated workload tracking. A negative value tracks unlimited workloads, zero disables tracking, and a positive value tracks the top N terminated workloads by energy consumption.
| 500.

|===

.Example `PowerMonitor` resource with default configuration
[source,yaml]
----
apiVersion: v1alpha1
kind: PowerMonitor
metadata:
  labels:
    app.kubernetes.io/name: powermonitor
    app.kubernetes.io/instance: powermonitor
    app.kubernetes.io/part-of: kepler-operator
  name: power-monitor
spec:
  kepler:
    deployment:
      nodeSelector:
        kubernetes.io/os: linux

      tolerations:
        - key: key1
          operator: Equal
          value: value1
          effect: NoSchedule

      security:
        mode: rbac
        allowedSANames:
          - openshift-user-workload-monitoring:prometheus-user-workload

    config:
      logLevel: info
      metricLevels: [node, pod, vm]
      staleness: 1s
      sampleRate: 10s
      maxTerminated: 1000
----

// Module included in the following assemblies:

// * power_monitoring/power-monitoring-configuration.adoc

[id="power-monitoring-monitoring-kepler-status_{context}"]
= Monitoring the {PM-kepler} status

You can monitor the state of the {PM-kepler} exporter with the `status` field of the `PowerMonitor` resource.

The `status` field includes information, such as the following:

* The number of nodes currently running the {PM-kepler} pods
* The number of nodes that should be running the {PM-kepler} pods
* Conditions representing the health of the {PM-kepler} resource

This provides you with valuable insights into the changes made through the `spec` field.

.Example state of the `PowerMonitor` resource
[source,yaml]
----
apiVersion: kepler.system.sustainable.computing.io/v1alpha1
kind: PowerMonitor
metadata:
  name: power-monitor
status:
   conditions: # <1>
     - lastTransitionTime: '2024-01-11T11:07:39Z'
       message: Reconcile succeeded
       observedGeneration: 1
       reason: ReconcileSuccess
       status: 'True'
       type: Reconciled
     - lastTransitionTime: '2024-01-11T11:07:39Z'
       message: >-
         power-monitor daemonset "openshift-power-monitoring/power-monitor" is deployed to all nodes and
         available; ready 2/2
       observedGeneration: 1
       reason: DaemonSetReady
       status: 'True'
       type: Available
   currentNumberScheduled: 2 # <2>
   desiredNumberScheduled: 2 # <3>
----
<1> The health of the `PowerMonitor` resource. In this example, the `PowerMonitor` resource is successfully reconciled and ready.
<2> The number of nodes currently running the {PM-kepler} pods is 2.
<3> The wanted number of nodes to run the {PM-kepler} pods is 2.
