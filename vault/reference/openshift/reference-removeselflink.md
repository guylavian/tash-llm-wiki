---
title: "RemoveSelfLink"
type: reference
domain: openshift
slug: reference-removeselflink
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/RemoveSelfLink
family: reference
documentKind: "doc"
---

# RemoveSelfLink

Sets the `.metadata.selfLink` field to blank (empty string) for all
objects and collections. This field has been deprecated since the Kubernetes v1.16
release. When this feature is enabled, the `.metadata.selfLink` field remains part of
the Kubernetes API, but is always unset.
