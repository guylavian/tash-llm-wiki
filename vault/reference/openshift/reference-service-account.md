---
title: "ServiceAccount"
type: reference
domain: openshift
slug: reference-service-account
tier: reference
source: https://kubernetes.io/docs/reference/glossary/service-account
family: reference
documentKind: "doc"
---

# ServiceAccount

Provides an identity for processes that run in a {{< glossary_tooltip text="Pod" term_id="pod" >}}.

<!--more--> 

When processes inside Pods access the cluster, they are authenticated by the API server as a particular service account, for example, `default`. When you create a Pod, if you do not specify a service account, it is automatically assigned the default service account in the same {{< glossary_tooltip text="Namespace" term_id="namespace" >}}.
