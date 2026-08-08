---
title: "bitsadmin cache and info"
type: reference
domain: windows-server
slug: administration-bitsadmin-cache-and-info
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cache-and-info
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cache and info command, which dumps a specific cache entry."
---

# bitsadmin cache and info

# bitsadmin cache and info

Dumps a specific cache entry.

## Syntax

```
bitsadmin /cache /info recordID [/verbose]
```

### Parameters

| Paramreter | Description |
| -------------- | -------------- |
| recordID | The GUID associated with the cache entry. |

## Examples

To dump the cache entry with the recordID value of {6511FB02-E195-40A2-B595-E8E2F8F47702}:

```
bitsadmin /cache /info {6511FB02-E195-40A2-B595-E8E2F8F47702}
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin cache command](bitsadmin-cache.md)
