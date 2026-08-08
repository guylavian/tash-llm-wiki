---
title: "bitsadmin geterrorcount"
type: reference
domain: windows-server
slug: administration-bitsadmin-geterrorcount
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-geterrorcount
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin geterrorcount command, which retrieves a count of the number of times the specified job generated a transient error."
---

# bitsadmin geterrorcount

# bitsadmin geterrorcount

Retrieves a count of the number of times the specified job generated a transient error.

## Syntax

```
bitsadmin /geterrorcount <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve error count information for the job named *myDownloadJob*:

```
bitsadmin /geterrorcount myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
