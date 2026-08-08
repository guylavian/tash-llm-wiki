---
title: "Set-SPOMultiGeoCompanyAllowedDataLocation"
type: reference
domain: powershell
slug: spps-set-spomultigeocompanyalloweddatalocation
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Set-SPOMultiGeoCompanyAllowedDataLocation
family: spps
documentKind: "doc"
---

# Set-SPOMultiGeoCompanyAllowedDataLocation

# Set-SPOMultiGeoCompanyAllowedDataLocation

## SYNOPSIS

Adds a multi-geo allowed location.

## SYNTAX

```
Set-SPOMultiGeoCompanyAllowedDataLocation [-Location] <String> [-InitialDomain] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to set the multi-geo allowed locations.

## EXAMPLES

### Example 1

```powershell
Set-SPOMultiGeoCompanyAllowedDataLocation -Location AUS -Domain contoso.com
```

Sets AUS (Australia) as an allowed multi-geo location for the domain contoso.com.

## PARAMETERS

### -InitialDomain

> Applicable: SharePoint Online

Sets the initial domain to associate with the specified data location.

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

### -Location

> Applicable: SharePoint Online

The Preferred Data Location (PDL) to allow.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

> Applicable: SharePoint Online

Prompts you for confirmation before executing the command.
For more information, type the following command: `get-help about_commonparameters`

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

> Applicable: SharePoint Online
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
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

[Remove-SPOMultiGeoCompanyAllowedDataLocation](/powershell/module/microsoft.online.sharepoint.powershell/remove-spomultigeocompanyalloweddatalocation)
