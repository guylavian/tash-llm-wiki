---
title: "lpq"
type: reference
domain: windows-server
slug: administration-lpq
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lpq
family: administration
documentKind: "reference"
abstract: "Reference article for the lpq command, which displays the status of a print queue on a computer running Line printer Daemon (LPD)."
---

# lpq

# lpq



Displays the status of a print queue on a computer running Line printer Daemon (LPD).

## Syntax

```
lpq -S <servername> -P <printername> [-l]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| -S `<servername>` | Specifies (by name or IP address) the computer or printer sharing device that hosts the LPD print queue with a status that you want to display. This parameter is required and must be capitalized. |
| -P `<Printername>` | Specifies (by name) the printer for the print queue with a status that you want to display. This parameter is required and must be capitalized. |
| -l | Specifies that you want to display details about the status of the print queue. |
| /? | Displays help at the command prompt. |

### Examples

To display the status of the *Laserprinter1* printer queue on an LPD host at *10.0.0.45*, type:

```
lpq -S 10.0.0.45 -P Laserprinter1
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Print Command Reference](print-command-reference.md)
