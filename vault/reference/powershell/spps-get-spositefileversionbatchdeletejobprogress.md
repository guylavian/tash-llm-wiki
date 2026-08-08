---
title: "Get-SPOSiteFileVersionBatchDeleteJobProgress"
type: reference
domain: powershell
slug: spps-get-spositefileversionbatchdeletejobprogress
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOSiteFileVersionBatchDeleteJobProgress
family: spps
documentKind: "doc"
---

# Get-SPOSiteFileVersionBatchDeleteJobProgress

# Get-SPOSiteFileVersionBatchDeleteJobProgress

## SYNOPSIS

Gets the progress of a trim job for a site collection.

## SYNTAX

```
Get-SPOSiteFileVersionBatchDeleteJobProgress [-Identity] <SpoSitePipeBind> [<CommonParameters>]
```

## DESCRIPTION

Gets the progress of a trim job for a site collection.

## EXAMPLES

### EXAMPLE 1

```powershell
Get-SPOSiteFileVersionBatchDeleteJobProgress -Identity https://contoso.sharepoint.com/sites/site1
```

Example 1 gets the progress of a trim job for a site collection.

## PARAMETERS

### -Identity

> Applicable: SharePoint Online

Specifies the URL of the site collection.

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

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Remove-SPOSiteFileVersionBatchDeleteJob](Remove-SPOSiteFileVersionBatchDeleteJob.md)

[New-SPOSiteFileVersionBatchDeleteJob](New-SPOSiteFileVersionBatchDeleteJob.md)
