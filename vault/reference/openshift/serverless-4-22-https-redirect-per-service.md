---
title: "HTTPS redirection per service"
type: reference
domain: openshift
slug: serverless-4-22-https-redirect-per-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/https-redirect-per-service
version: 4.22
family: serverless
documentKind: "Documentation"
---

# HTTPS redirection per service

[id="https-redirect-per-service"]
= HTTPS redirection per service

You can enable or disable HTTPS redirection for a service by configuring the `networking.knative.dev/http-option` annotation.

// Module is included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/https-redirect-per-service.adoc

[id="serverless-https-redirect-service_{context}"]
= Redirecting HTTPS for a service

// need better details from eng team about use case to update this topic
The following example shows how you can use this annotation in a Knative `Service` YAML object:

[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example
  namespace: default
  annotations:
    networking.knative.dev/http-option: "redirected"
spec:
  ...
----
