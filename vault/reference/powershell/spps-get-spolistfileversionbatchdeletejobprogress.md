---
title: "Get-SPOListFileVersionBatchDeleteJobProgress"
type: reference
domain: powershell
slug: spps-get-spolistfileversionbatchdeletejobprogress
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOListFileVersionBatchDeleteJobProgress
family: spps
documentKind: "doc"
---

# Get-SPOListFileVersionBatchDeleteJobProgress

# Get-SPOListFileVersionBatchDeleteJobProgress

## SYNOPSIS

Gets the progress of a trim job for a site collection.

## SYNTAX

```
Get-SPOListFileVersionBatchDeleteJobProgress [-Site] <SpoSitePipeBind> -List <SPOListPipeBind>
 [<CommonParameters>]
```

## DESCRIPTION

Gets the progress of a trim job for a document library.

## EXAMPLES

### EXAMPLE 1

```powershell
Get-SPOListFileVersionBatchDeleteJobProgress -Site https://contoso.sharepoint.com/sites/site1 -List "Documents"
```

Example 1 gets the progress of a trim job for a document library called "Documents".

## PARAMETERS

### -List

The document library name or Id.

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.SPOListPipeBind
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Site

> Applicable: SharePoint Online

Specifies the URL of the site.

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.SpoSitePipeBind
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

### Microsoft.Online.SharePoint.PowerShell.SpoSitePipeBind

### Microsoft.Online.SharePoint.PowerShell.SPOListPipeBind

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Remove-SPOListFileVersionBatchDeleteJob](Remove-SPOListFileVersionBatchDeleteJob.md)

[New-SPOListFileVersionBatchDeleteJob](New-SPOListFileVersionBatchDeleteJob.md)
