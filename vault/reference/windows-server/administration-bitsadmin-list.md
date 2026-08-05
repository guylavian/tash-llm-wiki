---
title: "bitsadmin list"
type: reference
domain: windows-server
slug: administration-bitsadmin-list
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-list
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin list command, which lists the transfer jobs owned by the current user."
---

# bitsadmin list

# bitsadmin list

Lists the transfer jobs owned by the current user.

## Syntax

```
bitsadmin /list [/allusers][/verbose]
```

### Parameters

| Parameter | Description |
| -------------- | -------------- |
| /allusers | Optional. Lists jobs for all users. You must have administrator privileges to use this parameter. |
| /verbose | Optional. Provides detailed information about each job. |

## Examples

To retrieve information about jobs owned by the current user.

```
bitsadmin /list
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
