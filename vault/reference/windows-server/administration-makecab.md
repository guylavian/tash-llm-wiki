---
title: "makecab"
type: reference
domain: windows-server
slug: administration-makecab
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/makecab
family: administration
documentKind: "reference"
abstract: "Reference article for the makecab command, which packages existing files into a cabinet (.cab) file."
---

# makecab

# makecab



Package existing files into a cabinet (.cab) file.


> [!NOTE]
> This command is the same as the [diantz command](diantz.md).

## Syntax

```
makecab [/v[n]] [/d var=<value> ...] [/l <dir>] <source> [<destination>]
makecab [/v[<n>]] [/d var=<value> ...] /f <directives_file> [...]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<source>` | File to compress. |
| `<destination>` | File name to give compressed file. If omitted, the last character of the source file name is replaced with an underscore (_) and used as the destination. |
| /f `<directives_file>` | A file with **makecab** directives (may be repeated). |
| /d var=`<value>` | Defines variable with specified value. |
| /l `<dir>` | Location to place destination (default is current directory). |
| /v[`<n>`] | Set debugging verbosity level (0=none,...,3=full). |
| /? | Displays help at the command prompt. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [diantz command](diantz.md)

- [Microsoft Cabinet format](/previous-versions/bb417343(v=msdn.10))
