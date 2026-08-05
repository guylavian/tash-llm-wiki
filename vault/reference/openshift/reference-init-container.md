---
title: "Init Container"
type: reference
domain: openshift
slug: reference-init-container
tier: reference
source: https://kubernetes.io/docs/reference/glossary/init-container
family: reference
documentKind: "doc"
---

# Init Container

One or more initialization {{< glossary_tooltip text="containers" term_id="container" >}} that must run to completion before any app containers run.

<!--more--> 

Initialization (init) containers are like regular app containers, with one difference: init containers must run to completion before any app containers can start. Init containers run in series: each init container must run to completion before the next init container begins.

Unlike {{< glossary_tooltip text="sidecar containers" term_id="sidecar-container" >}}, init containers do not remain running after Pod startup.

For more information, read [init containers](/docs/concepts/workloads/pods/init-containers/).
