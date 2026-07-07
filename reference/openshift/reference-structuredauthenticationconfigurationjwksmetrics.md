---
title: "StructuredAuthenticationConfigurationJWKSMetrics"
type: reference
domain: openshift
slug: reference-structuredauthenticationconfigurationjwksmetrics
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfigurationJWKSMetrics
family: reference
documentKind: "doc"
---

# StructuredAuthenticationConfigurationJWKSMetrics

Enables additional metrics for JSON Web Key Set (JWKS) operations in JWT authenticators
configured via `--authentication-config`. When enabled, the API server records metrics about
the last time JWKS was fetched and the hash value of the JWKS response.
See the [metrics reference](/docs/reference/instrumentation/metrics/) for details.
