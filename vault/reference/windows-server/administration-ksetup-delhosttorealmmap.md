---
title: "ksetup delhosttorealmmap"
type: reference
domain: windows-server
slug: administration-ksetup-delhosttorealmmap
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ksetup-delhosttorealmmap
family: administration
documentKind: "reference"
abstract: "Reference article for the ksetup delhosttorealmmap command, which removes a service principal name (SPN) mapping between the stated host and the realm."
---

# ksetup delhosttorealmmap

# ksetup delhosttorealmmap

Removes a service principal name (SPN) mapping between the stated host and the realm. This command also removes any mapping between a host to realm (or multiple hosts to realm).

The mapping is stored in the registry, under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\HostToRealm`. After running this command, we recommend making sure the mapping appears in the registry.

## Syntax

```
ksetup /delhosttorealmmap <hostname> <realmname>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<hostname>` | Specifies the fully-qualified domain name of the computer. |
| `<realmname>` | Specifies the uppercase DNS name, such as CORP.CONTOSO.COM. |

### Examples

To change the configuration of the realm CONTOSO, and to delete the mapping of the host computer IPops897 to the realm, type:

```
ksetup /delhosttorealmmap IPops897 CONTOSO
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ksetup command](ksetup.md)

- [ksetup addhosttorealmmap command](ksetup-addhosttorealmmap.md)
