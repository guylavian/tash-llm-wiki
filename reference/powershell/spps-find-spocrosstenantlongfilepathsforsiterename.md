---
title: "Find-SPOCrossTenantLongFilePathsForSiteRename"
type: reference
domain: powershell
slug: spps-find-spocrosstenantlongfilepathsforsiterename
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Find-SPOCrossTenantLongFilePathsForSiteRename
family: spps
documentKind: "doc"
---

# Find-SPOCrossTenantLongFilePathsForSiteRename

# Find-SPOCrossTenantLongFilePathsForSiteRename

## SYNOPSIS

Identify sites with file paths over 400 characters for cross-tenant user migration.

## SYNTAX

```
Find-SPOCrossTenantLongFilePathsForSiteRename
  [-OldSiteUrl <String>]
  [-NewSiteUrl <String>]
  [<CommonParameters>]
```

## DESCRIPTION
During SharePoint cross-tenant user migration, file paths from the source tenant must be 400 characters or fewer after merging with the target tenant. This cmdlet helps you identify sites that exceed this limit.

## EXAMPLES

### Example 1
```powershell
Find-SPOCrossTenantLongFilePathsForSiteRename -OldSiteUrl https://contoso.sharepoint.com/sites/site1 -NewSiteUrl https://fabrikam.sharepoint.com/sites/site1
```
Example 1 looks through the site inputted to find file paths that exceed the 400 character limit.

## PARAMETERS

### -NewSiteUrl
Specifies the new URL to assign to the SharePoint site after the rename.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OldSiteUrl
Specifies the original URL of the SharePoint site before the rename.  

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object
## NOTES

## RELATED LINKS
