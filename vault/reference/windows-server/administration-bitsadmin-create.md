---
title: "bitsadmin create"
type: reference
domain: windows-server
slug: administration-bitsadmin-create
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-create
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin create command, which creates a transfer job with the given display name."
---

# bitsadmin create

# bitsadmin create



Creates a transfer job with the given display name.

> [!NOTE]
> The **/Upload** and **/Upload-Reply** parameter types aren't supported by BITS 1.2 and earlier.

## Syntax

```
bitsadmin /create [type] displayname
```

### Parameters

| Parameter | Description |
| ------- | -------- |
| type | There are three types of jobs:<ul><li>**/Download.** Transfers data from a server to a local file.</li><li>**/Upload.** Transfers data from a local file to a server.</li><li>**/Upload-Reply.** Transfers data from a local file to a server and receives a reply file from the server.</li></ul>This parameter defaults to **/Download** if it's not specified. |
| displayname | The display name assigned to the newly created job. |

## Examples

To create a download job named *myDownloadJob*:

```
bitsadmin /create myDownloadJob
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin resume command](bitsadmin-resume.md)

- [bitsadmin command](bitsadmin.md)
