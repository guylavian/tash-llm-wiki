---
title: "Container Lifecycle Hooks"
type: reference
domain: openshift
slug: reference-container-lifecycle-hooks
tier: reference
source: https://kubernetes.io/docs/reference/glossary/container-lifecycle-hooks
family: reference
documentKind: "doc"
---

# Container Lifecycle Hooks

The lifecycle hooks expose events in the {{< glossary_tooltip text="Container" term_id="container" >}} management lifecycle and let the user run code when the events occur.

<!--more-->

Two hooks are exposed to Containers: PostStart which executes immediately after a container is created and PreStop which is blocking and is called immediately before a container is terminated.
