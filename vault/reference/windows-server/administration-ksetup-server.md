---
title: "ksetup server"
type: reference
domain: windows-server
slug: administration-ksetup-server
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ksetup-server
family: administration
documentKind: "reference"
abstract: "Reference article for the ksetup server command, which allows you to specify a name for a computer running the Windows operating system, so changes made by the ksetup command update the target computer."
---

# ksetup server

# ksetup server

Allows you to specify a name for a computer running the Windows operating system, so changes made by the **ksetup** command update the target computer.

The target server name is stored in the registry under `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\LSA\Kerberos`. This entry isn't reported when you run the **ksetup** command.

> [!IMPORTANT]
> There's no way to remove the targeted server name. Instead, you can change it back to the local computer name, which is the default.

## Syntax

```
ksetup /server <servername>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<servername>` | Specifies the full computer name on which the configuration will be effective, such as *IPops897.corp.contoso.com*.<p>If an incomplete fully-qualified domain computer name is specified, the command will fail. |

### Examples

To make your **ksetup** configurations effective on the *IPops897* computer, which is connected on the Contoso domain, type:

```
ksetup /server IPops897.corp.contoso.com
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ksetup command](ksetup.md)
