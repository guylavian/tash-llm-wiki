---
title: "How to use this documentation — pages 1641-1680"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1641-1680
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1641-1680
family: powershell
documentKind: "doc"
abstract: "Microsoft.PowerShell.Commands.GetProcessCommand is created along with the string that contains the arguments that are used when the cmdlet is invoked. C# GetProcessCommand gp = new GetProcessCommand(); gp.Name = new string[] { \"[a-t]*\" }; 3. Call the System.Management.Automation"
---

# How to use this documentation — pages 1641-1680

<!-- p.1641 -->

      Microsoft.PowerShell.Commands.GetProcessCommand is created along with the string
      that contains the arguments that are used when the cmdlet is invoked.

       C#

       GetProcessCommand gp = new GetProcessCommand();
       gp.Name = new string[] { "[a-t]*" };

   3. Call the System.Management.Automation.Cmdlet.Invoke* method to invoke the Get-
      Process cmdlet.

       C#

           foreach (Process p in gp.Invoke<Process>())
           {
             Console.WriteLine(p.ToString());
           }
       }

Example
In this example, the Get-Process cmdlet is invoked from within the
System.Management.Automation.Cmdlet.BeginProcessing method of a cmdlet.

 C#

 using System;
 using System.Diagnostics;
 using System.Management.Automation;       // PowerShell assembly.
 using Microsoft.PowerShell.Commands;      // PowerShell cmdlets assembly you want to
 call.

 namespace SendGreeting
 {
   // Declare the class as a cmdlet and specify an
   // appropriate verb and noun for the cmdlet name.
   [Cmdlet(VerbsCommunications.Send, "GreetingInvoke")]
   public class SendGreetingInvokeCommand : Cmdlet
   {
     // Declare the parameters for the cmdlet.
     [Parameter(Mandatory = true)]
     public string Name { get; set; }

      // Override the BeginProcessing method to invoke
      // the Get-Process cmdlet.
      protected override void BeginProcessing()
      {
        GetProcessCommand gp = new GetProcessCommand();

<!-- p.1642 -->

             gp.Name = new string[] { "[a-t]*" };
             foreach (Process p in gp.Invoke<Process>())
             {
               WriteVerbose(p.ToString());
             }
         }

         // Override the ProcessRecord method to process
         // the supplied user name and write out a
         // greeting to the user by calling the WriteObject
         // method.
         protected override void ProcessRecord()
         {
           WriteObject("Hello " + Name + "!");
         }
     }
 }

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1643 -->

How to invoke a PSCmdlet from within a
PSCmdlet
This example shows how to invoke a script based cmdlet or binary cmdlet inheriting from
[System.Management.Automation.PSCmdlet] from within a binary cmdlet. In this example, the

new cmdlet Get-ClipboardReverse calls Get-Clipboard to get the contents of the clipboard.
The Get-ClipboardReverse reverses the order of the characters and returns the reversed string.

  ７ Note

  The [PSCmdlet] class differs from the [Cmdlet] class. [PSCmdlet] implementations use
  runspace context information so you must invoke another cmdlet using the PowerShell
  pipeline API. In [Cmdlet] implementations you can call the cmdlet's .NET API directly. For
  an example, see How to invoke a Cmdlet from within a Cmdlet.

To invoke a cmdlet from within a PSCmdlet
   1. Ensure that the namespace for the [System.Management.Automation.PowerShell] API is
     referenced. In this example, the following namespaces are added.

       C#

       using System.Management.Automation;      // PowerShell assembly.
       using System.Text;

   2. To invoke a command from within another binary cmdlet you must use the [PowerShell]
     API to construct a new pipeline and add the cmdlet to be invoked. Call the
     System.Management.Automation.PowerShell.Invoke<T>() method to invoke the pipeline.

       C#

       using var ps = PowerShell.Create(RunspaceMode.CurrentRunspace);
       ps.AddCommand("Get-Clipboard").AddParameter("Raw");
       var output = ps.Invoke<string>();

Example

<!-- p.1644 -->

To invoke a script based cmdlet or binary cmdlet inheriting from [PSCmdlet] you must build a
PowerShell pipeline with the command and parameters you want to execute, then invoke the
pipeline.

  C#

  using System;
  using System.Management.Automation;       // PowerShell assembly.
  using System.Text;

  namespace ClipboardReverse
  {
      [Cmdlet(VerbsCommon.Get,"ClipboardReverse")]
      [OutputType(typeof(string))]
      public class ClipboardReverse : PSCmdlet
      {
          protected override void EndProcessing()
          {
              using var ps = PowerShell.Create(RunspaceMode.CurrentRunspace);
              ps.AddCommand("Get-Clipboard").AddParameter("Raw");
              var output = ps.Invoke<string>();
              if (ps.HadErrors)
              {
                  WriteError(new ErrorRecord(ps.Streams.Error[0].Exception,
                             "Get-Clipboard Error", ErrorCategory.NotSpecified,
  null));
              }
              else
              {
                  var sb = new StringBuilder();
                  foreach (var text in output)
                  {
                      sb.Append(text);
                  }

                      var reversed = sb.ToString().ToCharArray();
                      Array.Reverse(reversed);
                      WriteObject(new string(reversed));
                 }
            }
       }
  }

See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1645 -->

Tutorials for Writing Cmdlets
This section contains tutorials for writing cmdlets. These tutorials include the code needed to
write the cmdlets, plus an explanation of why the code is needed. These topics will be very
helpful for those who are just starting to write cmdlets.

  ） Important

  For those who want code examples with less description, see Cmdlet Samples.

In This Section
GetProc Tutorial - This tutorial describes how to define a cmdlet class and add basic
functionality such as adding parameters and reporting errors. The cmdlet described in this
tutorial is very similar to the Get-Process cmdlet provided by Windows PowerShell.

StopProc Tutorial - This tutorial describes how to define a cmdlet and add functionality such as
user prompts, wildcard support, and the use of parameter sets. The cmdlet described here
performs the same task as the Stop-Process cmdlet provided by Windows PowerShell.

SelectStr Tutorial - This tutorial describes how to define a cmdlet that accesses a data store.
The cmdlet described here performs the same task as the Select-String cmdlet provided by
Windows PowerShell.

See Also
GetProc Tutorial

StopProc Tutorial

SelectStr Tutorial

Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1646 -->

GetProc Tutorial
This section provides a tutorial for creating a Get-Proc cmdlet that is very similar to the Get-
Process cmdlet provided by Windows PowerShell. This tutorial provides fragments of code that
illustrate how cmdlets are implemented, and an explanation of the code.

Topics in this Tutorial
The topics in this tutorial are designed to be read sequentially, with each topic building on
what was discussed in the previous topic.

      Creating a Cmdlet without Parameters: This section describes how to create a cmdlet
      that retrieves information from the local computer without the use of parameters, and
      then writes the information to the pipeline.

      Adding Parameters that Process Command-Line Input: This section describes how to
      add a parameter to the Get-Proc cmdlet so that the cmdlet can process input based on
      explicit objects passed to the cmdlet. The implementation described here retrieves
      processes based on their name, and then writes the information to the pipeline.

      Adding Parameters that Process Pipeline Input: This section describes how to add a
      parameter to the Get-Proc cmdlet so that the cmdlet can process objects passed to it
      through the pipeline. The implementation cmdlet described here retrieves processes
      based on objects passed to the cmdlet, and then writes the information to the pipeline.

      Adding Non-terminating Error Reporting to Your Cmdlet: This section describes how to
      add non-terminating error reporting to a cmdlet. The implementation described here
      detects non-terminating errors that occur when processing input, and writes an error
      record to the error stream.

See Also
      Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1647 -->

Creating a Cmdlet without Parameters
This section describes how to create a cmdlet that retrieves information from the local
computer without the use of parameters, and then writes the information to the pipeline. The
cmdlet described here is a Get-Proc cmdlet that retrieves information about the processes of
the local computer, and then displays that information at the command line.

  ７ Note

  Be aware that when writing cmdlets, the Windows PowerShell® reference assemblies are
  downloaded onto disk (by default at C:\Program Files\Reference
  Assemblies\Microsoft\WindowsPowerShell\v1.0). They are not installed in the Global
  Assembly Cache (GAC).

Naming the Cmdlet
A cmdlet name consists of a verb that indicates the action the cmdlet takes and a noun that
indicates the items that the cmdlet acts upon. Because this sample Get-Proc cmdlet retrieves
process objects, it uses the verb "Get", defined by the
System.Management.Automation.VerbsCommon enumeration, and the noun "Proc" to indicate
that the cmdlet works on process items.

When naming cmdlets, do not use any of the following characters: # , () {} [] & - /\ $ ; : " '<> | ?
@`.

Choosing a Noun
You should choose a noun that is specific. It is best to use a singular noun prefixed with a
shortened version of the product name. An example cmdlet name of this type is " Get-
SQLServer ".

Choosing a Verb
You should use a verb from the set of approved cmdlet verb names. For more information
about the approved cmdlet verbs, see Cmdlet Verb Names.

Defining the Cmdlet Class

<!-- p.1648 -->

Once you have chosen a cmdlet name, define a .NET class to implement the cmdlet. Here is the
class definition for this sample Get-Proc cmdlet:

  C#

  [Cmdlet(VerbsCommon.Get, "Proc")]
    public class GetProcCommand : Cmdlet

  VB

  <Cmdlet(VerbsCommon.Get, "Proc")> _
  Public Class GetProcCommand
      Inherits Cmdlet

Notice that previous to the class definition, the
System.Management.Automation.CmdletAttribute attribute, with the syntax [Cmdlet(verb,
noun, ...)] , is used to identify this class as a cmdlet. This is the only required attribute for all

cmdlets, and it allows the Windows PowerShell runtime to call them correctly. You can set
attribute keywords to further declare the class if necessary. Be aware that the attribute
declaration for our sample GetProcCommand class declares only the noun and verb names for
the Get-Proc cmdlet.

  ７ Note

  For all Windows PowerShell attribute classes, the keywords that you can set correspond to
  properties of the attribute class.

When naming the class of the cmdlet, it is a good practice to reflect the cmdlet name in the
class name. To do this, use the form "VerbNounCommand" and replace "Verb" and "Noun" with
the verb and noun used in the cmdlet name. As is shown in the previous class definition, the
sample Get-Proc cmdlet defines a class called GetProcCommand, which derives from the
System.Management.Automation.Cmdlet base class.

  ） Important

  If you want to define a cmdlet that accesses the Windows PowerShell runtime directly,
  your .NET class should derive from the System.Management.Automation.PSCmdlet base
  class. For more information about this class, see Creating a Cmdlet that Defines
  Parameter Sets.

<!-- p.1649 -->

  ７ Note

  The class for a cmdlet must be explicitly marked as public. Classes that are not marked as
  public will default to internal and will not be found by the Windows PowerShell runtime.

Windows PowerShell uses the Microsoft.PowerShell.Commands namespace for its cmdlet
classes. It is recommended to place your cmdlet classes in a Commands namespace of your API
namespace, for example, xxx.PS.Commands.

Overriding an Input Processing Method
The System.Management.Automation.Cmdlet class provides three main input processing
methods, at least one of which your cmdlet must override. For more information about how
Windows PowerShell processes records, see How Windows PowerShell Works         .

For all types of input, the Windows PowerShell runtime calls
System.Management.Automation.Cmdlet.BeginProcessing to enable processing. If your cmdlet
must perform some preprocessing or setup, it can do this by overriding this method.

  ７ Note

  Windows PowerShell uses the term "record" to describe the set of parameter values
  supplied when a cmdlet is called.

If your cmdlet accepts pipeline input, it must override the
System.Management.Automation.Cmdlet.ProcessRecord method, and optionally the
System.Management.Automation.Cmdlet.EndProcessing method. For example, a cmdlet might
override both methods if it gathers all input using
System.Management.Automation.Cmdlet.ProcessRecord and then operates on the input as a
whole rather than one element at a time, as the Sort-Object cmdlet does.

If your cmdlet does not take pipeline input, it should override the
System.Management.Automation.Cmdlet.EndProcessing method. Be aware that this method is
frequently used in place of System.Management.Automation.Cmdlet.BeginProcessing when the
cmdlet cannot operate on one element at a time, as is the case for a sorting cmdlet.

Because this sample Get-Proc cmdlet must receive pipeline input, it overrides the
System.Management.Automation.Cmdlet.ProcessRecord method and uses the default

<!-- p.1650 -->

implementations for System.Management.Automation.Cmdlet.BeginProcessing and
System.Management.Automation.Cmdlet.EndProcessing. The
System.Management.Automation.Cmdlet.ProcessRecord override retrieves processes and
writes them to the command line using the
System.Management.Automation.Cmdlet.WriteObject method.

 C#

 protected override void ProcessRecord()
 {
   // Get the current processes
   Process[] processes = Process.GetProcesses();

     // Write the processes to the pipeline making them available
     // to the next cmdlet. The second parameter of this call tells
     // PowerShell to enumerate the array, and send one process at a
     // time to the pipeline.
     WriteObject(processes, true);
 }

 VB

 Protected Overrides Sub ProcessRecord()

      '/ Get the current processes.
      Dim processes As Process()
      processes = Process.GetProcesses()

      '/ Write the processes to the pipeline making them available
      '/ to the next cmdlet. The second parameter of this call tells
      '/ PowerShell to enumerate the array, and send one process at a
      '/ time to the pipeline.
      WriteObject(processes, True)

 End Sub 'ProcessRecord

Things to Remember About Input Processing

      The default source for input is an explicit object (for example, a string) provided by the
      user on the command line. For more information, see Creating a Cmdlet to Process
      Command Line Input.

      An input processing method can also receive input from the output object of an
      upstream cmdlet on the pipeline. For more information, see Creating a Cmdlet to Process
      Pipeline Input. Be aware that your cmdlet can receive input from a combination of
      command-line and pipeline sources.

<!-- p.1651 -->

     The downstream cmdlet might not return for a long time, or not at all. For that reason,
     the input processing method in your cmdlet should not hold locks during calls to
     System.Management.Automation.Cmdlet.WriteObject, especially locks for which the
     scope extends beyond the cmdlet instance.

  ） Important

  Cmdlets should never call System.Console.Writeline* or its equivalent.

     Your cmdlet might have object variables to clean up when it is finished processing (for
     example, if it opens a file handle in the
     System.Management.Automation.Cmdlet.BeginProcessing method and keeps the handle
     open for use by System.Management.Automation.Cmdlet.ProcessRecord). It is important
     to remember that the Windows PowerShell runtime does not always call the
     System.Management.Automation.Cmdlet.EndProcessing method, which should perform
     object cleanup.

For example, System.Management.Automation.Cmdlet.EndProcessing might not be called if the
cmdlet is canceled midway or if a terminating error occurs in any part of the cmdlet. Therefore,
a cmdlet that requires object cleanup should implement the complete System.IDisposable
pattern, including the finalizer, so that the runtime can call both
System.Management.Automation.Cmdlet.EndProcessing and System.IDisposable.Dispose* at
the end of processing.

Code Sample
For the complete C# sample code, see GetProcessSample01 Sample.

Defining Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet might need to define its own type, or the cmdlet might need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting      .

Building the Cmdlet

<!-- p.1652 -->

After implementing a cmdlet, you must register it with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications    .

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, you can test it by running it
on the command line. The code for our sample Get-Proc cmdlet is small, but it still uses the
Windows PowerShell runtime and an existing .NET object, which is enough to make it useful.
Let's test it to better understand what Get-Proc can do and how its output can be used. For
more information about using cmdlets from the command line, see the Getting Started with
Windows PowerShell.

   1. Start Windows PowerShell, and get the current processes running on the computer.

       PowerShell

       Get-Proc

     The following output appears.

       Output

       Handles    NPM(K)   PM(K)   WS(K)   VS(M)   CPU(s)   Id   ProcessName
       -------    ------   -----   -----   -----   ------   --   ----------
       254        7        7664    12048   66      173.75   1200 QCTRAY
       32         2        1372    2628    31        0.04   1860 DLG
       271        6        1216    3688    33        0.03   3816 lg
       27         2        560     1920    24        0.01   1768 TpScrex
       ...

   2. Assign a variable to the cmdlet results for easier manipulation.

       PowerShell

       $p=Get-Proc

   3. Get the number of processes.

       PowerShell

       $p.Length

<!-- p.1653 -->

  The following output appears.

    Output

    63

4. Retrieve a specific process.

    PowerShell

    $p[6]

  The following output appears.

    Output

    Handles    NPM(K)   PM(K)     WS(K)   VS(M)   CPU(s)   Id     ProcessName
    -------    ------   -----     -----   -----   ------   --     -----------
    1033       3        2400      3336    35      0.53     1588   rundll32

5. Get the start time of this process.

    PowerShell

    $p[6].StartTime

  The following output appears.

    Output

    Tuesday, July 26, 2005 9:34:15 AM

    PowerShell

    $p[6].StartTime.DayOfYear

    Output

    207

6. Get the processes for which the handle count is greater than 500, and sort the result.

    PowerShell

<!-- p.1654 -->

       $p | Where-Object {$_.HandleCount -gt 500 } | Sort-Object HandleCount

     The following output appears.

       Output

       Handles   NPM(K)   PM(K)   WS(K)   VS(M) CPU(s)    Id   ProcessName
       -------   ------   -----   -----   ----- ------    --   ----------
       568       14       2164    4972    39     5.55     824 svchost
       716        7       2080    5332    28    25.38     468 csrss
       761       21       33060   56608   440 393.56      3300 WINWORD
       791       71       7412    4540    59     3.31     492 winlogon
       ...

   7. Use the Get-Member cmdlet to list the properties available for each process.

       PowerShell

       $p | Get-Member -MemberType Property

       Output

           TypeName: System.Diagnostics.Process

     The following output appears.

       Output

       Name                        MemberType Definition
       ----                        ---------- ----------
       BasePriority                Property   System.Int32 BasePriority {get;}
       Container                   Property   System.ComponentModel.IContainer Conta...
       EnableRaisingEvents         Property   System.Boolean EnableRaisingEvents {ge...
       ...

See Also
Creating a Cmdlet to Process Command Line Input

Creating a Cmdlet to Process Pipeline Input

How to Create a Windows PowerShell Cmdlet

Extending Object Types and Formatting

<!-- p.1655 -->

How Windows PowerShell Works

How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell Reference

Cmdlet Samples

Last updated on 05/20/2025

<!-- p.1656 -->

Adding Parameters That Process
Command-Line Input
One source of input for a cmdlet is the command line. This topic describes how to add a
parameter to the Get-Proc cmdlet (which is described in Creating Your First Cmdlet) so that the
cmdlet can process input from the local computer based on explicit objects passed to the
cmdlet. The Get-Proc cmdlet described here retrieves processes based on their names, and
then displays information about the processes at a command prompt.

Defining the Cmdlet Class
The first step in cmdlet creation is cmdlet naming and the declaration of the .NET Framework
class that implements the cmdlet. This cmdlet retrieves process information, so the verb name
chosen here is "Get." (Almost any sort of cmdlet that is capable of retrieving information can
process command-line input.) For more information about approved cmdlet verbs, see Cmdlet
Verb Names.

Here's the class declaration for the Get-Proc cmdlet. Details about this definition are provided
in Creating Your First Cmdlet.

 C#

 [Cmdlet(VerbsCommon.Get, "proc")]
 public class GetProcCommand: Cmdlet

 VB

 <Cmdlet(VerbsCommon.Get, "Proc")> _
 Public Class GetProcCommand
     Inherits Cmdlet

Declaring Parameters
A cmdlet parameter enables the user to provide input to the cmdlet. In the following example,
Get-Proc and Get-Member are the names of pipelined cmdlets, and MemberType is a parameter

for the Get-Member cmdlet. The parameter has the argument "property."

PS> Get-Proc ; Get-Member -MemberType Property

<!-- p.1657 -->

To declare parameters for a cmdlet, you must first define the properties that represent the
parameters. In the Get-Proc cmdlet, the only parameter is Name , which in this case represents
the name of the .NET Framework process object to retrieve. Therefore, the cmdlet class defines
a property of type string to accept an array of names.

Here's the parameter declaration for the Name parameter of the Get-Proc cmdlet.

 C#

 /// <summary>
 /// Specify the cmdlet Name parameter.
 /// </summary>
   [Parameter(Position = 0)]
   [ValidateNotNullOrEmpty]
   public string[] Name
   {
     get { return processNames; }
     set { processNames = value; }
   }
   private string[] processNames;

    #endregion Parameters

 VB

 <Parameter(Position:=0), ValidateNotNullOrEmpty()> _
 Public Property Name() As String()
     Get
         Return processNames
     End Get

      Set(ByVal value As String())
          processNames = value
      End Set

 End Property

To inform the Windows PowerShell runtime that this property is the Name parameter, a
System.Management.Automation.ParameterAttribute attribute is added to the property
definition. The basic syntax for declaring this attribute is [Parameter()] .

  ７ Note

  A parameter must be explicitly marked as public. Parameters that are not marked as public
  default to internal and are not found by the Windows PowerShell runtime.

<!-- p.1658 -->

This cmdlet uses an array of strings for the Name parameter. If possible, your cmdlet should also
define a parameter as an array, because this allows the cmdlet to accept more than one item.

Things to Remember About Parameter Definitions

     Predefined Windows PowerShell parameter names and data types should be reused as
     much as possible to ensure that your cmdlet is compatible with Windows PowerShell
     cmdlets. For example, if all cmdlets use the predefined Id parameter name to identify a
     resource, user will easily understand the meaning of the parameter, regardless of what
     cmdlet they are using. Basically, parameter names follow the same rules as those used for
     variable names in the common language runtime (CLR). For more information about
     parameter naming, see Cmdlet Parameter Names.

     Windows PowerShell reserves a few parameter names to provide a consistent user
     experience. Do not use these parameter names: WhatIf , Confirm , Verbose , Debug , Warn ,
     ErrorAction , ErrorVariable , OutVariable , and OutBuffer . Additionally, the following

     aliases for these parameter names are reserved: vb , db , ea , ev , ov , and ob .

     Name is a simple and common parameter name, recommended for use in your cmdlets. It

     is better to choose a parameter name like this than a complex name that is unique to a
     specific cmdlet and hard to remember.

     Parameters are case-insensitive in Windows PowerShell, although by default the shell
     preserves case. Case-sensitivity of the arguments depends on the operation of the
     cmdlet. Arguments are passed to a parameter as specified at the command line.

     For examples of other parameter declarations, see Cmdlet Parameters.

Declaring Parameters as Positional or Named
A cmdlet must set each parameter as either a positional or named parameter. Both kinds of
parameters accept single arguments, multiple arguments separated by commas, and Boolean
settings. A Boolean parameter, also called a switch, handles only Boolean settings. The switch is
used to determine the presence of the parameter. The recommended default is false .

The sample Get-Proc cmdlet defines the Name parameter as a positional parameter with
position 0. This means that the first argument the user enters on the command line is
automatically inserted for this parameter. If you want to define a named parameter, for which
the user must specify the parameter name from the command line, leave the Position
keyword out of the attribute declaration.

<!-- p.1659 -->

  ７ Note

  Unless parameters must be named, we recommend that you make the most-used
  parameters positional so that users will not have to type the parameter name.

Declaring Parameters as Mandatory or Optional
A cmdlet must set each parameter as either an optional or a mandatory parameter. In the
sample Get-Proc cmdlet, the Name parameter is defined as optional because the Mandatory
keyword is not set in the attribute declaration.

Supporting Parameter Validation
The sample Get-Proc cmdlet adds an input validation attribute,
System.Management.Automation.ValidateNotNullOrEmptyAttribute, to the Name parameter to
enable validation that the input is neither null nor empty. This attribute is one of several
validation attributes provided by Windows PowerShell. For examples of other validation
attributes, see Validating Parameter Input.

 [Parameter(Position = 0)]
 [ValidateNotNullOrEmpty]
 public string[] Name

Overriding an Input Processing Method
If your cmdlet is to handle command-line input, it must override the appropriate input
processing methods. The basic input processing methods are introduced in Creating Your First
Cmdlet.

The Get-Proc cmdlet overrides the System.Management.Automation.Cmdlet.ProcessRecord
method to handle the Name parameter input provided by the user or a script. This method gets
the processes for each requested process name, or all for processes if no name is provided.
Notice that in System.Management.Automation.Cmdlet.ProcessRecord, the call to
System.Management.Automation.Cmdlet.WriteObject is the output mechanism for sending
output objects to the pipeline. The second parameter of this call, enumerateCollection , is set to

<!-- p.1660 -->

true to inform the Windows PowerShell runtime to enumerate the output array of process

objects and write one process at a time to the command line.

 C#

 protected override void ProcessRecord()
 {
   // If no process names are passed to the cmdlet, get all processes.
   if (processNames == null)
   {
     // Write the processes to the pipeline making them available
     // to the next cmdlet. The second argument of this call tells
     // PowerShell to enumerate the array, and send one process at a
     // time to the pipeline.
     WriteObject(Process.GetProcesses(), true);
   }
   else
   {
     // If process names are passed to the cmdlet, get and write
     // the associated processes.
     foreach (string name in processNames)
     {
       WriteObject(Process.GetProcessesByName(name), true);
     }
   }
 }

 VB

 Protected Overrides Sub ProcessRecord()

      '/ If no process names are passed to the cmdlet, get all processes.
      If processNames Is Nothing Then
          Dim processes As Process()
          processes = Process.GetProcesses()
      End If

      '/ If process names are specified, write the processes to the
      '/ pipeline to display them or make them available to the next cmdlet.

      For Each name As String In processNames
          '/ The second parameter of this call tells PowerShell to enumerate the
          '/ array, and send one process at a time to the pipeline.
          WriteObject(Process.GetProcessesByName(name), True)
      Next

 End Sub 'ProcessRecord

Code Sample

<!-- p.1661 -->

For the complete C# sample code, see GetProcessSample02 Sample.

Defining Object Types and Formatting
Windows PowerShell passes information between cmdlets by using .NET Framework objects.
Consequently, a cmdlet might need to define its own type, or a cmdlet might need to extend
an existing type provided by another cmdlet. For more information about defining new types
or extending existing types, see Extending Object Types and Formatting.

Building the Cmdlet
After you implement a cmdlet, you must register it with Windows PowerShell by using a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications.

Testing the Cmdlet
When your cmdlet is registered with Windows PowerShell, you can test it by running it on the
command line. Here are two ways to test the code for the sample cmdlet. For more information
about using cmdlets from the command line, see Getting Started with Windows PowerShell.

     At the Windows PowerShell prompt, use the following command to list the Internet
     Explorer process, which is named "IEXPLORE."

       PowerShell

       Get-Proc -Name iexplore

     The following output appears.

       Output

       Handles   NPM(K)   PM(K)   WS(K)   VS(M)   CPU(s)   Id    ProcessName
       -------   ------   -----   -----   -----    ------ --    -----------
           354       11   10036   18992     85    0.67   3284    iexplore

     To list the Internet Explorer, Outlook, and Notepad processes named "IEXPLORE,"
     "OUTLOOK," and "NOTEPAD," use the following command. If there are multiple processes,
     all of them are displayed.

       PowerShell

<!-- p.1662 -->

       Get-Proc -Name iexplore, outlook, notepad

     The following output appears.

       Handles     NPM(K)    PM(K)   WS(K)   VS(M) CPU(s)   Id   ProcessName
       -------     ------    -----   -----   ----- ------   --   -----------
           732         21    24696    5000     138   2.25 2288   iexplore
           715         19    20556   14116     136   1.78 3860   iexplore
          3917         62    74096   58112     468 191.56 1848   OUTLOOK
            39          2     1024    3280      30   0.09 1444   notepad
            39          2     1024     356      30   0.08 3396   notepad

See Also
Adding Parameters that Process Pipeline Input

Creating Your First Cmdlet

Extending Object Types and Formatting

How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell Reference

Cmdlet Samples

Last updated on 05/20/2025

<!-- p.1663 -->

Adding Parameters that Process Pipeline
Input
One source of input for a cmdlet is an object on the pipeline that originates from an upstream
cmdlet. This section describes how to add a parameter to the Get-Proc cmdlet (described in
Creating Your First Cmdlet) so that the cmdlet can process pipeline objects.

This Get-Proc cmdlet uses a Name parameter that accepts input from a pipeline object, retrieves
process information from the local computer based on the supplied names, and then displays
information about the processes at the command line.

Defining the Cmdlet Class
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. This cmdlet retrieves process information, so the verb name chosen
here is "Get". (Almost any sort of cmdlet that is capable of retrieving information can process
command-line input.) For more information about approved cmdlet verbs, see Cmdlet Verb
Names.

The following is the definition for this Get-Proc cmdlet. Details of this definition are given in
Creating Your First Cmdlet.

 C#

 [Cmdlet(VerbsCommon.Get, "proc")]
 public class GetProcCommand : Cmdlet

 VB

 <Cmdlet(VerbsCommon.Get, "Proc")> _
 Public Class GetProcCommand
     Inherits Cmdlet

Defining Input from the Pipeline
This section describes how to define input from the pipeline for a cmdlet. This Get-Proc cmdlet
defines a property that represents the Name parameter as described in Adding Parameters that

<!-- p.1664 -->

Process Command Line Input. (See that topic for general information about declaring
parameters.)

However, when a cmdlet needs to process pipeline input, it must have its parameters bound to
input values by the Windows PowerShell runtime. To do this, you must add the
ValueFromPipeline keyword or add the ValueFromPipelineByProperty keyword to the

System.Management.Automation.ParameterAttribute attribute declaration. Specify the
ValueFromPipeline keyword if the cmdlet accesses the complete input object. Specify the

ValueFromPipelineByProperty if the cmdlet accesses only a property of the object.

Here is the parameter declaration for the Name parameter of this Get-Proc cmdlet that accepts
pipeline input.

 C#

 [Parameter(
    Position = 0,
    ValueFromPipeline = true,
    ValueFromPipelineByPropertyName = true)]
 [ValidateNotNullOrEmpty]
 public string[] Name
 {
    get { return this.processNames; }
    set { this.processNames = value; }
 }

 VB

 <Parameter(Position:=0, ValueFromPipeline:=True, _
 ValueFromPipelineByPropertyName:=True), ValidateNotNullOrEmpty()> _
 Public Property Name() As String()
     Get
         Return processNames
     End Get

      Set(ByVal value As String())
          processNames = value
      End Set

 End Property

The previous declaration sets the ValueFromPipeline keyword to true so that the Windows
PowerShell runtime will bind the parameter to the incoming object if the object is the same
type as the parameter, or if it can be coerced to the same type. The
ValueFromPipelineByPropertyName keyword is also set to true so that the Windows PowerShell

runtime will check the incoming object for a Name property. If the incoming object has such a

<!-- p.1665 -->

property, the runtime will bind the Name parameter to the Name property of the incoming
object.

  ７ Note

  The setting of the ValueFromPipeline attribute keyword for a parameter takes precedence
  over the setting for the ValueFromPipelineByPropertyName keyword.

Overriding an Input Processing Method
If your cmdlet is to handle pipeline input, it needs to override the appropriate input processing
methods. The basic input processing methods are introduced in Creating Your First Cmdlet.

This Get-Proc cmdlet overrides the System.Management.Automation.Cmdlet.ProcessRecord
method to handle the Name parameter input provided by the user or a script. This method will
get the processes for each requested process name or all processes if no name is provided.
Notice that within System.Management.Automation.Cmdlet.ProcessRecord, the call to
WriteObject(System.Object,System.Boolean) is the output mechanism for sending output
objects to the pipeline. The second parameter of this call, enumerateCollection , is set to true
to tell the Windows PowerShell runtime to enumerate the array of process objects, and write
one process at a time to the command line.

 C#

 protected override void ProcessRecord()
 {
   // If no process names are passed to the cmdlet, get all processes.
   if (processNames == null)
   {
       // Write the processes to the pipeline making them available
       // to the next cmdlet. The second argument of this call tells
       // PowerShell to enumerate the array, and send one process at a
       // time to the pipeline.
       WriteObject(Process.GetProcesses(), true);
   }
   else
   {
     // If process names are passed to the cmdlet, get and write
     // the associated processes.
     foreach (string name in processNames)
     {
       WriteObject(Process.GetProcessesByName(name), true);
     } // End foreach (string name...).

<!-- p.1666 -->

     }
 }

 VB

 Protected Overrides Sub ProcessRecord()
     Dim processes As Process()

         '/ If no process names are passed to the cmdlet, get all processes.
         If processNames Is Nothing Then
             processes = Process.GetProcesses()
         Else

             '/ If process names are specified, write the processes to the
             '/ pipeline to display them or make them available to the next cmdlet.
             For Each name As String In processNames
                  '/ The second parameter of this call tells PowerShell to enumerate the
                  '/ array, and send one process at a time to the pipeline.
                  WriteObject(Process.GetProcessesByName(name), True)
             Next
         End If

 End Sub 'ProcessRecord

Code Sample
For the complete C# sample code, see GetProcessSample03 Sample.

Defining Object Types and Formatting
Windows PowerShell passes information between cmdlets using .NET objects. Consequently, a
cmdlet may need to define its own type, or the cmdlet may need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting   .

Building the Cmdlet
After implementing a cmdlet it must be registered with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications   .

Testing the Cmdlet

<!-- p.1667 -->

When your cmdlet has been registered with Windows PowerShell, test it by running it on the
command line. For example, test the code for the sample cmdlet. For more information about
using cmdlets from the command line, see the Getting Started with Windows PowerShell.

     At the Windows PowerShell prompt, enter the following commands to retrieve the
     process names through the pipeline.

       PowerShell

       PS> type ProcessNames | Get-Proc

     The following output appears.

       Handles   NPM(K)   PM(K)   WS(K) VS(M)    CPU(s)     Id   ProcessName
       -------   ------   -----   ----- -----    ------     --   -----------
           809       21   40856    4448    147     9.50   2288   iexplore
           737       21   26036   16348    144    22.03   3860   iexplore
            39        2    1024     388     30     0.08   3396   notepad
          3927       62   71836   26984    467   195.19   1848   OUTLOOK

     Enter the following lines to get the process objects that have a Name property from the
     processes called "IEXPLORE". This example uses the Get-Process cmdlet (provided by
     Windows PowerShell) as an upstream command to retrieve the "IEXPLORE" processes.

       PowerShell

       PS> Get-Process iexplore | Get-Proc

     The following output appears.

       Handles   NPM(K)   PM(K)   WS(K) VS(M)    CPU(s)     Id   ProcessName
       -------   ------   -----   ----- -----    ------     --   -----------
           801       21   40720    6544    142     9.52   2288   iexplore
           726       21   25872   16652    138    22.09   3860   iexplore
           801       21   40720    6544    142     9.52   2288   iexplore
           726       21   25872   16652    138    22.09   3860   iexplore

See Also
Adding Parameters that Process Command Line Input

<!-- p.1668 -->

Creating Your First Cmdlet

Extending Object Types and Formatting

How to Register Cmdlets, Providers, and Host Applications

Windows PowerShell Reference

Cmdlet Samples

Last updated on 05/20/2025

<!-- p.1669 -->

Adding Non-Terminating Error Reporting
to Your Cmdlet
Cmdlets can report non-terminating errors by calling the
System.Management.Automation.Cmdlet.WriteError method and still continue to operate on
the current input object or on further incoming pipeline objects. This section explains how to
create a cmdlet that reports non-terminating errors from its input processing methods.

For non-terminating errors (as well as terminating errors), the cmdlet must pass an
System.Management.Automation.ErrorRecord object identifying the error. Each error record is
identified by a unique string called the "error identifier". In addition to the identifier, the
category of each error is specified by constants defined by a
System.Management.Automation.ErrorCategory enumeration. The user can view errors based
on their category by setting the $ErrorView variable to "CategoryView".

For more information about error records, see Windows PowerShell Error Records.

Defining the Cmdlet
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. This cmdlet retrieves process information, so the verb name chosen
here is "Get". (Almost any sort of cmdlet that is capable of retrieving information can process
command-line input.) For more information about approved cmdlet verbs, see Cmdlet Verb
Names.

The following is the definition for this Get-Proc cmdlet. Details of this definition are given in
Creating Your First Cmdlet.

 C#

 [Cmdlet(VerbsCommon.Get, "proc")]
 public class GetProcCommand: Cmdlet

 VB

 <Cmdlet(VerbsCommon.Get, "Proc")> _
 Public Class GetProcCommand
     Inherits Cmdlet

<!-- p.1670 -->

Defining Parameters
If necessary, your cmdlet must define parameters for processing input. This Get-Proc cmdlet
defines a Name parameter as described in Adding Parameters that Process Command-Line
Input.

Here is the parameter declaration for the Name parameter of this Get-Proc cmdlet.

 C#

 [Parameter(
             Position = 0,
             ValueFromPipeline = true,
             ValueFromPipelineByPropertyName = true
 )]
 [ValidateNotNullOrEmpty]
 public string[] Name
 {
    get { return processNames; }
    set { processNames = value; }
 }
 private string[] processNames;

 VB

 <Parameter(Position:=0, ValueFromPipeline:=True, _
 ValueFromPipelineByPropertyName:=True), ValidateNotNullOrEmpty()> _
 Public Property Name() As String()
     Get
         Return processNames
     End Get

         Set(ByVal value As String())
             processNames = value
         End Set

 End Property

Overriding Input Processing Methods
All cmdlets must override at least one of the input processing methods provided by the
System.Management.Automation.Cmdlet class. These methods are discussed in Creating Your
First Cmdlet.

  ７ Note

<!-- p.1671 -->

  Your cmdlet should handle each record as independently as possible.

This Get-Proc cmdlet overrides the System.Management.Automation.Cmdlet.ProcessRecord
method to handle the Name parameter for input provided by the user or a script. This method
will get the processes for each requested process name or all processes if no name is provided.
Details of this override are given in Creating Your First Cmdlet.

Things to Remember When Reporting Errors
The System.Management.Automation.ErrorRecord object that the cmdlet passes when writing
an error requires an exception at its core. Follow the .NET guidelines when determining the
exception to use. Basically, if the error is semantically the same as an existing exception, the
cmdlet should use or derive from that exception. Otherwise, it should derive a new exception
or exception hierarchy directly from the System.Exception class.

When creating error identifiers (accessed through the FullyQualifiedErrorId property of the
ErrorRecord class) keep the following in mind.

     Use strings that are targeted for diagnostic purposes so that when inspecting the fully
     qualified identifier you can determine what the error is and where the error came from.

     A well formed fully qualified error identifier might be as follows.

      CommandNotFoundException,Microsoft.PowerShell.Commands.GetCommandCommand

Notice that in the previous example, the error identifier (the first token) designates what the
error is and the remaining part indicates where the error came from.

     For more complex scenarios, the error identifier can be a dot separated token that can be
     parsed on inspection. This allows you too branch on the parts of the error identifier as
     well as the error identifier and error category.

The cmdlet should assign specific error identifiers to different code paths. Keep the following
information in mind for assignment of error identifiers:

     An error identifier should remain constant throughout the cmdlet life cycle. Do not
     change the semantics of an error identifier between cmdlet versions.
     Use text for an error identifier that tersely corresponds to the error being reported. Do
     not use white space or punctuation.
     Have your cmdlet generate only error identifiers that are reproducible. For example, it
     should not generate an identifier that includes a process identifier. Error identifiers are

<!-- p.1672 -->

      useful to a user only when they correspond to identifiers that are seen by other users
      experiencing the same problem.

Unhandled exceptions are not caught by PowerShell in the following conditions:

      If a cmdlet creates a new thread and code running in that thread throws an unhandled
      exception, PowerShell will not catch the error and will terminate the process.
      If an object has code in its destructor or Dispose methods that causes an unhandled
      exception, PowerShell will not catch the error and will terminate the process.

Reporting Non-terminating Errors
Any one of the input processing methods can report a non-terminating error to the output
stream using the System.Management.Automation.Cmdlet.WriteError method.

Here is a code example from this Get-Proc cmdlet that illustrates the call to
System.Management.Automation.Cmdlet.WriteError from within the override of the
System.Management.Automation.Cmdlet.ProcessRecord method. In this case, the call is made if
the cmdlet cannot find a process for a specified process identifier.

 C#

 protected override void ProcessRecord()
 {
   // If no name parameter passed to cmdlet, get all processes.
   if (processNames == null)
   {
     WriteObject(Process.GetProcesses(), true);
   }
     else
     {
       // If a name parameter is passed to cmdlet, get and write
       // the associated processes.
       // Write a non-terminating error for failure to retrieve
       // a process.
       foreach (string name in processNames)
       {
         Process[] processes;

           try
           {
             processes = Process.GetProcessesByName(name);
           }
           catch (InvalidOperationException ex)
           {
             WriteError(new ErrorRecord(
                        ex,

<!-- p.1673 -->

                           "NameNotFound",
                           ErrorCategory.InvalidOperation,
                           name));
               continue;
           }

            WriteObject(processes, true);
          } // foreach (...
        } // else
    }

Things to Remember About Writing Non-terminating Errors
For a non-terminating error, the cmdlet must generate a specific error identifier for each
specific input object.

A cmdlet frequently needs to modify the PowerShell action produced by a non-terminating
error. It can do this by defining the ErrorAction and ErrorVariable parameters. If defining the
ErrorAction parameter, the cmdlet presents the user options

System.Management.Automation.ActionPreference, you can also directly influence the action
by setting the $ErrorActionPreference variable.

The cmdlet can save non-terminating errors to a variable using the ErrorVariable parameter,
which is not affected by the setting of ErrorAction . Failures can be appended to an existing
error variable by adding a plus sign (+) to the front of the variable name.

Code Sample
For the complete C# sample code, see GetProcessSample04 Sample.

Define Object Types and Formatting
PowerShell passes information between cmdlets using .NET objects. Consequently, a cmdlet
might need to define its own type, or the cmdlet might need to extend an existing type
provided by another cmdlet. For more information about defining new types or extending
existing types, see Extending Object Types and Formatting.

Building the Cmdlet
After implementing a cmdlet, you must register it with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications    .

<!-- p.1674 -->

Testing the Cmdlet
When your cmdlet has been registered with PowerShell, you can test it by running it on the
command line. Let's test the sample Get-Proc cmdlet to see whether it reports an error:

     Start PowerShell, and use the Get-Proc cmdlet to retrieve the processes named "TEST".

       PowerShell

       Get-Proc -Name test

     The following output appears.

       Get-Proc : Operation is not valid due to the current state of the object.
       At line:1 char:9
       + Get-Proc <<<< -Name test

See Also
     Adding Parameters that Process Pipeline Input

     Adding Parameters that Process Command-Line Input

     Creating Your First Cmdlet

     Extending Object Types and Formatting

     How to Register Cmdlets, Providers, and Host Applications

     Windows PowerShell Reference

     Cmdlet Samples

Last updated on 05/20/2025

<!-- p.1675 -->

StopProc Tutorial
This section provides a tutorial for creating the Stop-Proc cmdlet, which is very similar to the
Stop-Process cmdlet provided by Windows PowerShell. This tutorial provides fragments of
code that illustrate how cmdlets are implemented, and an explanation of the code.

Topics in this Tutorial
The topics in this tutorial are designed to be read sequentially, with each topic building on
what was discussed in the previous topic.

      Creating a Cmdlet that Modifies the System: This section describes how to create a
      cmdlet that supports system modifications, such as stopping a process running on the
      computer.

      Adding User Messages to Your Cmdlet: This section describes how to add the ability to
      write user messages, debug messages, warning messages, and progress information to
      your cmdlet.

      Adding Aliases, Wildcard Expansion, and Help to Cmdlet Parameters: This section
      describes how to create a cmdlet that supports parameter aliases, Help, and wildcard
      expansion.

      Adding Parameter Sets to Cmdlets: This section describes how to add parameter sets to
      a cmdlet. Parameter sets allow the cmdlet to operate differently based on what
      parameters are specified by the user.

See Also
      Windows PowerShell SDK

 Last updated on 05/20/2025

<!-- p.1676 -->

Creating a Cmdlet that Modifies the System
Sometimes a cmdlet must modify the running state of the system, not just the state of the
Windows PowerShell runtime. In these cases, the cmdlet should allow the user a chance to
confirm whether or not to make the change.

To support confirmation a cmdlet must do two things.

     Declare that the cmdlet supports confirmation when you specify the
     System.Management.Automation.CmdletAttribute attribute by setting the
     SupportsShouldProcess keyword to true .

     Call System.Management.Automation.Cmdlet.ShouldProcess during the execution of the
     cmdlet (as shown in the following example).

By supporting confirmation, a cmdlet exposes the Confirm and WhatIf parameters that are
provided by Windows PowerShell, and also meets the development guidelines for cmdlets (For
more information about cmdlet development guidelines, see Cmdlet Development Guidelines.).

Changing the System
The act of "changing the system" refers to any cmdlet that potentially changes the state of the
system outside Windows PowerShell. For example, stopping a process, enabling or disabling a
user account, or adding a row to a database table are all changes to the system that should be
confirmed. In contrast, operations that read data or establish transient connections do not
change the system and generally do not require confirmation. Confirmation is also not needed
for actions whose effect is limited to inside the Windows PowerShell runtime, such as Set-
Variable . Cmdlets that might or might not make a persistent change should declare

SupportsShouldProcess and call System.Management.Automation.Cmdlet.ShouldProcess only if

they are about to make a persistent change.

  ７ Note

  ShouldProcess confirmation applies only to cmdlets. If a command or script modifies the
  running state of a system by directly calling .NET methods or properties, or by calling
  applications outside of Windows PowerShell, this form of confirmation will not be
  available.

<!-- p.1677 -->

The StopProc Cmdlet
This topic describes a Stop-Proc cmdlet that attempts to stop processes that are retrieved
using the Get-Proc cmdlet (described in Creating Your First Cmdlet).

Defining the Cmdlet
The first step in cmdlet creation is always naming the cmdlet and declaring the .NET class that
implements the cmdlet. Because you are writing a cmdlet to change the system, it should be
named accordingly. This cmdlet stops system processes, so the verb name chosen here is
"Stop", defined by the System.Management.Automation.VerbsLifecycle class, with the noun
"Proc" to indicate that the cmdlet stops processes. For more information about approved
cmdlet verbs, see Cmdlet Verb Names.

The following is the class definition for this Stop-Proc cmdlet.

 C#

 [Cmdlet(VerbsLifecycle.Stop, "Proc",
         SupportsShouldProcess = true)]
 public class StopProcCommand : Cmdlet

Be aware that in the System.Management.Automation.CmdletAttribute declaration, the
SupportsShouldProcess attribute keyword is set to true to enable the cmdlet to make calls to

System.Management.Automation.Cmdlet.ShouldProcess and
System.Management.Automation.Cmdlet.ShouldContinue. Without this keyword set, the
Confirm and WhatIf parameters will not be available to the user.

Extremely Destructive Actions
Some operations are extremely destructive, such as reformatting an active hard disk partition.
In these cases, the cmdlet should set ConfirmImpact = ConfirmImpact.High when declaring the
System.Management.Automation.CmdletAttribute attribute. This setting forces the cmdlet to
request user confirmation even when the user has not specified the Confirm parameter.
However, cmdlet developers should avoid overusing ConfirmImpact for operations that are just
potentially destructive, such as deleting a user account. Remember that if ConfirmImpact is set
to System.Management.Automation.ConfirmImpact High.

Similarly, some operations are unlikely to be destructive, although they do in theory modify the
running state of a system outside Windows PowerShell. Such cmdlets can set ConfirmImpact to

<!-- p.1678 -->

System.Management.Automation.ConfirmImpact.Low. This will bypass confirmation requests
where the user has asked to confirm only medium-impact and high-impact operations.

Defining Parameters for System Modification
This section describes how to define the cmdlet parameters, including those that are needed to
support system modification. See Adding Parameters that Process CommandLine Input if you
need general information about defining parameters.

The Stop-Proc cmdlet defines three parameters: Name , Force , and PassThru .

The Name parameter corresponds to the Name property of the process input object. Be aware
that the Name parameter in this sample is mandatory, as the cmdlet will fail if it does not have a
named process to stop.

The Force parameter allows the user to override calls to
System.Management.Automation.Cmdlet.ShouldContinue. In fact, any cmdlet that calls
System.Management.Automation.Cmdlet.ShouldContinue should have a Force parameter so
that when Force is specified, the cmdlet skips the call to
System.Management.Automation.Cmdlet.ShouldContinue and proceeds with the operation. Be
aware that this does not affect calls to System.Management.Automation.Cmdlet.ShouldProcess.

The PassThru parameter allows the user to indicate whether the cmdlet passes an output
object through the pipeline, in this case, after a process is stopped. Be aware that this
parameter is tied to the cmdlet itself instead of to a property of the input object.

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

<!-- p.1679 -->

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
The cmdlet must override an input processing method. The following code illustrates the
System.Management.Automation.Cmdlet.ProcessRecord override used in the sample Stop-Proc
cmdlet. For each requested process name, this method ensures that the process is not a special
process, tries to stop the process, and then sends an output object if the PassThru parameter is
specified.

 C#

 protected override void ProcessRecord()
 {
   foreach (string name in processNames)
   {
     // For every process name passed to the cmdlet, get the associated
     // process(es). For failures, write a non-terminating error
     Process[] processes;

      try
      {
        processes = Process.GetProcessesByName(name);
      }
      catch (InvalidOperationException ioe)
      {
        WriteError(new ErrorRecord(ioe,"Unable to access the target process by name",
                   ErrorCategory.InvalidOperation, name));

<!-- p.1680 -->

        continue;
    }

    // Try to stop the process(es) that have been retrieved for a name
    foreach (Process process in processes)
    {
      string processName;

        try
        {
          processName = process.ProcessName;
        }

        catch (Win32Exception e)
          {
            WriteError(new ErrorRecord(e, "ProcessNameNotFound",
                       ErrorCategory.ReadError, process));
            continue;
          }

         // Call Should Process to confirm the operation first.
         // This is always false if WhatIf is set.
         if (!ShouldProcess(string.Format("{0} ({1})", processName,
                            process.Id)))
         {
           continue;
         }
         // Call ShouldContinue to make sure the user really does want
         // to stop a critical process that could possibly stop the computer.
         bool criticalProcess =
              criticalProcessNames.Contains(processName.ToLower());

        if (criticalProcess &&!force)
        {
          string message = String.Format
                ("The process \"{0}\" is a critical process and should not be
stopped. Are you sure you wish to stop the process?",
                processName);

           // It is possible that ProcessRecord is called multiple times
           // when the Name parameter receives objects as input from the
           // pipeline. So to retain YesToAll and NoToAll input that the
           // user may enter across multiple calls to ProcessRecord, this
           // information is stored as private members of the cmdlet.
           if (!ShouldContinue(message, "Warning!",
                               ref yesToAll,
                               ref noToAll))
           {
             continue;
           }
         } // if (criticalProcess...
         // Stop the named process.
         try
         {
           process.Kill();
