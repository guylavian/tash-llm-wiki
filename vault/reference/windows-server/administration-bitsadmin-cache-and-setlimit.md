---
title: "bitsadmin cache and setlimit"
type: reference
domain: windows-server
slug: administration-bitsadmin-cache-and-setlimit
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cache-and-setlimit
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cache and setlimit command, which sets the cache size limit."
---

# bitsadmin cache and setlimit

# bitsadmin cache and setlimit

Sets the cache size limit.

## Syntax

```
bitsadmin /cache /setlimit percent
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| percent | The cache limit defined as a percentage of the total hard disk space. |

## Examples

To set the cache size limit to 50%:

```
bitsadmin /cache /setlimit 50
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin cache command](bitsadmin-cache.md)
