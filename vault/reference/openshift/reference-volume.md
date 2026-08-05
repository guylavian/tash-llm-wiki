---
title: "Volume"
type: reference
domain: openshift
slug: reference-volume
tier: reference
source: https://kubernetes.io/docs/reference/glossary/volume
family: reference
documentKind: "doc"
---

# Volume

A directory containing data, accessible to the {{< glossary_tooltip text="containers" term_id="container" >}} in a {{< glossary_tooltip term_id="pod" >}}.

<!--more-->

A Kubernetes volume lives as long as the Pod that encloses it. Consequently, a volume outlives any containers that run within the Pod, and data in the volume is preserved across container restarts.

See [storage](/docs/concepts/storage/) for more information.
