---
title: "Set-FASTSearchConfiguration"
type: reference
domain: powershell
slug: spps-set-fastsearchconfiguration
tier: reference
source: https://learn.microsoft.com/en-us/powershell/module/spps/sharepoint/sharepoint-ps/Microsoft.SharePoint.Powershell/Set-FASTSearchConfiguration
family: spps
documentKind: "doc"
---

# Set-FASTSearchConfiguration

# Set-FASTSearchConfiguration

## SYNOPSIS
Configures the local instance of Microsoft FAST Search Server 2010 for SharePoint.

## SYNTAX

```
Set-FASTSearchConfiguration [-LogFile <String>] [<CommonParameters>]
```

## DESCRIPTION
This cmdlet configures the local instance of FAST Search Server 2010 for SharePoint.

FAST Search Server 2010 for SharePoint must be installed, but not running, on the local machine before you run this cmdlet.

If you are not running this cmdlet on the admin node in the FAST Search Server 2010 for SharePoint installation, make sure that the admin node is started before you run this cmdlet.

For permissions and the most current information about FAST Search Server 2010 for SharePoint cmdlets, see the online documentation, (https://go.microsoft.com/fwlink/?LinkId=163227).

## EXAMPLES

### EXAMPLE 1 (FAST Server for SharePoint 2010)
```
Set-FastSearchConfiguration -LogFile C:\log.txt
```

This example configures the local machine and writes the log output to C:\log.txt.

## PARAMETERS

### -LogFile

> Applicable: FAST Server for SharePoint 2010

Specifies the full path of a file where all log messages will be written.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
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
