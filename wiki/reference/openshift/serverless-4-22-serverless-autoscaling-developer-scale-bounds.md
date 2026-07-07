---
title: "Scale bounds"
type: reference
domain: openshift
slug: serverless-4-22-serverless-autoscaling-developer-scale-bounds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-autoscaling-developer-scale-bounds
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Scale bounds

[id="serverless-autoscaling-developer-scale-bounds"]
= Scale bounds

Scale bounds determine the minimum and maximum numbers of replicas that can serve an application at any given time. You can set scale bounds for an application to help prevent cold starts or control computing costs.

// minscale docs
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-autoscaling-developer-minscale_{context}"]
= Minimum scale bounds

The minimum number of replicas that can serve an application is determined by the `min-scale` annotation. If scale to zero is not enabled, the `min-scale` value defaults to `1`.

The `min-scale` value defaults to `0` replicas if the following conditions are met:

* The `min-scale` annotation is not set
* Scaling to zero is enabled
* The class `KPA` is used

.Example service spec with `min-scale` annotation
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
        autoscaling.knative.dev/min-scale: "0"
...
----
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-autoscaling-minscale-kn_{context}"]
= Setting the min-scale annotation by using the Knative CLI

Using the Knative (`kn`) CLI to set the `min-scale` annotation provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service` command with the `--scale-min` flag to create or modify the `min-scale` value for a service.

.Prerequisites

* Knative Serving is installed on the cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* Set the minimum number of replicas for the service by using the `--scale-min` flag:
+
[source,terminal]
----
$ kn service create <service_name> --image <image_uri> --scale-min <integer>
----
+
.Example command
[source,terminal]
----
$ kn service create example-service --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest --scale-min 2
----

// TODO: Check if it can be used with update and other service commands.

// maxscale docs
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-autoscaling-developer-maxscale_{context}"]
= Maximum scale bounds

The maximum number of replicas that can serve an application is determined by the `max-scale` annotation. If the `max-scale` annotation is not set, there is no upper limit for the number of replicas created.

.Example service spec with `max-scale` annotation
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
        autoscaling.knative.dev/max-scale: "10"
...
----
// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

[id="serverless-autoscaling-maxscale-kn_{context}"]
= Setting the max-scale annotation by using the Knative CLI

Using the Knative (`kn`) CLI to set the `max-scale` annotation provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service` command with the `--scale-max` flag to create or modify the `max-scale` value for a service.

.Prerequisites

* Knative Serving is installed on the cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* Set the maximum number of replicas for the service by using the `--scale-max` flag:
+
[source,terminal]
----
$ kn service create <service_name> --image <image_uri> --scale-max <integer>
----
+
.Example command
[source,terminal]
----
$ kn service create example-service --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest --scale-max 10
----
