---
title: "ServiceIPStaticSubrange"
type: reference
domain: openshift
slug: reference-serviceipstaticsubrange
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ServiceIPStaticSubrange
family: reference
documentKind: "doc"
---

# ServiceIPStaticSubrange

Enables a strategy for Services ClusterIP allocations, whereby the
ClusterIP range is subdivided. Dynamic allocated ClusterIP addresses will be allocated preferently
from the upper range allowing users to assign static ClusterIPs from the lower range with a low
risk of collision. See
[Avoiding collisions](/docs/reference/networking/virtual-ips/#avoiding-collisions)
for more details.
