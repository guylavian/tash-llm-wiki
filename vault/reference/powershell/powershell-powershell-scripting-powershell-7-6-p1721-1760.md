---
title: "How to use this documentation — pages 1721-1760"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1721-1760
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1721-1760
family: powershell
documentKind: "doc"
abstract: "/// specific items are searched. When this parameter /// is used, items that are not listed here are omitted /// from the search. /// </summary> [Parameter] [ValidateNotNullOrEmpty] public string[] Include { get { return includeStrings; } set { includeStrings = value; this.inclu"
---

# How to use this documentation — pages 1721-1760

<!-- p.1721 -->

    /// specific items are searched. When this parameter
    /// is used, items that are not listed here are omitted
    /// from the search.
    /// </summary>
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

    /// <summary>
    /// Declare an Exclude parameter that species which
    /// specific items are omitted from the search.
    /// </summary>
    ///
    [Parameter]
    [ValidateNotNullOrEmpty]
    public string[] Exclude
    {
      get
      {
        return excludeStrings;
      }
      set
      {
        excludeStrings = value;

        this.exclude = new WildcardPattern[excludeStrings.Length];
        for (int i = 0; i < excludeStrings.Length; i++)
        {
          this.exclude[i] = new WildcardPattern(excludeStrings[i],
WildcardOptions.IgnoreCase);
        }
      }
    }
    internal string[] excludeStrings;
    internal WildcardPattern[] exclude;

<!-- p.1722 -->

#endregion Parameters

#region Overrides
/// <summary>
/// If regular expressions are used for pattern matching,
/// then build an array of compiled regular expressions
/// at startup. This increases performance during scanning
/// operations when simple matching is not used.
/// </summary>
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

<!-- p.1723 -->

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

/// <summary>
/// Process the input and search for the specified patterns.
/// </summary>
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

<!-- p.1724 -->

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

<!-- p.1725 -->

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
#endregion Overrides

#region PrivateMethods
/// <summary>
/// Check for a match using the input string and the pattern(s)
/// specified.
/// </summary>
/// <param name="input">The string to test.</param>
/// <returns>MatchInfo object containing information about
/// result of a match</returns>
private MatchInfo SelectString(object input)
{
  string line = null;

 try
 {
   // Convert the object to a string type
   // safely using language support methods
   line = (string)LanguagePrimitives.ConvertTo(
                                                  input,
                                                  typeof(string)
                                                  );
   line = line.Trim(' ','\t');
 }
 catch (PSInvalidCastException ex)
 {
   WriteError(new ErrorRecord(
              ex,

<!-- p.1726 -->

               "CannotCastObjectToString",
               ErrorCategory.InvalidOperation,
               input)
               );

    return null;
}

MatchInfo result = null;

// If a scriptblock has been specified, call it
// with the path for processing. It will return
// one object.
if (script != null)
{
  WriteDebug("Executing script block.");

    Collection<PSObject> psObjects =
                         script.Invoke(
                                       line,
                                       simpleMatch,
                                       caseSensitive
                                      );

    foreach (PSObject psObject in psObjects)
    {
      if (LanguagePrimitives.IsTrue(psObject))
      {
        result = new MatchInfo();
        result.Line = line;
        result.IgnoreCase = !caseSensitive;

      break;
    } //End of If.
  } //End ForEach loop.
} // End of If if script exists.

// If script block exists, see if this line matches any
// of the match patterns.
else
{
  int patternIndex = 0;

    while (patternIndex < patterns.Length)
    {
      if ((simpleMatch &&
          wildcardPattern[patternIndex].IsMatch(line))
          || (regexPattern != null
          && regexPattern[patternIndex].IsMatch(line))
         )
      {
        result = new MatchInfo();
        result.IgnoreCase = !caseSensitive;
        result.Line = line;
        result.Pattern = patterns[patternIndex];

<!-- p.1727 -->

          break;
      }

      patternIndex++;

   }// While loop through patterns.
 }// Else for no script block specified.

 return result;

}// End of SelectString

/// <summary>
/// Check whether the supplied name meets the include/exclude criteria.
/// That is - it's on the include list if the include list was
/// specified, and not on the exclude list if the exclude list was specified.
/// </summary>
/// <param name="path">path to validate</param>
/// <returns>True if the path is acceptable.</returns>
private bool MeetsIncludeExcludeCriteria(string path)
{
  bool ok = false;

 // See if the file is on the include list.
 if (this.include != null)
 {
   foreach (WildcardPattern patternItem in this.include)
   {
      if (patternItem.IsMatch(path))
      {
        ok = true;
        break;
      }
   }
 }
 else
 {
   ok = true;
 }

 if (!ok)
    return false;

 // See if the file is on the exclude list.
 if (this.exclude != null)
 {
   foreach (WildcardPattern patternItem in this.exclude)
   {
     if (patternItem.IsMatch(path))
     {
       ok = false;
       break;
     }
   }

<!-- p.1728 -->

   }

   return ok;
 } //MeetsIncludeExcludeCriteria
 #endregion Private Methods

}// class SelectStringCommand

#endregion SelectStringCommand

#region MatchInfo

/// <summary>
/// Class representing the result of a pattern/literal match
/// that is passed through the pipeline by the Select-Str cmdlet.
/// </summary>
public class MatchInfo
{
  /// <summary>
  /// Indicates if the match was done ignoring case.
  /// </summary>
  /// <value>True if case was ignored.</value>
  public bool IgnoreCase
  {
    get { return ignoreCase; }
    set { ignoreCase = value; }
  }
  private bool ignoreCase;

 /// <summary>
 /// Specifies the number of the matching line.
 /// </summary>
 /// <value>The number of the matching line.</value>
 public UInt64 LineNumber
 {
   get { return lineNumber; }
   set { lineNumber = value; }
 }
 private UInt64 lineNumber;

 /// <summary>
 /// Specifies the text of the matching line.
 /// </summary>
 /// <value>The text of the matching line.</value>
 public string Line
 {
   get { return line; }
   set { line = value; }
 }
 private string line;

 /// <summary>
 /// Specifies the full path of the object(file) containing the
 /// matching line.
 /// </summary>

<!-- p.1729 -->

/// <remarks>
/// It will be "inputStream" if the object came from the input
/// stream.
/// </remarks>
/// <value>The path name</value>
public string Path
{
  get { return path; }
  set
  {
    pathSet = true;
    path = value;
  }
}
private string path;
private bool pathSet;

/// <summary>
/// Specifies the pattern that was used in the match.
/// </summary>
/// <value>The pattern string</value>
public string Pattern
{
  get { return pattern; }
  set { pattern = value; }
}
private string pattern;

private const string MatchFormat = "{0}:{1}:{2}";

/// <summary>
/// Returns the string representation of this object. The format
/// depends on whether a path has been set for this object or
/// not.
/// </summary>
/// <remarks>
/// If the path component is set, as would be the case when
/// matching in a file, ToString() returns the path, line
/// number and line text. If path is not set, then just the
/// line text is presented.
/// </remarks>
/// <returns>The string representation of the match object.</returns>
public override string ToString()
{
  if (pathSet)
     return String.Format(
     System.Threading.Thread.CurrentThread.CurrentCulture,
     MatchFormat,
     this.path,
     this.lineNumber,
     this.line
     );
  else
     return this.line;
}

<!-- p.1730 -->

}// End class MatchInfo

#endregion

#region PowerShell snap-in

/// <summary>
/// Create a PowerShell snap-in for the Select-Str cmdlet.
/// </summary>
[RunInstaller(true)]
public class SelectStringPSSnapIn : PSSnapIn
{
  /// <summary>
  /// Create an instance of the SelectStrPSSnapin class.
  /// </summary>
  public SelectStringPSSnapIn()
         : base()
  {
  }

 /// <summary>
 /// Specify the name of the PowerShell snap-in.
 /// </summary>
 public override string Name
 {
   get
   {
     return "SelectStrPSSnapIn";
   }
 }

 /// <summary>
 /// Specify the vendor of the PowerShell snap-in.
 /// </summary>
 public override string Vendor
 {
   get
   {
     return "Microsoft";
   }
 }

 /// <summary>
 /// Specify the localization resource information for the vendor.
 /// Use the format: SnapinName,VendorName.
 /// </summary>
 public override string VendorResource
 {
   get
   {
     return "SelectStrSnapIn,Microsoft";
   }
 }

 /// <summary>

<!-- p.1731 -->

      /// Specify the description of the PowerShell snap-in.
      /// </summary>
      public override string Description
      {
        get
          {
            return "This is a PowerShell snap-in for the Select-Str cmdlet.";
          }
      }

      /// <summary>
      /// Specify the localization resource information for the description.
      /// Use the format: SnapinName,Description.

     /// </summary>
     public override string DescriptionResource
     {
       get
       {
           return "SelectStrSnapIn,This is a PowerShell snap-in for the Select-Str
 cmdlet.";
       }
     }
   }
   #endregion PowerShell snap-in

 } //namespace Microsoft.Samples.PowerShell.Commands;

Building the Cmdlet
After implementing a cmdlet, you must register it with Windows PowerShell through a
Windows PowerShell snap-in. For more information about registering cmdlets, see How to
Register Cmdlets, Providers, and Host Applications   .

Testing the Cmdlet
When your cmdlet has been registered with Windows PowerShell, you can test it by running it
on the command line. The following procedure can be used to test the sample Select-Str
cmdlet.

   1. Start Windows PowerShell, and search the Notes file for occurrences of lines with the
     expression ".NET". Note that the quotation marks around the name of the path are
     required only if the path consists of more than one word.

       PowerShell

       Select-Str -Path "notes" -Pattern ".NET" -SimpleMatch=$false

<!-- p.1732 -->

  The following output appears.

    Output

    IgnoreCase   : True
    LineNumber   : 8
    Line         : Because Windows PowerShell works directly with .NET objects,
    there is often a .NET object
    Path         : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern      : .NET
    IgnoreCase   : True
    LineNumber   : 21
    Line         : You should normally define the class for a cmdlet in a .NET
    namespace
    Path         : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern      : .NET

2. Search the Notes file for occurrences of lines with the word "over", followed by any other
  text. The SimpleMatch parameter is using the default value of false . The search is case-
  insensitive because the CaseSensitive parameter is set to false .

    PowerShell

    Select-Str -Path notes -Pattern "over*" -SimpleMatch -CaseSensitive:$false

  The following output appears.

    Output

    IgnoreCase    : True
    LineNumber    : 45
    Line          : Override StopProcessing
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : over*
    IgnoreCase    : True
    LineNumber    : 49
    Line          : overriding the StopProcessing method
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : over*

3. Search the Notes file using a regular expression as the pattern. The cmdlet searches for
  alphabetical characters and blank spaces enclosed in parentheses.

    PowerShell

    Select-Str -Path notes -Pattern "\([A-Za-z:blank:]" -SimpleMatch:$false

<!-- p.1733 -->

  The following output appears.

    Output

    IgnoreCase    : True
    LineNumber    : 1
    Line          : Advisory Guidelines (Consider Following)
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : \([A-Za-z:blank:]
    IgnoreCase    : True
    LineNumber    : 53
    Line          : If your cmdlet has objects that are not disposed of (written to
    the pipeline)
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : \([A-Za-z:blank:]

4. Perform a case-sensitive search of the Notes file for occurrences of the word "Parameter".

    PowerShell

    Select-Str -Path notes -Pattern Parameter -CaseSensitive

  The following output appears.

    Output

    IgnoreCase    : False
    LineNumber    : 6
    Line          : Support an InputObject Parameter
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : Parameter
    IgnoreCase    : False
    LineNumber    : 30
    Line          : Support Force Parameter
    Path          : C:\PowerShell-Progs\workspace\Samples\SelectStr\notes
    Pattern       : Parameter

5. Search the Variable provider shipped with Windows PowerShell for variables that have
  numerical values from 0 through 9.

    PowerShell

    Select-Str -Path * -Pattern "[0-9]"

  The following output appears.

    Output

<!-- p.1734 -->

       IgnoreCase       : True
       LineNumber       : 1
       Line             : 64
       Path             : Variable:\MaximumHistoryCount
       Pattern          : [0-9]

   6. Use a script block to search the file SelectStrCommandSample.cs for the string "Pos". The
     -cmatch operator performs a case-insensitive pattern match.

       PowerShell

       Select-Str -Path "SelectStrCommandSample.cs" -Script {
           if ($args[0] -cmatch "Pos"){ return $true }
           return $false
       }

     The following output appears.

       Output

       IgnoreCase   : True
       LineNumber   : 37
       Line         :    Position = 0.
       Path         : C:\PowerShell-
       Progs\workspace\Samples\SelectStr\SelectStrCommandSample.cs
       Pattern      :

See Also
How to Create a Windows PowerShell Cmdlet

Creating Your First Cmdlet

Creating a Cmdlet that Modifies the System

Design Your Windows PowerShell Provider

How Windows PowerShell Works

How to Register Cmdlets, Providers, and Host Applications )

Windows PowerShell SDK

Last updated on 04/08/2026

<!-- p.1735 -->

Cmdlet Samples
This section describes sample code that is provided in the Windows PowerShell 2.0 SDK.

In This Section
     GetProcessSample01 Sample: This sample shows how to write a cmdlet that retrieves the
     processes on the local computer.

     GetProcessSample02 Sample: This sample shows how to write a cmdlet that retrieves the
     processes on the local computer. It provides a Name parameter that can be used to
     specify the processes to be retrieved.

     GetProcessSample03 Sample: This sample shows how to write a cmdlet that retrieves the
     processes on the local computer. It provides a Name parameter that can accept an object
     from the pipeline or a value from a property of an object whose property name is the
     same as the parameter name.

     GetProcessSample04 Sample: This sample shows how to write a cmdlet that retrieves the
     processes on the local computer. It generates a non-terminating error if an error occurs
     while retrieving a process.

     GetProcessSample05 Sample: This sample shows a complete version of the Get-Proc
     cmdlet.

     StopProcessSample01 Sample: This sample shows how to write a cmdlet that requests
     feedback from the user before it attempts to stop a process, and how to implement a
     PassThru parameter that indicates that the user wants the cmdlet to return an object.

     StopProcessSample02 Sample: This sample shows how to write a cmdlet that writes
     debug, verbose, and warning messages while stopping processes on the local computer.

     StopProcessSample03 Sample: This sample shows how to write a cmdlet whose
     parameters have aliases and that support wildcard characters.

     StopProcessSample04 Sample: This sample shows how to write a cmdlet that declares
     parameter sets, specifies the default parameter set, and can accept an input object.

     Events01 Sample: This sample shows how to create a cmdlet that allows the user to
     register for events raised by System.IO.FileSystemWatcher. With this cmdlet users can, for

<!-- p.1736 -->

     example, register an action to execute when a file is created under a specific directory.
     This sample derives from the
     Microsoft.PowerShell.Commands.ObjectEventRegistrationBase base class.

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1737 -->

GetProcessSample01 Sample
This sample shows how to implement a cmdlet that retrieves the processes on the local
computer. This cmdlet is a simplified version of the Get-Process cmdlet that is provided by
Windows PowerShell 2.0.

How to build the sample by using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the GetProcessSample01
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\GetProcessSample01 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Microsoft
     Visual Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Open a Command Prompt window.

   2. Navigate to the directory containing the sample .dll file.

   3. Run installutil "GetProcessSample01.dll" .

   4. Start Windows PowerShell.

   5. Run the following command to add the snap-in to the shell.

     Add-PSSnapin GetProcPSSnapIn01

   6. Enter the following command to run the cmdlet. Get-Proc

     Get-Proc

     This is a sample output that results from following these steps.

       Output

<!-- p.1738 -->

       Id              Name            State      HasMoreData          Location
       Command
       --              ----            -----      -----------          --------
       -------
       1               26932870-d3b... NotStarted False
       Write-Host "A f...

       PowerShell

       Set-Content $Env:TEMP\test.txt "This is a test file"

       Output

       A file was created in the TEMP directory

Requirements
This sample requires Windows PowerShell 1.0 or later.

Demonstrates
This sample demonstrates the following.

      Creating a basic sample cmdlet.

      Defining a cmdlet class by using the Cmdlet attribute.

      Creating a snap-in that works with both Windows PowerShell 1.0 and Windows
      PowerShell 2.0. Subsequent samples use modules instead of snap-ins so they require
      Windows PowerShell 2.0.

Example
This sample shows how to create a simple cmdlet and its snap-in.

 C#

 using System;
 using System.Diagnostics;
 using System.Management.Automation;                    //Windows PowerShell namespace
 using System.ComponentModel;

 namespace Microsoft.Samples.PowerShell.Commands

<!-- p.1739 -->

{

    #region GetProcCommand

    /// <summary>
    /// This class implements the Get-Proc cmdlet.
    /// </summary>
    [Cmdlet(VerbsCommon.Get, "Proc")]
    public class GetProcCommand : Cmdlet
    {
       #region Cmdlet Overrides

       /// <summary>
       /// The ProcessRecord method calls the Process.GetProcesses
       /// method to retrieve the processes of the local computer.
       /// Then, the WriteObject method writes the associated processes
       /// to the pipeline.
       /// </summary>
       protected override void ProcessRecord()
       {
          // Retrieve the current processes.
          Process[] processes = Process.GetProcesses();

           // Write the processes to the pipeline to make them available
           // to the next cmdlet. The second argument (true) tells Windows
           // PowerShell to enumerate the array and to send one process
           // object at a time to the pipeline.
           WriteObject(processes, true);
       }

       #endregion Overrides

    } //GetProcCommand

    #endregion GetProcCommand

    #region PowerShell snap-in

    /// <summary>
    /// Create this sample as a PowerShell snap-in
    /// </summary>
    [RunInstaller(true)]
    public class GetProcPSSnapIn01 : PSSnapIn
    {
        /// <summary>
        /// Create an instance of the GetProcPSSnapIn01
        /// </summary>
        public GetProcPSSnapIn01()
            : base()
        {
        }

       /// <summary>
       /// Get a name for this PowerShell snap-in. This name will be used in
registering

<!-- p.1740 -->

        /// this PowerShell snap-in.
        /// </summary>
        public override string Name
        {
            get
            {
                return "GetProcPSSnapIn01";
            }
        }

        /// <summary>
        /// Vendor information for this PowerShell snap-in.
        /// </summary>
        public override string Vendor
        {
            get
            {
                return "Microsoft";
            }
        }

        /// <summary>
        /// Gets resource information for vendor. This is a string of format:
        /// resourceBaseName,resourceName.
        /// </summary>
        public override string VendorResource
        {
            get
            {
                return "GetProcPSSnapIn01,Microsoft";
            }
        }

       /// <summary>
       /// Description of this PowerShell snap-in.
       /// </summary>
       public override string Description
       {
           get
           {
               return "This is a PowerShell snap-in that includes the Get-Proc
cmdlet.";
           }
       }
   }

    #endregion PowerShell snap-in
}

See Also
    Writing a Windows PowerShell Cmdlet

<!-- p.1741 -->

Last updated on 05/20/2025

<!-- p.1742 -->

GetProcessSample02 Sample
This sample shows how to write a cmdlet that retrieves the processes on the local computer. It
provides a Name parameter that can be used to specify the processes to be retrieved. This
cmdlet is a simplified version of the Get-Process cmdlet provided by Windows PowerShell 2.0.

How to build the sample using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the GetProcessSample02
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\GetProcessSample02 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Visual
     Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\GetProcessSample02

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module getprossessample02

   5. Run the following command to run the cmdlet:

     Get-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1743 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class using the Cmdlet attribute.

      Declaring a cmdlet parameter using the Parameter attribute.

      Specifying the position of the parameter.

      Declaring a validation attribute for the parameter input.

Example
This sample shows an implementation of the Get-Proc cmdlet that includes a Name parameter.

 C#

 namespace Microsoft.Samples.PowerShell.Commands
 {
   using System;
   using System.Diagnostics;
   using System.Management.Automation;     // Windows PowerShell namespace

   #region GetProcCommand

   /// <summary>
   /// This class implements the Get-Proc cmdlet.
   /// </summary>
   [Cmdlet(VerbsCommon.Get, "Proc")]
   public class GetProcCommand : Cmdlet
   {
     #region Parameters

      /// <summary>
      /// The names of the processes retrieved by the cmdlet.
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

<!-- p.1744 -->

      #endregion Parameters

      #region Cmdlet Overrides

       /// <summary>
       /// The ProcessRecord method calls the Process.GetProcesses
       /// method to retrieve the processes specified by the Name
       /// parameter. Then, the WriteObject method writes the
       /// associated process objects to the pipeline.
       /// </summary>
       protected override void ProcessRecord()
       {
         // If no process names are passed to the cmdlet, get all
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
         } // End if (processNames...).
       } // End ProcessRecord.
       #endregion Cmdlet Overrides
     } // End GetProcCommand class.
     #endregion GetProcCommand
 }

See Also
      Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1745 -->

GetProcessSample03 Sample
This sample shows how to implement a cmdlet that retrieves the processes on the local
computer. It provides a Name parameter that can accept an object from the pipeline or a value
from a property of an object whose property name is the same as the parameter name. This
cmdlet is a simplified version of the Get-Process cmdlet provided by Windows PowerShell 2.0.

How to build the sample using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the GetProcessSample03
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\GetProcessSample03 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Visual
     Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\GetProcessSample03

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module getprossessample03

   5. Run the following command to run the cmdlet:

     Get-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1746 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class using the Cmdlet attribute.

      Declaring a cmdlet parameter using the Parameter attribute.

      Specifying the position of the parameter.

      Specifying that the parameter takes input from the pipeline. The input can be taken from
      an object or a value from a property of an object whose property name is the same as the
      parameter name.

      Declaring a validation attribute for the parameter input.

Example
This sample shows an implementation of the Get-Proc cmdlet that includes a Name parameter
that accepts input from the pipeline.

 C#

 namespace Microsoft.Samples.PowerShell.Commands
 {
   using System;
   using System.Diagnostics;
   using System.Management.Automation;           // Windows PowerShell namespace
   #region GetProcCommand

    /// <summary>
    /// This class implements the Get-Proc cmdlet.
    /// </summary>
    [Cmdlet(VerbsCommon.Get, "Proc")]
    public class GetProcCommand : Cmdlet
    {
      #region Parameters

      /// <summary>
      /// The names of the processes retrieved by the cmdlet.
      /// </summary>
      private string[] processNames;

      /// <summary>
      /// Gets or sets the names of the
      /// process that the cmdlet will retrieve.
      /// </summary>
      [Parameter(

<!-- p.1747 -->

                 Position = 0,
                 ValueFromPipeline = true,
                 ValueFromPipelineByPropertyName = true)]
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
        // processes.
        if (this.processNames == null)
        {
          WriteObject(Process.GetProcesses(), true);
        }
        else
        {
          // If process names are passed to the cmdlet, get and write
          // the associated processes.
          foreach (string name in this.processNames)
          {
             WriteObject(Process.GetProcessesByName(name), true);
          }
        } // End if (processNames ...)
      } // End ProcessRecord.

       #endregion Overrides
     } // End GetProcCommand.
     #endregion GetProcCommand
 }

See Also
      Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1748 -->

GetProcessSample04 Sample
This sample shows how to implement a cmdlet that retrieves the processes on the local
computer. It generates a non-terminating error if an error occurs while retrieving a process.
This cmdlet is a simplified version of the Get-Process cmdlet provided by Windows PowerShell
2.0.

How to build the sample using Visual Studio
   1. With the Windows PowerShell 2.0 SDK installed, navigate to the GetProcessSample04
       folder. The default location is C:\Program Files (x86)\Microsoft
       SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\GetProcessSample04 .

   2. Double-click the icon for the solution (.sln) file. This opens the sample project in Visual
       Studio.

   3. In the Build menu, select Build Solution to build the library for the sample in the default
       \bin or \bin\debug folders.

How to run the sample
   1. Create the following module folder:

       [user]\Documents\WindowsPowerShell\Modules\GetProcessSample04

   2. Copy the sample assembly to the module folder.

   3. Start Windows PowerShell.

   4. Run the following command to load the assembly into Windows PowerShell:

       Import-Module getprossessample04

   5. Run the following command to run the cmdlet:

       Get-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1749 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class using the Cmdlet attribute.

      Declaring a cmdlet parameter using the Parameter attribute.

      Specifying the position of the parameter.

      Specifying that the parameter takes input from the pipeline. The input can be taken from
      an object or a value from a property of an object whose property name is the same as the
      parameter name.

      Declaring a validation attribute for the parameter input.

      Trapping a non-terminating error and writing an error message to the error stream.

Example
This sample shows how to create a cmdlet that handles non-terminating errors and writes error
messages to the error stream.

 C#

 namespace Microsoft.Samples.PowerShell.Commands
 {
     using System;
     using System.Diagnostics;
     using System.Management.Automation;      // Windows PowerShell namespace.
    #region GetProcCommand

      /// <summary>
      /// This class implements the Get-Proc cmdlet.
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
         /// Gets or sets the list of process names on
         /// which the Get-Proc cmdlet will work.

<!-- p.1750 -->

/// </summary>
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
    // If no process names are passed to cmdlet, get all
    // processes.
    if (this.processNames == null)
    {
        WriteObject(Process.GetProcesses(), true);
    }
    else
    {
        // If process names are passed to the cmdlet, get and write
        // the associated processes.
        // If a non-terminating error occurs while retrieving processes,
        // call the WriteError method to send an error record to the
        // error stream.
        foreach (string name in this.processNames)
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
                   "UnableToAccessProcessByName",
                   ErrorCategory.InvalidOperation,
                   name));
                continue;
            }

<!-- p.1751 -->

                    WriteObject(processes, true);
                } // foreach (string name...
            } // else
        } // ProcessRecord

        #endregion Overrides
      } // End GetProcCommand class.

     #endregion GetProcCommand
 }

See Also
     Writing a Windows PowerShell Cmdlet

Last updated on 05/20/2025

<!-- p.1752 -->

GetProcessSample05 Sample
This sample shows a complete version of the Get-Proc cmdlet.

How to build the sample using Visual Studio.
  1. Open Windows Explorer and navigate to the GetProcessSample05 directory under the
     Samples directory.

     With the Windows PowerShell 2.0 SDK installed, navigate to the GetProcessSample05
     folder. The default location is C:\Program Files (x86)\Microsoft
     SDKs\Windows\v7.0\Samples\sysmgmt\WindowsPowerShell\csharp\GetProcessSample05 .

  2. Double-click the icon for the solution (.sln) file. This opens the sample project in Visual
     Studio.

  3. In the Build menu, select Build Solution to build the library for the sample in the default
     \bin or \bin\debug folders.

How to run the sample
  1. Create the following module folder:

     [user]\Documents\WindowsPowerShell\Modules\GetProcessSample05

  2. Copy the sample assembly to the module folder.

  3. Start Windows PowerShell.

  4. Run the following command to load the assembly into Windows PowerShell:

     Import-Module getprossessample05

  5. Run the following command to run the cmdlet:

     Get-Proc

Requirements
This sample requires Windows PowerShell 2.0.

<!-- p.1753 -->

Demonstrates
This sample demonstrates the following.

      Declaring a cmdlet class using the Cmdlet attribute.

      Declaring a cmdlet parameter using the Parameter attribute.

      Specifying positions for parameters.

      Specifying that parameters can take input from the pipeline. The input can be taken from
      an object or a value from a property of an object whose property name is the same as the
      parameter name.

      Declaring a validation attribute for the parameter input.

      Handling errors and exceptions.

      Writing debug messages.

Example
This sample shows how to create a cmdlet that displays a list of specified processes.

 C#

 namespace Microsoft.Samples.PowerShell.Commands
 {
     using System;
     using System.Collections.Generic;
     using System.Diagnostics;
     using System.Management.Automation;    // Windows PowerShell namespace.
     using System.Security.Permissions;
     using Win32Exception = System.ComponentModel.Win32Exception;
     #region GetProcCommand

        /// <summary>
      /// This class implements the Get-Proc cmdlet.
      /// </summary>
      [Cmdlet(VerbsCommon.Get, "Proc",
          DefaultParameterSetName = "ProcessName")]
      public class GetProcCommand : PSCmdlet
      {
           #region Fields
           /// <summary>
           /// The names of the processes to act on.
           /// </summary>
           private string[] processNames;

<!-- p.1754 -->

 /// <summary>
 /// The identifiers of the processes to act on.
 /// </summary>
 private int[] processIds;

 /// <summary>
 /// The process objects to act on.
 /// </summary>
 private Process[] inputObjects;

 #endregion Fields

 #region Parameters

/// <summary>
/// Gets or sets the list of process names on
/// which the Get-Proc cmdlet will work.
/// </summary>
[Parameter(
   Position = 0,
   ParameterSetName = "ProcessName",
   ValueFromPipeline = true,
   ValueFromPipelineByPropertyName = true)]
[ValidateNotNullOrEmpty]
public string[] Name
{
   get { return this.processNames; }
   set { this.processNames = value; }
}

/// <summary>
/// Gets or sets the list of process identifiers on
/// which the Get-Proc cmdlet will work.
/// </summary>
[Parameter(
   ParameterSetName = "Id",
   Mandatory = true,
   ValueFromPipeline = true,
   ValueFromPipelineByPropertyName = true,
   HelpMessage = "The unique id of the process to get.")]
public int[] Id
{
   get { return this.processIds; }
   set { this.processIds = value; }
}

/// <summary>
/// Gets or sets Process objects directly. If the input is a
/// stream of [collection of] Process objects, the cmdlet bypasses the
/// ProcessName and Id parameters and reads the Process objects
/// directly. This allows the cmdlet to deal with processes that have
/// wildcard characters in their name.
/// <value>Process objects</value>
/// </summary>

<!-- p.1755 -->

[Parameter(
   ParameterSetName = "InputObject",
   Mandatory = true,
   ValueFromPipeline = true)]
public Process[] Input
{
   get { return this.inputObjects; }
   set { this.inputObjects = value; }
}

#endregion Parameters

#region Cmdlet Overrides

/// <summary>
/// The ProcessRecord method calls the Process.GetProcesses
/// method to retrieve the processes. Then, the WriteObject
/// method writes the associated processes to the pipeline.
/// </summary>
protected override void ProcessRecord()
{
   List<Process> matchingProcesses;

   WriteDebug("Obtaining the list of matching process objects.");

   switch (ParameterSetName)
   {
      case "Id":
         matchingProcesses = this.GetMatchingProcessesById();
         break;
      case "ProcessName":
         matchingProcesses = this.GetMatchingProcessesByName();
         break;
      case "InputObject":
         matchingProcesses = this.GetProcessesByInput();
         break;
      default:
         ThrowTerminatingError(
             new ErrorRecord(
                 new ArgumentException("Bad ParameterSetName"),
                 "UnableToAccessProcessList",
                 ErrorCategory.InvalidOperation,
                 null));
         return;
   } // switch (ParameterSetName)

   WriteDebug("Outputting the matching process objects.");

   matchingProcesses.Sort(ProcessComparison);

   foreach (Process process in matchingProcesses)
   {
      WriteObject(process);
   }
} // ProcessRecord

<!-- p.1756 -->

#endregion Overrides

#region protected Methods and Data

/// <summary>
/// Retrieves the list of all processes matching the ProcessName
/// parameter and generates a non-terminating error for each
/// specified process name which is not found even though the name
/// contains no wildcards.
/// </summary>
/// <returns>The matching processes.</returns>
[EnvironmentPermissionAttribute(
   SecurityAction.LinkDemand,
   Unrestricted = true)]
private List<Process> GetMatchingProcessesByName()
{
   new EnvironmentPermission(
      PermissionState.Unrestricted).Assert();

   List<Process> allProcesses =
      new List<Process>(Process.GetProcesses());

   // The keys dictionary is used for rapid lookup of
   // processes that are already in the matchingProcesses list.
   Dictionary<int, byte> keys = new Dictionary<int, byte>();

   List<Process> matchingProcesses = new List<Process>();

   if (null == this.processNames)
   {
        matchingProcesses.AddRange(allProcesses);
   }
   else
   {
        foreach (string pattern in this.processNames)
        {
            WriteVerbose("Finding matches for process name \""
               + pattern + "\".");

           // WildCard search on the available processes
           WildcardPattern wildcard =
              new WildcardPattern(
                  pattern,
                  WildcardOptions.IgnoreCase);

           bool found = false;

           foreach (Process process in allProcesses)
           {
               if (!keys.ContainsKey(process.Id))
               {
                   string processName = SafeGetProcessName(process);

                   // Remove the process from the allProcesses list

<!-- p.1757 -->

                   // so that it is not tested again.
                   if (processName.Length == 0)
                   {
                       allProcesses.Remove(process);
                   }

                   // Perform a wildcard search on this particular
                   // process name and check whether it matches the
                   // pattern specified.
                   if (!wildcard.IsMatch(processName))
                   {
                       continue;
                   }

                   WriteDebug("Found matching process id "
                      + process.Id + ".");

                   // A match is found.
                   found = true;

                   // Store the process identifier so that the same process
                   // is not added twice.
                   keys.Add(process.Id, 0);

                   // Add the process to the processes list.
                   matchingProcesses.Add(process);
               }
           } // foreach (Process...

           if (!found &&
             !WildcardPattern.ContainsWildcardCharacters(pattern))
           {
               WriteError(new ErrorRecord(
                  new ArgumentException("Cannot find process name "
                     + "\"" + pattern + "\"."),
                  "ProcessNameNotFound",
                  ErrorCategory.ObjectNotFound,
                  pattern));
           }
       } // foreach (string...
   } // if (null...

   return matchingProcesses;
} // GetMatchingProcessesByName

/// <summary>
/// Returns the name of a process. If an error occurs, a blank
/// string is returned.
/// </summary>
/// <param name="process">The process whose name is
/// returned.</param>
/// <returns>The name of the process.</returns>
[EnvironmentPermissionAttribute(
   SecurityAction.LinkDemand, Unrestricted = true)]
protected static string SafeGetProcessName(Process process)

<!-- p.1758 -->

{
    new EnvironmentPermission(PermissionState.Unrestricted).Assert();
    string name = String.Empty;

    if (process != null)
    {
       try
       {
           return process.ProcessName;
       }
       catch (Win32Exception)
       {
       }
       catch (InvalidOperationException)
       {
       }
    }

    return name;
} // SafeGetProcessName

#endregion Cmdlet Overrides

#region Private Methods

/// <summary>
/// Function to sort by process name first, and then by
/// the process identifier.
/// </summary>
/// <param name="x">First process object.</param>
/// <param name="y">Second process object.</param>
/// <returns>
/// Returns less than zero if x is less than y,
/// greater than 0 if x is greater than y, and 0 if x == y.
/// </returns>
private static int ProcessComparison(Process x, Process y)
{
   int diff = String.Compare(
      SafeGetProcessName(x),
      SafeGetProcessName(y),
      StringComparison.CurrentCultureIgnoreCase);

    if (0 != diff)
    {
         return diff;
    }
    else
    {
         return x.Id.CompareTo(y.Id);
    }
}

/// <summary>
/// Retrieves the list of all processes matching the Id
/// parameter and generates a non-terminating error for

<!-- p.1759 -->

/// each specified process identifier which is not found.
/// </summary>
/// <returns>
/// An array of processes that match the given identifier.
/// </returns>
[EnvironmentPermissionAttribute(
   SecurityAction.LinkDemand,
   Unrestricted = true)]
private List<Process> GetMatchingProcessesById()
{
   new EnvironmentPermission(
      PermissionState.Unrestricted).Assert();

   List<Process> matchingProcesses = new List<Process>();

   if (null != this.processIds)
   {
      // The keys dictionary is used for rapid lookup of the
      // processes already in the matchingProcesses list.
      Dictionary<int, byte> keys = new Dictionary<int, byte>();

       foreach (int processId in this.processIds)
       {
          WriteVerbose("Finding match for process id "
             + processId + ".");

           if (!keys.ContainsKey(processId))
           {
              Process process;
              try
              {
                   process = Process.GetProcessById(processId);
              }
              catch (ArgumentException ex)
              {
                  WriteError(new ErrorRecord(
                     ex,
                     "ProcessIdNotFound",
                     ErrorCategory.ObjectNotFound,
                     processId));
                  continue;
              }

               WriteDebug("Found matching process.");

               matchingProcesses.Add(process);
               keys.Add(processId, 0);
           }
       }
   }

   return matchingProcesses;
} // GetMatchingProcessesById

/// <summary>

<!-- p.1760 -->

      /// Retrieves the list of all processes matching the InputObject
      /// parameter.
      /// </summary>
      /// <returns>The matching processes.</returns>
      [EnvironmentPermissionAttribute(
         SecurityAction.LinkDemand,
         Unrestricted = true)]
      private List<Process> GetProcessesByInput()
      {
         new EnvironmentPermission(
            PermissionState.Unrestricted).Assert();

         List<Process> matchingProcesses = new List<Process>();

         if (null != this.Input)
         {
            // The keys dictionary is used for rapid lookup of the
            // processes already in the matchingProcesses list.
            Dictionary<int, byte> keys = new Dictionary<int, byte>();

             foreach (Process process in this.Input)
             {
                WriteVerbose("Refreshing process object.");

                 if (!keys.ContainsKey(process.Id))
                 {
                    try
                    {
                        process.Refresh();
                    }
                    catch (Win32Exception)
                    {
                    }
                    catch (InvalidOperationException)
                    {
                    }

                     matchingProcesses.Add(process);
                 }
             }
         }

         return matchingProcesses;
      } // GetProcessesByInput
      #endregion Private Methods
    } // End GetProcCommand class.

    #endregion GetProcCommand
}

See Also
    Writing a Windows PowerShell Cmdlet
