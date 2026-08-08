---
title: "URL scheme for external routes"
type: reference
domain: openshift
slug: serverless-4-22-url-scheme-external-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/url-scheme-external-routes
version: 4.22
family: serverless
documentKind: "Documentation"
---

# URL scheme for external routes

[id="url-scheme-external-routes"]
= URL scheme for external routes

The URL scheme of external routes defaults to HTTPS for enhanced security. This scheme is determined by the `default-external-scheme` key in the `KnativeServing` custom resource (CR) spec.

// URL scheme for external routes
// Module included in the following assemblies
//
// * serverless/knative-serving/external-ingress-routing/url-scheme-external-routes.adoc

[id="serverless-url-scheme-external-routes_{context}"]
= Setting the URL scheme for external routes
// should probably be a procedure, but this is out of scope for the abstracts PR

.Default spec
[source,yaml]
----
...
spec:
  config:
    network:
      default-external-scheme: "https"
...
----

You can override the default spec to use HTTP by modifying the `default-external-scheme` key:

.HTTP override spec
[source,yaml]
----
...
spec:
  config:
    network:
      default-external-scheme: "http"
...
----
