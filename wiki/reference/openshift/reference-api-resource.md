---
title: "API resource"
type: reference
domain: openshift
slug: reference-api-resource
tier: reference
source: https://kubernetes.io/docs/reference/glossary/api-resource
family: reference
documentKind: "doc"
---

# API resource

An entity in the Kubernetes type system, corresponding to an endpoint on the {{< glossary_tooltip text="Kubernetes API" term_id="kubernetes-api" >}}.
A resource typically represents an {{< glossary_tooltip text="object" term_id="object" >}}.
Some resources represent an operation on other objects, such as a permission check.
<!--more-->
Each resource represents an HTTP endpoint (URI) on the Kubernetes API server, defining the schema for the objects or operations on that resource.
