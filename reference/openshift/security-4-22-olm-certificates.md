---
title: "OLM certificates"
type: reference
domain: openshift
slug: security-4-22-olm-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/olm-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# OLM certificates

[id="cert-types-olm-certificates"]
= OLM certificates

== Management

All certificates for Operator Lifecycle Manager (OLM) components (`olm-operator`, `catalog-operator`, `packageserver`, and `marketplace-operator`) are managed by the system.

When installing Operators that include webhooks or API services in their `ClusterServiceVersion` (CSV) object, OLM creates and rotates the certificates for these resources. Certificates for resources in the `openshift-operator-lifecycle-manager` namespace are managed by OLM.

OLM does not update the certificates of Operators that it manages in proxy environments. These certificates must be managed by the user using the subscription config.

[role="_additional-resources"]
.Next steps

* Configuring proxy support in Operator Lifecycle Manager

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Proxy certificates
* Replacing the default ingress certificate
* Updating the CA bundle
