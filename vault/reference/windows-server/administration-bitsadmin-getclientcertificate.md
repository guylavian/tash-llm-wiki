---
title: "bitsadmin getclientcertificate"
type: reference
domain: windows-server
slug: administration-bitsadmin-getclientcertificate
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getclientcertificate
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getclientcertificate command, which retrieves the client certificate from the job."
---

# bitsadmin getclientcertificate

# bitsadmin getclientcertificate

Retrieves the client certificate from the job.

## Syntax

```
bitsadmin /getclientcertificate <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

## Examples

To retrieve the client certificate for the job named *myDownloadJob*:

```
bitsadmin /getclientcertificate myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
