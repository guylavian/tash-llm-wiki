---
title: "Security Context"
type: reference
domain: openshift
slug: reference-security-context
tier: reference
source: https://kubernetes.io/docs/reference/glossary/security-context
family: reference
documentKind: "doc"
---

# Security Context

The `securityContext` field defines privilege and access control settings for
a {{< glossary_tooltip text="Pod" term_id="pod" >}} or
{{< glossary_tooltip text="container" term_id="container" >}}.

<!--more-->

In a `securityContext`, you can define: the user that processes run as,
the group that processes run as, and privilege settings.
You can also configure security policies (for example: SELinux, AppArmor or seccomp).

The `PodSpec.securityContext` setting applies to all containers in a Pod.
