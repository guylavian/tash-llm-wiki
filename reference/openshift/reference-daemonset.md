---
title: "DaemonSet"
type: reference
domain: openshift
slug: reference-daemonset
tier: reference
source: https://kubernetes.io/docs/reference/glossary/daemonset
family: reference
documentKind: "doc"
---

# DaemonSet

Ensures a copy of a {{< glossary_tooltip text="Pod" term_id="pod" >}} is running across a set of nodes in a {{< glossary_tooltip text="cluster" term_id="cluster" >}}.

<!--more--> 

Used to deploy system daemons such as log collectors and monitoring agents that typically must run on every {{< glossary_tooltip term_id="node" >}}.
