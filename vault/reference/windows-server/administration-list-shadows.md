---
title: "list shadows"
type: reference
domain: windows-server
slug: administration-list-shadows
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/list-shadows
family: administration
documentKind: "reference"
abstract: "Reference article for the list shadows command, which lists persistent and existing non-persistent shadow copies that are on the system."
---

# list shadows

# list shadows

Lists persistent and existing non-persistent shadow copies that are on the system.

## Syntax

```
list shadows {all | set <setID> | id <shadowID>}
```

### Parameters

| Parameter | Description |
| ---------- | ---------- |
| all | Lists all shadow copies. |
| set `<setID>` | Lists shadow copies that belong to the specified Shadow Copy Set ID. |
| id `<shadowID>` | Lists any shadow copy with the specified shadow copy ID. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
