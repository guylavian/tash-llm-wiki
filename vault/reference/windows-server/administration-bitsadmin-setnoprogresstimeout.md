---
title: "bitsadmin setnoprogresstimeout"
type: reference
domain: windows-server
slug: administration-bitsadmin-setnoprogresstimeout
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-setnoprogresstimeout
family: administration
documentKind: "reference"
abstract: "Reference article for the bitsadmin setnoprogresstimeout command, which sets the length of time, in seconds, that the service tries to transfer the file after a transient error occurs."
---

# bitsadmin setnoprogresstimeout

# bitsadmin setnoprogresstimeout

Sets the length of time, in seconds, that BITS tries to transfer the file after the first transient error occurs.

## Syntax

```
bitsadmin /setnoprogresstimeout <job> <timeoutvalue>
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| job | The job's display name or GUID. |
| timeoutvalue | The length of time that BITS waits to transfer a file after the first error, in seconds. |

### Remarks

- The "no progress" timeout interval begins when the job encounters its first transient error.

- The timeout interval stops or resets when a byte of data is successfully transferred.

- If the "no progress" timeout interval exceeds the *timeoutvalue*, then the job is placed in a fatal error state.

## Examples

To set the "no progress" timeout value to 20 seconds, for the job named *myDownloadJob*:

```
bitsadmin /setnoprogresstimeout myDownloadJob 20
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [bitsadmin command](bitsadmin.md)
