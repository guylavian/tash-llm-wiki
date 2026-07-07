---
title: "Monitoring the External Secrets Operator for Red Hat OpenShift"
type: reference
domain: openshift
slug: security-4-22-external-secrets-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-monitoring
version: 4.22
family: security
documentKind: "Documentation"
---

# Monitoring the External Secrets Operator for Red Hat OpenShift

[id="external-secrets-monitoring"]
= Monitoring the External Secrets Operator for Red Hat OpenShift

[role="_abstract"]
By default, the {external-secrets-operator} exposes metrics for the Operator and the operands. You can configure OpenShift Monitoring to collect these metrics by using the Prometheus Operator format.

// Enabling user workload monitoring for the external-secrets-operator operand
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-monitoring.adoc

[id="external-secrets-enable-user-workload-monitor_{context}"]
= Enabling user workload monitoring

[role="_abstract"]
By default, the OpenShift Container Platform monitoring stack does not scrape metrics from user-installed applications like the External Secrets Operator. Enabling user workload monitoring is necessary to collect critical operational data, such as synchronization status, API error rates, and controller performance. This helps you to configure custom alerts for secret sync failures and create dashboards to monitor the overall health of your secret management system. You can enable monitoring for user-defined projects by configuring user workload monitoring in the cluster. For more information, see "Setting up metrics collection for user-defined projects".

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

* Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace by running the following command:
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
prometheus-operator-5f79cff9c9-67pjb   2/2     Running   0          25h
prometheus-user-workload-0             6/6     Running   0          25h
thanos-ruler-user-workload-0           4/4     Running   0          25h
----
+
The status of the pods such as `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` must be `Running`.

[role="_additional-resources"]
.Additional resources
* Setting up metrics collection for user-defined projects

// Metrics scraping for external-secrets-operator
// Module included in the following assemblies:
//
// * security/external_secrets_operator/exteernal-secrets-monitoring.adoc

[id="external-secrets-enable-operator-metrics_{context}"]
= Configuring metrics collection for {external-secrets-operator} by using a ServiceMonitor

[role="_abstract"]
The {external-secrets-operator} exposes metrics by default on port `8443` at the `/metrics` service endpoint. You can configure metrics collection for the Operator by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {external-secrets-operator}.
* You have enabled the user workload monitoring.

.Procedure

. Configure the Operator to use `HTTP` for the metrics server. `HTTPS` is enabled by default.

.. Update the subscription object for {external-secrets-operator} to configure the `HTTP` protocol by running the following command:
+
[source,terminal]
----
$ oc -n external-secrets-operator patch subscription openshift-external-secrets-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"METRICS_BIND_ADDRESS","value":":8080"}, {"name": "METRICS_SECURE", "value": "false"}]}}}'
----

.. To verify that the {external-secrets-operator-short} pod is redeployed and that the configured values for `METRICS_BIND_ADDRESS` and `METRICS_SECURE` are updated, run the following command:
+
[source,terminal]
----
$ oc set env --list deployment/external-secrets-operator-controller-manager -n external-secrets-operator | grep -e METRICS_BIND_ADDRESS -e METRICS_SECURE -e container
----
+
The following example shows that the `METRICS_BIND_ADDRESS` and `METRICS_SECURE` have been updated:
+
[source,terminal]
----
# deployments/external-secrets-operator-controller-manager, container manager
METRICS_BIND_ADDRESS=:8080
METRICS_SECURE=false
----

. Create the `Secret` resource with the `kubernetes.io/service-account.name` annotation to inject the token required for authenticating with the metrics server.

.. Create the `secret-external-secrets-operator.yaml` YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  labels:
    app: external-secrets-operator
  name: external-secrets-operator-metrics-auth
  namespace: external-secrets-operator
  annotations:
    kubernetes.io/service-account.name: external-secrets-operator-controller-manager
type: kubernetes.io/service-account-token
----

.. Create the `Secret` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f secret-external-secrets-operator.yaml
----

. Create the `ClusterRoleBinding` resource required for granting permissions to access metrics:

.. Create the `clusterrolebinding-external-secrets.yaml` YAML file:
+
The following example shows a `clusterrolebinding-external-secrets.yaml` file.
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    app: external-secrets-operator
  name: external-secrets-allow-metrics-access
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-secrets-operator-metrics-reader
subjects:
  - kind: ServiceAccount
    name: external-secrets-operator-controller-manager
    namespace: external-secrets-operator
----

.. Create the `ClusterRoldeBinding` custom resource by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterrolebinding-external-secrets.yaml
----

. Create the `ServiceMonitor` CR if using the default `HTTPS`:

.. Create the `servicemonitor-external-secrets-operator-https.yaml` YAML file:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: external-secrets-operator
  name: external-secrets-operator-metrics-monitor
  namespace: external-secrets-operator
spec:
  endpoints:
    - authorization:
        credentials:
          name: external-secrets-operator-metrics-auth
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
        serverName: external-secrets-operator-controller-manager-metrics-service.external-secrets-operator.svc.cluster.local
  namespaceSelector:
    matchNames:
      - external-secrets-operator
  selector:
    matchLabels:
      app: external-secrets-operator
      svc: external-secrets-operator-controller-manager-metrics-service
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-external-secrets-operator-https.yaml
----

. Create the `ServiceMonitor` CR if configured to use `HTTP`:

.. Create the `servicemonitor-external-secrets-operator-http.yaml` YAML file:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: external-secrets-operator
  name: external-secrets-operator-metrics-monitor
  namespace: external-secrets-operator
spec:
  endpoints:
    - authorization:
        credentials:
          name: external-secrets-operator-metrics-auth
          key: token
        type: Bearer
      interval: 60s
      path: /metrics
      port: metrics-http
      scheme: http
      scrapeTimeout: 30s
  namespaceSelector:
    matchNames:
      - external-secrets-operator
  selector:
    matchLabels:
      app: external-secrets-operator
      svc: external-secrets-operator-controller-manager-metrics-service
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-external-secrets-operator-http.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the Operator. The collected metrics are labeled with `job="external-secrets-operator-controller-manager-metrics-service"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Targets*.

. In the Label filter field, enter the following labels to filter the metrics targets for each operand:
+
[source,terminal]
----
$ service=external-secrets-operator-controller-manager-metrics-service
----

. Confirm that the *Status* column shows `Up` for the `external-secrets-operator`.

[role="_additional-resources"]
.Additional resources

* Configurable monitoring components

// Querying metrics for the external-secrets operator
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-monitoring.adoc

[id="external-secrets-query-operator-metrics_{context}"]
= Querying metrics for the {external-secrets-operator}

[role="_abstract"]
As a cluster administrator, or as a user with view access to all namespaces, you can query the Operator metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {external-secrets-operator}.
* You have enabled monitoring and metrics collection by creating a `ServiceMonitor` object.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Metrics*.

. In the query field, enter the following PromQL expressions to query the {external-secrets-operator} metric:
+
[source,promql]
----
{job="external-secrets-operator-controller-manager-metrics-service"}
----

[role="_additional-resources"]
.Additional resources

* Accessing metrics

// Metrics scraping for external-secrets operands by using a ServiceMonitor
// Module included in the following assemblies:
//
// * security/external_secrets_operator/exteernal-secrets-monitoring.adoc

[id="external-secrets-enable-metrics_{context}"]
= Configuring metrics collection for {external-secrets-operator} operands by using a ServiceMonitor

[role="_abstract"]
The {external-secrets-operator} operands exposes metrics by default on port `8080` at the `/metrics` service endpoint for all three components (`external-secrets`, `external-secrets-cert-controll`, and `external-secrets-webhook`). You can configure metrics collection for the external-secrets operands by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {external-secrets-operator}.
* You have enabled the user workload monitoring.

.Procedure

. Create the `ClusterRoleBinding` resource required for granting permissions to access metrics:

.. Create the `clusterrolebinding-external-secrets.yaml` YAML file:
+
The following example shows a `clusterrolebinding-external-secrets.yaml` file.
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    app: external-secrets
  name: external-secrets-allow-metrics-access
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-secrets-operator-metrics-reader
subjects:
  - kind: ServiceAccount
    name: external-secrets
    namespace: external-secrets
  - kind: ServiceAccount
    name: external-secrets-cert-controller
    namespace: external-secrets
  - kind: ServiceAccount
    name: external-secrets-webhook
    namespace: external-secrets
----

.. Create the `ClusterRoldeBinding` custom resource by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterrolebinding-external-secrets.yaml
----

. Create the `ServiceMonitor` CR:

.. Create the `servicemonitor-external-secrets.yaml` YAML file:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: external-secrets
  name: external-secrets-metrics-monitor
  namespace: external-secrets
spec:
  endpoints:
    - interval: 60s
      path: /metrics
      port: metrics
      scheme: http
      scrapeTimeout: 30s
  namespaceSelector:
    matchNames:
      - external-secrets
  selector:
    matchExpressions:
      - key: app.kubernetes.io/name
        operator: In
        values:
          - external-secrets
          - external-secrets-cert-controller
          - external-secrets-webhook
      - key: app.kubernetes.io/instance
        operator: In
        values:
          - external-secrets
      - key: app.kubernetes.io/managed-by
        operator: In
        values:
          - external-secrets-operator
----

.. Create the `ServiceMonitor` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f servicemonitor-external-secrets.yaml
----
+
After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the {external-secrets-operator} operands. The collected metrics are labeled with `job="external-secrets"`,`job="external-secrets-cainjector"`, and `job="external-secrets-webhook"`.

.Verification

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Targets*.

. In the Label filter field, enter the following labels to filter the metrics targets for each operand:
+
[source,terminal]
----
$ service=external-secrets
----
+
[source,terminal]
----
$ service=external-secrets-cert-controller-metrics
----
+
[source,terminal]
----
$ service=external-secrets-webhook
----

. Confirm that the *Status* column shows `Up` for the `external-secrets`, `external-secrets-cert-controller` and `external-secrets-webhook`.

[role="_additional-resources"]
.Additional resources

* Configuring user workload monitoring

// Querying metrics for the external-secrets operands
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-monitoring.adoc

[id="external-secrets-query-metrics_{context}"]
= Querying metrics for the external-secrets operand

[role="_abstract"]
As a cluster administrator, or as a user with view access to all namespaces, you can query `external-secrets` operand metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {external-secrets-operator}.
* You have enabled monitoring and metrics collection by creating a `ServiceMonitor` object.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Metrics*.

. In the query field, enter the following PromQL expressions to query the {external-secrets-operator} operands metric for each operand:
+
[source,promql]
----
{job="external-secrets"}
----
+
[source,promql]
----
{job="external-secrets-webhook"}
----
+
[source,promql]
----
{job="external-secrets-cert-controller-metrics"}
----

[role="_additional-resources"]
.Additional resources

* Accessing metrics
