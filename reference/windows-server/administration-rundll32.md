---
title: "rundll32"
type: reference
domain: windows-server
slug: administration-rundll32
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32
family: administration
documentKind: "reference"
abstract: "Reference article for the rundll32 command, which loads and runs 32-bit dynamic-link libraries (DLLs)."
---

# rundll32

# rundll32

Loads and runs 32-bit dynamic-link libraries (DLLs). There are no configurable settings for Rundll32. Help information is provided for a specific DLL you run with the **rundll32** command.

You must run the **rundll32** command from an elevated command prompt. To open an elevated command prompt, click **Start**, right-click **Command Prompt**, and then click **Run as administrator**.

## Syntax

```
rundll32 <DLLname>
```

### Parameters

| Parameter | Description |
|--|--|
| [Rundll32 printui.dll,PrintUIEntry](rundll32-printui.md) | Displays the printer user interface. |

## Remarks

Rundll32 can only call functions from a DLL explicitly written to be called by Rundll32.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
