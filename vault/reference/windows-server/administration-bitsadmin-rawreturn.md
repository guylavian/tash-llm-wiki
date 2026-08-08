---
title: "bitsadmin rawreturn"
type: reference
domain: windows-server
slug: administration-bitsadmin-rawreturn
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-rawreturn
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin rawreturn command that returns data suitable for parsing."
---

# bitsadmin rawreturn

# bitsadmin rawreturn

Applies to: Windows Server (All supported versions)

The bitsadmin rawreturn command returns data suitable for parsing. Typically, you use this command with the **/create** and **/get*** switches to receive only the value. You must specify this switch before other switches.

> [!NOTE]
> This command strips newline characters and formatting from the output.

## Syntax

```
bitsadmin /rawreturn
```

## Examples

To retrieve the raw data for the state of the job named *myDownloadJob*:

```
bitsadmin /rawreturn /getstate myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
