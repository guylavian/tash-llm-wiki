---
title: "About log visualization"
type: reference
domain: openshift
slug: observability-4-22-log-visualization
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log-visualization
version: 4.22
family: observability
documentKind: "Documentation"
---

# About log visualization

[id="log-visualization"]
= About log visualization

You can visualize your log data in the OpenShift Container Platform web console, or the Kibana web console, depending on your deployed log storage solution. The Kibana console can be used with ElasticSearch log stores, and the OpenShift Container Platform web console can be used with the ElasticSearch log store or the LokiStack.

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization.adoc
// * observability/logging/cluster-logging-deploying.adoc

[id="configuring-log-visualizer_{context}"]
= Configuring the log visualizer

You can configure which log visualizer type your {logging} uses by modifying the `ClusterLogging` custom resource (CR).

.Prerequisites

* You have administrator permissions.
* You have installed the {oc-first}.
* You have installed the {clo}.
* You have created a `ClusterLogging` CR.

[IMPORTANT]
====
If you want to use the OpenShift Container Platform web console for visualization, you must enable the {log-plug}. See the documentation about "Log visualization with the web console".
====

.Procedure

. Modify the `ClusterLogging` CR `visualization` spec:
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
  visualization:
    type: <visualizer_type> <1>
    kibana: <2>
      resources: {}
      nodeSelector: {}
      proxy: {}
      replicas: {}
      tolerations: {}
    ocpConsole: <3>
      logsLimit: {}
      timeout: {}
# ...
----
<1> The type of visualizer you want to use for your {logging}. This can be either `kibana` or `ocp-console`. The Kibana console is only compatible with deployments that use Elasticsearch log storage, while the OpenShift Container Platform console is only compatible with LokiStack deployments.
<2> Optional configurations for the Kibana console.
<3> Optional configurations for the OpenShift Container Platform web console.

. Apply the `ClusterLogging` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

[id="log-visualization-resource-logs"]
== Viewing logs for a resource

Resource logs are a default feature that provides limited log viewing capability. You can view the logs for various resources, such as builds, deployments, and pods by using the {oc-first} and the web console.

[TIP]
====
To enhance your log retrieving and viewing experience, install the {logging}. The {logging} aggregates all the logs from your OpenShift Container Platform cluster, such as node system audit logs, application container logs, and infrastructure logs, into a dedicated log store. You can then query, discover, and visualize your log data through the Kibana console or the OpenShift Container Platform web console. Resource logs do not access the {logging} log store.
====

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization.adoc
// * nodes/pods/nodes-pods-viewing.adoc

[id="viewing-resource-logs-cli-console_{context}"]
= Viewing resource logs

[role="_abstract"]
You can view logs for resources in the {oc-first} or web console. By viewing logs for resources, you can troubleshoot issues and monitor resource behavior.

Logs display from the end (or tail) by default.
