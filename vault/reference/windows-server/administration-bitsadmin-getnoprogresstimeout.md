---
title: "bitsadmin getnoprogresstimeout"
type: reference
domain: windows-server
slug: administration-bitsadmin-getnoprogresstimeout
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getnoprogresstimeout
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getnoprogresstimeout command, which retrieves the length of time, in seconds, that the service will try to transfer the file after a transient error occurs."
---

# bitsadmin getnoprogresstimeout

# bitsadmin getnoprogresstimeout

Retrieves the length of time, in seconds, that the service will try to transfer the file after a transient error occurs.

## Syntax

```
bitsadmin /getnoprogresstimeout <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the progress time out value for the job named *myDownloadJob*:

```
bitsadmin /getnoprogresstimeout myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
