---
title: "Configuring CPU and memory limits for {logging} components"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-memory
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-memory
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring CPU and memory limits for {logging} components

[id="cluster-logging-memory"]
= Configuring CPU and memory limits for {logging} components

You can configure both the CPU and memory limits for each of the {logging} components as needed.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

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
