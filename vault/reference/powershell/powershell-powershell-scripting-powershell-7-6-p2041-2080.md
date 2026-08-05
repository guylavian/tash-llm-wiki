---
title: "How to use this documentation — pages 2041-2080"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2041-2080
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2041-2080
family: powershell
documentKind: "doc"
abstract: "/// </summary> public class DatabaseTableInfo { /// <summary> /// Row from the \"tables\" schema /// </summary> public DataRow Data { get { return data; } set { data = value; } } private DataRow data; /// <summary> /// The table name. /// </summary> public string Name { get { retu"
---

# How to use this documentation — pages 2041-2080

<!-- p.2041 -->

/// </summary>
public class DatabaseTableInfo
{
    /// <summary>
    /// Row from the "tables" schema
    /// </summary>
    public DataRow Data
    {
        get
        {
            return data;
        }
        set
        {
            data = value;
        }
    }
    private DataRow data;

   /// <summary>
   /// The table name.
   /// </summary>
   public string Name
   {
       get
       {
           return name;
       }
       set
       {
           name = value;
       }
   }
   private String name;

   /// <summary>
   /// The number of rows in the table.
   /// </summary>
   public int RowCount
   {
       get
       {
           return rowCount;
       }
       set
       {
           rowCount = value;
       }
   }
   private int rowCount;

   /// <summary>
   /// The column definitions for the table.
   /// </summary>
   public DataColumnCollection Columns

<!-- p.2042 -->

   {
       get
       {
             return columns;
       }
       set
       {
             columns = value;
       }
   }
   private DataColumnCollection columns;

    /// <summary>
    /// Constructor.
    /// </summary>
    /// <param name="row">The row definition.</param>
    /// <param name="name">The table name.</param>
    /// <param name="rowCount">The number of rows in the table.</param>
    /// <param name="columns">Information on the column tables.</param>
    public DatabaseTableInfo(DataRow row, string name, int rowCount,
                    DataColumnCollection columns)
    {
        Name = name;
        Data = row;
        RowCount = rowCount;
        Columns = columns;
    } // DatabaseTableInfo
} // class DatabaseTableInfo

#endregion DatabaseTableInfo

#region DatabaseRowInfo

/// <summary>
/// Contains information specific to an individual table row.
/// Analogous to the FileInfo class.
/// </summary>
public class DatabaseRowInfo
{
    /// <summary>
    /// Row data information.
    /// </summary>
    public DataRow Data
    {
        get
        {
            return data;
        }
        set
        {
            data = value;
        }
    }
    private DataRow data;

<!-- p.2043 -->

   /// <summary>
   /// The row index.
   /// </summary>
   public string RowNumber
   {
       get
       {
           return rowNumber;
       }
       set
       {
           rowNumber = value;
       }
   }
   private string rowNumber;

    /// <summary>
    /// Constructor.
    /// </summary>
    /// <param name="row">The row information.</param>
    /// <param name="name">The row index.</param>
    public DatabaseRowInfo(DataRow row, string name)
    {
        RowNumber = name;
        Data = row;
    } // DatabaseRowInfo
} // class DatabaseRowInfo

#endregion DatabaseRowInfo

#region AccessDBContentReader

/// <summary>
/// Content reader used to retrieve data from this provider.
/// </summary>
public class AccessDBContentReader : IContentReader
{
    // A provider instance is required so as to get "content"
    private AccessDBProvider provider;
    private string path;
    private long currentOffset;

   internal AccessDBContentReader(string path, AccessDBProvider provider)
   {
       this.path = path;
       this.provider = provider;
   }

   /// <summary>
   /// Read the specified number of rows from the source.
   /// </summary>
   /// <param name="readCount">The number of items to
   /// return.</param>
   /// <returns>An array of elements read.</returns>
   public IList Read(long readCount)

<!-- p.2044 -->

       {
              // Read the number of rows specified by readCount and increment
              // offset
              string tableName;
              int rowNumber;
              PathType type = provider.GetNamesFromPath(path, out tableName, out
rowNumber);

              Collection<DatabaseRowInfo> rows =
                  provider.GetRows(tableName);
              Collection<DataRow> results = new Collection<DataRow>();

              if (currentOffset < 0 || currentOffset >= rows.Count)
              {
                  return null;
              }

              int rowsRead = 0;

              while (rowsRead < readCount && currentOffset < rows.Count)
              {
                  results.Add(rows[(int)currentOffset].Data);
                  rowsRead++;
                  currentOffset++;
              }

           return results;
       } // Read

       /// <summary>
       /// Moves the content reader specified number of rows from the
       /// origin
       /// </summary>
       /// <param name="offset">Number of rows to offset</param>
       /// <param name="origin">Starting row from which to offset</param>
       public void Seek(long offset, System.IO.SeekOrigin origin)
       {
           // get the number of rows in the table which will help in
           // calculating current position
           string tableName;
           int rowNumber;

              PathType type = provider.GetNamesFromPath(path, out tableName, out
rowNumber);

            if (type == PathType.Invalid)
            {
                throw new ArgumentException("Path specified must represent a table
or a row :" + path);
            }

              if (type == PathType.Table)
              {
                  Collection<DatabaseRowInfo> rows = provider.GetRows(tableName);

<!-- p.2045 -->

                 int numRows = rows.Count;

                 if (offset > rows.Count)
                 {
                     throw new
                            ArgumentException(
                                "Offset cannot be greater than the number of rows
available"
                                             );
                 }

                 if (origin == System.IO.SeekOrigin.Begin)
                 {
                      // starting from Beginning with an index 0, the current offset
                      // has to be advanced to offset - 1
                      currentOffset = offset - 1;
                 }
                 else if (origin == System.IO.SeekOrigin.End)
                 {
                      // starting from the end which is numRows - 1, the current
                      // offset is so much less than numRows - 1
                      currentOffset = numRows - 1 - offset;
                 }
                 else
                 {
                      // calculate from the previous value of current offset
                      // advancing forward always
                      currentOffset += offset;
                 }
             } // if (type...
             else
             {
                 // for row, the offset will always be set to 0
                 currentOffset = 0;
             }

       } // Seek

       /// <summary>
       /// Closes the content reader, so all members are reset
       /// </summary>
       public void Close()
       {
           Dispose();
       } // Close

       /// <summary>
       /// Dispose any resources being used
       /// </summary>
       public void Dispose()
       {
           Seek(0, System.IO.SeekOrigin.Begin);

           GC.SuppressFinalize(this);
       } // Dispose

<!-- p.2046 -->

    } // AccessDBContentReader

    #endregion AccessDBContentReader

    #region AccessDBContentWriter

    /// <summary>
    /// Content writer used to write data in this provider.
    /// </summary>
    public class AccessDBContentWriter : IContentWriter
    {
        // A provider instance is required so as to get "content"
        private AccessDBProvider provider;
        private string path;
        private long currentOffset;

       internal AccessDBContentWriter(string path, AccessDBProvider provider)
       {
           this.path = path;
           this.provider = provider;
       }

       /// <summary>
       /// Write the specified row contents in the source
       /// </summary>
       /// <param name="content"> The contents to be written to the source.
       /// </param>
       /// <returns>An array of elements which were successfully written to
       /// the source</returns>
       ///
       public IList Write(IList content)
       {
           if (content == null)
           {
               return null;
           }

              // Get the total number of rows currently available it will
              // determine how much to overwrite and how much to append at
              // the end
              string tableName;
              int rowNumber;
              PathType type = provider.GetNamesFromPath(path, out tableName, out
rowNumber);

              if (type == PathType.Table)
              {
                  OdbcDataAdapter da = provider.GetAdapterForTable(tableName);
                  if (da == null)
                  {
                      return null;
                  }

                 DataSet ds = provider.GetDataSetForTable(da, tableName);
                 DataTable table = provider.GetDataTable(ds, tableName);

<!-- p.2047 -->

                 string[] colValues = (content[0] as string).Split(',');

                 // set the specified row
                 DataRow row = table.NewRow();

                 for (int i = 0; i < colValues.Length; i++)
                 {
                     if (!String.IsNullOrEmpty(colValues[i]))
                     {
                         row[i] = colValues[i];
                     }
                 }

                 //table.Rows.InsertAt(row, rowNumber);
                 // Update the table
                 table.Rows.Add(row);
                 da.Update(ds, tableName);

            }
            else
            {
                throw new InvalidOperationException("Operation not supported.
Content can be added only for tables");
            }

           return null;
       } // Write

       /// <summary>
       /// Moves the content reader specified number of rows from the
       /// origin
       /// </summary>
       /// <param name="offset">Number of rows to offset</param>
       /// <param name="origin">Starting row from which to offset</param>
       public void Seek(long offset, System.IO.SeekOrigin origin)
       {
           // get the number of rows in the table which will help in
           // calculating current position
           string tableName;
           int rowNumber;

              PathType type = provider.GetNamesFromPath(path, out tableName, out
rowNumber);

            if (type == PathType.Invalid)
            {
                throw new ArgumentException("Path specified should represent either
a table or a row : " + path);
            }

              Collection<DatabaseRowInfo> rows =
                     provider.GetRows(tableName);

              int numRows = rows.Count;

<!-- p.2048 -->

             if (offset > rows.Count)
             {
                 throw new
                        ArgumentException(
                            "Offset cannot be greater than the number of rows
available"
                                                );
             }

             if (origin == System.IO.SeekOrigin.Begin)
             {
                 // starting from Beginning with an index 0, the current offset
                 // has to be advanced to offset - 1
                 currentOffset = offset - 1;
             }
             else if (origin == System.IO.SeekOrigin.End)
             {
                 // starting from the end which is numRows - 1, the current
                 // offset is so much less than numRows - 1
                 currentOffset = numRows - 1 - offset;
             }
             else
             {
                 // calculate from the previous value of current offset
                 // advancing forward always
                 currentOffset += offset;
             }

       } // Seek

       /// <summary>
       /// Closes the content reader, so all members are reset
       /// </summary>
       public void Close()
       {
           Dispose();
       } // Close

       /// <summary>
       /// Dispose any resources being used
       /// </summary>
       public void Dispose()
       {
           Seek(0, System.IO.SeekOrigin.Begin);

            GC.SuppressFinalize(this);
        } // Dispose
    } // AccessDBContentWriter

    #endregion AccessDBContentWriter

    #endregion Helper Classes
} // namespace Microsoft.Samples.PowerShell.Providers

<!-- p.2049 -->

See Also
System.Management.Automation.Provider.ItemCmdletProvider

System.Management.Automation.Provider.ContainerCmdletProvider

System.Management.Automation.Provider.NavigationCmdletProvider

Designing Your Windows PowerShell Provider

Last updated on 05/20/2025

<!-- p.2050 -->

Windows PowerShell Host Quickstart
To host Windows PowerShell in your application, you use the
System.Management.Automation.PowerShell class. This class provides methods that create a
pipeline of commands and then execute those commands in a runspace. The simplest way to
create a host application is to use the default runspace. The default runspace contains all of the
core Windows PowerShell commands. If you want your application to expose only a subset of
the Windows PowerShell commands, you must create a custom runspace.

  ７ Note

  To run the following samples, you need to have the Microsoft.PowerShell.SDK NuGet
  package installed.

Using the default runspace
To start, we'll use the default runspace, and use the methods of the
System.Management.Automation.PowerShell class to add commands, parameters, statements,
and scripts to a pipeline.

AddCommand
You use the System.Management.Automation.PowerShell.AddCommand method to add
commands to the pipeline. For example, suppose you want to get the list of running processes
on the machine. The way to run this command is as follows.

   1. Create a System.Management.Automation.PowerShell object.

       C#

       PowerShell ps = PowerShell.Create();

   2. Add the command that you want to execute.

       C#

       ps.AddCommand("Get-Process");

<!-- p.2051 -->

   3. Invoke the command.

       C#

       ps.Invoke();

If you call the AddCommand method more than once before you call the
System.Management.Automation.PowerShell.Invoke method, the result of the first command is
piped to the second, and so on. If you do not want to pipe the result of a previous command
to a command, add it by calling the
System.Management.Automation.PowerShell.AddStatement instead.

AddParameter
The previous example executes a single command without any parameters. You can add
parameters to the command by using the
System.Management.Automation.PSCommand.AddParameter method. For example, the
following code gets a list of all of the processes that are named powershell running on the
machine.

 C#

 PowerShell.Create().AddCommand("Get-Process")
                    .AddParameter("Name", "powershell")
                    .Invoke();

You can add additional parameters by calling the AddParameter method repeatedly.

 C#

 PowerShell.Create().AddCommand("Get-ChildItem")
                    .AddParameter("Path", @"C:\Windows")
                    .AddParameter("Filter", "*.exe")
                    .Invoke();

You can also add a dictionary of parameter names and values by calling the
System.Management.Automation.PowerShell.AddParameters method.

 C#

 var parameters = new Dictionary<string, string>
 {
     { "Path", @"C:\Windows" },
     { "Filter", "*.exe" }

<!-- p.2052 -->

 };

 PowerShell.Create().AddCommand("Get-Process")
                    .AddParameters(parameters)
                    .Invoke()

AddStatement
You can simulate batching by using the
System.Management.Automation.PowerShell.AddStatement method, which adds an additional
statement to the end of the pipeline. The following code gets a list of running processes with
the name powershell , and then gets the list of running services.

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddCommand("Get-Process").AddParameter("Name", "powershell");
 ps.AddStatement().AddCommand("Get-Service");
 ps.Invoke();

AddScript
You can run an existing script by calling the
System.Management.Automation.PowerShell.AddScript method. The following example adds a
script to the pipeline and runs it. This example assumes there is already a script named
MyScript.ps1 in a folder named D:\PSScripts .

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddScript(@"D:\PSScripts\MyScript.ps1").Invoke();

There is also a version of the AddScript method that takes a boolean parameter named
useLocalScope . If this parameter is set to true , then the script is run in the local scope. The

following code will run the script in the local scope.

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddScript(@"D:\PSScripts\MyScript.ps1", true).Invoke();

Creating a custom runspace

<!-- p.2053 -->

While the default runspace used in the previous examples loads all of the core Windows
PowerShell commands, you can create a custom runspace that loads only a specified subset of
all commands. You might want to do this to improve performance (loading a larger number of
commands is a performance hit), or to restrict the capability of the user to perform operations.
A runspace that exposes only a limited number of commands is called a constrained runspace.
To create a constrained runspace, you use the
System.Management.Automation.Runspaces.Runspace and
System.Management.Automation.Runspaces.InitialSessionState classes.

Creating an InitialSessionState object
To create a custom runspace, you must first create a
System.Management.Automation.Runspaces.InitialSessionState object. In the following
example, we use the System.Management.Automation.Runspaces.RunspaceFactory to create a
runspace after creating a default InitialSessionState object.

 C#

 InitialSessionState iss = InitialSessionState.CreateDefault();

 Runspace rs = RunspaceFactory.CreateRunspace(iss);
 rs.Open();

 PowerShell ps = PowerShell.Create();
 ps.Runspace = rs;
 ps.AddCommand("Get-Command");
 ps.Invoke();

 rs.Close();

Constraining the runspace
In the previous example, we created a default
System.Management.Automation.Runspaces.InitialSessionState object that loads all of the
built-in core Windows PowerShell. We could also have called the
System.Management.Automation.Runspaces.InitialSessionState.CreateDefault2 method to
create an InitialSessionState object that would load only the commands in the
Microsoft.PowerShell.Core snapin. To create a more constrained runspace, you must create an
empty InitialSessionState object by calling the
System.Management.Automation.Runspaces.InitialSessionState.Create method, and then add
commands to the InitialSessionState.

<!-- p.2054 -->

Using a runspace that loads only the commands that you specify provides significantly
improved performance.

You use the methods of the
System.Management.Automation.Runspaces.SessionStateCmdletEntry class to define cmdlets
for the initial session state. The following example creates an empty initial session state, then
defines and adds the Get-Command and Import-Module commands to the initial session state.
We then create a runspace constrained by that initial session state, and execute the commands
in that runspace.

Create the initial session state.

  C#

  InitialSessionState iss = InitialSessionState.Create();

Define and add commands to the initial session state.

  C#

  SessionStateCmdletEntry getCommand = new SessionStateCmdletEntry(
      "Get-Command", typeof(Microsoft.PowerShell.Commands.GetCommandCommand), "");
  SessionStateCmdletEntry importModule = new SessionStateCmdletEntry(
      "Import-Module", typeof(Microsoft.PowerShell.Commands.ImportModuleCommand),
  "");

  iss.Commands.Add(getCommand);
  iss.Commands.Add(importModule);

Create and open the runspace.

  C#

  Runspace rs = RunspaceFactory.CreateRunspace(iss);
  rs.Open();

Execute a command and show the result.

  C#

  PowerShell ps = PowerShell.Create();
  ps.Runspace = rs;
  ps.AddCommand("Get-Command");

  Collection<CommandInfo> result = ps.Invoke<CommandInfo>();

<!-- p.2055 -->

  foreach (CommandInfo entry in result)
  {
      Console.WriteLine(entry.Name);
  }

Close the runspace.

  C#

  rs.Close();

When run, the output of this code will look as follows.

  PowerShell

  Get-Command
  Import-Module

 Last updated on 10/16/2025

<!-- p.2056 -->

Creating Runspaces
A runspace is the operating environment for the commands that are invoked by a host
application. This environment includes the commands and data that are currently present, and
any language restrictions that currently apply.

Host applications can use the default runspace that is provided by Windows PowerShell, which
includes all available core commands, or create a custom runspace that includes only a subset
of the available commands. To create a customized runspace, you create a
System.Management.Automation.Runspaces.InitialSessionState object and assign it to your
runspace.

Runspace tasks
   1. Creating an InitialSessionState

   2. Creating a constrained runspace

   3. Creating multiple runspaces

See Also

 Last updated on 05/20/2025

<!-- p.2057 -->

Creating an InitialSessionState
PowerShell commands run in a runspace. To host PowerShell in your application, you must
create a System.Management.Automation.Runspaces.Runspace object. Every runspace has a
System.Management.Automation.Runspaces.InitialSessionState object associated with it. The
InitialSessionState specifies characteristics of the runspace, such as which commands, variables,
and modules are available for that runspace.

Create a default InitialSessionState
The CreateDefault and CreateDefault2 methods of the InitialSessionState class can be used to
create an InitialSessionState object. The CreateDefault method creates an InitialSessionState
with all of the built-in commands loaded, while the CreateDefault2 method loads only the
commands required to host PowerShell (the commands from the Microsoft.PowerShell.Core
module).

If you want to further limit the commands available in your host application you need to create
a constrained runspace. For information, see Creating a constrained runspace.

The following code shows how to create an InitialSessionState, assign it to a runspace, add
commands to the pipeline in that runspace, and invoke the commands. For more information
about adding and invoking commands, see Adding and invoking commands.

 C#

 namespace SampleHost
 {
   using System;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;

    class HostP4b
    {
      static void Main(string[] args)
      {
        // Call InitialSessionState.CreateDefault() to create an empty
        // InitialSessionState object, then add the variables that will be
        // available when the runspace is opened.
        InitialSessionState iss = InitialSessionState.CreateDefault();
        SessionStateVariableEntry var1 =
          new SessionStateVariableEntry("test1",
                                        "MyVar1",
                                        "Initial session state MyVar1 test");

<!-- p.2058 -->

        iss.Variables.Add(var1);

        SessionStateVariableEntry var2 =
          new SessionStateVariableEntry("test2",
                                        "MyVar2",
                                        "Initial session state MyVar2 test");
        iss.Variables.Add(var2);

        // Call RunspaceFactory.CreateRunspace(InitialSessionState) to
        // create the runspace where the pipeline is run.
        Runspace rs = RunspaceFactory.CreateRunspace(iss);
        rs.Open();

        // Call PowerShell.Create() to create the PowerShell object, then
        // specify the runspace and pipeline commands.
        PowerShell ps = PowerShell.Create();
        ps.Runspace = rs;
        ps.AddCommand("Get-Variable");
        ps.AddArgument("test*");

        Console.WriteLine("Variable             Value");
        Console.WriteLine("--------------------------");

        // Call ps.Invoke() to run the pipeline synchronously.
        foreach (PSObject result in ps.Invoke())
        {
          Console.WriteLine("{0,-20}{1}",
              result.Members["Name"].Value,
              result.Members["Value"].Value);
        } // End foreach.

        // Close the runspace to free resources.
        rs.Close();

       } // End Main.
     } // End SampleHost.
 }

See Also
Creating a constrained runspace

Adding and invoking commands

Last updated on 05/20/2025

<!-- p.2059 -->

Creating a constrained runspace
For performance or security reasons, you might want to restrict the Windows PowerShell
commands available to your host application. To do this you create an empty
System.Management.Automation.Runspaces.InitialSessionState by calling the
System.Management.Automation.Runspaces.InitialSessionState.Create* method, and then add
only the commands you want available.

Using a runspace that loads only the commands that you specify provides significantly
improved performance.

You use the methods of the
System.Management.Automation.Runspaces.SessionStateCmdletEntry class to define cmdlets
for the initial session state.

You can also make commands private. Private commands can be used by the host application,
but not by users of the application.

Adding commands to an empty runspace
The following example demonstrates how to create an empty InitialSessionState and add
commands to it.

  C#

  namespace Microsoft.Samples.PowerShell.Runspaces
  {
    using System;
    using System.Collections.ObjectModel;
    using System.Management.Automation;
    using System.Management.Automation.Runspaces;
    using Microsoft.PowerShell.Commands;
    using PowerShell = System.Management.Automation.PowerShell;

    /// <summary>
    /// This class contains the Main entry point for the application.
    /// </summary>
    internal class Runspace10b
    {
      /// <summary>
      /// This sample shows how to create an empty initial session state,
      /// how to add commands to the session state, and then how to create a
      /// runspace that has only those two commands. A PowerShell object
      /// is used to run the Get-Command cmdlet to show that only two commands

<!-- p.2060 -->

    /// are available.
    /// </summary>
    /// <param name="args">Parameter not used.</param>
    private static void Main(string[] args)
    {
      // Create an empty InitialSessionState and then add two commands.
      InitialSessionState iss = InitialSessionState.Create();

      // Add the Get-Process and Get-Command cmdlets to the session state.
      SessionStateCmdletEntry ssce1 = new SessionStateCmdletEntry(
                                                            "Get-Process",

typeof(GetProcessCommand),
                                                                  null);
      iss.Commands.Add(ssce1);

      SessionStateCmdletEntry ssce2 = new SessionStateCmdletEntry(
                                                            "Get-Command",

typeof(GetCommandCommand),
                                                                  null);
      iss.Commands.Add(ssce2);

      // Create a runspace.
      using (Runspace myRunSpace = RunspaceFactory.CreateRunspace(iss))
      {
        myRunSpace.Open();
        using (PowerShell powershell = PowerShell.Create())
        {
          powershell.Runspace = myRunSpace;

              // Create a pipeline with the Get-Command command.
              powershell.AddCommand("Get-Command");

              Collection<PSObject> results = powershell.Invoke();

              Console.WriteLine("Verb                 Noun");
              Console.WriteLine("----------------------------");

              // Display each result object.
              foreach (PSObject result in results)
              {
                Console.WriteLine(
                                 "{0,-20} {1}",
                                 result.Members["verb"].Value,
                                 result.Members["Noun"].Value);
              }
          }

          // Close the runspace and release any resources.
          myRunSpace.Close();
      }

      System.Console.WriteLine("Hit any key to exit...");
      System.Console.ReadKey();

<!-- p.2061 -->

          }
      }
  }

Making commands private
You can also make a command private, by setting it's
System.Management.Automation.CommandInfo.Visibility property to
System.Management.Automation.SessionStateEntryVisibility Private. The host application and
other commands can call that command, but the user of the application cannot. In the
following example, the Get-ChildItem command is private.

  C#

  defaultSessionState = InitialSessionState.CreateDefault();
  commandIndex = GetIndexOfEntry(defaultSessionState.Commands, "Get-ChildItem");
  defaultSessionState.Commands[commandIndex].Visibility =
  SessionStateEntryVisibility.Private;

  this.runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
  this.runspace.Open();

See Also
Creating an InitialSessionState

 Last updated on 05/20/2025

<!-- p.2062 -->

Creating multiple runspaces
If you create a large number of runspaces, you might consider creating a runspace pool. Using
a System.Management.Automation.Runspaces.RunspacePool object, rather than creating a
large number of individual runspaces with the same characteristics, can improve performance.

Creating and using a runspace pool.
The following example shows how to create a runspace pool and how to run a command
asynchronously in a runspace of the pool.

 C#

 namespace HostRunspacePool
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;
   using System.Management.Automation.Runspaces;

   /// <summary>
   /// This class provides the Main entry point for the Host application.
   /// </summary>
   internal class HostRunspacePool
   {
     /// <summary>
     /// This sample demonstrates the following.
     /// 1. Creating and opening a runspace pool.
     /// 2. Creating a PowerShell object.
     /// 3. Adding commands and arguments to the PowerShell object.
     /// 4. Running the commands asynchronously using the runspace
     ///    of the runspace pool.
     /// </summary>
     /// <param name="args">Parameter is not used.</param>
     private static void Main(string[] args)
     {
       // Create a pool of runspaces.
       using (RunspacePool rsp = RunspaceFactory.CreateRunspacePool())
       {
         rsp.Open();

          // Create a PowerShell object to run the following command.
          // Get-Process wmi*
          PowerShell gpc = PowerShell.Create();
          // Specify the runspace to use and add commands.
          gpc.RunspacePool = rsp;
          gpc.AddCommand("Get-Process").AddArgument("wmi*");

<!-- p.2063 -->

            // Invoke the command asynchronously.
            IAsyncResult gpcAsyncResult = gpc.BeginInvoke();
            // Get the results of running the command.
            PSDataCollection<PSObject> gpcOutput = gpc.EndInvoke(gpcAsyncResult);

            // Process the output.
            Console.WriteLine("The output from running the command: Get-Process wmi*");
            for (int i= 0; i < gpcOutput.Count; i++)
            {
              Console.WriteLine(
                                "Process Name: {0} Process Id: {1}",
                                gpcOutput[i].Properties["ProcessName"].Value,
                                gpcOutput[i].Properties["Id"].Value);
            }
          } // End using.
        } // End Main entry point.
      } // End HostPs5 class.
  }

See Also
Creating an InitialSessionState

 Last updated on 05/20/2025

<!-- p.2064 -->

Adding and invoking commands
After creating a runspace, you can add Windows PowerShell commands and scripts to a
pipeline, and then invoke the pipeline synchronously or asynchronously.

Creating a pipeline
The System.Management.Automation.PowerShell class provides several methods to add
commands, parameters, and scripts to the pipeline. You can invoke the pipeline synchronously
by calling an overload of the System.Management.Automation.PowerShell.Invoke* method, or
asynchronously by calling an overload of the
System.Management.Automation.PowerShell.BeginInvoke* and then the
System.Management.Automation.PowerShell.EndInvoke* method.

AddCommand
   1. Create a System.Management.Automation.PowerShell object.

       C#

       PowerShell ps = PowerShell.Create();

   2. Add the command that you want to execute.

       C#

       ps.AddCommand("Get-Process");

   3. Invoke the command.

       C#

       ps.Invoke();

If you call the System.Management.Automation.PowerShell.AddCommand* method more than
once before you call the System.Management.Automation.PowerShell.Invoke* method, the
result of the first command is piped to the second, and so on. If you do not want to pipe the
result of a previous command to a command, add it by calling the
System.Management.Automation.PowerShell.AddStatement* instead.

<!-- p.2065 -->

AddParameter
The previous example executes a single command without any parameters. You can add
parameters to the command by using the
System.Management.Automation.PSCommand.AddParameter* method For example, the
following code gets a list of all of the processes that are named powershell running on the
machine.

 C#

 PowerShell.Create().AddCommand("Get-Process")
                    .AddParameter("Name", "powershell")
                    .Invoke();

You can add additional parameters by calling
System.Management.Automation.PSCommand.AddParameter* repeatedly.

 C#

 PowerShell.Create().AddCommand("Get-Command")
                    .AddParameter("Name", "Get-VM")
                    .AddParameter("Module", "Hyper-V")
                    .Invoke();

You can also add a dictionary of parameter names and values by calling the
System.Management.Automation.PowerShell.AddParameters* method.

 C#

 IDictionary parameters = new Dictionary<String, String>();
 parameters.Add("Name", "Get-VM");

 parameters.Add("Module", "Hyper-V");
 PowerShell.Create().AddCommand("Get-Command")
    .AddParameters(parameters)
       .Invoke()

AddStatement
You can simulate batching by using the
System.Management.Automation.PowerShell.AddStatement* method, which adds an additional
statement to the end of the pipeline The following code gets a list of running processes with
the name powershell , and then gets the list of running services.

<!-- p.2066 -->

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddCommand("Get-Process").AddParameter("Name", "powershell");
 ps.AddStatement().AddCommand("Get-Service");
 ps.Invoke();

AddScript
You can run an existing script by calling the
System.Management.Automation.PowerShell.AddScript* method. The following example adds
a script to the pipeline and runs it. This example assumes there is already a script named
MyScript.ps1 in a folder named D:\PSScripts .

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddScript(File.ReadAllText(@"D:\PSScripts\MyScript.ps1")).Invoke();

There is also a version of the System.Management.Automation.PowerShell.AddScript* method
that takes a boolean parameter named useLocalScope . If this parameter is set to true , then the
script is run in the local scope. The following code will run the script in the local scope.

 C#

 PowerShell ps = PowerShell.Create();
 ps.AddScript(File.ReadAllText(@"D:\PSScripts\MyScript.ps1"), true).Invoke();

Invoking a pipeline synchronously
After you add elements to the pipeline, you invoke it. To invoke the pipeline synchronously,
you call an overload of the System.Management.Automation.PowerShell.Invoke* method. The
following example shows how to synchronously invoke a pipeline.

 C#

 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Management.Automation;

 namespace HostPS1e
 {
   class HostPS1e

<!-- p.2067 -->

     {
         static void Main(string[] args)
         {
           // Using the PowerShell.Create and AddCommand
           // methods, create a command pipeline.
           PowerShell ps = PowerShell.Create().AddCommand ("Sort-Object");

         // Using the PowerShell.Invoke method, run the command
         // pipeline using the supplied input.
         foreach (PSObject result in ps.Invoke(new int[] { 3, 1, 6, 2, 5, 4 }))
         {
             Console.WriteLine("{0}", result);
         } // End foreach.
       } // End Main.
     } // End HostPS1e.
 }

Invoking a pipeline asynchronously
You invoke a pipeline asynchronously by calling an overload of the
System.Management.Automation.PowerShell.BeginInvoke* to create an IAsyncResult object,
and then calling the System.Management.Automation.PowerShell.EndInvoke* method.

The following example shows how to invoke a pipeline asynchronously.

 C#

 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Management.Automation;

 namespace HostPS3
 {
   class HostPS3
   {
     static void Main(string[] args)
     {
       // Use the PowerShell.Create and PowerShell.AddCommand
       // methods to create a command pipeline that includes
       // Get-Process cmdlet. Do not include spaces immediately
       // before or after the cmdlet name as that will cause
       // the command to fail.
       PowerShell ps = PowerShell.Create().AddCommand("Get-Process");

          // Create an IAsyncResult object and call the
          // BeginInvoke method to start running the
          // command pipeline asynchronously.
          IAsyncResult asyncpl = ps.BeginInvoke();

<!-- p.2068 -->

          // Using the PowerShell.Invoke method, run the command
          // pipeline using the default runspace.
          foreach (PSObject result in ps.EndInvoke(asyncpl))
          {
            Console.WriteLine("{0,-20}{1}",
                    result.Members["ProcessName"].Value,
                    result.Members["Id"].Value);
          } // End foreach.
          System.Console.WriteLine("Hit any key to exit.");
          System.Console.ReadKey();
        } // End Main.
      } // End HostPS3.
  }

See Also
Creating an InitialSessionState

Creating a constrained runspace

 Last updated on 05/20/2025

<!-- p.2069 -->

Creating remote runspaces
PowerShell commands that take a ComputerName parameter can be run on any computer
that runs PowerShell. To run commands that don't take a ComputerName parameter, you can
use WS-Management to configure a runspace that connects to a specified computer, and run
commands on that computer.

Using a WSManConnection to create a remote
runspace
To create a runspace that connects to a remote computer, you create a
System.Management.Automation.Runspaces.WSManConnectionInfo object. You specify the
target endpoint for the connection by setting the
System.Management.Automation.Runspaces.WSManConnectionInfo.ConnectionUri property of
the object. You then create a runspace by calling the
System.Management.Automation.Runspaces.RunspaceFactory.CreateRunspace method,
specifying the System.Management.Automation.Runspaces.WSManConnectionInfo object as
the connectionInfo parameter.

The following example shows how to create a runspace that connects to a remote computer. In
the example, RemoteComputerUri is used as a placeholder for the actual URI of a remote
computer.

 C#

 namespace Samples
 {
   using System;
   using System.Collections.ObjectModel;
   using System.Management.Automation;                  // PowerShell namespace.
   using System.Management.Automation.Runspaces;        // PowerShell namespace.

    /// <summary>
    /// This class contains the Main entry point for this host application.
    /// </summary>
    internal class RemoteRunspace02
    {
      /// <summary>
      /// This sample shows how to create a remote runspace that
      /// runs commands on the local computer.
      /// </summary>
      /// <param name="args">Parameter not used.</param>

<!-- p.2070 -->

    private static void Main(string[] args)
    {
      // Create a WSManConnectionInfo object using the default constructor
      // to connect to the "localHost". The WSManConnectionInfo object can
      // also be used to specify connections to remote computers.
      Uri RemoteComputerUri = new Uri("http://Server01:5985/WSMAN");
      WSManConnectionInfo connectionInfo = new
WSManConnectionInfo(RemoteComputerUri);

      // Set the OperationTimeout property and OpenTimeout properties.
      // The OperationTimeout property is used to tell PowerShell
      // how long to wait (in milliseconds) before timing out for an
      // operation. The OpenTimeout property is used to tell Windows
      // PowerShell how long to wait (in milliseconds) before timing out
      // while establishing a remote connection.
      connectionInfo.OperationTimeout = 4 * 60 * 1000; // 4 minutes.
      connectionInfo.OpenTimeout = 1 * 60 * 1000; // 1 minute.

      // Create a remote runspace using the connection information.
      //using (Runspace remoteRunspace = RunspaceFactory.CreateRunspace())
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

       // Create a PowerShell object to run commands in the remote runspace.
       using (PowerShell powershell = PowerShell.Create())
       {
         powershell.Runspace = remoteRunspace;
         powershell.AddCommand("Get-Process");
         powershell.Invoke();

           Collection<PSObject> results = powershell.Invoke();

           Console.WriteLine("Process              HandleCount");
           Console.WriteLine("--------------------------------");

           // Display the results.
           foreach (PSObject result in results)
           {
             Console.WriteLine(
                               "{0,-20} {1}",
                               result.Members["ProcessName"].Value,
                               result.Members["HandleCount"].Value);
           }
       }

       // Close the connection. Call the Close() method to close the remote
       // runspace. The Dispose() method (called by using primitive) will call

<!-- p.2071 -->

                 // the Close() method if it is not already called.
                 remoteRunspace.Close();
             }
         }
     }
 }

Last updated on 05/20/2025

<!-- p.2072 -->

Creating a custom user interface
Windows PowerShell provides abstract classes and interfaces that allow you to create a custom
interactive UI that hosts the Windows PowerShell engine. To create a custom UI, you must
implement the System.Management.Automation.Host.PSHost class. Optionally, you can also
implement the System.Management.Automation.Host.PSHostRawUserInterface and
System.Management.Automation.Host.PSHostUserInterface classes, and the
System.Management.Automation.Host.IHostSupportsInteractiveSession and
System.Management.Automation.Host.IHostUISupportsMultipleChoiceSelection interfaces.

Last updated on 05/20/2025

<!-- p.2073 -->

Host Application Samples
This section includes sample code that is provided in the Windows PowerShell 2.0 SDK.

In This Section
PowerShell API Samples This section includes sample code that shows how to create runspaces
that restrict functionality, and how to asynchronously run commands using a runspace pool to
supply the runspaces.

Custom Host Samples Includes sample code for writing a custom host. The host is the
component of Windows PowerShell that provides communications between the user and the
Windows PowerShell engine. For more information about custom hosts, see Custom Host.

Runspace Samples Includes sample code for creating runspaces. For more information about
how runspaces are used, see Host Application Runspaces.

Remote Runspace Samples This section includes sample code that shows how to create
runspaces that can be used to connect to a computer by using WS-Management-based
Windows PowerShell remoting.

See Also

Last updated on 05/20/2025

<!-- p.2074 -->

Windows PowerShell API Samples
This section includes sample code that shows how to create runspaces that restrict
functionality, and how to asynchronously run commands by using a runspace pool to supply
the runspaces. You can use Microsoft Visual Studio to create a console application and then
copy the code from the topics in this section into your host application.

In This Section
PowerShell01 Sample This sample shows how to use a
System.Management.Automation.Runspaces.InitialSessionState object to limit the functionality
of a runspace. The output of this sample demonstrates how to restrict the language mode of
the runspace, how to mark a cmdlet as private, how to add and remove cmdlets and providers,
how to add a proxy command, and more.

PowerShell02 Sample This sample shows how to run commands asynchronously by using the
runspaces of a runspace pool. The sample generates a list of commands, and then runs those
commands while the Windows PowerShell engine opens a runspace from the pool when it is
needed.

 Last updated on 05/20/2025

<!-- p.2075 -->

Windows PowerShell01 Sample
This sample shows how to use a
System.Management.Automation.Runspaces.InitialSessionState object to limit the functionality
of a runspace. The output of this sample demonstrates how to restrict the language mode of
the runspace, how to mark a cmdlet as private, how to add and remove cmdlets and providers,
how to add a proxy command, and more. This sample concentrates on how to restrict the
runspace programmatically. Scripting alternatives to restricting the runspace include the
$ExecutionContext.SessionState.LanguageMode and PSSessionConfiguration commands.

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following:

     Restricting the language by setting the
     System.Management.Automation.Runspaces.InitialSessionState.LanguageMode property.

     Adding aliases to the initial session state by using a
     System.Management.Automation.Runspaces.SessionStateAliasEntry object.

     Marking commands as private.

     Removing providers from the initial session state by using the
     System.Management.Automation.Runspaces.InitialSessionState.Providers property.

     Removing commands from the initial session state by using the
     System.Management.Automation.Runspaces.InitialSessionState.Commands property.

     Adding commands and providers to the
     System.Management.Automation.Runspaces.InitialSessionState object.

Example
This sample shows several ways to limit the functionality of a runspace.

<!-- p.2076 -->

C#

namespace Sample
{
  using System;
  using System.Collections.ObjectModel;
  using System.Management.Automation;
  using System.Management.Automation.Runspaces;

  /// <summary>
  /// This class contains the Main entry point for the application.
  /// </summary>
  internal class PowerShell01
  {
    /// <summary>
    /// The runspace used to run commands.
    /// </summary>
    private Runspace runspace;

    /// <summary>
    /// Return the first index of the entry in <paramref name="entries"/>
    /// with the name <paramref name="name"/>. Return -1 if it is not found.
    /// </summary>
    /// <typeparam name="T">Type of ConstrainedSessionStateEntry</typeparam>
    /// <param name="entries">Collection of entries to search for <paramref
name="name"/> in.</param>
    /// <param name="name">Named of the entry we are looking for</param>
    /// <returns>
    /// The first index of the entry in <paramref name="entries"/> with the
    /// name <paramref name="name"/>, or return -1 if it is not found.
    /// </returns>
    private static int GetIndexOfEntry<T>(
            InitialSessionStateEntryCollection<T> entries,
            string name) where T : ConstrainedSessionStateEntry
    {
      int foundIndex = 0;
      foreach (T entry in entries)
      {
        if (entry.Name.Equals(name, StringComparison.OrdinalIgnoreCase))
        {
          return foundIndex;
        }

             foundIndex++;
         }

         return -1;
     }

     /// <summary>
     /// Run commands to demonstrate the ways to constrain the runspace.
     /// </summary>
     /// <param name="args">This parameter is unused.</param>
     private static void Main(string[] args)
     {

<!-- p.2077 -->

        new PowerShell01().RunCommands();
    }

    /// <summary>
    /// Run a script to display the results and errors.
    /// </summary>
    /// <param name="script">Script to be run.</param>
    /// <param name="scriptComment">Comment to be printed about
    /// the script.</param>
    private void RunScript(string script, string scriptComment)
    {
      Console.WriteLine("Running '{0}'\n{1}.\n\nPowerShell Output:", script,
scriptComment);

        // Using a PowerShell object, create a pipeline, add the script to the
        // pipeline, and specify the runspace where the pipeline is invoked.
        PowerShell powerShellCommand = PowerShell.Create();
        powerShellCommand.AddScript(script);
        powerShellCommand.Runspace = this.runspace;

        try
        {
          Collection<PSObject> results = powerShellCommand.Invoke();

         // Display the results.
         foreach (PSObject result in results)
         {
           Console.WriteLine(result);
         }

         // Display any non-terminating errors.
         foreach (ErrorRecord error in powerShellCommand.Streams.Error)
         {
           Console.WriteLine("PowerShell Error: {0}", error);
         }
        }
        catch (RuntimeException ex)
        {
          Console.WriteLine("PowerShell Error: {0}", ex.Message);
          Console.WriteLine();
        }

        Console.WriteLine("\n-----------------------------\n");
    }

    /// <summary>
    /// Run some commands to demonstrate the script capabilities.
    /// </summary>
    private void RunCommands()
    {
      this.runspace =
RunspaceFactory.CreateRunspace(InitialSessionState.CreateDefault());
      this.runspace.Open();
      this.RunScript("$a=0;$a", "Assigning to a variable will work for a default
InitialSessionState");

<!-- p.2078 -->

      this.runspace.Close();

      this.runspace =
RunspaceFactory.CreateRunspace(InitialSessionState.CreateDefault());
      this.runspace.InitialSessionState.LanguageMode =
PSLanguageMode.RestrictedLanguage;
      this.runspace.Open();
      this.RunScript("$a=0;$a", "Assigning to a variable will not work in
RestrictedLanguage LanguageMode");
      this.runspace.Close();

      this.runspace =
RunspaceFactory.CreateRunspace(InitialSessionState.CreateDefault());
      this.runspace.InitialSessionState.LanguageMode = PSLanguageMode.NoLanguage;
      this.runspace.Open();
      this.RunScript("10/2", "A script will not work in NoLanguage LanguageMode.");
      this.runspace.Close();

      this.runspace =
RunspaceFactory.CreateRunspace(InitialSessionState.CreateDefault());
      this.runspace.Open();
      string scriptComment = "Get-ChildItem with a default InitialSessionState will
work since the standard \n" +
           "PowerShell cmdlets are included in the default InitialSessionState";
      this.RunScript("Get-ChildItem", scriptComment);
      this.runspace.Close();

      InitialSessionState defaultSessionState =
InitialSessionState.CreateDefault();
      defaultSessionState.Commands.Add(new SessionStateAliasEntry("dir2", "Get-
ChildItem"));
      this.runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
      this.runspace.Open();
      this.RunScript("dir2", "An alias, like dir2, can be added to
InitialSessionState");
      this.runspace.Close();

      defaultSessionState = InitialSessionState.CreateDefault();
      int commandIndex = GetIndexOfEntry(defaultSessionState.Commands, "Get-
ChildItem");
      defaultSessionState.Commands.RemoveItem(commandIndex);
      this.runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
      this.runspace.Open();
      scriptComment = "Get-ChildItem was removed from the list of commands so
it\nwill no longer be found";
      this.RunScript("Get-ChildItem", scriptComment);
      this.runspace.Close();

      defaultSessionState = InitialSessionState.CreateDefault();
      defaultSessionState.Providers.Clear();
      this.runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
      this.runspace.Open();
      this.RunScript("Get-ChildItem", "There are no providers so Get-ChildItem will
not work");
      this.runspace.Close();

<!-- p.2079 -->

      // Marks a command as private, and then defines a proxy command
      // that uses the private command. One reason to define a proxy for
      // a command is to remove a parameter of the original command.
      // For a more complete sample of a proxy command, see the Runspace11
      // sample.
      defaultSessionState = InitialSessionState.CreateDefault();
      commandIndex = GetIndexOfEntry(defaultSessionState.Commands, "Get-
ChildItem");
      defaultSessionState.Commands[commandIndex].Visibility =
SessionStateEntryVisibility.Private;
      CommandMetadata getChildItemMetadata = new CommandMetadata(
           typeof(Microsoft.PowerShell.Commands.GetChildItemCommand));
      getChildItemMetadata.Parameters.Remove("Recurse");
      string getChildItemBody = ProxyCommand.Create(getChildItemMetadata);
      defaultSessionState.Commands.Add(new SessionStateFunctionEntry("Get-
ChildItem2", getChildItemBody));
      this.runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
      this.runspace.Open();
      this.RunScript("Get-ChildItem", "Get-ChildItem is private so it will not be
available");
      scriptComment = "Get-ChildItem2 is a proxy to Get-ChildItem. \n" +
                    "It works even when Get-ChildItem is private.";
      this.RunScript("Get-ChildItem2", scriptComment);
      scriptComment = "This will fail. Unlike Get-ChildItem, Get-ChildItem2 does
not have -Recurse";
      this.RunScript("Get-ChildItem2 -Recurse", scriptComment);

      InitialSessionState cleanSessionState = InitialSessionState.Create();
      this.runspace = RunspaceFactory.CreateRunspace(cleanSessionState);
      this.runspace.Open();
      scriptComment = "A script will not work because \n" +
                   "InitialSessionState.Create() will have the default LanguageMode
of NoLanguage";
      this.RunScript("10/2", scriptComment);
      this.runspace.Close();

      cleanSessionState = InitialSessionState.Create();
      cleanSessionState.LanguageMode = PSLanguageMode.FullLanguage;
      this.runspace = RunspaceFactory.CreateRunspace(cleanSessionState);
      this.runspace.Open();
      scriptComment = "Get-ChildItem, standard cmdlets and providers are not
present \n" +
                   "in an InitialSessionState returned from
InitialSessionState.Create()";
      this.RunScript("Get-ChildItem", scriptComment);
      this.runspace.Close();

      cleanSessionState = InitialSessionState.Create();
      cleanSessionState.Commands.Add(
                new SessionStateCmdletEntry(
                    "Get-ChildItem",
                    typeof(Microsoft.PowerShell.Commands.GetChildItemCommand),
                    null));
      cleanSessionState.Providers.Add(

<!-- p.2080 -->

                 new SessionStateProviderEntry(
                     "FileSystem",
                     typeof(Microsoft.PowerShell.Commands.FileSystemProvider),
                     null));
       cleanSessionState.LanguageMode = PSLanguageMode.FullLanguage;
       this.runspace = RunspaceFactory.CreateRunspace(cleanSessionState);
       this.runspace.Open();
       scriptComment = "Get-ChildItem and the FileSystem provider were explicitly
 added\n" +
                 "so Get-ChildItem will work";
       this.RunScript("Get-ChildItem", scriptComment);
       this.runspace.Close();

             Console.Write("Done...");
             Console.ReadLine();
         }
     }
 }

See Also
Writing a Windows PowerShell Host Application

Last updated on 05/20/2025
