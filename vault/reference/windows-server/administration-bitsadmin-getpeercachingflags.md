---
title: "bitsadmin getpeercachingflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-getpeercachingflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getpeercachingflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getpeercachingflags command, which retrieves flags that determine if the files of the job can be cached and served to peers, and if BITS can download content for the job from peers."
---

# bitsadmin getpeercachingflags

# bitsadmin getpeercachingflags



Retrieves flags that determine if the files of the job can be cached and served to peers, and if BITS can download content for the job from peers.

## Syntax

```
bitsadmin /getpeercachingflags <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the flags for the job named *myDownloadJob*:

```
bitsadmin /getpeercachingflags myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
