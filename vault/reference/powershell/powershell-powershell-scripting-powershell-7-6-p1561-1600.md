---
title: "How to use this documentation — pages 1561-1600"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1561-1600
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1561-1600
family: powershell
documentKind: "doc"
abstract: "In the following example, the Mode property is added to the System.IO.DirectoryInfo type. The CodeProperty element defines the extended property as a code property. The Name element specifies the name of the extended property. And, the GetCodeReference element defines the static"
---

# How to use this documentation — pages 1561-1600

<!-- p.1561 -->

In the following example, the Mode property is added to the System.IO.DirectoryInfo type. The
CodeProperty element defines the extended property as a code property. The Name element
specifies the name of the extended property. And, the GetCodeReference element defines the
static method that is referenced by the extended property. You can also add the CodeProperty
element to the members of the MemberSets element.

 XML

 <Type>
   <Name>System.IO.DirectoryInfo</Name>
   <Members>
     <CodeProperty>
       <Name>Mode</Name>
       <GetCodeReference>
         <TypeName>Microsoft.PowerShell.Commands.FileSystemProvider</TypeName>
         <MethodName>Mode</MethodName>
       </GetCodeReference>
     </CodeProperty>
   </Members>
 </Type>

Note properties
A note property defines a property that has a static value.

In the following example, the Status property, whose value is always Success, is added to the
System.IO.DirectoryInfo type. The NoteProperty element defines the extended property as a
note property. The Name element specifies the name of the extended property. The Value
element specifies the static value of the extended property. The NoteProperty element can also
be added to the members of the MemberSets element.

 XML

 <Type>
   <Name>System.IO.DirectoryInfo</Name>
   <Members>
     <NoteProperty>
       <Name>Status</Name>
       <Value>Success</Value>
     </NoteProperty>
   </Members>
 </Type>

Script properties

<!-- p.1562 -->

A script property defines a property whose value is the output of a script.

In the following example, the VersionInfo property is added to the System.IO.FileInfo type. The
ScriptProperty element defines the extended property as a script property. The Name element
specifies the name of the extended property. And, the GetScriptBlock element specifies the
script that generates the property value. You can also add the ScriptProperty element to the
members of the MemberSets element.

 XML

 <Type>
   <Name>System.IO.FileInfo</Name>
   <Members>
     <ScriptProperty>
       <Name>VersionInfo</Name>
       <GetScriptBlock>
         [System.Diagnostics.FileVersionInfo]::GetVersionInfo($this.FullName)
       </GetScriptBlock>
     </ScriptProperty>
   </Members>
 </Type>

Property sets
A property set defines a group of extended properties that can be referenced by the name of
the set. For example, the Format-Table Property parameter can specify a specific property set
to be displayed. When a property set is specified, only those properties that belong to the set
are displayed.

There's no restriction on the number of property sets that can be defined for an object.
However, the property sets used to define the default display properties of an object must be
specified within the PSStandardMembers member set. In the Types.ps1xml types file, the
default property set names include DefaultDisplayProperty, DefaultDisplayPropertySet, and
DefaultKeyPropertySet. Any additional property sets that you add to the PSStandardMembers
member set are ignored.

In the following example, the DefaultDisplayPropertySet property set is added to the
PSStandardMembers member set of the System.ServiceProcess.ServiceController type. The
PropertySet element defines the group of properties. The Name element specifies the name of
the property set. And, the ReferencedProperties element specifies the properties of the set. You
can also add the PropertySet element to the members of the Type element.

<!-- p.1563 -->

 XML

 <Type>
   <Name>System.ServiceProcess.ServiceController</Name>
   <Members>
     <MemberSet>
       <Name>PSStandardMembers</Name>
       <Members>
         <PropertySet>
            <Name>DefaultDisplayPropertySet</Name>
            <ReferencedProperties>
             <Name>Status</Name
             <Name>Name</Name>
             <Name>DisplayName</Name>
           </ReferencedProperties>
         </PropertySet>
       </Members>
     </MemberSet>
   </Members>
 </Type>

See also
About Types.ps1xml

System.Management.Automation

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1564 -->

Defining Default Methods for Objects
When you extend .NET Framework objects, you can add code methods and script methods to
the objects. The XML that is used to define these methods is described in the following
sections.

  ７ Note

  The examples in the following sections are from the Types.ps1xml types file in the
  Windows PowerShell installation directory ( $PSHOME ). For more information, see About
  Types.ps1xml.

Code methods
A code method references a static method of a .NET Framework object.

In the following example, the ToString method is added to the System.Xml.XmlNode type. The
PSCodeMethod element defines the extended method as a code method. The Name element
specifies the name of the extended method. And, the CodeReference element specifies the
static method. You can also add the PSCodeMethod element to the members of the
PSMemberSets element.

 XML

 <Type>
   <Name>System.Xml.XmlNode</Name>
   <Members>
     <CodeMethod>
       <Name>ToString</Name>
       <CodeReference>
         <TypeName>Microsoft.PowerShell.ToStringCodeMethods</TypeName>
         <MethodName>XmlNode</MethodName>
       </CodeReference>
     </CodeMethod>
   </Members>
 </Type>

Script methods

<!-- p.1565 -->

A script method defines a method whose value is the output of a script. In the following
example, the ConvertToDateTime method is added to the
System.Management.ManagementObject type. The PSScriptMethod element defines the
extended method as a script method. The Name element specifies the name of the extended
method. And, the Script element specifies the script that generates the method value. You can
also add the PSScriptMethod element to the members of the PSMemberSets element.

 XML

 <Type>
   <Name>System.Management.ManagementObject</Name>
   <Members>
     <ScriptMethod>
       <Name>ConvertToDateTime</Name>
       <Script>
         [System.Management.ManagementDateTimeConverter]::ToDateTime($args[0])
       </Script>
     </ScriptMethod>
   </Members>
 </Type>

See also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1566 -->

Defining Default Member Sets for Objects
The PSStandardMembers member set is used by Windows PowerShell to define the default
property sets for an object. The default property sets can be used by commands such as the
formatting cmdlets to display only those properties that are defined by the property set. The
default property sets include DefaultDisplayProperty, DefaultDisplayPropertySet, and
DefaultKeyPropertySet. Windows PowerShell ignores all other member sets and any other
property sets added to the PSStandardMembers member set.

Member Set for System.Diagnostics.Process
In the following example, the PSStandardMembers member set defines the
DefaultDisplayPropertySet property set for System.Diagnostics.Process objects. This property
set is used by the Format-List cmdlet.

 XML

 <Type>
   <Name>System.Diagnostics.Process</Name>
   <Members>
     <MemberSet>
      <Name>PSStandardMembers</Name>
      <Members>
        <PropertySet>
          <Name>DefaultDisplayPropertySet</Name>
          <ReferencedProperties>
            <Name>Id</Name>
            <Name>Handles</Name>
            <Name>CPU</Name>
            <Name>Name</Name>
          </ReferencedProperties>
       </PropertySet>
     </Members>
   </MemberSet>

The following output shows the default properties returned by the Format-List cmdlet. Only the
Id , Handles , CPU , and Name properties are returned for each process object.

 PowerShell

 Get-Process | Format-List

<!-- p.1567 -->

 Output

 Id      : 2036
 Handles : 27
 CPU     :
 Name    : AEADISRV

 Id      : 272
 Handles : 38
 CPU     :
 Name    : agrsmsvc
 ...

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1568 -->

Custom Formatting Files
The display format for the objects returned by cmdlets, functions, and scripts are defined using
formatting files ( format.ps1xml files). Several of these files are provided by Windows
PowerShell to define the default display format for those objects returned by Windows
PowerShell cmdlets. However, you can also create your own custom formatting files to
overwrite the default display formats or to define the display of objects returned by your own
commands.

Windows PowerShell uses the data in these formatting files to determine what is displayed and
how the data is formatted. The displayed data can include the properties of an object or the
value of a script block. Script blocks are used if you want to display some value that is not
available directly from the properties of an object. For example, you may want to add the value
of two properties of an object and display the sum as a separate piece of data. When you write
your own formatting file, you will need to define views for the objects that you want to display.
You can define a single view for each object, you can define a single view for multiple objects,
or you can define multiple views for the same object. There is no limit to the number of views
that you can define.

  ） Important

  Formatting files do not determine the elements of an object that are returned to the
  pipeline. When an object is returned to the pipeline, all members of that object are
  available.

Format Views
Formatting views can display objects in a table format, a list format, a wide format, and a
custom format. For the most part, each formatting definition is described by a set of XML tags
that describe a view. Each view contains the name of the view, the objects that use the view,
and the elements of the view, such as the column and row information for a table view.

The following views are available.

Table view Lists the properties of an object or a script block value in one or more columns. Each
column represents a property of the object or a script block value. You can define a table view
that displays all the properties of an object, a subset of the properties of an object, or a

<!-- p.1569 -->

combination of properties and script block values. Each row of the table represents a returned
object. For more information about this view, see Table View.

List view Lists the properties of an object or a script block value in a single column. Each row of
the list displays an optional label or the property name followed by the value of the property or
script block. For more information about this view, see List View.

Wide view Lists a single property of an object or a script block value in one or more columns.
There is no label or header for this view. For more information about this view, see Wide View.

Custom view Displays a customizable view of object properties or script block values that does
not adhere to the rigid structure of table views, list views, or wide views. You can define a
standalone custom view, or you can define a custom view that is used by another view, such as
a table view or list view. For more information about this view, see Custom View.

View XML Elements
The following example shows the XML tags used to define a table view that contains two
columns. The ViewDefinitions element is the container element for all the views defined in the
formatting file. The View element defines the specific table, list, wide, or custom view. Within
each view, the Name element specifies the name of the view, the ViewSelectedBy element
defines the objects that use the view, and the different control elements (such as the
TableControl element) define the format of the view.

 XML

 ViewDefinitions
   <View>
     <Name>Name of View</Name>
     <ViewSelectedBy>
       <TypeName>Object to display using this view</TypeName>
       <TypeName>Object to display using this view</TypeName>
     </ViewSelectedBy>
     <TableControl>
       <TableHeaders>
         <TableColumnHeader>
           <Width></Width>
         </TableColumnHeader>
         <TableColumnHeader>
           <Width></Width>
         </TableColumnHeader>
       </TableHeaders>
       <TableRowEntries>
         <TableRowEntry>
           <TableColumnItems>
             <TableColumnItem>

<!-- p.1570 -->

                <PropertyName>Header for column 1</PropertyName>
              </TableColumnItem>
              <TableColumnItem>
                <PropertyName>Header for column 2</PropertyName>
              </TableColumnItem>
            </TableColumnItems>
          </TableRowEntry>
        </TableRowEntries>
      </TableControl)
    </View>
  </ViewDefinitions>

See Also
Table View

List View

Wide View

Custom View

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1571 -->

Requesting Confirmation
ﾃ   Summarize this article for me

This section discusses confirmation messages that can be displayed before a cmdlet, function,
or provider performs an action.

In This Section
Requesting Confirmation Process for Commands Discusses the process that cmdlets, functions,
and providers must follow to request a confirmation before they make a change to the system.

Users Requesting Confirmation Discusses how users can make a cmdlet, function, or provider
request confirmation when the System.Management.Automation.Cmdlet.ShouldProcess
method is called.

Confirmation Messages Provides samples of the different confirmation messages that can be
displayed.

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 02/24/2026

<!-- p.1572 -->

Requesting Confirmation from Cmdlets
Cmdlets should request confirmation when they make a change to the system that's outside of
the Windows PowerShell environment. For example, if a cmdlet is about to add a user account
or stop a process, the cmdlet should require confirmation from the user before it proceeds. In
contrast, if a cmdlet is about to change a Windows PowerShell variable, the cmdlet doesn't
need to require confirmation.

In order to make a confirmation request, the cmdlet must indicate that it supports confirmation
requests, and it must call the System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue (optional) methods to display a
confirmation request message.

Supporting Confirmation Requests
To support confirmation requests, the cmdlet must set the SupportsShouldProcess parameter of
the Cmdlet attribute to true . This enables the Confirm and WhatIf cmdlet parameters that are
provided by Windows PowerShell. The Confirm parameter allows the user to control whether
the confirmation request is displayed. The WhatIf parameter allows the user to determine
whether the cmdlet should display a message or perform its action. Don't manually add the
Confirm and WhatIf parameters to a cmdlet.

The following example shows a Cmdlet attribute declaration that supports confirmation
requests.

 C#

 [Cmdlet(VerbsDiagnostic.Test, "RequestConfirmationTemplate1",
         SupportsShouldProcess = true)]

Calling the Confirmation request methods
In the cmdlet code, call the System.Management.Automation.Cmdlet.ShouldProcess method
before the operation that changes the system is performed. Design the cmdlet so that if the
call returns a value of false , the operation isn't performed, and the cmdlet processes the next
operation.

<!-- p.1573 -->

Calling the ShouldContinue Method
Most cmdlets request confirmation using only the
System.Management.Automation.Cmdlet.ShouldProcess method. However, some cases might
require additional confirmation. For these cases, supplement the
System.Management.Automation.Cmdlet.ShouldProcess call with a call to the
System.Management.Automation.Cmdlet.ShouldContinue method. This allows the cmdlet or
provider to more finely control the scope of the Yes to all response to the confirmation
prompt.

If a cmdlet calls the System.Management.Automation.Cmdlet.ShouldContinue method, the
cmdlet must also provide a Force [switch] parameter. If the user specifies Force when the
user invokes the cmdlet, the cmdlet should still call
System.Management.Automation.Cmdlet.ShouldProcess, but it should bypass the call to
System.Management.Automation.Cmdlet.ShouldContinue.

System.Management.Automation.Cmdlet.ShouldContinue will throw an exception when it's
called from a non-interactive environment where the user can't be prompted. Adding a Force
parameter ensures that the command can still be performed when it's invoked in a non-
interactive environment.

The following example shows how to call
System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue.

 C#

 if (ShouldProcess (...) )
 {
   if (Force || ShouldContinue(...))
   {
      // Add code that performs the operation.
   }
 }

The behavior of a System.Management.Automation.Cmdlet.ShouldProcess call can vary
depending on the environment in which the cmdlet is invoked. Using the previous guidelines
will help ensure that the cmdlet behaves consistently with other cmdlets, regardless of the host
environment.

Specify the Impact Level

<!-- p.1574 -->

When you create the cmdlet, specify the impact level (the severity) of the change. To do this,
set the value of the ConfirmImpact parameter of the Cmdlet attribute to High, Medium, or Low.
You can specify a value for ConfirmImpact only when you also specify the
SupportsShouldProcess parameter for the cmdlet.

For most cmdlets, you don't have to explicitly specify ConfirmImpact . Instead, use the default
setting of the parameter, which is Medium. If you set ConfirmImpact to High, the operation will
be confirmed by default. Reserve this setting for highly disruptive actions, such as reformatting
a hard-disk volume.

Calling Non-Confirmation Methods
If the cmdlet or provider must send a message but not request confirmation, it can call the
following three methods. Avoid using the
System.Management.Automation.Cmdlet.WriteObject method to send messages of these types
because System.Management.Automation.Cmdlet.WriteObject output is intermingled with the
normal output of your cmdlet or provider, which makes script writing difficult.

     To caution the user and continue with the operation, the cmdlet or provider can call the
     System.Management.Automation.Cmdlet.WriteWarning method.

     To provide additional information that the user can retrieve using the Verbose parameter,
     the cmdlet or provider can call the
     System.Management.Automation.Cmdlet.WriteVerbose method.

     To provide debugging-level detail for other developers or for product support, the cmdlet
     or provider can call the System.Management.Automation.Cmdlet.WriteDebug method.
     The user can retrieve this information using the Debug parameter.

Cmdlets and providers first call the following methods to request confirmation before they
attempt to perform an operation that changes a system outside of Windows PowerShell:

     System.Management.Automation.Cmdlet.ShouldProcess

     System.Management.Automation.Provider.CmdletProvider.ShouldProcess

They do so by calling the System.Management.Automation.Cmdlet.ShouldProcess method,
which prompts the user to confirm the operation based on how the user invoked the
command.

See Also

<!-- p.1575 -->

Writing a Windows PowerShell Cmdlet

Last updated on 04/08/2026

<!-- p.1576 -->

Users Requesting Confirmation
When you specify a value of true for the SupportsShouldProcess parameter of the Cmdlet
attribute declaration, the Confirm parameter is added to the parameters of the cmdlet.

In the default environment, users can specify the Confirm parameter so that confirmation is
requested when the ShouldProcess() method is called. This forces confirmation regardless of
the impact level setting.

If Confirm parameter is not used, the ShouldProcess() call requests confirmation if the
ConfirmImpact setting is equal to or greater than the $ConfirmPreference preference variable.

The default setting of $ConfirmPreference is High. Therefore, in the default environment, only
cmdlets and providers that specify a high-impact action request confirmation.

If Confirm is explicitly set to false ( -Confirm:$false ), the cmdlet runs without prompting for
confirmation and the $ConfirmPreference shell variable is ignored.

Remarks
      For cmdlets and providers that specify SupportsShouldProcess , but not ConfirmImpact ,
      those actions are handled as Medium impact actions, and they will not prompt by default.
      Their impact level is less than the default setting of the $ConfirmPreference preference
      variable.

      If the user specifies the Verbose parameter, they will be notified of the operation even if
      they are not prompted for confirmation.

See Also
      Writing a Windows PowerShell Cmdlet
      System.Management.Automation.Cmdlet.ShouldProcess

 Last updated on 05/20/2025

<!-- p.1577 -->

Confirmation Messages
ﾃ     Summarize this article for me

Here are different confirmation messages that can be displayed depending on the variants of
the System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue methods that are called.

    ） Important

    For sample code that shows how to request confirmations, see Requesting Confirmation
    from Cmdlets.

Specifying the Resource
You can specify the resource that is about to be changed by calling the
System.Management.Automation.Cmdlet.ShouldProcess method. In this case, you supply the
resource by using the target parameter of the method, and the operation is added by
Windows PowerShell. In the following message, the text "MyResource" is the resource acted on
and the operation is the name of the command that makes the call.

 Output

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Test-RequestConfirmationTemplate1" on Target "MyResource".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"):

If the user selects Yes or Yes to All to the confirmation request (as shown in the following
example), a call to the System.Management.Automation.Cmdlet.ShouldContinue method is
made, which causes a second confirmation message to be displayed.

 Output

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Test-RequestConfirmationTemplate1" on Target "MyResource".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default is
 "Y"): y

 Confirm
 Continue with this operation?
 [Y] Yes [N] No [S] Suspend [?] Help (default is "Y"):

<!-- p.1578 -->

Specifying the Operation and Resource
You can specify the resource that is about to be changed and the operation that the command
is about to perform by calling the System.Management.Automation.Cmdlet.ShouldProcess
method. In this case, you supply the resource by using the target parameter and the
operation by using the target parameter. In the following message, the text "MyResource" is
the resource acted on and "MyAction" is the operation to be performed.

  Output

  Confirm
  Are you sure you want to perform this action?
  Performing operation "MyAction" on Target "MyResource".
  [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend               [?] Help (default is
  "Y"):

If the user selects Yes or Yes to All to the previous message, a call to the
System.Management.Automation.Cmdlet.ShouldContinue method is made, which causes a
second confirmation message to be displayed.

  Output

  Confirm
  Are you sure you want to perform this action?
  Performing operation "MyAction" on Target "MyResource".
  [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend               [?] Help (default is
  "Y"): y

  Confirm
  Continue with this operation?
  [Y] Yes [N] No [S] Suspend [?] Help (default is "Y"):

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 02/24/2026

<!-- p.1579 -->

Windows PowerShell Error Reporting
The topics in this section discuss how cmdlets report errors.

In This Section
Error Reporting Concepts Describes the two mechanisms that cmdlets can use to report errors.

Terminating Errors Describes the method used to report terminating errors, where that method
can be called from within the cmdlet, and exceptions that can be returned by the Windows
PowerShell runtime when the method is called.

Non-Terminating Errors Describes the method used to report non-terminating errors and
where that method can be called from within the cmdlet.

Displaying Error Information by Category Discusses the ways that users can display error.

Windows PowerShell Error Records Describes the components of an error record.

Interpreting ErrorRecord Objects Discusses how ErrorRecord objects are interpreted.

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1580 -->

Error Reporting Concepts
Windows PowerShell provides two mechanisms for reporting errors: one mechanism for
terminating errors and another mechanism for non-terminating errors. It is important for your
cmdlet to report errors correctly so that the host application that is running your cmdlets can
react in an appropriate manner.

Your cmdlet should call the System.Management.Automation.Cmdlet.ThrowTerminatingError*
method when an error occurs that does not or should not allow the cmdlet to continue to
process its input objects. Your cmdlet should call the
System.Management.Automation.Cmdlet.WriteError method to report non-terminating errors
when the cmdlet can continue processing the input objects. Both methods provide an error
record that the host application can use to investigate the cause of the error.

Use the following guidelines to determine whether an error is a terminating or non-terminating
error.

         An error is a terminating error if it prevents your cmdlet from continuing to process the
         current object or from successfully processing any further input objects, regardless of
         their content.

         An error is a terminating error if you do not want your cmdlet to continue processing the
         current object or any further input objects, regardless of their content.

         An error is a terminating error if it occurs in a cmdlet that does not accept or return an
         object or if it occurs in a cmdlet that accepts or returns only one object.

         An error is a non-terminating error if you want your cmdlet to continue processing the
         current object and any further input objects.

         An error is a non-terminating error if it is related to a specific input object or subset of
         input objects.

See Also
System.Management.Automation.Cmdlet.ThrowTerminatingError*

System.Management.Automation.Cmdlet.WriteError

Windows PowerShell Error Records

<!-- p.1581 -->

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1582 -->

Terminating Errors
This topic discusses the method used to report terminating errors. It also discusses how to call
the method from within the cmdlet, and it discusses the exceptions that can be returned by the
Windows PowerShell runtime when the method is called.

When a terminating error occurs, the cmdlet should report the error by calling the
System.Management.Automation.Cmdlet.ThrowTerminatingError* method. This method allows
the cmdlet to send an error record that describes the condition that caused the terminating
error. For more information about error records, see Windows PowerShell Error Records.

When the System.Management.Automation.Cmdlet.ThrowTerminatingError* method is called,
the Windows PowerShell runtime permanently stops the execution of the pipeline and throws a
System.Management.Automation.PipelineStoppedException exception. Any subsequent
attempts to call System.Management.Automation.Cmdlet.WriteObject,
System.Management.Automation.Cmdlet.WriteError, or several other APIs causes those calls to
throw a System.Management.Automation.PipelineStoppedException exception.

The System.Management.Automation.PipelineStoppedException exception can also occur if
another cmdlet in the pipeline reports a terminating error, if the user has asked to stop the
pipeline, or if the pipeline has been halted before completion for any reason. The cmdlet does
not need to catch the System.Management.Automation.PipelineStoppedException exception
unless it must clean up open resources or its internal state.

Cmdlets can write any number of output objects or non-terminating errors before reporting a
terminating error. However, the terminating error permanently stops the pipeline, and no
further output, terminating errors, or non-terminating errors can be reported.

Cmdlets can call System.Management.Automation.Cmdlet.ThrowTerminatingError* only from
the thread that called the System.Management.Automation.Cmdlet.BeginProcessing,
System.Management.Automation.Cmdlet.ProcessRecord, or
System.Management.Automation.Cmdlet.EndProcessing input processing method. Do not
attempt to call System.Management.Automation.Cmdlet.ThrowTerminatingError* or
System.Management.Automation.Cmdlet.WriteError from another thread. Instead, errors must
be communicated back to the main thread.

It is possible for a cmdlet to throw an exception in its implementation of the
System.Management.Automation.Cmdlet.BeginProcessing,

<!-- p.1583 -->

System.Management.Automation.Cmdlet.ProcessRecord, or
System.Management.Automation.Cmdlet.EndProcessing method. Any exception thrown from
these methods (except for a few severe error conditions that stop the Windows PowerShell
host) is interpreted as a terminating error which stops the pipeline, but not Windows
PowerShell as a whole. (This applies only to the main cmdlet thread. Uncaught exceptions in
threads spawned by the cmdlet, in general, halt the Windows PowerShell host.) We recommend
that you use System.Management.Automation.Cmdlet.ThrowTerminatingError* rather than
throwing an exception because the error record provides additional information about the
error condition, which is useful to the end-user. Cmdlets should honor the managed code
guideline against catching and handling all exceptions ( catch (Exception e) ). Convert only
exceptions of known and expected types into error records.

See Also
System.Management.Automation.Cmdlet.BeginProcessing

System.Management.Automation.Cmdlet.EndProcessing

System.Management.Automation.Cmdlet.ProcessRecord

System.Management.Automation.PipelineStoppedException

System.Management.Automation.Cmdlet.ThrowTerminatingError*

System.Management.Automation.Cmdlet.WriteError

Windows PowerShell Error Records

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1584 -->

Non-Terminating Errors
This topic discusses the method used to report non-terminating errors. It also discusses how to
call the method from within the cmdlet.

When a non-terminating error occurs, the cmdlet should report this error by calling the
System.Management.Automation.Cmdlet.WriteError method. When the cmdlet reports a non-
terminating error, the cmdlet can continue to operate on this input object and on further
incoming pipeline objects. If the cmdlet calls the
System.Management.Automation.Cmdlet.WriteError method, the cmdlet can write an error
record that describes the condition that caused the non-terminating error. For more
information about error records, see Windows PowerShell Error Records.

Cmdlets can call System.Management.Automation.Cmdlet.WriteError as necessary from within
their input processing methods. However, cmdlets can call
System.Management.Automation.Cmdlet.WriteError only from the thread that called the
System.Management.Automation.Cmdlet.BeginProcessing,
System.Management.Automation.Cmdlet.ProcessRecord, or
System.Management.Automation.Cmdlet.EndProcessing input processing method. Do not call
System.Management.Automation.Cmdlet.WriteError from another thread. Instead,
communicate errors back to the main thread.

See Also
System.Management.Automation.Cmdlet.WriteError

System.Management.Automation.Cmdlet.BeginProcessing

System.Management.Automation.Cmdlet.ProcessRecord

System.Management.Automation.Cmdlet.EndProcessing

Windows PowerShell Error Records

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1585 -->

Displaying Error Information
This topic discusses the ways in which users can display error information.

When your cmdlet encounters an error, the presentation of the error information will, by
default, resemble the following error output.

  PowerShell

  $ Stop-Service lanmanworkstation
  You do not have sufficient permissions to stop the service Workstation.

However, users can view errors by category by setting the $ErrorView variable to
"CategoryView" . Category view displays specific information from the error record rather than a

free-text description of the error. This view can be useful if you have a long list of errors to
scan. In category view, the previous error message is displayed as follows.

  PowerShell

  $ $ErrorView = "CategoryView"
  $ Stop-Service lanmanworkstation
  CloseError: (System.ServiceProcess.ServiceController:ServiceController) [Stop-
  Service], ServiceCommandException

For more information about error categories, see Windows PowerShell Error Records.

See Also
Windows PowerShell Error Records

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1586 -->

Windows PowerShell Error Records
Cmdlets must pass an System.Management.Automation.ErrorRecord object that identifies the
error condition for terminating and non-terminating errors.

The System.Management.Automation.ErrorRecord object contains the following information:

     The exception that describes the error. Often, this is an exception that the cmdlet caught
     and converted into an error record. Every error record must contain an exception.

If the cmdlet did not catch an exception, it must create a new exception and choose the
exception class that best describes the error condition. However, you do not need to throw the
exception because it can be accessed through the
System.Management.Automation.ErrorRecord.Exception property of the
System.Management.Automation.ErrorRecord object.

     An error identifier that provides a targeted designator that can be used for diagnostic
     purposes and by Windows PowerShell scripts to handle specific error conditions with
     specific error handlers. Every error record must contain an error identifier (see Error
     Identifier).

     An error category that provides a general designator that can be used for diagnostic
     purposes. Every error record must specify an error category (see Error Category).

     An optional replacement error message and a recommended action (see Replacement
     Error Message).

     Optional invocation information about the cmdlet that threw the error. This information is
     specified by Windows PowerShell (see Invocation Message).

     The target object that was being processed when the error occurred. This might be the
     input object, or it might be another object that your cmdlet was processing. For example,
     for the command Remove-Item -Recurse C:\somedirectory , the error might be an instance
     of a FileInfo object for "C:\somedirectory\lockedfile". The target object information is
     optional.

Error Identifier

<!-- p.1587 -->

When you create an error record, specify an identifier that designates the error condition
within your cmdlet. Windows PowerShell combines the targeted identifier with the name of
your cmdlet to create a fully qualified error identifier. The fully qualified error identifier can be
accessed through the System.Management.Automation.ErrorRecord.FullyQualifiedErrorId
property of the System.Management.Automation.ErrorRecord object. The error identifier is not
available by itself. It is available only as part of the fully qualified error identifier.

Use the following guidelines to generate error identifiers when you create error records:

      Make error identifiers specific to an error condition. Target the error identifiers for
      diagnostic purposes and for scripts that handle specific error conditions with specific
      error handlers. A user should be able to use the error identifier to identify the error and
      its source. Error identifiers also enable reporting for specific error conditions from existing
      exceptions so that new exception subclasses are not required.

      In general, assign different error identifiers to different code paths. The end-user benefits
      from specific identifiers. Often, each code path that calls
      System.Management.Automation.Cmdlet.WriteError or
      System.Management.Automation.Cmdlet.ThrowTerminatingError* has its own identifier.
      As a rule, define a new identifier when you define a new template string for the error
      message, and vice-versa. Do not use the error message as an identifier.

      When you publish code using a particular error identifier, you establish the semantics of
      errors with that identifier for your complete product support lifecycle. Do not reuse it in a
      context that is semantically different from the original context. If the semantics of this
      error change, create and then use a new identifier.

      You should generally use a particular error identifier only for exceptions of a particular
      CLR type. If the type of the exception or the type of the target object changes, create and
      then use a new identifier.

      Choose text for your error identifier that concisely corresponds to the error that you are
      reporting. Use standard .NET Framework naming and capitalization conventions. Do not
      use white space or punctuation. Do not localize error identifiers.

      Do not dynamically generate error identifiers in a non-reproducible way. For example, do
      not incorporate error information such as a process ID. Error identifiers are useful only if
      they correspond to the error identifiers seen by other users who are experiencing the
      same error condition.

<!-- p.1588 -->

Error Category
When you create an error record, specify the category of the error using one of the constants
defined by the System.Management.Automation.ErrorCategory enumeration. Windows
PowerShell uses the error category to display error information when users set the $ErrorView
variable to "CategoryView" .

Avoid using the System.Management.Automation.ErrorCategory NotSpecified constant. If you
have any information about the error or about the operation that caused the error, choose the
category that best describes the error or the operation, even if the category is not a perfect
match.

The information displayed by Windows PowerShell is referred to as the category-view string
and is built from the properties of the System.Management.Automation.ErrorCategoryInfo
class. (This class is accessed through the error
System.Management.Automation.ErrorRecord.CategoryInfo property.)

 {Category}: ({TargetName}:{TargetType}):[{Activity}], {Reason}

The following list describes the information displayed:

     Category: A Windows PowerShell-defined System.Management.Automation.ErrorCategory
     constant.

     TargetName: By default, the name of the object the cmdlet was processing when the error
     occurred. Or, another cmdlet-defined string.

     TargetType: By default, the type of the target object. Or, another cmdlet-defined string.

     Activity: By default, the name of the cmdlet that created the error record. Or, some other
     cmdlet-defined string.

     Reason: By default, the exception type. Or, another cmdlet-defined string.

Replacement Error Message
When you develop an error record for a cmdlet, the default error message for the error comes
from the default message text in the System.Exception.Message property. This is a read-only
property whose message text is intended only for debugging purposes (according to the .NET

<!-- p.1589 -->

Framework guidelines). We recommend that you create an error message that replaces or
augments the default message text. Make the message more user-friendly and more specific to
the cmdlet.

The replacement message is provided by an System.Management.Automation.ErrorDetails
object. Use one of the following constructors of this object because they provide additional
localization information that can be used by Windows PowerShell.

     ErrorDetails(Cmdlet, String, String, Object[]): Use this constructor if your template string is
     a resource string in the same assembly in which the cmdlet is implemented or if you want
     to load the template string through an override of the
     System.Management.Automation.Cmdlet.GetResourceString method.

     ErrorDetails(Assembly, String, String, Object[]): Use this constructor if the template string
     is in another assembly and you do not load it through an override of
     System.Management.Automation.Cmdlet.GetResourceString.

The replacement message should conform to the .NET Framework design guidelines for writing
exception messages with a small difference. The guidelines state that exception messages
should be written for developers. These replacement messages should be written for the
cmdlet user.

The replacement error message must be added before the
System.Management.Automation.Cmdlet.WriteError or
System.Management.Automation.Cmdlet.ThrowTerminatingError* methods are called. To add a
replacement message, set the System.Management.Automation.ErrorRecord.ErrorDetails
property of the error record. When this property is set, Windows PowerShell displays the
System.Management.Automation.ErrorDetails.Message* property instead of the default
message text.

Recommended Action Information
The System.Management.Automation.ErrorDetails object can also provide information about
what actions are recommended when the error occurs.

Invocation information
When a cmdlet uses System.Management.Automation.Cmdlet.WriteError or
System.Management.Automation.Cmdlet.ThrowTerminatingError* to report an error record,
Windows PowerShell automatically adds information that describes the command that was

<!-- p.1590 -->

invoked when the error occurred. This information is provided by a
System.Management.Automation.InvocationInfo object that contains the name of the cmdlet
that was invoked by the command, the command itself, and information about the pipeline or
script. This property is read-only.

See Also
System.Management.Automation.Cmdlet.WriteError

System.Management.Automation.Cmdlet.ThrowTerminatingError*

System.Management.Automation.ErrorCategory

System.Management.Automation.ErrorCategoryInfo

System.Management.Automation.ErrorRecord

System.Management.Automation.ErrorDetails

System.Management.Automation.InvocationInfo

Windows PowerShell Error Reporting

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1591 -->

Interpreting ErrorRecord Objects
In most cases, an System.Management.Automation.ErrorRecord object represents a non-
terminating error generated by a command or script. Terminating errors can also specify the
additional information in an ErrorRecord via the
System.Management.Automation.IContainsErrorRecord interface.

If you want to write an error handler in your script or a host to handle specific errors that occur
during command or script execution, you must interpret the
System.Management.Automation.ErrorRecord object to determine whether it represents the
class of error that you want to handle.

When a cmdlet encounters a terminating or non-terminating error, it should create an error
record that describes the error condition. The host application must investigate these error
records and perform whatever action will mitigate the error. The host application must also
investigate error records for non-terminating errors that failed to process a record but were
able to continue, and it must investigate error records for terminating errors that caused the
pipeline to stop.

  ７ Note

  For terminating errors, the cmdlet calls the
  System.Management.Automation.Cmdlet.ThrowTerminatingError method. For non-
  terminating errors, the cmdlet calls the
  System.Management.Automation.Cmdlet.WriteError method.

Error Record Design
Error records are designed to provide additional error information that is not available in
exceptions while ensuring that the combined information in each error record is unique. This
uniqueness allows the host application to inspect the different parts of the error record so that
it can identify the error condition and the action the host must take.

Interpreting Error Records

<!-- p.1592 -->

You can review several parts of the error record to identify the error. These parts include the
following:

     The error category

     The error exception

     The fully qualified error identifier (FQID)

     Other information

The Error Category
The error category of the error record is one of the predefined constants provided by the
System.Management.Automation.ErrorCategory enumeration. This information is available
through the System.Management.Automation.ErrorRecord.CategoryInfo property of the
System.Management.Automation.ErrorRecord object.

The cmdlet can specify the CloseError, OpenError, InvalidType, ReadError, and WriteError
categories, and other error categories. The host application can use the error category to
capture groups of errors.

The Exception
The exception included in the error record is provided by the cmdlet and can be accessed
through the System.Management.Automation.ErrorRecord.Exception property of the
System.Management.Automation.ErrorRecord object.

Host applications can use the is keyword to identify that the exception is of a specific class or
of a derived class. It is better to branch on the exception type, as shown in the following
example.

 PowerShell

 `if (MyNonTerminatingError.Exception is AccessDeniedException)`
 {
   ...
 }

This way, you catch the derived classes. However, there are problems if the exception is
deserialized.

The FQID

<!-- p.1593 -->

The FQID is the most specific information you can use to identify the error. It is a string that
includes a cmdlet-defined identifier, the name of the cmdlet class, and the source that reported
the error. In general, an error record is analogous to an event record of a Windows Event log.
The FQID is analogous to the following tuple, which identifies the class of the event record: (log
name, source, event ID).

The FQID is designed to be inspected as a single string. However, cases exist in which the error
identifier is designed to be parsed by the host application. The following example is a well-
formed fully qualified error identifier.

CommandNotFoundException,Microsoft.PowerShell.Commands.GetCommandCommand.

In the previous example, the first token is the error identifier, which is followed by the name of
the cmdlet class. The error identifier can be a single token, or it can be a dot-separated
identifier that allows for branching on inspection of the identifier. Do not use white space or
punctuation in the error identifier. It is especially important not to use a comma; a comma is
used by Windows PowerShell to separate the identifier and the cmdlet class name.

Other Information
The System.Management.Automation.ErrorRecord object might also provide information that
describes the environment in which the error occurred. This information includes items such as
error details, invocation information, and the target object that was being processed when the
error occurred. Although this information might be useful to the host application, it is not
typically used to identify the error. This information is available through the following
properties:

     System.Management.Automation.ErrorRecord.ErrorDetails

     System.Management.Automation.ErrorRecord.InvocationInfo

     System.Management.Automation.ErrorRecord.TargetObject

See Also
     System.Management.Automation.ErrorRecord

     System.Management.Automation.ErrorCategory

     System.Management.Automation.ErrorCategoryinfo

     System.Management.Automation.Cmdlet.WriteError

<!-- p.1594 -->

     System.Management.Automation.Cmdlet.ThrowTerminatingError*

     Adding Non-Terminating Error Reporting to Your Cmdlet

     Windows PowerShell Error Reporting

     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1595 -->

Background Jobs
Cmdlets can perform their action internally or as a Windows PowerShellbackground job. When a
cmdlet runs as a background job, the work is done asynchronously in its own thread separate
from the pipeline thread that the cmdlet is using. From the user perspective, when a cmdlet
runs as a background job, the command prompt returns immediately even if the job takes an
extended amount of time to complete, and the user can continue without interruption while
the job runs.

Background Jobs, Child Jobs, and the Job
Repository
The job object that is returned by the cmdlets that support background jobs defines the job.
(The Start-Job cmdlet also returns a job object.) The name of the job, an identifier that is used
to specify the job, the state information, and the child jobs are included in this definition. The
job does not perform any of the work. Each background job has at least one child job because
the child job performs the actual work. When you run a cmdlet so that the work is performed
as a background job, the cmdlet must add the job and the child jobs to a common repository,
referred to as the job repository.

For more information about how background jobs are handled at the command line, see the
following:

     about_Jobs

     about_Job_Details

     about_Remote_Jobs

Writing a Cmdlet That Runs as a Background Job
To write a cmdlet that can be run as a background job, you must complete the following tasks:

     Define an AsJob [switch] parameter so that the user can decide whether to run the
     cmdlet as a background job.

     Create an object that derives from the System.Management.Automation.Job class. This
     object can be a custom job object or a job object provided by Windows PowerShell, such

<!-- p.1596 -->

      as a System.Management.Automation.PSEventJob object.

      In a record processing method, add an if statement that detects whether the cmdlet
      should run as a background job.

      For custom job objects, implement the job class.

      Return the appropriate objects, depending on whether the cmdlet is run as a background
      job.

For a code example, see How to Support Jobs.

Background Job-Related APIs
The following APIs are provided by Windows PowerShell to manage background jobs.

System.Management.Automation.Job Derives custom job objects. This is an abstract class.

System.Management.Automation.JobRepository Manages and provides information about the
current active background jobs.

System.Management.Automation.JobState Defines the state of the background job. States
include Started, Running, and Stopped.

System.Management.Automation.JobStateInfo Provides information about the state of a
background job and, if the last state change was caused by an error, the reason the job entered
its current state.

System.Management.Automation.JobStateEventArgs Provides the arguments for an event that
is raised when a background job changes state.

Windows PowerShell Job Cmdlets
The following cmdlets are provided by Windows PowerShell to manage background jobs.

Get-Job

Gets Windows PowerShell background jobs that are running in the current session.

Receive-Job

Gets the results of the Windows PowerShell background jobs in the current session.

<!-- p.1597 -->

Remove-Job

Deletes a Windows PowerShell background job.

Start-Job

Starts a Windows PowerShell background job.

Stop-Job

Stops a Windows PowerShell background job.

Wait-Job

Suppresses the command prompt until one or all of the Windows PowerShell background jobs
running in the session are complete.

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 04/08/2026

<!-- p.1598 -->

Invoking Cmdlets and Scripts Within a
Cmdlet
A cmdlet can invoke other cmdlets and scripts from within the input processing method of the
cmdlet. This allows you to add the functionality of existing cmdlets and scripts to your cmdlet
without having to rewrite the code.

The Invoke Method
All cmdlets can invoke an existing cmdlet by calling the
System.Management.Automation.Cmdlet.Invoke method from within an input processing
method, such as System.Management.Automation.Cmdlet.BeginProcessing, that is overridden
by the cmdlet. However, you can invoke only those cmdlets that derive directly from the
System.Management.Automation.Cmdlet class. You cannot invoke a cmdlet that derives from
the System.Management.Automation.PSCmdlet class.

The System.Management.Automation.Cmdlet.Invoke* method has the following variants.

System.Management.Automation.Cmdlet.Invoke This variant invokes the cmdlet object and
returns a collection of "T" type objects.

System.Management.Automation.Cmdlet.Invoke This variant invokes the cmdlet object and
returns a strongly typed enumerator. This variant allows the user to use the objects in the
collection to perform custom operations.

Examples
                                                                                       ﾉ   Expand table

 Example                     Description

 Invoking Cmdlets Within a   This example shows how to invoke a cmdlet from within another cmdlet.
 Cmdlet

 Invoking Scripts Within a   This example shows how to invoke a script that is supplied to the cmdlet
 Cmdlet                      from within another cmdlet.

See Also

<!-- p.1599 -->

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1600 -->

Cmdlet Sets
When you design your cmdlets, you might encounter cases in which you need to perform
several actions on the same piece of data. For example, you might need to get and set data or
start and stop a process. Although you will need to create separate cmdlets to perform each
action, your cmdlet design should include a base class from which the classes for the individual
cmdlets are derived.

Keep the following things in mind when implementing a base class.

      Declare any common parameters used by all the derived cmdlets in the base class.

      Add cmdlet-specific parameters to the appropriate cmdlet class.

      Override the appropriate input processing method in the base class.

      Declare the System.Management.Automation.CmdletAttribute attribute on all cmdlet
      classes, but do not declare it on the base class.

      Implement a System.Management.Automation.PSSnapIn or
      System.Management.Automation.CustomPSSnapIn class whose name and description
      reflects the set of cmdlets.

Example
The following example shows the implementation of a base class that is used by Get-Proc and
Stop-Proc cmdlet that derive from the same base class.

 C#

 using System;
 using System.Diagnostics;
 using System.Management.Automation;                      //Windows PowerShell namespace.

 namespace Microsoft.Samples.PowerShell.Commands
 {

    #region ProcessCommands

    /// <summary>
    /// This class implements a Stop-Proc cmdlet. The parameters
    /// for this cmdlet are defined by the BaseProcCommand class.
    /// </summary>
