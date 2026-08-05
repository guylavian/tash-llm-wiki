---
title: "bitsadmin getproxyusage"
type: reference
domain: windows-server
slug: administration-bitsadmin-getproxyusage
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-getproxyusage
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin getproxyusage command, which retrieves the proxy usage setting for the specified job."
---

# bitsadmin getproxyusage

# bitsadmin getproxyusage

Retrieves the proxy usage setting for the specified job.

## Syntax

```
bitsadmin /getproxyusage <job>
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| job | The job's display name or GUID. |

#### Output

The returned proxy usage values can be:

- **Preconfig** - Use the owner's Internet Explorer defaults.

- **No_Proxy** - Don't use a proxy server.

- **Override** - Use an explicit proxy list.

- **Autodetect** - Automatically detect the proxy settings.

## Examples

To retrieve the proxy usage for the job named *myDownloadJob*:

```
bitsadmin /getproxyusage myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
