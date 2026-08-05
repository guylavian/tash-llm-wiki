---
title: "Configuring the logging collector"
type: reference
domain: openshift
slug: observability-4-22-6x-cluster-logging-collector-6-0
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/6x-cluster-logging-collector-6.0
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring the logging collector

[id="cluster-logging-collector-6-1"]
= Configuring the logging collector

{logging-title-uc} collects operations and application logs from your cluster and enriches the data with Kubernetes pod and project metadata.
All supported modifications to the log collector are performed though the `spec.collection` stanza in the `ClusterLogForwarder` custom resource (CR).

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="log6x-creating-logfilesmetricexporter_{context}"]
= Creating a LogFileMetricExporter resource

To generate metrics from the logs produced by running containers, you must create a `LogFileMetricExporter` custom resource (CR).

If you do not create the `LogFileMetricExporter` CR, you might see a *No datapoints found* message in the OpenShift Container Platform web console dashboard for *Produced Logs*.

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
<1> Optional: The `nodeSelector` stanza defines which pods are scheduled on which nodes.
<2> The `resources` stanza defines resource requirements for the `LogFileMetricExporter` CR.
<3> Optional: The `tolerations` stanza defines the tolerations that the pods accept.

. Apply the `LogFileMetricExporter` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-collector.adoc

[id="log6x-cluster-logging-collector-limits_{context}"]
= Configure log collector CPU and memory limits

Use the log collector to adjust the CPU and memory limits.

.Procedure

* Edit the `ClusterLogForwarder` custom resource (CR):
+
[source,terminal]
----
$ oc -n openshift-logging edit ClusterLogging instance
----
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  collector:
    resources:
      limits: <1>
        memory: 736Mi
      requests:
        cpu: 100m
        memory: 736Mi
# ...
----
<1> Specify the CPU and memory limits and requests as needed. The values shown are the default values.

[id="cluster-logging-collector-input-receivers_{context}"]
== Configuring input receivers

The {clo} deploys a service for each configured input receiver so that clients can write to the collector. This service exposes the port specified for the input receiver. For log forwarder `ClusterLogForwarder` CR deployments, the service name is in the `<clusterlogforwarder_resource_name>-<input_name>` format.

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="log6x-log-collector-http-server_{context}"]
= Configuring the collector to receive audit logs as an HTTP server

You can configure your log collector to listen for HTTP connections to only receive audit logs by specifying `http` as a receiver input in the `ClusterLogForwarder` custom resource (CR).

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo}.
* You have created a `ClusterLogForwarder` CR.

.Procedure

. Modify the `ClusterLogForwarder` CR to add configuration for the `http` receiver input:
+
--
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  inputs:
  - name: http-receiver # <1>
    type: receiver
    receiver:
      type: http # <2>
      port: 8443 # <3>
      http:
        format: kubeAPIAudit # <4>
  outputs:
  - name: default-lokistack
    lokiStack:
      authentication:
        token:
          from: serviceAccount
      target:
        name: logging-loki
        namespace: openshift-logging
    tls:
      ca:
        key: service-ca.crt
        configMapName: openshift-service-ca.crt
    type: lokiStack
# ...
  pipelines: # <5>
    - name: http-pipeline
      inputRefs:
        - http-receiver
      outputRefs:
        - <output_name>
# ...
----
<1> Specify a name for your input receiver.
<2> Specify the input receiver type as `http`.
<3> Optional: Specify the port that the input receiver listens on. This must be a value between `1024` and `65535`. The default value is `8443`.
<4> Currently, only the `kube-apiserver` webhook format is supported for `http` input receivers.
<5> Configure a pipeline for your input receiver.
--

. Apply the changes to the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

. Verify that the collector is listening on the service that has a name in the  `<clusterlogforwarder_resource_name>-<input_name>` format by running the following command:
+
[source,terminal]
----
$ oc get svc
----
+
.Example output
+
[source,terminal]
----
NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)            AGE
collector                 ClusterIP   172.30.85.239    <none>        24231/TCP          3m6s
collector-http-receiver   ClusterIP   172.30.205.160   <none>        8443/TCP           3m6s
----
+
In this example output, the service name is `collector-http-receiver`.

. Extract the certificate authority (CA) certificate file by running the following command:
+
[source,terminal]
----
$ oc extract cm/openshift-service-ca.crt -n <namespace>
----

. Use the `curl` command to send logs by running the following command:
+
[source,terminal]
----
$ curl --cacert <openshift_service_ca.crt> https://collector-http-receiver.<namespace>.svc:8443 -XPOST -d '{"<prefix>":"<msessage>"}'
----
+
Replace `<openshift_service_ca.crt>` with the extracted CA certificate file.
+
[NOTE]
====
You can only forward logs within a cluster by following the verification steps.
====
// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/cluster-logging-collector.adoc

[id="log-collector-syslog-server_{context}"]
= Configuring the collector to listen for connections as a syslog server

You can configure your log collector to collect journal format infrastructure logs by specifying `syslog` as a receiver input in the `ClusterLogForwarder` custom resource (CR).

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo}.
* You have created a `ClusterLogForwarder` CR.

.Procedure

. Grant the `collect-infrastructure-logs` cluster role to the service account by running the following command:
+
.Example binding command
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-infrastructure-logs -z logcollector
----

. Modify the `ClusterLogForwarder` CR to add configuration for the `syslog` receiver input:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  inputs:
    - name: syslog-receiver # <1>
      type: receiver
      receiver:
        type: syslog # <2>
        port: 10514 # <3>
  outputs:
  - name: default-lokistack
    lokiStack:
      authentication:
        token:
          from: serviceAccount
      target:
        name: logging-loki
        namespace: openshift-logging
    tls:
      ca:
        key: service-ca.crt
        configMapName: openshift-service-ca.crt
    type: lokiStack
# ...
  pipelines: # <4>
    - name: syslog-pipeline
      inputRefs:
        - syslog-receiver
      outputRefs:
        - <output_name>
# ...
----
<1> Specify a name for your input receiver.
<2> Specify the input receiver type as `syslog`.
<3> Optional: Specify the port that the input receiver listens on. This must be a value between `1024` and `65535`.
<4> Configure a pipeline for your input receiver.

. Apply the changes to the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification

* Verify that the collector is listening on the service that has a name in the `<clusterlogforwarder_resource_name>-<input_name>` format by running the following command:
+
[source,terminal]
----
$ oc get svc
----
+
.Example output
+
[source,terminal]
----
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)            AGE
collector                   ClusterIP   172.30.85.239    <none>        24231/TCP          33m
collector-syslog-receiver   ClusterIP   172.30.216.142   <none>        10514/TCP          2m20s
----
+
In this example output, the service name is `collector-syslog-receiver`.
