---
title: "Remediating, fencing, and maintaining nodes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-remediating-fencing-maintaining-rhwa
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-remediating-fencing-maintaining-rhwa
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Remediating, fencing, and maintaining nodes

[id="nodes-remediating-fencing-maintaining-rhwa"]
= Remediating, fencing, and maintaining nodes

[role="_abstract"]
When node-level failures occur, due to issues such as kernel hangs or network issues, it is important to isolate the node, known as _fencing_, before initiating recovery of the workload, known as _remediation_, and then you can attempt to recover the node.

During node failures, the work required from the cluster does not decrease and workloads from affected nodes need to be restarted somewhere. Failures affecting these workloads risk data loss, corruption, or both.

For more information on remediation, fencing, and maintaining nodes, see the Workload Availability for Red Hat OpenShift documentation.
