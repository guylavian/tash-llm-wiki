---
title: "manage-bde tpm"
type: reference
domain: windows-server
slug: administration-manage-bde-tpm
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-tpm
family: administration
documentKind: "reference"
abstract: "Reference article for the manage-bde tpm command, which configures the computer's Trusted Platform Module (TPM)."
---

# manage-bde tpm

# manage-bde tpm



Configures the computer's Trusted Platform Module (TPM).

## Syntax

```
manage-bde -tpm [-turnon] [-takeownership <ownerpassword>] [-computername <name>] [{-?|/?}] [{-help|-h}]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| -turnon | Enables and activates the TPM, allowing the TPM owner password to be set. You can also use **-t** as an abbreviated version of this command. |
| -takeownership | Takes ownership of the TPM by setting an owner password. You can also use **-o** as an abbreviated version of this command. |
| `<ownerpassword>` | Represents the owner password that you specify for the TPM. |
| -computername | Specifies that manage-bde.exe is used to modify BitLocker protection on a different computer. You can also use **-cn** as an abbreviated version of this command. |
| `<name>` | Represents the name of the computer on which to modify BitLocker protection. Accepted values include the computer's NetBIOS name and the computer's IP address. |
| -? or /? | Displays brief Help at the command prompt. |
| -help or -h | Displays complete Help at the command prompt. |

### Examples

To turn on the TPM, type:

```
manage-bde -tpm -turnon
```

To take ownership of the TPM and set the owner password to *0wnerP@ss*, type:

```
manage-bde -tpm -takeownership 0wnerP@ss
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [TPM Management cmdlets for Windows PowerShell](/powershell/module/trustedplatformmodule/)

- [manage-bde command](manage-bde.md)
