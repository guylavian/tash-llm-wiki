---
title: "Troubleshooting logging alerts"
type: reference
domain: openshift
slug: observability-4-22-troubleshooting-logging-alerts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/troubleshooting-logging-alerts
version: 4.22
family: observability
documentKind: "Documentation"
---

# Troubleshooting logging alerts

[id="troubleshooting-logging-alerts"]
= Troubleshooting logging alerts

You can use the following procedures to troubleshoot logging alerts on your cluster.

// Module included in the following assemblies:
//
// * observability/logging/troubleshooting/troubleshooting-logging-alerts.adoc

[id="es-cluster-health-is-red_{context}"]
= Elasticsearch cluster health status is red

At least one primary shard and its replicas are not allocated to a node. Use the following procedure to troubleshoot this alert.

.Procedure

. Check the Elasticsearch cluster health and verify that the cluster `status` is red by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME -- health
----

. List the nodes that have joined the cluster by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cat/nodes?v
----

. List the Elasticsearch pods and compare them with the nodes in the command output from the previous step, by running the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get pods -l component=elasticsearch
----

. If some of the Elasticsearch nodes have not joined the cluster, perform the following steps.

.. Confirm that Elasticsearch has an elected master node by running the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cat/master?v
----

.. Review the pod logs of the elected master node for issues by running the following command and observing the output:
+
[source,terminal]
----
$ oc logs <elasticsearch_master_pod_name> -c elasticsearch -n openshift-logging
----

.. Review the logs of nodes that have not joined the cluster for issues by running the following command and observing the output:
+
[source,terminal]
----
$ oc logs <elasticsearch_node_name> -c elasticsearch -n openshift-logging
----

. If all the nodes have joined the cluster, check if the cluster is in the process of recovering by running the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cat/recovery?active_only=true
----
+
If there is no command output, the recovery process might be delayed or stalled by pending tasks.

. Check if there are pending tasks by running the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- health | grep number_of_pending_tasks
----

. If there are pending tasks, monitor their status. If their status changes and indicates that the cluster is recovering, continue waiting. The recovery time varies according to the size of the cluster and other factors. Otherwise, if the status of the pending tasks does not change, this indicates that the recovery has stalled.

. If it seems like the recovery has stalled, check if the `cluster.routing.allocation.enable` value is set to `none`, by running the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cluster/settings?pretty
----

. If the `cluster.routing.allocation.enable` value is set to `none`, set it to `all`, by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cluster/settings?pretty \
  -X PUT -d '{"persistent": {"cluster.routing.allocation.enable":"all"}}'
----

. Check if any indices are still red by running the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cat/indices?v
----

. If any indices are still red, try to clear them by performing the following steps.

.. Clear the cache by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name>/_cache/clear?pretty
----

.. Increase the max allocation retries by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name>/_settings?pretty \
  -X PUT -d '{"index.allocation.max_retries":10}'
----

.. Delete all the scroll items by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_search/scroll/_all -X DELETE
----

.. Increase the timeout by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name>/_settings?pretty \
  -X PUT -d '{"index.unassigned.node_left.delayed_timeout":"10m"}'
----

. If the preceding steps do not clear the red indices, delete the indices individually.

.. Identify the red index name by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cat/indices?v
----

.. Delete the red index by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_red_index_name> -X DELETE
----

. If there are no red indices and the cluster status is red, check for a continuous heavy processing load on a data node.

.. Check if the Elasticsearch JVM Heap usage is high by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_nodes/stats?pretty
----
+
In the command output, review the `node_name.jvm.mem.heap_used_percent` field to determine the JVM Heap usage.

.. Check for high CPU utilization. For more information about CPU utilitzation, see the OpenShift Container Platform "Reviewing monitoring dashboards" documentation.

[role="_additional-resources"]
.Additional resources
* Reviewing monitoring dashboards as a cluster administrator
* Fix a red or yellow cluster status

[id="elasticsearch-cluster-health-is-yellow"]
== Elasticsearch cluster health status is yellow

Replica shards for at least one primary shard are not allocated to nodes. Increase the node count by adjusting the `nodeCount` value in the `ClusterLogging` custom resource (CR).

[role="_additional-resources"]
.Additional resources
* Fix a red or yellow cluster status

// Module included in the following assemblies:
//
// * observability/logging/troubleshooting/troubleshooting-logging-alerts.adoc

[id="es-node-disk-low-watermark-reached_{context}"]
= Elasticsearch node disk low watermark reached

Elasticsearch does not allocate shards to nodes that reach the low watermark.

.Procedure

. Identify the node on which Elasticsearch is deployed by running the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get po -o wide
----

. Check if there are unassigned shards by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cluster/health?pretty | grep unassigned_shards
----

. If there are unassigned shards, check the disk space on each node, by running the following command:
+
[source,terminal]
----
$ for pod in `oc -n openshift-logging get po -l component=elasticsearch -o jsonpath='{.items[*].metadata.name}'`; \
  do echo $pod; oc -n openshift-logging exec -c elasticsearch $pod \
  -- df -h /elasticsearch/persistent; done
----

. In the command output, check the `Use` column to determine the used disk percentage on that node.
+
.Example output
[source,terminal]
----
elasticsearch-cdm-kcrsda6l-1-586cc95d4f-h8zq8
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-2-5b548fc7b-cwwk7
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme2n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-3-5dfc884d99-59tjw
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme3n1     19G  528M   19G   3% /elasticsearch/persistent
----
+
If the used disk percentage is above 85%, the node has exceeded the low watermark, and shards can no longer be allocated to this node.

. To check the current `redundancyPolicy`, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get es elasticsearch \
  -o jsonpath='{.spec.redundancyPolicy}'
----
+
If you are using a `ClusterLogging` resource on your cluster, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get cl \
  -o jsonpath='{.items[*].spec.logStore.elasticsearch.redundancyPolicy}'
----
+
If the cluster `redundancyPolicy` value is higher than the `SingleRedundancy` value, set it to the `SingleRedundancy` value and save this change.

. If the preceding steps do not fix the issue, delete the old indices.
.. Check the status of all indices on Elasticsearch by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME -- indices
----

.. Identify an old index that can be deleted.
.. Delete the index by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name> -X DELETE
----
// Module included in the following assemblies:
//
// * observability/logging/troubleshooting/troubleshooting-logging-alerts.adoc

[id="es-node-disk-high-watermark-reached_{context}"]
= Elasticsearch node disk high watermark reached

Elasticsearch attempts to relocate shards away from a node that has reached the high watermark to a node with low disk usage that has not crossed any watermark threshold limits.

To allocate shards to a particular node, you must free up some space on that node. If increasing the disk space is not possible, try adding a new data node to the cluster, or decrease the total cluster redundancy policy.

.Procedure

. Identify the node on which Elasticsearch is deployed by running the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get po -o wide
----

. Check the disk space on each node:
+
[source,terminal]
----
$ for pod in `oc -n openshift-logging get po -l component=elasticsearch -o jsonpath='{.items[*].metadata.name}'`; \
  do echo $pod; oc -n openshift-logging exec -c elasticsearch $pod \
  -- df -h /elasticsearch/persistent; done
----

. Check if the cluster is rebalancing:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_cluster/health?pretty | grep relocating_shards
----
+
If the command output shows relocating shards, the high watermark has been exceeded. The default value of the high watermark is 90%.

. Increase the disk space on all nodes. If increasing the disk space is not possible, try adding a new data node to the cluster, or decrease the total cluster redundancy policy.

. To check the current `redundancyPolicy`, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get es elasticsearch \
  -o jsonpath='{.spec.redundancyPolicy}'
----
+
If you are using a `ClusterLogging` resource on your cluster, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get cl \
  -o jsonpath='{.items[*].spec.logStore.elasticsearch.redundancyPolicy}'
----
+
If the cluster `redundancyPolicy` value is higher than the `SingleRedundancy` value, set it to the `SingleRedundancy` value and save this change.

. If the preceding steps do not fix the issue, delete the old indices.
.. Check the status of all indices on Elasticsearch by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME -- indices
----

.. Identify an old index that can be deleted.
.. Delete the index by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name> -X DELETE
----
// Module included in the following assemblies:
//
// * observability/logging/troubleshooting/troubleshooting-logging-alerts.adoc

[id="es-node-disk-flood-watermark-reached_{context}"]
= Elasticsearch node disk flood watermark reached

Elasticsearch enforces a read-only index block on every index that has both of these conditions:

* One or more shards are allocated to the node.
* One or more disks exceed the https://www.elastic.co/guide/en/elasticsearch/reference/6.8/disk-allocator.html[flood stage].

Use the following procedure to troubleshoot this alert.

.Procedure

. Get the disk space of the Elasticsearch node:
+
[source,terminal]
----
$ for pod in `oc -n openshift-logging get po -l component=elasticsearch -o jsonpath='{.items[*].metadata.name}'`; \
  do echo $pod; oc -n openshift-logging exec -c elasticsearch $pod \
  -- df -h /elasticsearch/persistent; done
----

. In the command output, check the `Avail` column to determine the free disk space on that node.
+
.Example output
[source,terminal]
----
elasticsearch-cdm-kcrsda6l-1-586cc95d4f-h8zq8
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-2-5b548fc7b-cwwk7
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme2n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-3-5dfc884d99-59tjw
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme3n1     19G  528M   19G   3% /elasticsearch/persistent
----

. Increase the disk space on all nodes. If increasing the disk space is not possible, try adding a new data node to the cluster, or decrease the total cluster redundancy policy.

. To check the current `redundancyPolicy`, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get es elasticsearch \
  -o jsonpath='{.spec.redundancyPolicy}'
----
+
If you are using a `ClusterLogging` resource on your cluster, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get cl \
  -o jsonpath='{.items[*].spec.logStore.elasticsearch.redundancyPolicy}'
----
+
If the cluster `redundancyPolicy` value is higher than the `SingleRedundancy` value, set it to the `SingleRedundancy` value and save this change.

. If the preceding steps do not fix the issue, delete the old indices.
.. Check the status of all indices on Elasticsearch by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME -- indices
----

.. Identify an old index that can be deleted.
.. Delete the index by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name> -X DELETE
----

. Continue freeing up and monitoring the disk space. After the used disk space drops below 90%, unblock writing to this node by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=_all/_settings?pretty \
  -X PUT -d '{"index.blocks.read_only_allow_delete": null}'
----

[id="troubleshooting-logging-alerts-es-jvm-heap-use-is-high"]
== Elasticsearch JVM heap usage is high

The Elasticsearch node Java virtual machine (JVM) heap memory used is above 75%. Consider https://www.elastic.co/guide/en/elasticsearch/reference/current/advanced-configuration.html#set-jvm-heap-size[increasing the heap size].

[id="troubleshooting-logging-alerts-aggregated-logging-system-cpu-is-high"]
== Aggregated logging system CPU is high

System CPU usage on the node is high. Check the CPU of the cluster node. Consider allocating more CPU resources to the node.

[id="troubleshooting-logging-alerts-es-process-cpu-is-high"]
== Elasticsearch process CPU is high

Elasticsearch process CPU usage on the node is high. Check the CPU of the cluster node. Consider allocating more CPU resources to the node.

// Module included in the following assemblies:
//
// * observability/logging/troubleshooting/troubleshooting-logging-alerts.adoc

[id="es-disk-space-low_{context}"]
= Elasticsearch disk space is running low

Elasticsearch is predicted to run out of disk space within the next 6 hours based on current disk usage. Use the following procedure to troubleshoot this alert.

.Procedure

. Get the disk space of the Elasticsearch node:
+
[source,terminal]
----
$ for pod in `oc -n openshift-logging get po -l component=elasticsearch -o jsonpath='{.items[*].metadata.name}'`; \
  do echo $pod; oc -n openshift-logging exec -c elasticsearch $pod \
  -- df -h /elasticsearch/persistent; done
----

. In the command output, check the `Avail` column to determine the free disk space on that node.
+
.Example output
[source,terminal]
----
elasticsearch-cdm-kcrsda6l-1-586cc95d4f-h8zq8
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-2-5b548fc7b-cwwk7
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme2n1     19G  522M   19G   3% /elasticsearch/persistent
elasticsearch-cdm-kcrsda6l-3-5dfc884d99-59tjw
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme3n1     19G  528M   19G   3% /elasticsearch/persistent
----

. Increase the disk space on all nodes. If increasing the disk space is not possible, try adding a new data node to the cluster, or decrease the total cluster redundancy policy.

. To check the current `redundancyPolicy`, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get es elasticsearch -o jsonpath='{.spec.redundancyPolicy}'
----
+
If you are using a `ClusterLogging` resource on your cluster, run the following command:
+
[source,terminal]
----
$ oc -n openshift-logging get cl \
  -o jsonpath='{.items[*].spec.logStore.elasticsearch.redundancyPolicy}'
----
+
If the cluster `redundancyPolicy` value is higher than the `SingleRedundancy` value, set it to the `SingleRedundancy` value and save this change.

. If the preceding steps do not fix the issue, delete the old indices.
.. Check the status of all indices on Elasticsearch by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME -- indices
----

.. Identify an old index that can be deleted.
.. Delete the index by running the following command:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch $ES_POD_NAME \
  -- es_util --query=<elasticsearch_index_name> -X DELETE
----

[role="_additional-resources"]
.Additional resources
* Fix a red or yellow cluster status

[id="troubleshooting-logging-alerts-es-filedescriptor-usage-is-high"]
== Elasticsearch FileDescriptor usage is high

Based on current usage trends, the predicted number of file descriptors on the node is insufficient. Check the value of `max_file_descriptors` for each node as described in the Elasticsearch File Descriptors documentation.
