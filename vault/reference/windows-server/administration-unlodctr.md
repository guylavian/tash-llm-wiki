---
title: "unlodctr"
type: reference
domain: windows-server
slug: administration-unlodctr
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/unlodctr
family: administration
documentKind: "reference"
abstract: "Reference article for the unlodctr command, which removes Performance counter names and Explain text for a service or device driver from the system registry."
---

# unlodctr

# unlodctr



Removes **Performance counter names** and **Explain text** for a service or device driver from the system registry.

> [!WARNING]
> Incorrectly editing the registry may severely damage your system. Before making changes to the registry, you should back up any valued data on the computer.

## Syntax

```
unlodctr <drivername>
```

### Parameters

| Parameter | Description |
|--|--|
| `<drivername>` | Removes the **Performance counter name** settings and **Explain text** for driver or service `<drivername>` from the Windows Server registry. If your `<drivername>` includes spaces, you must use quotation marks around the text, for example "Driver name". |
| /? | Displays help at the command prompt. |

#### Remarks

An exit code of **0** indicates the command line syntax was correct. It doesn't mean the operation was successful. Check the output from the command for potential error messages.

## Examples

To remove the current **Performance counter names** and **Explain text** for the Simple Mail Transfer Protocol (SMTP) service, type:

```
unlodctr SMTPSVC
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
