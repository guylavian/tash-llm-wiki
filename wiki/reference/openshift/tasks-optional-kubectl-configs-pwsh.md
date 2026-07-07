---
title: "PowerShell auto-completion"
type: reference
domain: openshift
slug: tasks-optional-kubectl-configs-pwsh
tier: reference
source: https://kubernetes.io/docs/tasks/tools/included/optional-kubectl-configs-pwsh
family: tasks
documentKind: "doc"
abstract: "Some optional configuration for powershell auto-completion."
---

# PowerShell auto-completion

The kubectl completion script for PowerShell can be generated with the command `kubectl completion powershell`.

To do so in all your shell sessions, add the following line to your `$PROFILE` file:

```powershell
kubectl completion powershell | Out-String | Invoke-Expression
```

This command will regenerate the auto-completion script on every PowerShell start up. You can also add the generated script directly to your `$PROFILE` file.

To add the generated script to your `$PROFILE` file, run the following line in your powershell prompt:

```powershell
kubectl completion powershell >> $PROFILE
```

After reloading your shell, kubectl autocompletion should be working.
