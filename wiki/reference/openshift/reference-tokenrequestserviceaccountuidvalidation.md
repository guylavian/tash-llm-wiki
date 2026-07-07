---
title: "TokenRequestServiceAccountUIDValidation"
type: reference
domain: openshift
slug: reference-tokenrequestserviceaccountuidvalidation
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/TokenRequestServiceAccountUIDValidation
family: reference
documentKind: "doc"
---

# TokenRequestServiceAccountUIDValidation

This is used to ensure that the UID provided in the TokenRequest matches
the UID of the ServiceAccount for which the token is being requested.
It helps prevent misuse of the TokenRequest API by ensuring that
tokens are only issued for the correct ServiceAccount.
