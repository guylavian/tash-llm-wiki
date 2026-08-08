---
title: "nslookup ls"
type: reference
domain: windows-server
slug: administration-nslookup-ls
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup-ls
family: administration
documentKind: "reference"
abstract: "Reference article for the nslookup ls command, which lists DNS domain information."
---

# nslookup ls

# nslookup ls



Lists DNS domain information.

## Syntax

```
ls [<option>] <DNSdomain> [{[>] <filename>|[>>] <filename>}]
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| `<option>` | The valid options include:<ul><li>**-t:** Lists all records of the specified type. For more information, see [nslookup set querytype](nslookup-set-querytype.md).</li><li>**-a:** Lists aliases of computers in the DNS domain. This parameter is the same as **-t CNAME**</li><li>**-d:** Lists all records for the DNS domain. This parameter is the same as **-t ANY**</li><li>**-h:** Lists CPU and operating system information for the DNS domain. This parameter is the same as **-t HINFO**</li><li>**-s:** Lists well-known services of computers in the DNS domain. This parameter is the same as **-t WKS**. |
| `<DNSdomain>` | Specifies the DNS domain for which you want information. |
| `<filename>` | Specifies a file name to use for the saved output. You can use the greater than (`>`) and double greater than (`>>`) characters to redirect the output in the usual manner. |
| /? | Displays help at the command prompt. |
| /help | Displays help at the command prompt. |

#### Remarks

- The default output of this command includes computer names and their associated IP addresses.

- If your output is directed to a file, hash marks are added for every 50 records received from the server.

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [nslookup set querytype](nslookup-set-querytype.md)
