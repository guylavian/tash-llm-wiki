---
title: "How to use this documentation — pages 1481-1520"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1481-1520
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1481-1520
family: powershell
documentKind: "doc"
abstract: "７ Note Good cmdlet design recommends that the most-used parameters be declared as positional parameters so that the user doesn't have to enter the parameter name when the cmdlet is run. Positional and named parameters accept single arguments or multiple arguments separated by co"
---

# How to use this documentation — pages 1481-1520

<!-- p.1481 -->

  ７ Note

  Good cmdlet design recommends that the most-used parameters be declared as
  positional parameters so that the user doesn't have to enter the parameter name when
  the cmdlet is run.

Positional and named parameters accept single arguments or multiple arguments separated by
commas. Multiple arguments are allowed only if the parameter accepts a collection such as an
array of strings. You may mix positional and named parameters in the same cmdlet. In this case,
the system retrieves the named arguments first, and then attempts to map the remaining
unnamed arguments to the positional parameters.

The following commands show the different ways in which you can specify single and multiple
arguments for the parameters of the Get-Command cmdlet. Notice that in the last two samples, -
Name doesn't need to be specified because the Name parameter is defined as a positional

parameter.

 PowerShell

 Get-Command -Name Get-Service
 Get-Command -Name Get-Service,Set-Service
 Get-Command Get-Service
 Get-Command Get-Service,Set-Service

Mandatory and Optional Parameters
You can also define cmdlet parameters as mandatory or optional parameters. (A mandatory
parameter must be specified before the PowerShell runtime invokes the cmdlet.) By default,
parameters are defined as optional.

To define a mandatory parameter, add the Mandatory keyword in the Parameter attribute
declaration, and set it to true , as shown in the following parameter declaration.

 C#

 [Parameter(Position = 0, Mandatory = true)]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }

<!-- p.1482 -->

 }
 private string userName;

To define an optional parameter, omit the Mandatory keyword in the Parameter attribute
declaration, as shown in the following parameter declaration.

 C#

 [Parameter(Position = 0)]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;

[switch] parameters
PowerShell provides a System.Management.Automation.SwitchParameter type that allows you
to define a parameter whose default value false unless the parameter is specified when the
cmdlet is called. Whenever possible, use [switch] parameters instead of Boolean parameters.

Consider the following example. Many PowerShell cmdlets return output. However, these
cmdlets have a PassThru [switch] parameter that overrides the default behavior. When you
use the PassThru parameter, the cmdlet returns output objects to the pipeline.

The following sample shows how to define a [switch] parameter:

 C#

 [Parameter()]
 public SwitchParameter GoodBye
 {
   get { return goodbye; }
   set { goodbye = value; }
 }
 private bool goodbye;

To make the cmdlet act on the parameter when it's specified, use the following structure within
one of the input processing methods.

 C#

 protected override void ProcessRecord()
 {

<!-- p.1483 -->

    WriteObject("Switch parameter test: " + userName + ".");
    if (goodbye)
    {
      WriteObject(" Goodbye!");
    }
  } // End ProcessRecord

By default, [switch] parameters are excluded from positional parameters. You can override
that in the Parameter attribute, but it can confuse users.

Design [switch] parameters so that using the parameter changes the default behavior of the
command to a less common or more complicated mode. The simplest behavior of a command
should be the default behavior that doesn't require the use of [switch] parameters. Base the
behavior controlled by the [switch] parameter on the value of the parameter, not its presence.

There are several ways to test for the presence of a [switch] parameter:

      MyInvocation.BoundParameters contains the [switch] parameter name as a key

      PSCmdlet.ParameterSetName when the [switch] parameter defines a unique parameter set

For example, it's possible to provide an explicit value for the switch using -MySwitch:$false or
splatting. If you only test for the presence of the parameter, the command behaves as if the
switch value is $true instead of $false .

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 04/08/2026

<!-- p.1484 -->

Standard Cmdlet Parameter Names and
Types
Cmdlet parameter names should be consistent across the cmdlets that you design. The
following topics list the parameter names that we recommend you use when you declare
cmdlet parameters. The topics also describe the recommended data type and functionality of
each parameter.

In This Section
Activity Parameters

Date and Time Parameters

Format Parameters

Property Parameters

Quantity Parameters

Resource Parameters

Security Parameters

Last updated on 05/20/2025

<!-- p.1485 -->

Activity Parameters
The following table lists the recommended names and functionality for activity parameters.

                                                                                        ﾉ   Expand table

 Parameter               Functionality

 Append                  Implement this parameter so that the user can add content to the end of a
 Data type:              resource when the parameter is specified.
 SwitchParameter

 CaseSensitive           Implement this parameter so the user can require case sensitivity when the
 Data type:              parameter is specified.
 SwitchParameter

 Command                 Implement this parameter so the user can specify a command string to run.
 Data type: String

 CompatibleVersion       Implement this parameter so the user can specify the semantics that the cmdlet
 Data type:              must be compatible with for compatibility with previous versions.
 System.Version object

 Compress                Implement this parameter so that data compression is used when the parameter
 Data type:              is specified.
 SwitchParameter

 CompressionLevel        Implement this parameter so that the user can specify the algorithm to use for
 Data type: Keyword      data compression.

 Continuous              Implement this parameter so that data is processed until the user terminates the
 Data type:              cmdlet when the parameter is specified. If the parameter is not specified, the
 SwitchParameter         cmdlet processes a predefined amount of data and then terminates the
                         operation.

 Create                  Implement this parameter to indicate that a resource is created if one does not
 Data type:              already exist when the parameter is specified.
 SwitchParameter

 Delete                  Implement this parameter so that resources are deleted when the cmdlet has
 Data type:              completed its operation when the parameter is specified.
 SwitchParameter

 Drain                   Implement this parameter to indicate that outstanding work items are processed
 Data type:              before the cmdlet processes new data when the parameter is specified. If the
 SwitchParameter         parameter is not specified, the work items are processed immediately.

<!-- p.1486 -->

Parameter              Functionality

Erase                  Implement this parameter so that the user can specify the number of times a
Data type: Int32       resource is erased before it is deleted.

ErrorLevel             Implement this parameter so that the user can specify the level of errors to
Data type: Int32       report.

Exclude                Implement this parameter so that the user can exclude something from an
Data type: String[]    activity. For more information about how to use input filters, see Input Filter
                       Parameters.

Filter                 Implement this parameter so that the user can specify a filter that selects the
Data type: Keyword     resources upon which to perform the cmdlet action. For more information about
                       how to use input filters, see Input Filter Parameters.

Follow                 Implement this parameter so that progress is tracked when the parameter is
Data type:             specified.
SwitchParameter

Force                  Implement this parameter to indicate that the user can perform an action even if
Data type:             restrictions are encountered when the parameter is specified. The parameter
SwitchParameter        does not allow security to be compromised. For example, this parameter lets a
                       user overwrite a read-only file.

Include                Implement this parameter so that the user can include something in an activity.
Data type: String[]    For more information about how to use input filters, see Input Filter Parameters.

Incremental            Implement this parameter to indicate that processing is performed incrementally
Data type:             when the parameter is specified. For example, this parameter lets a user perform
SwitchParameter        incremental backups that back up files only since the last backup.

InputObject            Implement this parameter when the cmdlet takes input from other cmdlets.
Data type: Object      When you define an InputObject parameter, always specify the
                       ValueFromPipeline keyword when you declare the Parameter attribute. For
                       more information about using input filters, see Input Filter Parameters.

Insert                 Implement this parameter so that the cmdlet inserts an item when the parameter
Data type:             is specified.
SwitchParameter

Interactive            Implement this parameter so that the cmdlet works interactively with the user
Data type:             when the parameter is specified.
SwitchParameter

Interval               Implement this parameter so that the user can specify a hash table of keywords
Data type: HashTable   that contains the values. The following example shows sample values for the
                       Interval parameter: -interval @{ResumeScan=15; Retry=3} .

Log                    Implement this parameter audit the actions of the cmdlet when the parameter is
Data type:             specified.

<!-- p.1487 -->

Parameter            Functionality

SwitchParameter

NoClobber            Implement this parameter so that the resource will not be overwritten when the
Data type:           parameter is specified. This parameter generally applies to cmdlets that create
SwitchParameter      new objects so that they can be prevented from overwriting existing objects with
                     the same name.

Notify               Implement this parameter so that the user will be notified that the activity is
Data type:           complete when the parameter is specified.
SwitchParameter

NotifyAddress        Implement this parameter so that the user can specify the e-mail address to use
Data type: Email     to send a notification when the Notify parameter is specified.
address

Overwrite            Implement this parameter so that the cmdlet overwrites any existing data when
Data type:           the parameter is specified.
SwitchParameter

Prompt               Implement this parameter so that the user can specify a prompt for the cmdlet.
Data type: String

Quiet                Implement this parameter so that the cmdlet suppresses user feedback during
Data type:           its actions when the parameter is specified.
SwitchParameter

Recurse              Implement this parameter so that the cmdlet recursively performs its actions on
Data type:           resources when the parameter is specified.
SwitchParameter

Repair               Implement this parameter so that the cmdlet will attempt to correct something
Data type:           from a broken state when the parameter is specified.
SwitchParameter

RepairString         Implement this parameter so that the user can specify a string to use when the
Data type: String    Repair parameter is specified.

Retry                Implement this parameter so the user can specify the number of times the
Data type: Int32     cmdlet will attempt an action.

Select               Implement this parameter so that the user can specify an array of the types of
Data type: Keyword   items.
array

Stream               Implement this parameter so the user can stream multiple output objects
Data type:           through the pipeline when the parameter is specified.
SwitchParameter

Strict               Implement this parameter so that all errors are handled as terminating errors
Data type:           when the parameter is specified.

<!-- p.1488 -->

 Parameter                   Functionality

 SwitchParameter

 TempLocation                Implement this parameter so the user can specify the location of temporary data
 Data type: String           that is used during the operation of the cmdlet.

 Timeout                     Implement this parameter so that the user can specify the timeout interval (in
 Data type: Int32            milliseconds).

 Truncate                    Implement this parameter so that the cmdlet will truncate its actions when the
 Data type:                  parameter is specified. If the parameter is not specified, the cmdlet performs
 SwitchParameter             another action.

 Verify                      Implement this parameter so that the cmdlet will test to determine whether an
 Data type:                  action has occurred when the parameter is specified.
 SwitchParameter

 Wait                        Implement this parameter so that the cmdlet will wait for user input before
 Data type:                  continuing when the parameter is specified.
 SwitchParameter

 WaitTime                    Implement this parameter so that the user can specify the duration (in seconds)
 Data type: Int32            that the cmdlet will wait for user input when the Wait parameter is specified.

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1489 -->

Date and Time Parameters
The following table lists recommended names and functionality for parameters that handle
date and time information. Date and time parameters are typically used to record when
something is created or accessed.

                                                                                      ﾉ   Expand table

 Parameter          Functionality

 Accessed           Implement this parameter so that when it is specified the cmdlet will operate on the
 Data type:         resources that have been accessed based on the date and time specified by the
 SwitchParameter    Before and After parameters. If this parameter is specified, the Created and
                    Modified parameters must be not be specified.

 After              Implement this parameter to specify the date and time after which the cmdlet was
 Data type:         used. For the After parameter to work, the cmdlet must also have an Accessed,
 DateTime           Created, or Modified parameter. And, that parameter must be set to true when the
                    cmdlet is called.

 Before             Implement this parameter to specify the date and time before which the cmdlet was
 Data type:         used. For the Before parameter to work, the cmdlet must also have an Accessed,
 DateTime           Created, or Modified parameter. And, that parameter must be set to true when the
                    cmdlet is called.

 Created            Implement this parameter so that when it is specified the cmdlet will operate on the
 Data type:         resources that have been created based on the date and time specified by the
 SwitchParameter    Before and After parameters. If this parameter is specified, the Accessed and
                    Modified parameters must not be specified.

 Exact              Implement this parameter so that when it is specified the resource term must match
 Data type:         the resource name exactly. When the parameter is not specified the resource term
 SwitchParameter    and name do not need to match exactly.

 Modified           Implement this parameter so that when it is specified the cmdlet will operate on
 Data type:         resources that have been changed based on the date and time specified by the
 DateTime           Before and After parameters. If this parameter is specified, the Accessed and
                    Created parameters must not be specified.

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

<!-- p.1490 -->

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1491 -->

Format Parameters
The following table lists recommended names and functionality for parameters that are used to
format or to generate data.

                                                                                        ﾉ   Expand table

 Parameter              Functionality

 As                     Implement this parameter to specify the cmdlet output format. For example,
 Data type: Keyword     possible values could be Text or Script.

 Binary                 Implement this parameter to indicate that the cmdlet handles binary values.
 Data type:
 SwitchParameter

 Encoding               Implement this parameter to specify the type of encoding that is supported. For
 Data type: Keyword     example, possible values could be ASCII, UTF8, Unicode, UTF7, BigEndianUnicode,
                        Byte, and String.

 NewLine                Implement this parameter so that the newline characters are supported when the
 Data type:             parameter is specified.
 SwitchParameter

 ShortName              Implement this parameter so that short names are supported when the parameter
 Data type:             is specified.
 SwitchParameter

 Width                  Implement this parameter so that the user can specify the width of the output
 Data type: Int32       device.

 Wrap                   Implement this parameter so that text wrapping is supported when the parameter
 Data type:             is specified.
 SwitchParameter

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1492 -->

Property Parameters
The following table lists the recommended names and functionality for property parameters.

                                                                                      ﾉ   Expand table

 Parameter             Functionality

 Count                 Implement this parameter so that the user can specify the number of objects to
 Data type: Int32      be processed.

 Description           Implement this parameter so that the user can specify a description for a
 Data type: String     resource.

 From                  Implement this parameter so that the user can specify the reference object to
 Data type: String     get information from.

 Id                    Implement this parameter so that the user can specify the identifier of a
 Data type: Resource   resource.
 dependent

 Input                 Implement this parameter so that the user can specify the input file
 Data type: String     specification.

 Location              Implement this parameter so that the user can specify the location of the
 Data type: String     resource.

 LogName               Implement this parameter so that the user can specify the name of the log file
 Data type: String     to process or use.

 Name                  Implement this parameter so that the user can specify the name of the resource.
 Data type: String

 Output                Implement this parameter so that the user can specify the output file.
 Data type: String

 Owner                 Implement this parameter so that the user can specify the name of the owner of
 Data type: String     the resource.

 Property              Implement this parameter so that the user can specify the name or the names of
 Data type: String     the properties to use.

 Reason                Implement this parameter so that the user can specify why this cmdlet is being
 Data type: String     invoked.

 Regex                 Implement this parameter so that regular expressions are used when the
 Data type:            parameter is specified. When this parameter is specified, wildcard characters are
 SwitchParameter       not resolved.

<!-- p.1493 -->

 Parameter                   Functionality

 Speed                       Implement this parameter so that the user can specify the baud rate. The user
 Data type: Int32            sets this parameter to the speed of the resource.

 State                       Implement this parameter so that the user can specify the names of states, such
 Data type: Keyword          as KEYDOWN.
 array

 Value                       Implement this parameter so that the user can specify a value to provide to the
 Data type: Object           cmdlet.

 Version                     Implement this parameter so that the user can specify the version of the
 Data type: String           property.

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1494 -->

Quantity Parameters
The following table lists the recommended names and functionality for quantity parameters.

                                                                                           ﾉ   Expand table

 Parameter        Functionality

 All              Implement this parameter so that true indicates that all resources should be acted
 Data type:       upon instead of a default subset of resources. Implement this parameter so that false
 Boolean          indicates a subset of the resources.

 Allocation       Implement this parameter so that the user can specify the number of items to allocate.
 Data type:
 Int32

 BlockCount       Implement this parameter so that the user can specify the block count.
 Data type:
 Int64

 Count            Implement this parameter so that the user can specify the count.
 Data type:
 Int64

 Scope            Implement this parameter so that the user can specify the scope to operate on.
 Data type:
 Keyword

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1495 -->

Resource Parameters
The following table lists the recommended names and functionality for resource parameters.
For these parameters, the resources could be the assembly that contains the cmdlet class or
the host application that is running the cmdlet.

                                                                                        ﾉ   Expand table

 Parameter      Functionality

 Application    Implement this parameter so that the user can specify an application.
 Data type:
 String

 Assembly       Implement this parameter so that the user can specify an assembly.
 Data type:
 String

 Attribute      Implement this parameter so that the user can specify an attribute.
 Data type:
 String

 Class          Implement this parameter so that the user can specify a Microsoft .NET Framework class.
 Data type:
 String

 Cluster        Implement this parameter so that the user can specify a cluster.
 Data type:
 String

 Culture        Implement this parameter so that the user can specify the culture in which to run the
 Data type:     cmdlet.
 String

 Domain         Implement this parameter so that the user can specify the domain name.
 Data type:
 String

 Drive          Implement this parameter so that the user can specify a drive name.
 Data type:
 String

 Event          Implement this parameter so that the user can specify an event name.
 Data type:
 String

<!-- p.1496 -->

Parameter          Functionality

Interface          Implement this parameter so that the user can specify a network interface name.
Data type:
String

IpAddress          Implement this parameter so that the user can specify an IP address.
Data type:
String

Job                Implement this parameter so that the user can specify a job.
Data type:
String

LiteralPath        Implement this parameter so that the user can specify the path to a resource when
Data type:         wildcard characters are not supported. (Use the Path parameter when wildcard
String             characters are supported.)

Mac                Implement this parameter so that the user can specify a media access controller (MAC)
Data type:         address.
String

ParentId           Implement this parameter so that the user can specify the parent identifier.
Data type:
String

Path               Implement this parameter so that the user can indicate the paths to a resource when
Data type:         wildcard characters are supported. (Use the LiteralPath parameter when wildcard
String, String[]   characters are not supported.) We recommend that you develop this parameter so that it
                   supports the full provider:path syntax used by providers. We also recommend that you
                   develop it so that it works with as many providers as possible.

Port               Implement this parameter so that the user can specify an integer value for networking or
Data type:         a string value such as "biztalk" for other types of port.
Integer, String

Printer            Implement this parameter so that the user can specify the printer for the cmdlet to use.
Data type:
Integer, String

Size               Implement this parameter so that the user can specify a size.
Data type:
Int32

TID                Implement this parameter so that the user can specify a transaction identifier (TID) for
Data type:         the cmdlet.
String

Type               Implement this parameter so that the user can specify the type of resource on which to
Data type:         operate.
String

<!-- p.1497 -->

 Parameter       Functionality

 URL             Implement this parameter so that the user can specify a Uniform Resource Locator (URL).
 Data type:
 String

 User            Implement this parameter so that the user can specify their name or the name of another
 Data type:      user.
 String

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1498 -->

Security Parameters
The following table lists the recommended names and functionality for parameters used to
provide security information for an operation, such as parameters that specify certificate key
and privilege information.

                                                                                      ﾉ    Expand table

 Parameter                                     Functionality

 ACL                                           Implement this parameter to specify the access
 Data type: String                             control level of protection for a catalog or for a
                                               Uniform Resource Identifier (URI).

 CertFile                                      Implement this parameter so that the user can specify
 Data type: String                             the name of a file that contains one of the following:
                                               - A Base64 or Distinguished Encoding Rules (DER)
                                               encoded x.509 certificate
                                               - A Public Key Cryptography Standards (PKCS) #12 file
                                               that contains at least one certificate and key

 CertIssuerName                                Implement this parameter so that the user can specify
 Data type: String                             the name of the issuer of a certificate or so that the
                                               user can specify a substring.

 CertRequestFile                               Implement this parameter to specify the name of a file
 Data type: String                             that contains a Base64 or DER-encoded PKCS #10
                                               certificate request.

 CertSerialNumber                              Implement this parameter to specify the serial
 Data type: String                             number that was issued by the certification authority.

 CertStoreLocation                             Implement this parameter so that the user can specify
 Data type: String                             the location of the certificate store. The location is
                                               typically a file path.

 CertSubjectName                               Implement this parameter so that the user can specify
 Data type: String                             the issuer of a certificate or so that the user can
                                               specify a substring.

 CertUsage                                     Implement this parameter to specify the key usage or
 Data type: String                             the enhanced key usage. The key can be represented
                                               as a bit mask, a bit, an object identifier (OID), or a
                                               string.

 Credential                                    Implement this parameter so that the cmdlet will
 Data type:                                    automatically prompt the user for a user name or

<!-- p.1499 -->

Parameter                                   Functionality

System.Management.Automation.PSCredential   password. A prompt for both is displayed if a full
                                            credential is not supplied directly.

CSPName                                     Implement this parameter so that the user can specify
Data type: String                           the name of the certificate service provider (CSP).

CSPType                                     Implement this parameter so that the user can specify
Data type: Integer                          the type of CSP.

Group                                       Implement this parameter so that the user can specify
Data type: String                           a collection of principals for access. For more
                                            information, see the description of the Principal
                                            parameter.

KeyAlgorithm                                Implement this parameter so that the user can specify
Data type: String                           the key generation algorithm to use for security.

KeyContainerName                            Implement this parameter so that the user can specify
Data type: String                           the name of the key container.

KeyLength                                   Implement this parameter so that the user can specify
Data type: Integer                          the length of the key in bits.

Operation                                   Implement this parameter so that the user can specify
Data type: String                           an action that can be performed on a protected
                                            object.

Principal                                   Implement this parameter so that the user can specify
Data type: String                           a unique identifiable entity for access.

Privilege                                   Implement this parameter so that the user can specify
Data type: String, String[]                 the rights a cmdlet needs to perform an operation for
                                            a particular entity.

Role                                        Implement this parameter so that the user can specify
Data type: String                           a set of operations that can be performed by an
                                            entity.

SaveCred                                    Implement this parameter so that credentials that
Data type: SwitchParameter                  were previously saved by the user will be used when
                                            the parameter is specified.

Scope                                       Implement this parameter so that the user can specify
Data type: String                           the group of protected objects for the cmdlet.

SID                                         Implement this parameter so that the user can specify
Data type: String                           a unique identifier that represents a principal.

Trusted                                     Implement this parameter so that trust levels are
Data type: SwitchParameter                  supported when the parameter is specified.

<!-- p.1500 -->

 Parameter                            Functionality

 TrustLevel                           Implement this parameter so that the user can specify
 Data type: Keyword                   the trust level that is supported. For example, possible
                                      values include internet, intranet, and fulltrust.

See Also
Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1501 -->

Parameter Aliases
Cmdlet parameters can also have aliases. You can use the aliases instead of the parameter
names when you type or specify the parameter in a command.

Benefits of Using Aliases
Adding aliases to parameters provides the following benefits.

      You can provide a shortcut so that the user does not have to use the complete parameter
      name when the cmdlet is called. For example, you could use the "CN" alias instead of the
      parameter name "ComputerName".

      You can define multiple aliases if you want to provide different names for the same
      parameter. You might want to define multiple aliases if you have to work with multiple
      user groups that refer to the same data in different ways.

      You can provide backwards compatibility for existing scripts if the name of a parameter
      changes.

      By using the Alias attribute along with the ValueFromPipelineByName attribute, you can
      define a parameter that allows your cmdlet to bind to different object types. For example,
      say you had two objects of different types and the first object had a writer property and
      the second object had an editor property. If your cmdlet had a parameter that had writer
      and editor aliases and the cmdlet accepted pipeline input based in property names, your
      cmdlet could bind to both objects using the two parameter aliases.

For more information about aliases that can be used with specific parameters, see Common
Parameter Names.

Defining Parameter Aliases
To define an alias for a parameter, declare the Alias attribute, as shown in the following
parameter declaration. In this example, multiple aliases are defined for the same parameter.
(For more information, seeHow to Declare Cmdlet Parameters.)

 C#

<!-- p.1502 -->

 [Alias("UN","Writer","Editor")]
 [Parameter()]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;

See Also
Common Parameter Names

How to Declare Cmdlet Parameters

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1503 -->

Common Parameter Names
The parameters described in this topic are referred to as common parameters. They're added
to cmdlets by the PowerShell runtime and can't be declared by the cmdlet.

  ７ Note

  These parameters are also added to provider cmdlets and to functions that are decorated
  with the CmdletBinding attribute.

General Common Parameters
The following parameters are added to all cmdlets and can be accessed whenever the cmdlet is
run. These parameters are defined by the CommonParameters class.

Debug (alias: db)
Data type: SwitchParameter

This parameter specifies whether programmer-level debugging messages that can be
displayed at the command line. These messages are intended for troubleshooting the
operation of the cmdlet, and are generated by calls to the WriteDebug method. Debug
messages don't need to be localized.

ErrorAction (alias: ea)
Data type: Enumeration

This parameter specifies what action should take place when an error occurs. The possible
values for this parameter are defined by the ActionPreference enumeration.

ErrorVariable (alias: ev)
Data type: String

This parameter specifies the variable in which to place objects when an error occurs. To append
to this variable, use +varname rather than clearing and setting the variable.

<!-- p.1504 -->

InformationAction (alias: infa)
Data type: Enumeration

This parameter specifies what action should take place when output is sent to the Information
stream. The possible values for this parameter are defined by the ActionPreference
enumeration.

InformationVariable (alias: iv)
Data type: String

This parameter specifies the variable in which to save output objects written to the Information
stream. To append to this variable, use +varname rather than clearing and setting the variable.

OutBuffer (alias: ob)
Data type: Int32

This parameter defines the number of objects to store in the output buffer before any objects
are passed down the pipeline. By default, objects are passed immediately down the pipeline.

OutVariable (alias: ov)
Data type: String

This parameter specifies the variable in which to place all output objects generated by the
cmdlet. To append to this variable, use +varname rather than clearing and setting the variable.

PipelineVariable (alias: pv)
Data type: String

This parameter stores the value of the current pipeline element as a variable for any named
command as it flows through the pipeline.

ProgressAction (alias: proga)
Data type: Enumeration

Determines how PowerShell responds to progress updates generated by a script, cmdlet, or
provider, such as the progress bars generated by the Write-Progress cmdlet.

<!-- p.1505 -->

This parameter was added in PowerShell 7.4.

Verbose (alias: vb)
Data type: SwitchParameter

This parameter specifies whether the cmdlet writes explanatory messages that can be displayed
at the command line. These messages are intended to provide additional help to the user, and
are generated by calls to the WriteVerbose method.

WarningAction (alias: wa)
Data type: Enumeration

This parameter specifies what action should take place when the cmdlet writes a warning
message. The possible values for this parameter are defined by the ActionPreference
enumeration.

WarningVariable (alias: wv)
Data type: String

This parameter specifies the variable in which warning messages can be saved. To append to
this variable, use +varname rather than clearing and setting the variable.

Risk-Mitigation Parameters
The following parameters are added to cmdlets that requests confirmation before they perform
their action. For more information about confirmation requests, see Requesting Confirmation.
These parameters are defined by the ShouldProcessParameters class.

Confirm (alias: cf)
Data type: SwitchParameter

This parameter specifies whether the cmdlet displays a prompt that asks if the user is sure that
they want to continue.

WhatIf (alias: wi)
Data type: SwitchParameter

<!-- p.1506 -->

This parameter specifies whether the cmdlet writes a message that describes the effects of
running the cmdlet without actually performing any action.

Transaction Parameters
The following parameter is added to cmdlets that support transactions. These parameters are
defined by the TransactionParameters class.

Transaction support was introduced in PowerShell 3.0 and discontinued in PowerShell 6.0.

UseTransaction (alias: usetx)
Data type: SwitchParameter

This parameter specifies whether the cmdlet uses the current transaction to perform its action.

See Also
      about_CommonParameters
      System.Management.Automation.Internal.CommonParameters
      System.Management.Automation.Internal.ShouldProcessParameters
      System.Management.Automation.Internal.TransactionParameters
      Writing a Windows PowerShell Cmdlet
      Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1507 -->

Cmdlet parameter sets
PowerShell uses parameter sets to enable you to write a single cmdlet that can do different
actions for different scenarios. Parameter sets enable you to expose different parameters to the
user. And, to return different information based on the parameters specified by the user.

Examples of parameter sets
For example, the PowerShell Get-EventLog cmdlet returns different information depending on
whether the user specifies the List or LogName parameter. If the List parameter is specified,
the cmdlet returns information about the log files themselves but not the event information
they contain. If the LogName parameter is specified, the cmdlet returns information about the
events in a specific event log. The List and LogName parameters identify two separate
parameter sets.

Unique parameter
Each parameter set must have a unique parameter that the PowerShell runtime uses to expose
the appropriate parameter set. If possible, the unique parameter should be a mandatory
parameter. When a parameter is mandatory, the user must specify the parameter, and the
PowerShell runtime uses that parameter to identify the parameter set. The unique parameter
can't be mandatory if your cmdlet is designed to run without specifying any parameters.

Multiple parameter sets
In the following illustration, the left column shows three valid parameter sets. Parameter A is
unique to the first parameter set, parameter B is unique to the second parameter set, and
parameter C is unique to the third parameter set. In the right column, the parameter sets don't
have a unique parameter.

Parameter set requirements

<!-- p.1508 -->

The following requirements apply to all parameter sets.

     Each parameter set must have at least one unique parameter. If possible, make this
     parameter a mandatory parameter.

     A parameter set that contains multiple positional parameters must define unique
     positions for each parameter. No two positional parameters can specify the same
     position.

     Only one parameter in a set can declare the ValueFromPipeline keyword with a value of
     true . Multiple parameters can define the ValueFromPipelineByPropertyName keyword with

     a value of true .

     If no parameter set is specified for a parameter, the parameter belongs to all parameter
     sets.

  ７ Note

  For a cmdlet or function, there is a limit of 32 parameter sets.

Default parameter sets
When multiple parameter sets are defined, you can use the DefaultParameterSetName keyword
of the Cmdlet attribute to specify the default parameter set. PowerShell uses the default
parameter set if it can't determine the parameter set to use based on the information provided
by the command. For more information about the Cmdlet attribute, see Cmdlet Attribute
Declaration.

Declaring parameter sets
To create a parameter set, you must specify the ParameterSetName keyword when you declare
the Parameter attribute for every parameter in the parameter set. For parameters that belong
to multiple parameter sets, add a Parameter attribute for each parameter set. This attribute
enables you to define the parameter differently for each parameter set. For example, you can
define a parameter as mandatory in one set and optional in another. However, each parameter
set must contain one unique parameter. For more information, see Parameter Attribute
Declaration.

<!-- p.1509 -->

In the following example, the UserName parameter is the unique parameter of the Test01
parameter set, and the ComputerName parameter is the unique parameter of the Test02
parameter set. The SharedParam parameter belongs to both sets and is mandatory for the
Test01 parameter set but optional for the Test02 parameter set.

 C#

 [Parameter(Position = 0, Mandatory = true, ParameterSetName = "Test01")]
 public string UserName
 {
   get { return userName; }
   set { userName = value; }
 }
 private string userName;

 [Parameter(Position = 0, Mandatory = true, ParameterSetName = "Test02")]
 public string ComputerName
 {
   get { return computerName; }
   set { computerName = value; }
 }
 private string computerName;

 [Parameter(Mandatory= true, ParameterSetName = "Test01")]
 [Parameter(ParameterSetName = "Test02")]
 public string SharedParam
 {
     get { return sharedParam; }
     set { sharedParam = value; }
 }
 private string sharedParam;

Last updated on 05/20/2025

<!-- p.1510 -->

Cmdlet dynamic parameters
Cmdlets can define parameters that are available to the user under special conditions, such as
when the argument of another parameter is a specific value. These parameters are added at
runtime and are referred to as dynamic parameters because they're only added when needed.
For example, you can design a cmdlet that adds several parameters only when a specific
[switch] parameter is specified.

  ７ Note

  Providers and PowerShell functions can also define dynamic parameters.

Dynamic parameters in PowerShell cmdlets
PowerShell uses dynamic parameters in several of its provider cmdlets. For example, the Get-
Item and Get-ChildItem cmdlets add a CodeSigningCert parameter at runtime when the Path

parameter specifies the Certificate provider path. If the Path parameter specifies a path for a
different provider, the CodeSigningCert parameter isn't available.

The following examples show how the CodeSigningCert parameter is added at runtime when
Get-Item is run.

In this example, the PowerShell runtime has added the parameter and the cmdlet is successful.

 PowerShell

 Get-Item -Path Cert:\CurrentUser -CodeSigningCert

 Output

 Location   : CurrentUser
 StoreNames : {SmartCardRoot, UserDS, AuthRoot, CA...}

In this example, a FileSystem drive is specified and an error is returned. The error message
indicates that the CodeSigningCert parameter can't be found.

 PowerShell

<!-- p.1511 -->

 Get-Item -Path C:\ -CodeSigningCert

 Output

 Get-Item : A parameter cannot be found that matches parameter name
 'CodeSigningCert'.
 At line:1 char:37
 + Get-Item -Path C:\ -CodeSigningCert <<<<
 --------
     CategoryInfo          : InvalidArgument: (:) [Get-Item],
 ParameterBindingException
     FullyQualifiedErrorId :
 NamedParameterNotFound,Microsoft.PowerShell.Commands.GetItemCommand

Support for dynamic parameters
To support dynamic parameters, the following elements must be included in the cmdlet code.

Interface
System.Management.Automation.IDynamicParameters. This interface provides the method that
retrieves the dynamic parameters.

For example:

public class SendGreetingCommand : Cmdlet, IDynamicParameters

Method
System.Management.Automation.IDynamicParameters.GetDynamicParameters. This method
retrieves the object that contains the dynamic parameter definitions.

For example:

 C#

  public object GetDynamicParameters()
  {
    if (employee)
    {
      context= new SendGreetingCommandDynamicParameters();
      return context;
    }
    return null;

<!-- p.1512 -->

 }
 private SendGreetingCommandDynamicParameters context;

Class
A class that defines the dynamic parameters to be added. This class must include a Parameter
attribute for each parameter and any optional Alias and Validation attributes that are needed
by the cmdlet.

For example:

 C#

 public class SendGreetingCommandDynamicParameters
 {
   [Parameter]
   [ValidateSet ("Marketing", "Sales", "Development")]
   public string Department
   {
     get { return department; }
     set { department = value; }
   }
   private string department;
 }

For a complete example of a cmdlet that supports dynamic parameters, see How to Declare
Dynamic Parameters.

See also
      System.Management.Automation.IDynamicParameters
      System.Management.Automation.IDynamicParameters.GetDynamicParameters
      How to Declare Dynamic Parameters
      Writing a Windows PowerShell Cmdlet

Last updated on 04/08/2026

<!-- p.1513 -->

Supporting Wildcard Characters in Cmdlet
Parameters
Often, you will have to design a cmdlet to run against a group of resources rather than against
a single resource. For example, a cmdlet might need to locate all the files in a data store that
have the same name or extension. You must provide support for wildcard characters when you
design a cmdlet that will be run against a group of resources.

     ７ Note

     Using wildcard characters is sometimes referred to as globbing.

Windows PowerShell Cmdlets That Use Wildcards
Many Windows PowerShell cmdlets support wildcard characters for their parameter values. For
example, almost every cmdlet that has a Name or Path parameter supports wildcard characters
for these parameters. (Although most cmdlets that have a Path parameter also have a
LiteralPath parameter that does not support wildcard characters.) The following command

shows how a wildcard character is used to return all the cmdlets in the current session whose
name contains the Get verb.

Get-Command get-*

Supported Wildcard Characters
Windows PowerShell supports the following wildcard characters.

                                                                                          ﾉ   Expand table

 Wildcard     Description                                        Example   Matches            Does not
                                                                                              match

 *            Matches zero or more characters, starting at the   a*        A, ag, Apple
              specified position

 ?            Matches any character at the specified position    ?n        An, in, on         ran

<!-- p.1514 -->

 Wildcard    Description                                     Example    Matches        Does not
                                                                                       match

 []          Matches a range of characters                   [a-        book, cook,    nook, took
                                                             l]ook      look

 []          Matches the specified characters                [bn]ook    book, nook     cook, look

When you design cmdlets that support wildcard characters, allow for combinations of wildcard
characters. For example, the following command uses the Get-ChildItem cmdlet to retrieve all
the .txt files that are in the C:\Techdocs folder and that begin with the letters "a" through "l."

Get-ChildItem C:\techdocs\[a-l]\*.txt

The previous command uses the range wildcard [a-l] to specify that the file name should
begin with the characters "a" through "l" and uses the * wildcard character as a placeholder
for any characters between the first letter of the filename and the .txt extension.

The following example uses a range wildcard pattern that excludes the letter "d" but includes
all the other letters from "a" through "f."

Get-ChildItem C:\techdocs\[a-cef]\*.txt

Handling Literal Characters in Wildcard Patterns
If the wildcard pattern you specify contains literal characters that should not be interpreted as
wildcard characters, use the backtick character ( ` ) as an escape character. When you specify
literal characters int the PowerShell API, use a single backtick. When you specify literal
characters at the PowerShell command prompt, use two backticks.

For example, the following pattern contains two brackets that must be taken literally.

When used in the PowerShell API use:

      "John Smith `[*`]"

When used from the PowerShell command prompt:

      "John Smith ``[*``]"

This pattern matches "John Smith [Marketing]" or "John Smith [Development]". For example:

<!-- p.1515 -->

  PS> "John Smith [Marketing]" -like "John Smith ``[*``]"
  True

  PS> "John Smith [Development]" -like "John Smith ``[*``]"
  True

Cmdlet Output and Wildcard Characters
When cmdlet parameters support wildcard characters, the operation usually generates an array
output. Occasionally, it makes no sense to support an array output because the user might use
only a single item. For example, the Set-Location cmdlet does not support array output
because the user sets only a single location. In this instance, the cmdlet still supports wildcard
characters, but it forces resolution to a single location.

See Also
Writing a Windows PowerShell Cmdlet

WildcardPattern Class

 Last updated on 05/20/2025

<!-- p.1516 -->

Validating Parameter Input
PowerShell can validate the arguments passed to cmdlet parameters in several ways.
PowerShell can validate the length, the range, and the pattern of the characters of the
argument. It can validate the number of arguments available (the count). These validation rules
are defined by validation attributes that are declared with the Parameter attribute on public
properties of the cmdlet class.

To validate a parameter argument, the PowerShell runtime uses the information provided by
the validation attributes to confirm the value of the parameter before the cmdlet is run. If the
parameter input is not valid, the user receives an error message. Each validation parameter
defines a validation rule that is enforced by PowerShell.

PowerShell enforces the validation rules based on the following attributes.

ValidateCount
Specifies the minimum and maximum number of arguments that a parameter can accept. For
more information, see ValidateCount Attribute Declaration.

ValidateLength
Specifies the minimum and maximum number of characters in the parameter argument. For
more information, see ValidateLength Attribute Declaration.

ValidatePattern
Specifies a regular expression that validates the parameter argument. For more information,
see ValidatePattern Attribute Declaration.

ValidateRange
Specifies the minimum and maximum values of the parameter argument. For more
information, see ValidateRange Attribute Declaration.

ValidateScript
Specifies the valid values for the parameter argument. For more information, see ValidateScript
Attribute Declaration.

<!-- p.1517 -->

ValidateSet
Specifies the valid values for the parameter argument. For more information, see ValidateSet
Attribute Declaration.

See Also
How to Validate Parameter Input

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1518 -->

Input Filter Parameters
A cmdlet can define Filter , Include , and Exclude parameters that filter the set of input
objects that the cmdlet affects.

Typically, the set of input objects is specified by an InputObject , Path , or Name parameter. For
example, a cmdlet can have a Path parameter that accepts multiple paths by using wildcard
characters, and each path points to an input object. Used together, the Filter , Include , and
Exclude parameters further qualify the paths the cmdlet works on each time it is invoked.

Include and Exclude Parameters
The Include and Exclude parameters identify the objects that are included or excluded from
the set of input objects passed to the cmdlet. Use these parameters when the filter can be
expressed in the standard wildcard language. (For more information about wildcard characters,
see Supporting Wildcards in Cmdlet Parameters.) The Include parameter includes all the
objects whose names match the inclusion filter. The Exclude parameter excludes all the objects
whose names match the filter.

Filter Parameter
The Filter parameter specifies a filter that is not expressed in the standard wildcard language.
For example, Active Directory Service Interfaces (ADSI) or SQL filters might be passed to the
cmdlet through its Filter parameter. In the cmdlets provided by Windows PowerShell, these
filters are specified by the Windows PowerShell providers that use the cmdlet to access a data
store. Each provider typically defines its own filter.

Filtering If No Set of Input Objects Is Specified
If no set of input objects is specified, this typically means to filter against all objects. For more
information, seeGet-Process.

See Also
Writing a Windows PowerShell Cmdlet

<!-- p.1519 -->

Last updated on 05/20/2025

<!-- p.1520 -->

Cmdlet Attributes
Windows PowerShell defines several attributes that you can use to add common functionality
to your cmdlets without implementing that functionality within your own code. This includes
the Cmdlet attribute that identifies a Microsoft .NET Framework class as a cmdlet class, the
OutputType attribute that specifies the .NET Framework types returned by the cmdlet, the
Parameter attribute that identifies public properties as cmdlet parameters, and more.

In This Section
Attributes in Cmdlet Code Describes the benefit of using attributes in cmdlet code.

Attribute Types Describes the different attributes that can decorate a cmdlet class.

Alias Attribute Declaration Describes how to define aliases for a cmdlet parameter name.

Cmdlet Attribute Declaration Describes how to define a .NET Framework class as a cmdlet.

Credential Attribute Declaration Describes how to add support for converting string input into
a System.Management.Automation.PSCredential object.

OutputType attribute Declaration Describes how to specify the .NET Framework types returned
by the cmdlet.

Parameter Attribute Declaration Describes how to define the parameters of a cmdlet.

ValidateCount Attribute Declaration Describes how to define how many arguments are allowed
for a parameter.

ValidateLength Attribute Declaration Describes how to define the length (in characters) of a
parameter argument.

ValidatePattern Attribute Declaration Describes how to define the valid patterns for a
parameter argument.

ValidateRange Attribute Declaration Describes how to define the valid range for a parameter
argument.

ValidateScript Attribute Declaration Describes how to define the possible values for a
parameter argument.
