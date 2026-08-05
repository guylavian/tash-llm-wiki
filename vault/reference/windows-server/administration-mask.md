---
title: "mask"
type: reference
domain: windows-server
slug: administration-mask
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mask
family: administration
documentKind: "reference"
abstract: "Reference article for the mask command, which removes hardware shadow copies that were imported by using the import command."
---

# mask

# mask

Removes hardware shadow copies that were imported by using the **import** command.

## Syntax

```
mask <shadowsetID>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| shadowsetID | Removes shadow copies that belong to the specified Shadow Copy Set ID. |

#### Remarks

- You can use an existing alias or an environment variable in place of *ShadowSetID*. Use **add** without parameters to see existing aliases.

### Examples

To remove the imported shadow copy *%Import_1%*, type:

```
mask %Import_1%
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
