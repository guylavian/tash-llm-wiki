---
title: "How to use this documentation — pages 2841-2880"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2841-2880
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2841-2880
family: powershell
documentKind: "doc"
abstract: "PowerShell function Add-Extension { param ([string]$Name, [string]$Extension = \"txt\") $Name = $Name + \".\" + $Extension $Name # .EXTERNALHELP C:\\ps-test\\Add-Extension.xml } Example 5: Redirecting to a Different Help Topic The following code is an excerpt from the beginning of the"
---

# How to use this documentation — pages 2841-2880

<!-- p.2841 -->

 PowerShell

 function Add-Extension
 {
     param ([string]$Name, [string]$Extension = "txt")
     $Name = $Name + "." + $Extension
     $Name

        # .EXTERNALHELP C:\ps-test\Add-Extension.xml
 }

Example 5: Redirecting to a Different Help Topic
The following code is an excerpt from the beginning of the built-in help function in
PowerShell, which displays one screen of Help text at a time. Because the Help topic for the
Get-Help cmdlet describes the Help function, the Help function uses the
.FORWARDHELPTARGETNAME and .FORWARDHELPCATEGORY keywords to redirect the user to the Get-

Help cmdlet Help topic.

 PowerShell

 function help
 {
     <#
       .FORWARDHELPTARGETNAME Get-Help
       .FORWARDHELPCATEGORY Cmdlet
     #>
     [CmdletBinding(DefaultParameterSetName='AllUsersView')]
     param(
             [Parameter(Position=0, ValueFromPipelineByPropertyName=$true)]
             [System.String]
             ${Name},
     ...
 }

The following command uses this feature. When a user types a Get-Help command for the
help function, Get-Help displays the Help topic for the Get-Help cmdlet.

 PowerShell

 PS> Get-Help help

 Output

 NAME
        Get-Help

<!-- p.2842 -->

 SYNOPSIS
     Displays information about Windows PowerShell cmdlets and concepts.
 ...

Last updated on 05/20/2025

<!-- p.2843 -->

Writing Help for PowerShell Cmdlets
PowerShell cmdlets can be useful, but unless your Help topics clearly explain what the cmdlet
does and how to use it, the cmdlet may not get used or, even worse, it might frustrate users.
The XML-based cmdlet Help file format enhances consistency, but great help requires much
more.

If you have never written cmdlet Help, review the following guidelines. The XML schema
required to author the cmdlet Help topic is described in the following section. Start with
Creating the Cmdlet Help File. That topic includes a description of the top-level XML nodes.

Writing Guidelines for Cmdlet Help
Write well
Nothing replaces a well-written topic. If you aren't a professional writer, find a writer or editor
to help you. Another alternative is to copy your Help text into Microsoft Word and use the
grammar and spelling checks to improve your work.

Write simply
Use simple words and phrases. Avoid jargon. Consider that many readers are equipped only
with a foreign-language dictionary and your Help topic.

Write consistently
Help for related cmdlets should be similar (for example, Get-Content and Set-Content ). Use
the standard descriptions for standard parameters, like Force and InputObject. (Copy them
from Help for the core cmdlets.) Use standard terms. For example, use "parameter", not
"argument", and use "cmdlet" not "command" or "command-let."

Start the synopsis with a verb
The synopsis field informs the user what the cmdlet does, not what it's or how it works. Verbs
create a task-based statement that informs users if this cmdlet meets their requirements. Use
simple verbs like "get", "create", and "change." Avoid "set", which can be vague and fancy
words like "modify".

<!-- p.2844 -->

Focus on objects
Most "get" cmdlets display something, but their primary function is to get an object. In your
Help, focus on the object, so that users understand that the default display is one of many, and
that they can use the methods and properties of the object that you retrieved for them in
different ways.

Write detailed descriptions
Briefly list everything that the cmdlet can do in the detailed description. If the main function is
to change one property, but the cmdlet can change all properties, list this in the detailed
description.

Use conventional syntax
Use the standard Backus-Naur format which is common for Windows and Unix command-line
Help.

Use Microsoft .NET types for parameter values
The placeholders for parameter values (in the syntax and parameter descriptions) show the
.NET Framework types of the objects that the parameter will accept. The PowerShell team
developed this convention to help teach users about the .NET Framework.

Write complete parameter descriptions
Parameter descriptions must inform users of two things: what the parameter does (its effect)
and what they must type for the parameter values.

Write practical examples
The examples should show how to use all of the parameters, but the most important thing is to
show how to use the cmdlet in real-world tasks. Start with a simple example and write
increasingly complex examples. In the final example, show how to use the cmdlet in a pipeline.

Use the Notes field
Use the Notes field to explain concepts that users need to understand the cmdlet. You can also
use notes to help users avoid common errors. Avoid URLs as they change. Instead, provide
users terms to search for.

<!-- p.2845 -->

Test your Help
Test the Help just like you test your code. Have friends and colleagues read your Help content
and provide feedback. You can also solicit feedback from newsgroups.

See Also
     How to Create the Cmdlet Help File
     How to Add the Cmdlet Name and Synopsis to a Cmdlet Help Topic
     How to Add the Detailed Description to a Cmdlet Help Topic
     How to Add Syntax to a Cmdlet Help Topic
     How to Add Parameters to a Cmdlet Help Topic
     How to add Input Types to a Cmdlet Help Topic
     How to Add Return Values to a Cmdlet Help Topic
     How to Add Notes to a Cmdlet Help Topic
     How to Add Examples to a Cmdlet Help Topic
     How to Add Related Links to a Cmdlet Help Topic
     Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.2846 -->

How to create the cmdlet help file

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section describes how to create a valid XML file that contains content for Windows
PowerShell cmdlet Help topics. This section discusses how to name the Help file, how to add
the appropriate XML headers, and how to add nodes that will contain the different sections of
the cmdlet Help content.

  ７ Note

  For a complete view of a Help file, open one of the dll-Help.xml files located in the
  Windows PowerShell installation directory. For example, the
  Microsoft.PowerShell.Commands.Management.dll-Help.xml file contains content for several

  of the PowerShell cmdlets.

How to create a cmdlet help file
   1. Create a text file and save it using UTF8 encoding. The filename must have the following
     format so that Windows PowerShell can detect it as a cmdlet Help file.

     <PSSnapInAssemblyName>.dll-Help.xml

   2. Add the following XML headers to the text file. Be aware that the file will be validated
     against the Microsoft Assistance Markup Language (MAML) schema. Currently,
     PowerShell doesn't provide any tools to validate the file.

     <?xml version="1.0" encoding="utf-8" ?> <helpItems xmlns="http://msh" schema="maml">

   3. Add a Command node to the cmdlet Help file for each cmdlet in the assembly. Each node
     within the Command node relates to the different sections of the cmdlet Help topic.

<!-- p.2847 -->

     The following table lists the XML element for each node, followed by a descriptions of
     each node.

                                                                                      ﾉ     Expand table

       Node                     Description

       <details>                Adds content for the NAME and SYNOPSIS sections of the cmdlet Help
                                topic. For more information, see How to Add the Cmdlet Name and
                                Synopsis.

       <maml:description>       Adds content for the DESCRIPTION section of the cmdlet Help topic. For
                                more information, see How to Add the Detailed Description to a Cmdlet
                                Help Topic.

       <command:syntax>         Adds content for the SYNTAX section of the cmdlet Help topic. For more
                                information, see How to Add Syntax to a Cmdlet Help Topic.

       <command:parameters>     Adds content for the PARAMETERS section of the cmdlet Help topic. For
                                more information, see How to Add Parameters to a Cmdlet Help Topic.

       <command:inputTypes>     Adds content for the INPUTS section of the cmdlet Help topic. For more
                                information, see How to Add Input Types to a Cmdlet Help Topic.

       <command:returnValues>   Adds content for the OUTPUTS section of the cmdlet Help topic. For
                                more information, see How to Add Return Values to a Cmdlet Help Topic.

       <maml:alertset>          Adds content for the NOTES section of the cmdlet Help topic. For more
                                information, see How to add Notes to a Cmdlet Help Topic.

       <command:examples>       Adds content for the EXAMPLES section of the cmdlet Help topic. For
                                more information, see How to Add Examples to a Cmdlet Help Topic.

       <maml:relatedLinks>      Adds content for the RELATED LINKS section of the cmdlet Help topic.
                                For more information, see How to Add Related Links to a Cmdlet Help
                                Topic.

Example
Here is an example of a Command node that includes the nodes for the various sections of the
cmdlet Help topic.

 XML

 <command:command
   xmlns:maml="http://schemas.microsoft.com/maml/2004/10"
   xmlns:command="http://schemas.microsoft.com/maml/dev/command/2004/10"
   xmlns:dev="http://schemas.microsoft.com/maml/dev/2004/10">
   <command:details>

<!-- p.2848 -->

     <!--Add name and synopsis here-->
   </command:details>
   <maml:description>
     <!--Add detailed description here-->
   </maml:description>
   <command:syntax>
     <!--Add syntax information here-->
   </command:syntax>
   <command:parameters>
     <!--Add parameter information here-->
   </command:parameters>
   <command:inputTypes>
     <!--Add input type information here-->
   </command:inputTypes>
   <command:returnValues>
     <!--Add return value information here-->
   </command:returnValues>
   <maml:alertSet>
     <!--Add Note information here-->
   </maml:alertSet>
   <command:examples>
     <!--Add cmdlet examples here-->
   </command:examples>
   <maml:relatedLinks>
     <!--Add links to related content here-->
   </maml:relatedLinks>
 </command:command>

See also
     How to Add the Cmdlet Name and Synopsis
     How to Add the Detailed Description to a Cmdlet Help Topic
     How to Add Syntax to a Cmdlet Help Topic
     How to Add Parameters to a Cmdlet Help Topic
     How to Add Input Types to a Cmdlet Help Topic
     How to Add Return Values to a Cmdlet Help Topic
     How to add Notes to a Cmdlet Help Topic
     How to Add Examples to a Cmdlet Help Topic
     How to Add Related Links to a Cmdlet Help Topic
     Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.2849 -->

How to add the cmdlet name and synopsis
to a cmdlet help topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier to
  write and maintain help. PlatyPS can also create the Updateable Help packages for you. For
  more information, see Create XML-based help using PlatyPS.

This section describes how to add content that's displayed in the NAME and SYNOPSIS sections
of the cmdlet help. In the Help file, this content is added to the Command node for each cmdlet.

  ７ Note

  For a complete view of a Help file, open one of the dll-Help.xml files located in the
  PowerShell installation directory. For example, the
  Microsoft.PowerShell.Commands.Management.dll-Help.xml file contains content for several of

  the PowerShell cmdlets.

To add the cmdlet name and a synopsis
The cmdlet Help can display two descriptions for the cmdlet. The first description is a short
description that's referred to as the synopsis. The second description is a more detailed
description that's discussed in Adding the Detailed Description to a Cmdlet Help Topic. Both
these descriptions should be written as a single paragraph.

The <command:details> node contains the cmdlet name and the synopsis. The cmdlet name is
enclosed in a <command:name> element, and the synopsis is enclosed in a <maml:description>
element. The <command:verb> and <command:noun> elements contain the cmdlet verb and noun,
respectively. For example, the following XML shows the <command:details> node for the Get-
ChildItem cmdlet.

 XML

<!-- p.2850 -->

 <command:details>
   <command:name>Get-ChildItem</command:name>
   <maml:description>
     <maml:para>Gets the items and child items in one or more specified locations.
 </maml:para>
   </maml:description>
   <command:verb>Get</command:verb>
   <command:noun>ChildItem</command:noun>
 </command:details>

Writing tips
     In the synopsis don't repeat the cmdlet name. Informing the user that the Get-Server
     cmdlet gets a server is brief, but not informative. Instead, use synonyms and add details to
     the description.

     Example: "Gets an object that represents a local or remote computer."

     Use simple verbs like "get", "create", and "change" in the synopsis. Avoid using "set"
     because it is vague, and fancy words such as "modify."

     Example: "Gets information about the Authenticode signature in a file."

     Write in active voice. For example, "Use the TimeSpan object..." is much clearer than "the
     TimeSpan object can be used to..."

     Avoid the verb "display" when describing cmdlets that get objects. Although Windows
     PowerShell displays cmdlet data, it's important to introduce users to the concept that the
     cmdlet returns .NET Framework objects whose data may not be displayed. If you emphasize
     the display, the user might not realize that the cmdlet may have returned many other useful
     properties and methods that aren't displayed.

See also
Windows PowerShell SDK

Last updated on 07/07/2026

<!-- p.2851 -->

How to Add a Cmdlet Description

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier to
  write and maintain help. PlatyPS can also create the Updateable Help packages for you. For
  more information, see Create XML-based help using PlatyPS.

This section describes how to add content that's displayed in the DESCRIPTION section of the
cmdlet Help. In the Help file, this content is added to the Command node for each cmdlet.

  ７ Note

  For a complete view of a Help file, open one of the dll-Help.xml files located in the
  PowerShell installation directory. For example, the
  Microsoft.PowerShell.Commands.Management.dll-Help.xml file contains content for several of

  the PowerShell cmdlets.

To Add a Description
The <maml:description> node contains the detailed description of the cmdlet. This element
contains one or more <maml:para> elements. The description is enclosed in a <maml:para>
element. The following example shows the structure of the XML:

 XML

 <maml:description>
   <maml:para>...</maml:para>
 </maml:description>

Writing tips
     Begin by explaining the basic features of the cmdlet in more detail. In many cases, you can
     explain the terms used in the cmdlet name and illustrate unfamiliar concepts with an
     example. For example, if the cmdlet appends data to a file, explain that it adds data to the
     end of an existing file.

<!-- p.2852 -->

     To find all of the features of the cmdlet, review the parameter list. Describe the primary
     function of the cmdlet, and then include other functions and features. For example, if the
     main function of the cmdlet is to change one property, but the cmdlet can change all of the
     properties, say so in the detailed description. If the cmdlet parameters let the users solicit
     information in different ways, explain it.

     Include information on ways that users can use the cmdlet, in addition to the obvious uses.
     For example, you can use the object that the Get-Host cmdlet retrieves to change the color
     of text in the Windows PowerShell command window.

     Example: "The Get-Acl cmdlet gets objects that represent the security descriptor of a file or
     resource. The security descriptor contains the access control lists (ACLs) of the resource. The
     ACL specifies the permissions that users and user groups have to access the resource."

     The detailed description should describe the cmdlet, but it shouldn't describe concepts that
     the cmdlet uses. Place concept definitions in Additional Notes.

See Also
Windows PowerShell SDK

Last updated on 07/07/2026

<!-- p.2853 -->

How to add syntax to a cmdlet help topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier to
  write and maintain help. PlatyPS can also create the Updateable Help packages for you. For
  more information, see Create XML-based help using PlatyPS.

Before you start to code the XML for the syntax diagram in the cmdlet Help file, read this section
to get a clear picture of the kind of data you need to provide, such as the parameter attributes,
and how that data is displayed in the syntax diagram..

Parameter attributes
     Required
        If true, the parameter must appear in all commands that use the parameter set.
        If false, the parameter is optional in all commands that use the parameter set.
     Position
        If named, the parameter name is required.
        If positional, the parameter name is optional. When it's omitted, the parameter value
        must be in the specified position in the command. For example, if the value is
        position="1", the parameter value must be the first or only unnamed parameter value in
        the command.
     Pipeline Input
        If true (ByValue), you can pipe input to the parameter. The input is associated with
        ("bound to") the parameter even if the property name and the object type don't match
        the expected type. The PowerShell parameter binding components try to convert the
        input to the correct type and fail the command only when the type can't be converted.
        Only one parameter in a parameter set can be associated by value.
        If true (ByPropertyName), you can pipe input to the parameter. However, the input is
        associated with the parameter only when the parameter name matches the name of a
        property of the input object. For example, if the parameter name is Path , objects piped
        to the cmdlet are associated with that parameter only when the object has a property
        named path.

<!-- p.2854 -->

        If true (ByValue, ByPropertyName), you can pipe input to the parameter either by
        property name or by value. Only one parameter in a parameter set can be associated by
        value.
        If false, you can't pipe input to this parameter.
     Globbing
        If true, the text that the user types for the parameter value can include wildcard
        characters.
        If false, the text that the user types for the parameter value can't include wildcard
        characters.

Parameter value attributes
     Required
        If true, the specified value must be used whenever using the parameter in a command.
        If false, the parameter value is optional. Typically, a value is optional only when it's one of
        several valid values for a parameter, such as in an enumerated type.

The Required attribute of a parameter value is different from the Required attribute of a
parameter.

The required attribute of a parameter indicates whether the parameter (and its value) must be
included when invoking the cmdlet. In contrast, the required attribute of a parameter value is
used only when the parameter is included in the command. It indicates whether that particular
value must be used with the parameter.

Typically, parameter values that are placeholders are required and parameter values that are
literal aren't required, because they're one of several values that might be used with the
parameter.

Gathering syntax information
   1. Start with the cmdlet name.

       SYNTAX
           Get-Tech

   2. List all the parameters of the cmdlet. Type a hyphen ( - ) before each parameter name.
     Separate the parameters into parameter sets (some cmdlets may have only one parameter

<!-- p.2855 -->

  set). In this example the Get-Tech cmdlet has two parameter sets.

    SYNTAX
        Get-Tech -Name -Type
        Get-Tech -Id -List -Type

  Start each parameter set with the cmdlet name.

  List the default parameter set first. The default parameter is specified by the cmdlet class.

  For each parameter set, list its unique parameter first, unless there are positional parameters
  that must appear first. In the previous example, the Name and Id parameters are unique
  parameters for the two parameter sets (each parameter set must have one parameter that's
  unique to that parameter set). This makes it easier for users to identify what parameter they
  need to supply for the parameter set.

  List the parameters in the order that they should appear in the command. If the order
  doesn't matter, list related parameters together, or list the most frequently used parameters
  first.

  Be sure to list the WhatIf and Confirm parameters if the cmdlet supports ShouldProcess.

  Don't list the common parameters (such as Verbose, Debug, and ErrorAction) in your syntax
  diagram. The Get-Help cmdlet adds that information for you when it displays the Help
  topic.

3. Add the parameter values. In PowerShell, parameter values are represented by their .NET
  type. However, the type name can be abbreviated, such as "string" for System.String.

    SYNTAX
        Get-Tech -Name string -Type Basic Advanced
        Get-Tech -Id int -List -Type Basic Advanced

  Abbreviate types as long as their meaning is clear, such as string for System.String and int
  for System.Int32.

  List all values of enumerations, such as the -Type parameter in the previous example, which
  can be set to basic or advanced.

<!-- p.2856 -->

  [switch] parameters, such as -List in the previous example, don't have values.

4. Add angle brackets to parameters values that are placeholder, as compared to parameter
  values that are literals.

    SYNTAX
        Get-Tech -Name <string> -Type Basic Advanced
        Get-Tech -Id <int> -List -Type Basic Advanced

5. Enclose optional parameters and their vales in square brackets.

    SYNTAX
        Get-Tech -Name <string> [-Type Basic Advanced]
        Get-Tech -Id <int> [-List] [-Type Basic Advanced]

6. Enclose optional parameters names (for positional parameters) in square brackets. The
  name for parameters that are positional, such as the Name parameter in the following
  example, don't have to be included in the command.

    SYNTAX
        Get-Tech [-Name] <string> [-Type Basic Advanced]
        Get-Tech -Id <int> [-List] [-Type Basic Advanced]

7. If a parameter value can contain multiple values, such as a list of names in the Name
  parameter, add a pair of square brackets directly following the parameter value.

    SYNTAX
        Get-Tech [-Name] <string[]> [-Type Basic Advanced]
        Get-Tech -Id <int[]> [-List] [-Type Basic Advanced]

8. If the user can choose from parameters or parameter values, such as the Type parameter,
  enclose the choices in curly brackets and separate them with the exclusive OR symbol(;).

    SYNTAX
        Get-Tech [-Name] <string[]> [-Type {Basic | Advanced}]

<!-- p.2857 -->

           Get-Tech -Id <int[]> [-List] [-Type {Basic | Advanced}]

   9. If the parameter value must use specific formatting, such as quotation marks or
     parentheses, show the format in the syntax.

       SYNTAX
           Get-Tech [-Name] <"string[]"> [-Type {Basic | Advanced}]
           Get-Tech -Id <int[]> [-List] [-Type {Basic | Advanced}]

Coding the syntax diagram XML
The syntax node of the XML begins immediately after the description node, which ends with the
</maml:description> tag. For information about gathering the data used in the syntax diagram,

see Gathering Syntax Information.

Adding a syntax node
The syntax diagram displayed in the cmdlet Help topic is generated from the data in the syntax
node of the XML. The syntax node is enclosed in a pair of <command:syntax> tags. With each
parameter set of the cmdlet enclosed in a pair of <command:syntaxitem> tags. There is no limit to
the number of <command:syntaxitem> tags that you can add.

The following example shows a syntax node that has syntax item nodes for two parameter sets.

 XML

 <command:syntax>
   <command:syntaxItem>
     ...
     <!--Parameter Set 1 (default parameter set) parameters go here-->
     ...
   </command:syntaxItem>
   <command:syntaxItem>
     ...
     <!--Parameter Set 2 parameters go here-->
     ...
   </command:syntaxItem>
 </command:syntax>

Adding the cmdlet name to the parameter set data

<!-- p.2858 -->

Each parameter set of the cmdlet is specified in a syntax item node. Each syntax item node begins
with a pair of <maml:name> tags that include the name of the cmdlet.

The following example includes a syntax node that has syntax item nodes for two parameter sets.

 XML

 <command:syntax>
   <command:syntaxItem>
     <maml:name>Cmdlet-Name</maml:name>
   </command:syntaxItem>
   <command:syntaxItem>
     <maml:name>Cmdlet-Name</maml:name>
   </command:syntaxItem>
 </command:syntax>

Adding parameters
Each parameter added to the syntax item node is specified within a pair of <command:parameter>
tags. You need a pair of <command:parameter> tags for each parameter included in the parameter
set, with the exception of the common parameters that are provided by PowerShell.

The attributes of the opening <command:parameter> tag determine how the parameter appears in
the syntax diagram. For information on parameter attributes, see Parameter Attributes.

  ７ Note

  The <command:parameter> tag supports a child element <maml:description> whose content is
  never displayed. The parameter descriptions are specified in the parameter node of the XML.
  To avoid inconsistencies between the information in the syntax item nodes and the
  parameter nodes, omit the <maml:description> or leave it empty.

The following example includes a syntax item node for a parameter set with two parameters.

 XML

 <command:syntaxItem>
   <maml:name>Cmdlet-Name</maml:name>
   <command:parameter required="true" globbing="true"
     pipelineInput="true (ByValue)" position="1">
     <maml:name>ParameterName1</maml:name>
     <command:parameterValue required="true">
       string[]
     </command:parameterValue>
   </command:parameter>

<!-- p.2859 -->

   <command:parameter required="true" globbing="true"
     pipelineInput="true (ByPropertyName)">
     <maml:name>ParameterName2</maml:name>
     <command:parameterValue required="true">
       int32[]
     </command:parameterValue>
   </command:parameter>
 </command:syntaxItem>

Last updated on 07/07/2026

<!-- p.2860 -->

How to add parameter information

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section describes how to add content that's displayed in the PARAMETERS section of the
cmdlet Help topic. The PARAMETERS section of the Help topic lists each of the parameters of
the cmdlet and provides a detailed description of each parameter.

The content of the PARAMETERS section should be consistent with the content of the SYNTAX
section of the Help topic. It's the responsibility of the Help author to make sure that both the
Syntax and Parameters node contain similar XML elements.

  ７ Note

  For a complete view of a Help file, open one of the dll-Help.xml files located in the
  PowerShell installation directory. For example, the
  Microsoft.PowerShell.Commands.Management.dll-Help.xml file contains content for several

  of the PowerShell cmdlets.

To add parameters
   1. Open the cmdlet Help file and locate the Command node for the cmdlet you are
     documenting. If you are adding a new cmdlet you will need to create a new Command
     node. Your Help file will contain a Command node for each cmdlet that you are providing
     Help content for. Here is an example of a blank Command node.

       XML

       <command:command>
       </command:command>

<!-- p.2861 -->

2. Within the Command node, locate the Description node and add a Parameters node as
  shown below. Only one Parameters node is allowed, and it should immediately follow the
  Syntax node.

    XML

    <command:command>
      <command:details></command:details>
      <maml:description></maml:description>
      <command:syntax></command:syntax>
      <command:parameters>
      </command:parameters>
    </command:command>

3. Within the Parameters node, add a Parameter node for each parameter of the cmdlet as
  shown below.

  In this example, a Parameter node is added for three parameters.

    XML

    <command:parameters>
      <command:parameter></command:parameter>
      <command:parameter></command:parameter>
      <command:parameter></command:parameter>
    </command:parameters>

  Because these are the same XML tags that are used in the Syntax node, and because the
  parameters specified here must match the parameters specified by the Syntax node, you
  can copy the Parameter nodes from the Syntax node and paste them into the Parameters
  node. However, be sure to copy only one instance of a Parameter node, even if the
  parameter is specified in multiple parameter sets in the syntax.

4. For each Parameter node, set the attribute values that define the characteristics of each
  parameter. These attributes include the following: required, globbing, pipelineinput, and
  position.

    XML

    <command:parameters>
      <command:parameter required="true" globbing="true"
               pipelineInput="false" position="named">
      </command:parameter>
      <command:parameter required="false" globbing="false"
               pipelineInput="false" position="named">
      </command:parameter>

<!-- p.2862 -->

      <command:parameter required="false" globbing="false"
               pipelineInput="false" position="named" ></command:parameter>
    </command:parameters>

5. For each Parameter node, add the name of the parameter. Here is an example of the
  parameter name added to the Parameter node.

    XML

    <command:parameters>
      <command:parameter required="true" globbing="true"
               pipelineInput="false" position="named">
        <maml:name> Add parameter name... </maml:name>
      </command:parameter>
    </command:parameters>

6. For each Parameter node, add the description of the parameter. Here is an example of
  the parameter description added to the Parameter node.

    XML

    <command:parameters>
      <command:parameter required="true" globbing="true"
               pipelineInput="false" position="named">
        <maml:name> Add parameter name... </maml:name>
        <maml:description>
          <maml:para> Add parameter description... </maml:para>
        </maml:description>
      </command:parameter>
    </command:parameters>

7. For each Parameter node, add the .NET type of the parameter. The parameter type is
  displayed along with the parameter name.

  Here is an example of the parameter .NET type added to the Parameter node.

    XML

    <command:parameters>
      <command:parameter required="true" globbing="true"
               pipelineInput="false" position="named">
        <maml:name> Add parameter name... </maml:name>
        <maml:description>
          <maml:para> Add parameter description... </maml:para>
        </maml:description>
        <dev:type> Add .NET Framework type... </dev:type>
      </command:parameter>
    </command:parameters>

<!-- p.2863 -->

  8. For each Parameter node, add the default value of the parameter. The following sentence
    is added to the parameter description when the content is displayed: DefaultValue is the
    default.

    Here is an example of the parameter default value is added to the Parameter node.

      XML

      <command:parameters>
        <command:parameter required="true" globbing="true"
                 pipelineInput="false" position="named">
          <maml:name> Add parameter name... </maml:name>
          <maml:description>
            <maml:para> Add parameter description... </maml:para>
          </maml:description>
          <dev:type> Add .NET Framework type... </dev:type>
          <dev:defaultvalue> Add default value...</dev:defaultvalue>
        </command:parameter>
      </command:parameters>

  9. For each Parameter that has multiple values, add a possibleValues node.

    Here is an example of the of a possibleValues node that defines two possible values for
    the parameter

      XML

      <dev:possibleValues>
        <dev:possibleValue>
          <dev:value>Unknown</dev:value>
          <maml:description>
            <maml:para></maml:para>
          </maml:description>
        </dev:possibleValue>
        <dev:possibleValue>
          <dev:value>String</dev:value>
          <maml:description>
            <maml:para></maml:para>
          </maml:description>
        </dev:possibleValue>
      </dev:possibleValues>

Here are some things to remember when adding parameters.

    The attributes of the parameter aren't displayed in all views of the cmdlet Help topic.
    However, they're displayed in a table following the parameter description when the user

<!-- p.2864 -->

     asks for the Full ( Get-Help <cmdletname> -Full ) or Parameter ( Get-Help <cmdletname> -
     Parameter ) view of the topic.

     The parameter description is one of the most important parts of a cmdlet Help topic. The
     description should be brief, as well as thorough. Also, remember that if the parameter
     description becomes too long, such as when two parameters interact with each other, you
     can add more content in the NOTES section of the cmdlet Help topic.

     The parameter description provides two types of information.

     What the cmdlet does when the parameter is used.

     What a legal value is for the parameter.

     Because the parameter values are expressed as .NET objects, users need more
     information about these values than they would in a traditional command-line Help. Tell
     the user what type of data the parameter is designed to accept, and include examples.

The default value of the parameter is the value that's used if the parameter isn't specified on
the command line. Note that the default value is optional, and isn't needed for some
parameters, such as required parameters. However, you should specify a default value for most
optional parameters.

The default value helps the user to understand the effect of not using the parameter. Describe
the default value very specifically, such as the "Current directory" or the "PowerShell installation
directory ( $PSHOME )" for an optional path. You can also write a sentence that describes the
default, such as the following sentence used for the PassThru parameter: "If PassThru isn't
specified, the cmdlet doesn't pass objects down the pipeline." Also, because the value is
displayed opposite the field name Default value, you don't need to include the term "default
value" in the entry.

The default value of the parameter isn't displayed in all views of the cmdlet Help topic.
However, it's displayed in a table (along with the parameter attributes) following the parameter
description when the user asks for the Full ( Get-Help <cmdletname> -Full ) or Parameter ( Get-
Help <cmdletname> -Parameter ) view of the topic.

The following XML shows a pair of <dev:defaultValue> tags added to the <command:parameter>
node. Notice that the default value follows immediately after the closing
</command:parameterValue> tag (when the parameter value is specified) or the closing

</maml:description> tag of the parameter description. name.

<!-- p.2865 -->

  XML

  <command:parameters>
    <command:parameter required="true" globbing="true"
             pipelineInput="false" position="named">
      <maml:name> Parameter name </maml:name>
      <maml:description>
        <maml:para> Parameter Description </maml:para>
      </maml:description>
      <command:parameterValue required="true">
        Value
      </command:parameterValue>
      <dev:defaultValue> Default parameter value </dev:defaultValue>
    </command:parameter>
  </command:parameters>

Add Values for Enumerated Types

If the parameter has multiple values or values of an enumerated type, you can use an optional
<dev:possibleValues> node. This node allows you to specify a name and description for

multiple values.

Be aware that the descriptions of the enumerated values don't appear in any of the default
Help views displayed by the Get-Help cmdlet, but other Help viewers may display this content
in their views.

The following XML shows a <dev:possibleValues> node with two values specified.

  XML

  <command:parameters>
    <command:parameter required="true" globbing="true"
             pipelineInput="false" position="named">
      <maml:name> Parameter name </maml:name>
      <maml:description>
        <maml:para> Parameter Description </maml:para>
      </maml:description>
      <command:parameterValue required="true">
        Value
      </command:parameterValue>
      <dev:defaultValue> Default parameter value </dev:defaultValue>
      <dev:possibleValues>
        <dev:possibleValue>
          <dev:value> Value 1 </dev:value>
          <maml:description>
            <maml:para> Description 1 </maml:para>
          </maml:description>
        <dev:possibleValue>
        <dev:possibleValue>
          <dev:value> Value 2 </dev:value>

<!-- p.2866 -->

         <maml:description>
           <maml:para> Description 2 </maml:para>
         </maml:description>
       <dev:possibleValue>
     </dev:possibleValues>
   </command:parameter>
 </command:parameters>

Last updated on 05/20/2025

<!-- p.2867 -->

How to add input types to a cmdlet help
topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section describes how to add an INPUTS section to a PowerShell cmdlet Help topic. The
INPUTS section lists the .NET classes of objects that the cmdlet accepts as input from the
pipeline, either by value or by property name.

There is no limit to the number of classes that you can add to an INPUTS section. The input
types are enclosed in a <command:inputTypes> node, with each class enclosed in a
<command:inputType> element.

The schema includes two <maml:description> elements in each <command:inputType> element.
However, the Get-Help cmdlet displays only the content of the
<command:inputType>/<maml:description> element.

Beginning in PowerShell 3.0, the Get-Help cmdlet displays the content of the <maml:uri>
element. This element lets you direct users to topics that describe the .NET class.

The following XML shows the <maml:inputTypes> node.

 XML

 <command:inputTypes>
   <command:inputType>
     <dev:type>
       <maml:name> Class name </maml:name>
       <maml:uri> URI of a topic that describes the class </maml:uri>
       <maml:description/>
     </dev:type>
     <maml:description>
       <maml:para> Brief description </maml:para>
     </maml:description>

<!-- p.2868 -->

    </command:inputType>
  </command:inputTypes>

The following XML shows an example of using the <maml:inputTypes> node to document an
input type.

  XML

  <command:inputTypes>
    <command:inputType>
      <dev:type>
        <maml:name>System.DateTime</maml:name>
        <maml:uri>https://learn.microsoft.com/dotnet/api/system.datetime</maml:uri>
        <maml:description/>
      </dev:type>
      <maml:description>
        <maml:para> You can pipe a date to the Set-Date cmdlet. <maml:para>
      <maml:description>
    </command:inputType>
  </command:inputTypes>

 Last updated on 05/20/2025

<!-- p.2869 -->

How to add return values to a cmdlet help
topic
This section describes how to add an OUTPUTS section to a PowerShell cmdlet Help topic. The
OUTPUTS section lists the .NET classes of objects that the cmdlet returns or passes down the
pipeline.

There is no limit to the number of classes that you can add to the OUTPUTS section. The return
types of a cmdlet are enclosed in a <command:returnValues> node, with each class enclosed in a
<command:returnValue> element.

If a cmdlet doesn't generate any output, use this section to indicate that there is no output. For
example, in place of the class name, write None and provide a brief explanation. If the cmdlet
generates output conditionally, use this node to explain the conditions and describe the
conditional output.

The schema includes two <maml:description> elements in each <command:returnValue>
element. However, the Get-Help cmdlet displays only the content of the
<command:returnValue>/<maml:description> element.

Beginning in PowerShell 3.0, the Get-Help cmdlet displays the content of the <maml:uri>
element. This element lets you direct users to topics that describe the .NET class.

The following XML shows the <maml:returnValues> node.

 XML

 <command:returnValues>
   <command:returnValue>
     <dev:type>
       <maml:name> Class Name </maml:name>
       <maml:uri> URI of a topic that describes the class </maml:uri>
       <maml:description/>
     </dev:type>
     <maml:description>
        <maml:para> Brief description <maml:para>

 </maml:description>
   </command: returnValue>
 </command: returnValues>

<!-- p.2870 -->

The following XML shows an example of using the <maml:returnValues> node to document an
output type.

 XML

 <command:returnValues>
   <command:returnValue>
     <dev:type>
       <maml:name> System.DateTime </maml:name>
       <maml:uri> https://learn.microsoft.com/dotnet/api/system.datetime
 </maml:uri>
       <maml:description/>
     </dev:type>
     <maml:description>
       <maml:para> Get-Date returns a DateTime object. <maml:para>
     </maml:description>
   </command: returnValue>
 </command: returnValues>

Last updated on 05/20/2025

<!-- p.2871 -->

How to add notes to a cmdlet help topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section describes how to add a NOTES section to a PowerShell cmdlet Help topic. The
NOTES section is used to explain details that don't fit easily into the other structured sections,
such as a more detailed explanation of a parameter. This content could include comments on
how the cmdlet works with a specific provider, some unique, yet important, uses of the cmdlet,
or ways to avoid possible error conditions.

The NOTES section is defined using a single <maml:alertset> node. There are no limits to the
number of notes that you can add to a Notes section. For each note, add a pair of
<maml:alert> tags to the <maml:alertset> node. The content of each note is added within a

set of <maml:para> tags. Use blank <maml:para> tags for spacing.

  XML

  <maml:alertSet>
    <maml:title>Optional title for Note</maml:title>
    <maml:alert>
      <maml:para>Note 1</maml:para>
      <maml:para>Note a</maml:para>
    </maml:alert>
    <maml:alert>
      <maml:para>Note 2</maml:para>
    </maml:alert>
  </maml:alertSet>

 Last updated on 05/20/2025

<!-- p.2872 -->

How to add examples to a cmdlet help
topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

Things to know about examples in cmdlet help
     List all of the parameter names in the command, even when the parameter names are
     optional. This helps the user to interpret the command easily.

     Avoid aliases and partial parameter names, even though they work in PowerShell.

     In the example description, explain the rational for the construction of the command.
     Explain why you chose particular parameters and values, and how you use variables.

     If the command uses expressions, explain them in detail.

     If the command uses properties and methods of objects, especially properties that don't
     appear in the default display, use the example as an opportunity tell the user about the
     object.

Help Views that Display Examples
Examples appear only in the Detailed and Full views of cmdlet Help.

Adding an examples node
The following XML shows how to add an Examples node that contains a single Example node.
Add additional example nodes for each examples you want to include in the topic.

 XML

<!-- p.2873 -->

 <command:examples>
   <command:example>
   </command:example>
 </command:examples>

Adding an example title
The following XML shows how to add a title for the example. The title is used to set the
example apart from other examples. PowerShell uses a standard header that includes a
sequential example number.

 XML

 <command:examples>
   <command:example>
     <maml:title>----------     EXAMPLE 1   ----------</maml:title>
   </command:example>
 </command:examples>

Adding preceding characters
The following XML shows how to add characters, such as the Windows PowerShell prompt, that
are displayed immediately before the example command (without any intervening spaces).
PowerShell uses the Windows PowerShell prompt: C:\PS> .

 XML

 <command:examples>
   <command:example>
     <maml:title>---------- EXAMPLE 1       ----------</maml:title>
     <maml:introduction>
       <maml:para>C:\PS></maml:para>
     </maml:introduction>
 </command:example>
 </command:examples>

Adding the command
The following XML shows how to add the actual command of the example. When adding the
command, type the entire name (do not use alias) of cmdlets and parameters. Also, use
lowercase characters whenever possible.

 XML

<!-- p.2874 -->

 <command:examples>
   <command:example>
     <maml:title>---------- EXAMPLE 1        ----------</maml:title>
     <maml:introduction>
       <maml:para>C:\PS></maml:para>
     </maml:introduction>
     <dev:code> command </dev:code>
 </command:example>
 </command:examples>

Adding a Description
The following XML shows how to add a description for the example. PowerShell uses a single
set of <maml:para> tags for the description, even though multiple <maml:para> tags can be
used.

 XML

 <command:examples>
   <command:example>
     <maml:title>---------- EXAMPLE 1 ----------</maml:title>
     <maml:introduction>
       <maml:para>C:\PS></maml:para>
     </maml:introduction>
     <dev:code> command </dev:code>
     <dev:remarks>
       <maml:para> command description </maml:para>
     </dev:remarks>
 </command:example>
 </command:examples>

Adding example output
The following XML shows how to add the output of the command. The command results
information is optional, but in some cases it's helpful to demonstrate the effect of using
specific parameters. PowerShell uses two sets of blank <maml:para> tags to separate the
command output from the command.

 XML

 <command:examples>
   <command:example>
     <maml:title>---------- EXAMPLE 1        ----------</maml:title>
     <maml:introduction>
       <maml:para>C:\PS></maml:para>
     </maml:introduction>

<!-- p.2875 -->

     <dev:code> command </dev:code>
     <dev:remarks>
       <maml:para> command description </maml:para>
       <maml:para></maml:para>
       <maml:para></maml:para>
       <maml:para> command output </maml:para>
 </dev:remarks>
 </command:example>
 </command:examples>

Last updated on 05/20/2025

<!-- p.2876 -->

How to add related links to a cmdlet help
topic

  ７ Note

  Manual authoring of XML-based help is very difficult. The PlatyPS module allows you to
  write help in Markdown and then convert it to XML-based help. This makes it much easier
  to write and maintain help. PlatyPS can also create the Updateable Help packages for you.
  For more information, see Create XML-based help using PlatyPS.

This section describes how to add references to other content that's related to a PowerShell
cmdlet Help topic. Because these references appear in a command window, they don't link
directly to the referenced content.

In the cmdlet Help topics that are included in PowerShell, these links reference other cmdlets,
conceptual content ( about_ ), and other documents and Help files that aren't related to
PowerShell.

The following XML shows how to add a RelatedLinks node that contains two references to
related topics.

  XML

  <maml:relatedLinks>
    <maml:navigationLink>
      <maml:linkText>Topic-name</maml:linkText>
    </maml:navigationLink>
    <maml:navigationLink>
      <maml:linkText>Topic-name</maml:linkText>
    </maml:navigationLink>
  </ maml:relatedLinks >

 Last updated on 05/20/2025

<!-- p.2877 -->

Writing Help for PowerShell Modules
09/23/2025

PowerShell modules can include Help topics about the module and about the module
members, such as cmdlets, providers, functions and scripts. The Get-Help cmdlet displays the
module Help topics in the same format as it displays Help for other PowerShell items, and
users use standard Get-Help commands to get the Help topics.

This document explains the format and correct placement of module Help topics, and it
suggests guidelines for module Help content.

Types of Module Help
A module can include the following types of Help.

     XML-based help
        Cmdlet Help. The Help topics that describe cmdlets in a module are XML files that use
        the command help schema
        Provider Help. The Help topics that describe providers in a module are XML files that
        use the provider help schema.
        Function Help. The Help topics that describe functions in a module can be XML files
        that use the command help schema or comment-based Help topics within the
        function, or the script or script module
        Script Help. The Help topics that describe scripts in a module can be XML files that use
        the command help schema or comment-based Help topics in the script or script
        module.
        The $PSHOME\Schemas\PSMaml folder contains the schema files that define the XML
        format.

     Conceptual ("About") help text files

     You can use a conceptual ("about") Help topic to describe the module and its members
     and to explain how the members can be used together to perform tasks. By default,
     PowerShell includes over 100 of these conceptual About Help topics.

        Conceptual Help topics are text files with UTF-8 with BOM encoding.

        The filename must use the about_<name>.help.txt format, such as
        about_MyModule.help.txt .

        For best display results, you should limit the length of each line to 80 characters.

<!-- p.2878 -->

        You can use the following sample template as a starting point for writing conceptual
        Help topics.

          ７ Note

          The TOPIC section header must start in the first column of the first line of the file.
          The section content on the second line should match the filename, without the
          .help.txt suffix. You must indent the content exactly 5 spaces. The third line must

          be blank. The SHORT DESCRIPTION section header must start in the first column of
          the fourth line. You must indent the content on the fifth line exactly 5 spaces.
          These requirements are necessary for the Get-Help cmdlet to recognize the
          content correctly.

          TOPIC
              about_<subject or module name>

          SHORT DESCRIPTION
              A short, one-line description of the topic contents.

          LONG DESCRIPTION
              A detailed, full description of the subject or purpose of the module.

          EXAMPLES
              Examples of how to use the module or how the subject feature works in
              practice.

          KEYWORDS
              Terms or titles on which you might expect your users to search for the
              information in this topic.

          SEE ALSO
              Text-only references for further reading. Hyperlinks can't work in the
              PowerShell console.

        Except for the first two sections, the structure of conceptual Help topics is arbitrary.
        The remaining section titles can be whatever is appropriate for your content. By
        convention, you should use the same capitalization, indentation, and blank line
        separations.

Placement of Module Help
The Get-Help cmdlet looks for module Help topic files in language-specific subdirectories of
the module directory.

<!-- p.2879 -->

For example, the following directory structure diagram shows the location of the Help topics
for the SampleModule module.

  <ModulePath>
      \SampleModule
          \<en-US>
               \about_SampleModule.help.txt
               \SampleModule.dll-help.xml
               \SampleNestedModule.dll-help.xml
          \<fr-FR>
               \about_SampleModule.help.txt
               \SampleModule.dll-help.xml
               \SampleNestedModule.dll-help.xml

  ７ Note

  In the example, the <ModulePath> placeholder represents one of the paths in the
  PSModulePath environment variable, such as $HOME\Documents\Modules , $PSHOME\Modules ,

  or a custom path that the user specifies.

Getting Module Help
When a user imports a module into a session, the Help topics for that module are imported
into the session along with the module. You can list the Help topic files in the value of the
FileList key in the module manifest, but Help topics aren't affected by the Export-ModuleMember
cmdlet.

You can provide module Help topics in different languages. The Get-Help cmdlet automatically
displays module Help topics in the language that's specified for the current user in the
Regional and Language Options item in Control Panel. In Windows Vista and later versions of
Windows, Get-Help searches for the Help topics in language-specific subdirectories of the
module directory in accordance with the language fallback standards established for Windows.

Beginning in PowerShell 3.0, running a Get-Help command for a cmdlet or function triggers
automatic importing of the module. The Get-Help cmdlet immediately displays the contents of
the help topics in the module.

If the module doesn't contain help topics and there are no help topics for the commands in the
module on the user's computer, Get-Help displays auto-generated help. The auto-generated
help includes the command syntax, parameters, and input and output types, but doesn't

<!-- p.2880 -->

include any descriptions. The auto-generated help includes text that directs the user to try to
use the Update-Help cmdlet to download help for the command from the internet or a file
share. It also recommends using the Online parameter of the Get-Help cmdlet to get the
online version of the help topic.

Supporting Updatable Help
Users of PowerShell 3.0 and later versions of PowerShell can download and install updated help
files for a module from the internet or from a local file share. The Update-Help and Save-Help
cmdlets hide the management details from the user. Users run the Update-Help cmdlet and
then use the Get-Help cmdlet to read the newest help files for the module at the PowerShell
command prompt. Users don't need to restart Windows or PowerShell.

Users behind firewalls and those without internet access can use Updatable Help, as well.
Administrators with internet access use the Save-Help cmdlet to download and install the
newest help files to a file share. Then, users use the Path parameter of the Update-Help cmdlet
to get the newest help files from the file share.

Module authors can include help files in the module and use Updatable Help to update the
help files, or omit help files from the module and use Updatable Help both to install and to
update them.

For more information about Updatable Help, see Supporting Updatable Help.

Supporting Online Help
Users who can't or don't install updated help files on their computers often rely on the online
version of module help topics. The Online parameter of the Get-Help cmdlet opens the online
version of a cmdlet or advanced function help topic for the user in their default internet
browser.

The Get-Help cmdlet uses the value of the HelpUri property of the cmdlet or function to find
the online version of the help topic.

Beginning in PowerShell 3.0, you can help users find the online version of cmdlet and function
help topics by defining the HelpUri attribute on the cmdlet class or the HelpUri property of the
CmdletBinding attribute. The value of the attribute is the value of the HelpUri property of the
cmdlet or function.

For more information, see Supporting Online Help.
