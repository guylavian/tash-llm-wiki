---
title: "ManifestBasedAdmissionControlConfig"
type: reference
domain: openshift
slug: reference-manifestbasedadmissioncontrolconfig
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ManifestBasedAdmissionControlConfig
family: reference
documentKind: "doc"
---

# ManifestBasedAdmissionControlConfig

Enable loading admission webhooks and CEL-based admission policies from
static manifest files on disk via the `staticManifestsDir` field in
`AdmissionConfiguration`. These policies are active from API server startup,
survive etcd unavailability, and can protect API-based admission resources
from modification.
