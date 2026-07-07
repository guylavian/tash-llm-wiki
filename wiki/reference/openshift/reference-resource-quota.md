---
title: "ResourceQuota"
type: reference
domain: openshift
slug: reference-resource-quota
tier: reference
source: https://kubernetes.io/docs/reference/glossary/resource-quota
family: reference
documentKind: "doc"
---

# ResourceQuota

Object that constrains aggregate resource
consumption, per {{< glossary_tooltip term_id="namespace" >}}.

<!--more-->

A ResourceQuota can either limit the quantity of {{< glossary_tooltip text="API resources" term_id="api-resource" >}}
that can be created in a namespace by type, or it can set a limit on the total amount of
{{< glossary_tooltip text="infrastructure resources" term_id="infrastructure-resource" >}}
that may be consumed on behalf of the namespace (and the objects within it).
