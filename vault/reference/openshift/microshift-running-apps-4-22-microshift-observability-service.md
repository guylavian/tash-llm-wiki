---
title: "Using MicroShift Observability"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-observability-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-observability-service
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using MicroShift Observability

[id="microshift-observability-service"]
= Using MicroShift Observability

[role="_abstract"]
{microshift-short} Observability collects and transmits system data for monitoring and analysis. The data includes performance and usage metrics, and error reporting.

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-install_{context}"]
= Installing and enabling {microshift-short} Observability

[role="_abstract"]
You can install {microshift-short} Observability at any time, including during the initial {microshift-short} installation. Observability collects and transmits system data for monitoring and analysis, such as performance and usage metrics and error reporting.

.Procedure
. Install the `microshift-observability` RPM by entering the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-observability
----

. Enable the `microshift-observability` system service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl enable microshift-observability
----

. Start the `microshift-observability` system service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift-observability
----

. Restart {microshift-short} after the initial installation.
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----
+
The installation is successful if there is no output after you start the `microshift-observability` RPM.

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-config_{context}"]
= Configuring {microshift-short} Observability

[role="_abstract"]
You must configure {microshift-short} Observability after it is installed by specifying a valid endpoint. You can specify any OpenTelemetry Protocol (OTLP)-compatible endpoint for each configuration before starting {microshift-short}.

[IMPORTANT]
====
If an endpoint is not specified, {microshift-short} Observability does not start.
====

.Procedure

. Update the `/etc/microshift/observability/opentelemetry-collector.yaml` file to specify an OTLP-compatible endpoint with the following information. The endpoint must link to an IP address or host name, and port number of an OTLP service.
+
.OTLP-compatible endpoint configuration
[source,yaml]
----
# ...
exporters:
  otlp:
    sending_queue:
      storage: file_storage
    endpoint: ${env:OTEL_BACKEND}:4317
    tls:
      insecure: true
# ...
service:
# ...
  telemetry:
    metrics:
      readers:
        - periodic:
            exporter:
              otlp:
                protocol: http/protobuf
                endpoint: http://${env:OTEL_BACKEND}:4318
# ...
----
+
Replace `${env:OTEL_BACKEND}` with the IP address or hostname of the remote back end. This IP address resolves to the local node's hostname. An unreachable endpoint is reported in the {microshift-short} service logs.

. Each time that you update the `opentelemetry-collector.yaml` file, you must restart {microshift-short} Observability to apply the updates.
+
Restart {microshift-short} Observability by entering the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-config-examples_{context}"]
= Selecting a {microshift-short} Observability configuration

[role="_abstract"]
The `opentelemetry-collector.yaml` file includes specific parameters that are used to collect data for monitoring the system resources. All warnings for node events are included in the collected data.

{microshift-short} Observability collects and transmits data for the following resources:

* CPU, memory, disk, and network metrics of containers, pods, and nodes
* Kubernetes events
* Host CPU, memory, disk, and network metrics
* System journals for certain {microshift-short} services, and dependencies
* Metrics exposed by pods that have the `prometheus.io/scrape`: `true` annotation

The amount and complexity of the data depends on predefined configurations. These configurations determine the number of data sources and the amount of collected data that is transmitted. These configurations are defined as `small`, `medium`, and `large`. `Large` is the default configuration.

Replace the values of the `exporters.otlp.endpoint` and `services.telemetry.metrics.readers[0].endpoint` fields with the IP address or hostname of the remote back end. This IP address resolves to the local node's host name. Any unreachable endpoint is reported in the {microshift-short} observability service logs.

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-config-small_{context}"]
= Selecting a small configuration

[role="_abstract"]
You can configure {microshift-short} Observability to collect the smallest amount of performance and resource information from various sources by updating the YAML file.

.Procedure

. Select a small configuration by adding the following information to the `/etc/microshift/observability/opentelemetry-collector.yaml` file:
+
[source,yaml]
----
 receivers:
  kubeletstats:
    auth_type: tls
    ca_file: /var/lib/microshift/certs/ca-bundle/client-ca.crt
    key_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.key
    cert_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.crt
    insecure_skip_verify: true
    collection_interval: 10s
    endpoint: "${env:K8S_NODE_NAME}:10250"
    node: ${env:K8S_NODE_NAME}
    k8s_api_config:
      auth_type: kubeConfig
  k8s_events:
    auth_type: kubeConfig
processors:
  batch:
  resourcedetection/system:
    detectors: [ "system" ]
    system:
      hostname_sources: [ "os" ]
exporters:
  otlp:
    sending_queue:
      storage: file_storage
    endpoint: ${env:OTEL_BACKEND}:4317
    tls:
      insecure: true
extensions:
  file_storage:
    directory: /var/lib/microshift-observability
service:
  extensions: [ file_storage ]
  pipelines:
    metrics/kubeletstats:
      receivers: [ kubeletstats ]
      processors: [ batch ]
      exporters: [ otlp ]
    logs/kube_events:
      receivers: [ k8s_events ]
      processors: [ resourcedetection/system, batch ]
      exporters: [ otlp ]
  telemetry:
    metrics:
      readers:
        - periodic:
            exporter:
              otlp:
                protocol: http/protobuf
                endpoint: http://${env:OTEL_BACKEND}:4318
----
+
Replace the variable `${env:OTEL_BACKEND}` with the IP address or hostname of the remote back end. This IP address resolves to the local node's hostname. Any unreachable endpoint is reported in the {microshift-short} service logs.

. Restart {microshift-short} Observability to complete the configuration selection by entering the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-config-medium_{context}"]
= Selecting a medium configuration

[role="_abstract"]
You can configure {microshift-short} Observability to collect performance and resource information from various sources by updating the YAML file.

.Procedure

. Select a medium configuration by adding the following information to the `/etc/microshift/observability/opentelemetry-collector.yaml` file:
+
[source,yaml]
----
 receivers:
  kubeletstats:
    auth_type: tls
    ca_file: /var/lib/microshift/certs/ca-bundle/client-ca.crt
    key_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.key
    cert_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.crt
    insecure_skip_verify: true
    collection_interval: 10s
    endpoint: "${env:K8S_NODE_NAME}:10250"
    node: ${env:K8S_NODE_NAME}
    k8s_api_config:
      auth_type: kubeConfig
  k8s_events:
    auth_type: kubeConfig
  journald:
    units:
      - microshift
    priority: info
processors:
  batch:
  resourcedetection/system:
    detectors: [ "system" ]
    system:
      hostname_sources: [ "os" ]
exporters:
  otlp:
    sending_queue:
      storage: file_storage
    endpoint: ${env:OTEL_BACKEND}:4317
    tls:
      insecure: true
extensions:
  file_storage:
    directory: /var/lib/microshift-observability
service:
  extensions: [ file_storage ]
  pipelines:
    metrics/kubeletstats:
      receivers: [ kubeletstats ]
      processors: [ batch ]
      exporters: [ otlp ]
    logs/kube_events:
      receivers: [ k8s_events ]
      processors: [ resourcedetection/system, batch ]
      exporters: [ otlp ]
    logs/journald:
      receivers: [ journald ]
      processors: [ resourcedetection/system ]
      exporters: [ otlp ]
  telemetry:
    metrics:
      readers:
        - periodic:
            exporter:
              otlp:
                protocol: http/protobuf
                endpoint: http://${env:OTEL_BACKEND}:4318
----
+
Replace the variable `${env:OTEL_BACKEND}` with the IP address or hostname of the remote back end. This IP address resolves to the local node's hostname. Any unreachable endpoint is reported in the `microshift-observability` service logs.

. Restart {microshift-short} Observability to complete the configuration selection by entering the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-config-large_{context}"]
= Selecting a large configuration

[role="_abstract"]
You can configure {microshift-short} Observability to collect the maximum amount of performance and resource information, from the maximum number of sources, by updating the YAML file.

.Procedure

. Select a large configuration by adding the following information to the `/etc/microshift/observability/opentelemetry-collector.yaml` file. `Large` is the default configuration.
+
[source,yaml]
----
receivers:
  kubeletstats:
    auth_type: tls
    ca_file: /var/lib/microshift/certs/ca-bundle/client-ca.crt
    key_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.key
    cert_file: /var/lib/microshift/certs/admin-kubeconfig-signer/openshift-observability-client/client.crt
    insecure_skip_verify: true
    collection_interval: 10s
    endpoint: "${env:K8S_NODE_NAME}:10250"
    node: ${env:K8S_NODE_NAME}
    k8s_api_config:
      auth_type: kubeConfig
  k8s_events:
    auth_type: kubeConfig
  hostmetrics:
    root_path: /
    collection_interval: 10s
    scrapers:
      cpu:
      memory:
      network:
      disk:
      filesystem:
  journald:
    units:
      - microshift
      - microshift-observability
      - microshift-etcd
      - crio
      - openvswitch.service
      - ovsdb-server.service
      - ovs-vswitchd.service
    priority: info
  prometheus:
    config:
      scrape_configs:
        - job_name: k8s
          scrape_interval: 10s
          kubernetes_sd_configs:
            - kubeconfig_file: /var/lib/microshift/resources/observability-client/kubeconfig
              role: pod
          relabel_configs:
              # Only scrape Pods with annotation "prometheus.io/scrape": "true"
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
              action: keep
              regex: true
              # Use value of "prometheus.io/path" annotation for scraping
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
              action: replace
              target_label: __metrics_path__
              regex: (.+)
              # Use value of "prometheus.io/port" annotation for scraping
            - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
              action: replace
              regex: ([^:]+)(?::\d+)?;(\d+)
              replacement: $1:$2
              target_label: __address__
processors:
  batch:
  resourcedetection/system:
    detectors: [ "system" ]
    system:
      hostname_sources: [ "os" ]
exporters:
  otlp:
    sending_queue:
      storage: file_storage
    endpoint: ${env:OTEL_BACKEND}:4317
    tls:
      insecure: true
extensions:
  file_storage:
    directory: /var/lib/microshift-observability
service:
  extensions: [ file_storage ]
  pipelines:
    metrics/kubeletstats:
      receivers: [ kubeletstats ]
      processors: [ batch ]
      exporters: [ otlp ]
    metrics/hostmetrics:
      receivers: [ hostmetrics ]
      processors: [ resourcedetection/system, batch ]
      exporters: [ otlp ]
    logs/kube_events:
      receivers: [ k8s_events ]
      processors: [ resourcedetection/system, batch ]
      exporters: [ otlp ]
    logs/host:
      receivers: [ hostmetrics ]
      processors: [ resourcedetection/system ]
      exporters: [ otlp ]
    logs/journald:
      receivers: [ journald ]
      processors: [ resourcedetection/system ]
      exporters: [ otlp ]
    metrics/pods:
      receivers: [ prometheus ]
      processors: [ batch ]
      exporters: [ otlp ]
  telemetry:
    metrics:
      readers:
        - periodic:
            exporter:
              otlp:
                protocol: http/protobuf
                endpoint: http://${env:OTEL_BACKEND}:4318
----
+
Replace the variable `${env:OTEL_BACKEND}` with the IP address or hostname of the remote back end. This IP address resolves to the local node's hostname. Any unreachable endpoint is reported in the `microshift-observability` service logs.

. Restart {microshift-short} Observability to complete the configuration selection by entering the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----

// Module included in the following assemblies:
//
// microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-verify_{context}"]
= Verifying the {microshift-short} Observability state

[role="_abstract"]
After {microshift-short} Observability starts, you can verify the state by using a `systemd` service. The {microshift-short} Observability service logs are available as `journald` logs.

.Procedure

. Check the {microshift-short} Observability status by entering the following command:
+
[source,terminal]
----
$ sudo systemctl status microshift-observability
----

. Check the {microshift-short} Observability logs by entering the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift-observability
----
