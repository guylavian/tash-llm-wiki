---
title: "How to use this documentation — pages 881-920"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0881-0920
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0881-0920
family: powershell
documentKind: "doc"
abstract: "By default, PowerShell Remoting uses Kerberos (if available) or NTLM for authentication. Both of these protocols authenticate to the remote machine without sending credentials to it. This is the most secure way to authenticate, but because the remote machine doesn't have the use"
---

# How to use this documentation — pages 881-920

<!-- p.881 -->

By default, PowerShell Remoting uses Kerberos (if available) or NTLM for authentication. Both
of these protocols authenticate to the remote machine without sending credentials to it. This is
the most secure way to authenticate, but because the remote machine doesn't have the user's
credentials, it can't access other computers and services on the user's behalf. This is known as
the second hop problem.

There are several ways to avoid this problem. For descriptions of these methods, and the pros
and cons of each, see Making the second hop in PowerShell Remoting.

References
      Windows Remote Management (WinRM)
      Web Services for Management (WS-Management)
      2.2.9.1 Encrypted Message Types
      Kerberos
      NTLM authentication protocol
      Investigating PowerShell Attacks

 Last updated on 12/09/2025

<!-- p.882 -->

Making the second hop in PowerShell
Remoting
The following scenario outlines the second hop problem:

   1. You're logged in to ServerA.
   2. From ServerA, you start a remote PowerShell session to connect to ServerB.
   3. A command you run on ServerB via your PowerShell Remoting session attempts to access
     a resource on ServerC.
   4. Access to the resource on ServerC is denied, because the credentials you used to create
     the PowerShell Remoting session aren't passed from ServerB to ServerC.

There are several ways to address this problem. The following table lists the methods in order
of preference.

                                                                                    ﾉ     Expand table

 Configuration                               Note

 CredSSP                                     Balances ease of use and security

 Resource-based Kerberos constrained         Higher security with simpler configuration
 delegation

 Kerberos constrained delegation             High security but requires Domain Administrator

 Kerberos delegation (unconstrained)         Not recommended

 Just Enough Administration (JEA)            Can provide the best security but requires more detailed
                                             configuration

 PSSessionConfiguration using RunAs          Simpler to configure but requires credential
                                             management

 Pass credentials inside an Invoke-Command   Simplest to use but you must provide credentials
 script block

CredSSP
You can use the Credential Security Support Provider (CredSSP) for authentication. CredSSP
caches credentials on the remote server (ServerB), so using it opens you up to credential theft
attacks. If the remote computer is compromised, the attacker has access to the user's
credentials. CredSSP is disabled by default on both client and server computers. You should
enable CredSSP only in the most trusted environments. For example, a domain administrator
connecting to a domain controller because the domain controller is highly trusted.

<!-- p.883 -->

For more information about security concerns when using CredSSP for PowerShell Remoting,
see Accidental Sabotage: Beware of CredSSP     .

For more information about credential theft attacks, see Mitigating Pass-the-Hash (PtH) Attacks
and Other Credential Theft      .

For an example of how to enable and use CredSSP for PowerShell remoting, see Enable
PowerShell "Second-Hop" Functionality with CredSSP      .

Pros
     It works for all servers with Windows Server 2008 or later.

Cons
     Has security vulnerabilities.
     Requires configuration of both client and server roles.
     doesn't work with the Protected Users group. For more information, see Protected Users
     Security Group.

Kerberos constrained delegation
You can use legacy constrained delegation (not resource-based) to make the second hop.
Configure Kerberos constrained delegation with the option "Use any authentication protocol"
to allow protocol transition.

Pros
     Requires no special coding
     Credentials aren't stored.

Cons
     Doesn't support the second hop for WinRM.
     Requires Domain Administrator access to configure.
     Must be configured on the Active Directory object of the remote server (ServerB).
     Limited to one domain. Can't cross domains or forests.
     Requires rights to update objects and Service Principal Names (SPNs).
     ServerB can acquire a Kerberos ticket to ServerC on behalf of the user without user
     intervention.

<!-- p.884 -->

  ７ Note

  Active Directory accounts that have the Account is sensitive and can't be delegated
  property set can't be delegated. For more information, see Security Focus: Analysing
  'Account is sensitive and can't be delegated' for Privileged Accounts and Kerberos
  Authentication Tools and Settings.

Resource-based Kerberos constrained delegation
Windows Server 2012 introduced resource-based Kerberos constrained delegation. You
configure credential delegation on the server object where resources reside. In the second hop
scenario described previously, you configure ServerC to specify from where it accepts
delegated credentials.

Pros
     Credentials aren't stored.
     Configured using PowerShell cmdlets. No special coding required.
     Doesn't require Domain Administrator access to configure.
     Works across domains and forests.

Cons
     Requires Windows Server 2012 or later.
     Doesn't support the second hop for WinRM.
     Requires rights to update objects and Service Principal Names (SPNs).

  ７ Note

  Active Directory accounts that have the Account is sensitive and can't be delegated
  property set can't be delegated. For more information, see Security Focus: Analysing
  'Account is sensitive and can't be delegated' for Privileged Accounts and Kerberos
  Authentication Tools and Settings.

Example
Let's look at a PowerShell example that configures resource-based constrained delegation on
ServerC that allow delegated credentials from a ServerB. This example assumes that all servers

<!-- p.885 -->

are running supported versions of Windows Server, and that there is at least one Windows
domain controller for each trusted domain.

Before you can configure constrained delegation, you must add the RSAT-AD-PowerShell
feature to install the Active Directory PowerShell module, and then import that module into
your session:

 PowerShell

 Add-WindowsFeature RSAT-AD-PowerShell
 Import-Module ActiveDirectory
 Get-Command -ParameterName PrincipalsAllowedToDelegateToAccount

Several available cmdlets now have a PrincipalsAllowedToDelegateToAccount parameter:

 Output
 CommandType Name                 ModuleName
 ----------- ----                 ----------
 Cmdlet      New-ADComputer       ActiveDirectory
 Cmdlet      New-ADServiceAccount ActiveDirectory
 Cmdlet      New-ADUser           ActiveDirectory
 Cmdlet      Set-ADComputer       ActiveDirectory
 Cmdlet      Set-ADServiceAccount ActiveDirectory
 Cmdlet      Set-ADUser           ActiveDirectory

The PrincipalsAllowedToDelegateToAccount parameter sets the Active Directory object
attribute msDS-AllowedToActOnBehalfOfOtherIdentity. This attribute contains an access
control list (ACL) that specifies the accounts that have permission to delegate credentials to the
associated account. For this example, it's the machine account for ServerA.

Now let's create the variables that represent the servers:

 PowerShell
 # Set up variables for reuse
 $ServerA = $Env:COMPUTERNAME
 $ServerB = Get-ADComputer -Identity ServerB
 $ServerC = Get-ADComputer -Identity ServerC

WinRM (and therefore PowerShell remoting) runs as the computer account by default. You can
see this by looking at the StartName property of the winrm service:

 PowerShell
 Get-CimInstance Win32_Service -Filter 'Name="winrm"' | Select-Object StartName

<!-- p.886 -->

 Output
 StartName
 ---------
 NT AUTHORITY\NetworkService

For ServerC to allow delegation from a PowerShell remoting session on ServerB, we must set
the PrincipalsAllowedToDelegateToAccount parameter on ServerC to the computer object of
ServerB:

 PowerShell

 # Grant resource-based Kerberos constrained delegation
 Set-ADComputer -Identity $ServerC -PrincipalsAllowedToDelegateToAccount $ServerB

 # Check the value of the attribute directly
 $x = Get-ADComputer -Identity $ServerC -Properties msDS-
 AllowedToActOnBehalfOfOtherIdentity
 $x.'msDS-AllowedToActOnBehalfOfOtherIdentity'.Access

 # Check the value of the attribute indirectly
 Get-ADComputer -Identity $ServerC -Properties PrincipalsAllowedToDelegateToAccount

The Kerberos Key Distribution Center (KDC) caches denied-access attempts (negative cache) for
15 minutes. If ServerB previously attempted to access ServerC, you need to clear the cache on
ServerB by invoking the following command:

 PowerShell
 Invoke-Command -ComputerName $ServerB.Name -Credential $cred -ScriptBlock {
     klist purge -li 0x3e7
 }

You could also restart the computer, or wait at least 15 minutes to clear the cache.

After clearing the cache, you can successfully run code from ServerA through ServerB to
ServerC:

 PowerShell
 # Capture a credential
 $cred = Get-Credential Contoso\Alice

 # Test kerberos double hop
 Invoke-Command -ComputerName $ServerB.Name -Credential $cred -ScriptBlock {
     Test-Path \\$($Using:ServerC.Name)\C$
     Get-Process lsass -ComputerName $($Using:ServerC.Name)
     Get-EventLog -LogName System -Newest 3 -ComputerName $($Using:ServerC.Name)
 }

<!-- p.887 -->

In this example, the Using: scope modifier is used to make the $ServerC variable visible to
ServerB. For more information about the Using: scope modifier, see about_Remote_Variables.

To allow multiple servers to delegate credentials to ServerC, set the value of the
PrincipalsAllowedToDelegateToAccount parameter on ServerC to an array:

 PowerShell
 # Set up variables for each server
 $ServerB1 = Get-ADComputer -Identity ServerB1
 $ServerB2 = Get-ADComputer -Identity ServerB2
 $ServerB3 = Get-ADComputer -Identity ServerB3
 $ServerC = Get-ADComputer -Identity ServerC

 $servers = @(
     $ServerB1,
     $ServerB2,
     $ServerB3
 )

 # Grant resource-based Kerberos constrained delegation
 Set-ADComputer -Identity $ServerC -PrincipalsAllowedToDelegateToAccount $servers

If you want to make the second hop across domains, use the Server parameter to specify fully
qualified domain name (FQDN) of the domain controller of the domain to which ServerB
belongs:

 PowerShell
 # For ServerC in Contoso domain and ServerB in other domain
 $ServerB = Get-ADComputer -Identity ServerB -Server dc1.alpineskihouse.com
 $ServerC = Get-ADComputer -Identity ServerC
 Set-ADComputer -Identity $ServerC -PrincipalsAllowedToDelegateToAccount $ServerB

To remove the ability to delegate credentials to ServerC, set the value of the
PrincipalsAllowedToDelegateToAccount parameter on ServerC to $null :

 PowerShell
 Set-ADComputer -Identity $ServerC -PrincipalsAllowedToDelegateToAccount $null

Information on resource-based Kerberos constrained
delegation
     What's New in Kerberos Authentication
     How Windows Server 2012 Eases the Pain of Kerberos Constrained Delegation, Part 1

<!-- p.888 -->

     How Windows Server 2012 Eases the Pain of Kerberos Constrained Delegation, Part 2
     Understanding Kerberos Constrained Delegation for Microsoft Entra application proxy
     deployments with Integrated Windows Authentication
     [MS-ADA2 Active Directory Schema Attributes M2.210 Attribute msDS-
     AllowedToActOnBehalfOfOtherIdentity]MS-ADA2
     [MS-SFU Kerberos Protocol Extensions: Service for User and Constrained Delegation
     Protocol 1.3.2 S4U2proxy]MS-SFU
     Remote Administration Without Constrained Delegation Using
     PrincipalsAllowedToDelegateToAccount

Kerberos delegation (unconstrained)
You can also use Kerberos unconstrained delegation to make the second hop. Like all Kerberos
scenarios, credentials aren't stored. This method doesn't support the second hop for WinRM.

  ２ Warning

  This method provides no control of where delegated credentials are used. It's less secure
  than CredSSP. This method should only be used for testing scenarios.

Just Enough Administration (JEA)
JEA allows you to restrict what commands an administrator can run during a PowerShell
session. It can be used to solve the second hop problem.

For information about JEA, see Just Enough Administration.

Pros
     No password maintenance when using a virtual account.

Cons
     Requires WMF 5.0 or later.
     Requires configuration on every intermediate server (ServerB).

PSSessionConfiguration using RunAs
You can create a session configuration on ServerB and set its RunAsCredential parameter.

<!-- p.889 -->

For information about using PSSessionConfiguration and RunAs to solve the second hop
problem, see Another solution to multi-hop PowerShell remoting.

Pros
     Works with any server with WMF 3.0 or later.

Cons
     Requires configuration of PSSessionConfiguration and RunAs on every intermediate
     server (ServerB).
     Requires password maintenance when using a domain RunAs account

Pass credentials inside an Invoke-Command script
block
You can pass credentials inside the ScriptBlock parameter of a call to the Invoke-Command
cmdlet.

Pros
     Doesn't require special server configuration.
     Works on any server running WMF 2.0 or later.

Cons
     Requires an awkward code technique.
     If running WMF 2.0, requires different syntax for passing arguments to a remote session.

Example
The following example shows how to pass credentials in a script block:

 PowerShell
 # This works without delegation, passing fresh creds
 # Note $Using:Cred in nested request
 $cred = Get-Credential Contoso\Administrator
 Invoke-Command -ComputerName ServerB -Credential $cred -ScriptBlock {
     hostname
     Invoke-Command -ComputerName ServerC -Credential $Using:cred -ScriptBlock

<!-- p.890 -->

 {hostname}
 }

See also
PowerShell Remoting Security Considerations

Last updated on 12/09/2025

<!-- p.891 -->

Securing a restricted PowerShell
remoting session
There are scenarios where you want to host a PowerShell session that, for security reasons, has
been limited to a subset of PowerShell commands.

By definition, a restricted session is one where Import-Module isn't allowed to be used. There may
be other limitations, but this is the primary requirement. If the user can import a module, then
they can run anything they want.

Examples of restricted sessions include:

     Just-Enough-Administration (JEA)
     Custom restricted remoting implementations such as the Exchange and Teams modules

For most system administrators, JEA provides the best experience for creating restricted sessions
and should be your first choice. For more information about JEA, see the JEA Overview.

Recommendations for custom session implementations
If your scenario requires a custom implementation, then you should follow these
recommendations.

Limit the use and capabilities of PowerShell providers
Review how the allowed providers are used to ensure that you don't create vulnerabilities in your
restricted session implementation.

  ２ Warning

  Don't allow the FileSystem provider. If users can write to any part of the file system, it's
  possible to completely bypass security.

  Don't allow the Certificate provider. With the provider enabled, a user could gain access to
  stored private keys.

Don't allow commands that can create new runspaces

<!-- p.892 -->

  ２ Warning

  The Windows Compatibility feature in PowerShell 7 creates a new runspace to host Windows
  PowerShell. Don't allow any commands that would run via the Windows Compatibility
  feature. The *-Job cmdlets can create new runspaces without the restrictions.

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
restricted commands
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

<!-- p.893 -->

You can run the following command to get a list of restricted commands:

 PowerShell

 $commands = [System.Management.Automation.CommandMetadata]::GetRestrictedCommands(
     [System.Management.Automation.SessionCapabilities]::RemoteServer
 )

You can examine the restricted proxy commands by using the following command:

 PowerShell

 $commands = [System.Management.Automation.CommandMetadata]::GetRestrictedCommands(
     [System.Management.Automation.SessionCapabilities]::RemoteServer
 )
 $getHelpProxyBlock =
 [System.Management.Automation.ProxyCommand]::Create($commands['Get-Help'])

Configure the session to use NoLanguage mode
PowerShell NoLanguage mode disables the PowerShell scripting language completely. You can't
run scripts or use variables. You can only run native commands and cmdlets.

For more information about language modes, see about_Language_Modes.

Don't allow the debugger to be used in the session
By default, the PowerShell debugger runs code in FullLanguage mode. Set the
UseFullLanguageModeInDebugger property in the SessionState to false.

For more information, see UseFullLanguageModeInDebugger.

Last updated on 07/01/2026

<!-- p.894 -->

PowerShell Remoting FAQ
When you work remotely, you type commands in PowerShell on one computer (known as the
"local computer"), but the commands run on another computer (known as the "remote
computer"). The experience of working remotely should be as much like working directly at the
remote computer as possible.

  ７ Note

  To use PowerShell remoting, the remote computer must be configured for remoting. For
  more information, see about_Remote_Requirements.

Must both computers have PowerShell
installed?
Yes. To work remotely, the local and remote computers must have PowerShell, the Microsoft .NET
Framework, and the Web Services for Management (WS-Management) protocol. Any files and
other resources that are needed to execute a particular command must be on the remote
computer.

Computers running Windows PowerShell 3.0 and computers running Windows PowerShell 2.0 can
connect to each other remotely and run remote commands. However, some features, such as the
ability to disconnect from a session and reconnect to it, work only when both computers are
running Windows PowerShell 3.0.

You must have permission to connect to the remote computer, permission to run PowerShell, and
permission to access data stores (such as files and folders), and the registry on the remote
computer.

For more information, see about_Remote_Requirements.

How does remoting work?
When you submit a remote command, the command is transmitted across the network to the
PowerShell engine on the remote computer, and it runs in the PowerShell client on the remote

<!-- p.895 -->

computer. The command results are sent back to the local computer and appear in the
PowerShell session on the local computer.

To transmit the commands and receive the output, PowerShell uses the WS-Management
protocol. For information about the WS-Management protocol, see WS-Management Protocol in
the Windows documentation.

Beginning in Windows PowerShell 3.0, PowerShell store remote session information on the
remote computer. This enables you to disconnect from the session and reconnect from a
different session or a different computer without interrupting the commands or losing state.

Is PowerShell remoting secure?
When you connect to a remote computer, the system uses the username and password
credentials on the local computer or the credentials that you supply in the command to log you
in to the remote computer. The credentials and the rest of the transmission are encrypted.

To increase protection, you can configure the remote computer to use Secure Sockets Layer (SSL)
instead of HTTP for Windows Remote Management (WinRM) requests. Then, users can use the
UseSSL parameter of the Invoke-Command , New-PSSession , and Enter-PSSession cmdlets when
establishing a connection. This option uses the more secure HTTPS channel instead of HTTP.

Do all remote commands require
PowerShell remoting?
No. Some cmdlets have a ComputerName parameter that lets you get objects from the remote
computer.

These cmdlets don't use PowerShell remoting. You can use them on any computer running
PowerShell. The following cmdlets don't require PowerShell remoting:

     Get-HotFix

     Rename-Computer

     Restart-Computer

     Stop-Computer

To find all the cmdlets with a ComputerName parameter, type:

 PowerShell

<!-- p.896 -->

 Get-Help * -Parameter ComputerName
 # or
 Get-Command -ParameterName ComputerName

To determine whether the ComputerName parameter of a particular cmdlet requires PowerShell
remoting, see the parameter description. To display the parameter description, type:

 PowerShell

 Get-Help <cmdlet-name> -Parameter ComputerName

For example:

 PowerShell

 Get-Help Get-HotFix -Parameter ComputerName

For all other commands, use the Invoke-Command cmdlet.

How do I run a command on a
remote computer?
To run a command on a remote computer, use the Invoke-Command cmdlet. Enclose your
command in braces ( {} ). Use the ScriptBlock parameter of Invoke-Command to specify the
command.

Use the ComputerName parameter of Invoke-Command to specify a remote computer. Or, you can
create a persistent connection to a remote computer (a session) and then use the Session
parameter of Invoke-Command to run the command in the session.

For example, the following commands run a Get-Process command remotely.

 PowerShell

 Invoke-Command -ComputerName Server01, Server02 -ScriptBlock {Get-Process}

 #   - OR -

 Invoke-Command -Session $s -ScriptBlock {Get-Process}

To interrupt a remote command, type Ctrl + C . The interruption request is passed to the remote
computer, where it terminates the remote command.

<!-- p.897 -->

For more information about remote commands, see about_Remote and the Help for the cmdlets
that support remoting.

Can I just telnet into a remote computer?
You can use the Enter-PSSession cmdlet to start an interactive session with a remote computer.

At the PowerShell prompt, type:

 PowerShell

 Enter-PSSession <ComputerName>

The command prompt changes to show that you are connected to the remote computer.

 <ComputerName>\C:>

The commands you enter run on the remote computer as though you entered them directly on
the remote computer.

To end the interactive session, type:

 PowerShell

 Exit-PSSession

An interactive session is a persistent session that uses the WS-Management protocol. It isn't the
same as using Telnet, but it provides a similar experience.

For more information, see Enter-PSSession .

Can I create a persistent connection?
Yes. You can run remote commands by specifying the name of the remote computer, its NetBIOS
name, or its IP address. Or, you can run remote commands by specifying a PowerShell session
(PSSession) that's connected to the remote computer.

When you use the ComputerName parameter of Invoke-Command or Enter-PSSession , PowerShell
establishes a temporary connection. PowerShell uses the connection to run only the current

<!-- p.898 -->

command, and then it closes the connection. This behavior works well for running a single
command or several unrelated commands, even on many remote computers.

When you use the New-PSSession cmdlet to create a PSSession, PowerShell establishes a
persistent connection for the PSSession. Then, you can run multiple commands in the PSSession,
including commands that share data.

Typically, you create a PSSession to run a series of related commands that share data. Otherwise,
the temporary connection created by the ComputerName parameter is sufficient for most
commands.

For more information about sessions, see about_PSSessions.

Can I run commands on more than one
computer at a time?
Yes. The ComputerName parameter of the Invoke-Command cmdlet accepts multiple computer
names, and the Session parameter accepts multiple PSSessions.

When you run an Invoke-Command command, PowerShell runs the commands on all of the
specified computers or in all of the specified PSSessions.

PowerShell can manage hundreds of concurrent remote connections. However, the number of
remote commands that you can send can be limited by the resources of your computer and its
capacity to establish and maintain multiple network connections.

For more information, see the example in the Invoke-Command Help article.

Where are my profiles?
PowerShell profiles aren't run automatically in remote sessions, so the commands that the profile
adds aren't present in the session. In addition, the $PROFILE automatic variable isn't populated in
remote sessions.

To run a profile in a session, use the Invoke-Command cmdlet.

For example, the following command runs the CurrentUserCurrentHost profile from the local
computer in the session in $s .

<!-- p.899 -->

 Invoke-Command -Session $s -FilePath $PROFILE

The following command runs the CurrentUserCurrentHost profile from the remote computer in
the session in $s .

 PowerShell

 Invoke-Command -Session $s {
   . "$HOME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1"
 }

After you run this command, the commands that the profile adds to the session are available in
$s .

You can also use a startup script in a session configuration to run a profile in every remote
session that uses the session configuration.

For more information about PowerShell profiles, see about_Profiles. For more information about
session configurations, see Register-PSSessionConfiguration .

How does throttling work on
remote commands?
To help you manage the resources on your local computer, PowerShell includes a per-command
throttling feature that lets you limit the number of concurrent remote connections that are
established for each command.

The default is 32 concurrent connections, but you can use the ThrottleLimit parameter of the
cmdlets to set a custom throttle limit for particular commands.

The throttling feature applies to each command, not to the entire session or to the computer. If
you're running commands concurrently in several sessions or PSSessions, the number of
concurrent connections is the sum of the concurrent connections in all the sessions.

To find cmdlets with a ThrottleLimit parameter, type:

 Get-Help * -Parameter ThrottleLimit
 -or-
 Get-Command -ParameterName ThrottleLimit

<!-- p.900 -->

Is the output of remote commands different
from local output?
When you use PowerShell locally, you send and receive "live" .NET Framework objects; "live"
objects are objects that are associated with actual programs or system components. When you
invoke the methods or change the properties of live objects, the changes affect the actual
program or component. And, when the properties of a program or component change, the
properties of the object that represent them also change.

However, because most live objects can't be transmitted over the network, PowerShell serializes
the objects returned by remote commands. Serialization converts each object into Common
Language Infrastructure XML (CLIXML) data elements for transmission.

When PowerShell receives a serialized object, it converts the CLIXML into a deserialized object
type. The deserialized object is an accurate record of the properties of the object, but it's no
longer a live object. The deserialized object has no methods because they're no longer effective.

Typically, you can use deserialized objects just as you would use live objects, but you must be
aware of their limitations. Also, the objects returned by Invoke-Command have additional
properties that help you to determine the origin of the command.

Some object types, such as DirectoryInfo objects and GUIDs, are converted back into live objects
when they're received. These objects don't need any special handling or formatting.

For information about interpreting and formatting remote output, see about_Remote_Output.

Can I run background jobs remotely?
Yes. A PowerShell background job is a PowerShell command that runs asynchronously without
interacting with the session. When you start a background job, the command prompt returns
immediately. You can continue to work in the session while the job runs.

You can start a background job even while other commands are running because background
jobs always run asynchronously in a temporary session.

You can run background jobs on a local or remote computer. By default, a background job runs
on the local computer. However, you can use the AsJob parameter of the Invoke-Command cmdlet
to run any remote command as a background job. And, you can use Invoke-Command to run a
Start-Job command remotely.

<!-- p.901 -->

For more information about background jobs in PowerShell, see about_Jobs and
about_Remote_Jobs.

Can I run Windows programs on a
remote computer?
You can use PowerShell remote commands to run Windows-based programs on remote
computers. For example, you can run Shutdown.exe or Ipconfig.exe on a remote computer.

However, you can't use PowerShell commands to open the user interface for any program on a
remote computer.

When you start a Windows program on a remote computer, the PowerShell command prompt
doesn't return until the program is finished or until you press Ctrl + C to interrupt the
command. For example, if you run the ipconfig.exe program on a remote computer, the
command prompt doesn't return until ipconfig.exe is completed.

If you use remote commands to start a program that has a user interface, the program process
starts, but the user interface doesn't appear. The program is still running. The command prompt
doesn't return until you stop the program or you press Ctrl + C , which interrupts the command
and stops the process.

For example, if you use a PowerShell command to run Notepad on a remote computer, the
Notepad process starts on the remote computer, but the Notepad user interface doesn't appear.
To interrupt the command and restore the command prompt, press Ctrl + C .

Can I limit the commands that users can run
remotely on my computer?
Yes. Every remote session must use one of the session configurations on the remote computer.
You can manage the session configurations on your computer. You can set permissions on those
session configurations to limit who can run commands remotely on your computer. You can also
limit which commands they can run.

A session configuration configures the environment for the session. You can define the
configuration by using an assembly that implements a new configuration class or by using a
script that runs in the session. The configuration can determine the commands that are available
in the session. And, the configuration can include settings that protect the computer, such as

<!-- p.902 -->

settings that limit the amount of data that the session can receive remotely in a single object or
command. You can also specify a security descriptor that determines the permissions that are
required to use the configuration.

The Enable-PSRemoting cmdlet creates the default session configurations on your computer:
Microsoft.PowerShell, Microsoft.PowerShell.Workflow, and Microsoft.PowerShell32 (64-bit
operating systems only). Enable-PSRemoting sets the security descriptor for the configuration to
allow only members of the Administrators group on your computer to use them.

You can use the session configuration cmdlets to edit the default session configurations, to create
new session configurations, and to change the security descriptors of all the session
configurations.

Beginning in Windows PowerShell 3.0, the New-PSSessionConfigurationFile cmdlet lets you
create custom session configurations by using a text file. The file includes options for setting the
language mode and for specifying the cmdlets and modules that are available in sessions that
use the session configuration.

When users use the Invoke-Command , New-PSSession , or Enter-PSSession cmdlets, they can use
the ConfigurationName parameter to indicate the session configuration that's used for the
session. And, they can change the default configuration that their sessions use by changing the
value of the $PSSessionConfigurationName preference variable in the session.

For more information about session configurations, see the Help for the session configuration
cmdlets. To find the session configuration cmdlets, type:

 PowerShell

 Get-Command *PSSessionConfiguration

What are fan in and fan out configurations?
The most common PowerShell remoting scenario involving multiple computers is the one-to-
many configuration, in which one local computer (the administrator's computer) runs PowerShell
commands on numerous remote computers. This is known as the "fan-out" scenario.

However, in some enterprises, the configuration is many-to-one, where many client computers
connect to a single remote computer that's running PowerShell, such as a file server or a kiosk.
This is known as the "fan-in" configuration.

PowerShell remoting supports both fan-out and fan-in configurations.

<!-- p.903 -->

For the fan-out configuration, PowerShell uses the Web Services for Management (WS-
Management) protocol and the WinRM service that supports the Microsoft implementation of
WS-Management. When a local computer connects to a remote computer, WS-Management
establishes a connection and uses a plug-in for PowerShell to start the PowerShell host process
(Wsmprovhost.exe) on the remote computer. The user can specify an alternate port, an alternate
session configuration, and other features to customize the remote connection.

To support the "fan-in" configuration, PowerShell uses internet Information Services (IIS) to host
WS-Management, to load the PowerShell plug-in, and to start PowerShell. In this scenario,
instead of starting each PowerShell session in a separate process, all PowerShell sessions run in
the same host process.

IIS hosting and fan-in remote management aren't supported in Windows XP or in Windows
Server 2003.

In a fan-in configuration, the user can specify a connection URI and an HTTP endpoint, including
the transport, computer name, port, and application name. IIS forwards all the requests with a
specified application name to the application. The default is WS-Management, which can host
PowerShell.

You can also specify an authentication mechanism and prohibit or allow redirection from HTTP
and HTTPS endpoints.

Can I test remoting on a single computer not
in a domain?
Yes. PowerShell remoting is available even when the local computer isn't in a domain. You can use
the remoting features to connect to sessions and to create sessions on the same computer. The
features work the same as they do when you connect to a remote computer.

To run remote commands on a computer in a workgroup, change the following Windows settings
on the computer.

Caution: These settings affect all users on the system and they can make the system more
vulnerable to a malicious attack. Use caution when making these changes.

     Windows Vista, Windows 7, Windows 8:

     Create the following registry entry, and then set its value to 1: LocalAccountTokenFilterPolicy
     in HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

<!-- p.904 -->

     You can use the following PowerShell command to add this entry:

       PowerShell

       $parameters = @{
         Path='HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
         Name='LocalAccountTokenFilterPolicy'
         propertyType='DWord'
         Value=1
       }
       New-ItemProperty @parameters

     Windows Server 2003, Windows Server 2008, Windows Server 2012, Windows Server 2012
     R2:

     The default setting of the Network Access: Sharing and security model for local accounts
     policy is Classic . Verify the setting is set to Classic .

Can I run remote commands on a computer in
another domain?
Yes. Typically, the commands run without error. However, you might need to use the Credential
parameter with Invoke-Command , New-PSSession , or Enter-PSSession cmdlets. The credentials can
be required even when the current user is a member of the Administrators group on the local
and remote computers.

However, if the remote computer isn't in a domain that the local computer trusts, the remote
computer might not be able to authenticate the user's credentials.

To enable authentication, use the following command to add the remote computer to the list of
trusted hosts for the local computer in WinRM. Type the command at the PowerShell prompt.

 PowerShell

 Set-Item WSMan:\localhost\Client\TrustedHosts -Value <Remote-computer-name>

For example, to add the Server01 computer to the list of trusted hosts on the local computer,
type the following command at the PowerShell prompt:

 PowerShell

 Set-Item WSMan:\localhost\Client\TrustedHosts -Value Server01

<!-- p.905 -->

Does PowerShell support remoting over SSH?
Yes. For more information, see PowerShell remoting over SSH.

See also
about_Remote

about_Profiles

about_PSSessions

about_Remote_Jobs

about_Remote_Variables

Invoke-Command

New-PSSession

<!-- p.906 -->

Desired State Configuration (DSC)
Overview
DSC is a management platform that enables you to manage your IT and development
infrastructure with configuration as code.

There are four versions of DSC available:

      Microsoft DSC 3.0 is the new version of DSC. This version provides true cross-platform
      support. It is a standalone product that's not dependent on PowerShell, however, you can
      still use your existing PowerShell DSC resources.

      PowerShell DSC 3.0 (preview) is the version of DSC supported by the Azure Machine
      Configuration on Linux.

      PowerShell DSC 2.0 is the version of DSC that shipped in PowerShell 7.

      With the release of PowerShell 7.2, the PSDesiredStateConfiguration module is no longer
      included in the PowerShell package. Separating DSC into its own module allows us to
      invest and develop DSC independent of PowerShell and reduces the size of the
      PowerShell package. Users of DSC will enjoy the benefit of upgrading DSC without the
      need to upgrade PowerShell, accelerating the time to deployment of new DSC features.
      Users that want to continue using DSC v2 can download PSDesiredStateConfiguration
      2.0.5 from the PowerShell Gallery.

      PowerShell DSC 1.1 is the legacy version of DSC that originally shipped in Windows
      PowerShell 5.1.

For more information, see the Desired State Configuration overview article.

 Last updated on 01/29/2026

<!-- p.907 -->

The PowerShell Gallery
Article • 04/13/2023

The PowerShell Gallery    is the central repository for PowerShell content. In it, you can
find PowerShell scripts, modules containing PowerShell cmdlets and Desired State
Configuration (DSC) resources. Some of these packages are authored by Microsoft, and
others are authored by the PowerShell community.

The PowerShellGet module contains cmdlets for discovering, installing, updating, and
publishing PowerShell packages from the PowerShell Gallery. These packages can
contain artifacts such as Modules, DSC Resources, Role Capabilities, and Scripts. Make
sure you have the latest version of PowerShellGet installed.

The documentation for PowerShellGet and the PowerShell Gallery has been moved to a
new location so that we can manage the version-specific information separate from the
versions of PowerShell.

See the new documentation in PowerShellGet and the PowerShell Gallery.

<!-- p.908 -->

Community Update
A list of resources and a summary of new articles and community contributions.

  What's new in Docs?

  ｈ WHAT'S NEW
  2026 Updates

  2025 Updates

  2024 Updates

  2023 Updates

  2022 Updates

  2021 Updates

  2020 Updates

  Contributor Hall of Fame

  Learning resources

  ｄ TRAINING
  PowerShell 101

  Deep Dives

  PowerShell Learn modules

  ｑ VIDEO
  Microsoft Virtual Academy videos

  Jason Helmick's - The Show

  The PSConfEU Channel

  The PowerShell.org Channel

<!-- p.909 -->

Community resources

ｅ OVERVIEW
Community support

ａ DOWNLOAD
Digital art

ｉ REFERENCE
PowerShell 7 usage stats

Top contributors to PowerShell

<!-- p.910 -->

Getting support from the community
The PowerShell Community is a vibrant and active group of users. This article can help you get
connected with other member of the community.

The PowerShell community can file issues, bugs, or feature requests in our GitHub   repository.
If you have questions, you may find help from other members of the community in one of
these public forums:

     User Groups
     PowerShell Tech Community
     DSC Community
     PowerShell.org
     Stack Overflow
     r/PowerShell subreddit
     PowerShell Virtual User Group - join via:
        Slack
        Discord

For information about our support policy, see the PowerShell Support Lifecycle.

Last updated on 04/07/2026

<!-- p.911 -->

Community Contributor Hall of Fame
The PowerShell Community is a vibrant and collaborative group. We greatly appreciate all the
help and support we get from the community. You can be a contributor too. To learn how, read
our Contributor's Guide.

These GitHub users are the All-Time Top Community Contributors. These tables list the top
contributors and the total contributions from the community for each year.

Pull Requests merged
Pull Requests help us fix those issues and make the documentation better for everyone.

                                                                                     ﾉ   Expand table

 PRs Merged           2015   2016   2017   2018   2019   2020   2021   2022   2023   2024     2025   2026    To

 Community               8    189    452    468    321    165    101    134    117       95    160      28   22

 matt9ucci                           157     80     30      1      6                                          2

 nschonni                                    14    138     10                                                 1

 kiazhi                        25     79     12                                                               1

 alexandair                    57      7     24      2      1                            1

 sethvs                                1     42            20      1     10              6       2      1

 doctordns                      5     32     20      7      9      5             1

 surfingoldelephant                                                                             58      5

 ehmiiz                                                                  22     14

 ArieHein                                            1                                   8      25      1

 yecril71pl                                                21      3      3

 changeworld                                                              3                     22

 skycommand                            1      3      3      6             1      4       1       4

 Dan1el42                      20

 NReilingh                      2            13      3

 it-praktyk                                  16      1

 vors                          15      1

<!-- p.912 -->

 PRs Merged           2015   2016   2017   2018   2019   2020   2021   2022   2023   2024      2025   2026    To

 kvprasoon                      2      1      6      2      2      2

 purdo17                                     13

 k-takai                                      5      1      7

 bergmeister                           1      3      3      1      1      2      1         1

 markekraus                           11      1

 exchange12rocks                       7      3                    1                                     1

 hrxn                                                              2      2      2         5

 baardhermansen                                      2      1             1      2                       5

GitHub issues opened
GitHub issues help us identify errors and gaps in our documentation.

                                                                                     ﾉ    Expand table

 Issues Opened        2015   2016   2017   2018   2019   2020   2021   2022   2023   2024      2025   2026    To

 Community               6     52     96    213    567    563    367    244    291       243    182      74   28

 mklement0                            19     60     56     61     28      8     20        24      2            2

 ehmiiz                                                                  21     14

 iRon7                                                      2      2      2     10         8      8

 iSazonov                              1      4     10      8      4      3                1

 jszabo98                                     2     15      6      1             1         2             1

 surfingoldelephant                                                                        6     19      2

 kilasuit                                            3      2      1      4      1         4      5      3

 juvtib                                                    15      7

 peetrike                                     1             4      2      6      4         3      1

 doctordns                             5      3      5      7      1

 JustinGrote                                  1      3      6      1      1      3         2      3

 vexx32                                       3     11                    3

 rkeithhill                            1      2      2      2      3      1      2                1      1

 KirkMunro                                    7      7      1

<!-- p.913 -->

Issues Opened         2015       2016   2017   2018   2019   2020   2021   2022   2023   2024   2025   2026   To

alexandair                          9      4      2

clamb123                                                              14

tabad                                                                               11      2

ThomasNieto                                                     3             2      4      3

trollyanov                                                            11      1

LaurentDardenne                            3      2                           5      2

Liturgist                                                1      1      1      2      5      2

jsilverm                                                        8                    4

CarloToso                                                                           11

vors                         1      6      2      1

UberKluger                                                      1      7      2

matt9ucci                                  2      5                    2             1

o-l-a-v                                                  1             1             4      2      2

ArmaanMcleod                                                                         4      6

Last updated on 07/02/2026

<!-- p.914 -->

What's new in PowerShell Docs for 2026
This article lists notable changes made to docs each month and celebrates the contributions from
the community.

Help us make the documentation better for you. Read the Contributor's Guide to learn how to
get started.

2026-June
Updated content

     Release notes for monthly maintenance releases of PowerShell
     Major cleanup of PSScriptAnalyzer rules documentation, including refactoring the rules
     table. The rules table now shows which rules are always enabled, and which rules can be
     configured or disabled.

GitHub stats

     46 PRs merged (8 from Community)
     42 issues opened (11 from Community, 31 Spam)
     43 issues closed (12 from Community, 31 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

Special thanks to @ArieHein for another large PR to clean up 160 articles.

                                                                                 ﾉ   Expand table

 GitHub Id                                       PRs merged                  Issues opened

 ArieHein                                             1

 baardhermansen                                       4

 michael-hollingsworth                                1

 naffee                                               1

<!-- p.915 -->

 GitHub Id                                        PRs merged                 Issues opened

 PtJade-Ceramic                                        1                           1

 trashCode                                                                         2

2026-May
Updated content

     Updated release notes for minor releases of 7.4, 7.5, 7.6, and 7.7-preview.
     Update release notes for Microsoft.PowerShell.PSResourceGet v1.3.0-preview1
     Start work on PSScriptAnalyzer rule documentation refresh
        Standardizing the structure and formatting
        Add links to related documentation
        Grammar and style edits

GitHub stats

     30 PRs merged (4 from Community)
     44 issues opened (10 from Community, 33 Spam)
     46 issues closed (10 from Community, 33 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                                   ﾉ   Expand table

 GitHub Id                                   PRs merged                     Issues opened

 Anyplace7803                                      1

 exchange12rocks                                   1

 Gijsreyn                                          1

 jsuther1974                                       1

2026-April
New content

<!-- p.916 -->

     about_Error_Handling
        Special thanks to @SufficientDaikon for their hard work creating this new article and
        updating all related content.
     PowerShell 7.7-preview.1 release
        What's New in PowerShell 7.7 - PowerShell
        Now, you can select PowerShell 7.7 from the version selector to view documentation
        PowerShell 7.7 cmdlet reference.

Updated content

     Updated release notes for minor releases of 7.4, 7.5, and 7.6.

GitHub stats

     26 PRs merged (4 from Community)
     40 issues opened (8 from Community, 29 Spam)
     40 issues closed (9 from Community, 29 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                                 ﾉ   Expand table

 GitHub Id                                   PRs merged                   Issues opened

 Anyplace7803                                     1

 Gijsreyn                                         1

 MukundaKatta                                     1

 SufficientDaikon                                 1                             1

2026-March
New and updated content

     Updated release notes for PowerShell 7.6.0 GA release
     Major rework of setup articles to simplify the structure
        Moved Homebrew installation instructions for macOS to Alternate ways to install
        PowerShell

<!-- p.917 -->

      Updated PSScriptAnalyzer docs for v1.25 release including 6 new or updated rules
            AlignAssignmentStatement
            AvoidLongLines
            UseConsistentParameterSetName
            UseConsistentParametersKind
            UseConstrainedLanguageMode
            UseSingleValueFromPipelineParameter

GitHub stats

      40 PRs merged (3 from Community)
      56 issues opened (18 from Community, 33 Spam)
      47 issues closed (12 from Community, 33 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                               ﾉ   Expand table

 GitHub Id                                   PRs merged                  Issues opened

 baardhermansen                                   1

 derkallevombau                                   1

 dodexahedron                                     1

 SufficientDaikon                                                              3

 kilasuit                                                                      2

2026-February
New and updated content

      Update PSResourceGet release notes for RC3
      Other general maintenance updates

GitHub stats

      20 PRs merged (4 from Community)
      46 issues opened (13 from Community, 32 Spam)

<!-- p.918 -->

     45 issues closed (13 from Community, 32 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                               ﾉ   Expand table

 GitHub Id                                  PRs merged                  Issues opened

 manpritxelentor                                 1

 putku45                                         1

 sethvs                                          1

 umutKaracelebi                                  1

2026-January
New and updated content

     New article - Windows PowerShell update message
     Updated How to use the PowerShell documentation
     Updated AI Shell docs to reflect the deprecated status
     Updated PowerShellGet docs
          Install a package manager for PowerShell
          Bootstrapping NuGet
     Retired PowerShellGet 1.x docs - 41 articles removed

GitHub stats

     49 PRs merged (7 from Community)
     48 issues opened (17 from Community, 31 Spam)
     56 issues closed (24 from Community, 32 Spam)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                               ﾉ   Expand table

<!-- p.919 -->

GitHub Id                    PRs merged   Issues opened

surfingoldelephant               5             2

taku-nm                          1

alexvy86                         1

Last updated on 07/02/2026

<!-- p.920 -->

What's new in PowerShell Docs for 2025
This article lists notable changes made to docs each month and celebrates the contributions
from the community.

Help us make the documentation better for you. Read the Contributor's Guide to learn how to
get started.

2025-December
New content

     Troubleshoot PowerShell startup issues

Updated content

     Updated PSResourceGet docs for 1.2.0-preview5 release
          Use the Azure Artifacts Credential Provider with Azure Artifacts feeds
          Retired 26 obsolete reference articles for PowerShellGet proxy module
     Updated Invoke-WebRequest in PowerShell 5.1 for a breaking change introduced by a
     CVE security patch.

GitHub stats

     22 PRs merged (3 from Community)
     31 issues opened (16 from Community)
     30 issues closed (15 Community issues closed)

Top Community Contributors

The following people contributed to PowerShell docs this month by submitting pull requests or
filing issues. Thank you!

                                                                                   ﾉ   Expand table

 GitHub Id                                     PRs merged                   Issues opened

 surfingoldelephant                                  3                             4

 kborowinski                                         1

 aberus                                              1

 iRon7                                                                             3
