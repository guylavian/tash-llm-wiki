---
title: "Remove-SPOSiteManageVersionPolicyJob"
type: reference
domain: powershell
slug: spps-remove-spositemanageversionpolicyjob
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Remove-SPOSiteManageVersionPolicyJob
family: spps
documentKind: "doc"
---

# Remove-SPOSiteManageVersionPolicyJob

# Remove-SPOSiteManageVersionPolicyJob

## SYNOPSIS
Stops processing of the in-progress manage version policy job for the given site.

> [!NOTE]
> This feature is currently in preview and may not be available in your tenant.

## SYNTAX

```powershell
Remove-SPOSiteManageVersionPolicyJob [-Identity] <SpoSitePipeBind> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## DESCRIPTION
Stops processing of the in-progress manage version policy job for the given site.

## EXAMPLES

### Example 1

```powershell
Remove-SPOSiteFileVersionBatchDeleteJob -Identity https://contoso.sharepoint.com/sites/site1
```

Stops further processing of site manage version policy job.

## PARAMETERS

### -Confirm
Prompts you for confirmation before running the cmdlet.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity
> Applicable: SharePoint Online

Specifies the URL of the site collection.

```yaml
Type: SpoSitePipeBind
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### Microsoft.Online.SharePoint.PowerShell.SpoSitePipeBind

## OUTPUTS

### System.Object
## NOTES

## RELATED LINKS
[Get-SPOSiteManageVersionPolicyJobProgress](Get-SPOSiteManageVersionPolicyJobProgress.md)
[New-SPOSiteManageVersionPolicyJob](New-SPOSiteManageVersionPolicyJob.md)
