---
title: "Get-SPOCustomCdnTenantApps"
type: reference
domain: powershell
slug: spps-get-spocustomcdntenantapps
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOCustomCdnTenantApps
family: spps
documentKind: "doc"
---

# Get-SPOCustomCdnTenantApps

# Get-SPOCustomCdnTenantApps

## SYNOPSIS

Retrieves all apps that use a custom content delivery network (CDN) from the Tenant App Catalog.

## SYNTAX

```
Get-SPOCustomCdnTenantApps [<CommonParameters>]
```

## DESCRIPTION

Retrieves all apps from the Tenant App Catalog that are configured to use a custom CDN. The output includes the product ID and title of each app.

## EXAMPLES

### EXAMPLE 1

```powershell
Get-SPOCustomCdnTenantApps
```

This example returns a list of all apps in the Tenant App Catalog that use a custom CDN.

## PARAMETERS

### CommonParameters

This cmdlet supports the common parameters: `-Debug`, `-ErrorAction`, `-ErrorVariable`, `-InformationAction`, `-InformationVariable`, `-OutVariable`, `-OutBuffer`, `-PipelineVariable`, `-ProgressAction`, `-Verbose`, `-WarningAction`, and `-WarningVariable`. For more information, see [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Get-SPOCustomCdnSiteCollectionApps](Get-SPOCustomCdnSiteCollectionApps.md)
