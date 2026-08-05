---
title: "Get-SPOSiteCollectionAppCatalogs"
type: reference
domain: powershell
slug: spps-get-spositecollectionappcatalogs
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOSiteCollectionAppCatalogs
family: spps
documentKind: "doc"
---

# Get-SPOSiteCollectionAppCatalogs

# Get-SPOSiteCollectionAppCatalogs

## SYNOPSIS

Use this cmdlet to get the Site Collection App Catalog.

## SYNTAX

```
Get-SPOSiteCollectionAppCatalogs [-Site] <SpoSitePipeBind> [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to get the Site Collection App Catalog. For more information, see [Use the App Catalog to make custom business apps available for your SharePoint environment](/sharepoint/use-app-catalog)

## EXAMPLES

### Example 1

```powershell
 Get-SPOSiteCollectionAppCatalogs -Site https://contoso.sharepoint.com/sites/Research
```

This example returns the Site Collection App Catalog for the site <https://contoso.sharepoint.com/sites/Research.>

## PARAMETERS

### -Site

> Applicable: SharePoint Online

Url of the site

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.SpoSitePipeBind
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/p/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
