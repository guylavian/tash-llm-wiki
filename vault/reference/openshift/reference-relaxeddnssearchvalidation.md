---
title: "RelaxedDNSSearchValidation"
type: reference
domain: openshift
slug: reference-relaxeddnssearchvalidation
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/RelaxedDNSSearchValidation
family: reference
documentKind: "doc"
---

# RelaxedDNSSearchValidation

Relax the server side validation for the DNS search string
(`.spec.dnsConfig.searches`) for containers. For example,
with this gate enabled, it is okay to include the `_` character
in the DNS name search string.
