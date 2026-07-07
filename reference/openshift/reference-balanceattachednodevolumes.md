---
title: "BalanceAttachedNodeVolumes"
type: reference
domain: openshift
slug: reference-balanceattachednodevolumes
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/BalanceAttachedNodeVolumes
family: reference
documentKind: "doc"
---

# BalanceAttachedNodeVolumes

Include volume count on node to be considered for
balanced resource allocation while scheduling. A node which has closer CPU,
memory utilization, and volume count is favored by the scheduler while making decisions.
