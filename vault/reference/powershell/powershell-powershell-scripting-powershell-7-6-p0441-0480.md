---
title: "How to use this documentation — pages 441-480"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0441-0480
family: powershell
documentKind: "doc"
abstract: "$Cred = Get-Credential -UserName domain\\user -Message 'Enter Password' Sometimes, you can't use the interactive method of creating credential objects shown in the previous example. Most automation tools require a non-interactive method. To create a credential without user intera"
---

# How to use this documentation — pages 441-480

<!-- p.441 -->

 $Cred = Get-Credential -UserName domain\user -Message 'Enter Password'

Sometimes, you can't use the interactive method of creating credential objects shown in the
previous example. Most automation tools require a non-interactive method. To create a
credential without user interaction, create a secure string containing the password. Then pass
the secure string and user name to the System.Management.Automation.PSCredential() method.

Use the following command to create a secure string containing the password:

 PowerShell

 ConvertTo-SecureString "MyPlainTextPassword" -AsPlainText -Force

Both the AsPlainText and Force parameters are required. Without those parameters, you
receive a message warning that you shouldn't pass plain text into a secure string. PowerShell
returns this warning because the plain text password gets recorded in various logs. Once you
have a secure string created, you need to pass it to the PSCredential() method to create the
credential object. In the following example, the variable $password contains the secure string
$Cred contains the credential object.

 PowerShell

 $password = ConvertTo-SecureString "MyPlainTextPassword" -AsPlainText -Force
 $Cred = New-Object System.Management.Automation.PSCredential ("username",
 $password)

Now that you know how to create credential objects, you can add credential parameters to
your PowerShell functions.

Adding a Credential Parameter
Just like any other parameter, you start off by adding it in the param block of your function. It's
recommended that you name the parameter $Credential because that's what existing
PowerShell cmdlets use. The type of the parameter should be
[System.Management.Automation.PSCredential] .

The following example shows the parameter block for a function called Get-Something . It has
two parameters: $Name and $Credential .

 PowerShell

<!-- p.442 -->

 function Get-Something {
     param(
         $Name,
         [System.Management.Automation.PSCredential]$Credential
     )

The code in this example is enough to have a working credential parameter, however there are
a few things you can add to make it more robust.

     Add the [ValidateNotNull()] validation attribute to check that the value being passed to
     Credential. If the parameter value is null, this attribute prevents the function from
     executing with invalid credentials.

     Add [System.Management.Automation.Credential()] . This allows you to pass in a username
     as a string and have an interactive prompt for the password.

     Set a default value for the $Credential parameter to
     [System.Management.Automation.PSCredential]::Empty . Your function you might be

     passing this $Credential object to existing PowerShell cmdlets. Providing a null value to
     the cmdlet called inside your function causes an error. Providing an empty credential
     object avoids this error.

   Tip

  Some cmdlets that accept a credential parameter do not support
  [System.Management.Automation.PSCredential]::Empty as they should. See the Dealing

  with Legacy Cmdlets section for a workaround.

Using credential parameters
The following example demonstrates how to use credential parameters. This example shows a
function called Set-RemoteRegistryValue , which is out of The Pester Book    . This function
defines the credential parameter using the techniques describe in the previous section. The
function calls Invoke-Command using the $Credential variable created by the function. This
allows you to change the user who's running Invoke-Command . Because the default value of
$Credential is an empty credential, the function can run without providing credentials.

 PowerShell

 function Set-RemoteRegistryValue {
     param(

<!-- p.443 -->

          $ComputerName,
          $Path,
          $Name,
          $Value,
          [ValidateNotNull()]
          [System.Management.Automation.PSCredential]
          [System.Management.Automation.Credential()]
          $Credential = [System.Management.Automation.PSCredential]::Empty
      )
         $null = Invoke-Command -ComputerName $ComputerName -ScriptBlock {
              Set-ItemProperty -Path $Using:Path -Name $Using:Name -Value
 $Using:Value
         } -Credential $Credential
 }

The following sections show different methods of providing credentials to Set-
RemoteRegistryValue .

Prompting for credentials
Using Get-Credential in parentheses () at run time causes the Get-Credential to run first.
You are prompted for a username and password. You could use the Credential or UserName
parameters of Get-Credential to pre-populate the username and domain. The following
example uses a technique called splatting to pass parameters to the Set-RemoteRegistryValue
function. For more information about splatting, check out the about_Splatting article.

 PowerShell

 $remoteKeyParams = @{
     ComputerName = $Env:COMPUTERNAME
     Path = 'HKLM:\SOFTWARE\Microsoft\WebManagement\Server'
     Name = 'EnableRemoteManagement'
     Value = '1'
 }

 Set-RemoteRegistryValue @remoteKeyParams -Credential (Get-Credential)

<!-- p.444 -->

Using (Get-Credential) seems cumbersome. Normally, when you use the Credential
parameter with only a username, the cmdlet automatically prompts for the password. The
[System.Management.Automation.Credential()] attribute enables this behavior.

 PowerShell

 $remoteKeyParams = @{
     ComputerName = $Env:COMPUTERNAME
     Path = 'HKLM:\SOFTWARE\Microsoft\WebManagement\Server'
     Name = 'EnableRemoteManagement'
     Value = '1'
 }

 Set-RemoteRegistryValue @remoteKeyParams -Credential duffney

<!-- p.445 -->

  ７ Note

  To set the registry value shown, these examples assume you have the Web Server features
  of Windows installed. Run Install-WindowsFeature Web-Server and Install-
  WindowsFeature web-mgmt-tools if required.

Provide credentials in a variable
You can also populate a credential variable ahead of time and pass it to the Credential
parameter of Set-RemoteRegistryValue function. Use this method with Continuous Integration /
Continuous Deployment (CI/CD) tools such as Jenkins, TeamCity, and Octopus Deploy. For an
example using Jenkins, check out Hodge's blog post Automating with Jenkins and PowerShell
on Windows - Part 2   .

This example uses the .NET method to create the credential object and a secure string to pass
in the password.

 PowerShell

 $password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
 $Cred = New-Object System.Management.Automation.PSCredential ("duffney", $password)

 $remoteKeyParams = @{
     ComputerName = $Env:COMPUTERNAME
     Path = 'HKLM:\SOFTWARE\Microsoft\WebManagement\Server'
     Name = 'EnableRemoteManagement'
     Value = '1'

<!-- p.446 -->

  }

  Set-RemoteRegistryValue @remoteKeyParams -Credential $Cred

For this example, the secure string is created using a clear text password. All of the previously
mentioned CI/CD have a secure method of providing that password at run time. When using
those tools, replace the plain text password with the variable defined within the CI/CD tool you
use.

Run without credentials
Since $Credential defaults to an empty credential object, you can run the command without
credentials, as shown in this example:

  PowerShell

  $remoteKeyParams = @{
      ComputerName = $Env:COMPUTERNAME
      Path = 'HKLM:\SOFTWARE\Microsoft\WebManagement\Server'
      Name = 'EnableRemoteManagement'
      Value = '1'
  }

  Set-RemoteRegistryValue @remoteKeyParams

Dealing with legacy cmdlets
Not all cmdlets support credential objects or allow empty credentials. Instead, the cmdlet
wants username and password parameters as strings. There are a few ways to work around this
limitation.

Using if-else to handle empty credentials
In this scenario, the cmdlet you want to run doesn't accept an empty credential object. This
example adds the Credential parameter to Invoke-Command only if it's not empty. Otherwise, it
runs the Invoke-Command without the Credential parameter.

  PowerShell

  function Set-RemoteRegistryValue {
      param(
          $ComputerName,
          $Path,
          $Name,

<!-- p.447 -->

          $Value,
          [ValidateNotNull()]
          [System.Management.Automation.PSCredential]
          [System.Management.Automation.Credential()]
          $Credential = [System.Management.Automation.PSCredential]::Empty
      )

     if($Credential -ne [System.Management.Automation.PSCredential]::Empty) {
         Invoke-Command -ComputerName:$ComputerName -Credential:$Credential {
              Set-ItemProperty -Path $Using:Path -Name $Using:Name -Value
 $Using:Value
         }
     } else {
         Invoke-Command -ComputerName:$ComputerName {
              Set-ItemProperty -Path $Using:Path -Name $Using:Name -Value
 $Using:Value
         }
     }
 }

Using splatting to handle empty credentials
This example uses parameter splatting to call the legacy cmdlet. The $Credential object is
conditionally added to the hash table for splatting and avoids the need to repeat the Invoke-
Command script block. To learn more about splatting inside functions, see the Splatting

Parameters Inside Advanced Functions      blog post.

 PowerShell

 function Set-RemoteRegistryValue {
     param(
         $ComputerName,
         $Path,
         $Name,
         $Value,
         [ValidateNotNull()]
         [System.Management.Automation.PSCredential]
         [System.Management.Automation.Credential()]
         $Credential = [System.Management.Automation.PSCredential]::Empty
     )

          $Splat = @{
              ComputerName = $ComputerName
          }

          if ($Credential -ne [System.Management.Automation.PSCredential]::Empty) {
              $Splat['Credential'] = $Credential
          }

          $null = Invoke-Command -ScriptBlock {
              Set-ItemProperty -Path $Using:Path -Name $Using:Name -Value

<!-- p.448 -->

 $Using:Value
         } @splat
 }

Working with string passwords
The Invoke-Sqlcmd cmdlet is an example of a cmdlet that accepts a string as a password.
Invoke-Sqlcmd allows you to run simple SQL insert, update, and delete statements. Invoke-

Sqlcmd requires a clear-text username and password rather than a more secure credential

object. This example shows how to extract the username and password from a credential
object.

The Get-AllSQLDatabases function in this example calls the Invoke-Sqlcmd cmdlet to query a
SQL server for all its databases. The function defines a Credential parameter with the same
attribute used in the previous examples. Since the username and password exist within the
$Credential variable, you can extract those values for use with Invoke-Sqlcmd .

The user name is available from the UserName property of the $Credential variable. To obtain
the password, you have to use the GetNetworkCredential() method of the $Credential object.
The values are extracted into variables that are added to a hash table used for splatting
parameters to Invoke-Sqlcmd .

 PowerShell

 function Get-AllSQLDatabases {
     param(
         $SQLServer,
         [ValidateNotNull()]
         [System.Management.Automation.PSCredential]
         [System.Management.Automation.Credential()]
         $Credential = [System.Management.Automation.PSCredential]::Empty
     )

          $UserName = $Credential.UserName
          $Password = $Credential.GetNetworkCredential().Password

          $splat = @{
              UserName = $UserName
              Password = $Password
              ServerInstance = 'SQLServer'
              Query = "Select * from Sys.Databases"
          }

          Invoke-Sqlcmd @splat
 }

 $credSplat = @{

<!-- p.449 -->

      TypeName = 'System.Management.Automation.PSCredential'
      ArgumentList = 'duffney',('P@ssw0rd' | ConvertTo-SecureString -AsPlainText -
  Force)
  }
  $Credential = New-Object @credSplat

  Get-AllSQLDatabases -SQLServer SQL01 -Credential $Credential

Continued learning credential management
Creating and storing credential objects securely can be difficult. The following resources can
help you maintain PowerShell credentials.

      BetterCredentials
      Azure Key Vault
      Vault Project
      SecretManagement module

 Last updated on 08/15/2025

<!-- p.450 -->

Avoid assigning variables in expressions
Article • 11/17/2022

PowerShell allows you to use assignments within expressions by enclosing the
assignment in parentheses () . PowerShell passes the assigned value through. For
example:

  PowerShell

  # In an `if` conditional
  if ($foo = Get-Item $PROFILE) { "$foo exists" }

  # Property access
  ($profileFile = Get-Item $PROFILE).LastWriteTime

  # You can even *assign* to such expressions.
  ($profileFile = Get-Item $PROFILE).LastWriteTime = Get-Date

  ７ Note

  While this syntax is allowed, its use is discouraged. There are cases where this does
  not work and the intent of the code author can be confusing to other code
  reviewers.

Limitations
The assignment case doesn't always work. When it doesn't work, the assignment is
discarded. If you create an instance of a mutable value type and attempt to both save
the instance in a variable and modify one of its properties in the same expression, the
property assignment is discarded.

  PowerShell

  # create mutable value type
  PS> Add-Type 'public struct Foo { public int x; }'

  # Create an instance, store it in a variable, and try to modify its
  property.
  # This assignment is effectively IGNORED.
  PS> ($var = [Foo]::new()).x = 1
  PS> $var.x
  0

<!-- p.451 -->

The difference is that you can't return a reference to the value. Essentially, ($var =
[Foo]::new()) is equivalent to $($var = [Foo]::new(); $var) . You're no longer

performing a member access on the variable you're performing a member access on the
variable's output, which is a copy.

The workaround is to create the instance and save it in a variable first, and then assign
to the property via the variable:

  PowerShell

  # create mutable value type
  PS> Add-Type 'public struct Foo { public int x; }'

  # Create an instance and store it in a variable first
  # and then modify its property via the variable.
  PS> $var = [Foo]::new()
  PS> $var.x = 1
  PS> $var.x
  1

<!-- p.452 -->

Avoid using Invoke-Expression
Article • 11/17/2022

The Invoke-Expression cmdlet should only be used as a last resort. In most scenarios,
safer and more robust alternatives are available. Forums like Stack Overflow are filled
with examples of Invoke-Expression misuse. Also note that PSScriptAnalyzer has a rule
for this. For more information, see AvoidUsingInvokeExpression.

Carefully consider the security implications. When a string from an untrusted source
such as user input is passed directly to Invoke-Expression , arbitrary commands can be
executed. Always consider a different, more robust and secure solution first.

Common scenarios
Consider the following usage scenarios:

      It's simpler to redirect PowerShell to execute something naturally. For example:

        PowerShell

        Get-Content ./file.ps1 | Invoke-Expression

      These cases are trivially avoidable. The script or code already exists in file or AST
      form, so you should write a script with parameters and invoke it directly instead of
      using Invoke-Expression on a string.

      Running a script from a trusted source. For example, running the install script
      from the PowerShell repository:

        PowerShell

        Invoke-WebRequest https://aka.ms/install-powershell.ps1 | Invoke-
        Expression

      You should only use this interactively. And, while this does make life simpler, this
      practice should be discouraged.

      Testing for parsing errors. The PowerShell team tests for parse errors in the source
      code using Invoke-Expression because that's the only way to turn a parse-time
      error into a runtime one.

<!-- p.453 -->

Conclusion
Most other scripting languages have a way to evaluate a string as code, and as an
interpreted language, PowerShell must have a way to dynamically run itself. But there's
no good reason to use Invoke-Expression in a production environment.

References
     Stack Overflow discussion - In what scenario was Invoke-Expression designed to be
     used?
     PowerShell Blog post - Invoke-Expression Considered Harmful

<!-- p.454 -->

Limitations of PowerShell transcripts
Article • 04/30/2025

Mixing Write-Host output with the output objects, strings, and PowerShell transcription is
complicated. There is a subtle interaction between the script and how transcription works with
PowerShell pipelines that can have unexpected results.

When you emit objects from your script the formatting of those objects is handled by Out-
Default . But the formatting can occur after the script has completed and transcription has

stopped. This means that the output doesn't get transcribed. Strings are handled differently.
Sometimes string output is passed through formatting, but not always. Write-Host makes an
immediate write to the host process. Write-Output is sent through the formatting system.
Combining the output of complex objects with writes to the host makes it difficult to predict
what gets logged in the transcript.

Scenario 1 - Output of a structured object after all
other operations
Consider the following script and its output:

  PowerShell

  PS> Get-Content scenario1.ps1
  Start-Transcript scenario1.log -UseMinimalHeader
  Write-Host '1'
  Write-Output '2'
  Get-Location
  Write-Host '4'
  Write-Output '5'
  Stop-Transcript

  PS> ./scenario1.ps1
  Transcript started, output file is scenario1.log
  1
  2

  4
  Path
  ----
  /Users/user1/src/projects/transcript
  5
  Transcript stopped, output file is
  /Users/user1/src/projects/transcript/scenario1.log

<!-- p.455 -->

The output to the console shows the output you expect, but not in the order you expect it.
Write-Host 4 is visible before Get-Location because Write-Host is optimized to write directly

to the host. There's code in transcription that copies the output to the transcript file and the
console. Then we have the regular output of Get-Location and Write-Output 5 sent as output
of the script.

  PowerShell

  PS> Get-Content scenario1.log
  **********************
  PowerShell transcript start
  Start time: 20191106114858
  **********************
  Transcript started, output file is s2
  1
  2

  4
  **********************
  PowerShell transcript end
  End time: 20191106114858
  **********************

Since transcription is turned off before the script exits, it's not rendered in the transcript. The
objects were sent to the next consumer in the pipeline. In this case, it's Out-Default , which
PowerShell inserted automatically. To complicate things further, the output of strings is also
optimized in the formatting system. The first Write-Output 2 gets emitted and captured by the
transcript. But the insertion of the Get-Location object causes its output to be pushed into the
stack of things that need actual formatting, which sets a bit of state for any remaining objects
that also may need formatting. This is why the second Write-Output 5 doesn't get added to
the transcript.

Scenario 2 - Move the object emission to the
beginning
Consider the following script and its output:

  PowerShell

  PS> Get-Content scenario2.ps1
  Start-Transcript scenario2.log -UseMinimalHeader
  Get-Location
  Write-Host '1'
  Write-Output '2'
  Get-Location

<!-- p.456 -->

  Write-Host '4'
  Write-Output '5'
  Stop-Transcript

  PS> ./scenario2.ps1
  Transcript started, output file is scenario2.log

  1
  4
  Path
  ----
  /Users/user1/src/projects/transcript
  2
  5
  Transcript stopped, output file is
  /Users/user1/src/projects/transcript/scenario2.log

We can see that the Write-Host commands happen before anything, and then the objects start
to come out. The Write-Output of a string forces the object to be rendered to the screen, but
notice that the transcript contains only the output of Write-Host . That's because those string
objects are piped to Out-Default for formatting after the script turned off transcription.

  PowerShell

  PS> Get-Content scenario2.log
  **********************
  PowerShell transcript start
  Start time: 20220606094609
  **********************
  Transcript started, output file is s3

  1
  4
  **********************
  PowerShell transcript end
  End time: 20220606094609
  **********************

Scenario 3 - Object emitted at the end of the script
For this scenario, the output of the complex object is at the end of the script.

  PowerShell

  PS> Get-Content scenario3.ps1
  Start-Transcript scenario3.log -UseMinimalHeader
  Write-Host '1'
  Write-Output '2'
  Write-Host '4'

<!-- p.457 -->

  Write-Output '5'
  Get-Location
  Stop-Transcript

  PS> ./scenario3.ps1
  Transcript started, output file is scenario3.log
  1
  2
  4
  5

  Path
  ----
  /Users/user1/src/projects/transcript
  Transcript stopped, output file is
  /Users/user1/src/projects/transcript/scenario3.log

The string output from both Write-Host and Write-Output makes it into the transcript.
However, the output from Get-Location occurs after transcription has stopped.

  **********************
  PowerShell transcript start
  Start time: 20220606100342
  **********************
  Transcript started, output file is scenario3.log
  1
  2
  4
  5

  **********************
  PowerShell transcript end
  End time: 20220606100342
  **********************

A way to ensure full transcription
This example is a slight variation on the original scenario, but now everything is logged to the
transcript. The original code is wrapped in a script block and the formatter explicitly invoked
via Out-Default .

  PowerShell

  PS> Get-Content scenario4.ps1
  Start-Transcript scenario4.log -UseMinimalHeader
  . {
      Write-Host '1'

<!-- p.458 -->

      Write-Output '2'
      Get-Location
      Write-Host '4'
      Write-Output '5'
  } | Out-Default
  Stop-Transcript

  PS> ./scenario4.ps1
  Transcript started, output file is scenario4.log
  1
  2

  4
  Path
  ----
  /Users/user1/src/projects/transcript
  5

  Transcript stopped, output file is
  /Users/user1/src/projects/transcript/scenario4.log

Notice that the last Write-Host call is still out of order, that's because of the optimization in
Write-Host that doesn't go into the output stream.

  PowerShell

  PS> Get-Content scenario4.log
  **********************
  PowerShell transcript start
  Start time: 20220606101038
  **********************
  Transcript started, output file is s5
  1
  2

  4
  Path
  ----
  /Users/user1/src/projects/transcript
  5

  **********************
  PowerShell transcript end
  End time: 20220606101038
  **********************

<!-- p.459 -->

Sample scripts for system administration
A collection of examples walks through scenarios for administering systems with PowerShell.

  Working with objects

  ｃ HOW-TO GUIDE
  Viewing object structure

  Selecting parts of objects

  Removing objects from the pipeline

  Sorting objects

  Creating .NET and COM objects

  Using static classes and methods

  Getting WMI objects with Get-CimInstance

  Manipulating items directly

  Managing computers

  ｃ HOW-TO GUIDE
  Changing computer state

  Collecting information about computers

  Creating Get-WinEvent queries with FilterHashtable

  Managing processes & services

  ｃ HOW-TO GUIDE
  Managing processes with process cmdlets

  Managing services

  Working with printers

<!-- p.460 -->

Performing networking tasks

Working with software installations

Decode a PowerShell command from a running process

Working with output

ｐ CONCEPT
Redirecting output

Using format commands to change output view

Managing drives & files

ｃ HOW-TO GUIDE
Managing current location

Managing PowerShell drives

Working with files and folders

Working with files folders and registry keys

Working with registry entries

Working with registry keys

Creating UI elements

ｃ HOW-TO GUIDE
Creating a custom input box

Creating a graphical date picker

Multiple selection list boxes

Selecting items from a list box

<!-- p.461 -->

Viewing object structure
Article • 12/09/2022

Because objects play such a central role in PowerShell, there are several native
commands designed to work with arbitrary object types. The most important one is the
Get-Member command.

The simplest technique for analyzing the objects that a command returns is to pipe the
output of that command to the Get-Member cmdlet. The Get-Member cmdlet shows you
the formal name of the object type and a complete listing of its members. The number
of elements that are returned can sometimes be overwhelming. For example, a process
object can have over 100 members.

The following command allows you to see all the members of a Process object and page
through the output.

  PowerShell

  Get-Process | Get-Member | Out-Host -Paging

  Output

  TypeName: System.Diagnostics.Process

  Name                               MemberType       Definition
  ----                               ----------       ----------
  Handles                            AliasProperty    Handles = Handlecount
  Name                               AliasProperty    Name = ProcessName
  NPM                                AliasProperty    NPM = NonpagedSystemMemorySize
  PM                                 AliasProperty    PM = PagedMemorySize
  VM                                 AliasProperty    VM = VirtualMemorySize
  WS                                 AliasProperty    WS = WorkingSet
  add_Disposed                       Method           System.Void
  add_Disposed(Event...
  ...

We can make this long list of information more usable by filtering for elements we want
to see. The Get-Member command lets you list only members that are properties. There
are several forms of properties. The cmdlet displays properties of a type using the
MemberType parameter with the value Properties . The resulting list is still very long,
but a more manageable:

  PowerShell

<!-- p.462 -->

  Get-Process | Get-Member -MemberType Properties

  Output

      TypeName: System.Diagnostics.Process

  Name                           MemberType       Definition
  ----                           ----------       ----------
  Handles                        AliasProperty    Handles = Handlecount
  Name                           AliasProperty    Name = ProcessName
  ...
  ExitCode                       Property         System.Int32 ExitCode {get;}
  ...
  Handle                         Property         System.IntPtr Handle {get;}
  ...
  CPU                            ScriptProperty System.Object CPU
  {get=$this.Total...
  ...
  Path                           ScriptProperty System.Object Path
  {get=$this.Main...
  ...

  ７ Note

  The allowed values of MemberType are AliasProperty, CodeProperty, Property,
  NoteProperty, ScriptProperty, Properties, PropertySet, Method, CodeMethod,
  ScriptMethod, Methods, ParameterizedProperty, MemberSet, and All.

There are more than 60 properties for a process. By default, PowerShell determines how
to display an object type using information stored in XML files that have names ending
in .format.ps1xml . The formatting definition for process objects is stored in
DotNetTypes.format.ps1xml .

If you need to look at properties other than those that PowerShell displays by default,
you can format the output using the Format-* cmdlets.

<!-- p.463 -->

Selecting parts of objects
You can use the Select-Object cmdlet to create new, custom PowerShell objects that contain
properties selected from the objects you use to create them. Type the following command to
create a new object that includes only the Name and FreeSpace properties of the
Win32_LogicalDisk WMI class:

  PowerShell

  Get-CimInstance -Class Win32_LogicalDisk |
      Select-Object -Property Name, FreeSpace

  Output

  Name        FreeSpace
  ----        ---------
  C:        50664845312

With Select-Object you can create calculated properties to display FreeSpace in gigabytes
rather than bytes.

  PowerShell

  Get-CimInstance -Class Win32_LogicalDisk |
      Select-Object -Property Name, @{
          Label='FreeSpace'
          Expression={($_.FreeSpace/1GB).ToString('F2')}
      }

  Output

  Name      FreeSpace
  ----      ---------
  C:        47.18

 Last updated on 03/24/2025

<!-- p.464 -->

Removing objects from the pipeline
Article • 12/09/2022

In PowerShell, you often generate and pass along more objects to a pipeline than you
want. You can specify the properties of particular objects to display using the Format-*
cmdlets, but this doesn't help with the problem of removing entire objects from the
display. You may want to filter objects before the end of a pipeline, so you can perform
actions on only a subset of the initially generated objects.

PowerShell includes a Where-Object cmdlet that allows you to test each object in the
pipeline and only pass it along the pipeline if it meets a particular test condition. Objects
that don't pass the test are removed from the pipeline. You supply the test condition as
the value of the FilterScript parameter.

Performing simple tests with Where-Object
The value of FilterScript is a script block - one or more PowerShell commands
surrounded by braces ( {} ) - that evaluates to true or false. These script blocks can be
simple, but creating them requires knowing about another PowerShell concept,
comparison operators. A comparison operator compares the items that appear on each
side of it. Comparison operators begin with a hyphen character ( - ) and are followed by
a name. Basic comparison operators work on almost any kind of object. The more
advanced comparison operators might only work on text or arrays.

  ７ Note

  By default, PowerShell comparison operators are case-insensitive.

Due to parsing considerations, symbols such as < , > , and = aren't used as comparison
operators. Instead, comparison operators are comprised of letters. The basic comparison
operators are listed in the following table.

                                                                            ﾉ   Expand table

 Comparison Operator      Meaning                                 Example (returns true)

 -eq                      is equal to                             1 -eq 1

 -ne                      isn't equal to                          1 -ne 2

 -lt                      Is less than                            1 -lt 2

<!-- p.465 -->

 Comparison Operator       Meaning                                     Example (returns true)

 -le                       Is less than or equal to                    1 -le 2

 -gt                       Is greater than                             2 -gt 1

 -ge                       Is greater than or equal to                 2 -ge 1

 -like                     Is like (wildcard comparison for text)      "file.doc" -like "f*.do?"

 -notlike                  isn't like (wildcard comparison for text)   "file.doc" -notlike "p*.doc"

 -contains                 Contains                                    1,2,3 -contains 1

 -notcontains              doesn't contain                             1,2,3 -notcontains 4

Where-Object script blocks use the special variable $_ to refer to the current object in

the pipeline. Here is an example of how it works. If you have a list of numbers, and only
want to return the ones that are less than 3, you can use Where-Object to filter the
numbers by typing:

  1,2,3,4 | Where-Object {$_ -lt 3}
  1
  2

Filtering based on object properties
Since $_ refers to the current pipeline object, we can access its properties for our tests.

As an example, we can look at the Win32_SystemDriver class in WMI. There might be
hundreds of system drivers on a particular system, but you might only be interested in a
particular set of the system drivers, such as those that are running. For the
Win32_SystemDriver class the relevant property is State. You can filter the system
drivers, selecting only the running ones by typing:

  PowerShell

  Get-CimInstance -Class Win32_SystemDriver |
      Where-Object {$_.State -eq 'Running'}

This still produces a long list. You may want to filter to only select the drivers set to start
automatically by testing the StartMode value as well:

<!-- p.466 -->

  PowerShell

  Get-CimInstance -Class Win32_SystemDriver |
      Where-Object {$_.State -eq "Running"} |
      Where-Object {$_.StartMode -eq "Auto"}

  Output

  DisplayName : RAS Asynchronous Media Driver
  Name        : AsyncMac
  State       : Running
  Status      : OK
  Started     : True

  DisplayName : Audio Stub Driver
  Name        : audstub
  State       : Running
  Status      : OK
  Started     : True
  ...

This gives us a lot of information we no longer need because we know that the drivers
are running. In fact, the only information we probably need at this point are the name
and the display name. The following command includes only those two properties,
resulting in much simpler output:

  PowerShell

  Get-CimInstance -Class Win32_SystemDriver |
      Where-Object {$_.State -eq "Running"} |
      Where-Object {$_.StartMode -eq "Manual"} |
      Format-Table -Property Name,DisplayName

  Output

  Name                DisplayName
  ----                -----------
  AsyncMac                 RAS Asynchronous Media Driver
  bindflt                  Windows Bind Filter Driver
  bowser                   Browser
  CompositeBus             Composite Bus Enumerator Driver
  condrv                   Console Driver
  HdAudAddService          Microsoft 1.1 UAA Function Driver for High Definition
  Audio Service
  HDAudBus                 Microsoft UAA Bus Driver for High Definition Audio
  HidUsb                   Microsoft HID Class Driver
  HTTP                     HTTP Service
  igfx                     igfx
  IntcDAud                 Intel(R) Display Audio

<!-- p.467 -->

     intelppm                 Intel Processor Driver
     ...

There are two Where-Object elements in the above command, but they can be
expressed in a single Where-Object element using the -and logical operator, like this:

  PowerShell

     Get-CimInstance -Class Win32_SystemDriver |
         Where-Object {($_.State -eq 'Running') -and ($_.StartMode -eq 'Manual')}
     |
         Format-Table -Property Name,DisplayName

The standard logical operators are listed in the following table.

                                                                              ﾉ   Expand table

 Logical Operator     Meaning                                    Example (returns true)

 -and                 Logical and; true if both sides are true   (1 -eq 1) -and (2 -eq 2)

 -or                  Logical or; true if either side is true    (1 -eq 1) -or (1 -eq 2)

 -not                 Logical not; reverses true and false       -not (1 -eq 2)

 !                    Logical not; reverses true and false       !(1 -eq 2)

<!-- p.468 -->

Sorting objects
We can organize displayed data to make it easier to scan using the Sort-Object cmdlet. Sort-
Object takes the name of one or more properties to sort on, and returns data sorted by the

values of those properties.

Basic sorting
Consider the problem of listing subdirectories and files in the current directory. If we want to
sort by LastWriteTime and then by Name, we can do it by typing:

 PowerShell

 Get-ChildItem |
     Sort-Object -Property LastWriteTime, Name |
     Format-Table -Property LastWriteTime, Name

 Output

 LastWriteTime                Name
 -------------                ----
 11/6/2017 10:10:11 AM        .localization-config
 11/6/2017 10:10:11 AM        .openpublishing.build.ps1
 11/6/2017 10:10:11 AM        appveyor.yml
 11/6/2017 10:10:11 AM        LICENSE
 11/6/2017 10:10:11 AM        LICENSE-CODE
 11/6/2017 10:10:11 AM        ThirdPartyNotices
 11/6/2017 10:10:15 AM        tests
 6/6/2018 7:58:59 PM          CONTRIBUTING.md
 6/6/2018 7:58:59 PM          README.md
 ...

You can also sort the objects in reverse order by specifying the Descending [switch]
parameter.

 PowerShell

 Get-ChildItem |
   Sort-Object -Property LastWriteTime, Name -Descending |
   Format-Table -Property LastWriteTime, Name

 Output

<!-- p.469 -->

 LastWriteTime              Name
 -------------              ----
 12/1/2018 10:13:50 PM      reference
 12/1/2018 10:13:50 PM      dsc
 ...
 6/6/2018 7:58:59 PM        README.md
 6/6/2018 7:58:59 PM        CONTRIBUTING.md
 11/6/2017 10:10:15 AM      tests
 11/6/2017 10:10:11 AM      ThirdPartyNotices
 11/6/2017 10:10:11 AM      LICENSE-CODE
 11/6/2017 10:10:11 AM      LICENSE
 11/6/2017 10:10:11 AM      appveyor.yml
 11/6/2017 10:10:11 AM      .openpublishing.build.ps1
 11/6/2017 10:10:11 AM      .localization-config

Using hash tables
You can sort different properties in different orders using hash tables in an array. Each hash
table uses an Expression key to specify the property name as string and an Ascending or
Descending key to specify the sort order by $true or $false . The Expression key is
mandatory. The Ascending or Descending key is optional.

The following example sorts objects in descending LastWriteTime order and ascending Name
order.

 PowerShell

 Get-ChildItem |
   Sort-Object -Property @{ Expression = 'LastWriteTime'; Descending = $true },
                         @{ Expression = 'Name'; Ascending = $true } |
   Format-Table -Property LastWriteTime, Name

 Output

 LastWriteTime          Name
 -------------          ----
 12/1/2018 10:13:50 PM dsc
 12/1/2018 10:13:50 PM reference
 11/29/2018 6:56:01 PM .openpublishing.redirection.json
 11/29/2018 6:56:01 PM gallery
 11/24/2018 10:33:22 AM developer
 11/20/2018 7:22:19 PM .markdownlint.json
 ...

You can also set a scriptblock to the Expression key. When running the Sort-Object cmdlet,
the scriptblock is executed and the result is used for sorting.

<!-- p.470 -->

The following example sorts objects in descending order by the time span between
CreationTime and LastWriteTime.

 PowerShell

 Get-ChildItem |
     Sort-Object -Property @{ Exp = { $_.LastWriteTime - $_.CreationTime }; Desc =
 $true } |
     Format-Table -Property LastWriteTime, CreationTime

 Output

 LastWriteTime              CreationTime
 -------------              ------------
 12/1/2018 10:13:50 PM      11/6/2017 10:10:11 AM
 12/1/2018 10:13:50 PM      11/6/2017 10:10:11 AM
 11/7/2018 6:52:24 PM       11/6/2017 10:10:11 AM
 11/7/2018 6:52:24 PM       11/6/2017 10:10:15 AM
 11/3/2018 9:58:17 AM       11/6/2017 10:10:11 AM
 10/26/2018 4:50:21 PM      11/6/2017 10:10:11 AM
 11/17/2018 1:10:57 PM      11/29/2017 5:48:30 PM
 11/12/2018 6:29:53 PM      12/7/2017 7:57:07 PM
 ...

Tips
You can omit the Property parameter name as following:

 PowerShell

 Sort-Object LastWriteTime, Name

Besides, you can refer to Sort-Object by its built-in alias, sort :

 PowerShell

 sort LastWriteTime, Name

The keys in the hash tables for sorting can be abbreviated as following:

 PowerShell

 Sort-Object @{ e = 'LastWriteTime'; d = $true }, @{ e = 'Name'; a = $true }

<!-- p.471 -->

In this example, the e stands for Expression, the d stands for Descending, and the a stands for
Ascending.

To improve readability, you can place the hash tables into a separate variable:

  PowerShell

  $order = @(
    @{ Expression = 'LastWriteTime'; Descending = $true }
    @{ Expression = 'Name'; Ascending = $true }
  )

  Get-ChildItem |
      Sort-Object $order |
      Format-Table LastWriteTime, Name

 Last updated on 04/08/2026

<!-- p.472 -->

Creating .NET and COM objects
  This sample only runs on Windows platforms.

There are software components with .NET Framework and COM interfaces that enable you to
perform many system administration tasks. PowerShell lets you use these components, so you
aren't limited to the tasks that can be performed by using cmdlets. Many of the cmdlets in the
initial release of PowerShell don't work against remote computers. We will demonstrate how to
get around this limitation when managing event logs by using the .NET Framework
System.Diagnostics.EventLog class directly from PowerShell.

Using New-Object for event log access
The .NET Framework Class Library includes a class named System.Diagnostics.EventLog that
can be used to manage event logs. You can create a new instance of a .NET Framework class by
using the New-Object cmdlet with the TypeName parameter. For example, the following
command creates an event log reference:

 PowerShell

 New-Object -TypeName System.Diagnostics.EventLog

 Output

    Max(K) Retain OverflowAction            Entries Name
    ------ ------ --------------            ------- ----

Although the command has created an instance of the EventLog class, the instance doesn't
include any data. that's because we didn't specify a particular event log. How do you get a real
event log?

Using constructors with New-Object
To refer to a specific event log, you need to specify the name of the log. New-Object has an
ArgumentList parameter. The arguments you pass as values to this parameter are used by a
special startup method of the object. The method is called a constructor because it's used to

<!-- p.473 -->

construct the object. For example, to get a reference to the Application log, you specify the
string 'Application' as an argument:

 PowerShell

 New-Object -TypeName System.Diagnostics.EventLog -ArgumentList Application

 Output

 Max(K) Retain OverflowAction             Entries Name
 ------ ------ --------------             ------- ----
 16,384      7 OverwriteOlder               2,160 Application

  ７ Note

  Since most of the .NET classes are contained in the System namespace, PowerShell
  automatically attempts to find classes you specify in the System namespace if it can't find
  a match for the typename you specify. This means that you can specify
  Diagnostics.EventLog instead of System.Diagnostics.EventLog .

Storing Objects in Variables
You might want to store a reference to an object, so you can use it in the current shell.
Although PowerShell lets you do a lot of work with pipelines, lessening the need for variables,
sometimes storing references to objects in variables makes it more convenient to manipulate
those objects.

The output from any valid PowerShell command can be stored in a variable. Variable names
always begin with $ . If you want to store the Application log reference in a variable named
$AppLog , type the name of the variable, followed by an equal sign and then type the command

used to create the Application log object:

 PowerShell

 $AppLog = New-Object -TypeName System.Diagnostics.EventLog -ArgumentList
 Application

If you then type $AppLog , you can see that it contains the Application log:

 PowerShell

<!-- p.474 -->

 $AppLog

 Output

   Max(K) Retain OverflowAction           Entries Name
   ------ ------ --------------           ------- ----
   16,384      7 OverwriteOlder             2,160 Application

Accessing a remote event log with New-Object
The commands used in the preceding section target the local computer; the Get-EventLog
cmdlet can do that. To access the Application log on a remote computer, you must supply both
the log name and a computer name (or IP address) as arguments.

 PowerShell

 $RemoteAppLog = New-Object -TypeName System.Diagnostics.EventLog Application,
 192.168.1.81
 $RemoteAppLog

 Output

   Max(K) Retain OverflowAction           Entries Name
   ------ ------ --------------           ------- ----
      512      7 OverwriteOlder               262 Application

Now that we have a reference to an event log stored in the $RemoteAppLog variable, what tasks
can we perform on it?

Clearing an event log with object methods
Objects often have methods that can be called to perform tasks. You can use Get-Member to
display the methods associated with an object. The following command and selected output
show some the methods of the EventLog class:

 PowerShell

 $RemoteAppLog | Get-Member -MemberType Method

 Output

     TypeName: System.Diagnostics.EventLog

<!-- p.475 -->

 Name                         MemberType Definition
 ----                         ---------- ----------
 ...
 Clear                        Method       System.Void Clear()
 Close                        Method       System.Void Close()
 ...
 GetType                      Method       System.Type GetType()
 ...
 ModifyOverflowPolicy         Method       System.Void ModifyOverflowPolicy(Overfl...
 RegisterDisplayName          Method       System.Void RegisterDisplayName(String ...
 ...
 ToString                     Method       System.String ToString()
 WriteEntry                   Method       System.Void WriteEntry(String message),...
 WriteEvent                   Method       System.Void WriteEvent(EventInstance in...

The Clear() method can be used to clear the event log. When calling a method, you must
always follow the method name by parentheses, even if the method doesn't require arguments.
This lets PowerShell distinguish between the method and a potential property with the same
name. Type the following to call the Clear method:

 PowerShell

 $RemoteAppLog.Clear()
 $RemoteAppLog

 Output

    Max(K) Retain OverflowAction            Entries Name
    ------ ------ --------------            ------- ----
       512      7 OverwriteOlder                  0 Application

Notice that the event log was cleared and now has 0 entries instead of 262.

Creating COM objects with New-Object
You can use New-Object to work with Component Object Model (COM) components.
Components range from the various libraries included with Windows Script Host (WSH) to
ActiveX applications such as Internet Explorer that are installed on most systems.

New-Object uses .NET Framework Runtime-Callable Wrappers to create COM objects, so it has

the same limitations that .NET Framework does when calling COM objects. To create a COM
object, you need to specify the ComObject parameter with the Programmatic Identifier or
ProgId of the COM class you want to use. A complete discussion of the limitations of COM use
and determining what ProgIds are available on a system is beyond the scope of this user's

<!-- p.476 -->

guide, but most well-known objects from environments such as WSH can be used within
PowerShell.

You can create the WSH objects by specifying these progids: WScript.Shell, WScript.Network,
Scripting.Dictionary, and Scripting.FileSystemObject. The following commands create these
objects:

 PowerShell

 New-Object -ComObject WScript.Shell
 New-Object -ComObject WScript.Network
 New-Object -ComObject Scripting.Dictionary
 New-Object -ComObject Scripting.FileSystemObject

Although most of the functionality of these classes is made available in other ways in Windows
PowerShell, a few tasks such as shortcut creation are still easier to do using the WSH classes.

Creating a desktop shortcut with WScript.Shell
One task that can be performed quickly with a COM object is creating a shortcut. Suppose you
want to create a shortcut on your desktop that links to the home folder for PowerShell. You
first need to create a reference to WScript.Shell, which we will store in a variable named
$WshShell :

 PowerShell

 $WshShell = New-Object -ComObject WScript.Shell

Get-Member works with COM objects, so you can explore the members of the object by typing:

 PowerShell

 $WshShell | Get-Member

 Output

     TypeName: System.__ComObject#{41904400-be18-11d3-a28b-00104bd35090}

 Name                         MemberType              Definition
 ----                         ----------              ----------
 AppActivate                  Method                  bool AppActivate (Variant, Va...
 CreateShortcut               Method                  IDispatch CreateShortcut (str...
 ...

<!-- p.477 -->

Get-Member has an optional InputObject parameter you can use instead of piping to provide

input to Get-Member . You would get the same output as shown above if you instead used the
command Get-Member -InputObject $WshShell. If you use InputObject, it treats its argument
as a single item. This means that if you have several objects in a variable, Get-Member treats
them as an array of objects. For example:

 PowerShell

 $a = 1,2,"three"
 Get-Member -InputObject $a

 Output

 TypeName: System.Object[]
 Name               MemberType    Definition
 ----               ----------    ----------
 Count              AliasProperty Count = Length
 ...

The WScript.Shell CreateShortcut method accepts a single argument, the path to the shortcut
file to create. We could type in the full path to the desktop, but there is an easier way. The
desktop is normally represented by a folder named Desktop inside the home folder of the
current user. Windows PowerShell has a variable $HOME that contains the path to this folder. We
can specify the path to the home folder by using this variable, and then add the name of the
Desktop folder and the name for the shortcut to create by typing:

 PowerShell

 $lnk = $WshShell.CreateShortcut("$HOME\Desktop\PSHome.lnk")

When you use something that looks like a variable name inside double-quotes, PowerShell tries
to substitute a matching value. If you use single-quotes, PowerShell doesn't try to substitute
the variable value. For example, try typing the following commands:

 PowerShell

 "$HOME\Desktop\PSHome.lnk"

 Output

 C:\Documents and Settings\aka\Desktop\PSHome.lnk

<!-- p.478 -->

 PowerShell

 '$HOME\Desktop\PSHome.lnk'

 Output

 $HOME\Desktop\PSHome.lnk

We now have a variable named $lnk that contains a new shortcut reference. If you want to see
its members, you can pipe it to Get-Member . The output below shows the members we need to
use to finish creating our shortcut:

 PowerShell

 $lnk | Get-Member

 Output

 TypeName: System.__ComObject#{f935dc23-1cf0-11d0-adb9-00c04fd58a0b}
 Name             MemberType   Definition
 ----             ----------   ----------
 ...
 Save             Method       void Save ()
 ...
 TargetPath       Property     string TargetPath () {get} {set}

We need to specify the TargetPath, which is the application folder for PowerShell, and then
save the shortcut by calling the Save method. The PowerShell application folder path is stored
in the variable $PSHOME , so we can do this by typing:

 PowerShell

 $lnk.TargetPath = $PSHOME
 $lnk.Save()

Using Internet Explorer from PowerShell
Many applications, including the Microsoft Office family of applications and Internet Explorer,
can be automated by using COM. The following examples illustrate some of the typical
techniques and issues involved in working with COM-based applications.

You create an Internet Explorer instance by specifying the Internet Explorer ProgId,
InternetExplorer.Application:

<!-- p.479 -->

 PowerShell

 $ie = New-Object -ComObject InternetExplorer.Application

This command starts Internet Explorer, but doesn't make it visible. If you type Get-Process , you
can see that a process named iexplore is running. In fact, if you exit PowerShell, the process
will continue to run. You must reboot the computer or use a tool like Task Manager to end the
iexplore process.

  ７ Note

  COM objects that start as separate processes, commonly called ActiveX executables, may
  or may not display a user interface window when they start up. If they create a window
  but don't make it visible, like Internet Explorer, the focus usually moves to the Windows
  desktop. You must make the window visible to interact with it.

By typing $ie | Get-Member , you can view properties and methods for Internet Explorer. To see
the Internet Explorer window, set the Visible property to $true by typing:

 PowerShell

 $ie.Visible = $true

You can then navigate to a specific Web address using the Navigate method:

 PowerShell

 $ie.Navigate("https://devblogs.microsoft.com/scripting/")

Using other members of the Internet Explorer object model, it's possible to retrieve text
content from the Web page. The following command displays the HTML text in the body of the
current Web page:

 PowerShell

 $ie.Document.Body.InnerText

To close Internet Explorer from within PowerShell, call its Quit() method:

 PowerShell

<!-- p.480 -->

 $ie.Quit()

The $ie variable no longer contains a valid reference even though it still appears to be a COM
object. If you attempt to use it, PowerShell returns an automation error:

 PowerShell

 $ie | Get-Member

 Output

 Get-Member : Exception retrieving the string representation for property "Appli
 cation" : "The object invoked has disconnected from its clients. (Exception fro
 m HRESULT: 0x80010108 (RPC_E_DISCONNECTED))"
 At line:1 char:16
 + $ie | Get-Member <<<<

You can either remove the remaining reference with a command like $ie = $null , or
completely remove the variable by typing:

 PowerShell

 Remove-Variable ie

  ７ Note

  There is no common standard for whether ActiveX executables exit or continue to run
  when you remove a reference to one. Depending on circumstances, such as whether the
  application is visible, whether an edited document is running in it, and even whether
  PowerShell is still running, the application may or may not exit. For this reason, you should
  test termination behavior for each ActiveX executable you want to use in PowerShell.

Getting warnings about .NET Framework-wrapped
COM objects
In some cases, a COM object might have an associated .NET Framework Runtime-Callable
Wrapper (RCW) that's used by New-Object . Since the behavior of the RCW may be different
from the behavior of the normal COM object, New-Object has a Strict parameter to warn you
