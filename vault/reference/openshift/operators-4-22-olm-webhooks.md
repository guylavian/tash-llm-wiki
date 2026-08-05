---
title: "Webhook management in Operator Lifecycle Manager"
type: reference
domain: openshift
slug: operators-4-22-olm-webhooks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-webhooks
version: 4.22
family: operators
documentKind: "Documentation"
---

# Webhook management in Operator Lifecycle Manager

[id="olm-webhooks"]
= Webhook management in Operator Lifecycle Manager

Webhooks allow Operator authors to intercept, modify, and accept or reject resources before they are saved to the object store and handled by the Operator controller. Operator Lifecycle Manager (OLM) can manage the lifecycle of these webhooks when they are shipped alongside your Operator.

[id="olm-webhooks-additional-resources"]
[role="_additional-resources"]
== Additional resources

* Types of webhook admission plugins
* Kubernetes documentation:
** Validating admission webhooks
** Mutating admission webhooks
** Conversion webhooks
