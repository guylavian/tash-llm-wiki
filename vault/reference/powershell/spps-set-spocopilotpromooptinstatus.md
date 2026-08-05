---
title: "Set-SPOCopilotPromoOptInStatus"
type: reference
domain: powershell
slug: spps-set-spocopilotpromooptinstatus
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Set-SPOCopilotPromoOptInStatus
family: spps
documentKind: "doc"
---

# Set-SPOCopilotPromoOptInStatus

# Set-SPOCopilotPromoOptInStatus

## SYNOPSIS

Sets the Opt-In Copilot promo status for the tenant.

## SYNTAX

```
Set-SPOCopilotPromoOptInStatus -IsCopilotPromoStatusEnabled <Boolean> [<CommonParameters>]
```

## DESCRIPTION

This cmdlet sets the Opt-In Copilot promo status for the tenant to `True` or `False`.

## EXAMPLES

### Example 1

```powershell
Set-SPOCopilotPromoOptInStatus -IsCopilotPromoStatusEnabled $true
```

Example 1 sets the Opt-In Copilot promo status for the tenant to `True`.

## PARAMETERS

### -IsCopilotPromoStatusEnabled

> Applicable: SharePoint Online

Use this parameter to set Copilot opt-in promo status.

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable,
-InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose,
-WarningAction, and -WarningVariable. For more information, see
[about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online)
