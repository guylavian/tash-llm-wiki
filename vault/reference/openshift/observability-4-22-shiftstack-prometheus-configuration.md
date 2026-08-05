---
title: "Monitoring clusters that run on RHOSO"
type: reference
domain: openshift
slug: observability-4-22-shiftstack-prometheus-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/shiftstack-prometheus-configuration
version: 4.22
family: observability
documentKind: "Documentation"
---

# Monitoring clusters that run on RHOSO

[id="shiftstack-prometheus-configuration"]
= Monitoring clusters that run on RHOSO

You can correlate observability metrics for clusters that run on {rhoso-first}. By collecting metrics from both environments, you can monitor and troubleshoot issues across the infrastructure and application layers.

There are two supported methods for metric correlation for clusters that run on {rhoso}:

- https://prometheus.io/docs/practices/remote_write/#remote-write-tuning[Remote writing] to an external Prometheus instance.
- Collecting data from the OpenShift Container Platform federation endpoint to the {rhoso} observability stack.

// Module included in the following assemblies:
//
// * observability/monitoring/shiftstack-prometheus-configuration.adoc

[id="monitoring-configuring-shiftstack-remotewrite_{context}"]
= Remote writing to an external Prometheus instance

Use remote write with both {rhoso-first} and OpenShift Container Platform to push their metrics to an external Prometheus instance.

.Prerequisites

- You have access to an external Prometheus instance.
- You have administrative access to {rhoso} and your cluster.
- You have certificates for secure communication with mTLS.
- Your Prometheus instance is configured for client TLS certificates and has been set up as a remote write receiver.
- The Cluster Observability Operator is installed on your {rhoso} cluster.
- The monitoring stack for your {rhoso} cluster is configured to collect the metrics that you are interested in.
- Telemetry is enabled in the {rhoso} environment.
+
[NOTE]
====
To verify that the telemetry service is operating normally, entering the following command:
[source,shell]
----
$ oc -n openstack get monitoringstacks metric-storage -o yaml
----
The `monitoringstacks` CRD indicates whether telemetry is enabled correctly.
====

.Procedure

// Steps 1, 2, 3, and 4 run on the OpenShift cluster hosting the RHOSO control plane. This configure RHOSO to send their metrics to an external prometheus.
//
// Steps 5, 6, 7, and 8 run on the tenant's OpenShift cluster. This configures the tenant OpenShift cluster to send their metrics to the same Prometheus instance.
// Comment from before moving telemetry check to prereqs -- offset by 1.

// on mgmt cluster

. Configure your {rhoso} management cluster to send metrics to Prometheus:

.. Create a secret that is named `mtls-bundle` in the `openstack` namespace that contains HTTPS client certificates for authentication to Prometheus by entering the following command:
+
[source,shell]
----
$ oc --namespace openstack \
    create secret generic mtls-bundle \
        --from-file=./ca.crt \
        --from-file=osp-client.crt \
        --from-file=osp-client.key
----

.. Open the `controlplane` configuration for editing by running the following command:
+
[source,shell]
----
$ oc -n openstack edit openstackcontrolplane/controlplane
----

.. With the configuration open, replace the `.spec.telemetry.template.metricStorage` section so that {rhoso} sends metrics to Prometheus. As an example:
+
[source,yaml]
----
      metricStorage:
        customMonitoringStack:
          alertmanagerConfig:
            disabled: false
          logLevel: info
          prometheusConfig:
            scrapeInterval: 30s
            remoteWrite:
            - url: https://external-prometheus.example.com/api/v1/write # <1>
              tlsConfig:
                ca:
                  secret:
                    name: mtls-bundle
                    key: ca.crt
                cert:
                  secret:
                    name: mtls-bundle
                    key: ocp-client.crt
                keySecret:
                  name: mtls-bundle
                  key: ocp-client.key
            replicas: 2
          resourceSelector:
            matchLabels:
              service: metricStorage
          resources:
            limits:
              cpu: 500m
              memory: 512Mi
            requests:
              cpu: 100m
              memory: 256Mi
          retention: 1d # <2>
        dashboardsEnabled: false
        dataplaneNetwork: ctlplane
        enabled: true
        prometheusTls: {}
----
<1> Replace this URL with the URL of your Prometheus instance.
<2> Set a retention period. Optionally, you can reduce retention for local metrics because of external collection.
// run on tenant's openshift cluster
. Configure the tenant cluster on which your workloads run to send metrics to Prometheus:

.. Create a cluster monitoring config map as a YAML file. The map must include a remote write configuration and cluster identifiers. As an example:
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
    prometheusK8s:
      retention: 1d # <1>
      remoteWrite:
      - url: "https://external-prometheus.example.com/api/v1/write"
        writeRelabelConfigs:
        - sourceLabels:
          - __tmp_openshift_cluster_id__
          targetLabel: cluster_id
          action: replace
        tlsConfig:
          ca:
            secret:
              name: mtls-bundle
              key: ca.crt
          cert:
            secret:
              name: mtls-bundle
              key: ocp-client.crt
          keySecret:
            name: mtls-bundle
            key: ocp-client.key
----
<1> Set a retention period. Optionally, you can reduce retention for local metrics because of external collection.

.. Save the config map as a file called `cluster-monitoring-config.yaml`.

.. Create a secret that is named `mtls-bundle` in the `openshift-monitoring` namespace that contains HTTPS client certificates for authentication to Prometheus by entering the following command:
+
[source,terminal]
----
$ oc --namespace openshift-monitoring \
    create secret generic mtls-bundle \
        --from-file=./ca.crt \
        --from-file=ocp-client.crt \
        --from-file=ocp-client.key
----

.. Apply the cluster monitoring configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f cluster-monitoring-config.yaml
----

After the changes propagate, you can see aggregated metrics in your external Prometheus instance.

[role="_additional-resources"]
.Additional resources
* Configuring remote write storage
* Adding cluster ID labels to metrics

// Module included in the following assemblies:
//
// * observability/monitoring/shiftstack-prometheus-configuration.adoc

[id="monitoring-configuring-shiftstack-scraping_{context}"]
= Collecting cluster metrics from the federation endpoint

You can employ the federation endpoint of your OpenShift Container Platform cluster to make metrics available to a {rhoso-first} cluster to practice pull-based monitoring.

.Prerequisites

- You have administrative access to {rhoso} and the tenant cluster that is running on it.
- Telemetry is enabled in the {rhoso} environment.
- The Cluster Observability Operator is installed on your cluster.
- The monitoring stack for your cluster is configured.
- Your cluster has its federation endpoint exposed.

.Procedure

. Connect to your cluster by using a username and password; do not log in by using a `kubeconfig` file that was generated by the installation program.

. To retrieve a token from the OpenShift Container Platform cluster, run the following command on it:
+
[source,terminal]
----
$ oc whoami -t
----

. Make the token available as a secret in the `openstack` namespace in the {rhoso} management cluster by running the following command:
+
[source,terminal]
----
$ oc -n openstack create secret generic ocp-federated --from-literal=token=<the_token_fetched_previously>
----

. To get the Prometheus federation route URL from your OpenShift Container Platform cluster, run the following command:
+
[source,terminal]
----
$ oc -n openshift-monitoring get route prometheus-k8s-federate -ojsonpath={'.status.ingress[].host'}
----

. Write a manifest for a scrape configuration and save it as a file called `cluster-scrape-config.yaml`. As an example:
+
[source,yaml]
----
apiVersion: monitoring.rhobs/v1alpha1
kind: ScrapeConfig
metadata:
  labels:
    service: metricStorage
  name: sos1-federated
  namespace: openstack
spec:
  params:
    'match[]':
    - '{__name__=~"kube_node_info|kube_persistentvolume_info|cluster:master_nodes"}' # <1>
  metricsPath: '/federate'
  authorization:
    type: Bearer
    credentials:
      name: ocp-federated # <2>
      key: token
  scheme: HTTPS # or HTTP
  scrapeInterval: 30s # <3>
  staticConfigs:
  - targets:
    - prometheus-k8s-federate-openshift-monitoring.apps.openshift.example # <4>
----
<1> Add metrics here. In this example, only the metrics `kube_node_info`, `kube_persistentvolume_info`, and `cluster:master_nodes` are requested.
<2> Insert the previously generated secret name here.
<3> Limit scraping to fewer than 1000 samples for each request with a maximum frequency of once every 30 seconds.
<4> Insert the URL you fetched previously here. If the endpoint is HTTPS and uses a custom certificate authority, add a `tlsConfig` section after it.

. While connected to the {rhoso} management cluster, apply the manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f cluster-scrape-config.yaml
----

After the config propagates, the cluster metrics are accessible for querying in the OpenShift Container Platform UI in RHOSO.

[role="_additional-resources"]
.Additional resources
* Querying metrics by using the federation endpoint for Prometheus

// Module included in the following assemblies:
//
// * observability/monitoring/shiftstack-prometheus-configuration.adoc

[id="monitoring-shiftstack-metrics_{context}"]
= Available metrics for clusters that run on RHOSO

To query metrics and identifying resources across the stack, there are helper metrics that establish a correlation between {rhoso-first} infrastructure resources and their representations in the tenant OpenShift Container Platform cluster.

To map nodes with {rhoso} compute instances, in the metric `kube_node_info`:

* `node` is the Kubernetes node name.

* `provider_id` contains the identifier of the corresponding compute service instance.

To map persistent volumes with {rhoso} block storage or shared filesystems shares, in the metric `kube_persistentvolume_info`:

* `persistentvolume` is the volume name.

* `csi_volume_handle` is the block storage volume or share identifier.

By default, the compute machines that back the cluster control plane nodes are created in a server group with a soft anti-affinity policy. As a result, the compute service creates them on separate hypervisors on a best-effort basis. However, if the state of the {rhoso} cluster is not appropriate for this distribution, the machines are created anyway.

In combination with the default soft anti-affinity policy, you can configure an alert that activates when a hypervisor hosts more than one control plane node of a given cluster to highlight the degraded level of high availability.

As an example, this PromQL query returns the number of OpenShift Container Platform master nodes per {rh-openstack} host:

[source,promql]
----
sum by (vm_instance) (
  group by (vm_instance, resource) (ceilometer_cpu)
    / on (resource) group_right(vm_instance) (
      group by (node, resource) (
        label_replace(kube_node_info, "resource", "$1", "system_uuid", "(.+)")
      )
    / on (node) group_left group by (node) (
      cluster:master_nodes
    )
  )
)
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Cluster Observability Operator overview
