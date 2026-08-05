---
title: "convert"
type: reference
domain: windows-server
slug: administration-convert
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/convert
family: administration
documentKind: "reference"
abstract: "Reference article for the convert command, which converts a disk from one disk type to another."
---

# convert

# convert

Converts a disk from one disk type to another.

## Syntax

```
convert basic
convert dynamic
convert gpt
convert mbr
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| [convert basic command](convert-basic.md) | Converts an empty dynamic disk into a basic disk. |
| [convert dynamic command](convert-dynamic.md) | Converts a basic disk into a dynamic disk. |
| [convert gpt command](convert-gpt.md) | Converts an empty basic disk with the master boot record (MBR) partition style into a basic disk with the GUID partition table (GPT) partition style. |
| [convert mbr command](convert-mbr.md) | Converts an empty basic disk with the GUID Partition Table (GPT) partition style into a basic disk with the master boot record (MBR) partition style. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
