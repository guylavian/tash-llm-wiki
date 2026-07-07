---
title: "StreamingProxyRedirects"
type: reference
domain: openshift
slug: reference-streamingproxyredirects
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects
family: reference
documentKind: "doc"
---

# StreamingProxyRedirects

Instructs the API server to intercept (and follow) redirects from the
backend (kubelet) for streaming requests. Examples of streaming requests include the `exec`,
`attach` and `port-forward` requests.
