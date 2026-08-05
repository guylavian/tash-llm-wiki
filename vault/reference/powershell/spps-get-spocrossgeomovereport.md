---
title: "Get-SPOCrossGeoMoveReport"
type: reference
domain: powershell
slug: spps-get-spocrossgeomovereport
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Get-SPOCrossGeoMoveReport
family: spps
documentKind: "doc"
---

# Get-SPOCrossGeoMoveReport

# Get-SPOCrossGeoMoveReport

## SYNOPSIS

Provides a report of objects moved between geo locations.

## SYNTAX

```
Get-SPOCrossGeoMoveReport [-Limit <UInt32>] [-MoveStartTime <DateTime>] [-MoveEndTime <DateTime>]
 -MoveJobType <JobType> [-MoveState <MoveState>] [-MoveDirection <MoveDirection>] [<CommonParameters>]
```

## DESCRIPTION

Use this cmdlet to return a report of objects moved between geo locations based on the specified parameters.

## EXAMPLES

### Example 1

```powershell
Get-SPOCrossGeoMoveReport -MoveJobType SiteMove -MoveState Failed
```

This example returns the failed site moves between geo locations.

## PARAMETERS

### -Limit

> Applicable: SharePoint Online

Limit the number of items to return for the report.

```yaml
Type: System.UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MoveDirection

> Applicable: SharePoint Online

The direction of the move to limit the report to. Valid values are:

* All
* MoveIn
* MoveOut

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.MoveDirection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MoveEndTime

> Applicable: SharePoint Online

The end time to limit the move report to.

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MoveJobType

> Applicable: SharePoint Online

The type of job to limit the report to. Valid values are:

* GroupMove
* SiteMove
* UserMove

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.JobType
Parameter Sets: (All)
Aliases:
Accepted values: UserMove, GroupMove, SiteMove

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MoveStartTime

> Applicable: SharePoint Online

The start time to limit the move report to.

```yaml
Type: System.DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MoveState

> Applicable: SharePoint Online

The type of state to limit the report to. Valid values are:

* All
* Failed
* InProgress
* NotStarted
* NotSupported
* Queued
* Rescheduled
* Stopped
* Success

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.MoveState
Parameter Sets: (All)
Aliases:
Accepted values: NotStarted, InProgress, Success, Failed, Stopped, Queued, NotSupported, Rescheduled, All

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/p/?LinkID=113216).

## INPUTS

### None

## OUTPUTS

### System.Object

## NOTES

## RELATED LINKS
