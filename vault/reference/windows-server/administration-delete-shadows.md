---
title: "delete shadows"
type: reference
domain: windows-server
slug: administration-delete-shadows
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/delete-shadows
family: administration
documentKind: "reference"
abstract: "Reference article for the delete shadows command, which deletes shadow copies."
---

# delete shadows

# delete shadows

Deletes shadow copies.

## Syntax

```
delete shadows [all | volume <volume> | oldest <volume> | set <setID> | id <shadowID> | exposed {<drive> | <mountpoint>}]
```

### Parameters

| Parameter | Description |
| ---- | ---- |
| all | Deletes all shadow copies. |
| volume `<volume>` | Deletes all shadow copies of the given volume. |
| oldest `<volume>` | Deletes the oldest shadow copy of the given volume. |
| set `<setID>` | Deletes the shadow copies in the Shadow Copy Set of the given ID. You can specify an alias by using the **%** symbol if the alias exists in the current environment. |
| id `<shadowID>` | Deletes a shadow copy of the given ID. You can specify an alias by using the **%** symbol if the alias exists in the current environment. |
| exposed {`<drive>` \| `<mountpoint>`} | Deletes shadow copies exposed at the specified drive or mount point. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [delete command](delete.md)
