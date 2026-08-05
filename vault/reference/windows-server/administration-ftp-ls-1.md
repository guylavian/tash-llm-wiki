---
title: "ftp ls"
type: reference
domain: windows-server
slug: administration-ftp-ls-1
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-ls_1
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp ls command, which displays an abbreviated list of files and subdirectories from the remote computer."
---

# ftp ls

# ftp ls



Displays an abbreviated list of files and subdirectories from the remote computer.

## Syntax

```
ls [<remotedirectory>] [<localfile>]
```

### Parameters

| Parameter | Description |
| --------- |------------ |
| `[<remotedirectory>]` | Specifies the directory for which you want to see a listing. If no directory is specified, the current working directory on the remote computer is used. |
| `[<localfile>]` | Specifies a local file in which to store the listing. If a local file is not specified, results are displayed on the screen. |

### Examples

To display an abbreviated list of files and subdirectories from the remote computer, type:

```
ls
```

To get an abbreviated directory listing of *dir1* on the remote computer and save it in a local file called *dirlist.txt*, type:

```
ls dir1 dirlist.txt
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
