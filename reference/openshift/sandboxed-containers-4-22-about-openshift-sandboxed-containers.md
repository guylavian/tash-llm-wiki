---
title: "About {osc}"
type: reference
domain: openshift
slug: sandboxed-containers-4-22-about-openshift-sandboxed-containers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/sandboxed_containers/about-openshift-sandboxed-containers
version: 4.22
family: sandboxed_containers
documentKind: "Documentation"
---

# About {osc}

[id="about-openshift-sandboxed-containers"]
= About {osc}

{osc} provide security by running containerized applications in lightweight virtual machines. This architecture isolates your workloads from other workloads on the cluster and does not require significant changes to your existing workflows.

Confidential Containers extend {osc} and provide an additional layer of security. They ensure that your workloads are isolated from hypervisors and cloud providers. Confidential Containers protect data in use by leveraging hardware-based Trusted Execution Environments, which are verified by the Trustee attestation service.

[NOTE]
====
Because {osc} releases on a different cadence from OpenShift Container Platform, its documentation is now available as a separate documentation set at Red Hat {osc}.
====
