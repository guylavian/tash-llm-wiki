---
title: "Get-SPOBuiltInDesignPackageVisibility"
type: reference
domain: powershell
slug: spps-get-spobuiltindesignpackagevisibility
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOBuiltInDesignPackageVisibility
family: spps
documentKind: "doc"
---

# Get-SPOBuiltInDesignPackageVisibility

# Get-SPOBuiltInDesignPackageVisibility

## SYNOPSIS

Gets the visibility of the available built-in Design Packages.

## SYNTAX

```
Get-SPOBuiltInDesignPackageVisibility [-DesignPackage <DesignPackageType>] [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to retrieve the current visibility state of each built-in design package.

## EXAMPLES

### Example 1

```powershell
Get-SPOBuiltInDesignPackageVisibility -DesignPackage Showcase
```

This example retrieves the current visibility state of Showcase built-in design package.

### Example 2

```powershell
Get-SPOBuiltInDesignPackageVisibility
```

This example retrieves the current visibility state of each built-in design package.

## PARAMETERS

### -DesignPackage

Name of the design package, available names are
- Topic
- Showcase
- Blank
- TeamSite

```yaml
Type: Microsoft.SharePoint.Administration.DesignPackageType
Parameter Sets: (All)
Aliases:
Accepted values: None, Topic, Showcase, Blank, TeamSite

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
