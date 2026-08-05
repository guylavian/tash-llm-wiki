---
title: "How to use this documentation — pages 1121-1160"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1121-1160
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1121-1160
family: powershell
documentKind: "doc"
abstract: "Creating the code To create a predictor, you must have the .NET 6 SDK installed for your platform. For more information on the SDK, see Download .NET 6.0 . Create a new PowerShell module project by following these steps: 1. Use the dotnet command-line tool to create a starter cl"
---

# How to use this documentation — pages 1121-1160

<!-- p.1121 -->

Creating the code
To create a predictor, you must have the .NET 6 SDK installed for your platform. For more
information on the SDK, see Download .NET 6.0 .

Create a new PowerShell module project by following these steps:

   1. Use the dotnet command-line tool to create a starter classlib project.

      PowerShell
      dotnet new classlib --name SamplePredictor

   2. Edit the SamplePredictor.csproj to contain the following information:

      XML

      <Project Sdk="Microsoft.NET.Sdk">

         <PropertyGroup>
           <TargetFramework>net6.0</TargetFramework>
         </PropertyGroup>

         <ItemGroup>
           <PackageReference Include="Microsoft.PowerShell.SDK" Version="7.2.0" />
         </ItemGroup>

<!-- p.1122 -->

   </Project>

3. Delete the default Class1.cs file created by dotnet and copy the following code to a
  SamplePredictorClass.cs file in your project folder.

   C#

   using System;
   using System.Collections.Generic;
   using System.Threading;
   using System.Management.Automation;
   using System.Management.Automation.Subsystem;
   using System.Management.Automation.Subsystem.Prediction;

   namespace PowerShell.Sample
   {
       public class SamplePredictor : ICommandPredictor
       {
           private readonly Guid _guid;

            internal SamplePredictor(string guid)
            {
                _guid = new Guid(guid);
            }

            /// <summary>
            /// Gets the unique identifier for a subsystem implementation.
            /// </summary>
            public Guid Id => _guid;

            /// <summary>
            /// Gets the name of a subsystem implementation.
            /// </summary>
            public string Name => "SamplePredictor";

            /// <summary>
            /// Gets the description of a subsystem implementation.
            /// </summary>
            public string Description => "A sample predictor";

           /// <summary>
           /// Get the predictive suggestions. It indicates the start of a
   suggestion rendering session.
           /// </summary>
           /// <param name="client">Represents the client that initiates the call.
   </param>
           /// <param name="context">The <see cref="PredictionContext"/> object to
   be used for prediction.</param>
           /// <param name="cancellationToken">The cancellation token to cancel
   the prediction.</param>
           /// <returns>An instance of <see cref="SuggestionPackage"/>.</returns>
           public SuggestionPackage GetSuggestion(PredictionClient client,

<!-- p.1123 -->

PredictionContext context, CancellationToken cancellationToken)
        {
            string input = context.InputAst.Extent.Text;
            if (string.IsNullOrWhiteSpace(input))
            {
                return default;
            }

            return new SuggestionPackage(new List<PredictiveSuggestion>{
                new PredictiveSuggestion(string.Concat(input, " HELLO WORLD"))
            });
       }

       #region "interface methods for processing feedback"

        /// <summary>
        /// Gets a value indicating whether the predictor accepts a specific
kind of feedback.
        /// </summary>
        /// <param name="client">Represents the client that initiates the call.
</param>
        /// <param name="feedback">A specific type of feedback.</param>
        /// <returns>True or false, to indicate whether the specific feedback
is accepted.</returns>
        public bool CanAcceptFeedback(PredictionClient client,
PredictorFeedbackKind feedback) => false;

        /// <summary>
        /// One or more suggestions provided by the predictor were displayed to
the user.
        /// </summary>
        /// <param name="client">Represents the client that initiates the call.
</param>
        /// <param name="session">The mini-session where the displayed
suggestions came from.</param>
        /// <param name="countOrIndex">
        /// When the value is greater than 0, it's the number of displayed
suggestions from the list
        /// returned in <paramref name="session"/>, starting from the index 0.
When the value is
        /// less than or equal to 0, it means a single suggestion from the list
got displayed, and
        /// the index is the absolute value.
        /// </param>
        public void OnSuggestionDisplayed(PredictionClient client, uint
session, int countOrIndex) { }

        /// <summary>
        /// The suggestion provided by the predictor was accepted.
        /// </summary>
        /// <param name="client">Represents the client that initiates the call.
</param>
        /// <param name="session">Represents the mini-session where the
accepted suggestion came from.</param>
        /// <param name="acceptedSuggestion">The accepted suggestion text.

<!-- p.1124 -->

</param>
        public void OnSuggestionAccepted(PredictionClient client, uint session,
string acceptedSuggestion) { }

        /// <summary>
        /// A command line was accepted to execute.
        /// The predictor can start processing early as needed with the latest
history.
        /// </summary>
        /// <param name="client">Represents the client that initiates the call.
</param>
        /// <param name="history">History command lines provided as references
for prediction.</param>
        public void OnCommandLineAccepted(PredictionClient client,
IReadOnlyList<string> history) { }

        /// <summary>
        /// A command line was done execution.
        /// </summary>
        /// <param name="client">Represents the client that initiates the call.
</param>
        /// <param name="commandLine">The last accepted command line.</param>
        /// <param name="success">Shows whether the execution was successful.
</param>
        public void OnCommandLineExecuted(PredictionClient client, string
commandLine, bool success) { }

        #endregion;
    }

    /// <summary>
    /// Register the predictor on module loading and unregister it on module
un-loading.
    /// </summary>
    public class Init : IModuleAssemblyInitializer, IModuleAssemblyCleanup
    {
        private const string Identifier = "843b51d0-55c8-4c1a-8116-
f0728d419306";

        /// <summary>
        /// Gets called when assembly is loaded.
        /// </summary>
        public void OnImport()
        {
            var predictor = new SamplePredictor(Identifier);
            SubsystemManager.RegisterSubsystem(SubsystemKind.CommandPredictor,
predictor);
        }

        /// <summary>
        /// Gets called when the binary module is unloaded.
        /// </summary>
        public void OnRemove(PSModuleInfo psModuleInfo)
        {

<!-- p.1125 -->

      SubsystemManager.UnregisterSubsystem(SubsystemKind.CommandPredictor, new
      Guid(Identifier));
              }
          }
      }

     The following example code returns the string "HELLO WORLD" for the prediction result
     for all user input. Since the sample predictor doesn't process any feedback, the code
     doesn't implement the feedback methods from the interface. Change the prediction and
     feedback code to meet the needs of your predictor.

       ７ Note

       The list view of PSReadLine doesn't support multiline suggestions. Each suggestion
       should be a single line. If your code has a multiline suggestion, you should split the
       lines into separate suggestions or join the lines with a semicolon ( ; ).

   4. Run dotnet build to produce the assembly. You can find the compiled assembly in the
     bin/Debug/net6.0 location of your project folder.

       ７ Note

       To ensure a responsive user experience, the ICommandPredictor interface has a 20ms
       time out for responses from the Predictors. Your predictor code must return results
       in less than 20ms to be displayed.

Using your predictor plugin
To try out your new predictor, open a new PowerShell 7.2 session and run the following
commands:

 PowerShell
 Set-PSReadLineOption -PredictionSource HistoryAndPlugin
 Import-Module .\bin\Debug\net6.0\SamplePredictor.dll

With the assembly is loaded in the session, you see the text "HELLO WORLD" appear as you
type in the terminal. You can press F2 to switch between the Inline view and the List view.

For more information about PSReadLine options, see Set-PSReadLineOption.

You can get a list of installed predictors, using the following command:

<!-- p.1126 -->

PowerShell
Get-PSSubsystem -Kind CommandPredictor

Output
Kind                    SubsystemType       IsRegistered Implementations
----                    -------------       ------------ ---------------
CommandPredictor        ICommandPredictor           True {SamplePredictor}

 ７ Note

  Get-PSSubsystem is an experimental cmdlet that was introduced in PowerShell 7.1 You

 must enable the PSSubsystemPluginModel experimental feature to use this cmdlet. For
 more information, see Using Experimental Features.

Last updated on 12/08/2025

<!-- p.1127 -->

How to create a feedback provider
PowerShell 7.4 introduced the concept of feedback providers. A feedback provider is a
PowerShell module that implements the IFeedbackProvider interface to provide command
suggestions based on user command execution attempts. The provider is triggered when
there's a success or failure execution. Feedback providers use information from the success or
failure to provide feedback.

Prerequisites
To create a feedback provider, you must satisfy the following prerequisites:

     Install PowerShell 7.4 or higher
        You must enable the PSFeedbackProvider experimental feature to enable support for
        feedback providers and predictors. For more information, see Using Experimental
        Features.
     Install .NET 8 SDK - 8.0.0 or higher
        See the Download .NET 8.0       page to get the latest version of the SDK.

Overview of a feedback provider
A feedback provider is a PowerShell binary module that implements the
System.Management.Automation.Subsystem.Feedback.IFeedbackProvider interface. This interface
declares the methods to get feedback based on the command line input. The feedback
interface can provide suggestions based on the success or failure of the command invoked by
the user. The suggestions can be anything that you want. For example, you might suggest ways
to address an error or better practices, like avoiding the use of aliases. For more information,
see the What are Feedback Providers?        blog post.

The following diagram shows the architecture of a feedback provider:

<!-- p.1128 -->

The following examples walk you through the process of creating a simple feedback provider.
Also, you can register the provider with the command predictor interface to add feedback
suggestions to the command-line predictor experience. For more information about predictors,
see Using predictors in PSReadLine and How to create a command line predictor.

Step 1 - Create a new class library project
Use the following command to create a new project in the project directory:

 PowerShell
 dotnet new classlib --name MyFeedbackProvider

Add a package reference for the System.Management.Automation package to your .csproj file.
The following example shows the updated .csproj file:

 XML

 <Project Sdk="Microsoft.NET.Sdk">

   <PropertyGroup>

<!-- p.1129 -->

       <TargetFramework>net8.0</TargetFramework>
       <ImplicitUsings>enable</ImplicitUsings>
       <Nullable>enable</Nullable>
     </PropertyGroup>

   <ItemGroup>
     <PackageReference Include="System.Management.Automation" Version="7.4.0-
 preview.3">
         <ExcludeAssets>contentFiles</ExcludeAssets>
         <PrivateAssets>All</PrivateAssets>
     </PackageReference>
   </ItemGroup>
 </Project>

  ７ Note

  You should change the version of the System.Management.Automation assembly to match
  the version of the PowerShell preview that you are targeting. The minimum version is
  7.4.0-preview.3.

Step 2 - Add the class definition for your provider
Change the name of the Class1.cs file to match the name of your provider. This example uses
myFeedbackProvider.cs . This file contains the two main classes that define the feedback

provider. The following example shows the basic template for the class definitions.

 C#
 using System.Management.Automation;
 using System.Management.Automation.Subsystem;
 using System.Management.Automation.Subsystem.Feedback;
 using System.Management.Automation.Subsystem.Prediction;
 using System.Management.Automation.Language;

 namespace myFeedbackProvider;

 public sealed class myFeedbackProvider : IFeedbackProvider, ICommandPredictor
 {

 }

 public class Init : IModuleAssemblyInitializer, IModuleAssemblyCleanup
 {

 }

<!-- p.1130 -->

Step 3 - Implement the Init class
The Init class registers and unregisters the feedback provider with the subsystem manager.
The OnImport() method runs when the binary module is being loaded. The OnRemove() method
runs when the binary module is being removed. This example registers both the feedback
provider and command predictor subsystem.

 C#

 public class Init : IModuleAssemblyInitializer, IModuleAssemblyCleanup
 {
     private const string Id = "<ADD YOUR GUID HERE>";

     public void OnImport()
     {
         var feedback = new myFeedbackProvider(Id);
         SubsystemManager.RegisterSubsystem(SubsystemKind.FeedbackProvider,
 feedback);
         SubsystemManager.RegisterSubsystem(SubsystemKind.CommandPredictor,
 feedback);
     }

      public void OnRemove(PSModuleInfo psModuleInfo)
      {
          SubsystemManager.UnregisterSubsystem<ICommandPredictor>(new Guid(Id));
          SubsystemManager.UnregisterSubsystem<IFeedbackProvider>(new Guid(Id));
      }
 }

Replace the <ADD YOUR GUID HERE> placeholder value with a unique Guid. You can generate a
Guid using the New-Guid cmdlet.

 PowerShell

 New-Guid

The Guid is a unique identifier for your provider. The provider must have a unique Id to be
registered with the subsystem.

Step 4 - Add class members and define the
constructor
The following code implements the properties defined in the interfaces, adds needed class
members, and creates the constructor for the myFeedbackProvider class.

<!-- p.1131 -->

C#

/// <summary>
/// Gets the global unique identifier for the subsystem implementation.
/// </summary>
private readonly Guid _guid;
public Guid Id => _guid;

/// <summary>
/// Gets the name of a subsystem implementation, this will be the name displayed
when triggered
/// </summary>
public string Name => "myFeedbackProvider";

/// <summary>
/// Gets the description of a subsystem implementation.
/// </summary>
public string Description => "This is very simple feedback provider";

/// <summary>
/// Default implementation. No function is required for a feedback provider.
/// </summary>
Dictionary<string, string>? ISubsystem.FunctionsToDefine => null;

/// <summary>
/// Gets the types of trigger for this feedback provider.
/// </summary>
/// <remarks>
/// The default implementation triggers a feedback provider by <see
cref="FeedbackTrigger.CommandNotFound"/> only.
/// </remarks>
public FeedbackTrigger Trigger => FeedbackTrigger.All;

/// <summary>
/// List of candidates from the feedback provider to be passed as predictor results
/// </summary>
private List<string>? _candidates;

/// <summary>
/// PowerShell session used to run PowerShell commands that help create suggestions.
/// </summary>
private PowerShell _powershell;

internal myFeedbackProvider(string guid)
{
    _guid = new Guid(guid); // Save guid
    _powershell = PowerShell.Create(); // Create PowerShell instance
}

Step 5 - Create the GetFeedback() method

<!-- p.1132 -->

The GetFeedback method takes two parameters, context and token . The context parameter
receives the information about the trigger so you can decide how to respond with suggestions.
The token parameter is used for cancellation. This function returns a FeedbackItem containing
the suggestion.

 C#
 /// <summary>
 /// Gets feedback based on the given commandline and error record.
 /// </summary>
 /// <param name="context">The context for the feedback call.</param>
 /// <param name="token">The cancellation token to cancel the operation.</param>
 /// <returns>The feedback item.</returns>
 public FeedbackItem? GetFeedback(FeedbackContext context, CancellationToken token)
 {
     // Target describes the different kinds of triggers to activate on,
     var target = context.Trigger;
     var commandLine = context.CommandLine;
     var ast = context.CommandLineAst;

      // defining the header and footer variables
      string header;
      string footer;

      // List of the actions
      List<string>? actions = new List<string>();

      // Trigger on success code goes here

      // Trigger on error code goes here

      return null;
 }

The following image shows how these fields are used in the suggestions that are displayed to
the user.

Create suggestions for a Success trigger
For a successful invocation, we want to expand any aliases used in the last execution. Using the
CommandLineAst , we identify any aliased commands and create a suggestion to use the fully

<!-- p.1133 -->

qualified command name instead.

 C#
 // Trigger on success
 if (target == FeedbackTrigger.Success)
 {
     // Getting the commands from the AST and only finding those that are Commands
     var astCmds = ast.FindAll((cAst) => cAst is CommandAst, true);

      // Inspect each of the commands
      foreach(var command in astCmds)
      {

          // Get the command name
          var aliasedCmd = ((CommandAst) command).GetCommandName();

          // Check if its an alias or not, if so then add it to the list of actions
          if(TryGetAlias(aliasedCmd, out string commandString))
          {
              actions.Add($"{aliasedCmd} --> {commandString}");
          }
      }

      // If no alias was found return null
      if(actions.Count == 0)
      {
          return null;
      }

     // If aliases are found, set the header to a description and return a new
 FeedbackItem.
     header = "You have used an aliased command:";
     // Copy actions to _candidates for the predictor
     _candidates = actions;

      return new FeedbackItem(header, actions);
 }

Implement the TryGetAlias() method
The TryGetAlias() method is a private helper function that returns a boolean value to indicate
whether the command is an alias. In the class constructor, we created a PowerShell instance
that we can use to run PowerShell commands. The TryGetAlias() method uses this PowerShell
instance to invoke the GetCommand method to determine if the command is an alias. The
AliasInfo object returned by GetCommand contains full name of the aliased command.

 C#

<!-- p.1134 -->

 /// <summary>
 /// Checks if a command is an alias.
 /// </summary>
 /// <param name="command">The command to check if alias</param>
 /// <param name="targetCommand">The referenced command by the aliased
 command</param>
 /// <returns>True if an alias and false if not</returns>
 private bool TryGetAlias(string command, out string targetCommand)
 {
     // Create PowerShell runspace as a session state proxy to run GetCommand and
 check
     // if its an alias
     AliasInfo? pwshAliasInfo =
         _powershell.Runspace.SessionStateProxy.InvokeCommand.GetCommand(command,
 CommandTypes.Alias) as AliasInfo;

      // if its null then it is not an aliased command so just return false
      if(pwshAliasInfo is null)
      {
          targetCommand = String.Empty;
          return false;
      }

      // Set targetCommand to referenced command name
      targetCommand = pwshAliasInfo.ReferencedCommand.Name;
      return true;
 }

Create suggestions for a Failure trigger
When a command execution fails, we want to suggest that the user Get-Help to get more
information about how to use the command.

 C#
 // Trigger on error
 if (target == FeedbackTrigger.Error)
 {
     // Gets the command that caused the error.
     var erroredCommand = context.LastError?.InvocationInfo.MyCommand;
     if (erroredCommand is null)
     {
         return null;
     }

     header = $"You have triggered an error with the command {erroredCommand}. Try
 using the following command to get help:";

     actions.Add($"Get-Help {erroredCommand}");
     footer = $"You can also check online documentation at
 https://learn.microsoft.com/en-us/powershell/module/?term={erroredCommand}";

<!-- p.1135 -->

     // Copy actions to _candidates for the predictor
     _candidates = actions;
     return new FeedbackItem(header, actions, footer,
 FeedbackDisplayLayout.Portrait);
 }

Step 6 - Send suggestions to the command line
predictor
Another way your feedback provider can enhance the user experience is to provide command
suggestions to the ICommandPredictor interface. For more information about creating a
command line predictor, see How to create a command line predictor.

The following code implements the methods necessary from the ICommandPredictor interface
to add predictor behavior to your feedback provider.

      CanAcceptFeedback() - This method returns a Boolean value that indicates whether the

      predictor accepts a specific type of feedback.
      GetSuggestion() - This method returns a SuggestionPackage object that contains the

      suggestions to be displayed by the predictor.
      OnCommandLineAccepted() - This method is called when a command line is accepted to

      execute.

 C#
 /// <summary>
 /// Gets a value indicating whether the predictor accepts a specific kind of
 feedback.
 /// </summary>
 /// <param name="client">Represents the client that initiates the call.</param>
 /// <param name="feedback">A specific type of feedback.</param>
 /// <returns>True or false, to indicate whether the specific feedback is accepted.
 </returns>
 public bool CanAcceptFeedback(PredictionClient client, PredictorFeedbackKind
 feedback)
 {
     return feedback switch
     {
         PredictorFeedbackKind.CommandLineAccepted => true,
         _ => false,
     };
 }

 /// <summary>
 /// Get the predictive suggestions. It indicates the start of a suggestion rendering
 session.

<!-- p.1136 -->

/// </summary>
/// <param name="client">Represents the client that initiates the call.</param>
/// <param name="context">The <see cref="PredictionContext"/> object to be used for
prediction.</param>
/// <param name="cancellationToken">The cancellation token to cancel the prediction.
</param>
/// <returns>An instance of <see cref="SuggestionPackage"/>.</returns>
public SuggestionPackage GetSuggestion(
    PredictionClient client,
    PredictionContext context,
    CancellationToken cancellationToken)
{
    if (_candidates is not null)
    {
        string input = context.InputAst.Extent.Text;
        List<PredictiveSuggestion>? result = null;

        foreach (string c in _candidates)
        {
            if (c.StartsWith(input, StringComparison.OrdinalIgnoreCase))
            {
                result ??= new List<PredictiveSuggestion>(_candidates.Count);
                result.Add(new PredictiveSuggestion(c));
            }
        }

        if (result is not null)
        {
            return new SuggestionPackage(result);
        }
    }

    return default;
}

/// <summary>
/// A command line was accepted to execute.
/// The predictor can start processing early as needed with the latest history.
/// </summary>
/// <param name="client">Represents the client that initiates the call.</param>
/// <param name="history">History command lines provided as references for
prediction.</param>
public void OnCommandLineAccepted(PredictionClient client, IReadOnlyList<string>
history)
{
    // Reset the candidate state once the command is accepted.
    _candidates = null;
}

Step 7 - Build the feedback provider

<!-- p.1137 -->

Now you are ready to build and begin using your feedback provider! To build the project, run
the following command:

 PowerShell
 dotnet build

This command create the PowerShell module as a DLL file in the following path of your project
folder: bin/Debug/net8.0/myFeedbackProvider

You may run into the error error NU1101: Unable to find package
System.Management.Automation. when building on Windows machines. To fix this add a
nuget.config file to your project directory and add the following:

 YAML
 <?xml version="1.0" encoding="utf-8"?>
 <configuration>
   <packageSources>
     <clear />
     <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
   </packageSources>
   <disabledPackageSources>
     <clear />
   </disabledPackageSources>
 </configuration>

Using a feedback provider
To test your new feedback provider, import the compiled module into your PowerShell session.
This can be done by importing the folder described after building has succeeded:

 PowerShell
 Import-Module ./bin/Debug/net8.0/myFeedbackProvider

Once you're satisfied with your module, you should create a module manifest, publish it to the
PowerShell Gallery, and install it in your $Env:PSModulePath . For more information, see How to
create a module manifest. You can add the Import-Module command to your $PROFILE script so
the module is available in PowerShell session.

You can get a list of installed feedback providers, using the following command:

 PowerShell

<!-- p.1138 -->

 Get-PSSubsystem -Kind FeedbackProvider

 Output
 Kind               SubsystemType        IsRegistered Implementations
 ----               -------------        ------------ ---------------
 FeedbackProvider   IFeedbackProvider            True {general}

  ７ Note

  Get-PSSubsystem is an experimental cmdlet that was introduced in PowerShell 7.1 You

  must enable the PSSubsystemPluginModel experimental feature to use this cmdlet. For
  more information, see Using Experimental Features.

The following screenshot shows some example suggestions from the new provider.

The following is a GIF showing how the predictor integration works from the new provider.

<!-- p.1139 -->

Other feedback providers
We have created other feedback provider that can be used as a good reference for deeper
examples.

command-not-found
The command-not-found feedback provider utilizes the command-not-found utility tool on Linux
systems to provide suggestions when native commands are attempted to run but are missing.
You can find the code in the GitHub Repository   or can download for yourself on the
PowerShell Gallery    .

PowerShell Adapter
The Microsoft.PowerShell.PowerShellAdapter is a feedback provider that helps you convert
text outputs from native commands into PowerShell objects. It detects "adapters" on your
system and suggests you to use them when you use the native command. You can learn more
about PowerShell Adapters from, PowerShell Adapter Feedback Provider      blog post. You can
also find the code in the GitHub Repository   or can download for yourself on the PowerShell
Gallery   .

Appendix - Full implementation code
The following code combines the previous examples into the find full implementation of the
provider class.

 C#

 using System.Management.Automation;
 using System.Management.Automation.Subsystem;
 using System.Management.Automation.Subsystem.Feedback;
 using System.Management.Automation.Subsystem.Prediction;
 using System.Management.Automation.Language;

 namespace myFeedbackProvider;

 public sealed class myFeedbackProvider : IFeedbackProvider, ICommandPredictor
 {
     /// <summary>
     /// Gets the global unique identifier for the subsystem implementation.
     /// </summary>
     private readonly Guid _guid;
     public Guid Id => _guid;

      /// <summary>

<!-- p.1140 -->

    /// Gets the name of a subsystem implementation, this will be the name displayed
when triggered
    /// </summary>
    public string Name => "myFeedbackProvider";

    /// <summary>
    /// Gets the description of a subsystem implementation.
    /// </summary>
    public string Description => "This is very simple feedback provider";

    /// <summary>
    /// Default implementation. No function is required for a feedback provider.
    /// </summary>
    Dictionary<string, string>? ISubsystem.FunctionsToDefine => null;

    /// <summary>
    /// Gets the types of trigger for this feedback provider.
    /// </summary>
    /// <remarks>
    /// The default implementation triggers a feedback provider by <see
cref="FeedbackTrigger.CommandNotFound"/> only.
    /// </remarks>
    public FeedbackTrigger Trigger => FeedbackTrigger.All;

    /// <summary>
    /// List of candidates from the feedback provider to be passed as predictor
results
    /// </summary>
    private List<string>? _candidates;

    /// <summary>
    /// PowerShell session used to run PowerShell commands that help create
suggestions.
    /// </summary>
    private PowerShell _powershell;

    // Constructor
    internal myFeedbackProvider(string guid)
    {
        _guid = new Guid(guid); // Save guid
        _powershell = PowerShell.Create(); // Create PowerShell instance
    }

    #region IFeedbackProvider
    /// <summary>
    /// Gets feedback based on the given commandline and error record.
    /// </summary>
    /// <param name="context">The context for the feedback call.</param>
    /// <param name="token">The cancellation token to cancel the operation.</param>
    /// <returns>The feedback item.</returns>
    public FeedbackItem? GetFeedback(FeedbackContext context, CancellationToken
token)
    {
        // Target describes the different kinds of triggers to activate on,
        var target = context.Trigger;

<!-- p.1141 -->

          var commandLine = context.CommandLine;
          var ast = context.CommandLineAst;

          // defining the header and footer variables
          string header;
          string footer;

          // List of the actions
          List<string>? actions = new List<string>();

        // Trigger on success
        if (target == FeedbackTrigger.Success)
        {
            // Getting the commands from the AST and only finding those that are
Commands
            var astCmds = ast.FindAll((cAst) => cAst is CommandAst, true);

              // Inspect each of the commands
              foreach(var command in astCmds)
              {

                  // Get the command name
                  var aliasedCmd = ((CommandAst) command).GetCommandName();

                  // Check if its an alias or not, if so then add it to the list of
actions
                  if(TryGetAlias(aliasedCmd, out string commandString))
                  {
                      actions.Add($"{aliasedCmd} --> {commandString}");
                  }
              }

              // If no alias was found return null
              if(actions.Count == 0)
              {
                  return null;
              }

            // If aliases are found, set the header to a description and return a
new FeedbackItem.
            header = "You have used an aliased command:";
            // Copy actions to _candidates for the predictor
            _candidates = actions;

              return new FeedbackItem(header, actions);
          }

          // Trigger on error
          if (target == FeedbackTrigger.Error)
          {
              // Gets the command that caused the error.
              var erroredCommand = context.LastError?.InvocationInfo.MyCommand;
              if (erroredCommand is null)
              {
                  return null;

<!-- p.1142 -->

            }

            header = $"You have triggered an error with the command
{erroredCommand}. Try using the following command to get help:";

            actions.Add($"Get-Help {erroredCommand}");
            footer = $"You can also check online documentation at
https://learn.microsoft.com/en-us/powershell/module/?term={erroredCommand}";

            // Copy actions to _candidates for the predictor
            _candidates = actions;
            return new FeedbackItem(header, actions, footer,
FeedbackDisplayLayout.Portrait);
        }
        return null;
    }

    /// <summary>
    /// Checks if a command is an alias.
    /// </summary>
    /// <param name="command">The command to check if alias</param>
    /// <param name="targetCommand">The referenced command by the aliased
command</param>
    /// <returns>True if an alias and false if not</returns>
    private bool TryGetAlias(string command, out string targetCommand)
    {
        // Create PowerShell runspace as a session state proxy to run GetCommand and
check
        // if its an alias
        AliasInfo? pwshAliasInfo =
            _powershell.Runspace.SessionStateProxy.InvokeCommand.GetCommand(command,
CommandTypes.Alias) as AliasInfo;

       // if its null then it is not an aliased command so just return false
       if(pwshAliasInfo is null)
       {
           targetCommand = String.Empty;
           return false;
       }

       // Set targetCommand to referenced command name
       targetCommand = pwshAliasInfo.ReferencedCommand.Name;
       return true;
    }
    #endregion IFeedbackProvider

    #region ICommandPredictor

    /// <summary>
    /// Gets a value indicating whether the predictor accepts a specific kind of
feedback.
    /// </summary>
    /// <param name="client">Represents the client that initiates the call.</param>
    /// <param name="feedback">A specific type of feedback.</param>
    /// <returns>True or false, to indicate whether the specific feedback is

<!-- p.1143 -->

accepted.</returns>
    public bool CanAcceptFeedback(PredictionClient client, PredictorFeedbackKind
feedback)
    {
        return feedback switch
        {
            PredictorFeedbackKind.CommandLineAccepted => true,
            _ => false,
        };
    }

    /// <summary>
    /// Get the predictive suggestions. It indicates the start of a suggestion
rendering session.
    /// </summary>
    /// <param name="client">Represents the client that initiates the call.</param>
    /// <param name="context">The <see cref="PredictionContext"/> object to be used
for prediction.</param>
    /// <param name="cancellationToken">The cancellation token to cancel the
prediction.</param>
    /// <returns>An instance of <see cref="SuggestionPackage"/>.</returns>
    public SuggestionPackage GetSuggestion(
        PredictionClient client,
        PredictionContext context,
        CancellationToken cancellationToken)
    {
        if (_candidates is not null)
        {
            string input = context.InputAst.Extent.Text;
            List<PredictiveSuggestion>? result = null;

            foreach (string c in _candidates)
            {
                if (c.StartsWith(input, StringComparison.OrdinalIgnoreCase))
                {
                    result ??= new List<PredictiveSuggestion>(_candidates.Count);
                    result.Add(new PredictiveSuggestion(c));
                }
            }

            if (result is not null)
            {
                return new SuggestionPackage(result);
            }
        }

        return default;
    }

    /// <summary>
    /// A command line was accepted to execute.
    /// The predictor can start processing early as needed with the latest history.
    /// </summary>
    /// <param name="client">Represents the client that initiates the call.</param>
    /// <param name="history">History command lines provided as references for

<!-- p.1144 -->

prediction.</param>
    public void OnCommandLineAccepted(PredictionClient client, IReadOnlyList<string>
history)
    {
        // Reset the candidate state once the command is accepted.
        _candidates = null;
    }

     #endregion;
}

public class Init : IModuleAssemblyInitializer, IModuleAssemblyCleanup
{
    private const string Id = "<ADD YOUR GUID HERE>";

    public void OnImport()
    {
        var feedback = new myFeedbackProvider(Id);
        SubsystemManager.RegisterSubsystem(SubsystemKind.FeedbackProvider,
feedback);
        SubsystemManager.RegisterSubsystem(SubsystemKind.CommandPredictor,
feedback);
    }

     public void OnRemove(PSModuleInfo psModuleInfo)
     {
         SubsystemManager.UnregisterSubsystem<ICommandPredictor>(new Guid(Id));
         SubsystemManager.UnregisterSubsystem<IFeedbackProvider>(new Guid(Id));
     }
}

Last updated on 12/08/2025

<!-- p.1145 -->

PlatyPS overview
10/09/2025

PlatyPS is the primary tool for creating the PowerShell help displayed using Get-Help .
PowerShell help files are written in Microsoft Assistance Markup Language      (MAML) format.
MAML defines an XML schema for the structure of help files.

There are two major versions of PlatyPS.

     Microsoft.PowerShell.PlatyPS v1.0.1 is the supported version of PlatyPS. This version is a
     complete rewrite in C# leveraging markdig       for parsing Markdown. This release includes
     several improvements:
        Provides a more accurate description of a PowerShell cmdlet and its parameters
        Increased performance - processes 1000s of Markdown files in seconds
        Creates an object model of the help file that you can manipulate in memory
        Provides cmdlets that you can chain together to perform complex operations
        Defines a new Markdown schema that includes all elements needed for Get-Help , plus
        information that was previously unavailable.
        Provide automatic conversion of existing Markdown (using the old schema) to new
        objects, enabling you to export to new Markdown, YAML, or MAML.
     platyPS v0.14.2 is the original implementation of PlatyPS. This version is no longer
     supported.

Benefits of using PlatyPS
Prior to PlatyPS, the help files were hand written with limited help from existing tools and
editors. PlatyPS simplifies the process by allowing you to write the help files in Markdown and
then convert it to MAML.

Markdown      is easy to learn, widely used in the open source community, and supported by
many editors including Visual Studio Code . Markdown is also easy to convert to other
formats such as HTML and PDF. You can use these Markdown files to create MAML help files
and to create HTML pages for a website.

Get started with PlatyPS
Before getting started with PlatyPS, you should understand the types of help supported by
PowerShell. For more information, see Types of help in PowerShell.

Creating help files with PlatyPS is a four-step process:

<!-- p.1146 -->

1. Create new or update existing Markdown help files.
2. Edit the Markdown help files to add descriptions and examples.
3. Test the Markdown help files to ensure they render correctly.
4. Convert and publish the help files.

<!-- p.1147 -->

Windows PowerShell Language
Specification 3.0
Article • 01/08/2025

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December
  2012 and is based on Windows PowerShell 3.0. This specification does not reflect
  the current state of PowerShell. There is no plan to update this documentation to
  reflect the current state. This documentation is presented here for historical
  reference.

  The specification document is available as a Microsoft Word document from the
  Microsoft Download Center at:
  https://www.microsoft.com/download/details.aspx?id=36389                That Word
  document has been converted for presentation here on Microsoft Learn. During
  conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

1. Introduction
PowerShell is a command-line shell and scripting language, designed especially for
system administrators.

Most shells operate by executing a command or utility in a new process, and presenting
the results to the user as text. These shells also have commands that are built into the
shell and run in the shell process. Because there are few built-in commands, many
utilities have been created to supplement them. PowerShell is very different. Instead of
processing text, the shell processes objects. PowerShell also includes a large set of built-
in commands with each having a consistent interface and these can work with user-
written commands.

An object is a data entity that has properties (i.e., characteristics) and methods (i.e.,
actions that can be performed on the object). All objects of the same type have the
same base set of properties and methods, but each instance of an object can have
different property values.

<!-- p.1148 -->

A major advantage of using objects is that it is much easier to pipeline commands; that
is, to write the output of one command to another command as input. (In a traditional
command-line environment, the text output from one command needs to be
manipulated to meet the input format of another.)

PowerShell includes a very rich scripting language that supports constructs for looping,
conditions, flow-control, and variable assignment. This language has syntax features and
keywords similar to those used in the C# programming language (§C.).

There are four kinds of commands in PowerShell: scripts, functions and methods,
cmdlets, and native commands.

     A file of commands is called a script. By convention, a script has a filename
     extension of .ps1. The top-most level of a PowerShell program is a script, which, in
     turn, can invoke other commands.

     PowerShell supports modular programming via named procedures. A procedure
     written in PowerShell is called a function, while an external procedure made
     available by the execution environment (and typically written in some other
     language) is called a method.

     A cmdlet (pronounced "command-let") is a simple, single-task command-line tool.
     Although a cmdlet can be used on its own, the full power of cmdlets is realized
     when they are used in combination to perform complex tasks.

     A native command is part of the host environment.

Each time the PowerShell runtime environment begins execution, it begins what is called
a session. Commands then execute within the context of that session.

This specification defines the PowerShell language, the built-in cmdlets, and the use of
objects via the pipeline.

Unlike most shells, which accept and return text, Windows PowerShell is built on top of
the .NET Framework common language runtime (CLR) and the .NET Framework, and
accepts and returns .NET Framework objects.

<!-- p.1149 -->

2. Lexical Structure

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

2.1 Grammars
This specification shows the syntax of the PowerShell language using two grammars. The lexical
grammar (§B.1) shows how Unicode characters are combined to form line terminators,
comments, white space, and tokens. The syntactic grammar (§B.2) shows how the tokens
resulting from the lexical grammar are combined to form PowerShell scripts.

For convenience, fragments of these grammars are replicated in appropriate places throughout
this specification.

Any use of the characters 'a' through 'z' in the grammars is case insensitive. This means that
letter case in variables, aliases, function names, keywords, statements, and operators is ignored.
However, throughout this specification, such names are written in lowercase, except for some
automatic and preference variables.

2.2 Lexical analysis
2.2.1 Scripts

<!-- p.1150 -->

Syntax:

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is optional in
  the syntax.

  Syntax

  input:
      input-elements~opt~      signature-block~opt~

  input-elements:
      input-element
      input-elements      input-element

  input-element:
      whitespace
      comment
      token

  signature-block:
      signature-begin      signature      signature-end

  signature-begin:
      new-line-character      # SIG # Begin signature block        new-line-character

  signature:
      base64 encoded signature blob in multiple single-line-comments

  signature-end:
      new-line-character      # SIG # End signature block        new-line-character

Description:

The input source stream to a PowerShell translator is the input in a script, which contains a
sequence of Unicode characters. The lexical processing of this stream involves the reduction of
those characters into a sequence of tokens, which go on to become the input of syntactic
analysis.

A script is a group of PowerShell commands stored in a script-file. The script itself has no name,
per se, and takes its name from its source file. The end of that file indicates the end of the
script.

A script may optionally contain a digital signature. A host environment is not required to
process any text that follows a signature or anything that looks like a signature. The creation

<!-- p.1151 -->

and use of digital signatures are not covered by this specification.

2.2.2 Line terminators
Syntax:

 Syntax

 new-line-character:
     Carriage return character (U+000D)
     Line feed character (U+000A)
     Carriage return character (U+000D) followed by line feed character (U+000A)

 new-lines:
     new-line-character
     new-lines new-line-character

Description:

The presence of new-line-characters in the input source stream divides it into lines that can be
used for such things as error reporting and the detection of the end of a single-line comment.

A line terminator can be treated as white space (§2.2.4).

2.2.3 Comments
Syntax:

 Syntax

 comment:
     single-line-comment
     requires-comment
     delimited-comment

 single-line-comment:
     # input-characters~opt~

 input-characters:
     input-character
     input-characters input-character

 input-character:
     Any Unicode character except a new-line-character

 requires-comment:
     #Requires whitespace command-arguments

 dash:

<!-- p.1152 -->

         - (U+002D)
         EnDash character (U+2013)
         EmDash character (U+2014)
         Horizontal bar character (U+2015)

  dashdash:
      dash dash

  delimited-comment:
      < # delimited-comment-text~opt~ hashes >

  delimited-comment-text:
      delimited-comment-section
      delimited-comment-text delimited-comment-section

  delimited-comment-section:
      >
      hashes~opt~ not-greater-than-or-hash

  hashes:
      #
      hashes #

  not-greater-than-or-hash:
      Any Unicode character except > or #

Description:

Source code can be annotated by the use of comments.

A single-line-comment begins with the character # and ends with a new-line-character.

A delimited-comment begins with the character pair <# and ends with the character pair #> . It
can occur as part of a source line, as a whole source line, or it can span any number of source
lines.

A comment is treated as white space.

The productions above imply that

         Comments do not nest.
         The character sequences <# and #> have no special meaning in a single-line comment.
         The character # has no special meaning in a delimited comment.

The lexical grammar implies that comments cannot occur inside tokens.

(See §A for information about creating script files that contain special-valued comments that
are used to generate documentation from script files.)

<!-- p.1153 -->

A requires-comment specifies the criteria that have to be met for its containing script to be
allowed to run. The primary criterion is the version of PowerShell being used to run the script.
The minimum version requirement is specified as follows:

#Requires -Version N[.n]

Where N is the (required) major version and n is the (optional) minor version.

A requires-comment can be present in any script file; however, it cannot be present inside a
function or cmdlet. It must be the first item on a source line. A script can contain multiple
requires-comments.

A character sequence is only recognized as a comment if that sequence begins with # or <# .
For example, hello#there is considered a single token whereas hello #there is considered the
token hello followed by a single-line comment. As well as following white space, the comment
start sequence can also be preceded by any expression-terminating or statement-terminating
character (such as ) , } , ] , ' , " , or ; ).

A requires-comment cannot be present inside a snap-in.

There are four other forms of a requires-comment:

  Syntax

  #Requires -Assembly AssemblyId
  #Requires -Module ModuleName
  #Requires -PSSnapin PSSnapin [ -Version *N* [.n] ]
  #Requires -ShellId ShellId

2.2.4 White space
Syntax:

  Syntax

  whitespace:
      Any character with Unicode class Zs, Zl, or Zp
      Horizontal tab character (U+0009)
      Vertical tab character (U+000B)
      Form feed character (U+000C)
      ` (The backtick character U+0060) followed by new-line-character

Description:

<!-- p.1154 -->

White space consists of any sequence of one or more whitespace characters.

Except for the fact that white space may act as a separator for tokens, it is ignored.

Unlike some popular languages, PowerShell does not consider line-terminator characters
(§2.2.2) to be white space. However, a line terminator can be treated as white space by
preceding it immediately by a backtick character, ` (U+0060). This is necessary when the
contents of a line are complete syntactically, yet the following line contains tokens intended to
be associated with the previous line. For example,

 PowerShell

 $number = 10 # assigns 10 to $number; nothing is written to the pipeline
 + 20 # writes 20 to the pipeline
 - 50 # writes -50 to the pipeline
 $number # writes $number's value, 10, to the pipeline

In this example, the backtick indicates the source line is continued. The following expression is
equivalent to $number = 10 + 20 - 50 .

 PowerShell

 $number = 10 `
 + 20 `
 - 50
 $number # writes $number's value to the pipeline
 -20

2.3 Tokens
Syntax:

 Syntax

 token:
     keyword
     variable
     command
     command-parameter
     command-argument-token
     integer-literal
     real-literal
     string-literal
     type-literal
     operator-or-punctuator

<!-- p.1155 -->

Description:

A token is the smallest lexical element within the PowerShell language.

Tokens can be separated by new-lines, comments, white space, or any combination thereof.

2.3.1 Keywords
Syntax:

 Syntax

 keyword: one of
     begin             break            catch        class
     continue          data             define       do
     dynamicparam      else             elseif       end
     exit              filter           finally      for
     foreach           from             function     if
     in                inlinescript     parallel     param
     process           return           switch       throw
     trap              try              until        using
     var               while            workflow

Description:

A keyword is a sequence of characters that has a special meaning when used in a context-
dependent place. Most often, this is as the first token in a statement; however, there are other
locations, as indicated by the grammar. (A token that looks like a keyword, but is not being
used in a keyword context, is a command-name or a command-argument.)

The keywords class , define , from , using , and var are reserved for future use.

  ７ Note

  Editor's Note: The class and using keywords were introduced in PowerShell 5.0. See
  about_Classes and about_Using.

2.3.2 Variables
Syntax:

 Syntax

<!-- p.1156 -->

 variable:
     $$
     $?
     $^
     $   variable-scope~opt~        variable-characters
     @   variable-scope~opt~        variable-characters
     braced-variable

 braced-variable:
     ${   variable-scope~opt~         braced-variable-characters       }

 variable-scope:
     Global:
     Local:
     Private:
     Script:
     Using:
     Workflow:
     variable-namespace

 variable-namespace:
     variable-characters        :

 variable-characters:
     variable-character
     variable-characters        variable-character

 variable-character:
     A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nd
     _   (The underscore character U+005F)
     ?

 braced-variable-characters:
     braced-variable-character
     braced-variable-characters         braced-variable-character

 braced-variable-character:
     Any Unicode character except
         }   (The closing curly brace character U+007D)
         `   (The backtick character U+0060)
     escaped-character

 escaped-character:
     `   (The backtick character U+0060) followed by any Unicode character

Description:

Variables are discussed in detail in (§5). The variable $? is discussed in §2.3.2.2. Scopes are
discussed in §3.5.

<!-- p.1157 -->

The variables $$ and $^ are reserved for use in an interactive environment, which is outside
the scope of this specification.

There are two ways of writing a variable name: A braced variable name, which begins with $ ,
followed by a curly bracket-delimited set of one or more almost-arbitrary characters; and an
ordinary variable name, which also begins with $ , followed by a set of one or more characters
from a more restrictive set than a braced variable name allows. Every ordinary variable name
can be expressed using a corresponding braced variable name.

  PowerShell

  $totalCost
  $Maximum_Count_26

  $végösszeg # Hungarian
  $итог # Russian
  $総計 # Japanese (Kanji)

  ${Maximum_Count_26}
  ${Name with`twhite space and `{punctuation`}}
  ${E:\\File.txt}

There is no limit on the length of a variable name, all characters in a variable name are
significant, and letter case is not distinct.

There are several different kinds of variables: user-defined (§2.3.2.1), automatic (§2.3.2.2), and
preference (§2.3.2.3). They can all coexist in the same scope (§3.5).

Consider the following function definition and calls:

  PowerShell

  function Get-Power ([long]$Base, [int]$Exponent) { ... }

  Get-Power 5 3 # $Base is 5, $Exponent is 3
  Get-Power -Exponent 3 -Base 5 # " " "

Each argument is passed by position or name, one at a time. However, a set of arguments can
be passed as a group with expansion into individual arguments being handled by the runtime
environment. This automatic argument expansion is known as splatting. For example,

  PowerShell

  $values = 5,3 # put arguments into an array
  Get-Power @values

<!-- p.1158 -->

 $hash = @{ Exponent = 3; Base = 5 } # put arguments into a Hashtable
 Get-Power @hash

 function Get-Power2 { Get-Power @args } # arguments are in an array

 Get-Power2 -Exponent 3 -Base 5 # named arguments splatted named in
 @args
 Get-Power2 5 3 # position arguments splatted positionally in @args

This is achieved by using @ instead of $ as the first character of the variable being passed. This
notation can only be used in an argument to a command.

Names are partitioned into various namespaces each of which is stored on a virtual drive (§3.1).
For example, variables are stored on Variable: , environment variables are stored on Env: ,
functions are stored on Function: , and aliases are stored on Alias: . All of these names can be
accessed as variables using the variable-namespace production within variable-scope. For
example,

 PowerShell

 function F { "Hello from F" }
 $Function:F # invokes function F

 Set-Alias A F
 $Alias:A # invokes function F via A

 $Count = 10
 $Variable:Count # accesses variable Count
 $Env:PATH # accesses environment variable PATH

Any use of a variable name with an explicit Variable: namespace is equivalent to the use of
that same variable name without that qualification. For example, $v and $Variable:v are
interchangeable.

As well as being defined in the language, variables can also be defined by the cmdlet New-
Variable.

2.3.2.1 User-defined variables

Any variable name allowed by the grammar but not used by automatic or preference variables
is available for user-defined variables.

User-defined variables are created and managed by user-defined script.

2.3.2.2 Automatic variables

<!-- p.1159 -->

Automatic variables store state information about the PowerShell environment. Their values
can be read in user-written script but not written.

  ７ Note

  The table originally found in this document was removed to reduce duplication. For a
  complete list of automatic variables, see about_Automatic_Variables.

2.3.2.3 Preference variables

Preference variables store user preferences for the session. They are created and initialized by
the PowerShell runtime environment. Their values can be read and written in user-written
script.

  ７ Note

  The table originally found in this document was removed to reduce duplication. For a
  complete list of preference variables, see about_Preference_Variables.

2.3.3 Commands
Syntax:

  Syntax

  generic-token:
      generic-token-parts

  generic-token-parts:
      generic-token-part
      generic-token-parts generic-token-part

  generic-token-part:
      expandable-string-literal
      verbatim-here-string-literal
      variable
      generic-token-char

  generic-token-char:
      Any Unicode character except
          {   }   (   )   ;   ,   |   &   $
          ` (The backtick character U+0060)
          double-quote-character
          single-quote-character

<!-- p.1160 -->

          whitespace
          new-line-character
          escaped-character

 generic-token-with-subexpr-start:
     generic-token-parts $(

2.3.4 Parameters
Syntax:

 Syntax

 command-parameter:
     dash first-parameter-char parameter-chars colon~opt~

 first-parameter-char:
     A Unicode character of classes Lu, Ll, Lt, Lm, or Lo
     _ (The underscore character U+005F)
     ?

 parameter-chars:
     parameter-char
     parameter-chars parameter-char

 parameter-char:
     Any Unicode character except
         { } ( ) ; , \| & . [
         colon
         whitespace
         new-line-character

 colon:
     : (The colon character U+003A)

 verbatim-command-argument-chars:
     verbatim-command-argument-part
     verbatim-command-argument-chars verbatim-command-argument-part

 verbatim-command-argument-part:
     verbatim-command-string
     & non-ampersand-character
     Any Unicode character except
         |
         new-line-character

 non-ampersand-character:
     Any Unicode character except &

 verbatim-command-string:
     double-quote-character non-double-quote-chars
     double-quote-character
