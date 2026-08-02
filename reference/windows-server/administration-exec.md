---
title: "exec"
type: reference
domain: windows-server
slug: administration-exec
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/exec
family: administration
documentKind: "reference"
abstract: "Reference article for the exec command, which runs a script file on the local computer."
---

# exec

# exec

Runs a script file on the local computer. This command also duplicates or restores data as part of a backup or restore sequence. If the script fails, an error is returned and DiskShadow quits.

The file can be a **cmd** script.

## Syntax

```
exec <scriptfile.cmd>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<scriptfile.cmd>` | Specifies the script file to run. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [diskshadow command](diskshadow.md)
