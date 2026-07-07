---
title: "Global HTTPS redirection"
type: reference
domain: openshift
slug: serverless-4-22-https-redirect-global
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/https-redirect-global
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Global HTTPS redirection

[id="https-redirect-global"]
= Global HTTPS redirection

HTTPS redirection provides redirection for incoming HTTP requests. These redirected HTTP requests are encrypted. You can enable HTTPS redirection for all services on the cluster by configuring the `httpProtocol` spec for the `KnativeServing` custom resource (CR).

// global https redirect
// Module included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/https-redirect-global.adoc

[id="serverless-https-redirect-global_{context}"]
= HTTPS redirection global settings

.Example `KnativeServing` CR that enables HTTPS redirection
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    network:
      httpProtocol: "redirected"
...
----
