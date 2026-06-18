---
title: "Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-concepts-threads
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-threads-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 5. Concepts for configuring thread pools
Understand concepts for avoiding resource exhaustion and congestion.
This section is intended when you want to understand the considerations and best practices on how to configure thread pools connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak for HA with the Operator.
5.1. Concepts
5.1.1. JGroups communications
JGroups communications, which is used in single-site setups for the communication between Red Hat build of Keycloak nodes, benefits from the use of virtual threads which are available in OpenJDK 21 when at least four cores are available for Red Hat build of Keycloak. This reduces the memory usage and removes the need to configure thread pool sizes. Therefore, the use of OpenJDK 21 is recommended.
5.1.2. Quarkus executor pool
Red Hat build of Keycloak requests, as well as blocking probes, are handled by an executor pool. Depending on the available CPU cores, it has a maximum size of 50 or more threads. Threads are created as needed, and will end when no longer needed, so the system will scale up and down automatically. Red Hat build of Keycloak allows configuring the maximum thread pool size by the http-pool-max-threads
configuration option. See Deploying Red Hat build of Keycloak for HA with the Operator for an example.
When running on Kubernetes, adjust the number of worker threads to avoid creating more load than what the CPU limit allows for the Pod to avoid throttling, which would lead to congestion. When running on physical machines, adjust the number of worker threads to avoid creating more load than the node can handle to avoid congestion. Congestion would result in longer response times and an increased memory usage, and eventually an unstable system.
Ideally, you should start with a low limit of threads and adjust it accordingly to the target throughput and response time. When the load and the number of threads increases, the database connections can also become a bottleneck. Once a request cannot acquire a database connection within 5 seconds, it will fail with a message in the log like Unable to acquire JDBC Connection
. The caller will receive a response with a 5xx HTTP status code indicating a server side error.
If you increase the number of database connections and the number of threads too much, the system will be congested under a high load with requests queueing up, which leads to a bad performance. The number of database connections is configured via the Database
settings db-pool-initial-size
, db-pool-min-size
and db-pool-max-size
respectively. Low numbers ensure fast response times for all clients, even if there is an occasionally failing request when there is a load spike.
5.1.3. Load Shedding
By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.
Configure http-max-queued-requests
to specify a maximum queue length to allow for effective load shedding once this queue size is exceeded. Assuming a Red Hat build of Keycloak Pod processes around 200 requests per second, a queue of 1000 would lead to maximum waiting times of around 5 seconds.
When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.
5.1.4. Probes
Red Hat build of Keycloak’s liveness probe is non-blocking to avoid a restart of a Pod under a high load.
The overall health probe and the readiness probe can in some cases block to check the connection to the database, so they might fail under a high load. Due to this, a Pod can become non-ready under a high load.
5.1.5. OS Resources
In order for Java to create threads, when running on Linux it needs to have file handles available. Therefore, the number of open files (as retrieved as ulimit -n
on Linux) need to provide head-space for Red Hat build of Keycloak to increase the number of threads needed. Each thread will also consume memory, and the container memory limits need to be set to a value that allows for this or the Pod will be killed by Kubernetes.
