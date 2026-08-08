---
title: "nslookup set timeout"
type: reference
domain: windows-server
slug: administration-nslookup-set-timeout
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup-set-timeout
family: administration
documentKind: "reference"
abstract: "Reference article for the nslookup set timeout command, which changes the initial number of seconds to wait for a reply to a lookup request."
---

# nslookup set timeout

# nslookup set timeout



Changes the number of seconds to wait for a reply to a lookup request. Use the [nslookup set retry](nslookup-set-retry.md) command to determine the number of times to try to send the request.

## Syntax

```
set timeout=<number>
```

### Parameters

| Parameter | Description |
| ---------- | ---------- |
| `<number>` | Specifies the number of seconds to wait for a reply. The default number of seconds to wait is **2**. |
| /? | Displays help at the command prompt. |
| /help | Displays help at the command prompt. |

### Examples

To set the timeout for getting a response to 5 seconds:

```
set timeout=5
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [nslookup set retry](nslookup-set-retry.md)
