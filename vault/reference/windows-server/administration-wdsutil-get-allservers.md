---
title: "get-AllServers"
type: reference
domain: windows-server
slug: administration-wdsutil-get-allservers
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil-get-allservers
family: administration
documentKind: "reference"
abstract: "Reference article for get-AllServers, which retrieves information about all Windows Deployment Services servers."
---

# get-AllServers

# get-AllServers

Retrieves information about all Windows Deployment Services servers.

> [!NOTE]
> This command may take an extended amount of time to complete if there are many Windows Deployment Services servers in your environment or if the network connection linking the servers is slow.

## Syntax

```
wdsutil [Options] /Get-AllServers /Show:{Config | Images | All} [/Detailed] [/Forest:{Yes | No}]
```

### Parameters

|   Parameter   |                                                                                                                 Description                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /Show:{Config |                                                                                                                    Images                                                                                                                    |
|  [/Detailed]  | When used in conjunction with the **/Show:Images** or **/Show:All**, returns all image metadata from each image. If the **/Detailed** option is not specified, the default behavior is to return the image name, description, and file name. |
| [/Forest:{Yes |                                                                                                                     No}]                                                                                                                     |

## Examples

To view information about all servers, type:
```
wdsutil /Get-AllServers /Show:Config
```
To view detailed information about all servers, type:
```
wdsutil /Verbose /Get-AllServers /Show:All /Detailed /Forest:Yes
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
