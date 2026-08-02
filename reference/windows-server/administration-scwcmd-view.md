---
title: "scwcmd view"
type: reference
domain: windows-server
slug: administration-scwcmd-view
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/scwcmd-view
family: administration
documentKind: "reference"
abstract: "Reference article for the scwcmd view command, which renders an .xml file by using a specified .xsl transform."
---

# scwcmd view

# scwcmd view



Renders an .xml file by using a specified .xsl transform. This command can be useful for displaying Security Configuration Wizard (SCW) .xml files by using different views.

## Syntax

```
scwcmd view /x:<Xmlfile.xml> [/s:<Xslfile.xsl>]
```

### Parameters

| Parameter | Description |
|--|--|
| /x:`<Xmlfile.xml>` | Specifies the .xml file to be viewed. This parameter must be specified. |
| /s:`<Xslfile.xsl>` | Specifies the .xsl transform to apply to the .xml file as part of the rendering process. This parameter is optional for SCW .xml files. When the **view** command is used to render a SCW .xml file, it will automatically try to load the correct default transform for the specified .xml file. If an .xsl transform is specified, the transform must be written under the assumption that the .xml file is in the same directory as the .xsl transform. |
| /? | Displays help at the command prompt. |

## Example

To view *Policyfile.xml* by using the *Policyview.xsl* transform, type:

```
scwcmd view /x:C:\policies\Policyfile.xml /s:C:\viewers\Policyview.xsl
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key.md)

- [scwcmd analyze command](scwcmd-analyze.md)

- [scwcmd configure command](scwcmd-configure.md)

- [scwcmd register command](scwcmd-register.md)

- [scwcmd rollback command](scwcmd-rollback.md)

- [scwcmd transform command](scwcmd-transform.md)
