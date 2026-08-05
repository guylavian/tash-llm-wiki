---
title: "vssadmin delete shadows"
type: reference
domain: windows-server
slug: administration-vssadmin-delete-shadows
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin-delete-shadows
family: administration
documentKind: "reference"
abstract: "A description of the vssadmin delete shadows command, which deletes a specified volume's shadow copies."
---

# vssadmin delete shadows

# vssadmin delete shadows



Deletes a specified volume's shadow copies. You can only delete shadow copies with the *client-accessible* type.

> [!NOTE]
> If you encounter the error "Error: Snapshots were found, but they were outside of your allowed context," the shadow copies are not client-accessible and cannot be deleted with `vssadmin`. Use the [diskshadow](diskshadow.md) command instead to manage and delete those shadow copies.

## Syntax

```
vssadmin delete shadows /for=<ForVolumeSpec> [/oldest | /all | /shadow=<ShadowID>] [/quiet]
```

### Parameters

| Parameter | Description |
|--|--|
| /for=`<ForVolumeSpec>` | Specifies which volume's shadow copy will be deleted. |
| /oldest | Deletes only the oldest shadow copy. |
| /all | Deletes all of the specified volume's shadow copies. |
| /shadow=`<ShadowID>` | Deletes the shadow copy specified by ShadowID. To get the shadow copy ID, use the [vssadmin list shadows command](vssadmin-list-shadows.md). When you enter a shadow copy ID, use the following format, where each *X* represents a hexadecimal character:<p>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX |
| /quiet | Specifies that the command won't display messages while running. |

## Examples

To delete the oldest shadow copy of volume C, type:

```
vssadmin delete shadows /for=c: /oldest
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [vssadmin command](vssadmin.md)

- [vssadmin list shadows command](vssadmin-list-shadows.md)

- [diskshadow command](diskshadow.md)
