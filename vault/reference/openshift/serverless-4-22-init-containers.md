---
title: "Init containers"
type: reference
domain: openshift
slug: serverless-4-22-init-containers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/init-containers
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Init containers

[id="init-containers"]
= Init containers

Init containers are specialized containers that are run before application containers in a pod. They are generally used to implement initialization logic for an application, which may include running setup scripts or downloading required configurations. You can enable the use of init containers for Knative services by modifying the `KnativeServing` custom resource (CR).

[NOTE]
====
Init containers may cause longer application start-up times and should be used with caution for serverless applications, which are expected to scale up and down frequently.
====

// enable init containers
// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-configuration.adoc

[id="serverless-admin-init-containers_{context}"]
= Enabling init containers

.Prerequisites

* You have installed {ServerlessOperatorName} and Knative Serving on your cluster.

* You have cluster administrator permissions.

* You have cluster or dedicated administrator permissions.

.Procedure

* Enable the use of init containers by adding the `kubernetes.podspec-init-containers` flag to the `KnativeServing` CR:
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    features:
      kubernetes.podspec-init-containers: enabled
...
----
