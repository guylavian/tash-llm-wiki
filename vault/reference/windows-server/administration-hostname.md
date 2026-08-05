---
title: "hostname"
type: reference
domain: windows-server
slug: administration-hostname
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/hostname
family: administration
documentKind: "reference"
abstract: "Reference article for the hostname command, which displays the host name portion of the full computer name of the computer."
---

# hostname

# hostname



Displays the host name portion of the full computer name of the computer.

>[!IMPORTANT]
> This command is available only if the Internet Protocol (TCP/IP) protocol is installed as a component in the properties of a network adapter in Network.

## Syntax

```
hostname
```

### Parameters

| Parameter | Description |
| ------- | -------- |
| /? | Displays help at the command prompt. |

Any parameter different than `/?` produces an error message and sets the errorlevel to 1.

### Notes

- Environment variable `%COMPUTERNAME%` usually will print the same string as `hostname`, but in uppercase.
- If environment variable `_CLUSTER_NETWORK_NAME_` is defined, `hostname` will print its value.

### Examples

- To display the name of the computer, type:

```shell
hostname
```

- To display the name of the computer in uppercase:

```shell
echo %COMPUTERNAME%
```

- To alter the hostname output:

```shell
set "_CLUSTER_NETWORK_NAME_=Altered Computer Name"
hostname
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
