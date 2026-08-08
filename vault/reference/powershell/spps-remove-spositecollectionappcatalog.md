---
title: "Remove-SPOSiteCollectionAppCatalog"
type: reference
domain: powershell
slug: spps-remove-spositecollectionappcatalog
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Remove-SPOSiteCollectionAppCatalog
family: spps
documentKind: "doc"
---

# Remove-SPOSiteCollectionAppCatalog

# Remove-SPOSiteCollectionAppCatalog

## SYNOPSIS

Removes the site collection app catalog.

## SYNTAX

```
Remove-SPOSiteCollectionAppCatalog [-Site] <SpoSitePipeBind> [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to remove the site collection app catalog.

## EXAMPLES

### Example 1

```powershell
Remove-SPOSiteCollectionAppCatalog -Site https://contoso.sharepoint.com/sites/Research
```

This example removes the site collection app catalog from the site <https://contoso.sharepoint.com/sites/Research.>

## PARAMETERS

### -Site

> Applicable: SharePoint Online

Url of the site collection.

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
