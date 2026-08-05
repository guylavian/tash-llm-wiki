---
title: "ftp user"
type: reference
domain: windows-server
slug: administration-ftp-user
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ftp-user
family: administration
documentKind: "reference"
abstract: "Reference article for the ftp user command, which specifies a user to the remote computer."
---

# ftp user

# ftp user



Specifies a user to the remote computer.

## Syntax

```
user <username> [<password>] [<account>]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<username>` | Specifies a user name with which to log on to the remote computer. |
| `[<password>]` | Specifies the password for *username*. If a password is not specified but is required, the **ftp** command prompts for the password. |
| `[<account>]` | Specifies an account with which to log on to the remote computer. If an *account* isn't specified but is required, the **ftp** command prompts for the account. |

### Examples

To specify *User1* with the password *Password1*, type:

```
user User1 Password1
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [Additional FTP guidance](/previous-versions/orphan-topics/ws.10/cc756013(v=ws.10))
