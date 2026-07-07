---
title: "Configuring the logging collector"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-collector-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-collector
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring the logging collector

[id="cluster-logging-collector"]
= Configuring the logging collector

{logging-title-uc} collects operations and application logs from your cluster and enriches the data with Kubernetes pod and project metadata.
All supported modifications to the log collector can be performed though the `spec.collection` stanza in the `ClusterLogging` custom resource (CR).

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying.adoc
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="configuring-logging-collector_{context}"]
= Configuring the log collector

You can configure which log collector type your {logging} uses by modifying the `ClusterLogging` custom resource (CR).

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo}.
* You have created a `ClusterLogging` CR.

.Procedure

. Modify the `ClusterLogging` CR `collection` spec:
+
.`ClusterLogging` CR example
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
# ...
spec:
# ...
  collection:
    type: <log_collector_type> <1>
    resources: {}
    tolerations: {}
# ...
----
<1> The log collector type you want to use for the {logging}. This can be `vector` or `fluentd`.

. Apply the `ClusterLogging` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="creating-logfilesmetricexporter_{context}"]
= Creating a LogFileMetricExporter resource

In {logging} version 5.8 and newer versions, the LogFileMetricExporter is no longer deployed with the collector by default. You must manually create a `LogFileMetricExporter` custom resource (CR) to generate metrics from the logs produced by running containers.

If you do not create the `LogFileMetricExporter` CR, you may see a *No datapoints found* message in the OpenShift Container Platform web console dashboard for *Produced Logs*.

.Prerequisites

* You have administrator permissions.
* You have installed the {clo}.
* You have installed the {oc-first}.

.Procedure

. Create a `LogFileMetricExporter` CR as a YAML file:
+
.Example `LogFileMetricExporter` CR
[source,yaml]
----
apiVersion: logging.openshift.io/v1alpha1
kind: LogFileMetricExporter
metadata:
  name: instance
  namespace: openshift-logging
spec:
  nodeSelector: {} # <1>
  resources: # <2>
    limits:
      cpu: 500m
      memory: 256Mi
    requests:
      cpu: 200m
      memory: 128Mi
  tolerations: [] # <3>
# ...
----
<1> Optional: The `nodeSelector` stanza defines which nodes the pods are scheduled on.
<2> The `resources` stanza defines resource requirements for the `LogFileMetricExporter` CR.
<3> Optional: The `tolerations` stanza defines the tolerations that the pods accept.

. Apply the `LogFileMetricExporter` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

A `logfilesmetricexporter` pod runs concurrently with a `collector` pod on each node.

* Verify that the `logfilesmetricexporter` pods are running in the namespace where you have created the `LogFileMetricExporter` CR, by running the following command and observing the output:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/component=logfilesmetricexporter -n openshift-logging
----
+
.Example output
[source,terminal]
----
NAME                           READY   STATUS    RESTARTS   AGE
logfilesmetricexporter-9qbjj   1/1     Running   0          2m46s
logfilesmetricexporter-cbc4v   1/1     Running   0          2m46s
----

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-collector.adoc

[id="cluster-logging-collector-limits_{context}"]
= Configure log collector CPU and memory limits

The log collector allows for adjustments to both the CPU and memory limits.

.Procedure

* Edit the `ClusterLogging` custom resource (CR) in the `openshift-logging` project:
+
[source,terminal]
----
$ oc -n openshift-logging edit ClusterLogging instance
----
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance
  namespace: openshift-logging
spec:
  collection:
    type: fluentd
    resources:
      limits: <1>
        memory: 736Mi
      requests:
        cpu: 100m
        memory: 736Mi
# ...
----
<1> Specify the CPU and memory limits and requests as needed. The values shown are the default values.

[source,yaml]
----
$ oc edit ClusterLogging instance

apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogging"
metadata:
  name: "instance"

....

spec:
  collection:
    logs:
      rsyslog:
        resources:
          limits: <1>
            memory: 358Mi
          requests:
            cpu: 100m
            memory: 358Mi
----
<1> Specify the CPU and memory limits and requests as needed. The values shown are the default values.

[id="cluster-logging-collector-input-receivers_{context}"]
== Configuring input receivers

The {clo} deploys a service for each configured input receiver so that clients can write to the collector. This service exposes the port specified for the input receiver.
The service name is generated as follows:

* For multi log forwarder `ClusterLogForwarder` CR deployments, the service name is in the `<clusterlogforwarder_resource_name>-<input_name>` format, for example, `example-http-receiver`.
* For legacy `ClusterLogForwarder` CR deployments named `instance` and that are located in the `openshift-logging` namespace, the service name is in the `collector-<input_name>` format, for example, `collector-http-receiver`.

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

//This file is for Logging 5.x

[id="log-collector-http-server_{context}"]
= Configuring the collector to receive audit logs as an HTTP server

You can configure your log collector to listen for HTTP connections and receive audit logs as an HTTP server by specifying `http` as a receiver input in the `ClusterLogForwarder` custom resource (CR). This enables you to use a common log store for audit logs that are collected from both inside and outside of your OpenShift Container Platform cluster.

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo}.
* You have created a `ClusterLogForwarder` CR.

.Procedure

. Modify the `ClusterLogForwarder` CR to add configuration for the `http` receiver input:
+
--
.Example `ClusterLogForwarder` CR if you are using a multi log forwarder deployment
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccountName: <service_account_name>
  inputs:
    - name: http-receiver # <1>
      receiver:
        type: http # <2>
        http:
          format: kubeAPIAudit # <3>
          port: 8443 # <4>
  pipelines: # <5>
    - name: http-pipeline
      inputRefs:
        - http-receiver
# ...
----
<1> Specify a name for your input receiver.
<2> Specify the input receiver type as `http`.
<3> Currently, only the `kube-apiserver` webhook format is supported for `http` input receivers.
<4> Optional: Specify the port that the input receiver listens on. This must be a value between `1024` and `65535`. The default value is `8443` if this is not specified.
<5> Configure a pipeline for your input receiver.
--
+
--
.Example `ClusterLogForwarder` CR if you are using a legacy deployment
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  inputs:
    - name: http-receiver # <1>
      receiver:
        type: http # <2>
        http:
          format: kubeAPIAudit # <3>
          port: 8443 # <4>
  pipelines: # <5>
  - inputRefs:
    - http-receiver
    name: http-pipeline
# ...
----
<1> Specify a name for your input receiver.
<2> Specify the input receiver type as `http`.
<3> Currently, only the `kube-apiserver` webhook format is supported for `http` input receivers.
<4> Optional: Specify the port that the input receiver listens on. This must be a value between `1024` and `65535`. The default value is `8443` if this is not specified.
<5> Configure a pipeline for your input receiver.
--

. Apply the changes to the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
//include::modules/log-collector-rsyslog-server.adoc[leveloffset=+2]
// uncomment for 5.9 release

[role="_additional-resources"]
.Additional resources
* Overview of API audit filter

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="cluster-logging-collector-tuning_{context}"]
= Advanced configuration for the Fluentd log forwarder

{logging-uc} includes multiple Fluentd parameters that you can use for tuning the performance of the Fluentd log forwarder. With these parameters, you can change the following Fluentd behaviors:

* Chunk and chunk buffer sizes
* Chunk flushing behavior
* Chunk forwarding retry behavior

Fluentd collects log data in a single blob called a _chunk_. When Fluentd creates a chunk, the chunk is considered to be in the _stage_, where the chunk gets filled with data. When the chunk is full, Fluentd moves the chunk to the _queue_, where chunks are held before being flushed, or written out to their destination. Fluentd can fail to flush a chunk for a number of reasons, such as network issues or capacity issues at the destination. If a chunk cannot be flushed, Fluentd retries flushing as configured.

By default in OpenShift Container Platform, Fluentd uses the _exponential backoff_ method to retry flushing, where Fluentd doubles the time it waits between attempts to retry flushing again, which helps reduce connection requests to the destination. You can disable exponential backoff and use the _periodic_ retry method instead, which retries flushing the chunks at a specified interval.

These parameters can help you determine the trade-offs between latency and throughput.

* To optimize Fluentd for throughput, you could use these parameters to reduce network packet count by configuring larger buffers and queues, delaying flushes, and setting longer times between retries. Be aware that larger buffers require more space on the node file system.

* To optimize for low latency, you could use the parameters to send data as soon as possible, avoid the build-up of batches, have shorter queues and buffers, and use more frequent flush and retries.

You can configure the chunking and flushing behavior using the following parameters in the `ClusterLogging` custom resource (CR). The parameters are then automatically added to the Fluentd config map for use by Fluentd.

[NOTE]
====
These parameters are:

* Not relevant to most users. The default settings should give good general performance.
* Only for advanced users with detailed knowledge of Fluentd configuration and performance.
* Only for performance tuning. They have no effect on functional aspects of logging.
====

.Advanced Fluentd Configuration Parameters
[options="header"]
|===

|Parameter |Description |Default

|`chunkLimitSize`
|The maximum size of each chunk. Fluentd stops writing data to a chunk when it reaches this size. Then, Fluentd sends the chunk to the queue and opens a new chunk.
|`8m`

|`totalLimitSize`
|The maximum size of the buffer, which is the total size of the stage and the queue. If the buffer size exceeds this value, Fluentd stops adding data to chunks and fails with an error. All data not in chunks is lost.
|Approximately 15% of the node disk distributed across all outputs.

|`flushInterval`
|The interval between chunk flushes. You can use `s` (seconds), `m` (minutes), `h` (hours), or `d` (days).
|`1s`

|`flushMode`
a| The method to perform flushes:

* `lazy`: Flush chunks based on the `timekey` parameter. You cannot modify the `timekey` parameter.
* `interval`: Flush chunks based on the `flushInterval` parameter.
* `immediate`: Flush chunks immediately after data is added to a chunk.
|`interval`

|`flushThreadCount`
|The number of threads that perform chunk flushing. Increasing the number of threads improves the flush throughput, which hides network latency.
|`2`

|`overflowAction`
a|The chunking behavior when the queue is full:

* `throw_exception`: Raise an exception to show in the log.
* `block`: Stop data chunking until the full buffer issue is resolved.
* `drop_oldest_chunk`: Drop the oldest chunk to accept new incoming chunks. Older chunks have less value than newer chunks.
|`block`

|`retryMaxInterval`
|The maximum time in seconds for the `exponential_backoff` retry method.
|`300s`

|`retryType`
a|The retry method when flushing fails:

* `exponential_backoff`: Increase the time between flush retries. Fluentd doubles the time it waits until the next retry until the `retry_max_interval` parameter is reached.
* `periodic`: Retries flushes periodically, based on the `retryWait` parameter.
|`exponential_backoff`

|`retryTimeOut`
|The maximum time interval to attempt retries before the record is discarded.
|`60m`

|`retryWait`
|The time in seconds before the next chunk flush.
|`1s`

|===

For more information on the Fluentd chunk lifecycle, see Buffer Plugins in the Fluentd documentation.

.Procedure

. Edit the `ClusterLogging` custom resource (CR) in the `openshift-logging` project:
+
[source,terminal]
+
----
$ oc edit ClusterLogging instance
----

. Add or modify any of the following parameters:
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance
  namespace: openshift-logging
spec:
  collection:
    fluentd:
      buffer:
        chunkLimitSize: 8m <1>
        flushInterval: 5s <2>
        flushMode: interval <3>
        flushThreadCount: 3 <4>
        overflowAction: throw_exception <5>
        retryMaxInterval: "300s" <6>
        retryType: periodic <7>
        retryWait: 1s <8>
        totalLimitSize: 32m <9>
# ...
----
<1> Specify the maximum size of each chunk before it is queued for flushing.
<2> Specify the interval between chunk flushes.
<3> Specify the method to perform chunk flushes: `lazy`, `interval`, or `immediate`.
<4> Specify the number of threads to use for chunk flushes.
<5> Specify the chunking behavior when the queue is full: `throw_exception`, `block`, or `drop_oldest_chunk`.
<6> Specify the maximum interval in seconds for the `exponential_backoff` chunk flushing method.
<7> Specify the retry type when chunk flushing fails: `exponential_backoff` or `periodic`.
<8> Specify the time in seconds before the next chunk flush.
<9> Specify the maximum size of the chunk buffer.

. Verify that the Fluentd pods are redeployed:
+
[source,terminal]
----
$ oc get pods -l component=collector -n openshift-logging
----

. Check that the new values are in the `fluentd` config map:
+
[source,terminal]
----
$ oc extract configmap/collector-config --confirm
----
+
.Example fluentd.conf
[source,terminal]
----
<buffer>
  @type file
  path '/var/lib/fluentd/default'
  flush_mode interval
  flush_interval 5s
  flush_thread_count 3
  retry_type periodic
  retry_wait 1s
  retry_max_interval 300s
  retry_timeout 60m
  queued_chunks_limit_size "#{ENV['BUFFER_QUEUE_LIMIT'] || '32'}"
  total_limit_size "#{ENV['TOTAL_LIMIT_SIZE_PER_BUFFER'] || '8589934592'}"
  chunk_limit_size 8m
  overflow_action throw_exception
  disable_chunk_backup true
</buffer>
----
