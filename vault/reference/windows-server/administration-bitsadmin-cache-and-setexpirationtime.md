---
title: "bitsadmin cache and setexpirationtime"
type: reference
domain: windows-server
slug: administration-bitsadmin-cache-and-setexpirationtime
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cache-and-setexpirationtime
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cache and setexpirationtime command, which sets the cache expiration time."
---

# bitsadmin cache and setexpirationtime

# bitsadmin cache and setexpirationtime



Sets the cache expiration time.

## Syntax

```
bitsadmin /cache /setexpirationtime secs
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| secs | The number of seconds until the cache expires. |

## Examples

To set the cache to expire in 60 seconds:

```
bitsadmin /cache / setexpirationtime 60
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin cache command](bitsadmin-cache.md)
