---
title: "logman query"
type: reference
domain: windows-server
slug: administration-logman-query
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman-query
family: administration
documentKind: "reference"
abstract: "Reference article for the logman query command, which queries data collector or data collector set properties."
---

# logman query

# logman query



Queries data collector or data collector set properties.

## Syntax

```
logman query [providers|Data Collector Set name] [options]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| -s `<computer name>` | Perform the command on the specified remote computer. |
| -config `<value>` | Specifies the settings file containing command options. |
| [-n] `<name>` | Name of the target object. |
| -ets | Sends commands to Event Trace Sessions directly without saving or scheduling. |
| /? | Displays context-sensitive help. |

### Examples

To list all Data Collector Sets configured on the target system, type:

```
logman query
```

To list the data collectors contained in the Data Collector Set named *perf_log*, type:

```
logman query perf_log
```

To list all available providers of data collectors on the target system, type:

```
logman query providers
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [logman command](logman.md)
