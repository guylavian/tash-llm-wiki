---
title: "Get-SPOTenantContentTypeReplicationParameters"
type: reference
domain: powershell
slug: spps-get-spotenantcontenttypereplicationparameters
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOTenantContentTypeReplicationParameters
family: spps
documentKind: "doc"
---

# Get-SPOTenantContentTypeReplicationParameters

# Get-SPOTenantContentTypeReplicationParameters

## SYNOPSIS

Gets content types for replication parameters

## SYNTAX

```
Get-SPOTenantContentTypeReplicationParameters [<CommonParameters>]
```

## DESCRIPTION

Before you run the cmdlets, please use `Connect-SPOService` to connect to SharePoint Online first.
This Cmdlets gets the content types that are being replicated from primary location to satellite

## EXAMPLES

### Example 1

```powershell
Get-SPOTenantContentTypeReplicationParameters
```

Gets content types for replication parameters

## PARAMETERS

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Introduction to the SharePoint Online management shell](https://support.office.com/en-us/article/introduction-to-the-sharepoint-online-management-shell-c16941c3-19b4-4710-8056-34c034493429)

[SharePoint Online Management Shell Download](https://www.microsoft.com/en-US/download/details.aspx?id=35588)

[Get-SPOAppErrors](Get-SPOAppErrors.md)

[Get-SPOTenantTaxonomyReplicationParameters](Get-SPOTenantTaxonomyReplicationParameters.md)

[Set-SPOTenantTaxonomyReplicationParameters](Set-SPOTenantTaxonomyReplicationParameters.md)

[Set-SPOTenantContentTypeReplicationParameters](Set-SPOTenantContentTypeReplicationParameters.md)
