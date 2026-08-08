---
title: "mklink"
type: reference
domain: windows-server
slug: administration-mklink
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mklink
family: administration
documentKind: "reference"
abstract: "Reference article for the mklink command, which creates a directory or file symbolic or hard link."
---

# mklink

# mklink

Creates a directory or file symbolic or hard link.

## Syntax

```
mklink [[/d] | [/h] | [/j]] <link> <target>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| /d | Creates a directory symbolic link. By default, this command creates a file symbolic link. |
| /h | Creates a hard link instead of a symbolic link. |
| /j | Creates a Directory Junction. |
| `<link>` | Specifies the name of the symbolic link being created. |
| `<target>` | Specifies the path (relative or absolute) that the new symbolic link refers to. |
| /? | Displays help at the command prompt. |

### Examples

To create and remove a symbolic link named MyFolder from the root directory to the \Users\User1\Documents directory, and a hard link named Myfile.file to the example.file file located within the directory, type:

```
mklink /d \MyFolder \Users\User1\Documents
mklink /h \MyFile.file \User1\Documents\example.file
rd \MyFolder
del \MyFile.file
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [del command](del.md)

- [rd command](rd.md)

- [New-Item in Windows PowerShell](/powershell/module/microsoft.powershell.management/new-item?view=powershell-6&preserve-view=true)
