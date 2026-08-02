---
title: "Get-SPOSiteReview"
type: reference
domain: powershell
slug: spps-get-spositereview
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOSiteReview
family: spps
documentKind: "doc"
---

# Get-SPOSiteReview

# Get-SPOSiteReview

## SYNOPSIS
Track all site access reviews initiated from Data Access Governance (DAG) reports.

## SYNTAX

```
Get-SPOSiteReview [-SiteReviewID <Guid>] [-Status <SiteReviewStatus>]
 [-ReportEntity <SiteAccessReportEntityEnum>] [-SiteID <Guid>] [<CommonParameters>]
```

## DESCRIPTION
This cmdlet fetches details of a particular access review or a group of access reviews as per the filtering criteria.

## EXAMPLES

### Example 1
```powershell
Get-SPOSiteReview -ReportEntity PermissionedUsers
```

The above cmdlet retrieves all site access reviews raised under all 'Permissioned user' snapshot reports.

## PARAMETERS

### -ReportEntity
Specifies the entity that could cause oversharing and hence tracked by these reports.

```yaml
Type: Microsoft.Online.SharePoint.TenantAdministration.SiteAccessReportEntityEnum
Parameter Sets: (All)
Aliases:
Accepted values: All, SharingLinks_Anyone, SharingLinks_PeopleInYourOrg, SharingLinks_Guests, SensitivityLabelForFiles, EveryoneExceptExternalUsersAtSite, EveryoneExceptExternalUsersForItems, PermissionedUsers

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteID
Specifies the ID of the site for which access reviews were initiated.

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteReviewID
Specifies the ID of the particular access review.

```yaml
Type: System.Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Status
Specifies the current status of the site access review.

```yaml
Type: Microsoft.Online.SharePoint.TenantAdministration.SiteReviewStatus
Parameter Sets: (All)
Aliases:
Accepted values: All, Pending, Failed, Completed

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

[Site access review for DAG reports](/sharepoint/site-access-review)

[Start-SPOSiteReview](./Start-SPOSiteReview.md)

[Start-SPODataAccessGovernanceInsight](./Start-SPODataAccessGovernanceInsight.md)

[Get-SPODataAccessGovernanceInsight](./Get-SPODataAccessGovernanceInsight.md)

[Export-SPODataAccessGovernanceInsight](./Export-SPODataAccessGovernanceInsight.md)

[Remove-SPODataAccessGovernanceInsight](./Remove-SPODataAccessGovernanceInsight.md)
