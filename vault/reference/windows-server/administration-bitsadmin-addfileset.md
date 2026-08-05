---
title: "bitsadmin addfileset"
type: reference
domain: windows-server
slug: administration-bitsadmin-addfileset
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-addfileset
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin addfileset command, which adds one or more files to the specified job."
---

# bitsadmin addfileset

# bitsadmin addfileset

Adds one or more files to the specified job.

## Syntax

```
bitsadmin /addfileset <job> <textfile>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| textfile | A text file, each line of which contains a remote and a local file name. **Note:** Names must space-delimited. Lines starting with a `#` character are treated as a comment. |

## Examples

```
bitsadmin /addfileset files.txt
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
