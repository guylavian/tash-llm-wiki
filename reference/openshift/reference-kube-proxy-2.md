---
title: "kube-proxy"
type: reference
domain: openshift
slug: reference-kube-proxy-2
tier: reference
source: https://kubernetes.io/docs/reference/glossary/kube-proxy
family: reference
documentKind: "doc"
---

# kube-proxy

kube-proxy is a network proxy that runs on each
{{< glossary_tooltip text="node" term_id="node" >}} in your cluster,
implementing part of the Kubernetes
{{< glossary_tooltip term_id="service">}} concept.

<!--more-->

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
maintains network rules on nodes. These network rules allow network
communication to your Pods from network sessions inside or outside of
your cluster.

kube-proxy uses the operating system packet filtering layer if there is one
and it's available. Otherwise, kube-proxy forwards the traffic itself.
