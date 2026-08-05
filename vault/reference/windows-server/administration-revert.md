---
title: "revert"
type: reference
domain: windows-server
slug: administration-revert
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/revert
family: administration
documentKind: "reference"
abstract: "Reference article for the revert command, which reverts a volume back to a specified shadow copy."
---

# revert

# revert

Reverts a volume back to a specified shadow copy. This is supported only for shadow copies in the CLIENTACCESSIBLE context. These shadow copies are persistent and can only be made by the system provider. If used without parameters, **revert** displays help at the command prompt.

## Syntax

```
revert <shadowcopyID>
```

### Parameters

| Parameter | Description |
|--|--|
| `<shadowcopyID>` | Specifies the shadow copy ID to revert the volume to. If you don't use this parameter, the command displays help at the command prompt. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
