---
title: "Monitoring and OpenShift Logging Operator component certificates"
type: reference
domain: openshift
slug: security-4-22-monitoring-and-cluster-logging-operator-component-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/monitoring-and-cluster-logging-operator-component-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# Monitoring and OpenShift Logging Operator component certificates

[id="cert-types-monitoring-and-cluster-logging-operator-component-certificates"]
= Monitoring and OpenShift Logging Operator component certificates

== Expiration

Monitoring components secure their traffic with service CA certificates. These certificates are valid for 2 years and are replaced automatically on rotation of the service CA, which is every 13 months.

If the certificate is present in the `openshift-monitoring` or `openshift-logging` namespace, it is system managed and rotated automatically.

== Management

These certificates are managed by the system and not the user.
