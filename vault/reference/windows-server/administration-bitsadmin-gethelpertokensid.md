---
title: "bitsadmin gethelpertokensid"
type: reference
domain: windows-server
slug: administration-bitsadmin-gethelpertokensid
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-gethelpertokensid
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin gethelpertokensid command, which returns the SID of a BITS transfer job's helper token, if one is set."
---

# bitsadmin gethelpertokensid

# bitsadmin gethelpertokensid

Returns the SID of a BITS transfer job's [helper token](/windows/win32/bits/helper-tokens-for-bits-transfer-jobs), if one is set.

> [!NOTE]
> This command isn't supported by BITS 3.0 and earlier.

## Syntax

```
bitsadmin /gethelpertokensid <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the SID of a BITS transfer job named *myDownloadJob*:

```
bitsadmin /gethelpertokensid myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
