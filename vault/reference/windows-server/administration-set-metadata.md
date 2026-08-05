---
title: "set metadata"
type: reference
domain: windows-server
slug: administration-set-metadata
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set-metadata
family: administration
documentKind: "reference"
abstract: "Reference article for the set metadata command, which sets the name and location of the shadow creation metadata file used to transfer shadow copies from one computer to another."
---

# set metadata

# set metadata

Sets the name and location of the shadow creation metadata file used to transfer shadow copies from one computer to another. If used without parameters, **set metadata** displays help at the command prompt.

## Syntax

```
set metadata [<drive>:][<path>]<metadata.cab>
```

### Parameters

| Parameter | Description |
|--|--|
| `[<drive>:][<path>]` | Specifies the location to create the metadata file. |
| `<metadata.cab>` | Specifies the name of the cab file to store shadow creation metadata. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [set context command](set-context.md)

- [set option command](set-option.md)

- [set verbose command](set-verbose.md)
