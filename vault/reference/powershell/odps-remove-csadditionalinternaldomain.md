---
title: "Remove-CsAdditionalInternalDomain"
type: reference
domain: powershell
slug: odps-remove-csadditionalinternaldomain
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/odps/skype/skype-ps/SkypeForBusiness/Remove-CsAdditionalInternalDomain
family: odps
documentKind: "doc"
---

# Remove-CsAdditionalInternalDomain

# Remove-CsAdditionalInternalDomain

## SYNOPSIS
Removes an additional internal domain previously configured for use in your organization. This cmdlet was introduced in Skype for Business Server 2015 Cumulative Update 6 - December 2017.

## SYNTAX

```
Remove-CsAdditionalInternalDomain [-Identity] <XdsGlobalRelativeIdentity> [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## DESCRIPTION
This cmdlet removes an additional internal domain previously configured for use in your organization.

Additional internal domains are not used locally by internal user or services URIs but must be treated
as internal by hybrid (split-domain) traffic analysis to support purely hosted and cloud appliance
domains.

## EXAMPLES

### Example 1
```powershell
Remove-CsAdditionalInternalDomain -Identity fabrikam.com
```

Example 1 removes the additional internal domain with the Identity fabrikam.com.

## PARAMETERS

### -Force

> Applicable: Skype for Business Server 2015, Skype for Business Server 2019

Suppresses the display of any non-fatal error message that might occur when running the command.

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

> Applicable: Skype for Business Server 2015, Skype for Business Server 2019

Fully qualified domain name (FQDN) for the new additional internal domain.

```yaml
Type: XdsGlobalRelativeIdentity
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm

> Applicable: Skype for Business Server 2015, Skype for Business Server 2019

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

### -WhatIf

> Applicable: Skype for Business Server 2015, Skype for Business Server 2019

The WhatIf switch causes the command to simulate its results. By using this switch, you can view what changes would occur without having to commit those changes.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable.
For more information, see about_CommonParameters (https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### Microsoft.Rtc.Management.Xds.XdsGlobalRelativeIdentity


## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
[New-CsAdditionalInternalDomain](https://learn.microsoft.com/powershell/module/skypeforbusiness/new-csadditionalinternaldomain?view=skype-ps)

[Get-CsAdditionalInternalDomain](https://learn.microsoft.com/powershell/module/skypeforbusiness/get-csadditionalinternaldomain?view=skype-ps)
