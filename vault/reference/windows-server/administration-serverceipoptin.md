---
title: "serverceipoptin"
type: reference
domain: windows-server
slug: administration-serverceipoptin
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/serverceipoptin
family: administration
documentKind: "reference"
abstract: "Reference article for the serverceipoptin, which allows you to participate in the Customer Experience Improvement Program (CEIP)."
---

# serverceipoptin

# serverceipoptin



Allows you to participate in the Customer Experience Improvement Program (CEIP).

## Syntax

```
serverceipoptin [/query] [/enable] [/disable]
```

### Parameters

| Parameter | Description |
|--|--|
| /query | Verifies your current setting. |
| /enable | Turns on your participation in CEIP. |
| /disable | Turns off your participation in CEIP. |
| /? | Displays help at the command prompt. |

## Examples

To verify your current settings, type:

```
serverceipoptin /query
```

To turn on your participation, type:

```
serverceipoptin /enable
```

To turn off your participation, type:

```
serverceipoptin /disable
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
