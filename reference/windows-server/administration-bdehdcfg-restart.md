---
title: "bdehdcfg restart"
type: reference
domain: windows-server
slug: administration-bdehdcfg-restart
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bdehdcfg-restart
family: administration
documentKind: "reference"
abstract: "Reference article for the bdehdcfg restart command, which tells bdehdcfg that the computer should be restarted after the drive preparation has concluded."
---

# bdehdcfg restart

# bdehdcfg: restart

Informs the bdehdcfg command-line tool that the computer should be restarted after the drive preparation has concluded. If other users are logged on to the computer and the **quiet** command is not specified, a prompt appears to confirm that the computer should be restarted.

## Syntax

```
bdehdcfg -target {default|unallocated|<drive_letter> shrink|<drive_letter> merge} -restart
```

#### Parameters

This command has no additional parameters.

## Examples

To use the **restart** command:

```
bdehdcfg -target default -restart
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bdehdcfg](bdehdcfg.md)
