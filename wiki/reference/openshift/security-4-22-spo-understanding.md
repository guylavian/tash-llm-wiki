---
title: "Understanding the Security Profiles Operator"
type: reference
domain: openshift
slug: security-4-22-spo-understanding
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-understanding
version: 4.22
family: security
documentKind: "Documentation"
---

# Understanding the Security Profiles Operator

[id="spo-understanding"]
= Understanding the Security Profiles Operator

OpenShift Container Platform administrators can use the Security Profiles Operator to define increased security measures in clusters.

[IMPORTANT]
====
The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.
====

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-understanding.adoc

[id="spo-about_{context}"]
= About Security Profiles

Security profiles can increase security at the container level in your cluster.

Seccomp security profiles list the syscalls a process can make. Permissions are broader than SELinux, enabling users to restrict operations system-wide, such as `write`.

SELinux security profiles provide a label-based system that restricts the access and usage of processes, applications, or files in a system. All files in an environment have labels that define permissions. SELinux profiles can define access within a given structure, such as directories.
