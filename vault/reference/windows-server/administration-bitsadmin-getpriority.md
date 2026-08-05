---
title: "bitsadmin getpriority"
type: reference
domain: windows-server
slug: administration-bitsadmin-getpriority
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getpriority
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getpriority command, which retrieves the priority of the specified job."
---

# bitsadmin getpriority

# bitsadmin getpriority

Retrieves the priority of the specified job.

## Syntax

```
bitsadmin /getpriority <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

#### Output

The returned priority for this command can be:

- **FOREGROUND**

- **HIGH**

- **NORMAL**

- **LOW**

- **UNKNOWN**

## Examples

To retrieve the priority for the job named *myDownloadJob*:

```
bitsadmin /getpriority myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
