---
title: "netsh set"
type: reference
domain: windows-server
slug: administration-netsh-set
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-set
family: administration
documentKind: "reference"
abstract: "The netsh set command targets local or remote devices to perform network configuration tasks in Windows."
---

# netsh set

# netsh set

The `netsh set` command allows administrators to specify the target machine for subsequent network configuration tasks, enabling operations on either local or remote systems. If a machine name isn't specified, the local machine is used. A username and password can't be used to connect to the local machine.

## Syntax

```
netsh set machine [name=]<string> [user=][[DomainName\]UserName] [pwd=][Password | *]
```

## Parameters

| Parameter | Description |
|--|--|
| `<name>` | Specifies the device name or network address of the machine on which you want to perform actions. |
| `<user>` | Provides the username credentials required to authenticate and connect to the remote machine. If your network uses a domain, specify the username in the format `DomainName\UserName`. |
| `<pwd>` | Supplies the password associated with the specified user account. If you enter an asterisk (`*`) instead of a password, you're prompted to input the password interactively for added security. |

## Examples

To specify a target machine using its IP address in a domain environment where the password is prompted, run the following command:

```cmd
netsh set machine name=192.168.1.10 user=DOMAIN\Admin pwd=*
```

## See also

- [Command-Line Syntax Key](command-line-syntax-key.md)
