---
title: "How to use this documentation — pages 841-880"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0841-0880
family: powershell
documentKind: "doc"
abstract: "Unregistering JEA configurations The Unregister-PSSessionConfiguration cmdlet removes a JEA endpoint. Unregistering a JEA endpoint prevents new users from creating new JEA sessions on the system. It also allows you to update a JEA configuration by re-registering an updated sessi"
---

# How to use this documentation — pages 841-880

<!-- p.841 -->

Unregistering JEA configurations
The Unregister-PSSessionConfiguration cmdlet removes a JEA endpoint. Unregistering a
JEA endpoint prevents new users from creating new JEA sessions on the system. It also
allows you to update a JEA configuration by re-registering an updated session
configuration file using the same endpoint name.

  PowerShell

  # Unregister the JEA endpoint called "ContosoMaintenance"
  Unregister-PSSessionConfiguration -Name 'ContosoMaintenance' -Force

  ２ Warning

  Unregistering a JEA endpoint causes the WinRM service to restart. This interrupts
  most remote management operations in progress, including other PowerShell
  sessions, WMI invocations, and some management tools. Only unregister
  PowerShell endpoints during planned maintenance windows.

Next steps
Test the JEA endpoint

<!-- p.842 -->

Using JEA
Article • 04/01/2024

This article describes the various ways you can connect to and use a JEA endpoint.

Using JEA interactively
If you're testing your JEA configuration or have simple tasks for users, you can use JEA
the same way you would a regular PowerShell remoting session. For complex remoting
tasks, it's recommended to use implicit remoting. Implicit remoting allows users to
operate with the data objects locally.

To use JEA interactively, you need:

      The name of the computer you're connecting to (can be the local machine)
      The name of the JEA endpoint registered on that computer
      Credentials that have access to the JEA endpoint on that computer

Given that information, you can start a JEA session using the New-PSSession or Enter-
PSSession cmdlets.

  PowerShell

  $sessionParams = @{
      ComputerName      = 'localhost'
      ConfigurationName = 'JEAMaintenance'
      Credential        = Get-Credential
  }
  Enter-PSSession @sessionParams

If the current user account has access to the JEA endpoint, you can omit the Credential
parameter.

When the PowerShell prompt changes to [localhost]: PS> you know that you're now
interacting with the remote JEA session. You can run Get-Command to check which
commands are available. Consult with your administrator to learn if there are any
restrictions on the available parameters or allowed parameter values.

Remember, JEA sessions operate in NoLanguage mode. Some of the ways you typically
use PowerShell may not be available. For instance, you can't use variables to store data
or inspect the properties on objects returned from cmdlets. The following example
shows two approaches to get the same commands to work in NoLanguage mode.

<!-- p.843 -->

  PowerShell

  # Using variables is prohibited in NoLanguage mode. The following will not
  work:
  # $vm = Get-VM -Name 'SQL01'
  # Start-VM -VM $vm

  # You can use pipes to pass data through to commands that accept input from
  the pipeline
  Get-VM -Name 'SQL01' | Start-VM

  # You can also wrap subcommands in parentheses and enter them inline as
  arguments
  Start-VM -VM (Get-VM -Name 'SQL01')

  # You can also use parameter sets that don't require extra data to be passed
  in
  Start-VM -VMName 'SQL01'

For more complex command invocations that make this approach difficult, consider
using implicit remoting or creating custom functions that wrap the functionality you
require. For more information on NoLanguageMode , see about_Language_Modes.

Using JEA with implicit remoting
PowerShell has an implicit remoting model that lets you import proxy cmdlets from a
remote machine and interact with them as if they were local commands. Implicit
remoting is explained in this Hey, Scripting Guy! blog post . Implicit remoting is useful
when working with JEA because it allows you to work with JEA cmdlets in a full language
mode. You can use tab completion, variables, manipulate objects, and even use local
scripts to automate tasks against a JEA endpoint. Anytime you invoke a proxy command,
the data is sent to the JEA endpoint on the remote machine and executed there.

Implicit remoting works by importing cmdlets from an existing PowerShell session. You
can optionally choose to prefix the nouns of each proxy cmdlet with a string of your
choosing. The prefix allows you to distinguish the commands that are for the remote
system. A temporary script module containing all the proxy commands is created and
imported for the duration of your local PowerShell session.

  PowerShell

  # Create a new PSSession to your JEA endpoint
  $jeaSession = New-PSSession -ComputerName 'SERVER01' -ConfigurationName
  'JEAMaintenance'

  # Import the entire PSSession and prefix each imported cmdlet with "JEA"
  Import-PSSession -Session $jeaSession -Prefix 'JEA'

<!-- p.844 -->

  # Invoke "Get-Command" on the remote JEA endpoint using the proxy cmdlet
  Get-JEACommand

  ） Important

  Some systems may not be able to import an entire JEA session due to constraints in
  the default JEA cmdlets. To get around this, only import the commands you need
  from the JEA session by explicitly providing their names to the -CommandName
  parameter. A future update will address the issue with importing entire JEA sessions
  on affected systems.

If you're unable to import a JEA session because of JEA constraints on the default
parameters, follow the steps below to filter out the default commands from the
imported set. You can continue use commands like Select-Object , but you'll just use
the local version installed on your computer instead of the one imported from the
remote JEA session.

  PowerShell

  # Create a new PSSession to your JEA endpoint
  $jeaSession = New-PSSession -ComputerName 'SERVER01' -ConfigurationName
  'JEAMaintenance'

  # Get a list of all the commands on the JEA endpoint
  $commands = Invoke-Command -Session $jeaSession -ScriptBlock { Get-Command }

  # Filter out the default cmdlets
  $jeaDefaultCmdlets = @(
      'Clear-Host'
      'Exit-PSSession'
      'Get-Command'
      'Get-FormatData'
      'Get-Help'
      'Measure-Object'
      'Out-Default'
      'Select-Object'
  )
  $filteredCommands = $commands.Name | Where-Object { $jeaDefaultCmdlets -
  notcontains $_ }

  # Import only commands explicitly added in role capabilities and prefix each
  # imported cmdlet with "JEA"
  Import-PSSession -Session $jeaSession -Prefix 'JEA' -CommandName
  $filteredCommands

<!-- p.845 -->

You can also persist the proxied cmdlets from implicit remoting using Export-PSSession.
For more information about implicit remoting, see the documentation for Import-
PSSession and Import-Module.

Using JEA programmatically
JEA can also be used in automation systems and in user applications, such as in-house
helpdesk apps and websites. The approach is the same as that for building apps that
talk to unconstrained PowerShell endpoints. Ensure the program is designed to work
with limitation imposed by JEA.

For simple, one-off tasks, you can use Invoke-Command to run commands in a JEA
session.

  PowerShell

  Invoke-Command -ComputerName 'SERVER01' -ConfigurationName 'JEAMaintenance'
  -ScriptBlock {
      Get-Process
      Get-Service
  }

To check which commands are available for use when you connect to a JEA session, run
Get-Command and iterate through the results to check for the allowed parameters.

  PowerShell

  $commandParameters = @{
      ComputerName      = 'SERVER01'
      ConfigurationName = 'JEAMaintenance'
      ScriptBlock       = { Get-Command }
  }
  Invoke-Command @commandParameters |
      Where-Object { $_.CommandType -in @('Function', 'Cmdlet') } |
      Format-Table Name, Parameters

If you're building a C# app, you can create a PowerShell runspace that connects to a JEA
session by specifying the configuration name in a WSManConnectionInfo object.

  C#

  // using System.Management.Automation;
  var computerName = "SERVER01";
  var configName   = "JEAMaintenance";
  // See
  https://learn.microsoft.com/dotnet/api/system.management.automation.pscreden

<!-- p.846 -->

  tial
  var creds          = // create a PSCredential object here

  WSManConnectionInfo connectionInfo = new WSManConnectionInfo(
      false,                 // Use SSL
      computerName,          // Computer name
      5985,                  // WSMan Port
      "/wsman",              // WSMan Path
                             // Connection URI with config name
      string.Format(
          CultureInfo.InvariantCulture,
          "http://schemas.microsoft.com/powershell/{0}",
          configName
      ),
      creds                  // Credentials
  );

  // Now, use the connection info to create a runspace where you can run the
  commands
  using (Runspace runspace = RunspaceFactory.CreateRunspace(connectionInfo))
  {
      // Open the runspace
      runspace.Open();

      using (PowerShell ps = PowerShell.Create())
      {
          // Set the PowerShell object to use the JEA runspace
          ps.Runspace = runspace;

           // Now you can add and invoke commands
           ps.AddCommand("Get-Command");
           foreach (var result in ps.Invoke())
           {
               Console.WriteLine(result);
           }
      }

      // Close the runspace
      runspace.Close();
  }

Using JEA with PowerShell Direct
Hyper-V in Windows 10 and Windows Server 2016 offers PowerShell Direct, a feature
that allows Hyper-V administrators to manage virtual machines with PowerShell
regardless of the network configuration or remote management settings on the virtual
machine.

You can use PowerShell Direct with JEA to give a Hyper-V administrator limited access to
your VM. This can be useful if you lose network connectivity to your VM and need a

<!-- p.847 -->

datacenter admin to fix the network settings.

No additional configuration is required to use JEA over PowerShell Direct. However, the
guest operating system running inside the virtual machine must be Windows 10,
Windows Server 2016, or higher. The Hyper-V admin can connect to the JEA endpoint
by using the -VMName or -VMId parameters on PSRemoting cmdlets:

  PowerShell

  $sharedParams = @{
      ConfigurationName = 'NICMaintenance'
      Credential        = Get-Credential -UserName 'localhost\JEAformyHoster'
  }
  # Entering a JEA session using PowerShell Direct when the VM name is unique
  Enter-PSSession -VMName 'SQL01' @sharedParams

  # Entering a JEA session using PowerShell Direct using VM ids
  $vm = Get-VM -VMName 'MyVM' | Select-Object -First 1
  Enter-PSSession -VMId $vm.VMId @sharedParams

It's recommended you create a dedicated user account with the minimum rights needed
to manage the system for use by a Hyper-V administrator. Remember, even an
unprivileged user can sign into a Windows machine by default, including using
unconstrained PowerShell. That allows them to browse the file system and learn more
about your OS environment. To lock down a Hyper-V administrator and limit them to
only access a VM using PowerShell Direct with JEA, you must deny local logon rights to
the Hyper-V admin's JEA account.

<!-- p.848 -->

JEA Security Considerations
JEA helps you improve your security posture by reducing the number of permanent
administrators on your machines. JEA uses a PowerShell session configuration to create a new
entry point for users to manage the system. Users who need elevated, but not unlimited, access
to the machine to do administrative tasks can be granted access to the JEA endpoint. Since JEA
allows these users to run administrative commands without having full administrator access, you
can then remove those users from highly privileged security groups.

Run-As account
Each JEA endpoint has a designated run-as account under which the connecting user's actions
are executed. This account is configurable in the session configuration file, and the account you
choose has a significant bearing on the security of your endpoint.

Virtual accounts are the recommended way of configuring the run-as account. Virtual accounts
are one-time, temporary local accounts that are created for the connecting user to use during the
duration of their JEA session. As soon as their session is terminated, the virtual account is
destroyed and can't be used anymore. The connecting user doesn't know the credentials for the
virtual account. The virtual account can't be used to access the system via other means like
Remote Desktop or an unconstrained PowerShell endpoint.

By default, virtual accounts are members of the local Administrators group on the machine. This
membership gives them full rights to manage anything on the system, but no rights to manage
resources on the network. When the user connects to other machines from the JEA session, the
user context is that of the local computer account, not the virtual account.

Domain controllers are a special case since there isn't a local Administrators group. Instead,
virtual accounts belong to Domain Admins and can manage the directory services on the domain
controller. The domain identity is still restricted for use on the domain controller where the JEA
session was instantiated. Any network access appears to come from the domain controller
computer object instead.

In both cases, you may assign the virtual account to specific security groups, especially when the
task can be done without local or domain administrator privileges. If you already have a security
group defined for your administrators, grant the virtual account membership to that group.
Group membership for virtual accounts is limited to local security groups on workstation and

<!-- p.849 -->

member servers. On domain controllers, virtual accounts must be members of domain security
groups. Once the virtual account has been added to one or more security groups, it no longer
belongs to the default groups (local or domain administrators).

The following table summarizes the possible configuration options and resulting permissions for
virtual accounts:

                                                                                     ﾉ   Expand table

 Computer type        Virtual account group    Local user context                    Network user
                      configuration                                                  context

 Domain controller    Default                  Domain user, member of                Computer
                                               <DOMAIN>\Domain Admins                account

 Domain controller    Domain groups A and B    Domain user, member of <DOMAIN>\A ,   Computer
                                               <DOMAIN>\B                            account

 Member server or     Default                  Local user, member of                 Computer
 workstation                                   BUILTIN\Administrators                account

 Member server or     Local groups C and D     Local user, member of <COMPUTER>\C    Computer
 workstation                                   and <COMPUTER>\D                      account

When you look at Security audit and Application event logs, you see that each JEA user session
has a unique virtual account. This unique account helps you track user actions in a JEA endpoint
back to the original user who ran the command. Virtual account names follow the format WinRM
Virtual Users\WinRM_VA_<ACCOUNTNUMBER>_<DOMAIN>_<sAMAccountName> For example, if user Alice in

domain Contoso restarts a service in a JEA endpoint, the username associated with any service
control manager events would be WinRM Virtual Users\WinRM_VA_1_contoso_alice .

Group-managed service accounts (gMSAs) are useful when a member server needs to have
access to network resources in the JEA session. For example, when a JEA endpoint is used to
control access to a REST API service hosted on a different machine. It's easy to write functions to
invoke the REST APIs, but you need a network identity to authenticate with the API. Using a
group-managed service account makes the second hop possible while maintaining control over
which computers can use the account. The security group (local or domain) memberships of the
gMSA defined the effective permissions for the gMSA account.

When a JEA endpoint is configured to use a gMSA, the actions of all JEA users appear to come
from the same gMSA. The only way to trace actions back to a specific user is to identify the set of
commands run in a PowerShell session transcript.

<!-- p.850 -->

Pass-through credentials are used when you don't specify a run-as account. PowerShell uses the
connecting user's credential to run commands on the remote server. To use pass-through
credentials, you must grant the connecting user direct access to privileged management groups.
This configuration is NOT recommended for JEA. If the connecting user already has administrator
privileges, they can bypass JEA and manage the system using other access methods.

Standard run-as accounts allow you to specify any user account under which the entire
PowerShell session runs. Session configurations using fixed run-as accounts (with the -
RunAsCredential parameter) aren't JEA-aware. Role definitions no longer function as expected.

Every user authorized to access the endpoint is assigned the same role.

You shouldn't use a RunAsCredential on a JEA endpoint because it's difficult to trace actions back
to specific users and lacks support for mapping users to roles.

WinRM Endpoint ACL
As with regular PowerShell remoting endpoints, each JEA endpoint has a separate access control
list (ACL) that controls who can authenticate with the JEA endpoint. If improperly configured,
trusted users may not be able to access the JEA endpoint, and untrusted users may have access.
The WinRM ACL doesn't affect the mapping of users to JEA roles. Mapping is controlled by the
RoleDefinitions field in the session configuration file used to register the endpoint.

By default, when a JEA endpoint has multiple role capabilities, the WinRM ACL is configured to
allow access to all mapped users. For example, a JEA session configured using the following
commands grants full access to CONTOSO\JEA_Lev1 and CONTOSO\JEA_Lev2 .

 PowerShell

 $newPSSessionConfigurationFileSplat = @{
     Path = '.\jea.pssc'
     SessionType = 'RestrictedRemoteServer'
     RoleDefinitions = @{
         'CONTOSO\JEA_Lev1' = 'Lev1Role'
         'CONTOSO\JEA_Lev2' = 'Lev2Role'
     }
     RunAsVirtualAccount = $true
 }
 New-PSSessionConfigurationFile @newPSSessionConfigurationFileSplat
 Register-PSSessionConfiguration -Path '.\jea.pssc' -Name 'MyJEAEndpoint'

You can audit user permissions with the Get-PSSessionConfiguration cmdlet.

 PowerShell

<!-- p.851 -->

 Get-PSSessionConfiguration -Name 'MyJEAEndpoint' | Select-Object Permission

 Output

 Permission
 ----------
 CONTOSO\JEA_Lev1 AccessAllowed
 CONTOSO\JEA_Lev2 AccessAllowed

To change which users have access, run either Set-PSSessionConfiguration -Name 'MyJEAEndpoint'
-ShowSecurityDescriptorUI for an interactive prompt or Set-PSSessionConfiguration -Name

'MyJEAEndpoint' -SecurityDescriptorSddl <SDDL string> to update the permissions. Users need

at least Invoke rights to access the JEA endpoint.

It's possible to create a JEA endpoint that doesn't map a defined role to every user that has
access. These users can start a JEA session, but only have access to the default cmdlets. You can
audit user permissions in a JEA endpoint by running Get-PSSessionCapability . For more
information, see Auditing and Reporting on JEA.

Least privilege roles
When designing JEA roles, it's important to remember that the virtual and group-managed
service accounts running behind the scenes can have unrestricted access to the local machine.
JEA role capabilities help limit the commands and applications that can be run in that privileged
context. Improperly designed roles can allow dangerous commands that may permit a user to
break out of the JEA boundaries or obtain access to sensitive information.

For example, consider the following role capability entry:

 PowerShell

 @{
      VisibleCmdlets = 'Microsoft.PowerShell.Management\*-Process'
 }

This role capability allows users to run any PowerShell cmdlet with the noun Process from the
Microsoft.PowerShell.Management module. Users may need to access cmdlets like Get-Process
to see what applications are running on the system and Stop-Process to kill applications that
aren't responding. However, this entry also allows Start-Process , which can be used to start up
an arbitrary program with full administrator permissions. The program doesn't need to be

<!-- p.852 -->

installed locally on the system. A connected user could start a program from a file share that
gives the user local administrator privileges, runs malware, and more.

A more secure version of this same role capability would look like:

 PowerShell

 @{
      VisibleCmdlets = 'Microsoft.PowerShell.Management\Get-Process',
                       'Microsoft.PowerShell.Management\Stop-Process'
 }

Avoid using wildcards in role capabilities. Be sure to regularly audit effective user permissions to
see which commands are accessible to a user. For more information, see the Check effective rights
section of the Auditing and Reporting on JEA article.

Best practice recommendations
The following are best practice recommendations to ensure the security of your JEA endpoints:

Limit the use and capabilities of PowerShell providers
Review how the allowed providers are used to ensure that you don't create vulnerabilities in your
configured session.

  ２ Warning

  Don't allow the FileSystem provider. If users can write to any part of the file system, it's
  possible to completely bypass security.

  Don't allow the Certificate provider. With the provider enabled, a user could gain access to
  stored private keys.

Don't allow commands that can create new runspaces.

  ２ Warning

  The Windows Compatibility feature in PowerShell 7 creates a new runspace to host Windows
  PowerShell. Don't allow any commands that would run via the Windows Compatibility
  feature. The *-Job cmdlets can create new runspaces without the restrictions.

<!-- p.853 -->

Don't allow commands that add TypeData or FormatData
Restricted endpoints must not expose the Update-TypeData , Remove-TypeData , or Update-
FormatData commands. The *-TypeData commands allow you to add ScriptProperty members to

types. The Update-FormatData command allows you to add ScriptBlock definitions to create
custom formatting. The ScriptProperty and ScriptBlock members might be evaluated in
FullLanguage mode, even when the session is configured to use a more restrictive language

mode.

Don't allow the Trace-Command cmdlet.

  ２ Warning

  Using Trace-Command brings all traced commands into the session.

Don't create your own proxy implementations for the
restricted commands.
PowerShell has a set of proxy commands for restricted command scenarios. These proxy
commands ensure that input parameters can't compromise the security of the session. The
following commands have restricted proxies:

     Exit-PSSession

     Get-Command

     Get-FormatData

     Get-Help

     Measure-Object

     Out-Default

     Select-Object

If you create your own implementation of these commands, you may inadvertently allow users to
run code prohibited by the JEA proxy commands.

JEA doesn't protect against admins
One of the core principles of JEA is that it allows nonadministrators to do some administrative
tasks. JEA doesn't protect against users who already have administrator privileges. Users who
belong Domain Admins, local Administrators, or other highly privileged groups can circumvent

<!-- p.854 -->

JEA's protections in other ways. For example, they could sign in with RDP, use remote MMC
consoles, or connect to unconstrained PowerShell endpoints. Also, local administrator on a
system can modify JEA configurations to add more users or change a role capability to extend
the scope of what a user can do in their JEA session. It's important to evaluate your JEA users'
extended permissions to see if there are other ways to gain privileged access to the system.

In addition to using JEA for regular day-to-day maintenance, it's common to have a just-in-time
privileged access management system. These systems allow designated users to temporarily
become a local administrator only after they complete a workflow that documents their use of
those permissions.

 Last updated on 06/17/2026

<!-- p.855 -->

Auditing and Reporting on JEA
Article • 04/01/2024

After you've deployed JEA, you need to regularly audit the JEA configuration. Auditing
helps you assess that the correct people have access to the JEA endpoint and their
assigned roles are still appropriate.

Find registered JEA sessions on a machine
To check which JEA sessions are registered on a machine, use the Get-
PSSessionConfiguration cmdlet.

  PowerShell

  # Filter for sessions that are configured as 'RestrictedRemoteServer' to
  # find JEA-like session configurations
  Get-PSSessionConfiguration | Where-Object { $_.SessionType -eq
  'RestrictedRemoteServer' }

  Output

  Name          : JEAMaintenance
  PSVersion     : 5.1
  StartupScript :
  RunAsUser     :
  Permission    : CONTOSO\JEA_DNS_ADMINS AccessAllowed,
  CONTOSO\JEA_DNS_OPERATORS AccessAllowed,
                  CONTOSO\JEA_DNS_AUDITORS AccessAllowed

The effective rights for the endpoint are listed in the Permission property. These users
have the right to connect to the JEA endpoint. However, the roles and commands they
have access to is determined by the RoleDefinitions property in the session
configuration file that was used to register the endpoint. Expand the RoleDefinitions
property to evaluate the role mappings in a registered JEA endpoint.

  PowerShell

  # Get the desired session configuration
  $jea = Get-PSSessionConfiguration -Name 'JEAMaintenance'

  # Enumerate users/groups and which roles they have access to
  $jea.RoleDefinitions.GetEnumerator() | Select-Object Name, @{
    Name = 'Role Capabilities'

<!-- p.856 -->

      Expression = { $_.Value.RoleCapabilities }
  }

Find available role capabilities on the machine
JEA gets role capabilities from the .psrc files stored in the RoleCapabilities folder inside
a PowerShell module. The following function finds all role capabilities available on a
computer.

  PowerShell

  function Find-LocalRoleCapability {
      $results = @()

      # Find modules with a "RoleCapabilities" subfolder and add any PSRC
  files to the result set
      Get-Module -ListAvailable | ForEach-Object {
          $psrcpath = Join-Path -Path $_.ModuleBase -ChildPath
  'RoleCapabilities'
          if (Test-Path $psrcpath) {
              $results += Get-ChildItem -Path $psrcpath -Filter *.psrc
          }
      }

      # Format the results nicely to make it easier to read
      $results | Select-Object @{ Name = 'Name'; Expression = {
  $_.Name.TrimEnd('.psrc') }}, @{
          Name = 'Path'; Expression = { $_.FullName }
      } | Sort-Object Name
  }

  ７ Note

  The order of results from this function isn't necessarily the order in which the role
  capabilities will be selected if multiple role capabilities share the same name.

Check effective rights for a specific user
The Get-PSSessionCapability cmdlet enumerates all the commands available on a JEA
endpoint based on a user's group memberships. The output of Get-PSSessionCapability
is identical to that of the specified user running Get-Command -CommandType All in a JEA
session.

  PowerShell

<!-- p.857 -->

  Get-PSSessionCapability -ConfigurationName 'JEAMaintenance' -Username
  'CONTOSO\Alice'

If your users aren't permanent members of groups that would grant them additional JEA
rights, this cmdlet may not reflect those extra permissions. This happens when using
just-in-time privileged access management systems to allow users to temporarily belong
to a security group. Carefully evaluate the mapping of users to roles and capabilities to
ensure that users only get the level of access needed to do their jobs successfully.

PowerShell event logs
If you enabled module or script block logging on the system, you can see events in the
Windows event logs for each command a user runs in a JEA session. To find these
events, open Microsoft-Windows-PowerShell/Operational event log and look for
events with event ID 4104.

Each event log entry includes information about the session in which the command was
run. For JEA sessions, the event includes information about the ConnectedUser and the
RunAsUser. The ConnectedUser is the actual user who created the JEA session. The
RunAsUser is the account JEA used to execute the command.

Application event logs show changes being made by the RunAsUser. So having module
and script logging enabled is required to trace a specific command invocation back to
the ConnectedUser.

Application event logs
Commands run in a JEA session that interact with external applications or services may
log events to their own event logs. Unlike PowerShell logs and transcripts, other logging
mechanisms don't capture the connected user of the JEA session. Instead, those
applications only log the virtual run-as user. To determine who ran the command, you
need to consult a session transcript or correlate PowerShell event logs with the time and
user shown in the application event log.

The WinRM log can also help you correlate run-as users to the connecting user in an
application event log. Event ID 193 in the Microsoft-Windows-Windows Remote
Management/Operational log records the security identifier (SID) and account name for
both the connecting user and run as user for every new JEA session.

Session transcripts

<!-- p.858 -->

If you configured JEA to create a transcript for each user session, a text copy of every
user's actions are stored in the specified folder.

The following command (as an administrator) finds all transcript directories.

  PowerShell

  Get-PSSessionConfiguration |
    Where-Object { $_.TranscriptDirectory -ne $null } |
      Format-Table Name, TranscriptDirectory

Each transcript starts with information about the time the session started, which user
connected to the session, and which JEA identity was assigned to them.

  **********************
  Windows PowerShell transcript start
  Start time: 20160710144736
  Username: CONTOSO\Alice
  RunAs User: WinRM Virtual Users\WinRM VA_1_CONTOSO_Alice
  Machine: SERVER01 (Microsoft Windows NT 10.0.14393.0)
  [...]

The body of the transcript contains information about each command the user invoked.
The exact syntax of the command used is unavailable in JEA sessions because of the way
commands are transformed for PowerShell remoting. However, you can still determine
the effective command that was executed. Below is an example transcript snippet from a
user running Get-Service Dns in a JEA session:

  PS>CommandInvocation(Get-Service): "Get-Service"
  >> ParameterBinding(Get-Service): name="Name"; value="Dns"
  >> CommandInvocation(Out-Default): "Out-Default"
  >> ParameterBinding(Out-Default): name="InputObject"; value="Dns"

  Running      Dns                 DNS Server

A CommandInvocation line is written for each command a user runs.
ParameterBindings record each parameter and value supplied with the command. In the
previous example, you can see that the parameter Name was supplied the with value
Dns for the Get-Service cmdlet.

<!-- p.859 -->

The output of each command also triggers a CommandInvocation, usually to Out-
Default . The InputObject of Out-Default is the PowerShell object returned from the

command. The details of that object are printed a few lines below, closely mimicking
what the user would have seen.

See also
PowerShell ♥ the Blue Team blog post on security

<!-- p.860 -->

Running Remote Commands
You can run commands on one or hundreds of computers with a single PowerShell command.
Windows PowerShell supports remote computing using various technologies, including WMI,
RPC, and WS-Management.

PowerShell supports WMI, WS-Management, and SSH remoting. In PowerShell 7 and higher,
RPC is supported only on Windows.

For more information about remoting in PowerShell, see the following articles:

     SSH Remoting in PowerShell
     WSMan Remoting in PowerShell

Windows PowerShell remoting without
configuration
Many Windows PowerShell cmdlets have the ComputerName parameter that enables you to
collect data and change settings on one or more remote computers. These cmdlets use varying
communication protocols and work on all Windows operating systems without any special
configuration.

These cmdlets include:

     Restart-Computer
     Test-Connection
     Clear-EventLog
     Get-EventLog
     Get-HotFix
     Get-Process
     Get-Service
     Set-Service
     Get-WinEvent
     Get-WmiObject

Typically, cmdlets that support remoting without special configuration have the
ComputerName parameter and don't have the Session parameter. To find these cmdlets in
your session, type:

 PowerShell

 Get-Command | Where-Object {
     $_.Parameters.Keys -contains "ComputerName" -and

<!-- p.861 -->

      $_.Parameters.Keys -notcontains "Session"
 }

Windows PowerShell remoting
By using the WS-Management protocol, Windows PowerShell remoting lets you run any
Windows PowerShell command on one or more remote computers. You can establish
persistent connections, start interactive sessions, and run scripts on remote computers.

To use Windows PowerShell remoting, the remote computer must be configured for remote
management. For more information, including instructions, see About Remote Requirements.

Once you configure Windows PowerShell remoting, many remoting strategies are available to
you. This article lists just a few of them. For more information, see About Remote.

Start an interactive session
To start an interactive session with a single remote computer, use the Enter-PSSession cmdlet.
For example, to start an interactive session with the Server01 remote computer, type:

 PowerShell

 Enter-PSSession Server01

The command prompt changes to display the name of the remote computer. Any commands
that you type at the prompt run on the remote computer and the results are displayed on the
local computer.

To end the interactive session, type:

 PowerShell

 Exit-PSSession

For more information about the Enter-PSSession and Exit-PSSession cmdlets, see:

     Enter-PSSession
     Exit-PSSession

Run a Remote Command
To run a command on one or more computers, use the Invoke-Command cmdlet. For example,
to run a Get-UICulture command on the Server01 and Server02 remote computers, type:

<!-- p.862 -->

 PowerShell

 Invoke-Command -ComputerName Server01, Server02 -ScriptBlock {Get-UICulture}

The output is returned to your computer.

 Output

 LCID      Name      DisplayName                     PSComputerName
 ----      ----      -----------                     --------------
 1033      en-US     English (United States)         server01.corp.fabrikam.com
 1033      en-US     English (United States)         server02.corp.fabrikam.com

Run a Script
To run a script on one or many remote computers, use the FilePath parameter of the Invoke-
Command cmdlet. The script must be on or accessible to your local computer. The results are

returned to your local computer.

For example, the following command runs the DiskCollect.ps1 script on the remote
computers, Server01 and Server02.

 PowerShell
 Invoke-Command -ComputerName Server01, Server02 -FilePath C:\Scripts\DiskCollect.ps1

Establish a Persistent Connection
Use the New-PSSession cmdlet to create a persistent session on a remote computer. The
following example creates remote sessions on Server01 and Server02. The session objects are
stored in the $s variable.

 PowerShell
 $s = New-PSSession -ComputerName Server01, Server02

Now that the sessions are established, you can run any command in them. And because the
sessions are persistent, you can collect data from one command and use it in another
command.

For example, the following command runs a Get-HotFix command in the sessions in the $s
variable and it saves the results in the $h variable. The $h variable is created in each of the
sessions in $s , but it doesn't exist in the local session.

<!-- p.863 -->

 PowerShell

 Invoke-Command -Session $s {$h = Get-HotFix}

Now you can use the data in the $h variable with other commands in the same session. The
results are displayed on the local computer. For example:

 PowerShell
 Invoke-Command -Session $s {$h | where {$_.InstalledBy -ne "NT AUTHORITY\SYSTEM"}}

Advanced Remoting
PowerShell includes cmdlets that allow you to:

     Configure and create remote sessions both from the local and remote ends
     Create customized and restricted sessions
     Import commands from a remote session that actually run implicitly on the remote
     session
     Configure the security of a remote session

PowerShell on Windows includes a WSMan provider. The provider creates a WSMan: drive that
lets you navigate through a hierarchy of configuration settings on the local computer and
remote computers.

For more information about the WSMan provider, see WSMan Provider and About WS-
Management Cmdlets, or in the Windows PowerShell console, type Get-Help WSMan .

For more information, see:

     PowerShell Remoting FAQ
     Register-PSSessionConfiguration
     Import-PSSession

For help with remoting errors, see about_Remote_Troubleshooting.

See Also
     about_Remote
     about_Remote_Requirements
     about_Remote_Troubleshooting
     about_PSSessions
     about_WS-Management_Cmdlets

<!-- p.864 -->

     Invoke-Command
     Import-PSSession
     New-PSSession
     Register-PSSessionConfiguration
     WSMan Provider

Last updated on 12/09/2025

<!-- p.865 -->

PowerShell remoting over SSH
09/08/2025

Overview
PowerShell remoting normally uses WinRM for connection negotiation and data transport. SSH
is now available for Linux and Windows platforms and allows true multiplatform PowerShell
remoting.

WinRM provides a robust hosting model for PowerShell remote sessions. SSH-based remoting
doesn't currently support remote endpoint configuration and Just Enough Administration (JEA).

SSH remoting lets you do basic PowerShell session remoting between Windows and Linux
computers. SSH remoting creates a PowerShell host process on the target computer as an SSH
subsystem. Eventually we'll implement a general hosting model, similar to WinRM, to support
endpoint configuration and JEA.

The New-PSSession , Enter-PSSession , and Invoke-Command cmdlets now have a new parameter
set to support this new remoting connection.

  [-HostName <string>]    [-UserName <string>]     [-KeyFilePath <string>]

To create a remote session, you specify the target computer with the HostName parameter
and provide the user name with UserName. When running the cmdlets interactively, you're
prompted for a password. You can also use SSH key authentication using a private key file with
the KeyFilePath parameter. Creating keys for SSH authentication varies by platform.

General setup information
PowerShell 6 or higher, and SSH must be installed on all computers. Install both the SSH client
( ssh.exe ) and server ( sshd.exe ) so that you can remote to and from the computers. OpenSSH
for Windows is now available in Windows 10 build 1809 and Windows Server 2019. For more
information, see Manage Windows with OpenSSH. For Linux, install SSH, including sshd server,
that's appropriate for your platform. You also need to install PowerShell from GitHub to get the
SSH remoting feature. The SSH server must be configured to create an SSH subsystem to host
a PowerShell process on the remote computer. And, you must enable password or key-based
authentication.

<!-- p.866 -->

Install the SSH service on a Windows computer
 1. Install the latest version of PowerShell. For more information, see Installing PowerShell on
   Windows.

   You can confirm that PowerShell has SSH remoting support by listing the New-PSSession
   parameter sets. You'll notice there are parameter set names that begin with SSH. Those
   parameter sets include SSH parameters.

     PowerShell

      (Get-Command New-PSSession).ParameterSets.Name

     Output

      Name
      ----
      SSHHost
      SSHHostHashParam

 2. Install the latest Win32 OpenSSH. For installation instructions, see Getting started with
   OpenSSH.

     ７ Note

     If you want to set PowerShell as the default shell for OpenSSH, see Configuring
     Windows for OpenSSH.

 3. Edit the sshd_config file located at $Env:ProgramData\ssh .

         Make sure password authentication is enabled:

           PasswordAuthentication yes

         Create the SSH subsystem that hosts a PowerShell process on the remote computer:

           Subsystem powershell C:/progra~1/powershell/7/pwsh.exe -sshs

<!-- p.867 -->

  ７ Note

  There is a bug in OpenSSH for Windows that prevents you from using a path
  with spaces for the subsystem executable. There are two ways to work around
  this issue:
     Use the Windows 8.3-style short name for the PowerShell executable path
     Create a symbolic link to the PowerShell executable that results in a path
     without spaces

  For more information, see issue #784     in the PowerShell/Win32-OpenSSH
  repository.

You only need to get the 8.3-style name for the segment of the path that contains
the space. By default PowerShell 7 is installed in C:\Program Files\PowerShell\7\ .
The 8.3-style name for Program Files should be progra~1 . You can use the
following command to verify the name:

  PowerShell

  Get-CimInstance Win32_Directory -Filter 'Name="C:\\Program Files"' |
      Select-Object EightDotThreeFileName

The 8.3 name is a legacy feature of the NTFS file system that can be disabled. This
feature must be enabled for the volume on which PowerShell is installed.

Alternatively, you can create a symbolic link to the PowerShell executable that
results in a path without spaces. This method is preferred because it allows you to
update the link if the path to the PowerShell executable ever changes, without also
needing to update your sshd_config file.

Use the following command to create a symbolic link to the executable:

  PowerShell

  $newItemSplat = @{
       ItemType = 'SymbolicLink'
       Path = 'C:\ProgramData\ssh\'
       Name = 'pwsh.exe'
       Value = (Get-Command pwsh.exe).Source
  }
  New-Item @newItemSplat

<!-- p.868 -->

         This command creates the symbolic link in the same directory used by the OpenSSH
         server to store the host keys and other configuration.

         Optionally, enable key authentication:

             PubkeyAuthentication yes

         For more information, see Managing OpenSSH Keys.

 4. Restart the sshd service.

      PowerShell

      Restart-Service sshd

 5. Add the path where OpenSSH is installed to your PATH environment variable. For
   example, C:\Program Files\OpenSSH\ . This entry allows for the ssh.exe to be found.

Install the SSH service on an Ubuntu Linux
computer
 1. Install the latest version of PowerShell, see Installing PowerShell on Ubuntu.

 2. Install Ubuntu OpenSSH Server     .

      Bash

      sudo apt install openssh-client
      sudo apt install openssh-server

 3. Edit the sshd_config file at location /etc/ssh .

         Make sure password authentication is enabled:

             PasswordAuthentication yes

         Optionally, enable key authentication:

<!-- p.869 -->

             PubkeyAuthentication yes

         For more information about creating SSH keys on Ubuntu, see the manpage for ssh-
         keygen     .

         Add a PowerShell subsystem entry:

             Subsystem powershell /usr/bin/pwsh -sshs -NoLogo

             ７ Note

             The default location of the PowerShell executable is /usr/bin/pwsh . The
             location can vary depending on how you installed PowerShell.

 4. Restart the ssh service.

      Bash

      sudo systemctl restart sshd.service

Install the SSH service on a macOS computer
 1. Install the latest version of PowerShell. For more information, Installing PowerShell on
   macOS.

   Make sure SSH Remoting is enabled by following these steps:
    a. Open System Settings .
   b. Click on General
    c. Click on Sharing .
   d. Check Remote Login to set Remote Login: On .
    e. Allow access to the appropriate users.

 2. Edit the sshd_config file at location /private/etc/ssh/sshd_config .

   Use a text editor such as nano:

      Bash

<!-- p.870 -->

      sudo nano /private/etc/ssh/sshd_config

          Make sure password authentication is enabled:

             PasswordAuthentication yes

          Add a PowerShell subsystem entry:

             Subsystem powershell /usr/local/bin/pwsh -sshs -NoLogo

             ７ Note

             The default location of the PowerShell executable is /usr/local/bin/pwsh . The
             location can vary depending on how you installed PowerShell.

          Optionally, enable key authentication:

             PubkeyAuthentication yes

 3. Restart the sshd service.

      Bash

      sudo launchctl stop com.openssh.sshd
      sudo launchctl start com.openssh.sshd

 ７ Note

 When you upgrade your operating system, the SSH configuration file might be
 overwritten. Make sure you check the configuration file after an upgrade.

Authentication

<!-- p.871 -->

PowerShell remoting over SSH relies on the authentication exchange between the SSH client
and SSH service and doesn't implement any authentication schemes itself. The result is that any
configured authentication schemes including multi-factor authentication are handled by SSH
and independent of PowerShell. For example, you can configure the SSH service to require
public key authentication and a one-time password for added security. Configuration of multi-
factor authentication is outside the scope of this documentation. Refer to documentation for
SSH on how to correctly configure multi-factor authentication and validate it works outside of
PowerShell before attempting to use it with PowerShell remoting.

  ７ Note

  Users retain the same privileges in remote sessions. Meaning, Administrators have access
  to an elevated shell, and normal users do not.

PowerShell remoting example
The easiest way to test remoting is to try it on a single computer. In this example, we create a
remote session back to the same Linux computer. We're using PowerShell cmdlets interactively
so we see prompts from SSH asking to verify the host computer and prompting for a
password. You can do the same thing on a Windows computer to ensure remoting is working.
Then, remote between computers by changing the host name.

Linux to Linux
  PowerShell

  $session = New-PSSession -HostName UbuntuVM1 -UserName TestUser

  Output

  The authenticity of host 'UbuntuVM1 (9.129.17.107)' can't be established.
  ECDSA key fingerprint is SHA256:2kCbnhT2dUE6WCGgVJ8Hyfu1z2wE4lifaJXLO7QJy0Y.
  Are you sure you want to continue connecting (yes/no)?
  TestUser@UbuntuVM1s password:

  PowerShell

  $session

  Output

<!-- p.872 -->

  Id Name   ComputerName       ComputerType      State     ConfigurationName
 Availability
  -- ----   ------------       ------------      -----     -----------------     --------
 ----
   1 SSH1   UbuntuVM1          RemoteMachine     Opened    DefaultShell
 Available

 PowerShell

 Enter-PSSession $session

 Output

 [UbuntuVM1]: PS /home/TestUser> uname -a
 Linux TestUser-UbuntuVM1 4.2.0-42-generic 49~16.04.1-Ubuntu SMP Wed Jun 29
 20:22:11 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

 [UbuntuVM1]: PS /home/TestUser> Exit-PSSession

 PowerShell

 Invoke-Command $session -ScriptBlock { Get-Process pwsh }

 Output

 Handles NPM(K)     PM(K)        WS(K)        CPU(s)      Id   SI ProcessName
 PSComputerName
 ------- ------     -----        -----        ------      --   -- -----------   ---------
 -----
       0        0       0           19          3.23   10635 635 pwsh           UbuntuVM1
       0        0       0           21          4.92   11033 017 pwsh           UbuntuVM1
       0        0       0           20          3.07   11076 076 pwsh           UbuntuVM1

Linux to Windows
 PowerShell

 Enter-PSSession -HostName WinVM1 -UserName PTestName

 PTestName@WinVM1s password:

<!-- p.873 -->

 PowerShell

 [WinVM1]: PS C:\Users\PTestName\Documents> cmd /c ver

 Output

 Microsoft Windows [Version 10.0.10586]

Windows to Windows
 PowerShell

 C:\Users\PSUser\Documents>pwsh.exe

 Output

 PowerShell
 Copyright (c) Microsoft Corporation. All rights reserved.

 PowerShell

 $session = New-PSSession -HostName WinVM2 -UserName PSRemoteUser

 Output

 The authenticity of host 'WinVM2 (10.13.37.3)' can't be established.
 ECDSA key fingerprint is SHA256:kSU6slAROyQVMEynVIXAdxSiZpwDBigpAF/TXjjWjmw.
 Are you sure you want to continue connecting (yes/no)?
 Warning: Permanently added 'WinVM2,10.13.37.3' (ECDSA) to the list of known hosts.
 PSRemoteUser@WinVM2's password:

 PowerShell

 $session

 Output

   Id Name             ComputerName     ComputerType    State
 ConfigurationName       Availability
   -- ----             ------------     ------------    -----       ----------------
 -      ------------
    1 SSH1             WinVM2           RemoteMachine   Opened      DefaultShell
 Available

<!-- p.874 -->

 PowerShell

 Enter-PSSession -Session $session

 Output

 [WinVM2]: PS C:\Users\PSRemoteUser\Documents> $PSVersionTable

 Name                                Value
 ----                                -----
 PSEdition                           Core
 PSCompatibleVersions                {1.0, 2.0, 3.0, 4.0...}
 SerializationVersion                1.1.0.1
 BuildVersion                        3.0.0.0
 CLRVersion
 PSVersion                           6.0.0-alpha
 WSManStackVersion                   3.0
 PSRemotingProtocolVersion           2.3
 GitCommitId                         v6.0.0-alpha.17

 [WinVM2]: PS C:\Users\PSRemoteUser\Documents>

Limitations
    The sudo command doesn't work in a remote session to a Linux computer.

    PSRemoting over SSH doesn't support Profiles and doesn't have access to $PROFILE . Once
    in a session, you can load a profile by dot sourcing the profile with the full filepath. This
    isn't related to SSH profiles. You can configure the SSH server to use PowerShell as the
    default shell and to load a profile through SSH. See the SSH documentation for more
    information.

    Prior to PowerShell 7.1, remoting over SSH didn't support second-hop remote sessions.
    This capability was limited to sessions using WinRM. PowerShell 7.1 allows Enter-
    PSSession and Enter-PSHostProcess to work from within any interactive remote session.

See also
    Installing PowerShell on Linux
    Installing PowerShell on macOS
    Installing PowerShell on Windows
    Manage Windows with OpenSSH
    Managing OpenSSH Keys

<!-- p.875 -->

Ubuntu SSH

<!-- p.876 -->

Using WS-Management (WSMan)
Remoting in PowerShell

Enabling PowerShell remoting
To enable PowerShell remoting, run the Enable-PSRemoting cmdlet in an elevated PowerShell
session. Running Enable-PSRemoting configures a remoting endpoint for the specific
installation version that you're running the cmdlet in. For example, when you run Enable-
PSRemoting while running PowerShell 7.4, PowerShell creates a remoting endpoint runs

PowerShell 7.4. If you run Enable-PSRemoting while running PowerShell 7-preview, PowerShell
creates a remoting endpoint that runs PowerShell 7-preview. You can create multiple remoting
endpoints for different versions of that run side-by-side.

Running Enable-PSRemoting creates two endpoints for that version.

     One has a simple name corresponding to the PowerShell major version. that hosts the
     session. For example, PowerShell.7.4.
     The other configuration name contains the full version number. For example,
     PowerShell.7.4.7.

You can connect to the latest version of PowerShell 7 host version using the simple name,
PowerShell.7.4. You can connect to a specific version of PowerShell using the longer, version-
specific name.

Use the ConfigurationName parameter with the New-PSSession and Enter-PSSession cmdlets
to connect to a named configuration.

Remoting to older versions of Windows
The following prerequisites must be met to enable PowerShell remoting over WSMan on older
versions of Windows.

     Install the Windows Management Framework (WMF) 5.1 (as necessary). For more
     information about WMF, see WMF Overview.
     Install the Universal C Runtime    on Windows versions predating Windows 10. It's
     available via direct download or Windows Update. Fully patched systems already have
     this package installed.

<!-- p.877 -->

WSMan remoting isn't supported on non-Windows
platforms
Since the release of PowerShell 6, support for remoting over WS-Management (WSMan) on
non-Windows platforms is only available to a limited set of Linux distributions. On non-
Windows, WSMan relied on the Open Management Infrastructure (OMI)          project. The OMI
WSMan client depends on OpenSSL 1.0. All Linux distributions use OpenSSL 2.0, which isn't
backward-compatible. There are no supported distributions that have the dependencies
needed for the OMI WSMan client to work.

WSMan-based remoting is still supported between Windows systems. Remoting over SSH is
supported for all platforms. For more information, see PowerShell remoting over SSH.

Further reading
      Enable-PSRemoting
      Enter-PSSession
      New-PSSession

 Last updated on 12/09/2025

<!-- p.878 -->

Security Considerations for PowerShell
Remoting using WinRM
PowerShell Remoting is the recommended way to manage Windows systems. PowerShell
Remoting is enabled by default in Windows Server 2012 R2 and higher. This document covers
security concerns, recommendations, and best practices when using PowerShell Remoting.

What is PowerShell Remoting?
PowerShell Remoting uses Windows Remote Management (WinRM) to allow users to run
PowerShell commands on remote computers. WinRM is the Microsoft implementation of the
Web Services for Management (WS-Management)          protocol. You can find more information
about using PowerShell Remoting at Running Remote Commands.

PowerShell Remoting isn't the same as using the ComputerName parameter of a cmdlet to run
it on a remote computer, which uses Remote Procedure Call (RPC) as its underlying protocol.

PowerShell Remoting default settings
PowerShell Remoting with WinRM listens on the following ports:

     HTTP: 5985
     HTTPS: 5986

By default, PowerShell Remoting only allows connections from members of the Administrators
group. Sessions are launched under the user's context, so all operating system access controls
applied to individual users and groups continue to apply to them while connected over
PowerShell Remoting.

On private networks, the default Windows Firewall rule for PowerShell Remoting accepts all
connections. On public networks, the default Windows Firewall rule allows PowerShell
Remoting connections only from within the same subnet. You have to explicitly change that
rule to open PowerShell Remoting to all connections on a public network.

  ２ Warning

  The firewall rule for public networks is meant to protect the computer from potentially
  malicious external connection attempts. Use caution when removing this rule. For more
  information about configuring WinRM, see Installation and configuration for Windows
  Remote Management.

<!-- p.879 -->

Process isolation
PowerShell Remoting uses WinRM for communication between computers. WinRM runs as a
service under the Network Service account, and spawns isolated processes running as user
accounts to host PowerShell instances. An instance of PowerShell running as one user has no
access to a process running an instance of PowerShell as another user.

Event logs generated by PowerShell Remoting
Researchers from Mandiant presented a session at the BlackHat conference that provides a
good summary of the event logs and other security evidence generated by PowerShell
Remoting sessions. For more information, see Investigating PowerShell Attacks       .

Encryption and transport protocols
It's helpful to consider the security of a PowerShell Remoting connection from two
perspectives: initial authentication, and ongoing communication.

Regardless of the transport protocol used (HTTP or HTTPS), WinRM always encrypts all
PowerShell remoting communication after initial authentication.

Initial authentication
Authentication confirms the identity of the client to the server - and ideally - the server to the
client.

When a client connects to a domain server using its computer name, the default authentication
protocol is Kerberos. Kerberos guarantees both the user identity and server identity without
sending any sort of reusable credential.

When a client connects to a domain server using its IP address, or connects to a workgroup
server, Kerberos authentication isn't possible. In that case, PowerShell Remoting relies on the
NTLM authentication protocol. The NTLM authentication protocol guarantees the user identity
without sending any sort of delegable credential. To prove user identity, the NTLM protocol
requires that both the client and server compute a session key from the user's password
without ever exchanging the password itself. The server typically doesn't know the user's
password, so it communicates with the domain controller, which does know the user's
password and calculates the session key for the server.

The NTLM protocol doesn't, however, guarantee server identity. As with all protocols that use
NTLM for authentication, an attacker with access to a domain-joined computer's machine

<!-- p.880 -->

account could invoke the domain controller to compute an NTLM session-key and impersonate
the server.

NTLM-based authentication is disabled by default. You can enable NTLM by either configuring
SSL on the target server, or by configuring the WinRM TrustedHosts setting on the client.

Using SSL certificates to validate server identity during NTLM-based
connections
Since the NTLM authentication protocol can't ensure the identity of the target server (only that
it already knows your password), you can configure target servers to use SSL for PowerShell
Remoting. Assigning an SSL certificate to the target server (if issued by a Certificate Authority
that the client also trusts) enables NTLM-based authentication that guarantees both the user
identity and server identity.

Ignoring NTLM-based server identity errors

If deploying an SSL certificate to a server for NTLM connections is infeasible, you can suppress
the resulting identity errors by adding the server to the WinRM TrustedHosts list. Adding a
server name to the TrustedHosts list shouldn't be considered as any form of statement of the
trustworthiness of the hosts themselves - as the NTLM authentication protocol can't guarantee
that you are in fact connecting to the host you're intending to connect to. Instead, you should
consider the TrustedHosts setting to be the list of hosts for which you wish to suppress the
error generated by being unable to verify the server's identity.

Ongoing Communication
Once initial authentication is complete, the WinRM encrypts the ongoing communication.
When you connect over HTTPS, WinRM uses the TLS protocol to negotiate the encryption used
to transport data. When you connect over HTTP, WinRM uses the message-level encryption
negotiated by the initial authentication protocol.

     Basic authentication provides no encryption.
     NTLM authentication uses an RC4 cipher with a 128-bit key.
     The etype in the TGS ticket determines Kerberos authentication encryption. Modern
     systems use the AES-256 algorithm.
     CredSSP encryption uses the TLS cipher suite negotiated in the handshake.

Making the second hop
