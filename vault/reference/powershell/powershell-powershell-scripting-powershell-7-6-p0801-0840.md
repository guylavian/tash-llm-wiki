---
title: "How to use this documentation — pages 801-840"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0801-0840
family: powershell
documentKind: "doc"
abstract: "Script files can't be imported as modules PowerShell allows you to import script files ( .ps1 ) as a module. All defined functions become publicly accessible. ConstrainedLanguage mode blocks importation of script file to prevent unintended exposure of dangerous script functions."
---

# How to use this documentation — pages 801-840

<!-- p.801 -->

     Script files can't be imported as modules

     PowerShell allows you to import script files ( .ps1 ) as a module. All defined functions
     become publicly accessible. ConstrainedLanguage mode blocks importation of script file
     to prevent unintended exposure of dangerous script functions.

     Setting variables AllScope restriction

     ConstrainedLanguage mode disables the ability to set AllScope on variables. Limiting the

     scope of variables prevents the variables from interfering with the session state of trusted
     commands.

     Type method invocation not allowed

     ConstrainedLanguage mode doesn't allow method invocation on unapproved types.

     Blocking methods on unapproved types prevents invocation of .NET type methods that
     might be dangerous or allow code injection.

     Type property setters not allowed

     ConstrainedLanguage mode restricts invocation of property setters on unapproved types.

     Blocking property setters on unapproved types prevents code injection attacks.

     Type creation not allowed

     ConstrainedLanguage mode blocks type creation on unapproved types to block untrusted

     constructors that could allow code injection.

     Module scope operator not allowed

     ConstrainedLanguage mode doesn't allow the use of the module scope operator. For

     example: & (Get-Module MyModule) MyFunction . Blocking the module scope operator
     prevents access to module private functions and variables.

Further reading
     For more information about PowerShell language modes, see about_Language_Modes.
     For information about how to configure and use App Control, see How to use App
     Control for PowerShell.

Last updated on 12/09/2025

<!-- p.802 -->

How to use App Control to secure
PowerShell
This article describes how to set up a App Control for Business policy. You can configure the
policy to enforce or audit the policy's rule. In audit mode, PowerShell behavior doesn't change
but it logs Event ID 16387 messages to the PowerShellCore/Analytic event log. In enforcement
mode, PowerShell applies the policy's restrictions.

This article assumes you're using a test machine so that you can test PowerShell behavior
under a machine wide App Control policy before you deploy the policy in your environment.

Create an App Control policy
An App Control policy is described in an XML file, which contains information about policy
options, files allowed, and signing certificates recognized by the policy. When the policy is
applied, only approved files are allowed to load and run. PowerShell either blocks unapproved
script files from running or runs them in ConstrainedLanguage mode, depending on policy
options.

You create and manipulate App Control policy using the ConfigCI module, which is available
on all supported Windows versions. This Windows PowerShell module can be used in Windows
PowerShell 5.1 or in PowerShell 7 through the Windows Compatibility layer. It's easier to use
this module in Windows PowerShell. The policy you create can be applied to any version of
PowerShell.

Steps to create an App Control policy
For testing, you just need to create a default policy and a self signed code signing certificate.

   1. Create a default policy

       PowerShell
       New-CIPolicy -Level PcaCertificate -FilePath .\SystemCIPolicy.xml -UserPEs

     This command creates a default policy file called SystemCIPolicy.xml that allows all
     Microsoft code-signed files to run.

        ７ Note

<!-- p.803 -->

    Running this command can take up to two hours because it must scan the entire test
    machine.

2. Disable Audit Mode in default policy

  A new policy is always created in Audit mode. To test policy enforcement, you need to
  disable Audit mode when you apply the policy. Edit the SystemCIPolicy.xml file using a
  text editor like notepad.exe or Visual Studio Code (VS Code). Comment out the Audit
  mode option.

   XML

   <!--
   <Rule>
     <Option>Enabled:Audit Mode</Option>
   </Rule>
   -->

3. Create a self-signed code signing certificate

  You need a code signing certificate to sign any test binaries or script files that you want to
  run on your test machine. The New-SelfSignedCertificate is provided by the PKI module.
  For best results, you should run this command in Windows PowerShell 5.1.

   PowerShell
   $newSelfSignedCertificateSplat = @{
       DnsName = $Env:COMPUTERNAME
       CertStoreLocation = "Cert:\CurrentUser\My\"
       Type = 'CodeSigningCert'
   }
   $cert = New-SelfSignedCertificate @newSelfSignedCertificateSplat
   Export-Certificate -Cert $cert -FilePath C:\certs\signing.cer
   Import-Certificate -FilePath C:\certs\signing.cer -CertStoreLocation
   "Cert:\CurrentUser\Root\"
   $cert = Get-ChildItem Cert:\CurrentUser\My\ -CodeSigningCert

   dir C:\bin\PowerShell\pwsh.exe | Set-AuthenticodeSignature -Certificate $cert

4. Add the code signing certificate to the policy

  Use the following command to add the new code signing certificate to the policy.

   PowerShell
   Add-SignerRule -FilePath .\SystemCIPolicy.xml -CertificatePath
   C:\certs\signing.cer -User

<!-- p.804 -->

   5. Convert the XML policy file to a policy enforcement binary file

     Finally, you need to convert the XML file to a binary file used by App Control to apply a
     policy.

      PowerShell

      ConvertFrom-CIPolicy -XmlFilePath .\SystemCIPolicy.xml -BinaryFilePath
      .\SIPolicy.p7b

   6. Apply the App Control policy

     To apply the policy to your test machine, copy the SIPolicy.p7b file to the required
     system location, C:\Windows\System32\CodeIntegrity .

       ７ Note

       Some policies definition must be copied to a subfolder such as
        C:\Windows\System32\CodeIntegrity\CiPolicies . For more information, see App

       Control Admin Tips & Known Issues.

   7. Disable the App Control policy

     To disable the policy, rename the SIPolicy.p7b file. If you need to do more testing, you
     can change the name back to reenable the policy.

      PowerShell

      Rename-Item -Path .\SIPolicy.p7b -NewName .\SIPolicy.p7b.off

Test using App Control policy auditing
PowerShell 7.4 added a new feature to support App Control policies in Audit mode. In audit
mode, PowerShell runs the untrusted scripts in ConstrainedLanguage mode without errors, but
logs messages to the event log instead. The log messages describe what restrictions would
apply if the policy were in Enforce mode.

Viewing audit events
PowerShell logs audit events to the PowerShellCore/Analytic event log. The log isn't enabled
by default. To enable the log, open the Windows Event Viewer, right-click on the
PowerShellCore/Analytic log and select Enable Log.

<!-- p.805 -->

Alternatively, you can run the following command from an elevated PowerShell session.

 PowerShell

 wevtutil.exe sl PowerShellCore/Analytic /enabled:true /quiet

You can view the events in the Windows Event Viewer or use the Get-WinEvent cmdlet to
retrieve the events.

 PowerShell

 Get-WinEvent -LogName PowerShellCore/Analytic -Oldest |
     Where-Object Id -EQ 16387 | Format-List

 Output
 TimeCreated : 4/19/2023 10:11:07 AM
 ProviderName : PowerShellCore
 Id           : 16387
 Message      : App Control Audit.

       Title: Method or Property Invocation
       Message: Method or Property 'WriteLine' on type 'System.Console' invocation will
 not
           be allowed in ConstrainedLanguage mode.
           At C:\scripts\Test1.ps1:3 char:1
           + [System.Console]::WriteLine("pwnd!")
           + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       FullyQualifiedId: MethodOrPropertyInvocationNotAllowed

The event message includes the script position where the restriction would be applied. This
information helps you understand where you need to change your script so that it runs under
the App Control policy.

  ） Important

  After you review the audit events, you should disable the Analytic log. Analytic logs grow
  quickly and consume large amounts of disk space.

Viewing audit events in the PowerShell debugger
If you set the $DebugPreference variable to Break for an interactive PowerShell session,
PowerShell breaks into the command-line script debugger at the current location in the script
where the audit event occurred. The breakpoint allows you to debug your code and inspect the
current state of the script in real time.

<!-- p.806 -->

Last updated on 12/09/2025

<!-- p.807 -->

Preventing script injection attacks
PowerShell scripts, like other programming languages, can be vulnerable to injection attacks.
An injection attack occurs when a user provides input to a vulnerable function that includes
extra commands. The vulnerable function runs the extra commands, which can be a serious
security vulnerability. For example, a malicious user could abuse the vulnerable function to run
arbitrary code on a remote computer, possibly compromising that computer and gaining
access to other machines on the network.

Once you're aware of the issue, there are several ways to protect against injection attacks.

Example of vulnerable code
PowerShell code injection vulnerabilities involve user input that contains script code. The user
input is added to vulnerable script where PowerShell parses and runs it.

 PowerShell

 function Get-ProcessById
 {
     param ($ProcId)

       Invoke-Expression -Command "Get-Process -Id $ProcId"
 }

The Get-ProcessById function looks up a local process by its Id value. It takes a $ProcId
parameter argument of any type. The $ProcId is then converted to a string and inserted into
another script. Invoke-Expression cmdlet parses and runs the provided string. This function
works fine when a valid process Id integer is passed in.

 PowerShell
 Get-ProcessById $PID

     NPM(K)   PM(M)       WS(M)      CPU(s)       Id   SI ProcessName
     ------   -----       -----      ------       --   -- -----------
         97   50.09      132.72        1.20    12528    3 pwsh

However, the $ProcId parameter doesn't specify a type. It accepts any arbitrary string value
that can include other commands.

 PowerShell
 Get-ProcessById "$PID; Write-Host 'pwnd!'"

<!-- p.808 -->

In this example, the function correctly retrieved the process identified by $PID , but also ran the
injected script Write-Host 'pwnd!' .

 Output

  NPM(K)      PM(M)       WS(M)        CPU(s)      Id   SI ProcessName
  ------      -----       -----        ------      --   -- -----------
       92     45.66      122.52          1.06   21736    3 pwsh
 pwnd!

Ways to guard against injection attacks
The are several ways to guard against an injection attack.

Use typed input
You can specify a type for the $ProcId argument.

 PowerShell

 function Get-ProcessById
 {
     param ([int] $ProcId)

      Invoke-Expression -Command "Get-Process -Id $ProcId"
 }
 Get-ProcessById "$PID; Write-Host 'pwnd!'"

 Output

 Get-ProcessById:
 Line |
    7 | Get-ProcessById "$PID; Write-Host 'pwnd!'"
       |                  ~~~~~~~~~~~~~~~~~~~~~~~~~
       | Cannot process argument transformation on parameter 'ProcId'. Cannot convert
 value
 "8064; Write-Host 'pwnd!'" to type "System.Int32". Error: "The input string '8064;
 Write-Host 'pwnd!'
 was not in a correct format."

Here, the $ProcId input parameter is restricted to an integer type, so an error occurs when a
string is passed in that can't be converted to an integer.

Don't use Invoke-Expression

<!-- p.809 -->

Instead of using Invoke-Expression , directly call Get-Process , and let PowerShell's parameter
binder validate the input.

 PowerShell

 function Get-ProcessById
 {
     param ($ProcId)

      Get-Process -Id $ProcId
 }
 Get-ProcessById "$PID; Write-Host 'pwnd!'"

 Output

 Get-Process:
 Line |
    5 |       Get-Process -Id $ProcId
      |                       ~~~~~~~
      | Cannot bind parameter 'Id'. Cannot convert value "8064; Write-Host 'pwnd!'"
 to type
 "System.Int32". Error: "The input string '8064; Write-Host 'pwnd!' was not in a
 correct
 format."

As a best practice, you should avoid using Invoke-Expression , especially when handling user
input. Invoke-Expression is dangerous because it parses and runs whatever string content you
provide, making it vulnerable to injection attacks. It's better to rely on PowerShell parameter
binding.

Wrap strings in single quotes
However, there are times when using Invoke-Expression is unavoidable and you also need to
handle user string input. You can safely handle user input using single quotes around each
string input variable. The single quote ensures that PowerShell's parser treats the user input as
a single string literal.

 PowerShell

 function Get-ProcessById
 {
     param ($ProcId)

      Invoke-Expression -Command "Get-Process -Id '$ProcId'"
 }

 Get-ProcessById "$PID; Write-Host 'pwnd!'"

<!-- p.810 -->

 Output

 Get-Process: Cannot bind parameter 'Id'. Cannot convert value "8064; Write-Host " to
 type
 "System.Int32". Error: "The input string '8064; Write-Host' was not in a correct
 format."

However, this version of the function isn't safe from injection attacks. A malicious user can still
use single quotes in their input to inject code.

 PowerShell
 Get-ProcessById "$PID'; Write-Host 'pwnd!';'"

This example uses single quotes in the user input to force the function to run three separate
statements, one of which is arbitrary code injected by the user.

 Output
  NPM(K)      PM(M)       WS(M)       CPU(s)         Id   SI ProcessName
  ------      -----       -----       ------         --   -- -----------
       97     46.08      183.10         1.08       2524    3 pwsh
 pwnd!

Use the EscapeSingleQuotedStringContent() method

To protect against the user inserting their own single quote characters to exploit the function,
you must use the EscapeSingleQuotedStringContent() API. EscapeSingleQuotedStringContent()
is a public static method of the PowerShell
System.Management.Automation.Language.CodeGeneration class. This method makes the
user-provided input safe by escaping any single quotes included in the user input.

 PowerShell
 function Get-ProcessById
 {
     param ($ProcId)

      $ProcIdClean = [System.Management.Automation.Language.CodeGeneration]::
          EscapeSingleQuotedStringContent("$ProcId")
      Invoke-Expression -Command "Get-Process -Id '$ProcIdClean'"
 }
 Get-ProcessById "$PID'; Write-Host 'pwnd!';'"

 Output

<!-- p.811 -->

 Get-Process: Cannot bind parameter 'Id'. Cannot convert value "8064'; Write-Host
 'pwnd!';'" to type
 "System.Int32". Error: "The input string '8064'; Write-Host 'pwnd!';'' was not in a
 correct format."

For more information, see EscapeSingleQuotedStringContent().

Detecting vulnerable code with Injection Hunter
Injection Hunter is a module written by Lee Holmes that contains PowerShell Script Analyzer
rules for detecting code injection vulnerabilities. Use one of the following commands to install
the module from the PowerShell Gallery:

 PowerShell
 # Use PowerShellGet v2.x
 Install-Module InjectionHunter

 # Use PowerShellGet v3.x
 Install-PSResource InjectionHunter

You can use this module to automate security analysis during builds, continuous integration
processes, deployments, and other scenarios.

 PowerShell
 $RulePath = (Get-Module -List InjectionHunter).Path
 Invoke-ScriptAnalyzer -CustomRulePath $RulePath -Path .\Invoke-Dangerous.ps1

 Output

 RuleName                                 Severity      ScriptName Line    Message
 --------                                 --------      ---------- ----    -------
 InjectionRisk.InvokeExpression           Warning       Invoke-Dan 3       Possible script
 injection risk via the
                                                        gerous.ps1         Invoke-Expression
 cmdlet. Untrusted input can cause
                                                                           arbitrary
 PowerShell expressions to be run.
                                                                           Variables may be
 used directly for dynamic parameter
                                                                           arguments,
 splatting can be used for dynamic
                                                                           parameter names,
 and the invocation operator can be
                                                                           used for dynamic
 command names. If content escaping
                                                                           is truly needed,

<!-- p.812 -->

 PowerShell has several valid quote
                                                    characters, so
 [System.Management.Automation.Languag

 e.CodeGeneration]::Escape* should be used.

For more information, see PSScriptAnalyzer.

Related links
     Lee Holmes' blog post about Injection Hunter
     Injection Hunter

Last updated on 12/09/2025

<!-- p.813 -->

Just Enough Administration
Article • 04/01/2024

Just Enough Administration (JEA) is a security technology that enables delegated
administration for anything managed by PowerShell. With JEA, you can:

      Reduce the number of administrators on your machines using virtual accounts or
      group-managed service accounts to perform privileged actions on behalf of
      regular users.
      Limit what users can do by specifying which cmdlets, functions, and external
      commands they can run.
      Better understand what your users are doing with transcripts and logs that show
      you exactly which commands a user executed during their session.

Why is JEA important?

Highly privileged accounts used to administer your servers pose a serious security risk.
Should an attacker compromise one of these accounts, they could launch lateral
attacks    across your organization. Each compromised account gives an attacker access
to even more accounts and resources, and puts them one step closer to stealing
company secrets, launching a denial-of-service attack, and more.

It's not always easy to remove administrative privileges, either. Consider the common
scenario where the DNS role is installed on the same machine as your Active Directory
Domain Controller. Your DNS administrators require local administrator privileges to fix
issues with the DNS server. But to do so, you must make them members of the highly
privileged Domain Admins security group. This approach effectively gives DNS
Administrators control over your whole domain and access to all resources on that
machine.

JEA addresses this problem through the principle of Least Privilege. With JEA, you can
configure a management endpoint for DNS administrators that gives them access only
to the PowerShell commands they need to get their job done. This means you can
provide the appropriate access to repair a poisoned DNS cache or restart the DNS server
without unintentionally giving them rights to Active Directory, or to browse the file
system, or run potentially dangerous scripts. Better yet, when the JEA session is
configured to use temporary privileged virtual accounts, your DNS administrators can
connect to the server using non-admin credentials and still run commands that typically
require admin privileges. JEA enables you to remove users from widely privileged
local/domain administrator roles and carefully control what they can do on each
machine.

<!-- p.814 -->

Next steps
To learn more about the requirements to use JEA, see the Prerequisites article.

Samples and DSC resource
Sample JEA configurations and the JEA DSC resource can be found in the JEA GitHub
repository   .

<!-- p.815 -->

JEA Prerequisites
Article • 04/01/2024

Just Enough Administration is a feature included in PowerShell 5.0 and higher. This
article describes the prerequisites that must be satisfied to start using JEA.

Check which version of PowerShell is installed
To check which version of PowerShell is installed on your system, check the
$PSVersionTable variable in a Windows PowerShell prompt.

  PowerShell

  $PSVersionTable.PSVersion

  Output

  Major    Minor   Build   Revision
  -----    -----   -----   --------
  5        1       14393   1000

JEA is available with PowerShell 5.0 and higher. For full functionality, it's recommended
that you install the latest version of PowerShell available for your system. The following
table describes JEA's availability on Windows Server:

                                                                              ﾉ   Expand table

 Server Operating System                JEA Availability

 Windows Server 2016+                   Preinstalled

 Windows Server 2012 R2                 Full functionality with WMF 5.1

 Windows Server 2012                    Full functionality with WMF 5.1

 Windows Server 2008 R2                 Reduced functionality1 with WMF 5.1

You can also use JEA on your home or work computer:

                                                                              ﾉ   Expand table

<!-- p.816 -->

 Client Operating System             JEA Availability

 Windows 10 1607+                    Preinstalled

 Windows 10 1603, 1511               Preinstalled, with reduced functionality2

 Windows 10 1507                     Not available

 Windows 8, 8.1                      Full functionality with WMF 5.1

 Windows 7                           Reduced functionality1 with WMF 5.1

     1 JEA can't be configured to use group-managed service accounts on Windows

     Server 2008 R2 or Windows 7. Virtual accounts and other JEA features are
     supported.

     2 The following JEA features aren't supported on Windows 10 versions 1511 and

     1603:
        Running as a group-managed service account
        Conditional access rules in session configurations
        The user drive
        Granting access to local user accounts

     To get support for these features, update Windows to version 1607 (Anniversary
     Update) or higher.

Install Windows Management Framework
If you're running an older version of PowerShell, you may need to update your system
with the latest Windows Management Framework (WMF) update. For more information,
see the WMF documentation.

It's recommended that you test your workload's compatibility with WMF before
upgrading all of your servers.

Windows 10 users should install the latest feature updates to obtain the current version
of Windows PowerShell.

Enable PowerShell Remoting
PowerShell Remoting provides the foundation on which JEA is built. It's necessary to
ensure PowerShell Remoting is enabled and properly secured before you can use JEA.
For more information, see WinRM Security.

<!-- p.817 -->

PowerShell Remoting is enabled by default on Windows Server 2012 and higher. You can
enable PowerShell Remoting by running the following command in an elevated
PowerShell window.

  PowerShell

  Enable-PSRemoting

Enable PowerShell module and script block
logging (optional)
The following steps enable logging for all PowerShell actions on your system.
PowerShell Module Logging isn't required for JEA, however it's recommended you turn
on logging to ensure the commands users run are logged in a central location.

You can configure the PowerShell Module Logging policy using Group Policy.

   1. Open the Local Group Policy Editor on a workstation or a Group Policy Object in
     the Group Policy Management Console on an Active Directory Domain Controller
   2. Navigate to Computer Configuration\Administrative Templates\Windows
     Components\Windows PowerShell
   3. Double-click on Turn on Module Logging
   4. Click Enabled
   5. In the Options section, click on Show next to Module Names
   6. Type * in the pop-up window to log commands from all modules.
   7. Click OK to set the policy
   8. Double-click on Turn on PowerShell Script Block Logging
   9. Click Enabled
 10. Click OK to set the policy
 11. (On domain-joined machines only) Run gpupdate or wait for Group Policy to
     process the updated policy and apply the settings

You can also enable system-wide PowerShell transcription through Group Policy.

Next steps
     Create a role capability file
     Create a session configuration file

See also

<!-- p.818 -->

WinRM Security
PowerShell ♥ the Blue Team

<!-- p.819 -->

JEA Role Capabilities
When creating a JEA endpoint, you need to define one or more role capabilities that describe
what someone can do in a JEA session. A role capability is a PowerShell data file with the .psrc
extension that lists all the cmdlets, functions, providers, and external programs that are made
available to connecting users.

Determine which commands to allow
The first step in creating a role capability file is to consider what the users need access to. The
requirements gathering process can take a while, but it's important. Giving users access to too
few cmdlets and functions can prevent them from getting their job done. Allowing access to
too many cmdlets and functions can allow users to do more than you intended and weaken
your security stance.

How you go about this process depends on your organization and goals. The following tips can
help ensure you're on the right path.

   1. Identify the commands users are using to get their jobs done. This may involve surveying
     IT staff, checking automation scripts, or analyzing PowerShell session transcripts and logs.
   2. Update use of command-line tools to PowerShell equivalents, where possible, for the best
     auditing and JEA customization experience. External programs can't be constrained as
     granularly as native PowerShell cmdlets and functions in JEA.
   3. Restrict the scope of the cmdlets to only allow specific parameters or parameter values.
     This is especially important if users should manage only part of a system.
   4. Create custom functions to replace complex commands or commands that are difficult to
     constrain in JEA. A simple function that wraps a complex command or applies additional
     validation logic can offer additional control for admins and end-user simplicity.
   5. Test the scoped list of allowable commands with your users or automation services, and
     adjust as necessary.

Examples of potentially dangerous commands
Careful selection of commands is important to ensure the JEA endpoint doesn't allow the user
to elevate their permissions.

  ） Important

<!-- p.820 -->

  Essential information required for user successCommands in a JEA session are often run
  with elevated privileges.

The following list contains examples of commands that can be used maliciously if allowed in an
unconstrained state. This isn't an exhaustive list and should only be used as a cautionary
starting point.

     Risk: Granting the connecting user admin privileges to bypass JEA

     Example:

       PowerShell

       Add-LocalGroupMember -Member 'CONTOSO\jdoe' -Group 'Administrators'

     Related commands:
         Add-ADGroupMember

         Add-LocalGroupMember

         net.exe

         dsadd.exe

     Risk: Running arbitrary code, such as malware, exploits, or custom scripts to bypass
     protections

     Example:

       PowerShell

       Start-Process -FilePath '\\san\share\malware.exe'

     Related commands:
         Start-Process

         New-Service

         Invoke-Item

         Invoke-WmiMethod

         Invoke-CimMethod

         Invoke-Expression

         Invoke-Command

         New-ScheduledTask

         Register-ScheduledJob

<!-- p.821 -->

Create a role capability file
You can create a new PowerShell role capability file with the New-PSRoleCapabilityFile cmdlet.

  PowerShell

  New-PSRoleCapabilityFile -Path .\MyFirstJEARole.psrc

You should edit the created role capability file to allow only the commands required for the
role. The PowerShell help documentation contains several examples of how you can configure
the file.

Allowing PowerShell cmdlets and functions
To authorize users to run PowerShell cmdlets or functions, add the cmdlet or function name to
the VisibleCmdlets or VisibleFunctions fields. If you aren't sure whether a command is a
cmdlet or function, you can run Get-Command <name> and check the CommandType property in
the output.

  PowerShell

  VisibleCmdlets = @('Restart-Computer', 'Get-NetIPAddress')

Sometimes the scope of a specific cmdlet or function is too broad for your users' needs. A DNS
admin, for example, may only need access to restart the DNS service. In multi-tenant
environments, tenants have access to self-service management tools. Tenants should be limited
to managing their own resources. For these cases, you can restrict which parameters are
exposed from the cmdlet or function.

  PowerShell

  VisibleCmdlets = @{
      Name       = 'Restart-Computer'
      Parameters = @{ Name = 'Name' }
  }

In more advanced scenarios, you may also need to restrict the values a user may use with these
parameters. Role capabilities let you define a set of values or a regular expression pattern that
determine what input is allowed.

  PowerShell

<!-- p.822 -->

 VisibleCmdlets = @(
     @{
         Name       = 'Restart-Service'
         Parameters = @{ Name = 'Name'; ValidateSet = @('Dns', 'Spooler') }
     }
     @{
         Name       = 'Start-Website'
         Parameters = @{ Name = 'Name'; ValidatePattern = 'HR_*' }
     }
 )

  ７ Note

  The common PowerShell parameters are always allowed, even if you restrict the available
  parameters. You shouldn't explicitly list them in the Parameters field.

The list below describes the various ways you can customize a visible cmdlet or function. You
can mix and match any of the below in the VisibleCmdlets field.

     Use case: Allow the user to run My-Func without any restrictions on the parameters.

       PowerShell

       @{ Name = 'My-Func' }

     Use case: Allow the user to run My-Func from the module MyModule without any
     restrictions on the parameters.

       PowerShell

       @{ Name = 'MyModule\My-Func' }

     Use case: Allow the user to run any cmdlet or function with the verb My .

       PowerShell

       @{ Name = 'My-*' }

     Use case: Allow the user to run any cmdlet or function with the noun Func .

       PowerShell

       @{ Name = '*-Func' }

<!-- p.823 -->

     Use case: Allow the user to run My-Func with the Param1 and Param2 parameters. Any
     value can be supplied to the parameters.

       PowerShell

       @{ Name = 'My-Func'; Parameters = @{ Name = 'Param1'}, @{ Name = 'Param2' }}

     Use case: Allow the user to run My-Func with the Param1 parameter. Only Value1 and
     Value2 can be supplied to the parameter.

       PowerShell

       @{
            Name       = 'My-Func'
            Parameters = @{ Name = 'Param1'; ValidateSet = @('Value1', 'Value2') }
       }

     Use case: Allow the user to run My-Func with the Param1 parameter. Any value starting
     with contoso can be supplied to the parameter.

       PowerShell

       @{
            Name       = 'My-Func'
            Parameters = @{ Name = 'Param1'; ValidatePattern = 'contoso.*' }
       }

  ２ Warning

  For best security practices, it isn't recommended to use wildcards when defining visible
  cmdlets or functions. Instead, you should explicitly list each trusted command to ensure
  no other commands that share the same naming scheme are unintentionally authorized.

You can't apply both a ValidatePattern and ValidateSet to the same cmdlet or function.

If you do, the ValidatePattern overrides the ValidateSet.

For more information about ValidatePattern, check out this Hey, Scripting Guy! post    and the
PowerShell Regular Expressions reference content.

Allowing external commands and PowerShell scripts

<!-- p.824 -->

To allow users to run executables and PowerShell scripts ( .ps1 ) in a JEA session, you have to
add the full path to each program in the VisibleExternalCommands field.

 PowerShell

 VisibleExternalCommands = @(
     'C:\Windows\System32\whoami.exe'
     'C:\Program Files\Contoso\Scripts\UpdateITSoftware.ps1'
 )

Where possible, use PowerShell cmdlet or function equivalents for any external executables
you authorize since you have control over the parameters allowed with PowerShell cmdlets and
functions.

Many executables allow you to read the current state and then change it by providing different
parameters.

For example, consider the role of a file server admin that manages network shares hosted on a
system. One way of managing shares is to use net share . However, allowing net.exe is
dangerous because the user could use the command to gain admin privileges with the
command net group Administrators unprivilegedjeauser /add . A more secure option is to
allow the Get-SmbShare cmdlet, which achieves the same result but has a much more limited
scope.

When making external commands available to users in a JEA session, always specify the
complete path to the executable. This prevents the execution of similarly named and
potentially malicious programs located elsewhere on the system.

Allowing access to PowerShell providers
By default, no PowerShell providers are available in JEA sessions. This reduces the risk of
sensitive information and configuration settings being disclosed to the connecting user.

When necessary, you can allow access to the PowerShell providers using the VisibleProviders
command. For a full list of providers, run Get-PSProvider .

 PowerShell

 VisibleProviders = 'Registry'

For simple tasks that require access to the file system, registry, certificate store, or other
sensitive providers, consider writing a custom function that works with the provider on the

<!-- p.825 -->

user's behalf. The functions, cmdlets, and external programs available in a JEA session aren't
subject to the same constraints as JEA. They can access any provider by default. Also consider
using the user drive when users need to copy files to or from a JEA endpoint.

Creating custom functions
You can author custom functions in a role capability file to simplify complex tasks for your end
users. Custom functions are also useful when you require advanced validation logic for cmdlet
parameter values. You can write simple functions in the FunctionDefinitions field:

 PowerShell

 VisibleFunctions = 'Get-TopProcess'

 FunctionDefinitions = @{
     Name        = 'Get-TopProcess'
     ScriptBlock = {
         param($Count = 10)

           Get-Process |
               Sort-Object -Property CPU -Descending |
               Microsoft.PowerShell.Utility\Select-Object -First $Count
      }
 }

  ） Important

  Don't forget to add the name of your custom functions to the VisibleFunctions field so
  they can be run by the JEA users.

The body (script block) of custom functions runs in the default language mode for the system
and isn't subject to JEA's language constraints. This means that functions can access the file
system and registry, and run commands that weren't made visible in the role capability file.
Take care to avoid running arbitrary code when using parameters. Avoid piping user input
directly into cmdlets like Invoke-Expression .

In the above example, notice that the fully qualified module name (FQMN)
Microsoft.PowerShell.Utility\Select-Object was used instead of the shorthand Select-

Object . Functions defined in role capability files are still subject to the scope of JEA sessions,

which includes the proxy functions JEA creates to constrain existing commands.

<!-- p.826 -->

By default, Select-Object is a constrained cmdlet in all JEA sessions that doesn't allow the
selection of arbitrary properties on objects. To use the unconstrained Select-Object in
functions, you must explicitly request the full implementation using the FQMN. Any
constrained cmdlet in a JEA session has the same constraints when invoked from a function.
For more information, see about_Command_Precedence.

If you're writing several custom functions, it's more convenient to put them in a PowerShell
script module. You make those functions visible in the JEA session using the VisibleFunctions
field like you would with built-in and third-party modules.

For tab completion to work properly in JEA sessions you must include the built-in function
TabExpansion2 in the VisibleFunctions list.

Make the role capabilities available to a
configuration
Prior to PowerShell 6, for PowerShell to find a role capability file it must be stored in a
RoleCapabilities folder in a PowerShell module. The module can be stored in any folder

included in the $Env:PSModulePath environment variable, however you shouldn't place it in
$Env:SystemRoot\System32 or a folder where untrusted users could modify the files.

The following example creates a PowerShell script module called ContosoJEA in the
$Env:ProgramFiles path to host the role capabilities file.

 PowerShell

 # Create a folder for the module
 $modulePath = Join-Path $Env:ProgramFiles "WindowsPowerShell\Modules\ContosoJEA"
 New-Item -ItemType Directory -Path $modulePath

 # Create an empty script module and module manifest.
 # At least one file in the module folder must have the same name as the folder
 itself.
 $rootModulePath = Join-Path $modulePath "ContosoJEAFunctions.psm1"
 $moduleManifestPath = Join-Path $modulePath "ContosoJEA.psd1"
 New-Item -ItemType File -Path $RootModulePath
 New-ModuleManifest -Path $moduleManifestPath -RootModule "ContosoJEAFunctions.psm1"

 # Create the RoleCapabilities folder and copy in the PSRC file
 $rcFolder = Join-Path $modulePath "RoleCapabilities"
 New-Item -ItemType Directory $rcFolder
 Copy-Item -Path .\MyFirstJEARole.psrc -Destination $rcFolder

For more information about PowerShell modules, see Understanding a PowerShell Module.

<!-- p.827 -->

Starting in PowerShell 6, the RoleDefinitions property was added to the session configuration
file. This property lets you specify the location of a role configuration file for your role
definition. See the examples in New-PSSessionConfigurationFile.

Updating role capabilities
You can edit a role capability file to update the settings at any time. Any new JEA sessions
started after the role capability has been updated will reflect the revised capabilities.

This is why controlling access to the role capabilities folder is so important. Only highly trusted
administrators should be allowed to change role capability files. If an untrusted user can
change role capability files, they can easily give themselves access to cmdlets that allow them
to elevate their privileges.

For administrators looking to lock down access to the role capabilities, ensure Local System has
read-only access to the role capability files and containing modules.

How role capabilities are merged
Users are granted access to all matching role capabilities in the session configuration file when
they enter a JEA session. JEA tries to give the user the most permissive set of commands
allowed by any of the roles.

VisibleCmdlets and VisibleFunctions
The most complex merge logic affects cmdlets and functions, which can have their parameters
and parameter values limited in JEA.

The rules are as follows:

   1. If a cmdlet is only made visible in one role, it's visible to the user with any applicable
     parameter constraints.
   2. If a cmdlet is made visible in more than one role, and each role has the same constraints
     on the cmdlet, the cmdlet is visible to the user with those constraints.
   3. If a cmdlet is made visible in more than one role, and each role allows a different set of
     parameters, the cmdlet and all the parameters defined across every role are visible to the
     user. If one role doesn't have constraints on the parameters, all parameters are allowed.
   4. If one role defines a validate set or validate pattern for a cmdlet parameter, and the other
     role allows the parameter but doesn't constrain the parameter values, the validate set or
     pattern is ignored.

<!-- p.828 -->

  5. If a validate set is defined for the same cmdlet parameter in more than one role, all values
     from all validate sets are allowed.
  6. If a validate pattern is defined for the same cmdlet parameter in more than one role, any
     values that match any of the patterns are allowed.
  7. If a validate set is defined in one or more roles, and a validate pattern is defined in
     another role for the same cmdlet parameter, the validate set is ignored and rule (6)
     applies to the remaining validate patterns.

Below is an example of how roles are merged according to these rules:

 PowerShell

 # Role A Visible Cmdlets
 $roleA = @{
     VisibleCmdlets = @(
         'Get-Service'
           @{
              Name       = 'Restart-Service'
              Parameters = @{ Name = 'DisplayName'; ValidateSet = 'DNS Client' }
         }
     )
 }

 # Role B Visible Cmdlets
 $roleB = @{
     VisibleCmdlets = @(
         @{
             Name       = 'Get-Service';
             Parameters = @{ Name = 'DisplayName'; ValidatePattern = 'DNS.*' }
         }
         @{
             Name       = 'Restart-Service'
             Parameters = @{ Name = 'DisplayName'; ValidateSet = 'DNS Server' }
         }
     )
 }

 # Resulting permissions for a user who belongs to both role A and B
 # - The constraint in role B for the DisplayName parameter on Get-Service
 #   is ignored because of rule #4
 # - The ValidateSets for Restart-Service are merged because both roles use
 #   ValidateSet on the same parameter per rule #5
 $mergedAandB = @{
     VisibleCmdlets = @(
         'Get-Service'
         @{
             Name = 'Restart-Service';
             Parameters = @{
                 Name = 'DisplayName'
                 ValidateSet = 'DNS Client', 'DNS Server'
             }

<!-- p.829 -->

            }
       )
  }

VisibleExternalCommands, VisibleAliases, VisibleProviders,
ScriptsToProcess
All other fields in the role capability file are added to a cumulative set of allowable external
commands, aliases, providers, and startup scripts. Any command, alias, provider, or script
available in one role capability is available to the JEA user.

Be careful to ensure that the combined set of providers from one role capability and
cmdlets/functions/commands from another don't allow users unintentional access to system
resources. For example, if one role allows the Remove-Item cmdlet and another allows the
FileSystem provider, you are at risk of a JEA user deleting arbitrary files on your computer.

Additional information about identifying users' effective permissions can be found in the
auditing JEA article.

Next steps
Create a session configuration file

 Last updated on 03/24/2025

<!-- p.830 -->

JEA Session Configurations
A JEA endpoint is registered on a system by creating and registering a PowerShell session
configuration file. Session configurations define who can use the JEA endpoint and which roles
they have access to. They also define global settings that apply to all users of the JEA session.

Create a session configuration file
To register a JEA endpoint, you must specify how that endpoint is configured. There are many
options to consider. The most important options are:

     Who has access to the JEA endpoint
     Which roles they may be assigned
     Which identity JEA uses under the covers
     The name of the JEA endpoint

These options are defined in a PowerShell data file with a .pssc extension known as a
PowerShell session configuration file. The session configuration file can be edited using any
text editor.

Run the following command to create a blank template configuration file.

  PowerShell

  New-PSSessionConfigurationFile -SessionType RestrictedRemoteServer -Path
  .\MyJEAEndpoint.pssc

   Tip

  Only the most common configuration options are included in the template file by default.
  Use the -Full switch to include all applicable settings in the generated PSSC.

The -SessionType RestrictedRemoteServer field indicates that the session configuration is used
by JEA for secure management. Sessions of this type operate in NoLanguage mode and only
have access to the following default commands (and aliases):

      Clear-Host ( cls , clear )

      Exit-PSSession ( exsn , exit )

<!-- p.831 -->

      Get-Command ( gcm )

      Get-FormatData

      Get-Help

      Measure-Object ( measure )

      Out-Default

      Select-Object ( select )

No PowerShell providers are available, nor are any external programs (executables or scripts).

For more information about language modes, see about_Language_Modes.

Choose the JEA identity
Behind the scenes, JEA needs an identity (account) to use when running a connected user's
commands. You define which identity JEA uses in the session configuration file.

Local Virtual Account

Local virtual accounts are useful when all roles defined for the JEA endpoint are used to
manage the local machine and a local administrator account is sufficient to run the commands
successfully. Virtual accounts are temporary accounts that are unique to a specific user and
only last for the duration of their PowerShell session. On a member server or workstation,
virtual accounts belong to the local computer's Administrators group. On an Active Directory
Domain Controller, virtual accounts belong to the domain's Domain Admins group.

 PowerShell

 # Setting the session to use a virtual account
 RunAsVirtualAccount = $true

If the roles defined by the session configuration don't require full administrative privilege, you
can specify the security groups to which the virtual account will belong. On a member server or
workstation, the specified security groups must be local groups, not groups from a domain.

When one or more security groups are specified, the virtual account isn't assigned to the local
or domain administrators group.

 PowerShell

 # Setting the session to use a virtual account that only belongs to the
 NetworkOperator and NetworkAuditor local groups

<!-- p.832 -->

 RunAsVirtualAccount = $true
 RunAsVirtualAccountGroups = 'NetworkOperator', 'NetworkAuditor'

  ７ Note

  Virtual accounts are temporarily granted the Logon as a service right in the local server
  security policy. If one of the VirtualAccountGroups specified has already been granted this
  right in the policy, the individual virtual account will no longer be added and removed
  from the policy. This can be useful in scenarios such as domain controllers where revisions
  to the domain controller security policy are closely audited. This is only available in
  Windows Server 2016 with the November 2018 or later rollup and Windows Server 2019
  with the January 2019 or later rollup.

Group-managed service account

A group-managed service account (GMSA) is the appropriate identity to use when JEA users
need to access network resources such as file shares and web services. GMSAs give you a
domain identity that's used to authenticate with resources on any machine within the domain.
The rights that a GMSA provides are determined by the resources you're accessing. You don't
have admin rights on any machines or services unless the machine or service administrator has
explicitly granted those rights to the GMSA.

 PowerShell

 # Configure JEA sessions to use the GMSA in the local computer's domain
 # with the sAMAccountName of 'MyJEAGMSA'
 GroupManagedServiceAccount = 'Domain\MyJEAGMSA'

GMSAs should only be used when necessary:

     It's difficult to trace back actions to a user when using a GMSA. Every user shares the
     same run-as identity. You must review PowerShell session transcripts and logs to correlate
     individual users with their actions.

     The GMSA may have access to many network resources that the connecting user doesn't
     need access to. Always try to limit effective permissions in a JEA session to follow the
     principle of least privilege.

  ７ Note

<!-- p.833 -->

  Group managed service accounts are only available on domain-joined machines using
  PowerShell 5.1 or newer.

For more information about securing a JEA session, see the security considerations article.

Session transcripts
It's recommended that you configure a JEA endpoint to automatically record transcripts of
users' sessions. PowerShell session transcripts contain information about the connecting user,
the run as identity assigned to them, and the commands run by the user. They can be useful to
an auditing team who needs to understand who made a specific change to a system.

To configure automatic transcription in the session configuration file, provide a path to a folder
where the transcripts should be stored.

 PowerShell

 TranscriptDirectory = 'C:\ProgramData\JEAConfiguration\Transcripts'

Transcripts are written to the folder by the Local System account, which requires read and write
access to the directory. Standard users should have no access to the folder. Limit the number
of security administrators that have access to audit the transcripts.

User drive
If your connecting users need to copy files to or from the JEA endpoint, you can enable the
user drive in the session configuration file. The user drive is a PSDrive that's mapped to a
unique folder for each connecting user. This folder allows users to copy files to or from the
system without giving them access to the full file system or exposing the FileSystem provider.
The user drive contents are persistent across sessions to accommodate situations where
network connectivity may be interrupted.

 PowerShell

 MountUserDrive = $true

By default, the user drive allows you to store a maximum of 50MB of data per user. You can
limit the amount of data a user can consume with the UserDriveMaximumSize field.

 PowerShell

<!-- p.834 -->

 # Enables the user drive with a per-user limit of 500MB (524288000 bytes)
 MountUserDrive = $true
 UserDriveMaximumSize = 524288000

If you don't want data in the user drive to be persistent, you can configure a scheduled task on
the system to automatically clean up the folder every night.

  ７ Note

  The user drive is only available in PowerShell 5.1 or newer.

For more information about PSDrives, see Managing PowerShell drives.

Role definitions
Role definitions in a session configuration file define the mapping of users to roles. Every user
or group included in this field is granted permission to the JEA endpoint when it's registered.
Each user or group can be included as a key in the hashtable only once, but can be assigned
multiple roles. The name of the role capability should be the name of the role capability file,
without the .psrc extension.

 PowerShell

 RoleDefinitions = @{
     'CONTOSO\JEA_DNS_ADMINS'    = @{ RoleCapabilities = 'DnsAdmin', 'DnsOperator',
 'DnsAuditor' }
     'CONTOSO\JEA_DNS_OPERATORS' = @{ RoleCapabilities = 'DnsOperator', 'DnsAuditor'
 }
     'CONTOSO\JEA_DNS_AUDITORS' = @{ RoleCapabilities = 'DnsAuditor' }
 }

If a user belongs to more than one group in the role definition, they get access to the roles of
each. When two roles grant access to the same cmdlets, the most permissive parameter set is
granted to the user.

When specifying local users or groups in the role definitions field, be sure to use the computer
name, not localhost or wildcards. You can check the computer name by inspecting the
$Env:COMPUTERNAME variable.

 PowerShell

<!-- p.835 -->

 RoleDefinitions = @{
     'MyComputerName\MyLocalGroup' = @{ RoleCapabilities = 'DnsAuditor' }
 }

Role capability search order
As shown in the example above, role capabilities are referenced by the base name of the role
capability file. The base name of a file is the filename without the extension. If multiple role
capabilities are available on the system with the same name, PowerShell uses its implicit search
order to select the effective role capability file. JEA does not give access to all role capability
files with the same name.

JEA uses the $Env:PSModulePath environment variable to determine which paths to scan for
role capability files. Within each of those paths, JEA looks for valid PowerShell modules that
contain a "RoleCapabilities" subfolder. As with importing modules, JEA prefers role capabilities
that are shipped with Windows to custom role capabilities with the same name.

For all other naming conflicts, precedence is determined by the order in which Windows
enumerates the files in the directory. The order isn't guaranteed to be alphabetical. The first
role capability file found that matches the specified name is used for the connecting user. Since
the role capability search order isn't deterministic, it's strongly recommended that role
capabilities have unique filenames.

Conditional access rules
All users and groups included in the RoleDefinitions field are automatically granted access to
JEA endpoints. Conditional access rules allow you to refine this access and require users to
belong to additional security groups that don't impact the roles to which they're assigned. This
is useful when you want to integrate a just-in-time privileged access management solution,
smartcard authentication, or other multifactor authentication solution with JEA.

Conditional access rules are defined in the RequiredGroups field in a session configuration file.
There, you can provide a hashtable (optionally nested) that uses 'And' and 'Or' keys to
construct your rules. Here are some examples of how to use this field:

 PowerShell

 # Example 1: Connecting users must belong to a security group called "elevated-jea"
 RequiredGroups = @{ And = 'elevated-jea' }

 # Example 2: Connecting users must have signed on with 2 factor authentication or a

<!-- p.836 -->

  smart card
  # The 2 factor authentication group name is "2FA-logon" and the smart card group
  # name is "smartcard-logon"
  RequiredGroups = @{ Or = '2FA-logon', 'smartcard-logon' }

  # Example 3: Connecting users must elevate into "elevated-jea" with their JIT
  system and
  # have logged on with 2FA or a smart card
  RequiredGroups = @{ And = 'elevated-jea', @{ Or = '2FA-logon', 'smartcard-logon' }}

  ７ Note

  Conditional access rules are only available in PowerShell 5.1 or newer.

Other properties
Session configuration files can also do everything a role capability file can do, just without the
ability to give connecting users access to different commands. If you want to allow all users
access to specific cmdlets, functions, or providers, you can do so right in the session
configuration file. For a full list of supported properties in the session configuration file, run
Get-Help New-PSSessionConfigurationFile -Full .

Testing a session configuration file
You can test a session configuration using the Test-PSSessionConfigurationFile cmdlet. It's
recommended that you test your session configuration file if you've manually edited the .pssc
file. Testing ensures the syntax is correct. If a session configuration file fails this test, it can't be
registered on the system.

Sample session configuration file
The following example shows how to create and validate a session configuration for JEA. The
role definitions are created and stored in the $roles variable for convenience and readability. it
isn't a requirement to do so.

  PowerShell

  $roles = @{
      'CONTOSO\JEA_DNS_ADMINS'    = @{ RoleCapabilities = 'DnsAdmin', 'DnsOperator',
  'DnsAuditor' }
      'CONTOSO\JEA_DNS_OPERATORS' = @{ RoleCapabilities = 'DnsOperator', 'DnsAuditor'
  }
      'CONTOSO\JEA_DNS_AUDITORS' = @{ RoleCapabilities = 'DnsAuditor' }

<!-- p.837 -->

  }

  $parameters = @{
      SessionType = 'RestrictedRemoteServer'
      Path = '.\JEAConfig.pssc'
      RunAsVirtualAccount = $true
      TranscriptDirectory = 'C:\ProgramData\JEAConfiguration\Transcripts'
      RoleDefinitions = $roles
      RequiredGroups = @{ Or = '2FA-logon', 'smartcard-logon' }
  }
  New-PSSessionConfigurationFile @parameters
  Test-PSSessionConfigurationFile -Path .\JEAConfig.pssc # should yield True

Updating session configuration files
To change the properties of a JEA session configuration, including the mapping of users to
roles, you must unregister. Then, re-register the JEA session configuration using an updated
session configuration file.

Next steps
      Register a JEA configuration
      Author JEA roles

 Last updated on 03/24/2025

<!-- p.838 -->

Registering JEA Configurations
Article • 04/01/2024

Once you have your role capabilities and session configuration file created, the last step
is to register the JEA endpoint. Registering the JEA endpoint with the system makes the
endpoint available for use by users and automation engines.

Single machine configuration
For small environments, you can deploy JEA by registering the session configuration file
using the Register-PSSessionConfiguration cmdlet.

Before you begin, ensure that the following prerequisites have been met:

      One or more roles has been created and placed in the RoleCapabilities folder of a
      PowerShell module.
      A session configuration file has been created and tested.
      The user registering the JEA configuration has administrator rights on the system.
      You've selected a name for your JEA endpoint.

The name of the JEA endpoint is required when users connect to the system using JEA.
The Get-PSSessionConfiguration cmdlet lists the names of the endpoints on a system.
Endpoints that start with microsoft are typically shipped with Windows. The
microsoft.powershell endpoint is the default endpoint used when connecting to a

remote PowerShell endpoint.

  PowerShell

  Get-PSSessionConfiguration | Select-Object Name

  Output

  Name
  ----
  microsoft.powershell
  microsoft.powershell.workflow
  microsoft.powershell32

Run the following command to register the endpoint.

  PowerShell

<!-- p.839 -->

  Register-PSSessionConfiguration -Path .\MyJEAConfig.pssc -Name
  'JEAMaintenance' -Force

  ２ Warning

  The previous command restarts the WinRM service on the system. This terminates
  all PowerShell remoting sessions and any ongoing DSC configurations. We
  recommended you take production machines offline before running the command
  to avoid disrupting business operations.

After registration, you're ready to use JEA. You may delete the session configuration file
at any time. The configuration file isn't used after registration of the endpoint.

Multi-machine configuration with DSC
When deploying JEA on multiple machines, the simplest deployment model uses the JEA
Desired State Configuration (DSC) resource to quickly and consistently deploy JEA on
each machine.

To deploy JEA with DSC, ensure the following prerequisites are met:

     One or more role capabilities have been authored and added to a PowerShell
     module.
     The PowerShell module containing the roles is stored on a (read-only) file share
     accessible by each machine.
     Settings for the session configuration have been determined. You don't need to
     create a session configuration file when using the JEA DSC resource.
     You have credentials that allow administrative actions on each machine or access
     to the DSC pull server used to manage the machines.
     You've downloaded the JEA DSC resource        .

Create a DSC configuration for your JEA endpoint on a target machine or pull server. In
this configuration, the JustEnoughAdministration DSC resource defines the session
configuration file and the File resource copies the role capabilities from the file share.

The following properties are configurable using the DSC resource:

     Role Definitions
     Virtual account groups
     Group-managed service account name
     Transcript directory

<!-- p.840 -->

     User drive
     Conditional access rules
     Startup scripts for the JEA session

The syntax for each of these properties in a DSC configuration is consistent with the
PowerShell session configuration file.

Below is a sample DSC configuration for a general server maintenance module. It
assumes that a valid PowerShell module containing role capabilities is located on the
\\myfileshare\JEA file share.

  PowerShell

  Configuration JEAMaintenance
  {
      Import-DscResource -Module JustEnoughAdministration,
  PSDesiredStateConfiguration

      File MaintenanceModule
      {
          SourcePath = "\\myfileshare\JEA\ContosoMaintenance"
          DestinationPath = "C:\Program
  Files\WindowsPowerShell\Modules\ContosoMaintenance"
          Checksum = "SHA-256"
          Ensure = "Present"
          Type = "Directory"
          Recurse = $true
      }

      JeaEndpoint JEAMaintenanceEndpoint
      {
          EndpointName = "JEAMaintenance"
          RoleDefinitions = "@{ 'CONTOSO\JEAMaintenanceAuditors' = @{
  RoleCapabilities = 'GeneralServerMaintenance-Audit' };
  'CONTOSO\JEAMaintenanceAdmins' = @{ RoleCapabilities =
  'GeneralServerMaintenance-Audit', 'GeneralServerMaintenance-Admin' } }"
          TranscriptDirectory = 'C:\ProgramData\JEAConfiguration\Transcripts'
          DependsOn = '[File]MaintenanceModule'
      }
  }

Next, the configuration is applied on a system by directly invoking the Local
Configuration Manager or updating the pull server configuration.

The DSC resource also allows you to replace the default Microsoft.PowerShell endpoint.
When replaced, the resource automatically registers a backup endpoint named
Microsoft.PowerShell.Restricted. The backup endpoint has the default WinRM ACL that
allows Remote Management Users and local Administrators group members to access it.
