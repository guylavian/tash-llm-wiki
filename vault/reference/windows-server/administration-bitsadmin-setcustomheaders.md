---
title: "bitsadmin setcustomheaders"
type: reference
domain: windows-server
slug: administration-bitsadmin-setcustomheaders
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setcustomheaders
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setcustomheaders command, which adds a custom HTTP header to a GET request."
---

# bitsadmin setcustomheaders

# bitsadmin setcustomheaders

Add a custom HTTP header to a GET request sent to an HTTP server. For more information about GET requests, see [Method Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html#sec9.3) and [Header Field Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).

## Syntax

```
bitsadmin /setcustomheaders <job> <header1> <header2> <...>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| `<header1> <header2>` and so on | The custom headers for the job. |

## Examples

To add a custom HTTP header for the job named *myDownloadJob*:

```
bitsadmin /setcustomheaders myDownloadJob accept-encoding:deflate/gzip
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
