---
title: "Monitoring {cert-manager-operator}"
type: reference
domain: openshift
slug: security-4-22-cert-manager-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-monitoring
version: 4.22
family: security
documentKind: "Documentation"
---

# Monitoring {cert-manager-operator}

[id="cert-manager-monitoring"]
= Monitoring {cert-manager-operator}

[role="_abstract"]
By default, the {cert-manager-operator} exposes metrics for the three core components: controller, cainjector, and webhook. You can configure OpenShift Monitoring to collect these metrics by using the Prometheus Operator format.

// Enabling user workload monitoring for the cert-manager operand
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-monitoring.adoc

[id="cert-manager-enable-user-workload-monitor_{context}"]
= Enabling user workload monitoring

[role="_abstract"]
To collect metrics from your specific applications, enable monitoring for user-defined projects. You can enable monitoring for user-defined projects by configuring user workload monitoring in the cluster. For more information, see "Setting up metrics collection for user-defined projects".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Create the `cluster-monitoring-config.yaml` YAML file:
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

. Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace by running the following command:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pod
----
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
prometheus-operator-6cb6bd9588-dtzxq   2/2     Running   0          50s
prometheus-user-workload-0             6/6     Running   0          48s
prometheus-user-workload-1             6/6     Running   0          48s
thanos-ruler-user-workload-0           4/4     Running   0          42s
thanos-ruler-user-workload-1           4/4     Running   0          42s
----
+
The status of the pods such as `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` must be `Running`.

[role="_additional-resources"]
.Additional resources
* Setting up metrics collection for user-defined projects

// Metrics scraping for cert-manager operands by using a ServiceMonitor
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-monitoring.adoc

[id="cert-manager-enable-metrics_{context}"]
= Configuring metrics collection for {cert-manager-operator} operands by using a ServiceMonitor

[role="_abstract"]]
The {cert-manager-operator} operands expose metrics by default on port `9402` at the `/metrics` service endpoint. You can configure metrics collection for the cert-manager operands by creating a `ServiceMonitor` custom resource (CR) that enables Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {cert-manager-operator}.
* You have enabled the user workload monitoring.

.Procedure

. Create the `ServiceMonitor` CR:

.. Create the YAML file that defines the `ServiceMonitor` CR:
+
.Example `servicemonitor-cert-manager.yaml` file
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: cert-manager
    app.kubernetes.io/instance: cert-manager
    app.kubernetes.io/name: cert-manager
  name: cert-manager
  namespace: cert-manager
spec:
  endpoints:
    - honorLabels: false
      interval: 60s
      path: /metrics
      scrapeTimeout: 30s
      targetPort: 9402
  selector:
    matchExpressions:
      - key: app.kubernetes.io/name
        operator: In
        values:
          - cainjector
          - cert-manager
          - webhook
      - key: app.kubernetes.io/instance
        operator: In
        values:
          - cert-manager
      - key: app.kubernetes.io/component
        operator: In
        values:
          - cainjector
          - controller
          - webhook
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-cert-manager.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the {cert-manager-operator} operands. The collected metrics are labeled with `job="cert-manager"`,`job="cert-manager-cainjector"`, and `job="cert-manager-webhook"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* → *Targets*.

. In the *Label* filter field, enter the following labels to filter the metrics targets for each operand:
+
[source,terminal]
----
$ service=cert-manager
----
+
[source,terminal]
----
$ service=cert-manager-webhook
----
+
[source,terminal]
----
$ service=cert-manager-cainjector
----

. Confirm that the *Status* column shows `Up` for the `cert-manager`, `cert-manager-webhook`, and `cert-manager-cainjector` entries.

[role="_additional-resources"]
.Additional resources

* Configuring user workload monitoring

// Querying metrics for the cert-manager operands
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-monitoring.adoc

[id="cert-manager-query-metrics_{context}"]
= Querying metrics for the {cert-manager-operator} operands

[role="_abstract"]
As a cluster administrator, or as a user with view access to all namespaces, you can query {cert-manager-operator} operands metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {cert-manager-operator}.
* You have enabled monitoring and metrics collection by creating `ServiceMonitor` object.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Observe* → *Metrics*.

. In the query field, enter the following PromQL expressions to query the {cert-manager-operator} operands metric for each operand:
+
[source,promql]
----
{job="cert-manager"}
----
+
[source,promql]
----
{job="cert-manager-webhook"}
----
+
[source,promql]
----
{job="cert-manager-cainjector"}
----

[role="_additional-resources"]
.Additional resources

* Accessing metrics as an administrator

// Configuring metrics collection for cert-manager Operator for Red Hat OpenShift istio-csr operand by using a ServiceMonitor
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-monitoring.adoc

[id="cert-manager-config-metrics-collection_{context}"]
= Configuring metrics collection for the istio-csr operand

[role="_abstract"]
The `istio-csr` operand exposes metrics by default on port `9402` at the `/metrics` service endpoint. You can configure metrics collection for the operand by creating a `ServiceMonitor` custom resource (CR), which enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed the {cert-manager-operator}.
* You have enabled user workload monitoring.

.Procedure

. Create the `ServiceMonitor` CR definition file:
+
.Example `servicemonitor-istio-csr.yaml` file
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: cert-manager-istio-csr
    app.kubernetes.io/instance: cert-manager-istio-csr
    app.kubernetes.io/name: cert-manager-istio-csr
  name: cert-manager-istio-csr
  namespace: <istio_csr_project_name>
spec:
  endpoints:
    - honorLabels: false
      interval: 60s
      path: /metrics
      scrapeTimeout: 30s
      targetPort: 9402
  namespaceSelector:
    matchNames:
      - <istio_csr_project_name>
  selector:
    matchLabels:
      app: cert-manager-istio-csr
      app.kubernetes.io/instance: cert-manager-istio-csr
      app.kubernetes.io/name: cert-manager-istio-csr
----
+
Replace `<istio_csr_project_name>` with the namespace where you created the `IstioCSR` CR.

. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-istio-csr.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance starts collecting metrics from the istio-csr operand. The collected metrics are labeled with `job="cert-manager-istio-csr"`.

.Verification

. Log in to the OpenShift Container Platform web console.
. Click *Observe* -> *Targets*.
. In the **Label filter** field, enter the `service=cert-manager-istio-csr` label to filter the metrics targets.
. Confirm that the *Status* column shows *Up* for the `cert-manager-istio-csr` target.

[role="_additional-resources"]
.Additional resources

* Configuring user workload monitoring

// Querying metrics for the istio-csr operand
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-monitoring.adoc

[id="cert-manager-query-metrics-for-istio-csr-operand_{context}"]
= Querying metrics for the istio-csr operand

[role="_abstract"]
Cluster administrators, or users with view access to all namespaces, can query metrics for the istio-csr operand by using the OpenShift Container Platform web console. For more information, see "Accessing metrics".

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have installed the {cert-manager-operator}.
* You have enabled monitoring and metrics collection by creating the `ServiceMonitor` object for the istio-csr operand.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Click *Observe* -> *Metrics*.
. In the query field, enter the `{job="cert-manager-istio-csr"}` PromQL expression to query the `istio-csr` operand metrics. The results display metrics collected for the istio-csr operand, which can help you monitor its performance and behavior.

[role="_additional-resources"]
.Additional resources

* Accessing metrics as an administrator
