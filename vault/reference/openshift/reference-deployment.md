---
title: "Deployment"
type: reference
domain: openshift
slug: reference-deployment
tier: reference
source: https://kubernetes.io/docs/reference/glossary/deployment
family: reference
documentKind: "doc"
---

# Deployment

An API object that manages a replicated application, typically by running Pods with no local state.

<!--more--> 

Each replica is represented by a {{< glossary_tooltip term_id="pod" >}}, and the Pods are distributed among the 
{{< glossary_tooltip text="nodes" term_id="node" >}} of a cluster.
For workloads that do require local state, consider using a {{< glossary_tooltip term_id="StatefulSet" >}}.
