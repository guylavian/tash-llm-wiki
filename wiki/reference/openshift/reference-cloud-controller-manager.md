---
title: "Cloud Controller Manager"
type: reference
domain: openshift
slug: reference-cloud-controller-manager
tier: reference
source: https://kubernetes.io/docs/reference/glossary/cloud-controller-manager
family: reference
documentKind: "doc"
---

# Cloud Controller Manager

A Kubernetes {{< glossary_tooltip text="control plane" term_id="control-plane" >}} component
that embeds cloud-specific control logic. The cloud controller manager lets you link your
cluster into your cloud provider's API, and separates out the components that interact
with that cloud platform from components that only interact with your cluster.

<!--more-->

By decoupling the interoperability logic between Kubernetes and the underlying cloud
infrastructure, the cloud-controller-manager component enables cloud providers to release
features at a different pace compared to the main Kubernetes project.
