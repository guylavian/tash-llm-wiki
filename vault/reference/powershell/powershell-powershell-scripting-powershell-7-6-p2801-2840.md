---
title: "How to use this documentation — pages 2801-2840"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2801-2840
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2801-2840
family: powershell
documentKind: "doc"
abstract: "None. Parent Elements ﾉ Expand table Element Description SelectionCondition Element for EntrySelectedBy Defines the condition that must exist for this for WideEntry definition to be used. Text Value Specify the name of the selection set. Remarks The selection condition can speci"
---

# How to use this documentation — pages 2801-2840

<!-- p.2801 -->

None.

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this
 for WideEntry                                    definition to be used.

Text Value
Specify the name of the selection set.

Remarks
The selection condition can specify a selection set or .NET type, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

Selection sets are common groups of .NET objects that can be used by any view that the
formatting file defines. For more information about creating and referencing selection sets, see
Defining Sets of Objects.

For more information about other components of a wide view, see Creating a Wide View.

See Also
Creating a Wide View

Defining Conditions for When Data Is Displayed

Defining Selection Sets

SelectionCondition Element for EntrySelectedBy for WideEntry

TypeName Element for SelectionCondition for EntrySelectedBy for WideEntry

Writing a PowerShell Formatting File

<!-- p.2802 -->

Last updated on 05/20/2025

<!-- p.2803 -->

TypeName Element for SelectionCondition
for EntrySelectedBy for WideControl
Specifies a .NET type that triggers the condition. When this type is present, the definition is
used.

Schema
        Configuration Element
        ViewDefinitions Element
        View Element
        WideControl Element
        WideEntries Element
        WideEntry Element
        EntrySelectedBy Element
        SelectionCondition Element
        TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe attributes, child elements, and the parent element of the
TypeName element.

Attributes
None.

Child Elements
None.

<!-- p.2804 -->

Parent Elements

                                                                                     ﾉ    Expand table

 Element                                          Description

 SelectionCondition Element for EntrySelectedBy   Defines the condition that must exist for this wide
 for WideEntry                                    entry to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
The selection condition can specify a .NET type or a selection set, but cannot specify both. For
more information about how to use selection conditions, see Defining Conditions for when
Data is Displayed.

For more information about other components of a wide view, see Creating a Wide View.

See Also
Creating a Wide View

Defining Conditions for When Data Is Displayed

SelectionCondition Element for EntrySelectedBy for WideEntry

SelectionSetName Element for SelectionCondition for EntrySelectedBy for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2805 -->

TypeName Element for EntrySelectedBy for
WideEntry
Specifies a .NET type for the definition. The definition is used whenever this object is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     EntrySelectedBy Element
     TypeName Element

Syntax
 XML

 <TypeName>Nameof.NetType</TypeName>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
TypeName element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2806 -->

                                                                                       ﾉ   Expand table

 Element                        Description

 EntrySelectedBy Element for    Defines the .NET types that use this wide entry or the condition that
 WideEntry                      must exist for this entry to be used.

Text Value
Specify the fully qualified name of the .NET type, such as System.IO.DirectoryInfo .

Remarks
Each wide entry must specify one or more .NET types, a selection set, or the selection condition
that must exist for the definition to be used.

For more information about other components of a wide view, see Creating a Wide View.

See Also
Creating a Wide View

EntrySelectedBy Element for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2807 -->

SelectionSetName Element for
EntrySelectedBy for WideControl
Specifies a set of .NET objects for the definition. The definition is used whenever one of these
objects is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     EntrySelectedBy Element
     SelectionSetName Element

Syntax
 XML

 <SelectionSetName>NameofSelectionSet</SelectionSetName>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
SelectionSetName element.

Attributes
None.

Child Elements
None.

<!-- p.2808 -->

Parent Elements

                                                                                      ﾉ   Expand table

 Element                       Description

 EntrySelectedBy Element for   Defines the .NET types that use this wide entry or the condition that
 WideEntry                     must exist for this entry to be used.

Text Value
Specify the name of the selection set.

Remarks
Each definition must specify one type name, selection set, or selection condition.

Selection sets are typically used when you want to define a group of objects that are used in
multiple views. For example, you might want to create a table view and a list view for the same
set of objects. For more information about defining selection sets, see Defining Sets of Objects
for a View.

For more information about other components of a wide view, see Creating a Wide View.

See Also
Creating a Wide View

Defining Selection Sets

EntrySelectedBy Element for WideEntry

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2809 -->

WideItem Element for WideControl
Defines the property or script whose value is displayed.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     WideItem Element

Syntax
 XML

 <WideItem>
   <PropertyName>.NetTypeProperty</PropertyName>
   <ScriptBlock>ScriptToExecute</ScriptBlock>
   <FormatString>FormatPattern</FormatString>
 </WideItem>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
WideItem element. The FormatString element is optional. However, you must specify a

PropertyName or ScriptBlock element, but you cannot specify both.

Attributes
None.

Child Elements

                                                                               ﾉ   Expand table

<!-- p.2810 -->

 Element                                Description

 FormatString Element for WideItem      Optional element.
 for WideControl
                                        Specifies a format pattern that defines how the property or
                                        script value is displayed in the view.

 PropertyName Element for WideItem      Specifies the property of the object whose value is displayed in
                                        the wide view.

 ScriptBlock Element for WideItem       Specifies the script whose value is displayed in the wide view.

Parent Elements

                                                                                        ﾉ   Expand table

 Element                             Description

 WideEntry Element                   Provides a definition of the wide view.

Remarks
For more information about the components of a wide view, see Wide View.

Example
The following example shows a WideEntry element that defines a single WideItem element. The
WideItem element defines the property or script whose value is displayed in the view.

 XML

 <WideEntry>
   <WideItem>
     <PropertyName>ProcessName</PropertyName>
   </WideItem>
 </WideEntry>

For a complete example of a wide view, see Wide View (Basic).

See Also
FormatString Element for WideItem for WideControl

PropertyName Element for WideItem

<!-- p.2811 -->

ScriptBlock Element for WideItem

WideEntry Element

Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2812 -->

FormatString Element for WideItem
Specifies a format pattern that defines how the property or script value is displayed in the view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     WideItem Element
     FormatString Element

Syntax
 XML

 <FormatString>PropertyPattern</FormatString>

Attributes and Elements
The following sections describe the attributes, child elements, and the parent element of the
FormatString element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                ﾉ   Expand table

<!-- p.2813 -->

 Element                        Description

 WideItem Element for           Defines the property or script whose value is displayed in a row of the
 WideControl                    list view.

Text Value
Specify the pattern that is used to format the data. For example, you can use this pattern to
format the value of any property that is of type System.TimeSpan: {0:MMM}{0:dd}{0:HH}:
{0:mm}.

Remarks
Format strings can be used when creating table views, list views, wide views, or custom views.
For more information about formatting a value displayed in a view, see Formatting Displayed
Data.

For more information about using format strings in wide views, see Creating a Wide View.

Example
The following example shows how to define a formatting string for the value of the StartTime
property.

  XML

  <WideItem>
    <PropertyName>StartTime</PropertyName>
    <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
  </WideItem>

See Also
Creating a Wide View

WideItem Element for WideControl

Writing a Windows PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2814 -->

PropertyName Element for WideItem for
WideControl
Specifies the property of the object whose value is displayed in the wide view.

     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     WideItem Element
     PropertyName Element

Syntax
 XML

 <PropertyName>.NetTypeProperty</PropertyName>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
PropertyName element.

Attributes
None.

Child Elements
None.

Parent Elements

                                                                                  ﾉ   Expand table

<!-- p.2815 -->

 Element               Description

 WideItem Element      Defines the property or script whose value is displayed in the wide view.

Text Value
Specify the name of the property whose value is displayed.

Remarks
For more information about the components of a wide view, see Creating a Wide View.

Example
This example shows a wide view that displays the value of the ProcessName property of the
System.Diagnostics.Process object.

 XML

 View>
   <Name>process</Name>
   <ViewSelectedBy>
     <TypeName>System.Diagnostics.Process</TypeName>
   </ViewSelectedBy>
   <WideControl>
     <WideEntries>
       <WideEntry>
         <WideItem>
           <PropertyName>ProcessName</PropertyName>
         </WideItem>
       </WideEntry>
     </WideEntries>
   </WideControl>
 </View>

See Also
WideItem Element

Creating a Wide View

Writing a PowerShell Formatting File

<!-- p.2816 -->

Last updated on 05/20/2025

<!-- p.2817 -->

ScriptBlock Element for WideItem for
WideControl
Specifies the script whose value is displayed in the wide view.

Schema
     Configuration Element
     ViewDefinitions Element
     View Element
     WideControl Element
     WideEntries Element
     WideEntry Element
     WideItem Element
     ScriptBlock Element

Syntax
 XML

 <ScriptBlock>ScriptToExecute</ScriptBlock>

Attributes and Elements
The following sections describe the attributes, child elements, and parent element of the
ScriptBlock element.

Attributes
None.

Child Elements
None.

Parent Elements

<!-- p.2818 -->

                                                                                          ﾉ   Expand table

 Element                Description

 WideItem Element       Defines the property or script block whose value is displayed in the wide view.

Text Value
Specify the script whose value is displayed.

Remarks
For more information about the components of a wide view, see Creating a Wide View.

Example
This example shows a WideItem element that defines a script whose value is displayed in the
view.

  XML

  <WideItem>
    <ScriptBlock>ScriptToExecute</ScriptBlock>
  </WideItem>

See Also
WideItem Element

Creating a Wide View

Writing a PowerShell Formatting File

 Last updated on 05/20/2025

<!-- p.2819 -->

Writing Help for PowerShell Scripts and
Functions
PowerShell scripts and functions should be fully documented whenever they're shared with
others. The Get-Help cmdlet displays the script and function help topics in the same format as
it displays help for cmdlets, and all the Get-Help parameters work on script and function help
topics.

PowerShell scripts can include a help topic about the script and help topics about each
functions in the script. Functions that are shared independently of scripts can include their own
help topics.

This document explains the format and correct placement of the help topics, and it suggests
guidelines for the content.

Types of Script and Function Help
Comment-Based Help
The help topic that describes a script or function can be implemented as a set of comments
within the script or function. When writing comment-based help for a script and for functions
in a script, pay careful attention to the rules for placing the comment-based help. The
placement determines whether the Get-Help cmdlet associates the help topic with the script or
a function. For more information about writing comment-based help topics, see
about_Comment_Based_Help.

XML-Based Command Help
The help topic that describes a script or function can be implemented in an XML file that uses
the command help schema. To associate the script or function with the XML file, use the
.EXTERNALHELP comment keyword followed by the path and name of the XML file.

When the .EXTERNALHELP comment keyword is present, it takes precedence over comment-
based help, even when Get-Help can't find a help file that matches the value of the
.EXTERNALHELP keyword.

Online Help

<!-- p.2820 -->

You can post your help topics on the internet and then direct Get-Help to open the topics. For
more information about writing comment-based help topics, see Supporting Online Help.

There is no established method for writing conceptual ("About") topics for scripts and
functions. However, you can post conceptual topics on the internet list the topics and their
URLs in the Related Links section of a command help topic.

Content Considerations for Script and Function
Help
     If you are writing a very brief help topic with only a few of the available command help
     sections, be sure to include clear descriptions of the script or function parameters. Also
     include one or two sample commands in the examples section, even if you decide to omit
     example descriptions.

     In all descriptions, refer to the command as a script or function. This information helps
     the user to understand and manage the command.

     For example, the following detailed description states that the New-Topic command is a
     script. This reminds users that they need to specify the path and full name when they run
     it.

           "The New-Topic script creates a blank conceptual topic for each topic name in the
           input file..."

     The following detailed description states that Disable-PSRemoting is a function. This
     information is particularly useful to users when the session includes multiple commands
     with the same name, some of which might be hidden by a command with higher
     precedence.

           The Disable-PSRemoting function disables all session configurations on the local
           computer...

     In a script help topic, explain how to use the script as a whole. If you are also writing help
     topics for functions in the script, mention the functions in your script help topic and
     include references to the function help topics in the Related Links section of the script
     help topic. Conversely, when a function is part of a script, explain in the function help
     topic the role that the function plays in the script and how it might be used

<!-- p.2821 -->

     independently. Then list the script help topic in the Related Links section of the function
     help topic.

     When writing examples for a script help topic, be sure to include the path to the script file
     in the example command. This reminds users that they must specify the path explicitly,
     even when the script is in the current directory.

     In a function help topic, remind users that the function exists only in the current session
     and, to use it in other sessions, they need to add it, or add it a PowerShell profile.

     Get-Help displays the help topic for a script or function only when the script file and help

     topic files are saved in the correct locations. Therefore, it's not useful to include
     instructions for installing PowerShell, or saving or installing the script or function in a
     script or function help topic. Instead, include any installation instructions in the document
     that you use to distribute the script or function.

See Also
Writing Comment-Based Help Topics

Last updated on 05/20/2025

<!-- p.2822 -->

Writing Comment-Based Help Topics
You can write comment-based Help topics for functions and scripts using special Help
comment keywords.

The Get-Help cmdlet displays comment-based Help in the same format in which it displays the
cmdlet Help topics that are generated from XML files. Users can use all of the parameters of
Get-Help , such as Detailed, Full, Example, and Online, to display function and script Help.

You can also write XML-based Help topics for scripts and functions and use the Help comment
keywords to redirect users to the XML-based topics or other topics.

In This Section
     Syntax of Comment-Based Help - Describes the syntax of comment-based help.
     Comment-Based Help Keywords - Lists the keywords in comment-based help.
     Placing Comment-Based Help in Functions - Shows where to place comment-based help
     for a function.
     Placing Comment-Based Help in Scripts - Shows where to place comment-based help for
     a script.

Last updated on 05/20/2025

<!-- p.2823 -->

Syntax of Comment-Based Help
This section describes the syntax of comment-based help.

Syntax Diagram
The syntax for comment-based Help is as follows:

  # .< help keyword>
  # <help content>

-or -

  <#
  .< help keyword>
  < help content>
  #>

Syntax Description
Comment-based Help is written as a series of comments. You can type a comment symbol ( # )
before each line of comments, or you can use the <# and #> symbols to create a comment
block. All the lines within the comment block are interpreted as comments.

Each section of comment-based Help is defined by a keyword and each keyword is preceded
by a dot ( . ). The keywords can appear in any order. The keyword names aren't case-sensitive.

A comment block must contain at least one help keyword. Some of the keywords, such as
.EXAMPLE , can appear many times in the same comment block. The Help content for each

keyword begins on the line after the keyword and can span multiple lines.

All the lines in a comment-based Help topic must be contiguous. If a comment-based Help
topic follows a comment that isn't part of the Help topic, there must be at least one blank line
between the last non-Help comment line and the beginning of the comment-based Help.

<!-- p.2824 -->

For example, the following comment-based help topic contains the .DESCRIPTION keyword and
its value, which is a description of a function or script.

  PowerShell

  <#
      .DESCRIPTION
      The Get-Function function displays the name and syntax of all functions in the
  session.
  #>

 Last updated on 05/20/2025

<!-- p.2825 -->

Comment-Based Help Keywords
09/23/2025

This topic lists and describes the keywords in comment-based help.

Keywords in Comment-Based Help
The following are valid comment-based Help keywords. They're listed in the order in which
they typically appear in a Help topic along with their intended use. These keywords can appear
in any order in the comment-based Help, and they're not case-sensitive.

Note that the .EXTERNALHELP keyword takes precedence over all other comment-based help
keywords. When .EXTERNALHELP is present, the Get-Help cmdlet doesn't display comment-
based help, even when it can't find a help file that matches the value of the keyword.

.SYNOPSIS
A brief description of the function or script. This keyword can be used only once in each topic.

.DESCRIPTION
A detailed description of the function or script. This keyword can be used only once in each
topic.

.PARAMETER <Parameter-Name>
The description of a parameter. You can include a .PARAMETER keyword for each parameter in
the function or script.

The .PARAMETER keywords can appear in any order in the comment block, but the order in
which the parameters appear in the param statement or function declaration determines the
order in which the parameters appear in Help topic. To change the order of parameters in the
Help topic, change the order of the parameters in the param statement or function declaration.

You can also specify a parameter description by placing a comment in the param statement
immediately before the parameter variable name. If you use both a param statement comment
and a .PARAMETER keyword, the description associated with the .PARAMETER keyword is used,
and the param statement comment is ignored.

<!-- p.2826 -->

.EXAMPLE
A sample command that uses the function or script, optionally followed by sample output and
a description. Repeat this keyword for each example.

.INPUTS
The .NET types of objects that can be piped to the function or script. You can also include a
description of the input objects. Repeat this keyword for each input type.

.OUTPUTS
The .NET type of the objects that the cmdlet returns. You can also include a description of the
returned objects. Repeat this keyword for each output type.

.NOTES
Additional information about the function or script.

.LINK
The name of a related topic. Repeat this keyword for each related topic. This content appears in
the Related Links section of the Help topic.

The .LINK keyword content can also include a Uniform Resource Identifier (URI) to an online
version of the same help topic. The online version opens when you use the Online parameter
of Get-Help . The URI must begin with http or https .

.COMPONENT
The name of the technology or feature that the function or script uses, or to which it's related.
The Component parameter of Get-Help uses this value to filter the search results returned by
Get-Help .

.ROLE
The name of the user role for the help topic. The Role parameter of Get-Help uses this value to
filter the search results returned by Get-Help .

<!-- p.2827 -->

.FUNCTIONALITY
The keywords that describe the intended use of the function. The Functionality parameter of
Get-Help uses this value to filter the search results returned by Get-Help .

.FORWARDHELPTARGETNAME <Command-Name>
Redirects to the help topic for the specified command. You can redirect users to any help topic,
including help content for a function, script, cmdlet, or provider.

  PowerShell

  # .FORWARDHELPTARGETNAME <Command-Name>

.FORWARDHELPCATEGORY
Specifies the help category of the item in .FORWARDHELPTARGETNAME . Valid values are Alias ,
Cmdlet , HelpFile , Function , Provider , General , FAQ , Glossary , ScriptCommand ,

ExternalScript , Filter , or All . Use this keyword to avoid conflicts when there are commands

with the same name.

  PowerShell

  # .FORWARDHELPCATEGORY <Category>

.REMOTEHELPRUNSPACE <PSSession-variable>
Specifies a session that contains the help topic. Enter a variable that contains a PSSession
object. This keyword is used by the [Export-PSSession][09] cmdlet to find the help content for
the exported commands.

  PowerShell

  # .REMOTEHELPRUNSPACE <PSSession-variable>

.EXTERNALHELP
Specifies an XML-based help file for the script or function.

<!-- p.2828 -->

  PowerShell

  # .EXTERNALHELP <XML Help File>

The .EXTERNALHELP keyword is required when a function or script is documented in XML files.
Without this keyword, Get-Help can't find the XML-based help file for the function or script.

The .EXTERNALHELP keyword takes precedence over other comment-based help keywords. If
.EXTERNALHELP is present, Get-Help doesn't display comment-based help, even if it can't find a

help topic that matches the value of the .EXTERNALHELP keyword.

If the function is exported by a module, set the value of the .EXTERNALHELP keyword to a
filename without a path. Get-Help looks for the specified filename in a language-specific
subdirectory of the module directory. There are no requirements for the name of the XML-
based help file for a function. Beginning in PowerShell 5.0, functions that are exported by a
module can be documented in a help file that's named for the module. You don't need to use
.EXTERNALHELP comment keyword. For example, if the Test-Function function is exported by

the MyModule module, you can name the help file MyModule-help.xml . The Get-Help cmdlet
looks for help for the Test-Function function in the MyModule-help.xml file in the module
directory.

If the function isn't included in a module, include a path to the XML-based help file. If the value
includes a path and the path contains UI-culture-specific subdirectories, Get-Help searches the
subdirectories recursively for an XML file with the name of the script or function in accordance
with the language fallback standards established for Windows, just as it does in a module
directory.

For more information about the cmdlet help XML-based help file format, see How to Write
Cmdlet Help.

<!-- p.2829 -->

Placing Comment-Based Help in Functions
This topic explains where to place comment-based help for a function so that the Get-Help
cmdlet associates the comment-based help topic with the correct function.

Where to Place Comment-Based Help for a
Function
     At the beginning of the function body.

     At the end of the function body.

     Before the Function keyword. When the function is in a script or script module, there
     can't be more than one blank line between the last line of the comment-based help and
     the Function keyword. Otherwise, Get-Help associates the help with the script, not with
     the function.

Examples of Help Placement in a Function
The following examples show each of the three placement options for comment-based help for
a function.

Help at the Beginning of a Function Body
The following example shows comment-based at the beginning of a function body.

 PowerShell

 function MyProcess
 {
     <#
        .DESCRIPTION
        The MyProcess function gets the Windows PowerShell process.
     #>

      Get-Process powershell
 }

Help at the End of a Function Body

<!-- p.2830 -->

The following example shows comment-based at the end of a function body.

 PowerShell

 function MyFunction
 {
     Get-Process powershell

      <#
           .DESCRIPTION
           The MyProcess function gets the Windows PowerShell process.
      #>
 }

Help Before the Function Keyword
The following examples shows comment-based on the line before the function keyword.

 PowerShell

 <#
      .DESCRIPTION
      The MyProcess function gets the Windows PowerShell process.
 #>
 function MyFunction { Get-Process powershell}

Last updated on 05/20/2025

<!-- p.2831 -->

Placing Comment-Based Help in Scripts
This topic explains where to place comment-based help for a script so that the Get-Help
cmdlet associates the comment-based help topic with scripts and not with any functions that
might be in the script.

Where to Place Comment-Based Help for a Script
      At the beginning of the script file.

      Script Help can be preceded in the script only by comments and blank lines.

      At the end of the script file.

      If the first item in the script body (after the Help) is a function declaration, there must be
      at least two blank lines between the end of the script Help and the function declaration.
      Otherwise, the Help is interpreted as being Help for the function, not Help for the script.

Examples of Help Placement in a Script
The following examples show each of the placement options for comment-based help for a
script.

Help at the Beginning of a Script
The following example shows comment-based at the beginning of a script.

  PowerShell

  <#
  .DESCRIPTION
  This script performs a series of network connection tests.
  #>

  param [string]$ComputerName
  ...

Help at the End of a Script
The following example shows comment-based at the end of a script.

<!-- p.2832 -->

 PowerShell

 ...
 function Ping { Test-Connection -ComputerName $ComputerName }

 <#
 .DESCRIPTION
 This script performs a series of network connection tests.
 #>

Last updated on 05/20/2025

<!-- p.2833 -->

Autogenerated Elements of Comment-
Based Help
The Get-Help cmdlet automatically generates several elements of a comment-based topic.
These autogenerated elements make comment-based help look very much like the help that's
generated from XML files.

Autogenerated Elements
The Get-Help cmdlet automatically generates the following elements of a help topic. You can't
edit these elements directly, but you can change the results by changing the source of the
element.

Name
The Name section of a function Help topic is taken from the function name in the function
definition. The Name of a script Help topic is taken from the script filename. To change the
name or its capitalization, change the function definition or the script filename.

Syntax
The Syntax section of the Help topic is generated from the parameter list in the param
statement of the function or script. To add detail to the Help topic syntax, such as the .NET type
of a parameter, add the detail to the parameter list. If you don't specify a parameter type, the
Object type is inserted as the default value.

Parameter List
The Parameters section of the Help topic is generated from the parameter list in the function or
script and from the descriptions that you add using the .PARAMETER keyword or comments in
the parameter list.

Parameters appear in the Parameters section in the same order that they appear in the
parameter list. The spelling and capitalization of parameter names is also taken from the
parameter list; it isn't affected by the parameter name specified by the .PARAMETER keyword.

Common Parameters

<!-- p.2834 -->

The common parameters are added to the syntax and parameter list of the Help topic, even if
they have no effect. For more information about the common parameters, see
about_CommonParameters.

Parameter Attribute Table
Get-Help generates the table of parameter attributes that appears when you use the Full or

Parameter parameter of Get-Help . The value of the Required, Position, and Default value
attributes is taken from the function or script syntax.

Remarks
The Remarks section of the Help topic is automatically generated from the function or script
name. You can't change or affect its content.

 Last updated on 05/20/2025

<!-- p.2835 -->

Examples of Comment-based Help
This topic includes examples that demonstrate how to use comment-based help for scripts and
functions.

Example 1: Comment-based Help for a Function
The following sample function includes comment-based Help.

 PowerShell

 function Add-Extension
 {
     param ([string]$Name,[string]$Extension = "txt")
     $Name = $Name + "." + $Extension
     $Name

      <#
             .SYNOPSIS
             Adds a file name extension to a supplied name.

             .DESCRIPTION
             Adds a file name extension to a supplied name.
             Takes any strings for the file name or extension.

             .PARAMETER Name
             Specifies the file name.

             .PARAMETER Extension
             Specifies the extension. "Txt" is the default.

             .INPUTS
             None. You can't pipe objects to Add-Extension.

             .OUTPUTS
             System.String. Add-Extension returns a string with the extension or file
 name.

             .EXAMPLE
             PS> Add-Extension -Name "File"
             File.txt

             .EXAMPLE
             PS> Add-Extension -Name "File" -Extension "doc"
             File.doc

             .EXAMPLE
             PS> Add-Extension "File" "doc"

<!-- p.2836 -->

             File.doc

             .LINK
             Online version: http://www.fabrikam.com/add-extension.html

             .LINK
             Set-Item
        #>
 }

The following output shows the results of a Get-Help command that displays the help for the
Add-Extension function.

 PowerShell

 PS> Get-Help Add-Extension -Full

 Output

 NAME
        Add-Extension

 SYNOPSIS
     Adds a file name extension to a supplied name.

 SYNTAX
     Add-Extension [[-Name] <String>] [[-Extension] <String>] [<CommonParameters>]

 DESCRIPTION
     Adds a file name extension to a supplied name. Takes any strings for the file
 name or extension.

 PARAMETERS
     -Name
         Specifies the file name.

             Required?                     false
             Position?                     0
             Default value
             Accept pipeline input?        false
             Accept wildcard characters?

        -Extension
            Specifies the extension. "Txt" is the default.

             Required?                     false
             Position?                     1
             Default value
             Accept pipeline input?        false
             Accept wildcard characters?

<!-- p.2837 -->

       <CommonParameters>
           This cmdlet supports the common parameters: -Verbose, -Debug,
           -ErrorAction, -ErrorVariable, -WarningAction, -WarningVariable,
           -OutBuffer and -OutVariable. For more information, type
           "Get-Help about_CommonParameters".

 INPUTS
     None. You can't pipe objects to Add-Extension.

 OUTPUTS
     System.String. Add-Extension returns a string with the extension or file name.

       -------------------------- EXAMPLE 1 --------------------------

       PS> Add-Extension -Name "File"
       File.txt

       -------------------------- EXAMPLE 2 --------------------------

       PS> Add-Extension -Name "File" -Extension "doc"
       File.doc

       -------------------------- EXAMPLE 3 --------------------------

       PS> Add-Extension "File" "doc"
       File.doc

 RELATED LINKS
     Online version: http://www.fabrikam.com/add-extension.html
     Set-Item

Example 2: Comment-based Help for a Script
The following sample function includes comment-based Help.

Notice the blank lines between the closing #> and the param statement. In a script that doesn't
have a param statement, there must be at least two blank lines between the final comment in
the Help topic and the first function declaration. Without these blank lines, Get-Help associates
the Help topic with the function, instead of the script.

 PowerShell

 <#
      .SYNOPSIS
      Performs monthly data updates.

      .DESCRIPTION
      The Update-Month.ps1 script updates the registry with new data generated
      during the past month and generates a report.

<!-- p.2838 -->

    .PARAMETER InputPath
    Specifies the path to the CSV-based input file.

    .PARAMETER OutputPath
    Specifies the name and path for the CSV-based output file. By default,
    MonthlyUpdates.ps1 generates a name from the date and time it runs, and
    saves the output in the local directory.

    .INPUTS
    None. You can't pipe objects to Update-Month.ps1.

    .OUTPUTS
    None. Update-Month.ps1 doesn't generate any output.

    .EXAMPLE
    PS> .\Update-Month.ps1

    .EXAMPLE
    PS> .\Update-Month.ps1 -InputPath C:\Data\January.csv

    .EXAMPLE
    PS> .\Update-Month.ps1 -InputPath C:\Data\January.csv -OutputPath
 C:\Reports\2009\January.csv
 #>

 param ([string]$InputPath, [string]$OutputPath)

 function Get-Data { }

The following command gets the script Help. Because the script isn't in a directory that's listed
in the PATH environment variable, the Get-Help command that gets the script Help must
specify the script path.

 PowerShell

 PS> Get-Help C:\ps-test\update-month.ps1 -Full

 Output

 NAME
        C:\ps-test\Update-Month.ps1

 SYNOPSIS
     Performs monthly data updates.

 SYNTAX
     C:\ps-test\Update-Month.ps1 [-InputPath] <String> [[-OutputPath]
     <String>] [<CommonParameters>]

 DESCRIPTION
     The Update-Month.ps1 script updates the registry with new data

<!-- p.2839 -->

    generated during the past month and generates a report.

PARAMETERS
    -InputPath
        Specifies the path to the CSV-based input file.

          Required?                     true
          Position?                     0
          Default value
          Accept pipeline input?        false
          Accept wildcard characters?

    -OutputPath
        Specifies the name and path for the CSV-based output file. By
        default, MonthlyUpdates.ps1 generates a name from the date
        and time it runs, and saves the output in the local directory.

          Required?                     false
          Position?                     1
          Default value
          Accept pipeline input?        false
          Accept wildcard characters?

    <CommonParameters>
        This cmdlet supports the common parameters: -Verbose, -Debug,
        -ErrorAction, -ErrorVariable, -WarningAction, -WarningVariable,
        -OutBuffer and -OutVariable. For more information, type,
        "Get-Help about_CommonParameters".

INPUTS
          None. You can't pipe objects to Update-Month.ps1.

OUTPUTS
          None. Update-Month.ps1 doesn't generate any output.

-------------------------- EXAMPLE 1 --------------------------

PS> .\Update-Month.ps1

-------------------------- EXAMPLE 2 --------------------------

PS> .\Update-Month.ps1 -InputPath C:\Data\January.csv

-------------------------- EXAMPLE 3 --------------------------

PS> .\Update-Month.ps1 -InputPath C:\Data\January.csv -OutputPath
C:\Reports\2009\January.csv

RELATED LINKS

Example 3: Parameter Descriptions in a param
Statement

<!-- p.2840 -->

This example shows how to insert parameter descriptions in the param statement of a function
or script. This format is most useful when the parameter descriptions are brief.

 PowerShell

 function Add-Extension
 {
     param
     (
         [string]
         # Specifies the file name.
         $Name,

            [string]
            # Specifies the file name extension. "Txt" is the default.
            $Extension = "txt"
       )
       $Name = $Name + "." + $Extension
       $Name

       <#
            .SYNOPSIS
            Adds a file name extension to a supplied name.
 ...
       #>
 }

The results are the same as the results for Example 1. Get-Help interprets the parameter
descriptions as though they were accompanied by the .PARAMETER keyword.

Example 4: Redirecting to an XML File
You can write XML-based Help topics for functions and scripts. Although comment-based Help
is easier to implement, XML-based Help is required if you want more precise control over Help
content or if you are translating Help topics into multiple languages.The following example
shows the first few lines of the Update-Month.ps1 script. The script uses the .EXTERNALHELP
keyword to specify the path to an XML-based Help topic for the script.

 PowerShell

 # .EXTERNALHELP C:\MyScripts\Update-Month-Help.xml

       param ([string]$InputPath, [string]$OutputPath)

       function Get-Data { }

The following example shows the use of the .EXTERNALHELP keyword in a function.
