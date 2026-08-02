---
title: "How to use this documentation — pages 761-800"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0761-0800
family: powershell
documentKind: "doc"
abstract: "The following are profiles that can be created and used in Windows PowerShell ISE. Each profile is saved to its own specific path. ﾉ Expand table Profile Type Profile Path Current user, PowerShell ISE $PROFILE.CurrentUserCurrentHost , or $PROFILE All users, PowerShell ISE $PROFI"
---

# How to use this documentation — pages 761-800

<!-- p.761 -->

The following are profiles that can be created and used in Windows PowerShell ISE. Each profile
is saved to its own specific path.

                                                                                     ﾉ   Expand table

 Profile Type                            Profile Path

 Current user, PowerShell ISE            $PROFILE.CurrentUserCurrentHost , or $PROFILE

 All users, PowerShell ISE               $PROFILE.AllUsersCurrentHost

 Current user, All hosts                 $PROFILE.CurrentUserAllHosts

 All users, All hosts                    $PROFILE.AllUsersAllHosts

To create a new profile
To create a new "Current user, Windows PowerShell ISE" profile, run this command:

 PowerShell

 if (!(Test-Path -Path $PROFILE )) {
     New-Item -Type File -Path $PROFILE -Force
 }

To create a new "All users, Windows PowerShell ISE" profile, run this command:

 PowerShell
 if (!(Test-Path -Path $PROFILE.AllUsersCurrentHost)) {
     New-Item -Type File -Path $PROFILE.AllUsersCurrentHost -Force
 }

To create a new "Current user, All Hosts" profile, run this command:

 PowerShell
 if (!(Test-Path -Path $PROFILE.CurrentUserAllHosts)) {
     New-Item -Type File -Path $PROFILE.CurrentUserAllHosts -Force
 }

To create a new "All users, All Hosts" profile, type:

 PowerShell

 if (!(Test-Path -Path $PROFILE.AllUsersAllHosts)) {
     New-Item -Type File -Path $PROFILE.AllUsersAllHosts -Force

<!-- p.762 -->

}

To edit a profile
    1. To open the profile, run the command psEdit with the variable that specifies the profile
      you want to edit. For example, to open the "Current user, Windows PowerShell ISE"
      profile, type: psEdit $PROFILE

    2. Add some items to your profile. The following are a few examples to get you started:

           To change the default background color of the Console Pane to blue, in the profile
           file type: $psISE.Options.OutputPaneBackground = 'blue' .

           To change font size to 20, in the profile file type: $psISE.Options.FontSize =20

    3. To save your profile file, on the File menu, click Save. Next time you open the Windows
      PowerShell ISE, your customizations are applied.

See Also
      about_Profiles
      Introducing the Windows PowerShell ISE

Last updated on 11/20/2025

<!-- p.763 -->

How to Use Tab Completion in the Script
Pane and Console Pane
Tab completion provides automatic help when you are typing in the Script Pane or in the
Command Pane. Use the following steps to take advantage of this feature:

To automatically complete a command entry
In the Command Pane or Script Pane, type a few characters of a command and then press TAB
to select the desired completion text. If multiple items begin with the text that you initially
typed, then continue pressing TAB until the item you want appears. Tab completion can help
with typing a cmdlet name, parameter name, variable name, object property name, or a file
path.

  ７ Note

  In the Script Pane, pressing TAB will automatically complete a command only when you
  are editing .ps1 , .psd1 , or .psm1 files. Tab completion works any time when you are
  typing in the Command Pane.

To automatically complete a cmdlet parameter
entry
In the Command Pane or Script pane, type a cmdlet followed by a dash and then press TAB .

For example, type Get-Process - and then press TAB multiple times to display each of the
parameters for the cmdlet in turn.

See Also
        Introducing the Windows PowerShell ISE
        How to Create a PowerShell Tab

 Last updated on 11/20/2025

<!-- p.764 -->

How to Use the Console Pane in the
Windows PowerShell ISE
The Console pane in the Windows PowerShell Integrated Scripting Environment (ISE) operates
exactly like the stand-alone Windows PowerShell ISE console window.

To run a command in the Console Pane, type a command, and then press ENTER . To enter
multiple commands that you want to execute in sequence, type SHIFT + ENTER between
commands. See How to Use Tab Completion in the Script Pane and Console Pane for help in
typing commands.

To stop a command, on the toolbar, click Stop Operation, or press CTRL + BREAK . You can also
use CTRL + C to stop a command if the context is unambiguous. For example, if some text has
been selected in the current Pane, then CTRL + C maps to the copy operation.

Beginning in Windows PowerShell v3, the Output pane was combined with the Console pane.
This has the benefit of behaving like the stand-alone Windows PowerShell console and
eliminates the differences in procedures that were needed when they were separate. You can:

     Select and copy text from the Console pane to the Clipboard for pasting in any other
     window. To select text, click and hold the mouse in the output pane while dragging the
     mouse over the text you want to capture. You can also use the cursor arrow keys while
     holding SHIFT to select text. Then press CTRL + C or click the Copy icon in the toolbar.

     Paste the selected text at a current cursor position. Click the Paste icon on the toolbar.

     Clear all the text in the Console pane. To clear the Console pane, you can click the Clear
     Console Pane icon on the toolbar, or run the command Clear-Host or its alias, cls .

See Also
     Introducing the Windows PowerShell ISE

Last updated on 11/20/2025

<!-- p.765 -->

How to Write and Run Scripts in the
Windows PowerShell ISE
This article describes how to create, edit, run, and save scripts in the Script Pane.

How to create and run scripts
You can open and edit Windows PowerShell files in the Script Pane. Specific file types of
interest in Windows PowerShell are script files ( .ps1 ), script data files ( .psd1 ), and script
module files ( .psm1 ). These file types are syntax colored in the Script Pane editor. Other
common file types you may open in the Script Pane are configuration files ( .ps1xml ), XML files,
and text files.

  ７ Note

  The Windows PowerShell execution policy determines whether you can run scripts and
  load Windows PowerShell profiles and configuration files. The default execution policy,
  Restricted, prevents all scripts from running, and prevents loading profiles. To change the
  execution policy to allow profiles to load and be used, see Set-ExecutionPolicy and
  about_Signing.

To create a new script file
On the toolbar, click New, or on the File menu, click New. The created file appears in a new file
tab under the current PowerShell tab. Remember that the PowerShell tabs are only visible when
there are more than one. By default a file of type script ( .ps1 ) is created, but it can be saved
with a new name and extension. Multiple script files can be created in the same PowerShell tab.

To open an existing script
On the toolbar, click Open, or on the File menu, click Open. In the Open dialog box, select the
file you want to open. The opened file appears in a new tab.

To close a script tab
Click the Close icon (X) of the file tab you want to close or select the File menu and click Close.

If the file has been altered since it was last saved, you're prompted to save or discard it.

<!-- p.766 -->

To display the file path
On the file tab, point to the file name. The fully qualified path to the script file appears in a
tooltip.

To run a script
On the toolbar, click Run Script, or on the File menu, click Run.

To run a portion of a script
   1. In the Script Pane, select a portion of a script.
   2. On the File menu, click Run Selection, or on the toolbar, click Run Selection.

To stop a running script
There are several ways to stop a running script.

      Click Stop Operation on the toolbar
      Press CTRL + BREAK
      Select the File menu and click Stop Operation.

Pressing CTRL + C also works unless some text is currently selected, in which case CTRL + C
maps to the copy function for the selected text.

How to write and edit text in the Script Pane
You can copy, cut, paste, find, and replace text in the Script Pane. You can also undo and redo
the last action you just performed. The keyboard shortcuts for these actions are the same
shortcuts used for all Windows applications.

To enter text in the Script Pane
   1. Move the cursor to the Script Pane by clicking anywhere in the Script Pane, or by clicking
      Go to Script Pane in the View menu.
   2. Create a script. Syntax coloring and tab completion provide a richer editing experience in
      Windows PowerShell ISE.
   3. See How to Use Tab Completion in the Script Pane and Console Pane for details about
      using the tab completion feature to help in typing.

<!-- p.767 -->

To find text in the Script Pane
   1. To find text anywhere, press CTRL + F or, on the Edit menu, click Find in Script.
   2. To find text after the cursor, press F3 or, on the Edit menu, click Find Next in Script.
   3. To find text before the cursor, press SHIFT + F3 or, on the Edit menu, click Find Previous
     in Script.

To find and replace text in the Script Pane
Press CTRL + H or, on the Edit menu, click Replace in Script. Enter the text you want to find and
the replacement text, then press ENTER .

To go to a particular line of text in the Script Pane
   1. In the Script Pane, press CTRL + G or, on the Edit menu, click Go to Line.
   2. Enter a line number.

To copy text in the Script Pane
   1. In the Script Pane, select the text that you want to copy.
   2. Press CTRL + C or, on the toolbar, click the Copy icon, or on the Edit menu, click Copy.

To cut text in the Script Pane
   1. In the Script Pane, select the text that you want to cut.
   2. Press CTRL + X or, on the toolbar, click the Cut icon, or on the Edit menu, click Cut.

To paste text into the Script Pane
Press CTRL + V or, on the toolbar, click the Paste icon, or on the Edit menu, click Paste.

To undo an action in the Script Pane
Press CTRL + Z or, on the toolbar, click the Undo icon, or on the Edit menu, click Undo.

To redo an action in the Script Pane
Press CTRL + Y or, on the toolbar, click the Redo icon, or on the Edit menu, click Redo.

<!-- p.768 -->

How to save a script
An asterisk appears next to the script name to mark a file that hasn't been saved since it was
changed. The asterisk disappears when the file is saved.

To save a script
Press CTRL + S or, on the toolbar, click the Save icon, or on the File menu, click Save.

To save and name a script
   1. On the File menu, click Save As. The Save As dialog box will appear.
   2. In the File name box, enter a name for the file.
   3. In the Save as type box, select a file type. For example, in the Save as type box, select
     'PowerShell Scripts ( *.ps1 )'.
   4. Click Save.

To save a script in ASCII encoding
By default, Windows PowerShell ISE saves new script files ( .ps1 ), script data files ( .psd1 ), and
script module files ( .psm1 ) as Unicode (BigEndianUnicode). To save a script in another
encoding, such as ASCII (ANSI), use the Save or SaveAs methods on the $psISE.CurrentFile
object.

The following command saves a new script as MyScript.ps1 with ASCII encoding.

 PowerShell
 $psISE.CurrentFile.SaveAs("MyScript.ps1", [System.Text.Encoding]::ASCII)

The following command replaces the current script file with a file with the same name, but with
ASCII encoding.

 PowerShell
 $psISE.CurrentFile.Save([System.Text.Encoding]::ASCII)

The following command gets the encoding of the current file.

 PowerShell
 $psISE.CurrentFile.encoding

<!-- p.769 -->

Windows PowerShell ISE supports the following encoding options: ASCII, BigEndianUnicode,
Unicode, UTF32, UTF7, UTF8, and Default. The value of the Default option varies with the
system.

Windows PowerShell ISE doesn't change the encoding of script files when you use the Save or
Save As commands.

See Also
     Exploring the Windows PowerShell ISE

Last updated on 11/20/2025

<!-- p.770 -->

Keyboard Shortcuts for the Windows
PowerShell ISE
Use the following keyboard shortcuts to perform actions in Windows PowerShell Integrated
Scripting Environment (ISE). Windows PowerShell ISE is available as part of the Windows Server
and Windows client operating systems.

Keyboard shortcuts for editing text
You can use the following keyboard shortcuts when you edit text.

                                                                                     ﾉ   Expand table

 Action           Keyboard     Use in
                  Shortcuts

 Help             F1           Script Pane Important: You can specify that F1 help comes from
                               Microsoft Learn or downloaded Help (see Update-Help ). To select, click
                               Tools, Options, then on the General Settings tab, set or clear Use local
                               help content instead of online content.

 Select All       CTRL + A     Script Pane

 Copy             CTRL + C     Script Pane, Command Pane, Output Pane

 Cut              CTRL + X     Script Pane, Command Pane

 Expand or        CTRL + M     Script Pane
 Collapse
 Outlining

 Find in Script   CTRL + F     Script Pane

 Find Next in     F3           Script Pane
 Script

 Find Previous    SHIFT + F3   Script Pane
 in Script

 Find Matching    CTRL + ]     Script Pane
 Brace

 Paste            CTRL + V     Script Pane, Command Pane

 Make             CTRL + U     Script Pane, Command Pane
 Lowercase

<!-- p.771 -->

 Action            Keyboard            Use in
                   Shortcuts

 Make               CTRL +             Script Pane, Command Pane
 Uppercase          SHIFT + U

 Redo               CTRL + Y           Script Pane, Command Pane

 Replace in         CTRL + H           Script Pane
 Script

 Save               CTRL + S           Script Pane

 Select All         CTRL + A           Script Pane, Command Pane, Output Pane

 Show Snippets      CTRL + J           Script Pane, Command Pane

 Undo               CTRL + Z           Script Pane, Command Pane

 Show               CTRL +             Script Pane
 Intellisense       Space
 Help

 Delete word to     CTRL +             Script Pane
 left               Backspace

 Delete word to     CTRL +             Script Pane
 right              Delete

Keyboard shortcuts for running scripts
You can use the following keyboard shortcuts when you run scripts in the Script Pane.

                                                                                    ﾉ   Expand table

 Action           Keyboard Shortcut

 New              CTRL + N

 Open             CTRL + O

 Run              F5

 Run Selection    F8

 Stop             CTRL + BREAK . CTRL + C can be used when the context is unambiguous (when there is
 Execution        no text selected).

<!-- p.772 -->

 Action             Keyboard Shortcut

 Tab (to next        CTRL + TAB Note: Tab to next script works only when you have a single Windows
 script)            PowerShell tab open, or when you have more than one Windows PowerShell tab open,
                    but the focus is in the Script Pane.

 Tab (to             CTRL + SHIFT + TAB Note: Tab to previous script works when you have only one
 previous           Windows PowerShell tab open, or if you have more than one Windows PowerShell tab
 script)            open, and the focus is in the Script Pane.

Keyboard shortcuts for customizing the view
You can use the following keyboard shortcuts to customize the view in Windows PowerShell
ISE. They are accessible from all the panes in the application.

                                                                                        ﾉ   Expand table

 Action                                                                      Keyboard Shortcut

 Go to Command (v2) or Console (v3 and later) Pane                           CTRL + D

 Go to Output Pane (v2 only)                                                 CTRL + SHIFT + O

 Go to Script Pane                                                           CTRL + I

 Show Script Pane                                                            CTRL + R

 Hide Script Pane                                                            CTRL + R

 Move Script Pane Up                                                         CTRL + 1

 Move Script Pane Right                                                      CTRL + 2

 Maximize Script Pane                                                        CTRL + 3

 Zoom In                                                                     CTRL + +

 Zoom Out                                                                    CTRL + -

Keyboard shortcuts for debugging scripts
You can use the following keyboard shortcuts when you debug scripts.

                                                                                        ﾉ   Expand table

<!-- p.773 -->

Action                        Keyboard Shortcut         Use in

Run/Continue                   F5                       Script Pane, when debugging a script

Step Into                      F11                      Script Pane, when debugging a script

Step Over                      F10                      Script Pane, when debugging a script

Step Out                       SHIFT + F11              Script Pane, when debugging a script

Display Call Stack             CTRL + SHIFT + D         Script Pane, when debugging a script

List Breakpoints               CTRL + SHIFT + L         Script Pane, when debugging a script

Toggle Breakpoint              F9                       Script Pane, when debugging a script

Remove All Breakpoints         CTRL + SHIFT + F9        Script Pane, when debugging a script

Stop Debugger                  SHIFT + F5               Script Pane, when debugging a script

 ７ Note

 You can also use the keyboard shortcuts designed for the Windows PowerShell console
 when you debug scripts in Windows PowerShell ISE. To use these shortcuts, you must type
 the shortcut in the Command Pane and press ENTER .

                                                                                   ﾉ   Expand table

Action                                       Keyboard            Use in
                                             Shortcut

Continue                                     C                   Console Pane, when debugging a
                                                                 script

Step Into                                    S                   Console Pane, when debugging a
                                                                 script

Step Over                                    V                   Console Pane, when debugging a
                                                                 script

Step Out                                     O                   Console Pane, when debugging a
                                                                 script

Repeat Last Command (for Step Into or Step   ENTER               Console Pane, when debugging a
Over)                                                            script

Display Call Stack                           K                   Console Pane, when debugging a
                                                                 script

<!-- p.774 -->

 Action                                           Keyboard             Use in
                                                  Shortcut

 Stop Debugging                                       Q                Console Pane, when debugging a
                                                                       script

 List the Script                                      L                Console Pane, when debugging a
                                                                       script

 Display Console Debugging Commands                   H or ?           Console Pane, when debugging a
                                                                       script

Keyboard shortcuts for Windows PowerShell tabs
You can use the following keyboard shortcuts when you use Windows PowerShell tabs.

                                                                                         ﾉ   Expand table

 Action                       Keyboard Shortcut

 Close PowerShell Tab          CTRL + W

 New PowerShell Tab            CTRL + T

 Previous PowerShell tab       CTRL + SHIFT + TAB . This shortcut works only when no files are open on any
                              Windows PowerShell tab.

 Next Windows                  CTRL + TAB . This shortcut works only when no files are open on any
 PowerShell tab               Windows PowerShell tab.

Keyboard shortcuts for starting and exiting
You can use the following keyboard shortcuts to exit the Windows PowerShell ISE or to start a
new Windows PowerShell session outside of the ISE.

                                                                                         ﾉ   Expand table

 Action                 Keyboard Shortcut

 Exit                      ALT + F4 closes the ISE.

 Start powershell.exe      CTRL + SHIFT + P opens a new Windows PowerShell session outside of the ISE.

See Also

<!-- p.775 -->

     PowerShell Magazine: The Complete List of Windows PowerShell ISE Keyboard Shortcuts

Last updated on 11/20/2025

<!-- p.776 -->

Accessibility in Windows PowerShell ISE
This topic describes the accessibility features of Windows PowerShell Integrated Scripting
Environment (ISE) that you might find helpful.

     How to change the size and location of the Console and Script Panes
     Keyboard shortcuts for editing text
     Keyboard shortcuts for running scripts
     Keyboard shortcuts for customizing the view
     Keyboard shortcuts for debugging scripts
     Keyboard shortcuts for Windows PowerShell tabs
     Keyboard shortcuts for starting and exiting
     Breakpoint management with cmdlets

Microsoft is committed to making its products and services easier for everyone to use. The
following topics provide information about the features, products, and services that make
Windows PowerShell ISE more accessible for people with disabilities.

In addition to accessibility features and utilities in Microsoft Windows, the following features
make Windows PowerShell ISE more accessible for people with disabilities:

     Keyboard Shortcuts

     Syntax Coloring Table and the ability to modify several other color settings using the
      $psISE.Options scripting object.

     Text Size Change

How to change the size and location of the
Console and Script Panes
You can use the following steps to change the size and location of the Console Pane and the
Script Pane. When you open the Windows PowerShell ISE again, the size and location changes
you made will be retained.

To resize the Script Pane and Console Pane
   1. Pause the pointer on the split line between the Script Pane and Console Pane.
   2. When the mouse pointer changes to a two-headed arrow, drag the border to change the
     size of the pane.

<!-- p.777 -->

To move the Script Pane and Console Pane
Do one of the following:

       To move the Script Pane above the Console Pane, press CTRL + 1 or, on the toolbar, click
       the Show Script Pane Top icon, or in the View menu, click Show Script Pane Top.
       To move the Script Pane to the right of the Console Pane, press CTRL + 2 or, on the
       toolbar, click the Show Script Pane Right icon, or in the View menu, click Show Script
       Pane Right.
       To maximize the Script Pane, press CTRL + 3 or, on the toolbar, click the Show Script Pane
       Maximized icon, or in the View menu, click Show Script Pane Maximized.
       To maximize the Console Pane and hide the Script Pane, on the far right edge of the row
       of tabs, click the Hide Script Pane icon, in the View menu, click to deselect the Show
       Script Pane menu option.
       To display the Script Pane when the Console Pane is maximized, on the far right edge of
       the row of tabs, click the Show Script Pane icon, or in the View menu, click to select the
       Show Script Pane menu option.

Keyboard shortcuts for editing text
You can use the following keyboard shortcuts when you edit text.

                                                                                  ﾉ   Expand table

 Action                           Keyboard Shortcuts            Use in

 Copy                              CTRL + C                     Script Pane, Console Pane

 Cut                               CTRL + X                     Script Pane, Console Pane

 Find in Script                    CTRL + F                     Script Pane

 Find Next in Script               F3                           Script Pane

 Find Previous in Script           SHIFT + F3                   Script Pane

 Paste                             CTRL + V                     Script Pane, Console Pane

 Redo                              CTRL + Y                     Script Pane, Console Pane

 Replace in Script                 CTRL + H                     Script Pane

 Save                              CTRL + S                     Script Pane

 Select All                        CTRL + A                     Script Pane, Console Pane

<!-- p.778 -->

 Action                                   Keyboard Shortcuts              Use in

 Undo                                     CTRL + Z                        Script Pane, Console Pane

Keyboard shortcuts for running scripts
You can use the following keyboard shortcuts when you run scripts in the Script Pane.

                                                                                            ﾉ   Expand table

 Action              Keyboard Shortcut

 New                 CTRL + N

 Open                CTRL + O

 Run                 F5

 Run Selection       F8

 Stop Execution      CTRL + BREAK . CTRL + C can be used when the context is unambiguous (when there is
                     no text selected).

 Tab (to next        CTRL + TAB Note: Tab to next script works only when you have a single PowerShell tab
 script)             open, or when you have more than one PowerShell tab open, but the focus is in the
                     Script Pane.

 Tab (to             CTRL + SHIFT + TAB Note: Tab to previous script works when you have only one
 previous script)    PowerShell tab open, or if you have more than one PowerShell tab open, and the focus
                     is in the Script Pane.

Keyboard shortcuts for customizing the view
You can use the following keyboard shortcuts to customize the view in Windows PowerShell
ISE. They are accessible from all the panes in the application.

                                                                                            ﾉ   Expand table

 Action                                                        Keyboard Shortcut

 Go to Console Pane                                            CTRL + D

 Go to Script Pane                                             CTRL + I

 Show Script Pane                                              CTRL + R

<!-- p.779 -->

 Action                                                Keyboard Shortcut

 Hide Script Pane                                      CTRL + R

 Move Script Pane Up                                   CTRL + 1

 Move Script Pane Right                                CTRL + 2

 Maximize Script Pane                                  CTRL + 3

 Zoom In                                               CTRL + PLUS

 Zoom Out                                              CTRL + MINUS

Keyboard shortcuts for debugging scripts
You can use the following keyboard shortcuts when you debug scripts.

                                                                                   ﾉ   Expand table

 Action                      Keyboard Shortcut          Use in

 Run/Continue                 F5                        Script Pane, when debugging a script

 Step Into                    F11                       Script Pane, when debugging a script

 Step Over                    F10                       Script Pane, when debugging a script

 Step Out                     SHIFT + F11               Script Pane, when debugging a script

 Display Call Stack           CTRL + SHIFT + D          Script Pane, when debugging a script

 List Breakpoints             CTRL + SHIFT + L          Script Pane, when debugging a script

 Toggle Breakpoint            F9                        Script Pane, when debugging a script

 Remove All Breakpoints       CTRL + SHIFT + F9         Script Pane, when debugging a script

 Stop Debugger                SHIFT + F5                Script Pane, when debugging a script

  ７ Note

  You can also use the keyboard shortcuts designed for the Windows PowerShell console
  when you debug scripts in Windows PowerShell ISE. To use these shortcuts, you must type
  the shortcut in the Console Pane and press ENTER .

<!-- p.780 -->

                                                                                   ﾉ   Expand table

 Action                                   Keyboard Shortcut   Use in

 Continue                                 C                   Console Pane, when debugging a script

 Step Into                                S                   Console Pane, when debugging a script

 Step Over                                V                   Console Pane, when debugging a script

 Step Out                                 O                   Console Pane, when debugging a script

 Repeat Last Command                      ENTER               Console Pane, when debugging a script
 (Step Into/Over)

 Display Call Stack                       K                   Console Pane, when debugging a script

 Stop Debugging                           Q                   Console Pane, when debugging a script

 List the Script                          L                   Console Pane, when debugging a script

 Display Console Debugging Commands       H or ?              Console Pane, when debugging a script

Keyboard shortcuts for Windows PowerShell tabs
You can use the following keyboard shortcuts when you use Windows PowerShell tabs.

                                                                                   ﾉ   Expand table

 Action                       Keyboard Shortcut

 Close PowerShell Tab          CTRL + W

 New PowerShell Tab            CTRL + T

 Previous PowerShell tab       CTRL + SHIFT + TAB (Only when no files are open on any PowerShell
                              tab)

 Next Windows PowerShell       CTRL + TAB (Only when no files are open on any PowerShell tab)
 tab

Keyboard shortcuts for starting and exiting
You can use the following keyboard shortcuts to start the Windows PowerShell console
( powershell.exe ) or to exit Windows PowerShell ISE.

<!-- p.781 -->

                                                                               ﾉ   Expand table

 Action                                                             Keyboard Shortcut

 Exit                                                               ALT + F4

 Start powershell.exe (Windows PowerShell console)                  CTRL + SHIFT + P

Breakpoint Management
For the visually impaired, breakpoint information is available through the cmdlets for managing
breakpoints, such as Get-PSBreakpoint and Set-PSBreakpoint. For more information please see
'How to manage breakpoints' in How to Debug Scripts in the Windows PowerShell ISE.

See Also
Introducing the Windows PowerShell ISE

Last updated on 11/20/2025

<!-- p.782 -->

Windows Management Framework
08/29/2025

Windows Management Framework (WMF) provides a consistent management interface for
Windows. WMF provides a seamless way to manage various versions of Windows client and
Windows Server. WMF installer packages contain updates to management functionality and are
available for older versions of Windows.

  ７ Note

  WMF 5.1 is the only supported version of WMF and is included in all currently supported
  versions of Windows. This information in this article provides a history of WMF versions.

WMF installation adds and/or updates the following features:

     Windows PowerShell
     Windows PowerShell Desired State Configuration (DSC)
     Windows PowerShell Integrated Script Environment (ISE)
     Windows Remote Management (WinRM)
     Windows Management Instrumentation (WMI)
     Windows PowerShell Web Services (Management OData IIS Extension)
     Software Inventory Logging (SIL)
     Server Manager CIM Provider

WMF Release Notes
To learn about the enhancements in Windows PowerShell and other components, see the
release notes for each version of WMF:

     WMF 5.1
     WMF 5.0

WMF availability across Windows operating
systems
                                                                               ﾉ   Expand table

<!-- p.783 -->

OS Version               End of        WMF 5.1         WMF        WMF        WMF        WMF
                         Support                       5.0        4.0        3.0        2.0

Windows Server 2022      2031-10-14    Included

Windows Server 2019      2029-01-09    Included

Windows Server 2016      2027-01-11    Included

Windows 11               2025-10-14    Included

Windows 10               2025-10-14    Included in     Included
                                       1607+

Windows Server 2012      Out of        Yes             Yes        Included
R2                       support

Windows 8.1              Out of        Yes             Yes        Included
                         support

Windows Server 2012      Out of        Yes             Yes        Yes        Included
                         support

Windows 8                Out of                                              Included
                         support

Windows Server 2008      Out of        Yes             Yes        Yes        Yes        Included
R2 SP1                   support

Windows 7 SP1            Out of        Yes             Yes        Yes        Yes        Included
                         support

Windows Server 2008      Out of                                              Yes        Yes
SP2                      support

Windows Vista            Out of                                                         Yes
                         support

Windows Server 2003      Out of                                                         Yes
                         support

Windows XP               Out of                                                         Yes
                         support

      Included: The features of the specified version of WMF were shipped in the indicated
      version of Windows client or Windows Server.
      Out of support: Microsoft no longer supports these products. You must upgrade to a
      supported version. For more information, see the Microsoft Lifecycle Policy   page.

 ７ Note

<!-- p.784 -->

The version of WMF that shipped in an operating system is supported for the lifetime of
support for that version of the operating system. The standalone installers for WMF 5.0
and older are no longer available or supported.

<!-- p.785 -->

PowerShell Security
Learn about PowerShell's security features and best practices.

   Security features

   ｅ OVERVIEW
   PowerShell security features

   Using App Control for Business

   ｃ HOW-TO GUIDE
   Preventing script injection attacks

   Securing a restricted PowerShell remoting session

   PowerShell remoting

   ｐ CONCEPT
   Running remote commands

   Using WS-Management (WSMan) Remoting in PowerShell

   Security Considerations for PowerShell Remoting using WinRM

   PowerShell Remoting FAQ

   ｃ HOW-TO GUIDE
   Making the second hop in PowerShell Remoting

   PowerShell remoting over SSH

   Just Enough Administration (JEA)

   ｐ CONCEPT
   Overview

<!-- p.786 -->

Prerequisites

JEA Role Capabilities

Session configurations

Security considerations

ｃ HOW-TO GUIDE
Registering JEA Configurations

Using JEA

Auditing and Reporting on JEA

Using App Control

ｅ OVERVIEW
Using App Control for Business

How App Control works with PowerShell

ｃ HOW-TO GUIDE
How to use App Control to secure PowerShell

Managing secrets

ｐ CONCEPT
Overview of the SecretManagement and SecretStore modules

Understanding the security features of SecretManagement and SecretStore

ｃ HOW-TO GUIDE
Managing a SecretStore vault

Use the SecretStore in automation

Use Azure Key Vault in automation

ｉ REFERENCE

<!-- p.787 -->

Microsoft.PowerShell.SecretManagement module

Microsoft.PowerShell.SecretStore module

<!-- p.788 -->

PowerShell security features
PowerShell has several features designed to improve the security of your scripting environment.

Execution policy
PowerShell's execution policy is a safety feature that controls the conditions under which
PowerShell loads configuration files and runs scripts. This feature helps prevent the execution of
malicious scripts. You can use a Group Policy setting to set execution policies for computers and
users. Execution policies only apply to the Windows platform.

For more information, see about_Execution_Policies.

Use of the SecureString class
PowerShell has several cmdlets that support the use of the System.Security.SecureString class.
And, as with any .NET class, you can use SecureString in your own scripts. However, Microsoft
doesn't recommend using SecureString for new development. Microsoft recommends that you
avoid using passwords and rely on other means to authenticate, such as certificates or Windows
authentication.

PowerShell continues to support the SecureString class for backward compatibility. Using a
SecureString is still more secure than using a plain text string. PowerShell still relies on the
SecureString type to avoid accidentally exposing the contents to the console or in logs. Use
SecureString carefully, because it can be easily converted to a plain text string. For a full
discussion about using SecureString, see the System.Security.SecureString class documentation.

Module and script block logging
Module Logging allows you to enable logging for selected PowerShell modules. This setting is
effective in all sessions on the computer. PowerShell records pipeline execution events for the
specified modules in the Windows PowerShell event log.

Script Block Logging enables logging for the processing of commands, script blocks, functions,
and scripts - whether invoked interactively, or through automation. PowerShell logs this
information to the Microsoft-Windows-PowerShell/Operational event log.

For more information, see the following articles:

<!-- p.789 -->

     about_Group_Policy_Settings
     about_Logging_Windows
     about_Logging_Non-Windows

AMSI Support
The Windows Antimalware Scan Interface (AMSI) is an API that allows applications to pass actions
to an antimalware scanner, such as Windows Defender, to scan for malicious payloads. Beginning
with PowerShell 5.1, PowerShell running on Windows 10 (and higher) passes all script blocks to
AMSI.

PowerShell 7.3 extends the data it sends to AMSI for inspection. It now includes all .NET method
invocations.

For more information about AMSI, see How AMSI helps.

Constrained language mode
ConstrainedLanguage mode protects your system by limiting the cmdlets and .NET types
allowed in a PowerShell session. For a full description, see about_Language_Modes.

Application Control
Windows 10 includes two technologies, App Control for Business and AppLocker that you can
use to control applications. PowerShell detects if a system wide application control policy is being
enforced. The policy applies certain behaviors when running script blocks, script files, or loading
module files to prevent arbitrary code execution on the system.

App Control for Business is designed as a security feature under the servicing criteria defined by
the Microsoft Security Response Center (MSRC). App Control for Business is the preferred
application control system for Windows. For more information about how PowerShell supports
AppLocker and App Control for Business, see Use App Control to secure PowerShell.

AppLocker is a legacy application control system that's still supported in and Windows 11.
AppLocker isn't a security feature under the servicing criteria defined by MSRC. For more
information about servicing criteria, see Microsoft Security Servicing Criteria for Windows   .

System Lockdown mode

<!-- p.790 -->

In PowerShell, System Lockdown mode is an abstraction of the system-wide application control
policy enforced by Windows through App Control for Business or AppLocker. When an
application control policy is active, PowerShell enters System Lockdown mode. In System
Lockdown mode, the application control policy determines the language mode for each
runspace.

  ） Important

  Without System Lockdown mode, language mode doesn't propagate between runspaces.
  Each runspace independently queries the Windows application control policy to determine
  its language mode. Setting the language mode on one runspace doesn't affect other
  runspaces. Without an active application control policy, new runspaces default to
  FullLanguage mode.

Software Bill of Materials (SBOM)
Beginning with PowerShell 7.2, all install packages contain a Software Bill of Materials (SBOM).
The PowerShell team also produces SBOMs for modules that they own but ship independently
from PowerShell.

You can find SBOM files in the following locations:

     In PowerShell, find the SBOM at $PSHOME/_manifest/spdx_2.2/manifest.spdx.json .
     For modules, find the SBOM in the module's folder under
     _manifest/spdx_2.2/manifest.spdx.json .

The creation and publishing of the SBOM is the first step to modernize Federal Government
cybersecurity and enhance software supply chain security. For more information about this
initiative, see the blog post Generating SBOMs with SPDX at Microsoft     .

Secure data transfer in PowerShell remoting
Prior to PowerShell v7.6-preview5, a Session_Key is used to encrypt a SecureString before
sending it a PowerShell remote session. The PowerShell Remoting Protocol (PSRP) performs a key
exchange between client and server when a SecureString object needs to be transferred. The
exchange involves the following steps:

   1. The client side generates a public/private key pair and sends the public key to the server.
   2. The server generates a session key for symmetric encryption.

<!-- p.791 -->

   3. The server uses the public key to encrypt the session key and sends it to the client.
   4. Both the client and server use the new session key to encrypt a SecureString object.

The PowerShell Remoting Protocol (PSRP) uses the RSAEncryptionPadding.Pkcs1 algorithm during
the key exchange. The algorithm is NOT secure, so the key exchange doesn't provide any extra
security.

  ） Important

  You must use a secure transport layer to ensure secure data transfer over PSRP.

Beginning in PowerShell v7.6-preview.5, the key exchange was deprecated. The version of PSRP
was incremented to v2.4 and includes the following changes:

     The following PSRP messages are deprecated when both client and server are v2.4 or
     higher:
            PUBLIC_KEY
            PUBLIC_KEY_REQUEST
            ENCRYPTED_SESSION_KEY

     The encryption and decryption steps for SecureString are skipped when both client and
     server are v2.4 or higher.

This change is backward compatible.

     For old clients or servers (v2.3 or lower), the key exchange is still used when needed.
     PSRP can use a named pipe remote sessions when both client and server are on the same
     machine. Since it's possible for a remote client to connect to named pipe and the data is no
     longer encrypted with a session key, the named pipe (used for Enter-PSHostProcess ) rejects
     the remote client.

Security Servicing Criteria
A security boundary provides a logical separation between the code and data of security domains
with different levels of trust. Security features build upon security boundaries to provide robust
protection against specific threats. For security features in this category, Microsoft intends to
address reported vulnerabilities through servicing.

Security features of PowerShell

<!-- p.792 -->

      System Lockdown with App Control for Business
      Constrained language mode with App Control for Business

For more information, see the Microsoft Security Servicing Criteria for Windows
documentation.

In some cases, a security feature may provide protection against a threat without being able to
provide a robust defense. These security features are typically referred to as defense-in-depth
features or mitigations because they provide additional security but may have by-design
limitations that prevent them from fully mitigating a threat. A bypass for a defense-in-depth
security feature by itself does not pose a direct risk because an attacker must also have found a
vulnerability that affects a security boundary, or they must rely on additional techniques, such as
social engineering to achieve the initial stage of a device compromise.

Defense-in-depth features of PowerShell

      Constrained language mode with AppLocker or configured through session configuration or
      by manually setting $ExecutionContext.SessionState.LanguageMode
      System Lockdown with AppLocker
      Execution Policy

 Last updated on 07/17/2026

<!-- p.793 -->

Use App Control to secure PowerShell
Windows 10 includes two technologies, App Control for Business and AppLocker, that you can
use to control applications. They allow you to create a lockdown experience to help secure
your PowerShell environment.

AppLocker builds on the application control features of Software Restriction Policies.
AppLocker allows you to create rules to allow or deny apps for specific users or groups. You
identify the apps based on unique properties of the files.

Application Control for Business, introduced in Windows 10 as Windows Defender Application
Control (WDAC), allows you to control which drivers and applications are allowed to run on
Windows.

Lockdown policy detection
PowerShell detects both AppLocker and App Control for Business system wide policies.
AppLocker doesn't have way to query the policy enforcement status. To detect that AppLocker
is enforcing a policy, PowerShell creates two temporary files and tries to run them. The
filenames use the following name format:

     $Env:TEMP/__PSScriptPolicyTest_<random-8dot3-name>.ps1

     $Env:TEMP/__PSScriptPolicyTest_<random-8dot3-name>.psm1

App Control for Business is the preferred application control system for Windows. App Control
puts the system into System Lockdown mode. System Lockdown mode is the feature that
detects the policies and determines if a context needs to be initialized or changed to a specific
language mode.

App Control is designed as a security feature under the servicing criteria defined by the
Microsoft Security Response Center (MSRC). For more information, see Application Controls for
Windows and App Control and AppLocker feature availability.

  ７ Note

  When choosing between App Control or AppLocker, we recommend that you implement
  application control using App Control for Business rather than AppLocker. Microsoft is no
  longer investing in AppLocker. AppLocker will only receive security fixes.

App Control policy enforcement

<!-- p.794 -->

When PowerShell runs under an App Control policy, its behavior changes based on the defined
security policy. Under an App Control policy, PowerShell runs trusted scripts and modules
allowed by the policy in FullLanguage mode. All other scripts and script blocks are untrusted
and run in ConstrainedLanguage mode. PowerShell throws errors when the untrusted scripts
attempt to perform actions that aren't allowed in ConstrainedLanguage mode. It can be difficult
to know why a script failed to run correctly in ConstrainedLanguage mode.

App Control policy auditing
PowerShell 7.4 added a new feature to support App Control policies in Audit mode. In audit
mode, PowerShell runs the untrusted scripts in ConstrainedLanguage mode without errors, but
logs messages to the event log instead. The log messages describe what restrictions would
apply if the policy were in Enforce mode.

History of changes
Windows PowerShell 5.1 was the first version of PowerShell to support App Control. The
security features of App Control and AppLocker improve with each new release of PowerShell.
The following sections describe how this support changed in each version of PowerShell. The
changes are cumulative, so the features described in the later versions include changes from
earlier versions.

Changes in PowerShell 7.4
On Windows, when PowerShell runs under an App Control policy, its behavior changes based
on the defined security policy. Under an App Control policy, PowerShell runs trusted scripts
and modules allowed by the policy in FullLanguage mode. All other scripts and script blocks
are untrusted and run in ConstrainedLanguage mode. PowerShell throws errors when the
untrusted scripts attempt to perform disallowed actions. It's difficult to know why a script fails
to run correctly in ConstrainedLanguage mode.

PowerShell 7.4 now supports App Control policies in Audit mode. In audit mode, PowerShell
runs the untrusted scripts in ConstrainedLanguage mode but logs messages to the event log
instead of throwing errors. The log messages describe what restrictions would apply if the
policy were in Enforce mode.

Changes in PowerShell 7.3

<!-- p.795 -->

     PowerShell 7.3 now supports the ability to block or allow PowerShell script files via the
     App Control API.

Changes in PowerShell 7.2
     There was a corner-case scenario in AppLocker where you only have Deny rules and
     constrained mode isn't used to enforce the policy that allows you to bypass the execution
     policy. Beginning in PowerShell 7.2, a change was made to ensure AppLocker rules take
     precedence over a Set-ExecutionPolicy -ExecutionPolicy Bypass command.

     PowerShell 7.2 now disallows the use of the Add-Type cmdlet in a NoLanguage mode
     PowerShell session on a locked down machine.

     PowerShell 7.2 now disallows scripts from using COM objects in AppLocker system
     lockdown conditions. Cmdlets that use COM or DCOM internally aren't affected.

Further reading
     For more information about how App Control works and what restrictions it enforces, see
     How App Control works with PowerShell.
     For more information about securing PowerShell with App Control, see How to use App
     Control.

Last updated on 01/26/2026

<!-- p.796 -->

How App Control works with PowerShell
This article explains how App Control for Business secures PowerShell and the restrictions it
imposes. The secure behavior of PowerShell varies based on the version of Windows and
PowerShell you're using.

How PowerShell detects a system lockdown policy
PowerShell detects both AppLocker and App Control for Business system wide polices.
AppLocker is deprecated. App Control is the preferred application control system for Windows.

Legacy App Control policy enforcement detection
PowerShell uses the legacy App Control WldpGetLockdownPolicy API to discover two things:

     System wide policy enforcement: None , Audit , Enforce
     Individual file policy: None , Audit (allowed by policy), Enforce (not allowed by policy)

All versions of PowerShell (v5.1 - v7.x) support this App Control policy detection.

Latest App Control policy enforcement detection
App Control introduced new APIs in recent versions of Windows. Beginning with version 7.3,
PowerShell uses the new WldpCanExecuteFile API to decide how a file should be handled.
Windows PowerShell 5.1 doesn't support this new API. The new API takes precedence over the
legacy API for individual files. However, PowerShell continues to use the legacy API to get the
system wide policy configuration. If the new API isn't available, PowerShell falls back to the old
API behavior.

The new API provides the following information for each file:

      WLDP_CAN_EXECUTE_ALLOWED
      WLDP_CAN_EXECUTE_BLOCKED

      WLDP_CAN_EXECUTE_REQUIRE_SANDBOX

PowerShell behavior under lockdown policy
PowerShell can run in both interactive and non-interactive modes.

     In interactive mode, PowerShell is a command-line application that takes users command-
     line input as commands or scripts to run. Results are displayed back to the user.

<!-- p.797 -->

      In non-interactive mode, PowerShell loads modules and runs script files without user
      input. Result data streams are either ignored or redirected to a file.

Interactive mode running under policy enforcement
PowerShell runs commands in ConstrainedLanguage mode. This mode prevents interactive
users from running certain commands or executing arbitrary code. For more information about
the restrictions in this mode, see the PowerShell restrictions under lockdown policy section of
this article.

Noninteractive mode running under policy enforcement
When PowerShell runs a script or loads a module, it uses the App Control API to get the policy
enforcement for the file.

PowerShell version 7.3 or higher uses the WldpCanExecuteFile API if available. This API returns
one of the following results:

      WLDP_CAN_EXECUTE_ALLOWED : The policy allows the file for use in FullLanguage mode with a

      few restrictions.
      WLDP_CAN_EXECUTE_BLOCKED : The policy disallows the file. PowerShell throws an error when

      the file is run or loaded.
      WLDP_CAN_EXECUTE_REQUIRE_SANDBOX : The policy doesn't approve the file, but it can be run

      or loaded in ConstrainedLanguage mode.

In Windows PowerShell 5.1 or if WldpCanExecuteFile API isn't available, PowerShell's per file
behavior is:

      None : The file is run loaded in FullLanguage mode with a few restrictions.

      Audit : The file is run or loaded in FullLanguage mode with no restrictions. In PowerShell

      7.4 or higher, the policy logs restriction information to the Windows event logs.
      Enforce : The file is run or loaded in ConstrainedLanguage mode.

PowerShell restrictions under lockdown policy
When PowerShell detects the system is under an App Control lockdown policy, it applies
restrictions even if the script is trusted and running in FullLanguage mode. These restrictions
prevent known behaviors of PowerShell that could result in arbitrary code execution on a
locked-down system. The lockdown policy enforces the following restrictions:

      Module dot-sourcing with wildcard function export restriction

<!-- p.798 -->

Any module that uses script dot-sourcing and exports functions using wildcard names
results in an error. Blocking wildcard exports prevents script injection from a malicious
user who can plant an untrusted script that gets dot-sourced into a trusted module. The
malicious script could then gain access to the trusted module's private functions.

Security recommendation: Never use script dot-sourcing in a module and always export
module functions with explicit names (no wildcard characters).

Nested module with wildcard function export restriction

If a parent module exports functions using function name wildcard characters, PowerShell
removes any function name in a nested module from the function export list. Blocking
wildcard exports from nested modules prevents accidental exporting of dangerous nested
functions through wildcard name matching.

Security recommendation: Always export module functions with explicit names (no
wildcard characters).

Interactive shell parameter type conversion

When the system is locked down, interactive PowerShell sessions run in
ConstrainedLanguage mode to prevent arbitrary code execution. Trusted modules loaded

into the session run in FullLanguage mode. If a trusted module cmdlet uses complex
types for its parameters, type conversion during parameter binding can fail if the
conversion isn't allowed across trust boundaries. The failure occurs when PowerShell tries
to convert a value by running a type constructor. Type constructors aren't allowed to run
in ConstrainedLanguage mode.

In this example, parameter binding type conversion is normally allowed, but fails when
run in ConstrainedLanguage mode. The ConnectionPort type constructor isn't allowed:

 PowerShell
 PS> Create-ConnectionOnPort -Connection 22
 Create-ConnectionOnPort: Cannot bind parameter 'Connection'. Cannot convert the
 "22"
 value of type "System.Int32" to type "ConnectionPort".

Enter-PSHostProcess cmdlet disallowed

The Enter-PSHostProcess cmdlet is disabled and throws an error if used. This command is
used for attach-and-debug sessions. It allows you to connect to any other PowerShell
session on the local machine. The cmdlet is disabled to prevent information disclosure
and arbitrary code execution.

<!-- p.799 -->

PowerShell restrictions under constrained
language mode
A script or function not approved by the App Control policy is untrusted. When you run an
untrusted command, PowerShell either blocks the command from running (new behavior) or
runs the command in ConstrainedLanguage mode. The following restrictions apply to
ConstrainedLanguage mode:

     Add-Type cmdlet disallowed

     Blocking Add-Type prevents the execution of arbitrary .NET code.

     Import-LocalizedData cmdlet restricted

     Blocking the SupportedCommand parameter of Import-LocalizedData prevents the
     execution of arbitrary code.

     Invoke-Expression cmdlet restricted

     All script blocks passed to the Invoke-Expression cmdlet are run in ConstrainedLanguage
     mode to prevent arbitrary code execution.

     New-Object cmdlet restricted

     The New-Object cmdlet is restricted to use only allowed .NET and COM types, to prevent
     access to untrusted types.

     ForEach-Object cmdlet restriction

     Type method invocation for variables passed to the ForeEach-Object is disallowed for any
     .NET type not in the approved list. In general, ConstrainedLanguage mode disallows any
     object method invocation except for approved .NET types to prevent access to untrusted
     .NET types.

     Export-ModuleMember cmdlet restriction

     Using Export-ModuleMember cmdlet to export functions in a nested module script file
     where the child module isn't trusted and the parent module is trusted, results in an error.
     Blocking this scenario prevents a malicious untrusted module from exporting dangerous
     functions from a trusted module.

     New-Module cmdlet restriction

<!-- p.800 -->

When you run New-Module in a trusted script, any script block provided by the
ScriptBlock parameter is marked to run in ConstrainedLanguage mode to prevent the

injection of arbitrary code into a trusted execution context.

Configuration keyword not allowed

The Configuration language keyword isn't allowed in ConstrainedLanguage mode to
prevent code injection attacks.

class keyword not allowed

The class language keyword isn't allowed in ConstrainedLanguage mode to prevent the
injection of arbitrary code.

Script Block processing scope restrictions

Child script blocks aren't allowed to run in parent script block scopes if the script blocks
have different trust levels. For example, you create a child relationship when you dot-
source one script into another. Blocking this scenario prevents an untrusted script from
getting access to dangerous functions in the trusted script scope.

Prevent command discovery of untrusted script functions

PowerShell command discovery doesn't return functions from an untrusted source, such
as an untrusted script or module, to a trusted function. Blocking discovery of untrusted
commands prevents code injection through command planting.

Hashtable to object conversion not allowed

ConstrainedLanguage mode blocks hashtable to object conversions in the Data sections

of PowerShell data ( .psd1 ) files to prevent potential code injection attacks.

Automatic type conversion restricted

ConstrainedLanguage mode blocks automatic type conversion except for a small set of

approved safe types to prevent potential code injection attacks.

Implicit module function export restriction

If a module doesn't explicitly export functions, PowerShell implicitly exports all defined
module functions automatically as a convenience feature. In ConstrainedLanguage mode,
implicit exports no longer occur when a module is loaded across trust boundaries.
Blocking implicit exports prevents unintended exposure of dangerous module functions
not meant for public use.
