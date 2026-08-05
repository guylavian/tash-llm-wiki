---
title: "ftp ascii"
type: reference
domain: windows-server
slug: administration-ftp-ascii
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-ascii
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp ascii command, which sets the file transfer type to ASCII."
---

# ftp ascii

# ftp ascii



Sets the file transfer type to ASCII. The **ftp** command supports both ASCII (default) and binary image file transfer types, but we recommend using ASCII when transferring text files. In ASCII mode, character conversions to and from the network standard character set are performed. For example, end-of-line characters are converted as necessary, based on the target operating system.

## Syntax

```
ascii
```

### Examples

To set the file transfer type to ASCII, type:

```
ascii
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ftp binary command](ftp-binary.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
