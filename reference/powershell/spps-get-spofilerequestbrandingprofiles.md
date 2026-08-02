---
title: "Get-SPOFileRequestBrandingProfiles"
type: reference
domain: powershell
slug: spps-get-spofilerequestbrandingprofiles
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOFileRequestBrandingProfiles
family: spps
documentKind: "doc"
---

# Get-SPOFileRequestBrandingProfiles

# Get-SPOFileRequestBrandingProfiles

## SYNOPSIS

Retrieves branding profiles configured for the file request feature, including details about logo and background assets.

## SYNTAX

```
Get-SPOFileRequestBrandingProfiles [<CommonParameters>]
```

## DESCRIPTION

This cmdlet returns the branding profiles currently configured for the file request feature in the tenant. Each profile contains metadata about the logo and background image assets, such as file name and file URL. The cmdlet will output the asset library URL being used, along with information for both the primary and secondary branding profiles (if present). Each tenant can have at most one primary and one secondary branding profile.

## EXAMPLES

### Example 1

```powershell
Get-SPOFileRequestBrandingProfiles
```

This example retrieves the branding profiles configured for the file request feature. If profiles have been added using `Add-SPOFileRequestBrandingProfile`, the output will include the asset library URL and details abou the branding profiles such as file names and URLs for primary and secondary profiles if present.

## PARAMETERS

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/p/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS

[Add-SPOFileRequestBrandingProfile](/powershell/module/microsoft.online.sharepoint.powershell/add-spofilerequestbrandingprofile)

[Remove-SPOFileRequestBrandingProfile](/powershell/module/microsoft.online.sharepoint.powershell/remove-spofilerequestbrandingprofile)

[Switch-SPOFileRequestBrandingProfiles](/powershell/module/microsoft.online.sharepoint.powershell/switch-spofilerequestbrandingprofiles)
