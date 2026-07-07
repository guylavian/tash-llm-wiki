---
title: "ReloadKubeletServerCertificateFile"
type: reference
domain: openshift
slug: reference-reloadkubeletservercertificatefile
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ReloadKubeletServerCertificateFile
family: reference
documentKind: "doc"
---

# ReloadKubeletServerCertificateFile

Enable the kubelet TLS server to update its certificate if the specified certificate file are changed.

This feature is useful when specifying `tlsCertFile` and `tlsPrivateKeyFile` in kubelet configuration.
The feature gate has no effect for other cases such as using TLS bootstrap.
