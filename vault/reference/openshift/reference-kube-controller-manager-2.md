---
title: "kube-controller-manager"
type: reference
domain: openshift
slug: reference-kube-controller-manager-2
tier: reference
source: https://kubernetes.io/docs/reference/glossary/kube-controller-manager
family: reference
documentKind: "doc"
---

# kube-controller-manager

Control plane component that runs {{< glossary_tooltip text="controller" term_id="controller" >}} processes.

<!--more-->

Logically, each {{< glossary_tooltip text="controller" term_id="controller" >}} is a separate process, but to reduce complexity, they are all compiled into a single binary and run in a single process.
