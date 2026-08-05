---
title: "nslookup set retry"
type: reference
domain: windows-server
slug: administration-nslookup-set-retry
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup-set-retry
family: administration
documentKind: "reference"
abstract: "Reference article for the nslookup set retry command, which sets the number of tries to get information from a specified server."
---

# nslookup set retry

# nslookup set retry



This command sets the number of times a request is resent to a server for information, before giving up.

> [!NOTE]
> To change the length of time before the request times out, use the [nslookup set timeout](nslookup-set-timeout.md) command.

## Syntax

```
set retry=<number>
```

### Parameters

| Parameter | Description |
| ---------- | ---------- |
| `<number>` | Specifies the new value for the number of retries. The default number of retries is **1**. |
| /? | Displays help at the command prompt. |
| /help | Displays help at the command prompt. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [nslookup set timeout](nslookup-set-timeout.md)
