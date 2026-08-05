---
title: "Volume Plugin"
type: reference
domain: openshift
slug: reference-volume-plugin
tier: reference
source: https://kubernetes.io/docs/reference/glossary/volume-plugin
family: reference
documentKind: "doc"
---

# Volume Plugin

A Volume Plugin enables integration of storage within a {{< glossary_tooltip text="Pod" term_id="pod" >}}.

<!--more--> 

A Volume Plugin lets you attach and mount storage volumes for use by a {{< glossary_tooltip text="Pod" term_id="pod" >}}. Volume plugins can be _in tree_ or _out of tree_. _In tree_ plugins are part of the Kubernetes code repository and follow its release cycle. _Out of tree_ plugins are developed independently.
