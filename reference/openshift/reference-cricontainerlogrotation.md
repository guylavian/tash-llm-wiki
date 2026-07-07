---
title: "CRIContainerLogRotation"
type: reference
domain: openshift
slug: reference-cricontainerlogrotation
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/CRIContainerLogRotation
family: reference
documentKind: "doc"
---

# CRIContainerLogRotation

Enable container log rotation for CRI container runtime.
The default max size of a log file is 10MB and the default max number of
log files allowed for a container is 5.
These values can be configured in the kubelet config.
See [logging at node level](/docs/concepts/cluster-administration/logging/#logging-at-the-node-level)
for more details.
