---
title: "Container Runtime"
type: reference
domain: openshift
slug: reference-container-runtime
tier: reference
source: https://kubernetes.io/docs/reference/glossary/container-runtime
family: reference
documentKind: "doc"
---

# Container Runtime

A fundamental component that empowers Kubernetes to run containers effectively.
 It is responsible for managing the execution and lifecycle of containers within the Kubernetes environment.

<!--more-->

Kubernetes supports container runtimes such as
{{< glossary_tooltip term_id="containerd" >}}, {{< glossary_tooltip term_id="cri-o" >}},
and any other implementation of the [Kubernetes CRI (Container Runtime
Interface)](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/container-runtime-interface.md).
