---
title: "Exchange Server — pages 481-520"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0481-0520
family: exchange
documentKind: "doc"
abstract: "The Exchange Install Domain Servers group is added to the Exchange Servers USG in the root domain. Permissions are assigned at the domain level for the Exchange Servers USG and the Organization Management USG. The objectVersion property in the Microsoft Exchange System Objects c"
---

# Exchange Server — pages 481-520

<!-- p.481 -->

The Exchange Install Domain Servers group is added to the Exchange Servers USG in the
root domain.

Permissions are assigned at the domain level for the Exchange Servers USG and the
Organization Management USG.

The objectVersion property in the Microsoft Exchange System Objects container under
DC=<root domain> is set. To verify that the Active Directory domains were successfully
prepared, you can check the value stored in this attribute. For more information, see
Exchange Active Directory versions.

<!-- p.482 -->

Prepare Active Directory and domains for
Exchange Server
06/11/2025

APPLIES TO:        2016    2019      Subscription Edition

Exchange uses Active Directory to store information about mailboxes and the configuration of
Exchange servers in the organization. Before you install Exchange Server, you need to prepare
your Active Directory forest and its domains for the new version of Exchange. There are two
ways to do this:

     Let the Exchange Setup wizard do it for you: If you don't have a large Active Directory
     deployment, and you don't have a separate team that manages Active Directory, we
     recommend using the Setup wizard. Your account needs to be a member of both the
     Schema Admins and Enterprise Admins security groups. For more information about how
     to use the Setup wizard, check out Install Exchange Mailbox servers using the Setup
     wizard.

  ） Important

  If Exchange is deployed in a multi-site Active Directory environment and is not in the same
  site as the domain controller that holds the Schema Master role, you cannot prepare
  Active Directory using the wizard. Instead, follow Step 1 and Step 2 in this topic.

     Follow the steps in this topic: If you have a large Active Directory deployment, or if a
     separate team manages Active Directory, this topic is for you. Following the steps in this
     topic gives you much more control over each stage of preparation, and who can do each
     step. For example, Exchange administrators might not have the required permissions to
     extend the Active Directory schema.

For details on new schema classes and attributes that Exchange adds to Active Directory,
including those made by Cumulative Updates (CUs), see Active Directory schema changes in
Exchange Server.

For details about what's happening when Active Directory is being prepared for Exchange, see
What changes in Active Directory when Exchange is installed?.

If you aren't familiar with Active Directory forests or domains, check out Active Directory
Domain Services Overview.

<!-- p.483 -->

What do you need to know before you begin?
   Estimated time to complete: 10-15 minutes or more (not including Active Directory
   replication), depending on organization size and the number of child domains.

   The computer that you use for these procedures needs to meet the system requirements
   for Exchange.

   Verify that your Active Directory meets the requirements for Exchange:

      Exchange 2019 and SE: Exchange 2019 and SE Network and directory servers.

      Exchange 2016: Exchange 2016 Network and directory servers.

   If your organization has multiple Active Directory domains, we recommend the following
   approach:
      Do these procedures in an Active Directory site that contains an Active Directory server
      from every domain.
      Install the first Exchange server in an Active Directory site that contains a writeable
      global catalog server from every domain.

   The computer that you use for all procedures in this topic requires access to Setup.exe in
   the Exchange installation files:

      1. Download the latest version of Exchange. For more information, see Updates for
          Exchange Server.
      2. In File Explorer, right-click on the Exchange ISO image file that you downloaded, and
          then select Mount. Note the virtual DVD drive letter that's assigned.
      3. Open a Windows Command Prompt window. For example:
            Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then
            press OK.
            Press Start. In the Search box, type Command Prompt, then in the list of results,
            select Command Prompt.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server .

 ７ Note

<!-- p.484 -->

       The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
       the September 2021 Cumulative Updates (CUs). You now must use either
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
       installs.

       The examples below use the /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
       switch. It's up to you to change the switch to
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

Step 1: Extend the Active Directory schema

   Tip

  If you don't have a separate team that manages your Active Directory schema, you can
  skip this step and go directly to Step 2: Prepare Active Directory. If you don't extend the
  schema in this step, the /PrepareAd command in Step 2 will automatically extend the
  schema for you. If you skip this step, the requirements will also apply to Step 2.

When you extend the Active Directory schema for Exchange, the following requirements apply:

     Your account needs to be a member of the Schema Admins and Enterprise Admins
     security groups. If you have multiple Active Directory forests, make sure you're logged
     into the right one.

     The computer needs to be a member of the same Active Directory domain and site as the
     schema master.

     If you use the /DomainController:<DomainControllerFQDN> switch, you need to specify
     the domain controller that's the schema master.

     The only supported way to extend the schema for Exchange is to use Setup.exe with
     /PrepareSchema, /PrepareAD, or the Exchange Setup wizard. Other ways of extending the
     schema aren't supported.

To extend the schema for Exchange, run the following command in a Windows Command
Prompt window:

  Console

<!-- p.485 -->

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareSchema

For example, if the Exchange installation files are available on drive E:, run the following
command:

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareSchema

  ７ Note

  When you run this command, a prerequisite check is performed that will tell you which
  requirements are missing.

After Setup finishes extending the schema, you'll need to wait while Active Directory replicates
the changes to all of your domain controllers before you proceed. To check the progress of the
replication, you can use the repadmin tool in Windows Server. For more information about how
to use the repadmin tool, see Repadmin.

Step 2: Prepare Active Directory
After the Active Directory schema has been extended, you can prepare other parts of Active
Directory for Exchange. During this step, Exchange will create containers, objects, and other
items in Active Directory to store information. The collection of the Exchange containers,
objects, attributes, and so on, is called the Exchange organization.

When you prepare Active Directory for Exchange, the following requirements apply:

     Your account needs to be a member of the Enterprise Admins security group. If you
     skipped Step 1 because you want the /PrepareAD command to extend the schema, the
     account also needs to be a member of the Schema Admins security group.
     The computer needs to be a member of the same Active Directory domain and site as the
     schema master, and must be able to contact all of the domains in the forest on TCP port
     389.
     Wait until Active Directory has finished replicating the schema changes from Step 1 to all
     domain controllers before you try to prepare Active Directory.
     If you install a new Exchange organization you need to select a name for the Exchange
     organization. The organization name is used internally by Exchange, isn't typically seen by

<!-- p.486 -->

     users, doesn't affect the functionality of Exchange, and doesn't determine what you can
     use for email addresses.
        The organization name can't contain more than 64 characters, and can't be blank.
        Valid characters are A to Z, a to z, 0 to 9, hyphen or dash (-), and space, but leading or
        trailing spaces aren't allowed.
        You can't change the organization name after it's set.
     If you want to enable Active Directory split permissions, you must also provide the
      /ActiveDirectorySplitPermissions:true parameter as described here.

To prepare Active Directory for Exchange, run the following command in a Windows Command
Prompt window:

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD /OrganizationName:"
  <Organization name>"

This example uses the Exchange installation files on drive E: and names the Exchange
organization "Contoso Corporation".

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD
  /OrganizationName:"Contoso Corporation"

  ） Important

  If you have a hybrid deployment configured between your on-premises organization and
  Exchange Online, add the /TenantOrganizationConfig switch to the command.

  For existing environments, you don't need to use the /OrganizationName and
  /TenantOrganizationConfig switches.

As in Step 1, you'll need to wait while Active Directory replicates the changes from this step to
all of your domain controllers before you proceed, and you can use the repadmin tool to check
the progress of the replication.

Step 3: Prepare Active Directory domains

   Tip

<!-- p.487 -->

  If you have only one domain, you can skip this step because the /PrepareAD command in
  Step 2 has already prepared the domain for you.

The final step is to prepare the Active Directory domain where Exchange servers will be
installed or where mail-enabled users will be located. This step creates additional containers
and security groups, and sets the permissions so Exchange can access them.

If you have multiple domains in your Active Directory forest, you have the following choices in
how to prepare them:

     Prepare all domains in the Active Directory forest
     Choose the Active Directory domains to prepare

Regardless of the method you choose, wait until Active Directory has finished replicating the
changes from Step 2 to all domain controllers before you proceed. Otherwise, you might get
an error when you try to prepare the domains.

Prepare all domains in the Active Directory forest
When you prepare all domains in the Active Directory forest for Exchange, your account needs
to be a member of the Enterprise Admins security group.

To prepare all domains in your Active Directory forest, run the following command in a
Windows Command Prompt window:

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAllDomains

For example, if the Exchange installation files are available on drive E:, run the following
command:

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
  /PrepareAllDomains

Choose the Active Directory domains to prepare

   Tip

<!-- p.488 -->

  You don't need to do this step in the domain where you ran the /PrepareAD command in
  Step 2, because the /PrepareAD command has automatically prepared that domain for
  you.

When you prepare specific domains in your Active Directory forest, the following requirements
apply:

     You need to prepare every domain where an Exchange server will be installed.
     You need to prepare any domain that will contain mail-enabled users, even if the domain
     won't contain any Exchange servers.
     Your account needs to be a member of the Domain Admins group in the domain that you
     want to prepare.
     If the domain that you want to prepare was created after you ran /PrepareAD in Step 2,
     your account also needs to be a member of the Organization Management role group in
     Exchange.

To prepare a specific domain in your Active Directory forest, run the following command in a
Windows Command Prompt window:

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareDomain[:<DomainFQDN>]

  ７ Note

         If the computer is a member of the domain that you want to prepare, you can use
         the /PrepareDomain switch by itself. Otherwise, you need to specify the FQDN of the
         domain.

         You need to run this command for each Active Directory domain where you'll install
         an Exchange server or where mail-enabled users will be located.

This example uses the Exchange installation files on drive E: to prepare the
engineering.corp.contoso.com domain:

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
  /PrepareDomain:engineering.corp.contoso.com

<!-- p.489 -->

This is the same example, but run on a computer that's a member of the
engineering.corp.contoso.com domain:

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareDomain

How do you know this worked?
To verify that you successfully prepared Active Directory and domains for Exchange, use any of
the following steps:

     Use ADSI Edit and the information from the tables in the next section to verify that the
     specified objects have the correct values for the release of Exchange that you're installing.
     To learn more about ADSI Edit, see ADSI Edit (adsiedit.msc).

        Ｕ Caution

        Never change values in ADSI Edit unless you're told to do so by Microsoft Customer
        Service and Support. Changing values in ADSI Edit can cause irreparable damage to
        your Exchange organization and Active Directory.

     Check the Exchange setup log to verify that Active Directory preparation has completed
     successfully. For more information, see Verify an Exchange installation. Note that you
     can't use the Get-ExchangeServer cmdlet as described in the topic until you've
     completed the installation of at least one Exchange Mailbox server in an Active Directory
     site.

You can use https://aka.ms/ExSetupAssist     if you encounter failure in running the AD
Preparation commands.

Exchange Active Directory versions
The tables in the following sections contain the Exchange objects in Active Directory that are
updated each time you install a new version of Exchange (a new installation or a CU). You can
compare the object versions you see with the values in the tables to verify that Exchange
successfully updated Active Directory during the installation.

     rangeUpper is located in the Schema naming context in the properties of the ms-Exch-
     Schema-Version-Pt container.

<!-- p.490 -->

    objectVersion (Default) is the objectVersion attribute located in the Default naming
    context in the properties of the Microsoft Exchange System Objects container.
    objectVersion (Configuration) is the objectVersion attribute located in the Configuration
    naming context in Services > Microsoft Exchange in the properties of the <Your
    Exchange Organization Name> container.

Exchange SE Active Directory versions

                                                                                 ﾉ    Expand table

Exchange SE version                 rangeUpper           objectVersion          objectVersion
                                                           (Default)           (Configuration)

Exchange SE RTM                       17003                 13243                    16763

Exchange 2019 Active Directory versions

                                                                                 ﾉ    Expand table

Exchange 2019 version                         rangeUpper       objectVersion      objectVersion
                                                                 (Default)       (Configuration)

Exchange 2019 CU15                               17003              13243             16763

Exchange 2019 CU14                               17003              13243             16762

Exchange 2019 CU13                               17003              13243             16761

Exchange 2019 CU12                               17003              13243             16760

Exchange 2019 CU11 with KB5014260                17003              13243             16759

Exchange 2019 CU11                               17003              13242             16759

Exchange 2019 CU10                               17003              13241             16758

Exchange 2019 CU9                                17002              13240             16757

Exchange 2019 CU8                                17002              13239             16756

Exchange 2019 CU7                                17001              13238             16755

Exchange 2019 CU6                                17001              13237             16754

Exchange 2019 CU5                                17001              13237             16754

Exchange 2019 CU4                                17001              13237             16754

<!-- p.491 -->

Exchange 2019 version               rangeUpper   objectVersion    objectVersion
                                                   (Default)     (Configuration)

Exchange 2019 CU3                     17001         13237            16754

Exchange 2019 CU2                     17001         13237            16754

Exchange 2019 CU1                     17000         13236            16752

Exchange 2019 RTM                     17000         13236            16751

Exchange 2019 Preview                 15332         13236            16213

Exchange 2016 Active Directory versions

                                                                 ﾉ   Expand table

Exchange 2016 version               rangeUpper   objectVersion    objectVersion
                                                   (Default)     (Configuration)

Exchange 2016 CU23                    15334         13243            16223

Exchange 2016 CU22 with KB5014260     15334         13243            16222

Exchange 2016 CU22                    15334         13242            16222

Exchange 2016 CU21                    15334         13241            16221

Exchange 2016 CU20                    15333         13240            16220

Exchange 2016 CU19                    15333         13239            16219

Exchange 2016 CU18                    15332         13238            16218

Exchange 2016 CU17                    15332         13237            16217

Exchange 2016 CU16                    15332         13237            16217

Exchange 2016 CU15                    15332         13237            16217

Exchange 2016 CU14                    15332         13237            16217

Exchange 2016 CU13                    15332         13237            16217

Exchange 2016 CU12                    15332         13236            16215

Exchange 2016 CU11                    15332         13236            16214

Exchange 2016 CU10                    15332         13236            16213

Exchange 2016 CU9                     15332         13236            16213

<!-- p.492 -->

Exchange 2016 version   rangeUpper   objectVersion    objectVersion
                                       (Default)     (Configuration)

Exchange 2016 CU8         15332         13236            16213

Exchange 2016 CU7         15332         13236            16213

Exchange 2016 CU6         15330         13236            16213

Exchange 2016 CU5         15326         13236            16213

Exchange 2016 CU4         15326         13236            16213

Exchange 2016 CU3         15326         13236            16212

Exchange 2016 CU2         15325         13236            16212

Exchange 2016 CU1         15323         13236            16211

Exchange 2016 RTM         15317         13236            16210

Exchange 2016 Preview     15317         13236            16041

<!-- p.493 -->

Deploy new installations of Exchange
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Before you begin your installation of Exchange Server, see Planning and deployment for
important planning information, and information about system requirements and prerequisites.

The following topics provide information about deploying new installations of Exchange 2019
in your organization:

Install Exchange Mailbox servers using the Setup wizard

Install Exchange using unattended mode

Install Exchange Edge Transport servers using the Setup wizard

Delegate the installation of Exchange servers

Exchange dev/test environment in Azure

After you've completed your installation, see Exchange post-installation tasks.

<!-- p.494 -->

Install Exchange Mailbox servers using the
Setup wizard
07/01/2025

APPLIES TO:      2016       2019     Subscription Edition

Before you install an Exchange Server Mailbox server, verify the following prerequisites:

     Verify the network, computer hardware, operating system, and software requirements at:
     Exchange Server system requirements and Exchange Server prerequisites.

     The target server must be a member of an Active Directory domain.

     The account that you use to install Exchange requires the following permissions*:

        Enterprise Admins group membership: Required if this is the first Exchange server in
        the organization.

        Schema Admins group membership: Required if you haven't previously extended the
        Active Directory schema or prepared Active Directory for Exchange Server.

        Exchange Organization Management role group membership: Required if you've
        already prepared the Active Directory domain that will contain the Exchange server, or
        if other Exchange servers already exist in the organization.

     * Members of the Delegated Setup role group can install Exchange on servers that have

     already been provisioned in Active Directory by an Exchange administrator. For more
     information, see Delegate the installation of Exchange servers.

     Verify that you've read the release notes at Release notes for Exchange Server.

For more information about planning and deploying Exchange, see Planning and deployment
for Exchange Server.

To install the Edge Transport role on a computer, see Install Exchange Edge Transport servers
using the Setup wizard. Note that you can't install the Edge Transport role on a Mailbox server.

What do you need to know before you begin?
     Estimated time to complete: 60 minutes

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

<!-- p.495 -->

 Ｕ Caution

 After you install Exchange on a server, you must not change the server name. Renaming a
 server after you've installed an Exchange server role is not supported.

Install the Exchange Mailbox server role
 1. Download the latest version of version of Exchange. For more information, see Updates
    for Exchange Server.

 2. In File Explorer, right-click on the Exchange ISO image file that you downloaded, and then
    select Mount. In the resulting virtual DVD drive that appears, start Exchange Setup by
    double-clicking Setup.exe .

 3. The Exchange Server Setup wizard opens. On the Check for Updates? page, choose one
    of the following options, and then click Next to continue:

         Connect to the Internet and check for updates: We recommend this option, which
         searches for updates to the version of Exchange that you're currently installing (it
         doesn't detect newer Cumulative Updates). This option takes you to the
         Downloading Updates page that searches for updates. Click Next to continue.

         Don't check for updates right now

<!-- p.496 -->

4. The Copying Files page shows the progress of copying files to the local hard drive.
  Typically, the files are copied to %WinDir%\Temp\ExchangeSetup , but you can confirm the
  location in the Exchange Setup log at C:\ExchangeSetupLogs\ExchangeSetup.log .

<!-- p.497 -->

5. On the Introduction page, we recommend that you visit the Exchange Server deployment
  planning links if you haven't already reviewed them. Click Next to continue.

<!-- p.498 -->

6. On the License Agreement page, review the software license terms, select I accept the
  terms in the license agreement, and then click Next to continue.

7. On the Recommended Settings page, choose one of the following settings:

       Use recommended settings: Exchange automatically sends error reports and
       information about your computer hardware and how you use Exchange to
       Microsoft. For information about what's sent to Microsoft and how it's used, click ?
       or the help links on the page.

       Don't use recommended settings: These settings are disabled, but you can enable
       them at any time after Setup completes.

  Click Next to continue.

<!-- p.499 -->

8. On the Server Role Selection page, configure the following options:

       Mailbox role: Select this option, which also automatically installs the Management
       Tools.

       Automatically install Windows Server roles and features that are required to
       install Exchange: Select this option to have the Setup wizard install the required
       Windows prerequisites. You might need to reboot the computer to complete the
       installation of some Windows features. If you don't select this option, you need to
       install the Windows features manually.

  Note: Selecting this option installs only the Windows features that are required by
  Exchange. You need to install other prerequisites manually. For more information, see
  Exchange Server prerequisites.

  Click Next to continue.

<!-- p.500 -->

9. On the Installation Space and Location page, either accept the default installation
  location ( C:\Program Files\Microsoft\Exchange Server\V15 ), or click Browse to choose a
  new location. Make sure that you have enough disk space available in the location where
  you want to install Exchange. Click Next to continue.

<!-- p.501 -->

10. If this is the first Exchange server in your organization and you haven't already done the
   steps in Prepare Active Directory and domains for Exchange, you arrive on the Exchange
   Organization page. On this page, configure the following settings:

         Specify the name for this Exchange organization: The default value is First
         Organization, but you typically use the company name for this value. The
         organization name is used internally by Exchange, isn't typically seen by users,
         doesn't affect the functionality of Exchange, and doesn't determine what you can
         use for email addresses.

            The organization name can't contain more than 64 characters, and can't be blank.

            Valid characters are A to Z, a to z, 0 to 9, hyphen or dash (-), and space, but
            leading or trailing spaces aren't allowed.

            You can't change the organization name after it's set.

         Apply Active Directory split permission security model to the Exchange
         organization: Most organizations don't need to select this option. If you need to
         separate management of Active Directory security principals and the Exchange
         configuration, split permissions might work for you. For more information, click ?.

   Click Next to continue.

<!-- p.502 -->

11. On the Malware Protection Settings page, choose whether you want disable malware
   scanning. Malware scanning is enabled by default (the value No is selected). If you disable
   malware scanning, you can enable it in the future. Click Next to continue.

<!-- p.503 -->

12. On the Readiness Checks page, verify that the organization and server role prerequisite
   checks completed successfully. If they haven't, the only option on the page is Retry, so
   you need to resolve the errors before you can continue.

   After you resolve the errors, click Retry to run the prerequisite checks again. You can fix
   some errors without exiting Setup, while the fix for other errors requires you to restart the
   computer. If you restart the computer, you need to start over at Step 1.

   When no more errors are detected on the Readiness Checks page, the Retry button
   changes to Install so you can continue. Be sure to review any warnings, and then click
   Install to install Exchange.

<!-- p.504 -->

13. On the Setup Progress page, a progress bar indicates how the installation is proceeding.

14. On the Setup Completed page, click Finish, and then restart the computer.

<!-- p.505 -->

Next steps
  To verify that you've successfully installed Exchange, see Verify an Exchange installation.

  Complete your deployment by performing the tasks provided in Exchange post-
  installation tasks.

  Having problems? Ask for help in the Exchange forums. Visit the forums at Exchange
  Server   .

<!-- p.506 -->

Install Exchange Edge Transport servers
using the Setup wizard
07/01/2025

APPLIES TO:      2016      2019      Subscription Edition

Before you install an Exchange Server Edge Transport server, verify the following prerequisites:

     We recommend that you install Edge Transport servers in a perimeter network that's
     outside of your organization's internal Active Directory forest. Installing the Edge
     Transport server role on domain-joined computers only enables domain management of
     Windows features and settings. Edge Transport servers don't directly access Active
     Directory. Instead, they use Active Directory Lightweight Directory Services (AD LDS) to
     store configuration and recipient information. For more information about the Edge
     Transport role, see Edge Transport servers.

       ） Important

       When Exchange Server Edge Transport server is domain-joined, a user from that
       domain must run the Exchange Management Shell. If a local user signs into the
       server, cmdlets in the Exchange Management Shell will result in "Access Denied".

     Verify the network, computer hardware, operating system, and software requirements at:
     Exchange Server system requirements and Exchange Server prerequisites.

     Verify the local account on the target computer is a member of the local Administrators
     group.

     Verify that you've read the release notes at Release notes for Exchange Server.

For more information about planning and deploying Exchange, see Planning and deployment
for Exchange Server.

To install the Mailbox role on a computer, see Install Exchange Mailbox servers using the Setup
wizard. Note that you can't install the Edge Transport role on a Mailbox server.

What do you need to know before you begin?
     Estimated time to complete: 40 minutes

<!-- p.507 -->

    You need to configure the primary DNS suffix on the computer. For example, if the fully
    qualified domain name of your computer is edge.contoso.com, the DNS suffix for the
    computer is contoso.com. For more information, see Primary DNS Suffix is missing
    [ms.exch.setupreadiness.FqdnMissing].

    For information about keyboard shortcuts that may apply to the procedures in this topic,
    see Keyboard shortcuts in the Exchange admin center.

 Ｕ Caution

 After you install Exchange on a server, you must not change the server name. Renaming a
 server after you've installed an Exchange server role is not supported.

Install the Exchange Edge Transport server role
 1. Download the latest version of Exchange. For more information, see Updates for
    Exchange Server.

 2. In File Explorer, right-click on the Exchange ISO image file that you downloaded, and then
    select Mount. In the resulting virtual DVD drive that appears, start Exchange Setup by
    double-clicking Setup.exe .

 3. The Exchange Server Setup wizard opens. On the Check for Updates? page, choose one
    of the following options, and then click Next to continue:

         Connect to the Internet and check for updates: We recommend this option, which
         searches for updates to the version of Exchange that you're currently installing (it
         doesn't detect newer Cumulative Updates). This option takes you to the
         Downloading Updates page that searches for updates. Click Next to continue.

         Don't check for updates right now

<!-- p.508 -->

4. The Copying Files page shows the progress of copying files to the local hard drive.
  Typically, the files are copied to %WinDir%\Temp\ExchangeSetup , but you can confirm the
  location in the Exchange Setup log at C:\ExchangeSetupLogs\ExchangeSetup.log .

<!-- p.509 -->

5. On the Introduction page, we recommend that you visit the Exchange Server deployment
  planning links if you haven't already reviewed them. Click Next to continue.

<!-- p.510 -->

6. On the License Agreement page, review the software license terms, select I accept the
  terms in the license agreement, and then click Next to continue.

7. On the Recommended Settings page, choose one of the following settings:

       Use recommended settings: Exchange automatically sends error reports and
       information about your computer hardware and how you use Exchange to
       Microsoft. For information about what's sent to Microsoft and how it's used, click ?
       or the help links on the page.

       Don't use recommended settings: These settings are disabled, but you can enable
       them at any time after Setup completes.

  Click Next to continue.

<!-- p.511 -->

8. On the Server Role Selection page, configure the following options:

       Edge Transport role: Select this option, which also automatically installs the
       Management Tools.

       Automatically install Windows Server roles and features that are required to
       install Exchange: Select this option to have the Setup wizard install the required
       Windows prerequisites. You might need to reboot the computer to complete the
       installation of some Windows features. If you don't select this option, you need to
       install the Windows features manually.

  Note: Selecting this option installs only the Windows features that are required by
  Exchange. You need to install other prerequisites manually. For more information, see
  Exchange Server prerequisites.

  Click Next to continue.

9. On the Installation Space and Location page, either accept the default installation
  location ( C:\Program Files\Microsoft\Exchange Server\V15 ), or click Browse to choose a
  new location. Make sure that you have enough disk space available in the location where
  you want to install Exchange. Click Next to continue.

<!-- p.512 -->

10. On the Readiness Checks page, verify that the organization and server role prerequisite
   checks completed successfully. If they haven't, the only option on the page is Retry, so
   you need to resolve the errors before you can continue.

<!-- p.513 -->

   After you resolve the errors, click Retry to run the prerequisite checks again. You can fix
   some errors without exiting Setup, while the fix for other errors requires you to restart the
   computer. If you restart the computer, you need to start over at Step 1.

   When no more errors are detected on the Readiness Checks page, the Retry button
   changes to Install so you can continue. Be sure to review any warnings, and then click
   Install to install Exchange.

11. On the Setup Progress page, a progress bar indicates how the installation is proceeding.

<!-- p.514 -->

12. On the Setup Completed page, click Finish, and then restart the computer.

Next steps

<!-- p.515 -->

To verify that you've successfully installed Exchange, see Verify an Exchange installation.

Complete your deployment by performing the tasks provided in Exchange post-
installation tasks.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
Server   .

<!-- p.516 -->

Use unattended mode in Exchange Setup
07/01/2025

APPLIES TO:        2016       2019       Subscription Edition

Running Exchange Setup from the command line allows you to automate the installation of Exchange do and other related tasks on Exchange
servers (for example, remove an existing Exchange server or recover a failed Exchange server).

This topic describes the available command line switches, and provides examples.

For more information about planning for Exchange Server, see Planning and deployment for Exchange Server.

For information about tasks to complete after installation, see Exchange Server post-installation tasks.

Primary command line switches for unattended mode
The primary (top-level, scenario-defining) command line switches that are available in unattended Setup mode in Exchange Server are described
in the following table:

                                                                                                                                                      ﾉ    Expand table

 Switch                                                     Description

 /IAcceptExchangeServerLicenseTerms                         Note: Beginning with the September 2021 Cumulative Updates, this switch is no longer available in
                                                            Exchange Server 2016 or Exchange Server 2019.

                                                            This switch is required in all unattended setup commands (whenever you run Setup.exe with any
                                                            additional switches). If you don't use this switch, you'll get an error. To read the license terms, visit
                                                            Microsoft License Terms     .

 /IAcceptExchangeServerLicenseTerms_DiagnosticDataON        Note: These switches are available beginning with the September 2021 Cumulative Updates for
 /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF       Exchange Server 2016 and Exchange Server 2019.

                                                            One of these switches is required in all unattended setup commands (whenever you run Setup.exe
                                                            with any additional switches). If you don't use one of these switches, you'll get an error. To read the
                                                            license terms, visit Microsoft License Terms .

                                                            To accept the license terms and send diagnostic data to Microsoft use the switch with suffix
                                                            DiagnosticDataON.

                                                            To accept the license terms but not send diagnostic data to Microsoft use the switch with suffix
                                                            DiagnosticDataOFF.

 /Mode:<InstallationMode>                                   Valid values are:
 (or /m:<InstallationMode>)                                       Install: Installs Exchange on a new server using the Exchange server roles specified by the /Roles
                                                                  switch. This is the default value if the command doesn't use the /Mode switch.
                                                                  Uninstall: Uninstalls Exchange from a working server.
                                                                  Upgrade: Installs a Cumulative Update (CU) on an Exchange server.
                                                                  RecoverServer: Recovers an Exchange server using the existing Exchange server object in Active
                                                                  Directory after a catastrophic hardware or software failure on the server. For instructions, see
                                                                  Recover Exchange servers.

 /Roles:<ServerRole>                                        This switch is required in /Mode:Install commands. Valid values are:
 (or /Role:<ServerRole> or /r:<ServerRole>)
                                                                  Mailbox (or mb): Installs the Mailbox server role and the Exchange management tools on the
                                                                  local server. This is the default value. You can't use this value with EdgeTransport.
                                                                  EdgeTransport (or et): Installs the Edge Transport server role and the Exchange management
                                                                  tools on the local server. You can't use this value with Mailbox.
                                                                  ManagementTools (or mt or t): Installs the Exchange management tools on clients or other
                                                                  Windows servers that aren't running Exchange.

 /PrepareAD (or /p)                                         Use these switches to extend the Active Directory schema for Exchange, prepare Active Directory for
 /PrepareSchema (or /ps)                                    Exchange, and prepare some or all Active Directory domains for Exchange. For more information, see
 /PrepareDomain:<DomainFQDN> (or /pd:                       Prepare Active Directory and domains for Exchange
 <DomainFQDN>)
 /PrepareAllDomains (or /pad)

 /NewProvisionedServer[:<ServerName>] (or /nprs[:           The /NewProvisionedServer switch creates the Exchange server object in Active Directory. After that, a
 <ServerName>]                                              member of the Delegated Setup role group can install Exchange on the server. For more information,
                                                            see Delegate the installation of Exchange servers.

<!-- p.517 -->

 Switch                                                          Description

 /RemoveProvisionedServer:<ServerName> (or /rprs:                The /RemoveProvisionedServer switch removes a provisioned Exchange server object from Active
 <ServerName>)                                                   Directory before Exchange is installed on the server.

 /AddUmLanguagePack:<Culture1>,<Culture2>...                     Note: These switches aren't available in Exchange 2019 or later. They're only available in Exchange
 <CultureN>                                                      2016.
 /RemoveUmLanguagePack:<Culture1>,<Culture2>...
 <CultureN>                                                      Adds or removes Unified Messaging (UM) language packs from existing Exchange 2016 Mailbox
                                                                 servers. UM language packs enable callers and Outlook Voice Access users to interact with the UM
                                                                 system in those languages. You can't add or remove the en-US language pack.
                                                                 You can install language packs on existing Mailbox servers by using the /AddUmLanguagePack switch
                                                                 or by running the UMLanguagePack.<Culture>.exe file directly. You can only remove installed
                                                                 language packs by using the /RemoveUmLanguagePack switch. For more information, see UM
                                                                 languages, prompts, and greetings.

Optional command line switches for unattended mode
The optional (supporting) command line switches that are available in unattended Setup mode in Exchange Server are described in the following
table:

                                                                                                                                                      ﾉ   Expand table

 Switch                              Valid values                  Default value                                   Available with           Description

 /ActiveDirectorySplitPermissions:   True or False                 False                                           /Mode:Install            Specifies the Active Directory spli
 <TrueOrFalse>                                                                                                     /Roles:Mailbox or        the "Active Directory split permis
                                                                                                                   /PrepareAD
                                                                                                                   commands for the
                                                                                                                   first Exchange server
                                                                                                                   in the organization.

 /AdamLdapPort:                      A valid TCP port number       50389                                           /Mode:Install            Specifies a custom LDAP port to
 <TCPPortNumber>                                                                                                   /Roles:EdgeTransport     Edge Transport servers. The value
                                                                                                                   commands                  HKEY_LOCAL_MACHINE\SOFTWARE\Mic

 /AdamSslPort:                       A valid TCP port number       50636                                           /Mode:Install            Specifies a custom SSL (TLS) port
 <TCPPortNumber>                                                                                                   /Roles:EdgeTransport     the registry at
                                                                                                                   commands                  HKEY_LOCAL_MACHINE\SOFTWARE\Mic

 /AnswerFile:"                       The name and location of      n/a                                             /Mode:Install            Use this switch to create a text fil
 <PathAndFileName>"                  a text file (for                                                              /Roles:Mailbox or        settings. You can use the followin
 (or af:"<PathAndFileName>")         example,"D:\Server                                                            /Mode:Install            CustomerFeedbackEnabled, DbFile
                                     data\answer.txt").                                                            /Roles:EdgeTransport     IAcceptExchangeServerLicenseTerm
                                                                                                                   commands                 UpdatesDir. Don't use the forward
                                                                                                                                            switch/value pair on one line in th

 /CustomerFeedbackEnabled:           True or False                 False                                           /Mode:Install and        Specifies whether to allow or prev
 <TrueOrFalse>                                                                                                     /PrepareAD               future Exchange features. You can
                                                                                                                   commands                 the ErrorReportingEnabled param

 /DoNotEnableEP                      n/a                           n/a                                             /Mode:Install and        Can be used to skip enabling Exte
                                                                                                                   /Mode:Upgrade            Exchange Server 2019 CU14 (or la

 /DoNotEnableEP_FEEWS                n/a                           n/a                                             /Mode:Install and        Can be used to skip enabling Exte
                                                                                                                   /Mode:Upgrade            available with Exchange Server 20
                                                                                                                                            published via Hybrid Agent. It can

 /DbFilePath:"<Path>\                A folder path and an .edb     %ExchangeInstallPath%Mailbox\                   /Mode:Install            Specifies the location of the first
 <FileName>.edb"                     filename (for example,        <DatabaseName>\<DatabaseName>.edb               /Roles:Mailbox           name of the database file with th
                                     "D:\Exchange Database         where:                                          commands                 the /LogFolderPath switch.
                                     Files\DB01\db01.edb").
                                                                           <DatabaseName> is Mailbox
                                                                           Database <10DigitNumber> that
                                                                           matches the default name of the
                                                                           database or the value you specified
                                                                           with the /MdbName switch (without
                                                                           the .edb file name extension).
                                                                           %ExchangeInstallPath% is
                                                                           %ProgramFiles%\Microsoft\Exchange
                                                                           Server\V15\ or the location you
                                                                           specified with the /TargetDir switch.

<!-- p.518 -->

Switch                        Valid values                  Default value                                  Available with           Description

/DisableAMFiltering           n/a                           n/a                                            /Mode:Install            Disables the built-in Exchange an
                                                                                                           /Roles:Mailbox           filtering, see Antimalware protect
                                                                                                           commands

/DomainController:            The server name (for          A randomly selected domain controller in       All /Mode commands       Specifies the domain controller th
<ServerNameOrFQDN>            example, DC01) or FQDN        the same Active Directory site as the target   (except when you're      controller must meet the minimu
(or /dc:<ServerNameOrFQDN>)   (for example,                 server where you're running Setup.             installing an Edge
                              dc01.contoso.com) of the                                                     Transport server) or     If you use this switch in /PrepareS
                              domain controller.                                                           /PrepareAD,              Exchange, you must specify the s
                                                                                                           /PrepareSchema,
                                                                                                           /PrepareDomain and
                                                                                                           /PrepareAllDomains
                                                                                                           commands

/DoNotStartTransport          n/a                           n/a                                            /Mode:Install            Tells Setup to not start the Micros
                                                                                                           /Roles:Mailbox ,         servers after Setup is complete. Y
                                                                                                           /Mode:Install            email messages (for example, con
                                                                                                           /Roles:EdgeTransport ,   Exchange server.)
                                                                                                           and
                                                                                                           /Mode:RecoverServer
                                                                                                           commands.

/EnableErrorReporting         n/a                           Disabled                                       /Mode:Install ,          Specifies whether to allow Exchan
                                                                                                           /Mode:Upgrade , and      can enable or disable error repor
                                                                                                           /Mode:RecoverServer      parameter on the Set-ExchangeS
                                                                                                           commands

/InstallWindowsComponents     n/a                           n/a                                            /Mode:Install            Installs the required Windows rol
                                                                                                           commands                 Setup will resume where the insta

/LogFolderPath:"<Path>"       A folder path (for example,   %ExchangeInstallPath%Mailbox\                  /Mode:Install            Specifies the location of the trans
                              "E:\Exchange Database         <DatabaseName> where:                          /Roles:Mailbox           server. You can specify the locatio
                              Logs").                                                                      commands
                                                                  <DatabaseName> is Mailbox
                                                                  Database <10DigitNumber> that
                                                                  matches the default name of the
                                                                  database or the value you specified
                                                                  with the /MdbName switch (without
                                                                  the .edb file name extension).
                                                                  %ExchangeInstallPath% is
                                                                  %ProgramFiles%\Microsoft\Exchange
                                                                  Server\V15\ or the location you
                                                                  specified with the /TargetDir switch.

/MdbName:"<FileName>"         A database filename           Mailbox Database <10DigitNumber> (for          /Mode:Install            Specifies the name of the first ma
                              without the .edb extension    example, Mailbox Database 0139595516).         /Roles:Mailbox           location of the database files with
                              (for example, "db01")                                                        commands

/OrganizationName:"           A text string (for example,   Blank in command line setup; First             /Mode:Install            The organization name is used in
<Organization Name>"          "Contoso Corporation").       Organization in the Exchange Setup wizard.     /Roles:Mailbox or        of Exchange, and doesn't determ
(or /on:"<Organization                                                                                     /PrepareAD                     The organization name can
Name>")                                                                                                    commands for the               Valid characters are A to Z,
                                                                                                           first Exchange server          allowed.
                                                                                                           in the organization.           You can't change the organ

/SourceDir:"<Path>"           A folder path (for example,   The ServerRoles\UnifiedMessaging folder on     /AddUmLanguagePack       Specifies the location of the lang
(or /s:"<Path>")              "Z:\Exchange).                the Exchange installation media.               commands in              2016 Mailbox servers.
                                                                                                           Exchange 2016 (not
                                                                                                           available in Exchange
                                                                                                           2019)

/TargetDir:"<Path>"           A folder path (for example,   %ProgramFiles%\Microsoft\Exchange              /Mode:Install and        Specifies where to install Exchang
(or /t:"<Path>")              "D:\Program                   Server\V15\                                    /Mode:RecoverServer      or on a ROM drive, RAM disk, net
                              Files\Microsoft\Exchange").                                                  commands                 When you recover a failed Exchan
                                                                                                                                    switch to specify the custom path

/TenantOrganizationConfig:"   A folder path (for example    n/a                                            /Mode:Install or         Required in hybrid deployments
<Path>"                       "C:\Data")                                                                   /PrepareAD               the location of the text file that c
                                                                                                           commands.                organization. You create this file b
                                                                                                                                    your Microsoft 365 or Office 365

<!-- p.519 -->

Switch                             Valid values                  Default value                           Available with          Description

/UpdatesDir:"<Path>"               A folder path (for example,   The Updates folder at the root of the   /Mode:Install ,         Specifies the source location of u
(or /u:"<Path>")                   "D:\Downloads\Exchange        Exchange installation media.            /Mode:Upgrade ,         Any UM language packs located
                                   Updates").                                                            /Mode:RecoverServer ,   server.
                                                                                                         and
                                                                                                         /AddUmLanguagePack
                                                                                                         commands.

What do you need to know before you begin?
    Download the latest version of Exchange on the target computer. For more information, see Updates for Exchange Server.

    Verify the network, computer hardware, operating system, and software requirements at: Exchange Server system requirements and
    Exchange Server prerequisites.

    Verify that you've read the release notes at Release notes for Exchange Server.

         Ｕ Caution

         After you install Exchange on a server, you must not change the server name. Renaming a server after you've installed an Exchange
         server role is not supported.

    For Mailbox servers:

         Estimated time to complete: 60 minutes

         The target server must be a member of an Active Directory domain.

         The account that you use to install Exchange requires the following permissions:*:

              Enterprise Admins group membership: Required if this is the first Exchange server in the organization.

              Schema Admins group membership: Required if you haven't previously extended the Active Directory schema or prepared Active
              Directory for Exchange.

              Exchange Organization Management role group membership: Required if you've already prepared the Active Directory domain that
              will contain the Exchange server, or if other Exchange servers already exist in the organization.

         *
             Members of the Delegated Setup role group can install Exchange on servers that have already been provisioned in Active Directory by
         an Exchange administrator. For more information, see Delegate the installation of Exchange servers.

    For Edge Transport servers:

         Estimated time to complete: 40 minutes

         We recommend that you install Edge Transport servers in a perimeter network that's outside of your organization's internal Active
         Directory forest. Installing the Edge Transport server role on domain-joined computers only enables domain management of Windows
         features and settings. Edge Transport servers don't directly access Active Directory. Instead, they use Active Directory Lightweight
         Directory Services (AD LDS) to store configuration and recipient information. For more information about the Edge Transport role, see
         Edge Transport servers.

         Verify the local account on the target computer is a member of the local Administrators group on the target server.

         You need to configure the primary DNS suffix on the computer. For example, if the fully qualified domain name of your computer is
         edge.contoso.com, the DNS suffix for the computer is contoso.com. For more information, see Primary DNS Suffix is missing
         [ms.exch.setupreadiness.FqdnMissing].

         In coexistence scenarios, Exchange 2010 Hub Transport servers need an update before you can subscribe an Exchange 2016 Edge
         Transport server to an Active Directory site that contains Exchange 2010 Hub Transport servers. If you don't install this update, the
         EdgeSync Subscription won't work correctly for Exchange 2010 Hub Transport server that participates in EdgeSync synchronization. For
         more information, see Supported coexistence scenarios for Exchange 2016.

    For information about keyboard shortcuts that may apply to the procedures in this topic, see Keyboard shortcuts in the Exchange admin
    center.

<!-- p.520 -->

Use Setup.exe to install Exchange in unattended mode
   1. On the target server, open File Explorer, right-click on the Exchange ISO image file that you downloaded, and then select Mount. Note the
     virtual DVD drive letter that's assigned.

   2. Open a Windows Command Prompt window. For example:

            Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then press OK.

            Press Start. In the Search box, type Command Prompt, then in the list of results, select Command Prompt.

   3. In the Command Prompt window, use the following syntax:

       Console

        <Virtual DVD drive letter>:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON [Switches]

     Setup copies the setup files to the local computer.

     Setup checks the prerequisites, including all prerequisites specific to the server roles that you're installing. If you haven't met all the
     prerequisites, Setup fails and returns an error message that explains the reason for the failure. If you've met all the prerequisites, Setup
     installs Exchange.

   4. Restart the server after the Exchange installation is complete.

   5. Complete your deployment by performing the tasks provided in Exchange Server post-installation tasks.

Unattended mode examples
Prepare Active Directory for Exchange in unattended mode
This example configures "Fabrikam Ltd" as the Exchange organization name in Active Directory and prepares Active Directory for the version of
Exchange that's being installed.

  Console

  Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD /OrganizationName:"Fabrikam Ltd"

For more information, see Prepare Active Directory and domains for Exchange.

Install Mailbox servers in unattended mode
     This example installs the first Exchange server (Mailbox server) in the organization, configures "Contoso Corporation" as the Exchange
     organization name in Active Directory, and installs the Exchange management tools on the local server.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Install /Roles:Mailbox /on:"Contoso Corporation"

     This example installs the Mailbox server role and the management tools in the default folder on the local server in an organization where
     Active Directory has already been prepared for the version of Exchange that's being installed.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /r:MB

     This example installs the Mailbox server role and the management tools in the "C:\Exchange Server" folder on the local server.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Install /Role:Mailbox /TargetDir:"C:\Exchange Server"

     This example installs the Mailbox server role on the local server by using the settings in the ExchangeConfig.txt file.
