---
title: "Troubleshooting monitoring issues"
type: reference
domain: openshift
slug: observability-4-22-troubleshooting-monitoring-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/troubleshooting-monitoring-issues
version: 4.22
family: observability
documentKind: "Documentation"
---

# Troubleshooting monitoring issues

[id="troubleshooting-monitoring-issues"]
= Troubleshooting monitoring issues

Find troubleshooting steps for common issues with core platform and user-defined project monitoring.
Find troubleshooting steps for common issues with user-defined project monitoring.

// Investigating why user-defined project metrics are unavailable (OCP/ROSA HCP)
// Module included in the following assemblies:
//
// * observability/monitoring/troubleshooting-monitoring-issues.adoc
// * support/troubleshooting/investigating-monitoring-issues.adoc

[id="investigating-why-user-defined-metrics-are-unavailable_{context}"]
= Investigating why user-defined project metrics are unavailable

[role="_abstract"]
`ServiceMonitor` resources enable you to determine how to use the metrics exposed by a service in user-defined projects. Follow the steps outlined in this procedure if you have created a `ServiceMonitor` resource but cannot see any corresponding metrics in the Metrics UI.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the {oc-first}.
* You have enabled and configured monitoring for user-defined projects.
* You have created a `ServiceMonitor` resource.

.Procedure

. Ensure that your project and resources are not excluded from user workload monitoring. The following examples use the `ns1` project.

.. Verify that the project _does not_ have the `openshift.io/user-monitoring=false` label attached:
+
[source,terminal]
----
$ oc get namespace ns1 --show-labels | grep 'openshift.io/user-monitoring=false'
----
+
[NOTE]
====
The default label set for user workload projects is `openshift.io/user-monitoring=true`. However, the label is not visible unless you manually apply it.
====

.. Verify that the `ServiceMonitor` and `PodMonitor` resources _do not_ have the `openshift.io/user-monitoring=false` label attached. The following example checks the `prometheus-example-monitor` service monitor.
+
[source,terminal]
----
$ oc -n ns1 get servicemonitor prometheus-example-monitor --show-labels | grep 'openshift.io/user-monitoring=false'
----

.. If the label is attached, remove the label:
+
.Example of removing the label from the project
[source,terminal]
----
$ oc label namespace ns1 'openshift.io/user-monitoring-'
----
+
.Example of removing the label from the resource
[source,terminal]
----
$ oc -n ns1 label servicemonitor prometheus-example-monitor 'openshift.io/user-monitoring-'
----
+
.Example output
[source,terminal]
----
namespace/ns1 unlabeled
----

. Check that the corresponding labels match in the service and `ServiceMonitor` resource configurations. The following examples use the `prometheus-example-app` service, the `prometheus-example-monitor` service monitor, and the `ns1` project.
.. Obtain the label defined in the service.
+
[source,terminal]
----
$ oc -n ns1 get service prometheus-example-app -o yaml
----
+
.Example output
[source,terminal]
----
  labels:
    app: prometheus-example-app
----
+
.. Check that the `matchLabels` definition in the `ServiceMonitor` resource configuration matches the label output in the previous step.
+
[source,terminal]
----
$ oc -n ns1 get servicemonitor prometheus-example-monitor -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
kind: ServiceMonitor
metadata:
  name: prometheus-example-monitor
  namespace: ns1
spec:
  endpoints:
  - interval: 30s
    port: web
    scheme: http
  selector:
    matchLabels:
      app: prometheus-example-app
----
+
[NOTE]
====
You can check service and `ServiceMonitor` resource labels as a developer with view permissions for the project.
====

. Inspect the logs for the Prometheus Operator in the `openshift-user-workload-monitoring` project.
.. List the pods in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pods
----
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
prometheus-operator-776fcbbd56-2nbfm   2/2     Running   0          132m
prometheus-user-workload-0             5/5     Running   1          132m
prometheus-user-workload-1             5/5     Running   1          132m
thanos-ruler-user-workload-0           3/3     Running   0          132m
thanos-ruler-user-workload-1           3/3     Running   0          132m
----
+
.. Obtain the logs from the `prometheus-operator` container in the `prometheus-operator` pod. In the following example, the pod is called `prometheus-operator-776fcbbd56-2nbfm`:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring logs prometheus-operator-776fcbbd56-2nbfm -c prometheus-operator
----
+
If there is a issue with the service monitor, the logs might include an error similar to this example:
+
[source,terminal]
----
level=warn ts=2020-08-10T11:48:20.906739623Z caller=operator.go:1829 component=prometheusoperator msg="skipping servicemonitor" error="it accesses file system via bearer token file which Prometheus specification prohibits" servicemonitor=eagle/eagle namespace=openshift-user-workload-monitoring prometheus=user-workload
----

. Review the target status for your endpoint on the *Metrics targets* page in the OpenShift Container Platform web console UI.
.. Log in to the OpenShift Container Platform web console and go to *Observe* → *Targets*.

.. Locate the metrics endpoint in the list, and review the status of the target in the *Status* column.

.. If the *Status* is *Down*, click the URL for the endpoint to view more information on the *Target Details* page for that metrics target.

. Configure debug level logging for the Prometheus Operator in the `openshift-user-workload-monitoring` project.
.. Edit the `user-workload-monitoring-config` `ConfigMap` object in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring edit configmap user-workload-monitoring-config
----
+
.. Add `logLevel: debug` for `prometheusOperator` under `data/config.yaml` to set the log level to `debug`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-workload-monitoring-config
  namespace: openshift-user-workload-monitoring
data:
  config.yaml: |
    prometheusOperator:
      logLevel: debug
# ...
----
+
.. Save the file to apply the changes. The affected `prometheus-operator` pod is automatically redeployed.
+
.. Confirm that the `debug` log-level has been applied to the `prometheus-operator` deployment in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get deploy prometheus-operator -o yaml |  grep "log-level"
----
+
.Example output
[source,terminal]
----
        - --log-level=debug
----
+
Debug level logging will show all calls made by the Prometheus Operator.
+
.. Check that the `prometheus-operator` pod is running:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pods
----
+
[NOTE]
====
If an unrecognized Prometheus Operator `loglevel` value is included in the config map, the `prometheus-operator` pod might not restart successfully.
====
+
.. Review the debug logs to see if the Prometheus Operator is using the `ServiceMonitor` resource. Review the logs for other related errors.

[role="_additional-resources"]
.Additional resources

* Enabling monitoring for user-defined projects
* Specifying how a service is monitored
* Getting detailed information about a metrics target

// Investigating why user-defined project metrics are unavailable (OSD/ROSA Classic)

// Module included in the following assemblies:
//
// * observability/monitoring/troubleshooting-monitoring-issues.adoc

[id="troubleshooting-monitoring-issues_{context}"]
= Determining why user-defined project metrics are unavailable

[role="_abstract"]
If metrics are not displaying when monitoring user-defined projects, follow these steps to troubleshoot the issue.

.Procedure

. Query the metric name and verify that the project is correct:
.. In the *Developer* perspective of the web console, click *Observe* and go to the *Metrics* tab.
.. Select the project that you want to view metrics for in the *Project:* list.
.. Select an existing query from the *Select query* list, or run a custom query by adding a PromQL query to the *Expression* field.
+
The metrics are displayed in a chart.
+
Queries must be done on a per-project basis. The metrics that are shown relate to the project that you have selected.
. Verify that the pod that you want metrics from is actively serving metrics. Run the following `oc exec` command into a pod to target the `podIP`, `port`, and `/metrics`.
+
[source,terminal]
----
$ oc exec <sample_pod> -n <sample_namespace> -- curl <target_pod_IP>:<port>/metrics
----
+
[NOTE]
====
You must run the command on a pod that has `curl` installed.
====
+
The following example output shows a result with a valid version metric.
+
.Example output
[source,terminal]
----
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
# HELP version Version information about this binary-- --:--:-- --:--:--     0
# TYPE version gauge
version{version="v0.1.0"} 1
100   102  100   102    0     0  51000      0 --:--:-- --:--:-- --:--:-- 51000
----
+
An invalid output indicates that there is a problem with the corresponding application.

. If you are using a `PodMonitor` CRD, verify that the `PodMonitor` CRD is configured to point to the correct pods using label matching. For more information, see the Prometheus Operator documentation.
. If you are using a `ServiceMonitor` CRD, and if the `/metrics` endpoint of the pod is showing metric data, follow these steps to verify the configuration:
.. Verify that the service is pointed to the correct `/metrics` endpoint. The service `labels` in this output must match the services monitor `labels` and the `/metrics` endpoint defined by the service in the subsequent steps.
+
[source,terminal]
----
$ oc get service
----
+
.Example output
[source,terminal]
----
apiVersion: v1
kind: Service
metadata:
  labels:
    app: prometheus-example-app
  name: prometheus-example-app
  namespace: ns1
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
    name: web
  selector:
    app: prometheus-example-app
  type: ClusterIP
----
+
--
where:

`kind`:: Specifies an API type. This example shows a service API.
`metadata.labels`:: Specifies the labels that are used for this service.
--

.. Query the `serviceIP`, `port`, and `/metrics` endpoints to see if the same metrics from the `curl` command you ran on the pod previously:
... Run the following command to find the service IP:
+
[source,terminal]
----
$ oc get service -n <target_namespace>
----
... Query the `/metrics` endpoint:
+
[source,terminal]
----
$ oc exec <sample_pod> -n <sample_namespace> -- curl <service_IP>:<port>/metrics
----
+
Valid metrics are returned in the following example.
+
.Example output
[source,terminal]
----
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                               Dload  Upload   Total   Spent    Left  Speed
100   102  100   102    0     0  51000      0 --:--:-- --:--:-- --:--:--   99k
# HELP version Version information about this binary
# TYPE version gauge
version{version="v0.1.0"} 1
----
.. Use label matching to verify that the `ServiceMonitor` object is configured to point to the required service. To do this, compare the `Service` object from the `oc get service` output to the `ServiceMonitor` object from the `oc get servicemonitor` output. The labels must match for the metrics to be displayed.
+
For example, from the previous steps, notice how the `Service` object has the `app: prometheus-example-app` label and the `ServiceMonitor` object has the same `app: prometheus-example-app` match label.
. If the configuration is valid and metrics remain unavailable, contact the support team.

// Determining why Prometheus is consuming a lot of disk space
// Module included in the following assemblies:
//
// * observability/monitoring/troubleshooting-monitoring-issues.adoc
// * support/troubleshooting/investigating-monitoring-issues.adoc

[id="determining-why-prometheus-is-consuming-disk-space_{context}"]
= Determining why Prometheus is consuming a lot of disk space

[role="_abstract"]
Developers can create labels to define attributes for metrics in the form of key-value pairs. The number of potential key-value pairs corresponds to the number of possible values for an attribute. An attribute that has an unlimited number of potential values is called an unbound attribute. For example, a `customer_id` attribute is unbound because it has an infinite number of possible values.

Every assigned key-value pair has a unique time series. The use of many unbound attributes in labels can result in an exponential increase in the number of time series created. This can impact Prometheus performance and can consume a lot of disk space.

You can use the following measures when Prometheus consumes a lot of disk:

* *Check the time series database (TSDB) status using the Prometheus HTTP API* for more information about which labels are creating the most time series data. Doing so requires cluster administrator privileges.

* *Check the number of scrape samples* that are being collected.

* *Reduce the number of unique time series that are created* by reducing the number of unbound attributes that are assigned to user-defined metrics.
+
[NOTE]
====
Using attributes that are bound to a limited set of possible values reduces the number of potential key-value pair combinations.
====
+
* *Enforce limits on the number of samples that can be scraped* across user-defined projects. This requires cluster administrator privileges.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the {oc-first}.

.Procedure

. In the OpenShift Container Platform web console, go to *Observe* -> *Metrics*.

. Enter a Prometheus Query Language (PromQL) query in the *Expression* field.
The following example queries help to identify high cardinality metrics that might result in high disk space consumption:

* By running the following query, you can identify the ten jobs that have the highest number of scrape samples:
+
[source,text]
----
topk(10, max by(namespace, job) (topk by(namespace, job) (1, scrape_samples_post_metric_relabeling)))
----
+
* By running the following query, you can pinpoint time series churn by identifying the ten jobs that have created the most time series data in the last hour:
+
[source,text]
----
topk(10, sum by(namespace, job) (sum_over_time(scrape_series_added[1h])))
----

. Investigate the number of unbound label values assigned to metrics with higher than expected scrape sample counts:

* *If the metrics relate to a user-defined project*, review the metrics key-value pairs assigned to your workload. These are implemented through Prometheus client libraries at the application level. Try to limit the number of unbound attributes referenced in your labels.

* *If the metrics relate to a core OpenShift Container Platform project*, create a Red Hat support case on the Red Hat Customer Portal.

. Review the TSDB status using the Prometheus HTTP API by following these steps when logged in as a
cluster administrator:
`dedicated-admin`:
+
.. Get the Prometheus API route URL by running the following command:
+
[source,terminal]
----
$ HOST=$(oc -n openshift-monitoring get route prometheus-k8s -ojsonpath='{.status.ingress[].host}')
----
+
.. Extract an authentication token by running the following command:
+
[source,terminal]
----
$ TOKEN=$(oc whoami -t)
----
+
.. Query the TSDB status for Prometheus by running the following command:
+
[source,terminal]
----
$ curl -H "Authorization: Bearer $TOKEN" -k "https://$HOST/api/v1/status/tsdb"
----
+
.Example output
[source,terminal]
----
"status": "success","data":{"headStats":{"numSeries":507473,
"numLabelPairs":19832,"chunkCount":946298,"minTime":1712253600010,
"maxTime":1712257935346},"seriesCountByMetricName":
[{"name":"etcd_request_duration_seconds_bucket","value":51840},
{"name":"apiserver_request_sli_duration_seconds_bucket","value":47718},
...
----

[role="_additional-resources"]
.Additional resources

* Accessing monitoring APIs by using the CLI
* Setting scrape intervals, evaluation intervals, and enforced limits for user-defined projects
* Submitting a support case

// Resolving the KubePersistentVolumeFillingUp alert firing for Prometheus
// Module included in the following assemblies:
//
// * monitoring/troubleshooting-monitoring-issues.adoc
// * support/troubleshooting/investigating-monitoring-issues.adoc

[id="resolving-the-kubepersistentvolumefillingup-alert-firing-for-prometheus_{context}"]
= Resolving the KubePersistentVolumeFillingUp alert firing for Prometheus

[role="_abstract"]
As a cluster administrator, you can resolve the `KubePersistentVolumeFillingUp` alert being triggered for Prometheus.

The critical alert fires when a persistent volume (PV) claimed by a `prometheus-k8s-*` pod in the `openshift-monitoring` project has less than 3% total space remaining. This can cause Prometheus to function abnormally.

[NOTE]
====
There are two `KubePersistentVolumeFillingUp` alerts:

* *Critical alert*:  The alert with the `severity="critical"` label is triggered when the mounted PV has less than 3% total space remaining.
* *Warning alert*: The alert with the `severity="warning"` label is triggered when the mounted PV has less than 15% total space remaining and is expected to fill up within four days.
====

To address this issue, you can remove Prometheus time-series database (TSDB) blocks to create more space for the PV.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the {oc-first}.

.Procedure

. List the size of all TSDB blocks, sorted from oldest to newest, by running the following command:
+
[source,terminal]
----
$ oc debug <prometheus_k8s_pod_name> -n openshift-monitoring \
-c prometheus --image=$(oc get po -n openshift-monitoring <prometheus_k8s_pod_name> \
-o jsonpath='{.spec.containers[?(@.name=="prometheus")].image}') \
-- sh -c 'cd /prometheus/;du -hs $(ls -dtr */ | grep -Eo "[0-9|A-Z]{26}")'
----
+
Replace `<prometheus_k8s_pod_name>` with the pod mentioned in the `KubePersistentVolumeFillingUp` alert description.
+
.Example output
[source,terminal]
----
308M    01HVKMPKQWZYWS8WVDAYQHNMW6
52M     01HVK64DTDA81799TBR9QDECEZ
102M    01HVK64DS7TRZRWF2756KHST5X
140M    01HVJS59K11FBVAPVY57K88Z11
90M     01HVH2A5Z58SKT810EM6B9AT50
152M    01HV8ZDVQMX41MKCN84S32RRZ1
354M    01HV6Q2N26BK63G4RYTST71FBF
156M    01HV664H9J9Z1FTZD73RD1563E
216M    01HTHXB60A7F239HN7S2TENPNS
104M    01HTHMGRXGS0WXA3WATRXHR36B
----

. Identify which and how many blocks could be removed, then remove the blocks. The following example command removes the three oldest Prometheus TSDB blocks from the `prometheus-k8s-0` pod:
+
[source,terminal]
----
$ oc debug prometheus-k8s-0 -n openshift-monitoring \
-c prometheus --image=$(oc get po -n openshift-monitoring prometheus-k8s-0 \
-o jsonpath='{.spec.containers[?(@.name=="prometheus")].image}') \
-- sh -c 'ls -latr /prometheus/ | egrep -o "[0-9|A-Z]{26}" | head -3 | \
while read BLOCK; do rm -r /prometheus/$BLOCK; done'
----

. Verify the usage of the mounted PV and ensure there is enough space available by running the following command:
+
[source,terminal]
----
$ oc debug <prometheus_k8s_pod_name> -n openshift-monitoring \
--image=$(oc get po -n openshift-monitoring <prometheus_k8s_pod_name> \
-o jsonpath='{.spec.containers[?(@.name=="prometheus")].image}') -- df -h /prometheus/
----
+
Replace `<prometheus_k8s_pod_name>` with the pod mentioned in the `KubePersistentVolumeFillingUp` alert description.
+
The following example output shows the mounted PV claimed by the `prometheus-k8s-0` pod that has 63% of space remaining:
+
.Example output
[source,terminal]
----
Starting pod/prometheus-k8s-0-debug-j82w4 ...
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p4  40G   15G  40G  37% /prometheus

Removing debug pod ...
----

// Resolving the AlertmanagerReceiversNotConfigured alert firing for Prometheus
// Module included in the following assemblies:
//
// * monitoring/troubleshooting-monitoring-issues.adoc

[id="resolving-the-alertmanagerreceiversnotconfigured-alert_{context}"]
= Resolving the AlertmanagerReceiversNotConfigured alert

Every cluster that is deployed has the `AlertmanagerReceiversNotConfigured` alert firing by default. To resolve the issue, you must configure alert receivers.

* For default platform monitoring, follow the steps in "Configuring alert notifications" in _Configuring core platform monitoring_.

* For user workload monitoring, follow the steps in "Configuring alert notifications" in _Configuring user workload monitoring_.

[role="_additional-resources"]
.Additional resources
* Configuring alert notifications for default platform monitoring
* Configuring alert notifications for user workload monitoring
