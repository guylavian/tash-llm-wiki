---
title: "bitsadmin getnotifyinterface"
type: reference
domain: windows-server
slug: administration-bitsadmin-getnotifyinterface
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getnotifyinterface
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getnotifyinterface command, which determines if another program has registered a COM callback interface for the specified job."
---

# bitsadmin getnotifyinterface

# bitsadmin getnotifyinterface

Determines whether another program has registered a COM callback interface (the notify interface) for the specified job.

## Syntax

```
bitsadmin /getnotifyinterface <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

#### Output

The output for this command displays either, **Registered** or **Unregistered**.

> [!NOTE]
> It's not possible to determine the program that registered the callback interface.

## Examples

To retrieve the notify interface for the job named *myDownloadJob*:

```
bitsadmin /getnotifyinterface myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
