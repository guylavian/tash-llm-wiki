---
title: "How to use this documentation — pages 1681-1720"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1681-1720
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1681-1720
family: powershell
documentKind: "doc"
abstract: "} catch (Exception e) { if ((e is Win32Exception) || (e is SystemException) || (e is InvalidOperationException)) { // This process could not be stopped so write // a non-terminating error. string message = String.Format(\"{0} {1} {2}\", \"Could not stop process \\\"\", processName, \"\\"
---

# How to use this documentation — pages 1681-1720

<!-- p.1681 -->

            }
            catch (Exception e)
            {
              if ((e is Win32Exception) || (e is SystemException) ||
                  (e is InvalidOperationException))
              {
                // This process could not be stopped so write
                // a non-terminating error.
                string message = String.Format("{0} {1} {2}",
                                 "Could not stop process \"", processName,
                                 "\".");
                WriteError(new ErrorRecord(e, message,
                           ErrorCategory.CloseError, process));
                           continue;
              } // if ((e is...
              else throw;
            } // catch

         // If the PassThru parameter argument is
         // True, pass the terminated process on.
         if (passThru)
         {
           WriteObject(process);
         }
     } // foreach (Process...
   } // foreach (string...
 } // ProcessRecord

Calling the ShouldProcess Method
The input processing method of your cmdlet should call the
System.Management.Automation.Cmdlet.ShouldProcess method to confirm execution of an
operation before a change (for example, deleting files) is made to the running state of the
system. This allows the Windows PowerShell runtime to supply the correct "WhatIf" and
"Confirm" behavior within the shell.

  ７ Note

  If a cmdlet states that it supports should process and fails to make the
  System.Management.Automation.Cmdlet.ShouldProcess call, the user might modify the
  system unexpectedly.

The call to System.Management.Automation.Cmdlet.ShouldProcess sends the name of the
resource to be changed to the user, with the Windows PowerShell runtime taking into account
any command-line settings or preference variables in determining what should be displayed to
the user.

<!-- p.1682 -->

The following example shows the call to
System.Management.Automation.Cmdlet.ShouldProcess from the override of the
System.Management.Automation.Cmdlet.ProcessRecord method in the sample Stop-Proc
cmdlet.

 C#

 if (!ShouldProcess(string.Format("{0} ({1})", processName,
                    process.Id)))
 {
   continue;
 }

Calling the ShouldContinue Method
The call to the System.Management.Automation.Cmdlet.ShouldContinue method sends a
secondary message to the user. This call is made after the call to
System.Management.Automation.Cmdlet.ShouldProcess returns true and if the Force
parameter was not set to true . The user can then provide feedback to say whether the
operation should be continued. Your cmdlet calls
System.Management.Automation.Cmdlet.ShouldContinue as an additional check for potentially
dangerous system modifications or when you want to provide yes-to-all and no-to-all options
to the user.

The following example shows the call to
System.Management.Automation.Cmdlet.ShouldContinue from the override of the
System.Management.Automation.Cmdlet.ProcessRecord method in the sample Stop-Proc
cmdlet.

 C#

 if (criticalProcess &&!force)
 {
   string message = String.Format
         ("The process \"{0}\" is a critical process and should not be stopped. Are
 you sure you wish to stop the process?",
         processName);

    // It is possible that ProcessRecord is called multiple times
    // when the Name parameter receives objects as input from the
    // pipeline. So to retain YesToAll and NoToAll input that the
    // user may enter across multiple calls to ProcessRecord, this
    // information is stored as private members of the cmdlet.
    if (!ShouldContinue(message, "Warning!",

<!-- p.1683 -->

                          ref yesToAll,
                          ref noToAll))
    {
      continue;
    }
  } // if (criticalProcess...

Stopping Input Processing
The input processing method of a cmdlet that makes system modifications must provide a way
of stopping the processing of input. In the case of this Stop-Proc cmdlet, a call is made from
the System.Management.Automation.Cmdlet.ProcessRecord method to the
System.Diagnostics.Process.Kill* method. Because the PassThru parameter is set to true ,
System.Management.Automation.Cmdlet.ProcessRecord also calls
System.Management.Automation.Cmdlet.WriteObject to send the process object to the
pipeline.

Code Sample
For the complete C# sample code, see StopProcessSample01 Sample.

Defining Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet may need to define its own type, or the cmdlet may need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting.

Building the Cmdlet
After implementing a cmdlet, it must be registered with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications.

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, you can test it by running it
on the command line. Here are several tests that test the Stop-Proc cmdlet. For more
information about using cmdlets from the command line, see the Running commands in the
shell.

<!-- p.1684 -->

Start Windows PowerShell and use the Stop-Proc cmdlet to stop processing as shown
below. Because the cmdlet specifies the Name parameter as mandatory, the cmdlet
queries for the parameter.

 PowerShell

 PS> Stop-Proc

The following output appears.

 Cmdlet Stop-Proc at command pipeline position 1
 Supply values for the following parameters:
 Name[0]:

Now let's use the cmdlet to stop the process named "NOTEPAD". The cmdlet asks you to
confirm the action.

 PowerShell

 PS> Stop-Proc -Name notepad

The following output appears.

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Stop-Proc" on Target "notepad (4996)".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
 is "Y"): Y

Use Stop-Proc as shown to stop the critical process named "WINLOGON". You are
prompted and warned about performing this action because it will cause the operating
system to reboot.

 PowerShell

 PS> Stop-Proc -Name Winlogon

The following output appears.

<!-- p.1685 -->

       Output

       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "winlogon (656)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): Y
       Warning!
       The process " winlogon " is a critical process and should not be stopped. Are
       you sure you wish to stop the process?
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): N

     Let's now try to stop the WINLOGON process without receiving a warning. Be aware that
     this command entry uses the Force parameter to override the warning.

       PowerShell

       PS> Stop-Proc -Name winlogon -Force

     The following output appears.

       Output

       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "winlogon (656)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): N

See Also
     Adding Parameters that Process Command-Line Input
     Extending Object Types and Formatting
     How to Register Cmdlets, Providers, and Host Applications
     Windows PowerShell SDK
     Cmdlet Samples

Last updated on 02/24/2026

<!-- p.1686 -->

Adding User Messages to Your Cmdlet
Cmdlets can write several kinds of messages that can be displayed to the user by the Windows
PowerShell runtime. These messages include the following types:

      Verbose messages that contain general user information.

      Debug messages that contain troubleshooting information.

      Warning messages that contain a notification that the cmdlet is about to perform an
      operation that can have unexpected results.

      Progress report messages that contain information about how much work the cmdlet has
      completed when performing an operation that takes a long time.

There are no limits to the number of messages that your cmdlet can write or the type of
messages that your cmdlet writes. Each message is written by making a specific call from within
the input processing method of your cmdlet.

Defining the Cmdlet
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. Any sort of cmdlet can write user notifications from its input
processing methods; so, in general, you can name this cmdlet using any verb that indicates
what system modifications the cmdlet performs. For more information about approved cmdlet
verbs, see Cmdlet Verb Names.

The Stop-Proc cmdlet is designed to modify the system; therefore, the
System.Management.Automation.CmdletAttribute declaration for the .NET class must include
the SupportsShouldProcess attribute keyword and be set to true .

The following code is the definition for this Stop-Proc cmdlet class. For more information about
this definition, see Creating a Cmdlet that Modifies the System.

 C#

 [Cmdlet(VerbsLifecycle.Stop, "proc",
         SupportsShouldProcess = true)]
 public class StopProcCommand : Cmdlet

<!-- p.1687 -->

Defining Parameters for System Modification
The Stop-Proc cmdlet defines three parameters: Name , Force , and PassThru . For more
information about defining these parameters, see Creating a Cmdlet that Modifies the System.

Here is the parameter declaration for the Stop-Proc cmdlet.

 C#

 [Parameter(
             Position = 0,
             Mandatory = true,
             ValueFromPipeline = true,
             ValueFromPipelineByPropertyName = true
 )]
 public string[] Name
 {
    get { return processNames; }
    set { processNames = value; }
 }
 private string[] processNames;

 /// <summary>
 /// Specify the Force parameter that allows the user to override
 /// the ShouldContinue call to force the stop operation. This
 /// parameter should always be used with caution.
 /// </summary>
 [Parameter]
 public SwitchParameter Force
 {
   get { return force; }
   set { force = value; }
 }
 private bool force;

 /// <summary>
 /// Specify the PassThru parameter that allows the user to specify
 /// that the cmdlet should pass the process object down the pipeline
 /// after the process has been stopped.
 /// </summary>
 [Parameter]
 public SwitchParameter PassThru
 {
   get { return passThru; }
   set { passThru = value; }
 }
 private bool passThru;

Overriding an Input Processing Method

<!-- p.1688 -->

Your cmdlet must override an input processing method, most often it will be
System.Management.Automation.Cmdlet.ProcessRecord. This Stop-Proc cmdlet overrides the
System.Management.Automation.Cmdlet.ProcessRecord input processing method. In this
implementation of the Stop-Proc cmdlet, calls are made to write verbose messages, debug
messages, and warning messages.

  ７ Note

  For more information about how this method calls the
  System.Management.Automation.Cmdlet.ShouldProcess and
  System.Management.Automation.Cmdlet.ShouldContinue methods, see Creating a
  Cmdlet that Modifies the System.

Writing a Verbose Message
The System.Management.Automation.Cmdlet.WriteVerbose method is used to write general
user-level information that is unrelated to specific error conditions. The system administrator
can then use that information to continue processing other commands. In addition, any
information written using this method should be localized as needed.

The following code from this Stop-Proc cmdlet shows two calls to the
System.Management.Automation.Cmdlet.WriteVerbose method from the override of the
System.Management.Automation.Cmdlet.ProcessRecord method.

 C#

 message = String.Format("Attempting to stop process \"{0}\".", name);
 WriteVerbose(message);

 C#

 message = String.Format("Stopped process \"{0}\", pid {1}.",
                         processName, process.Id);

 WriteVerbose(message);

Writing a Debug Message
The System.Management.Automation.Cmdlet.WriteDebug method is used to write debug
messages that can be used to troubleshoot the operation of the cmdlet. The call is made from

<!-- p.1689 -->

an input processing method.

  ７ Note

  Windows PowerShell also defines a Debug parameter that presents both verbose and
  debug information. If your cmdlet supports this parameter, it does not need to call
  System.Management.Automation.Cmdlet.WriteDebug in the same code that calls
  System.Management.Automation.Cmdlet.WriteVerbose.

The following two sections of code from the sample Stop-Proc cmdlet show calls to the
System.Management.Automation.Cmdlet.WriteDebug method from the override of the
System.Management.Automation.Cmdlet.ProcessRecord method.

This debug message is written immediately before
System.Management.Automation.Cmdlet.ShouldProcess is called.

 C#

 message =
           String.Format("Acquired name for pid {0} : \"{1}\"",
                        process.Id, processName);
 WriteDebug(message);

This debug message is written immediately before
System.Management.Automation.Cmdlet.WriteObject is called.

 C#

 message =
          String.Format("Writing process \"{0}\" to pipeline",
          processName);
 WriteDebug(message);
 WriteObject(process);

Windows PowerShell automatically routes any
System.Management.Automation.Cmdlet.WriteDebug calls to the tracing infrastructure and
cmdlets. This allows the method calls to be traced to the hosting application, a file, or a
debugger without your having to do any extra development work within the cmdlet. The
following command-line entry implements a tracing operation.

PS> Trace-Expression Stop-Proc -File proc.log -Command Stop-Proc notepad

<!-- p.1690 -->

Writing a Warning Message
The System.Management.Automation.Cmdlet.WriteWarning method is used to write a warning
when the cmdlet is about to perform an operation that might have an unexpected result, for
example, overwriting a read-only file.

The following code from the sample Stop-Proc cmdlet shows the call to the
System.Management.Automation.Cmdlet.WriteWarning method from the override of the
System.Management.Automation.Cmdlet.ProcessRecord method.

 C#

  if (criticalProcess)
  {
    message =
              String.Format("Stopping the critical process \"{0}\".",
                            processName);
    WriteWarning(message);
 } // if (criticalProcess...

Writing a Progress Message
The System.Management.Automation.Cmdlet.WriteProgress is used to write progress messages
when cmdlet operations take an extended amount of time to complete. A call to
System.Management.Automation.Cmdlet.WriteProgress passes a
System.Management.Automation.Progressrecord object that is sent to the hosting application
for rendering to the user.

  ７ Note

  This Stop-Proc cmdlet does not include a call to the
  System.Management.Automation.Cmdlet.WriteProgress method.

The following code is an example of a progress message written by a cmdlet that is attempting
to copy an item.

 C#

 int myId = 0;
 string myActivity = "Copy-item: Copying *.* to C:\abc";
 string myStatus = "Copying file bar.txt";
 ProgressRecord pr = new ProgressRecord(myId, myActivity, myStatus);

<!-- p.1691 -->

 WriteProgress(pr);

 pr.RecordType = ProgressRecordType.Completed;
 WriteProgress(pr);

Code Sample
For the complete C# sample code, see StopProcessSample02 Sample.

Define Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet might need to define its own type, or the cmdlet might need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting   .

Building the Cmdlet
After implementing a cmdlet, it must be registered with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications   .

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, you can test it by running it
on the command line. Let's test the sample Stop-Proc cmdlet. For more information about
using cmdlets from the command line, see the Getting Started with Windows PowerShell.

     The following command-line entry uses Stop-Proc to stop the process named
     "NOTEPAD", provide verbose notifications, and print debug information.

       PowerShell

       PS> Stop-Proc -Name notepad -Verbose -Debug

     The following output appears.

       VERBOSE: Attempting to stop process " notepad ".
       DEBUG: Acquired name for pid 5584 : "notepad"

<!-- p.1692 -->

       Confirm
       Continue with this operation?
       [Y] Yes [A] Yes to All [H] Halt Command      [S] Suspend   [?] Help (default is
       "Y"): Y

       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "notepad (5584)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): Y
       VERBOSE: Stopped process "notepad", pid 5584.

See Also
Create a Cmdlet that Modifies the System

How to Create a Windows PowerShell Cmdlet

Extending Object Types and Formatting

How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1693 -->

Adding Aliases, Wildcard Expansion, and
Help to Cmdlet Parameters
This section describes how to add aliases, wildcard expansion, and Help messages to the
parameters of the Stop-Proc cmdlet (described in Creating a Cmdlet that Modifies the System).

This Stop-Proc cmdlet attempts to stop processes that are retrieved using the Get-Proc cmdlet
(described in Creating Your First Cmdlet).

Defining the Cmdlet
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. Because you are writing a cmdlet to change the system, it should be
named accordingly. Because this cmdlet stops system processes, it uses the verb Stop, defined
by the System.Management.Automation.VerbsLifecycle class, with the noun Proc to indicate
process. For more information about approved cmdlet verbs, see Cmdlet Verb Names.

The following code is the class definition for this Stop-Proc cmdlet.

 C#

 [Cmdlet(VerbsLifecycle.Stop, "proc",
         SupportsShouldProcess = true)]
 public class StopProcCommand : Cmdlet

Defining Parameters for System Modification
Your cmdlet needs to define parameters that support system modifications and user feedback.
The cmdlet should define a Name parameter or equivalent so that the cmdlet will be able to
modify the system by some sort of identifier. In addition, the cmdlet should define the Force
and PassThru parameters. For more information about these parameters, see Creating a
Cmdlet that Modifies the System.

Defining a Parameter Alias
A parameter alias can be an alternate name or a well-defined 1-letter or 2-letter short name for
a cmdlet parameter. In both cases, the goal of using aliases is to simplify user entry from the

<!-- p.1694 -->

command line. Windows PowerShell supports parameter aliases through the
System.Management.Automation.AliasAttribute attribute, which uses the declaration syntax
[Alias()] .

The following code shows how an alias is added to the Name parameter.

 C#

 /// <summary>
 /// Specify the mandatory Name parameter used to identify the
 /// processes to be stopped.
 /// </summary>
 [Parameter(
             Position = 0,
             Mandatory = true,
             ValueFromPipeline = true,
             ValueFromPipelineByPropertyName = true,
             HelpMessage = "The name of one or more processes to stop. Wildcards are
 permitted."
 )]
 [Alias("ProcessName")]
 public string[] Name
 {
    get { return processNames; }
    set { processNames = value; }
 }
 private string[] processNames;

In addition to using the System.Management.Automation.AliasAttribute attribute, the Windows
PowerShell runtime performs partial name matching, even if no aliases are specified. For
example, if your cmdlet has a FileName parameter and that is the only parameter that starts
with F , the user could enter Filename , Filenam , File , Fi , or F and still recognize the entry as
the FileName parameter.

Creating Help for Parameters
Windows PowerShell allows you to create Help for cmdlet parameters. Do this for any
parameter used for system modification and user feedback. For each parameter to support
Help, you can set the HelpMessage attribute keyword in the
System.Management.Automation.ParameterAttribute attribute declaration. This keyword
defines the text to display to the user for assistance in using the parameter. You can also set
the HelpMessageBaseName keyword to identify the base name of a resource to use for the
message. If you set this keyword, you must also set the HelpMessageResourceId keyword to
specify the resource identifier.

<!-- p.1695 -->

The following code from this Stop-Proc cmdlet defines the HelpMessage attribute keyword for
the Name parameter.

 C#

 /// <summary>
 /// Specify the mandatory Name parameter used to identify the
 /// processes to be stopped.
 /// </summary>
 [Parameter(
             Position = 0,
             Mandatory = true,
             ValueFromPipeline = true,
             ValueFromPipelineByPropertyName = true,
             HelpMessage = "The name of one or more processes to stop. Wildcards are
 permitted."
 )]

Overriding an Input Processing Method
Your cmdlet must override an input processing method, most often this will be
System.Management.Automation.Cmdlet.ProcessRecord. When modifying the system, the
cmdlet should call the System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue methods to allow the user to provide
feedback before a change is made. For more information about these methods, see Creating a
Cmdlet that Modifies the System.

Supporting Wildcard Expansion
To allow the selection of multiple objects, your cmdlet can use the
System.Management.Automation.WildcardPattern and
System.Management.Automation.WildcardOptions classes to provide wildcard expansion
support for parameter input. Examples of wildcard patterns are lsa* , *.txt , and [a-c]* . Use
the back-quote character ( ` ) as an escape character when the pattern contains a character that
should be used literally.

Wildcard expansions of file and path names are examples of common scenarios where the
cmdlet may want to allow support for path inputs when the selection of multiple objects is
required. A common case is in the file system, where a user wants to see all files residing in the
current folder.

<!-- p.1696 -->

You should need a customized wildcard pattern matching implementation only rarely. In this
case, your cmdlet should support either the full POSIX 1003.2, 3.13 specification for wildcard
expansion or the following simplified subset:

      Question mark ( ? ). Matches any character at the specified location.
      Asterisk ( * ). Matches zero or more characters starting at the specified location.
      Open bracket ( [ ). Introduces a pattern bracket expression that can contain characters or
      a range of characters. If a range is required, a hyphen ( - ) is used to indicate the range.
      Close bracket ( ] ). Ends a pattern bracket expression.
      Back-quote escape character ( ` ). Indicates that the next character should be taken
      literally. Be aware that when specifying the back-quote character from the command line
      (as opposed to specifying it programmatically), the back-quote escape character must be
      specified twice.

  ７ Note

  For more information about wildcard patterns, see Supporting Wildcards in Cmdlet
  Parameters.

The following code shows how to set wildcard options and define the wildcard pattern used for
resolving the Name parameter for this cmdlet.

 C#

 WildcardOptions options = WildcardOptions.IgnoreCase |
                           WildcardOptions.Compiled;
 WildcardPattern wildcard = new WildcardPattern(name,options);

The following code shows how to test whether the process name matches the defined wildcard
pattern. Notice that, in this case, if the process name does not match the pattern, the cmdlet
continues on to get the next process name.

 C#

 if (!wildcard.IsMatch(processName))
 {
   continue;
 }

Code Sample

<!-- p.1697 -->

For the complete C# sample code, see StopProcessSample03 Sample.

Define Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet may need to define its own type, or the cmdlet may need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting   .

Building the Cmdlet
After implementing a cmdlet, it must be registered with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications   .

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, you can test it by running it
on the command line. Let's test the sample Stop-Proc cmdlet. For more information about
using cmdlets from the command line, see the Getting Started with Windows PowerShell.

     Start Windows PowerShell and use Stop-Proc to stop a process using the ProcessName
     alias for the Name parameter.

       PowerShell

       PS> Stop-Proc -ProcessName notepad

     The following output appears.

       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "notepad (3496)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): Y

     Make the following entry on the command line. Because the Name parameter is
     mandatory, you are prompted for it. Entering !? brings up the help text associated with
     the parameter.

<!-- p.1698 -->

 PowerShell

 PS> Stop-Proc

The following output appears.

 Cmdlet Stop-Proc at command pipeline position 1
 Supply values for the following parameters:
 (Type !? for Help.)
 Name[0]: !?
 The name of one or more processes to stop. Wildcards are permitted.
 Name[0]: notepad

Now make the following entry to stop all processes that match the wildcard pattern
*note* . You are prompted before stopping each process that matches the pattern.

 PowerShell

 PS> Stop-Proc -Name *note*

The following output appears.

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Stop-Proc" on Target "notepad (1112)".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
 is "Y"): Y

The following output appears.

 Confirm
 Are you sure you want to perform this action?
 Performing operation "Stop-Proc" on Target "ONENOTEM (3712)".
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
 is "Y"): N

The following output appears.

<!-- p.1699 -->

       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "ONENOTE (3592)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help (default
       is "Y"): N

See Also
     Create a Cmdlet that Modifies the System
     How to Create a Windows PowerShell Cmdlet
     Extending Object Types and Formatting
     How to Register Cmdlets, Providers, and Host Applications
     Supporting Wildcards in Cmdlet Parameters
     Windows PowerShell SDK

Last updated on 05/20/2025

<!-- p.1700 -->

Adding Parameter Sets to a Cmdlet

Things to Know About Parameter Sets
Windows PowerShell defines a parameter set as a group of parameters that operate together.
By grouping the parameters of a cmdlet, you can create a single cmdlet that can change its
functionality based on what group of parameters the user specifies.

An example of a cmdlet that uses two parameter sets to define different functionalities is the
Get-EventLog cmdlet that is provided by Windows PowerShell. This cmdlet returns different

information when the user specifies the List or LogName parameter. If the LogName parameter
is specified, the cmdlet returns information about the events in a given event log. If the List
parameter is specified, the cmdlet returns information about the log files themselves (not the
event information they contain). In this case, the List and LogName parameters identify two
separate parameter sets.

Two important things to remember about parameter sets is that the Windows PowerShell
runtime uses only one parameter set for a particular input, and that each parameter set must
have at least one parameter that is unique for that parameter set.

To illustrate that last point, this Stop-Proc cmdlet uses three parameter sets: ProcessName ,
ProcessId , and InputObject . Each of these parameter sets has one parameter that is not in the

other parameter sets. The parameter sets could share other parameters, but the cmdlet uses
the unique parameters ProcessName , ProcessId , and InputObject to identify which set of
parameters that the Windows PowerShell runtime should use.

Declaring the Cmdlet Class
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. For this cmdlet, the lifecycle verb "Stop" is used because the cmdlet
stops system processes. The noun name "Proc" is used because the cmdlet works on processes.
In the declaration below, note that the cmdlet verb and noun name are reflected in the name
of the cmdlet class.

  ７ Note

<!-- p.1701 -->

  For more information about approved cmdlet verb names, see Cmdlet Verb Names.

The following code is the class definition for this Stop-Proc cmdlet.

 C#

 [Cmdlet(VerbsLifecycle.Stop, "Proc",
         DefaultParameterSetName = "ProcessId",
         SupportsShouldProcess = true)]
 public class StopProcCommand : PSCmdlet

 VB

 <Cmdlet(VerbsLifecycle.Stop, "Proc", DefaultParameterSetName:="ProcessId", _
 SupportsShouldProcess:=True)> _
 Public Class StopProcCommand
     Inherits PSCmdlet

Declaring the Parameters of the Cmdlet
This cmdlet defines three parameters needed as input to the cmdlet (these parameters also
define the parameter sets), as well as a Force parameter that manages what the cmdlet does
and a PassThru parameter that determines whether the cmdlet sends an output object through
the pipeline. By default, this cmdlet does not pass an object through the pipeline. For more
information about these last two parameters, see Creating a Cmdlet that Modifies the System.

Declaring the Name Parameter
This input parameter allows the user to specify the names of the processes to be stopped. Note
that the ParameterSetName attribute keyword of the
System.Management.Automation.ParameterAttribute attribute specifies the ProcessName
parameter set for this parameter.

 C#

 [Parameter(
    Position = 0,
    ParameterSetName = "ProcessName",
    Mandatory = true,
    ValueFromPipeline = true,
    ValueFromPipelineByPropertyName = true,
    HelpMessage = "The name of one or more processes to stop. Wildcards are
 permitted."
 )]

<!-- p.1702 -->

 [Alias("ProcessName")]
 public string[] Name
 {
     get { return processNames; }
     set { processNames = value; }
 }
 private string[] processNames;

 VB

 <Parameter(Position:=0, ParameterSetName:="ProcessName", _
 Mandatory:=True, _
 ValueFromPipeline:=True, ValueFromPipelineByPropertyName:=True, _
 HelpMessage:="The name of one or more processes to stop. " & _
     "Wildcards are permitted."), [Alias]("ProcessName")> _
 Public Property Name() As String()
     Get
         Return processNames
     End Get
     Set(ByVal value As String())
         processNames = value
     End Set
 End Property

 Private processNames() As String

Note also that the alias "ProcessName" is given to this parameter.

Declaring the Id Parameter
This input parameter allows the user to specify the identifiers of the processes to be stopped.
Note that the ParameterSetName attribute keyword of the
System.Management.Automation.ParameterAttribute attribute specifies the ProcessId
parameter set.

 C#

 [Parameter(
             ParameterSetName = "ProcessId",
             Mandatory = true,
             ValueFromPipelineByPropertyName = true,
             ValueFromPipeline = true
 )]
 [Alias("ProcessId")]
 public int[] Id
 {
    get { return processIds; }
    set { processIds = value; }

<!-- p.1703 -->

 }
 private int[] processIds;

 VB

 <Parameter(ParameterSetName:="ProcessId", _
 Mandatory:=True, _
 ValueFromPipelineByPropertyName:=True, _
 ValueFromPipeline:=True), [Alias]("ProcessId")> _
 Public Property Id() As Integer()
     Get
         Return processIds
     End Get
     Set(ByVal value As Integer())
         processIds = value
     End Set
 End Property
 Private processIds() As Integer

Note also that the alias "ProcessId" is given to this parameter.

Declaring the InputObject Parameter
This input parameter allows the user to specify an input object that contains information about
the processes to be stopped. Note that the ParameterSetName attribute keyword of the
System.Management.Automation.ParameterAttribute attribute specifies the InputObject
parameter set for this parameter.

 C#

 [Parameter(
            ParameterSetName = "InputObject",
            Mandatory = true,
            ValueFromPipeline = true)]
 public Process[] InputObject
 {
   get { return inputObject; }
   set { inputObject = value; }
 }
 private Process[] inputObject;

 VB

 <Parameter(ParameterSetName:="InputObject", _
 Mandatory:=True, ValueFromPipeline:=True)> _
 Public Property InputObject() As Process()
     Get
         Return myInputObject

<!-- p.1704 -->

     End Get
     Set(ByVal value As Process())
         myInputObject = value
     End Set
 End Property
 Private myInputObject() As Process

Note also that this parameter has no alias.

Declaring Parameters in Multiple Parameter Sets
Although there must be a unique parameter for each parameter set, parameters can belong to
more than one parameter set. In these cases, give the shared parameter a
System.Management.Automation.ParameterAttribute attribute declaration for each set to
which that the parameter belongs. If a parameter is in all parameter sets, you only have to
declare the parameter attribute once and do not need to specify the parameter set name.

Overriding an Input Processing Method
Every cmdlet must override an input processing method, most often this will be the
System.Management.Automation.Cmdlet.ProcessRecord method. In this cmdlet, the
System.Management.Automation.Cmdlet.ProcessRecord method is overridden so that the
cmdlet can process any number of processes. It contains a Select statement that calls a
different method based on which parameter set the user has specified.

 C#

 protected override void ProcessRecord()
 {
   switch (ParameterSetName)
   {
     case "ProcessName":
          ProcessByName();
          break;

      case "ProcessId":
           ProcessById();
           break;

      case "InputObject":
           foreach (Process process in inputObject)
           {
             SafeStopProcess(process);
           }
           break;

      default:

<!-- p.1705 -->

          throw new ArgumentException("Bad ParameterSet Name");
   } // switch (ParameterSetName...
 } // ProcessRecord

 VB

 Protected Overrides Sub ProcessRecord()
     Select Case ParameterSetName
         Case "ProcessName"
             ProcessByName()

          Case "ProcessId"
              ProcessById()

          Case "InputObject"
              Dim process As Process
              For Each process In myInputObject
                  SafeStopProcess(process)
              Next process

          Case Else
              Throw New ArgumentException("Bad ParameterSet Name")
      End Select

 End Sub 'ProcessRecord ' ProcessRecord

The Helper methods called by the Select statement are not described here, but you can see
their implementation in the complete code sample in the next section.

Code Sample
For the complete C# sample code, see StopProcessSample04 Sample.

Defining Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet might need to define its own type, or the cmdlet might need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting   .

Building the Cmdlet
After implementing a cmdlet, you must register it with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications   .

<!-- p.1706 -->

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, test it by running it on the
command line. Here are some tests that show how the ProcessId and InputObject parameters
can be used to test their parameter sets to stop a process.

     With Windows PowerShell started, run the Stop-Proc cmdlet with the ProcessId
     parameter set to stop a process based on its identifier. In this case, the cmdlet is using the
     ProcessId parameter set to stop the process.

       PS> Stop-Proc -Id 444
       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "notepad (444)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend              [?] Help (default
       is "Y"): Y

     With Windows PowerShell started, run the Stop-Proc cmdlet with the InputObject
     parameter set to stop processes on the Notepad object retrieved by the Get-Process
     command.

       PS> Get-Process notepad | Stop-Proc
       Confirm
       Are you sure you want to perform this action?
       Performing operation "Stop-Proc" on Target "notepad (444)".
       [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend              [?] Help (default
       is "Y"): N

See Also
Creating a Cmdlet that Modifies the System

How to Create a Windows PowerShell Cmdlet

Extending Object Types and Formatting

How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell SDK

<!-- p.1707 -->

Last updated on 05/20/2025

<!-- p.1708 -->

SelectStr Tutorial
This section provides a tutorial for creating the Select-Str cmdlet, which is very similar to the
Select-String cmdlet provided by Windows PowerShell. This tutorial provides fragments of code
that illustrate how cmdlets are implemented, and an explanation of the code.

Topic in this Tutorial
Creating a Cmdlet to Access a Data Store This section describes how to create a cmdlet that
selects strings that are in a file or object.

See Also
Creating a Cmdlet to Access a Data Store

Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1709 -->

Creating a Cmdlet to Access a Data Store
This section describes how to create a cmdlet that accesses stored data by way of a Windows
PowerShell provider. This type of cmdlet uses the Windows PowerShell provider infrastructure
of the Windows PowerShell runtime and, therefore, the cmdlet class must derive from the
System.Management.Automation.PSCmdlet base class.

The Select-Str cmdlet described here can locate and select strings in a file or object. The
patterns used to identify the string can be specified explicitly through the Path parameter of
the cmdlet or implicitly through the Script parameter.

The cmdlet is designed to use any Windows PowerShell provider that derives from
System.Management.Automation.Provider.IContentCmdletProvider. For example, the cmdlet
can specify the FileSystem provider or the Variable provider that is provided by Windows
PowerShell. For more information aboutWindows PowerShell providers, see Designing Your
Windows PowerShell provider.

Defining the Cmdlet Class
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. This cmdlet detects certain strings, so the verb name chosen here is
"Select", defined by the System.Management.Automation.VerbsCommon class. The noun name
"Str" is used because the cmdlet acts upon strings. In the declaration below, note that the
cmdlet verb and noun name are reflected in the name of the cmdlet class. For more
information about approved cmdlet verbs, see Cmdlet Verb Names.

The .NET class for this cmdlet must derive from the System.Management.Automation.PSCmdlet
base class, because it provides the support needed by the Windows PowerShell runtime to
expose the Windows PowerShell provider infrastructure. Note that this cmdlet also makes use
of the .NET Framework regular expressions classes, such as
System.Text.RegularExpressions.Regex.

The following code is the class definition for this Select-Str cmdlet.

 C#

 [Cmdlet(VerbsCommon.Select, "Str", DefaultParameterSetName="PatternParameterSet")]
 public class SelectStringCommand : PSCmdlet

<!-- p.1710 -->

This cmdlet defines a default parameter set by adding the DefaultParameterSetName attribute
keyword to the class declaration. The default parameter set PatternParameterSet is used when
the Script parameter is not specified. For more information about this parameter set, see the
Pattern and Script parameter discussion in the following section.

Defining Parameters for Data Access
This cmdlet defines several parameters that allow the user to access and examine stored data.
These parameters include a Path parameter that indicates the location of the data store, a
Pattern parameter that specifies the pattern to be used in the search, and several other

parameters that support how the search is performed.

  ７ Note

  For more information about the basics of defining parameters, see [Adding Parameters
  that Process Command Line Input][04].

Declaring the Path Parameter
To locate the data store, this cmdlet must use a Windows PowerShell path to identify the
Windows PowerShell provider that is designed to access the data store. Therefore, it defines a
Path parameter of type string array to indicate the location of the provider.

 C#

 [Parameter(
            Position = 0,
            ParameterSetName = "ScriptParameterSet",
            Mandatory = true)]
 [Parameter(
            Position = 0,
            ParameterSetName = "PatternParameterSet",
            ValueFromPipeline = true,
            Mandatory = true)]
            [Alias("PSPath")]
 public string[] Path
 {
   get { return paths; }
   set { paths = value; }
 }
 private string[] paths;

Note that this parameter belongs to two different parameter sets and that it has an alias.

<!-- p.1711 -->

Two System.Management.Automation.ParameterAttribute attributes declare that the Path
parameter belongs to the ScriptParameterSet and the PatternParameterSet . For more
information about parameter sets, see Adding Parameter Sets to a Cmdlet.

The System.Management.Automation.AliasAttribute attribute declares a PSPath alias for the
Path parameter. Declaring this alias is strongly recommended for consistency with other

cmdlets that access Windows PowerShell providers. For more information aboutWindows
PowerShell paths, see "PowerShell Path Concepts" in How Windows PowerShell Works           .

Declaring the Pattern Parameter
To specify the patterns to search for, this cmdlet declares a Pattern parameter that is an array
of strings. A positive result is returned when any of the patterns are found in the data store.
Note that these patterns can be compiled into an array of compiled regular expressions or an
array of wildcard patterns used for literal searches.

 C#

 [Parameter(
            Position = 1,
            ParameterSetName = "PatternParameterSet",
            Mandatory = true)]
 public string[] Pattern
 {
   get { return patterns; }
   set { patterns = value; }
 }
 private string[] patterns;
 private Regex[] regexPattern;
 private WildcardPattern[] wildcardPattern;

When this parameter is specified, the cmdlet uses the default parameter set
PatternParameterSet . In this case, the cmdlet uses the patterns specified here to select strings.

In contrast, the Script parameter could also be used to provide a script that contains the
patterns. The Script and Pattern parameters define two separate parameter sets, so they are
mutually exclusive.

Declaring Search Support Parameters
This cmdlet defines the following support parameters that can be used to modify the search
capabilities of the cmdlet.

<!-- p.1712 -->

The Script parameter specifies a script block that can be used to provide an alternate search
mechanism for the cmdlet. The script must contain the patterns used for matching and return a
System.Management.Automation.PSObject object. Note that this parameter is also the unique
parameter that identifies the ScriptParameterSet parameter set. When the Windows
PowerShell runtime sees this parameter, it uses only parameters that belong to the
ScriptParameterSet parameter set.

 C#

 [Parameter(
            Position = 1,
            ParameterSetName = "ScriptParameterSet",
            Mandatory = true)]
 public ScriptBlock Script
 {
   set { script = value; }
   get { return script; }
 }
 ScriptBlock script;

The SimpleMatch parameter is a [switch] parameter that indicates whether the cmdlet is to
explicitly match the patterns as they are supplied. When the user specifies the parameter at the
command line ( true ), the cmdlet uses the patterns as they are supplied. If the parameter is not
specified ( false ), the cmdlet uses regular expressions. The default for this parameter is false .

 C#

 [Parameter]
 public SwitchParameter SimpleMatch
 {
   get { return simpleMatch; }
   set { simpleMatch = value; }
 }
 private bool simpleMatch;

The CaseSensitive parameter is a [switch] parameter that indicates whether a case-sensitive
search is performed. When the user specifies the parameter at the command line ( true ), the
cmdlet checks for the uppercase and lowercase of characters when comparing patterns. If the
parameter is not specified ( false ), the cmdlet does not distinguish between uppercase and
lowercase. For example "MyFile" and "myfile" would both be returned as positive hits. The
default for this parameter is false .

 C#

<!-- p.1713 -->

 [Parameter]
 public SwitchParameter CaseSensitive
 {
   get { return caseSensitive; }
   set { caseSensitive = value; }
 }
 private bool caseSensitive;

The Exclude and Include parameters identify items that are explicitly excluded from or
included in the search. By default, the cmdlet will search all items in the data store. However, to
limit the search performed by the cmdlet, these parameters can be used to explicitly indicate
items to be included in the search or omitted.

 C#

 [Parameter]
 public SwitchParameter CaseSensitive
 {
   get { return caseSensitive; }
   set { caseSensitive = value; }
 }
 private bool caseSensitive;

 C#

 [Parameter]
 [ValidateNotNullOrEmpty]
 public string[] Include
 {
   get
   {
     return includeStrings;
   }
   set
   {
     includeStrings = value;

     this.include = new WildcardPattern[includeStrings.Length];
     for (int i = 0; i < includeStrings.Length; i++)
     {
       this.include[i] = new WildcardPattern(includeStrings[i],
 WildcardOptions.IgnoreCase);
     }
   }
 }

 internal string[] includeStrings = null;
 internal WildcardPattern[] include = null;

<!-- p.1714 -->

Declaring Parameter Sets
This cmdlet uses two parameter sets ( ScriptParameterSet and PatternParameterSet , which is
the default) as the names of two parameter sets used in data access. PatternParameterSet is
the default parameter set and is used when the Pattern parameter is specified.
ScriptParameterSet is used when the user specifies an alternate search mechanism through

the Script parameter. For more information about parameter sets, see Adding Parameter Sets
to a Cmdlet.

Overriding Input Processing Methods
Cmdlets must override one or more of the input processing methods for the
System.Management.Automation.PSCmdlet class. For more information about the input
processing methods, see Creating Your First Cmdlet.

This cmdlet overrides the System.Management.Automation.Cmdlet.BeginProcessing method to
build an array of compiled regular expressions at startup. This increases performance during
searches that do not use simple matching.

 C#

 protected override void BeginProcessing()
 {
   WriteDebug("Validating patterns.");
   if (patterns != null)
   {
     foreach(string pattern in patterns)
     {
       if (pattern == null)
       ThrowTerminatingError(new ErrorRecord(
                             new ArgumentNullException(
                             "Search pattern cannot be null."),
                             "NullSearchPattern",
                             ErrorCategory.InvalidArgument,
                             pattern)
                             );
     }

      WriteVerbose("Search pattern(s) are valid.");

      // If a simple match is not specified, then
      // compile the regular expressions once.
      if (!simpleMatch)
      {
        WriteDebug("Compiling search regular expressions.");

        RegexOptions regexOptions = RegexOptions.Compiled;

<!-- p.1715 -->

        if (!caseSensitive)
           regexOptions |= RegexOptions.Compiled;
        regexPattern = new Regex[patterns.Length];

        for (int i = 0; i < patterns.Length; i++)
        {
          try
          {
            regexPattern[i] = new Regex(patterns[i], regexOptions);
          }
          catch (ArgumentException ex)
          {
            ThrowTerminatingError(new ErrorRecord(
                          ex,
                          "InvalidRegularExpression",
                          ErrorCategory.InvalidArgument,
                          patterns[i]
                       ));
          }
        } //Loop through patterns to create RegEx objects.

        WriteVerbose("Pattern(s) compiled into regular expressions.");
      }// If not a simple match.

      // If a simple match is specified, then compile the
      // wildcard patterns once.
      else
      {
        WriteDebug("Compiling search wildcards.");

        WildcardOptions wildcardOptions = WildcardOptions.Compiled;

        if (!caseSensitive)
        {
          wildcardOptions |= WildcardOptions.IgnoreCase;
        }

        wildcardPattern = new WildcardPattern[patterns.Length];
        for (int i = 0; i < patterns.Length; i++)
        {
          wildcardPattern[i] =
                       new WildcardPattern(patterns[i], wildcardOptions);
        }

       WriteVerbose("Pattern(s) compiled into wildcard expressions.");
     }// If match is a simple match.
   }// If valid patterns are available.
 }// End of function BeginProcessing().

This cmdlet also overrides the System.Management.Automation.Cmdlet.ProcessRecord method
to process the string selections that the user makes on the command line. It writes the results
of string selection in the form of a custom object by calling a private MatchString method.

<!-- p.1716 -->

C#

protected override void ProcessRecord()
{
  UInt64 lineNumber = 0;
  MatchInfo result;
  ArrayList nonMatches = new ArrayList();

  // Walk the list of paths and search the contents for
  // any of the specified patterns.
  foreach (string psPath in paths)
  {
    // Once the filepaths are expanded, we may have more than one
    // path, so process all referenced paths.
    foreach(PathInfo path in
             SessionState.Path.GetResolvedPSPathFromPSPath(psPath)
           )
    {
      WriteVerbose("Processing path " + path.Path);

      // Check if the path represents one of the items to be
      // excluded. If so, continue to next path.
      if (!MeetsIncludeExcludeCriteria(path.ProviderPath))
         continue;

      // Get the content reader for the item(s) at the
      // specified path.
      Collection<IContentReader> readerCollection = null;
      try
      {
        readerCollection =
                    this.InvokeProvider.Content.GetReader(path.Path);
      }
      catch (PSNotSupportedException ex)
      {
        WriteError(new ErrorRecord(ex,
                   "ContentAccessNotSupported",
                    ErrorCategory.NotImplemented,
                    path.Path)
                   );
        return;
      }

      foreach(IContentReader reader in readerCollection)
      {
        // Reset the line number for this path.
        lineNumber = 0;

        // Read in a single block (line in case of a file)
        // from the object.
        IList items = reader.Read(1);

        // Read and process one block(line) at a time until
        // no more blocks(lines) exist.

<!-- p.1717 -->

       while (items != null && items.Count == 1)
       {
         // Increment the line number each time a line is
         // processed.
         lineNumber++;

          String message = String.Format("Testing line {0} : {1}",
                                        lineNumber, items[0]);

          WriteDebug(message);

          result = SelectString(items[0]);

          if (result != null)
          {
            result.Path = path.Path;
            result.LineNumber = lineNumber;

            WriteObject(result);
          }
          else
          {
            // Add the block(line) that did not match to the
            // collection of non matches , which will be stored
            // in the SessionState variable $NonMatches
            nonMatches.Add(items[0]);
          }

          // Get the next line from the object.
          items = reader.Read(1);

        }// While loop for reading one line at a time.
      }// Foreach loop for reader collection.
    }// Foreach loop for processing referenced paths.
  }// Foreach loop for walking of path list.

  // Store the list of non-matches in the
  // session state variable $NonMatches.
  try
  {
    this.SessionState.PSVariable.Set("NonMatches", nonMatches);
  }
  catch (SessionStateUnauthorizedAccessException ex)
  {
    WriteError(new ErrorRecord(ex,
               "CannotWriteVariableNonMatches",
               ErrorCategory.InvalidOperation,
               nonMatches)
              );
  }

}// End of protected override void ProcessRecord().

<!-- p.1718 -->

Accessing Content
Your cmdlet must open the provider indicated by the Windows PowerShell path so that it can
access the data. The System.Management.Automation.SessionState object for the runspace is
used for access to the provider, while the
System.Management.Automation.PSCmdlet.InvokeProvider* property of the cmdlet is used to
open the provider. Access to content is provided by retrieval of the
System.Management.Automation.ProviderIntrinsics object for the provider opened.

This sample Select-Str cmdlet uses the
System.Management.Automation.ProviderIntrinsics.Content* property to expose the content to
scan. It can then call the
System.Management.Automation.ContentCmdletProviderIntrinsics.GetReader* method, passing
the required Windows PowerShell path.

Code Sample
The following code shows the implementation of this version of this Select-Str cmdlet. Note
that this code includes the cmdlet class, private methods used by the cmdlet, and the Windows
PowerShell snap-in code used to register the cmdlet. For more information about registering
the cmdlet, see Building the Cmdlet.

 C#

 //
 // Copyright (c) 2006 Microsoft Corporation. All rights reserved.
 //
 // THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
 // ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 // THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 // PARTICULAR PURPOSE.
 //
 using System;
 using System.Text.RegularExpressions;
 using System.Collections;
 using System.Collections.ObjectModel;
 using System.Management.Automation;
 using System.Management.Automation.Provider;
 using System.ComponentModel;

 namespace Microsoft.Samples.PowerShell.Commands
 {
   #region SelectStringCommand
   /// <summary>
   /// This cmdlet searches through PSObjects for particular patterns.

<!-- p.1719 -->

  /// </summary>
  /// <remarks>
  /// This cmdlet can be used to search any object, such as a file or a
  /// variable, whose provider exposes methods for reading and writing
  /// content.
  /// </remarks>
  [Cmdlet(VerbsCommon.Select, "Str",
DefaultParameterSetName="PatternParameterSet")]
  public class SelectStringCommand : PSCmdlet
  {
    #region Parameters
    /// <summary>
    /// Declare a Path parameter that specifies where the data is stored.
    /// This parameter must specify a PowerShell that indicates the
    /// PowerShell provider that is used to access the objects to be
    /// searched for matching patterns. This parameter should also have
    /// a PSPath alias to provide consistency with other cmdlets that use
    /// PowerShell providers.
    /// </summary>
    /// <value>Path of the object(s) to search.</value>
    [Parameter(
               Position = 0,
               ParameterSetName = "ScriptParameterSet",
               Mandatory = true)]
    [Parameter(
               Position = 0,
               ParameterSetName = "PatternParameterSet",
               ValueFromPipeline = true,
               Mandatory = true)]
               [Alias("PSPath")]
    public string[] Path
    {
      get { return paths; }
      set { paths = value; }
    }
    private string[] paths;

    /// <summary>
    /// Declare a Pattern parameter that specifies the pattern(s)
    /// used to find matching patterns in the string representation
    /// of the objects. A positive result will be returned
    /// if any of the patterns are found in the objects.
    /// </summary>
    /// <remarks>
    /// The patterns will be compiled into an array of wildcard
    /// patterns for a simple match (literal string matching),
    /// or the patterns will be converted into an array of compiled
    /// regular expressions.
    /// </remarks>
    /// <value>Array of patterns to search.</value>
    [Parameter(
               Position = 1,
               ParameterSetName = "PatternParameterSet",
               Mandatory = true)]
    public string[] Pattern

<!-- p.1720 -->

{
    get { return patterns; }
    set { patterns = value; }
}
private string[] patterns;
private Regex[] regexPattern;
private WildcardPattern[] wildcardPattern;

/// <summary>
/// Declare a Script parameter that specifies a script block
/// that is called to perform the matching operations
/// instead of the matching performed by the cmdlet.
/// </summary>
/// <value>Script block that will be called for matching</value>
[Parameter(
           Position = 1,
           ParameterSetName = "ScriptParameterSet",
           Mandatory = true)]
public ScriptBlock Script
{
  set { script = value; }
  get { return script; }
}
ScriptBlock script;

/// <summary>
/// Declare a switch parameter that specifies if the pattern(s) are used
/// literally. If not (default), searching is
/// done using regular expressions.
/// </summary>
/// <value>If True, a literal pattern is used.</value>
[Parameter]
public SwitchParameter SimpleMatch
{
  get { return simpleMatch; }
  set { simpleMatch = value; }
}
private bool simpleMatch;

/// <summary>
/// Declare a switch parameter that specifies if a case-sensitive
/// search is performed. If not (default), a case-insensitive search
/// is performed.
/// </summary>
/// <value>If True, a case-sensitive search is made.</value>
[Parameter]
public SwitchParameter CaseSensitive
{
  get { return caseSensitive; }
  set { caseSensitive = value; }
}
private bool caseSensitive;

/// <summary>
/// Declare an Include parameter that species which
