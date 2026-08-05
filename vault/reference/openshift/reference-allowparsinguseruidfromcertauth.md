---
title: "AllowParsingUserUIDFromCertAuth"
type: reference
domain: openshift
slug: reference-allowparsinguseruidfromcertauth
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/AllowParsingUserUIDFromCertAuth
family: reference
documentKind: "doc"
---

# AllowParsingUserUIDFromCertAuth

When this feature is enabled, the subject name attribute `1.3.6.1.4.1.57683.2`
in an X.509 certificate will be parsed as the user UID during certificate authentication.
