---
title: "Overview of nodes"
type: reference
domain: openshift
slug: nodes-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/index
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Overview of nodes

[id="run-once-duration-override-about"]
= {run-once-operator} overview

[role="_abstract"]
You can use the {run-once-operator} to specify a maximum time limit that run-once pods can be active for.

// About the {run-once-operator}
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/index.adoc

[id="run-once-about_{context}"]
= About the {run-once-operator}

OpenShift Container Platform relies on run-once pods to perform tasks such as deploying a pod or performing a build. Run-once pods are pods that have a `RestartPolicy` of `Never` or `OnFailure`.

Cluster administrators can use the {run-once-operator} to force a limit on the time that those run-once pods can be active. After the time limit expires, the cluster will try to actively terminate those pods. The main reason to have such a limit is to prevent tasks such as builds to run for an excessive amount of time.

To apply the run-once duration override from the {run-once-operator} to run-once pods, you must enable it on each applicable namespace.

If both the run-once pod and the {run-once-operator} have their `activeDeadlineSeconds` value set, the lower of the two values is used.

[NOTE]
====
You cannot install the {run-once-operator} on clusters managed by the HyperShift Operator.
====
