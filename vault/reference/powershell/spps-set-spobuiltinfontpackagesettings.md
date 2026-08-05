---
title: "Set-SPOBuiltInFontPackageSettings"
type: reference
domain: powershell
slug: spps-set-spobuiltinfontpackagesettings
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Set-SPOBuiltInFontPackageSettings
family: spps
documentKind: "doc"
---

# Set-SPOBuiltInFontPackageSettings

# Set-SPOBuiltInFontPackageSettings

## SYNOPSIS

Use this cmdlet to set settings of [built-in font packages](/sharepoint/brand-center-font-packages).

## SYNTAX

```
Set-SPOBuiltInFontPackageSettings [-HideBuiltInFontPackages <Boolean>] [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to set settings of [built-in font packages](/sharepoint/brand-center-font-packages).

## EXAMPLES

### Example 1

```powershell
Set-SPOBuiltInFontPackageSettings -HideBuiltInFontPackages $true
```

This example sets the built-in font packages to be hidden from SharePoint sites.

## PARAMETERS

### -HideBuiltInFontPackages

```yaml
Type: System.Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### System.Boolean

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Get-SPOBuiltInFontPackageSettings](./Get-SPOBuiltInFontPackageSettings.md)
