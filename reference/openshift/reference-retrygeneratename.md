---
title: "RetryGenerateName"
type: reference
domain: openshift
slug: reference-retrygeneratename
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/RetryGenerateName
family: reference
documentKind: "doc"
---

# RetryGenerateName

Enables retrying of object creation when the
{{< glossary_tooltip text="API server" term_id="kube-apiserver" >}}
is expected to generate a [name](/docs/concepts/overview/working-with-objects/names/#names).

When this feature is enabled, requests using `generateName` are retried automatically in case the
control plane detects a name conflict with an existing object, up to a limit of 8 total attempts.
