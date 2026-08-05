---
title: "bitsadmin cache and delete"
type: reference
domain: windows-server
slug: administration-bitsadmin-cache-and-delete
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cache-and-delete
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cache and delete command, which deletes a specific cache entry."
---

# bitsadmin cache and delete

# bitsadmin cache and delete

Deletes a specific cache entry.

## Syntax

```
bitsadmin /cache /delete recordID
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| recordID | The GUID associated with the cache entry. |

## Examples

To delete the cache entry with the RecordID of {6511FB02-E195-40A2-B595-E8E2F8F47702}:

```
bitsadmin /cache /delete {6511FB02-E195-40A2-B595-E8E2F8F47702}
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin cache command](bitsadmin-cache.md)
