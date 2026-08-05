---
title: "Get-FASTSearchSecurityPublicFilter"
type: reference
domain: powershell
slug: spps-get-fastsearchsecuritypublicfilter
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.SharePoint.Powershell/Get-FASTSearchSecurityPublicFilter
family: spps
documentKind: "doc"
---

# Get-FASTSearchSecurityPublicFilter

# Get-FASTSearchSecurityPublicFilter

## SYNOPSIS
Gets the public filter general setting.

## SYNTAX

```
Get-FASTSearchSecurityPublicFilter [[-Worker] <WorkerPoolNode>] [<CommonParameters>]
```

## DESCRIPTION
This cmdlet retrieves the public filter general setting configuration information.
The public filter is the search security filter that is used to find documents that all users have access to.

For permissions and the most current information about FAST Search Server 2010 for SharePoint cmdlets, see the online documentation, (https://go.microsoft.com/fwlink/?LinkId=163227).

## EXAMPLES

### EXAMPLE 1
```
Get-FASTSearchSecurityPublicFilter
```

This example gets the security public filter's general setting configuration information.

### EXAMPLE 2
```
Get-FASTSearchSecurityWorkerNode workerserver | Get-FASTSearchSecurityPublicFilter
```

This example gets the security public filter's general setting configuration information for a security worker with the server name of "workerserver".

## PARAMETERS

### -Worker

> Applicable: FAST Server for SharePoint 2010

The optional Worker parameter specifies the WorkerPoolNode object for the security worker that is to handle the request.

```yaml
Type: WorkerPoolNode
Parameter Sets: (All)
Aliases:

Required: False
Position: 9999
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see about_CommonParameters (https://go.microsoft.com/fwlink/?LinkID=113216).

## INPUTS

## OUTPUTS

## NOTES

## RELATED LINKS

[Set-FASTSearchSecurityPublicFilter](Set-FASTSearchSecurityPublicFilter.md)
