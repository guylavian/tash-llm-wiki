---
title: "Get-FASTSearchSecurityLotusNotesUserStore"
type: reference
domain: powershell
slug: spps-get-fastsearchsecuritylotusnotesuserstore
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.SharePoint.Powershell/Get-FASTSearchSecurityLotusNotesUserStore
family: spps
documentKind: "doc"
---

# Get-FASTSearchSecurityLotusNotesUserStore

# Get-FASTSearchSecurityLotusNotesUserStore

## SYNOPSIS
Gets a Lotus Notes user store.

## SYNTAX

```
Get-FASTSearchSecurityLotusNotesUserStore [[-Identity] <String>] [<CommonParameters>]
```

## DESCRIPTION
This cmdlet retrieves a specific Lotus Notes user store.
If the Identity parameter is not specified, the cmdlet gets a list of all Lotus Notes user stores.

For permissions and the most current information about FAST Search Server 2010 for SharePoint cmdlets, see the online documentation, (https://go.microsoft.com/fwlink/?LinkId=163227).

## EXAMPLES

### EXAMPLE 1
```
Get-FASTSearchSecurityLotusNotesUserStore -Identity ln1
```

This example gets the Lotus Notes user store with the identity "ln1".

## PARAMETERS

### -Identity

> Applicable: FAST Server for SharePoint 2010

The identity of the Lotus Notes user store to get.
If not specified, a list of all Lotus Notes user stores is returned.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see about_CommonParameters (https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

## OUTPUTS

## NOTES

## RELATED LINKS

[New-FASTSearchSecurityLotusNotesUserStore](New-FASTSearchSecurityLotusNotesUserStore.md)

[Set-FASTSearchSecurityLotusNotesUserStore](Set-FASTSearchSecurityLotusNotesUserStore.md)
