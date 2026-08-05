---
title: "Core infrastructure documentation — pages 921-960"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0921-0960
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0921-0960
family: sccm
documentKind: "doc"
abstract: "For the user account that installs a CAS as part of a site expansion, add them to the proper role at the stand-alone primary site. Use the built-in Full Administrator or Infrastructure Administrator roles. For more information including the complete list of required permissions,"
---

# Core infrastructure documentation — pages 921-960

<!-- p.921 -->

For the user account that installs a CAS as part of a site expansion, add them to the
proper role at the stand-alone primary site. Use the built-in Full Administrator or
Infrastructure Administrator roles.

For more information including the complete list of required permissions, see Site
installation account.

Top-level site roles
Before you expand the site, uninstall the following site system roles from the stand-
alone primary site:

     Asset Intelligence sync point
     Endpoint protection point
     Service connection point

Configuration Manager only supports these roles at the top-level site of the hierarchy.
Uninstall these site system roles before you expand the stand-alone primary site. After
you expand the site, reinstall these site system roles at the CAS.

All other site system roles can remain installed at the primary site.

Configuration Manager setup also includes a prerequisite check that the standalone
primary site doesn't include the cloud management gateway (CMG) service. Before you
expand the site to a hierarchy, remove the CMG. Then redeploy it from the new CAS.

Open the SQL Server Service Broker port
The network port must be open for the SQL Server Service Broker (SSB) between the
stand-alone primary site and the server for the CAS.

To successfully replicate data between a CAS and a primary site, Configuration Manager
requires an open port between the two sites for SSB to use. When you install a CAS and
expand a stand-alone primary site, the prerequisite check doesn't verify that the port
you specify for the SSB is open on the primary site.

Known issues with Azure services
After you expand the site, you need to reconfigure the following Azure services with
Configuration Manager:

     Log Analytics
     Microsoft Store for Business

<!-- p.922 -->

     Tenant attach

The easiest method is to renew the Microsoft Entra tenant secret key. For more
information, see Renew secret key.

Instead of renewing the secret key, remove and then recreate the connection to that
service.

Secondary sites
The following prerequisites are for installing secondary sites:

     The necessary Windows Server roles, features, and Windows components must be
     installed. For more information, see Site system prerequisites.

     The administrator who configures the installation of the secondary site in the
     Configuration Manager console needs role-based administration permissions that
     are equivalent to the security role of Infrastructure Administrator or Full
     Administrator.

     Add the computer account of the parent primary site to the Administrators group
     on the secondary site server.

     When the secondary site uses a previously installed instance of SQL Server to host
     the secondary site database:

           The computer account of the parent primary site needs sysadmin permissions
           on the instance of SQL Server on the secondary site server.

           The Local System account of the secondary site server computer needs
           sysadmin permissions on the instance of SQL Server on the secondary site
           server.

             ） Important

             When Configuration Manager setup finishes, both accounts still need
             sysadmin permissions to SQL Server. Don't remove the sysadmin
             permissions from these accounts.

     The secondary site server must meet all prerequisite configurations. These
     configurations include SQL Server and the default site system roles of the
     management point and distribution point.

<!-- p.923 -->

Next steps
After you've confirmed the prerequisites, you're ready to run setup. For more
information, see Use the Setup Wizard to install Configuration Manager sites.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.924 -->

Use the Setup Wizard to install
Configuration Manager sites
Article • 12/16/2024

Applies to: Configuration Manager (current branch)

To install a new Configuration Manager site by using a guided user interface, use the
Configuration Manager Setup Wizard (setup.exe). The wizard supports installing a
primary site or central administration site (CAS). You also use the wizard to upgrade an
evaluation installation of Configuration Manager to a fully licensed installation. When
you don't want to use the wizard, you can instead use an installation script and run an
unattended command-line installation.

Install a secondary site from within the Configuration Manager console. Secondary sites
don't support a scripted command-line installation.

Before you install a site, be familiar with the details in the following articles:

      Design a hierarchy of sites
      Site and site system prerequisites
      Prepare to install sites
      Prerequisites for installing sites
      Assess server readiness with the Prerequisite Checker
      Release notes

   Tip

  If you need assistance with site installation, see the Support options and
  community resources. For example, the Microsoft Q&A forum for Configuration
  Manager site and client deployment.

When you're ready to get started, see the following articles for the specific processes:

Use the setup wizard to install a central administration or primary site

Use the setup wizard to install a secondary site

Feedback

<!-- p.925 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.926 -->

Use the setup wizard to install a central
administration or primary site
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use this procedure to install a central administration site (CAS) or a primary site. Also
use it to upgrade an evaluation site to a fully licensed Configuration Manager site.

First, review the overview for using the setup wizard. It includes links to important
prerequisite articles.

If you're installing a CAS as part of a site expansion scenario, first read Expand a stand-
alone primary site before using the following procedure.

Process to install a CAS or primary site
   1. On the computer where you want to install the site, run
      <InstallationMedia>\SMSSETUP\BIN\X64\Setup.exe to start the Configuration

      Manager Setup Wizard.

        ７ Note

        When you install a CAS to expand on a stand-alone primary site, or install a
        new child primary site in an existing hierarchy, use installation media (source
        files) that match the version of the existing site or sites. If you've installed in-
        console updates that have changed the version of the previously installed
        sites, don't use the original installation media. Instead, use source files from
        the CD.Latest folder of an updated site. Configuration Manager requires you
        to use source files that match the version of the existing site that your new
        site will connect to.

   2. On the Before You Begin page, choose Next.

   3. On the Getting Started page, select the type of site that you want to install:

            Central administration site, as the first site of a new hierarchy, or when
            expanding a stand-alone primary site:

            Select Install a Configuration Manager central administration site.

<!-- p.927 -->

       Later in this process, you'll choose to install a CAS for a new hierarchy, or to
       expand a stand-alone primary site.

       Primary site, as a stand-alone primary site that is the first site of a new
       hierarchy, or as a child primary:

       Select Install a Configuration Manager primary site.

          Tip

         Typically, you only select the option Use typical installation options for
         a stand-alone primary site when you want to install a stand-alone
         primary site in a test environment. When you select this option, setup
         does the following actions:
            Automatically configures the site as a stand-alone primary site.
            Uses a default installation path.
            Uses a local installation of the default instance of SQL Server for the
            site database.
            Installs a management point and a distribution point on the site
            server computer.
            Configures the site with English and the display language of the OS
            on the primary site server if it matches one of the languages that
            Configuration Manager supports.

4. On the Product Key page:

       Choose whether to install Configuration Manager as an evaluation edition or
       a licensed edition.

          If you select a licensed edition, enter your product key, and choose Next.

          If you select an evaluation edition, choose Next. You can upgrade an
          evaluation installation to a full installation later.

       You can also specify the Software Assurance expiration date of your
       licensing agreement. It's a convenient reminder of that date. If you don't
       enter this date during Setup, you can specify it later from within the
       Configuration Manager console.

         ７ Note

<!-- p.928 -->

          Microsoft doesn't validate the expiration date that you entered and
          doesn't use this date for license validation. You can use it as a reminder
          of your expiration date. This date is useful because Configuration
          Manager periodically checks for new software updates offered online.
          Your software assurance license status should be current so that you're
          eligible to use these additional updates.

  For more information, see Licensing and branches.

5. On the Microsoft Software License Terms page, read and accept the license terms.

6. On the Prerequisite Licenses page, read and accept the license terms for the
  prerequisite software. Setup downloads and automatically installs the software on
  site systems or clients when it's required. Accept all of the terms before you
  continue to the next page.

7. On the Prerequisite Downloads page, specify whether Setup must download the
  latest prerequisite redistributable files from the internet or use previously
  downloaded files:

       If you want Setup to download the files at this time, select Download
       required files. Then specify a location to store the files.

       If you previously downloaded the files by using Setup Downloader, select Use
       previously downloaded files. Then specify the download folder.

           Tip

          If you use previously downloaded files, verify that the path to the
          download folder contains the most recent version of the files.

8. On the Server Language Selection page, select the languages that are available for
  the Configuration Manager console and for reports. The wizard selects English by
  default and you can't remove it. For more information, see Language packs.

9. On the Client Language Selection page, select the languages that are available to
  client computers. Also specify whether to enable all client languages for mobile
  device clients. The wizard selects English by default and you can't remove it.

    ） Important

<!-- p.929 -->

      When you use a CAS, make sure that client languages you configure at the
      CAS include all client languages that you configure at each child primary site.
      Clients that install from a distribution point have access to the client
      languages from the top-tier site, while clients that install from a management
      point have access to the client languages from their assigned primary site.

10. On the Site and Installation Settings page, specify the following settings for the
   new site that you're installing:

         Site code: Each site code in a hierarchy must be unique. Use three alpha-
         numeric characters: A through Z and 0 through 9 . Because the site code is
         used in folder names, don't use the following Windows-reserved names:
            AUX
            CON

            NUL
            PRN

            SMS

           ７ Note

           Setup doesn't verify whether the site code that you specify is already in
           use, or if it's a reserved name.

         Site name: Each site requires this friendly name, which can help you identify
         the site.

         Installation folder: This folder is the path to the Configuration Manager
         installation. You can't change the location after the site installs. The path can't
         contain Unicode characters or trailing spaces.

           ７ Note

           Consider whether you want to use the default installation folder. If you
           use the default OS partition in a production environment, you may
           experience the following issues in the future:
               If Configuration Manager uses the additional free disk space on the
               OS partition, neither Windows or Configuration Manager will operate
               properly. If you install Configuration Manager on a separate partition,
               its disk consumption won't impact the OS.

<!-- p.930 -->

              Configuration Manager performance is better with a fast disk. Some
              server designs don't optimize the OS disk for speed.
              You can service, restore, or reinstall the OS without impacting your
              Configuration Manager installation.

11. On the Site Installation page, use the following option that matches your scenario:

         I'm installing a CAS:

         On the Central Administration Site Installation page, select Install as the
         first site in a new hierarchy, and then choose Next to continue.

         I'm expanding a stand-alone primary into a hierarchy with a CAS:

         On the Central Administration Site Installation page, select Expand an
         existing stand-alone primary into a hierarchy. Then specify the FQDN of the
         stand-alone primary site server, and choose Next to continue.

         The media that you use to install the new CAS must match the version of the
         primary site.

         I'm installing a stand-alone primary site:

         On the Primary Site Installation page, select Install the primary site as a
         stand-alone site, and then choose Next.

         I'm installing a child primary site:

         On the Primary Site Installation page, select Join the primary site to an
         existing hierarchy. Then specify the FQDN for the CAS, and choose Next.

12. On the Database Information page, specify the following information:

         SQL Server name (FQDN): By default, this value is set to the site server
         computer.

         If you use a custom port, add that port to the FQDN of the SQL Server. Follow
         the FQDN of the SQL Server with a comma and then the port number. For
         example, for server SQLServer1.fabrikam.com, use the following string to
         specify custom port 1551: SQLServer1.fabrikam.com,1551

         Instance name: By default, this value is blank. It uses the default instance of
         SQL Server on the site server computer.

<!-- p.931 -->

        Database name: By default, this value is set to CM_<Sitecode> . You can
        customize this value.

        Service Broker Port: By default, this value is set to use the default SQL Server
        Service Broker (SSB) port of 4022. SQL Server uses it to communicate directly
        to the site database at other sites.

13. On the second Database Information page, you can specify custom locations for
   the SQL Server data file and the SQL Server log file for the site database:

        By default, it uses the default file locations for SQL Server.

        When you use a SQL Server Always On failover cluster instance, the option to
        specify custom file locations isn't available.

        The prerequisite checker doesn't run a check for free disk space for custom
        file locations.

14. On the SMS Provider Settings page, specify the FQDN for the server where you
   want to install the SMS Provider.

        By default, it specifies the site server.

        After the site installs, you can configure more SMS Providers. For more
        information, see Plan for the SMS Provider.

15. On the Client Communication Settings page, choose how clients will
   communicate with site systems. The more secure option is to require all site
   systems to use HTTPS. Otherwise, you individually configure the communication
   method for each site system role.

     ） Important

     Starting in Configuration Manager version 2103, sites that allow HTTP client
     communication are deprecated. Configure the site for HTTPS or Enhanced
     HTTP. For more information, see Enable the site for HTTPS-only or enhanced
     HTTP.

        All site system roles accept only HTTPS communication from clients: When
        you select this option, clients must have a valid PKI certificate for client
        authentication. For more information, see PKI certificate requirements.

        Configure the communication method on each site system role: Starting in
        version 2203, when you select this option, setup configures the site to use

<!-- p.932 -->

           Enhanced HTTP.

     ７ Note

     This page only applies when you install a primary site. If you're installing a
     CAS, skip this page.

16. On the Site System Roles page, choose whether to install a management point or
   distribution point. For each role that you choose to have installed by Setup:

     ７ Note

     This step only applies when you install a primary site. If you're installing a CAS,
     skip this step.

           Enter the FQDN for the server that will host the role. Then choose the client
           connection method that the server will support: HTTP or HTTPS.

           If you selected All site system roles accept only HTTPS communication from
           clients on the previous page, the wizard automatically configures the client
           connection settings for HTTPS. You can't change this setting unless you go
           back to the previous page.

     ７ Note

     To install site system roles, Setup uses the site system installation account. By
     default, it uses the primary site's computer account. This account must be a
     local administrator on the remote computer to install the role. If this account
     lacks the required permissions, don't install the roles during Setup. After you
     configure additional accounts to use as site system installation accounts,
     install the roles from the Configuration Manager console. For more
     information, see Accounts.

17. On the Usage Data page, review the information about data that Microsoft
   collects, and then choose Next. For more information, see Diagnostics and usage
   data.

18. The Service Connection Point Setup page is only available when you're installing a
   stand-alone primary site or a CAS.

<!-- p.933 -->

      ７ Note

      If you're installing a child primary site, skip this step.

   If you're installing a CAS as part of a site expansion scenario, and the stand-alone
   primary site already has this role, first uninstall it from the stand-alone primary site.
   Configuration Manager can only have one instance of the service connection point
   in a hierarchy. It's only supported at the top-tier site of the hierarchy.

   After you select a configuration for the Service Connection Point, choose Next.
   After Setup completes, you can change this configuration from the Configuration
   Manager console. For more information, see About the service connection point.

19. On the Settings Summary page, review the setting that you've selected. When
   you're ready, choose Next to start the Prerequisite Checker.

20. On the Prerequisite Installation Check page, it lists any problems that the checker
   can identify.

         When the Prerequisite Checker finds a problem, choose an item in the list for
         details about how to resolve the problem.

         Before you can continue to install the site, resolve any Failed items. Try to
         resolve all Warning items, but they don't block installation.

         After you resolve any issues, choose Run Check to rerun the Prerequisite
         Checker.

         When the Prerequisite Checker runs, and no checks receive a Failed status,
         you can choose Begin Install to start the site installation.

       Tip

      In addition to the feedback that the wizard provides, you can find additional
      information about prerequisite issues in the ConfigMgrPrereq.log file. It's in
      the root of the system drive on the server. For more information, see List of
      prerequisite checks.

21. On the Installation page, Setup displays the installation status. When the core site
   server installation is complete, you can Close the installation wizard. When you
   close the wizard, the installation and initial site configurations continue in the
   background.

<!-- p.934 -->

             You can connect a Configuration Manager console to the site before Setup is
             complete. This console connects as read-only, and lets you view objects and
             settings, but you can't modify anything.

             After Setup completes, you can connect a console to edit objects and
             settings.

             If setup fails, you can Report update error to Microsoft. For more
             information, see Report setup and upgrade failures to Microsoft.

Expand a stand-alone primary site
When you've installed a stand-alone primary site as your first site, you can later install a
CAS to expand that site into a larger hierarchy. This process is also called site expansion.
The main reason to expand to a hierarchy is for scale. A hierarchy allows you to support
more clients than a stand-alone primary site can support. For more information, see Size
and scale numbers.

When you expand a stand-alone primary site, you install a new CAS that uses the
existing stand-alone primary site database as a reference. After the new CAS installs, the
stand-alone primary site functions as a child primary site.

     You can only expand a stand-alone primary site into a new hierarchy.

     You can only expand one stand-alone primary site into a specific hierarchy. You
     can't use this option to join other stand-alone primary sites into the same
     hierarchy. Instead, use the Migration Wizard to migrate data from one hierarchy
     into another. For more information, see Migrate data between hierarchies.

     After you expand a stand-alone site into a hierarchy with a CAS, you can install
     other child primary child sites.

     To remove a primary site from a hierarchy with a CAS, first uninstall the primary
     site.

Before you start, first see the prerequisites to expand a site.

To expand the site, use the process to install a CAS or primary site with the following
caveats:

     Install the CAS by using the same version of Configuration Manager as the stand-
     alone primary site.

<!-- p.935 -->

     On the Getting Started page of the Setup Wizard, select the option to install a
     CAS. At a later stage of Setup, you'll choose an option to expand an existing stand-
     alone primary site.

     On the Client Language Selection page for the new CAS, select the same client
     languages that you configured on the original primary site.

     On the Site Installation page, select the option to expand the stand-alone primary
     site.

     If you enable Endpoint Analytics for devices uploaded to Microsoft Endpoint
     Manager, in version 2107 or later, re-enable this option.

Next steps
Use the setup wizard to install a secondary site

Configure sites and hierarchies

Install consoles

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.936 -->

Use the setup wizard to install a
secondary site
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use this procedure to install a secondary site. Install a secondary site from within the
Configuration Manager console. Secondary sites don't support a scripted command-line
installation.

      In a hierarchy, you don't have to connect the console to the parent primary site. If
      the console isn't connected to the parent primary site for the new secondary site,
      Configuration Manager replicates the command to install the secondary site to the
      correct primary site.

      Before you start the secondary site installation, make sure that your user account
      has the prerequisite permissions. Also make sure that the server that will host the
      new secondary site meets all the prerequisites for use as a secondary site server.
      For more information, see Prerequisites for installing sites and Site and site system
      prerequisites.

      When you install the secondary site, Configuration Manager configures the new
      site to use the same client communication ports as the parent primary site.

Before you start, review the overview for using the setup wizard. It includes links to
important prerequisite articles.

Process to install a secondary site
   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and select the Sites node. Select the site that will be
      the parent primary site of the new secondary site.

   2. In the ribbon, select Create Secondary Site. This action starts the Create
      Secondary Site Wizard.

   3. On the Before You Begin page, confirm that the listed server is the primary site
      that you want to be the parent of the new secondary site. Then choose Next.

   4. On the General page, specify the following settings:

<!-- p.937 -->

        Site code: Each site code in a hierarchy must be unique. Use three alpha-
        numeric characters: A through Z and 0 through 9 . Because the site code is
        used in folder names, don't use the following Windows-reserved names:
            AUX

            CON

            NUL
            PRN

            SMS

    ７ Note

    Setup doesn't verify whether the site code that you specify is already in use, or
    if it's a reserved name.

        Site server name: This value is the FQDN of the server for the new secondary
        site.

        Site name: Each site requires this friendly name, which can help you identify
        the site in the console.

        Installation folder: This folder is the path to the Configuration Manager
        installation. You can't change the location after the site installs. The path can't
        contain Unicode characters or trailing spaces.

    ） Important

    After you specify details on this page, you can choose Summary to skip to the
    end of the wizard. This action uses the default settings for the remainder of
    the secondary site options.

           Only use this option when you're familiar with the default settings in this
           wizard, and they're the settings you want to use.

           When you use the default settings, boundary groups aren't associated
           with the distribution point. Until you configure boundary groups that
           include the secondary site server, clients won't use the distribution point
           that's installed on this secondary site as a content source location.

5. On the Installation Source Files page, choose how the secondary site server gets
  the source files to install the site.

<!-- p.938 -->

  When you use CD.Latest source files that are shared on the network or copied
  locally to the target secondary site server:

       The CD.Latest source file location includes a folder named Redist. Move this
       Redist folder as a subfolder under the SMSSETUP folder.

       Copy the following files from the Redist folder to the SMSSETUP\BIN\X64
       folder:
          SharedManagementObjects.msi
          SQLSysClrTypes.msi
          sqlncli.msi

       If any of the files from Redist aren't available, Setup fails to install the
       secondary site.

       The computer account of the secondary site server needs Read permissions
       to the source file folder and share.

6. On the SQL Server Settings page, specify the version of SQL Server to use:

    ７ Note

    Setup doesn't validate the information that you enter on this page until it
    starts the installation. Before you continue, verify these settings.

       Install and configure a local copy of SQL Express on the secondary site
       computer

          SQL Server Service port: Specify the SQL Server service port for SQL
          Server Express to use. The service port is typically configured to use TCP
          port 1433, but you can configure another port.

          SQL Server Broker port: Specify the SQL Server Service Broker (SSB) port
          for SQL Server Express to use. The Service Broker is typically configured to
          use TCP port 4022, but you can configure a different port. Specify a valid
          port that no other site or service is using, and that the firewall doesn't
          block.

       Use an existing SQL Server instance

          SQL Server FQDN: Review the FQDN for the computer running SQL Server.
          Use a local server running SQL Server to host the secondary site database,
          and you can't modify this setting.

<!-- p.939 -->

          SQL Server instance: Specify the instance of SQL Server to use as the
          secondary site database. Leave this option blank to use the default
          instance.

          ConfigMgr site database name: Specify the name to use for the secondary
          site database.

          SQL Server Broker port: Specify the SQL Server Service Broker (SSB) port
          for SQL Server to use. Specify a valid port that no other site or service is
          using, and that the firewall doesn't block.

     Tip

    For a list of the SQL Server versions that Configuration Manager supports, see
    Supported SQL Server versions.

7. On the Distribution Point page, configure settings for the distribution point that
  Setup will install on the secondary site server.

       Required settings:

          Specify how client devices communicate with the distribution point:
          Choose between HTTP and HTTPS.

             ） Important

             Starting in Configuration Manager version 2103, sites that allow HTTP
             client communication are deprecated. Configure the site for HTTPS or
             Enhanced HTTP. For more information, see Enable the site for
             HTTPS-only or enhanced HTTP.

          Create a self-signed certificate or import a PKI client certificate: Choose
          between using a self-signed certificate or importing a certificate from your
          PKI. A self-signed certificate lets you also allow anonymous connections
          from Configuration Manager clients to the content library. The certificate is
          used to authenticate the distribution point to a management point before
          the distribution point sends status messages. For more information, see
          PKI certificate requirements.

       Optional settings:

<!-- p.940 -->

          Install and configure IIS if required by Configuration Manager: Select this
          setting to let Configuration Manager install and configure Internet
          Information Services (IIS) on the server. Configuration Manager only
          installs IIS if it's not already installed on the server. IIS is required on all
          distribution points.

             ７ Note

             Although this setting is optional, IIS is required to add the distribution
             point role.

          Enable and configure BranchCache for this distribution point

          Description: This value is a friendly description for the distribution point to
          help you recognize it in the console.

          Enable this distribution point for prestaged content

8. On the Drive Settings page, specify the drive settings for the secondary site
  distribution point.

  You can configure up to two disk drives for the content library and two disk drives
  for the package share. However, Configuration Manager can use other drives when
  the first two reach the configured drive space reserve. Use this Drive Settings page
  to configure the priority for the disk drives and the amount of free disk space to
  remain on each disk drive.

       Drive space reserve (MB): The value that you configure for this setting
       determines the amount of free space on a drive before Configuration
       Manager chooses a different drive and continues the copy process to that
       drive. Content files can span multiple drives.

       Content Locations: Specify the content locations for the content library and
       package share. Configuration Manager copies content to the primary content
       location until the amount of free space reaches the value that's specified for
       Drive space reserve (MB).

  By default, the content locations are set to Automatic. The primary content
  location is set to the disk drive that has the most space at installation time. The
  secondary location is set to the disk drive that has the most free disk space after
  the primary drive. When the primary and secondary drives reach the drive space
  reserve, Configuration Manager selects another available drive with the most free
  disk space and continues the copy process.

<!-- p.941 -->

   9. On the Content Validation page, specify whether to validate the integrity of
     content files on the distribution point.

           When you enable content validation on a schedule, Configuration Manager
           starts the process at the scheduled time. It verifies all content on the
           distribution point.

           You can also configure the Content validation priority.

 10. On the Boundary Groups page, manage the boundary groups for this distribution
     point:

           Allow fallback source location for content: This option allows clients outside
           these boundary groups to fall back and use the distribution point as a source
           location for content when no preferred distribution points are available.

     For more information, see the Fundamental concepts for content management.

 11. On the Summary page, verify the settings, and then choose Next to install the
     secondary site. When the wizard shows the Completion page, you can close the
     wizard. The secondary site installation continues in the background.

How to verify the secondary site installation status
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the new secondary site, and then choose Show Install Status in the ribbon.

         Tip

        When you install more than one secondary site at a time, the Prerequisite
        Checker runs against a single site at a time. It finishes a site before it starts to
        check the next site.

Next steps
Configure sites and hierarchies

Install consoles

<!-- p.942 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.943 -->

Use a command line to install
Configuration Manager sites
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can run Configuration Manager setup at a command prompt to automate the
installation of different kinds of site types. This article provides an overview of the
command-line methods.

Supported tasks for command-line installations
      Install a central administration site (CAS) or primary site

      Modify the languages in use at a CAS or primary site

      Recovery a site

   Tip

  You can also install the Configuration Manager client and console from the
  command prompt. For more information, see the following articles:

        Install consoles
        Deploy clients to Windows computers

About the command-line script file
For unattended installations of Configuration Manager, you can specify a script file that
contains installation options.

  ７ Note

  You can't use the unattended script file to upgrade an evaluation site to a licensed
  installation of Configuration Manager.

To use an answer file with setup, first configure the script file with required keys and
values. For an unattended installation of a CAS or primary site, the script file requires the
following sections:

<!-- p.944 -->

      Identification
      Options

      SQLConfigOptions
      HierarchyExpansionOption

      CloudConnectorOptions

      SABranchOptions

Then run setup with the command line-option /SCRIPT and specify a script file.

To recover a site, the script file also uses the RecoveryOptions section.

For a list of keys and values to use in an unattended installation script file, see
Unattended setup script file keys.

  ７ Note

  When you run setup from the CD.Latest folder for a scripted install or recovery,
  include the CDLatest key with a value of 1 . This value isn't supported with
  installation media from the Microsoft Volume License site. For more information on
  how to use this key name in the script file, see Command-line options.

Create the script
When you run setup to install a site using the user interface, setup automatically creates
the installation script. When you confirm the settings on the Summary page of the
wizard, the following actions happen:

     Setup creates the script %TEMP%\ConfigMgrAutoSave.ini . You can rename this file
     before you use it, but it needs the .ini file extension.
     The unattended installation script contains the settings that you selected in the
     wizard.
     You can modify the script to install other sites in your hierarchy.
     You can use this script to do an unattended setup of Configuration Manager.

This script file provides the same information as the Setup Wizard, except that there are
no default settings. Specify all values for the setup keys that are required and necessary
for your requirements.

When setup creates the unattended installation script, it includes the product key that
you entered in the Setup Wizard. This key can be a valid product key, or EVAL to install
an evaluation version of Configuration Manager. The product key value in the script is

<!-- p.945 -->

required by the prerequisite checker. When setup starts the actual site installation, it
clears the product key value in the script. Before using the script for an unattended
installation of a new site, edit the script to provide a valid product key or to specify an
evaluation installation of Configuration Manager.

   Tip

  You can also manually create the script file from a plain-text editor like Notepad.

Section names, key names, and values
The script contains section names, key names, and values.

     Required section key names vary depending on the installation type.
     The order of the sections and the order of the keys within sections aren't
     important.
     The keys aren't case-sensitive.
     When you provide values for keys, the name of the key must be followed by an
     equal sign ( = ) and the value for the key. For example, CDLatest=1

To view the full set of options, see Command-line options for setup and scripts.

Use a setup script file
To use a setup script file, specify the file name after the /SCRIPT command-line option.

     The script file name requires the .ini extension.

     Provide the full path to the file. For example, if you name the file setup.ini , and
     store it in the C:\Setup folder, then use the following command line: setup.exe
     /script C:\Setup\setup.ini

     The account that runs setup must have Administrator rights on the computer.
     When you run setup with the unattended script, open the command prompt
     window with the Run as administrator option.

Modify languages
To modify the languages that are installed at a site from a command prompt:

     Run setup from <ConfigMgrInstallationPath>\Bin\X64 on the site server

<!-- p.946 -->

     Use the /MANAGELANGS command-line option
     Specify a language script file with the languages to add or remove

For example, use the following command syntax: setupwpf.exe /MANAGELANGS <language
script file>

For more information values to use in the language script file, see Manage languages.

For more information on languages in Configuration Manager, see Language packs.

Next steps
Command-line options for setup

Unattended setup script file keys

Install the Configuration Manager console

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.947 -->

Command-line options for
Configuration Manager setup
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use this information to configure scripts or to install Configuration Manager from a
command line. For more information on how to use these command-line options, see
Command-line overview.

Run setup.exe from the \BIN\X64 directory of the Configuration Manager installation
path on the site server.

   Tip

  You can also use setupwpf.exe from the same folder, but it doesn't include basic
  prerequisite checks.

/DEINSTALL
Uninstall the site. Run setup from the site server computer.

/DONTSTARTSITECOMP
Install a site, but prevent the Site Component Manager service from starting. Until the
Site Component Manager service starts, the site isn't active. The Site Component
Manager is responsible for installing and starting the SMS_Executive service, and for
other processes at the site. After the site install is finished, when you start the Site
Component Manager service, it installs the SMS_Executive service and other processes
that are necessary for the site to operate.

/HIDDEN
Hide the user interface during setup. Only use this option with the /SCRIPT option. The
unattended script file must provide all required options or setup fails.

/NOUSERINPUT

<!-- p.948 -->

Disable user input during setup, but display the setup wizard. Only use this option with
the /SCRIPT option. The unattended script file must provide all required options or
setup fails.

/RESETSITE
Run a site reset. This action resets the database and service accounts for the site. For
more information, see Run a site reset.

/SQLMOVE
Move the site database. This action moves the site database to a new instance of SQL
Server on the same computer, or to a different computer that runs a supported version
of SQL Server. For more information, see Modify the site database configuration.

Provide the SQL server name, database name and instance name in the following
format:

/SQLMOVE <SQL Server FQDN>:<Database Name>:<SSB Port>

/SQLMOVE <SQL Server FQDN>:<InstanceName>\<Database Name>:<SSB Port>

/TESTDBUPGRADE
Run a test on a backup of the site database to make sure that the database can
upgrade.

  ） Important

  The test upgrade is no longer a required or recommend step for most sites.

  If your database is suspect, or is modified by customizations not explicitly
  supported by Configuration Manager, continue to use this process.

  Don't run this command-line option on your production site database. Running this
  command-line option on your production site database upgrades the site database
  and could render your site inoperable.

Provide the instance name and database name for the site database. If you specify only
the database name, setup uses the default instance name.

<!-- p.949 -->

/TESTDBUPGRADE <Instance name>\<Database name>

/TESTDBUPGRADE CM_ABC

/TESTDBUPGRADE Named\CM_ABC

For more information, see Test the database upgrade when installing an update.

/UPGRADE
Run an unattended upgrade of a site. Specify the product key including the dash ( - )
delimiters. Also specify the path to the previously downloaded setup prerequisite files.

For example: /UPGRADE xxxxx-xxxxx-xxxxx-xxxxx-xxxxx C:\Setup\prereqs

For more information about setup prerequisite files, see Setup Downloader.

/SCRIPT
Run an unattended installation. Use a setup initialization file with this option. For more
information about how to run setup unattended, see Install sites using a command line.
For more information on the script file keys and values, see Unattended setup script file
keys.

For example: /SCRIPT C:\Setup\setup.ini

/SDKINST
Install the SMS Provider on the specified server. Provide the fully qualified domain name
(FQDN) for the SMS Provider computer. For more information about the SMS Provider,
see Plan for the SMS Provider.

For example: /SDKINST cm02.contoso.com

/SDKDEINST
Uninstall the SMS Provider on the specified computer. Provide the FQDN for the SMS
Provider computer.

For example: /SDKDEINST cm01.contoso.com

<!-- p.950 -->

/MANAGELANGS
Manage the languages that are installed at a previously installed site. Provide the
location for the language script file that contains the language settings. For more
information, see the Keys to manage languages.

For example: /MANAGELANGS C:\Setup\langsetup.ini

Next steps
Unattended setup script file keys

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.951 -->

Unattended setup script file keys
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article defines all of the keys and values to specify in the .ini installation script file.
Use this file with the /SCRIPT command-line option to do an unattended installation or
recovery of a Configuration Manager site. The tables in this article show:

      The available setup script keys and their corresponding values
      If they're required
      Which type of installation they're used for
      A short description of the key

For more information, see the following articles:

      Command-line overview
      Setup command-line options

Specify the section names in square brackets ( [] ): [<Section name>] . For example,
[Identification] .

When you provide values for keys, the name of the key must be followed by an equal
sign ( = ) and the value for the key: <Key name>=<Value> . For example, CDLatest=1 . Make
sure the keys are under the appropriate section.

Each section and each value needs to be unique in a single script. For example, there
can only be one [Identification] section and only one Action key.

Supported actions
A script is primarily defined by the Action key in the Identification section. The
following list includes all of the currently supported actions for running setup
unattended:

      InstallCAS : Install a central administration site (CAS)

      InstallPrimarySite : Install a primary site

      ManageLanguages : Add or remove client and server languages
      RecoverPrimarySite : Recovery a primary site

      RecoverCCAR : Recover a CAS

<!-- p.952 -->

Install a site

Identification section for site install

Depending upon the type of site you're installing, include the following keys with the
appropriate values in the Identification section:

                                                                                   ﾉ    Expand table

 Key         Required   Values                     Details
 name

 Action      Yes        - InstallPrimarySite       - Install a primary site.
                        - InstallCAS               - Install a central administration site (CAS)

 CDLatest    Yes 2      1 : Setup runs from        When you run setup from the CD.Latest folder,
                        CD.Latest                  include this key and value. This value tells setup
                                                   that you're using media from CD.Latest .

Note 2: CDLatest required

The CDLatest key is only required when you run setup from the CD.Latest folder to
install a primary site or a central administration site. For more information, see About the
command-line script file.

Options section for site install

Include the following keys in the Options section to install a site:

                                                                                   ﾉ    Expand table

 Key name               Required    Values                   Details

 ProductID              Yes         - xxxxx-xxxxx-           The type of license to install.
                                    xxxxx-xxxxx-xxxxx :
                                    A valid product key
                                    with dashes
                                    - Eval : Install the
                                    evaluation version

 SiteCode               Yes         Three character          The three-character site code that
                                    code, for example        uniquely identifies the site in the
                                       XYZ                   hierarchy.

<!-- p.953 -->

 Key name               Required   Values                   Details

 SiteName               Yes        A site name              The friendly name for this site to help
                                                            identify it.

 SMSInstallDir          Yes        Local directory path     The installation folder for the
                                                            Configuration Manager program files.

 SDKServer              Yes        SMS Provider             The FQDN of the first server to host
                                   FQDN                     the SMS Provider.

 PrerequisiteComp       Yes        - 0 : Download           Specify whether prerequisite files have
                                   - 1 : Already            already been downloaded. If you use a
                                   downloaded               value of 0 , setup downloads the files.

 PrerequisitePath       Yes        Local directory path     The path to the prerequisite files.
                                                            Depending on the PrerequisiteComp
                                                            value, setup uses this path to store
                                                            downloaded files or to locate
                                                            previously downloaded files.

 AdminConsole           Yes        - 0 : Don't install      Specify whether to install the
                                   - 1 : Install            Configuration Manager console on
                                                            the site server.

 JoinCEIP               Yes        0                        While support for the Customer
                                                            Experience Improvement Program
                                                            (CEIP) was removed from the product,
                                                            this key is still required.

 MobileDeviceLanguage   Yes        - 0 : Don't install      Specify whether the mobile device
                                   - 1 : Install            client languages are installed.

When you install a site, you can also specify the keys to manage languages, such as
AddServerLanguages or AddClientLanguages . For more information, see Options section
for languages.

The following keys in the Options section are specific to a primary site:

                                                                                  ﾉ   Expand table

 Key name                     Required      Values            Details

 ManagementPoint              No            MP FQDN           The FQDN of the server that will
                                                              host the first management point
                                                              (MP) site system role.

 ManagementPointProtocol      No            HTTPS or HTTP     The protocol to use for the MP.

<!-- p.954 -->

 Key name                       Required   Values               Details

 DistributionPoint              No         DP FQDN              The FQDN of the server that will
                                                                host the first distribution point (DP)
                                                                site system role.

 DistributionPointProtocol      No         HTTPS or HTTP        The protocol to use for the DP.

 DistributionPointInstallIIS    No         - 0 : Don't          Specify whether to install IIS on the
                                           install              DP.
                                           - 1 : Install

 RoleCommunicationProtocol      Yes        EnforceHTTPS         Specify whether to configure all site
                                           or                   systems to accept only HTTPS
                                           HTTPorHTTPS          communication from clients, or to
                                                                configure the communication
                                                                method for each site system role.
                                                                When you select EnforceHTTPS ,
                                                                clients need a valid public key
                                                                infrastructure (PKI) certificate for
                                                                client authentication.

 ClientsUsePKICertificate       Yes        - 0 : Don't use      Specify whether clients will use a
                                           - 1 : Use            client PKI certificate to communicate
                                                                with site system roles.

 UseFQDN                        No         - 0 : Don't use      Specify whether the site systems'
                                           - 1 : Use            FQDN is for use on the internet.

 ParentSiteCode                 No         Site code            When you're adding a child primary
                                                                site to an existing hierarchy, specify
                                                                the site code of the CAS.

 ParentSiteServer               No         FQDN                 When you're adding a child primary
                                                                site to an existing hierarchy, specify
                                                                the FQDN of the CAS server.

SQLConfigOptions section for site install

Include the following keys in the SQLConfigOptions section to install a site:

                                                                                     ﾉ   Expand table

 Key name            Required   Values               Details

 SQLServerName       Yes        FQDN of SQL          The name of the server or clustered instance
                                Server               that's running SQL Server to host the site
                                                     database.

<!-- p.955 -->

 Key name          Required     Values               Details

 DatabaseName      Yes          Name or              The name of the SQL Server database to create
                                Instance\Name        or use. If it's on the default instance, just specify
                                                     the database name. Otherwise specify the
                                                     instance and name.

 SQLServerPort     No           Port number          The port that SQL Server uses. By default, it
                                                     uses 1433.

 SQLSSBPort        No           Port number          The SQL Server Service Broker (SSB) port. By
                                                     default, SSB uses TCP port 4022.

 SQLDataFilePath   No           Local directory      An alternate location to create the database
                                path                 .mdb file.

 SQLLogFilePath    No           Local directory      An alternate location to create the database .ldf
                                path                 log file.

 AGBackupShare     No           Network share        The network location for sharing database
                                path                 backups when creating the site database in an
                                                     Availability Group. The backup share is only
                                                     needed if automatic seeding is not set.

CloudConnectorOptions section for site install

Include the following keys in the CloudConnectorOptions section to install a site:

                                                                                      ﾉ   Expand table

 Key name                Required      Values        Details

 CloudConnector          Yes           - 0 : Don't   Specify whether to install a service connection
                                       install       point (SCP) at this site. Because you can only
                                       -             install the SCP at the top-tier site of a hierarchy,
                                       1 : Install   set this value to 0 for a child primary site.

 CloudConnectorServer    Yes*          SCP           The FQDN of the server that will host the SCP
                                       FQDN          role. * Only required when CloudConnector
                                                     equals 1 .

 UseProxy                Yes*          - 0 : No      Specify whether the SCP uses a proxy server. *
                                       proxy         Only required when CloudConnector equals 1 .
                                       - 1 : Use
                                       proxy

 ProxyName               Yes*          Proxy         The FQDN of the proxy server that the SCP uses.
                                       FQDN          * Only required when UseProxy equals 1 .

<!-- p.956 -->

 Key name               Required         Values         Details

 ProxyPort              Yes*             Port           The port number of the proxy server that the
                                         number         SCP uses. * Only required when UseProxy equals
                                                        1.

SABranchOptions section for site install

Include the following keys in the SABranchOptions section to install a site:

                                                                                       ﾉ   Expand table

 Key name         Required     Values             Details

 SAActive         Yes          - 0 : You          Specify if you have active Software Assurance (SA). For
                               don't have         more information, see Product and licensing FAQ.
                               SA
                               - 1 : SA is
                               active

 CurrentBranch    Yes          - 0 : Install      Specify whether to use Configuration Manager current
                               the LTSB           branch or long-term servicing branch (LTSB). For more
                               - 1 : Install      information, see Which branch of Configuration
                               current            Manager should I use?
                               branch

 SAExpiration     No           Date               The date when SA expires, used as a convenient
                                                  reminder of that date. For more information, see
                                                  Licensing and branches.

HierarchyExpansionOption section for site expansion

When you're installing a CAS to expand a standalone primary site into a hierarchy, use
the following keys in the HierarchyExpansionOption section:

                                                                                       ﾉ   Expand table

 Key name               Required        Values          Details

 CCARSiteServer         No              CAS FQDN        The FQDN of the CAS that a primary site
                                                        attaches to when it joins the Configuration
                                                        Manager hierarchy. Specify the CAS during
                                                        setup.

 CASRetryInterval       No              Minutes         If the connection to the CAS fails, the primary
                                                        site waits this number of minutes, and then

<!-- p.957 -->

 Key name                Required    Values         Details

                                                    reattempts the connection.

 WaitForCASTimeout       No          0 to 100       The maximum timeout value in minutes for a
                                                    primary site to connect to the CAS.

 UseDistributionView     No          - 0 : Don't    Specify whether to use distributed views to
                                     enable         optimize database replication.
                                     - 1 : Enable

 JoinPrimarySiteName     No          Site server    The FQDN of the primary site server to expand.
                                     FQDN

Manage languages

Identification section for languages

Include the following key in the Identification section to manage languages:

                                                                                  ﾉ   Expand table

 Key        Required     Values               Details
 name

 Action     Yes          ManageLanguages      Manages the server, client, and mobile client language
                                              support at a site.

Options section for languages

Include the following keys in the Options section to manage languages:

                                                                                  ﾉ   Expand table

 Key name                 Required     Values            Details

 AddServerLanguages       No           See note 1        The server languages that will be available
                                                         for the Configuration Manager console,
                                                         reports, and other objects.

 AddClientLanguages       No           See note 1        The languages that will be available to
                                                         client computers.

 DeleteServerLanguages    No           See note 1        The languages to remove. They'll no
                                                         longer be available for the Configuration

<!-- p.958 -->

 Key name                Required   Values            Details

                                                      Manager console, reports, and other
                                                      objects.

                                    See note 1
 DeleteClientLanguages   No                           The languages to remove, and which will
                                                      no longer be available to client computers.
                                                      English is available by default, you can't
                                                      remove it.

 MobileDeviceLanguage    Yes        - 0 : Don't       Specify whether the mobile device client
                                    install           languages are installed.
                                    - 1 : Install

 PrerequisiteComp        Yes        - 0:              Specify whether prerequisite files have
                                    Download          already been downloaded. For example, if
                                    - 1 : Already     you use a value of 0 , setup downloads the
                                    downloaded        files.

 PrerequisitePath        Yes        Local directory   The path to the prerequisite files.
                                    path              Depending on the PrerequisiteComp value,
                                                      setup uses this path to store downloaded
                                                      files or to locate previously downloaded
                                                      files.

 ResetSecSiteLangs       No         - 0 : Don't       Reset the language packs installed at a
                                    reset             secondary site.
                                    - 1 : Reset

Note 1: Supported language values
Use the three-letter code for the server languages or client languages that Configuration
Manager supports. For example, to add support for German on the client, specify the
following key and value pair: AddClientLanguages=DEU

English ( ENG ) is available by default. You don't have to add it, and you can't remove it.

Recover a site

Identification section for site recovery

Depending upon the type of site you're recovering, include the following keys with the
appropriate values in the Identification section:

                                                                               ﾉ   Expand table

<!-- p.959 -->

 Key        Required     Values                         Details
 name

 Action     Yes          - RecoverPrimarySite           - Recover a primary site
                         - RecoverCCAR                  - Recover a CAS

 CDLatest   Yes 3          1 : Setup runs from          When you run setup from the CD.Latest folder,
                         CD.Latest                      include this key and value. This value tells setup
                                                        that you're using media from CD.Latest.

Note 3: CDLatest required
The CDLatest key is only required when you run setup from the CD.Latest folder to
recover a site. For more information, see About the command-line script file.

RecoveryOptions section for site recovery

Include the following keys in the RecoveryOptions section to recover a site:

                                                                                       ﾉ   Expand table

 Key name                      Required    Values             Details

 ServerRecoveryOptions         Yes         - 1 : Site         What components to recover. See note 4
                                           server and
                                           SQL Server
                                           - 2 : Site
                                           server only
                                           - 4 : SQL
                                           Server only

 DatabaseRecoveryOptions       Yes*        - 10 : Restore     Specify how setup recovers the site
                                           from backup        database in SQL Server. * Only required
                                           - 20 :             when ServerRecoveryOptions is 1 or 4 .
                                           Manually
                                           recovered
                                           - 40 : Create
                                           new
                                           database
                                           - 80 : Skip

 ReferenceSite                 Yes*        FQDN               The reference primary site that the CAS
                                                              uses to recover global data. * Only
                                                              required when DatabaseRecoveryOptions
                                                              is 40 . See note 5

<!-- p.960 -->

 Key name                   Required   Values        Details

 SiteServerBackupLocation   No         Directory     The path to the site server backup set. If
                                       path          you don't specify a value, setup reinstalls
                                                     the site without restoring it from a
                                                     backup set.

 BackupLocation             Yes*       Directory     The path to the site database backup set.
                                       path          * Required when ServerRecoveryOptions
                                                     is 1 or 4 , and DatabaseRecoveryOptions
                                                     is 10 .

Note 4: ServerRecoveryOptions value notes
      1 or 2 : To recover the site by using a site backup, specify a value for
      SiteServerBackupLocation . If you don't specify a value, setup reinstalls the site

     without restoring it from a backup set.

      4 : The BackupLocation key is required when you configure a value of 10 for the
      DatabaseRecoveryOptions key, which is to restore the site database from backup.

Note 5: ReferenceSite value notes

     If the database backup is older than the change-tracking retention period, or when
     you recover the site without a backup, specify the reference primary site that the
     CAS uses to recover global data.

     When you don't specify a reference site, and the backup is older than the change-
     tracking retention period, all primary sites are reinitialized with the restored data
     from the CAS.

     When you don't specify a reference site, and the backup is within the change-
     tracking retention period, only changes that are made after the backup are
     replicated from primary sites. When there are conflicting changes from different
     primary sites, the CAS uses the first one that it receives.

Options section for site recovery

Many of the keys in the Options section are also required for site recovery. For more
information, see Options section for site install. The following table summarizes the keys
in the Options section for site recovery:
