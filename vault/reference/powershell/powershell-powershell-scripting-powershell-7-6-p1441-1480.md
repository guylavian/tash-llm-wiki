---
title: "How to use this documentation — pages 1441-1480"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1441-1480
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1441-1480
family: powershell
documentKind: "doc"
abstract: "The verb-and-noun pair that identifies the cmdlet. The default parameter set that's used when multiple parameter sets are specified. The default parameter set is used when Windows PowerShell doesn't have enough information to determine which parameter set to use. Indicates if th"
---

# How to use this documentation — pages 1441-1480

<!-- p.1441 -->

     The verb-and-noun pair that identifies the cmdlet.

     The default parameter set that's used when multiple parameter sets are specified. The
     default parameter set is used when Windows PowerShell doesn't have enough information
     to determine which parameter set to use.

     Indicates if the cmdlet supports calls to the
     System.Management.Automation.Cmdlet.ShouldProcess* method. This method displays a
     confirmation message to the user before the cmdlet makes a change to the system. For
     more information about how confirmation requests are made, see Requesting Confirmation.

     Indicate the impact level (or severity) of the action associated with the confirmation
     message. In most cases, the default value of Medium should be used. For more information
     about how the impact level affects the confirmation requests that are displayed to the user,
     see Requesting Confirmation.

For more information about how to declare the cmdlet attribute, see CmdletAttribute
Declaration.

Override an input processing method (RC03)
For the cmdlet to participate in the Windows PowerShell environment, it must override at least
one of the following input processing methods.

     System.Management.Automation.Cmdlet.BeginProcessing This method is called one time,
     and it is used to provide pre-processing functionality.
     System.Management.Automation.Cmdlet.ProcessRecord This method is called multiple
     times, and it's used to provide record-by-record functionality.
     System.Management.Automation.Cmdlet.EndProcessing This method is called one time, and
     it's used to provide post-processing functionality.

Specify the OutputType attribute (RC04)
The OutputType attribute (introduced in Windows PowerShell 2.0) specifies the .NET Framework
type that your cmdlet returns to the pipeline. By specifying the output type of your cmdlets you
make the objects returned by your cmdlet more discoverable by other cmdlets. For more
information about decorating the cmdlet class with this attribute, see OutputType Attribute
Declaration.

Don't retain handles to output objects (RC05)

<!-- p.1442 -->

Your cmdlet shouldn't retain any handles to the objects that are passed to the
System.Management.Automation.Cmdlet.WriteObject* method. These objects are passed to the
next cmdlet in the pipeline, or they're used by a script. If you retain the handles to the objects,
two entities will own each object, which causes errors.

Handle errors robustly (RC06)
An administration environment inherently detects and makes important changes to the system
that you are administering. Therefore, it's vital that cmdlets handle errors correctly. For more
information about error records, see Windows PowerShell Error Reporting.

     When an error prevents a cmdlet from continuing to process any more records, it's a
     terminating error. The cmdlet must call the
     System.Management.Automation.Cmdlet.ThrowTerminatingError* method that references
     an System.Management.Automation.ErrorRecord object. If an exception isn't caught by the
     cmdlet, the Windows PowerShell runtime itself throws a terminating error that contains less
     information.

     For a non-terminating error that doesn't stop operation on the next record that's coming
     from the pipeline (for example, a record produced by a different process), the cmdlet must
     call the System.Management.Automation.Cmdlet.WriteError* method that references an
     System.Management.Automation.ErrorRecord object. An example of a non-terminating
     error is the error that occurs if a particular process fails to stop. Calling the
     System.Management.Automation.Cmdlet.WriteError* method allows the user to consistently
     perform the actions requested and to retain the information for particular actions that fail.
     Your cmdlet should handle each record as independently as possible.

     The System.Management.Automation.ErrorRecord object that's referenced by the
     System.Management.Automation.Cmdlet.ThrowTerminatingError* and
     System.Management.Automation.Cmdlet.WriteError* methods requires an exception at its
     core. Follow the .NET Framework design guidelines when you determine the exception to
     use. If the error is semantically the same as an existing exception, use that exception or
     derive from that exception. Otherwise, derive a new exception or exception hierarchy
     directly from the System.Exception type.

An System.Management.Automation.ErrorRecord object also requires an error category that
groups errors for the user. The user can view errors based on the category by setting the value of
the $ErrorView shell variable to CategoryView. The possible categories are defined by the
System.Management.Automation.ErrorCategory enumeration.

<!-- p.1443 -->

      If a cmdlet creates a new thread, and if the code that's running in that thread throws an
      unhandled exception, Windows PowerShell can't catch the error and terminates the process.

      If an object has code in its destructor that causes an unhandled exception, Windows
      PowerShell can't catch the error and terminates the process. This also occurs if an object
      calls Dispose methods that cause an unhandled exception.

Use a Windows PowerShell module to deploy your
cmdlets (RC07)
Create a Windows PowerShell module to package and deploy your cmdlets. Support for modules
is introduced in Windows PowerShell 2.0. You can use the assemblies that contain your cmdlet
classes directly as binary module files (this is very useful when testing your cmdlets), or you can
create a module manifest that references the cmdlet assemblies. You can also add existing snap-
in assemblies when using modules. For more information about modules, see Writing a Windows
PowerShell Module.

See also
      Strongly Encouraged Development Guidelines
      Advisory Development Guidelines
      Writing a Windows PowerShell Cmdlet

 Last updated on 06/16/2026

<!-- p.1444 -->

Strongly Encouraged Development
Guidelines
This section describes guidelines that you should follow when you write your cmdlets. They are
separated into guidelines for designing cmdlets and guidelines for writing your cmdlet code.
You might find that these guidelines are not applicable for every scenario. However, if they do
apply and you do not follow these guidelines, your users might have a poor experience when
they use your cmdlets.

Design Guidelines
The following guidelines should be followed when designing cmdlets to ensure a consistent
user experience between using your cmdlets and other cmdlets. When you find a Design
guideline that applies to your situation, be sure to look at the Code guidelines for similar
guidelines.

Use a Specific Noun for a Cmdlet Name (SD01)
Nouns used in cmdlet naming need to be very specific so that the user can discover your
cmdlets. Prefix generic nouns such as "server" with a shortened version of the product name.
For example, if a noun refers to a server that is running an instance of Microsoft SQL Server,
use a noun such as "SQLServer". The combination of specific nouns and the short list of
approved verbs enable the user to quickly discover and anticipate functionality while avoiding
duplication among cmdlet names.

To enhance the user experience, the noun that you choose for a cmdlet name should be
singular. For example, use the name Get-Process instead of Get-Processes . It is best to follow
this rule for all cmdlet names, even when a cmdlet is likely to act upon more than one item.

Use Pascal Case for Cmdlet Names (SD02)
Use Pascal case for parameter names. In other words, capitalize the first letter of verb and all
terms used in the noun. For example, " Clear-ItemProperty ".

Parameter Design Guidelines (SD03)

<!-- p.1445 -->

A cmdlet needs parameters that receive the data on which it must operate, and parameters
that indicate information that is used to determine the characteristics of the operation. For
example, a cmdlet might have a Name parameter that receives data from the pipeline, and the
cmdlet might have a Force parameter to indicate that the cmdlet can be forced to perform its
operation. There is no limit to the number of parameters that a cmdlet can define.

Use Standard Parameter Names

Your cmdlet should use standard parameter names so that the user can quickly determine what
a particular parameter means. If a more specific name is required, use a standard parameter
name, and then specify a more specific name as an alias. For example, the Get-Service cmdlet
has a parameter that has a generic name ( Name ) and a more specific alias ( ServiceName ). Both
terms can be used to specify the parameter.

For more information about parameter names and their data types, see Cmdlet Parameter
Name and Functionality Guidelines.

Use Singular Parameter Names

Avoid using plural names for parameters whose value is a single element. This includes
parameters that take arrays or lists because the user might supply an array or list with only one
element.

Plural parameter names should be used only in those cases where the value of the parameter is
always a multiple-element value. In these cases, the cmdlet should verify that multiple
elements are supplied, and the cmdlet should display a warning to the user if multiple
elements are not supplied.

Use Pascal Case for Parameter Names

Use Pascal case for parameter names. In other words, capitalize the first letter of each word in
the parameter name, including the first letter of the name. For example, the parameter name
ErrorAction uses the correct capitalization. The following parameter names use incorrect

capitalization:

      errorAction

      erroraction

Parameters That Take a List of Options

There are two ways to create a parameter whose value can be selected from a set of options.

<!-- p.1446 -->

     Define an enumeration type (or use an existing enumeration type) that specifies the valid
     values. Then, use the enumeration type to create a parameter of that type.

     Add the ValidateSet attribute to the parameter declaration. For more information about
     this attribute, see ValidateSet Attribute Declaration.

Use Standard Types for Parameters

To ensure consistency with other cmdlets, use standard types for parameters where ever
possible. For more information about the types that should be used for different parameter,
see Standard Cmdlet Parameter Names and Types. This topic provides links to several topics
that describe the names and .NET Framework types for groups of standard parameters, such as
the "activity parameters".

Use Strongly-Typed .NET Framework Types

Parameters should be defined as .NET Framework types to provide better parameter validation.
For example, parameters that are restricted to one value from a set of values should be defined
as an enumeration type. To support a Uniform Resource Identifier (URI) value, define the
parameter as a System.Uri type. Avoid basic string parameters for all but free-form text
properties.

Use Consistent Parameter Types

When the same parameter is used by multiple cmdlets, always use the same parameter type.
For example, if the Process parameter is a System.Int16 type for one cmdlet, do not make the
Process parameter for another cmdlet a System.Uint16 type.

Parameters That Take True and False

If your parameter takes only true and false , define the parameter as type
System.Management.Automation.SwitchParameter. A [switch] parameter is treated as true
when it is specified in a command. If the parameter is not included in a command, Windows
PowerShell considers the value of the parameter to be false . Do not define Boolean
parameters.

If your parameter needs to differentiate between 3 values: $true, $false and "unspecified", then
define a parameter of type Nullable<bool>. The need for a 3rd, "unspecified" value typically
occurs when the cmdlet can modify a Boolean property of an object. In this case "unspecified"
means to not change the current value of the property.

<!-- p.1447 -->

Support Arrays for Parameters

Frequently, users must perform the same operation against multiple arguments. For these
users, a cmdlet should accept an array as parameter input so that a user can pass the
arguments into the parameter as a Windows PowerShell variable. For example, the Get-Process
cmdlet uses an array for the strings that identify the names of the processes to retrieve.

Support the PassThru Parameter

By default, many cmdlets that modify the system, such as the Stop-Process cmdlet, act as
"sinks" for objects and do not return a result. These cmdlet should implement the PassThru
parameter to force the cmdlet to return an object. When the PassThru parameter is specified,
the cmdlet returns an object by using a call to the
System.Management.Automation.Cmdlet.WriteObject method. For example, the following
command stops the Calc (CalculatorApp.exe) and passes the resultant process to the pipeline.

 PowerShell

 Stop-Process -Name CalculatorApp -PassThru

In most cases, Add, Set, and New cmdlets should support a PassThru parameter.

Support Parameter Sets

A cmdlet is intended to accomplish a single purpose. However, there is frequently more than
one way to describe the operation or the operation target. For example, a process might be
identified by its name, by its identifier, or by a process object. The cmdlet should support all
the reasonable representations of its targets. Normally, the cmdlet satisfies this requirement by
specifying sets of parameters (referred to as parameter sets) that operate together. A single
parameter can belong to any number of parameter sets. For more information about
parameter sets, see Cmdlet Parameter Sets.

When you specify parameter sets, set only one parameter in the set to ValueFromPipeline. For
more information about how to declare the Parameter attribute, see ParameterAttribute
Declaration.

When parameter sets are used, the default parameter set is defined by the Cmdlet attribute.
The default parameter set should include the parameters most likely to be used in an
interactive Windows PowerShell session. For more information about how to declare the
Cmdlet attribute, see CmdletAttribute Declaration.

<!-- p.1448 -->

Provide Feedback to the User (SD04)
Use the guidelines in this section to provide feedback to the user. This feedback allows the user
to be aware of what is occurring in the system and to make better administrative decisions.

The Windows PowerShell runtime allows a user to specify how to handle output from each call
to the Write method by setting a preference variable. The user can set several preference
variables, including a variable that determines whether the system should display information
and a variable that determines whether the system should query the user before taking further
action.

Support the WriteWarning, WriteVerbose, and WriteDebug Methods

A cmdlet should call the System.Management.Automation.Cmdlet.WriteWarning method when
the cmdlet is about to perform an operation that might have an unintended result. For
example, a cmdlet should call this method if the cmdlet is about to overwrite a read-only file.

A cmdlet should call the System.Management.Automation.Cmdlet.WriteVerbose method when
the user requires some detail about what the cmdlet is doing. For example, a cmdlet should call
this information if the cmdlet author feels that there are scenarios that might require more
information about what the cmdlet is doing.

The cmdlet should call the System.Management.Automation.Cmdlet.WriteDebug method when
a developer or product support engineer must understand what has corrupted the cmdlet
operation. It is not necessary for the cmdlet to call the
System.Management.Automation.Cmdlet.WriteDebug method in the same code that calls the
System.Management.Automation.Cmdlet.WriteVerbose method because the Debug parameter
presents both sets of information.

Support WriteProgress for Operations that take a Long Time

Cmdlet operations that take a long time to complete and that cannot run in the background
should support progress reporting through periodic calls to the
System.Management.Automation.Cmdlet.WriteProgress method.

Use the Host Interfaces

Occasionally, a cmdlet must communicate directly with the user instead of by using the various
Write or Should methods supported by the System.Management.Automation.Cmdlet class. In
this case, the cmdlet should derive from the System.Management.Automation.PSCmdlet class

<!-- p.1449 -->

and use the System.Management.Automation.PSCmdlet.Host* property. This property supports
different levels of communication type, including the PromptForChoice, Prompt, and
WriteLine/ReadLine types. At the most specific level, it also provides ways to read and write
individual keys and to deal with buffers.

Unless a cmdlet is specifically designed to generate a graphical user interface (GUI), it should
not bypass the host by using the System.Management.Automation.PSCmdlet.Host* property.
An example of a cmdlet that is designed to generate a GUI is the Out-GridView cmdlet.

  ７ Note

  Cmdlets should not use the System.Console API.

Create a Cmdlet Help File (SD05)
For each cmdlet assembly, create a Help.xml file that contains information about the cmdlet.
This information includes a description of the cmdlet, descriptions of the cmdlet's parameters,
examples of the cmdlet's use, and more.

Code Guidelines
The following guidelines should be followed when coding cmdlets to ensure a consistent user
experience between using your cmdlets and other cmdlets. When you find a Code guideline
that applies to your situation, be sure to look at the Design guidelines for similar guidelines.

Coding Parameters (SC01)
Define a parameter by declaring a public property of the cmdlet class that is decorated with
the Parameter attribute. Parameters do not have to be static members of the derived .NET
Framework class for the cmdlet. For more information about how to declare the Parameter
attribute, see Parameter Attribute Declaration.

Support Windows PowerShell Paths

The Windows PowerShell path is the mechanism for normalizing access to namespaces. When
you assign a Windows PowerShell path to a parameter in the cmdlet, the user can define a
custom "drive" that acts as a shortcut to a specific path. When a user designates such a drive,
stored data, such as data in the Registry, can be used in a consistent way.

<!-- p.1450 -->

If your cmdlet allows the user to specify a file or a data source, it should define a parameter of
type System.String. If more than one drive is supported, the type should be an array. The name
of the parameter should be Path , with an alias of PSPath . Additionally, the Path parameter
should support wildcard characters. If support for wildcard characters is not required, define a
LiteralPath parameter.

If the data that the cmdlet reads or writes has to be a file, the cmdlet should accept Windows
PowerShell path input, and the cmdlet should use the
System.Management.Automation.SessionState.Path property to translate the Windows
PowerShell paths into paths that the file system recognizes. The specific mechanisms include
the following methods:

     System.Management.Automation.PSCmdlet.GetResolvedProviderPathFromPSPath
     System.Management.Automation.PSCmdlet.GetUnresolvedProviderPathFromPSPath
     System.Management.Automation.PathIntrinsics.GetResolvedProviderPathFromPSPath
     System.Management.Automation.PathIntrinsics.GetUnresolvedProviderPathFromPSPath

If the data that the cmdlet reads or writes is only a set of strings instead of a file, the cmdlet
should use the provider content information ( Content member) to read and write. This
information is obtained from the
System.Management.Automation.Provider.CmdletProvider.InvokeProvider property. These
mechanisms allow other data stores to participate in the reading and writing of data.

Support Wildcard Characters

A cmdlet should support wildcard characters if possible. Support for wildcard characters occurs
in many places in a cmdlet (especially when a parameter takes a string to identify one object
from a set of objects). For example, the sample Stop-Proc cmdlet from the StopProc Tutorial
defines a Name parameter to handle strings that represent process names. This parameter
supports wildcard characters so that the user can easily specify the processes to stop.

When support for wildcard characters is available, a cmdlet operation usually produces an
array. Occasionally, it does not make sense to support an array because the user might use
only a single item at a time. For example, the Set-Location cmdlet does not need to support an
array because the user is setting only a single location. In this instance, the cmdlet still supports
wildcard characters, but it forces resolution to a single location.

For more information about wildcard-character patterns, see Supporting Wildcard Characters
in Cmdlet Parameters.

<!-- p.1451 -->

Defining Objects

This section contains guidelines for defining objects for cmdlets and for extending existing
objects.

Define Standard Members

Define standard members to extend an object type in a custom Types.ps1xml file (use the
Windows PowerShell Types.ps1xml file as a template). Standard members are defined by a
node with the name PSStandardMembers. These definitions allow other cmdlets and the
Windows PowerShell runtime to work with your object in a consistent way.

Define ObjectMembers to Be Used as Parameters

If you are designing an object for a cmdlet, ensure that its members map directly to the
parameters of the cmdlets that will use it. This mapping allows the object to be easily sent to
the pipeline and to be passed from one cmdlet to another.

Preexisting .NET Framework objects that are returned by cmdlets are frequently missing some
important or convenient members that are needed by the script developer or user. These
missing members can be particularly important for display and for creating the correct member
names so that the object can be correctly passed to the pipeline. Create a custom Types.ps1xml
file to document these required members. When you create this file, we recommend the
following naming convention: <Your_Product_Name>.Types.ps1xml.

For example, you could add a Mode script property to the System.IO.FileInfo type to display the
attributes of a file more clearly. Additionally, you could add a Count alias property to the
System.Array type to allow the consistent use of that property name (instead of Length ).

Implement the IComparable Interface

Implement a System.IComparable interface on all output objects. This allows the output objects
to be easily piped to various sorting and analysis cmdlets.

Update Display Information

If the display for an object does not provide the expected results, create a custom
<YourProductName>.Format.ps1xml file for that object.

Support Well Defined Pipeline Input (SC02)
Implement for the Middle of a Pipeline

<!-- p.1452 -->

Implement a cmdlet assuming that it will be called from the middle of a pipeline (that is, other
cmdlets will produce its input or consume its output). For example, you might assume that the
Get-Process cmdlet, because it generates data, is used only as the first cmdlet in a pipeline.

However, because this cmdlet is designed for the middle of a pipeline, this cmdlet allows
previous cmdlets or data in the pipeline to specify the processes to retrieve.

Support Input from the Pipeline

In each parameter set for a cmdlet, include at least one parameter that supports input from the
pipeline. Support for pipeline input allows the user to retrieve data or objects, to send them to
the correct parameter set, and to pass the results directly to a cmdlet.

A parameter accepts input from the pipeline if the Parameter attribute includes the
ValueFromPipeline keyword, the ValueFromPipelineByPropertyName keyword attribute, or both

keywords in its declaration. If none of the parameters in a parameter set support the
ValueFromPipeline or ValueFromPipelineByPropertyName keywords, the cmdlet cannot

meaningfully be placed after another cmdlet because it will ignore any pipeline input.

Support the ProcessRecord Method

To accept all the records from the preceding cmdlet in the pipeline, your cmdlet must
implement the System.Management.Automation.Cmdlet.ProcessRecord method. Windows
PowerShell calls this method multiple times, once for every record that is sent to your cmdlet.

Write Single Records to the Pipeline (SC03)
When a cmdlet returns objects, the cmdlet should write the objects immediately as they are
generated. The cmdlet should not hold them in order to buffer them into a combined array.
The cmdlets that receive the objects as input will then be able to process, display, or process
and display the output objects without delay. A cmdlet that generates output objects one at a
time should call the System.Management.Automation.Cmdlet.WriteObject method. A cmdlet
that generates output objects in batches (for example, because an underlying API returns an
array of output objects) should call the System.Management.Automation.Cmdlet.WriteObject
Method with its second parameter set to true .

Make Cmdlets Case-Insensitive and Case-Preserving (SC04)
By default, Windows PowerShell itself is case-insensitive. However, because it deals with many
preexisting systems, Windows PowerShell does preserve case for ease of operation and
compatibility. In other words, if a character is supplied in uppercase letters, Windows

<!-- p.1453 -->

PowerShell keeps it in uppercase letters. For systems to work well, a cmdlet needs to follow this
convention. If possible, it should operate in a case-insensitive way. It should, however, preserve
the original case for cmdlets that occur later in a command or in the pipeline.

See Also
Required Development Guidelines

Advisory Development Guidelines

Writing a Windows PowerShell Cmdlet

 Last updated on 04/08/2026

<!-- p.1454 -->

Advisory Development Guidelines
Article • 05/22/2025

This section describes guidelines that you should consider to ensure good development and
user experiences. Sometimes they might apply, and sometimes they might not.

Design Guidelines
The following guidelines should be considered when designing cmdlets. When you find a
Design guideline that applies to your situation, be sure to look at the Code guidelines for
similar guidelines.

Support an InputObject Parameter (AD01)
Because Windows PowerShell works directly with Microsoft .NET Framework objects, a .NET
Framework object is often available that exactly matches the type the user needs to perform a
particular operation. InputObject is the standard name for a parameter that takes such an
object as input. For example, the sample Stop-Proc cmdlet in the StopProc Tutorial defines an
InputObject parameter of type Process that supports the input from the pipeline. The user can

get a set of process objects, manipulate them to select the exact objects to stop, and then pass
them to the Stop-Proc cmdlet directly.

Support the Force Parameter (AD02)
Occasionally, a cmdlet needs to protect the user from performing a requested operation. Such
a cmdlet should support a Force parameter to allow the user to override that protection if the
user has permissions to perform the operation.

For example, the Remove-Item cmdlet doesn't normally remove a read-only file. However, this
cmdlet supports a Force parameter so a user can force removal of a read-only file. If the user
already has permission to modify the read-only attribute, and the user removes the file, use of
the Force parameter simplifies the operation. However, if the user doesn't have permission to
remove the file, the Force parameter has no effect.

Handle Credentials Through Windows PowerShell (AD03)
A cmdlet should define a Credential parameter to represent credentials. This parameter must
be of type System.Management.Automation.PSCredential and must be defined using a
Credential attribute declaration. This support automatically prompts the user for the user

<!-- p.1455 -->

name, for the password, or for both when a full credential isn't supplied directly. For more
information about the Credential attribute, see Credential Attribute Declaration.

Support Encoding Parameters (AD04)
If your cmdlet reads or writes text to or from a binary form, such as writing to or reading from
a file in a filesystem, then your cmdlet has to have Encoding parameter that specifies how the
text is encoded in the binary form.

Test Cmdlets Should Return a Boolean (AD05)
Cmdlets that perform tests against their resources should return a System.Boolean type to the
pipeline so that they can be used in conditional expressions.

Code Guidelines
The following guidelines should be considered when writing cmdlet code. When you find a
guideline that applies to your situation, be sure to look at the Design guidelines for similar
guidelines.

Follow Cmdlet Class Naming Conventions (AC01)
By following standard naming conventions, you make your cmdlets more discoverable, and you
help the user understand exactly what the cmdlets do. This practice is particularly important for
other developers using Windows PowerShell because cmdlets are public types.

Define a Cmdlet in the Correct Namespace
You normally define the class for a cmdlet in a .NET Framework namespace that appends
.Commands to the namespace that represents the product in which the cmdlet runs. For

example, cmdlets that are included with Windows PowerShell are defined in the
Microsoft.PowerShell.Commands namespace.

Name the Cmdlet Class to Match the Cmdlet Name
When you name the .NET Framework class that implements a cmdlet, name the class <Verb>
<Noun>Command , where you replace the <Verb> and <Noun> placeholders with the verb and noun

used for the cmdlet name. For example, the Get-Process cmdlet is implemented by a class
called GetProcessCommand .

<!-- p.1456 -->

If No Pipeline Input Override the BeginProcessing Method
(AC02)
If your cmdlet doesn't accept input from the pipeline, processing should be implemented in
the System.Management.Automation.Cmdlet.BeginProcessing method. Use of this method
allows Windows PowerShell to maintain ordering between cmdlets. The first cmdlet in the
pipeline always returns its objects before the remaining cmdlets in the pipeline get a chance to
start their processing.

To Handle Stop Requests Override the StopProcessing Method
(AC03)
Override the System.Management.Automation.Cmdlet.StopProcessing method so that your
cmdlet can handle stop signal. Some cmdlets take a long time to complete their operation, and
they let a long time pass between calls to the Windows PowerShell runtime, such as when the
cmdlet blocks the thread in long-running RPC calls. This includes cmdlets that make calls to the
System.Management.Automation.Cmdlet.WriteObject method, to the
System.Management.Automation.Cmdlet.WriteError method, and to other feedback
mechanisms that may take a long time to complete. For these cases the user might need to
send a stop signal to these cmdlets.

Implement the IDisposable Interface (AC04)
If your cmdlet has objects that aren't disposed of (written to the pipeline) by the
System.Management.Automation.Cmdlet.ProcessRecord method, your cmdlet might require
additional object disposal. For example, if your cmdlet opens a file handle in its
System.Management.Automation.Cmdlet.BeginProcessing method and keeps the handle open
for use by the System.Management.Automation.Cmdlet.ProcessRecord method, this handle has
to be closed at the end of processing.

The Windows PowerShell runtime doesn't always call the
System.Management.Automation.Cmdlet.EndProcessing method. For example, the
System.Management.Automation.Cmdlet.EndProcessing method might not be called if the
cmdlet is canceled midway through its operation or if a terminating error occurs in any part of
the cmdlet. Therefore, the .NET Framework class for a cmdlet that requires object cleanup
should implement the complete System.IDisposable interface pattern, including the finalizer, so
that the Windows PowerShell runtime can call both the
System.Management.Automation.Cmdlet.EndProcessing and System.IDisposable.Dispose*
methods at the end of processing.

<!-- p.1457 -->

Use Serialization-friendly Parameter Types (AC05)
To support running your cmdlet on remote computers, use types that can be serialized on the
client computer and then rehydrated on the server computer. The follow types are
serialization-friendly.

Primitive types:

     Byte, SByte, Decimal, Single, Double, Int16, Int32, Int64, Uint16, UInt32, and UInt64.
     Boolean, Guid, Byte[], TimeSpan, DateTime, Uri, and Version.
     Char, String, XmlDocument.

Built-in rehydratable types:

     PSPrimitiveDictionary
     SwitchParameter
     PSListModifier
     PSCredential
     IPAddress, MailAddress
     CultureInfo
     X509Certificate2, X500DistinguishedName
     DirectorySecurity, FileSecurity, RegistrySecurity

Other types:

     SecureString
     Containers (lists and dictionaries of the above type)

Use SecureString for Sensitive Data (AC06)
When handling sensitive data always use the System.Security.SecureString data type. This could
include pipeline input to parameters, as well as returning sensitive data to the pipeline.

While .NET recommends against using SecureString for new development, PowerShell
continues to support the SecureString class for backward compatibility. Using a SecureString is
still more secure than using a plain text string. PowerShell still relies on the SecureString type
to avoid accidentally exposing the contents to the console or in logs. Use SecureString
carefully, because it can be easily converted to a plain text string. For a full discussion about
using SecureString, see the System.Security.SecureString class documentation.

See Also
Required Development Guidelines

<!-- p.1458 -->

Strongly Encouraged Development Guidelines

Writing a Windows PowerShell Cmdlet

<!-- p.1459 -->

Cmdlet Class Declaration
A Microsoft .NET Framework class is declared as a cmdlet by specifying the Cmdlet attribute as
metadata for the class. (The Cmdlet attribute is the only required attribute for all cmdlets).
When you specify the Cmdlet attribute, you must specify the verb-and-noun pair that identifies
the cmdlet to the user. And, you must describe the Windows PowerShell functionality that the
cmdlet supports. For more information about the declaration syntax that is used to specify the
Cmdlet attribute, see Cmdlet Attribute Declaration.

  ７ Note

  The Cmdlet attribute is defined by the System.Management.Automation.CmdletAttribute
  class. The properties of this class correspond to the declaration parameters that are used
  when you declare the attribute.

Nouns
The noun of the cmdlet specifies the resources upon which the cmdlet acts. The noun
differentiates your cmdlets from other cmdlets.

Nouns in cmdlet names must be specific, and in the case of generic nouns, such as server, it is
best to add a short prefix that differentiates your resource from other similar resources. For
example, a cmdlet name that includes a noun with a prefix is Get-SQLServer . The combination
of a specific noun with a more general verb enables the user to quickly locate the cmdlet by its
action and then identify the cmdlet by its resource while avoiding unnecessary cmdlet name
duplication.

For a list of special characters that cannot be used in cmdlet names, see Required Development
Guidelines.

Verbs
When you specify a verb, the development guidelines require you to use one of the predefined
verbs provided by Windows PowerShell. By using one of these predefined verbs, you will
ensure consistency between the cmdlets that you write and the cmdlets that are written by
Microsoft and by others. For example, the "Get" verb is used for cmdlets that retrieve data.

<!-- p.1460 -->

For more information about guidelines for verbs, see Cmdlet Verb Names. For a list of special
characters that cannot be used in cmdlet names, see Required Development Guidelines.

Supporting Windows PowerShell Functionality
The Cmdlet attribute also allows you to specify that your cmdlet supports some of the
common functionality that is provided by Windows PowerShell. This includes support for
common functionality such as user feedback confirmation (referred to as support for the
ShouldProcess feature) and support for transactions. (Support for transactions was introduced
in Windows PowerShell 2.0).

For more information about the declaration syntax that is used to specify the Cmdlet attribute,
see Cmdlet Attribute Declaration.

Cmdlet Class Definition
The following code is the definition for a GetProc cmdlet class. Notice that Pascal casing is used
and that the name of the class includes the verb and noun of the cmdlet.

 C#

 [Cmdlet(VerbsCommon.Get, "Proc")]
 public class GetProcCommand : Cmdlet

Pascal Casing
When you name cmdlets, use Pascal casing. For example, the Get-Item and Get-ItemProperty
cmdlets show the correct way to use capitalization when you are naming cmdlets.

See Also
System.Management.Automation.CmdletAttribute

CmdletAttribute Declaration

Cmdlet Verb Names

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

<!-- p.1461 -->

Last updated on 05/20/2025

<!-- p.1462 -->

Approved Verbs for PowerShell Commands
PowerShell uses a verb-noun pair for the names of cmdlets and for their derived .NET classes.
The verb part of the name identifies the action that the cmdlet performs. The noun part of the
name identifies the entity on which the action is performed. For example, the Get-Command
cmdlet retrieves all the commands that are registered in PowerShell.

  ７ Note

  PowerShell uses the term verb to describe a word that implies an action even if that word
  isn't a standard verb in the English language. For example, the term New is a valid
  PowerShell verb name because it implies an action even though it isn't a verb in the
  English language.

Each approved verb has a corresponding alias prefix defined. We use this alias prefix in aliases
for commands using that verb. For example, the alias prefix for Import is ip and, accordingly,
the alias for Import-Module is ipmo . This is a recommendation but not a rule; in particular, it
need not be respected for command aliases mimicking well known commands from other
environments.

Verb Naming Recommendations
The following recommendations help you choose an appropriate verb for your cmdlet, to
ensure consistency between the cmdlets that you create, the cmdlets that are provided by
PowerShell, and the cmdlets that are designed by others.

     Use one of the predefined verb names provided by PowerShell
     Use the verb to describe the general scope of the action, and use parameters to further
     refine the action of the cmdlet.
     Don't use a synonym of an approved verb. For example, always use Remove , never use
      Delete or Eliminate .

     Use only the form of each verb that's listed in this topic. For example, use Get , but don't
     use Getting or Gets .
     Don't use the following reserved verbs or aliases. The PowerShell language and a rare few
     cmdlets use these verbs under exceptional circumstances.
         ForEach ( foreach )
         Ping ( pi )

         Sort ( sr )

         Tee ( te )

<!-- p.1463 -->

         Where ( wh )

You may get a complete list of verbs using the Get-Verb cmdlet.

Similar Verbs for Different Actions
The following similar verbs represent different actions.

New vs. Add

Use the New verb to create a new resource. Use the Add to add something to an existing
container or resource. For example, Add-Content adds output to an existing file.

New vs. Set

Use the New verb to create a new resource. Use the Set verb to modify an existing resource,
optionally creating it if it doesn't exist, such as the Set-Variable cmdlet.

Find vs. Search

Use the Find verb to look for an object. Use the Search verb to create a reference to a
resource in a container.

Get vs. Read

Use the Get verb to obtain information about a resource (such as a file) or to obtain an object
with which you can access the resource in future. Use the Read verb to open a resource and
extract information contained within.

Invoke vs. Start

Use the Invoke verb to perform synchronous operations, such as running a command and
waiting for it to end. Use the Start verb to begin asynchronous operations, such as starting an
autonomous process.

Ping vs. Test

Use the Test verb.

<!-- p.1464 -->

Common Verbs
PowerShell uses the System.Management.Automation.VerbsCommon enumeration class to
define generic actions that can apply to almost any cmdlet. The following table lists most of
the defined verbs.

                                                                                              ﾉ    Expand table

 Verb           Action                                                               Synonyms to avoid
 (alias)

 Add ( a )      Adds a resource to a container, or attaches an item to another       Append , Attach ,
                item. For example, the Add-Content cmdlet adds content to a          Concatenate , Insert
                file. This verb is paired with Remove .

 Clear ( cl )   Removes all the resources from a container but doesn't delete        Flush , Erase , Release ,
                the container. For example, the Clear-Content cmdlet removes         Unmark , Unset , Nullify
                the contents of a file but doesn't delete the file.

 Close          Changes the state of a resource to make it inaccessible,
 ( cs )         unavailable, or unusable. This verb is paired with Open.

 Copy ( cp )    Copies a resource to another name or to another container. For       Duplicate , Clone ,
                example, the Copy-Item cmdlet copies an item (such as a file)        Replicate , Sync
                from one location in the data store to another location.

 Enter ( et )   Specifies an action that allows the user to move into a resource.    Push , Into
                For example, the Enter-PSSession cmdlet places the user in an
                interactive session. This verb is paired with Exit .

 Exit ( ex )    Sets the current environment or context to the most recently         Pop , Out
                used context. For example, the Exit-PSSession cmdlet places
                the user in the session that was used to start the interactive
                session. This verb is paired with Enter .

 Find ( fd )    Looks for an object in a container that's unknown, implied,          Search
                optional, or specified.

 Format         Arranges objects in a specified form or layout
 (f)

 Get ( g )      Specifies an action that retrieves a resource. This verb is paired   Read , Open , Cat , Type ,
                with Set .                                                           Dir , Obtain , Dump ,
                                                                                     Acquire , Examine , Find ,
                                                                                     Search

 Hide ( h )     Makes a resource undetectable. For example, a cmdlet whose           Block
                name includes the Hide verb might conceal a service from a
                user. This verb is paired with Show .

<!-- p.1465 -->

Verb          Action                                                              Synonyms to avoid
(alias)

Join ( j )    Combines resources into one resource. For example, the Join-        Combine , Unite , Connect ,
              Path cmdlet combines a path with one of its child paths to          Associate
              create a single path. This verb is paired with Split .

Lock ( lk )   Secures a resource. This verb is paired with Unlock .               Restrict , Secure

Move ( m )    Moves a resource from one location to another. For example,         Transfer , Name , Migrate
              the Move-Item cmdlet moves an item from one location in the
              data store to another location.

New ( n )     Creates a resource. (The Set verb can also be used when             Create , Generate , Build ,
              creating a resource that includes data, such as the Set-Variable    Make , Allocate
              cmdlet.)

Open          Changes the state of a resource to make it accessible, available,
( op )        or usable. This verb is paired with Close .

Optimize      Increases the effectiveness of a resource.
( om )

Pop ( pop )   Removes an item from the top of a stack. For example, the Pop-
              Location cmdlet changes the current location to the location
              that was most recently pushed onto the stack.

Push ( pu )   Adds an item to the top of a stack. For example, the Push-
              Location cmdlet pushes the current location onto the stack.

Redo ( re )   Resets a resource to the state that was undone.

Remove        Deletes a resource from a container. For example, the Remove-       Clear , Cut , Dispose ,
(r)           Variable cmdlet deletes a variable and its value. This verb is      Discard , Erase
              paired with Add .

Rename        Changes the name of a resource. For example, the Rename-Item        Change
( rn )        cmdlet, which is used to access stored data, changes the name
              of an item in the data store.

Reset         Sets a resource back to its original state.
( rs )

Resize        Changes the size of a resource.
( rz )

Search        Creates a reference to a resource in a container.                   Find , Locate
( sr )

Select        Locates a resource in a container. For example, the Select-         Find , Locate
( sc )        String cmdlet finds text in strings and files.

<!-- p.1466 -->

 Verb           Action                                                                Synonyms to avoid
 (alias)

 Set ( s )      Replaces data on an existing resource or creates a resource that       Write , Reset , Assign ,
                contains some data. For example, the Set-Date cmdlet changes           Configure , Update
                the system time on the local computer. (The New verb can also
                be used to create a resource.) This verb is paired with Get .

 Show           Makes a resource visible to the user. This verb is paired with         Display , Produce
 ( sh )         Hide .

 Skip ( sk )    Bypasses one or more resources or points in a sequence.                Bypass , Jump

 Split ( sl )   Separates parts of a resource. For example, the Split-Path             Separate
                cmdlet returns different parts of a path. This verb is paired with
                Join .

 Step ( st )    Moves to the next point or resource in a sequence.

 Switch         Specifies an action that alternates between two resources, such
 ( sw )         as to change between two locations, responsibilities, or states.

 Undo           Sets a resource to its previous state.
 ( un )

 Unlock         Releases a resource that was locked. This verb is paired with          Release , Unrestrict ,
 ( uk )         Lock .                                                                 Unsecure

 Watch          Continually inspects or monitors a resource for changes.
 ( wc )

Communications Verbs
PowerShell uses the System.Management.Automation.VerbsCommunications class to define
actions that apply to communications. The following table lists most of the defined verbs.

                                                                                               ﾉ    Expand table

 Verb (alias)       Action                                                                 Synonyms to avoid

 Connect ( cc )     Creates a link between a source and a destination. This verb is        Join , Telnet , Login
                    paired with Disconnect .

 Disconnect         Breaks the link between a source and a destination. This verb is       Break , Logoff
 ( dc )             paired with Connect .

 Read ( rd )        Acquires information from a source. This verb is paired with           Acquire , Prompt , Get
                     Write .

<!-- p.1467 -->

 Verb (alias)     Action                                                              Synonyms to avoid

 Receive ( rc )   Accepts information sent from a source. This verb is paired with    Read , Accept , Peek
                  Send .

 Send ( sd )      Delivers information to a destination. This verb is paired with     Put , Broadcast ,
                  Receive .                                                           Mail , Fax

 Write ( wr )     Adds information to a target. This verb is paired with Read .       Put , Print

Data Verbs
PowerShell uses the System.Management.Automation.VerbsData class to define actions that
apply to data handling. The following table lists most of the defined verbs.

                                                                                          ﾉ     Expand table

 Verb Name        Action                                                              Synonyms to avoid
 (alias)

 Backup ( ba )    Stores data by replicating it.                                       Save , Burn ,
                                                                                       Replicate , Sync

 Checkpoint       Creates a snapshot of the current state of the data or of its        Diff
 ( ch )           configuration.

 Compare ( cr )   Evaluates the data from one resource against the data from           Diff
                  another resource.

 Compress         Compacts the data of a resource. Pairs with Expand .                 Compact
 ( cm )

 Convert ( cv )   Changes the data from one representation to another when the         Change , Resize ,
                  cmdlet supports bidirectional conversion or when the cmdlet          Resample
                  supports conversion between multiple data types.

 ConvertFrom      Converts one primary type of input (the cmdlet noun indicates        Export , Output , Out
 ( cf )           the input) to one or more supported output types.

 ConvertTo        Converts from one or more types of input to a primary output         Import , Input , In
 ( ct )           type (the cmdlet noun indicates the output type).

 Dismount         Detaches a named entity from a location. This verb is paired with    Unmount , Unlink
 ( dm )           Mount .

 Edit ( ed )      Modifies existing data by adding or removing content.                Change , Update ,
                                                                                       Modify

<!-- p.1468 -->

Verb Name           Action                                                                 Synonyms to avoid
(alias)

Expand ( en )       Restores the data of a resource that has been compressed to its        Explode , Uncompress
                    original state. This verb is paired with Compress .

Export ( ep )       Encapsulates the primary input into a persistent data store, such      Extract , Backup
                    as a file, or into an interchange format. This verb is paired with
                    Import .

Group ( gp )        Arranges or associates one or more resources

Import ( ip )       Creates a resource from data that's stored in a persistent data        BulkLoad , Load
                    store (such as a file) or in an interchange format. For example, the
                     Import-Csv cmdlet imports data from a comma-separated value
                    ( CSV ) file to objects that can be used by other cmdlets. This verb
                    is paired with Export .

Initialize ( in )   Prepares a resource for use, and sets it to a default state.           Erase , Init , Renew ,
                                                                                           Rebuild ,
                                                                                           Reinitialize , Setup

Limit ( l )         Applies constraints to a resource.                                     Quota

Merge ( mg )        Creates a single resource from multiple resources.                     Combine , Join

Mount ( mt )        Attaches a named entity to a location. This verb is paired with        Connect
                    Dismount .

Out ( o )           Sends data out of the environment. For example, the Out-
                    Printer cmdlet sends data to a printer.

Publish ( pb )      Makes a resource available to others. This verb is paired with         Deploy , Release ,
                    Unpublish .                                                            Install

Restore ( rr )      Sets a resource to a predefined state, such as a state set by          Repair , Return ,
                    Checkpoint . For example, the Restore-Computer cmdlet starts a         Undo , Fix
                    system restore on the local computer.

Save ( sv )         Preserves data to avoid loss.

Sync ( sy )         Assures that two or more resources are in the same state.              Replicate , Coerce ,
                                                                                           Match

Unpublish           Makes a resource unavailable to others. This verb is paired with       Uninstall , Revert ,
( ub )              Publish .                                                              Hide

Update ( ud )       Brings a resource up-to-date to maintain its state, accuracy,          Refresh , Renew ,
                    conformance, or compliance. For example, the Update-FormatData         Recalculate , Re-
                    cmdlet updates and adds formatting files to the current                index
                    PowerShell console.

<!-- p.1469 -->

Diagnostic Verbs
PowerShell uses the System.Management.Automation.VerbsDiagnostic class to define actions
that apply to diagnostics. The following table lists most of the defined verbs.

                                                                                              ﾉ    Expand table

 Verb            Action                                                                Synonyms to avoid
 (alias)

 Debug           Examines a resource to diagnose operational problems.                 Diagnose
 ( db )

 Measure         Identifies resources that are consumed by a specified operation,      Calculate , Determine ,
 ( ms )          or retrieves statistics about a resource.                             Analyze

 Ping ( pi )     Deprecated - Use the Test verb instead.

 Repair ( rp )   Restores a resource to a usable condition                             Fix , Restore

 Resolve         Maps a shorthand representation of a resource to a more               Expand , Determine
 ( rv )          complete representation.

 Test ( t )      Verifies the operation or consistency of a resource.                  Diagnose , Analyze ,
                                                                                       Salvage , Verify

 Trace ( tr )    Tracks the activities of a resource.                                  Track , Follow , Inspect ,
                                                                                       Dig

Lifecycle Verbs
PowerShell uses the System.Management.Automation.VerbsLifecycle class to define actions
that apply to the lifecycle of a resource. The following table lists most of the defined verbs.

                                                                                              ﾉ    Expand table

 Verb            Action                                                                 Synonyms to avoid
 (alias)

 Approve         Confirms or agrees to the status of a resource or process.
 ( ap )

 Assert ( as )   Affirms the state of a resource.                                        Certify

 Build ( bd )    Creates an artifact (usually a binary or document) out of some set
                 of input files (usually source code or declarative documents.) This
                 verb was added in PowerShell 6.

<!-- p.1470 -->

Verb             Action                                                                 Synonyms to avoid
(alias)

Complete         Concludes an operation.
( cp )

Confirm          Acknowledges, verifies, or validates the state of a resource or        Acknowledge , Agree ,
( cn )           process.                                                               Certify , Validate ,
                                                                                        Verify

Deny ( dn )      Refuses, objects, blocks, or opposes the state of a resource or        Block , Object ,
                 process.                                                               Refuse , Reject

Deploy           Sends an application, website, or solution to a remote target[s] in
( dp )           such a way that a consumer of that solution can access it after
                 deployment is complete. This verb was added in PowerShell 6.

Disable ( d )    Configures a resource to an unavailable or inactive state. For         Halt , Hide
                 example, the Disable-PSBreakpoint cmdlet makes a breakpoint
                 inactive. This verb is paired with Enable .

Enable ( e )     Configures a resource to an available or active state. For example,    Start , Begin
                 the Enable-PSBreakpoint cmdlet makes a breakpoint active. This
                 verb is paired with Disable .

Install ( is )   Places a resource in a location, and optionally initializes it. This   Setup
                 verb is paired with Uninstall .

Invoke ( i )     Performs an action, such as running a command or a method.             Run , Start

Register         Creates an entry for a resource in a repository such as a database.
( rg )           This verb is paired with Unregister .

Request          Asks for a resource or asks for permissions.
( rq )

Restart ( rt )   Stops an operation and then starts it again. For example, the          Recycle
                 Restart-Service cmdlet stops and then starts a service.

Resume           Starts an operation that has been suspended. For example, the
( ru )           Resume-Service cmdlet starts a service that has been suspended.
                 This verb is paired with Suspend .

Start ( sa )     Initiates an operation. For example, the Start-Service cmdlet          Launch , Initiate ,
                 starts a service. This verb is paired with Stop .                      Boot

Stop ( sp )      Discontinues an activity. This verb is paired with Start .             End , Kill , Terminate ,
                                                                                        Cancel

Submit           Presents a resource for approval.                                      Post
( sb )

<!-- p.1471 -->

 Verb             Action                                                                 Synonyms to avoid
 (alias)

 Suspend          Pauses an activity. For example, the Suspend-Service cmdlet              Pause
 ( ss )           pauses a service. This verb is paired with Resume .

 Uninstall        Removes a resource from an indicated location. This verb is
 ( us )           paired with Install .

 Unregister       Removes the entry for a resource from a repository. This verb is         Remove
 ( ur )           paired with Register .

 Wait ( w )       Pauses an operation until a specified event occurs. For example,         Sleep , Pause
                  the Wait-Job cmdlet pauses operations until one or more of the
                  background jobs are complete.

Security Verbs
PowerShell uses the System.Management.Automation.VerbsSecurity class to define actions that
apply to security. The following table lists most of the defined verbs.

                                                                                                ﾉ     Expand table

 Verb (alias)     Action                                                                      Synonyms to
                                                                                              avoid

 Block ( bl )     Restricts access to a resource. This verb is paired with Unblock .           Prevent , Limit ,
                                                                                               Deny

 Grant ( gr )     Allows access to a resource. This verb is paired with Revoke .               Allow , Enable

 Protect ( pt )   Safeguards a resource from attack or loss. This verb is paired with          Encrypt ,
                  Unprotect .                                                                  Safeguard , Seal

 Revoke ( rk )    Specifies an action that doesn't allow access to a resource. This verb       Remove , Disable
                  is paired with Grant .

 Unblock          Removes restrictions to a resource. This verb is paired with Block .         Clear , Allow
 ( ul )

 Unprotect        Removes safeguards from a resource that were added to prevent it             Decrypt , Unseal
 ( up )           from attack or loss. This verb is paired with Protect .

Other Verbs

<!-- p.1472 -->

PowerShell uses the System.Management.Automation.VerbsOther class to define canonical
verb names that don't fit into a specific verb name category such as the common,
communications, data, lifecycle, or security verb names verbs.

                                                                             ﾉ     Expand table

 Verb (alias)       Action                                           Synonyms to avoid

 Use ( u )          Uses or includes a resource to do something.

See Also
      System.Management.Automation.VerbsCommon
      System.Management.Automation.VerbsCommunications
      System.Management.Automation.VerbsData
      System.Management.Automation.VerbsDiagnostic
      System.Management.Automation.VerbsLifecycle
      System.Management.Automation.VerbsSecurity
      System.Management.Automation.VerbsOther
      Cmdlet Declaration
      Windows PowerShell Shell SDK

 Last updated on 03/30/2026

<!-- p.1473 -->

Cmdlet Input Processing Methods
Cmdlets must override one or more of the input processing methods described in this topic to
perform their work. These methods allow the cmdlet to perform operations of pre-processing,
input processing, and post-processing. These methods also allow you to stop cmdlet
processing. For a more detailed example of how to use these methods, see SelectStr Tutorial.

Pre-Processing Operations
Cmdlets should override the System.Management.Automation.Cmdlet.BeginProcessing method
to add any preprocessing operations that are valid for all the records that will be processed
later by the cmdlet. When PowerShell processes a command pipeline, PowerShell calls this
method once for each instance of the cmdlet in the pipeline. For more information about how
PowerShell invokes the command pipeline, see Cmdlet Processing Lifecycle.

The following code shows an implementation of the BeginProcessing method.

  C#

  protected override void BeginProcessing()
  {
    // Replace the WriteObject method with the logic required by your cmdlet.
    WriteObject("This is a test of the BeginProcessing template.");
  }

Input Processing Operations
Cmdlets can override the System.Management.Automation.Cmdlet.ProcessRecord method to
process the input that is sent to the cmdlet. When PowerShell processes a command pipeline,
PowerShell calls this method for each input record that is processed by the cmdlet. For more
information about how PowerShell invokes the command pipeline, see Cmdlet Processing
Lifecycle.

The following code shows an implementation of the ProcessRecord method.

  C#

  protected override void ProcessRecord()
  {
    // Replace the WriteObject method with the logic required by your cmdlet.

<!-- p.1474 -->

      WriteObject("This is a test of the ProcessRecord template.");
  }

Post-Processing Operations
Cmdlets should override the System.Management.Automation.Cmdlet.EndProcessing method
to add any post-processing operations that are valid for all the records that were processed by
the cmdlet. For example, your cmdlet might have to clean up object variables after it is finished
processing.

When PowerShell processes a command pipeline, PowerShell calls this method once for each
instance of the cmdlet in the pipeline. However, it is important to remember that the
PowerShell runtime will not call the EndProcessing method if the cmdlet is canceled midway
through its input processing or if a terminating error occurs in any part of the cmdlet. For this
reason, a cmdlet that requires object cleanup should implement the complete
System.IDisposable pattern, including a finalizer, so that the runtime can call both the
EndProcessing and System.IDisposable.Dispose methods at the end of processing. For more
information about how PowerShell invokes the command pipeline, see Cmdlet Processing
Lifecycle.

The following code shows an implementation of the EndProcessing method.

  C#

  protected override void EndProcessing()
  {
    // Replace the WriteObject method with the logic required by your cmdlet.
    WriteObject("This is a test of the EndProcessing template.");
  }

See Also
System.Management.Automation.Cmdlet.BeginProcessing

System.Management.Automation.Cmdlet.ProcessRecord

System.Management.Automation.Cmdlet.EndProcessing

SelectStr Tutorial

System.IDisposable

<!-- p.1475 -->

Windows PowerShell Shell SDK

Last updated on 05/20/2025

<!-- p.1476 -->

Cmdlet Parameters
Cmdlet parameters provide the mechanism that allows a cmdlet to accept input. Parameters
can accept input directly from the command line, or from objects passed to the cmdlet
through the pipeline, The arguments (also known as values) of these parameters can specify
the input that the cmdlet accepts, how the cmdlet should perform its actions, and the data that
the cmdlet returns to the pipeline.

In This Section
Declaring Properties as Parameters Provides basic information you must understand before
you declare the parameters of a cmdlet.

Types of Cmdlet Parameters Describes the different types of parameters that you can declare in
cmdlets.

Cmdlet Parameter Name and Functionality Guidelines Discusses the names, recommended
data type, and functionality of standard parameters.

Parameter Aliases Discusses the aliases that you can define for parameters.

Common Parameter Names This topic describes the parameters that Windows PowerShell adds
to cmdlets.

Cmdlet Parameter Sets Discusses how parameter sets enable you to write a single cmdlet that
can perform different actions for different scenarios.

Cmdlet Dynamic Parameters Discusses parameters that are available to the user under special
conditions.

Supporting Wildcard Characters in Cmdlet Parameters Describes how to provide support for
wildcard characters when you design a cmdlet that will be run against a group of resources.

Validating Parameter Input Describes how Windows PowerShell validates the arguments passed
to cmdlet parameters.

Input Filter Parameters Discusses the Filter , Include , and Exclude parameters that filter the
set of input objects that the cmdlet affects.

<!-- p.1477 -->

Related Sections
How to Validate Parameter Input

See Also
Parameter Attribute Declaration

Windows PowerShell Cmdlets

Last updated on 05/20/2025

<!-- p.1478 -->

Declaring Properties as Parameters
This topic provides basic information you must understand before you declare the parameters
of a cmdlet.

To declare the parameters of a cmdlet within your cmdlet class, define the public properties
that represent each parameter, and then add one or more Parameter attributes to each
property. The Windows PowerShell runtime uses the Parameter attributes to identify the
property as a cmdlet parameter. The basic syntax for declaring the Parameter attribute is
[Parameter()] .

Here is an example of a property defined as a required parameter.

 C#

 [Parameter(Position = 0, Mandatory = true)]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;

Here are some things to remember about parameters.

      A parameter must be explicitly marked as public. Parameters that are not marked as
      public default to internal and will not be found by the Windows PowerShell runtime.

      Parameters should be defined as Microsoft .NET Framework types to provide better
      parameter validation. For example, parameters that are restricted to one value out of a set
      of values should be defined as an enumeration type. Parameters that take a Uniform
      Resource Identifier (URI) value should be of type System.Uri.

      Avoid basic string parameters for all but free-form text properties.

      You can add a parameter to any number of parameter sets. For more information about
      parameter sets, see Cmdlet Parameter Sets.

Windows PowerShell also provides a set of common parameters that are automatically
available to every cmdlet. For more information about these parameters and their aliases, see
Cmdlet Common Parameters.

<!-- p.1479 -->

See Also
Cmdlet Common Parameters

Types of Cmdlet Parameter

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1480 -->

Types of Cmdlet Parameters
This topic describes the different types of parameters that you can declare in cmdlets. Cmdlet
parameters can be positional, named, required, optional, or [switch] parameters.

Positional and Named Parameters
All cmdlet parameters are either named or positional parameters. A named parameter requires
that you type the parameter name and argument when calling the cmdlet. A positional
parameter requires only that you type the arguments in relative order. The system then maps
the first unnamed argument to the first positional parameter. The system maps the second
unnamed argument to the second unnamed parameter, and so on. By default, all cmdlet
parameters are named parameters.

To define a named parameter, omit the Position keyword in the Parameter attribute
declaration, as shown in the following parameter declaration.

 C#

 [Parameter(ValueFromPipeline=true)]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;

To define a positional parameter, add the Position keyword in the Parameter attribute
declaration, and then specify a position. In the following sample, the UserName parameter is
declared as a positional parameter with position 0. This means that the first argument of the
call is automatically bound to this parameter.

 C#

 [Parameter(Position = 0)]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;
