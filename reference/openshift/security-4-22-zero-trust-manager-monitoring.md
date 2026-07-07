---
title: "Monitoring {zero-trust-full}git"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-monitoring
version: 4.22
family: security
documentKind: "Documentation"
---

# Monitoring {zero-trust-full}git

[id="zero-trust-manager-monitoring_{context}"]
= Monitoring {zero-trust-full}git

[role="_abstract"]
Track the performance of the {zero-trust-full} by collecting metrics. Configure monitoring to collect metrics from the Security Production Identity Framework for Everyone (SPIRE) Server and SPIRE Agent components.
// Enabling metrics for the {zero-trust-full}

// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-enable-monitoring_{context}"]
= Enabling user workload monitoring

[role="_abstract"]
Enable user workload monitoring to track metrics for your user-defined projects. Configuring this feature allows you to observe application performance and helps you maintain the health of your services.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.

.Procedure

. Create the `cluster-monitoring-config.yaml` file to define and configure the `ConfigMap`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
    enableUserWorkload: true
----

. Apply the `ConfigMap` by running the following command:
+
[source,terminal]
----
$ oc apply -f cluster-monitoring-config.yaml
----

.Verification

* Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pod
----
+
.Example output
[source,text]
----
NAME                                   READY   STATUS    RESTARTS   AGE
prometheus-operator-6cb6bd9588-dtzxq   2/2     Running   0          50s
prometheus-user-workload-0             6/6     Running   0          48s
prometheus-user-workload-1             6/6     Running   0          48s
thanos-ruler-user-workload-0           4/4     Running   0          42s
thanos-ruler-user-workload-1           4/4     Running   0          42s
----

The status of the pods such as `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` must be `Running`.

[role="_additional-resources"]
.Additional resources

* Setting up metrics collection for user-defined projects

// Module included in the following assemblies:
//
// * security/zer_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-enable-metrics-server_{context}"]
= Configuring metrics collection for SPIRE Server by using a ServiceMonitor

[role="_abstract"]
To collect custom metrics from the SPIRE Server, create a ServiceMonitor custom resource (CR). This configuration enables the Prometheus Operator to scrape metrics from the default endpoint, which helps you monitor your SPIRE deployment.

The SPIRE Server operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Server by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.

* You have installed the {zero-trust-full}.

* You have deployed the SPIRE Server operand in the cluster.

* You have enabled the user workload monitoring.

.Procedure

. Create the `ServiceMonitor` CR:

.. Create the YAML file that defines the `ServiceMonitor` CR:
+
.Example `servicemonitor-spire-server` file
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
labels:
  app.kubernetes.io/name: server
  app.kubernetes.io/instance: spire
name: spire-server-metrics
namespace: zero-trust-workload-identity-manager
spec:
endpoints:
- port: metrics
  interval: 30s
  path: /metrics
selector:
  matchLabels:
    app.kubernetes.io/name: server
    app.kubernetes.io/instance: spire
namespaceSelector:
  matchNames:
  - zero-trust-workload-identity-manager
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc create -f servicemonitor-spire-server.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Server. The collected metrics are labeled with `job="spire-server"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Targets*.

. In the *Label* filter field, enter the following label to filter the metrics targets:
+
[source,terminal]
----
$ service=zero-trust-workload-identity-manager-metrics-service
----

. Confirm that the *Status* column shows `Up` for the `spire-server-metrics` entry.

[role="_additional-resources"]
.Additional resources

* Configuring user workload monitoring

// Module included in the following assemblies:
//
// * security/zer_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-enable-metrics-agent_{context}"]
= Configuring metrics collection for SPIRE Agent by using a Service Monitor

[role="_abstract"]
Configure metrics collection for the SPIRE Agent by creating a `ServiceMonitor` custom resource (CR). This enables the Prometheus Operator to collect custom metrics that the SPIRE Agent exposes on the default port.

The SPIRE Agent operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Agent by creating a `ServiceMonitor` custom resource (CR), which enables the Prometheus Operator to collect custom metrics.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.

* You have installed the {zero-trust-full}.

* You have deployed the SPIRE Agent operand in the cluster.

* You have enabled the user workload monitoring.

.Procedure

. Create the `ServiceMonitor` CR:

.. Create the YAML file that defines the `ServiceMonitor` CR:
+
.Example `servicemonitor-spire-agent.yaml` file
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app.kubernetes.io/name: agent
    app.kubernetes.io/instance: spire
  name: spire-agent-metrics
  namespace: zero-trust-workload-identity-manager
spec:
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
  selector:
    matchLabels:
      app.kubernetes.io/name: agent
      app.kubernetes.io/instance: spire
  namespaceSelector:
    matchNames:
    - zero-trust-workload-identity-manager
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc create -f servicemonitor-spire-agent.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Agent. The collected metrics are labeled with `job="spire-agent"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* → *Targets*.

. In the *Label* filter field, enter the following label to filter the metrics targets:
+
[source,terminal]
----
$ service=spire-agent
----

. Confirm that the *Status* column shows `Up` for the `spire-agent-metrics` entry.

// Module included in the following assemblies:
//
// * security/zer_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-enable-metrics-operator_{context}"]
= Configuring metrics collection for the Operator by using a ServiceMonitor

[role="_abstract"]
The {zero-trust-full} exposes metrics by default on port 8443 at the `/metrics` service endpoint. You can configure metrics collection for the Operator by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

The SPIRE Server operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Server by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.

* You have installed the {zero-trust-full}.

* You have enabled the user workload monitoring.

.Procedure

. Configure the Operator to use HTTP or HTTPS protocols for the metrics server.

.. Update the subscription object for {zero-trust-full} to configure the HTTP protocol by running the following command:
+
[source,terminal]
----
$ oc -n zero-trust-workload-identity-manager patch subscription zero-trust-workload-identity-manager-subscription --type='merge' -p '{"spec":{"config":{"env":[{"name":"METRICS_BIND_ADDRESS","value":":8080"}, {"name": "METRICS_SECURE", "value": "false"}]}}}'
----

.. Verify the {zero-trust-full} pod is redeployed and that the configured values for `METRICS_BIND_ADDRESS` and `METRICS_SECURE` is updated by running the following command:
+
[source,terminal]
----
$ oc set env --list deployment/zero-trust-workload-identity-manager-controller-manager -n zero-trust-workload-identity-manager | grep -e METRICS_BIND_ADDRESS -e METRICS_SECURE -e container
----
+
.Example output
[source,text]
----
deployments/zero-trust-workload-identity-manager-controller-manager, container manager
METRICS_BIND_ADDRESS=:8080
METRICS_SECURE=false
----

. Create the `Secret` resource with `kubernetes.io/service-account.name` annotation to inject the token required for authenticating with the metrics server.

..  Create the `secret-zero-trust-workload-identity-manager.yaml` YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
 labels:
   name: zero-trust-workload-identity-manager
 name: zero-trust-workload-identity-manager-metrics-auth
 namespace: zero-trust-workload-identity-manager
 annotations:
   kubernetes.io/service-account.name: zero-trust-workload-identity-manager-controller-manager
type: kubernetes.io/service-account-token
----

.. Create the `Secret` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f secret-zero-trust-workload-identity-manager.yaml
----

. Create the `ClusterRoleBinding` resource required for granting permissions to access the metrics.

.. Create the `clusterrolebinding-zero-trust-workload-identity-manager.yaml` YAML file:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 labels:
   name: zero-trust-workload-identity-manager
 name: zero-trust-workload-identity-manager-allow-metrics-access
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: zero-trust-workload-identity-manager-metrics-reader
subjects:
- kind: ServiceAccount
  name: zero-trust-workload-identity-manager-controller-manager
  namespace: zero-trust-workload-identity-manager
----

.. Create the `ClusterRoleBinding` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterrolebinding-zero-trust-workload-identity-manager.yaml
----

. Create the following `ServiceMonitor` CR if the metrics server is configured to use `http`.

.. Create the `servicemonitor-zero-trust-workload-identity-manager-http.yaml` YAML file:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    name: zero-trust-workload-identity-manager
  name: zero-trust-workload-identity-manager-metrics-monitor
  namespace: zero-trust-workload-identity-manager
spec:
  endpoints:
    - authorization:
        credentials:
          name: zero-trust-workload-identity-manager-metrics-auth
          key: token
        type: Bearer
      interval: 60s
      path: /metrics
      port: metrics-http
      scheme: http
      scrapeTimeout: 30s
  namespaceSelector:
    matchNames:
      - zero-trust-workload-identity-manager
  selector:
    matchLabels:
      name: zero-trust-workload-identity-manager
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-zero-trust-workload-identity-manager-http.yaml
----
. Create the following `ServiceMonitor` CR if the metrics server is configured to use `https`.

.. Create the `servicemonitor-zero-trust-workload-identity-manager-https.yaml` YAML file:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    name: zero-trust-workload-identity-manager
  name: zero-trust-workload-identity-manager-metrics-monitor
  namespace: zero-trust-workload-identity-manager
spec:
  endpoints:
    - authorization:
        credentials:
          name: zero-trust-workload-identity-manager-metrics-auth
          key: token
        type: Bearer
      interval: 60s
      path: /metrics
      port: metrics-https
      scheme: https
      scrapeTimeout: 30s
      tlsConfig:
        ca:
          configMap:
            name: openshift-service-ca.crt
            key: service-ca.crt
        serverName: zero-trust-workload-identity-manager-metrics-service.zero-trust-workload-identity-manager.svc.cluster.local
  namespaceSelector:
    matchNames:
      - zero-trust-workload-identity-manager
  selector:
    matchLabels:
      name: zero-trust-workload-identity-manager
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-zero-trust-workload-identity-manager-https.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Server. The collected metrics are labeled with `job="zero-trust-workload-identity-manager-metrics-service"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* → *Targets*.

. In the *Label* filter field, enter the following label to filter the metrics targets:
+
[source,terminal]
----
$ service=zero-trust-workload-identity-manager-metrics-service
----

. Confirm that the *Status* column shows `Up` for the `zero-trust-workload-identity-manager` entry.

[role="_additional-resources"]
.Additional resources

* Configuring user workload monitoring

// Querying metrics for the {zero-trust-full}
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-query-metrics_{context}"]
= Querying metrics for the {zero-trust-full}

[role="_abstract"]
Query SPIRE Agent and SPIRE Server metrics using the OpenShift Container Platform web console or the command line. This helps you monitor the performance of SPIRE components that match specific job labels.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

* You have installed the {zero-trust-full}.

* You have deployed the SPIRE Server and SPIRE Agent operands in the cluster.

* You have enabled monitoring and metrics collection by creating `ServiceMonitor` objects.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Metrics*.

. In the query field, enter the following PromQL expression to query SPIRE Server metrics:
+
[source,promql]
----
{job="spire-server"}
----

. In the query field, enter the following PromQL expression to query SPIRE Agent metrics.
+
[source,promql]
----
{job="spire-agent"}
----

[role="_additional-resources"]
.Additional resources

* Accessing metrics

// available metrics
// Module included in the following assemblies:
//
// * security/zer_trust_workload_identity_manager/zero-trust-manager-monitoring.adoc

[id="zero-trust-manager-available-metrics_{context}"]
= {zero-trust-full} monitoring available metrics

[role="_abstract"]
Monitor the health and performance of {zero-trust-full} components by reviewing exposed metrics. This reference describes controller, certificate, and runtime metrics that help you maintain system health and troubleshoot errors.

The {zero-trust-full} exposes the following metrics:

Controller runtime metrics::

* `controller_runtime_active_workers`: Number of currently used workers per controller

* `controller_runtime_max_concurrent_reconciles`: Maximum number of concurrent reconciles per controller

* `controller_runtime_reconcile_errors_total`: Total number of reconciliation errors per controller

* `controller_runtime_reconcile_time_seconds`: Length of time per reconciliation per controller

* `controller_runtime_reconcile_total`: Total number of reconciliations per controller

Certificate watcher metrics::

* `certwatcher_read_certificate_errors_total`: Total number of certificate read errors

* `certwatcher_read_certificate_total`: Total number of certificates read

Go runtime metrics::

Standard Go runtime metrics including:

* `go_gc_duration_seconds`: Garbage collection duration

* `go_goroutines`: Number of goroutines

* `go_memstats_*`: Memory statistics

* `process_*`: Process statistics

 Custom Operator metrics::

The operator also exposes custom metrics related to:

* SPIRE Server status and health

* SPIRE Agent deployment status

* SPIFFE CSI Driver status

* OIDC Discovery Provider status

* Workload identity management operations
