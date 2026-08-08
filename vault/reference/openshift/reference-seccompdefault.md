---
title: "SeccompDefault"
type: reference
domain: openshift
slug: reference-seccompdefault
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SeccompDefault
family: reference
documentKind: "doc"
---

# SeccompDefault

Enables the use of `RuntimeDefault` as the default seccomp profile
for all workloads.
The seccomp profile is specified in the `securityContext` of a Pod and/or a Container.
