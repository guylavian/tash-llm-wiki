---
title: "bitsadmin removeclientcertificate"
type: reference
domain: windows-server
slug: administration-bitsadmin-removeclientcertificate
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-removeclientcertificate
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin removeclientcertificate command, which removes the client certificate from the job."
---

# bitsadmin removeclientcertificate

# bitsadmin removeclientcertificate

Removes the client certificate from the job.

## Syntax

```
bitsadmin /removeclientcertificate <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To remove the client certificate from the job named *myDownloadJob*:

```
bitsadmin /removeclientcertificate myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
