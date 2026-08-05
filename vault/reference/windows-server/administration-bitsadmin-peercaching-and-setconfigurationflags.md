---
title: "bitsadmin peercaching and setconfigurationflags"
type: reference
domain: windows-server
slug: administration-bitsadmin-peercaching-and-setconfigurationflags
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-peercaching-and-setconfigurationflags
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin peercaching and setconfigurationflags command, which sets the configuration flags that determine if the computer can serve content to peers and if it can download content from peers."
---

# bitsadmin peercaching and setconfigurationflags

# bitsadmin peercaching and setconfigurationflags

Sets the configuration flags that determine if the computer can serve content to peers and if it can download content from peers.

## Syntax

```
bitsadmin /peercaching /setconfigurationflags <job> <value>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |
| value | An unsigned integer with the following interpretation for the bits in the binary representation:<ul><li>To allow the job's data to be downloaded from a peer, set the least significant bit.</li><li>To allow the job's data to be served to peers, set the second bit from the right.</li></ul>|

## Examples

To specify the job's data to be downloaded from peers for the job named *myDownloadJob*:

```
bitsadmin /peercaching /setconfigurationflags myDownloadJob 1
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)

- [bitsadmin peercaching command](bitsadmin-peercaching.md)
