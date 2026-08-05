---
title: "bitsadmin peercaching and getconfigurationflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-peercaching-and-getconfigurationflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-peercaching-and-getconfigurationflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin peercaching and getconfigurationflags command, which gets the configuration flags that determine if the computer serves content to peers and if it can download content from peers."
---

# bitsadmin peercaching and getconfigurationflags

# bitsadmin peercaching and getconfigurationflags

Gets the configuration flags that determine if the computer serves content to peers and if it can download content from peers.

## Syntax

```
bitsadmin /peercaching /getconfigurationflags <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To get the configuration flags for the job named *myDownloadJob*:

```
bitsadmin /peercaching /getconfigurationflags myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)

- [bitsadmin peercaching command](bitsadmin-peercaching.md)
