---
title: "How to use this documentation — pages 1521-1560"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1521-1560
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1521-1560
family: powershell
documentKind: "doc"
abstract: "ValidateSet Attribute Declaration Describes how to define the possible values for a parameter argument. Reference Writing a Windows PowerShell Cmdlet Last updated on 05/20/2025 Attributes in Cmdlet Code To use the common functionality provided by Windows PowerShell, the classes"
---

# How to use this documentation — pages 1521-1560

<!-- p.1521 -->

ValidateSet Attribute Declaration Describes how to define the possible values for a parameter
argument.

Reference
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1522 -->

Attributes in Cmdlet Code
To use the common functionality provided by Windows PowerShell, the classes and public
properties defined in the cmdlet code are decorated with attributes. For example, the following
class definition uses the Cmdlet attribute to identify the Microsoft .NET Framework class in
which the Get-Proc cmdlet is implemented. (This cmdlet is used as an example in this
document, and is similar to the Get-Process cmdlet provided by Windows PowerShell.)

  C#

  [Cmdlet(VerbsCommon.Get, "Proc")]
  public class GetProcCommand : Cmdlet

These attributes are considered metadata because their implementation is separate from the
implementation of the cmdlet code. When the Windows PowerShell runtime runs the cmdlet, it
recognizes the attributes and then performs the appropriate action for each attribute.

Although you might want to implement your own version of the functionality provided by
these attributes, a good cmdlet design uses these common functionalities.

For more information about the different attributes that can be declared in your cmdlets, see
Attribute Types.

See Also
Attribute Types

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1523 -->

Attribute Types
Cmdlet attributes can be grouped by functionality. The following sections describe the
available attributes and describe what the runtime does when the attribute is invoked.

Cmdlet Attributes
Cmdlet
Identifies a .NET Framework class as a cmdlet. This is the required base attribute. For more
information, see Cmdlet Attribute Declaration.

Parameter Attributes
Parameter
Identifies a public property in the cmdlet class as a cmdlet parameter. For more information,
see Parameter Attribute Declaration.

Alias
Specifies one or more aliases for a parameter. For more information, see Alias Attribute
Declaration.

Argument Validation Attributes
ValidateCount
Specifies the minimum and maximum number of arguments that are allowed for a cmdlet
parameter. For more information, see ValidateCount Attribute Declaration.

ValidateLength
Specifies a minimum and maximum number of characters for a cmdlet parameter argument.
For more information, see ValidateLength Attribute Declaration.

ValidatePattern

<!-- p.1524 -->

Specifies a regular expression pattern that the cmdlet parameter argument must match. For
more information, see ValidatePattern Attribute Declaration.

ValidateRange
Specifies the minimum and maximum values for a cmdlet parameter argument. For more
information, see ValidateRange Attribute Declaration.

ValidateSet
Specifies a set of valid values for the cmdlet parameter argument. For more information, see
ValidateSet Attribute Declaration.

See Also
Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1525 -->

Alias Attribute Declaration
The Alias attribute allows the user to specify different names for a cmdlet or a cmdlet
parameter. Aliases can be used to provide shortcuts for a parameter name, or they can provide
different names that are appropriate for different scenarios.

Syntax
 C#

 [Alias(aliasNames)]

Parameters
aliasNames (String[]) Required. Specifies a set of comma-separated alias names for the cmdlet

parameter.

Remarks
The Alias attribute is defined by the System.Management.Automation.AliasAttribute class.

Cmdlet aliases
      The Alias attribute is used with the cmdlet declaration. For more information about how
      to declare these attributes, see Cmdlet Aliases.
      Each parameter alias name must be unique. Windows PowerShell does not check for
      duplicate alias names.

Parameter aliases
      The Alias attribute is used with the Parameter attribute when you specify a cmdlet
      parameter. For more information about how to declare these attributes, see How to
      Declare Cmdlet Parameters.
      Each parameter alias name must be unique within a cmdlet. Windows PowerShell does
      not check for duplicate alias names.
      The Alias attribute is used once for each parameter in a cmdlet.

<!-- p.1526 -->

See Also
Cmdlet Aliases

Parameter Aliases

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1527 -->

Cmdlet Attribute Declaration
The Cmdlet attribute identifies a Microsoft .NET Framework class as a cmdlet and specifies the
verb and noun used to invoke the cmdlet.

Syntax
 C#

 [Cmdlet("verbName", "nounName")]
 [Cmdlet("verbName", "nounName", Named Parameters...)]

Parameters

VerbName (System.String) Required. Specifies the cmdlet verb. This verb specifies the action

taken by the cmdlet. For more information about approved cmdlet verbs, see Cmdlet Verb
Names and Required Development Guidelines.

NounName (System.String) Required. Specifies the cmdlet noun. This noun specifies the resource

that the cmdlet acts upon. For more information about cmdlet nouns, see Cmdlet Declaration
and Strongly Encouraged Development Guidelines.

SupportsShouldProcess (System.Boolean) Optional named parameter. True indicates that the

cmdlet supports calls to the System.Management.Automation.Cmdlet.ShouldProcess method,
which provides the cmdlet with a way to prompt the user before an action that changes the
system is performed. False , the default value, indicates that the cmdlet does not support calls
to the System.Management.Automation.Cmdlet.ShouldProcess method. For more information
about confirmation requests, see Requesting Confirmation.

ConfirmImpact (System.Management.Automation.ConfirmImpact) Optional named parameter.

Specifies when the action of the cmdlet should be confirmed by a call to the
System.Management.Automation.Cmdlet.ShouldProcess method.
System.Management.Automation.Cmdlet.ShouldProcess will only be called when the
ConfirmImpact value of the cmdlet (by default, Medium) is equal to or greater than the value
of the $ConfirmPreference variable. This parameter should be specified only when the
SupportsShouldProcess parameter is specified.

<!-- p.1528 -->

DefaultParameterSetName (System.String) Optional named parameter. Specifies the default

parameter set that the Windows PowerShell runtime attempts to use when it cannot determine
which parameter set to use. Notice that this situation can be eliminated by making the unique
parameter of each parameter set a mandatory parameter.

There is one case where Windows PowerShell cannot use the default parameter set even if a
default parameter set name is specified. The Windows PowerShell runtime cannot distinguish
between parameter sets based solely on object type. For example, if you have one parameter
set that takes a string as the file path, and another set that takes a FileInfo object directly,
Windows PowerShell cannot determine which parameter set to use based on the values passed
to the cmdlet, nor does it use the default parameter set. In this case, even if you specify a
default parameter set name, Windows PowerShell throws an ambiguous parameter set error
message.

SupportsTransactions (System.Boolean) Optional named parameter. True indicates that the

cmdlet can be used within a transaction. When True is specified, the Windows PowerShell
runtime adds the UseTransaction parameter to the parameter list of the cmdlet. False , the
default value, indicates that the cmdlet cannot be used within a transaction.

Remarks
     Together, the verb and noun are used to identify your registered cmdlet and to invoke
     your cmdlet within a script.

     When the cmdlet is invoked from the Windows PowerShell console, the command
     resembles the following command:

VerbName-NounName

     All cmdlets that change resources outside of Windows PowerShell should include the
      SupportsShouldProcess keyword when the Cmdlet attribute is declared, which allows the

     cmdlet to call the System.Management.Automation.Cmdlet.ShouldProcess method before
     the cmdlet performs its action. If the
     System.Management.Automation.Cmdlet.ShouldProcess call returns false , the action
     should not be taken. For more information about the confirmation requests generated by
     the System.Management.Automation.Cmdlet.ShouldProcess call, see Requesting
     Confirmation.

The Confirm and WhatIf cmdlet parameters are available only for cmdlets that support
System.Management.Automation.Cmdlet.ShouldProcess calls.

<!-- p.1529 -->

Example
The following class definition uses the Cmdlet attribute to identify the .NET Framework class for
a Get-Proc cmdlet that retrieves information about the processes running on the local
computer.

  C#

  [Cmdlet(VerbsCommon.Get, "Proc")]
  public class GetProcCommand : Cmdlet

For more information about the Get-Proc cmdlet, see GetProc Tutorial.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1530 -->

Credential Attribute Declaration
The Credential attribute is an optional attribute that can be used with credential parameters of
type System.Management.Automation.PSCredential so that a string can also be passed as an
argument to the parameter. When this attribute is added to a parameter declaration, Windows
PowerShell converts the string input into a System.Management.Automation.PSCredential
object. For example, the Get-Credential cmdlet uses this attribute to have Windows PowerShell
generate the System.Management.Automation.PSCredential object that is returned by the
cmdlet.

Syntax
 C#

 [Credential]

Remarks
      Typically this attribute is used by parameters of type
      System.Management.Automation.PSCredential so that a string can also be passed as an
      argument to the parameter. When a System.Management.Automation.PSCredential
      object is passed to the parameter, Windows PowerShell does nothing.

      When creating the System.Management.Automation.PSCredential object, Windows
      PowerShell uses the current Host to display the appropriate prompts to the user. For
      example, the default Host displays a prompt for a user name and password when this
      attribute is used. However, if a custom host is being used that defines a different prompt
      then that prompt would be displayed.

      This attribute is used with the Parameter attribute. For more information about that
      attribute, see Parameter Attribute Declaration.

      The credential attribute is defined by the
      System.Management.Automation.CredentialAttribute class.

See Also
Parameter Aliases

<!-- p.1531 -->

Parameter Attribute Declaration

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1532 -->

OutputType Attribute Declaration
The OutputType attribute identifies the .NET Framework types returned by a cmdlet, function,
or script.

Syntax
  C#

  [OutputType(params string[] type)]
  [OutputType(params Type[] type)]
  [OutputType(params string[] type, Named Parameters...)]
  [OutputType(params Type[] type, Named Parameters...)]

Parameters

Type ( string[] or Type[] ) Required. Specifies the types returned by the cmdlet function, or
script.

ParameterSetName (string[]) Optional. Specifies the parameter sets that return the types
specified in the type parameter.

providerCmdlet Optional. Specifies the provider cmdlet that returns the types specified in the
type parameter.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1533 -->

Parameter Attribute Declaration
The Parameter attribute identifies a public property of the cmdlet class as a cmdlet parameter.

Syntax
  C#

  [Parameter()]
  [Parameter(Named Parameters...)]

Parameters

Mandatory (System.Boolean) Optional named parameter. True indicates the cmdlet parameter

is required. If a required parameter is not provided when the cmdlet is invoked, Windows
PowerShell prompts the user for a parameter value. The default is false .

ParameterSetName (System.String) Optional named parameter. Specifies the parameter set that

this cmdlet parameter belongs to. If no parameter set is specified, the parameter belongs to all
parameter sets.

Position (System.Int32) Optional named parameter. Specifies the position of the parameter

within a Windows PowerShell command.

ValueFromPipeline (System.Boolean) Optional named parameter. True indicates that the

cmdlet parameter takes its value from a pipeline object. Specify this keyword if the cmdlet
accesses the complete object, not just a property of the object. The default is false .

ValueFromPipelineByPropertyName (System.Boolean) Optional named parameter. True indicates

that the cmdlet parameter takes its value from a property of a pipeline object that has either
the same name or the same alias as this parameter. For example, if the cmdlet has a Name
parameter and the pipeline object also has a Name property, the value of the Name property is
assigned to the Name parameter of the cmdlet. The default is false .

ValueFromRemainingArguments (System.Boolean) Optional named parameter. True indicates that

the cmdlet parameter accepts all remaining arguments that are passed to the cmdlet. The
default is false .

<!-- p.1534 -->

HelpMessage (System.String) Optional named parameter. Specifies a short description of the

parameter. Windows PowerShell displays this message when a cmdlet is run and a mandatory
parameter is not specified.

HelpMessageBaseName (System.String) Optional named parameter. Specifies the location where

resource identifiers reside. For example, this parameter could specify a resource assembly that
contains Help messages that you want to localize.

HelpMessageResourceId (System.String) Optional named parameter.Specifies the resource

identifier for a Help message.

DontShow (System.Boolean) Optional named parameter. True indicates that the parameter is

hidden from the user for tab expansion and IntelliSense. The default is false .

Remarks
     For more information about how to declare this attribute, see How to Declare Cmdlet
     Parameters.

     A cmdlet can have any number of parameters. However, for a better user experience, limit
     the number of parameters.

     Parameters must be declared on public non-static fields or properties. Parameters should
     be declared on properties. The property must have a public set accessor, and if the
     ValueFromPipeline or ValueFromPipelineByPropertyName keyword is specified, the

     property must have a public get accessor.

     When you specify positional parameters, limit the number of positional parameters in a
     parameter set to less than five. And, positional parameters do not have to be contiguous.
     Positions 5, 100, and 250 work the same as positions 0, 1, and 2.

     When the Position keyword is not specified, the cmdlet parameter must be referenced
     by its name.

     When you use parameter sets, note the following:

        Each parameter set must have at least one unique parameter. Good cmdlet design
        indicates this unique parameter should also be mandatory if possible. If your cmdlet is
        designed to be run without parameters, the unique parameter cannot be mandatory.

        No parameter set should contain more than one positional parameter with the same
        position.

<!-- p.1535 -->

        Only one parameter in a parameter set should declare ValueFromPipeline = true .

        Multiple parameters can define ValueFromPipelineByPropertyName = true .

     For more information about the guidelines for parameter names, see Cmdlet Parameter
     Names.

     The parameter attribute is defined by the
     System.Management.Automation.ParameterAttribute class.

     The DontShow parameter has the following side effects:
        Affects all parameter sets for the associated parameter, even if there's a parameter set
        in which DontShow is unused.
        Hides common parameters from tab completion and IntelliSense. DontShow doesn't
        hide the optional common parameters: WhatIf, Confirm, or UseTransaction.

See Also
     System.Management.Automation.ParameterAttribute
     Cmdlet Parameter Names
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1536 -->

ValidateCount Attribute Declaration
The ValidateCount attribute specifies the minimum and maximum number of arguments
allowed for a cmdlet parameter.

Syntax
 C#

 [ValidateCount(int minLength, int maxlength)]

Parameters

MinLength (System.Int32) Required. Specifies the minimum number of arguments.

MaxLength (System.Int32) Required. Specifies the maximum number of arguments.

Remarks
      For more information about how to declare this attribute, see How to Validate an
      Argument Count.
      When this attribute is not invoked, the corresponding cmdlet parameter can have any
      number of arguments.
      The Windows PowerShell runtime throws an error under the following conditions:
        The MinLength and MaxLength attribute parameters are not of type System.Int32.
        The value of the MaxLength attribute parameter is less than the value of the MinLength
        attribute parameter.
      The ValidateCount attribute is defined by the
      System.Management.Automation.ValidateCountAttribute class.

See Also
System.Management.Automation.ValidateCountAttribute

How to Validate an Argument Count

Writing a Windows PowerShell Cmdlet

<!-- p.1537 -->

Last updated on 05/20/2025

<!-- p.1538 -->

ValidateLength Attribute Declaration
The ValidateLength attribute specifies the minimum and maximum number of characters for a
cmdlet parameter argument. This attribute can also be used by Windows PowerShell functions.

Syntax
 C#

 [ValidateLength(int minLength, int maxlength)]

Parameters

MinLength (System.Int32) Required. Specifies the minimum number of characters allowed.

MaxLength (System.Int32) Required. Specifies the maximum number of characters allowed.

Remarks
      For more information about how to declare this attribute, see How to Declare Input
      Validation Rules.

      When this attribute is not used, the corresponding parameter argument can be of any
      length.

      The Windows PowerShell runtime throws an error under the following conditions:

        When the value of the MaxLength attribute parameter is less than the value of the
         MinLength attribute parameter.

        When the MaxLength attribute parameter is set to 0.

        When the argument is not a string.

      The ValidateLength attribute is defined by the
      System.Management.Automation.ValidateLengthAttribute class.

See Also
System.Management.Automation.ValidateLengthAttribute

<!-- p.1539 -->

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1540 -->

ValidatePattern Attribute Declaration
The ValidatePattern attribute specifies a regular expression pattern that validates the argument
of a cmdlet parameter. This attribute can also be used by Windows PowerShell functions.

When ValidatePattern is invoked within a cmdlet, the Windows PowerShell runtime converts the
argument of the cmdlet parameter to a string and then compares that string to the pattern
supplied by the ValidatePattern attribute. The cmdlet is run only if the converted string
representation of the argument and the supplied pattern match. If they do not match, an error
is thrown by the Windows PowerShell runtime.

Syntax
 C#

 [ValidatePattern(string regexString)]
 [ValidatePattern(string regexString, Named Parameters)]

Parameters

RegexString (System.String) Required. Specifies a regular expression that validates the

parameter argument.

Options (System.Text.RegularExpressions.RegexOptions) Optional named parameter. Specifies a
bitwise combination of System.Text.RegularExpressions.RegexOptions flags that specify regular
expression options.

Remarks
      This attribute can be used only once per parameter.

      You can use the Option parameter of the attribute to further define the pattern. For
      example, you can make the pattern case sensitive.

      If this attribute is applied to a collection, each element in the collection must match the
      pattern.

      The ValidatePattern attribute is defined by the
      System.Management.Automation.ValidatePatternAttribute class.

<!-- p.1541 -->

See Also
System.Management.Automation.ValidatePatternAttribute

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1542 -->

ValidateRange Attribute Declaration
The ValidateRange attribute specifies the minimum and maximum values (the range) for the
cmdlet parameter argument. This attribute can also be used by Windows PowerShell functions.

Syntax
 C#

 [ValidateRange(object minRange, object maxRange)]

Parameters

MinRange (System.Object) Required. Specifies the minimum value allowed.

MaxRange (System.Object) Required. Specifies the maximum value allowed.

Remarks
      The Windows PowerShell runtime throws a construction error when the value of the
      MinRange parameter is greater than the value of the MaxRange parameter.

      The Windows PowerShell runtime throws a validation error under the following
      conditions:

        When the value of the argument is less than the MinRange limit or greater than the
         MaxRange limit.

        When the argument is not of the same type as the MinRange and the MaxRange
        parameters.

      The ValidateRange attribute is defined by the
      System.Management.Automation.ValidateRangeAttribute class.

See Also
System.Management.Automation.ValidateRangeAttribute

Writing a Windows PowerShell Cmdlet

<!-- p.1543 -->

Last updated on 05/20/2025

<!-- p.1544 -->

ValidateScript Attribute Declaration
The ValidateScript attribute specifies a script that's used to validate a parameter or variable
value. PowerShell pipes the value to the script, and generates an error if the script returns
$false or if the script throws an exception.

When you use the ValidateScript attribute, the value that's being validated is mapped to the
$_ variable. You can use the $_ variable to refer to the value in the script.

Syntax
 C#

 [ValidateScriptAttribute(ScriptBlock scriptBlock)]
 [ValidateScriptAttribute(ScriptBlock scriptBlock, Named Parameters)]

Parameters
      scriptBlock - (System.Management.Automation.ScriptBlock) Required. The script block

      used to validate the input.
      ErrorMessage - Optional named parameter - The item being validated and the validating

      scriptblock are passed as the first and second formatting arguments.

  ７ Note

  The ErrorMessage argument was added in PowerShell 6.

Remarks
      This attribute can be used only once per parameter.
      If this attribute is applied to a collection, each element in the collection must match the
      pattern.
      The ValidateScript attribute is defined by the
      System.Management.Automation.ValidateScriptAttribute class.

See Also

<!-- p.1545 -->

System.Management.Automation.ValidateScriptAttribute

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1546 -->

ValidateSet Attribute Declaration
The ValidateSetAttribute attribute specifies a set of possible values for a cmdlet parameter
argument. This attribute can also be used by Windows PowerShell functions.

When this attribute is specified, the Windows PowerShell runtime determines whether the
supplied argument for the cmdlet parameter matches an element in the supplied element set.
The cmdlet is run only if the parameter argument matches an element in the set. If no match is
found, an error is thrown by the Windows PowerShell runtime.

Syntax
 C#

 [ValidateSetAttribute(params string[] validValues)]
 [ValidateSetAttribute(params string[] validValues, Named Parameters)]

Parameters

ValidValues (System.String) Required. Specifies the valid parameter element values. The

following sample shows how to specify one element or multiple elements.

 C#

 [ValidateSetAttribute("Steve")]
 [ValidateSetAttribute("Steve","Mary")]

IgnoreCase (System.Boolean) Optional named parameter. The default value of true indicates

that case is ignored. A value of false makes the cmdlet case-sensitive.

Remarks
      This attribute can be used only once per parameter.

      If the parameter value is an array, every element of the array must match an element of
      the attribute set.

      The ValidateSetAttribute attribute is defined by the
      System.Management.Automation.ValidateSetAttribute class.

<!-- p.1547 -->

See Also
System.Management.Automation.ValidateSetAttribute

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1548 -->

Cmdlet Aliases
You can use cmdlet aliases to improve the cmdlet user experience. You can add aliases to
frequently used cmdlets to reduce typing and to make it easier to complete tasks quickly. You
can include built-in aliases in your cmdlets, or users can define their own custom aliases.

For example, the Get-Command cmdlet has a built-in gcm alias. You can also use aliases to add
command names from other languages so that users do not have to learn new commands.

Alias Guidelines
Follow these guidelines when you create built-in aliases for your cmdlets:

     Before you assign aliases, start Windows PowerShell, and then run the Get-Alias cmdlet to
     see the aliases that are already used.

     Include an alias prefix that references the verb of the cmdlet name and an alias suffix that
     references the noun of the cmdlet name. For example, the alias for the Import-Module
     cmdlet is ipmo . For a list of all the verbs and their aliases, see Cmdlet Verbs.

     For cmdlets that have the same verb, include the same alias prefix. For example, the
     aliases for all the Windows PowerShell cmdlets that have the "Get" verb in their name use
     the "g" prefix.

     For cmdlets that have the same noun, include the same alias suffix. For example, the
     aliases for all the Windows PowerShell cmdlets that have the "Session" noun in their name
     use the "sn" suffix.

     For cmdlets that are equivalent to commands in other languages, use the name of the
     command.

     In general, make aliases as short as possible. Make sure the alias has at least one distinct
     character for the verb and one distinct character for the noun. Add more characters as
     needed to make the alias unique.

     For cmdlet written in C# (or any other compiled .NET language), the alias can be defined
     using the Alias attribute. For example:

       C#

<!-- p.1549 -->

       [Cmdlet("Get", "SomeObject")]
       [Alias("gso")]
       public class GetSomeObjectCommand : Cmdlet

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1550 -->

Cmdlet Output
This section discusses the types of cmdlet output and the methods that cmdlets can call to
generate output such as error messages and objects. This section also describes how to define
the .NET Framework types that are returned by your cmdlets and how those objects are
displayed.

In This Section
Types of Cmdlet Output Describes the types and output that cmdlets can generate and the
methods that cmdlets call to generate the output.

Cmdlet Error Reporting Discusses cmdlet error reporting, a subset of cmdlet output.

Extending Output Objects Discusses how to use the types files ( .ps1xml ) to extend the .NET
Framework objects that are returned by cmdlets, functions, and scripts.

PowerShell Formatting Files Describes the formatting files ( .format.ps1xml ) files that define the
default display for a specific set of .NET Framework objects in Windows PowerShell.

Custom Formatting Files Describes how to create your own custom formatting files to
overwrite the default display formats or to define the display of objects returned by your own
commands.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1551 -->

Types of cmdlet output
PowerShell provides several methods that can be called by cmdlets to generate output. These
methods use a specific operation to write their output to a specific data stream, such as the
success data stream or the error data stream. This article describes the types of output and the
methods used to generate them.

Types of output
Success output
Cmdlets can report success by returning an object that can be processed by the next command
in the pipeline. After the cmdlet has successfully performed its action, the cmdlet calls the
System.Management.Automation.Cmdlet.WriteObject method. We recommend that you call
this method instead of the System.Console.WriteLine or
System.Management.Automation.Host.PSHostUserInterface.WriteLine methods.

You can provide a PassThru [switch] parameter for cmdlets that do not typically return
objects. When the PassThru [switch] parameter is specified at the command line, the cmdlet
is asked to return an object. For an example of a cmdlet that has a PassThru parameter, see
Add-History.

Error output
Cmdlets can report errors. When a terminating error occurs, the cmdlet throws an exception.
When a non-terminating error occurs, the cmdlet calls the
System.Management.Automation.Provider.CmdletProvider.WriteError method to send an error
record to the error data stream. For more information about error reporting, see Error
Reporting Concepts.

Verbose output
Cmdlets can provide useful information to you while the cmdlet is correctly processing records
by calling the System.Management.Automation.Cmdlet.WriteVerbose method. The method
generates verbose messages that indicate how the action is proceeding.

By default, verbose messages are not displayed. You can specify the Verbose parameter when
the cmdlet is run to display these messages. Verbose is a common parameter that is available

<!-- p.1552 -->

to all cmdlets.

Progress output
Cmdlets can provide progress information to you when the cmdlet is performing tasks that
take a long time to complete, such as copying a directory recursively. To display progress
information the cmdlet calls the System.Management.Automation.Cmdlet.WriteProgress
method.

Debug output
Cmdlets can provide debug messages that are helpful when troubleshooting the cmdlet code.
To display debug information the cmdlet calls the
System.Management.Automation.Cmdlet.WriteDebug method.

By default, debug messages are not displayed. You can specify the Debug parameter when the
cmdlet is run to display these messages. Debug is a common parameter that is available to all
cmdlets.

Warning output
Cmdlets can display warning messages by calling the
System.Management.Automation.Cmdlet.WriteWarning method.

By default, warning messages are displayed. However, you can configure warning messages by
using the $WarningPreference variable or by using the Verbose and Debug parameters when
the cmdlet is called.

Displaying output
For all write-method calls, the content display is determined by specific runtime variables. The
exception is the System.Management.Automation.Cmdlet.WriteObject method. By using these
variables, you can make the appropriate write call at the correct place in your code and not
worry about when or if the output should be displayed.

Accessing the output functionality of a host
application

<!-- p.1553 -->

You can also design a cmdlet to directly access the output functionality of a host application
through the PowerShell runtime. Using the host APIs provided by PowerShell instead of
System.Console or System.Windows.Forms ensures that your cmdlet will work with a variety of
hosts. For example: the powershell.exe console host, the powershell_ise.exe graphical host,
the PowerShell remoting host, and third-party hosts.

See also
Error Reporting Concepts

Cmdlet Overview

Writing a Windows PowerShell Cmdlet

 Last updated on 04/08/2026

<!-- p.1554 -->

Cmdlet error reporting
Cmdlets should report errors differently depending on whether the errors are terminating
errors or non-terminating errors. Terminating errors are errors that cause the pipeline to be
terminated immediately, or errors that occur when there's no reason to continue processing.
Non-terminating errors are those errors that report a current error condition, but the cmdlet
can continue to process input objects. With non-terminating errors, the user is typically notified
of the problem, but the cmdlet continues to process the next input object.

Unless specified otherwise, all classes and methods mentioned in this document come from
the System.Management.Automation namespace.

Terminating and non-terminating errors
The following guidelines can be used to determine if an error condition is a terminating error
or a non-terminating error.

     Does the error condition prevent your cmdlet from successfully processing any further
     input objects? If so, this is a terminating error.

     Is the error condition related to a specific input object or a subset of input objects? If so,
     this is a non-terminating error.

     Does the cmdlet accept multiple input objects, such that processing may succeed on
     another input object? If so, this is a non-terminating error.

     Cmdlets that can accept multiple input objects should decide between what are
     terminating and non-terminating errors, even when a particular situation applies to only a
     single input object.

     Cmdlets can receive any number of input objects and send any number of success or
     error objects before throwing a terminating exception. There's no relationship between
     the number of input objects received and the number of success and error objects sent.

     Cmdlets that can accept only 0-1 input objects and generate only 0-1 output objects
     should treat errors as terminating errors and generate terminating exceptions.

Reporting non-terminating errors

<!-- p.1555 -->

The reporting of a non-terminating error should always be done within the cmdlet's
implementation of the following methods:

     Cmdlet.BeginProcessing
     Cmdlet.ProcessRecord
     Cmdlet.EndProcessing

These types of errors are reported by calling the Cmdlet.WriteError method that in turn sends
an error record to the error stream.

Reporting terminating errors
Terminating errors are reported by throwing exceptions or by calling the
Cmdlet.ThrowTerminatingError method. Be aware that cmdlets can also catch and rethrow
exceptions such as OutOfMemory, however, they aren't required to rethrow exceptions as the
PowerShell runtime will catch them as well.

You can also define your own exceptions for issues specific to your situation, or add additional
information to an existing exception using its error record.

Error records
PowerShell describes a non-terminating error condition with ErrorRecord objects. Each object
provides error category information, an optional target object, and details about the error
condition.

Error identifiers
The error identifier is a simple string that identifies the error condition within the cmdlet.
PowerShell combines this identifier with a cmdlet identifier to create a fully qualified error
identifier that can be used later when filtering error streams or logging errors, when
responding to specific errors, or with other user-specific activities.

The following guidelines should be followed when specifying error identifiers:

     Assign different, highly specific, error identifiers to different code paths. Each code path
     that calls Cmdlet.WriteError or Cmdlet.ThrowTerminatingError should have its own error
     identifier.

     Error identifiers should be unique to Common Language Runtime (CLR) exception types
     for both terminating and non-terminating errors.

<!-- p.1556 -->

      Don't change the semantics of an error identifier between versions of your cmdlet or
      PowerShell provider. After the semantics of an error identifier is established, it should
      remain constant throughout the lifecycle of your cmdlet.

      For terminating errors, use a unique error identifier for a particular CLR exception type. If
      the exception type changes, use a new error identifier.

      For non-terminating errors, use a specific error identifier for a specific input object.

      Choose text for the identifier that tersely corresponds to the error being reported. Don't
      use white space or punctuation.

      Don't generate error identifiers that aren't reproducible. For example, don't generate
      identifiers that include a process identifier. Error identifiers are useful only when they
      correspond to identifiers that are seen by other users who are experiencing the same
      problem.

Error categories
Error categories are used to group errors for the user. PowerShell defines these categories and
cmdlets and PowerShell providers must choose between them when generating the error
record.

For a description of the error categories that are available, see the ErrorCategory enumeration.
In general, you should avoid using NoError, UndefinedError, and GenericError whenever
possible.

Users can view errors based on category when they set $ErrorView to CategoryView.

See also
      Cmdlet Overview

      Types of Cmdlet Output

      Windows PowerShell Reference

 Last updated on 05/20/2025

<!-- p.1557 -->

Extending Output Objects
You can extend the .NET Framework objects that are returned by cmdlets, functions, and scripts
by using types files ( .ps1xml ). Types files are XML-based files that let you add properties and
methods to existing objects. For example, Windows PowerShell provides the Types.ps1xml file,
which adds elements to several existing .NET Framework objects. The Types.ps1xml file is
located in the Windows PowerShell installation directory ( $PSHOME ). You can create your own
types file to further extend those objects or to extend other objects. When you extend an
object by using a types file, any instance of the object is extended with the new elements.

Extending the System.Array Object
The following example shows how Windows PowerShell extends the System.Array object in the
Types.ps1xml file. By default, System.Array objects have a Length property that lists the number
of objects in the array. However, because the name "length" does not clearly describe the
property, Windows PowerShell adds the Count alias property, which displays the same value as
the Length property. The following XML adds the Count property to the System.Array type.

 XML

 <Type>
   <Name>System.Array</Name>
   <Members>
     <AliasProperty>
       <Name>Count</Name>
       <ReferencedMemberName>Length</ReferencedMemberName>
     </AliasProperty>
   </Members>
 </Type>

To see this new alias property, use a Get-Member command on any array, as shown in the
following example.

 PowerShell

 Get-Member -InputObject (1,2,3,4)

The command returns the following results.

<!-- p.1558 -->

  Output

  Name              MemberType    Definition
  ----              ----------    ----------
  Count             AliasProperty Count = Length
  Address           Method        System.Object& Address(Int32 )
  Clone             Method        System.Object Clone()
  CopyTo            Method        System.Void CopyTo(Array array, Int32 index):
  Equals            Method        System.Boolean Equals(Object obj)
  Get               Method        System.Object Get(Int32 )
  ...
  Length            Property       System.Int32 Length {get;}

You can use either the Count property or the Length property to determine how many objects
are in an array. For example:

  PowerShell

  PS> (1, 2, 3, 4).Count

  Output

  4

  PowerShell

  PS> (1, 2, 3, 4).Length

  Output

  4

Custom Types Files
To create a custom types file, start by copying an existing types file. The new file can have any
name, but it must have a .ps1xml file name extension. When you copy the file, you can place
the new file in any directory that is accessible to Windows PowerShell, but it is useful to place
the files in the Windows PowerShell installation directory ( $PSHOME ) or in a subdirectory of the
installation directory.

To add your own extended types to the file, add a types element for each object that you want
to extend. The following topics provide examples.

      For more information about adding properties and property sets, see Extended Properties

<!-- p.1559 -->

     For more information about adding methods, see Extended Methods.

     For more information about adding member sets, see Extended Member Sets.

After you define your own extended types, use one of the following methods to make your
extended objects available:

     To make your extended types file available to the current session, use the Update-
     TypeData cmdlet to add the new file. If you want your types to take precedence over the
     types that are defined in other types files (including the Types.ps1xml file), use the
     PrependData parameter of the Update-TypeData cmdlet.

     To make your extended types file available to all future sessions, add the types file to a
     module, export the current session, or add the Update-TypeData command to your
     Windows PowerShell profile.

Signing Types Files
Types files should be digitally signed to prevent tampering because the XML can include script
blocks. For more information about adding digital signatures, see about_Signing

See Also
Defining Default Properties for Objects

Defining Default Methods for Objects

Defining Default Member Sets for Objects

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1560 -->

Extending Properties for Objects
When you extend .NET Framework objects, you can add alias properties, code properties, note
properties, script properties, and property sets to the objects. The XML that defines these
properties is described in the following sections.

  ７ Note

  The examples in the following sections are from the default Types.ps1xml types file in the
  PowerShell installation directory ( $PSHOME ). For more information, see About
  Types.ps1xml.

Alias properties
An alias property defines a new name for an existing property.

In the following example, the Count property is added to the System.Array type. The
AliasProperty element defines the extended property as an alias property. The Name element
specifies the new name. And, the ReferencedMemberName element specifies the existing
property that is referenced by the alias. You can also add the AliasProperty element to the
members of the MemberSets element.

 XML

 <Type>
   <Name>System.Array</Name>
   <Members>
     <AliasProperty>
       <Name>Count</Name>
       <ReferencedMemberName>Length</ReferencedMemberName>
     </AliasProperty>
   </Members>
 </Type>

Code properties
A code property references a static property of a .NET Framework object.
