---
title: "bitsadmin gethttpmethod"
type: reference
domain: windows-server
slug: administration-bitsadmin-gethttpmethod
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-gethttpmethod
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin gethttpmethod command, which gets the HTTP verb to use with the job."
---

# bitsadmin gethttpmethod

# bitsadmin gethttpmethod

Gets the HTTP verb to use with the job.

## Syntax

```
bitsadmin /gethttpmethod <Job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the HTTP verb to use with the job named *myDownloadJob*:

```
bitsadmin /gethttpmethod myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
