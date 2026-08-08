---
title: "Concurrency"
type: reference
domain: openshift
slug: serverless-4-22-serverless-concurrency
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-concurrency
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Concurrency

[id="serverless-concurrency"]
= Concurrency

Concurrency determines the number of simultaneous requests that can be processed by each replica of an application at any given time. Concurrency can be configured as a _soft limit_ or a _hard limit_:

* A soft limit is a targeted requests limit, rather than a strictly enforced bound. For example, if there is a sudden burst of traffic, the soft limit target can be exceeded.

* A hard limit is a strictly enforced upper bound requests limit. If concurrency reaches the hard limit, surplus requests are buffered and must wait until there is enough free capacity to execute the requests.
+
[IMPORTANT]
====
Using a hard limit configuration is only recommended if there is a clear use case for it with your application. Having a low, hard limit specified may have a negative impact on the throughput and latency of an application, and might cause cold starts.
====

Adding a soft target and a hard limit means that the autoscaler targets the soft target number of concurrent requests, but imposes a hard limit of the hard limit value for the maximum number of requests.

If the hard limit value is less than the soft limit value, the soft limit value is tuned down, because there is no need to target more requests than the number that can actually be handled.

// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-concurrency-limits-configure-soft_{context}"]
= Configuring a soft concurrency target

A soft limit is a targeted requests limit, rather than a strictly enforced bound. For example, if there is a sudden burst of traffic, the soft limit target can be exceeded. You can specify a soft concurrency target for your Knative service by setting the `autoscaling.knative.dev/target` annotation in the spec, or by using the `kn service` command with the correct flags.

.Procedure

* Optional: Set the `autoscaling.knative.dev/target` annotation for your Knative service in the spec of the `Service` custom resource:
+
.Example service spec
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/target: "200"
----

* Optional: Use the `kn service` command to specify the `--concurrency-target` flag:
+
[source,terminal]
----
$ kn service create <service_name> --image <image_uri> --concurrency-target <integer>
----
+
.Example command to create a service with a concurrency target of 50 requests
[source,terminal]
----
$ kn service create example-service --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest --concurrency-target 50
----
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-concurrency-limits-configure-hard_{context}"]
= Configuring a hard concurrency limit

A hard concurrency limit is a strictly enforced upper bound requests limit. If concurrency reaches the hard limit, surplus requests are buffered and must wait until there is enough free capacity to execute the requests. You can specify a hard concurrency limit for your Knative service by modifying the `containerConcurrency` spec, or by using the `kn service` command with the correct flags.

.Procedure

* Optional: Set the `containerConcurrency` spec for your Knative service in the spec of the `Service` custom resource:
+
.Example service spec
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
  template:
    spec:
      containerConcurrency: 50
----
+
The default value is `0`, which means that there is no limit on the number of simultaneous requests that are permitted to flow into one replica of the service at a time.
+
A value greater than `0` specifies the exact number of requests that are permitted to flow into one replica of the service at a time. This example would enable a hard concurrency limit of 50 requests.

* Optional: Use the `kn service` command to specify the `--concurrency-limit` flag:
+
[source,terminal]
----
$ kn service create <service_name> --image <image_uri> --concurrency-limit <integer>
----
+
.Example command to create a service with a concurrency limit of 50 requests
[source,terminal]
----
$ kn service create example-service --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest --concurrency-limit 50
----
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-target-utilization_{context}"]
= Concurrency target utilization

This value specifies the percentage of the concurrency limit that is actually targeted by the autoscaler. This is also known as specifying the _hotness_ at which a replica runs, which enables the autoscaler to scale up before the defined hard limit is reached.

For example, if the `containerConcurrency` value is set to 10, and the `target-utilization-percentage` value is set to 70 percent, the autoscaler creates a new replica when the average number of concurrent requests across all existing replicas reaches 7. Requests numbered 7 to 10 are still sent to the existing replicas, but additional replicas are started in anticipation of being required after the `containerConcurrency` value is reached.

.Example service configured using the target-utilization-percentage annotation
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/target-utilization-percentage: "70"
...
----
