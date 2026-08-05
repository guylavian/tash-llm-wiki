---
title: "Remove-SPOOrgNewsSite"
type: reference
domain: powershell
slug: spps-remove-spoorgnewssite
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Remove-SPOOrgNewsSite
family: spps
documentKind: "doc"
---

# Remove-SPOOrgNewsSite

# Remove-SPOOrgNewsSite

## SYNOPSIS

Removes a given site from the list of organizational news sites based on its URL in your SharePoint Online Tenant

## SYNTAX

```
Remove-SPOOrgNewsSite -OrgNewsSiteUrl <String> [<CommonParameters>]
```

## DESCRIPTION

This cmdlet will remove a site from list of organizational news sites based on its URL.

## EXAMPLES

### EXAMPLE 1

```powershell
Remove-SPOOrgNewsSite -OrgNewsSiteUrl https://contoso.sharepoint.com/sites/Marketing
```

This example removes <https://contoso.sharepoint.com/sites/Marketing> from the list of organizational news sites.

## PARAMETERS

### -OrgNewsSiteUrl

> Applicable: SharePoint Online

The URL of a site to be marked as an organizational news site.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
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

[Get-SPOOrgNewsSite](Get-SPOOrgNewsSite.md)

[Set-SPOOrgNewsSite](Set-SPOOrgNewsSite.md)
