---
title: "Get-SPOTenantApplyFileVersionPolicyJobImpact"
type: reference
domain: powershell
slug: spps-get-spotenantapplyfileversionpolicyjobimpact
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOTenantApplyFileVersionPolicyJobImpact
family: spps
documentKind: "doc"
---

# Get-SPOTenantApplyFileVersionPolicyJobImpact

# Get-SPOTenantApplyFileVersionPolicyJobImpact

## SYNOPSIS

Estimates how many versions would be trimmed and how much storage would be freed if a trimming job were run with the given version policy. SharePoint Advanced Management license or Copilot license is required to run this cmdlet.

> [!NOTE]
> This feature is currently in preview and may not be available in your tenant.

## SYNTAX

```
Get-SPOTenantApplyFileVersionPolicyJobImpact -VersionPolicy <SPOFileVersionPolicySettings> [<CommonParameters>]
```

## DESCRIPTION

Queries the version dataset collected by a previously completed `New-SPOTenantApplyFileVersionPolicyJob -CollectVersionData` job and returns an estimated impact object showing how many versions would be trimmed and how much storage would be freed if a trimming job were run with the given version policy.

> [!NOTE]
> - A completed job that was started with `-CollectVersionData` is required before running this cmdlet. Use `Get-SPOTenantApplyFileVersionPolicyJobProgress` to confirm the job has completed.
> - The estimate is based on a snapshot collected during the job and may not reflect changes made to the tenant after the job ran.
> - The estimate does not account for versions protected by retention policies, retention labels, or eDiscovery holds. Actual versions deleted may be fewer than estimated.

## EXAMPLES

### Example 1
```powershell
$policy = Get-SPOTenantVersionPolicy |  Get-SPOVersionPolicyWithChanges -MajorVersionLimit 50
Get-SPOTenantApplyFileVersionPolicyJobImpact -VersionPolicy $policy
```

Estimates the impact of a trimming job run with a modified policy that limits to 50 major versions.

## PARAMETERS

### -VersionPolicy
The version policy to evaluate. Use `Get-SPOTenantVersionPolicy` and `Get-SPOVersionPolicyWithChanges` to build this value.

```yaml
Type: SPOFileVersionPolicySettings
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

### Microsoft.Online.SharePoint.TenantAdministration.SPOTenantVersionPolicyImpact

## NOTES

## RELATED LINKS

[New-SPOTenantApplyFileVersionPolicyJob](New-SPOTenantApplyFileVersionPolicyJob.md)

[Get-SPOTenantApplyFileVersionPolicyJobProgress](Get-SPOTenantApplyFileVersionPolicyJobProgress.md)

[Get-SPOTenantVersionPolicy](Get-SPOTenantVersionPolicy.md)

[Get-SPOVersionPolicyWithChanges](Get-SPOVersionPolicyWithChanges.md)

[SharePoint Advanced Management](/sharepoint/sharepoint-advanced-management-licensing)

[Microsoft 365 Copilot](/microsoft-365/copilot/microsoft-365-copilot-licensing)
