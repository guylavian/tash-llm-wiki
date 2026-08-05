---
title: "sc delete"
type: reference
domain: windows-server
slug: administration-sc-delete
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-delete
family: administration
documentKind: "reference"
abstract: "Reference article for the sc delete command, which deletes a service subkey from the registry."
---

# sc delete

# sc delete

Deletes a service subkey from the registry. If the service is running or if another process has an open handle to the service, the service is marked for deletion.

> [!NOTE]
> We don't recommend you to use this command to delete built-in operating system services such as DHCP, DNS, or Internet Information Services. To install, remove, or reconfigure operating system roles, services and components, see [Install or Uninstall Roles, Role Services, or Features](/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features)

## Syntax

```
sc <server> delete [service name]
```

### Parameters

| Parameter | Description |
|--|--|
| `<server>` | Specifies the name of the remote server on which the service is located. The name must use the Universal Naming Convention (UNC) format (for example, \\\MyServer). To run `sc` locally, don't use this parameter. |
| `<service name>` | Specifies the service name returned by the **getkeyname** operation. |
| /? | Displays help at the command prompt. |

## Examples

To delete the service subkey **NewServ** from the registry on the local computer, type:

```
sc delete NewServ
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)
