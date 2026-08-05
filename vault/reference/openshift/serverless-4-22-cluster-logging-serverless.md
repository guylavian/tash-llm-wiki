---
title: "Using OpenShift Logging with {ServerlessProductName}"
type: reference
domain: openshift
slug: serverless-4-22-cluster-logging-serverless
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/cluster-logging-serverless
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Using OpenShift Logging with {ServerlessProductName}

[id="cluster-logging-serverless"]
= Using OpenShift Logging with {ServerlessProductName}

// Module included in the following assemblies:
//
// * virt/support/virt-openshift-cluster-monitoring.adoc
// * observability/logging/cluster-logging.adoc
// * serverless/monitor/cluster-logging-serverless.adoc

[id="cluster-logging-about_{context}"]
= About deploying {logging}

Administrators can deploy the {logging} by using the OpenShift Container Platform web console or the {oc-first} to install the {logging} Operators. The Operators are responsible for deploying, upgrading, and maintaining the {logging}.

Administrators and application developers can view the logs of the projects for which they have view access.

[id="cluster-logging-about-custom-resources_{context}"]
== Logging custom resources

You can configure your {logging} deployment with custom resource (CR) YAML files implemented by each Operator.

*{clo}*:

* `ClusterLogging` (CL) - After the Operators are installed, you create a `ClusterLogging` custom resource (CR) to schedule {logging} pods and other resources necessary to support the {logging}. The `ClusterLogging` CR deploys the collector and forwarder, which currently are both implemented by a daemonset running on each node. The {clo} watches the `ClusterLogging` CR and adjusts the logging deployment accordingly.

* `ClusterLogForwarder` (CLF) - Generates collector configuration to forward logs per user configuration.

*{loki-op}*:

* `LokiStack` - Controls the Loki cluster as log store and the web proxy with OpenShift Container Platform authentication integration to enforce multi-tenancy.

*{es-op}*:

[NOTE]
====
These CRs are generated and managed by the {es-op}. Manual changes cannot be made without being overwritten by the Operator.
====

* `ElasticSearch` - Configure and deploy an Elasticsearch instance as the default log store.

* `Kibana` - Configure and deploy Kibana instance to search, query and view logs.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-deploying-about.adoc
// * serverless/monitor/cluster-logging-serverless.adoc

[id="cluster-logging-deploying-about_{context}"]
= About deploying and configuring {logging}

The {logging} is designed to be used with the default configuration, which is tuned for small to medium sized OpenShift Container Platform clusters.

The installation instructions that follow include a sample `ClusterLogging` custom resource (CR), which you can use to create a {logging} instance and configure your {logging} environment.

If you want to use the default {logging} install, you can use the sample CR directly.

If you want to customize your deployment, make changes to the sample CR as needed. The following describes the configurations you can make when installing your OpenShift Logging instance or modify after installation. See the Configuring sections for more information on working with each component, including modifications you can make outside of the `ClusterLogging` custom resource.

[id="cluster-logging-deploy-about-config_{context}"]
== Configuring and Tuning the {logging}

You can configure your {logging} by modifying the `ClusterLogging` custom resource deployed
in the `openshift-logging` project.

You can modify any of the following components upon install or after install:

Memory and CPU::
You can adjust both the CPU and memory limits for each component by modifying the `resources`
block with valid memory and CPU values:

[source,yaml]
----
spec:
  logStore:
    elasticsearch:
      resources:
        limits:
          cpu:
          memory: 16Gi
        requests:
          cpu: 500m
          memory: 16Gi
      type: "elasticsearch"
  collection:
    logs:
      fluentd:
        resources:
          limits:
            cpu:
            memory:
          requests:
            cpu:
            memory:
        type: "fluentd"
  visualization:
    kibana:
      resources:
        limits:
          cpu:
          memory:
        requests:
          cpu:
          memory:
      type: kibana
----

Elasticsearch storage::
You can configure a persistent storage class and size for the Elasticsearch cluster using the `storageClass` `name` and `size` parameters. The Red Hat OpenShift Logging Operator creates a persistent volume claim (PVC) for each data node in the Elasticsearch cluster based on these parameters.

[source,yaml]
----
  spec:
    logStore:
      type: "elasticsearch"
      elasticsearch:
        nodeCount: 3
        storage:
          storageClassName: "gp2"
          size: "200G"
----

This example specifies each data node in the cluster will be bound to a PVC that
requests "200G" of "gp2" storage. Each primary shard will be backed by a single replica.

[NOTE]
====
Omitting the `storage` block results in a deployment that includes ephemeral storage only.

[source,yaml]
----
  spec:
    logStore:
      type: "elasticsearch"
      elasticsearch:
        nodeCount: 3
        storage: {}
----
====

Elasticsearch replication policy::
You can set the policy that defines how Elasticsearch shards are replicated across data nodes in the cluster:

* `FullRedundancy`. The shards for each index are fully replicated to every data node.
* `MultipleRedundancy`. The shards for each index are spread over half of the data nodes.
* `SingleRedundancy`. A single copy of each shard. Logs are always available and recoverable as long as at least two data nodes exist.
* `ZeroRedundancy`. No copies of any shards. Logs may be unavailable (or lost) in the event a node is down or fails.

Log collectors::
You can select which log collector is deployed as a daemon set to each node in the OpenShift Container Platform cluster, either:

* Fluentd - The default log collector based on Fluentd.
* Rsyslog - Alternate log collector supported as **Tech Preview** only.

----
  spec:
    collection:
      logs:
        fluentd:
          resources:
            limits:
              cpu:
              memory:
            requests:
              cpu:
              memory:
        type: "fluentd"
----

[id="cluster-logging-deploy-about-sample_{context}"]
== Sample modified ClusterLogging custom resource

The following is an example of a `ClusterLogging` custom resource modified using the options previously described.

.Sample modified `ClusterLogging` custom resource
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogging"
metadata:
  name: "instance"
  namespace: "openshift-logging"
spec:
  managementState: "Managed"
  logStore:
    type: "elasticsearch"
    retentionPolicy:
      application:
        maxAge: 1d
      infra:
        maxAge: 7d
      audit:
        maxAge: 7d
    elasticsearch:
      nodeCount: 3
      resources:
        limits:
          memory: 32Gi
        requests:
          cpu: 3
          memory: 32Gi
        storage:
          storageClassName: "gp2"
          size: "200G"
      redundancyPolicy: "SingleRedundancy"
  visualization:
    type: "kibana"
    kibana:
      resources:
        limits:
          memory: 1Gi
        requests:
          cpu: 500m
          memory: 1Gi
      replicas: 1
  collection:
    logs:
      type: "fluentd"
      fluentd:
        resources:
          limits:
            memory: 1Gi
          requests:
            cpu: 200m
            memory: 1Gi
----
