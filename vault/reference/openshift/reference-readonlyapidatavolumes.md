---
title: "ReadOnlyAPIDataVolumes"
type: reference
domain: openshift
slug: reference-readonlyapidatavolumes
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ReadOnlyAPIDataVolumes
family: reference
documentKind: "doc"
---

# ReadOnlyAPIDataVolumes

Set [`configMap`](/docs/concepts/storage/volumes/#configmap), 
[`secret`](/docs/concepts/storage/volumes/#secret), 
[`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) and 
[`projected`](/docs/concepts/storage/volumes/#projected) 
{{< glossary_tooltip term_id="volume" text="volumes" >}} to be mounted read-only.

Since Kubernetes v1.10, these volume types are always read-only and you cannot opt out.
