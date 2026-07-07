---
title: "Specifying the TLS for your cluster"
type: reference
domain: openshift
slug: security-4-22-rosa-specifying-tls-for-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/rosa-specifying-tls-for-cluster
version: 4.22
family: security
documentKind: "Documentation"
---

# Specifying the TLS for your cluster

[id="rosa-specifying-tls-for-cluster"]
= Specifying the TLS for your cluster

[role="_abstract"]
OpenShift Container Platform supports the Modern Transport Layer Security (TLS) 1.3 security profile, allowing you to use TLS 1.3 for enhanced security of your client-facing ingress endpoint.

// Module included in the following assemblies:
//
// rosa-specifying-tls-for-cluster.adoc
[id="rosa-tls-support_{context}"]
= TLS support for your clusters

[role="_abstract"]
With OpenShift Container Platform, you can use the Modern Transport Layer Security (TLS) 1.3 security profile for managed endpoints, giving you authority over the API server and OAuth endpoints. Even when Red{nbsp}Hat manages the underlying control plane infrastructure, you still have control. By using this TLS 1.3profile, you ensure that administrative and automation tools, such as the `oc` command line tool and the CI/CD integration, use TLS 1.3 for all communications.
