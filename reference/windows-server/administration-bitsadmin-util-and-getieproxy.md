---
title: "bitsadmin util and getieproxy"
type: reference
domain: windows-server
slug: administration-bitsadmin-util-and-getieproxy
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-util-and-getieproxy
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin util and getieproxy command, which retrieves the proxy usage for the given service account."
---

# bitsadmin util and getieproxy

# bitsadmin util and getieproxy



Retrieves the proxy usage for the given service account. This command shows the value for each proxy usage, not just the proxy usage you specified for the service account. For details about setting the proxy usage for specific service accounts, see the [bitsadmin util and setieproxy](bitsadmin-util-and-setieproxy.md) command.

## Syntax

```
bitsadmin /util /getieproxy <account> [/conn <connectionname>]
```

### Parameters

| Parameter | Description |
| --------- | ---------- |
| account | Specifies the service account whose proxy settings you want to retrieve. Possible values include:<ul><li>LOCALSYSTEM</li><li>   NETWORKSERVICE</li><li>LOCALSERVICE.</li></ul> |
| connectionname | Optional. Used with the **/conn** parameter to specify which modem connection to use. If you don't specify the **/conn** parameter, BITS uses the LAN connection. |

## Examples

To display the proxy usage for the NETWORK SERVICE account:

```
bitsadmin /util /getieproxy NETWORKSERVICE
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin util command](bitsadmin-util.md)

- [bitsadmin command](bitsadmin.md)
