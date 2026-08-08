---
title: "Remove-SPOSiteDesign"
type: reference
domain: powershell
slug: spps-remove-spositedesign
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Remove-SPOSiteDesign
family: spps
documentKind: "doc"
---

# Remove-SPOSiteDesign

# Remove-SPOSiteDesign

## SYNOPSIS

Removes a site design. It no longer appears in the UI for creating a new site.

## SYNTAX

```
Remove-SPOSiteDesign [-Identity] <SPOSiteDesignPipeBind> [<CommonParameters>]
```

## DESCRIPTION

Removes a site design. It no longer appears in the UI for creating a new site.

## EXAMPLES

### Example 1

This example shows how to remove a site design.

```powershell
Remove-SPOSiteDesign 21209d88-38de-4844-9823-f1f600a1179a
```

## PARAMETERS

### -Identity

## PARAMETERS

### -Identity

> Applicable: SharePoint Online

The ID of the site design to remove.

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.SPOSiteDesignPipeBind
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### Microsoft.Online.SharePoint.PowerShell.SPOSiteDesignPipeBind

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
