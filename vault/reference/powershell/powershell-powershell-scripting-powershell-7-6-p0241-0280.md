---
title: "How to use this documentation — pages 241-280"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0241-0280
family: powershell
documentKind: "doc"
abstract: "PSReadLine defaults to InlineView . You can switch between InlineView and ListView by pressing the F2 key. You can also use the PredictionViewStyle parameter of Set- PSReadLineOption to change the view. Managing Predictive IntelliSense To use Predictive IntelliSense, you must ha"
---

# How to use this documentation — pages 241-280

<!-- p.241 -->

PSReadLine defaults to InlineView . You can switch between InlineView and ListView by
pressing the F2 key. You can also use the PredictionViewStyle parameter of Set-
PSReadLineOption to change the view.

Managing Predictive IntelliSense
To use Predictive IntelliSense, you must have a newer version of PSReadLine installed. For best
results, install the latest version of the module.

Install PSReadLine using the Microsoft.PowerShell.PSResourceGet     module:

 PowerShell

 Install-PSResource -Name PSReadLine

PSReadLine can be installed in Windows PowerShell 5.1 or in PowerShell 7 or higher. To use
predictor plug-ins, you must be running in PowerShell 7.2 or higher. Windows PowerShell 5.1
can use the history-based predictor.

In PSReadLine 2.2.6, Predictive IntelliSense is enabled by default depending on the following
conditions:

     If Virtual Terminal (VT) is supported and PSReadLine running in PowerShell 7.2 or higher,
     PredictionSource is set to HistoryAndPlugin
     If VT is supported and PSReadLine running in PowerShell older than 7.2,
     PredictionSource is set to History
     If VT isn't supported, PredictionSource is set to None .

Use the following command to see the current setting:

 PowerShell

 Get-PSReadLineOption | Select-Object -Property PredictionSource

You can change the prediction source using the Set-PSReadLineOption cmdlet with the
PredictionSource parameter. The PredictionSource can be set to:

      None

      History

      Plugin

      HistoryAndPlugin

<!-- p.242 -->

  ７ Note

  History-based predictions come from the history maintained by PSReadLine. That history
  is more comprehensive than the session-based history you can see using Get-History . For
  more information, see Command history section of about_PSReadLine.

Setting the prediction color
By default, predictions appear in light grey text on the same line the user is typing. To support
accessibility needs, you can customize the prediction color. Colors are defined using ANSI
escape sequences. You can use $PSStyle to compose ANSI escape sequences.

 PowerShell

 Set-PSReadLineOption -Colors @{ InlinePrediction = $PSStyle.Background.Blue }

Or you can create your own. The default light-grey prediction text color can be restored using
the following ANSI escape sequence.

 PowerShell

 Set-PSReadLineOption -Colors @{ InlinePrediction = "`e[38;5;238m" }

For more information about setting prediction color and other PSReadLine settings, see Set-
PSReadLineOption.

Changing keybindings
PSReadLine contains functions to navigate and accept predictions. For example:

     AcceptSuggestion - Accept the current inline suggestion

     AcceptNextSuggestionWord - Accept the next word of the inline suggestion

     AcceptSuggestion is built within ForwardChar , which is bound to RightArrow by default

     AcceptNextSuggestionWord is built within the function ForwardWord , which can be bound

     to Ctrl + f

You can use the Set-PSReadLineKeyHandler cmdlet to change key bindings.

 PowerShell

<!-- p.243 -->

 Set-PSReadLineKeyHandler -Chord "Ctrl+f" -Function ForwardWord

With this binding, pressing Ctrl + f accepts the next word of an inline suggestion when the
cursor is at the end of current editing line. You can bind other keys to AcceptSuggestion and
AcceptNextSuggestionWord for similar functionalities. For example, you might want to make

RightArrow   accept the next word of the inline suggestion, instead of the whole suggestion line.

 PowerShell

 Set-PSReadLineKeyHandler -Chord "RightArrow" -Function ForwardWord

Using other predictor plug-ins
The Az.Tools.Predictor module was the first plug-in for Predictive IntelliSense. It uses Machine
Learning to predict what Azure PowerShell command you want to run and the parameters you
want to use. For more information and installation instructions, see Announcing General
Availability of Az.Tools.Predictor   .

The CompletionPredictor module adds an IntelliSense experience for anything that can be tab-
completed in PowerShell. With PSReadLine set to InlineView , you get the normal tab
completion experience. When you switch to ListView , you get the IntelliSense experience. You
can install the CompletionPredictor      module from the PowerShell Gallery.

<!-- p.244 -->

As previously noted, ListView shows you the source of the prediction. If you have multiple
plug-ins installed, the predictions are grouped by source with History listed first followed by
each plug-in in the order that they were loaded.

Creating your own predictor module
You can write your own predictor using C# to create a compiled PowerShell module. The
module must implement the
System.Management.Automation.Subsystem.Prediction.ICommandPredictor interface. This
interface declares the methods used to query for prediction results and provide feedback.

For more information, see How to create a command-line predictor.

 Last updated on 04/07/2026

<!-- p.245 -->

Using dynamic help
Dynamic Help provides just-in-time help that allows you to stay focused on your work without
losing your place typing on the command line.

Getting cmdlet help
Dynamic Help provides a view of full cmdlet help shown in an alternative screen buffer.
PSReadLine maps the function ShowCommandHelp to the F1 key.

     When the cursor is at the end of a fully expanded cmdlet name, pressing F1 displays the
     help for that cmdlet.
     When the cursor is at the end of a fully expanded parameter name, pressing F1 displays
     the help for the cmdlet beginning at the parameter.

The pager in PSReadLine allows you to scroll the displayed help using the up and down arrow
keys. Pressing Q exits the alternative screen buffer and returns to the current cursor position
on the command line on the primary screen.

Getting focused parameter help
Pressing Alt + h provides dynamic help for parameters. The help is shown below the current
command line similar to MenuComplete. The cursor must be at the end of the fully expanded
parameter name when you press the Alt + h key.

<!-- p.246 -->

Select arguments on the command line
To quickly select and edit the arguments of a cmdlet without disturbing your syntax, use Alt +
a . It searches from the current cursor position and stops when it finds an argument on the

command line. It selects the full argument, making it simple to replace or edit the argument.

Choosing keybindings
Not all keybindings work for all operating systems and terminal applications. For example,
keybindings for the Alt key don't work on macOS by default. On Linux, Ctrl + [ is the same
as Escape . And Ctrl + Spacebar generates a Control + 2 key sequence instead of the Control +
Spacebar   sequence expected.

To work around these quirks, map the PSReadLine function to an available key combination.
For example:

 PowerShell

<!-- p.247 -->

 Set-PSReadLineKeyHandler -Chord 'Ctrl+l' -Function ShowParameterHelp
 Set-PSReadLineKeyHandler -Chord 'Ctrl+k' -Function SelectCommandArgument

For more information about keybindings and workarounds, see Using PSReadLine key handlers.

Last updated on 11/21/2025

<!-- p.248 -->

Using aliases
An alias is an alternate name or shorthand name for a cmdlet or for a command element, such
as a function, script, file, or executable file. You can run the command using the alias instead of
the executable name.

Managing command aliases
PowerShell provides cmdlets for managing command aliases. The following command shows
the cmdlets that manage aliases.

 PowerShell

 Get-Command -Noun Alias

 Output

 CommandType Name         Version Source
 ----------- ----         ------- ------
 Cmdlet      Export-Alias 7.0.0.0 Microsoft.PowerShell.Utility
 Cmdlet      Get-Alias    7.0.0.0 Microsoft.PowerShell.Utility
 Cmdlet      Import-Alias 7.0.0.0 Microsoft.PowerShell.Utility
 Cmdlet      New-Alias    7.0.0.0 Microsoft.PowerShell.Utility
 Cmdlet      Remove-Alias 7.0.0.0 Microsoft.PowerShell.Utility
 Cmdlet      Set-Alias    7.0.0.0 Microsoft.PowerShell.Utility

For more information, see about_Aliases.

Use the Get-Alias cmdlet to list the aliases available in your environment. To list the aliases for a
single cmdlet, use the Definition parameter and specify the executable name.

 PowerShell

 Get-Alias -Definition Get-ChildItem

 Output
 CommandType        Name
 -----------        ----
 Alias              dir -> Get-ChildItem
 Alias              gci -> Get-ChildItem
 Alias              ls -> Get-ChildItem

To get the definition of a single alias, use the Name parameter.

<!-- p.249 -->

 PowerShell

 Get-Alias -Name gci

 Output
 CommandType          Name
 -----------          ----
 Alias                gci -> Get-ChildItem

To create an alias, use the Set-Alias command. You can create aliases for cmdlets, functions,
scripts, and native executables files.

 PowerShell

 Set-Alias -Name np -Value Notepad.exe
 Set-Alias -Name cmpo -Value Compare-Object

Compatibility aliases in Windows
PowerShell has several aliases that allow Unix and cmd.exe users to use familiar commands in
Windows. The following table shows common commands, the related PowerShell cmdlet, and
the PowerShell alias:

                                                                                    ﾉ   Expand table

 Windows Command Shell        Unix command   PowerShell cmdlet    PowerShell alias

 cd , chdir                    cd             Set-Location        sl , cd , chdir

 cls                           clear          Clear-Host          cls clear

 copy                          cp             Copy-Item           cpi , cp , copy

 del , erase , rd , rmdir      rm             Remove-Item         ri , del , erase , rd , rm , rmdir

 dir                           ls             Get-ChildItem       gci , dir , ls

 echo                          echo           Write-Output        write echo

 md                            mkdir          New-Item            ni

 move                          mv             Move-Item           mi , move , mv

 popd                          popd           Pop-Location        popd

                               pwd            Get-Location        gl , pwd , $PWD

<!-- p.250 -->

 Windows Command Shell         Unix command      PowerShell cmdlet      PowerShell alias

 pushd                         pushd              Push-Location         pushd

 ren                           mv                 Rename-Item           rni , ren

 type                          cat                Get-Content           gc , cat , type

  ７ Note

  The aliases in this table are Windows-specific. Some aliases aren't available on other
  platforms to allow an existing native command to work in a PowerShell session. For
  example, ls isn't defined as a PowerShell alias on macOS or Linux so that PowerShell runs
  the native command instead of Get-ChildItem .

Creating alternate names for commands with
parameters
You can assign an alias to a cmdlet, script, function, or executable file. Unlike some Unix shells,
the definition of the alias can't include parameters. For example, you can assign an alias to the
Get-Eventlog cmdlet, but you can't assign an alias to the Get-Eventlog -LogName System

command. You must create a function that contains the command with parameters.

For more information, see about_Aliases.

Parameter aliases and shorthand names
PowerShell also provides ways to create shorthand names for parameters. Parameter aliases are
defined using the Alias attribute when you declare the parameter. Parameter aliases can't be
defined using the *-Alias cmdlets.

For more information, see the Alias attribute documentation.

In addition to parameter aliases, PowerShell lets you specify the parameter name using the
fewest characters needed to uniquely identify the parameter. For example, the Get-ChildItem
cmdlet has the Filter and Force parameters. Using -F is ambiguous because both parameters
start with the letter F . If you try to use -F , PowerShell returns an error:

 PowerShell

 PS> Get-ChildItem -f

<!-- p.251 -->

 Output

 Get-ChildItem : Parameter cannot be processed because the parameter name 'f' is
 ambiguous. Possible
 matches include: -Filter -Force.

To uniquely identify the Filter parameter, you need to use -Fi .

  ７ Note

  The Get-ChildItem cmdlet also has a dynamic parameter, -File . Using -f , -fi and -fil
  doesn't create ambiguity with -File because -File is a dynamic FileSystem provider
  parameter. PowerShell binds dynamic parameters after binding static parameters. The only
  way to specify the parameter is to use the full name, -File .

Don't use aliases in scripts
Aliases are a convenience feature to be used interactively in the shell. You should always use
the full command and parameter names in your scripts.

      You can delete or redefine aliases in a profile script
      Aliases you define in your profile aren't be available to other users
      Aliases make your code harder to read and maintain

 Last updated on 01/13/2026

<!-- p.252 -->

Customizing your shell environment
A PowerShell profile is a script that runs when PowerShell starts. You can use the profile to
customize the environment. You can:

     Add aliases, functions, and variables
     Load modules
     Create PowerShell drives
     Run arbitrary commands
     Change preference settings

Putting these settings in your profile ensures that they're available whenever you start
PowerShell on your system.

  ７ Note

  To run scripts in Windows, the PowerShell execution policy needs to be set to
  RemoteSigned at a minimum. Execution policies don't apply to macOS and Linux. For more

  information, see about_Execution_Policy.

The $PROFILE variable
The $PROFILE automatic variable stores the paths to the PowerShell profiles that are available
in the current session.

There are four possible profiles available to support different user scopes and different
PowerShell hosts. The fully qualified paths for each profile script are stored in the following
member properties of $PROFILE .

     AllUsersAllHosts
     AllUsersCurrentHost
     CurrentUserAllHosts
     CurrentUserCurrentHost

You can create profile scripts that run for all users or just one user, the CurrentUser.
CurrentUser profiles are stored under the user's home directory path. The location varies
depending on the operating system and the version of PowerShell you use.

By default, referencing the $PROFILE variable returns the path to the "Current User, Current
Host" profile. The other profiles path can be accessed through the properties of the $PROFILE
variable. The following command shows the default profile locations on Windows.

<!-- p.253 -->

 PowerShell
 PS> $PROFILE | Select-Object *
 AllUsersAllHosts       : C:\Program Files\PowerShell\7\profile.ps1
 AllUsersCurrentHost    : C:\Program
 Files\PowerShell\7\Microsoft.PowerShell_profile.ps1
 CurrentUserAllHosts    : C:\Users\username\Documents\PowerShell\profile.ps1
 CurrentUserCurrentHost :
 C:\Users\username\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
 Length                 : 69

The following command shows the default profile locations on Ubuntu Linux.

 PowerShell
 $PROFILE | Select-Object *

 AllUsersAllHosts       : /opt/microsoft/powershell/7/profile.ps1
 AllUsersCurrentHost    :
 /opt/microsoft/powershell/7/Microsoft.PowerShell_profile.ps1
 CurrentUserAllHosts    : /home/username/.config/powershell/profile.ps1
 CurrentUserCurrentHost :
 /home/username/.config/powershell/Microsoft.PowerShell_profile.ps1
 Length                 : 67

There are also profiles that run for all PowerShell hosts or specific hosts. The profile script for
each PowerShell host has a name unique for that host. For example, the filename for the
standard Console Host on Windows or the default terminal application on other platforms is
Microsoft.PowerShell_profile.ps1 . For Visual Studio Code (VS Code), the filename is
Microsoft.VSCode_profile.ps1 .

For more information, see about_Profiles.

How to create your personal profile
When you first install PowerShell on a system, the profile script files and the directories they
belong to don't exist. The following command creates the "Current User, Current Host" profile
script file if it doesn't exist.

 PowerShell

 if (!(Test-Path -Path $PROFILE)) {
   New-Item -ItemType File -Path $PROFILE -Force
 }

The Force parameter of New-Item cmdlet creates the necessary folders when they don't exist.
After you create the script file, you can use your favorite editor to customize your shell

<!-- p.254 -->

environment.

Adding customizations to your profile
The previous articles talked about using tab completion, command predictors, and aliases.
These articles showed the commands used to load the required modules, create custom
completers, define key bindings, and other settings. These customizations are the kind that you
want to have available in every PowerShell interactive session. The profile script is the place for
these settings.

The simplest way to edit your profile script is to open the file in your favorite code editor. For
example, the following command opens the profile in VS Code .

 PowerShell
 code $PROFILE

You could also use notepad.exe on Windows, vi on Linux, or any other text editor.

The following profile script has examples for many of the customizations mentioned in the
previous articles. You can use any of these settings in your own profile.

 PowerShell
 ## Map PSDrives to other registry hives
 if (!(Test-Path HKCR:)) {
     $null = New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT
     $null = New-PSDrive -Name HKU -PSProvider Registry -Root HKEY_USERS
 }

 ## Customize the prompt
 function prompt {
     $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
     $principal = [Security.Principal.WindowsPrincipal] $identity
     $adminRole = [Security.Principal.WindowsBuiltInRole]::Administrator

      $prefix = if (Test-Path Variable:/PSDebugContext) { '[DBG]: ' } else { '' }
      if ($principal.IsInRole($adminRole)) {
          $prefix = "[ADMIN]:$prefix"
      }
      $body = 'PS ' + $PWD.path
      $suffix = $(if ($NestedPromptLevel -ge 1) { '>>' }) + '> '
      "${prefix}${body}${suffix}"
 }

 ## Create $PSStyle if running on a version older than 7.2
 ## - Add other ANSI color definitions as needed

<!-- p.255 -->

 if ($PSVersionTable.PSVersion.ToString() -lt '7.2.0') {
     # define escape char since "`e" may not be supported
     $esc = [char]0x1b
     $PSStyle = [pscustomobject]@{
         Foreground = @{
             Magenta = "${esc}[35m"
             BrightYellow = "${esc}[93m"
         }
         Background = @{
             BrightBlack = "${esc}[100m"
         }
     }
 }

 ## Set PSReadLine options and keybindings
 $PSROptions = @{
     ContinuationPrompt = ' '
     Colors             = @{
         Operator         = $PSStyle.Foreground.Magenta
         Parameter        = $PSStyle.Foreground.Magenta
         Selection        = $PSStyle.Background.BrightBlack
         InLinePrediction = $PSStyle.Foreground.BrightYellow +
 $PSStyle.Background.BrightBlack
     }
 }
 Set-PSReadLineOption @PSROptions
 Set-PSReadLineKeyHandler -Chord 'Ctrl+f' -Function ForwardWord
 Set-PSReadLineKeyHandler -Chord 'Enter' -Function ValidateAndAcceptLine

 ## Add argument completer for the dotnet CLI tool
 $scriptblock = {
     param($wordToComplete, $commandAst, $cursorPosition)
     dotnet complete --position $cursorPosition $commandAst.ToString() |
         ForEach-Object {
             [System.Management.Automation.CompletionResult]::new($_, $_,
 'ParameterValue', $_)
         }
 }
 Register-ArgumentCompleter -Native -CommandName dotnet -ScriptBlock $scriptblock

This profile script provides examples for the following customization:

     Adds two new PSDrives for the other root registry hives.
     Creates a customized prompt that changes if you're running in an elevated session.
     Configures PSReadLine and adds key binding. The color settings use the $PSStyle feature
     to define the ANSI color settings.
     Adds tab completion for the dotnet CLI tool. The tool provides parameters to help resolve
     the command-line arguments. The script block for Register-ArgumentCompleter uses that
     feature to provide the tab completion.

<!-- p.256 -->

Last updated on 11/21/2025

<!-- p.257 -->

Using PSReadLine key handlers
The PSReadLine module provides key handlers that map PSReadLine functions to keyboard
chords. Keyboard chords are a sequence of one or more keystrokes that are pressed at the
same time. For example, the chord Ctrl + Spacebar is the combination of the Ctrl and
Spacebar   keys pressed at the same time. A PSReadLine function is a predefined action that can
be performed on a command line. For example, the MenuComplete function allows you to
choose from a list of options from a menu complete the input on the command line.

PSReadLine has several predefined key handlers that are bound by default. You can also define
your own custom key handlers. Run the following command to list the key handlers that are
currently defined.

 PowerShell
 Get-PSReadLineKeyHandler

You can also get a list of all unbound PSReadLine functions that are available to be bound to a
key chord.

 PowerShell
 Get-PSReadLineKeyHandler -Unbound

You can use the Set-PSReadLineKeyHandler cmdlet to bind a function to a key handler. The
following command binds the MenuComplete function to the chord Ctrl + Spacebar .

 PowerShell
 Set-PSReadLineKeyHandler -Chord 'Ctrl+Spacebar' -Function MenuComplete

Finding key names and chord bindings
The names of the keys in the chord match the names in the [System.ConsoleKey] enumeration.
For more information, see System.ConsoleKey documentation. For example, the name of the 2
key in [System.ConsoleKey] is D2 , whereas the name of the 2 key on the numeric keypad is
NumPad2 . You can use the [System.Console]::ReadKey() method to find the name of the key

you pressed.

 PowerShell

 [System.Console]::ReadKey()

<!-- p.258 -->

The following output shows the information returned by the ReadKey() method for the Ctrl +
2   key chord.

 Output

 KeyChar Key Modifiers
 ------- --- ---------
         D2   Control

For the PSReadLine key handler cmdlets, this chord is represented as Ctrl+D2 . The following
example binds this chord to a function.

 PowerShell
 Set-PSReadLineKeyHandler -Chord 'Ctrl+D2' -Function MenuComplete

You can bind multiple cords to a single function. By default, the BackwardDeleteChar function is
bound to two chords.

 PowerShell

 Get-PSReadLineKeyHandler -Chord Backspace, Ctrl+h

 Output
 Key       Function           Description
 ---       --------           -----------
 Backspace BackwardDeleteChar Delete the character before the cursor
 Ctrl+h    BackwardDeleteChar Delete the character before the cursor

    ７ Note

    The Chord parameter is case-sensitive. Meaning, you can create different bindings for
    Ctrl + X   and Ctrl + x .

On Windows, you can also use the Alt + ? key chord to show the function bound to the next
key chord you enter. When you type Alt + ? , you see the following prompt:

 Output
 what-is-key:

When you hit the Backspace key, you get the following response:

<!-- p.259 -->

 Output

 Backspace: BackwardDeleteChar - Delete the character before the cursor

Key handlers on non-Windows computers
The key codes generated by your keyboard can be different depending on the operating
system and terminal application you're using.

macOS
The Macintosh keyboard doesn't have an Alt key like Windows and Linux systems. Instead, it
has the ⌥ Option key. macOS uses this key differently than the Alt key on other systems.
However, you can configure the terminal and iTerm2 applications on macOS to treat it as an
Alt   key.

Configuring the Terminal application
Open the Settings window from the App bar in Terminal.app. Select Profiles and choose the
profile you want to configure. Select the Keyboard tab of the configuration options. Below the
list of keys, select the Use Option as Meta Key setting. This setting allows the ⌥ Option key to
act as Alt in the Terminal application.

<!-- p.260 -->

Configuring the iTerm2 application

Open the Settings window from the App Bar in iTerm.app. Select Profiles and choose the
profile you want to configure. Select the Keys tab of the configuration options. Select the Esc+
option for both the Left Option Key and Right Option Key settings. This setting allows the
⌥ Option   key to act as Alt in the iTerm application.

<!-- p.261 -->

  ７ Note

  The exact steps vary depending on the versions of macOS and the terminal applications.
  These examples were captured on macOS Ventura 13.2.1 and iTerm2 v3.4.16.

Linux
On Linux platforms, the key code generated can be different than other systems. For example:

     Ctrl + [   is the same as Escape

     Ctrl + Spacebar   generates the key codes for Ctrl + D2 . If you want to map a function to
     Ctrl + Spacebar , you must use the chord Ctrl+D2 .

      PowerShell
      Set-PSReadLineKeyHandler -Chord 'Ctrl+D2' -Function MenuComplete

Use the ReadKey() method to verify the key codes generated by your keyboard.

Commonly used key handlers
Here are a few commonly used key handlers that are bound by default on Windows.
Keybindings can be different on non-Windows platforms.

<!-- p.262 -->

MenuComplete
Complete the input by selecting from a menu of possible completion values.

Default chord: Ctrl+Spacebar

The following example shows the menu of possible completions for commands beginning with
select .

 Output
 PS C:\> select<Ctrl+Spacebar>
 select                   Select-Object                 Select-PSFPropertyValue     Select-
 Xml
 Select-AzContext         Select-PSFConfig              Select-PSMDBuildProject
 Select-AzSubscription    Select-PSFObject              Select-String

 Select-Object

Use the arrow keys to select the completion you want. Press the Enter key to complete the
input. As you move through the selections, help for the selected command is displayed below
the menu.

ClearScreen
This function clears the screen similar to the cls or clear commands.

Default chord: Ctrl+l

SelectCommandArgument
Selects the next argument on the command line.

Default chord: Alt+a

You might have command in your history that you want to run again with different parameter
values. You can use the chord to cycle through each parameter and change the value as
needed.

New-AzVM -ResourceGroupName myRGName -Location eastus -Name myVM

Pressing Alt + a selects the next parameter argument in turn: myRGName , eastus , myVM .

GotoBrace

<!-- p.263 -->

Moves the cursor to the matching brace.

Default chord: Ctrl+]

The GotoBrace function moves your cursor to the closing brace that matches the brace at the
current cursor position on the command line. The function works for brackets ( [] ), braces ( {} ),
and parentheses ( () ).

DigitArgument
Start or accumulate a numeric argument that's used to repeat a keystroke the specified number
of times.

Default chord: Alt+0 through Alt+9

For example, typing Alt + 4 + # enters #### on the command line.

See also
      Get-PSReadLineKeyHandler
      Set-PSReadLineKeyHandler

 Last updated on 11/21/2025

<!-- p.264 -->

Configuring a light colored theme
The default colors for both PowerShell and PSReadLine are selected for a dark background
terminal. However, some users might choose to use a light background with dark text. Since
most of the default colors don't set the background, using light foreground colors on a light
background produces unreadable text.

Beginning in PowerShell 7.2, PowerShell adds colorized output to the default console
experience. The $PSStyle feature is not natively available in Windows PowerShell. However,
using the PSStyle   module from the PowerShell Gallery, you can set color values using these
same techniques described in this article.

The colors used are defined in the $PSStyle variable and are designed for a dark background.
You can change these colors to work better for a light background terminal.

PSReadLine allows you to define colors for 18 different syntax elements. You can view the
current settings using the Get-PSReadLineOption cmdlet.

 Output

 EditMode                               : Windows
 AddToHistoryHandler                    : System.Func`2[System.String,System.Object]
 HistoryNoDuplicates                    : True
 HistorySavePath                        :
 C:\Users\user1\AppData\Roaming\Microsoft\Wind...
 HistorySaveStyle                       : SaveIncrementally
 HistorySearchCaseSensitive             : False
 HistorySearchCursorMovesToEnd          : False
 MaximumHistoryCount                    : 4096
 ContinuationPrompt                     : >>
 ExtraPromptLineCount                   : 0
 PromptText                             : {> }
 BellStyle                              : Audible
 DingDuration                           : 50
 DingTone                               : 1221
 CommandsToValidateScriptBlockArguments : {ForEach-Object, %, Invoke-Command, icm...}
 CommandValidationHandler               :
 CompletionQueryItems                   : 100
 MaximumKillRingCount                   : 10
 ShowToolTips                           : True
 ViModeIndicator                        : None
 WordDelimiters                         : ;:,.[]{}()/\|^&*-=+'"-—―
 AnsiEscapeTimeout                      : 100
 PredictionSource                       : HistoryAndPlugin
 PredictionViewStyle                    : InlineView
 CommandColor                           : "`e[93m"
 CommentColor                           : "`e[32m"
 ContinuationPromptColor                : "`e[37m"
 DefaultTokenColor                      : "`e[37m"
 EmphasisColor                          : "`e[96m"

<!-- p.265 -->

 ErrorColor                                 : "`e[91m"
 InlinePredictionColor                      : "`e[38;5;238m"
 KeywordColor                               : "`e[92m"
 ListPredictionColor                        : "`e[33m"
 ListPredictionSelectedColor                : "`e[48;5;238m"
 MemberColor                                : "`e[97m"
 NumberColor                                : "`e[97m"
 OperatorColor                              : "`e[90m"
 ParameterColor                             : "`e[90m"
 SelectionColor                             : "`e[30;47m"
 StringColor                                : "`e[36m"
 TypeColor                                  : "`e[37m"
 VariableColor                              : "`e[92m"

The color settings are stored as strings containing ANSI escape sequences that change the
color in your terminal. Using the Set-PSReadLineOption cmdlet you can change the colors to
values that work better for a light-colored background.

Defining colors for a light theme
The PowerShell ISE can be configured to use a light theme for both the editor and console
panes. You can also view and change the colors that the ISE uses for various syntax and output
types. You can use these color choices to define a similar theme for PSReadLine.

The following hashtable defines colors for PSReadLine that mimic the colors in the PowerShell
ISE.

 PowerShell
 $ISETheme = @{
     Command                     = $PSStyle.Foreground.FromRGB(0x0000FF)
     Comment                     = $PSStyle.Foreground.FromRGB(0x006400)
     ContinuationPrompt          = $PSStyle.Foreground.FromRGB(0x0000FF)
     Default                     = $PSStyle.Foreground.FromRGB(0x0000FF)
     Emphasis                    = $PSStyle.Foreground.FromRGB(0x287BF0)
     Error                       = $PSStyle.Foreground.FromRGB(0xE50000)
     InlinePrediction            = $PSStyle.Foreground.FromRGB(0x93A1A1)
     Keyword                     = $PSStyle.Foreground.FromRGB(0x00008b)
     ListPrediction              = $PSStyle.Foreground.FromRGB(0x06DE00)
     Member                      = $PSStyle.Foreground.FromRGB(0x000000)
     Number                      = $PSStyle.Foreground.FromRGB(0x800080)
     Operator                    = $PSStyle.Foreground.FromRGB(0x757575)
     Parameter                   = $PSStyle.Foreground.FromRGB(0x000080)
     String                      = $PSStyle.Foreground.FromRGB(0x8b0000)
     Type                        = $PSStyle.Foreground.FromRGB(0x008080)
     Variable                    = $PSStyle.Foreground.FromRGB(0xff4500)
     ListPredictionSelected      = $PSStyle.Background.FromRGB(0x93A1A1)
     Selection                   = $PSStyle.Background.FromRGB(0x00BFFF)
 }

<!-- p.266 -->

  ７ Note

  You can use the FromRGB() method to create the ANSI escape sequences for the colors
  you want. For more information about $PSStyle , see about_ANSI_Terminals. For more
  information about ANSI escape sequences, see the ANSI escape code        article in
  Wikipedia.

Setting the color theme in your profile
To have the color settings you want in every PowerShell session, you must add the
configuration settings to your PowerShell profile script. For an example, see Customizing your
shell environment

Add the $ISETheme variable and the following Set-PSReadLineOption command to your profile.

 PowerShell

 Set-PSReadLineOption -Colors $ISETheme

The following settings work better for a light background terminal.

 PowerShell
 $PSStyle.Formatting.FormatAccent       = $PSStyle.Foreground.Green
 $PSStyle.Formatting.TableHeader        = $PSStyle.Foreground.Green
 $PSStyle.Formatting.ErrorAccent        = $PSStyle.Foreground.Cyan
 $PSStyle.Formatting.Error              = $PSStyle.Foreground.Red
 $PSStyle.Formatting.Warning            = $PSStyle.Foreground.Yellow
 $PSStyle.Formatting.Verbose            = $PSStyle.Foreground.Yellow
 $PSStyle.Formatting.Debug              = $PSStyle.Foreground.Yellow
 $PSStyle.Progress.Style                = $PSStyle.Foreground.Yellow
 $PSStyle.FileInfo.Directory            = $PSStyle.Background.FromRgb(0x2f6aff) +
                                          $PSStyle.Foreground.BrightWhite
 $PSStyle.FileInfo.SymbolicLink         = $PSStyle.Foreground.Cyan
 $PSStyle.FileInfo.Executable           = $PSStyle.Foreground.BrightMagenta
 $PSStyle.FileInfo.Extension['.ps1']    = $PSStyle.Foreground.Cyan
 $PSStyle.FileInfo.Extension['.ps1xml'] = $PSStyle.Foreground.Cyan
 $PSStyle.FileInfo.Extension['.psd1']   = $PSStyle.Foreground.Cyan
 $PSStyle.FileInfo.Extension['.psm1']   = $PSStyle.Foreground.Cyan

Choosing colors for accessibility
The ISE color theme might not work for users with color-blindness or other conditions that
limit their ability to see colors.

<!-- p.267 -->

The World Wide Web Consortium (W3C)           has recommendations for using colors for
accessibility. The Web Content Accessibility Guidelines (WCAG) 2.1 recommends that "visual
presentation of text and images of text has a contrast ratio of at least 4.5:1." For more
information, see Success Criterion 1.4.3 Contrast (Minimum)     .

The Contrast Ratio       website provides a tool that lets you pick foreground and background
colors and measure the contrast. You can use this tool to find color combinations that work
best for you.

 Last updated on 12/09/2025

<!-- p.268 -->

Improve the accessibility of output in
PowerShell
Most terminal environments only display raw text. Users that rely on screen readers are faced
with tedious narration when consuming large amounts of raw text because the raw output
doesn't have the accessibility metadata to characterize the format of the content.

There are two ways to improve the accessibility of the output in PowerShell:

     Output the data in a way that it can be viewed in another tool that supports screen
     reading technologies.
     Reduce the amount of output displayed in the terminal by filtering and selecting the data
     you want and output the text in a more readable format.

Display the data in a tool outside of the terminal
For large amounts of data, rather than output to the host, consider writing output in a format
that can be viewed in another tool that supports screen reading technologies. You might need
to save the data to a file in a format that can be opened in another application.

Out-GridView command on Windows
For small to moderate size output, use the Out-GridView command. The output is rendered
using Windows Presentation Foundation (WPF) in tabular form, much like a spreadsheet. The
GridView control allows you to sort, filter, and search the data, which reduces the amount of
data that needs to be read. The GridView control is also accessible to screen readers. The
Narrator tool built into Windows is able to read the GridView details, including column names
and row count.

The following example shows how to display a list of services in a GridView control.

 PowerShell
 Get-Service | Out-GridView

The Out-GridView command is only available in PowerShell on Windows.

Character Separated Value (CSV) format
Spreadsheet applications such as Microsoft Excel support CSV files. The following example
shows how to save the output of a command to a CSV file.

<!-- p.269 -->

 PowerShell
 Get-Service | Export-Csv -Path .\myFile.csv
 Invoke-Item .\myFile.csv

The Invoke-Item command opens the file in the default application for CSV files, which is
usually Microsoft Excel.

HyperText Markup Language (HTML) format
HTML files can be viewed by web browsers such as Microsoft Edge. The following example
shows how to save the output of a command to an HTML file.

 PowerShell
 Get-Service | ConvertTo-Html | Out-File .\myFile.html
 Invoke-Item .\myFile.html

The Invoke-Item command opens the file in your default web browser.

Reduce the amount of output
One way to improve the accessibility of the output is to reduce the amount of output displayed
in the terminal. PowerShell has several commands that can help you filter and select the data
you want.

Select and filter data
Rather than returning a large mount of data, use commands such as Select-Object , Sort-
Object , and Where-Object to reduce the amount of output. The following example gets the list

of services on the computer.

Each of the following commands improves the output in a different way:

     The -ErrorAction SilentlyContinue parameter suppresses error messages that might be
     generated if the user doesn't have permission to view some services.
     The Where-Object command reduces the number of items returned by filtering the list to
     only show services that are running and have event in the description.
     The Select-Object command selects only the service name and display name.
     The Format-List command displays the output in list format, which provides a better
     narration experience for screen readers.

<!-- p.270 -->

 PowerShell

 Get-Service -ErrorAction SilentlyContinue |
     Where-Object {$_.Status -eq 'Running' -and $_.Description -match 'event'} |
     Select-Object Name, DisplayName |
     Format-List

Reformat the output with calculated properties
The default property names of .NET objects output by PowerShell can be verbose and
confusing. You can use calculated properties to change the property names and values to
something easier to understood when read by a narrator technology.

The following example shows how to get the top five processes by memory usage and display
the process name and memory usage in megabytes.

 PowerShell
 Get-Process |
     Sort-Object WorkingSet -Descending |
     Select-Object -First 5 -Property ProcessName,
         @{n="MemoryMB"; e={'{0:N}' -f ($_.WorkingSet/1Mb)}} |
     Format-List

By default, Get-Process displays the WorkingSet as the number of bytes of memory used.
Without formatting, it can be difficult to understand the magnitude of the number. The
calculated property converts the number of bytes to megabytes and formats the number with
commas and limits the value to two decimal places.

 Output
 ProcessName : vmmemWSL
 MemoryMB    : 1,217.69

 ProcessName : Memory Compression
 MemoryMB    : 780.45

 ProcessName : Code
 MemoryMB    : 726.43

 ProcessName : OUTLOOK
 MemoryMB    : 460.16

 ProcessName : msedgewebview2
 MemoryMB    : 428.94

Additional reading

<!-- p.271 -->

     Out-GridView
     Export-Csv
     ConvertTo-Html
     about_Calculated_Properties

Last updated on 11/21/2025

<!-- p.272 -->

Deep dive articles
Article • 11/17/2022

The articles in this section are designed to be an in-depth look into PowerShell topics.
These articles don't replace the reference articles, but provide diverse examples,
illustrate edge cases, and warn about pitfalls and common mistakes.

This collection is also a showcase for community contributions. The inaugural set of
articles come from @KevinMarquette       and were originally published at
PowerShellExplained.com .

How to contribute content
If you're interested in contributing content to this collection, please read the Contributor
Guide    . When you are ready to propose a contribution, submit an issue in the GitHub
repository using the Document Idea template       and include a link to the existing
content you want to share.

<!-- p.273 -->

Everything you wanted to know about
arrays
Arrays are a fundamental language feature of most programming languages. They're a
collection of values or objects that are difficult to avoid. Let's take a close look at arrays and
everything they have to offer.

  ７ Note

  The original version     of this article appeared on the blog written by
  @KevinMarquette . The PowerShell team thanks Kevin for sharing this content with us.
  Please check out his blog at PowerShellExplained.com         .

What is an array?
I'm going to start with a basic technical description of what arrays are and how they are used
by most programming languages before I shift into the other ways PowerShell makes use of
them.

An array is a data structure that serves as a collection of multiple items. You can iterate over the
array or access individual items using an index. The array is created as a sequential chunk of
memory where each value is stored right next to the other.

I'll touch on each of those details as we go.

Basic usage
Because arrays are such a basic feature of PowerShell, there is a simple syntax for working with
them in PowerShell.

Create an array
An empty array can be created by using @()

 PowerShell

<!-- p.274 -->

 PS> $data = @()
 PS> $data.Count
 0

We can create an array and seed it with values just by placing them in the @() parentheses.

 PowerShell

 PS> $data = @('Zero','One','Two','Three')
 PS> $data.Count
 4

 PS> $data
 Zero
 One
 Two
 Three

This array has 4 items. When we call the $data variable, we see the list of our items. If it's an
array of strings, then we get one line per string.

We can declare an array on multiple lines. The comma is optional in this case and generally left
out.

 PowerShell

 $data = @(
     'Zero'
     'One'
     'Two'
     'Three'
 )

I prefer to declare my arrays on multiple lines like that. Not only does it get easier to read when
you have multiple items, it also makes it easier to compare to previous versions when using
source control.

Other syntax

It's commonly understood that @() is the syntax for creating an array, but comma-separated
lists work most of the time.

 PowerShell

 $data = 'Zero','One','Two','Three'

<!-- p.275 -->

Write-Output to create arrays

One cool little trick worth mentioning is that you can use Write-Output to quickly create strings
at the console.

  PowerShell

  $data = Write-Output Zero One Two Three

This is handy because you don't have to put quotes around the strings when the parameter
accepts strings. I would never do this in a script but it's fair game in the console.

Accessing items
Now that you have an array with items in it, you may want to access and update those items.

Offset

To access individual items, we use the brackets [] with an offset value starting at 0. This is how
we get the first item in our array:

  PowerShell

  PS> $data = 'Zero','One','Two','Three'
  PS> $data[0]
  Zero

The reason why we use zero here is because the first item is at the beginning of the list so we
use an offset of 0 items to get to it. To get to the second item, we would need to use an offset
of 1 to skip the first item.

  PowerShell

  PS> $data[1]
  One

This would mean that the last item is at offset 3.

  PowerShell

  PS> $data[3]
  Three

<!-- p.276 -->

Index

Now you can see why I picked the values that I did for this example. I introduced this as an
offset because that is what it really is, but this offset is more commonly referred to as an index.
An index that starts at 0 . For the rest of this article I will call the offset an index.

Special index tricks

In most languages, you can only specify a single number as the index and you get a single item
back. PowerShell is much more flexible. You can use multiple indexes at once. By providing a
list of indexes, we can select several items.

  PowerShell

  PS> $data[0,2,3]
  Zero
  Two
  Three

The items are returned based on the order of the indexes provided. If you duplicate an index,
you get that item both times.

  PowerShell

  PS> $data[3,0,3]
  Three
  Zero
  Three

We can specify a sequence of numbers with the built-in .. operator.

  PowerShell

  PS> $data[1..3]
  One
  Two
  Three

This works in reverse too.

  PowerShell

  PS> $data[3..1]
  Three

<!-- p.277 -->

  Two
  One

You can use negative index values to offset from the end. So if you need the last item in the
list, you can use -1 .

  PowerShell

  PS> $data[-1]
  Three

One word of caution here with the .. operator. The sequence 0..-1 and -1..0 evaluate to
the values 0,-1 and -1,0 . It's easy to see $data[0..-1] and think it would enumerate all items
if you forget this detail. $data[0..-1] gives you the same value as $data[0,-1] by giving you
the first and last item in the array (and none of the other values). Here is a larger example:

  PowerShell

  PS> $a = 1,2,3,4,5,6,7,8
  PS> $a[2..-1]
  3
  2
  1
  8

This is the same as:

  PowerShell

  PS> $a[2,1,0,-1]
  3
  2
  1
  8

Out of bounds

In most languages, if you try to access an index of an item that is past the end of the array, you
would get some type of error or an exception. PowerShell silently returns nothing.

  PowerShell

  PS> $null -eq $data[9000]
  True

<!-- p.278 -->

Cannot index into a null array

If your variable is $null and you try to index it like an array, you get a
System.Management.Automation.RuntimeException exception with the message Cannot index

into a null array .

  PowerShell

  PS> $empty = $null
  PS> $empty[0]
  Error: Cannot index into a null array.

So make sure your arrays are not $null before you try to access elements inside them.

Count

Arrays and other collections have a Count property that tells you how many items are in the
array.

  PowerShell

  PS> $data.Count
  4

PowerShell 3.0 added a Count property to most objects. you can have a single object and it
should give you a count of 1 .

  PowerShell

  PS> $date = Get-Date
  PS> $date.Count
  1

Even $null has a Count property except it returns 0 .

  PowerShell

  PS> $null.Count
  0

There are some traps here that I will revisit when I cover checking for $null or empty arrays
later on in this article.

Off-by-one errors

<!-- p.279 -->

A common programming error is created because arrays start at index 0. Off-by-one errors can
be introduced in two ways.

The first is by mentally thinking you want the second item and using an index of 2 and really
getting the third item. Or by thinking that you have four items and you want last item, so you
use the count to access the last item.

 PowerShell

 $data[ $data.Count ]

PowerShell is perfectly happy to let you do that and give you exactly what item exists at index
4: $null . You should be using $data.Count - 1 or the -1 that we learned about above.

 PowerShell

 PS> $data[ $data.Count - 1 ]
 Three

This is where you can use the -1 index to get the last element.

 PowerShell

 PS> $data[ -1 ]
 Three

Lee Dailey also pointed out to me that we can use $data.GetUpperBound(0) to get the max
index number.

 PowerShell

 PS> $data.GetUpperBound(0)
 3
 PS> $data[ $data.GetUpperBound(0) ]
 Three

The second most common way is when iterating the list and not stopping at the right time. I'll
revisit this when we talk about using the for loop.

Updating items
We can use the same index to update existing items in the array. This gives us direct access to
update individual items.

<!-- p.280 -->

 PowerShell

 $data[2] = 'dos'
 $data[3] = 'tres'

If we try to update an item that is past the last element, then we get an Index was outside the
bounds of the array. error.

 PowerShell

 PS> $data[4] = 'four'
 Index was outside the bounds of the array.
 At line:1 char:1
 + $data[4] = 'four'
 + ~~~~~~~~~~~~~
 + CategoryInfo          : OperationStopped: (:) [], IndexOutOfRangeException
 + FullyQualifiedErrorId : System.IndexOutOfRangeException

I'll revisit this later when I talk about how to make an array larger.

Iteration
At some point, you might need to walk or iterate the entire list and perform some action for
each item in the array.

Pipeline

Arrays and the PowerShell pipeline are meant for each other. This is one of the simplest ways
to process over those values. When you pass an array to a pipeline, each item inside the array
is processed individually.

 PowerShell

 PS> $data = 'Zero','One','Two','Three'
 PS> $data | ForEach-Object {"Item: [$PSItem]"}
 Item: [Zero]
 Item: [One]
 Item: [Two]
 Item: [Three]

If you have not seen $PSItem before, just know that it's the same thing as $_ . You can use
either one because they both represent the current object in the pipeline.

ForEach loop
