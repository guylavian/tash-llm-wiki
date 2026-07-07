---
title: "fish auto-completion"
type: reference
domain: openshift
slug: tasks-optional-kubectl-configs-fish
tier: reference
source: https://kubernetes.io/docs/tasks/tools/included/optional-kubectl-configs-fish
family: tasks
documentKind: "doc"
abstract: "Optional configuration to enable fish shell auto-completion."
---

# fish auto-completion

{{< note >}}
Autocomplete for Fish requires kubectl 1.23 or later.
{{< /note >}}

The kubectl completion script for Fish can be generated with the command `kubectl completion fish`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following line to your `~/.config/fish/config.fish` file:

```shell
kubectl completion fish | source
```

After reloading your shell, kubectl autocompletion should be working.
