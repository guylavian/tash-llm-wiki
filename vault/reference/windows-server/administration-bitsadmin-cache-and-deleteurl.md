---
title: "bitsadmin cache and deleteURL"
type: reference
domain: windows-server
slug: administration-bitsadmin-cache-and-deleteurl
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-cache-and-deleteurl
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin cache and deleteURL command, which deletes all cache entries for the given URL."
---

# bitsadmin cache and deleteURL

# bitsadmin cache and deleteURL

Deletes all cache entries for the given URL.

## Syntax

```
bitsadmin /deleteURL URL
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| URL | The Uniform Resource Locator that identifies a remote file. |

## Examples

To delete all cache entries for `https://www.contoso.com/en/us/default.aspx`:

```
bitsadmin /deleteURL https://www.contoso.com/en/us/default.aspx
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin cache command](bitsadmin-cache.md)
