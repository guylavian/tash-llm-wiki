---
title: "telnet unset"
type: reference
domain: windows-server
slug: administration-telnet-unset
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/telnet-unset
family: administration
documentKind: "reference"
abstract: "Reference article for the telnet unset command, which turns off previously set options."
---

# telnet unset

# telnet: unset



Turns off previously set options.

## Syntax

```
u {bsasdel | crlf | delasbs | escape | localecho | logging | ntlm} [?]
```

### Parameters

| Parameter | Description |
|--|--|
| bsasdel | Sends **backspace** as a **backspace**. |
| crlf | Sends the **Enter** key as a CR. Also known as line feed mode. |
| delasbs | Sends **delete** as **delete**. |
| escape | Removes the escape character setting. |
| localecho | Turns off localecho. |
| logging | Turns off logging. |
| ntlm | Turns off NTLM authentication. |
| ? | Displays help for this command. |

## Example

Turn off logging.

```
u logging
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
