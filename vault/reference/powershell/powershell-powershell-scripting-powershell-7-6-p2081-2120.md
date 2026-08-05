---
title: "How to use this documentation — pages 2081-2120"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2081-2120
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2081-2120
family: powershell
documentKind: "doc"
abstract: "Windows PowerShell02 Sample This sample shows how to run commands asynchronously using the runspaces of a runspace pool. The sample generates a list of commands, and then runs those commands while the Windows PowerShell engine opens a runspace from the pool when it is needed. Re"
---

# How to use this documentation — pages 2081-2120

<!-- p.2081 -->

Windows PowerShell02 Sample
This sample shows how to run commands asynchronously using the runspaces of a runspace
pool. The sample generates a list of commands, and then runs those commands while the
Windows PowerShell engine opens a runspace from the pool when it is needed.

Requirements
      This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following:

      Creating a RunspacePool object with a minimum and maximum number of runspaces
      allowed to be open at the same time.
      Creating a list of commands.
      Running the commands asynchronously.
      Calling the
      System.Management.Automation.Runspaces.RunspacePool.GetAvailableRunspaces*
      method to see how many runspaces are free.
      Capturing the command output with the
      System.Management.Automation.PowerShell.EndInvoke* method.

Example
This sample shows how to open the runspaces of a runspace pool, and how to asynchronously
run commands in those runspaces.

 C#

 namespace Sample
 {
   using System;
   using System.Collections;
   using System.Collections.Generic;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;

   /// <summary>

<!-- p.2082 -->

  /// This class contains the Main entry point for the application.
  /// </summary>
  internal class PowerShell02
  {
    /// <summary>
    /// Runs many commands with the help of a RunspacePool.
    /// </summary>
    /// <param name="args">This parameter is unused.</param>
    private static void Main(string[] args)
    {
      // Creating and opening runspace pool. Use a minimum of 1 runspace and a
maximum of
      // 5 runspaces can be opened at the same time.
      RunspacePool runspacePool = RunspaceFactory.CreateRunspacePool(1, 5);
      runspacePool.Open();

      using (runspacePool)
      {
        // Define the commands to be run.
        List<PowerShell> powerShellCommands = new List<PowerShell>();

       // The command results.
       List<IAsyncResult> powerShellCommandResults = new List<IAsyncResult>();

       // The maximum number of runspaces that can be opened at one time is
       // 5, but we can queue up many more commands that will use the
       // runspace pool.
       for (int i = 0; i < 100; i++)
       {
         // Using a PowerShell object, run the commands.
         PowerShell powershell = PowerShell.Create();

           // Instead of setting the Runspace property of powershell,
           // the RunspacePool property is used. That is the only difference
           // between running commands with a runspace and running commands
           // with a runspace pool.
           powershell.RunspacePool = runspacePool;

          // The script to be run outputs a sequence number and the number of
available runspaces
          // in the pool.
          string script = String.Format(
                        "write-output ' Command: {0}, Available Runspaces: {1}'",
                        i,
                        runspacePool.GetAvailableRunspaces());

           // The three lines below look the same running with a runspace or
           // with a runspace pool.
           powershell.AddScript(script);
           powerShellCommands.Add(powershell);
           powerShellCommandResults.Add(powershell.BeginInvoke());
       }

       // Collect the results.
       for (int i = 0; i < 100; i++)

<!-- p.2083 -->

            {
           // EndInvoke will wait for each command to finish, so we will be getting
 the commands
           // in the same 0 to 99 order that they have been invoked withy
 BeginInvoke.
           PSDataCollection<PSObject> results =
 powerShellCommands[i].EndInvoke(powerShellCommandResults[i]);

           // Print all the results. One PSObject with a plain string is the
 expected result.
           PowerShell02.PrintCollection(results);
         }
       }
     }

         /// <summary>
         /// Iterates through a collection printing all items.
         /// </summary>
         /// <param name="collection">collection to be printed</param>
         private static void PrintCollection(IList collection)
         {
           foreach (object obj in collection)
           {
             Console.WriteLine("PowerShell Result: {0}", obj);
           }
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2084 -->

Custom Host Samples
This section includes sample code for writing a custom host. You can use Microsoft Visual
Studio to create a console application and then copy the code from the topics in this section
into your host application.

In This Section
Host01 Sample This sample shows how to implement a host application that uses a basic
custom host.

Host02 Sample This sample shows how to write a host application that uses the Windows
PowerShell runtime along with a custom host implementation. The host application sets the
host culture to German, runs the Get-Process cmdlet and displays the results as you would see
them using pwrsh.exe, and then prints out the current data and time in German.

Host03 Sample This sample shows how to build an interactive console-based host application
that reads commands from the command line, executes the commands, and then displays the
results to the console.

Host04 Sample This sample shows how to build an interactive console-based host application
that reads commands from the command line, executes the commands, and then displays the
results to the console. This host application also supports displaying prompts that allow the
user to specify multiple choices.

Host05 Sample This sample shows how to build an interactive console-based host application
that reads commands from the command line, executes the commands, and then displays the
results to the console. This host application also supports calls to remote computers by using
the Enter-PSSession and Exit-PSSession cmdlets

Host06 Sample This sample shows how to build an interactive console-based host application
that reads commands from the command line, executes the commands, and then displays the
results to the console. In addition, this sample uses the Tokenizer APIs to specify the color of
the text that is entered by the user.

See Also

<!-- p.2085 -->

Last updated on 05/20/2025

<!-- p.2086 -->

Host01 Sample
This sample shows how to implement a host application that uses a custom host. In this sample
a runspace is created that uses the custom host, and then the
System.Management.Automation.PowerShell API is used to run a script that calls "exit." The
host application then looks at the output of the script and prints out the results.

This sample uses the default UI features provided by Windows PowerShell. For more
information about implementing the UI features of a custom host, see Host02 Sample.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a custom host class that derives from the
      System.Management.Automation.Host.PSHost class.

      Creating a runspace that uses the custom host class.

      Creating a System.Management.Automation.PowerShell object that runs a script that calls
      exit.

      Verifying that the correct exit code was used in the exit process.

Example 1
The following code shows an implementation of a host application that uses a simple custom
host interface.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {

       using System;
       using System.Management.Automation;
       using System.Management.Automation.Runspaces;
       using PowerShell = System.Management.Automation.PowerShell;

<!-- p.2087 -->

/// <summary>
/// This class contains the Main entry point for this host application.
/// </summary>
internal class Host01
{

   /// <summary>
   /// Indicator to tell the host application that it should exit.
   /// </summary>
   private bool shouldExit;

   /// <summary>
   /// The exit code that the host application will use to exit.
   /// </summary>
   private int exitCode;

   /// <summary>
   /// Gets or sets a value indicating whether the
   /// host application should exit.
   /// </summary>
   public bool ShouldExit
   {
       get { return this.shouldExit; }
       set { this.shouldExit = value; }
   }

   /// <summary>
   /// Gets or sets the PSHost implementation that is
   /// used to tell the host application what code to use
   /// when exiting.
   /// </summary>
   public int ExitCode
   {
       get { return this.exitCode; }
       set { this.exitCode = value; }
   }

   /// <summary>
   /// This sample uses a PowerShell object to run
   /// a script that calls exit. The host application looks at
   /// this and prints out the result.
   /// </summary>
   /// <param name="args">Parameter not used.</param>
   private static void Main(string[] args)
   {
       // Create an instance of this host application class so that
       // the Windows PowerShell engine will have access to the
       // ShouldExit and ExitCode parameters.
       Host01 me = new Host01();

       // Create the host instance to use.
       MyHost myHost = new MyHost(me);

       // Create a runspace that uses the host object and run the
       // script using a PowerShell object.

<!-- p.2088 -->

              using (Runspace myRunSpace = RunspaceFactory.CreateRunspace(myHost))
              {
                  // Open the runspace.
                  myRunSpace.Open();

                   // Create a PowerShell object to run the script.
                   using (PowerShell powershell = PowerShell.Create())
                   {
                       powershell.Runspace = myRunSpace;

                       // Create the pipeline and run the script
                       // "exit (2+2)".
                       string script = "exit (2+2)";
                       powershell.AddScript(script);
                       powershell.Invoke(script);
                   }

                   // Check the flags and see if they were set properly.
                   Console.WriteLine(
                       "ShouldExit={0} (should be True); ExitCode={1} (should be 4)",
                       me.ShouldExit,
                       me.ExitCode);

                   // close the runspace to free resources.
                   myRunSpace.Close();
              }

              Console.WriteLine("Hit any key to exit...");
              Console.ReadKey();
          }
      }
 }

Example 2
The following code is the implementation of the System.Management.Automation.Host.PSHost
class that is used by this host application. Those elements that are not implemented throw an
exception or return nothing.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
     using System;
     using System.Globalization;
     using System.Management.Automation.Host;

      /// <summary>
      /// This is a sample implementation of the PSHost abstract class for
      /// console applications. Not all members are implemented. Those that
      /// are not implemented throw a NotImplementedException exception or

<!-- p.2089 -->

/// return nothing.
/// </summary>
internal class MyHost : PSHost
{
    /// <summary>
    /// A reference to the PSHost implementation.
    /// </summary>
    private Host01 program;

   /// <summary>
   /// The culture information of the thread that created
   /// this object.
   /// </summary>
   private CultureInfo originalCultureInfo =
       System.Threading.Thread.CurrentThread.CurrentCulture;

   /// <summary>
   /// The UI culture information of the thread that created
   /// this object.
   /// </summary>
   private CultureInfo originalUICultureInfo =
       System.Threading.Thread.CurrentThread.CurrentUICulture;

   /// <summary>
   /// The identifier of this PSHost implementation.
   /// </summary>
   private Guid myId = Guid.NewGuid();

   /// <summary>
   /// Initializes a new instance of the MyHost class. Keep
   /// a reference to the host application object so that it
   /// can be informed of when to exit.
   /// </summary>
   /// <param name="program">
   /// A reference to the host application object.
   /// </param>
   public MyHost(Host01 program)
   {
       this.program = program;
   }

   /// <summary>
   /// Return the culture information to use. This implementation
   /// returns a snapshot of the culture information of the thread
   /// that created this object.
   /// </summary>
   public override System.Globalization.CultureInfo CurrentCulture
   {
       get { return this.originalCultureInfo; }
   }

   /// <summary>
   /// Return the UI culture information to use. This implementation
   /// returns a snapshot of the UI culture information of the thread
   /// that created this object.

<!-- p.2090 -->

/// </summary>
public override System.Globalization.CultureInfo CurrentUICulture
{
    get { return this.originalUICultureInfo; }
}

/// <summary>
/// This implementation always returns the GUID allocated at
/// instantiation time.
/// </summary>
public override Guid InstanceId
{
    get { return this.myId; }
}

/// <summary>
/// Return a string that contains the name of the host implementation.
/// Keep in mind that this string may be used by script writers to
/// identify when your host is being used.
/// </summary>
public override string Name
{
    get { return "MySampleConsoleHostImplementation"; }
}

/// <summary>
/// This sample does not implement a PSHostUserInterface component so
/// this property simply returns null.
/// </summary>
public override PSHostUserInterface UI
{
    get { return null; }
}

/// <summary>
/// Return the version object for this application. Typically this
/// should match the version resource in the application.
/// </summary>
public override Version Version
{
    get { return new Version(1, 0, 0, 0); }
}

/// <summary>
/// Not implemented by this example class. The call fails with
/// a NotImplementedException exception.
/// </summary>
public override void EnterNestedPrompt()
{
    throw new NotImplementedException(
        "The method or operation is not implemented.");
}

/// <summary>
/// Not implemented by this example class. The call fails

<!-- p.2091 -->

           /// with a NotImplementedException exception.
           /// </summary>
           public override void ExitNestedPrompt()
           {
               throw new NotImplementedException(
                   "The method or operation is not implemented.");
           }

           /// <summary>
           /// This API is called before an external application process is
           /// started. Typically it is used to save state so the parent can
           /// restore state that has been modified by a child process (after
           /// the child exits). In this example, this functionality is not
           /// needed so the method returns nothing.
           /// </summary>
           public override void NotifyBeginApplication()
           {
               return;
           }

           /// <summary>
           /// This API is called after an external application process finishes.
           /// Typically it is used to restore state that a child process may
           /// have altered. In this example, this functionality is not
           /// needed so the method returns nothing.
           /// </summary>
           public override void NotifyEndApplication()
           {
              return;
           }

           /// <summary>
           /// Indicate to the host application that exit has
           /// been requested. Pass the exit code that the host
           /// application should use when exiting the process.
           /// </summary>
           /// <param name="exitCode">The exit code to use.</param>
           public override void SetShouldExit(int exitCode)
           {
               this.program.ShouldExit = true;
               this.program.ExitCode = exitCode;
           }
      }
 }

See Also

Last updated on 05/20/2025

<!-- p.2092 -->

Host02 Sample
This sample shows how to write a host application that uses the Windows PowerShell runtime
along with a custom host implementation. The host application sets the host culture to
German, runs the Get-Process cmdlet and displays the results as you would see them by using
pwrsh.exe, and then prints out the current data and time in German.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a custom host whose classes derive from the
      System.Management.Automation.Host.PSHost class, the
      System.Management.Automation.Host.PSHostUserInterface class, and the
      System.Management.Automation.Host.PSHostRawUserInterface class.

      Creating a runspace that uses the custom host.

      Setting the host culture to German.

      Creating a System.Management.Automation.PowerShell object that runs a script to
      retrieve and sort the processes, then retrieves the current date which is displayed in
      German.

Example 1
The following code shows an implementation of a host application that uses the custom host.

 C#

 // Copyright (c) 2006 Microsoft Corporation. All rights reserved.
 //
 // THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
 // ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 // THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 // PARTICULAR PURPOSE.
 //
 using System;
 using System.Collections.Generic;

<!-- p.2093 -->

using System.Text;
using System.Management.Automation;
using System.Management.Automation.Host;
using System.Management.Automation.Runspaces;
using System.Globalization;

namespace Microsoft.Samples.PowerShell.Host
{
  class Host02
  {
    /// <summary>
    /// Define the property that the PSHost implementation will
    /// use to tell the host application that it should exit.
    /// </summary>
    public bool ShouldExit
    {
      get { return shouldExit; }
      set { shouldExit = value; }
    }
    private bool shouldExit;

    /// <summary>
    /// Define the property that the PSHost implementation will
    /// use to tell the host application what exit code to use
    /// when exiting.
    /// </summary>
    public int ExitCode
    {
      get { return exitCode; }
      set { exitCode = value; }
    }
    private int exitCode;

    /// <summary>
    /// This sample uses the PowerShell runtime along with a host
    /// implementation to call Get-Process and display the results
    /// as you would see them in powershell.exe.
    /// </summary>
    /// <param name="args">Ignored</param>
    static void Main(string[] args)
    {
       // Set the current culture to German. We want this to be picked up when the
MyHost
       // instance is created...
       System.Threading.Thread.CurrentThread.CurrentCulture =
CultureInfo.GetCultureInfo("de-de");

      // Create the runspace so that you can access the pipeline.
      MyHost myHost = new MyHost(new Host02());

      Runspace myRunSpace = RunspaceFactory.CreateRunspace(myHost);
      myRunSpace.Open();

      // Create the pipeline.
      Pipeline pipe = myRunSpace.CreatePipeline();

<!-- p.2094 -->

             // Add the script we want to run. This script does two things.
             // First, it runs the Get-Process cmdlet with the cmdlet output
             // sorted by handle count. Second, the GetDate cmdlet is piped
             // to the Out-String cmdlet so that we can see the
             // date displayed in German.

             pipe.Commands.AddScript(@"
                           Get-Process | sort HandleCount
                           # This should display the date in German...
                           Get-Date | Out-String
                           ");

       // Add the default outputter to the end of the pipe and indicate
       // that it should handle both output and errors from the previous
       // commands. This will result in the output being written using the PSHost
       // and PSHostUserInterface classes instead of returning objects to the
 hosting
       // application.
       pipe.Commands.Add("Out-Default");

 pipe.Commands[0].MergeMyResults(PipelineResultTypes.Error,PipelineResultTypes.Outpu
 t);

             // Invoke the pipeline. There will not be any objects
             // returned. The Out-Default cmdlet consumes the objects.
             pipe.Invoke();

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

Example 2
The following code is the implementation of the System.Management.Automation.Host.PSHost
class that is used by this host application. Those elements that are not implemented throw an
exception or return nothing.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;
   using System.Globalization;
   using System.Management.Automation.Host;

     /// <summary>
     /// This is a sample implementation of the PSHost abstract class for
     /// console applications. Not all members are implemented. Those that

<!-- p.2095 -->

/// are not implemented throw a NotImplementedException exception or
/// return nothing.
/// </summary>
internal class MyHost : PSHost
{
  /// <summary>
  /// A reference to the PSHost implementation.
  /// </summary>
  private Host02 program;

 /// <summary>
 /// The culture information of the thread that created
 /// this object.
 /// </summary>
 private CultureInfo originalCultureInfo =
     System.Threading.Thread.CurrentThread.CurrentCulture;

 /// <summary>
 /// The UI culture information of the thread that created
 /// this object.
 /// </summary>
 private CultureInfo originalUICultureInfo =
     System.Threading.Thread.CurrentThread.CurrentUICulture;

 /// <summary>
 /// The identifier of this PSHost implementation.
 /// </summary>
 private Guid myId = Guid.NewGuid();

 /// <summary>
 /// Initializes a new instance of the MyHost class. Keep
 /// a reference to the host application object so that it
 /// can be informed of when to exit.
 /// </summary>
 /// <param name="program">
 /// A reference to the host application object.
 /// </param>
 public MyHost(Host02 program)
 {
   this.program = program;
 }

 /// <summary>
 /// A reference to the implementation of the PSHostUserInterface
 /// class for this application.
 /// </summary>
 private MyHostUserInterface myHostUserInterface = new MyHostUserInterface();

 /// <summary>
 /// Gets the culture information to use. This implementation
 /// returns a snapshot of the culture information of the thread
 /// that created this object.
 /// </summary>
 public override System.Globalization.CultureInfo CurrentCulture
 {

<!-- p.2096 -->

    get { return this.originalCultureInfo; }
}

/// <summary>
/// Gets the UI culture information to use. This implementation
/// returns a snapshot of the UI culture information of the thread
/// that created this object.
/// </summary>
public override System.Globalization.CultureInfo CurrentUICulture
{
  get { return this.originalUICultureInfo; }
}

/// <summary>
/// Gets an identifier for this host. This implementation always
/// returns the GUID allocated at instantiation time.
/// </summary>
public override Guid InstanceId
{
  get { return this.myId; }
}

/// <summary>
/// Gets a string that contains the name of this host implementation.
/// Keep in mind that this string may be used by script writers to
/// identify when your host is being used.
/// </summary>
public override string Name
{
  get { return "MySampleConsoleHostImplementation"; }
}

/// <summary>
/// Gets an instance of the implementation of the PSHostUserInterface
/// class for this application. This instance is allocated once at startup time
/// and returned every time thereafter.
/// </summary>
public override PSHostUserInterface UI
{
  get { return this.myHostUserInterface; }
}

/// <summary>
/// Gets the version object for this application. Typically this
/// should match the version resource in the application.
/// </summary>
public override Version Version
{
  get { return new Version(1, 0, 0, 0); }
}

/// <summary>
/// This API Instructs the host to interrupt the currently running
/// pipeline and start a new nested input loop. In this example this
/// functionality is not needed so the method throws a

<!-- p.2097 -->

/// NotImplementedException exception.
/// </summary>
public override void EnterNestedPrompt()
{
  throw new NotImplementedException(
        "The method or operation is not implemented.");
}

/// <summary>
/// This API instructs the host to exit the currently running input loop.
/// In this example this functionality is not needed so the method
/// throws a NotImplementedException exception.
/// </summary>
public override void ExitNestedPrompt()
{
  throw new NotImplementedException(
        "The method or operation is not implemented.");
}

/// <summary>
/// This API is called before an external application process is
/// started. Typically it is used to save state so that the parent
/// can restore state that has been modified by a child process (after
/// the child exits). In this example this functionality is not
/// needed so the method returns nothing.
/// </summary>
public override void NotifyBeginApplication()
{
  return;
}

/// <summary>
/// This API is called after an external application process finishes.
/// Typically it is used to restore state that a child process has
/// altered. In this example, this functionality is not needed so
/// the method returns nothing.
/// </summary>
public override void NotifyEndApplication()
{
  return;
}

/// <summary>
/// Indicate to the host application that exit has
/// been requested. Pass the exit code that the host
/// application should use when exiting the process.
/// </summary>
/// <param name="exitCode">The exit code that the
/// host application should use.</param>
public override void SetShouldExit(int exitCode)
{
  this.program.ShouldExit = true;
  this.program.ExitCode = exitCode;
}

<!-- p.2098 -->

     }
 }

Example 3
The following code is the implementation of the
System.Management.Automation.Host.PSHostUserInterface class that is used by this host
application.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;
   using System.Collections.Generic;
   using System.Globalization;
   using System.Management.Automation;
   using System.Management.Automation.Host;

     /// <summary>
     /// A sample implementation of the PSHostUserInterface abstract class for
     /// console applications. Not all members are implemented. Those that are
     /// not implemented throw a NotImplementedException exception. Members that
     /// are implemented include those that map easily to Console APIs.
     /// </summary>
     internal class MyHostUserInterface : PSHostUserInterface
     {
       /// <summary>
       /// An instance of the PSRawUserInterface class.
       /// </summary>
       private MyRawUserInterface myRawUi = new MyRawUserInterface();

         /// <summary>
         /// Gets an instance of the PSRawUserInterface class for this host
         /// application.
         /// </summary>
         public override PSHostRawUserInterface RawUI
         {
           get { return this.myRawUi; }
         }

         /// <summary>
         /// Prompts the user for input. In this example this functionality is not
         /// needed so the method throws a NotImplementException exception.
         /// </summary>
         /// <param name="caption">The caption or title of the prompt.</param>
         /// <param name="message">The text of the prompt.</param>
         /// <param name="descriptions">A collection of FieldDescription objects that
         /// describe each field of the prompt.</param>
         /// <returns>Throws a NotImplementedException exception.</returns>
         public override Dictionary<string, PSObject> Prompt(

<!-- p.2099 -->

                                                        string caption,
                                                        string message,

System.Collections.ObjectModel.Collection<FieldDescription> descriptions)
    {
       throw new NotImplementedException(
           "The method or operation is not implemented.");
    }

    /// <summary>
    /// Provides a set of choices that enable the user to choose a
    /// single option from a set of options. In this example this
    /// functionality is not needed so the method throws a
    /// NotImplementException exception.
    /// </summary>
    /// <param name="caption">Text that proceeds (a title) the choices.</param>
    /// <param name="message">A message that describes the choice.</param>
    /// <param name="choices">A collection of ChoiceDescription objects that
describes
    /// each choice.</param>
    /// <param name="defaultChoice">The index of the label in the Choices parameter
    /// collection. To indicate no default choice, set to -1.</param>
    /// <returns>Throws a NotImplementedException exception.</returns>
    public override int PromptForChoice(string caption, string message,
System.Collections.ObjectModel.Collection<ChoiceDescription> choices, int
defaultChoice)
    {
      throw new NotImplementedException("The method or operation is not
implemented.");
    }

    /// <summary>
    /// Prompts the user for credentials with a specified prompt window caption,
    /// prompt message, user name, and target name. In this example this
    /// functionality is not needed so the method throws a
    /// NotImplementException exception.
    /// </summary>
    /// <param name="caption">The caption for the message window.</param>
    /// <param name="message">The text of the message.</param>
    /// <param name="userName">The user name whose credential is to be prompted
for.</param>
    /// <param name="targetName">The name of the target for which the credential is
collected.</param>
    /// <returns>Throws a NotImplementedException exception.</returns>
    public override PSCredential PromptForCredential(
                                                     string caption,
                                                     string message,
                                                     string userName,
                                                     string targetName)
    {
      throw new NotImplementedException("The method or operation is not
implemented.");
    }

    /// <summary>

<!-- p.2100 -->

    /// Prompts the user for credentials by using a specified prompt window
caption,
    /// prompt message, user name and target name, credential types allowed to be
    /// returned, and UI behavior options. In this example this functionality
    /// is not needed so the method throws a NotImplementException exception.
    /// </summary>
    /// <param name="caption">The caption for the message window.</param>
    /// <param name="message">The text of the message.</param>
    /// <param name="userName">The user name whose credential is to be prompted
for.</param>
    /// <param name="targetName">The name of the target for which the credential is
collected.</param>
    /// <param name="allowedCredentialTypes">A PSCredentialTypes constant that
    /// identifies the type of credentials that can be returned.</param>
    /// <param name="options">A PSCredentialUIOptions constant that identifies the
UI
    /// behavior when it gathers the credentials.</param>
    /// <returns>Throws a NotImplementedException exception.</returns>
    public override PSCredential PromptForCredential(
                                                     string caption,
                                                     string message,
                                                     string userName,
                                                     string targetName,
                                                     PSCredentialTypes
allowedCredentialTypes,
                                                     PSCredentialUIOptions options)
    {
      throw new NotImplementedException("The method or operation is not
implemented.");
    }

    /// <summary>
    /// Reads characters that are entered by the user until a newline
    /// (carriage return) is encountered.
    /// </summary>
    /// <returns>The characters that are entered by the user.</returns>
    public override string ReadLine()
    {
      return Console.ReadLine();
    }

    /// <summary>
    /// Reads characters entered by the user until a newline (carriage return)
    /// is encountered and returns the characters as a secure string. In this
    /// example this functionality is not needed so the method throws a
    /// NotImplementException exception.
    /// </summary>
    /// <returns>Throws a NotImplemented exception.</returns>
    public override System.Security.SecureString ReadLineAsSecureString()
    {
      throw new NotImplementedException("The method or operation is not
implemented.");
    }

    /// <summary>

<!-- p.2101 -->

/// Writes characters to the output display of the host.
/// </summary>
/// <param name="value">The characters to be written.</param>
public override void Write(string value)
{
  System.Console.Write(value);
}

/// <summary>
/// Writes characters to the output display of the host and specifies the
/// foreground and background colors of the characters. This implementation
/// ignores the colors.
/// </summary>
/// <param name="foregroundColor">The color of the characters.</param>
/// <param name="backgroundColor">The background color to use.</param>
/// <param name="value">The characters to be written.</param>
public override void Write(
                           ConsoleColor foregroundColor,
                           ConsoleColor backgroundColor,
                           string value)
{
   // Colors are ignored.
   System.Console.Write(value);
}

/// <summary>
/// Writes a debug message to the output display of the host.
/// </summary>
/// <param name="message">The debug message that is displayed.</param>
public override void WriteDebugLine(string message)
{
  Console.WriteLine(String.Format(
                                  CultureInfo.CurrentCulture,
                                  "DEBUG: {0}",
                                  message));
}

/// <summary>
/// Writes an error message to the output display of the host.
/// </summary>
/// <param name="value">The error message that is displayed.</param>
public override void WriteErrorLine(string value)
{
  Console.WriteLine(String.Format(
                                  CultureInfo.CurrentCulture,
                                  "ERROR: {0}",
                                  value));
}

/// <summary>
/// Writes a newline character (carriage return)
/// to the output display of the host.
/// </summary>
public override void WriteLine()
{

<!-- p.2102 -->

        System.Console.WriteLine();
    }

    /// <summary>
    /// Writes a line of characters to the output display of the host
    /// and appends a newline character(carriage return).
    /// </summary>
    /// <param name="value">The line to be written.</param>
    public override void WriteLine(string value)
    {
      System.Console.WriteLine(value);
    }

    /// <summary>
    /// Writes a line of characters to the output display of the host
    /// with foreground and background colors and appends a newline (carriage
return).
    /// </summary>
    /// <param name="foregroundColor">The foreground color of the display. </param>
    /// <param name="backgroundColor">The background color of the display. </param>
    /// <param name="value">The line to be written.</param>
    public override void WriteLine(ConsoleColor foregroundColor, ConsoleColor
backgroundColor, string value)
    {
      // Write to the output stream, ignore the colors
      System.Console.WriteLine(value);
    }

    /// <summary>
    /// Writes a progress report to the output display of the host.
    /// </summary>
    /// <param name="sourceId">Unique identifier of the source of the record.
</param>
    /// <param name="record">A ProgressReport object.</param>
    public override void WriteProgress(long sourceId, ProgressRecord record)
    {
    }

    /// <summary>
    /// Writes a verbose message to the output display of the host.
    /// </summary>
    /// <param name="message">The verbose message that is displayed.</param>
    public override void WriteVerboseLine(string message)
    {
      Console.WriteLine(String.Format(CultureInfo.CurrentCulture, "VERBOSE: {0}",
message));
    }

    /// <summary>
    /// Writes a warning message to the output display of the host.
    /// </summary>
    /// <param name="message">The warning message that is displayed.</param>
    public override void WriteWarningLine(string message)
    {
      Console.WriteLine(String.Format(CultureInfo.CurrentCulture, "WARNING: {0}",

<!-- p.2103 -->

 message));
     }
   }
 }

Example 4
The following code is the implementation of the
System.Management.Automation.Host.PSHostRawUserInterface class that is used by this host
application. Those elements that are not implemented throw an exception or return nothing.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;
   using System.Management.Automation.Host;

   /// <summary>
   /// A sample implementation of the PSHostRawUserInterface for console
   /// applications. Members of this class that easily map to the .NET
   /// console class are implemented. More complex methods are not
   /// implemented and throw a NotImplementedException exception.
   /// </summary>
   internal class MyRawUserInterface : PSHostRawUserInterface
   {
     /// <summary>
     /// Gets or sets the background color of the displayed text.
     /// This maps to the corresponding Console.Background property.
     /// </summary>
     public override ConsoleColor BackgroundColor
     {
       get { return Console.BackgroundColor; }
       set { Console.BackgroundColor = value; }
     }

      /// <summary>
      /// Gets or sets the size of the host buffer. In this example the
      /// buffer size is adapted from the Console buffer size members.
      /// </summary>
      public override Size BufferSize
      {
        get { return new Size(Console.BufferWidth, Console.BufferHeight); }
        set { Console.SetBufferSize(value.Width, value.Height); }
      }

      /// <summary>
      /// Gets or sets the cursor position. In this example this
      /// functionality is not needed so the property throws a
      /// NotImplementException exception.
      /// </summary>

<!-- p.2104 -->

    public override Coordinates CursorPosition
    {
      get { throw new NotImplementedException(
                 "The method or operation is not implemented."); }
      set { throw new NotImplementedException(
                 "The method or operation is not implemented."); }
    }

    /// <summary>
    /// Gets or sets the size of the displayed cursor. In this example
    /// the cursor size is taken directly from the Console.CursorSize
    /// property.
    /// </summary>
    public override int CursorSize
    {
      get { return Console.CursorSize; }
      set { Console.CursorSize = value; }
    }

    /// <summary>
    /// Gets or sets the foreground color of the displayed text.
    /// This maps to the corresponding Console.ForegroundColor property.
    /// </summary>
    public override ConsoleColor ForegroundColor
    {
      get { return Console.ForegroundColor; }
      set { Console.ForegroundColor = value; }
    }

    /// <summary>
    /// Gets a value indicating whether the user has pressed a key. This maps
    /// to the corresponding Console.KeyAvailable property.
    /// </summary>
    public override bool KeyAvailable
    {
      get { return Console.KeyAvailable; }
    }

    /// <summary>
    /// Gets the dimensions of the largest window that could be
    /// rendered in the current display, if the buffer was at the least
    /// that large. This example uses the Console.LargestWindowWidth and
    /// Console.LargestWindowHeight properties to determine the returned
    /// value of this property.
    /// </summary>
    public override Size MaxPhysicalWindowSize
    {
      get { return new Size(Console.LargestWindowWidth,
Console.LargestWindowHeight); }
    }

    /// <summary>
    /// Gets the dimensions of the largest window size that can be
    /// displayed. This example uses the Console.LargestWindowWidth and
    /// console.LargestWindowHeight properties to determine the returned

<!-- p.2105 -->

    /// value of this property.
    /// </summary>
    public override Size MaxWindowSize
    {
      get { return new Size(Console.LargestWindowWidth,
Console.LargestWindowHeight); }
    }

    /// <summary>
    /// Gets or sets the position of the displayed window. This example
    /// uses the Console window position APIs to determine the returned
    /// value of this property.
    /// </summary>
    public override Coordinates WindowPosition
    {
      get { return new Coordinates(Console.WindowLeft, Console.WindowTop); }
      set { Console.SetWindowPosition(value.X, value.Y); }
    }

    /// <summary>
    /// Gets or sets the size of the displayed window. This example
    /// uses the corresponding Console window size APIs to determine the
    /// returned value of this property.
    /// </summary>
    public override Size WindowSize
    {
      get { return new Size(Console.WindowWidth, Console.WindowHeight); }
      set { Console.SetWindowSize(value.Width, value.Height); }
    }

    /// <summary>
    /// Gets or sets the title of the displayed window. The example
    /// maps the Console.Title property to the value of this property.
    /// </summary>
    public override string WindowTitle
    {
      get { return Console.Title; }
      set { Console.Title = value; }
    }

    /// <summary>
    /// This API resets the input buffer. In this example this
    /// functionality is not needed so the method returns nothing.
    /// </summary>
    public override void FlushInputBuffer()
    {
    }

    /// <summary>
    /// This API returns a rectangular region of the screen buffer. In
    /// this example this functionality is not needed so the method throws
    /// a NotImplementException exception.
    /// </summary>
    /// <param name="rectangle">Defines the size of the rectangle.</param>
    /// <returns>Throws a NotImplementedException exception.</returns>

<!-- p.2106 -->

    public override BufferCell[,] GetBufferContents(Rectangle rectangle)
    {
      throw new NotImplementedException(
               "The method or operation is not implemented.");
    }

    /// <summary>
    /// This API reads a pressed, released, or pressed and released keystroke
    /// from the keyboard device, blocking processing until a keystroke is
    /// typed that matches the specified keystroke options. In this example
    /// this functionality is not needed so the method throws a
    /// NotImplementException exception.
    /// </summary>
    /// <param name="options">Options, such as IncludeKeyDown, used when
    /// reading the keyboard.</param>
    /// <returns>Throws a NotImplementedException exception.</returns>
    public override KeyInfo ReadKey(ReadKeyOptions options)
    {
      throw new NotImplementedException(
                "The method or operation is not implemented.");
    }

    /// <summary>
    /// This API crops a region of the screen buffer. In this example
    /// this functionality is not needed so the method throws a
    /// NotImplementException exception.
    /// </summary>
    /// <param name="source">The region of the screen to be scrolled.</param>
    /// <param name="destination">The region of the screen to receive the
    /// source region contents.</param>
    /// <param name="clip">The region of the screen to include in the operation.
</param>
    /// <param name="fill">The character and attributes to be used to fill all
cell.</param>
    public override void ScrollBufferContents(Rectangle source, Coordinates
destination, Rectangle clip, BufferCell fill)
    {
      throw new NotImplementedException(
                "The method or operation is not implemented.");
    }

    /// <summary>
    /// This method copies an array of buffer cells into the screen buffer
    /// at a specified location. In this example this functionality is
    /// not needed so the method throws a NotImplementedException exception.
    /// </summary>
    /// <param name="origin">The parameter is not used.</param>
    /// <param name="contents">The parameter is not used.</param>
    public override void SetBufferContents(Coordinates origin,
                                           BufferCell[,] contents)
    {
      throw new NotImplementedException(
                "The method or operation is not implemented.");
    }

<!-- p.2107 -->

         /// <summary>
         /// This method copies a given character, foreground color, and background
         /// color to a region of the screen buffer. In this example this
         /// functionality is not needed so the method throws a
         /// NotImplementException exception./// </summary>
         /// <param name="rectangle">Defines the area to be filled. </param>
         /// <param name="fill">Defines the fill character.</param>
         public override void SetBufferContents(Rectangle rectangle, BufferCell fill)
         {
           throw new NotImplementedException(
                     "The method or operation is not implemented.");
         }
     }
 }

See Also
System.Management.Automation.PowerShell

System.Management.Automation.Host.PSHost

System.Management.Automation.Host.PSHostUserInterface

System.Management.Automation.Host.PSHostRawUserInterface

Last updated on 05/20/2025

<!-- p.2108 -->

Host03 Sample
This sample shows how to build an interactive console-based host application that reads
commands from the command line, executes the commands, and then displays the results to
the console.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a custom host whose classes derive from the
      System.Management.Automation.Host.PSHost class, the
      System.Management.Automation.Host.PSHostUserInterface class, and the
      System.Management.Automation.Host.PSHostRawUserInterface class.

      Building a console application that uses these host classes to build an interactive
      Windows PowerShell shell.

Example 1
This example allows the user to enter commands at a command line, processes those
commands, and then prints out the results.

 C#

 // Copyright (c) 2006 Microsoft Corporation. All rights reserved.
 //
 // THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
 // ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 // THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 // PARTICULAR PURPOSE.
 //

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
   using PowerShell = System.Management.Automation.PowerShell;

<!-- p.2109 -->

/// This class contains the Main entry point for this host application.
internal class PSListenerConsoleSample
{
  /// Indicator to tell the host application that it should exit.
  private bool shouldExit;

 /// The exit code that the host application will use to exit.
 private int exitCode;

 /// Holds the instance of the PSHost implementation for this interpreter.
 private MyHost myHost;

 /// Holds the runspace for this interpreter.
 private Runspace myRunSpace;

 /// Holds a reference to the currently executing pipeline so it can be
 /// stopped by the control-C handler.
 private PowerShell currentPowerShell;

 /// Used to serialize access to instance data.
 private object instanceLock = new object();

 /// Create this instance of the console listener.
 private PSListenerConsoleSample()
 {
   // Create the host and runspace instances for this interpreter.
   // Note that this application does not support console files so
   // only the default snapins will be available.
   this.myHost = new MyHost(this);
   this.myRunSpace = RunspaceFactory.CreateRunspace(this.myHost);
   this.myRunSpace.Open();
 }

 /// Gets or sets a value indicating whether the host application
 /// should exit.
 public bool ShouldExit
 {
   get { return this.shouldExit; }
   set { this.shouldExit = value; }
 }

 /// Gets or sets the exit code that the host application will use
 /// when exiting.
 public int ExitCode
 {
   get { return this.exitCode; }
   set { this.exitCode = value; }
 }

 /// Creates and initiates the listener instance.
 /// param name="args";This parameter is not used.
 private static void Main(string[] args)
 {
   // Display the welcome message...

<!-- p.2110 -->

      Console.Title = "PowerShell Console Host Sample Application";
      ConsoleColor oldFg = Console.ForegroundColor;
      Console.ForegroundColor = ConsoleColor.Cyan;
      Console.WriteLine("    PowerShell Console Host Interactive Sample");
      Console.WriteLine("    =====================================");
      Console.WriteLine(string.Empty);
      Console.WriteLine("This is an example of a simple interactive console host
that uses the ");
      Console.WriteLine("Windows PowerShell engine to interpret commands. Type
'exit' to exit.");
      Console.WriteLine(string.Empty);
      Console.ForegroundColor = oldFg;

        // Create the listener and run it - this never returns...
        PSListenerConsoleSample listener = new PSListenerConsoleSample();
        listener.Run();
    }

    /// A helper class that builds and executes a pipeline that writes to the
    /// default output path. Any exceptions that are thrown are just passed to
    /// the caller. Since all output goes to the default outputter, this method()
    /// won't return anything.
    /// param name="cmd"; The script to run.
    /// param name="input";Any input arguments to pass to the script. If null
    /// then nothing is passed in.
    private void executeHelper(string cmd, object input)
    {
      // Ignore empty command lines.
      if (String.IsNullOrEmpty(cmd))
      {
        return;
      }

        // Create the pipeline object and make it available
        // to the ctrl-C handle through the currentPowerShell instance
        // variable
        lock (this.instanceLock)
        {
          this.currentPowerShell = PowerShell.Create();
        }

        this.currentPowerShell.Runspace = this.myRunSpace;

        // Create a pipeline for this execution. Place the result in the
        // currentPowerShell instance variable so that it is available
        // to be stopped.
        try
        {
          this.currentPowerShell.AddScript(cmd);

          // Now add the default outputter to the end of the pipe and indicate
          // that it should handle both output and errors from the previous
          // commands. This will result in the output being written using the PSHost
          // and PSHostUserInterface classes instead of returning objects to the
hosting

<!-- p.2111 -->

         // application.
         this.currentPowerShell.AddCommand("Out-Default");

this.currentPowerShell.Commands.Commands[0].MergeMyResults(PipelineResultTypes.Erro
r, PipelineResultTypes.Output);

         // If there was any input specified, pass it in, otherwise just
         // execute the pipeline.
         if (input != null)
         {
           this.currentPowerShell.Invoke(new object[] { input });
         }
         else
         {
           this.currentPowerShell.Invoke();
         }
        }
        finally
        {
          // Dispose of the pipeline line and set it to null, locked because
          // currentPowerShell may be accessed by the ctrl-C handler.
          lock (this.instanceLock)
          {
            this.currentPowerShell.Dispose();
            this.currentPowerShell = null;
          }
        }
    }

    /// An exception occurred that we want to display
    /// using the display formatter. To do this we run
    /// a second pipeline passing in the error record.
    /// The runtime will bind this to the $input variable
    /// which is why $input is being piped to Out-String.
    /// We then call WriteErrorLine to make sure the error
    /// gets displayed in the correct error color.

    /// param name="e"; The exception to display.
    private void ReportException(Exception e)
    {
      if (e != null)
      {
        object error;
        IContainsErrorRecord icer = e as IContainsErrorRecord;
        if (icer != null)
        {
          error = icer.ErrorRecord;
        }
        else
        {
          error = (object)new ErrorRecord(e, "Host.ReportException",
ErrorCategory.NotSpecified, null);
        }

         lock (this.instanceLock)

<!-- p.2112 -->

         {
             this.currentPowerShell = PowerShell.Create();
         }

         this.currentPowerShell.Runspace = this.myRunSpace;

         try
         {
           this.currentPowerShell.AddScript("$input").AddCommand("Out-String");

             // Do not merge errors, this function will swallow errors.
             Collection<PSObject> result;
             PSDataCollection<object> inputCollection = new PSDataCollection<object>
();
             inputCollection.Add(error);
             inputCollection.Complete();
             result = this.currentPowerShell.Invoke(inputCollection);

             if (result.Count > 0)
             {
               string str = result[0].BaseObject as string;
               if (!string.IsNullOrEmpty(str))
               {
                 // Remove \r\n that is added by Out-String.
                 this.myHost.UI.WriteErrorLine(str.Substring(0, str.Length - 2));
               }
             }
        }
        finally
        {
          // Dispose of the pipeline line and set it to null, locked because
currentPowerShell
          // may be accessed by the ctrl-C handler.
          lock (this.instanceLock)
          {
            this.currentPowerShell.Dispose();
            this.currentPowerShell = null;
          }
        }
      }
    }

      /// Basic script execution routine - any runtime exceptions are
      /// caught and passed back into the engine to display.

      /// param name="cmd"; The parameter is not used.
      private void Execute(string cmd)
      {
        try
        {
          // Execute the command with no input.
          this.executeHelper(cmd, null);
        }
        catch (RuntimeException rte)
        {

<!-- p.2113 -->

            this.ReportException(rte);
        }
    }

    /// Method used to handle control-C's from the user. It calls the
    /// pipeline Stop() method to stop execution. If any exceptions occur
    /// they are printed to the console but otherwise ignored.

    /// param name="sender"; See sender property of ConsoleCancelEventHandler
documentation.
    /// param name="e"; See e property of ConsoleCancelEventHandler documentation.
    private void HandleControlC(object sender, ConsoleCancelEventArgs e)
    {
      try
      {
        lock (this.instanceLock)
        {
          if (this.currentPowerShell != null &&
this.currentPowerShell.InvocationStateInfo.State == PSInvocationState.Running)
          {
            this.currentPowerShell.Stop();
          }
        }

            e.Cancel = true;
        }
        catch (Exception exception)
        {
          this.myHost.UI.WriteErrorLine(exception.ToString());
        }
    }

    /// Implements the basic listener loop. It sets up the ctrl-C handler, then
    /// reads a command from the user, executes it and repeats until the ShouldExit
    /// flag is set.
    private void Run()
    {
      // Set up the control-C handler.
      Console.CancelKeyPress += new ConsoleCancelEventHandler(this.HandleControlC);
      Console.TreatControlCAsInput = false;

      // Read commands to execute until ShouldExit is set by
      // the user calling "exit".
      while (!this.ShouldExit)
      {
        this.myHost.UI.Write(ConsoleColor.Cyan, ConsoleColor.Black,
"\nPSConsoleSample: ");
        string cmd = Console.ReadLine();
        this.Execute(cmd);
      }

        // Exit with the desired exit code that was set by exit command.
        // This is set in the host by the MyHost.SetShouldExit() implementation.
        Environment.Exit(this.ExitCode);
    }

<!-- p.2114 -->

     }
 }

Example 2
The following code is the implementation of the System.Management.Automation.Host.PSHost
class that is used by this host application. Those elements that are not implemented throw an
exception or return nothing.

 C#

 // Copyright (c) 2006 Microsoft Corporation. All rights reserved.
 //
 // THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
 // ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 // THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 // PARTICULAR PURPOSE.
 //
 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Management.Automation;
 using System.Management.Automation.Host;
 using System.Management.Automation.Runspaces;

 namespace Microsoft.Samples.PowerShell.Host
 {
   /// <summary>
   /// Simple PowerShell interactive console host listener implementation. This
 class
   /// implements a basic read-evaluate-print loop or 'listener' allowing you to
   /// interactively work with the PowerShell runtime.
   /// </summary>
   class PSListenerConsoleSample
   {
      /// <summary>
      /// Define the property that the PSHost implementation will use to tell the
 host
      /// application that it should exit.
      /// </summary>
      public bool ShouldExit
      {
        get { return shouldExit; }
        set { shouldExit = value; }
      }
      private bool shouldExit;

         /// <summary>
         /// Define the property that the PSHost implementation will use to tell the
 host
         /// application what code to use when exiting.

<!-- p.2115 -->

/// </summary>
public int ExitCode
{
  get { return exitCode; }
  set { exitCode = value; }
}
private int exitCode;
/// <summary>
/// Holds the instance of the PSHost implementation for this interpreter.
/// </summary>
private MyHost myHost;

/// <summary>
/// Holds the runspace for this interpreter.
/// </summary>
private Runspace myRunSpace;

/// <summary>
/// Holds a reference to the currently executing pipeline so it can be
/// stopped by the control-C handler.
/// </summary>
private Pipeline currentPipeline;

/// <summary>
/// Used to serialize access to instance data...
/// </summary>
private object instanceLock = new object();

/// <summary>
/// Create this instance of the console listener.
/// </summary>
PSListenerConsoleSample()
{
  // Create the host and runspace instances for this interpreter. Note that
  // this application doesn't support console files so only the default snapins
  // will be available.
  myHost = new MyHost(this);
  myRunSpace = RunspaceFactory.CreateRunspace(myHost);
  myRunSpace.Open();
}

/// <summary>
/// A helper class that builds and executes a pipeline that writes to the
/// default output path. Any exceptions that are thrown are just passed to
/// the caller. Since all output goes to the default outputter, this method()
/// won't return anything.
/// </summary>
/// <param name="cmd">The script to run</param>
/// <param name="input">Any input arguments to pass to the script. If null
/// then nothing is passed in.</param>
void executeHelper(string cmd, object input)
{
  // Ignore empty command lines.
  if (String.IsNullOrEmpty(cmd))
    return;

<!-- p.2116 -->

      // Create the pipeline object and make it available
      // to the ctrl-C handle through the currentPipeline instance
      // variable.
      lock (instanceLock)
      {
        currentPipeline = myRunSpace.CreatePipeline();
      }

      // Create a pipeline for this execution. Place the result in the
currentPipeline
      // instance variable so that it is available to be stopped.
      try
      {
        currentPipeline.Commands.AddScript(cmd);

          // Now add the default outputter to the end of the pipe and indicate
          // that it should handle both output and errors from the previous
          // commands. This will result in the output being written using the PSHost
          // and PSHostUserInterface classes instead of returning objects to the
hosting
        // application.
        currentPipeline.Commands.Add("Out-Default");
        currentPipeline.Commands[0].MergeMyResults(PipelineResultTypes.Error,
PipelineResultTypes.Output);

          // If there was any input specified, pass it in, otherwise just
          // execute the pipeline.
          if (input != null)
          {
            currentPipeline.Invoke(new object[] { input });
          }
          else
          {
            currentPipeline.Invoke();
          }
      }
      finally
      {
        // Dispose of the pipeline line and set it to null, locked because
currentPipeline
        // may be accessed by the ctrl-C handler.
        lock (instanceLock)
        {
          currentPipeline.Dispose();
          currentPipeline = null;
        }
      }
    }

    /// <summary>
    /// Basic script execution routine - any runtime exceptions are
    /// caught and passed back into the runtime to display.
    /// </summary>
    /// <param name="cmd"></param>

<!-- p.2117 -->

    void Execute(string cmd)
    {
      try
      {
        // execute the command with no input...
        executeHelper(cmd, null);
      }
      catch (RuntimeException rte)
      {
        // An exception occurred that we want to display
        // using the display formatter. To do this we run
        // a second pipeline passing in the error record.
        // The runtime will bind this to the $input variable
        // which is why $input is being piped to Out-Default
        executeHelper("$input | Out-Default", rte.ErrorRecord);
      }
    }

    /// <summary>
    /// Method used to handle control-C's from the user. It calls the
    /// pipeline Stop() method to stop execution. If any exceptions occur,
    /// they are printed to the console; otherwise they are ignored.
    /// </summary>
    /// <param name="sender">See ConsoleCancelEventHandler documentation</param>
    /// <param name="e">See ConsoleCancelEventHandler documentation</param>
    void HandleControlC(object sender, ConsoleCancelEventArgs e)
    {
      try
      {
        lock (instanceLock)
        {
          if (currentPipeline != null && currentPipeline.PipelineStateInfo.State ==
PipelineState.Running)
                    currentPipeline.Stop();
        }
        e.Cancel = true;
      }
      catch (Exception exception)
      {
        this.myHost.UI.WriteErrorLine(exception.ToString());
      }
    }

    /// <summary>
    /// Implements the basic listener loop. It sets up the ctrl-C handler, then
    /// reads a command from the user, executes it and repeats until the ShouldExit
    /// flag is set.
    /// </summary>
    private void Run()
    {
      // Set up the control-C handler.
      Console.CancelKeyPress += new ConsoleCancelEventHandler(HandleControlC);
      Console.TreatControlCAsInput = false;

      // Loop reading commands to execute until ShouldExit is set by

<!-- p.2118 -->

             // the user calling "exit".
             while (!ShouldExit)
             {
               myHost.UI.Write(ConsoleColor.Cyan, ConsoleColor.Black, "\nPSConsoleSample:
 ");
                 string cmd = Console.ReadLine();
                 Execute(cmd);
             }

             // Exit with the desired exit code that was set by exit command.
             // This is set in the host by the MyHost.SetShouldExit() implementation.
             Environment.Exit(ExitCode);
         }

     /// <summary>
     /// Creates and initiates the listener instance.
     /// </summary>
     /// <param name="args">Ignored for now.</param>
     static void Main(string[] args)
     {
       // Display the welcome message.
       Console.Title = "PowerShell Console Host Sample Application";
       ConsoleColor oldFg = Console.ForegroundColor;
       Console.ForegroundColor = ConsoleColor.Cyan;
       Console.WriteLine("    PowerShell Console Host Interactive Sample");
       Console.WriteLine("    =====================================");
       Console.WriteLine("");
       Console.WriteLine("This is an example of a simple interactive console host
 using the PowerShell");
       Console.WriteLine("engine to interpret commands. Type 'exit' to exit.");
       Console.WriteLine("");
       Console.ForegroundColor = oldFg;

             // Create the listener and run it - this never returns.
             PSListenerConsoleSample listener = new PSListenerConsoleSample();
             listener.Run();
         }
     }
 }

Example 3
The following code is the implementation of the
System.Management.Automation.Host.PSHostUserInterface class that is used by this host
application.

 C#

 namespace Microsoft.Samples.PowerShell.Host
 {
   using System;

<!-- p.2119 -->

using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Globalization;
using System.Management.Automation;
using System.Management.Automation.Host;
using System.Text;

/// <summary>
/// A sample implementation of the PSHostUserInterface abstract class for
/// console applications. Not all members are implemented. Those that are
/// not implemented throw a NotImplementedException exception or return
/// nothing. Members that are implemented include those that map easily to
/// Console APIs and a basic implementation of the prompt API provided.
/// </summary>
internal class MyHostUserInterface : PSHostUserInterface
{
  /// <summary>
  /// An instance of the PSRawUserInterface object.
  /// </summary>
  private MyRawUserInterface myRawUi = new MyRawUserInterface();

 /// <summary>
 /// Gets an instance of the PSRawUserInterface object for this host
 /// application.
 /// </summary>
 public override PSHostRawUserInterface RawUI
 {
   get { return this.myRawUi; }
 }

 /// <summary>
 /// Prompts the user for input.
 /// <param name="caption">The caption or title of the prompt.</param>
 /// <param name="message">The text of the prompt.</param>
 /// <param name="descriptions">A collection of FieldDescription objects that
 /// describe each field of the prompt.</param>
 /// <returns>A dictionary object that contains the results of the user
 /// prompts.</returns>
 public override Dictionary<string, PSObject> Prompt(
                                    string caption,
                                    string message,
                                    Collection<FieldDescription> descriptions)
 {
   this.Write(
              ConsoleColor.Blue,
              ConsoleColor.Black,
              caption + "\n" + message + " ");
   Dictionary<string, PSObject> results =
            new Dictionary<string, PSObject>();
   foreach (FieldDescription fd in descriptions)
   {
     string[] label = GetHotkeyAndLabel(fd.Label);
     this.WriteLine(label[1]);
     string userData = Console.ReadLine();
     if (userData == null)

<!-- p.2120 -->

            {
                return null;
            }

            results[fd.Name] = PSObject.AsPSObject(userData);
        }

        return results;
    }

    /// <summary>

/// Provides a set of choices that enable the user to choose a
    /// single option from a set of options.
    /// </summary>
    /// <param name="caption">Text that proceeds (a title) the choices.</param>
    /// <param name="message">A message that describes the choice.</param>
    /// <param name="choices">A collection of ChoiceDescription objects that
describe
    /// each choice.</param>
    /// <param name="defaultChoice">The index of the label in the Choices parameter
    /// collection. To indicate no default choice, set to -1.</param>
    /// <returns>The index of the Choices parameter collection element that
corresponds
    /// to the option that is selected by the user.</returns>
    public override int PromptForChoice(
                                         string caption,
                                         string message,
                                         Collection<ChoiceDescription> choices,
                                         int defaultChoice)
    {
      // Write the caption and message strings in Blue.
      this.WriteLine(
                      ConsoleColor.Blue,
                      ConsoleColor.Black,
                      caption + "\n" + message + "\n");

        // Convert the choice collection into something that is easier to
        // work with. See the BuildHotkeysAndPlainLabels method for details.
        Dictionary<string, PSObject> results =
            new Dictionary<string, PSObject>();
        string[,] promptData = BuildHotkeysAndPlainLabels(choices);

        // Format the overall choice prompt string to display...
        StringBuilder sb = new StringBuilder();
        for (int element = 0; element < choices.Count; element++)
        {
          sb.Append(String.Format(
                                  CultureInfo.CurrentCulture,
                                  "|{0}> {1} ",
                                  promptData[0, element],
                                  promptData[1, element]));
        }

        sb.Append(String.Format(
