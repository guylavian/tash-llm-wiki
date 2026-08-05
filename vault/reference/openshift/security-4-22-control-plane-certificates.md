---
title: "Control plane certificates"
type: reference
domain: openshift
slug: security-4-22-control-plane-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/control-plane-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# Control plane certificates

[id="cert-types-control-plane-certificates"]
= Control plane certificates

== Location

Control plane certificates are included in these namespaces:

* openshift-config-managed
* openshift-kube-apiserver
* openshift-kube-apiserver-operator
* openshift-kube-controller-manager
* openshift-kube-controller-manager-operator
* openshift-kube-scheduler

== Management

Control plane certificates are managed by the system and rotated automatically.

In the rare case that your control plane certificates have expired, see Recovering from expired control plane certificates.
