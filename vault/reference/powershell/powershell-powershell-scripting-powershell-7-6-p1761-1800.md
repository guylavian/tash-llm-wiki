---
title: "How to use this documentation — pages 1761-1800"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1761-1800
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1761-1800
family: powershell
documentKind: "doc"
abstract: "Last updated on 05/20/2025 StopProcessSample01 Sample This sample shows how to write a cmdlet that requests feedback from the user before it attempts to stop a process, and how to implement a PassThru parameter indicating that the user wants the cmdlet to return an object. This"
---

# How to use this documentation — pages 1761-1800

<!-- p.1761 -->

Last updated on 05/20/2025

<!-- p.1762 -->

StopProcessSample01 Sample
This sample shows how to write a cmdlet that requests feedback from the user before it
attempts to stop a process, and how to implement a PassThru parameter indicating that the
user wants the cmdlet to return an object. This cmdlet is similar to the Stop-Process cmdlet
provided by Windows PowerShell 2.0.

How to build the sample by using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the StopProcessSample01
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\StopProcessSample01 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
     Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\StopProcessSample01

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module stopprossessample01

   5. Run the following command to run the cmdlet:

     Stop-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1763 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class by using the Cmdlet attribute.

      Declaring a cmdlet parameters by using the Parameter attribute.

      Calling the ShouldProcess method to request confirmation.

      Implementing a PassThru parameter that indicates if the user wants the cmdlet to return
      an object. By default, this cmdlet does not return an object to the pipeline.

Example
This sample shows how to implement a PassThru parameter that indicates that the user wants
the cmdlet to return an object, and how to request user feedback by calls to the ShouldProcess
and ShouldContinue methods.

 C#

 using System;
 using System.Diagnostics;
 using System.Collections;
 using Win32Exception = System.ComponentModel.Win32Exception;
 using System.Management.Automation;    // Windows PowerShell namespace
 using System.Globalization;

 namespace Microsoft.Samples.PowerShell.Commands
 {
    #region StopProcCommand

        /// <summary>
      /// This class implements the Stop-Proc cmdlet.
      /// </summary>
      [Cmdlet(VerbsLifecycle.Stop, "Proc",
           SupportsShouldProcess = true)]
      public class StopProcCommand : Cmdlet
      {
           #region Parameters

         /// <summary>
         /// This parameter provides the list of process names on
         /// which the Stop-Proc cmdlet will work.
         /// </summary>
          [Parameter(
             Position = 0,
             Mandatory = true,

<!-- p.1764 -->

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
/// This parameter overrides the ShouldContinue call to force
/// the cmdlet to stop its operation. This parameter should always
/// be used with caution.
/// </summary>
[Parameter]
public SwitchParameter Force
{
    get { return force; }
    set { force = value; }
}
private bool force;

/// <summary>
/// This parameter indicates that the cmdlet should return
/// an object to the pipeline after the processing has been
/// completed.
/// </summary>
[Parameter]
public SwitchParameter PassThru
{
    get { return passThru; }
    set { passThru = value; }
}
private bool passThru;

#endregion Parameters

#region Cmdlet Overrides

/// <summary>
/// The ProcessRecord method does the following for each of the
/// requested process names:
/// 1) Check that the process is not a critical process.
/// 2) Attempt to stop that process.
/// If no process is requested then nothing occurs.
/// </summary>
protected override void ProcessRecord()
{
    foreach (string name in processNames)
    {
        // For every process name passed to the cmdlet, get the associated
        // processes.
        // Write a non-terminating error for failure to retrieve
        // a process.

<!-- p.1765 -->

               Process[] processes;

               try
               {
                     processes = Process.GetProcessesByName(name);
               }
               catch (InvalidOperationException ioe)
               {
                   WriteError(new ErrorRecord(ioe,"UnableToAccessProcessByName",
                       ErrorCategory.InvalidOperation, name));

                     continue;
               }

               // Try to stop the processes that have been retrieved.
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

                   // Confirm the operation with the user first.
                   // This is always false if the WhatIf parameter is set.
                   if (!ShouldProcess(string.Format(CultureInfo.CurrentCulture,"{0}
({1})", processName,
                               process.Id)))
                   {
                       continue;
                   }

                     // Make sure that the user really wants to stop a critical
                     // process that could possibly stop the computer.
                     bool criticalProcess =

criticalProcessNames.Contains(processName.ToLower(CultureInfo.CurrentCulture));

                   if (criticalProcess &&!force)
                   {
                       string message = String.Format
                           (CultureInfo.CurrentCulture,
                                "The process \"{0}\" is a critical process and
should not be stopped. Are you sure you wish to stop the process?",
                                    processName);

                           // It is possible that the ProcessRecord method is called
                           // multiple times when objects are received as inputs from

<!-- p.1766 -->

                       // the pipeline. So to retain YesToAll and NoToAll input
that
                       // the user may enter across multiple calls to this
function,
                      // they are stored as private members of the cmdlet.
                      if (!ShouldContinue(message, "Warning!",
                                              ref yesToAll, ref noToAll))
                      {
                          continue;
                      }
                  } // if (criticalProcess...

                  // Stop the named process.
                  try
                  {
                      process.Kill();
                  }
                  catch (Exception e)
                  {
                      if ((e is Win32Exception) || (e is SystemException) ||
                         (e is InvalidOperationException))
                      {
                          // This process could not be stopped so write
                          // a non-terminating error.
                          WriteError(new ErrorRecord(e, "CouldNotStopProcess",
                                          ErrorCategory.CloseError, process));
                          continue;
                      } // if ((e is...
                      else throw;
                  } // catch

                   // If the PassThru parameter is
                   // specified, return the terminated process.
                   if (passThru)
                   {
                       WriteObject(process);
                   }
               } // foreach (Process...
           } // foreach (string...
       } // ProcessRecord

       #endregion Cmdlet Overrides

       #region Private Data

       private bool yesToAll, noToAll;

       /// <summary>
       /// Partial list of critical processes that should not be
       /// stopped. Lower case is used for case insensitive matching.
       /// </summary>
       private ArrayList criticalProcessNames = new ArrayList(
          new string[] { "system", "winlogon", "spoolsv" }
       );

<!-- p.1767 -->

          #endregion Private Data

     } // StopProcCommand

     #endregion StopProcCommand
 }

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1768 -->

StopProcessSample02 Sample
This sample shows how to write a cmdlet that writes debug (WriteDebug), verbose
(WriteVerbose), and warning (WriteWarning) messages while stopping processes on the local
computer. This cmdlet is similar to the Stop-Process cmdlet provided by Windows PowerShell
2.0.

How to build the sample by using Visual Studio
   1. Open Windows Internet Explorer and navigate to the StopProcessSample02 directory
       under the Samples directory.

       With the Windows PowerShell 2.0 SDK installed, navigate to the StopProcessSample02
       folder. The default location is C:\Program Files (x86)\Microsoft
       SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\StopProcessSample02 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
       Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
       \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

       [user]\Documents\WindowsPowerShell\Modules\StopProcessSample02

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

       Import-Module stopprossessample02

   5. Run the following command to run the cmdlet:

       Stop-Proc

<!-- p.1769 -->

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class by using the Cmdlet attribute.

      Declaring a cmdlet parameters by using the Parameter attribute.

      Writing verbose messages. For more information about the method used to write verbose
      messages, see System.Management.Automation.Cmdlet.WriteVerbose.

      Writing error messages. For more information about the method used to write error
      messages, see System.Management.Automation.Cmdlet.WriteError.

      Writing warning messages. For more information about the method used to write
      warning messages, see System.Management.Automation.Cmdlet.WriteWarning.

Example
This sample shows how to write debug, verbose, and warning messages by using the
WriteDebug , WriteVerbose , and WriteWarning methods.

 C#

 using System;
 using System.Diagnostics;
 using System.Collections;
 using Win32Exception = System.ComponentModel.Win32Exception;
 using System.Management.Automation;             //Windows PowerShell namespace
 using System.Globalization;

 namespace Microsoft.Samples.PowerShell.Commands
 {
    #region StopProcCommand

        /// <summary>
      /// This class implements the Stop-Proc cmdlet.
      /// </summary>
      [Cmdlet(VerbsLifecycle.Stop, "Proc",
           SupportsShouldProcess = true)]
      public class StopProcCommand : Cmdlet
      {

<!-- p.1770 -->

 #region Parameters

/// <summary>
/// This parameter provides the list of process names on
/// which the Stop-Proc cmdlet will work.
/// </summary>
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
 /// This parameter overrides the ShouldContinue call to force
 /// the cmdlet to stop its operation. This parameter should always
 /// be used with caution.
 /// </summary>
 [Parameter]
 public SwitchParameter Force
 {
     get { return force; }
     set { force = value; }
 }
 private bool force;

 /// <summary>
 /// This parameter indicates that the cmdlet should return
 /// an object to the pipeline after the processing has been
 /// completed.
 /// </summary>
 [Parameter]
 public SwitchParameter PassThru
 {
     get { return passThru; }
     set { passThru = value; }
 }
 private bool passThru;

 #endregion Parameters

 #region Cmdlet Overrides

 /// <summary>
 /// The ProcessRecord method does the following for each of the
 /// requested process names:
 /// 1) Check that the process is not a critical process.
 /// 2) Attempt to stop that process.
 /// If no process is requested then nothing occurs.

<!-- p.1771 -->

/// </summary>
protected override void ProcessRecord()
{
    foreach (string name in processNames)
    {
        string message = null;

       // For every process name passed to the cmdlet, get the associated
       // processes.
       // Write a non-terminating error for failure to retrieve
       // a process.

       // Write a user-friendly verbose message to the pipeline. These
       // messages are intended to give the user detailed information
       // on the operations performed by the cmdlet. These messages will
       // appear with the -Verbose option.
       message = String.Format(CultureInfo.CurrentCulture,
                      "Attempting to stop process \"{0}\".", name);
       WriteVerbose(message);

       Process[] processes;

       try
       {
             processes = Process.GetProcessesByName(name);
       }
       catch (InvalidOperationException ioe)
       {
           WriteError(new ErrorRecord(ioe,
                             "UnableToAccessProcessByName",
                                 ErrorCategory.InvalidOperation,
                                     name));
           continue;
       }

       // Try to stop the processes that have been retrieved.
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
                                   ErrorCategory.ObjectNotFound, process));
                 continue;
             }

             // Write a debug message to the host that can be used when
             // troubleshooting a problem. All debug messages will appear
             // with the -Debug option.
             message = String.Format(CultureInfo.CurrentCulture,

<!-- p.1772 -->

                                 "Acquired name for pid {0} : \"{1}\"",
                                        process.Id, processName);
                   WriteDebug(message);

                   // Confirm the operation first.
                   // This is always false if the WhatIf parameter is specified.
                   if (!ShouldProcess(string.Format(CultureInfo.CurrentCulture,
                                        "{0} ({1})",
                                            processName, process.Id)))
                   {
                       continue;
                   }

                   // Make sure that the user really wants to stop a critical
                   // process that can possibly stop the computer.
                   bool criticalProcess =
criticalProcessNames.Contains(processName.ToLower(CultureInfo.CurrentCulture));

                   if (criticalProcess && !force)
                   {
                       message = String.Format(CultureInfo.CurrentCulture,
                                    "The process \"{0}\" is a critical process and
should not be stopped. Are you sure you wish to stop the process?",
                                        processName);

                       // It is possible that the ProcessRecord method is called
                       // multiple times when objects are received as inputs from
                       // the pipeline. So to retain YesToAll and NoToAll input
that
                       // the user may enter across multiple calls to this
function,
                       // they are stored as private members of the cmdlet.
                       if (!ShouldContinue(message, "Warning!",
                                     ref yesToAll, ref noToAll))
                       {
                           continue;
                       }
                   } // if (criticalProcess...

                   // Display a warning message if the cmdlet is stopping a
                   // critical process.
                   if (criticalProcess)
                   {
                       message = String.Format(CultureInfo.CurrentCulture,
                                     "Stopping the critical process \"{0}\".",
                                          processName);
                       WriteWarning(message);
                   } // if (criticalProcess...

                   // Stop the named process.
                   try
                   {
                       process.Kill();
                   }
                   catch (Exception e)

<!-- p.1773 -->

               {
                   if ((e is Win32Exception) || (e is SystemException) ||
                       (e is InvalidOperationException))
                   {
                       // This process could not be stopped so write
                       // a non-terminating error.
                       WriteError(new ErrorRecord(
                                        e,
                                        "CouldNotStopProcess",
                                        ErrorCategory.CloseError,
                                        process)
                                  );
                       continue;
                   } // if ((e is...
                       else throw;
               } // catch

               message = String.Format(CultureInfo.CurrentCulture,
                              "Stopped process \"{0}\", pid {1}.",
                                    processName, process.Id);

               WriteVerbose(message);

               // If the PassThru parameter is specified,
               // return the terminated process object to the pipeline.
               if (passThru)
               {
                   message = String.Format(CultureInfo.CurrentCulture,
                                 "Writing process \"{0}\" to pipeline",
                                      processName);
                   WriteDebug(message);
                   WriteObject(process);
               } // if (passThru...
           } // foreach (Process...
        } // foreach (string...
    } // ProcessRecord

    #endregion Cmdlet Overrides

    #region Private Data

    private bool yesToAll, noToAll;

    /// <summary>
    /// Partial list of critical processes that should not be
    /// stopped. Lower case is used for case insensitive matching.
    /// </summary>
    private ArrayList criticalProcessNames = new ArrayList(
       new string[] { "system", "winlogon", "spoolsv" }
    );

    #endregion Private Data

} // StopProcCommand

<!-- p.1774 -->

     #endregion StopProcCommand
 }

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1775 -->

StopProcessSample03 Sample
This sample shows how to write a cmdlet whose parameters have aliases and whose
parameters support wildcard characters. This cmdlet is similar to the Stop-Process cmdlet
provided by Windows PowerShell 2.0.

How to build the sample by using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the StopProcessSample03
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\StopProcessSample03 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
     Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\StopProcessSample03

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module stopprossessample03

   5. Run the following command to run the cmdlet:

     Stop-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1776 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class by using the Cmdlet attribute.

      Declaring a cmdlet parameters by using the Parameter attribute.

      Adding aliases to parameter declarations..

      Adding wildcard support to parameters.

Example
This sample shows how to declare parameter aliases and support wildcards.

 C#

 using System;
 using System.Diagnostics;
 using System.Collections;
 using Win32Exception = System.ComponentModel.Win32Exception;
 using System.Management.Automation;             //Windows PowerShell namespace
 using System.Globalization;

 namespace Microsoft.Samples.PowerShell.Commands
 {

      #region StopProcCommand

        /// <summary>
      /// This class implements the Stop-Proc cmdlet.
      /// </summary>
      [Cmdlet(VerbsLifecycle.Stop, "Proc",
           SupportsShouldProcess = true)]
      public class StopProcCommand : Cmdlet
      {
           #region Parameters

       /// <summary>
       /// This parameter provides the list of process names on
       /// which the Stop-Proc cmdlet will work.
       /// </summary>
        [Parameter(
           Position = 0,
           Mandatory = true,
           ValueFromPipeline = true,
           ValueFromPipelineByPropertyName = true,
           HelpMessage = "The name of one or more processes to stop. Wildcards are
 permitted."

<!-- p.1777 -->

       )]
       [Alias("ProcessName")]
       public string[] Name
       {
           get { return processNames; }
           set { processNames = value; }
       }
       private string[] processNames;

       /// <summary>
       /// This parameter overrides the ShouldContinue call to force
       /// the cmdlet to stop its operation. This parameter should always
       /// be used with caution.
       /// </summary>
       [Parameter]
       public SwitchParameter Force
       {
          get { return force; }
          set { force = value; }
       }
       private bool force;

       /// <summary>
       /// This parameter indicates that the cmdlet should return
       /// an object to the pipeline after the processing has been
       /// completed.
       /// </summary>
       [Parameter(
          ValueFromPipelineByPropertyName = true,
          HelpMessage = "If set, the process(es) will be passed to the pipeline
after stopped."
       )]
       public SwitchParameter PassThru
       {
          get { return passThru; }
          set { passThru = value; }
       }
       private bool passThru;

       #endregion Parameters

       #region Cmdlet Overrides
       /// <summary>
       /// The ProcessRecord method does the following for each of the
       /// requested process names:
       /// 1) Check that the process is not a critical process.
       /// 2) Attempt to stop that process.
       /// If no process is requested then nothing occurs.
       /// </summary>
       protected override void ProcessRecord()
       {
           Process[] processes = null;

          try
          {

<!-- p.1778 -->

    processes = Process.GetProcesses();
}
catch (InvalidOperationException ioe)
{
    base.ThrowTerminatingError(new ErrorRecord(ioe,
              "UnableToAccessProcessList",
                  ErrorCategory.InvalidOperation,
                      null));
}

// For every process name passed to the cmdlet, get the associated
// processes.
// Write a non-terminating error for failure to retrieve
// a process.
foreach (string name in processNames)
{
    // Write a user-friendly verbose message to the pipeline. These
    // messages are intended to give the user detailed information
    // on the operations performed by the cmdlet. These messages will
    // appear with the -Verbose option.
    string message = String.Format(CultureInfo.CurrentCulture,
                         "Attempting to stop process \"{0}\".", name);
    WriteVerbose(message);

    // Validate the process name against a wildcard pattern.
    // If the name does not contain any wildcard patterns, it
    // will be treated as an exact match.
    WildcardOptions options = WildcardOptions.IgnoreCase |
                              WildcardOptions.Compiled;
    WildcardPattern wildcard = new WildcardPattern(name,options);

    foreach (Process process in processes)
    {
        string processName;

       try
       {
           processName = process.ProcessName;
       }
       catch (Win32Exception e)
       {
           WriteError(new ErrorRecord(
                                  e, "ProcessNameNotFound",
                                    ErrorCategory.ObjectNotFound,
                                      process)
                     );
           continue;
       }

       // Write a debug message to the host that can be used when
       // troubleshooting a problem. All debug messages will appear
       // with the -Debug option.
       message = String.Format(CultureInfo.CurrentCulture,
                    "Acquired name for pid {0} : \"{1}\"",
                          process.Id, processName);

<!-- p.1779 -->

                   WriteDebug(message);

                   // Check to see if this process matches the current process
                   // name pattern. Skip this process if it does not.
                   if (!wildcard.IsMatch(processName))
                   {
                       continue;
                   }

                   // Stop the process.
                   SafeStopProcess(process);
               } // foreach (Process...
           } // foreach (string...
       } // ProcessRecord

       #endregion Cmdlet Overrides

       #region Helper Methods

       /// <summary>
       /// Safely stops a named process. Used as standalone function
       /// to declutter the ProcessRecord method.
       /// </summary>
       /// <param name="process">The process to stop.</param>
       private void SafeStopProcess(Process process)
       {
           string processName = null;
           try
           {
               processName = process.ProcessName;
           }
           catch (Win32Exception e)
           {
               WriteError(new ErrorRecord(e, "ProcessNameNotFound",
                                 ErrorCategory.ObjectNotFound, process));
               return;
           }

           string message = null;

           // Confirm the operation first.
           // This is always false if the WhatIf parameter is specified.
           if (!ShouldProcess(string.Format(CultureInfo.CurrentCulture,
                    "{0} ({1})", processName, process.Id)))
           {
               return;
           }

           // Make sure that the user really wants to stop a critical
           // process that could possibly stop the computer.
           bool criticalProcess =
criticalProcessNames.Contains(processName.ToLower(CultureInfo.CurrentCulture));

           if (criticalProcess && !force)
           {

<!-- p.1780 -->

               message = String.Format(CultureInfo.CurrentCulture,
                            "The process \"{0}\" is a critical process and should
not be stopped. Are you sure you wish to stop the process?",
                                processName);

               // It is possible that ProcessRecord is called multiple
               // when objects are received as inputs from a pipeline.
               // So, to retain YesToAll and NoToAll input that the
               // user may enter across multiple calls to this
               // function, they are stored as private members of the
               // Cmdlet.
               if (!ShouldContinue(message, "Warning!",
                            ref yesToAll, ref noToAll))
               {
                   return;
               }
           } // if (criticalProcess...

           // Display a warning message if stopping a critical
           // process.
           if (criticalProcess)
           {
               message = String.Format(CultureInfo.CurrentCulture,
                            "Stopping the critical process \"{0}\".",
                                processName);
               WriteWarning(message);
           } // if (criticalProcess...

           try
           {
                 // Stop the process.
                 process.Kill();
           }
           catch (Exception e)
           {
               if ((e is Win32Exception) || (e is SystemException) ||
                   (e is InvalidOperationException))
               {
                   // This process could not be stopped so write
                   // a non-terminating error.
                   WriteError(new ErrorRecord(e, "CouldNotStopProcess",
                                    ErrorCategory.CloseError,
                                    process)
                               );
                   return;
               } // if ((e is...
               else throw;
           } // catch

           message = String.Format(CultureInfo.CurrentCulture,
                        "Stopped process \"{0}\", pid {1}.",
                              processName, process.Id);

           WriteVerbose(message);

<!-- p.1781 -->

              // If the PassThru parameter is specified,
              // return the terminated process to the pipeline.
              if (passThru)
              {
                  message = String.Format(CultureInfo.CurrentCulture,
                               "Writing process \"{0}\" to pipeline",
                                   processName);
                  WriteDebug(message);
                  WriteObject(process);
              } // if (passThru...
          } // SafeStopProcess

          #endregion Helper Methods

          #region Private Data

          private bool yesToAll, noToAll;

          /// <summary>
          /// Partial list of the critical processes that should not be
          /// stopped. Lower case is used for case insensitive matching.
          /// </summary>
          private ArrayList criticalProcessNames = new ArrayList(
             new string[] { "system", "winlogon", "spoolsv" }
          );

          #endregion Private Data

    } // StopProcCommand

    #endregion StopProcCommand
 } // namespace Microsoft.Samples.PowerShell.Commands

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1782 -->

StopProcessSample04 Sample
This sample shows how to write a cmdlet that declares parameter sets, specifies the default
parameter set, and can accept an input object. This cmdlet is similar to the Stop-Process
cmdlet provided by Windows PowerShell 2.0.

How to build the sample by using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the StopProcessSample04
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\StopProcessSample04 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
     Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\StopProcessSample04

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module stopprossessample04

   5. Run the following command to run the cmdlet:

     Stop-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1783 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class by using the Cmdlet attribute.

      Declaring a cmdlet parameters by using the Parameter attribute.

      Adding a parameter that accepts input object.

      Adding parameters to parameter sets

      Specifying the default parameter set.

Example
The following code shows an implementation of the Stop-Proc cmdlet that declare parameter
sets, specifies the default parameter set, and can accept an input object.

This sample shows the input object, how to declare parameter sets, and how to specify the
default parameter set to use.

 C#

 using System;
 using System.Diagnostics;
 using System.Collections;
 using Win32Exception = System.ComponentModel.Win32Exception;
 using System.Management.Automation;             //Windows PowerShell namespace
 using System.Globalization;

 namespace Microsoft.Samples.PowerShell.Commands
 {
    #region StopProcCommand

      /// <summary>
      /// This class implements the Stop-Proc cmdlet.
      /// </summary>
      [Cmdlet(VerbsLifecycle.Stop, "Proc",
          DefaultParameterSetName = "ProcessId",
          SupportsShouldProcess = true)]
      public class StopProcCommand : PSCmdlet
      {
          #region Parameters

         /// <summary>
         /// This parameter provides the list of process names on
         /// which the Stop-Proc cmdlet will work.

<!-- p.1784 -->

      /// </summary>
       [Parameter(
          Position = 0,
          ParameterSetName = "ProcessName",
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

       /// <summary>
       /// This parameter overrides the ShouldContinue call to force
       /// the cmdlet to stop its operation. This parameter should always
       /// be used with caution.
       /// </summary>
       [Parameter]
       public SwitchParameter Force
       {
           get { return force; }
           set { force = value; }
       }
       private bool force;

       /// <summary>
       /// This parameter indicates that the cmdlet should return
       /// an object to the pipeline after the processing has been
       /// completed.
       /// </summary>
       [Parameter(
          HelpMessage = "If set the process(es) will be passed to the pipeline
after stopped."
       )]
       public SwitchParameter PassThru
       {
           get { return passThru; }
           set { passThru = value; }
       }
       private bool passThru;

      /// This parameter provides the list of process identifiers on
      /// which the Stop-Proc cmdlet will work.
       [Parameter(
          ParameterSetName = "ProcessId",
          Mandatory = true,
          ValueFromPipelineByPropertyName = true,
          ValueFromPipeline = true
       )]

<!-- p.1785 -->

[Alias("ProcessId")]
public int[] Id
{
    get { return processIds; }
    set { processIds = value; }
}
private int[] processIds;

/// <summary>
/// This parameter accepts an array of Process objects from the
/// the pipeline. This object contains the processes to stop.
/// </summary>
/// <value>Process objects</value>
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

#endregion Parameters

#region CmdletOverrides

/// <summary>
/// The ProcessRecord method does the following for each of the
/// requested process names:
/// 1) Check that the process is not a critical process.
/// 2) Attempt to stop that process.
/// If no process is requested then nothing occurs.
/// </summary>
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

<!-- p.1786 -->

                   throw new ArgumentException("Bad ParameterSet Name");
           } // switch (ParameterSetName...
       } // ProcessRecord

       #endregion Cmdlet Overrides

       #region Helper Methods

       /// <summary>
       /// Returns all processes with matching names.
       /// </summary>
       /// <param name="processName">
       /// The name of the processes to return.
       /// </param>
       /// <param name="allProcesses">An array of all
       /// computer processes.</param>
       /// <returns>An array of matching processes.</returns>
       internal ArrayList SafeGetProcessesByName(string processName,
                                ref ArrayList allProcesses)
       {
           // Create and array to store the matching processes.
           ArrayList matchingProcesses = new ArrayList();

          // Create the wildcard for pattern matching.
          WildcardOptions options = WildcardOptions.IgnoreCase |
                                    WildcardOptions.Compiled;
          WildcardPattern wildcard = new WildcardPattern(processName, options);

          // Walk all of the machine processes.
          foreach(Process process in allProcesses)
          {
              string processNameToMatch = null;
              try
              {
                  processNameToMatch = process.ProcessName;
              }
              catch (Win32Exception e)
              {
                  // Remove the process from the list so that it is not
                  // checked again.
                  allProcesses.Remove(process);

                   string message =
                         String.Format(CultureInfo.CurrentCulture, "The process \"
{0}\" could not be found",
                                             processName);
                   WriteVerbose(message);
                   WriteError(new ErrorRecord(e, "ProcessNotFound",
                                    ErrorCategory.ObjectNotFound, processName));

                   continue;
               }

               if (!wildcard.IsMatch(processNameToMatch))
               {

<!-- p.1787 -->

                     continue;
                 }

               matchingProcesses.Add(process);
           } // foreach(Process...

           return matchingProcesses;
       } // SafeGetProcessesByName

       /// <summary>
       /// Safely stops a named process. Used as standalone function
       /// to declutter the ProcessRecord method.
       /// </summary>
       /// <param name="process">The process to stop.</param>
       private void SafeStopProcess(Process process)
       {
           string processName = null;

           try
           {
                 processName = process.ProcessName;
           }
           catch (Win32Exception e)
           {
               WriteError(new ErrorRecord(e, "ProcessNotFound",
                                ErrorCategory.OpenError, processName));

                 return;
           }

           // Confirm the operation first.
           // This is always false if the WhatIf parameter is specified.
           if (!ShouldProcess(string.Format(CultureInfo.CurrentCulture,
                    "{0} ({1})", processName, process.Id)))
           {
               return;
           }

           // Make sure that the user really wants to stop a critical
           // process that can possibly stop the computer.
           bool criticalProcess =
criticalProcessNames.Contains(processName.ToLower(CultureInfo.CurrentCulture));

           string message = null;
           if (criticalProcess && !force)
           {
               message = String.Format(CultureInfo.CurrentCulture,
                                            "The process \"{0}\" is a critical
process and should not be stopped. Are you sure you wish to stop the process?",
                                                processName);
               // It is possible that the ProcessRecord method is called
               // multiple times when objects are received as inputs from
               // the pipeline. So to retain YesToAll and NoToAll input that
               // the user may enter across multiple calls to this function,
               // they are stored as private members of the cmdlet.

<!-- p.1788 -->

    if (!ShouldContinue(message, "Warning!",
                 ref yesToAll, ref noToAll))
    {
        return;
    }
} // if (criticalProcess...

// Display a warning message if stopping a critical
// process.
if (criticalProcess)
{
    message =
      String.Format(CultureInfo.CurrentCulture,
                     "Stopping the critical process \"{0}\".",
                         processName);
    WriteWarning(message);
} // if (criticalProcess...

try
{
      // Stop the process.
      process.Kill();
}
catch (Exception e)
{
    if ((e is Win32Exception) || (e is SystemException) ||
        (e is InvalidOperationException))
    {
        // This process could not be stopped so write
        // a non-terminating error.
        WriteError(new ErrorRecord(e, "CouldNotStopProcess",
                         ErrorCategory.CloseError,
                         process)
                    );

        return;
    } // if ((e is...
    else throw;
} // catch

// Write a user-level verbose message to the pipeline. These are
// intended to give the user detailed information on the
// operations performed by the cmdlet. These messages will
// appear with the -Verbose option.
message = String.Format(CultureInfo.CurrentCulture,
                             "Stopped process \"{0}\", pid {1}.",
                                 processName, process.Id);

WriteVerbose(message);

// If the PassThru parameter is specified, return the terminated
// process to the pipeline.
if (passThru)
{
    // Write a debug message to the host that can be used

<!-- p.1789 -->

        // when troubleshooting a problem. All debug messages
        // will appear with the -Debug option
        message =
            String.Format(CultureInfo.CurrentCulture,
                             "Writing process \"{0}\" to pipeline",
                                 processName);
        WriteDebug(message);
        WriteObject(process);
    } // if (passThru..
} // SafeStopProcess

/// <summary>
/// Stop processes based on their names (using the
/// ParameterSetName as ProcessName)
/// </summary>
private void ProcessByName()
{
    ArrayList allProcesses = null;

   // Get a list of all processes.
   try
   {
       allProcesses = new ArrayList(Process.GetProcesses());
   }
   catch (InvalidOperationException ioe)
   {
       base.ThrowTerminatingError(new ErrorRecord(
            ioe, "UnableToAccessProcessList",
            ErrorCategory.InvalidOperation, null));
   }

   // If a process name is passed to the cmdlet, get
   // the associated processes.
   // Write a non-terminating error for failure to
   // retrieve a process.
   foreach (string name in processNames)
   {
       // The allProcesses array list is passed as a reference because
       // any process whose name cannot be obtained will be removed
       // from the list so that its not compared the next time.
       ArrayList processes =
           SafeGetProcessesByName(name, ref allProcesses);

       // If no processes were found write a non-
       // terminating error.
       if (processes.Count == 0)
       {
           WriteError(new ErrorRecord(
               new Exception("Process not found."),
               "ProcessNotFound",
               ErrorCategory.ObjectNotFound,
               name));
       } // if (processes...
       // Otherwise terminate all processes in the list.
       else

<!-- p.1790 -->

                 {
                      foreach (Process process in processes)
                      {
                          SafeStopProcess(process);
                      } // foreach (Process...
                  } // else
              } // foreach (string...
          } // ProcessByName

          /// <summary>
          /// Stop processes based on their identifiers (using the
          /// ParameterSetName as ProcessIds)
          /// </summary>
          internal void ProcessById()
          {
              foreach (int processId in processIds)
              {
                  Process process = null;
                  try
                  {
                      process = Process.GetProcessById(processId);

                     // Write a debug message to the host that can be used
                     // when troubleshooting a problem. All debug messages
                     // will appear with the -Debug option
                     string message =
                         String.Format(CultureInfo.CurrentCulture,
                                          "Acquired process for pid : {0}",
                                              process.Id);
                     WriteDebug(message);
                 }
                 catch (ArgumentException ae)
                 {
                     string
                         message = String.Format(CultureInfo.CurrentCulture,
                                              "The process id {0} could not be
found",
                                                  processId);
                     WriteVerbose(message);
                     WriteError(new ErrorRecord(ae, "ProcessIdNotFound",
                                      ErrorCategory.ObjectNotFound, processId));
                     continue;
                 }

                  SafeStopProcess(process);
              } // foreach (int...
          } // ProcessById

          #endregion Helper Methods

          #region Private Data

          private bool yesToAll, noToAll;

          /// <summary>

<!-- p.1791 -->

          /// Partial list of critical processes that should not be
          /// stopped. Lower case is used for case insensitive matching.
          /// </summary>
          private ArrayList criticalProcessNames = new ArrayList(
             new string[] { "system", "winlogon", "spoolsv", "calc" }
          );

          #endregion Private Data

     } // StopProcCommand

     #endregion StopProcCommand
 }

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1792 -->

Events01 Sample
This sample shows how to create a cmdlet that allows the user to register for events that are
raised by System.IO.FileSystemWatcher. With this cmdlet, users can register an action to
execute when a file is created under a specific directory. This sample derives from the
Microsoft.PowerShell.Commands.ObjectEventRegistrationBase base class.

How to build the sample by using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the Events01 folder. The
     default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\Events01 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
     Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\events01

   2. Copy the library file for the sample to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the cmdlet into Windows PowerShell:

       PowerShell

       Import-Module events01

   5. Use the Register-FileSystemEvent cmdlet to register an action that will write a message
     when a file is created under the TEMP directory.

       PowerShell

<!-- p.1793 -->

       Register-FileSystemEvent $Env:TEMP Created -Filter "*.txt" -Action { Write-
       Host "A file was created in the TEMP directory" }

   6. Create a file under the TEMP directory and note that the action is executed (the message
     is displayed).

This is a sample output that results by following these steps.

 Output

 Id              Name            State      HasMoreData           Location
 Command
 --              ----            -----      -----------           --------               ---
 ----
 1               26932870-d3b... NotStarted False
 Write-Host "A f...

 PowerShell

 Set-Content $Env:TEMP\test.txt "This is a test file"

 Output

 A file was created in the TEMP directory

Requirements
This sample requires Windows PowerShell 2.0.

Demonstrates
This sample demonstrates the following.

How to write a cmdlet for event registration
The cmdlet derives from the Microsoft.PowerShell.Commands.ObjectEventRegistrationBase
class, which provides support for parameters common to the Register-*Event cmdlets.
Cmdlets that are derived from Microsoft.PowerShell.Commands.ObjectEventRegistrationBase
need only to define their particular parameters and override the GetSourceObject and
GetSourceObjectEventName abstract methods.

<!-- p.1794 -->

Example
This sample shows how to register for events raised by System.IO.FileSystemWatcher.

 C#

 namespace Sample
 {
     using System;
     using System.IO;
     using System.Management.Automation;
     using System.Management.Automation.Runspaces;
     using Microsoft.PowerShell.Commands;

      [Cmdlet(VerbsLifecycle.Register, "FileSystemEvent")]
      public class RegisterObjectEventCommand : ObjectEventRegistrationBase
      {
          /// <summary>The FileSystemWatcher that exposes the events.</summary>
          private FileSystemWatcher fileSystemWatcher = new FileSystemWatcher();

          /// <summary>Name of the event to which the cmdlet registers.</summary>
          private string eventName = null;

          /// <summary>
          /// Gets or sets the path that will be monitored by the FileSystemWatcher.
          /// </summary>
          [Parameter(Mandatory = true, Position = 0)]
          public string Path
          {
              get
              {
                  return this.fileSystemWatcher.Path;
              }

              set
              {
                    this.fileSystemWatcher.Path = value;
              }
          }

         /// <summary>
         /// Gets or sets the name of the event to which the cmdlet registers.
         /// <para>
         /// Currently System.IO.FileSystemWatcher exposes 6 events: Changed,
 Created,
         /// Deleted, Disposed, Error, and Renamed. Check the documentation of
         /// FileSystemWatcher for details on each event.
         /// </para>
         /// </summary>
         [Parameter(Mandatory = true, Position = 1)]
         public string EventName
         {
             get

<!-- p.1795 -->

            {
                  return this.eventName;
            }

            set
            {
                  this.eventName = value;
            }
       }

       /// <summary>
       /// Gets or sets the filter that will be user by the FileSystemWatcher.
       /// </summary>
       [Parameter(Mandatory = false)]
       public string Filter
       {
           get
           {
               return this.fileSystemWatcher.Filter;
           }

            set
            {
                  this.fileSystemWatcher.Filter = value;
            }
       }

        /// <summary>
        /// Derived classes must implement this method to return the object that
generates
        /// the events to be monitored.
        /// </summary>
        /// <returns> This sample returns an instance of
System.IO.FileSystemWatcher</returns>
        protected override object GetSourceObject()
        {
            return this.fileSystemWatcher;
        }

        /// <summary>
        /// Derived classes must implement this method to return the name of the
event to
        /// be monitored. This event must be exposed by the input object.
        /// </summary>
        /// <returns> This sample returns the event specified by the user with the
-EventName parameter.</returns>
        protected override string GetSourceObjectEventName()
        {
            return this.eventName;
        }
    }
}

<!-- p.1796 -->

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1797 -->

Writing a Windows PowerShell Module
This document is written for administrators, script developers, and cmdlet developers who
need to package and distribute their Windows PowerShell cmdlets. By using Windows
PowerShell modules, you can package and distribute your Windows PowerShell solutions
without using a compiled language.

Windows PowerShell modules enable you to partition, organize, and abstract your Windows
PowerShell code into self-contained, reusable units. With these reusable units, you can easily
share your modules directly with others. If you are a script developer, you can also repackage
third-party modules to create custom script-based applications. Modules, similar to modules in
other scripting languages such as Perl and Python, enable production-ready scripting solutions
that use reusable, redistributable components, with the added benefit of enabling you to
repackage and abstract multiple components to create custom solutions.

At their most basic, Windows PowerShell will treat any valid Windows PowerShell script code
saved in a .psm1 file as a module. PowerShell will also automatically treat any binary cmdlet
assembly as a module. However, you can also use a module (or more specifically, a module
manifest) to bundle an entire solution together. The following scenarios describe typical uses
for Windows PowerShell modules.

Libraries
Modules can be used to package and distribute cohesive libraries of functions that perform
common tasks. Typically, the names of these functions share one or more nouns that reflect the
common task that they are used for. These functions can also be similar to .NET Framework
classes in that they can have public and private members. For example, a library can contain a
set of functions for file transfers. In this case, the noun reflecting the common task might be
"file."

Configuration
Modules can be used to customize your environment by adding specific cmdlets, providers,
functions, and variables.

Compiled Code Development and Distribution

<!-- p.1798 -->

Cmdlet and provider developers can use modules to test and distribute their compiled code
without needing to create snap-ins. They can import the assembly that contains the compiled
code as a module (a binary module) without needing to create and register snap-ins.

See Also
Understanding a Windows PowerShell Module

How to Write a PowerShell Script Module

How to Write a PowerShell Binary Module

How to Write a PowerShell Module Manifest

about_PSModulePath

Importing a PowerShell Module

Installing a PowerShell Module

Last updated on 05/20/2025

<!-- p.1799 -->

Understanding a Windows PowerShell
Module
A module is a set of related Windows PowerShell functionalities, grouped together as a
convenient unit (usually saved in a single directory). By defining a set of related script files,
assemblies, and related resources as a module, you can reference, load, persist, and share your
code much easier than you would otherwise.

The main purpose of a module is to allow the reuse and abstraction of Windows PowerShell code.
For example, the most basic way of creating a module is to simply save a Windows PowerShell
script as a .psm1 file. Doing so allows you to control which functions and variables are exposed to
users variables in the script are public or private. Saving the script as a .psm1 file also allows you
to control the scope of certain variables. Finally, you can also use cmdlets such as Install-Module
to organize, install, and use your script as a building block for larger solutions.

Module Components and Types
A module is made up of four basic components:

   1. Some sort of code file - usually either a PowerShell script or a managed cmdlet assembly.

   2. Anything else that the above code file may need, such as additional assemblies, help files, or
     scripts.

   3. A manifest file that describes the above files, as well as stores metadata such as author and
     versioning information.

   4. A directory that contains all of the above content, and is located where PowerShell can
     reasonably find it.

        ７ Note

        None of these components, by themselves, are actually necessary. For example, a
        module can technically be only a script stored in a .psm1 file. You can also have a
        module that's nothing but a manifest file, which is used mainly for organizational
        purposes. You can also write a script that dynamically creates a module, and as such
        doesn't actually need a directory to store anything in. The following sections describe

<!-- p.1800 -->

        the types of modules you can get by mixing and matching the different possible parts
        of a module together.

Script Modules
As the name implies, a script module is a file ( .psm1 ) that contains any valid Windows PowerShell
code. Script developers and administrators can use this type of module to create modules whose
members include functions, variables, and more. At heart, a script module is simply a Windows
PowerShell script with a different extension, which allows administrators to use import, export,
and management functions on it.

In addition, you can use a manifest file to include other resources in your module, such as data
files, other dependent modules, or runtime scripts. Manifest files are also useful for tracking
metadata such as authoring and versioning information.

Finally, a script module, like any other module that isn't dynamically created, needs to be saved in
a folder that PowerShell can reasonably discover. Usually, this is on the PowerShell module path;
but if necessary you can explicitly describe where your module is installed. For more information,
see How to Write a PowerShell Script Module.

Binary Modules
A binary module is a .NET Framework assembly ( .dll ) that contains compiled code, such as C#.
Cmdlet developers can use this type of module to share cmdlets, providers, and more. Existing
snap-ins can also be used as binary modules. Compared to a script module, a binary module
allows you to create cmdlets that are faster or use features (such as multithreading) that aren't as
easy to code in Windows PowerShell scripts.

As with script modules, you can include a manifest file to describe additional resources that your
module uses, and to track metadata about your module. Similarly, you probably should install
your binary module in a folder somewhere along the PowerShell module path. For more
information, see How to How to Write a PowerShell Binary Module.

Manifest Modules
A manifest module is a module that uses a manifest file to describe all of its components, but
doesn't have any sort of core assembly or script. Formally, a manifest module leaves the
ModuleToProcess or RootModule element of the manifest empty. However, you can still use the

other features of a module, such as the ability to load up dependent assemblies or automatically
