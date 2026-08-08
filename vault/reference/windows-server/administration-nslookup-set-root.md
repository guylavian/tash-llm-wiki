---
title: "nslookup set root"
type: reference
domain: windows-server
slug: administration-nslookup-set-root
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup-set-root
family: administration
documentKind: "reference"
abstract: "Reference article for the nslookup set root command, which changes the name of the root server that's used for queries."
---

# nslookup set root

# nslookup set root



Changes the name of the root server used for queries.

> [!NOTE]
> This command supports the [nslookup root](nslookup-root.md) command.

## Syntax

```
set root=<rootserver>
```

### Parameters

| Parameter | Description |
| ---------- | ---------- |
| `<rootserver>` | Specifies the new name for the root server. The default value is **ns.nic.ddn.mil**. |
| /? | Displays help at the command prompt. |
| /help | Displays help at the command prompt. |

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [nslookup root](nslookup-root.md)
