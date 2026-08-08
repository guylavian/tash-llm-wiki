---
title: "How to use this documentation — pages 1361-1400"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1361-1400
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1361-1400
family: powershell
documentKind: "doc"
abstract: "Syntax attribute-list: attribute attribute-list new-lines~opt~ attribute attribute: [ new-lines~opt~ attribute-name ( attribute-arguments new-lines~opt~ ) new-lines~opt~ ] type-literal attribute-name: type-spec attribute-arguments: attribute-argument attribute-argument new-lines"
---

# How to use this documentation — pages 1361-1400

<!-- p.1361 -->

  Syntax

  attribute-list:
      attribute
      attribute-list new-lines~opt~ attribute

  attribute:
      [ new-lines~opt~ attribute-name ( attribute-arguments new-lines~opt~ )
  new-lines~opt~ ]
      type-literal

  attribute-name:
      type-spec

  attribute-arguments:
      attribute-argument
      attribute-argument new-lines~opt~ ,
      attribute-arguments

  attribute-argument:
      new-lines~opt~ expression
      new-lines~opt~ simple-name
      new-lines~opt~ simple-name = new-lines~opt~ expression

An attribute consists of an attribute-name and an optional list of positional and named
arguments. The positional arguments (if any) precede the named arguments. A named
argument consists of a simple-name, optionally followed by an equal sign and followed
by an expression. If the expression is omitted, the value $true is assumed.

The attribute-name is a reserved attribute type (§12.3) or some implementation-defined
attribute type.

12.2 Attribute instances
An attribute instance is an object of an attribute type. The instance represents an
attribute at run-time.

To create an object of some attribute type A, use the notation A() . An attribute is
declared by enclosing its instance inside [] , as in [A()] . Some attribute types have
positional and named parameters (§8.14), just like functions and cmdlets. For example,

[A(10,IgnoreCase=$true)]

shows an instance of type A being created using a positional parameter whose
argument value is 10, and a named parameter, IgnoreCase, whose argument value is
$true .

<!-- p.1362 -->

12.3 Reserved attributes
The attributes described in the following sections can be used to augment or modify the
behavior of PowerShell functions, filters, scripts, and cmdlets.

12.3.1 The Alias attribute
This attribute is used in a script-parameter to specify an alternate name for a parameter.
A parameter may have multiple aliases, and each alias name must be unique within a
parameter-list. One possible use is to have different names for a parameter in different
parameter sets (see ParameterSetName).

The attribute argument has type string[].

Consider a function call Test1 that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [Alias("CN")]
      [Alias("Name", "System")]
      [string[]] $ComputerName
  )

  Test1 "Mars", "Saturn"                      # pass argument by position
  Test1 -ComputerName "Mars", "Saturn"        # pass argument by name
  Test1 -CN "Mars", "Saturn"                  # pass argument using first alias
  Test1 -Name "Mars", "Saturn"                # pass argument using second alias
  Test1 -Sys "Mars", "Saturn"                 # pass argument using third alias

Consider a function call Test2 that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true, ValueFromPipelineByPropertyName = $true)]
      [Alias('PSPath')]
      [string] $LiteralPath
  )

  Get-ChildItem "E:\*.txt" | Test2 -LiteralPath { $_ ; "`n`t";
      $_.FullName + ".bak" }
  Get-ChildItem "E:\*.txt" | Test2

<!-- p.1363 -->

Cmdlet Get-ChildItem (alias dir ) adds to the object it returns a new NoteProperty of
type string , called PSPath.

12.3.2 The AllowEmptyCollection attribute
This attribute is used in a script-parameter to allow an empty collection as the argument
of a mandatory parameter.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [AllowEmptyCollection()]
      [string[]] $ComputerName
  )

  Test "Red", "Green" # $ComputerName has Length 2
  Test "Red" # $ComputerName has Length 1
  Test -Comp @() # $ComputerName has Length 0

12.3.3 The AllowEmptyString attribute
This attribute is used in a script-parameter to allow an empty string as the argument of a
mandatory parameter.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [AllowEmptyString()]
      [string] $ComputerName
  )

  Test "Red" # $ComputerName is "Red"
  Test "" # empty string is permitted
  Test -Comp "" # empty string is permitted

12.3.4 The AllowNull attribute

<!-- p.1364 -->

This attribute is used in a script-parameter to allow $null as the argument of a
mandatory parameter for which no implicit conversion is available.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [AllowNull()]
      [int[]] $Values
  )

  Test 10, 20, 30        # $values has Length 3, values 10, 20, 30
  Test 10, $null, 30     # $values has Length 3, values 10, 0, 30
  Test -Val $null        # $values has value $null

Note that the second case above does not need this attribute; there is already an
implicit conversion from $null to int.

12.3.5 The CmdletBinding attribute
This attribute is used in the attribute-list of param-block of a function to indicate that
function acts similar to a cmdlet. Specifically, it allows functions to access a number of
methods and properties through the $PSCmdlet variable by using begin, process, and
end named blocks (§8.10.7).

When this attribute is present, positional arguments that have no matching positional
parameters cause parameter binding to fail and $args is not defined. (Without this
attribute $args would take on any unmatched positional argument values.)

The following arguments are used to define the characteristics of the parameter:

                                                                               ﾉ   Expand table

 Parameter Name              Purpose

 SupportsShouldProcess       Type: bool; Default value: $false
 (named)
                             Specifies whether the function supports calls to the ShouldProcess
                             method, which is used to prompt the user for feedback before the
                             function makes a change to the system. A value of $true indicates
                             that it does. A value of $false indicates that it doesn't.

 ConfirmImpact (named)       Type: string; Default value: "Medium"

<!-- p.1365 -->

 Parameter Name              Purpose

                             Specifies the impact level of the action performed. The call to the
                             ShouldProcess method displays a confirmation prompt only when
                             the ConfirmImpact argument is greater than or equal to the value
                             of the $ConfirmPreference preference variable.

                             The possible values of this argument are:

                             None: Suppress all requests for confirmation.

                             Low: The action performed has a low risk of losing data.

                             Medium: The action performed has a medium risk of losing data.

                             High: The action performed has a high risk of losing data.

                             The value of $ConfirmPreference can be set so that only cmdlets
                             with an equal or higher impact level can request confirmation
                             before they perform their operation. For example, if
                             $ConfirmPreference is set to Medium, cmdlets with a Medium or
                             High impact level can request confirmation. Requests from cmdlets
                             with a low impact level are suppressed.

 DefaultParameterSetName     Type: string; Default value: "__AllParameterSets"
 (named)
                             Specifies the parameter set to use if that cannot be determined
                             from the arguments. See the named argument ParameterSetName
                             in the attribute Parameter ([§12.3.7][§12.3.7]).

 PositionalBinding (named)   Type: bool; Default value: $true

                             Specifies whether positional binding is supported or not. The value
                             of this argument is ignored if any parameters specify non-default
                             values for either the named argument Position or the named
                             argument ParameterSetName in the attribute Parameter ([§12.3.7]
                             [§12.3.7]). Otherwise, if the argument is $false then no parameters
                             are positional, otherwise parameters are assigned a position based
                             on the order the parameters are specified.

Here's is an example of the framework for using this attribute:

  PowerShell

  [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = "Low")]
  param ( ... )

  begin { ... }
  Get-process { ... }
  end { ... }

<!-- p.1366 -->

12.3.6 The OutputType attribute
This attribute is used in the attribute-list of param-block to specify the types returned.
The following arguments are used to define the characteristics of the parameter:

                                                                                 ﾉ   Expand table

 Parameter Name           Purpose

 Type (position 0)        Type: string[] or array of type literals

                          A list of the types of the values that are returned.

 ParameterSetName         Type: string[]
 (named)
                          Specifies the parameter sets that return the types indicated by the
                          corresponding elements of the Type parameter.

Here are several examples of this attribute's use:

  PowerShell

  [OutputType([int])] param ( ... )
  [OutputType("double")] param ( ... )
  [OutputType("string","string")] param ( ... )

12.3.7 The Parameter attribute
This attribute is used in a script-parameter. The following named arguments are used to
define the characteristics of the parameter:

                                                                                 ﾉ   Expand table

 Parameter                            Purpose

 HelpMessage (named)                  Type: string

                                      This argument specifies a message that is intended to
                                      contain a short description of the parameter. This message
                                      is used in an implementation-defined manner when the
                                      function or cmdlet is run yet a mandatory parameter having
                                      a HelpMessage does not have a corresponding argument.

                                      The following example shows a parameter declaration that
                                      provides a description of the parameter.

<!-- p.1367 -->

Parameter                  Purpose

                           param ( [Parameter(Mandatory = $true,
                           HelpMessage = "An array of computer names.")]
                           [string[]] $ComputerName )

                           Windows PowerShell: If a required parameter is not
                           provided the runtime prompts the user for a parameter
                           value. The prompt dialog box includes the HelpMessage
                           text.

Mandatory (named)          Type: bool; Default value: $false

                           This argument specifies whether the parameter is required
                           within the given parameter set (see ParameterSetName
                           argument below). A value of $true indicates that it is. A
                           value of $false indicates that it isn't.

                           param ( [Parameter(Mandatory = $true)]
                           [string[]] $ComputerName )

                           Windows PowerShell: If a required parameter is not
                           provided the runtime prompts the user for a parameter
                           value. The prompt dialog box includes the HelpMessage
                           text, if any.

ParameterSetName (named)   Type: string; Default value: "__AllParameterSets"

                           It is possible to write a single function or cmdlet that can
                           perform different actions for different scenarios. It does this
                           by exposing different groups of parameters depending on
                           the action it wants to take. Such parameter groupings are
                           called parameter sets.

                           The argument ParameterSetName specifies the parameter
                           set to which a parameter belongs. This behavior means that
                           each parameter set must have one unique parameter that is
                           not a member of any other parameter set.

                           For parameters that belong to multiple parameter sets, add
                           a Parameter attribute for each parameter set. This allows
                           the parameter to be defined differently for each parameter
                           set.

                           A parameter set that contains multiple positional
                           parameters must define unique positions for each
                           parameter. No two positional parameters can specify the
                           same position.

                           If no parameter set is specified for a parameter, the
                           parameter belongs to all parameter sets.

<!-- p.1368 -->

Parameter          Purpose

                   When multiple parameter sets are defined, the named
                   argument DefaultParameterSetName of the attribute
                   CmdletBinding ([§12.3.5][§12.3.5]) is used to specify the
                   default parameter set. The runtime uses the default
                   parameter set if it cannot determine the parameter set to
                   use based on the information provided by the command, or
                   raises an exception if no default parameter set has been
                   specified.

                   The following example shows a function Test with a
                   parameter declaration of two parameters that belong to
                   two different parameter sets, and a third parameter that
                   belongs to both sets:

                   param ( [Parameter(Mandatory = $true,
                   ParameterSetName = "Computer")]
                   [string[]] $ComputerName,

                   [Parameter(Mandatory = $true,
                   ParameterSetName = "User")]
                   [string[]] $UserName,

                   [Parameter(Mandatory = $true,
                   ParameterSetName = "Computer")]
                   [Parameter(ParameterSetName = "User")]
                   [int] $SharedParam = 5 )

                   if ($PSCmdlet.ParameterSetName -eq "Computer")
                   {
                   # handle "Computer" parameter set
                   }

                   elseif ($PSCmdlet.ParameterSetName -eq "User")
                   {
                   # handle "User" parameter set
                   }
                   …
                   }

                   Test -ComputerName "Mars","Venus" -SharedParam 10
                   Test -UserName "Mary","Jack"
                   Test -UserName "Mary","Jack" -SharedParam 20

Position (named)   Type: int

                   This argument specifies the position of the parameter in the
                   argument list. If this argument is not specified, the
                   parameter name or its alias must be specified explicitly
                   when the parameter is set. If none of the parameters of a

<!-- p.1369 -->

Parameter                         Purpose

                                  function has positions, positions are assigned to each
                                  parameter based on the order in which they are received.

                                  The following example shows the declaration of a
                                  parameter whose value must be specified as the first
                                  argument when the function is called.

                                  param ( [Parameter(Position = 0)]
                                  [string[]] $ComputerName )

ValueFromPipeline (named)         Type: bool; Default value: $false

                                  This argument specifies whether the parameter accepts
                                  input from a pipeline object. A value of $true indicates that
                                  it does. A value of $false indicates that it does not.

                                  Specify $true if the function or cmdlet accesses the
                                  complete object, not just a property of the object.

                                  Only one parameter in a parameter set can declare
                                  ValueFromPipeline as $true.

                                  The following example shows the parameter declaration of
                                  a mandatory parameter, $ComputerName, that accepts the
                                  input object that is passed to the function from the
                                  pipeline.

                                  param ( [Parameter(Mandatory = $true,
                                  ValueFromPipeline=$true)]
                                  [string[]] $ComputerName )

                                  For an example of using this parameter in conjunction with
                                  the Alias attribute see [§12.3.1][§12.3.1].

ValueFromPipelineByPropertyName   Type: bool; Default value: $false
(named)
                                  This argument specifies whether the parameter takes its
                                  value from a property of a pipeline object that has either
                                  the same name or the same alias as this parameter. A value
                                  of $true indicates that it does. A value of $false indicates
                                  that it does not.

                                  Specify $true if the following conditions are true: the
                                  parameter accesses a property of the piped object, and the
                                  property has the same name as the parameter, or the
                                  property has the same alias as the parameter.

                                  A parameter having ValueFromPipelineByPropertyName set
                                  to $true need not have a parameter in the same set with
                                  ValueFromPipeline set to $true.

<!-- p.1370 -->

Parameter                     Purpose

                              If a function has a parameter $ComputerName, and the
                              piped object has a ComputerName property, the value of
                              the ComputerName property is assigned to the
                              $ComputerName parameter of the Function:

                              param ( [Parameter(Mandatory = $true,
                              ValueFromPipelineByPropertyName = $true)]
                              [string[]] $ComputerName )

                              Multiple parameters in a parameter set can define the
                              ValueFromPipelineByPropertyName as $true. Although, a
                              single input object cannot be bound to multiple
                              parameters, different properties in that input object may be
                              bound to different parameters.

                              When binding a parameter with a property of an input
                              object, the runtime environment first looks for a property
                              with the same name as the parameter. If such a property
                              does not exist, the runtime environment looks for aliases to
                              that parameter, in their declaration order, picking the first
                              such alias for which a property exists.

                              function Process-Date
                              {
                              param(
                              [Parameter(ValueFromPipelineByPropertyName=$true)]
                              [int]$Year,

                              [Parameter(ValueFromPipelineByPropertyName=$true)]
                              [int]$Month,

                              [Parameter(ValueFromPipelineByPropertyName=$true)]
                              [int]$Day
                              )

                              process { … }
                              }

                              Get-Date | Process-Date

ValueFromRemainingArguments   Type: bool; Default value: $false
(named)
                              This argument specifies whether the parameter accepts all
                              of the remaining arguments that are not bound to the
                              parameters of the function. A value of $true indicates that it
                              does. A value of $false indicates that it does not.

                              The following example shows a parameter $Others that
                              accepts all the remaining arguments of the input object
                              that is passed to the function Test:

<!-- p.1371 -->

 Parameter                           Purpose

                                     param ( [Parameter(Mandatory = $true)][int] $p1,
                                     [Parameter(Mandatory = $true)][int] $p2,
                                     [Parameter(ValueFromRemainingArguments = $true)]
                                     [string[]] $Others )

                                     Test 10 20 # $Others has Length 0
                                     Test 10 20 30 40 # $Others has Length 2, value 30,40

An implementation may define other attributes as well.

The following attributes are provided as well:

     HelpMessageBaseName: Specifies the location where resource identifiers reside.
     For example, this parameter could specify a resource assembly that contains Help
     messages that are to be localized.
     HelpMessageResourceId: Specifies the resource identifier for a Help message.

12.3.8 The PSDefaultValue attribute
This attribute is used in a script-parameter to provide additional information about the
parameter. The attribute is used in an implementation defined manner. The following
arguments are used to define the characteristics of the parameter:

                                                                                 ﾉ   Expand table

 Parameter    Purpose
 Name

 Help         Type: string
 (named)
              This argument specifies a message that is intended to contain a short description
              of the default value of a parameter. This message is used in an implementation-
              defined manner.

              Windows PowerShell: The message is used as part of the description of the
              parameter for the help topic displayed by the [Get-Help]
              (xref:Microsoft.PowerShell.Core.Get-Help) cmdlet.

 Value        Type: object
 (named)
              This argument specifies a value that is intended to be the default value of a
              parameter. The value is used in an implementation-defined manner.

              Windows PowerShell: The value is used as part of the description of the parameter
              for the help topic displayed by the [Get-Help](xref:Microsoft.PowerShell.Core.Get-
              Help)cmdlet when the Help property is not specified.

<!-- p.1372 -->

12.3.9 The SupportsWildcards attribute
This attribute is used in a script-parameter to provide additional information about the
parameter. The attribute is used in an implementation defined manner.

This attribute is used as part of the description of the parameter for the help topic
displayed by the Get-Help cmdlet.

12.3.10 The ValidateCount attribute
This attribute is used in a script-parameter to specify the minimum and maximum
number of argument values that the parameter can accept. The following arguments are
used to define the characteristics of the parameter:

                                                                           ﾉ   Expand table

 Parameter Name         Purpose

 MinLength              Type: int
 (position 0)
                        This argument specifies the minimum number of argument values
                        allowed.

 MaxLength              Type: int
 (position 1)
                        This argument specifies the maximum number of argument values
                        allowed.

In the absence of this attribute, the parameter's corresponding argument value list can
be of any length.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [ValidateCount(2, 5)]
      [int[]] $Values
  )

  Temp 10, 20, 30
  Temp 10                             # too few argument values
  Temp 10, 20, 30, 40, 50, 60         # too many argument values

  [ValidateCount(3, 4)]$Array = 1..3

<!-- p.1373 -->

  $Array = 10                          # too few argument values
  $Array = 1..100                      # too many argument values

12.3.11 The ValidateLength attribute
This attribute is used in a script-parameter or variable to specify the minimum and
maximum length of the parameter's argument, which must have type string. The
following arguments are used to define the characteristics of the parameter:

                                                                             ﾉ   Expand table

 Parameter Name           Purpose

 MinLength (position 0)   Type: int

                          This argument specifies the minimum number of characters allowed.

 MaxLength (position 1)   Type: int

                          This argument specifies the maximum number of characters allowed.

In the absence of this attribute, the parameter's corresponding argument can be of any
length.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param ( [Parameter(Mandatory = $true)]
  [ValidateLength(3,6)]
  [string[]] $ComputerName )

  Test "Thor","Mars"         # length is ok
  Test "Io","Mars"           # "Io" is too short
  Test "Thor","Jupiter"      # "Jupiter" is too long

12.3.12 The ValidateNotNull attribute
This attribute is used in a script-parameter or variable to specify that the argument of
the parameter cannot be $null or be a collection containing a null-valued element.

Consider a function call Test that has the following param block, and which is called as
`shown:

<!-- p.1374 -->

  PowerShell

  param (
      [ValidateNotNull()]
      [string[]] $Names
  )

  Test "Jack", "Jill"         # ok
  Test "Jane", $null          # $null array element value not allowed
  Test $null                  # null array not allowed

  [ValidateNotNull()]$Name = "Jack" # ok
  $Name = $null           # null value not allowed

12.3.13 The ValidateNotNullOrEmpty attribute
This attribute is used in a script-parameter or variable to specify that the argument if the
parameter cannot be $null, an empty string, or an empty array, or be a collection
containing a $null-valued or empty string element.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [ValidateNotNullOrEmpty()]
      [string[]] $Names
  )

  Test "Jack", "Jill"        # ok
  Test "Mary", ""            # empty string not allowed
  Test "Jane", $null         # $null array element value not allowed
  Test $null                 # null array not allowed
  Test @()                   # empty array not allowed

  [ValidateNotNullOrEmpty()]$Name = "Jack" # ok
  $Name = ""             # empty string not allowed
  $Name = $null          # null value not allowed

12.3.14 The ValidatePattern attribute
This attribute is used in a script-parameter or variable to specify a regular expression for
matching the pattern of the parameter's argument. The following arguments are used to
define the characteristics of the parameter:

<!-- p.1375 -->

                                                                                 ﾉ   Expand table

 Parameter Name             Purpose

 RegexString (position 0)   Type: String

                            A regular expression that is used to validate the parameter's argument

 Options (named)            Type: Regular-Expression-Option

                            See [§4.2.6.4][§4.2.6.4] for the allowed values.

If the argument is a collection, each element in the collection must match the pattern.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [ValidatePattern('\^[A-Z][1-5][0-9]$')]
      [string] $Code,

       [ValidatePattern('\^(0x|0X)([A-F]|[a-f]|[0-9])([A-F]|[a-f]|[0-9])$')]
       [string] $HexNum,

       [ValidatePattern('\^[+|-]?[1-9]$')]
       [int] $Minimum
  )

  Test -C A12 # matches pattern
  Test -C A63 # does not match pattern

  Test -H 0x4f # matches pattern
  Test -H "0XB2" # matches pattern
  Test -H 0xK3 # does not match pattern

  Test -M -4 # matches pattern
  Test -M "+7" # matches pattern
  Test -M -12 # matches pattern, but is too long

  [ValidatePattern('\^[a-z][a-z0-9]\*$')]$ident = "abc"
  $ident = "123" # does not match pattern

12.3.15 The ValidateRange attribute
This attribute is used in a script-parameter or variable to specify the minimum and
maximum values of the parameter's argument. The following arguments are used to
define the characteristics of the parameter:

<!-- p.1376 -->

                                                                            ﾉ      Expand table

 Parameter Name               Purpose

 MinRange (position 0)        Type: object

                              This argument specifies the minimum value allowed.

 MaxRange (position 1)        Type: object

                              This argument specifies the maximum value allowed.

In the absence of this attribute, there is no range restriction.

Consider a function call Test1 that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [ValidateRange(1, 10)]
      [int] $StartValue
  )

  Test1 2
  Test1 -St 7
  Test1 -3 # value is too small
  Test1 12 # value is too large

Consider a function call Test2 that has the following param block and calls:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [ValidateRange("b", "f")]
      [string] $Name
  )

  Test2 "Bravo" # ok
  Test2 "Alpha" # value compares less than the minimum
  Test2 "Hotel" # value compares greater than the maximum

Consider a function call Test3 that has the following param block, and which is called as
shown:

  PowerShell

<!-- p.1377 -->

  param (
      [Parameter(Mandatory = $true)]
      [ValidateRange(0.002, 0.003)]
      [double] $Distance
  )

  Test3 0.002
  Test3 0.0019       # value is too small
  Test3 "0.005"      # value is too large

  [ValidateRange(13, 19)]$teenager = 15
  $teenager = 20 # value is too large

12.3.16 The ValidateScript attribute
This attribute is used in a script-parameter or variable to specify a script that is to be
used to validate the parameter's argument.

The argument in position 1 is a script-block-expression.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param (
      [Parameter(Mandatory = $true)]
      [ValidateScript( { ($_ -ge 1 -and $_ -le 3) -or ($_ -ge 20) })]
      [int] $Count
  )

  Test 2 # ok, valid value
  Test 25 # ok, valid value
  Test 5 # invalid value
  Test 0 # invalid value

  [ValidateScript({$_.Length --gt 7})]$password = "password" # ok
  $password = "abc123" # invalid value

12.3.17 The ValidateSet attribute
This attribute is used in a script-parameter or variable to specify a set of valid values for
the argument of the parameter. The following arguments are used to define the
characteristics of the parameter:

<!-- p.1378 -->

                                                                                  ﾉ   Expand table

 Parameter Name             Purpose

 ValidValues (position 0)   Type: string[]

                            The set of valid values.

 IgnoreCase (named)         Type: bool; Default value: $true

                            Specifies whether case should be ignored for parameters of type string.

If the parameter has an array type, every element of the corresponding argument array
must match an element of the value set.

Consider a function call Test that has the following param block, and which is called as
shown:

  PowerShell

  param ( [ValidateSet("Red", "Green", "Blue")]
      [string] $Color,

       [ValidateSet("up", "down", "left", "right", IgnoreCase =
           $false)]
       [string] $Direction

  )

  Test -Col "RED"           # case is ignored, is a member of the set
  Test -Col "white"         # case is ignored, is not a member of the set

  Test -Dir "up"            # case is not ignored, is a member of the set
  Test -Dir "Up"            # case is not ignored, is not a member of the set

  [ValidateSet(("Red", "Green", "Blue")]$color = "RED" # ok, case is ignored
  $color = "Purple" # case is ignored, is not a member of the set

<!-- p.1379 -->

13. Cmdlets

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

A cmdlet is a single-feature command that manipulates objects in PowerShell. Cmdlets can be
recognized by their name format, a verb and noun separated by a dash ( - ), such as Get-Help ,
Get-Process , and Start-Service . A verb pattern is a verb expressed using wildcards, as in W* . A

noun pattern is a noun expressed using wildcards, as in event.

Cmdlets should be simple and be designed to be used in combination with other cmdlets. For
example, Get cmdlets should only retrieve data, Set cmdlets should only establish or change
data, Format cmdlets should only format data, and Out cmdlets should only direct the output
to a specified destination.

For each cmdlet, provide a help file that can be accessed by typing:

Get-Help *cmdlet-name* -Detailed

The detailed view of the cmdlet help file should include a description of the cmdlet, the
command syntax, descriptions of the parameters, and an example that demonstrate the use of
that cmdlet.

Cmdlets are used similarly to operating system commands and utilities. PowerShell commands
are not case-sensitive.

<!-- p.1380 -->

  ７ Note

  Editor's note: The original document contains a list of cmdlet with descriptions, syntax
  diagrams, parameter definitions, and examples. This information is incomplete and out
  dated. For current information about cmdlet, consult the Reference section of the
  PowerShell documentation.

13.1 Common parameters
The common parameters are a set of cmdlet parameters that can be used with any cmdlet. They
are implemented by the PowerShell runtime environment itself, not by the cmdlet developer,
and they are automatically available to any cmdlet or function that uses the Parameter
attribute (§12.3.7) or CmdletBinding attribute (§12.3.5).

Although the common parameters are accepted by any cmdlet, they might not have any
semantics for that cmdlet. For example, if a cmdlet does not generate any verbose output,
using the Verbose common parameter has no effect.

Several common parameters override system defaults or preferences that can be set via
preference variables (§2.3.2.3). Unlike the preference variables, the common parameters affect
only the commands in which they are used.

  ７ Note

  Editor's note: The original document contains a list of the Common Parameters. This
  information is incomplete and out dated. For current information see
  about_CommonParameters.

 Last updated on 03/24/2025

<!-- p.1381 -->

A. Comment-Based Help

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

PowerShell provides a mechanism for programmers to document their scripts using special
comment directives. Comments using such syntax are called help comments. The cmdlet Get-
Help generates documentation from these directives.

A.1 Introduction
A help comment contains a help directive of the form .name followed on one or more
subsequent lines by the help content text. The help comment can be made up of a series of
single-line-comments or a delimited-comment (§2.2.3). The set of comments comprising the
documentation for a single entity is called a help topic.

For example,

 PowerShell

 # <help-directive-1>
 # <help-content-1>
 ...

 # <help-directive-n>
 # <help-content-n>

<!-- p.1382 -->

or

 PowerShell

 <#
 <help-directive-1>
 <help-content-1>
 ...

 <help-directive-n>
 <help-content-n>
 #>

All of the lines in a help topic must be contiguous. If a help topic follows a comment that is not
part of that topic, there must be at least one blank line between the two.

The directives can appear in any order, and some of the directives may appear multiple times.

Directive names are not case-sensitive.

When documenting a function, help topics may appear in one of three locations:

     Immediately before the function definition with no more than one blank line between the
     last line of the function help and the line containing the function statement.
     Inside the function's body immediately following the opening curly bracket.
     Inside the function's body immediately preceding the closing curly bracket.

When documenting a script file, help topics may appear in one of two locations:

     At the beginning of the script file, optionally preceded by comments and blank lines only.
     If the first item in the script after the help is a function definition, there must be at least
     two blank lines between the end of the script help and that function declaration.
     Otherwise, the help will be interpreted as applying to the function instead of the script
     file.
     At the end of the script file.

A.2 Help directives
A.2.1 .DESCRIPTION
Syntax:

 Syntax

<!-- p.1383 -->

 .DESCRIPTION

Description:

This directive allows for a detailed description of the function or script. (The .SYNOPSIS
directive (§A.2.11) is intended for a brief description.) This directive can be used only once in
each topic.

Examples:

 PowerShell

 <#
 .DESCRIPTION
 Computes Base to the power Exponent. Supports non-negative integer
 powers only.
 #>

A.2.2 .EXAMPLE
Syntax:

 Syntax

 .EXAMPLE

Description:

This directive allows an example of command usage to be shown.

If this directive occurs multiple times, each associated help content block is displayed as a
separate example.

Examples:

 PowerShell

 <#
 .EXAMPLE
 Get-Power 3 4
 81

 .EXAMPLE
 Get-Power -Base 3 -Exponent 4

<!-- p.1384 -->

 81
 #>

A.2.3 .EXTERNALHELP
Syntax:

 Syntax

 .EXTERNALHELP <XMLHelpFilePath>

Description:

This directive specifies the path to an XML-based help file for the script or function.

Although comment-based help is easier to implement, XML-based Help is required if more
precise control is needed over help content or if help topics are to be translated into multiple
languages. The details of XML-based help are not defined by this specification.

Examples:

 PowerShell

 <#
 .EXTERNALHELP C:\MyScripts\Update-Month-Help.xml
 #>

A.2.4 .FORWARDHELPCATEGORY
Syntax:

 Syntax

 .FORWARDHELPCATEGORY <Category>

Description:

Specifies the help category of the item in ForwardHelpTargetName (§A.2.5). Valid values are
Alias, All, Cmdlet, ExternalScript, FAQ, Filter, Function, General, Glossary, HelpFile, Provider,
and ScriptCommand. Use this directive to avoid conflicts when there are commands with the
same name.

Examples:

<!-- p.1385 -->

See §A.2.5.

A.2.5 .FORWARDHELPTARGETNAME
Syntax:

 Syntax

 .FORWARDHELPTARGETNAME <Command-Name>

Description:

Redirects to the help topic specified by <Command-Name> .

Examples:

 PowerShell

 function Help {
 <#
 .FORWARDHELPTARGETNAME Get-Help
 .FORWARDHELPCATEGORY Cmdlet
 #>
     ...
 }

The command Get-Help help is treated as if it were Get-Help Get-Help instead.

A.2.6 .INPUTS
Syntax:

 Syntax

 .INPUTS

Description:

The pipeline can be used to pipe one or more objects to a script or function. This directive is
used to describe such objects and their types.

If this directive occurs multiple times, each associated help content block is collected in the one
documentation entry, in the directives' lexical order.

Examples:

<!-- p.1386 -->

 PowerShell

 <#
 .INPUTS
 None. You cannot pipe objects to Get-Power.

 .INPUTS
 For the Value parameter, one or more objects of any kind can be written
 to the pipeline. However, the object is converted to a string before it
 is added to the item.
 #>
 function Process-Thing {
     param ( ...
         [Parameter(ValueFromPipeline=$true)]
         [Object[]]$Value,
         ...
     )
     ...
 }

A.2.7 .LINK
Syntax:

 Syntax

 .LINK

Description:

This directive specifies the name of a related topic.

If this directive occurs multiple times, each associated help content block is collected in the one
documentation entry, in the directives' lexical order.

The Link directive content can also include a URI to an online version of the same help topic.
The online version is opens when Get-Help is invoked with the Online parameter. The URI must
begin with "http" or "https".

Examples:

 PowerShell

 <#
 .LINK
 Online version: http://www.acmecorp.com/widget.html

 .LINK

<!-- p.1387 -->

 Set-ProcedureName
 #>

A.2.8 .NOTES
Syntax:

 Syntax

 .NOTES

Description:

This directive allows additional information about the function or script to be provided. This
directive can be used only once in each topic.

Examples:

 PowerShell

 <#
 .NOTES
 *arbitrary text goes here*
 #>

A.2.9 .OUTPUTS
Syntax:

 Syntax

 .OUTPUTS

Description:

This directive is used to describe the objects output by a command.

If this directive occurs multiple times, each associated help content block is collected in the one
documentation entry, in the directives' lexical order.

Examples:

 PowerShell

<!-- p.1388 -->

 <#
 .OUTPUTS
 double - Get-Power returns Base to the power Exponent.

 .OUTPUTS
 None unless the -PassThru switch parameter is used.
 #>

A.2.10 .PARAMETER
Syntax:

 Syntax

 .PARAMETER <Parameter-Name>

Description:

This directive allows for a detailed description of the given parameter. This directive can be
used once for each parameter. Parameter directives can appear in any order in the comment
block; however, the order in which their corresponding parameters are actually defined in the
source determines the order in which the parameters and their descriptions appear in the
resulting documentation.

An alternate format involves placing a parameter description comment immediately before the
declaration of the corresponding parameter variable's name. If the source contains both a
parameter description comment and a Parameter directive, the description associated with the
Parameter directive is used.

Examples:

 PowerShell

 <#
 .PARAMETER Base
 The integer value to be raised to the Exponent-th power.

 .PARAMETER Exponent
 The integer exponent to which Base is to be raised.
 #>

 function Get-Power {
     param ([long]$Base, [int]$Exponent)
     ...
 }

<!-- p.1389 -->

  function Get-Power {
      param ([long]
          # The integer value to be raised to the Exponent-th power.
          $Base,
          [int]
          # The integer exponent to which Base is to be raised.
          $Exponent
      )
      ...
  }

A.2.11 .SYNOPSIS
Syntax:

  PowerShell

  .SYNOPSIS

Description:

This directive allows for a brief description of the function or script. (The .DESCRIPTION directive
(§A.2.1) is intended for a detailed description.) This directive can be used only once in each
topic.

Examples:

  PowerShell

  <#
  .SYNOPSIS
  Computes Base to the power Exponent.
  #>

 Last updated on 03/24/2025

<!-- p.1390 -->

B. Grammar

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

This appendix contains summaries of the lexical and syntactic grammars found in the main
document.

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is optional in
  the syntax.

B.1 Lexical grammar
 Syntax

 input:
     input-elements~opt~ signature-block~opt~

 input-elements:
     input-element
     input-elements input-element

 input-element:
     whitespace
     comment

<!-- p.1391 -->

     token

 signature-block:
     signature-begin signature signature-end

 signature-begin:
     new-line-character # SIG # Begin signature block new-line-character

 signature:
     base64 encoded signature blob in multiple single-line-comments

 signature-end:
     new-line-character # SIG # End signature block new-line-character

B.1.1 Line terminators

 Syntax

 new-line-character:
     Carriage return character (U+000D)
     Line feed character (U+000A)
     Carriage return character (U+000D) followed by line feed character (U+000A)

 new-lines:
     new-line-character
     new-lines new-line-character

B.1.2 Comments

 Syntax

 comment:
     single-line-comment
     requires-comment
     delimited-comment

 single-line-comment:
     # input-characters~opt~

 input-characters:
     input-character
     input-characters input-character

 input-character:
     Any Unicode character except a new-line-character

 requires-comment:
     #Requires whitespace command-arguments

 dash:
     - (U+002D)

<!-- p.1392 -->

     EnDash character (U+2013)
     EmDash character (U+2014)
     Horizontal bar character (U+2015)

 dashdash:
     dash dash

 delimited-comment:
     <# delimited-comment-text~opt~ hashes >

 delimited-comment-text:
     delimited-comment-section
     delimited-comment-text delimited-comment-section

 delimited-comment-section:
     >
     hashes~opt~ not-greater-than-or-hash

 hashes:
     #
     hashes #

 not-greater-than-or-hash:
     Any Unicode character except > or #

B.1.3 White space

 Syntax

 whitespace:
     Any character with Unicode class Zs, Zl, or Zp
     Horizontal tab character (U+0009)
     Vertical tab character (U+000B)
     Form feed character (U+000C)
     ` (The backtick character U+0060) followed by new-line-character

B.1.4 Tokens

 Syntax

 token:
     keyword
     variable
     command
     command-parameter
     command-argument-token
     integer-literal
     real-literal
     string-literal

<!-- p.1393 -->

     type-literal
     operator-or-punctuator

B.1.5 Keywords

 Syntax

 keyword: one of
     begin             break            catch        class
     continue          data             define       do
     dynamicparam      else             elseif       end
     exit              filter           finally      for
     foreach           from             function     if
     in                inlinescript     parallel     param
     process           return           switch       throw
     trap              try              until        using
     var               while            workflow

B.1.6 Variables

 Syntax

 variable:
     $$
     $?
     $^
     $   variable-scope~opt~     variable-characters
     @   variable-scope~opt~     variable-characters
     braced-variable

 braced-variable:
     ${   variable-scope~opt~         braced-variable-characters   }

 variable-scope:
     Global:
     Local:
     Private:
     Script:
     Using:
     Workflow:
     variable-namespace

 variable-namespace:
     variable-characters     :

 variable-characters:
     variable-character
     variable-characters     variable-character

 variable-character:

<!-- p.1394 -->

     A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nd
     _   (The underscore character U+005F)
     ?

 braced-variable-characters:
     braced-variable-character
     braced-variable-characters      braced-variable-character

 braced-variable-character:
     Any Unicode character except
         }   (The closing curly brace character U+007D)
         `   (The backtick character U+0060)
     escaped-character

 escaped-character:
     `   (The backtick character U+0060) followed by any Unicode character

B.1.7 Commands

 Syntax

 generic-token:
     generic-token-parts

 generic-token-parts:
     generic-token-part
     generic-token-parts generic-token-part

 generic-token-part:
     expandable-string-literal
     verbatim-here-string-literal
     variable
     generic-token-char

 generic-token-char:
     Any Unicode character except
         {   }   (   )   ;   ,   |   &   $
         ` (The backtick character U+0060)
         double-quote-character
         single-quote-character
         whitespace
         new-line-character
         escaped-character

 generic-token-with-subexpr-start:
     generic-token-parts $(

B.1.8 Parameters

 Syntax

<!-- p.1395 -->

 command-parameter:
     dash first-parameter-char parameter-chars colon~opt~

 first-parameter-char:
     A Unicode character of classes Lu, Ll, Lt, Lm, or Lo
     _ (The underscore character U+005F)
     ?

 parameter-chars:
     parameter-char
     parameter-chars parameter-char

 parameter-char:
     Any Unicode character except
         { } ( ) ; , | & . [
         colon
         whitespace
         new-line-character

 colon:
     : (The colon character U+003A)

 verbatim-command-argument-chars:
     verbatim-command-argument-part
     verbatim-command-argument-chars verbatim-command-argument-part

 verbatim-command-argument-part:
     verbatim-command-string
     & non-ampersand-character
     Any Unicode character except
         |
         new-line-character

 non-ampersand-character:
     Any Unicode character except &

 verbatim-command-string:
     double-quote-character non-double-quote-chars
     double-quote-character

 non-double-quote-chars:
     non-double-quote-char
     non-double-quote-chars non-double-quote-char

 non-double-quote-char:
     Any Unicode character except
         double-quote-character

B.1.9 Literals

 Syntax

<!-- p.1396 -->

 literal:
     integer-literal
     real-literal
     string-literal

B.1.9.1 Integer Literals

 Syntax

 integer-literal:
     decimal-integer-literal
     hexadecimal-integer-literal

 decimal-integer-literal:
     decimal-digits numeric-type-suffix~opt~ numeric-multiplier~opt~

 decimal-digits:
     decimal-digit
     decimal-digit decimal-digits

 decimal-digit: one of
     0 1 2 3 4 5 6         7   8   9

 numeric-type-suffix:
     long-type-suffix
     decimal-type-suffix

 hexadecimal-integer-literal:
     0x hexadecimal-digits long-type-suffix~opt~
     numeric-multiplier~opt~

 hexadecimal-digits:
     hexadecimal-digit
     hexadecimal-digit decimal-digits

 hexadecimal-digit: one of
     0 1 2 3 4 5 6 7           8   9   a   b   c   d   e   f

 long-type-suffix:
     l

 numeric-multiplier: one of
     kb mb gb tb pb

B.1.9.2 Real Literals

 Syntax

 real-literal:
     decimal-digits . decimal-digits exponent-part~opt~ decimal-type-suffix~opt~
 numeric-multiplier~opt~

<!-- p.1397 -->

     . decimal-digits exponent-part~opt~ decimal-type-suffix~opt~ numeric-
 multiplier~opt~
     decimal-digits exponent-part decimal-type-suffix~opt~ numeric-multiplier~opt~

 exponent-part:
     e sign~opt~   decimal-digits

 sign: one of
     +
     dash

 decimal-type-suffix:
     d
     l

B.1.9.3 String Literals

 Syntax

 string-literal:
     expandable-string-literal
     expandable-here-string-literal
     verbatim-string-literal
     verbatim-here-string-literal

 expandable-string-literal:
     double-quote-character expandable-string-characters~opt~   dollars~opt~ double-
 quote-character

 double-quote-character:
     " (U+0022)
     Left double quotation mark (U+201C)
     Right double quotation mark (U+201D)
     Double low-9 quotation mark (U+201E)

 expandable-string-characters:
       expandable-string-part
       expandable-string-characters
       expandable-string-part

 expandable-string-part:
     Any Unicode character except
         $
         double-quote-character
         ` (The backtick character U+0060)
     braced-variable
     $ Any Unicode character except
         (
         {
         double-quote-character
         ` (The backtick character U+0060)*
     $ escaped-character
     escaped-character

<!-- p.1398 -->

    double-quote-character double-quote-character

dollars:
    $
    dollars $

expandable-here-string-literal:
    @ double-quote-character whitespace~opt~     new-line-character
        expandable-here-string-characters~opt~   new-line-character   double-quote-
character @

expandable-here-string-characters:
    expandable-here-string-part
    expandable-here-string-characters   expandable-here-string-part

expandable-here-string-part:
    Any Unicode character except
        $
        new-line-character
    braced-variable
    $ Any Unicode character except
        (
        new-line-character
    $ new-line-character Any Unicode character except double-quote-char
    $ new-line-character double-quote-char Any Unicode character except @
    new-line-character Any Unicode character except double-quote-char
    new-line-character double-quote-char Any Unicode character except @

expandable-string-with-subexpr-start:
    double-quote-character expandable-string-chars~opt~    $(

expandable-string-with-subexpr-end:
    double-quote-char

expandable-here-string-with-subexpr-start:
    @ double-quote-character whitespace~opt~ new-line-character expandable-here-
string-chars~opt~ $(

expandable-here-string-with-subexpr-end:
    new-line-character double-quote-character    @

verbatim-string-literal:
    single-quote-character verbatim-string-characters~opt~ single-quote-char

single-quote-character:
    ' (U+0027)
    Left single quotation mark (U+2018)
    Right single quotation mark (U+2019)
    Single low-9 quotation mark (U+201A)
    Single high-reversed-9 quotation mark (U+201B)

verbatim-string-characters:
    verbatim-string-part
    verbatim-string-characters verbatim-string-part

<!-- p.1399 -->

 verbatim-string-part:
     *Any Unicode character except* single-quote-character
     single-quote-character single-quote-character

 verbatim-here-string-literal:
     @ single-quote-character whitespace~opt~   new-line-character
         verbatim-here-string-characters~opt~   new-line-character
             single-quote-character *@*

 verbatim-*here-string-characters:
     verbatim-here-string-part
     verbatim-here-string-characters   verbatim-here-string-part

 verbatim-here-string-part:
     Any Unicode character except* new-line-character
     new-line-character Any Unicode character except single-quote-character
     new-line-character single-quote-character Any Unicode character except @

B.1.10 Simple Names

 Syntax

 simple-name:
     simple-name-first-char simple-name-chars

 simple-name-first-char:
     A Unicode character of classes Lu, Ll, Lt, Lm, or Lo
     _ (The underscore character U+005F)

 simple-name-chars:
     simple-name-char
     simple-name-chars simple-name-char

 simple-name-char:
     A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nd
     _ (The underscore character U+005F)

B.1.11 Type Names

 Syntax

 type-name:
     type-identifier
     type-name . type-identifier

 type-identifier:
     type-characters

 type-characters:
     type-character
     type-characters type-character

<!-- p.1400 -->

 type-character:
     A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nd
     _ (The underscore character U+005F)

 array-type-name:
     type-name [

 generic-type-name:
     type-name [

B.1.12 Operators and punctuators

 Syntax

 operator-or-punctuator: one of
     {   }    [  ]   (    )  @(   @{     $(    ;
     && || &     |   ,    ++ ..   ::     .
     !   *    /  %   +
     dash       dashdash
     dash and   dash band   dash bnot     dash bor
     dash bxor dash not     dash or       dash xor
     assignment-operator
     merging-redirection-operator
     file-redirection-operator
     comparison-operator
     format-operator

 assignment-operator: one of
     =    dash =    +=    *=    /=      %=

 file-redirection-operator: one of
     > >> 2> 2>> 3> 3>> 4> 4>>
     5> 5>> 6> 6>> *> *>> <

 merging-redirection-operator: one of
     *>&1 2>&1 3>&1 4>&1 5>&1 6>&1
     *>&2 1>&2 3>&2 4>&2 5>&2 6>&2

 comparison-operator: one of
     dash as           dash ccontains         dash ceq
     dash cge          dash cgt               dash cle
     dash clike        dash clt               dash cmatch
     dash cne          dash cnotcontains      dash cnotlike
     dash cnotmatch    dash contains          dash creplace
     dash csplit       dash eq                dash ge
     dash gt           dash icontains         dash ieq
     dash ige          dash igt               dash ile
     dash ilike        dash ilt               dash imatch
     dash in           dash ine               dash inotcontains
     dash inotlike     dash inotmatch         dash ireplace
     dash is           dash isnot             dash isplit
     dash join         dash le                dash like
