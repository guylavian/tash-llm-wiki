---
title: "Chapter 5. Troubleshooting using metrics - Red Hat build of Keycloak 26.4 Observability Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-metrics-for-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/observability_guide/metrics-for-troubleshooting-
guide: observability_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
---

# Chapter 5. Troubleshooting using metrics - Red Hat build of Keycloak 26.4 Observability Guide

Chapter 5. Troubleshooting using metrics
Use metrics for troubleshooting errors and performance issues.
For a running Red Hat build of Keycloak deployment it is important to understand how the system performs and whether it meets your service level objectives (SLOs). For more details on SLOs, proceed to the Monitoring performance with Service Level Indicators chapter.
This guide will provide directions to answer the question: “What can I do when my SLOs are not met?”
Red Hat build of Keycloak consists of several components where an issue or misconfiguration of one of them can move your service level indicators to undesirable numbers.
A guidance provided by this guide is illustrated in the following example:
Observation: Latency service level objective is not met.
Metrics that indicate a problem:
- Red Hat build of Keycloak’s database connection pool is often exhausted, and there are threads queuing for a connection to be retrieved from the pool.
-
Red Hat build of Keycloak’s
users
cache hit ratio is at a low percentage, around 5%. This means only 1 out of 20 user searches is able to obtain user data from the cache and the rest needs to load it from the database.
Possible mitigations suggested:
-
Increasing the
users
cache size to a higher number which would decrease the number of reads from the database. - Increasing the number of connections in the connection pool. This would need to be checked with metrics for your database and tuning it for a higher load, for example, by increasing the number of available processors.
- This guide focuses on Red Hat build of Keycloak metrics. Troubleshooting the database itself is out of scope.
- This guide provides general guidance. You should always confirm the configuration change by conducting a performance test comparing the metrics in question for the old and the new configuration.
Grafana dashboards for the metrics below can be found in Visualizing activities in dashboards chapter.
5.1. List of Red Hat build of Keycloak key metrics
5.2. Self-provided metrics
Learn about the key metrics that Red Hat build of Keycloak provides.
This is part of the Troubleshooting using metrics chapter.
5.2.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.2.2. Metrics
5.2.2.1. User Event Metrics
User event metrics are disabled by default. See Monitoring user activities with event metrics on how to enable them and how to configure which tags are recorded.
| Metric | Description |
|---|---|
|
| Counting the occurrence of user events. |
Tags
The tags client_id
and idp
are disabled by default to avoid a too high cardinality.
realm
- Realm
client_id
- Client ID
idp
- Identity Provider
event
-
User event, for example
login
orlogout
. See the Server Administration Guide on event types for an overview of the available events. error
-
Error specific to the event, for example
invalid_user_credentials
for the eventlogin
. Empty string if no error occurred.
The snippet below is an example of a response provided by the metric endpoint:
# HELP keycloak_user_events_total Keycloak user events
# TYPE keycloak_user_events_total counter
keycloak_user_events_total{client_id="security-admin-console",error="",event="code_to_token",idp="",realm="master",} 1.0
keycloak_user_events_total{client_id="security-admin-console",error="",event="login",idp="",realm="master",} 1.0
keycloak_user_events_total{client_id="security-admin-console",error="",event="logout",idp="",realm="master",} 1.0
keycloak_user_events_total{client_id="security-admin-console",error="invalid_user_credentials",event="login",idp="",realm="master",} 1.0
5.2.2.2. Password hashing
| Metric | Description |
|---|---|
|
| Counting password hashes validations. |
Tags
realm
- Realm
algorithm
-
Algorithm used for hashing password, for example
argon2
hashing_strength
-
String denoting strength of hashing algorithm, for example, number of iterations depending on the algorithm. For example,
Argon2id-1.3[m=7168,t=5,p=1]
outcome
Outcome of password validation. Possible values:
valid
- Password correct
invalid
- Password incorrect
error
- Error when creating the hash of the password
To configure what tags are available provide a comma-separated list of tag names to the following option spi-credential—keycloak-password—validations-counter-tags
. By default, all tags are enabled.
The snippet below is an example of a response provided by the metric endpoint:
# HELP keycloak_credentials_password_hashing_validations_total Password validations
# TYPE keycloak_credentials_password_hashing_validations_total counter
keycloak_credentials_password_hashing_validations_total{algorithm="argon2",hashing_strength="Argon2id-1.3[m=7168,t=5,p=1]",outcome="valid",realm="realm-0",} 39949.0
5.2.3. Next steps
Return back to the Troubleshooting using metrics or proceed to JVM metrics.
5.3. JVM metrics
Use JVM metrics to observe performance of Red Hat build of Keycloak.
This is part of the Troubleshooting using metrics chapter.
5.3.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.3.2. Metrics
5.3.2.1. JVM info
| Metric | Description |
|---|---|
|
| Information about the JVM such as version, runtime and vendor. |
5.3.2.2. Heap memory usage
| Metric | Description |
|---|---|
|
| The amount of memory that the JVM has committed for use, reflecting the portion of the allocated memory that is guaranteed to be available for the JVM to use. |
|
| The amount of memory currently used by the JVM, indicating the actual memory consumption by the application and JVM internals. |
5.3.2.3. Garbage collection
| Metric | Description |
|---|---|
|
| The maximum duration, in seconds, of garbage collection pauses experienced by the JVM due to a particular cause, which helps you quickly differentiate between types of GC (minor, major) pauses. |
|
| The total cumulative time spent in garbage collection pauses, indicating the impact of GC pauses on application performance in the JVM. |
|
| Counts the total number of garbage collection pause events, helping to assess the frequency of GC pauses in the JVM. |
|
| The percentage of CPU time spent on garbage collection, indicating the impact of GC on application performance in the JVM. It refers to the proportion of the total CPU processing time that is dedicated to executing garbage collection (GC) operations, as opposed to running application code or performing other tasks. This metric helps determine how much overhead GC introduces, affecting the overall performance of the Red Hat build of Keycloak’s JVM. |
5.3.2.4. CPU Usage in Kubernetes
| Metric | Description |
|---|---|
|
| Cumulative CPU time consumed by the container in core-seconds. |
5.3.3. Next steps
Return back to the Troubleshooting using metrics or proceed to Database Metrics.
5.4. Database Metrics
Use metrics to describe Red Hat build of Keycloak’s connection to the database.
This is part of the Troubleshooting using metrics chapter.
5.4.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.4.2. Database connection pool metrics
Configure Red Hat build of Keycloak to use a fixed size database connection pool. See the Concepts for database connection pools chapter for more information.
If there is a high count of threads waiting for a database connection, increasing the database connection pool size is not always the best option. It might overload the database which would then become the bottleneck. Consider the following options instead:
-
Reduce the number of HTTP worker threads using the option
http-pool-max-threads
to make it match the available database connections, and thereby reduce contention and resource usage in Red Hat build of Keycloak and increase throughput. -
Check which database statements are executed on the database. If you see, for example, a lot of information about clients and groups being fetched, and the
users
andrealms
cache are full, this might indicate that it is time to increase the sizes of those caches and see if this reduces your database load.
| Metric | Description |
|---|---|
|
| Idle database connections. |
|
| Database connections used in ongoing transactions. |
|
| Threads waiting for a database connection to become available. |
5.4.3. Next steps
Return back to the Troubleshooting using metrics or proceed to HTTP metrics.
5.5. HTTP metrics
Use metrics to monitor the Red Hat build of Keycloak HTTP requests processing.
This is part of the Troubleshooting using metrics chapter.
5.5.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.5.2. Metrics
5.5.2.1. Processing time
The processing time is exposed by these metrics, to monitor the Red Hat build of Keycloak performance and how long it takes to processing the requests.
On a healthy cluster, the average processing time will remain stable. Spikes or increases in the processing time may be an early sign that some node is under load.
Tags
method
- HTTP method.
outcome
- A more general outcome tag.
status
- The HTTP status code.
uri
- The requested URI.
| Metric | Description |
|---|---|
|
| The total number of requests processed. |
|
| The total duration for all the requests processed. |
You can enable histograms for this metric by setting http-metrics-histograms-enabled
to true
, and add additional buckets for service level objectives using the option http-metrics-slos
.
When histograms are enabled, the percentile buckets are available. Those are useful to create heat maps and analyze latencies, still collecting and exposing the percentile buckets will increase the load of to your monitoring system.
5.5.2.2. Active requests
The current number of active requests is also available.
| Metric | Description |
|---|---|
|
| The current number of active requests |
5.5.2.3. Bandwidth
The metrics below helps to monitor the bandwidth and consumed traffic used by Red Hat build of Keycloak and consumed by the requests and responses received or sent.
| Metric | Description |
|---|---|
|
| The total number of responses sent. |
|
| The total number of bytes sent. |
|
| The total number of requests received. |
|
| The total number of bytes received. |
When histograms are enabled, the percentile buckets are available. Those are useful to create heat maps and analyze latencies, still collecting and exposing the percentile buckets will increase the load of to your monitoring system.
5.5.3. Next steps
Return back to the Troubleshooting using metrics or,
- For single-cluster deployments, proceed to Clustering metrics,
- and for multi-cluster deployments, proceed to Embedded Infinispan metrics for multi-cluster deployments
5.5.4. Relevant options
| Value | |
|---|---|
|
Available only when metrics are enabled |
|
|
Available only when metrics are enabled |
5.6. Local caching metrics
Use metrics to monitor health for local caching.
Global tags
cache=<name>
- The cache name.
5.6.1. Size
Monitor the number of entries in your local cache.
| Metric | Description |
|---|---|
|
| The number of cached entries. |
5.6.2. Data Access
The following metrics monitor the cache accesses, such as lookup and evictions.
5.6.2.1. Reads
Tags
result=hit|miss
-
The result of the read/lookup operation. If the value is
hit
, the entry was found in the cache.
The read requests can be monitored using a single metric.
| Metric | Description |
|---|---|
|
| The total number of cache lookups. |
Hit Ratio for read operation
An expression can be used to compute the hit ratio for a cache in systems such as Prometheus. For example, the hit ratio for read operations can be expressed as:
cache_gets_total{result="hit"} / cache_gets_total
5.6.2.2. Evictions
When a cache is limited, eviction is the process of removing the least used entries to make space available for new entries to be cached.
| Metric | Description |
|---|---|
|
| The number of times the cache was evicted. |
5.7. Clustering metrics
Use metrics to monitor communication between Red Hat build of Keycloak nodes.
This is part of the Troubleshooting using metrics chapter.
5.7.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.7.2. Metrics
Deploying multiple Red Hat build of Keycloak nodes allows the load to be distributed amongst them, but this requires communication between the nodes. This section describes metrics that are useful for monitoring the communication between Red Hat build of Keycloak in order to identify possible faults.
This is relevant only for single-cluster deployments. When multiple clusters are used, as described in Multi-cluster deployments, Red Hat build of Keycloak nodes are not clustered together and therefore there is no communication between them directly.
Global tags
cluster=<name>
- The cluster name. If metrics from multiple clusters are being collected, this tag helps identify where they belong to.
node=<node>
- The name of the node reporting the metric.
All metric names prefixed with vendor_jgroups_
are provided for troubleshooting and debugging purposes only. The metric names can change in upcoming releases of Red Hat build of Keycloak without further notice. Therefore, we advise not using them in dashboards or in monitoring and alerting.
5.7.2.1. Response Time
The following metrics expose the response time for the remote requests. The response time is measured between two nodes and includes the processing time. All requests are measured by these metrics, and the response time should remain stable through the cluster lifecycle.
In a healthy cluster, the response time will remain stable. An increase in response time may indicate a degraded cluster or a node under heavy load.
Tags
node=<node>
- It identifies the sender node.
target_node=<node>
- It identifies the receiver node.
| Metric | Description |
|---|---|
|
| The number of synchronous requests to a receiver node. |
|
| The total duration of synchronous request to a receiver node |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.7.2.2. Bandwidth
All the bytes received and sent by the Red Hat build of Keycloak are collected by these metrics. Also, all the internal messages, as heartbeats, are counted too. They allow computing the bandwidth currently used by each node.
The metric name depends on the JGroups transport protocol in use.
| Metric | Protocol | Description |
|---|---|---|
|
|
| The total number of bytes received by a node. |
|
|
| |
|
|
| |
|
|
| The total number of bytes sent by a node. |
|
|
| |
|
|
|
5.7.2.3. Thread Pool
Monitoring the thread pool size is a good indicator that a node is under a heavy load. All requests received are added to the thread pool for processing and, when it is full, the request is discarded. A retransmission mechanism ensures a reliable communication with an increase of resource usage.
In a healthy cluster, the thread pool should never be closer to its maximum size (by default, 200
threads).
Thread pool metrics are not available with virtual threads. Virtual threads are enabled by default when running with OpenJDK 21.
The metric name depends on the JGroups transport protocol in use. The default transport protocol is TCP.
| Metric | Protocol | Description |
|---|---|---|
|
|
| Current number of threads in the thread pool. |
|
|
| |
|
|
| |
|
|
| The largest number of threads that have ever simultaneously been in the pool. |
|
|
| |
|
|
|
5.7.2.4. Flow Control
Flow control takes care of adjusting the rate of a message sender to the rate of the slowest receiver over time. This is implemented through a credit-based system, where each sender decrements its credits when sending. The sender blocks when the credits fall below 0, and only resumes sending messages when it receives a replenishment message from the receivers.
The metrics below show the number of blocked messages and the average blocking time. When a value is different from zero, it may signal that a receiver is overloaded and may degrade the cluster performance.
Each node has two independent flow control protocols, UFC
for unicast messages and MFC
for multicast messages.
A healthy cluster shows a value of zero for all metrics.
| Metric | Description |
|---|---|
|
| The number of times flow control blocks the sender for unicast messages. |
|
| Average time blocked (in ms) in flow control when trying to send an unicast message. |
|
| The number of times flow control blocks the sender for multicast messages. |
|
| Average time blocked (in ms) in flow control when trying to send a multicast message. |
5.7.2.5. Retransmissions
JGroups provides reliable delivery of messages. When a message is dropped on the network, or the receiver cannot handle the message, a retransmission is required. Retransmissions increase resource usage, and it is usually a signal of an overload system.
Random Early Drop (RED) monitors the sender queues. When the queues are almost full, the message is dropped, and a retransmission must happen. It prevents threads from being blocked by a full sender queue.
A healthy cluster shows a value of zero for all metrics.
| Metric | Description |
|---|---|
|
| The number of retransmitted messages. |
|
| The total number of dropped messages by the sender. |
|
| Percentage of all messages that were dropped by the sender. |
5.7.2.6. Network Partitions
5.7.2.6.1. Cluster Size
The cluster size metric reports the number of nodes present in the cluster. If it differs, it may signal that a node is joining, shutdown or, in the worst case, a network partition is happening.
A healthy cluster shows the same value in all nodes.
| Metric | Description |
|---|---|
|
| The number of nodes in the cluster. |
5.7.2.6.2. Network Partition Events
Network partitions in a cluster can happen due to various reasons. This metrics does not help predict network splits but signals that it happened, and the cluster has been merged.
A healthy cluster shows a value of zero for this metric.
| Metric | Description |
|---|---|
|
| The amount of time a network split was detected and healed. |
5.7.3. Next steps
Return back to the Troubleshooting using metrics or proceed to Embedded Infinispan metrics for single-cluster deployments.
5.8. Embedded Infinispan metrics for single-cluster deployments
Use metrics to monitor caching health and cluster replication.
This is part of the Troubleshooting using metrics chapter.
5.8.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.8.2. Metrics
Global tags
cache=<name>
- The cache name.
5.8.2.1. Size
Monitor the number of entries in your cache using these two metrics. If the cache is clustered, each entry has an owner node and zero or more backup copies of different nodes.
Sum the unique entry size metric to get a cluster total number of entries.
| Metric | Description |
|---|---|
|
| The approximate number of entries stored by the node, including backup copies. |
|
| The approximate number of entries stored by the node, excluding backup copies. |
5.8.2.2. Data Access
The following metrics monitor the cache accesses, such as the reads, writes and their duration.
5.8.2.2.1. Stores
A store operation is a write operation that writes or updates a value stored in the cache.
| Metric | Description |
|---|---|
|
| The total number of store requests. |
|
| The total duration of all store requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.8.2.2.2. Reads
A read operation reads a value from the cache. It divides into two groups, a hit if a value is found, and a miss if not found.
| Metric | Description |
|---|---|
|
| The total number of read hits requests. |
|
| The total duration of all read hits requests. |
|
| The total number of read misses requests. |
|
| The total duration of all read misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.8.2.2.3. Removes
A remove operation removes a value from the cache. It divides in two groups, a hit if a value exists, and a miss if the value does not exist.
| Metric | Description |
|---|---|
|
| The total number of remove hits requests. |
|
| The total duration of all remove hits requests. |
|
| The total number of remove misses requests. |
|
| The total duration of all remove misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
For users
and realms
cache, the database invalidation translates into a remove operation. These metrics are a good indicator of how frequent the database entities are modified and therefore removed from the cache.
Hit Ratio for read and remove operations
An expression can be used to compute the hit ratio for a cache in systems such as Prometheus. As an example, the hit ratio for read operations can be expressed as:
vendor_statistics_hit_times_seconds_count
/
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count)
Read/Write ratio
An expression can be used to compute the read-write ratio for a cache, using the metrics above:
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count)
/
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count
+ vendor_statistics_remove_hit_times_seconds_count
+ vendor_statistics_remove_miss_times_seconds_count
+ vendor_statistics_store_times_seconds_count)
5.8.2.2.4. Eviction
Eviction is the process to limit the cache size and, when full, an entry is removed to make room for a new entry to be cached. As Red Hat build of Keycloak caches the database entities in the users
, realms
and authorization
, database access always proceeds with an eviction event.
| Metric | Description |
|---|---|
|
| The total number of eviction events. |
Eviction rate
A rapid increase of eviction and very high database CPU usage means the users
or realms
cache is too small for smooth Red Hat build of Keycloak operation, as data needs to be re-loaded very often from the database which slows down responses. If enough memory is available, consider increasing the max cache size using the CLI options cache-embedded-users-max-count
or cache-embedded-realms-max-count
5.8.2.3. Locking
Write and remove operations hold the lock until the value is replicated in the local cluster and to the remote site.
On a healthy cluster, the number of locks held should remain constant, but deadlocks may create temporary spikes.
| Metric | Description |
|---|---|
|
| The number of locks currently being held by this node. |
5.8.2.4. Transactions
Transactional caches use both One-Phase-Commit and Two-Phase-Commit protocols to complete a transaction. These metrics keep track of the operation duration.
The PESSMISTIC
locking mode uses One-Phase-Commit and does not create commit requests.
In a healthy cluster, the number of rollbacks should remain zero. Deadlocks should be rare, but they increase the number of rollbacks.
| Metric | Description |
|---|---|
|
| The total number of prepare requests. |
|
| The total duration of all prepare requests. |
|
| The total number of rollback requests. |
|
| The total duration of all rollback requests. |
|
| The total number of commit requests. |
|
| The total duration of all commit requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.8.2.5. State Transfer
State transfer happens when a node joins or leaves the cluster. It is required to balance the data stored and guarantee the desired number of copies.
This operation increases the resource usage, and it will affect negatively the overall performance.
| Metric | Description |
|---|---|
|
| The number of in-flight transactional segments the local node requested from other nodes. |
|
| The number of in-flight segments the local node requested from other nodes. |
5.8.2.6. Cluster Data Replication
The cluster data replication can be the main source of failure. These metrics not only report the response time, i.e., the time it takes to replicate an update, but also the failures.
On a healthy cluster, the average replication time will be stable or with little variance. The number of failures should not increase.
| Metric | Description |
|---|---|
|
| The total number of successful replications. |
|
| The total number of failed replications. |
|
| The average time spent, in milliseconds, replicating data in the cluster. |
Success ratio
An expression can be used to compute the replication success ratio:
(vendor_rpc_manager_replication_count)
/
(vendor_rpc_manager_replication_count
+ vendor_rpc_manager_replication_failures)
5.8.3. Next steps
Return back to the Troubleshooting using metrics.
5.9. Embedded Infinispan metrics for multi-cluster deployments
Use metrics to monitor caching health.
This is part of the Troubleshooting using metrics chapter.
5.9.1. Prerequisites
- Metrics need to be enabled for Red Hat build of Keycloak. Follow the Gaining insights with metrics chapter for more details.
- A monitoring system collecting the metrics.
5.9.2. Metrics
Global tags
cache=<name>
- The cache name.
5.9.2.1. Size
Monitor the number of entries in your cache using these two metrics. If the cache is clustered, each entry has an owner node and zero or more backup copies of different nodes.
Sum the unique entry size metric to get a cluster total number of entries.
| Metric | Description |
|---|---|
|
| The approximate number of entries stored by the node, including backup copies. |
|
| The approximate number of entries stored by the node, excluding backup copies. |
5.9.2.2. Data Access
The following metrics monitor the cache accesses, such as the reads, writes and their duration.
5.9.2.2.1. Stores
A store operation is a write operation that writes or updates a value stored in the cache.
| Metric | Description |
|---|---|
|
| The total number of store requests. |
|
| The total duration of all store requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.9.2.2.2. Reads
A read operation reads a value from the cache. It divides into two groups, a hit if a value is found, and a miss if not found.
| Metric | Description |
|---|---|
|
| The total number of read hits requests. |
|
| The total duration of all read hits requests. |
|
| The total number of read misses requests. |
|
| The total duration of all read misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.9.2.2.3. Removes
A remove operation removes a value from the cache. It divides in two groups, a hit if a value exists, and a miss if the value does not exist.
| Metric | Description |
|---|---|
|
| The total number of remove hits requests. |
|
| The total duration of all remove hits requests. |
|
| The total number of remove misses requests. |
|
| The total duration of all remove misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
For users
and realms
cache, the database invalidation translates into a remove operation. These metrics are a good indicator of how frequent the database entities are modified and therefore removed from the cache.
Hit Ratio for read and remove operations
An expression can be used to compute the hit ratio for a cache in systems such as Prometheus. As an example, the hit ratio for read operations can be expressed as:
vendor_statistics_hit_times_seconds_count
/
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count)
Read/Write ratio
An expression can be used to compute the read-write ratio for a cache, using the metrics above:
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count)
/
(vendor_statistics_hit_times_seconds_count
+ vendor_statistics_miss_times_seconds_count
+ vendor_statistics_remove_hit_times_seconds_count
+ vendor_statistics_remove_miss_times_seconds_count
+ vendor_statistics_store_times_seconds_count)
5.9.2.2.4. Eviction
Eviction is the process to limit the cache size and, when full, an entry is removed to make room for a new entry to be cached. As Red Hat build of Keycloak caches the database entities in the users
, realms
and authorization
, database access always proceeds with an eviction event.
| Metric | Description |
|---|---|
|
| The total number of eviction events. |
Eviction rate
A rapid increase of eviction and very high database CPU usage means the users
or realms
cache is too small for smooth Red Hat build of Keycloak operation, as data needs to be re-loaded very often from the database which slows down responses. If enough memory is available, consider increasing the max cache size using the CLI options cache-embedded-users-max-count
or cache-embedded-realms-max-count
5.9.2.3. Transactions
Transactional caches use both One-Phase-Commit and Two-Phase-Commit protocols to complete a transaction. These metrics keep track of the operation duration.
The PESSMISTIC
locking mode uses One-Phase-Commit and does not create commit requests.
In a healthy cluster, the number of rollbacks should remain zero. Deadlocks should be rare, but they increase the number of rollbacks.
| Metric | Description |
|---|---|
|
| The total number of prepare requests. |
|
| The total duration of all prepare requests. |
|
| The total number of rollback requests. |
|
| The total duration of all rollback requests. |
|
| The total number of commit requests. |
|
| The total duration of all commit requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.9.3. Next steps
Return back to the Troubleshooting using metrics or proceed to External Data Grid metrics.
5.10. External Data Grid metrics
Use metrics to monitor external Data Grid performance.
This is part of the Troubleshooting using metrics chapter.
5.10.1. Prerequisites
5.10.1.1. Enabled Data Grid server metrics
Data Grid exposes metrics in the endpoint /metrics
. By default, they are enabled. We recommend enabling the attribute name-as-tags
as it makes the metrics name independent on the cache name.
To configure metrics in the Data Grid server, just enabled as shown in the XML below.
infinispan.xml
<infinispan>
<cache-container statistics="true">
<metrics gauges="true" histograms="false" name-as-tags="true" />
</cache-container>
</infinispan>
Using the Data Grid Operator in Kubernetes, metrics can be enabled by using a ConfigMap
with a custom configuration. It is shown below an example.
ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
name: cluster-config
data:
infinispan-config.yaml: >
infinispan:
cacheContainer:
metrics:
gauges: true
namesAsTags: true
histograms: false
infinispan.yaml CR
apiVersion: infinispan.org/v1
kind: Infinispan
metadata:
name: infinispan
annotations:
infinispan.org/monitoring: 'true'
spec:
configMapName: "cluster-config"
Additional information can be found in the Infinispan documentation and Infinispan operator documentation.
5.10.2. Clustering and Network
This section describes metrics that are useful for monitoring the communication between Data Grid nodes to identify possible network issues.
Global tags
cluster=<name>
- The cluster name. If metrics from multiple clusters are being collected, this tag helps identify where they belong to.
node=<node>
- The name of the node reporting the metric.
All metric names prefixed with vendor_jgroups_
are provided for troubleshooting and debugging purposes only. The metric names can change in upcoming releases of Red Hat build of Keycloak without further notice. Therefore, we advise not using them in dashboards or in monitoring and alerting.
5.10.2.1. Response Time
The following metrics expose the response time for the remote requests. The response time is measured between two nodes and includes the processing time. All requests are measured by these metrics, and the response time should remain stable through the cluster lifecycle.
In a healthy cluster, the response time will remain stable. An increase in response time may indicate a degraded cluster or a node under heavy load.
Tags
node=<node>
- It identifies the sender node.
target_node=<node>
- It identifies the receiver node.
| Metric | Description |
|---|---|
|
| The number of synchronous requests to a receiver node. |
|
| The total duration of synchronous request to a receiver node |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.2.2. Bandwidth
All the bytes received and sent by the Data Grid are collected by these metrics. Also, all the internal messages, as heartbeats, are counted too. They allow computing the bandwidth currently used by each node.
The metric name depends on the JGroups transport protocol in use.
| Metric | Protocol | Description |
|---|---|---|
|
|
| The total number of bytes received by a node. |
|
|
| |
|
|
| |
|
|
| The total number of bytes sent by a node. |
|
|
| |
|
|
|
5.10.2.3. Thread Pool
Monitoring the thread pool size is a good indicator that a node is under a heavy load. All requests received are added to the thread pool for processing and, when it is full, the request is discarded. A retransmission mechanism ensures a reliable communication with an increase of resource usage.
In a healthy cluster, the thread pool should never be closer to its maximum size (by default, 200
threads).
Thread pool metrics are not available with virtual threads. Virtual threads are enabled by default when running with OpenJDK 21.
The metric name depends on the JGroups transport protocol in use. The default transport protocol is TCP.
| Metric | Protocol | Description |
|---|---|---|
|
|
| Current number of threads in the thread pool. |
|
|
| |
|
|
| |
|
|
| The largest number of threads that have ever simultaneously been in the pool. |
|
|
| |
|
|
|
5.10.2.4. Flow Control
Flow control takes care of adjusting the rate of a message sender to the rate of the slowest receiver over time. This is implemented through a credit-based system, where each sender decrements its credits when sending. The sender blocks when the credits fall below 0, and only resumes sending messages when it receives a replenishment message from the receivers.
The metrics below show the number of blocked messages and the average blocking time. When a value is different from zero, it may signal that a receiver is overloaded and may degrade the cluster performance.
Each node has two independent flow control protocols, UFC
for unicast messages and MFC
for multicast messages.
A healthy cluster shows a value of zero for all metrics.
| Metric | Description |
|---|---|
|
| The number of times flow control blocks the sender for unicast messages. |
|
| Average time blocked (in ms) in flow control when trying to send an unicast message. |
|
| The number of times flow control blocks the sender for multicast messages. |
|
| Average time blocked (in ms) in flow control when trying to send a multicast message. |
5.10.2.5. Retransmissions
JGroups provides reliable delivery of messages. When a message is dropped on the network, or the receiver cannot handle the message, a retransmission is required. Retransmissions increase resource usage, and it is usually a signal of an overload system.
Random Early Drop (RED) monitors the sender queues. When the queues are almost full, the message is dropped, and a retransmission must happen. It prevents threads from being blocked by a full sender queue.
A healthy cluster shows a value of zero for all metrics.
| Metric | Description |
|---|---|
|
| The number of retransmitted messages. |
|
| The total number of dropped messages by the sender. |
|
| Percentage of all messages that were dropped by the sender. |
5.10.2.6. Network Partitions
5.10.2.6.1. Cluster Size
The cluster size metric reports the number of nodes present in the cluster. If it differs, it may signal that a node is joining, shutdown or, in the worst case, a network partition is happening.
A healthy cluster shows the same value in all nodes.
| Metric | Description |
|---|---|
|
| The number of nodes in the cluster. |
5.10.2.6.2. Cross-Site Status
The cross-site status reports connection status to the other site. It returns a value of 1
if is online or 0
if offline. The value of 2
is used on nodes where the status is unknown; not all nodes establish connections to the remote sites and do not contain this information.
A healthy cluster shows a value greater than zero.
| Metric | Description |
|---|---|
|
| The single site status (1 if online). |
Tags
site=<name>
- The name of the destination site.
5.10.2.6.3. Network Partition Events
Network partitions in a cluster can happen due to various reasons. This metrics does not help predict network splits but signals that it happened, and the cluster has been merged.
A healthy cluster shows a value of zero for this metric.
| Metric | Description |
|---|---|
|
| The amount of time a network split was detected and healed. |
5.10.3. Data Grid Caches
The metrics in this section help monitoring the Data Grid caches health and the cluster replication.
Global tags
cache=<name>
- The cache name.
5.10.3.1. Size
Monitor the number of entries in your cache using these two metrics. If the cache is clustered, each entry has an owner node and zero or more backup copies of different nodes.
Sum the unique entry size metric to get a cluster total number of entries.
| Metric | Description |
|---|---|
|
| The approximate number of entries stored by the node, including backup copies. |
|
| The approximate number of entries stored by the node, excluding backup copies. |
5.10.3.2. Data Access
The following metrics monitor the cache accesses, such as the reads, writes and their duration.
5.10.3.2.1. Stores
A store operation is a write operation that writes or updates a value stored in the cache.
| Metric | Description |
|---|---|
|
| The total number of store requests. |
|
| The total duration of all store requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.3.2.2. Reads
A read operation reads a value from the cache. It divides into two groups, a hit if a value is found, and a miss if not found.
| Metric | Description |
|---|---|
|
| The total number of read hits requests. |
|
| The total duration of all read hits requests. |
|
| The total number of read misses requests. |
|
| The total duration of all read misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.3.2.3. Removes
A remove operation removes a value from the cache. It divides in two groups, a hit if a value exists, and a miss if the value does not exist.
| Metric | Description |
|---|---|
|
| The total number of remove hits requests. |
|
| The total duration of all remove hits requests. |
|
| The total number of remove misses requests. |
|
| The total duration of all remove misses requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.3.3. Locking
Write and remove operations hold the lock until the value is replicated in the local cluster and to the remote site.
On a healthy cluster, the number of locks held should remain constant, but deadlocks may create temporary spikes.
| Metric | Description |
|---|---|
|
| The number of locks currently being held by this node. |
5.10.3.4. Transactions
Transactional caches use both One-Phase-Commit and Two-Phase-Commit protocols to complete a transaction. These metrics keep track of the operation duration.
The PESSMISTIC
locking mode uses One-Phase-Commit and does not create commit requests.
In a healthy cluster, the number of rollbacks should remain zero. Deadlocks should be rare, but they increase the number of rollbacks.
| Metric | Description |
|---|---|
|
| The total number of prepare requests. |
|
| The total duration of all prepare requests. |
|
| The total number of rollback requests. |
|
| The total duration of all rollback requests. |
|
| The total number of commit requests. |
|
| The total duration of all commit requests. |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.3.5. State Transfer
State transfer happens when a node joins or leaves the cluster. It is required to balance the data stored and guarantee the desired number of copies.
This operation increases the resource usage, and it will affect negatively the overall performance.
| Metric | Description |
|---|---|
|
| The number of in-flight transactional segments the local node requested from other nodes. |
|
| The number of in-flight segments the local node requested from other nodes. |
5.10.3.6. Cluster Data Replication
The cluster data replication can be the main source of failure. These metrics not only report the response time, i.e., the time it takes to replicate an update, but also the failures.
On a healthy cluster, the average replication time will be stable or with little variance. The number of failures should not increase.
| Metric | Description |
|---|---|
|
| The total number of successful replications. |
|
| The total number of failed replications. |
|
| The average time spent, in milliseconds, replicating data in the cluster. |
Success ratio
An expression can be used to compute the replication success ratio:
(vendor_rpc_manager_replication_count)
/
(vendor_rpc_manager_replication_count
+ vendor_rpc_manager_replication_failures)
5.10.3.7. Cross Site Data Replication
Like cluster data replication, the metrics in this section measure the time it takes to replicate the data to the other sites.
On a healthy cluster, the average cross-site replication time will be stable or with little variance.
Tags
site=<name>
- indicates the receiving site.
| Metric | Description |
|---|---|
|
| The total number of cross-site requests. |
|
| The total duration of all cross-site requests. |
|
| The total number of cross-site requests. This metric is more detailed with a per-site counter. |
|
| The total duration of all cross-site requests. This metric is more detailed with a per-site duration. |
|
| The total number of cross-site requests handled by this node. This metric is more detailed with a per-site counter. |
|
|
The site status. A value of 1 indicates that it is online. This value reacts to the Data Grid CLI commands |
When histogram is enabled, the percentile buckets are available. Those are useful to create heat maps but, collecting and exposing the percentile buckets may have a negative impact on the deployment performance.
5.10.4. Next steps
Return back to the Troubleshooting using metrics.
