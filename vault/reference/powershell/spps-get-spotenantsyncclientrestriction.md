---
title: "Get-SPOTenantSyncClientRestriction"
type: reference
domain: powershell
slug: spps-get-spotenantsyncclientrestriction
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOTenantSyncClientRestriction
family: spps
documentKind: "doc"
---

# Get-SPOTenantSyncClientRestriction

# Get-SPOTenantSyncClientRestriction

## SYNOPSIS

Returns the current configuration status.

## SYNTAX

```
Get-SPOTenantSyncClientRestriction [<CommonParameters>]
```

## DESCRIPTION

The `Get-SPOTenantSyncClientRestriction` cmdlet returns whether the TenantRestrictionEnabled property is true or false and DomainGUIDs that are currently in the safe recipient list which is represented by the AllowedDomainList property.

This cmdlet, that does not take any input, also returns the current state of the BlockMacSync and GrooveBlockOption properties.

You must be at least a SharePoint Online administrator to run the cmdlet.

Requires a valid `Connect-SPOService` context to identify the tenant. For information on how to connect to the tenant, see `Connect-SPOService`.

## EXAMPLES

### EXAMPLE 1

```powershell
Get-SPOTenantSyncClientRestriction
```

This example returns a current boolean value of the TenantRestrictionEnabled and BlockMacSync properties and a current set list of domains GUIDs in the AllowedDomainList property.

## PARAMETERS

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
