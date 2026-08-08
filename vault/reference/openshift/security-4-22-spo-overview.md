---
title: "Security Profiles Operator overview"
type: reference
domain: openshift
slug: security-4-22-spo-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-overview
version: 4.22
family: security
documentKind: "Documentation"
---

# Security Profiles Operator overview

[id="spo-overview"]
= Security Profiles Operator overview

OpenShift Container Platform Security Profiles Operator (SPO) provides a way to define secure computing (https://kubernetes.io/docs/tutorials/security/seccomp/[seccomp]) profiles and SELinux profiles as custom resources, synchronizing profiles to every node in a given namespace. For the latest updates, see the release notes.

The SPO can distribute custom resources to each node while a reconciliation loop ensures that the profiles stay up-to-date. See Understanding the Security Profiles Operator.

The SPO manages SELinux policies and seccomp profiles for namespaced workloads. For more information, see Enabling the Security Profiles Operator.

You can create seccomp and SELinux profiles, bind policies to pods, record workloads, and synchronize all worker nodes in a namespace.

Use Advanced Security Profile Operator tasks to enable the log enricher, configure webhooks and metrics, or restrict profiles to a single namespace.

Use SPO Advanced Audit Logging to access logs in RHCOS containers for container-level security audit features.

Troubleshoot the Security Profiles Operator as needed, or engage Red Hat support.

You can Uninstall the Security Profiles Operator by removing the profiles before removing the Operator.
