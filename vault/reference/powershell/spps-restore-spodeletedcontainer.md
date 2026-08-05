---
title: "Restore-SPODeletedContainer"
type: reference
domain: powershell
slug: spps-restore-spodeletedcontainer
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.Online.SharePoint.PowerShell/Restore-SPODeletedContainer
family: spps
documentKind: "doc"
---

# Restore-SPODeletedContainer

# Restore-SPODeletedContainer

## SYNOPSIS

Recovers a deleted Container from the Recycle Bin.

## SYNTAX

```
Restore-SPODeletedContainer [-Identity] <SPOContainerPipeBind> [<CommonParameters>]
```

## DESCRIPTION

The `Restore-SPODeletedContainer` cmdlet recovers a previously deleted File Storage Container from the Recycle Bin. Restored Containers will be retrieved by the [`Get-SPOContainer`](./Get-SPOContainer.md) cmdlet. You must be at least a SharePoint Online Administrator to run this cmdlet.

## EXAMPLES

### Example 1

```powershell
Restore-SPODeletedContainer -Identity b66f5b2e-4cbd-4754-9ad3-8291c2c81ade
```
Example 1 restores the Container with `ContainerId` `b66f5b2e-4cbd-4754-9ad3-8291c2c81ade` from the Recycle Bin.

## PARAMETERS

### -Identity

> Applicable: SharePoint Online

Use this parameter to specify the `ContainerId` of the deleted container to be restored.

```yaml
Type: Microsoft.Online.SharePoint.PowerShell.SPOContainerPipeBind
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
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

[Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online)

[Get-SPODeletedContainer](./Get-SPODeletedContainer.md)
