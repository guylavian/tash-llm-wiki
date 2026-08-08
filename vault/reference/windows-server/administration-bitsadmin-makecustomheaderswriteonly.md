---
title: "bitsadmin makecustomheaderswriteonly"
type: reference
domain: windows-server
slug: administration-bitsadmin-makecustomheaderswriteonly
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-makecustomheaderswriteonly
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin makecustomheaderswriteonly command, which make a job's Custom HTTP Headers write-only."
---

# bitsadmin makecustomheaderswriteonly

# bitsadmin makecustomheaderswriteonly

Make a job's Custom HTTP Headers write-only.

> [!IMPORTANT]
> This action can't be undone.

## Syntax

```
bitsadmin /makecustomheaderswriteonly <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To make Custom HTTP Headers write-only for the job named *myDownloadJob*:

```
bitsadmin /makecustomheaderswriteonly myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
