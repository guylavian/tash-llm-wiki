---
title: "File Integrity Operator overview"
type: reference
domain: openshift
slug: security-4-22-fio-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/fio-overview
version: 4.22
family: security
documentKind: "Documentation"
---

# File Integrity Operator overview

[id="fio-overview"]
= File Integrity Operator overview

The File Integrity Operator continually runs file integrity checks on the cluster nodes. It deploys a DaemonSet that initializes and runs privileged Advanced Intrusion Detection Environment (AIDE) containers on each node, providing a log of files that have been modified since the initial run of the DaemonSet pods.

[NOTE]
====
File Integrity Operator is not supported on HCP clusters.
====

For the latest updates, see the File Integrity Operator release notes.

Installing the File Integrity Operator

Updating the File Integrity Operator

Understanding the File Integrity Operator

Configuring the Custom File Integrity Operator

Performing advanced Custom File Integrity Operator tasks

Troubleshooting the File Integrity Operator

Uninstalling the File Integrity Operator
