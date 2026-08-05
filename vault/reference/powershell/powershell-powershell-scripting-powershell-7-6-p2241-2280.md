---
title: "How to use this documentation — pages 2241-2280"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2241-2280
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2241-2280
family: powershell
documentKind: "doc"
abstract: "using PowerShell = System.Management.Automation.PowerShell; /// <summary> /// This class contains the Main entry point for this host application. /// </summary> internal class Runspace08 { /// <summary> /// This sample shows how to use a PowerShell object to run commands. The //"
---

# How to use this documentation — pages 2241-2280

<!-- p.2241 -->

  using PowerShell = System.Management.Automation.PowerShell;

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace08
  {
    /// <summary>
    /// This sample shows how to use a PowerShell object to run commands. The
    /// PowerShell object builds a pipeline that include the Get-Process cmdlet,
    /// which is then piped to the Sort-Object cmdlet. Parameters are added to the
    /// Sort-Object cmdlet to sort the HandleCount property in descending order.
    /// </summary>
    /// <param name="args">Parameter is not used.</param>
    /// <remarks>
    /// This sample demonstrates:
    /// 1. Creating a PowerShell object
    /// 2. Adding individual commands to the PowerShell object.
    /// 3. Adding parameters to the commands.
    /// 4. Running the pipeline of the PowerShell object synchronously.
    /// 5. Working with PSObject objects to extract properties
    ///    from the objects returned by the commands.
    /// </remarks>
    private static void Main(string[] args)
    {
      Collection<PSObject> results; // Holds the result of the pipeline execution.

      // Create the PowerShell object. Notice that no runspace is specified so a
      // new default runspace is used.
      PowerShell powershell = PowerShell.Create();

      // Use the using statement so that we can dispose of the PowerShell object
      // when we are done.
      using (powershell)
      {
        // Add the Get-Process cmdlet to the pipeline of the PowerShell object.
        powershell.AddCommand("Get-Process");

        // Add the Sort-Object cmdlet and its parameters to the pipeline of
        // the PowerShell object so that we can sort the HandleCount property
        // in descending order.
        powershell.AddCommand("Sort-
Object").AddParameter("Descending").AddParameter("Property", "HandleCount");

          // Run the commands of the pipeline synchronously.
          results = powershell.Invoke();
      }

      // Even after disposing of the PowerShell object, we still
      // need to set the powershell variable to null so that the
      // garbage collector can clean it up.
      powershell = null;

      Console.WriteLine("Process              HandleCount");
      Console.WriteLine("--------------------------------");

<!-- p.2242 -->

             // Display the results returned by the commands.
             foreach (PSObject result in results)
             {
               Console.WriteLine(
                                  "{0,-20} {1}",
                                  result.Members["ProcessName"].Value,
                                  result.Members["HandleCount"].Value);
             }

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2243 -->

Runspace09 Sample
This sample shows how to add a script to the pipeline of a
System.Management.Automation.PowerShell object and how to run the script asynchronously.
Events are used to handle the output of the script.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Creating a System.Management.Automation.PowerShell object that uses the runspace.

      Adding a script the pipeline of the System.Management.Automation.PowerShell object.

      Using the System.Management.Automation.PowerShell.BeginInvoke* method to run the
      pipeline asynchronously.

      Using the events of the System.Management.Automation.PowerShell object to process
      the output of the script.

      Using the System.Management.Automation.PowerShell.Stop* method to interrupt the
      invocation of the pipeline.

Example
This sample runs to run a script that generates the numbers from 1 to 10 with delays between
each number. The script is run asynchronously and events are used to handle the output.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.Generic;
   using System.Collections.ObjectModel;
   using System.Diagnostics;
   using System.Management.Automation;

<!-- p.2244 -->

  using System.Management.Automation.Runspaces;
  using PowerShell = System.Management.Automation.PowerShell;

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace09
  {
    /// <summary>
    /// This sample shows how to use a PowerShell object to run a
    /// script that generates the numbers from 1 to 10 with delays
    /// between each number. The pipeline of the PowerShell object
    /// is run asynchronously and events are used to handle the output.
    /// </summary>
    /// <param name="args">The parameter is not used.</param>
    /// <remarks>
    /// This sample demonstrates the following:
    /// 1. Creating a PowerShell object.
    /// 2. Adding a script to the pipeline of the PowerShell object.
    /// 3. Using the BeginInvoke method to run the pipeline asynchronously.
    /// 4. Using the events of the PowerShell object to process the
    ///    output of the script.
    /// 5. Using the PowerShell.Stop() method to interrupt the invocation of
    ///    the pipeline.
    /// </remarks>
    private static void Main(string[] args)
    {
      Console.WriteLine("Print the numbers from 1 to 10. Hit any key to halt
processing\n");

      using (PowerShell powershell = PowerShell.Create())
      {
        // Add a script to the PowerShell object. The script generates the
        // numbers from 1 to 10 in half second intervals.
        powershell.AddScript("1..10 | foreach {$_ ; Start-Sleep -Milli 500}");

        // Add the event handlers. If we did not care about hooking the DataAdded
        // event, we would let BeginInvoke create the output stream for us.
        PSDataCollection<PSObject> output = new PSDataCollection<PSObject>();
        output.DataAdded += new EventHandler<DataAddedEventArgs>(Output_DataAdded);
        powershell.InvocationStateChanged += new
EventHandler<PSInvocationStateChangedEventArgs>(Powershell_InvocationStateChanged);

        // Invoke the pipeline asynchronously.
        IAsyncResult asyncResult = powershell.BeginInvoke<PSObject, PSObject>(null,
output);

       // Wait for things to happen. If the user hits a key before the
       // script has completed, then call the PowerShell Stop() method
       // to halt processing.
       Console.ReadKey();
       if (powershell.InvocationStateInfo.State != PSInvocationState.Completed)
       {
         // Stop the invocation of the pipeline.
         Console.WriteLine("\nStopping the pipeline!\n");

<!-- p.2245 -->

                 powershell.Stop();

                 // Wait for the Windows PowerShell state change messages to be displayed.
                 System.Threading.Thread.Sleep(500);
                 Console.WriteLine("\nPress a key to exit");
                 Console.ReadKey();
             }
         }
     }

     /// <summary>
     /// The output data added event handler. This event is called when
     /// data is added to the output pipe. It reads the data that is
     /// available and displays it on the console.
     /// </summary>
     /// <param name="sender">The output pipe this event is associated with.</param>
     /// <param name="e">Parameter is not used.</param>
     private static void Output_DataAdded(object sender, DataAddedEventArgs e)
     {
       PSDataCollection<PSObject> myp = (PSDataCollection<PSObject>)sender;

         Collection<PSObject> results = myp.ReadAll();
         foreach (PSObject result in results)
         {
           Console.WriteLine(result.ToString());
         }
     }

     /// <summary>
     /// This event handler is called when the pipeline state is changed.
     /// If the state change is to Completed, the handler issues a message
     /// asking the user to exit the program.
     /// </summary>
     /// <param name="sender">This parameter is not used.</param>
     /// <param name="e">The PowerShell state information.</param>
     private static void Powershell_InvocationStateChanged(object sender,
 PSInvocationStateChangedEventArgs e)
     {
       Console.WriteLine("PowerShell object state changed: state: {0}\n",
 e.InvocationStateInfo.State);
       if (e.InvocationStateInfo.State == PSInvocationState.Completed)
       {
         Console.WriteLine("Processing completed, press a key to exit!");
       }
     }
   }
 }

See Also
Writing a Windows PowerShell Host Application

<!-- p.2246 -->

Last updated on 05/20/2025

<!-- p.2247 -->

Runspace10 Sample
This sample shows how to create a default initial session state, how to add a cmdlet to the
System.Management.Automation.Runspaces.InitialSessionState, how to create a runspace that
uses the initial session state, and how to run the command by using a
System.Management.Automation.PowerShell object.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

     Creating a System.Management.Automation.Runspaces.InitialSessionState object.

     Adding a cmdlet (defined by the Host application) to the
     System.Management.Automation.Runspaces.InitialSessionState object.

     Creating a System.Management.Automation.Runspaces.Runspace object that uses the
     object.

     Creating a System.Management.Automation.PowerShell object that uses the
     System.Management.Automation.Runspaces.Runspace object.

     Adding the command to the pipeline of the System.Management.Automation.PowerShell
     object.

     Extracting properties from the System.Management.Automation.PSObject objects
     returned by the command.

Example
This sample creates a runspace that uses a
System.Management.Automation.Runspaces.InitialSessionState object to define the elements
that are available when the runspace is opened. In this sample, the Get-Proc cmdlet (defined by
the Host application) is added to the initial session state, and the cmdlet is run synchronously
by using a System.Management.Automation.PowerShell object.

<!-- p.2248 -->

C#

namespace Microsoft.Samples.PowerShell.Runspaces
{
  using System;
  using System.Collections.Generic;
  using System.Collections.ObjectModel;
  using System.Diagnostics;
  using System.Management.Automation;
  using System.Management.Automation.Runspaces;
  using PowerShell = System.Management.Automation.PowerShell;

  #region GetProcCommand

  /// <summary>
  /// Class that implements the GetProcCommand.
  /// </summary>
  [Cmdlet(VerbsCommon.Get, "Proc")]
  public class GetProcCommand : Cmdlet
  {
    #region Cmdlet Overrides

     /// <summary>
     /// For each of the requested process names, retrieve and write
     /// the associated processes.
     /// </summary>
     protected override void ProcessRecord()
     {
       // Get the current processes.
       Process[] processes = Process.GetProcesses();

         // Write the processes to the pipeline making them available
         // to the next cmdlet. The second argument (true) tells the
         // system to enumerate the array, and send one process object
         // at a time to the pipeline.
         WriteObject(processes, true);
     }

    #endregion Overrides
  } // End GetProcCommand class.

  #endregion GetProcCommand

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace10
  {
    /// <summary>
    /// This sample shows how to create a default initial session state, how to add
    /// add a cmdlet to the InitialSessionState object, and then how to create
    /// a Runspace object.
    /// </summary>
    /// <param name="args">Parameter is not used.</param>

<!-- p.2249 -->

    /// This sample demonstrates:
    /// 1. Creating an InitialSessionState object.
    /// 2. Adding a cmdlet to the InitialSessionState object.
    /// 3. Creating a runspace that uses the InitialSessionState object.
    /// 4. Creating a PowerShell object that uses the Runspace object.
    /// 5. Running the added command synchronously.
    /// 6. Working with PSObject objects to extract properties
    ///    from the objects returned by the pipeline.
    private static void Main(string[] args)
    {
      // Create a default InitialSessionState object. The default
      // InitialSessionState object contains all the elements provided
      // by Windows PowerShell.
      InitialSessionState iss = InitialSessionState.CreateDefault();

      // Add the Get-Proc cmdlet to the InitialSessionState object.
      SessionStateCmdletEntry ssce = new SessionStateCmdletEntry("Get-Proc",
typeof(GetProcCommand), null);
      iss.Commands.Add(ssce);

      // Create a Runspace object that uses the InitialSessionState object.
      // Notice that no PSHost object is specified, so the default host is used.
      // See the Hosting samples for information on creating your own custom host.
      using (Runspace myRunSpace = RunspaceFactory.CreateRunspace(iss))
      {
        myRunSpace.Open();

          using (PowerShell powershell = PowerShell.Create())
          {
            powershell.Runspace = myRunSpace;

              // Add the Get-Proc cmdlet to the pipeline of the PowerShell object.
              powershell.AddCommand("Get-Proc");

              Collection<PSObject> results = powershell.Invoke();

              Console.WriteLine("Process              HandleCount");
              Console.WriteLine("--------------------------------");

              // Display the output of the pipeline.
              foreach (PSObject result in results)
              {
                 Console.WriteLine(
                                   "{0,-20} {1}",
                                   result.Members["ProcessName"].Value,
                                   result.Members["HandleCount"].Value);
              }
          }

          // Close the runspace to release resources.
          myRunSpace.Close();
      }

      System.Console.WriteLine("Hit any key to exit...");
      System.Console.ReadKey();

<!-- p.2250 -->

         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2251 -->

Runspace11 Sample
This sample shows how to use the System.Management.Automation.ProxyCommand class to
create a proxy command that calls an existing cmdlet, but restricts the set of available
parameters. The proxy command is then added to an initial session state that is used to create
a constrained runspace. This means that the user can access the functionality of the cmdlet
only through the proxy command.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

     Creating a System.Management.Automation.CommandMetadata object that describes
     the metadata of an existing cmdlet.

     Creating a System.Management.Automation.Runspaces.InitialSessionState object.

     Modifying the cmdlet metadata to remove a parameter of the cmdlet.

     Adding the cmdlet to the System.Management.Automation.Runspaces.InitialSessionState
     object and making the cmdlet private.

     Creating a proxy function that calls the existing cmdlet, but exposes only a restricted set
     of parameters.

     Adding the proxy function to the initial session state.

     Creating a System.Management.Automation.PowerShell object that uses the
     System.Management.Automation.Runspaces.Runspace object.

     Calling the private cmdlet and the proxy function using a
     System.Management.Automation.PowerShell object to demonstrate the constrained
     runspace.

Example

<!-- p.2252 -->

This creates a proxy command for a private cmdlet to demonstrate a constrained runspace.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Collections.Generic;
   using System.Diagnostics;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;
   using PowerShell = System.Management.Automation.PowerShell;

   #region GetProcCommand

   /// <summary>
   /// This class implements the Get-Proc cmdlet. It has been copied
   /// verbatim from the GetProcessSample02.cs sample.
   /// </summary>
   [Cmdlet(VerbsCommon.Get, "Proc")]
   public class GetProcCommand : Cmdlet
   {
     #region Parameters

      /// <summary>
      /// The names of the processes to act on.
      /// </summary>
      private string[] processNames;

      /// <summary>
      /// Gets or sets the list of process names on which
      /// the Get-Proc cmdlet will work.
      /// </summary>
      [Parameter(Position = 0)]
      [ValidateNotNullOrEmpty]
      public string[] Name
      {
        get { return this.processNames; }
        set { this.processNames = value; }
      }

      #endregion Parameters

      #region Cmdlet Overrides

      /// <summary>
      /// The ProcessRecord method calls the Process.GetProcesses
      /// method to retrieve the processes specified by the Name
      /// parameter. Then, the WriteObject method writes the
      /// associated processes to the pipeline.
      /// </summary>
      protected override void ProcessRecord()
      {
        // If no process names are passed to the cmdlet, get all

<!-- p.2253 -->

      // processes.
      if (this.processNames == null)
      {
        WriteObject(Process.GetProcesses(), true);
      }
      else
      {
        // If process names are passed to cmdlet, get and write
        // the associated processes.
        foreach (string name in this.processNames)
        {
           WriteObject(Process.GetProcessesByName(name), true);
        }
      } // if (processNames...
    } // ProcessRecord

    #endregion Cmdlet Overrides
  } // GetProcCommand

  #endregion GetProcCommand

  /// <summary>
  /// This class contains the Main entry point for this host application.
  /// </summary>
  internal class Runspace11
  {
    /// <summary>
    /// This shows how to use the ProxyCommand class to create a proxy
    /// command that calls an existing cmdlet, but restricts the set of
    /// available parameters. The proxy command is then added to an initial
    /// session state that is used to create a constrained runspace. This
    /// means that the user can access the cmdlet only through the proxy
    /// command.
    /// </summary>
    /// <remarks>
    /// This sample demonstrates the following:
    /// 1. Creating a CommandMetadata object that describes the metadata of an
    ///    existing cmdlet.
    /// 2. Modifying the cmdlet metadata to remove a parameter of the cmdlet.
    /// 3. Adding the cmdlet to an initial session state and making it private.
    /// 4. Creating a proxy function that calls the existing cmdlet, but exposes
    ///    only a restricted set of parameters.
    /// 6. Adding the proxy function to the initial session state.
    /// 7. Calling the private cmdlet and the proxy function to demonstrate the
    ///    constrained runspace.
    /// </remarks>
    private static void Main()
    {
      // Create a default initial session state. The default initial session state
      // includes all the elements that are provided by Windows PowerShell.
      InitialSessionState iss = InitialSessionState.CreateDefault();

      // Add the Get-Proc cmdlet to the initial session state.
      SessionStateCmdletEntry cmdletEntry = new SessionStateCmdletEntry("Get-Proc",
typeof(GetProcCommand), null);

<!-- p.2254 -->

      iss.Commands.Add(cmdletEntry);

      // Make the cmdlet private so that it is not accessible.
      cmdletEntry.Visibility = SessionStateEntryVisibility.Private;

      // Set the language mode of the initial session state to NoLanguage to
      //prevent users from using language features. Only the invocation of
      // public commands is allowed.
      iss.LanguageMode = PSLanguageMode.NoLanguage;

      // Create the proxy command using cmdlet metadata to expose the
      // Get-Proc cmdlet.
      CommandMetadata cmdletMetadata = new CommandMetadata(typeof(GetProcCommand));

      // Remove one of the parameters from the command metadata.
      cmdletMetadata.Parameters.Remove("Name");

      // Generate the body of a proxy function that calls the original cmdlet,
      // but does not have the removed parameter.
      string bodyOfProxyFunction = ProxyCommand.Create(cmdletMetadata);

      // Add the proxy function to the initial session state. The name of the proxy
      // function can be the same as the name of the cmdlet, but to clearly
      // demonstrate that the original cmdlet is not available a different name is
      // used for the proxy function.
      iss.Commands.Add(new SessionStateFunctionEntry("Get-ProcProxy",
bodyOfProxyFunction));

      // Create the constrained runspace using the initial session state.
      using (Runspace myRunspace = RunspaceFactory.CreateRunspace(iss))
      {
        myRunspace.Open();

       // Call the private cmdlet to demonstrate that it is not available.
       try
       {
         using (PowerShell powershell = PowerShell.Create())
         {
           powershell.Runspace = myRunspace;
           powershell.AddCommand("Get-Proc").AddParameter("Name", "*explore*");
           powershell.Invoke();
         }
       }
       catch (CommandNotFoundException e)
       {
         System.Console.WriteLine(
                       "Invoking 'Get-Proc' failed as expected: {0}: {1}",
                       e.GetType().FullName,
                       e.Message);
       }

       // Call the proxy function to demonstrate that the -Name parameter is
       // not available.
       try
       {

<!-- p.2255 -->

                   using (PowerShell powershell = PowerShell.Create())
                   {
                     powershell.Runspace = myRunspace;
                     powershell.AddCommand("Get-ProcProxy").AddParameter("Name", "idle");
                     powershell.Invoke();
                   }
         }
         catch (ParameterBindingException e)
         {
            System.Console.WriteLine(
                          "\nInvoking 'Get-ProcProxy -Name idle' failed as expected:
 {0}: {1}",
                          e.GetType().FullName,
                          e.Message);
         }

                 // Call the proxy function to demonstrate that it calls into the
                 // private cmdlet to retrieve the processes.
                 using (PowerShell powershell = PowerShell.Create())
                 {
                   powershell.Runspace = myRunspace;
                   powershell.AddCommand("Get-ProcProxy");
                   List<Process> processes = new List<Process>(powershell.Invoke<Process>
 ());
           System.Console.WriteLine(
                         "\nInvoking the Get-ProcProxy function called into the Get-
 Proc cmdlet and returned {0} processes",
                         processes.Count);
         }

                 // Close the runspace to release resources.
                 myRunspace.Close();
             }

             System.Console.WriteLine("Hit any key to exit...");
             System.Console.ReadKey();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025

<!-- p.2256 -->

Remote Runspace Samples
This section includes sample code that shows how to create runspaces that can be used to
connect to a computer by using WS-Management-based Windows PowerShell remoting. You
can use Microsoft Visual Studio to create a console application and then copy the code from
the topics in this section into your host application.

In This Section

  ７ Note

  For more information about running commands on a remote computer, see Windows
  PowerShell Remoting.

RemoteRunspace01 Sample This sample shows how to create a remote runspace that is used
to establish a remote connection.

RemoteRunspacePool01 Sample This sample shows how to construct a remote runspace pool
and how to run multiple commands concurrently by using this pool.

 Last updated on 05/20/2025

<!-- p.2257 -->

RemoteRunspace01 Sample
This sample shows how to create a remote runspace that is used to establish a remote
connection.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a System.Management.Automation.Runspaces.WSManConnectionInfo object.

      Setting the
      System.Management.Automation.Runspaces.RunspaceConnectionInfo.OperationTimeout*
      and System.Management.Automation.Runspaces.RunspaceConnectionInfo.OpenTimeout*
      properties of the System.Management.Automation.Runspaces.WSManConnectionInfo
      object.

      Creating a remote runspace that uses the
      System.Management.Automation.Runspaces.WSManConnectionInfo object to establish
      the remote connection.

      Closing the remote runspace to release the remote connection.

Example
This sample defines a remote connection and then uses that connection information to
establish a remote connection.

 C#

 namespace Microsoft.Samples.PowerShell.Runspaces
 {
   using System;
   using System.Management.Automation;                 // Windows PowerShell namespace.
   using System.Management.Automation.Runspaces;       // Windows PowerShell namespace.

   /// <summary>
   /// This class contains the Main entry point for the application.
   /// </summary>

<!-- p.2258 -->

    internal class RemoteRunspace01
    {
      /// <summary>
      /// This sample shows how to use a WSManConnectionInfo object to set
      /// various timeouts and how to establish a remote connection.
      /// </summary>
      /// <param name="args">This parameter is not used.</param>
      public static void Main(string[] args)
      {
        // Create a WSManConnectionInfo object using the default constructor
        // to connect to the "localHost". The WSManConnectionInfo object can
        // also specify connections to remote computers.
        WSManConnectionInfo connectionInfo = new WSManConnectionInfo();

      // Set the OperationTimeout property. The OperationTimeout is used to tell
      // Windows PowerShell how long to wait (in milliseconds) before timing out
      // for any operation. This includes sending input data to the remote
computer,
      // receiving output data from the remote computer, and more. The user can
      // change this timeout depending on whether the connection is to a computer
      // in the data center or across a slow WAN.
      connectionInfo.OperationTimeout = 4 * 60 * 1000; // 4 minutes.

      // Set the OpenTimeout property. OpenTimeout is used to tell Windows
PowerShell
      // how long to wait (in milliseconds) before timing out while establishing a
      // remote connection. The user can change this timeout depending on whether
the
      // connection is to a computer in the data center or across a slow WAN.
      connectionInfo.OpenTimeout = 1 * 60 * 1000; // 1 minute.

      // Create a remote runspace using the connection information.
      using (Runspace remoteRunspace =
RunspaceFactory.CreateRunspace(connectionInfo))
      {
        // Establish the connection by calling the Open() method to open the
runspace.
        // The OpenTimeout value set previously will be applied while establishing
        // the connection. Establishing a remote connection involves sending and
        // receiving some data, so the OperationTimeout will also play a role in
this process.
        remoteRunspace.Open();

                // Add the code to run commands in the remote runspace here. The
                // OperationTimeout value set previously will play a role here because
                // running commands involves sending and receiving data.

                // Close the connection. Call the Close() method to close the remote
                // runspace. The Dispose() method (called by using primitive) will call
                // the Close() method if it is not already called.
                remoteRunspace.Close();
            }
        }
    }
}

<!-- p.2259 -->

Last updated on 05/20/2025

<!-- p.2260 -->

RemoteRunspacePool01 Sample
This sample shows how to construct a remote runspace pool and how to run multiple
commands concurrently by using this pool.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
      Creating a System.Management.Automation.Runspaces.WSManConnectionInfo object.

      Setting the
      System.Management.Automation.Runspaces.RunspaceConnectionInfo.OperationTimeout*
      and System.Management.Automation.Runspaces.RunspaceConnectionInfo.OpenTimeout*
      properties of the System.Management.Automation.Runspaces.WSManConnectionInfo
      object.

      Creating a remote runspace that uses the
      System.Management.Automation.Runspaces.WSManConnectionInfo object to establish
      the remote connection.

      Running the Get-Process and Get-Service cmdlets concurrently by using the remote
      runspace pool.

      Closing the remote runspace pool to release the remote connection.

Example
This sample shows how to construct a remote runspace pool and how to run multiple
commands concurrently by using this pool.

 C#

 namespace Samples
 {
   using System;
   using System.Management.Automation;                // Windows PowerShell namespace.
   using System.Management.Automation.Runspaces;      // Windows PowerShell namespace.

<!-- p.2261 -->

  /// <summary>
  /// This class contains the Main entry point for the application.
  /// </summary>
  internal class RemoteRunspacePool01
  {
    /// <summary>
    /// This sample shows how to construct a remote RunspacePool and how to
    /// concurrently run the Get-Process and Get-Service commands using the
    /// runspaces of the pool.
    /// </summary>
    /// <param name="args">Parameter is not used.</param>
    public static void Main(string[] args)
    {
      // Create a WSManConnectionInfo object using the default constructor to
      // connect to the "localhost". The WSManConnectionInfo object can also
      // specify connections to remote computers.
      WSManConnectionInfo connectionInfo = new WSManConnectionInfo();

      // Create a remote runspace pool that uses the WSManConnectionInfo object.
      // The minimum runspaces value of 1 specifies that Windows PowerShell will
      // keep at least 1 runspace open. The maximum runspaces value of 2 specifies
      // that Windows PowerShell will allows 2 runspaces to be opened at the
      // same time so that two commands can be run concurrently.
      using (RunspacePool remoteRunspacePool =
             RunspaceFactory.CreateRunspacePool(1, 2, connectionInfo))
      {
        // Call the Open() method to open the runspace pool and establish
        // the connection.
        remoteRunspacePool.Open();

        // Call the Create() method to create a pipeline, call the
AddCommand(string)
        // method to add the "Get-Process" command, and then call the BeginInvoke()
        // method to run the command asynchronously using a runspace of the pool.
        PowerShell gpsCommand = PowerShell.Create().AddCommand("Get-Process");
        gpsCommand.RunspacePool = remoteRunspacePool;
        IAsyncResult gpsCommandAsyncResult = gpsCommand.BeginInvoke();

        // The previous call does not block the current thread because it is
        // running asynchronously. Because the remote runspace pool can open two
        // runspaces, the second command can be run.
        PowerShell getServiceCommand = PowerShell.Create().AddCommand("Get-
Service");
        getServiceCommand.RunspacePool = remoteRunspacePool;
        IAsyncResult getServiceCommandAsyncResult =
getServiceCommand.BeginInvoke();

        // When you are ready to handle the output, wait for the command to
complete
        // before extracting results. A call to the EndInvoke() method will block
and return
        // the output.
        PSDataCollection<PSObject> gpsCommandOutput =
gpsCommand.EndInvoke(gpsCommandAsyncResult);

<!-- p.2262 -->

           // Process the output from the first command.
           if ((gpsCommandOutput != null) && (gpsCommandOutput.Count > 0))
           {
             Console.WriteLine("The first output from running Get-Process command: ");
             Console.WriteLine(
                               "Process Name: {0} Process Id: {1}",
                               gpsCommandOutput[0].Properties["ProcessName"].Value,
                               gpsCommandOutput[0].Properties["Id"].Value);
             Console.WriteLine();
           }

           // Now process the output from the second command. As discussed previously,
 wait
         // for the command to complete before extracting the results.
         PSDataCollection<PSObject> getServiceCommandOutput =
 getServiceCommand.EndInvoke(
                                    getServiceCommandAsyncResult);

           // Process the output of the second command as needed.
           if ((getServiceCommandOutput != null) && (getServiceCommandOutput.Count >
 0))
           {
               Console.WriteLine("The first output from running Get-Service command: ");
               Console.WriteLine(
                                 "Service Name: {0} Description: {1} State: {2}",

 getServiceCommandOutput[0].Properties["ServiceName"].Value,

 getServiceCommandOutput[0].Properties["DisplayName"].Value,
                             getServiceCommandOutput[0].Properties["Status"].Value);
         }

           // Once done with running all the commands, close the remote runspace pool.
           // The Dispose() method (called by using primitive) will call Close(), if
 it
            // is not already called.
            remoteRunspacePool.Close();
          } // End Using.
        } // End Main.
      } // End RemoteRunspacePool01 class
 }

See Also

Last updated on 05/20/2025

<!-- p.2263 -->

Formatting File Overview
The display format for the objects that are returned by commands (cmdlets, functions, and
scripts) are defined by using formatting files ( format.ps1xml ). Several of these files are
provided by PowerShell to define the display format for those objects returned by PowerShell-
provided commands, such as the System.Diagnostics.Process object returned by the Get-
Process cmdlet. However, you can also create your own custom formatting files to overwrite

the default display formats or you can write a custom formatting file to define the display of
objects returned by your own commands.

  ） Important

  Formatting files do not determine the elements of an object that are returned to the
  pipeline. When an object is returned to the pipeline, all members of that object are
  available even if some are not displayed.

PowerShell uses the data in these formatting files to determine what is displayed and how the
displayed data is formatted. The displayed data can include the properties of an object or the
value of a script. Scripts are used if you want to display some value that is not available directly
from the properties of an object, such as adding the value of two properties of an object and
then displaying the sum as a piece of data. Formatting of the displayed data is done by
defining views for the objects that you want to display. You can define a single view for each
object, you can define a single view for multiple objects, or you can define multiple views for
the same object. There is no limit to the number of views that you can define.

Common Features of Formatting Files
Each formatting file can define the following components that can be shared across all the
views defined by the file:

     Default configuration setting, such as whether the data displayed in the rows of tables will
     be displayed on the next line if the data is longer than the width of the column. For more
     information about these settings, see Wrap Element for TableRowEntry.

     Sets of objects that can be displayed by any of the views of the formatting file. For more
     information about these sets (referred to as selection sets), see Defining Sets of Objects.

<!-- p.2264 -->

     Common controls that can be used by all the views of the formatting file. Controls give
     you finer control on how data is displayed. For more information about controls, see
     Defining Custom Controls.

Formatting Views
Formatting views can display objects in a table format, list format, wide format, and custom
format. For the most part, each formatting definition is described by a set of XML tags that
describe the view. Each view contains the name of the view, the objects that use the view, and
the elements of the view, such as the column and row information for a table view.

Table View
Lists the properties of an object or a script block value in one or more columns. Each column
represents a single property of the object or a script value. You can define a table view that
displays all the properties of an object, a subset of the properties of an object, or a
combination of properties and script values. Each row of the table represents a returned object.
Creating a table view is very similar to when you pipe an object to the Format-Table cmdlet.
For more information about this view, see Table View.

List View
Lists the properties of an object or a script value in a single column. Each row of the list
displays an optional label or the property name followed by the value of the property or script.
Creating a list view is very similar to piping an object to the Format-List cmdlet. For more
information about this view, see List View.

Wide View
Lists a single property of an object or a script value in one or more columns. There is no label
or header for this view. Creating a wide view is very similar to piping an object to the Format-
Wide cmdlet. For more information about this view, see Wide View.

Custom View
Displays a customizable view of object properties or script values that does not adhere to the
rigid structure of table views, list views, or wide views. You can define a stand-alone custom
view, or you can define a custom view that is used by another view, such as a table view or list

<!-- p.2265 -->

view. Creating a custom view is very similar to piping an object to the Format-Custom cmdlet.
For more information about this view, see Custom View.

Components of a View
The following XML examples show the basic XML components of a view. The individual XML
elements vary depending on which view you want to create, but the basic components of the
views are all the same.

To start with, each view has a Name element that specifies a user friendly name that is used to
reference the view. a ViewSelectedBy element that defines which .NET objects are displayed by
the view, and a control element that defines the view.

 XML

 <ViewDefinitions>
   <View>
     <Name>NameOfView</Name>
     <ViewSelectedBy>...</ViewSelectedBy>
     <TableControl>...</TableControl>
   </View>
   <View>
     <Name>NameOfView</Name>
     <ViewSelectedBy>...</ViewSelectedBy>
     <ListControl>...</ListControl>
   <View>
   <View>
     <Name>NameOfView</Name>
     <ViewSelectedBy>...</ViewSelectedBy>
     <WideControl>...</WideControl>
   <View>
   <View>
     <Name>NameOfView</Name>
     <ViewSelectedBy>...</ViewSelectedBy>
     <CustomControl>...</CustomControl>
   </View>
 </ViewDefinitions>

Within the control element, you can define one or more entry elements. If you use multiple
definitions, you must specify which .NET objects use each definition. Typically only one entry,
with only one definition, is needed for each control.

 XML

 <ListControl>
   <ListEntries>

<!-- p.2266 -->

     <ListEntry>
       <EntrySelectedBy>...</EntrySelectedBy>
       <ListItems>...</ListItems>
     </ListEntry>
     <ListEntry>
         <EntrySelectedBy>...</EntrySelectedBy>
       <ListItems>...</ListItems>
     </ListEntry>
     <ListEntry>
         <EntrySelectedBy>...</EntrySelectedBy>
       <ListItems>...</ListItems>
     </ListEntry>
   </ListEntries>
 </ListControl>

Within each entry element of a view, you specify the item elements that define the .NET
properties or scripts that are displayed by that view.

 XML

 <ListItems>
   <ListItem>...</ListItem>
   <ListItem>...</ListItem>
   <ListItem>...</ListItem>
 </ListItems>

As shown in the preceding examples, the formatting file can contain multiple views, a view can
contain multiple definitions, and each definition can contain multiple items.

Example of a Table View
The following example shows the XML tags used to define a table view that contains two
columns. The ViewDefinitions element is the container element for all the views defined in the
formatting file. The View element defines the specific table, list, wide, or custom view. Within
each View element, the Name element specifies the name of the view, the ViewSelectedBy
element defines the objects that use the view, and the different control elements (such as the
TableControl element shown in the following example) define the type of the view.

 XML

 <ViewDefinitions>
   <View>
     <Name>Name of View</Name>
     <ViewSelectedBy>
       <TypeName>Object to display using this view</TypeName>

<!-- p.2267 -->

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
                <PropertyName>Header for column 1</PropertyName>
              </TableColumnItem>
              <TableColumnItem>
                <PropertyName>Header for column 2</PropertyName>
              </TableColumnItem>
            </TableColumnItems>
          </TableRowEntry>
        </TableRowEntries>
      </TableControl>
    </View>
  </ViewDefinitions>

See Also
Creating a List View

Creating a Table View

Creating a Wide View

Creating Custom Controls

Writing a PowerShell Formatting and Types File

 Last updated on 05/20/2025

<!-- p.2268 -->

Formatting File Concepts
The topics in this section provide information that you might need to know when creating your
own formatting files, such as the different types of views that you can define and the special
components of those views.

In This Section
Creating a Table View Provides an example of a displayed table view and the XML elements
used to define the view.

Creating a List View Provides an example of a displayed list view and the XML elements used to
define the view.

Creating a Wide View Provides an example of a displayed wide view and the XML elements
used to define the view.

Creating Custom Controls Provides an example of a custom control.

Defining Selection Sets Provides information, an example, and describes the XML elements
used to create a selection set.

Defining Conditions for Displaying Data When defining what data is displayed by a view or a
control, you can specify a condition that must exist for the data to be displayed.

Formatting Displayed Data You can specify how the individual data points in your List, Table, or
Wide view are displayed.

PowerShell Formatting Files Lists the available formatting files provided by PowerShell.

 Last updated on 05/20/2025

<!-- p.2269 -->

Creating a Table View
A table view displays data in one or more columns. Each row in the table represents a .NET
object, and each column of the table represents a property of the object or a script value. You
can define a table view that displays all the properties of an object or a subset of the properties
of an object.

A Table View Display
The following example shows how Windows PowerShell displays the
System.ServiceProcess.ServiceController object that is returned by the Get-Service cmdlet. For
this object, Windows PowerShell has defined a table view that displays the Status property,
the Name property (this property is an alias property for the ServiceName property), and the
DisplayName property. Each row in the table represents an object returned by the cmdlet.

 Output

 Status     Name                 DisplayName
 ------     ----                 -----------
 Stopped    AJRouter             AllJoyn Router Service
 Stopped    ALG                  Application Layer Gateway Service
 Stopped    AppIDSvc             Application Identity
 Running    Appinfo              Application Information

Defining the Table View
The following XML shows the table view schema for displaying the
System.ServiceProcess.ServiceController object. You must specify each property that you want
displayed in the table view.

 XML

 <View>
   <Name>service</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <TableControl>
     <TableHeaders>
       <TableColumnHeader>
         <Width>8</Width>
       </TableColumnHeader>

<!-- p.2270 -->

       <TableColumnHeader>
         <Width>18</Width>
       </TableColumnHeader>
       <TableColumnHeader>
         <Width>38</Width>
       </TableColumnHeader>
     </TableHeaders>
     <TableRowEntries>
       <TableRowEntry>
         <TableColumnItems>
           <TableColumnItem>
            <PropertyName>Status</PropertyName>
           </TableColumnItem>
           <TableColumnItem>
             <PropertyName>Name</PropertyName>
           </TableColumnItem>
           <TableColumnItem>
             <PropertyName>DisplayName</PropertyName>
           </TableColumnItem>
         </TableColumnItems>
       </TableRowEntry>
     </TableRowEntries>
   </TableControl>
 </View>

The following XML elements are used to define a list view:

     The View element is the parent element of the table view. (This is the same parent
     element for the list, wide, and custom control views.)

     The Name element specifies the name of the view. This element is required for all views.

     The ViewSelectedBy element defines the objects that use the view. This element is
     required.

     The GroupBy element (not shown in this example) defines when a new group of objects is
     displayed. A new group is started whenever the value of a specific property or script
     changes. This element is optional.

     The Controls element (not shown in this example) defines the custom controls that are
     defined by the table view. Controls give you a way to further specify how the data is
     displayed. This element is optional. A view can define its own custom controls, or it can
     use common controls that can be used by any view in the formatting file. For more
     information about custom controls, see Creating Custom Controls.

     The HideTableHeaders element (not show in this example) specifies that the table will not
     show any labels at the top of the table. This element is optional.

<!-- p.2271 -->

     The TableControl element that defines the header and row information of the table.
     Similar to all other views, a table view can display the values of object properties or values
     generated by scripts.

Defining Column Headers
   1. The TableHeaders element and its child elements define what is displayed at the top of
     the table.

   2. The TableColumnHeader element defines what is displayed at the top of a column of the
     table. Specify these elements in the order that you want the headers displayed.

     There is no limit to the number of these element that you can use, but the number of
     TableColumnHeader elements in your table view must equal the number of
     TableRowEntry elements that you use.

   3. The Label element specifies the text that is displayed. This element is optional.

   4. The Width element specifies the width (in characters) of the column. This element is
     optional.

   5. The Alignment element specifies how the label is displayed. The label can be aligned to
     the left, to the right, or centered. This element is optional.

Defining the Table Rows
Table views can provide one or more definitions that specify what data is displayed in the rows
of the table by using the child elements of the TableRowEntries element. Notice that you can
specify multiple definitions for the rows of the table, but the headers for the rows remains the
same, regardless of what row definition is used. Typically, a table will have only one definition.

In the following example, the view provides a single definition that displays the values of
several properties of the System.Diagnostics.Process object. A table view can display the value
of a property or the value of a script (not shown in the example) in its rows.

 XML

 <TableRowEntries>
       <TableRowEntry>
         <TableColumnItems>
           <TableColumnItem>
            <PropertyName>Status</PropertyName>
           </TableColumnItem>

<!-- p.2272 -->

            <TableColumnItem>
              <PropertyName>Name</PropertyName>
            </TableColumnItem>
            <TableColumnItem>
              <PropertyName>DisplayName</PropertyName>
            </TableColumnItem>
          </TableColumnItems>
        </TableRowEntry>
      </TableRowEntries>

The following XML elements can be used to provide definitions for a row:

     The TableRowEntries element and its child elements define what is displayed in the rows
     of the table.

     The TableRowEntry element provides a definition of the row. At least one TableRowEntry is
     required; however, there is no maximum limit to the number of elements that you can
     add. In most cases, a view will have only one definition.

     The EntrySelectedBy element specifies the objects that are displayed by a specific
     definition. This element is optional and is needed only when you define multiple
     TableRowEntry elements that display different objects.

     The Wrap element specifies that text that exceeds the column width is displayed on the
     next line. By default, text that exceeds the column width is truncated.

     The TableColumnItems element defines the properties or scripts whose values are
     displayed in the row.

     The TableColumnItem element defines the property or script whose value is displayed in
     the column of the row. A TableColumnItem element is required for each column of the
     row. The first entry is displayed in first column, the second entry in the second column,
     and so on.

     The PropertyName element specifies the property whose value is displayed in the row.
     You must specify either a property or a script, but you cannot specify both.

     The ScriptBlock element specifies the script whose value is displayed in the row. You must
     specify either a script or a property, but you cannot specify both.

     The FormatString element specifies a format pattern that defines how the property or
     script value is displayed. This element is optional.

<!-- p.2273 -->

     The Alignment element specifies how the value of the property or script is displayed. The
     value can be aligned to the left, to the right, or centered. This element is optional.

Defining the Objects That Use the Table View
There are two ways to define which .NET objects use the table view. You can use the
ViewSelectedBy element to define the objects that can be displayed by all the definitions of the
view, or you can use the EntrySelectedBy element to define which objects are displayed by a
specific definition of the view. In most cases, a view has only one definition, so objects are
typically defined by the ViewSelectedBy element.

The following example shows how to define the objects that are displayed by the table view
using the ViewSelectedBy and TypeName elements. There is no limit to the number of
TypeName elements that you can specify, and their order is not significant.

 XML

 <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <TypeName>System.ServiceProcess.ServiceController</TypeName>
   </ViewSelectedBy>
   <TableControl>...</TableControl>
 </View>

The following XML elements can be used to specify the objects that are used by the table view:

     The ViewSelectedBy element defines which objects are displayed by the list view.

     The TypeName element specifies the .NET object that is displayed by the view. The fully
     qualified .NET type name is required. You must specify at least one type or selection set
     for the view, but there is no maximum number of elements that can be specified.

The following example uses the ViewSelectedBy and SelectionSetName elements. Use selection
sets where you have a related set of objects that are displayed using multiple views, such as
when you define a list view and a table view for the same objects. For more information about
how to create a selection set, see Defining Selection Sets.

 XML

 <View>
   <Name>System.ServiceProcess.ServiceController</Name>
   <ViewSelectedBy>
     <SelectionSetName>.NET Type Set</SelectionSetName>

<!-- p.2274 -->

    </ViewSelectedBy>
    <TableControl>...</TableControl>
  </View>

The following XML elements can be used to specify the objects that are used by the list view:

      The ViewSelectedBy element defines which objects are displayed by the list view.

      The SelectionSetName element specifies a set of objects that can be displayed by the
      view. You must specify at least one selection set or type for the view, but there is no
      maximum number of elements that can be specified.

The following example shows how to define the objects displayed by a specific definition of the
table view using the EntrySelectedBy element. Using this element, you can specify the .NET
type name of the object, a selection set of objects, or a selection condition that specifies when
the definition is used. For more information about how to create a selection conditions, see
Defining Conditions for Displaying Data.

  ７ Note

  When creating multiple definitions of the table view you cannot specify different column
  headers. You can specify only what is displayed in the rows of the table, such as what
  objects are displayed.

  XML

  <TableRowEntry>
    <EntrySelectedBy>
      <TypeName>.NET Type</TypeName>
    </EntrySelectedBy>
  </TableRowEntry>

The following XML elements can be used to specify the objects that are used by a specific
definition of the list view:

      The EntrySelectedBy element defines which objects are displayed by the definition.

      The TypeName element specifies the .NET object that is displayed by the definition. When
      using this element, the fully qualified .NET type name is required. You must specify at
      least one type, selection set, or selection condition for the definition, but there is no
      maximum number of elements that can be specified.

<!-- p.2275 -->

     The SelectionSetName element (not shown) specifies a set of objects that can be
     displayed by this definition. You must specify at least one type, selection set, or selection
     condition for the definition, but there is no maximum number of elements that can be
     specified.

     The SelectionCondition element (not shown) specifies a condition that must exist for this
     definition to be used. You must specify at least one type, selection set, or selection
     condition for the definition, but there is no maximum number of elements that can be
     specified. For more information about defining selection conditions, see Defining
     Conditions for Displaying Data.

Using Format Strings
Formatting strings can be added to a view to further define how the data is displayed. The
following example shows how to define a formatting string for the value of the StartTime
property.

  XML

  <TableColumnItem>
    <PropertyName>StartTime</PropertyName>
    <FormatString>{0:MMM} {0:DD} {0:HH}:{0:MM}</FormatString>
  </TableColumnItem>

The following XML elements can be used to specify a format pattern:

     The TableColumnItem element defines the property or script whose value is displayed in
     the column of the row. A TableColumnItem element is required for each column of the
     row. The first entry is displayed in first column, the second entry in the second column,
     and so on.

     The PropertyName element specifies the property whose value is displayed in the row.
     You must specify either a property or a script, but you cannot specify both.

     The FormatString element specifies a format pattern that defines how the property or
     script value is displayed.

In the following example, the ToString method is called to format the value of the script.
Scripts can call any method of an object. Therefore, if an object has a method, such as
ToString , that has formatting parameters, the script can call that method to format the output

value of the script.

<!-- p.2276 -->

 XML

 <ListItem>
   <ScriptBlock>
     [string]::Format("{0,-10} {1,-8}", $_.LastWriteTime.ToString("d"),
 $_.LastWriteTime.ToString("t"))
   </ScriptBlock>
 </ListItem>

The following XML element can be used to calling the ToString method:

     The TableColumnItem element defines the property or script whose value is displayed in
     the column of the row. A TableColumnItem element is required for each column of the
     row. The first entry is displayed in first column, the second entry in the second column,
     and so on.

     The ScriptBlock element specifies the script whose value is displayed in the row. You must
     specify either a script or a property, but you cannot specify both.

See Also
Writing a PowerShell Formatting File

Last updated on 05/20/2025

<!-- p.2277 -->

Creating a List View
A list view displays data in a single column (in sequential order). The data displayed in the list
can be the value of a .NET property or the value of a script.

A List View Display
The following output shows how Windows PowerShell displays the properties of
System.ServiceProcess.ServiceController objects that are returned by the Get-Service cmdlet. In
this example, three objects were returned, with each object separated from the preceding
object by a blank line.

 PowerShell

 Get-Service | Format-List

 Output

 Name                : AEADIFilters
 DisplayName         : Andrea ADI Filters Service
 Status              : Running
 DependentServices   : {}
 ServicesDependedOn : {}
 CanPauseAndContinue : False
 CanShutdown         : False
 CanStop             : True
 ServiceType         : Win32OwnProcess

 Name                : AeLookupSvc
 DisplayName         : Application Experience
 Status              : Running
 DependentServices   : {}
 ServicesDependedOn : {}
 CanPauseAndContinue : False
 CanShutdown         : False
 CanStop             : True
 ServiceType         : Win32ShareProcess

 Name                : AgereModemAudio
 DisplayName         : Agere Modem Call Progress Audio
 Status              : Running
 DependentServices   : {}
 ServicesDependedOn : {}
 CanPauseAndContinue : False
 CanShutdown         : False
 CanStop             : True

<!-- p.2278 -->

  ServiceType            : Win32OwnProcess
  ...

Defining the List View
The following XML shows the list view schema for displaying several properties of the
System.ServiceProcess.ServiceController object. You must specify each property that you want
displayed in the list view.

  XML

  <View>
    <Name>System.ServiceProcess.ServiceController</Name>
    <ViewSelectedBy>
      <TypeName>System.ServiceProcess.ServiceController</TypeName>
    </ViewSelectedBy>
    <ListControl>
      <ListEntries>
        <ListEntry>
          <ListItems>
            <ListItem>
              <PropertyName>Name</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>DisplayName</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>Status</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>ServiceType</PropertyName>
            </ListItem>
          </ListItems>
        </ListEntry>
      </ListEntries>
    </ListControl>
  </View>

The following XML elements are used to define a list view:

     The View element is the parent element of the list view. (This is the same parent element
     for the table, wide, and custom control views.)

     The Name element specifies the name of the view. This element is required for all views.

     The ViewSelectedBy element defines the objects that use the view. This element is
     required.

<!-- p.2279 -->

      The GroupBy element defines when a new group of objects is displayed. A new group is
      started whenever the value of a specific property or script changes. This element is
      optional.

      The Controls element defines the custom controls that are defined by the list view.
      Controls give you a way to further specify how the data is displayed. This element is
      optional. A view can define its own custom controls, or it can use common controls that
      can be used by any view in the formatting file. For more information about custom
      controls, see Creating Custom Controls.

      The ListControl element defines what is displayed in the view and how it is formatted.
      Similar to all other views, a list view can display the values of object properties or values
      generated by script.

For an example of a complete formatting file that defines a simple list view, see List View
(Basic).

Providing Definitions for Your List View
List views can provide one or more definitions by using the child elements of the ListControl
element. Typically, a view will have only one definition. In the following example, the view
provides a single definition that displays several properties of the System.Diagnostics.Process
object. A list view can display the value of a property or the value of a script (not shown in the
example).

  XML

  <ListControl>
      <ListEntries>
        <ListEntry>
          <ListItems>
            <ListItem>
              <PropertyName>Name</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>DisplayName</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>Status</PropertyName>
            </ListItem>
            <ListItem>
              <PropertyName>ServiceType</PropertyName>
            </ListItem>
          </ListItems>
        </ListEntry>

<!-- p.2280 -->

      </ListEntries>
    </ListControl>

The following XML elements can be used to provide definitions for a list view:

     The ListControl element and its child elements define what is displayed in the view.

     The ListEntries element provides the definitions of the view. In most cases, a view will
     have only one definition. This element is required.

     The ListEntry element provides a definition of the view. At least one ListEntry is required;
     however, there is no maximum limit to the number of elements that you can add. In most
     cases, a view will have only one definition.

     The EntrySelectedBy element specifies the objects that are displayed by a specific
     definition. This element is optional and is needed only when you define multiple ListEntry
     elements that display different objects.

     The ListItems element specifies the properties and scripts whose values are displayed in
     the rows of the list view.

     The ListItem element specifies a property or script whose value is displayed in a row of
     the list view. A list view must specify at least one property or script. There is no maximum
     limit to the number of rows that can be specified.

     The PropertyName element specifies the property whose value is displayed in the row.
     You must specify either a property or a script, but you cannot specify both.

     The ScriptBlock element specifies the script whose value is displayed in the row. You must
     specify either a script or a property, but you cannot specify both.

     The Label element specifies the label that is displayed to the left of the property or script
     value in the row. This element is optional. If a label is not specified, the name of the
     property or the script is displayed. For a complete example, see List View (Labels).

     The ItemSelectionCondition element specifies a condition that must exist for the row to
     be displayed. For more information about adding conditions to the list view, see Defining
     Conditions for Displaying Data. This element is optional.

     The FormatString element specifies a pattern that is used to display the value of the
     property or script. This element is optional.
