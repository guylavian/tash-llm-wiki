---
title: "Log visualization with Kibana"
type: reference
domain: openshift
slug: observability-4-22-logging-kibana
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-kibana
version: 4.22
family: observability
documentKind: "Documentation"
---

# Log visualization with Kibana

[id="logging-kibana"]
= Log visualization with Kibana

If you are using the ElasticSearch log store, you can use the Kibana console to visualize collected log data.

Using Kibana, you can do the following with your data:

* Search and browse the data using the *Discover* tab.
* Chart and map the data using the *Visualize* tab.
* Create and view custom dashboards using the *Dashboard* tab.

Use and configuration of the Kibana interface is beyond the scope of this documentation. For more information about using the interface, see the Kibana documentation.

[NOTE]
====
The audit logs are not stored in the internal OpenShift Container Platform Elasticsearch instance by default. To view the audit logs in Kibana, you must use the Log Forwarding API to configure a pipeline that uses the `default` output for audit logs.
====

// Module included in the following assemblies:
//
// * logging/log_visualizer/logging-kibana.adoc

[id="cluster-logging-visualizer-indices_{context}"]
= Defining Kibana index patterns

An index pattern defines the Elasticsearch indices that you want to visualize. To explore and visualize data in Kibana, you must create an index pattern.

.Prerequisites

* A user must have the `cluster-admin` role, the `cluster-reader` role, or both roles to view the *infra* and *audit* indices in Kibana. The default `kubeadmin` user has proper permissions to view these indices.
+
If you can view the pods and logs in the `default`, `kube-` and `openshift-` projects, you should be able to access these indices. You can use the following command to check if the current user has appropriate permissions:
+
[source,terminal]
----
$ oc auth can-i get pods --subresource log -n <project>
----
+
.Example output
[source,terminal]
----
yes
----
+
[NOTE]
====
The audit logs are not stored in the internal OpenShift Container Platform Elasticsearch instance by default. To view the audit logs in Kibana, you must use the Log Forwarding API to configure a pipeline that uses the `default` output for audit logs.
====

* Elasticsearch documents must be indexed before you can create index patterns. This is done automatically, but it might take a few minutes in a new or updated cluster.

.Procedure

To define index patterns and create visualizations in Kibana:

. In the OpenShift Container Platform console, click the Application Launcher {launch} and select *Logging*.

. Create your Kibana index patterns by clicking *Management* -> *Index Patterns* -> *Create index pattern*:

** Each user must manually create index patterns when logging into Kibana the first time to see logs for their projects. Users must create an index pattern named `app` and use the `@timestamp` time field to view their container logs.

** Each admin user must create index patterns when logged into Kibana the first time for the `app`, `infra`, and `audit` indices using the `@timestamp` time field.

. Create Kibana Visualizations from the new index patterns.
// Module included in the following assemblies:
//
// * logging/viewing/cluster-logging-visualizer.adoc

[id="cluster-logging-visualizer-kibana_{context}"]
= Viewing cluster logs in Kibana

You view cluster logs in the Kibana web console. The methods for viewing and visualizing your data in Kibana that are beyond the scope of this documentation. For more information, refer to the Kibana documentation.

.Prerequisites

* The Red Hat OpenShift Logging and Elasticsearch Operators must be installed.

* Kibana index patterns must exist.

* A user must have the `cluster-admin` role, the `cluster-reader` role, or both roles to view the *infra* and *audit* indices in Kibana. The default `kubeadmin` user has proper permissions to view these indices.
+
If you can view the pods and logs in the `default`, `kube-` and `openshift-` projects, you should be able to access these indices. You can use the following command to check if the current user has appropriate permissions:
+
[source,terminal]
----
$ oc auth can-i get pods --subresource log -n <project>
----
+
.Example output
[source,terminal]
----
yes
----
+
[NOTE]
====
The audit logs are not stored in the internal OpenShift Container Platform Elasticsearch instance by default. To view the audit logs in Kibana, you must use the Log Forwarding API to configure a pipeline that uses the `default` output for audit logs.
====

.Procedure

To view logs in Kibana:

. In the OpenShift Container Platform console, click the Application Launcher {launch} and select *Logging*.

. Log in using the same credentials you use to log in to the OpenShift Container Platform console.
+
The Kibana interface launches.

. In Kibana, click *Discover*.

. Select the index pattern you created from the drop-down menu in the top-left corner: *app*, *audit*, or *infra*.
+
The log data displays as  time-stamped documents.

. Expand one of the time-stamped documents.

. Click the *JSON* tab to display the log entry for that document.
+
.Sample infrastructure log entry in Kibana
[%collapsible]
====
[source,terminal]
----
{
  "_index": "infra-000001",
  "_type": "_doc",
  "_id": "YmJmYTBlNDkZTRmLTliMGQtMjE3NmFiOGUyOWM3",
  "_version": 1,
  "_score": null,
  "_source": {
    "docker": {
      "container_id": "f85fa55bbef7bb783f041066be1e7c267a6b88c4603dfce213e32c1"
    },
    "kubernetes": {
      "container_name": "registry-server",
      "namespace_name": "openshift-marketplace",
      "pod_name": "redhat-marketplace-n64gc",
      "container_image": "registry.redhat.io/redhat/redhat-marketplace-index:v4.7",
      "container_image_id": "registry.redhat.io/redhat/redhat-marketplace-index@sha256:65fc0c45aabb95809e376feb065771ecda9e5e59cc8b3024c4545c168f",
      "pod_id": "8f594ea2-c866-4b5c-a1c8-a50756704b2a",
      "host": "ip-10-0-182-28.us-east-2.compute.internal",
      "master_url": "https://kubernetes.default.svc",
      "namespace_id": "3abab127-7669-4eb3-b9ef-44c04ad68d38",
      "namespace_labels": {
        "openshift_io/cluster-monitoring": "true"
      },
      "flat_labels": [
        "catalogsource_operators_coreos_com/update=redhat-marketplace"
      ]
    },
    "message": "time=\"2020-09-23T20:47:03Z\" level=info msg=\"serving registry\" database=/database/index.db port=50051",
    "level": "unknown",
    "hostname": "ip-10-0-182-28.internal",
    "pipeline_metadata": {
      "collector": {
        "ipaddr4": "10.0.182.28",
        "inputname": "fluent-plugin-systemd",
        "name": "fluentd",
        "received_at": "2020-09-23T20:47:15.007583+00:00",
        "version": "1.7.4 1.6.0"
      }
    },
    "@timestamp": "2020-09-23T20:47:03.422465+00:00",
    "viaq_msg_id": "YmJmYTBlNDktMDMGQtMjE3NmFiOGUyOWM3",
    "openshift": {
      "labels": {
        "logging": "infra"
      }
    }
  },
  "fields": {
    "@timestamp": [
      "2020-09-23T20:47:03.422Z"
    ],
    "pipeline_metadata.collector.received_at": [
      "2020-09-23T20:47:15.007Z"
    ]
  },
  "sort": [
    1600894023422
  ]
}
----
====

[id="logging-kibana-configuring"]
== Configuring Kibana

You can configure using the Kibana console by modifying the `ClusterLogging` custom resource (CR).

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-collector.adoc

[id="cluster-logging-memory-limits_{context}"]
= Configuring CPU and memory limits

The {logging} components allow for adjustments to both the CPU and memory limits.

.Procedure

. Edit the `ClusterLogging` custom resource (CR) in the `openshift-logging` project:
+
[source,terminal]
----
$ oc -n openshift-logging edit ClusterLogging instance
----
+
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogging"
metadata:
  name: "instance"
  namespace: openshift-logging

...

spec:
  managementState: "Managed"
  logStore:
    type: "elasticsearch"
    elasticsearch:
      nodeCount: 3
      resources: <1>
        limits:
          memory: 16Gi
        requests:
          cpu: 200m
          memory: 16Gi
      storage:
        storageClassName: "gp2"
        size: "200G"
      redundancyPolicy: "SingleRedundancy"
  visualization:
    type: "kibana"
    kibana:
      resources: <2>
        limits:
          memory: 1Gi
        requests:
          cpu: 500m
          memory: 1Gi
      proxy:
        resources: <2>
          limits:
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
      replicas: 2
  collection:
    logs:
      type: "fluentd"
      fluentd:
        resources: <3>
          limits:
            memory: 736Mi
          requests:
            cpu: 200m
            memory: 736Mi
----
<1> Specify the CPU and memory limits and requests for the log store as needed. For Elasticsearch, you must adjust both the request value and the limit value.
<2> Specify the CPU and memory limits and requests for the log visualizer as needed.
<3> Specify the CPU and memory limits and requests for the log collector as needed.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-visualizer.adoc

[id="cluster-logging-kibana-scaling_{context}"]
= Scaling redundancy for the log visualizer nodes

You can scale the pod that hosts the log visualizer for redundancy.

.Procedure

. Edit the `ClusterLogging` custom resource (CR) in the `openshift-logging` project:
+
[source,terminal]
----
$ oc -n openshift-logging edit ClusterLogging instance
----
+
[source,yaml]
----
$ oc edit ClusterLogging instance

apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogging"
metadata:
  name: "instance"
  namespace: openshift-logging
....

spec:
  visualization:
    type: "kibana"
    kibana:
      replicas: 1 <1>
----
<1> Specify the number of Kibana nodes.
