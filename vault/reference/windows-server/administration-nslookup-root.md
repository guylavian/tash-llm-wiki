---
title: "nslookup root"
type: reference
domain: windows-server
slug: administration-nslookup-root
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup-root
family: administration
documentKind: "reference"
abstract: "Reference article for the nslookup root command, which changes the default server to the server for the root of the Domain Name System (DNS) domain name space."
---

# nslookup root

# nslookup root



Changes the default server to the server for the root of the Domain Name System (DNS) domain name space. Currently, the ns.nic.ddn.mil name server is used. You can change the name of the root server using the [nslookup set root](nslookup-set-root.md) command.

> [!NOTE]
> This command is the same as `lserver ns.nic.ddn.mil`.

## Syntax

```
root
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| /? | Displays help at the command prompt. |
| /help | Displays help at the command prompt. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [nslookup set root](nslookup-set-root.md)
