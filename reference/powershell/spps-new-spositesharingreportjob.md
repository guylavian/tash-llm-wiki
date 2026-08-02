---
title: "New-SPOSiteSharingReportJob"
type: reference
domain: powershell
slug: spps-new-spositesharingreportjob
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/New-SPOSiteSharingReportJob
family: spps
documentKind: "doc"
---

# New-SPOSiteSharingReportJob

# New-SPOSiteSharingReportJob

## SYNOPSIS

Creates a new sharing report job.

## SYNTAX

```
New-SPOSiteSharingReportJob [-Site] <SpoSitePipeBind> [-ReportStorageWebUrl] <String>
 [-ReportStorageFolderUrl] <String> [<CommonParameters>]
```

## DESCRIPTION
This cmdlet is not currently active in Production and may be removed in the future. You will receive the error, "Site collection sharing report feature has not been enabled", if you run this cmdlet which is currently by design.

## EXAMPLES

### EXAMPLE 1

```powershell
$site = Get-SPOSite -Identity https://contoso.sharepoint.com/sites/site1

New-SPOSiteSharingReportJob -Site $site -ReportStorageWebUrl 'https://contoso.sharepoint.com/sites/site2/web1' -ReportStorageFolderUrl '/Documents/folder'
```

## PARAMETERS

### -ReportStorageFolderUrl

> Applicable: SharePoint Online

Location to where the report will be exported.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReportStorageWebUrl

> Applicable: SharePoint Online

Report web storage URL.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Site

> Applicable: SharePoint Online

Specifies the site.

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

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
