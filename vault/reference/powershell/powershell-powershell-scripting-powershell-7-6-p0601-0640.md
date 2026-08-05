---
title: "How to use this documentation — pages 601-640"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0601-0640
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0601-0640
family: powershell
documentKind: "doc"
abstract: "Multiple-selection list boxes Article • 12/09/2022 This sample only applies to Windows platforms. Use Windows PowerShell 3.0 and later releases to create a multiple-selection list box control in a custom Windows Form. Create list box controls that allow multiple selections Copy"
---

# How to use this documentation — pages 601-640

<!-- p.601 -->

Multiple-selection list boxes
Article • 12/09/2022

  This sample only applies to Windows platforms.

Use Windows PowerShell 3.0 and later releases to create a multiple-selection list box
control in a custom Windows Form.

Create list box controls that allow multiple
selections
Copy and then paste the following into Windows PowerShell ISE, and then save it as a
PowerShell script ( .ps1 ) file.

  PowerShell

  Add-Type -AssemblyName System.Windows.Forms
  Add-Type -AssemblyName System.Drawing

  $form = New-Object System.Windows.Forms.Form
  $form.Text = 'Data Entry Form'
  $form.Size = New-Object System.Drawing.Size(300,200)
  $form.StartPosition = 'CenterScreen'

  $OKButton = New-Object System.Windows.Forms.Button
  $OKButton.Location = New-Object System.Drawing.Point(75,120)
  $OKButton.Size = New-Object System.Drawing.Size(75,23)
  $OKButton.Text = 'OK'
  $OKButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
  $form.AcceptButton = $OKButton
  $form.Controls.Add($OKButton)

  $CancelButton = New-Object System.Windows.Forms.Button
  $CancelButton.Location = New-Object System.Drawing.Point(150,120)
  $CancelButton.Size = New-Object System.Drawing.Size(75,23)
  $CancelButton.Text = 'Cancel'
  $CancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
  $form.CancelButton = $CancelButton
  $form.Controls.Add($CancelButton)

  $label = New-Object System.Windows.Forms.Label
  $label.Location = New-Object System.Drawing.Point(10,20)
  $label.Size = New-Object System.Drawing.Size(280,20)
  $label.Text = 'Please make a selection from the list below:'
  $form.Controls.Add($label)

  $listBox = New-Object System.Windows.Forms.Listbox

<!-- p.602 -->

  $listBox.Location = New-Object System.Drawing.Point(10,40)
  $listBox.Size = New-Object System.Drawing.Size(260,20)

  $listBox.SelectionMode = 'MultiExtended'

  [void] $listBox.Items.Add('Item 1')
  [void] $listBox.Items.Add('Item 2')
  [void] $listBox.Items.Add('Item 3')
  [void] $listBox.Items.Add('Item 4')
  [void] $listBox.Items.Add('Item 5')

  $listBox.Height = 70
  $form.Controls.Add($listBox)
  $form.Topmost = $true

  $result = $form.ShowDialog()

  if ($result -eq [System.Windows.Forms.DialogResult]::OK)
  {
      $x = $listBox.SelectedItems
      $x
  }

The script begins by loading two .NET Framework classes: System.Drawing and
System.Windows.Forms. You then start a new instance of the .NET Framework class
System.Windows.Forms.Form. That provides a blank form or window to which you can
start adding controls.

  PowerShell

  $form = New-Object System.Windows.Forms.Form

After you create an instance of the Form class, assign values to three properties of this
class.

         Text. This becomes the title of the window.
         Size. This is the size of the form, in pixels. The preceding script creates a form
         that's 300 pixels wide by 200 pixels tall.
         StartingPosition. This optional property is set to CenterScreen in the preceding
         script. If you don't add this property, Windows selects a location when the form is
         opened. By setting the StartingPosition to CenterScreen, you're automatically
         displaying the form in the middle of the screen each time it loads.

  PowerShell

  $form.Text = 'Data Entry Form'
  $form.Size = New-Object System.Drawing.Size(300,200)

<!-- p.603 -->

  $form.StartPosition = 'CenterScreen'

Next, create an OK button for your form. Specify the size and behavior of the OK button.
In this example, the button position is 120 pixels from the form's top edge, and 75 pixels
from the left edge. The button height is 23 pixels, while the button length is 75 pixels.
The script uses predefined Windows Forms types to determine the button behaviors.

  PowerShell

  $OKButton = New-Object System.Windows.Forms.Button
  $OKButton.Location = New-Object System.Drawing.Size(75,120)
  $OKButton.Size = New-Object System.Drawing.Size(75,23)
  $OKButton.Text = 'OK'
  $OKButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
  $form.AcceptButton = $OKButton
  $form.Controls.Add($OKButton)

Similarly, you create a Cancel button. The Cancel button is 120 pixels from the top, but
150 pixels from the left edge of the window.

  PowerShell

  $CancelButton = New-Object System.Windows.Forms.Button
  $CancelButton.Location = New-Object System.Drawing.Point(150,120)
  $CancelButton.Size = New-Object System.Drawing.Size(75,23)
  $CancelButton.Text = 'Cancel'
  $CancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
  $form.CancelButton = $CancelButton
  $form.Controls.Add($CancelButton)

Next, provide label text on your window that describes the information you want users
to provide.

  PowerShell

  $label = New-Object System.Windows.Forms.Label
  $label.Location = New-Object System.Drawing.Point(10,20)
  $label.Size = New-Object System.Drawing.Size(280,20)
  $label.Text = 'Please make a selection from the list below:'
  $form.Controls.Add($label)

Add the control (in this case, a list box) that lets users provide the information you've
described in your label text. There are many other controls you can apply besides text
boxes; for more controls, see System.Windows.Forms Namespace.

  PowerShell

<!-- p.604 -->

   $listBox = New-Object System.Windows.Forms.Listbox
   $listBox.Location = New-Object System.Drawing.Point(10,40)
   $listBox.Size = New-Object System.Drawing.Size(260,20)

Here's how you specify that you want to allow users to select multiple values from the
list.

   PowerShell

   $listBox.SelectionMode = 'MultiExtended'

In the next section, you specify the values you want the list box to display to users.

   PowerShell

   [void] $listBox.Items.Add('Item 1')
   [void] $listBox.Items.Add('Item 2')
   [void] $listBox.Items.Add('Item 3')
   [void] $listBox.Items.Add('Item 4')
   [void] $listBox.Items.Add('Item 5')

Specify the maximum height of the list box control.

   PowerShell

   $listBox.Height = 70

Add the list box control to your form, and instruct Windows to open the form atop other
windows and dialog boxes when it's opened.

   PowerShell

   $form.Controls.Add($listBox)
   $form.Topmost = $true

Add the following line of code to display the form in Windows.

   PowerShell

   $result = $form.ShowDialog()

Finally, the code inside the if block instructs Windows what to do with the form after
users select one or more options from the list box, and then click the OK button or press

<!-- p.605 -->

the Enter key.

  PowerShell

  if ($result -eq [System.Windows.Forms.DialogResult]::OK)
  {
      $x = $listBox.SelectedItems
      $x
  }

See also
     Weekend Scripter: Fixing PowerShell GUI Examples
     GitHub: Dave Wyatt's WinFormsExampleUpdates
     Windows PowerShell Tip of the Week: Multi-Select List Boxes - And More!)

<!-- p.606 -->

Selecting items from a list box
  This sample only applies to Windows platforms.

Use Windows PowerShell 3.0 and later releases to create a dialog box that lets users select
items from a list box control.

Create a list box control, and select items from it
Copy and then paste the following into Windows PowerShell ISE, and then save it as a
PowerShell script ( .ps1 ) file.

  PowerShell

  Add-Type -AssemblyName System.Windows.Forms
  Add-Type -AssemblyName System.Drawing

  $form = New-Object System.Windows.Forms.Form
  $form.Text = 'Select a Computer'
  $form.Size = New-Object System.Drawing.Size(300,200)
  $form.StartPosition = 'CenterScreen'

  $okButton = New-Object System.Windows.Forms.Button
  $okButton.Location = New-Object System.Drawing.Point(75,120)
  $okButton.Size = New-Object System.Drawing.Size(75,23)
  $okButton.Text = 'OK'
  $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
  $form.AcceptButton = $okButton
  $form.Controls.Add($okButton)

  $cancelButton = New-Object System.Windows.Forms.Button
  $cancelButton.Location = New-Object System.Drawing.Point(150,120)
  $cancelButton.Size = New-Object System.Drawing.Size(75,23)
  $cancelButton.Text = 'Cancel'
  $cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
  $form.CancelButton = $cancelButton
  $form.Controls.Add($cancelButton)

  $label = New-Object System.Windows.Forms.Label
  $label.Location = New-Object System.Drawing.Point(10,20)
  $label.Size = New-Object System.Drawing.Size(280,20)
  $label.Text = 'Please select a computer:'
  $form.Controls.Add($label)

  $listBox = New-Object System.Windows.Forms.ListBox
  $listBox.Location = New-Object System.Drawing.Point(10,40)
  $listBox.Size = New-Object System.Drawing.Size(260,20)

<!-- p.607 -->

 $listBox.Height = 80

 [void] $listBox.Items.Add('atl-dc-001')
 [void] $listBox.Items.Add('atl-dc-002')
 [void] $listBox.Items.Add('atl-dc-003')
 [void] $listBox.Items.Add('atl-dc-004')
 [void] $listBox.Items.Add('atl-dc-005')
 [void] $listBox.Items.Add('atl-dc-006')
 [void] $listBox.Items.Add('atl-dc-007')

 $form.Controls.Add($listBox)

 $form.Topmost = $true

 $result = $form.ShowDialog()

 if ($result -eq [System.Windows.Forms.DialogResult]::OK)
 {
     $x = $listBox.SelectedItem
     $x
 }

The script begins by loading two .NET Framework classes: System.Drawing and
System.Windows.Forms. You then start a new instance of the .NET Framework class
System.Windows.Forms.Form. That provides a blank form or window to which you can start
adding controls.

 PowerShell

 Add-Type -AssemblyName System.Windows.Forms
 Add-Type -AssemblyName System.Drawing

After you create an instance of the Form class, assign values to three properties of this class.

     Text. This becomes the title of the window.
     Size. This is the size of the form, in pixels. The preceding script creates a form that's 300
     pixels wide by 200 pixels tall.
     StartingPosition. This optional property is set to CenterScreen in the preceding script. If
     you don't add this property, Windows selects a location when the form is opened. By
     setting the StartingPosition to CenterScreen, you're automatically displaying the form in
     the middle of the screen each time it loads.

 PowerShell

 $form.Text = 'Select a Computer'
 $form.Size = New-Object System.Drawing.Size(300,200)

<!-- p.608 -->

 $form.StartPosition = 'CenterScreen'

Next, create an OK button for your form. Specify the size and behavior of the OK button. In this
example, the button position is 120 pixels from the form's top edge, and 75 pixels from the left
edge. The button height is 23 pixels, while the button length is 75 pixels. The script uses
predefined Windows Forms types to determine the button behaviors.

 PowerShell

 $okButton = New-Object System.Windows.Forms.Button
 $okButton.Location = New-Object System.Drawing.Point(75,120)
 $okButton.Size = New-Object System.Drawing.Size(75,23)
 $okButton.Text = 'OK'
 $okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
 $form.AcceptButton = $okButton
 $form.Controls.Add($okButton)

Similarly, you create a Cancel button. The Cancel button is 120 pixels from the top, but 150
pixels from the left edge of the window.

 PowerShell

 $cancelButton = New-Object System.Windows.Forms.Button
 $cancelButton.Location = New-Object System.Drawing.Point(150,120)
 $cancelButton.Size = New-Object System.Drawing.Size(75,23)
 $cancelButton.Text = 'Cancel'
 $cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
 $form.CancelButton = $cancelButton
 $form.Controls.Add($cancelButton)

Next, provide label text on your window that describes the information you want users to
provide. In this case, you want users to select a computer.

 PowerShell

 $label = New-Object System.Windows.Forms.Label
 $label.Location = New-Object System.Drawing.Point(10,20)
 $label.Size = New-Object System.Drawing.Size(280,20)
 $label.Text = 'Please select a computer:'
 $form.Controls.Add($label)

Add the control (in this case, a list box) that lets users provide the information you've described
in your label text. There are many other controls you can apply besides list boxes; for more
controls, see System.Windows.Forms Namespace.

<!-- p.609 -->

 PowerShell

 $listBox = New-Object System.Windows.Forms.ListBox
 $listBox.Location = New-Object System.Drawing.Point(10,40)
 $listBox.Size = New-Object System.Drawing.Size(260,20)
 $listBox.Height = 80

In the next section, you specify the values you want the list box to display to users.

  ７ Note

  The list box created by this script allows only one selection. To create a list box control that
  allows multiple selections, specify a value for the SelectionMode property, similarly to the
  following: $listBox.SelectionMode = 'MultiExtended' . For more information, see
  Multiple-selection List Boxes.

 PowerShell

 [void] $listBox.Items.Add('atl-dc-001')
 [void] $listBox.Items.Add('atl-dc-002')
 [void] $listBox.Items.Add('atl-dc-003')
 [void] $listBox.Items.Add('atl-dc-004')
 [void] $listBox.Items.Add('atl-dc-005')
 [void] $listBox.Items.Add('atl-dc-006')
 [void] $listBox.Items.Add('atl-dc-007')

Add the list box control to your form, and instruct Windows to open the form atop other
windows and dialog boxes when it's opened.

 PowerShell

 $form.Controls.Add($listBox)
 $form.Topmost = $true

Add the following line of code to display the form in Windows.

 PowerShell

 $result = $form.ShowDialog()

Finally, the code inside the if block instructs Windows what to do with the form after users
select an option from the list box, and then click the OK button or press the Enter key.

<!-- p.610 -->

 PowerShell

 if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
     $x = $listBox.SelectedItem
     $x
 }

See also
     GitHub: Dave Wyatt's WinFormsExampleUpdates
     Windows PowerShell Tip of the Week: Selecting Items from a List Box

Last updated on 03/24/2025

<!-- p.611 -->

Using Experimental Features in PowerShell
The Experimental Features support in PowerShell provides a mechanism for experimental features
to coexist with existing stable features in PowerShell or PowerShell modules.

An experimental feature is one where the design isn't finalized. The feature is available for users
to test and provide feedback. Once an experimental feature is finalized, the design changes
become breaking changes.

  Ｕ Caution

  Experimental features aren't intended to be used in production since the changes are
  allowed to be breaking. Experimental features aren't officially supported. However, we
  appreciate any feedback and bug reports. You can file issues in the GitHub source
  repository   .

For more information about enabling or disabling these features, see
about_Experimental_Features.

Experimental feature lifecycle
The Get-ExperimentalFeature cmdlet returns all experimental features available to PowerShell.
Experimental features can come from modules or the PowerShell engine. Module-based
experimental features are only available after you import the module. In the following example,
the PSDesiredStateConfiguration isn't loaded, so the
PSDesiredStateConfiguration.InvokeDscResource feature isn't available.

 PowerShell

 Get-ExperimentalFeature

 Output

 Name                            Enabled Source   Description
 ----                            ------- ------   -----------
 PSFeedbackProvider                 True PSEngine Replace the hard-coded suggestion
 framework with the extensible feedb…
 PSLoadAssemblyFromNativeCode      False PSEngine Expose an API to allow assembly
 loading from native code

<!-- p.612 -->

  PSNativeWindowsTildeExpansion       True PSEngine On windows, expand unquoted tilde
  (`~`) with the user's current home …
  PSRedirectToVariable                True PSEngine Add support for redirecting to the
  variable drive
  PSSerializeJSONLongEnumAsNumber     True PSEngine Serialize enums based on long or
  ulong as an numeric value rather tha…
  PSSubsystemPluginModel              True PSEngine A plugin model for registering and
  un-registering PowerShell subsyste…

Use the Enable-ExperimentalFeature and Disable-ExperimentalFeature cmdlets to enable or
disable a feature. You must start a new PowerShell session for this change to be in effect. Run the
following command to enable the PSCommandNotFoundSuggestion feature:

  PowerShell

  Enable-ExperimentalFeature PSFeedbackProvider

  Output

  WARNING: Enabling and disabling experimental features do not take effect until next
  start
  of PowerShell.

When an experimental feature becomes mainstream, it's no longer available as an experimental
feature because the functionality is now part of the PowerShell engine or module. For example,
the PSAnsiRenderingFileInfo feature became mainstream in PowerShell 7.3. You get the
functionality of the feature automatically.

  ７ Note

  Some features have configuration requirements, such as preference variables, that must be
  set to get the desired results from the feature.

When an experimental feature is discontinued, that feature is no longer available in the
PowerShell. For example, the PSNativePSPathResolution feature was discontinued in PowerShell
7.3.

Available features
This article describes the experimental features that are available and how to use the feature.

Legend

<!-- p.613 -->

     The      icon indicates that the experimental feature is available in the version of PowerShell
     The      icon indicates the version of PowerShell where the experimental feature became
     mainstream
     The      icon indicates the version of PowerShell where the experimental feature was
     removed

                                                                                    ﾉ    Expand table

 Name                                                              7.4       7.5        7.6     7.7

 PSCommandNotFoundSuggestion

 PSCommandWithArgs

 PSFeedbackProvider

 PSLoadAssemblyFromNativeCode

 PSModuleAutoLoadSkipOfflineFiles

 PSNativeWindowsTildeExpansion

 PSProfileDSCResource

 PSRedirectToVariable

 PSSerializeJSONLongEnumAsNumber

 PSSubsystemPluginModel

PSDesiredStateConfiguration module v2 and higher

     PSDesiredStateConfiguration.InvokeDscResource

PSCommandNotFoundSuggestion

  ７ Note

  This feature became mainstream in PowerShell 7.5-preview.5.

Recommends potential commands based on fuzzy matching search after a
CommandNotFoundException.

 PowerShell

<!-- p.614 -->

 PS> get

 Output

 get: The term 'get' isn't recognized as the name of a cmdlet, function, script file,
 or operable program. Check the spelling of the name, or if a path was included, verify
 that the path is correct and try again.

 Suggestion [4,General]: The most similar commands are: set, del, ft, gal, gbp, gc,
 gci,
 gcm, gdr, gcs.

PSCommandWithArgs

  ７ Note

  This feature became mainstream in PowerShell 7.5-preview.5.

This feature enables the -CommandWithArgs parameter for pwsh . This parameter allows you to
execute a PowerShell command with arguments. Unlike -Command , this parameter populates the
$args built-in variable that can be used by the command.

The first string is the command and subsequent strings delimited by whitespace are the
arguments.

For example:

 PowerShell

 pwsh -CommandWithArgs '$args | % { "arg: $_" }' arg1 arg2

This example produces the following output:

 Output

 arg: arg1
 arg: arg2

This feature was added in PowerShell 7.4-preview.2.

PSDesiredStateConfiguration.InvokeDscResource

<!-- p.615 -->

Enables compilation to MOF on non-Windows systems and enables the use of Invoke-
DSCResource without an LCM.

Beginning with PowerShell 7.2, the PSDesiredStateConfiguration module was removed and this
feature is disabled by default. To enable this feature you must install the
PSDesiredStateConfiguration v2.0.5 module from the PowerShell Gallery and enable the feature.

DSC v3 doesn't have this experimental feature. DSC v3 only supports Invoke-DSCResource and
doesn't use or support MOF compilation. For more information, see PowerShell Desired State
Configuration v3.

PSFeedbackProvider

  ７ Note

  This experimental feature was added in PowerShell 7.4-preview.3. This feature became
  mainstream in PowerShell 7.6-preview.6.

When you enable this feature, PowerShell uses a new feedback provider to give you feedback
when a command can't be found. The feedback provider is extensible, and can be implemented
by third-party modules. The feedback provider can be used by other subsystems, such as the
predictor subsystem, to provide predictive IntelliSense results.

This feature includes two built-in feedback providers:

     GeneralCommandErrorFeedback serves the same suggestion functionality existing today

     UnixCommandNotFound, available on Linux, provides feedback similar to bash.

     The UnixCommandNotFound serves as both a feedback provider and a predictor. The
     suggestion from command-not-found command is used both for providing the feedback
     when command can't be found in an interactive run, and for providing predictive
     IntelliSense results for the next command line.

PSLoadAssemblyFromNativeCode
Exposes an API to allow assembly loading from native code.

PSModuleAutoLoadSkipOfflineFiles

<!-- p.616 -->

  ７ Note

  This feature became mainstream in PowerShell 7.5-preview.5.

With this feature enabled, if a user's PSModulePath contains a folder from a cloud provider, such
as OneDrive, PowerShell no longer triggers the download of all files contained within that folder.
Any file marked as not downloaded are skipped. Users who use cloud providers to sync their
modules between machines should mark the module folder as Pinned or the equivalent status
for providers other than OneDrive. Marking the module folder as Pinned ensures that the files are
always kept on disk.

This feature was added in PowerShell 7.4-preview.1.

PSNativeWindowsTildeExpansion

  ７ Note

  This experimental feature was added in PowerShell 7.5-preview.2. This feature became
  mainstream in PowerShell 7.6-preview.6.

When this feature is enabled, PowerShell expands unquoted tilde ( ~ ) to the user's current home
folder before invoking native commands. The following examples show how the feature works.

With the feature disabled, the tilde is passed to the native command as a literal string.

  PowerShell

  PS> cmd.exe /c echo ~
  ~

With the feature enabled, PowerShell expands the tilde before it's passed to the native command.

  PowerShell

  PS> cmd.exe /c echo ~
  C:\Users\username

This feature only applies to Windows. On non-Windows platforms, tilde expansion is handled
natively.

<!-- p.617 -->

PSProfileDSCResource

  ７ Note

  This experimental feature was added in PowerShell 7.6-preview.6.

The PowerShell 7.6-preview.6 release added this feature as an advertisement for a new DSCv3
resource. The experimental feature flag doesn't do anything. You can use the new DSC v3
resource regardless of whether this feature is enabled or disabled.

The Microsoft.PowerShell/Profile resource enables you to manage PowerShell profiles using
Desired State Configuration (DSC) v3. This release includes two new files in the $PSHOME folder:

       pwsh.profile.dsc.resource.json - DSC v3 resource manifest file

       pwsh.profile.resource.ps1 - DSC v3 resource implementation file

The resource supports operations to get, set, and export profile content for different profile
types. For more information, see the notes in the PR PowerShell/PowerShell#26157         .

PSRedirectToVariable

  ７ Note

  This experimental feature was added in PowerShell 7.5-preview.4. This feature became
  mainstream in PowerShell 7.6-preview.6.

When enabled, this feature adds support for redirecting to the Variable: drive. This feature allows
you to redirect data to a variable using the Variable:name syntax. PowerShell inspects the target
of the redirection and if it uses the Variable provider it calls Set-Variable rather than Out-File .

The following example shows how to redirect the output of a command to a Variable:

 PowerShell

 . {
     "Output 1"
     Write-Warning "Warning, Warning!"
     "Output 2"
 } 3> Variable:warnings
 $warnings

<!-- p.618 -->

 Output

 Output 1
 Output 2
 WARNING: Warning, Warning!

PSSerializeJSONLongEnumAsNumber

  ７ Note

  This experimental feature was added in PowerShell 7.5-preview.5.

This feature enables the cmdlet ConvertTo-Json to serialize any enum values based on
Int64/long or UInt64/ulong as a numeric value rather than the string representation of that

enum value. This aligns the behavior of enum serialization with other enum base types where the
cmdlet serializes enums as their numeric value. Use the EnumsAsStrings parameter to serialize as
the string representation.

For example:

 PowerShell

 # PSSerializeJSONLongEnumAsNumber disabled
 @{
     Key = [System.Management.Automation.Tracing.PowerShellTraceKeywords]::Cmdlets
 } | ConvertTo-Json
 # { "Key": "Cmdlets" }

 # PSSerializeJSONLongEnumAsNumber enabled
 @{
     Key = [System.Management.Automation.Tracing.PowerShellTraceKeywords]::Cmdlets
 } | ConvertTo-Json
 # { "Key": 32 }

 # -EnumsAsStrings to revert back to the old behaviour
 @{
     Key = [System.Management.Automation.Tracing.PowerShellTraceKeywords]::Cmdlets
 } | ConvertTo-Json -EnumsAsStrings
 # { "Key": "Cmdlets" }

PSSubsystemPluginModel

  ７ Note

<!-- p.619 -->

  This feature became mainstream in PowerShell 7.6-preview.6.

This feature enables the subsystem plugin model in PowerShell. The feature makes it possible to
separate components of System.Management.Automation.dll into individual subsystems that
reside in their own assembly. This separation reduces the disk footprint of the core PowerShell
engine and allows these components to become optional features for a minimal PowerShell
installation.

Currently, only the CommandPredictor subsystem is supported. This subsystem is used along
with the PSReadLine module to provide custom prediction plugins. In future, Job,
CommandCompleter, Remoting and other components could be separated into subsystem
assemblies outside of System.Management.Automation.dll .

The experimental feature includes a new cmdlet, Get-PSSubsystem. This cmdlet is only available
when the feature is enabled. This cmdlet returns information about the subsystems that are
available on the system.

 Last updated on 04/20/2026

<!-- p.620 -->

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

<!-- p.621 -->

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

<!-- p.622 -->

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

<!-- p.623 -->

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

<!-- p.624 -->

PowerShell learning resources
Additional resources for learning about PowerShell.

Learn training modules
Microsoft Learn is a free, online training platform that provides interactive learning for
Microsoft products and more. Our goal is to help you become proficient on our technologies
and learn more skills with fun, guided, hands-on, interactive content that's specific to your role
and goals.

     PowerShell training

Blogs and community
In addition to the Help available at the command line, the following resources provide more
information for users who want to run PowerShell.

     PowerShell Team Blog . The best resource for learning directly from the PowerShell
     product team.
     PowerShell Community Blog        articles are scenario-driven. Written by the community, for
     the community.
     Have questions about using PowerShell? Connect with hundreds of other people who
     have similar interests in one of the many community forums listed on the PowerShell
     Community page.

Microsoft Virtual Academy
The Microsoft Virtual Academy videos have been moved to Channel 9.

     Getting Started with Microsoft PowerShell
     Advanced Tools & Scripting with PowerShell 3.0 Jump Start
     Testing PowerShell with Pester
     Getting Started with PowerShell Desired State Configuration (DSC)
     Advanced PowerShell DSC and Custom Resources
     SharePoint Automation with DSC

Resources for PowerShell Developers
The following resources provide resources to help developers create their own PowerShell
modules, functions, cmdlets, providers, and hosting applications.

<!-- p.625 -->

     PowerShell SDK
     PowerShell SDK API Browser

Last updated on 11/21/2025

<!-- p.626 -->

PowerShell Glossary
This article lists common terms used to talk about PowerShell.

B
binary module
A PowerShell module whose root module is a binary ( .dll ) file. A binary module may or may
not include a module manifest.

C
CommonParameter
A parameter that's added to all cmdlets, advanced functions, and workflows by the PowerShell
engine.

D
dot source
In PowerShell, to start a command by typing a dot and a space before the command.
Commands that are dot sourced run in the current scope instead of in a new scope. Any
variables, aliases, functions, or drives that command creates are created in the current scope
and are available to users when the command is completed.

dynamic module
A module that exists only in memory. The New-Module and Import-PSSession cmdlets create
dynamic modules.

dynamic parameter
A parameter that's added to a PowerShell cmdlet, function, or script under certain conditions.
Cmdlets, functions, providers, and scripts can add dynamic parameters.

F

<!-- p.627 -->

format file
A PowerShell XML file that has the .format.ps1xml extension and that defines how PowerShell
displays an object based on its .NET Framework type.

G
global session state
The session state that contains the data that's accessible to the user of a PowerShell session.

H
Host
The interface that the PowerShell engine uses to communicate with the user. For example, the
host specifies how prompts are handled between PowerShell and the user.

host application
A program that loads the PowerShell engine into its process and uses it to perform operations.

I
input processing method
A method that a cmdlet can use to process the records it receives as input. The input
processing methods include the BeginProcessing method, the ProcessRecord method, the
EndProcessing method, and the StopProcessing method.

M
manifest module
A PowerShell module that has a manifest and whose RootModule key is empty.

member-access enumeration
A PowerShell convenience feature to automatically enumerate items in a collection when using
the member-access operator ( . ).

<!-- p.628 -->

module
A self-contained reusable unit that allows you to partition, organize, and abstract your
PowerShell code. A module can contain cmdlets, providers, functions, variables, and other
types of resources that can be imported as a single unit.

module manifest
A PowerShell data file ( .psd1 ) that describes the contents of a module and that controls how a
module is processed.

module session state
The session state that contains the public and private data of a PowerShell module. The private
data in this session state isn't available to the user of a PowerShell session.

N
non-terminating error
An error that doesn't stop PowerShell from continuing to process the command. See also,
terminating error.

noun
The word that follows the hyphen in a PowerShell cmdlet name. The noun describes the
resources upon which the cmdlet acts.

P
parameter set
A group of parameters that can be used in the same command to perform a specific action.

pipe
In PowerShell, to send the results of the preceding command as input to the next command in
the pipeline.

pipeline

<!-- p.629 -->

A series of commands connected by pipeline operators ( | ). Each pipeline operator sends the
results of the preceding command as input to the next command.

PowerShell cmdlet
A single command that participates in the pipeline semantics of PowerShell. This includes
binary (C#) cmdlets, advanced script functions, CDXML, and Workflows.

PowerShell command
The elements in a pipeline that cause an action to be carried out. PowerShell commands are
either typed at the keyboard or invoked programmatically.

PowerShell data file
A text file that has the .psd1 file extension. PowerShell uses data files for various purposes
such as storing module manifest data and storing translated strings for script
internationalization.

PowerShell drive
A virtual drive that provides direct access to a data store. It can be defined by a PowerShell
provider or created at the command line. Drives created at the command line are session-
specific drives and are lost when the session is closed.

provider
A Microsoft .NET Framework-based program that makes the data in a specialized data store
available in PowerShell so that you can view and manage it.

PSSession
A type of PowerShell session that's created, managed, and closed by the user.

R
root module
The module specified in the RootModule key in a module manifest.

<!-- p.630 -->

runspace
In PowerShell, the operating environment in which each command in a pipeline is executed.

S
scalar value
In PowerShell, a scalar value is any value type that is not enumerable. This includes the .NET
primitive types, such as booleans and numbers, and other value types such as String, DateTime
and Guid.

For a list of .NET primitive types, see the Remarks section of System.Type.IsPrimitive Property.

script block
In the PowerShell programming language, a collection of statements or expressions that can be
used as a single unit. A script block can accept arguments and return values.

script file
A file that has the .ps1 extension and contains a script written in the PowerShell language.

script module
A PowerShell module whose root module is a script module ( .psm1 ) file. A script module may
include a module manifest. The script defines the members that the script module exports.

shell
The command interpreter that's used to pass commands to the operating system.

[switch] parameter

A parameter that doesn't take an argument. The value of a [switch] parameter defaults to
$false . When a [switch] parameter is used, its value becomes $true .

T
terminating error

<!-- p.631 -->

An error that stops PowerShell from processing the command. See also, non-terminating error.

transaction
An atomic unit of work. The work in a transaction must be completed as a whole. If any part of
the transaction fails, the entire transaction fails.

type file
A PowerShell XML file that has the .types.ps1xml extension and that extends the properties of
Microsoft .NET Framework types in PowerShell.

V
verb
The word that precedes the hyphen in a PowerShell cmdlet name. The verb describes the
action that the cmdlet performs.

W
Windows PowerShell ISE
The Integrated Scripting Environment (ISE) - A Windows PowerShell host application that
enables you to run commands and to write, test, and debug scripts in a friendly, syntax-
colored, Unicode-compliant environment.

Windows PowerShell snap-in
A resource that defines a set of cmdlets, providers, and Microsoft .NET Framework types that
can be added to the Windows PowerShell environment. PowerShell snap-ins have been
replaced by modules.

Windows PowerShell Workflow
A workflow is a sequence of programmed, connected steps that perform long-running tasks or
require the coordination of multiple steps across multiple devices or managed nodes. Windows
PowerShell Workflow lets IT pros and developers author sequences of multi-device
management activities, or single tasks within a workflow, as workflows. Windows PowerShell
Workflow lets you adapt and run both PowerShell scripts and XAML files as workflows.

<!-- p.632 -->

Windows PowerShell Workflow is built on the Windows Workflow Foundation, which has been
deprecated.

Last updated on 04/08/2026

<!-- p.633 -->

Overview of what's new in PowerShell
A collection of release notes and documentation about the new features available in new
versions of PowerShell.

  What's new in PowerShell 7

  ｈ WHAT'S NEW
  What's new in PowerShell 7.6 (LTS)

  What's new in PowerShell 7.5

  What's new in PowerShell 7.4 (LTS)

  Differences between Windows PowerShell 5.1 and PowerShell 7

  PowerShell differences on non-Windows platforms

  What's new in PowerShell 5.1

  ｈ WHAT'S NEW
  What is Windows PowerShell?

  Differences between Windows PowerShell 5.1 and PowerShell 7

  Migrating from Windows PowerShell 5.1 to PowerShell 7

  History & Compatibility

  ｈ WHAT'S NEW
  Release history of modules and cmdlets

  Module compatibility

  Previous versions of PowerShell

<!-- p.634 -->

What's New in PowerShell 7.7
PowerShell 7.7-preview.2 includes the following features, updates, and breaking changes.
PowerShell 7.7.0 is built on the .NET 11.0.100-preview.4 runtime.

For a complete list of changes, see the CHANGELOG      in the GitHub repository.

Updated modules
PowerShell 7.7 includes the following updated modules:

     Microsoft.PowerShell.PSResourceGet v1.2.0
     PSReadLine v2.4.5

Breaking Changes
     Add ValidateNotNullOrEmpty attribute to the -Property of Format-Table , Format-List , and
     Format-Custom (#26552     )
     Use ArgumentException.ThrowIfNullOrEmpty for not-null-not-empty argument validation.
     (#26668    )
        The exception thrown changes to System.ArgumentException from
        System.Management.Automation.PSArgumentNullException .

     Correct handling of explicit -[<Operator>]:$false parameter values in Where-Object
     (#26485    ) (Thanks @yotsuda!)

Tab completion improvements
     Add tab completion for $PSBoundParameters.Keys switch cases and access patterns
     (#26483    ) (Thanks @yotsuda!)

Cmdlet improvements
     Handle empty-string and null-value results returned from custom argument completer
     more properly (#27398     )
     Add missing resource strings for Get-WinEvent (#27397 ) (Thanks @MartinGC94!)
     Improve Get-WinEvent -ListLog exception handling (#27395       ) (Thanks @MartinGC94!)
     Update MaxVisitCount and MaxHashtableKeyCount if VisitorSafeValueContext indicates
     SkipLimitCheck is true for Import-PowerShellDataFile

<!-- p.635 -->

Correct handling of explicit -<SwitchParameter>:$false parameter values for the following
cmdlets:
   ConvertFrom-Csv , ConvertTo-Csv , Export-Csv , and Import-Csv (#26719     ) (Thanks
  @yotsuda!)
   Get-Random (#26457     ) (Thanks @yotsuda!)
   Get-SecureRandom (#26460     ) (Thanks @yotsuda!)
   Get-TimeZone (#26463     ) (Thanks @yotsuda!)
   Get-Uptime (#26141     ) (Thanks @logiclrd!)
   New-Guid (#26140     ) (Thanks @logiclrd!)
   New-PSSession (#26469     ) (Thanks @yotsuda!)
   Split-Path (#26474     ) (Thanks @yotsuda!)
   Test-Connection (#26479     ) (Thanks @yotsuda!)
   Where-Object (#26485     ) (Thanks @yotsuda!)
Add -ExcludeProperty parameter to Format-* cmdlets (#26514 ) (Thanks @yotsuda!)
Add -Extension parameter to Join-Path cmdlet (#26482         ) (Thanks @yotsuda!)
Make Export-Csv -Append and -NoHeader mutually exclusive (#26472 ) (Thanks
@yotsuda!)
Mark -NoTypeInformation as obsolete no-op and evaluate -IncludeTypeInformation on by
value on Csv cmdlets (#26719 ) (Thanks @yotsuda!)
Add SubjectAlternativeName property to the Signature object returned from Get-
AuthenticodeSignature (#26252     )
Add property and event for debug attach (#25788 ) (Thanks @jborean93!)
Add $PSApplicationOutputEncoding variable (#21219 ) (Thanks @jborean93!)
Add ToRegex method to WildcardPattern class (#26515 ) (Thanks @yotsuda!)
Update PowerShell Profile DSC resource manifests to allow null for content (#26929       )
DSC v3 resource for PowerShell Profile (#26157 )
Dynamically evaluate width of LastWriteTime for formatting output on Unix (#24624            )
(Thanks @MathiasMagnus!)
Fix formatting to properly handle the Reset VT sequences that appear in the middle of a
string (#26424   )
Fix Invoke-RestMethod to support read-only files in multipart form data (#26454     ) (Thanks
@yotsuda!)
Fix memory leak in GetFileShares (#25896        ) (Thanks @xtqqczze!)
Fix NOTES section formatting in comment-based help (#26512         ) (Thanks @yotsuda!)
Fix Test-Json false positive errors when using oneOf or anyOf in schema (#26618      )
(Thanks @yotsuda!)

<!-- p.636 -->

     Fix the CLR internal error and null ref exception when running Show-Command with PowerShell
     API (#26669      )
     Handle null reference exception in CsvCommands.cs : ConvertPSObjectToCSV (#26144 )
     (Thanks @mikkas456!)
     Improve ValidateLength error message consistency and refactor validation tests (#25806 )
     (Thanks @jorgeasaurus!)
     Support TargetObject position in ParserErrors (#26649     ) (Thanks @jborean93!)
     Add verbose message to Get-Service when properties cannot be returned (#27109        )
     (Thanks @reabr!)
     Fix Remove-Item confirmation message to use provider path instead (#27123 ) (Thanks
     @scuzqy!)
     PSStyle: validate background index against BackgroundColorMap (#27106 ) (Thanks
     @cuiweixie!)

Engine improvements
     Update PowerShell telemetry to respect the diagnostics and feedback setting on Windows
     (#27328     )
     Fix up default value for parameters with the in modifier (#26785 ) (Thanks @jborean93!)
     Fix WSManInstance COM interface with ResourceURI (#26692 ) (Thanks @jborean93!)
     Refactor the module path construction code to make it more robust and easier to maintain
     (#26565     )
     Fix checks for local user config file paths (#26269   )
     Delay update notification for one week to ensure all packages become available (#27095 )
     Disable AMSI content logging in release (#26235 ) (Thanks @xtqqczze!)
     Add property and event for debug attach (#25788 ) (Thanks @jborean93!)
     Enable usage in AppContainers (#27266      )

Experimental features
PowerShell 7.7 includes the following experimental features.

     PSLoadAssemblyFromNativeCode - Load assemblies from native code
     PSSerializeJSONLongEnumAsNumber - ConvertTo-Json now treats large enums as numbers
     PSProfileDSCResource - Add DSC v3 resource for PowerShell Profiles

Last updated on 06/12/2026

<!-- p.637 -->

What's New in PowerShell 7.6
PowerShell 7.6.4 includes the following features, updates, and breaking changes. PowerShell 7.6.4
is built on the .NET 10.0.10 runtime.

For a complete list of changes, see the CHANGELOG     in the GitHub repository.

Installer updates
The macOS PKG package is now notarized and signed by Microsoft. For more information, see
Install PowerShell 7 on macOS.

Updated modules
PowerShell 7.6.4 includes the following updated modules:

     Microsoft.PowerShell.PSResourceGet v1.2.0
     PSReadLine v2.4.5
     Microsoft.PowerShell.ThreadJob v2.2.0

Breaking Changes
     The Microsoft.PowerShell.ThreadJob replaces the ThreadJob module. The Start-ThreadJob
     cmdlet hasn't changed, so there shouldn't be an impact unless you have scripts that use the
     module qualified name. If you are using the module qualified name, update the name to
      Microsoft.PowerShell.ThreadJob\Start-ThreadJob .

     Fix WildcardPattern.Escape to escape lone backticks correctly (#25211   ) (Thanks
     @ArmaanMcleod!)
     Convert -ChildPath parameter to string[] for Join-Path cmdlet (#24677 ) (Thanks
     @ArmaanMcleod!)
     Remove trailing space from event source name (#24192      ) (Thanks @MartinGC94!)

Tab completion improvements
     Properly Expand Aliases to their actual ResolvedCommand (#26571      ) (Thanks @kilasuit!)
     Use parameter HelpMessage for tool tip in parameter completion (#25108       ) (Thanks
     @jborean93!)
     Remove duplicate modules from completion results (#25538      ) (Thanks @MartinGC94!)

<!-- p.638 -->

Add completion for variables assigned in ArrayLiteralAst and ParenExpressionAst
(#25303   ) (Thanks @MartinGC94!)
Fix tab completion for env/function variables (#25346   ) (Thanks @jborean93!)
Update Named and Statement block type inference to not consider AssignmentStatements
and Increment/decrement operators as part of their output (#21137      ) (Thanks
@MartinGC94!)
Add -PropertyType argument completer for New-ItemProperty (#21117 ) (Thanks
@ArmaanMcleod!)
Add completion single/double quote support for -Noun parameter for Get-Command
(#24977   ) (Thanks @ArmaanMcleod!)
Add completion single/double quote support for -PSEdition parameter for Get-Module
(#24971   ) (Thanks @ArmaanMcleod!)
Convert InvalidCommandNameCharacters in AnalysisCache to SearchValues<char> for
more efficient char searching (#24880   ) (Thanks @ArmaanMcleod!)
Convert s_charactersRequiringQuotes in Completion Completers to SearchValues<char> for
more efficient char searching (#24879   ) (Thanks @ArmaanMcleod!)
Update IndexOfAny() calls with invalid path/filename to SearchValues<char> for more
efficient char searching ([#24896][24896]) (Thanks @ArmaanMcleod!)
Replace char[] array in CompletionRequiresQuotes with cached SearchValues<char>
(#24907   ) (Thanks @ArmaanMcleod!)
Add quote handling in Verb , StrictModeVersion , Scope and PropertyType Argument
Completers with single helper method (#24839 ) (Thanks @ArmaanMcleod!)
Fix share completion with provider and spaces (#19440     ) (Thanks @MartinGC94!)
Improve variable type inference (#19830 ) (Thanks @MartinGC94!)
Add tooltips for hashtable key completions (#17864 ) (Thanks @MartinGC94!)
Fix type inference of parameters in classic functions (#25172   ) (Thanks @MartinGC94!)
Improve assignment type inference (#21143 ) (Thanks @MartinGC94!)
Exclude OutVariable assignments within the same CommandAst when inferring variables
(#25224   ) (Thanks @MartinGC94!)
Fix parameter completion when script requirements fail (#17687     ) (Thanks @MartinGC94!)
Improve the completion for attribute arguments (#25129 ) (Thanks @MartinGC94!)
Fix completion that relies on pseudobinding in script blocks (#25122   ) (Thanks
@MartinGC94!)
Don't complete duplicate command names (#21113 ) (Thanks @MartinGC94!)
Add completion for variables assigned by command redirection (#25104       ) (Thanks
@MartinGC94!)

<!-- p.639 -->

  Fix TypeName.GetReflectionType() to work when the TypeName instance represents a generic
  type definition within a GenericTypeName (#24985 )
  Update variable/property assignment completion so it can fallback to type inference
  (#21134   ) (Thanks @MartinGC94!)
  Handle type inference for redirected commands (#21131 ) (Thanks @MartinGC94!)
  Use Get-Help approach to find about_*.help.txt files with correct locale for completions
  (#24194   ) (Thanks @MartinGC94!)
  Fix completion of variables assigned inside Do loops (#25076 ) (Thanks @MartinGC94!)
  Fix completion of provider paths when a path returns itself instead of its children
  (#24755   ) (Thanks @MartinGC94!)
  Enable completion of scoped variables without specifying scope (#20340 ) (Thanks
  @MartinGC94!)
  Fix issue with incomplete results when completing paths with wildcards in non-filesystem
  providers (#24757    ) (Thanks @MartinGC94!)

Cmdlet improvements
  Update MaxVisitCount and MaxHashtableKeyCount if VisitorSafeValueContext indicates
  SkipLimitCheck is true for Import-PowerShellDataFile

  Add implicit localization fallback to Import-LocalizedData (#19896    ) (Thanks @chrisdent-
  de!)
  Add -Delimiter parameter to Get-Clipboard (#26572        ) (Thanks @MartinGC94!)
  Fix Out-GridView by replacing use of obsolete BinaryFormatter with custom implementation
  (#25497   ) (Thanks @mawosoft!)
  Improve verbose and debug logging level messaging in web cmdlets (#25510          ) (Thanks
  @JustinGrote!)
  Improve debug logging of Web cmdlet request and response (#25479 ) (Thanks
  @JustinGrote!)
  Add the parameter Register-ArgumentCompleter -NativeFallback to support registering a
  cover-all completer for native commands (#25230 )
  Treat -Target as literal in New-Item (#25186   ) (Thanks @GameMicrowave!)
  Update PATH environment variable for package manager executable on Windows
  (#25847   )
  Update Get-Service to ignore common errors when retrieving non-critical properties for a
  service (#24245   ) (Thanks @jborean93!)
  Add single/double quote support for Join-String Argument Completer (#25283            ) (Thanks
  @ArmaanMcleod!)

<!-- p.640 -->

  Remove IsScreenReaderActive() check from ConsoleHost (#26118 )
  Improve the $using expression support in Invoke-Command (#24025      ) (Thanks
  @jborean93!)
  Change the default feedback provider timeout from 300ms to 1000ms (#25910 )
  Add support for thousands separators in [bigint] casting (#25396     ) (Thanks
  @AbishekPonmudi!)
  Add MethodInvocation trace for overload tracing (#21320    ) (Thanks @jborean93!)
  Fix ConvertFrom-Json to ignore comments inside array literals (#14553 ) (#26050 )
  (Thanks @MatejKafka!)
  Fix -Debug to not trigger the ShouldProcess prompt (#26081 )
  Fix Write-Host to respect OutputRendering = PlainText (#21188    )
  Fix debug tracing error with magic extents (#25726 ) (Thanks @jborean93!)
  Fix quoting in completion if the path includes a double quote character (#25631 ) (Thanks
  @MartinGC94!)
  Fix the common parameter -ProgressAction for advanced functions (#24591          ) (Thanks
  @cmkb3!)
  Fix the NullReferenceException when writing progress records to console from multiple
  threads (#25440    ) (Thanks @kborowinski!)
  Use absolute path in FileSystemProvider.CreateDirectory (#24615 ) (Thanks @Tadas!)
  Make inherited protected internal instance members accessible in PowerShell class scope
  (#25245    ) (Thanks @mawosoft!)
  Add internal methods to check Preferences (#25514 ) (Thanks @iSazonov!)
  Add -ExcludeModule parameter to Get-Command (#18955 ) (Thanks @MartinGC94!)
  Return correct FileName property for Get-Item when listing alternate data streams
  (#18019    ) (Thanks @kilasuit!)
  Fix Get-ItemProperty to report non-terminating error for cast exception (#21115     ) (Thanks
  @ArmaanMcleod!)
  Fix a bug in how q handles XmlNode object (#24669    ) (Thanks @brendandburns!)
  Error when New-Item -Force is passed an invalid directory name (#24936 ) (Thanks
  @kborowinski!)
  Allow Start-Transcript to use $Transcript which is a PSObject wrapped string to specify
  the transcript path (#24963   ) (Thanks @kborowinski!)
  Improve Start-Process -Wait polling efficiency (#24711    ) (Thanks @jborean93!)
  Add completion of modules by their shortname (#20330      ) (Thanks @MartinGC94!)

Engine improvements
