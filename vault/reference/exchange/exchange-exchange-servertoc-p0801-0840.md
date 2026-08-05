---
title: "Exchange Server — pages 801-840"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0801-0840
family: exchange
documentKind: "doc"
abstract: "Active Directory functional level isn't Windows Server 2003 or later [ForestLevelNotWin2003Native] 07/23/2025 Exchange Server 2016 Setup can't continue because the Active Directory forest functional level of the target forest isn't Windows Server 2003 native or later. Before you"
---

# Exchange Server — pages 801-840

<!-- p.801 -->

Active Directory functional level isn't
Windows Server 2003 or later
[ForestLevelNotWin2003Native]
07/23/2025

Exchange Server 2016 Setup can't continue because the Active Directory forest functional level
of the target forest isn't Windows Server 2003 native or later. Before you can install Exchange
2016, you must raise the forest functional level to Windows Server 2003 or later.

For information about how to raise the forest functional level, see Raise the Forest Functional
Level.

For more information about Active Directory functional levels, see the following topics:

     What are Active Directory Functional Levels?

     How Active Directory Functional Levels Work

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.802 -->

Cannot write to the Exchange organization
container [GlobalServerInstall]
07/23/2025

Exchange Setup can't continue because the user account doesn't have the permissions that are
required to write to the organization container in the Active Directory directory service.

Setup requires that the account you're using to install Exchange has permissions to create and
modify objects in Active Directory:

     If this is the first Exchange server in your organization, your account needs to be a
     member of the Schema Admins security group (to extend the schema) and the Enterprise
     Admins security group (to prepare Active Directory).

     After you prepare Active Directory for the version of Exchange that you're installing, your
     account needs to be a member of the Organization Management role group.

For more information, see Prepare Active Directory and domains for Exchange.

To resolve this issue, run Exchange set up again using an account that has the appropriate
permissions (grant permissions to the current account or use a different account).

  ） Important

  Cross-forest installation of Exchange isn't supported. Use an account in the Active
  Directory forest where you're installing Exchange.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.803 -->

Global updates required
[GlobalUpdateRequired]
07/23/2025

Exchange Setup can't continue because the user account doesn't have the permissions that are
required to write to the organization container in the Active Directory directory service.

Setup requires that the account you're using to install Exchange has permissions to create and
modify objects in Active Directory:

     If this is the first Exchange server in your organization, your account needs to be a
     member of the Schema Admins security group (to extend the schema) and the Enterprise
     Admins security group (to prepare Active Directory).

     After you prepare Active Directory for the version of Exchange that you're installing, your
     account needs to be a member of the Organization Management role group.

For more information, see Prepare Active Directory and domains for Exchange.

To resolve this issue, run Setup again using an account that has the appropriate permissions
(grant permissions to the current account or use a different account).

  ） Important

  Cross-forest installation of Exchange isn't supported. Use an account in the Active
  Directory forest where you're installing Exchange.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.804 -->

The Host record for the local computer
can't be found in the DNS database
[HostRecordMissing]
07/23/2025

Exchange Setup can't continue because the Host (A) record for this computer can't be found in
the DNS zone for the domain. Setup requires a valid A record for the server, and Exchange uses
email server A records to find the IP address of the next hop to send messages.

To resolve this issue:

     Verify that the local TCP/IP configuration points to the correct DNS server. For more
     information, see Configure TCP/IP settings.

     Use Nslookup.exe to verify that the Host (A) record exists on the DNS server. For more
     information, see To verify A resource records exist in DNS.

For information about DNS name resolution, troubleshooting, and A records, see the following:

     Troubleshooting DNS

     Managing resource records

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.805 -->

Installation on domain controllers is not
supported with Active Directory split
permissions
[InstallOnDCInADSplitPermissionMode]
07/23/2025

Exchange Setup detected that you're installing Exchange on an Active Directory domain
controller and one of the following conditions is true:

     The Exchange organization is already configured for Active Directory split permissions.

     You selected the Active Directory split permissions option in Exchange Setup.

Installing Exchange on domain controllers isn't supported when the Exchange organization is
configured for Active Directory split permissions. To install Exchange on a domain controller,
you need to configure the Exchange organization for Role Based Access Control (RBAC) split
permissions or shared permissions.

  ） Important

  We don't recommend installing Exchange on Active Directory domain controllers. For
  more information, see Installing Exchange on a domain controller is not recommended
  [WarningInstallExchangeRolesOnDomainController].

If you want to use Active Directory split permissions, you need install Exchange on a member
server.

For more information about split and shared permissions in Exchange 2013 or later, see the
following topics:

     Understanding Split Permissions

     Configure Exchange 2013 for Split Permissions

     Configure Exchange 2013 for Shared Permissions

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.806 -->

The current account isn't logged into an
Active Directory domain
[LoggedOntoDomain]
Article • 01/23/2024

Exchange Setup can't continue because it detected that the current account isn't logged on to
an Active Directory domain. You need to log in using an Active Directory account that has the
permissions required to install Exchange.

Setup requires that the account you're using to install Exchange has permissions to create and
modify objects in Active Directory:

      If this is the first Exchange server in your organizaiton, your account needs to be a
      member of the Schema Admins security group (to extend the schema) and the Enterprise
      Admins security group (to prepare Active Directory).

      After you prepare Active Directory for the version of Exchange that you're installing, your
      account needs to be a member of the Organization Management role group.

For more information, see Prepare Active Directory and domains for Exchange.

To resolve this issue, run Setup again using an account that has the appropriate permissions
(grant permissions to the current account or use a different account).

  ） Important

  Cross-forest installation of Exchange isn't supported. Use an account in the Active
  Directory forest where you're installing Exchange.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server      .

<!-- p.807 -->

The computer needs to be restarted before
Setup can continue [RebootPending]
Article • 01/23/2024

Exchange Setup can't continue because it detected a pending reboot to complete the
installation of other programs or Windows updates.

Why is this happening?
When programs and Windows updates are installed, they make changes to files that are stored
on your computer. Some programs or updates need to modify or replace files that are
currently in use. When this happens, you need to restart the computer before other programs
can be installed.

If the installation of a previous program or Windows update didn't complete successfully,
Windows and other programs might think a restart is required. You'll continue to see this error
each time you run Exchange Setup if this happens (the failed installation can't fix the condition
that indicates a restart is required).

How do I fix it?
Typically, you only need to restart the server to get past this error, but you might get this error
again after a restart (for example, additional program or Windows updates also require a
restart). Try restarting the server again.

If you see this error after you've restarted the server more than two or three times, try
reinstalling any programs or Windows updates that you've installed recently. This might allow a
failed installation to complete successfully.

If you still receive this error after multiple restarts and reinstalling recent programs or Windows
updates, we recommend that you contact Microsoft Customer Service and Support. They'll help
you find the reason why Windows and other programs think your computer needs to be
restarted. To contact Microsoft support, go to Support for business      and select Servers >
Exchange Server.

  Ｕ Caution

  Although it's tempting, we strongly recommend that you don't attempt to work around
  this issue by manually deleting or changing registry keys or values. Although you might fix

<!-- p.808 -->

  this issue now, manually modifying the registry might cause issues later on. This is
  especially important if the failed installation was a Windows update.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server   .

<!-- p.809 -->

The logged-on user is not a member of the
Schema Admins group
[SchemaUpdateRequired]
07/23/2025

Exchange Setup can't continue because the user account isn't a member of the Schema
Admins and Enterprise Admins security groups.

Setup requires that the account you're using to install Exchange has permissions to create and
modify objects in Active Directory:

     If this is the first Exchange server in your organization, your account needs to be a
     member of the Schema Admins security group (to extend the schema) and the Enterprise
     Admins security group (to prepare Active Directory).

     After you prepare Active Directory for the version of Exchange that you're installing, your
     account needs to be a member of the Organization Management role group.

For more information, see Prepare Active Directory and domains for Exchange.

To resolve this issue, run Exchange set up again using an account that has the appropriate
permissions (grant permissions to the current account or use a different account).

  ） Important

  Cross-forest installation of Exchange isn't supported. Use an account in the Active
  Directory forest where you're installing Exchange.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.810 -->

UCMA 4.0, Core Runtime not installed
[UcmaRedistMsi]
07/23/2025

Exchange 2016 Setup requires the Unified Communications Managed API 4.0 Runtime for
Unified Messaging (UM) services on the Mailbox server role. You need to install this update
before Exchange 2016 Setup can continue.

Download and install the 64-bit update from Unified Communications Managed API 4.0
Runtime      , and then click Retry on the Readiness Checks page in the Exchange 2016 Setup
wizard.

  ７ Note

  If the installation of this update requires a reboot, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.811 -->

Cannot remove mailbox database
[UnwillingToRemoveMailboxDatabase]
07/23/2025

Exchange Setup can't continue because it can't remove a user mailbox database from the local
server without incurring potential data loss.

Before Exchange Setup removes the Mailbox server role from a server, it checks for one of the
following conditions:

     All mailbox databases are removed from the server.
     Databases on the server don't contain active mailboxes. However, user mailboxes might
     still remain on the server.

To resolve this issue, do either of these steps:

     To preserve the mailboxes and their content, move the mailboxes to another server. For
     instructions, see Mailbox moves in Exchange Server.

     Disable the mailboxes if they're no longer required. For more information, see Disable-
     Mailbox.

     Remove the mailbox databases if they're no longer required. For instructions, see Manage
     mailbox databases in Exchange Server.

After you deal with the mailbox databases on the server, run Exchange Setup again.

     For more information about how to identify a mailbox in the database, see Get-Mailbox.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.812 -->

Installing Exchange on a domain controller
isn't recommended
[WarningInstallExchangeRolesOnDomainCo
ntroller]
07/23/2025

Exchange Server 2016 or Exchange 2019 Setup has detected that the target computer is an
Active Directory domain controller, and we don't recommend installing Exchange on domain
controllers.

If you install Exchange on a domain controller, be aware of the following issues:

     Configuring Exchange for Active Directory split permissions isn't supported. For more
     information about split permissions, see Understanding split permissions.

     The Exchange Trusted Subsystem universal security group (USG) is added to the Domain
     Admins group. This action grants all Exchange servers domain administrator rights in the
     domain.

     Exchange Server and Active Directory are both resource-intensive applications. There are
     performance implications when both applications are running on the same computer.

     The domain controller must be a global catalog server, but Exchange services might not
     start correctly on a global catalog server.

     System shutdown will take considerably longer if Exchange you didn't stop the Exchange
     services before you shut down or restart the server.

     Demoting the domain controller to a member server isn't supported.

     Running Exchange on a clustered node that's also an Active Directory domain controller
     isn't supported.

Therefore, we recommend that you install Exchange on a member server, not on a domain
controller.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.813 -->

KB2619234 update not installed
[Win7RpcHttpAssocCookieGuidUpdateNotI
nstalled]
07/23/2025

Exchange Server 2016 Setup can't continue because the local computer requires a software
update. You'll need to install this update before Exchange 2016 Setup can continue.

Exchange 2016 Setup requires a Windows Server update that allows Outlook Anywhere (RPC
over HTTP) to work correctly.

Download and install the 64-bit update from KB2619234      , and then click retry on the
Readiness Checks page.

  ７ Note

  If this update requires a reboot to complete installation, you'll need to exit Exchange 2016
  Setup, reboot, and then start Setup again.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.814 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedFrontendTransportFirstInstall]
07/23/2025

Exchange Setup can't continue because this is the first Exchange server in the organization, and
the first Exchange server needs to be installed by a member of the Enterprise Admins security
group (to create the Exchange Organization container and configure objects in it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

     A member of the Schema Admins group can extend the Active Directory schema using
     another computer in the domain before you install Exchange.

     Exchange Setup can extend the schema if your account is a member of the Schema
     Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.815 -->

No Exchange 2010 servers detected
[NoE14ServerWarning]
07/23/2025

Microsoft Exchange Server 2016 Setup displayed this warning because no Exchange 2010
servers exist in the organization.

  Ｕ Caution

  If you continue with Exchange Server 2016 installation, you won't be able to add Exchange
  2010 servers to the organization in the future.

Before deploying Exchange 2016, consider the following factors that may require you to deploy
Exchange 2010 servers prior to deploying Exchange 2016:

     Third-party or in-house developed applications: Applications developed for earlier
     versions of Exchange may not be compatible with Exchange 2016. You may need to
     maintain Exchange 2010 servers to support these applications.

     Coexistence or migration requirements: If you plan on migrating mailboxes into your
     organization, some solutions may require the use of Exchange 2010 servers.

If you decide that you need to deploy Exchange 2010 servers, you need to do so before you
deploy Exchange 2016. You need to prepare Active Directory for each Exchange version in the
following order:

   1. Exchange 2010

   2. Exchange 2013 (only required if you're planning to deploy Exchange 2013 at a later date)

   3. Exchange 2016

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.816 -->

The computer needs to be restarted before
Setup can continue
[PendingRebootWindowsComponents]
Article • 01/23/2024

Exchange Setup can't continue because it detected a pending reboot to complete the
installation of other programs or Windows updates.

Why is this happening?
When programs and Windows updates are installed, they make changes to files that are stored
on your computer. Some programs or updates need to modify or replace files that are
currently in use. When this happens, you need to restart the computer before other programs
can be installed.

If the installation of a previous program or Windows update didn't complete successfully,
Windows and other programs might think a restart is required. You'll continue to see this error
each time you run Exchange Setup if this happens (the failed installation can't fix the condition
that indicates a restart is required).

How do I fix it?
Typically, you only need to restart the server to get past this error, but you might get this error
again after a restart (for example, additional program or Windows updates also require a
restart). Try restarting the server again.

If you see this error after you've restarted the server more than two or three times, try
reinstalling any programs or Windows updates that you've installed recently. This might allow a
failed installation to complete successfully.

If you still receive this error after multiple restarts and reinstalling recent programs or Windows
updates, we recommend that you contact Microsoft Customer Service and Support. They'll help
you find the reason why Windows and other programs think your computer needs to be
restarted. To contact Microsoft support, go to Support for business      and select Servers >
Exchange Server.

  Ｕ Caution

  Although it's tempting, we strongly recommend that you don't attempt to work around
  this issue by manually deleting or changing registry keys or values. Although you might fix

<!-- p.817 -->

  this issue now, manually modifying the registry might cause issues later on. This is
  especially important if the failed installation was a Windows update.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server   .

<!-- p.818 -->

Can't install Exchange 2016 or later in a
forest that contains Exchange 2000 or
Exchange 2003 servers.
[Exchange2000or2003PresentInOrg]
Article • 05/09/2025

Exchange Setup can't continue because a version of Exchange that's too old for coexistence
with the version that you're installing was found in the Active Directory forest. Before you can
continue, you need to eliminate all unsupported versions of Exchange from your forest, which
might require that you to upgrade to an interim version of Exchange first.

The installation of Exchange Server 2016 or later can't continue because Setup found one or
more Exchange 2000 or Exchange 2003 servers in the Active Directory forest. Before you can
install Exchange 2016 or later in your organization, you need to remove all Exchange 2000 or
Exchange 2003 servers from the forest.

The upgrade path that you need to follow depends on your current version of Exchange. The
upgrade paths are described in the next section.

  ７ Note

  When you need to upgrade to an interim version of Exchange, you need to migrate all
  mailboxes, public folders and other components onto the interim version of Exchange
  before you decommission and remove the earlier Exchange servers.

Exchange Server 2019
                                                                                ﾉ   Expand table

 Current Exchange      Latest Exchange version for   Upgrade path summary
 version               coexistence

 Exchange 2000         Exchange 2007                 Exchange 2000 > Exchange 2007 > Exchange
                                                     2013 > Exchange 2019.

 Exchange 2003         Exchange 2010                 Exchange 2003 > Exchange 2010 > Exchange
                                                     2016 > Exchange 2019.

 Exchange 2007         Exchange 2013                 Exchange 2007 > Exchange 2013 > Exchange
                                                     2019.

<!-- p.819 -->

 Current Exchange    Latest Exchange version for   Upgrade path summary
 version             coexistence

 Exchange 2010       Exchange 2016                 Exchange 2010 > Exchange 2016 > Exchange
                                                   2019.

Exchange Server 2016
                                                                              ﾉ     Expand table

 Current Exchange    Latest Exchange version for   Upgrade path summary
 version             coexistence

 Exchange 2000       Exchange 2007                 Exchange 2000 > Exchange 2007 > Exchange
                                                   2013 > Exchange 2016.

 Exchange 2003       Exchange 2010                 Exchange 2003 > Exchange 2010 > Exchange
                                                   2016.

 Exchange 2007       Exchange 2013                 Exchange 2007 > Exchange 2013 > Exchange
                                                   2016.

 Exchange 2010       Exchange 2016                 Exchange 2010 > Exchange 2016.

When upgrading to Exchange 2013 or later, you can use the Exchange Deployment Assistant to
help complete your deployment. For more information, see Exchange Deployment Assistant .

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server         .

<!-- p.820 -->

An incompatible operating system was
found [ValidOSVersion]
07/23/2025

Microsoft Exchange Server 2016 Setup can't continue because it detected an incompatible
operating system. You must install a compatible operating system on this computer before you
install Exchange 2016. The following table shows the operating systems that are compatible
with Exchange 2016.

     ） Important

     Exchange 2016 doesn't support the Server Core installation option of Windows Server.

Supported operating systems for Exchange 2016:

                                                                                    ﾉ   Expand table

    Component                                 Requirement

    Mailbox and Edge Transport server roles   Windows Server 2016 Standard or Datacenter*
                                              Windows Server 2012 R2 Standard or Datacenter
                                              Windows Server 2012 Standard or Datacenter

    Management tools                          One of the following:
                                                   Windows Server 2016 Standard or Datacenter*
                                                   Windows Server 2012 R2 Standard or Datacenter
                                                   Windows Server 2012 Standard or Datacenter
                                                   64-bit edition of Windows 10
                                                   64-bit edition of Windows 8.1

*
    Requires Exchange Server 2016 Cumulative Update 3 or later.

For more information, see Exchange Server system requirements.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.821 -->

ExecutionPolicy GPO is defined
[PowerShellExecutionPolicyCheckSet]
07/23/2025

Exchange Setup can't continue because it detected that the ExecutionPolicy Group Policy
Object (GPO) defines one or both of the following policies:

     MachinePolicy

     UserPolicy

It doesn't matter how the policies have been defined; it only matters that they have been
defined.

Exchange Setup stops and disables the Windows Management Instrumentation (WMI) service.
When either of these policies are defined, the WMI service needs to be enabled to run a
Windows PowerShell script. If the policies are defined and the WMI service is stopped, Setup
will fail and the server will be left in an inconsistent state.

To allow Setup to continue, you need to temporarily remove any definition of MachinePolicy or
UserPolicy in the ExecutionPolicy GPO:

  PowerShell

  Set-ItemProperty -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell -Name
  ExecutionPolicy -Value ""

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.822 -->

Primary DNS Suffix is missing
[ms.exch.setupreadiness.FqdnMissing]
07/23/2025

Exchange Setup can't continue because the primary DNS suffix (for example, contoso.com) isn't
configured on the target server. Typically, you'll encounter this error when you're trying to
install the Edge Transport server role.

To resolve this issue, add a primary DNS suffix on the computer and then run Setup again.

   1. Replace <Value> with the DNS suffix you want to use (for example, contoso.com), and run
     the following command in Windows PowerShell on the target server:

  PowerShell

  Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters -
  Name 'NV Domain' -Value <Value>

   2. Restart the computer and run Setup again.

  ） Important

  Changing the computer name or primary DNS suffix after you install Exchange isn't
  supported.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.823 -->

MAPI over HTTP isn't enabled
[WarnMapiHttpNotEnabled]
07/23/2025

Microsoft Exchange Server 2016 Setup displayed this warning because there are servers
running Exchange 2016 or later in this organization and MAPI over HTTP isn't enabled.

MAPI over HTTP is the preferred Outlook connectivity method when connecting to servers
running Exchange 2016 or later. MAPI over HTTP improves the reliability and stability of the
Outlook and Exchange connections, by moving the transport layer to the industry standard
HTTP model. This allows a higher level of visibility of transport errors and enhanced
recoverability. Additional functionality includes support for an explicit pause-and-resume
function. This enables supported clients to change networks or resume from hibernation while
maintaining the same server context.

Exchange Setup won't automatically enable MAPI over HTTP to avoid making unexpected
changes to client connectivity. However, we recommend that you enable MAPI over HTTP
instantly to receive the benefits it provides.

For more information about MAPI over HTTP and how to enable it, see MAPI over HTTP in
Exchange Server.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.824 -->

Can't install Exchange 2016 or later in a
forest that contains Exchange 2007
[E16E12CoexistenceMinVersionRequirement
]
07/23/2025

The installation of Exchange Server 2016 or later can't continue because Setup found one or
more Exchange 2007 servers in the Active Directory forest. Before you can install Exchange
2016 or later in your organization, you need to remove all Exchange 2007 servers from the
forest.

The upgrade steps from Exchange 2007 are:

   1. Install Exchange 2013 into your Exchange 2007 organization.

   2. Configure Exchange 2013 and Exchange 2007 coexistence.

   3. Migrate Exchange 2007 mailboxes, public folders, and other components to Exchange
      2013.

   4. Decommission and remove all Exchange 2007 servers.

   5. Install Exchange 2016 or Exchange 2019 into your Exchange 2013 organization.

   6. Configure coexistence with Exchange 2013.

   7. Migrate Exchange 2013 mailboxes, public folders, and other components to Exchange
      2016 or Exchange 2019.

   8. Decommission and remove all Exchange 2013 servers.

The coexistence (and therefore, upgrade) options for Exchange are described in the following
table:

                                                                                 ﾉ   Expand table

 Current Exchange version              Latest Exchange version for coexistence

 Exchange 2000                         Exchange 2007

 Exchange 2003                         Exchange 2010

 Exchange 2007                         Exchange 2013

<!-- p.825 -->

 Current Exchange version             Latest Exchange version for coexistence

 Exchange 2010                        Exchange 2016

 Exchange 2013                        Exchange 2019

When upgrading to Exchange 2013 or later, you can use the Exchange Deployment Assistant to
help complete your deployment. For more information, see Exchange Deployment Assistant .

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.826 -->

Exchange 2010 SP3 RU11 or later is required
for coexistence with Exchange 2016
[E16E14CoexistenceMinVersionRequirement
]
Article • 05/09/2025

The installation of Exchange Server 2016 can't continue because Setup found one or more
Exchange 2010 servers that aren't running the minimum required version of Exchange 2010.
Before you can install Exchange 2016 in your organization, all Exchange 2010 servers in the
forest need to be running Exchange 2010 Service Pack 3 (SP3) and Update Rollup 11 (RU11) or
later. This requirement includes Exchange 2010 Edge Transport servers.

  ） Important

  After you upgrade your Exchange 2010 Edge Transport servers to Exchange 2010 SP3
  RU11 or later, you need to re-create the Edge subscription between your Exchange
  organization and each Edge Transport server (to update the Edge Transport server's
  Exchange version in Active Directory). For more information about re-creating Edge
  subscriptions in Exchange 2010, see Managing Edge Subscriptions.

<!-- p.827 -->

Exchange 2013 CU10 or later is required for
coexistence with Exchange 2016 or later
[E16E15CoexistenceMinVersionRequirement
]
Article • 01/23/2024

The installation of Exchange Server 2016 or later can't continue because Setup found one or
more Exchange 2013 servers that aren't running the minimum required version of Exchange
2013. Before you can install Exchange 2016 or later in your organization, all Exchange 2013
servers in the forest need to be running Exchange 2013 Cumulative Update 10 (CU10) or later.
This requirement includes Exchange 2013 Edge Transport servers.

  ） Important

  After you upgrade your Exchange 2013 Edge Transport servers to Exchange 2013 CU10 or
  later, you need to re-create the Edge subscription between your Exchange organization
  and each Edge Transport server (to update the Edge Transport server's Exchange version in
  Active Directory). For more information about re-creating Edge subscriptions in Exchange
  2013, see Manage Edge Subscriptions.

<!-- p.828 -->

Exchange 2013 servers can't coexist with
Exchange Server 2019 CU15 or later
[E19E15CoexistenceRequirement]
Article • 09/24/2024

The installation of Exchange Server 2019 CU15 or later can't continue because Setup found one
or more Exchange 2013 servers. Before you can install Exchange 2019 CU15 or later in your
organization, all Exchange 2013 servers in the forest must be removed.

More information can be found in the Upgrading your organization from current versions to
Exchange Server SE     blog post.

<!-- p.829 -->

Windows component Web-Metabase isn't
installed on this computer [ms-exch-
setupreadiness-
LonghornIIS6MetabaseNotInstalled]
Article • 01/16/2025

Microsoft Exchange Server Setup displayed this error because the Web-Metabase Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue.

To install the feature on a Windows Server, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Web-Metabase

To install the feature on a Windows Client, run the following PowerShell command:

  PowerShell

  Enable-WindowsOptionalFeature -Online -FeatureName IIS-Metabase -All

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.830 -->

Windows component Web-Mgmt-Console
isn't installed on this computer [ms-exch-
setupreadiness-
LonghornIIS7ManagementConsoleInstalled
]
Article • 01/16/2025

Microsoft Exchange Server Setup displayed this error because the Web-Mgmt-Console Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue.

To install the feature on a Windows Server, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Web-Mgmt-Console

To install the feature on a Windows Client, run the following PowerShell command:

  PowerShell

  Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementConsole -All

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.831 -->

Visual C++ Redistributable Package for
Visual Studio 2012 isn't installed on this
computer [ms-exch-setupreadiness-
VC2012RedistDependencyRequirement]
Article • 01/16/2025

Microsoft Exchange Server Setup displayed this error because the Visual C++ Redistributable
Package for Visual Studio 2012 isn't installed on the computer.

You must install the missing component before Microsoft Exchange Server Setup can continue.

Download Visual C++ Redistributable Package for Visual Studio 2012

For a complete list of required Windows features and updates and components, check out
Exchange Server prerequisites.

<!-- p.832 -->

Visual C++ Redistributable Package for
Visual Studio 2013 isn't installed on this
computer [ms-exch-setupreadiness-
VC2013RedistDependencyRequirement]
Article • 01/16/2025

Microsoft Exchange Server Setup displayed this error because the Visual C++ Redistributable
Package for Visual Studio 2013 isn't installed on the computer.

You must install the missing component before Microsoft Exchange Server Setup can continue.

Download Visual C++ Redistributable Package for Visual Studio 2013

For a complete list of required Windows features and updates and components, check out
Exchange Server prerequisites.

<!-- p.833 -->

Windows component NET-Framework-45-
Core isn't installed on this computer
[NETFramework45CoreNotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the NET-Framework-45-Core
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature NET-Framework-45-Core

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.834 -->

Windows component NET-Framework-45-
ASPNET isn't installed on this computer
[NETFramework45ASPNETNotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the NET-Framework-45-ASPNET
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature NET-Framework-45-ASPNET

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.835 -->

Windows component NET-WCF-HTTP-
Activation45 isn't installed on this
computer
[NETWCFHTTPActivation45NotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the NET-WCF-HTTP-Activation45
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature NET-WCF-HTTP-Activation45

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.836 -->

Windows component NET-WCF-Pipe-
Activation45 isn't installed on this
computer
[NETWCFPipeActivation45NotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the NET-WCF-Pipe-Activation45
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature NET-WCF-Pipe-Activation45

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.837 -->

Windows component NET-WCF-TCP-
PortSharing45 isn't installed on this
computer
[NETWCFTCPPortSharing45NotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the NET-WCF-TCP-PortSharing45
Windows component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature NET-WCF-TCP-PortSharing45

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.838 -->

Windows component Web-Net-Ext45 isn't
installed on this computer
[WebNetExt45NotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the Web-Net-Ext45 Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Web-Net-Ext45

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.839 -->

Windows component Web-ISAPI-Ext isn't
installed on this computer
[WebISAPIExtNotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the Web-ISAPI-Ext Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Web-ISAPI-Ext

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.

<!-- p.840 -->

Windows component Web-ASP-NET45 isn't
installed on this computer
[WebASPNET45NotInstalled]
Article • 09/16/2024

Microsoft Exchange Server Setup displayed this error because the Web-ASP-NET45 Windows
component isn't installed on the computer.

You must install the missing feature before Microsoft Exchange Server Setup can continue. To
install the feature, run the following PowerShell command:

  PowerShell

  Install-WindowsFeature Web-ASP-NET45

For a complete list of required Windows features and updates, check out Exchange Server
prerequisites.
