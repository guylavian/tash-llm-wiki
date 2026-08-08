---
title: "ftp rename"
type: reference
domain: windows-server
slug: administration-ftp-rename
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-rename
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp rename command, which renames remote files."
---

# ftp rename

# ftp rename



Renames remote files.

## Syntax

```
rename <filename> <newfilename>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<filename>` | Specifies the file that you want to rename. |
| `<newfilename>` | Specifies the new file name. |

### Examples

To rename the remote file *example.txt* to *example1.txt*, type:

```
rename example.txt example1.txt
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
