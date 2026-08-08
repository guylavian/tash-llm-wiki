---
title: "Multi-container support for Serving"
type: reference
domain: openshift
slug: serverless-4-22-multi-container-support-for-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/multi-container-support-for-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Multi-container support for Serving

[id="multi-container-support-for-serving"]
= Multi-container support for Serving

You can deploy a multi-container pod by using a single Knative service. This method is useful for separating application responsibilities into smaller, specialized parts.

// Multi-container support
// Module included in the following assemblies:
//
// * serverless/knative-serving/config-applications/multi-container-support-for-serving.adoc

[id="serverless-configuring-multi-container-service_{context}"]
= Configuring a multi-container service

Multi-container support is enabled by default. You can create a multi-container pod by specifiying multiple containers in the service.

.Procedure

. Modify your service to include additional containers. Only one container can handle requests, so specify `ports` for exactly one container. Here is an example configuration with two containers:
+
.Multiple containers configuration
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
...
spec:
  template:
    spec:
      containers:
        - name: first-container <1>
          image: gcr.io/knative-samples/helloworld-go
          ports:
            - containerPort: 8080 <2>
        - name: second-container <3>
          image: gcr.io/knative-samples/helloworld-java
----
<1> First container configuration.
<2> Port specification for the first container.
<3> Second container configuration.
