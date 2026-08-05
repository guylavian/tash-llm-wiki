---
title: "Get-SPOFileArchivePolicySites"
type: reference
domain: powershell
slug: spps-get-spofilearchivepolicysites
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOFileArchivePolicySites
family: spps
documentKind: "doc"
---

# Get-SPOFileArchivePolicySites

# Get-SPOFileArchivePolicySites

## SYNOPSIS

Gets the list of sites associated with a file archive policy.

## SYNTAX

```
Get-SPOFileArchivePolicySites -PolicyId <Guid> [<CommonParameters>]
```

## DESCRIPTION

This cmdlet retrieves the list of sites that have been added to a file archive policy. This is applicable to policies with a PolicyType of `SelectedSites`.

> [!NOTE]
> This cmdlet is part of the file archive policies feature which is currently in preview.

## EXAMPLES

### Example 1

```powershell
Get-SPOFileArchivePolicySites -PolicyId "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

Returns all sites associated with the specified file archive policy.

## PARAMETERS

### -PolicyId

Specifies the unique identifier (GUID) of the policy to retrieve the site list for.

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

This cmdlet supports the common parameters: `-Debug`, `-ErrorAction`, `-ErrorVariable`, `-InformationAction`, `-InformationVariable`, `-OutVariable`, `-OutBuffer`, `-PipelineVariable`, `-ProgressAction`, `-Verbose`, `-WarningAction`, and `-WarningVariable`. For more information, see [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Add-SPOSiteToFileArchivePolicy](Add-SPOSiteToFileArchivePolicy.md)

[Get-SPOFileArchivePolicy](Get-SPOFileArchivePolicy.md)

[Get-SPOFileArchivePolicyReport](Get-SPOFileArchivePolicyReport.md)

[New-SPOFileArchivePolicy](New-SPOFileArchivePolicy.md)

[Remove-SPOFileArchivePolicy](Remove-SPOFileArchivePolicy.md)

[Remove-SPOSiteToFileArchivePolicy](Remove-SPOSiteToFileArchivePolicy.md)

[Set-SPOFileArchivePolicy](Set-SPOFileArchivePolicy.md)
