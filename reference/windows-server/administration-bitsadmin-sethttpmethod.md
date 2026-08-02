---
title: "bitsadmin sethttpmethod"
type: reference
domain: windows-server
slug: administration-bitsadmin-sethttpmethod
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-sethttpmethod
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin sethttpmethod command, which sets the HTTP verb to use."
---

# bitsadmin sethttpmethod

# bitsadmin sethttpmethod

Sets the HTTP verb to use.

## Syntax

```
bitsadmin /sethttpmethod <job> <httpmethod>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| httpmethod | The HTTP verb to use. For information about available verbs, see [Method Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
