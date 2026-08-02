---
title: "Approve-SPOTenantServicePrincipalPermissionRequest"
type: reference
domain: powershell
slug: spps-approve-spotenantserviceprincipalpermissionrequest
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Approve-SPOTenantServicePrincipalPermissionRequest
family: spps
documentKind: "doc"
---

# Approve-SPOTenantServicePrincipalPermissionRequest

# Approve-SPOTenantServicePrincipalPermissionRequest

## SYNOPSIS

Approves a permission request for the current tenant's "SharePoint Online Client" service principal

## SYNTAX

```
Approve-SPOTenantServicePrincipalPermissionRequest -RequestId <Guid> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## DESCRIPTION

Approves a permission request for the current tenant's "SharePoint Online Client" service principal

The return value of a successful call is a permission grant object. See the [Description section of Get-SPOTenantServicePrincipalPermissionGrants](/powershell/module/microsoft.online.sharepoint.powershell/get-spotenantserviceprincipalpermissiongrants#description) for more information about a permission grant object.

To get the collection of permission grants for the "SharePoint Online Client" service principal, use the [Get-SPOTenantServicePrincipalPermissionGrants](/powershell/module/microsoft.online.sharepoint.powershell/get-spotenantserviceprincipalpermissiongrants) command.

Approving a permission request also removes that request from the list of permission requests.

## EXAMPLES

### EXAMPLE 1

```powershell
$requests = Get-SPOTenantServicePrincipalPermissionRequests
$requestToApprove = $requests | ? { $_.Resource -eq 'Office 365 SharePoint Online' -and $_.Scope -eq 'MyFiles.Read' } | Select-Object -First 1

if ($requestToApprove -ne $null)
{
    Approve-SPOTenantServicePrincipalPermissionRequest -RequestId $requestToApprove.Id
}
```

Approves the permission request for the 'Office 365 SharePoint Online' resource with scope claim 'MyFiles.Read'.
If there is no request with those properties, then no approve action will be taken.

## PARAMETERS

### -RequestId

The ID of the permission request to approve

```yaml
Type: System.Guid
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
