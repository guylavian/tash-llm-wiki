---
title: "reg export"
type: reference
domain: windows-server
slug: administration-reg-export
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-export
family: administration
documentKind: "reference"
abstract: "Reference article for the reg export command, which copies the specified subkeys, entries, and values of the local computer into a file for transfer to other servers."
---

# reg export

# reg export

Copies the specified subkeys, entries, and values of the local computer into a file for transfer to other servers.

## Syntax

```
reg export <keyname> <filename> [/y]
```

### Parameters

| Parameter | Description |
|--|--|
| `<keyname>` | Specifies the full path of the subkey. The export operation only works with the local computer. The *keyname* must include a valid root key. Valid root keys for the local computer are: **HKLM**, **HKCU**, **HKCR**, **HKU**, and **HKCC**. If the registry key name contains a space, enclose the key name in quotes. |
| `<filename>` | Specifies the name and path of the file to be created during the operation. The file must have a .reg extension. |
| /y | Overwrites any existing file with the name *filename* without prompting for confirmation. |
| /? | Displays help at the command prompt. |

#### Remarks

- The return values for the **reg export** operation are:

    | Value | Description |
    |--|--|
    | 0 | Success |
    | 1 | Failure |

### Examples

To export the contents of all subkeys and values of the key MyApp to the file AppBkUp.reg, type:

```
reg export HKLM\Software\MyCo\MyApp AppBkUp.reg
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
