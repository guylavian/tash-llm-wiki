---
title: "ksetup domain"
type: reference
domain: windows-server
slug: administration-ksetup-domain
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ksetup-domain
family: administration
documentKind: "reference"
abstract: "Reference article for the ksetup domain command, which sets the domain name for all Kerberos operations."
---

# ksetup domain

# ksetup domain

Sets the domain name for all Kerberos operations.

## Syntax

```
ksetup /domain <domainname>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<domainname>` | Name of the domain to which you want to establish a connection. Use the fully-qualified domain name or a simple form of the name, such as contoso.com or contoso.|

### Examples

To establish a connection to a valid domain, such as Microsoft, by using the `ksetup /mapuser` subcommand, type:

```
ksetup /mapuser principal@realm domain-user /domain domain-name
```

After a successful connection, you'll receive a new TGT or an existing TGT will be refreshed.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [ksetup command](ksetup.md)

- [ksetup mapuser command](ksetup-mapuser.md)
