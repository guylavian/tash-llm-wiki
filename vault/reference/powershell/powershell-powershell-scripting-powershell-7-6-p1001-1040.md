---
title: "How to use this documentation — pages 1001-1040"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1001-1040
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1001-1040
family: powershell
documentKind: "doc"
abstract: "Choosing a version of PowerShell to use with the extension With PowerShell installing side-by-side with Windows PowerShell, it's now possible to use a specific version of PowerShell with the PowerShell extension. This feature looks at a few well- known paths on different operati"
---

# How to use this documentation — pages 1001-1040

<!-- p.1001 -->

Choosing a version of PowerShell to use with the extension
With PowerShell installing side-by-side with Windows PowerShell, it's now possible to use a
specific version of PowerShell with the PowerShell extension. This feature looks at a few well-
known paths on different operating systems to discover installations of PowerShell.

Use the following steps to choose the version:

     1. Open the Command Palette on Windows or Linux with Ctrl + Shift + P . On macOS, use
        Cmd + Shift + P .

     2. Search for Session.
     3. Click on PowerShell: Show Session Menu.
     4. Choose the version of PowerShell you want to use from the list.

If you installed PowerShell to a non-typical location, it might not show up initially in the
Session Menu. You can extend the session menu by adding your own custom paths as
described below.

The PowerShell session menu can also be accessed from the {} icon in the bottom right corner
of status bar. Hovering on or selecting this icon displays a shortcut to the session menu and a
small pin icon. If you select the pin icon, the version number is added to the status bar. The
version number is a shortcut to the session menu requiring fewer clicks.

  ７ Note

  Pinning the version number replicates the behavior of the extension in versions of VS
  Code before 1.65. The 1.65 release of VS Code changed the APIs the PowerShell extension
  uses and standardized the status bar for language extensions.

Configuration settings for Visual Studio Code
First, if you're not familiar with how to change settings in VS Code, we recommend reading
Visual Studio Code's settings    documentation.

After reading the documentation, you can add configuration settings in settings.json .

 JSON

 {
       "editor.renderWhitespace": "all",
       "editor.renderControlCharacters": true,
       "files.trimTrailingWhitespace": true,
       "files.encoding": "utf8bom",

<!-- p.1002 -->

       "files.autoGuessEncoding": true
 }

If you don't want these settings to affect all files types, VS Code also allows per-language
configurations. Create a language-specific setting by putting settings in a [<language-name>]
field. For example:

 JSON
 {
       "[powershell]": {
           "files.encoding": "utf8bom",
           "files.autoGuessEncoding": true
       }
 }

   Tip

  For more information about file encoding in VS Code, see Understanding file encoding.
  Also, check out How to replicate the ISE experience in VS Code for other tips on how to
  configure VS Code for PowerShell editing.

Adding your own PowerShell paths to the session menu
You can add other PowerShell executable paths to the session menu through the Visual Studio
Code setting     : powershell.powerShellAdditionalExePaths .

You can do this using the GUI:

     1. From the Command Palette search for and select Open User Settings. Or use the
       keyboard shortcut on Windows or Linux Ctrl + , . On macOS, use Cmd + , .
     2. In the Settings editor, search for PowerShell Additional Exe Paths.
     3. Click Add Item.
     4. For the Key (under Item), provide your choice of name for this additional PowerShell
       installation.
     5. For the Value (under Value), provide the absolute path to the executable itself.

You can add as many additional paths as you like. The added items show up in the session
menu with the given key as the name.

Alternatively you can add key-value pairs to the object
powershell.powerShellAdditionalExePaths in your settings.json :

<!-- p.1003 -->

 JSON

 {
     "powershell.powerShellAdditionalExePaths": {
         "Downloaded PowerShell": "C:/Users/username/Downloads/PowerShell/pwsh.exe",
         "Built PowerShell": "C:/Users/username/src/PowerShell/src/powershell-win-
 core/bin/Debug/net6.0/win7-x64/publish/pwsh.exe"
     },
 }

  ７ Note

  Prior to version 2022.5.0 of the extension, this setting was a list of objects with the
  required keys exePath and versionName . A breaking change was introduced to support
  configuration via GUI. If you had previously configured this setting, please convert it the
  new format. The value given for versionName is now the Key, and the value given for
     exePath is now the Value. You can do this more easily by resetting the value and using the

  Settings interface.

To set the default PowerShell version, set the value powershell.powerShellDefaultVersion to
the text displayed in the session menu (the text used for the key):

 JSON

 {
       "powershell.powerShellAdditionalExePaths": {
           "Downloaded PowerShell": "C:/Users/username/Downloads/PowerShell/pwsh.exe",
       },
       "powershell.powerShellDefaultVersion": "Downloaded PowerShell",
 }

After you've configured this setting, restart VS Code or to reload the current VS Code window
from the Command Palette, type Developer: Reload Window .

If you open the session menu, you now see your additional PowerShell installations.

   Tip

  If you build PowerShell from source, this is a great way to test out your local build of
  PowerShell.

Debugging with Visual Studio Code

<!-- p.1004 -->

No-workspace debugging
In VS Code version 1.9 (or higher), you can debug PowerShell scripts without opening the
folder that contains the PowerShell script.

     1. Open the PowerShell script file with File > Open File...
     2. Set a breakpoint - select a line then press F9
     3. Press F5 to start debugging

You should see the Debug actions pane appear that allows you to break into the debugger,
step, resume, and stop debugging.

Workspace debugging
Workspace debugging refers to debugging in the context of a folder that you've opened from
the File menu using Open Folder.... The folder you open is typically your PowerShell project
folder or the root of your Git repository. Workspace debugging allows you to define multiple
debug configurations other than just debugging the currently open file.

Follow these steps to create a debug configuration file:

     1. Open the Debug view on Windows or Linux by pressing Ctrl + Shift + D . On macOS,
       press Cmd + Shift + D .

     2. Click the create a launch.json file link.

     3. From the Select Environment prompt, choose PowerShell.

     4. Choose the type of debugging you'd like to use:

             Launch Current File - Launch and debug the file in the currently active editor
             window
             Launch Script - Launch and debug the specified file or command
             Interactive Session - Debug commands executed from the Integrated Console
             Attach - Attach the debugger to a running PowerShell Host Process

VS Code creates a directory and a file .vscode\launch.json in the root of your workspace
folder to store the debug configuration. If your files are in a Git repository, you typically want
to commit the launch.json file. The contents of the launch.json file are:

 JSON
 {
     "version": "0.2.0",
     "configurations": [

<!-- p.1005 -->

         {
              "type": "PowerShell",
              "request": "launch",
              "name": "PowerShell Launch (current file)",
              "script": "${file}",
              "args": [],
              "cwd": "${file}"
         },
         {
              "type": "PowerShell",
              "request": "attach",
              "name": "PowerShell Attach to Host Process",
              "processId": "${command.PickPSHostProcess}",
              "runspaceId": 1
         },
         {
              "type": "PowerShell",
              "request": "launch",
              "name": "PowerShell Interactive Session",
              "cwd": "${workspaceRoot}"
         }
     ]
 }

This file represents the common debug scenarios. When you open this file in the editor, you
see an Add Configuration... button. You can click this button to add more PowerShell debug
configurations. One useful configuration to add is PowerShell: Launch Script. With this
configuration, you can specify a file containing optional arguments that are used whenever you
press F5 no matter which file is active in the editor.

After the debug configuration is established, you can select the configuration you want to use
during a debug session. Select a configuration from the debug configuration drop-down in the
Debug view's toolbar.

Troubleshooting the PowerShell extension
If you experience any issues using VS Code for PowerShell script development, see the
troubleshooting guide     on GitHub.

Useful resources
There are a few videos and blog posts that may be helpful to get you started using the
PowerShell extension for VS Code:

Videos

<!-- p.1006 -->

      Using Visual Studio Code as Your Default PowerShell Editor
      Visual Studio Code: deep dive into debugging your PowerShell scripts

Blog posts
      PowerShell Extension
      Write and debug PowerShell scripts in Visual Studio Code
      Debugging Visual Studio Code Guidance
      Debugging PowerShell in Visual Studio Code
      Get started with PowerShell development in Visual Studio Code
      Visual Studio Code editing features for PowerShell development - Part 1
      Visual Studio Code editing features for PowerShell development - Part 2
      Debugging PowerShell script in Visual Studio Code - Part 1
      Debugging PowerShell script in Visual Studio Code - Part 2

PowerShell extension project source code
The PowerShell extension's source code can be found on GitHub .

If you're interested in contributing, Pull Requests are greatly appreciated. Follow along with the
developer documentation       on GitHub to get started.

 Last updated on 12/08/2025

<!-- p.1007 -->

How to replicate the ISE experience in
Visual Studio Code
While the PowerShell extension for VS Code doesn't seek complete feature parity with the
PowerShell ISE, there are features in place to make the VS Code experience more natural for
users of the ISE.

This document tries to list settings you can configure in VS Code to make the user experience a
bit more familiar compared to the ISE.

ISE Mode

  ７ Note

  This feature is available in the PowerShell Preview extension since version 2019.12.0 and in
  the PowerShell extension since version 2020.3.0.

The easiest way to replicate the ISE experience in Visual Studio Code is by turning on "ISE
Mode". To do this, open the command palette ( F1 OR Ctrl + Shift + P OR Cmd + Shift + P on
macOS) and type in "ISE Mode". Select "PowerShell: Enable ISE Mode" from the list.

This command automatically applies the settings described below The result looks like this:

<!-- p.1008 -->

ISE Mode configuration settings
ISE Mode makes the following changes to VS Code settings.

     Key bindings

                                                                                ﾉ   Expand table

      Function                                        ISE Binding        VS Code Binding

      Interrupt and break debugger                     Ctrl + B           F6

      Execute current line/highlighted text            F8                 F8

      List available snippets                          Ctrl + J           Ctrl + Alt + J

       ７ Note

       You can configure your own key bindings in VS Code as well.

     Simplified ISE-like UI

     If you're looking to simplify the Visual Studio Code UI to look more closely to the UI of
     the ISE, apply these two settings:

      JSON

      "workbench.activityBar.visible": false,
      "debug.openDebug": "neverOpen",

     These settings hide the "Activity Bar" and the "Debug Side Bar" sections shown inside the
     red box below:

<!-- p.1009 -->

The end result looks like this:

<!-- p.1010 -->

Tab completion

To enable more ISE-like tab completion, add this setting:

 JSON

 "editor.tabCompletion": "on",

No focus on console when executing

To keep the focus in the editor when you execute with F8 :

 JSON
 "powershell.integratedConsole.focusConsoleOnExecute": false

The default is true for accessibility purposes.

<!-- p.1011 -->

Don't start integrated console on startup

To stop the integrated console on startup, set:

 JSON
 "powershell.integratedConsole.showOnStartup": false

  ７ Note

  The background PowerShell process still starts to provide IntelliSense, script analysis,
  symbol navigation, etc., but the console won't be shown.

Assume files are PowerShell by default

To make new/untitled files, register as PowerShell by default:

 JSON
 "files.defaultLanguage": "powershell",

Color scheme

There are a number of ISE themes available for VS Code to make the editor look much
more like the ISE.

In the Command Palette type theme to get Preferences: Color Theme and press Enter . In
the drop-down list, select PowerShell ISE .

You can set this theme in the settings with:

 JSON
 "workbench.colorTheme": "PowerShell ISE",

PowerShell Command Explorer

Thanks to the work of @corbob , the PowerShell extension has the beginnings of its
own command explorer.

In the Command Palette, enter PowerShell Command Explorer and press Enter .

Open in the ISE

<!-- p.1012 -->

  If you want to open a file in the Windows PowerShell ISE anyway, open the Command
  Palette, search for "open in ise", then select PowerShell: Open Current File in PowerShell
  ISE.

Other resources
  4sysops has a great article    on configuring VS Code to be more like the ISE.
  Mike F Robbins has a great post     on setting up VS Code.

VS Code Tips
  Command Palette

  The Command Palette is handy way of executing commands in VS Code. Open the
  command palette using F1 OR Ctrl + Shift + P OR Cmd + Shift + P on macOS.

  For more information, see the VS Code documentation .

  Hide the Debug Console panel

  The PowerShell extension uses the built-in debugging interface of VS Code to allow for
  debugging of PowerShell scripts and modules. However, the extension does not use the
  Debug Console panel. To hide the Debug Console, right-click on Debug Console and
  select Hide 'Debug Console'.

  For more information about debugging PowerShell with Visual Studio Code, see Using VS
  Code.

<!-- p.1013 -->

More settings
If you know of more ways to make VS Code feel more familiar for ISE users, contribute to this
doc. If there's a compatibility configuration you're looking for, but you can't find any way to
enable it, open an issue      and ask away!

We're always happy to accept PRs and contributions as well!

 Last updated on 12/08/2025

<!-- p.1014 -->

Using Visual Studio Code for remote
editing and debugging
For those of you that are familiar with the ISE, you may recall that you could run psedit
file.ps1 from the integrated console to open files - local or remote - right in the ISE.

This feature is also available in the PowerShell extension for VS Code. This guide shows you
how to do it.

Prerequisites
This guide assumes that you have:

     A remote resource (ex: a VM, a container) that you have access to
     PowerShell running on it and the host machine
     VS Code and the PowerShell extension for VS Code

This feature works on PowerShell and Windows PowerShell.

This feature also works when connecting to a remote machine via WinRM, PowerShell Direct, or
SSH. If you want to use SSH, but are using Windows, check out the Win32 version of SSH !

  ） Important

  The Open-EditorFile and psedit commands only work in the PowerShell Integrated
  Console created by the PowerShell extension for VS Code.

Usage examples
These examples show remote editing and debugging from a MacBook Pro to an Ubuntu VM
running in Azure. The process is identical on Windows.

Local file editing with Open-EditorFile
With the PowerShell extension for VS Code started and the PowerShell Integrated Console
opened, we can type Open-EditorFile foo.ps1 or psedit foo.ps1 to open the local foo.ps1 file
right in the editor.

<!-- p.1015 -->

  ７ Note

  The file foo.ps1 must already exist.

From there, we can:

     Add breakpoints to the gutter

<!-- p.1016 -->

Hit F5 to debug the PowerShell script.

<!-- p.1017 -->

While debugging, you can interact with the debug console, check out the variables in the
scope on the left, and all the other standard debugging tools.

Remote file editing with Open-EditorFile
Now let's get into remote file editing and debugging. The steps are nearly the same, there's
just one thing we need to do first - enter our PowerShell session to the remote server.

There's a cmdlet for to do so. It's called Enter-PSSession .

In short:

      Enter-PSSession -ComputerName foo starts a session via WinRM

      Enter-PSSession -ContainerId foo and Enter-PSSession -VmId foo start a session via

     PowerShell Direct
      Enter-PSSession -HostName foo starts a session via SSH

For more information, see the documentation for Enter-PSSession.

Since we're remoting to an Ubuntu VM in Azure, we're using SSH.

<!-- p.1018 -->

First, in the Integrated Console, run Enter-PSSession . You're connected to the remote session
when [<hostname>] shows up to the left of your prompt.

Now, we can do the same steps as if we're editing a local script.

   1. Run Open-EditorFile test.ps1 or psedit test.ps1 to open the remote test.ps1 file

<!-- p.1019 -->

2. Edit the file/set breakpoints

<!-- p.1020 -->

3. Start debugging (F5) the remote file

<!-- p.1021 -->

If you have any problems, you can open issues in the GitHub repo   .

Last updated on 12/08/2025

<!-- p.1022 -->

Understanding file encoding in VS Code
and PowerShell
When using VS Code to create and edit PowerShell scripts, it's important that your files are
saved using the correct character encoding format.

What is file encoding and why is it important?
VS Code manages the interface between a human entering strings of characters into a buffer
and reading/writing blocks of bytes to the filesystem. When VS Code saves a file, it uses a text
encoding to decide what bytes each character becomes. For more information, see
about_Character_Encoding.

Similarly, when PowerShell runs a script it must convert the bytes in a file to characters to
reconstruct the file into a PowerShell program. Since VS Code writes the file and PowerShell
reads the file, they need to use the same encoding system. This process of parsing a
PowerShell script goes: bytes -> characters -> tokens -> abstract syntax tree -> execution.

Both VS Code and PowerShell are installed with a sensible default encoding configuration.
However, the default encoding used by PowerShell has changed with the release of PowerShell
6. To ensure you have no problems using PowerShell or the PowerShell extension in VS Code,
you need to configure your VS Code and PowerShell settings properly.

Common causes of encoding issues
Encoding problems occur when the encoding of VS Code or your script file doesn't match the
expected encoding of PowerShell. There is no way for PowerShell to automatically determine
the file encoding.

You're more likely to have encoding problems when you're using characters not in the 7-bit
ASCII character set   . For example:

     Extended non-letter characters like em-dash ( — ), non-breaking space ( ) or left double
     quotation mark ( " )
     Accented latin characters ( É , ü )
     Non-latin characters like Cyrillic ( Д , Ц )
     CJK characters ( 本 , 화 , が )

Common reasons for encoding issues are:

<!-- p.1023 -->

     The encodings of VS Code and PowerShell haven't been changed from their defaults. For
     PowerShell 5.1 and below, the default encoding is different from VS Code's.
     Another editor has opened and overwritten the file in a new encoding. This often
     happens with the ISE.
     The file is checked into source control in an encoding that's different from what VS Code
     or PowerShell expects. This can happen when collaborators use editors with different
     encoding configurations.

How to tell when you have encoding issues
Often encoding errors present themselves as parse errors in scripts. If you find strange
character sequences in your script, this can be the problem. In the example below, an en-dash
( – ) appears as the characters â&euro;" :

 Output
 Send-MailMessage : A positional parameter cannot be found that accepts argument
 'Testing FuseMail SMTP...'.
 At C:\Users\<User>\<OneDrive>\Development\PowerShell\Scripts\Send-
 EmailUsingSmtpRelay.ps1:6 char:1
 + Send-MailMessage â&euro;"From $from â&euro;"To $recipient1 â&euro;"Subject
 $subject ...
 + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     + CategoryInfo          : InvalidArgument: (:) [Send-MailMessage],
 ParameterBindingException
     + FullyQualifiedErrorId :
 PositionalParameterNotFound,Microsoft.PowerShell.Commands.SendMailMessage

This problem occurs because VS Code encodes the character – in UTF-8 as the bytes 0xE2
0x80 0x93 . When these bytes are decoded as Windows-1252, they're interpreted as the

characters â&euro;" .

Some strange character sequences that you might see include:

      â&euro;" instead of – (an en-dash)
      â&euro;" instead of — (an em-dash)

      Ã„2 instead of Ä
      Â instead of      (a non-breaking space)
      Ã&copy; instead of é

This handy reference      lists the common patterns that indicate a UTF-8/Windows-1252
encoding problem.

<!-- p.1024 -->

How the PowerShell extension in VS Code interacts
with encodings
The PowerShell extension interacts with scripts in a number of ways:

   1. When scripts are edited in VS Code, the contents are sent by VS Code to the extension.
     The Language Server Protocol      mandates that this content is transferred in UTF-8.
     Therefore, it isn't possible for the extension to get the wrong encoding.
   2. When scripts are executed directly in the Integrated Console, they're read from the file by
     PowerShell directly. If PowerShell's encoding differs from VS Code's, something can go
     wrong here.
   3. When a script that's open in VS Code references another script that isn't open in VS Code,
     the extension falls back to loading that script's content from the file system. The
     PowerShell extension defaults to UTF-8 encoding, but uses byte-order mark        , or BOM,
     detection to select the correct encoding.

The problem occurs when assuming the encoding of BOM-less formats (like UTF-8           with no
BOM and Windows-1252       ). The PowerShell extension defaults to UTF-8. The extension can't
change VS Code's encoding settings. For more information, see issue #824         .

Choosing the right encoding
Different systems and applications can use different encodings:

     In .NET Standard, on the web, and in the Linux world, UTF-8 is now the dominant
     encoding.
     Many .NET Framework applications use UTF-16        . For historical reasons, this is sometimes
     called "Unicode", a term that now refers to a broad standard      that includes both UTF-8
     and UTF-16.
     On Windows, many native applications that predate Unicode continue to use Windows-
     1252 by default.

Unicode encodings also have the concept of a byte-order mark (BOM). BOMs occur at the
beginning of text to tell a decoder which encoding the text is using. For multi-byte encodings,
the BOM also indicates endianness     of the encoding. BOMs are designed to be bytes that
rarely occur in non-Unicode text, allowing a reasonable guess that text is Unicode when a BOM
is present.

BOMs are optional and their adoption isn't as popular in the Linux world because a
dependable convention of UTF-8 is used everywhere. Most Linux applications presume that
text input is encoded in UTF-8. While many Linux applications will recognize and correctly
handle a BOM, a number don't, leading to artifacts in text manipulated with those applications.

<!-- p.1025 -->

Therefore:

     If you work primarily with Windows applications and Windows PowerShell, you should
     prefer an encoding like UTF-8 with BOM or UTF-16.
     If you work across platforms, you should prefer UTF-8 with BOM.
     If you work mainly in Linux-associated contexts, you should prefer UTF-8 without BOM.
     Windows-1252 and latin-1 are essentially legacy encodings that you should avoid if
     possible. However, some older Windows applications may depend on them.
     It's also worth noting that script signing is encoding-dependent    , meaning a change of
     encoding on a signed script will require resigning.

Configuring VS Code
VS Code's default encoding is UTF-8 without BOM.

To set VS Code's encoding , go to the VS Code settings ( Ctrl + , ) and set the
"files.encoding" setting:

 JSON
 "files.encoding": "utf8bom"

Some possible values are:

      utf8 : [UTF-8] without BOM
      utf8bom : [UTF-8] with BOM

      utf16le : Little endian [UTF-16]

      utf16be : Big endian [UTF-16]
      windows1252 : [Windows-1252]

You should get a dropdown for this in the GUI view, or completions for it in the JSON view.

You can also add the following to autodetect encoding when possible:

 JSON
 "files.autoGuessEncoding": true

If you don't want these settings to affect all files types, VS Code also allows per-language
configurations. Create a language-specific setting by putting settings in a [<language-name>]
field. For example:

 JSON

<!-- p.1026 -->

 "[powershell]": {
     "files.encoding": "utf8bom",
     "files.autoGuessEncoding": true
 }

You may also want to consider installing the Gremlins tracker    for Visual Studio Code. This
extension reveals certain Unicode characters that easily corrupted because they're invisible or
look like other normal characters.

Configuring PowerShell
PowerShell's default encoding varies depending on version:

       In PowerShell 6+, the default encoding is UTF-8 without BOM on all platforms.
       In Windows PowerShell, the default encoding is usually Windows-1252, which is an
       extension of latin-1   (also known as ISO 8859-1).

In PowerShell 5+ you can find your default encoding with this:

 PowerShell
 [psobject].Assembly.GetTypes() | Where-Object { $_.Name -eq 'ClrFacade'} |
   ForEach-Object {
     $_.GetMethod('GetDefaultEncoding',
 [System.Reflection.BindingFlags]'nonpublic,static').Invoke($null, @())
   }

The following script    can be used to determine what encoding your PowerShell session infers
for a script without a BOM.

 PowerShell
 $badBytes = [byte[]]@(0xC3, 0x80)
 $utf8Str = [System.Text.Encoding]::UTF8.GetString($badBytes)
 $bytes = [System.Text.Encoding]::ASCII.GetBytes('Write-Output "') + [byte[]]@(0xC3,
 0x80) + [byte[]]@(0x22)
 $path = Join-Path ([System.IO.Path]::GetTempPath()) 'encodingtest.ps1'

 try
 {
       [System.IO.File]::WriteAllBytes($path, $bytes)

       switch (& $path)
       {
           $utf8Str
           {
               return 'UTF-8'
               break

<!-- p.1027 -->

           }

           default
           {
               return 'Windows-1252'
               break
           }
     }
 }
 finally
 {
     Remove-Item $path
 }

It's possible to configure PowerShell to use a given encoding more generally using profile
settings. See the following articles:

      @mklement0's answer about PowerShell encoding on Stack Overflow         .
      @rkeithhill's blog post about dealing with BOM-less UTF-8 input in PowerShell     .

It's not possible to force PowerShell to use a specific input encoding. PowerShell 5.1 and below,
running on Windows with the locale set to en-US, defaults to Windows-1252 encoding when
there's no BOM. Other locale settings may use a different encoding. To ensure interoperability,
it's best to save scripts in a Unicode format with a BOM.

  ） Important

  Any other tools you have that touch PowerShell scripts may be affected by your encoding
  choices or re-encode your scripts to another encoding.

Existing scripts
Scripts already on the file system may need to be re-encoded to your new chosen encoding. In
the bottom bar of VS Code, you'll see the label UTF-8. Click it to open the action bar and select
Save with encoding. You can now pick a new encoding for that file. See VS Code's encoding
for full instructions.

If you need to re-encode multiple files, you can use the following script:

 PowerShell
 Get-ChildItem *.ps1 -Recurse | ForEach-Object {
     $content = Get-Content -Path $_
     Set-Content -Path $_.FullName -Value $content -Encoding UTF8 -PassThru -Force
 }

<!-- p.1028 -->

The PowerShell Integrated Scripting Environment (ISE)
If you also edit scripts using the PowerShell ISE, you need to synchronize your encoding
settings there.

The ISE should honor a BOM, but it's also possible to use reflection to set the encoding     .
Note that this wouldn't be persisted between startups.

Source control software
Some source control tools, such as git, ignore encodings; git just tracks the bytes. Others, like
Azure DevOps or Mercurial, may not. Even some git-based tools rely on decoding text.

When this is the case, make sure you:

     Configure the text encoding in your source control to match your VS Code configuration.
     Ensure all your files are checked into source control in the relevant encoding.
     Be wary of changes to the encoding received through source control. A key sign of this is
     a diff indicating changes but where nothing seems to have changed (because bytes have
     but characters have not).

Collaborators' environments
On top of configuring source control, ensure that your collaborators on any files you share
don't have settings that override your encoding by re-encoding PowerShell files.

Other programs
Any other program that reads or writes a PowerShell script may re-encode it.

Some examples are:

     Using the clipboard to copy and paste a script. This is common in scenarios like:
        Copying a script into a VM
        Copying a script out of an email or webpage
        Copying a script into or out of a Microsoft Word or PowerPoint document
     Other text editors, such as:
        Notepad
        vim
        Any other PowerShell script editor
     Text editing utilities, like:
         Get-Content / Set-Content / Out-File

<!-- p.1029 -->

         PowerShell redirection operators like > and >>
          sed / awk

      File transfer programs, like:
         A web browser, when downloading scripts
         A file share

Some of these tools deal in bytes rather than text, but others offer encoding configurations. In
those cases where you need to configure an encoding, you need to make it the same as your
editor encoding to prevent problems.

Other resources on encoding in PowerShell
There are a few other nice posts on encoding and configuring encoding in PowerShell that are
worth a read:

      about_Character_Encoding
      @mklement0's summary of PowerShell encoding on Stack Overflow
      Previous issues opened on VS Code-PowerShell for encoding problems:
         #1308
         #1628
         #1680
         #1744
         #1751
      The classic Joel on Software write up about Unicode
      Encoding in .NET Standard

 Last updated on 12/08/2025

<!-- p.1030 -->

Using Visual Studio Code to debug
compiled cmdlets
This guide shows you how to interactively debug C# source code for a compiled PowerShell
module using Visual Studio Code (VS Code) and the C# extension.

Some familiarity with the Visual Studio Code debugger is assumed.

     For a general introduction to the VS Code debugger, see Debugging in Visual Studio
     Code    .

     For examples of debugging PowerShell script files and modules, see Using Visual Studio
     Code for remote editing and debugging.

This guide assumes you have read and followed the instructions in the Writing Portable
Modules guide.

Creating a build task
Build your project automatically before launching a debugging session. Rebuilding ensures that
you debug the latest version of your code.

Configure a build task:

   1. In the Command Palette, run the Configure Default Build Task command.

     Run Configure Default Build Task

   2. In the Select a task to configure dialog, choose Create tasks.json file from template.

   3. In the Select a Task Template dialog, choose .NET Core.

A new tasks.json file is created if one doesn't exist yet.

To test your build task:

   1. In the Command Palette, run the Run Build Task command.

   2. In the Select the build task to run dialog, choose build.

Information about DLL files being locked
By default, a successful build doesn't show output in the terminal pane. If you see output that
contains the text Project file doesn't exist, you should edit the tasks.json file. Include the

<!-- p.1031 -->

explicit path to the C# project expressed as "${workspaceFolder}/myModule" . In this example,
myModule is the name of the project folder. This entry must go after the build entry in the

args list as follows:

 JSON
     {
         "label": "build",
         "command": "dotnet",
         "type": "shell",
         "args": [
             "build",
             "${workspaceFolder}/myModule",
             // Ask dotnet build to generate full paths for file names.
             "/property:GenerateFullPaths=true",
             // Do not generate summary otherwise it leads to duplicate errors in
 Problems panel
             "/consoleloggerparameters:NoSummary",
         ],
         "group": "build",
         "presentation": {
             "reveal": "silent"
         },
         "problemMatcher": "$msCompile"
     }

When debugging, your module DLL is imported into the PowerShell session in the VS Code
terminal. The DLL becomes locked. The following message is displayed when you run the build
task without closing the terminal session:

 Output

 Could not copy "obj\Debug\netstandard2.0\myModule.dll" to
 "bin\Debug\netstandard2.0\myModule.dll"`.

Terminal sessions must be closed before you rebuild.

Setting up the debugger
To debug the PowerShell cmdlet, you need to set up a custom launch configuration. This
configuration is used to:

     Build your source code
     Start PowerShell with your module loaded
     Leave PowerShell open in the terminal pane

<!-- p.1032 -->

When you invoke your cmdlet in the terminal session, the debugger stops at any breakpoints
set in your source code.

Configuring launch.json for PowerShell
   1. Install the C# for Visual Studio Code    extension

   2. In the Debug pane, add a debug configuration

   3. In the Select environment dialog, choose .NET Core

   4. The launch.json file is opened in the editor. With your cursor inside the configurations
     array, you see the configuration picker. If you don't see this list, select Add
     Configuration.

   5. To create a default debug configuration, select Launch .NET Core Console App:

     Launch .NET Core Console App

   6. Edit the name , program , args , and console fields as follows:

       JSON
        {
            "name": "PowerShell cmdlets: pwsh",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "pwsh",
            "args": [
                "-NoExit",
                "-NoProfile",
                "-Command",
                "Import-Module
       ${workspaceFolder}/myModule/bin/Debug/netstandard2.0/myModule.dll",
            ],
            "cwd": "${workspaceFolder}",
            "stopAtEntry": false,
            "console": "integratedTerminal"
        }

The program field is used to launch pwsh so that the cmdlet being debugged can be run. The -
NoExit argument prevents the PowerShell session from exiting as soon as the module is

imported. The path in the Import-Module argument is the default build output path when
you've followed the Writing Portable Modules guide. If you've created a module manifest
( .psd1 file), you should use the path to that instead. The / path separator works on Windows,

<!-- p.1033 -->

Linux, and macOS. You must use the integrated terminal to run the PowerShell commands you
want to debug.

  ７ Note

  If the debugger doesn't stop at any breakpoints, look in the Visual Studio Code Debug
  Console for a line that says:

   Loaded '/path/to/myModule.dll'. Skipped loading symbols. Module is optimized and
   the debugger option 'Just My Code' is enabled.

  If you see this, add "justMyCode": false to your launch config (at the same level as
  "console": "integratedTerminal" .

Configuring launch.json for Windows PowerShell
This launch configuration works for testing your cmdlets in Windows PowerShell
( powershell.exe ). Create a second launch configuration with the following changes:

   1. name should be PowerShell cmdlets: powershell

   2. type should be clr

   3. program should be powershell

     It should look like this:

      JSON

       {
           "name": "PowerShell cmdlets: powershell",
           "type": "clr",
           "request": "launch",
           "preLaunchTask": "build",
           "program": "powershell",
           "args": [
               "-NoExit",
               "-NoProfile",
               "-Command",
               "Import-Module
      ${workspaceFolder}/myModule/bin/Debug/netstandard2.0/myModule.dll",
           ],
           "cwd": "${workspaceFolder}",
           "stopAtEntry": false,

<!-- p.1034 -->

              "console": "integratedTerminal"
         }

Launching a debugging session
Now everything is ready to begin debugging.

      Place a breakpoint in the source code for the cmdlet you want to debug:

      A breakpoint shows as a red dot in the gutter

      Ensure that the relevant PowerShell cmdlets configuration is selected in the configuration
      drop-down menu in the Debug view:

      Select the launch configuration

      Press F5 or click on the Start Debugging button

      Switch to the terminal pane and invoke your cmdlet:

      Invoke the cmdlet

      Execution stops at the breakpoint:

      Executions halts at breakpoint

You can step through the source code, inspect variables, and inspect the call stack.

To end debugging, click Stop in the debug toolbar or press Shift + F5 . The shell used for
debugging exits and releases the lock on the compiled DLL file.

 Last updated on 12/08/2025

<!-- p.1035 -->

PowerShell scripting performance
considerations
PowerShell scripts that leverage .NET directly and avoid the pipeline tend to be faster than
idiomatic PowerShell. Idiomatic PowerShell uses cmdlets and PowerShell functions, often
leveraging the pipeline, and resorting to .NET only when necessary.

  ７ Note

  Many of the techniques described here aren't idiomatic PowerShell and may reduce the
  readability of a PowerShell script. Script authors are advised to use idiomatic PowerShell
  unless performance dictates otherwise.

Suppressing output
There are many ways to avoid writing objects to the pipeline.

     Assignment or file redirection to $null
     Casting to [void]
     Pipe to Out-Null

The speeds of assigning to $null , casting to [void] , and file redirection to $null are almost
identical. However, calling Out-Null in a large loop can be significantly slower, especially in
PowerShell 5.1.

 PowerShell
 $tests = @{
     'Assign to $null' = {
         $arrayList = [System.Collections.ArrayList]::new()
         foreach ($i in 0..$args[0]) {
             $null = $arraylist.Add($i)
         }
     }
     'Cast to [void]' = {
         $arrayList = [System.Collections.ArrayList]::new()
         foreach ($i in 0..$args[0]) {
             [void] $arraylist.Add($i)
         }
     }
     'Redirect to $null' = {
         $arrayList = [System.Collections.ArrayList]::new()
         foreach ($i in 0..$args[0]) {
             $arraylist.Add($i) > $null

<!-- p.1036 -->

          }
     }
     'Pipe to Out-Null' = {
         $arrayList = [System.Collections.ArrayList]::new()
         foreach ($i in 0..$args[0]) {
             $arraylist.Add($i) | Out-Null
         }
     }
 }

 10kb, 50kb, 100kb | ForEach-Object {
     $groupResult = foreach ($test in $tests.GetEnumerator()) {
         $ms = (Measure-Command { & $test.Value $_ }).TotalMilliseconds

          [pscustomobject]@{
              Iterations        = $_
              Test              = $test.Key
              TotalMilliseconds = [Math]::Round($ms, 2)
          }

          [GC]::Collect()
          [GC]::WaitForPendingFinalizers()
     }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
     $groupResult | Select-Object *, @{
         Name        = 'RelativeSpeed'
         Expression = {
              $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
              [Math]::Round($relativeSpeed, 2).ToString() + 'x'
         }
     }
 }

These tests were run on a Windows 11 machine in PowerShell 7.3.4. The results are shown
below:

 Output

 Iterations Test              TotalMilliseconds RelativeSpeed
 ---------- ----              ----------------- -------------
      10240 Assign to $null               36.74 1x
      10240 Redirect to $null             55.84 1.52x
      10240 Cast to [void]                62.96 1.71x
      10240 Pipe to Out-Null              81.65 2.22x
      51200 Assign to $null              193.92 1x
      51200 Cast to [void]               200.77 1.04x
      51200 Redirect to $null            219.69 1.13x
      51200 Pipe to Out-Null             329.62 1.7x
     102400 Redirect to $null            386.08 1x
     102400 Assign to $null              392.13 1.02x

<!-- p.1037 -->

      102400 Cast to [void]                    405.24 1.05x
      102400 Pipe to Out-Null                  572.94 1.48x

The times and relative speeds can vary depending on the hardware, the version of PowerShell,
and the current workload on the system.

Array addition
Generating a list of items is often done using an array with the addition operator:

 PowerShell

 $results = @()
 $results += Get-Something
 $results += Get-SomethingElse
 $results

  ７ Note

  In PowerShell 7.5, array addition was optimized and no longer creates a new array for each
  operation. The performance considerations described here still apply to PowerShell
  versions prior to 7.5. For more information, see What's New in PowerShell 7.5.

Array addition is inefficient because arrays have a fixed size. Each addition to the array creates
a new array big enough to hold all elements of both the left and right operands. The elements
of both operands are copied into the new array. For small collections, this overhead may not
matter. Performance can suffer for large collections.

There are a couple of alternatives. If you don't actually require an array, instead consider using
a typed generic list ( [List<T>] ):

 PowerShell
 $results = [System.Collections.Generic.List[Object]]::new()
 $results.AddRange((Get-Something))
 $results.AddRange((Get-SomethingElse))
 $results

The performance impact of using array addition grows exponentially with the size of the
collection and the number additions. This code compares explicitly assigning values to an array
with using array addition and using the Add(T) method on a [List<T>] object. It defines
explicit assignment as the baseline for performance.

<!-- p.1038 -->

 PowerShell
 $tests = @{
     'PowerShell Explicit Assignment' = {
         param($Count)

         $result = foreach($i in 1..$Count) {
             $i
         }
     }
     '.Add(T) to List<T>' = {
         param($Count)

         $result = [Collections.Generic.List[int]]::new()
         foreach($i in 1..$Count) {
             $result.Add($i)
         }
     }
     '+= Operator to Array' = {
         param($Count)

         $result = @()
         foreach($i in 1..$Count) {
             $result += $i
         }
     }
 }

 5kb, 10kb, 100kb | ForEach-Object {
     $groupResult = foreach($test in $tests.GetEnumerator()) {
         $ms = (Measure-Command { & $test.Value -Count $_ }).TotalMilliseconds

         [pscustomobject]@{
             CollectionSize    = $_
             Test              = $test.Key
             TotalMilliseconds = [Math]::Round($ms, 2)
         }

         [GC]::Collect()
         [GC]::WaitForPendingFinalizers()
     }

     $groupResult = $groupResult | Sort-Object TotalMilliseconds
     $groupResult | Select-Object *, @{
         Name        = 'RelativeSpeed'
         Expression = {
              $relativeSpeed = $_.TotalMilliseconds /
 $groupResult[0].TotalMilliseconds
              [Math]::Round($relativeSpeed, 2).ToString() + 'x'
         }
     }
 }

These tests were run on a Windows 11 machine in PowerShell 7.3.4.

<!-- p.1039 -->

 Output
 CollectionSize Test                           TotalMilliseconds RelativeSpeed
 -------------- ----                           ----------------- -------------
           5120 PowerShell Explicit Assignment             26.65 1x
           5120 .Add(T) to List<T>                        110.98 4.16x
           5120 += Operator to Array                      402.91 15.12x
          10240 PowerShell Explicit Assignment              0.49 1x
          10240 .Add(T) to List<T>                        137.67 280.96x
          10240 += Operator to Array                     1678.13 3424.76x
         102400 PowerShell Explicit Assignment             11.18 1x
         102400 .Add(T) to List<T>                       1384.03 123.8x
         102400 += Operator to Array                   201991.06 18067.18x

When you're working with large collections, array addition is dramatically slower than adding
to a List<T> .

When using a [List<T>] object, you need to create the list with a specific type, like [string]
or [int] . When you add objects of a different type to the list, they are cast to the specified
type. If they can't be cast to the specified type, the method raises an exception.

 PowerShell

 $intList = [System.Collections.Generic.List[int]]::new()
 $intList.Add(1)
 $intList.Add('2')
 $intList.Add(3.0)
 $intList.Add('Four')
 $intList

 Output
 MethodException:
 Line |
    5 | $intList.Add('Four')
      | ~~~~~~~~~~~~~~~~~~~~
      | Cannot convert argument "item", with value: "Four", for "Add" to type
      "System.Int32": "Cannot convert value "Four" to type "System.Int32".
      Error: "The input string 'Four' was not in a correct format.""

 1
 2
 3

When you need the list to be a collection of different types of objects, create it with [Object]
as the list type. You can enumerate the collection inspect the types of the objects in it.

 PowerShell

<!-- p.1040 -->

 $objectList = [System.Collections.Generic.List[Object]]::new()
 $objectList.Add(1)
 $objectList.Add('2')
 $objectList.Add(3.0)
 $objectList | ForEach-Object { "$_ is $($_.GetType())" }

 Output

 1 is int
 2 is string
 3 is double

If you do require an array, you can call the ToArray() method on the list or you can let
PowerShell create the array for you:

 PowerShell
 $results = @(
     Get-Something
     Get-SomethingElse
 )

In this example, PowerShell creates an [ArrayList] to hold the results written to the pipeline
inside the array expression. Just before assigning to $results , PowerShell converts the
[ArrayList] to an [Object[]] .

Type-safe collections
PowerShell is a loosely typed language, which makes coding easier but can have performance
implications. Consider using type-safe (or type-specific) collections. Type-safe collections
consume less memory and are faster. Compare the following examples:

 PowerShell
 $Stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
 $ListInt = [System.Collections.Generic.List[int]]::new()
 for ($i = 0; $i -lt 1mb; $i++) {
     $ListInt.Add($i)
 }
 $Stopwatch.Stop()
 Write-Host "Time to add 1mb integers to List[int]:
 $($Stopwatch.Elapsed.TotalSeconds) seconds."

 Output
 Time to add 1mb integers to List[int]: 9.8841501 seconds.
