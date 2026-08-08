---
title: "How to use this documentation — pages 1601-1640"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1601-1640
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1601-1640
family: powershell
documentKind: "doc"
abstract: "[Cmdlet(VerbsLifecycle.Stop, \"Proc\", SupportsShouldProcess = true)] public class StopProcCommand : BaseProcCommand { public override void ProcessObject(Process process) { if (ShouldProcess(process.ProcessName, \"Stop-Proc\")) { process.Kill(); } } } /// <summary> /// This class im"
---

# How to use this documentation — pages 1601-1640

<!-- p.1601 -->

[Cmdlet(VerbsLifecycle.Stop, "Proc", SupportsShouldProcess = true)]
public class StopProcCommand : BaseProcCommand
{
  public override void ProcessObject(Process process)
  {
    if (ShouldProcess(process.ProcessName, "Stop-Proc"))
    {
      process.Kill();
    }
  }
}

/// <summary>
/// This class implements a Get-Proc cmdlet. The parameters
/// for this cmdlet are defined by the BaseProcCommand class.
/// </summary>

[Cmdlet(VerbsCommon.Get, "Proc")]
public class GetProcCommand : BaseProcCommand
{
  public override void ProcessObject(Process process)
  {
    WriteObject(process);
  }
}

/// <summary>
/// This class is the base class that defines the common
/// functionality used by the Get-Proc and Stop-Proc
/// cmdlets.
/// </summary>
public class BaseProcCommand : Cmdlet
{
  #region Parameters

 // Defines the Name parameter that is used to
 // specify a process by its name.
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

 // Defines the Exclude parameter that is used to
 // specify which processes should be excluded when
 // the cmdlet performs its action.
 [Parameter()]
 public string[] Exclude

<!-- p.1602 -->

{
    get { return excludeNames; }
    set { excludeNames = value; }
}
private string[] excludeNames = new string[0];
#endregion Parameters

public virtual void ProcessObject(Process process)
{
  throw new NotImplementedException("This method should be overridden.");
}

#region Cmdlet Overrides
// <summary>
// For each of the requested process names, retrieve and write
// the associated processes.
// </summary>
protected override void ProcessRecord()
{
  // Set up the wildcard characters used in resolving
  // the process names.
  WildcardOptions options = WildcardOptions.IgnoreCase |
                            WildcardOptions.Compiled;

    WildcardPattern[] include = new WildcardPattern[Name.Length];
    for (int i = 0; i < Name.Length; i++)
    {
      include[i] = new WildcardPattern(Name[i], options);
    }

    WildcardPattern[] exclude = new WildcardPattern[Exclude.Length];
    for (int i = 0; i < Exclude.Length; i++)
    {
      exclude[i] = new WildcardPattern(Exclude[i], options);
    }

    foreach (Process p in Process.GetProcesses())
    {
      foreach (WildcardPattern wIn in include)
      {
        if (wIn.IsMatch(p.ProcessName))
        {
          bool processThisOne = true;
          foreach (WildcardPattern wOut in exclude)
          {
            if (wOut.IsMatch(p.ProcessName))
            {
              processThisOne = false;
              break;
            }
          }
          if (processThisOne)
          {
            ProcessObject(p);
          }

<!-- p.1603 -->

                    break;
                }
            }
           }
         }
         #endregion Cmdlet Overrides
     }
         #endregion ProcessCommands
 }

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1604 -->

Windows PowerShell Session State
Session state refers to the current configuration of a Windows PowerShell session or module. A
Windows PowerShell session is the operational environment that is used interactively by the
command-line user or programmatically by a host application. The session state for a session is
referred to as the global session state.

From a developer perspective, a Windows PowerShell session refers to the time between when
a host application opens a Windows PowerShell runspace and when it closes the runspace.
Looked at another way, the session is the lifetime of an instance of the Windows PowerShell
engine that is invoked while the runspace exists.

Module Session State
Module session states are created whenever the module or one of its nested modules is
imported into the session. When a module exports an element such as a cmdlet, function, or
script, a reference to that element is added to the global session state of the session. However,
when the element is run, it is executed within the session state of the module.

Session-State Data
Session state data can be public or private. Public data is available to calls from outside the
session state while private data is available only to calls from within the session state. For
example, a module can have a private function that can be called only by the module or only
internally by a public element that has been exported. This is similar to the private and public
members of a .NET Framework type.

Session-state data is stored by the current instance of the execution engine within the context
of the current Windows PowerShell session. Session-state data consists of the following items:

     Path information

     Drive information

     Windows PowerShell provider information

     Information about the imported modules and references to the module elements (such as
     cmdlets, functions, and scripts) that are exported by the module. This information and

<!-- p.1605 -->

      these references are for the global session state only.

      Session-state variable information

Accessing Session-State Data Within Cmdlets
Cmdlets can access session-state data either indirectly through the
System.Management.Automation.PSCmdlet.SessionState* property of the cmdlet class or
directly through the System.Management.Automation.SessionState class. The
System.Management.Automation.SessionState class provides properties that can be used to
investigate different types of session-state data.

See Also
System.Management.Automation.PSCmdlet.SessionState

System.Management.Automation.SessionState

Windows PowerShell Cmdlets

Writing a Windows PowerShell Cmdlet

Windows PowerShell Shell SDK

 Last updated on 05/20/2025

<!-- p.1606 -->

Examples of Cmdlet Code
ﾃ     Summarize this article for me

This section contains examples of cmdlet code that you can use to start writing your own
cmdlets.

    ） Important

    If you want step-by-step instructions for writing cmdlets, see Tutorials for Writing
    Cmdlets.

In This Section
       How to Write a Simple Cmdlet - This example shows the basic structure of cmdlet code.
       How to Declare Cmdlet Parameters - This example shows how to declare the different
       types of parameters.
       How to Declare Parameter Sets - This example shows how to declare sets of parameters
       that can change the action a cmdlet performs.
       How to Validate Parameter Input - These examples show how to validate parameter input.
       How to Declare Dynamic Parameters - This example shows how to declare a parameter
       that is added at runtime.
       How to Invoke Scripts Within a Cmdlet - This example shows how to invoke a script that
       is supplied to a cmdlet.
       How To Override Input Processing Methods - These examples show the basic structure
       used to override the BeginProcessing, ProcessRecord, and EndProcessing methods.
       How to Support ShouldProcess Calls - This example shows how the
       System.Management.Automation.Cmdlet.ShouldProcess and
       System.Management.Automation.Cmdlet.ShouldContinue methods should be called from
       within a cmdlet.
       How to Support Transactions - This example shows how to indicate that the cmdlet
       supports transactions and how to implement the action that is taken when the cmdlet is
       used within a transaction.
       How to Support Transactions - This example shows how to indicate that the cmdlet
       supports transactions and how to implement the action that is taken when the cmdlet is
       used within a transaction.
       How to Support Jobs - This example shows how to support jobs when you write cmdlets.
       How to Invoke a Cmdlet From Within a Cmdlet - This example shows how to invoke a
       cmdlet from within another cmdlet, which allows you to add the functionality of the
       invoked cmdlet to the cmdlet you are developing.

<!-- p.1607 -->

See Also
Writing a Windows PowerShell Cmdlet

Last updated on 02/24/2026

<!-- p.1608 -->

How to write a cmdlet
This article shows how to write a cmdlet. The Send-Greeting cmdlet takes a single user name as
input and then writes a greeting to that user. Although the cmdlet does not do much work, this
example demonstrates the major sections of a cmdlet.

Steps to write a cmdlet
   1. To declare the class as a cmdlet, use the Cmdlet attribute. The Cmdlet attribute specifies
      the verb and the noun for the cmdlet name.

      For more information about the Cmdlet attribute, see CmdletAttribute Declaration.

   2. Specify the name of the class.

   3. Specify that the cmdlet derives from either of the following classes:

           System.Management.Automation.Cmdlet
           System.Management.Automation.PSCmdlet

   4. To define the parameters for the cmdlet, use the Parameter attribute. In this case, only
      one required parameter is specified.

      For more information about the Parameter attribute, see ParameterAttribute Declaration.

   5. Override the input processing method that processes the input. In this case, the
      System.Management.Automation.Cmdlet.ProcessRecord method is overridden.

   6. To write the greeting, use the method
      System.Management.Automation.Cmdlet.WriteObject. The greeting is displayed in the
      following format:

       Output

       Hello <UserName>!

Example
 C#

<!-- p.1609 -->

 using System.Management.Automation;      // Windows PowerShell assembly.

 namespace SendGreeting
 {
   // Declare the class as a cmdlet and specify the
   // appropriate verb and noun for the cmdlet name.
   [Cmdlet(VerbsCommunications.Send, "Greeting")]
   public class SendGreetingCommand : Cmdlet
   {
     // Declare the parameters for the cmdlet.
     [Parameter(Mandatory=true)]
     public string Name
     {
       get { return name; }
       set { name = value; }
     }
     private string name;

         // Override the ProcessRecord method to process
         // the supplied user name and write out a
         // greeting to the user by calling the WriteObject
         // method.
         protected override void ProcessRecord()
         {
           WriteObject("Hello " + name + "!");
         }
     }
 }

See also
System.Management.Automation.Cmdlet

System.Management.Automation.PSCmdlet

System.Management.Automation.Cmdlet.ProcessRecord

System.Management.Automation.Cmdlet.WriteObject

CmdletAttribute Declaration

ParameterAttribute Declaration

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1610 -->

How to Declare Cmdlet Parameters
These examples show how to declare named, positional, required, optional, and [switch]
parameters. These examples also show how to define a parameter alias.

How to Declare a Named Parameter
     Define a public property as shown in the following code. When you add the Parameter
     attribute, omit the Position keyword from the attribute.

       C#

       [Parameter()]
       public string UserName
       {
         get { return userName; }
         set { userName = value; }
       }
       private string userName;

For more information about the Parameter attribute, see Parameter Attribute Declaration.

How to Declare a Positional Parameter
     Define a public property as shown in the following code. When you add the Parameter
     attribute, set the Position keyword to the argument position. A value of 0 indicates the
     first position.

       C#

       [Parameter(Position = 0)]
       public string UserName
       {
         get { return userName; }
         set { userName = value; }
       }
       private string userName;

For more information about the Parameter attribute, see Parameter Attribute Declaration.

How to Declare a Mandatory Parameter

<!-- p.1611 -->

     Define a public property as shown in the following code. When you add the Parameter
     attribute, set the Mandatory keyword to true .

       C#

       [Parameter(Position = 0, Mandatory = true)]
       public string UserName
       {
         get { return userName; }
         set { userName = value; }
       }
       private string userName;

For more information about the Parameter attribute, see Parameter Attribute Declaration.

How to Declare an Optional Parameter
     Define a public property as shown in the following code. When you add the Parameter
     attribute, omit the Mandatory keyword.

       C#

       [Parameter(Position = 0)]
       public string UserName
       {
         get { return userName; }
         set { userName = value; }
       }
       private string userName;

How to Declare a [switch] parameter
     Define a public property as type System.Management.Automation.SwitchParameter, and
     then declare the Parameter attribute.

       C#

       [Parameter(Position = 1)]
       public SwitchParameter GoodBye
       {
         get { return goodbye; }
         set { goodbye = value; }
       }
       private bool goodbye;

<!-- p.1612 -->

For more information about the Parameter attribute, see Parameter Attribute Declaration.

How to Declare a Parameter with Aliases
      Define a public property as shown in the following code. Add an Alias attribute that lists
      the aliases for the parameter. In this example, three aliases are defined for the same
      parameter. The first alias provides a shortcut. The second and third aliases provide names
      you can use for different scenarios.

        C#

        [Alias("UN","Writer","Editor")]
        [Parameter()]
        public string UserName
        {
          get { return userName; }
          set { userName = value; }
        }
        private string userName;

For more information about the Alias attribute, see Alias Attribute Declaration.

See Also
System.Management.Automation.SwitchParameter

Parameter Attribute Declaration

Alias Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 04/08/2026

<!-- p.1613 -->

How to Declare Parameter Sets
This example shows how to define two parameter sets when you declare the parameters for a
cmdlet. Each parameter set has both a unique parameter and a shared parameter that is used
by both parameter sets. For more information about parameters sets, including how to specify
the default parameter set, see Cmdlet Parameter Sets.

  ） Important

  Whenever possible, define the unique parameter of a parameter set as a required
  parameter. However, if you want your cmdlet to run without specifying any parameters,
  the unique parameter can be an optional parameter. For example, the unique parameter
  of the Get-Command cmdlet is optional.

How to Define Two Parameter Sets
   1. Add the ParameterSet keyword to the Parameter attribute for the unique parameter of
     the first parameter set.

       C#

       [Parameter(Position = 0, Mandatory = true,
                  ParameterSetName = "Test01")]
       public string UserName
       {
         get { return userName; }
         set { userName = value; }
       }
       private string userName;

   2. Add the ParameterSet keyword to the Parameter attribute for the unique parameter of
     the second parameter set.

       C#

       [Parameter(Position = 0, Mandatory = true,
                  ParameterSetName = "Test02")]
       public string ComputerName
       {
         get { return computerName; }
         set { computerName = value; }

<!-- p.1614 -->

       }
       private string computerName;

  3. For the parameter that belongs to both parameter sets, add a Parameter attribute for
     each parameter set and then add the ParameterSet keyword to each set. In each
     Parameter attribute, you can specify how that parameter is defined. A parameter can be
     optional in one set and mandatory in another.

       C#

       [Parameter(Mandatory= true, ParameterSetName = "Test01")]
       [Parameter(ParameterSetName = "Test02")]
       public string SharedParam
       {
           get { return sharedParam; }
           set { sharedParam = value; }
       }
       private string sharedParam;

See Also
Cmdlet Parameter Sets

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1615 -->

How to Validate Parameter Input
This section contains examples that show how to validate parameter input by using various
attributes to implement validation rules.

In This Section
How to Validate an Argument with a Script Describes how to validate an argument set by using
the ArgumentSet attribute.

How to Validate an Argument Set Describes how to validate an argument set by using the
ArgumentSet attribute.

How to Validate an Argument Range Describes how to validate an argument range by using
the ArgumentRange attribute.

How to Validate an Argument Pattern Describes how to validate an argument pattern by using
the ArgumentPattern attribute.

How to Validate the Argument Length Describes how to validate the length of an argument by
using the ArgumentLength attribute.

How to Validate an Argument Count Describes how to validate an argument count by using the
ArgumentCount attribute.

The way a parameter is declared can affect validation. For more information, see How to
Declare Cmdlet Parameters.

Reference
See Also
Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1616 -->

How to validate an argument using a script
This example shows how to specify a validation rule that uses a script to check the parameter
argument before the cmdlet is run. The value of the parameter is piped to the script. The script
must return $true for every value piped to it.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidateScriptAttribute.

To validate an argument using a script
     Add the ValidateScript attribute as shown in the following code. This example specifies a
     script to validate that the input value is an odd number.

       C#

       [ValidateScript("$_ % 2", ErrorMessage = "The item '{0}' did not pass
       validation of script '{1}'")]
       [Parameter(Position = 0, Mandatory = true)]
       public int32 OddNumber
       {
          get { return oddNumber; }
          set { oddNumber = value; }
       }

       private int32 oddNumber;

For more information about how to declare this attribute, see ValidateScript Attribute
Declaration.

See Also
System.Management.Automation.ValidateScriptAttribute

ValidateScript Attribute Declaration

Writing a Windows PowerShell Cmdlet

<!-- p.1617 -->

Last updated on 05/20/2025

<!-- p.1618 -->

How to Validate an Argument Set
This example shows how to specify a validation rule that the Windows PowerShell runtime can
use to check the parameter argument before the cmdlet is run. This validation rule provides a
set of the valid values for the parameter argument.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidateSetAttribute.

To validate an argument set
      Add the ValidateSet attribute as shown in the following code. This example specifies a set
      of three possible values for the UserName parameter.

        C#

        [ValidateSet("Steve", "Mary", "Carl", IgnoreCase = true)]
        [Parameter(Position = 0, Mandatory = true)]
        public string UserName
        {
          get { return userName; }
          set { userName = value; }
        }

        private string userName;

For more information about how to declare this attribute, see ValidateSet Attribute Declaration.

See Also
System.Management.Automation.ValidateSetAttribute

ValidateSet Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1619 -->

How to Validate an Argument Range
This example shows how to specify a validation rule that the Windows PowerShell runtime can
use to check the minimum and maximum values of the parameter argument before the cmdlet
is run. You set this validation rule by declaring the ValidateRange attribute.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidateRangeAttribute.

To validate an argument range
      Add the ValidateRange attribute as shown in the following code. This example specifies a
      range of 0 to 5 for the InputData parameter.

        C#

        [ValidateRange(0, 5)]
        [Parameter(Position = 0, Mandatory = true)]
        public int InputData
        {
          get { return inputData; }
          set { inputData = value; }
        }
        private int inputData;

For more information about how to declare this attribute, see ValidateRange Attribute
Declaration.

See Also
ValidateRange Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1620 -->

How to Validate an Argument Pattern
This example shows how to specify a validation rule that the Windows PowerShell runtime can
use to check the character pattern of the parameter argument before the cmdlet is run. You set
this validation rule by declaring the ValidatePattern attribute.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidatePatternAttribute.

To validate an argument pattern
      Add the Validate attribute as shown in the following code. This example specifies a
      pattern of four digits, where each digit has a value of 0 through 9.

        C#

        [ValidatePattern("[0-9][0-9][0-9][0-9]")]
        [Parameter(Position = 0, Mandatory = true)]
        public int InputData
        {
          get { return inputData; }
          set { inputData = value; }
        }

        private int inputData;

For more information about how to declare this attribute, see ValidatePattern Attribute
Declaration.

See Also
ValidatePattern Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1621 -->

How to Validate the Argument Length
This example shows how to specify a validation rule that the Windows PowerShell runtime can
use to check the number of characters (the length) of the parameter argument before the
cmdlet is run. You set this validation rule by declaring the ValidateLength attribute.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidateLengthAttribute.

To validate the argument length
      Add the Validate attribute as shown in the following code. This example specifies that the
      length of the argument should have a length of 0 to 10 characters.

        C#

        [ValidateLength(0, 10)]
        [Parameter(Position = 0, Mandatory = true)]
        public string UserName
        {
          get { return userName; }
          set { userName = value; }
        }
        private string userName;

For more information about how to declare this attribute, see ValidateLength Attribute
Declaration.

See Also
ValidateLength Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1622 -->

How to Validate an Argument Count
This example shows how to specify a validation rule that the Windows PowerShell runtime can
use to check the number of arguments (the count) that a parameter accepts before the cmdlet
is run. You set this validation rule by declaring the ValidateCount attribute.

  ７ Note

  For more information about the class that defines this attribute, see
  System.Management.Automation.ValidateCountAttribute.

To validate an argument count
      Add the Validate attribute as shown in the following code. This example specifies that the
      parameter will accept one argument or as many as three arguments.

        C#

        [ValidateCount(1, 3)]
        [Parameter(Position = 0, Mandatory = true)]
        public string[] UserNames
        {
          get { return userNames; }
          set { userNames = value; }
        }

        private string[] userNames;

For more information about how to declare this attribute, see ValidateCount Attribute
Declaration.

See Also
ValidateCount Attribute Declaration

Writing a Windows PowerShell Cmdlet

 Last updated on 05/20/2025

<!-- p.1623 -->

How to Declare Dynamic Parameters
This example shows how to define dynamic parameters that are added to the cmdlet at
runtime. In this example, the Department parameter is added to the cmdlet whenever the user
specifies the Employee [switch] parameter. For more information about dynamic parameters,
see Cmdlet Dynamic Parameters.

To define dynamic parameters
  1. In the cmdlet class declaration, add the
     System.Management.Automation.IDynamicParameters interface as shown.

       C#

       public class SendGreetingCommand : Cmdlet, IDynamicParameters

  2. Call the System.Management.Automation.IDynamicParameters.GetDynamicParameters*
     method, which returns the object in which the dynamic parameters are defined. In this
     example, the method is called when the Employee parameter is specified.

       C#

       public object GetDynamicParameters()
       {
           if (employee)
           {
             context= new SendGreetingCommandDynamicParameters();
             return context;
           }
           return null;
       }
       private SendGreetingCommandDynamicParameters context;

  3. Declare a class that defines the dynamic parameters to be added. You can use the
     attributes that you used to declare the static cmdlet parameters to declare the dynamic
     parameters.

       C#

       public class SendGreetingCommandDynamicParameters
       {
         [Parameter]

<!-- p.1624 -->

           [ValidateSet ("Marketing", "Sales", "Development")]
           public string Department
           {
             get { return department; }
             set { department = value; }
           }
           private string department;
       }

Example
In this example, the Department parameter is added whenever the user specifies the Employee
parameter. The Department parameter is an optional parameter, and the ValidateSet attribute is
used to specify the allowed arguments.

 C#

 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Management.Automation;         // PowerShell assembly.

 namespace SendGreeting
 {
   // Declare the cmdlet class that supports the
   // IDynamicParameters interface.
   [Cmdlet(VerbsCommunications.Send, "Greeting")]
   public class SendGreetingCommand : Cmdlet, IDynamicParameters
   {
     // Declare the parameters for the cmdlet.
     [Parameter(Mandatory = true)]
     public string Name
     {
       get { return name; }
       set { name = value; }
     }
     private string name;

      [Parameter]
      [Alias ("FTE")]
      public SwitchParameter Employee
      {
        get { return employee; }
        set { employee = value; }
      }
      private Boolean employee;

      // Implement GetDynamicParameters to
      // retrieve the dynamic parameter.
      public object GetDynamicParameters()

<!-- p.1625 -->

         {
             if (employee)
             {
               context= new SendGreetingCommandDynamicParameters();
               return context;
             }
             return null;
     }
     private SendGreetingCommandDynamicParameters context;

         // Override the ProcessRecord method to process the
         // supplied user name and write out a greeting to
         // the user by calling the WriteObject method.
         protected override void ProcessRecord()
         {
           WriteObject("Hello " + name + "! ");
           if (employee)
           {
             WriteObject("Department: " + context.Department);
           }
         }
     }

     // Define the dynamic parameters to be added
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
 }

See Also
         System.Management.Automation.RuntimeDefinedParameterDictionary
         System.Management.Automation.IDynamicParameters.GetDynamicParameters*
         Cmdlet Dynamic Parameters
         Windows PowerShell SDK

Last updated on 04/08/2026

<!-- p.1626 -->

How to Invoke Scripts Within a Cmdlet
This example shows how to invoke a script that is supplied to a cmdlet. The script is executed
by the cmdlet, and its results are returned to the cmdlet as a collection of
System.Management.Automation.PSObject objects.

To invoke a script block
   1. The command verifies that a script block was supplied to the cmdlet. If a script block was
     supplied, the command invokes the script block with its required parameters.

       C#

       if (script != null)
       {
            WriteDebug("Executing script block.");

             // Invoke the script block with the required arguments.
             Collection<PSObject> PSObjects = script.Invoke(
                 line,
                 simpleMatch,
                 caseSensitive
             );
            // more code as needed...
       }

   2. Then, the script iterates through the returned collection of
     System.Management.Automation.PSObject objects and perform the necessary operations.

       C#

       foreach (PSObject object in PSObjects)
       {
           if (LanguagePrimitives.IsTrue(object))
           {
                result = new MatchInfo();
                result.Line = line;
                result.IgnoreCase = !caseSensitive;
                break;
           }
       }

See Also

<!-- p.1627 -->

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1628 -->

How to Override Input Processing Methods
These examples show how to overwrite the input processing methods within a cmdlet. These
methods are used to perform the following operations:

      The System.Management.Automation.Cmdlet.BeginProcessing method is used to perform
      one-time startup operations that are valid for all the objects processed by the cmdlet. The
      Windows PowerShell runtime calls this method only once.

      The System.Management.Automation.Cmdlet.ProcessRecord method is used to process
      the objects passed to the cmdlet. The Windows PowerShell runtime calls this method for
      each object passed to the cmdlet.

      The System.Management.Automation.Cmdlet.EndProcessing method is used to perform
      one-time post processing operations. The Windows PowerShell runtime calls this method
      only once.

To override the BeginProcessing method
      Declare a protected override of the
      System.Management.Automation.Cmdlet.BeginProcessing method.

The following class prints a sample message. To use this class, change the verb and noun in the
Cmdlet attribute, change the name of the class to reflect the new verb and noun, and then add
the functionality you require to the override of the
System.Management.Automation.Cmdlet.BeginProcessing method.

 C#

 [Cmdlet(VerbsDiagnostic.Test, "BeginProcessingClass")]
 public class TestBeginProcessingClassTemplate : Cmdlet
 {
   // Override the BeginProcessing method to add preprocessing
   //operations to the cmdlet.
   protected override void BeginProcessing()
   {
     // Replace the WriteObject method with the logic required
     // by your cmdlet. It is used here to generate the following
     // output:
     // "This is a test of the BeginProcessing template."
     WriteObject("This is a test of the BeginProcessing template.");

<!-- p.1629 -->

     }
 }

To override the ProcessRecord method
         Declare a protected override of the
         System.Management.Automation.Cmdlet.ProcessRecord method.

The following class prints a sample message. To use this class, change the verb and noun in the
Cmdlet attribute, change the name of the class to reflect the new verb and noun, and then add
the functionality you require to the override of the
System.Management.Automation.Cmdlet.ProcessRecord method.

 C#

 [Cmdlet(VerbsDiagnostic.Test, "ProcessRecordClass")]
 public class TestProcessRecordClassTemplate : Cmdlet
 {
     // Override the ProcessRecord method to add processing
     //operations to the cmdlet.
     protected override void ProcessRecord()
     {
         // Replace the WriteObject method with the logic required
         // by your cmdlet. It is used here to generate the following
         // output:
         // "This is a test of the ProcessRecord template."
         WriteObject("This is a test of the ProcessRecord template.");
     }
 }

To override the EndProcessing method
         Declare a protected override of the
         System.Management.Automation.Cmdlet.EndProcessing method.

The following class prints a sample. To use this class, change the verb and noun in the Cmdlet
attribute, change the name of the class to reflect the new verb and noun, and then add the
functionality you require to the override of the
System.Management.Automation.Cmdlet.EndProcessing method.

 C#

 [Cmdlet(VerbsDiagnostic.Test, "EndProcessingClass")]
 public class TestEndProcessingClassTemplate : Cmdlet

<!-- p.1630 -->

 {
     // Override the EndProcessing method to add postprocessing
     //operations to the cmdlet.
     protected override void EndProcessing()
     {
       // Replace the WriteObject method with the logic required
       // by your cmdlet. It is used here to generate the following
       // output:
       // "This is a test of the BeginProcessing template."
       WriteObject("This is a test of the EndProcessing template.");
     }
 }

See Also
System.Management.Automation.Cmdlet.BeginProcessing

System.Management.Automation.Cmdlet.EndProcessing

System.Management.Automation.Cmdlet.ProcessRecord

Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1631 -->

How to Support Transactions
This example shows the basic code elements that add support for transactions to a cmdlet.

  ） Important

  For more information about how Windows PowerShell handles transactions, see About
  Transactions.

To support transactions
  1. When you declare the Cmdlet attribute, specify that the cmdlet supports transactions.
     When the cmdlet supports transactions, Windows PowerShell adds the UseTransaction
     parameter to the cmdlet when it is run.

       C#

       [Cmdlet(VerbsCommunications.Send, "GreetingTx",
               SupportsTransactions=true )]

  2. Within one of the input processing methods, add an if block to determine if a
     transaction is available. If the if statement resolves to true , the actions within this
     statement can be performed within the context of the current transaction.

       C#

       if (TransactionAvailable())
       {
         using (CurrentPSTransaction)
         {
           WriteObject("Hello " + name + "       from within a transaction.");
         }
       }

See Also
Writing a Windows PowerShell Cmdlet

<!-- p.1632 -->

Last updated on 05/20/2025

<!-- p.1633 -->

How to Support Jobs
This example shows how to support jobs when you write cmdlets. If you want users to run your
cmdlet as a background job, you must include the code described in the following procedure.
For more information about background jobs, see Background Jobs.

To support jobs
  1. Define an AsJob [switch] parameter so that the user can decide whether to run the
     cmdlet as a job.

     The following example shows an AsJob parameter declaration.

       C#

       [Parameter()]
       public SwitchParameter AsJob
       {
         get { return asjob; }
         set { asjob = value; }
       }
       private bool asjob;

  2. Create an object that derives from the System.Management.Automation.Job class. This
     object can be a custom job object or one of the job objects provided by Windows
     PowerShell, such a System.Management.Automation.PSEventJob object.

     The following example shows a custom job object.

       C#

       private SampleJob job = new SampleJob("Get-ProcAsJob");

  3. In a record processing method, add an if statement to detect whether the cmdlet
     should run as a job. The following code uses the
     System.Management.Automation.Cmdlet.ProcessRecord method.

       C#

       protected override void ProcessRecord()
       {
         if (asjob)

<!-- p.1634 -->

        {
            // Add the job definition to the job repository,
            // return the job object, and then create the thread
            // used to run the job.
            JobRepository.Add(job);
            WriteObject(job);
            ThreadPool.QueueUserWorkItem(WorkItem);
        }
        else
        {
          job.ProcessJob();
          foreach (PSObject p in job.Output)
          {
            WriteObject(p);
          }
        }
    }

4. For custom job objects, implement the job class.

    C#

    private class SampleJob : Job
    {
      internal SampleJob(string command)
          : base(command)
      {
        SetJobState(JobState.NotStarted);
      }
      public override string StatusMessage
      {
        get { throw new NotImplementedException(); }
      }

        public override bool HasMoreData
        {
          get
          {
            return hasMoreData;
          }
        }
        private bool hasMoreData = true;

        public override string Location
        {
          get { throw new NotImplementedException(); }
        }

        public override void StopJob()
        {
          throw new NotImplementedException();
        }

<!-- p.1635 -->

          internal void ProcessJob()
          {
            SetJobState(JobState.Running);
            DoProcessLogic();
            SetJobState(JobState.Completed);
          }

          // Retrieve the processes of the local computer.
          void DoProcessLogic()
          {
            Process[] p = Process.GetProcesses();

           foreach (Process pl in p)
           {
             Output.Add(PSObject.AsPSObject(pl));
           }
           Output.Complete();
         } // End DoProcessLogic.
       } // End SampleJob class.

   5. If the cmdlet performs the work, call the
      System.Management.Automation.Cmdlet.WriteObject method to return a process object
      to the pipeline. If the work is performed as a job, add child job to the job.

       C#

       void DoProcessLogic(bool asJob)
       {
         Process[] p = Process.GetProcesses();

         foreach (Process pl in p)
         {
           if (!asjob)
           {
             WriteObject(pl);
           }
           else
           {
             job.ChildJobs[0].Output.Add(PSObject.AsPSObject(pl));
           }
         }
       } // End DoProcessLogic.

Example
The following sample code shows the code for a Get-Proc cmdlet that can retrieve processes
internally or by using a background job.

 C#

<!-- p.1636 -->

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Management.Automation;   // Windows PowerShell namespace.
using System.Threading;               // Thread pool namespace for posting work.
using System.Diagnostics;             // Diagnostics namespace for retrieving
                                      // process objects.

// This sample shows a cmdlet whose work can be done by the cmdlet or by using
// a background job. Background jobs are executed in their own thread,
// independent of the pipeline thread in which the cmdlet is executed.
//
// To load this cmdlet, create a module folder and copy the GetProcessSample06.dll
// assembly into the module folder. Make sure that the path to the module folder
// is added to the $PSModulePath environment variable.
// Module folder path:
//    user/documents/WindowsPowerShell/modules/GetProcessSample06
//
// To import the module, run the following command: Import-Module
GetProcessSample06.
// To test the cmdlet, run the following command: Get-Proc -Name <process name>
//

//
namespace Microsoft.Samples.PowerShell.Commands
{
   /// <summary>
   /// This cmdlet retrieves process internally or returns
   /// a job that retrieves the processes.
   /// </summary>
   [Cmdlet(VerbsCommon.Get, "Proc")]
   public sealed class GetProcCommand : PSCmdlet
   {

    #region Parameters
    /// <summary>
    /// Specify the Name parameter. This parameter accepts
    /// process names from the command line.
    /// </summary>
    [Parameter(
               Position = 0,
               ValueFromPipeline = true,
               ValueFromPipelineByPropertyName = true)]
    [ValidateNotNullOrEmpty]
    public string[] Name
    {
      get { return processNames; }
      set { processNames = value; }
    }
    private string[] processNames;

    /// <summary>
    /// Specify the AsJob parameter. This parameter indicates

<!-- p.1637 -->

/// whether the cmdlet should retrieve the processes internally
/// or return a Job object that retrieves the processes.
/// </summary>
[Parameter()]
public SwitchParameter AsJob
{
  get { return asjob; }
  set { asjob = value; }
}
private bool asjob;

#endregion Parameters

#region Cmdlet Overrides

// Create a custom job object.
private SampleJob job = new SampleJob("Get-ProcAsJob");

/// <summary>
/// Determines if the processes should be retrieved
/// internally or if a Job object should be returned.
/// </summary>
protected override void ProcessRecord()
{
  if (asjob)
  {
    // Add the job definition to the job repository,
    // return the job object, and then create the thread
    // used to run the job.
    JobRepository.Add(job);
    WriteObject(job);
    ThreadPool.QueueUserWorkItem(WorkItem);
  }
  else
  {
    job.ProcessJob();
    foreach (PSObject p in job.Output)
    {
       WriteObject(p);
    }
  }
}
#endregion Overrides

// Implement a custom job that derives
// from the System.Management.Automation.Job class.
private class SampleJob : Job
{
  internal SampleJob(string command)
      : base(command)
  {
    SetJobState(JobState.NotStarted);
  }
  public override string StatusMessage
  {

<!-- p.1638 -->

     get { throw new NotImplementedException(); }
 }

 public override bool HasMoreData
 {
   get
   {
     return hasMoreData;
   }
 }
 private bool hasMoreData = true;

 public override string Location
 {
   get { throw new NotImplementedException(); }
 }

 public override void StopJob()
 {
   throw new NotImplementedException();
 }

 internal void ProcessJob()
 {
   SetJobState(JobState.Running);
   DoProcessLogic();
   SetJobState(JobState.Completed);
 }

 // Retrieve the processes of the local computer.
 void DoProcessLogic()
 {
   Process[] p = Process.GetProcesses();

    foreach (Process pl in p)
    {
      Output.Add(PSObject.AsPSObject(pl));
    }
    Output.Complete();
  } // End DoProcessLogic.
} // End SampleJob class.

void WorkItem(object dummy)
{
   job.ProcessJob();
}

// Display the results of the work. If not a job,
// process objects are returned. If a job, the
// output is added to the job as a child job.
void DoProcessLogic(bool asJob)
{
  Process[] p = Process.GetProcesses();

 foreach (Process pl in p)

<!-- p.1639 -->

        {
            if (!asjob)
            {
              WriteObject(pl);
            }
            else
            {
              job.ChildJobs[0].Output.Add(PSObject.AsPSObject(pl));
            }
         }
       } // End DoProcessLogic.
     } //End GetProcCommand
 }

Last updated on 04/08/2026

<!-- p.1640 -->

How to Invoke a Cmdlet from Within a
Cmdlet
This example shows how to invoke a binary cmdlet that derives from
[System.Management.Automation.Cmdlet] directly from within another binary cmdlet, which

allows you to add the functionality of the invoked cmdlet to the binary cmdlet you are
developing. In this example, the Get-Process cmdlet is invoked to get the processes that are
running on the local computer. The call to the Get-Process cmdlet is equivalent to the
following command. This command retrieves all the processes whose names start with the
characters "a" through "t".

 PowerShell

 Get-Process -Name [a-t]*

  ） Important

  You can invoke only those cmdlets that derive directly from the
  System.Management.Automation.Cmdlet class. You can't invoke a cmdlet that derives
  from the System.Management.Automation.PSCmdlet class. For an example, see How to
  invoke a PSCmdlet from within a PSCmdlet.

To invoke a cmdlet from within a cmdlet
   1. Ensure that the assembly that defines the cmdlet to be invoked is referenced and that the
     appropriate using statement is added. In this example, the following namespaces are
     added.

       C#

       using System.Diagnostics;
       using System.Management.Automation;         // PowerShell assembly.
       using Microsoft.PowerShell.Commands;        // PowerShell cmdlets assembly you want
       to call.

   2. In the input processing method of the cmdlet, create a new instance of the cmdlet to be
     invoked. In this example, an object of type
