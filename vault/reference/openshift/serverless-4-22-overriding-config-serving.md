---
title: "Overriding Knative Serving system deployment configurations"
type: reference
domain: openshift
slug: serverless-4-22-overriding-config-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/overriding-config-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Overriding Knative Serving system deployment configurations

[id="overriding-config-serving"]
= Overriding Knative Serving system deployment configurations

You can override the default configurations for some specific deployments by modifying the `deployments` spec in the `KnativeServing` custom resources (CRs).

[NOTE]
====
You can only override probes that are defined in the deployment by default.

All Knative Serving deployments define a readiness and a liveness probe by default, with these exceptions:

* `net-kourier-controller` and `3scale-kourier-gateway` only define a readiness probe.
* `net-istio-controller` and `net-istio-webhook` define no probes.
====

// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-configuration.adoc

[id="knative-serving-CR-system-deployments_{context}"]
= Overriding system deployment configurations

Currently, overriding default configuration settings is supported for the `resources`, `replicas`, `labels`, `annotations`, and `nodeSelector` fields, as well as for the `readiness` and `liveness` fields for probes.

In the following example, a `KnativeServing` CR overrides the `webhook` deployment so that:

* The `readiness` probe timeout for `net-kourier-controller` is set to be 10 seconds.
* The deployment has specified CPU and memory resource limits.
* The deployment has 3 replicas.
* The `example-label: label` label is added.
* The `example-annotation: annotation` annotation is added.
* The `nodeSelector` field is set to select nodes with the `disktype: hdd` label.

[NOTE]
====
The `KnativeServing` CR label and annotation settings override the deployment's labels and annotations for both the deployment itself and the resulting pods.
====

.KnativeServing CR example
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: ks
  namespace: knative-serving
spec:
  high-availability:
    replicas: 2
  deployments:
  - name: net-kourier-controller
    readinessProbes: <1>
      - container: controller
        timeoutSeconds: 10
  - name: webhook
    resources:
    - container: webhook
      requests:
        cpu: 300m
        memory: 60Mi
      limits:
        cpu: 1000m
        memory: 1000Mi
    replicas: 3
    labels:
      example-label: label
    annotations:
      example-annotation: annotation
    nodeSelector:
      disktype: hdd
----
<1> You can use the `readiness` and `liveness` probe overrides to override all fields of a probe in a container of a deployment as specified in the Kubernetes API except for the fields related to the probe handler: `exec`, `grpc`, `httpGet`, and `tcpSocket`.

[role="_additional-resources"]
.Additional resources
* Probe configuration section of the Kubernetes API documentation
