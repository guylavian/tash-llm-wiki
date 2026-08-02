---
title: "Core infrastructure documentation — pages 1001-1040"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1001-1040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1001-1040
family: sccm
documentKind: "doc"
abstract: "2. Open Active Directory Users and Computers. 3. In the navigation pane, expand corp.contoso.com, right-click the Service Accounts organizational unit (OU), and then choose New > User. 4. Complete the New Object – User wizard with the following settings, and then choose Finish:"
---

# Core infrastructure documentation — pages 1001-1040

<!-- p.1001 -->

   2. Open Active Directory Users and Computers.

   3. In the navigation pane, expand corp.contoso.com, right-click the Service Accounts
     organizational unit (OU), and then choose New > User.

   4. Complete the New Object – User wizard with the following settings, and then choose
     Finish:

          First name: svc-cm-dmzmpdbconnect
          User logon name: svc-cm-dmzmpdbconnect
          Password: Use a strong, non-expiring password.
          Select Password never expires and clear User must change password at next logon.

   5. Close Active Directory Users and Computers.

To add the installation account to the local Administrators
group on management point server
   1. Sign in to DMZ-MP using a local or domain administrator account.

   2. Open Computer Management, expand Local Users and Groups, and then choose Groups.

   3. Right-click Administrators, and then choose Add to Group.

   4. In the Administrators Properties dialog box, choose Add.

   5. In the Select Users, Computers, Service Accounts or Groups dialog box, enter
     FABRIKAM\svc-cm-dmzmpinstall in the object name box, choose Check Names to validate,

     and then choose OK.

   6. Choose OK to close Administrators Properties.

Step 2: Grant SQL Server database permissions for the
MP connection account
The management point must be able to read and write data in the site database. Grant this
access by adding the svc-cm-dmzmpdbconnect account as a SQL Server login and assigning the
required database roles.

  ） Important

<!-- p.1002 -->

  The MP database connection account must reside in the trusted domain ( corp.contoso.com )
  because it connects to SQL Server ( SQLServer ) in that domain. Specify the account as a
  Windows login using the NetBIOS domain name CORP\svc-cm-dmzmpdbconnect . If name
  resolution fails, use the FQDN format corp.contoso.com\svc-cm-dmzmpdbconnect . For more
  information, see Management point connection account.

To create the SQL Server login and assign database roles
   1. Sign in to SQLServer using a SQL Server administrator account, and open SQL Server
     Management Studio.

   2. In Object Explorer, expand Security, right-click Logins, and then choose New Login.

   3. In the Login – New dialog box, on the General page, complete the following settings:

              Login name: Enter CORP\svc-cm-dmzmpdbconnect .
              Select Windows authentication.

   4. In the left pane of the Login – New dialog box, choose User Mapping.

   5. In the Users mapped to this login list, select the check box next to the Configuration
     Manager site database (for example, CM_P01).

   6. In the Database role membership section at the bottom of the page, select the following
     roles:

              smsdbrole_MP
              smsdbrole_MPUserSvc

   7. Choose OK to create the login.

   8. Close SQL Server Management Studio.

Step 3: Configure firewall rules
The following table lists the minimum firewall rules required for this deployment. Configure these
rules on all network firewalls and host-based Windows Firewall profiles between
corp.contoso.com and branch.fabrikam.com .

                                                                                  ﾉ   Expand table

<!-- p.1003 -->

 Source                Direction    Destination          Protocol   Port       Purpose

 SiteServer (site      →             DMZ-MP              TCP        135        RPC endpoint mapper
 server)                            (management point)

 SiteServer (site      →             DMZ-MP              TCP        49152–     RPC dynamic ports
 server)                            (management point)              65535

 SiteServer (site      ↔             DMZ-MP              TCP        445        SMB (file transfer)
 server)                            (management point)

 DMZ-MP                →             SQLServer (site     TCP        1433       SQL Server (MP
 (management point)                 database)                                  database connection)

   Tip

  If your SQL Server uses a named instance or a non-default port, update the SQL Server row
  in the table accordingly. For more information about all ports that Configuration Manager
  uses, see Ports used in Configuration Manager.

The following connections are required so the management point can authenticate to domain
controllers in the CORP forest, and vice versa. DNS ports aren't included.

                                                                                      ﾉ   Expand table

 Source               Direction    Destination                      Protocol   Port   Purpose

 SiteServer (site     →            DC.branch.fabrikam.com (BRANCH   UDP        389    CLDAP
 server)                           Domain Controller)

 SiteServer (site     →            DC.branch.fabrikam.com (BRANCH   TCP        88     Kerberos
 server)                           Domain Controller)                                 authentication

 DMZ-MP               →            DC.corp.contoso.com (CORP        UDP        389    CLDAP
 (management                       Domain Controller)
 point)

 DMZ-MP               →            DC.corp.contoso.com (CORP        TCP        88     Kerberos
 (management                       Domain Controller)                                 authentication
 point)

   Tip

  Both the site server and the management point must be able to locate a Kerberos Key
  Distribution Center (KDC) in the other domain. To do this, each server must be able to

<!-- p.1004 -->

  resolve DNS SRV records such as _kerberos._tcp.dc._msdcs.corp.contoso.com and
  _kerberos._tcp.dc._msdcs.branch.fabrikam.com .

Step 4: Install prerequisites on management
point server
Before you add the management point role, install the required Windows features and
supporting components on DMZ-MP . For the complete and current list, see Site and site system
prerequisites.

For this example, prepare DMZ-MP with these Windows roles and features:

     Web Server (IIS) role and auto-selected features.
     .NET Framework 3.5 feature.
     .NET Framework 4.8 feature. Windows Server 2022 and later include this version by default.
     IIS Server Extension (in Background Intelligent Transfer Service (BITS)). Select the feature
     and all automatically selected options.
     Web Server (IIS) role services: Windows Authentication, ISAPI Extensions, IIS 6 Metabase
     Compatibility, and IIS 6 WMI Compatibility

To install the required Windows features
   1. Sign in to DMZ-MP using a local or domain administrator account.

   2. Open an elevated Windows PowerShell session.

   3. Run the following command:

       PowerShell

       Install-WindowsFeature NET-Framework-Features, NET-Framework-Core, BITS, BITS-
       IIS-Ext, Web-Server, Web-WebServer, Web-Common-Http, Web-Default-Doc, Web-Dir-
       Browsing, Web-Http-Errors, Web-Static-Content, Web-Health, Web-Http-Logging, Web-
       Log-Libraries, Web-Request-Monitor, Web-Http-Tracing, Web-Performance, Web-Stat-
       Compression, Web-Security, Web-Filtering, Web-Windows-Auth, Web-App-Dev, Web-
       ISAPI-Ext, Web-Http-Redirect, Web-Mgmt-Tools, Web-Mgmt-Console, Web-Mgmt-Compat,
       Web-Metabase, Web-WMI -IncludeManagementTools

  ７ Note

<!-- p.1005 -->

  The .NET Framework 3.5 feature payload is removed from the base OS image on modern
  Windows Server versions.

  For offline environments, you can install .NET Framework 3.5 by using either method:

          PowerShell: Mount Windows Server installation media and run Install-WindowsFeature
          Net-Framework-Core -Source D:\sources\sxs (replace D: with your media drive).

          Add Roles and Features Wizard: In Server Manager > Add Roles and Features, select
          .NET Framework 3.5 Features. On Confirm installation selections, choose Specify an
          alternate source path and enter D:\sources\sxs .

  Use installation media that matches the same Windows Server version as DMZ-MP . For more
  information, see Enable .NET Framework 3.5 by using the Add Roles and Features Wizard
  and Enable .NET Framework 3.5 by using PowerShell.

   4. Restart DMZ-MP if Windows prompts for a restart.

Step 5: Install the management point role
This procedure installs the management point role on DMZ-MP by using the Create Site System
Server wizard. The wizard lets you specify the cross-forest accounts and settings required by the
role.

   1. In the Configuration Manager console, go to the Administration workspace. Expand Site
        Configuration, and then choose Servers and Site System Roles.

   2. On the Home tab, in the Create group, choose Create Site System Server.

   3. On the General page, complete the following settings, and then choose Next:

             Name: Enter the FQDN of the management point server: DMZ-MP.branch.fabrikam.com .

             Site code: Select P01 (or the appropriate site code for your environment).

             Site system installation account: Choose Specify an account, and then enter
             FABRIKAM\svc-cm-dmzmpinstall .

               ） Important

               You must specify a Site System Installation Account when the target server is in
               an untrusted forest. The site server can't use its own computer account to

<!-- p.1006 -->

            authenticate to a server in a forest without trust. For more information, see Site
            system installation account.

4. On the General page, select Require the site server to initiate connections to this site
  system.

    ） Important

     DMZ-MP lacks permissions to connect back to the site server. With this option selected,

    all data transfers are initiated by the site server and use the same Site system
    installation account.

5. On the Proxy page, configure a proxy server if DMZ-MP requires one to reach internet
  endpoints. Otherwise, choose Next.

6. On the System Role Selection page, select Management point, and then choose Next.

7. On the Management Point page, complete the following settings, and then choose Next:

       Client connections: Choose HTTPS to require encrypted client communication
       (requires a PKI web server certificate bound to the IIS Default Web Site on DMZ-MP ) or
       EHTTP.
       Generate alert when the management point is not healthy: Optionally select this to
       receive in-console alerts when the management point is unhealthy.
       Leave other options at their default settings.

8. On the Management Point Database Connection page, complete the following settings,
  and then choose Next:

       Use the site database: This is the default configuration. You don't need to specify the
       SQL Server instance because the site already has this information.
       Management point database connection: Choose Specify an account, and then enter
        corp.contoso.com\svc-cm-dmzmpdbconnect . Use the FQDN format to ensure that the

       management point can resolve the account in the trusted domain and authenticate to
       SQL Server successfully.

            ） Important

<!-- p.1007 -->

              You must specify the Management point connection account when the
              management point is in an untrusted domain or forest because it authenticates
              directly to SQL Server in the trusted domain. Specifying the account in the format
              DomainFQDN\UserName (for example, corp.contoso.com\svc-cm-dmzmpdbconnect )

              helps with name resolution during Kerberos authentication. For more information,
              see Management point connection account.

   9. Review the summary on the Summary page, and then choose Next to complete the wizard.

  10. Choose Close on the Completion page.

  ７ Note

  After you close the wizard, Configuration Manager creates the site system server object and
  begins the background installation of the management point role on DMZ-MP . The installation
  can take several minutes to complete. Monitor the progress as described in Step 6.

Step 6: Verify the management point installation
After the wizard finishes, verify that the management point installed successfully and is healthy
before directing clients to it.

To verify the management point status in the Configuration
Manager console
   1. In the Configuration Manager console, go to the Monitoring workspace. Expand System
     Status, and then choose Component Status.

   2. Locate the SMS_MP_CONTROL_MANAGER component on DMZ-MP.branch.fabrikam.com . In
     the Status column, confirm that the status is OK.

        ７ Note

        It can take up to 30 minutes after the wizard closes for the management point to
        appear healthy. If the status is Warning or Critical, right-click the component, choose
        Show Messages > All, and review the failure details. Then review the log files described
        below.

<!-- p.1008 -->

 3. Repeat the check for the SMS_MP_FILE_DISPATCH_MANAGER component.

To verify the management point installation by reviewing
log files
 1. Sign in to DMZ-MP , and locate the SMS folder at the root of one of the drives.

 2. If the folder doesn't exist, review SiteComp.log on the site server to confirm that the site
   server connected to DMZ-MP and started the installation by using the Site system installation
   account. If the SMS folder is missing, the site server likely can't communicate with DMZ-MP or
   doesn't have permissions to create the folder and install the role.

 3. Review the following log files on DMZ-MP for messages related to management point
   installation and configuration:

                                                                                            ﾉ   Expand table

    Log file        Location on DMZ-MP       What to look for

     MPSetup.log    \SMS\Logs                High-level prerequisite and MP installation messages: in
                                             particular, CcmSetup , msoledbsql.msi , IIS-ASPNET45 feature
                                             and mp.msi .

     MPMSI.log      \SMS\Logs                Details about MP installation and MSI rollback state. If
                                             installation fails with error 1603 , search this file for the
                                             detailed error message.

     CCMSetup.log   %Windir%\CCMSetup\Logs   Client binary installation messages and related
                                             prerequisites (for example, vcredist and Microsoft Policy
                                             Platform). Installation should complete with return code 0 .

     BGBSetup.log   \SMS\Logs                Client Notification Server installation messages: look for
                                             successful completion.

 4. After the MP is installed, the SMS_CCM folder should appear on the same drive as SMS . This
   folder might not appear if the client was installed before the management point. In that
   case, review the CCM\Logs folder for the installed client. Then review the following log files
   on DMZ-MP for messages related to management point communication with the site server
   and site database:

                                                                                            ﾉ   Expand table

<!-- p.1009 -->

    Log file            Location on     What to look for
                        DMZ-MP

     MpControl.log      \SMS\Logs       Regular Management Point and User Service availability checks.
                                        The successful check resembles Call to HttpSendRequestSync
                                        succeeded for port 443 with status code 200, text: OK .

     BGBServer.log      \SMS\Logs       Client Notification (fast channel) server reporting. Typical entries
                                        include the number of connected clients, such as Total online
                                        clients: 100 (TCP: 99 HTTP: 1)~~ .

     MPFDM.log          \SMS\Logs       On DMZ-MP , this log should show minimal activity and include
                                        Remote site is in pull-mode. . On the site server, the same log
                                        should show file-move activity, with entries similar to ~Moved
                                        file... .

     MP_Framework.log   \SMS_CCM\Logs   Database connection messages that use the Management point
                                        connection account, such as Loaded MP settings cache from reg
                                        key HKLM\Software\Microsoft\SMS\MP: Database Settings: . If
                                        errors occur, look for failed authentication or SQL Server
                                        connectivity issues.

To test client communication with the new management point
 1. On a client computer in branch.fabrikam.com , copy the client installation files to a local
   folder. Open an elevated Command Prompt in that folder, and run the following command
   to manually assign the client to the new management point:

     Windows Command Prompt

     ccmsetup.exe SMSSITECODE=P01 SMSMP=DMZ-MP.branch.fabrikam.com

      ７ Note

      If the MP is configured for HTTPS, make sure the client has an enrolled PKI client
      certificate and include the /UsePKICert switch with ccmsetup.exe . For more
      information, see About client installation properties.

 2. Review %Windir%\CCMSetup\Logs\CCMSetup.log to confirm the successful installation.

 3. Review \SMS_CCM\Logs\ClientIDManagerStartup.log to confirm successful client registration.
   Look for messages similar to [RegTask] - Client is registered. Server assigned ClientID
   is GUID:00000000-0000-0000-0000-000000000000. Approval status 1 .

<!-- p.1010 -->

  4. Verify that the client appears in the Configuration Manager console and shows an Online
     icon. Add the Management Point column to the console view to confirm that the client is
     assigned to DMZ-MP.branch.fabrikam.com .

More information
     Add site system roles
     Install site system roles
     Site and site system prerequisites for Configuration Manager
     Communications across Active Directory forests
     Accounts used in Configuration Manager
     PKI certificate requirements for Configuration Manager

Last updated on 05/28/2026

<!-- p.1011 -->

About the service connection point in
Configuration Manager
Article • 07/17/2024

Applies to: Configuration Manager (current branch)

The service connection point is a site system role that provides several important
functions for the hierarchy. Before you set up the service connection point, understand
and plan for its range of uses. Planning for usage might affect how you set up this site
system role:

      Download updates that apply to your Configuration Manager infrastructure. Only
      relevant updates for your infrastructure are made available based on usage data
      you upload.

      Upload usage data from your Configuration Manager infrastructure. You can
      control the level or amount of detail that you upload. For more information, see
      Usage data levels and settings.

      Deploy a cloud management gateway in Azure

      Synchronize apps from the Microsoft Store for Business and Education

      Discover users and groups in Microsoft Entra ID

Each hierarchy supports a single instance of this role. It can only be installed at the top-
tier site of your hierarchy, which is a central administration site (CAS) or stand-alone
primary site. If you expand a stand-alone primary site to a larger hierarchy, uninstall this
role from the primary site, and then install it at the CAS.

Modes of operation
The service connection point supports two modes of operation:

      Online: The service connection point automatically checks every 24 hours for
      updates. It downloads new updates that are available for your current
      infrastructure and product version to make them available in the Configuration
      Manager console.

      Offline: The service connection point doesn't connect to the Microsoft cloud
      service. To manually import available updates, use the service connection tool.

<!-- p.1012 -->

Change mode
If you change between online or offline modes after you install the service connection
point, restart the SMS_DMP_DOWNLOADER thread of the SMS_Executive service.
Restarting this thread makes the change become effective. To restart this thread, use the
Configuration Manager Service Manager.

   Tip

  You can also restart the SMS_Executive service for Configuration Manager, which
  restarts most site components. Alternatively, wait for a scheduled task like a site
  backup, which stops and restarts the SMS_Executive service for you.

To use the Configuration Manager Service Manager to restart the
SMS_DMP_DOWNLOADER thread:

   1. In the Configuration Manager console go to the Monitoring workspace, expand
     System Status, and select the Component Status node. In the ribbon, choose
     Start, and then select Configuration Manager Service Manager.

   2. In the service manager navigation pane, expand the site, expand Components, and
     then choose the component that you want to restart: SMS_DMP_DOWNLOADER.

   3. Go to the Component menu, and choose Query.

   4. Confirm the current status of the component. Then go to the Component menu,
     and choose Stop.

   5. Query the component again to confirm that it stopped. Then choose the Start
     component action to restart it.

Remote site system requirements
When you install the service connection point on a site system server that's remote from
the site server, configure one of the following requirements:

     The computer account of the site server must be a local admin on the computer
     that hosts a remote service connection point.

     or

     Set up the site system server that hosts this role with a site system installation
     account. The distribution manager on the site server uses the site system

<!-- p.1013 -->

     installation account to transfer updates from the service connection point.

Internet access requirements
If your organization restricts network communication with the internet using a firewall or
proxy device, you need to allow the service connection point to access internet
endpoints.

For more information, see Internet access requirements. Other Configuration Manager
features may require additional endpoints from the service connection point.

These configurations apply to the server that hosts the service connection point and any
firewalls between that server and the internet. Allow communication through outgoing
HTTPS port TCP 443 to the internet locations.

The service connection point supports using a web proxy with or without authentication
to use these locations. For more information, see Proxy server support.

If the Configuration Manager site fails to connect to required endpoints for a cloud
service, it raises a critical status message ID 11488. When it can't connect to the service,
the SMS_SERVICE_CONNECTOR component status changes to critical. View detailed
status in the Component Status node of the Configuration Manager console.

Starting in version 2010, the service connection point validates important internet
endpoints for tenant attach. These checks help make sure that the cloud-connected
services are available. It also helps you troubleshoot issues by quickly determining if
network connectivity is a problem. For more information, see Validate internet access.

The specific URLs required by the service connection point vary by Configuration
Manager feature:

     Updates and servicing
     Windows servicing
     Azure services
     Microsoft Store for Business
     Cloud services
     Configuration Manager console
     Tenant attach
     External notifications

   Tip

<!-- p.1014 -->

  The service connection point uses the Microsoft Intune service when it connects to
  go.microsoft.com or manage.microsoft.com . There's a known issue in which the

  Intune connector experiences connectivity issues if the Baltimore CyberTrust Root
  Certificate isn't installed, is expired, or is corrupted on the service connection point.
  For more information, see Service connection point doesn't download updates.

Validate internet access
If you use tenant attach, starting in version 2010, the service connection point now
checks important internet endpoints. These checks help make sure that the cloud-
connected services are available. It also helps you troubleshoot issues by quickly
determining if network connectivity is a problem.

For the list of internet endpoints, see the following section of the Internet access
requirements article: Tenant attach.

For more details, review the EndpointConnectivityCheckWorker.log file on the service
connection point.

A failure isn't always determined by the HTTP status code, but if there's network
connectivity to an endpoint. The following scenarios can cause a check to fail:

     Network connection timeout

     SSL/TLS failure

     Unexpected status code:

                                                                             ﾉ    Expand table

      Status      Description               Possible reason
      code

      407         Proxy authentication      May indicate a proxy issue
                  required

      408         Request timeout           May indicate a proxy issue

      426         Upgrade required          May indicate a TLS misconfiguration

      451         Unavailable for legal     May indicate a proxy issue
                  reasons

      502         Bad gateway               May indicate a proxy issue

<!-- p.1015 -->

         Status   Description                 Possible reason
         code

         511      Network authentication      May indicate a proxy issue
                  required

         598      Network read timeout        Not RFC compliant, but used by some proxy servers
                  error                       to indicate a network timeout

         599      Network connection          Not RFC compliant, but used by some proxy servers
                  timeout error               to indicate a network timeout

There are also the following status messages for the SMS_SERVICE_CONNECTOR
component:

                                                                                  ﾉ   Expand table

 Message ID          Severity            Notes

 11410               Informational       All checks are successful

 11411               Warning             One or more non-critical failures occurred

 11412               Error               One or more critical failures occurred

Install
When you run Setup to install the top-tier site of a hierarchy, you can install the service
connection point.

After setup runs, or if you're reinstalling the role, use the Add Site System Roles wizard
or the Create Site System Server wizard. (Only install the service connection point on
the top-tier site of your hierarchy.) For more information, see Install site system roles.

Move the role
There are several scenarios in which you may need to move the service connection point
to another server:

     Recovery
     Site server high availability
     Site expansion

After you move the service connection point, check all site functions. For example, you
may need to renew the secret key for any connections to Microsoft Entra tenants. For

<!-- p.1016 -->

more information, see Renew secret key.

Console notifications for the service connection
point
Occasionally, the Configuration Manager console may give you a notification about your
service connection point. The notification asks you to restart the SMS_EXECUTIVE service
on the server that hosts the service connection point. This notification occurs because a
configuration change was made by Microsoft on the services that your service
connection point connects to. Features of Configuration Manager that rely on these
services may not function for your site properly until the SMS_EXECUTIVE service is
restarted.

Log files
To view information about uploads to Microsoft, view the Dmpuploader.log on the
server that runs the service connection point. For download progress of updates, view
the Dmpdownloader.log. For the complete list of logs related to the service connection
point, see Log files - Service connection point.

Next steps
Use the following flowcharts to understand the process flow and key log entries. This
process includes update downloads and replication of updates to other sites.

     Flowchart - Download updates

     Flowchart - Update replication

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1017 -->

Configuration options for site system
roles in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Most configuration options for Configuration Manager site system roles are self-
explanatory or are explained in the wizard or dialog boxes when you configure them.
The following sections explain site system roles whose settings might require additional
information.

Certificate registration point

  ２ Warning

  Starting in version 2203, the certificate registration point is no longer supported.
  For more information, see Frequently asked questions about resource access
  deprecation.

For more information about how to set up the certificate registration point, see
Introduction to certificate profiles.

Distribution point
For more information about how to set up the distribution point for content
deployment, see Manage content and content infrastructure.

For more information about how to set up the distribution point for PXE deployments,
see Use PXE to deploy Windows over the network.

For more information about how to set up the distribution point for multicast
deployments, see Use multicast to deploy Windows over the network.

Install and configure IIS if required by Configuration
Manager
Select this option to let Configuration Manager install and set up IIS on the site system if
it's not already installed. IIS must be installed on all distribution points, and you must

<!-- p.1018 -->

select this setting to continue in the wizard.

Site system installation account
For distribution points that are installed on a site server, only the computer account of
the site server is supported for use as the site system installation account. For more
information, see Accounts.

Enrollment point
Enrollment points are used to install macOS computers and enroll devices that you
manage with on-premises mobile device management. For more information, see the
following articles:

     How to deploy clients to Macs

     How users enroll devices with on-premises MDM

Allowed connections
The HTTPS setting is automatically selected and requires a PKI certificate on the server
for server authentication to the enrollment proxy point, and encryption of data over SSL.
For more information, see PKI certificate requirements.

For an example deployment of the server certificate and information about how to
configure it in IIS, see Deploying the web server certificate for site systems that run IIS.

Enrollment proxy point
For more information about how to set up an enrollment proxy point for mobile devices,
see How users enroll devices with on-premises MDM.

Client connections
The HTTPS setting is automatically selected. It requires the following PKI certificates on
the server:

     For server authentication to mobile devices and Mac computers that you enroll
     with Configuration Manager
     For encryption of data over Secure Sockets Layer (SSL)

<!-- p.1019 -->

For more information about the certificate requirements, see PKI certificate
requirements.

For an example deployment of the server certificate and information about how to
configure it in IIS, see Deploying the web server certificate for site systems that run IIS.

Fallback status point

Number of state messages and Throttle interval (in
seconds)
The default settings for these options are 10,000 state messages and 3,600 seconds for
the throttle interval. While these settings are sufficient for most circumstances, you
might have to change them when both of the following conditions are true:

     The fallback status point accepts connections only from the intranet.

     You use the fallback status point during a client deployment rollout for many
     computers.

In this scenario, a continuous stream of state messages might create a backlog of state
messages that causes high processor usage on the site server for a sustained period. In
addition, you might not see up-to-date information about the client deployment in the
Configuration Manager console and in the client deployment reports.

These fallback status point settings are designed to be set up for state messages that
are generated during client deployment. The settings aren't designed to be set up for
client communication issues, like when clients on the internet can't connect to their
internet-based management point. Because the fallback status point can't apply these
settings just to the state messages that are generated during client deployment, don't
configure these settings when the fallback status point accepts connections from the
internet.

Each computer that successfully installs the Configuration Manager client sends the
following four state messages to the fallback status point:

     Client deployment started

     Client deployment succeeded

     Client assignment started

     Client assignment succeeded

<!-- p.1020 -->

Computers that can't be installed or that assign the Configuration Manager client send
additional state messages.

For example, if you deploy the Configuration Manager client to 20,000 computers, the
deployment might send 80,000 state messages to the fallback status point. Because the
default throttling configuration lets 10,000 state messages to be sent to the fallback
status point each 3,600 seconds (1 hour), state messages might become backlogged on
the fallback status point. Also consider the available network bandwidth between the
fallback status point and the site server and the processing power of the site server to
process many state messages.

To help prevent these issues, consider an increase in the number of state messages and
a decrease in the throttle interval.

Reset the throttle values for the fallback status point if either of the following conditions
is true:

      You calculate that the current throttle values are higher than required to process
      state messages from the fallback status point.

      You find that the current throttle settings create high processor usage on the site
      server.

Don't change the settings for the fallback status point throttle settings unless you
understand the consequences. For example, when you increase the throttle settings to
high, the processor usage on the site server can increase to high, which slows down all
site operations.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1021 -->

Database replicas for management
points for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager primary sites can use a database replica to reduce the CPU load
placed on the site database server by management points as they service requests from
clients. When a management point uses a database replica, it requests data from the
SQL Server computer that hosts the database replica instead of from the site database
server.

This configuration can help reduce the CPU processing requirements on the site
database server by offloading frequent processing tasks related to clients. An example
of frequent processing tasks for clients includes sites where there are a large number of
clients that make frequent requests for client policy.

About
      Replicas are a partial copy of the site database that replicates to a separate
      instance of SQL Server.

          Primary sites support a dedicated database replica for each management point
          at the site.

          Secondary sites don't support database replicas.

          A single database replica can be used by more than a one management point
          from the same site.

          A SQL Server can host multiple database replicas for use by different
          management points so long as each runs in a separate instance of SQL Server.

      Replicas synchronize a copy of the site database on a fixed schedule from data that
      the site's database server publishes for this purpose.

      You can configure management points to use a replica when you install it, or at a
      later time. For an existing management point, reconfigure it to use the database
      replica.

      Regularly monitor the site database server and each database replica server to
      make sure that replication occurs between them. Make sure that the performance

<!-- p.1022 -->

     of the database replica server is sufficient for the site and client performance that
     you require.

Prerequisites

SQL Server requirements
     The SQL Server that hosts the database replica has the same requirements as the
     site database server. The replica server doesn't need to run the same version or
     edition of SQL Server as the site database server, as long as it runs a supported
     version and edition of SQL Server. For more information, see Support for SQL
     Server versions.

     The SQL Server service on the computer that hosts the replica database must run
     as the System account.

     Both the SQL Server that hosts the site database and that hosts a database replica
     must have SQL Server replication installed.

     The site database must publish the database replica, and each remote database
     replica server must subscribe to the published data.

     Configure both SQL Servers to support a max text repl size of 2 GB. For more
     information and how to configure this setting for SQL Server, see Configure the
     max text repl size Server Configuration Option.

Self-signed certificate
To configure a database replica, create a self-signed certificate on the database replica
server. Make this certificate available to each management point that will use that
database replica server.

     The certificate is automatically available to a management point that's installed on
     the database replica server.

     To make this certificate available to remote management points, first export the
     certificate. Then add it to the Trusted People certificate store on the remote
     management point.

Client notification

<!-- p.1023 -->

To support client notification with a database replica for a management point, configure
communication between the site database server and the database replica server for the
SQL Server Service Broker:

     Configure each database with information about the other database.

     Exchange certificates between the two databases for secure communication.

Limitations
     When you configure the site to publish database replicas, use the following
     procedures instead of the normal guidance:

        Uninstall a site server that publishes a database replica

        Move a site server database that publishes a database replica

     User deployments in Software Center won't work against a management point
     using a SQL Server replica.

     Upgrades to Configuration Manager current branch: Before you upgrade a site,
     either from System Center 2012 Configuration Manager to Configuration Manager
     current branch or updating Configuration Manager current branch to the latest
     release, disable database replicas for management points. After your site upgrades,
     you can reconfigure the database replicas for management points.

     Multiple replicas on a single SQL Server: If you configure separate instances of a
     database replica server to host multiple database replicas for management points,
     use a modified configuration script. As noted in step 4 of the process to Configure
     database replicas, this action prevents overwriting the self-signed certificate in use
     by previously configured database replicas on that server.

Configure
To configure a database replica, the following steps are required:

     Step 1 - Configure the site database server to Publish the database replica

     Step 2 - Configuring the database replica server

     Step 3 - Configure management points to use the database replica

     Step 4 -Configure a self-signed certificate for the database replica server

<!-- p.1024 -->

     Step 5 - Configure the SQL Server Service Broker for the database replica server

Step 1 - Configure the site database server to publish the
database replica
Use the following procedure as an example of how to configure the site database server
to publish the database replica. The specific steps might vary depending upon the
version of Windows Server.

Do the following steps on the site database server:

   1. Set the SQL Server Agent to automatically start.

   2. Create a local user group with the name ConfigMgr_MPReplicaAccess. For each
     database replica server that you use at this site, add its computer account to this
     group. This action enables those database replica servers to synchronize with the
     published database replica.

       ７ Note

       You can also create a domain group for this purpose.

   3. Configure a file share with the name ConfigMgr_MPReplica.

   4. Add the following permissions to the ConfigMgr_MPReplica share:

       ７ Note

       If the SQL Server Agent uses an account other than the local system account,
       replace SYSTEM with that account name in the following list.

          Share permissions:

             SYSTEM: Change

             ConfigMgr_MPReplicaAccess: Read

          NTFS permissions:

             SYSTEM: Full Control

             ConfigMgr_MPReplicaAccess: Read, Read & execute, and List folder
             contents

<!-- p.1025 -->

   5. Use SQL Server Management Studio to connect to the site database and run the
     following stored procedure as a query: spCreateMPReplicaPublication

       ７ Note

       If you're using a domain group instead of a local group, change this SQL
       statement to: EXEC spCreateMPReplicaPublication
       N'<DomainName>\ConfigMgr_MPReplicaAccess'

When the stored procedure completes, the site database server is configured to publish
the database replica.

Step 2 - Configure the database replica server
Use the following procedure as an example of how to configure a database replica
server. The specific steps might vary depending upon the version of Windows Server.

Do the following steps on the database replica server:

   1. Set the SQL Server Agent to automatic startup.

   2. Use SQL Server Management Studio to connect to the local server. Browse to the
     Replication folder, select Local Subscriptions, and then select New Subscriptions.
     This action starts the New Subscription Wizard.

      a. On the Publication page, select Find SQL Server Publisher. Enter the name of
        the site database server, and then select Connect.

     b. Select ConfigMgr_MPReplica, and then select Next.

      c. On the Distribution Agent Location page, select Run each agent at its
        Subscriber (pull subscriptions), and then select Next.

     d. On the Subscribers page, do one of the following actions:

             Select an existing database from the database replica server to use for the
             database replica, and then select OK.

             Select New database to create a new database for the database replica.
             On the New Database page, specify a database name, and then select OK.

      e. Select Next to continue.

<!-- p.1026 -->

f. On the Distribution Agent Security page, select the properties button (...) in the
  Subscriber Connection row of the dialog box. Then configure the security
  settings for the connection.

     Tip

    The properties button, (...), is in the fourth column of the display box.

    Configure the account that runs the Distribution Agent process (process
    account):

       If the SQL Server Agent runs as local system, select Run under the SQL
       Server Agent service account (This is not a recommended security best
       practice.)

       If the SQL Server Agent runs by using a different account, select Run
       under the following Windows account, and then configure that account.
       You can specify a Windows account or a SQL Server account.

       ） Important

       Grant the account that runs the Distribution Agent permissions to the
       publisher as a pull subscription. For more information about configuring
       these permissions, see Distribution agent security.

    For Connect to the Distributor, select By impersonating the process
    account.

    For Connect to the Subscriber, select By impersonating the process
    account.

    After you configure the connection security settings, select OK to save them,
    and then select Next.

a. On the Synchronization Schedule page, select Define schedule, and then
  configure the New Job Schedule. Set the frequency to occur Daily, recur every 5
  minute(s), and the duration to have No end date. Select Next to save the
  schedule, and then select Next again.

b. On the Wizard Actions page, enable the option to Create the subscriptions(s),
  and then select Next.

c. Complete the wizard.

<!-- p.1027 -->

   3. Immediately after completing the New Subscription Wizard, use SQL Server
     Management Studio to connect to the database replica server database. Run the
     following query to enable the TRUSTWORTHY database property: ALTER DATABASE
     <MP Replica Database Name> SET TRUSTWORTHY ON;

   4. Review the synchronization status to validate that the subscription is successful:

           On the subscriber computer:

             In SQL Server Management Studio, connect to the database replica
             server, and expand Replication.

             Expand Local Subscriptions, right-click the subscription to the site
             database publication, and then select View Synchronization Status.

           On the publisher computer:
             In SQL Server Management Studio, connect to the site database
             computer, right-click the Replication folder, and then select Launch
             Replication Monitor.

   5. To enable common language runtime (CLR) integration for the database replica,
     use SQL Server Management Studio to connect to the database replica on the
     database replica server. Run the following stored procedure as a query: exec
     sp_configure 'clr enabled', 1; RECONFIGURE WITH OVERRIDE

   6. For each management point that uses a database replica server, add that
     management points computer account to the local Administrators group on that
     database replica server.

        Tip

       This step isn't necessary for a management point that runs on the database
       replica server.

The database replica is now ready for a management point to use.

Step 3 - Configure management points to use the
database replica
You can configure a management point at a primary site to use a database replica when
you install the management point role, or you can reconfigure an existing management
point to use a database replica.

<!-- p.1028 -->

Use the following information to configure a management point to use a database
replica:

      To configure a new management point:

           1. On the Management Point Database page of the wizard to install the
             management point, select Use a database replica.
           2. Specify the FQDN of the computer that hosts the database replica.
           3. For the ConfigMgr site database name, specify the database name of the
             database replica on that computer.

      To configure a previously installed management point:

           1. Open the properties page of the management point, and switch to the
             Management Point Database tab.
           2. Select Use a database replica, and then specify the FQDN of the computer
             that hosts the database replica.
           3. Next, for ConfigMgr site database name, specify the database name of the
             database replica on that computer.

For each management point that uses a database replica, manually add the computer
account of the management point server to the db_datareader role for the database
replica.

In addition to configuring the management point to use the database replica server,
enable Windows Authentication in IIS on the management point:

   1. Open Internet Information Services (IIS) Manager.

   2. Select the website used by the management point, and open Authentication.

   3. Set Windows Authentication to Enabled, and then close Internet Information
      Services (IIS) Manager.

Step 4 -Configure a self-signed certificate for the
database replica server
Use the following procedures as an example of how to configure the self-signed
certificate on the database replica server. The specific steps might vary depending upon
the version of Windows Server.

Configure a self-signed certificate for the database replica server

<!-- p.1029 -->

1. On the database replica server, open a PowerShell command prompt with
  administrative privileges, and then run the following command: Set-
  ExecutionPolicy Unrestricted

2. Copy the following PowerShell script and save it as a file with the name
  CreateMPReplicaCert.ps1. Place a copy of this file in the root folder of the system
  partition of the database replica server.

    ） Important

    If you're configuring more than one database replica on a single SQL Server,
    for each subsequent replica you configure, use a modified version of this
    script for this procedure. For more information, see Supplemental script for
    additional database replicas on a single SQL Server.

    PowerShell

     # Script for creating a self-signed certificate for the local machine
     and configuring SQL Server to use it.

     Param($SQLInstance)

     $ConfigMgrCertFriendlyName = "ConfigMgr SQL Server Identification
     Certificate"

     # Get local computer name
     $computerName = "$env:computername"

     # Get the SQL Server name
     #$key="HKLM:\SOFTWARE\Microsoft\SMS\MP"
     #$value="SQL Server Name"
     #$sqlServerName= (Get-ItemProperty $key).$value
     #$dbValue="Database Name"
     #$sqlInstance_DB_Name= (Get-ItemProperty $key).$dbValue

     $sqlServerName = [System.Net.Dns]::GetHostByName("localhost").HostName
     $sqlInstanceName = "MSSQLSERVER"
     $SQLServiceName = "MSSQLSERVER"

     if ($SQLInstance -ne $Null)
     {
         $sqlInstanceName = $SQLInstance
         $SQLServiceName = "MSSQL$" + $SQLInstance
     }

     # Delete existing cert if one exists
     function Get-Certificate($storename, $storelocation)
     {
         $store=new-object

<!-- p.1030 -->

System.Security.Cryptography.X509Certificates.X509Store($storename,$sto
relocation)

$store.Open([Security.Cryptography.X509Certificates.OpenFlags]::ReadWri
te)
    $store.Certificates
}

$cert = Get-Certificate "My" "LocalMachine" | ?{$_.FriendlyName -eq
$ConfigMgrCertFriendlyName}
if($cert -is [Object])
{
    $store = new-object
System.Security.Cryptography.X509Certificates.X509Store("My","LocalMach
ine")

$store.Open([Security.Cryptography.X509Certificates.OpenFlags]::ReadWri
te)
    $store.Remove($cert)
    $store.Close()

    # Remove this cert from Trusted People too...
    $store = new-object
System.Security.Cryptography.X509Certificates.X509Store("TrustedPeople"
,"LocalMachine")

$store.Open([Security.Cryptography.X509Certificates.OpenFlags]::ReadWri
te)
    $store.Remove($cert)
    $store.Close()
}

# Create the new cert
$name = new-object -com "X509Enrollment.CX500DistinguishedName.1"
$name.Encode("CN=" + $sqlServerName, 0)

$key = new-object -com "X509Enrollment.CX509PrivateKey.1"
$key.ProviderName = "Microsoft RSA SChannel Cryptographic Provider"
$key.KeySpec = 1
$key.Length = 1024
$key.SecurityDescriptor = "D:PAI(A;;0xd01f01ff;;;SY)
(A;;0xd01f01ff;;;BA)(A;;0x80120089;;;NS)"
$key.MachineContext = 1
$key.Create()

$serverauthoid = new-object -com "X509Enrollment.CObjectId.1"
$serverauthoid.InitializeFromValue("1.3.6.1.5.5.7.3.1")
$ekuoids = new-object -com "X509Enrollment.CObjectIds.1"
$ekuoids.add($serverauthoid)
$ekuext = new-object -com
"X509Enrollment.CX509ExtensionEnhancedKeyUsage.1"
$ekuext.InitializeEncode($ekuoids)

$cert = new-object -com
"X509Enrollment.CX509CertificateRequestCertificate.1"

<!-- p.1031 -->

$cert.InitializeFromPrivateKey(2, $key, "")
$cert.Subject = $name
$cert.Issuer = $cert.Subject
$cert.NotBefore = get-date
$cert.NotAfter = $cert.NotBefore.AddDays(3650)
$cert.X509Extensions.Add($ekuext)
$cert.Encode()

$enrollment = new-object -com "X509Enrollment.CX509Enrollment.1"
$enrollment.InitializeFromRequest($cert)
$enrollment.CertificateFriendlyName = "ConfigMgr SQL Server
Identification Certificate"
$certdata = $enrollment.CreateRequest(0x1)
$enrollment.InstallResponse(0x2, $certdata, 0x1, "")

# Add this cert to the trusted peoples store
[Byte[]]$bytes = [System.Convert]::FromBase64String($certdata)

$trustedPeople = new-object
System.Security.Cryptography.X509certificates.X509Store
"TrustedPeople", "LocalMachine"
$trustedPeople.Open([Security.Cryptography.X509Certificates.OpenFlags]:
:ReadWrite)
$trustedPeople.Add([Security.Cryptography.X509Certificates.X509Certific
ate2]$bytes)
$trustedPeople.Close()

# Get thumbprint from cert
$sha = new-object
System.Security.Cryptography.SHA1CryptoServiceProvider
$certHash = $sha.ComputeHash($bytes)
$certHashCharArray = "";
$certThumbprint = "";

# Format the bytes into a hexadecimal string
foreach($byte in $certHash)
{
    $temp = ($byte | % {"{0:x}" -f $_}) -join ""
    $temp = ($temp | % {"{0,2}" -f $_})
    $certHashCharArray = $certHashCharArray+ $temp;
}
$certHashCharArray = $certHashCharArray.Replace(' ', '0');

# SQL Server needs the thumbprint in lower case
foreach($char in $certHashCharArray)
{
    [System.String]$myString = $char;
    $certThumbprint = $certThumbprint + $myString.ToLower();
}

# Configure SQL Server to use this cert
$path = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\Instance
Names\SQL"
$subKey = (Get-ItemProperty $path).$sqlInstanceName
$realPath = "HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\" + $subKey

<!-- p.1032 -->

         + "\MSSQLServer\SuperSocketNetLib"
         $certKeyName = "Certificate"
         Set-ItemProperty -path $realPath -name $certKeyName -Type string -Value
         $certThumbprint

         # restart SQL Server service
         Restart-Service $SQLServiceName -Force

   3. On the database replica server, run the following command that applies to the
      configuration of your SQL Server:

               For a default instance of SQL Server: Enter the following command in the
               PowerShell session: .\CreateMPReplicaCert.ps1 . When the script runs, it
               creates the self-signed certificate and configures SQL Server to use the
               certificate.

               For a named instance of SQL Server: Use PowerShell to run the following
               command: .\CreateMPReplicaCert.ps1 <SQL Server instance name>

      After the script completes, verify that the SQL Server Agent is running. If not,
      restart the SQL Server Agent.

Configure remote management points to use the self-signed
certificate of the database replica server

Do the following steps on the database replica server to export the server's self-signed
certificate:

   1. Go to the Start menu, select Run, and type mmc.exe . In the empty console, select
      File, and then select Add/Remove Snap-in.

   2. In the Add or Remove Snap-ins dialog box, select Certificates from the list of
      Available snap-ins, and then select Add.

   3. In the Certificate snap-in dialog box, select Computer account, and then select
      Next.

   4. In the Select Computer dialog box, make sure that Local computer: (the
      computer this console is running on) is selected, and then select Finish.

   5. In the Add or Remove Snap-ins dialog box, select OK.

   6. In the console, expand Certificates (Local Computer), expand Personal, and select
      Certificates.

<!-- p.1033 -->

   7. Right-click the certificate with the friendly name of ConfigMgr SQL Server
     Identification Certificate, select All Tasks, and then select Export.

   8. Complete the Certificate Export Wizard with the default options. Save the
     certificate with the .cer file name extension.

Do the following steps on the management point server to add the self-signed
certificate for the database replica server to the Trusted People certificate store:

   1. Repeat the preceding steps to open the Certificate snap-in MMC on the
     management point computer.

   2. In the Certificates console, expand Certificates (Local Computer), expand Trusted
     People, right-click Certificates, select All Tasks, and then select Import. This action
     starts the Certificate Import Wizard.

   3. On the File to Import page, select the saved certificate, and then select Next.

   4. On the Certificate Store page, select Place all certificates in the following store,
     with the Certificate store set to Trusted People, and then select Next.

   5. Select Finish to close the wizard and complete the certificate configuration on the
     management point.

Step 5 - Configure the SQL Server Service Broker for the
database replica server
To support client notification with a database replica for a management point, configure
communication between the site database server and the database replica server for the
SQL Server Service Broker. Configure each database with information about the other
database, and to exchange certificates between the two databases for secure
communication.

  ７ Note

  Before you can use the following procedure, the database replica server must
  successfully complete the initial synchronization with the site database server.

The following procedure doesn't modify the Service Broker port that's configured in SQL
Server for the site database server or the database replica server. This procedure
configures each database to communicate with the other database by using the correct
Service Broker port.

<!-- p.1034 -->

Use the following procedure to configure the Service Broker for the site database server
and the database replica server:

   1. Use SQL Server Management Studio to connect to the replica server database.
     Then run the following query to enable the Service Broker on the database replica
     server: ALTER DATABASE <Replica Database Name> SET ENABLE_BROKER,
     HONOR_BROKER_PRIORITY ON WITH ROLLBACK IMMEDIATE

   2. On the database replica server, configure the Service Broker for client notification
     and export the Service Broker certificate. Run a SQL Server stored procedure that
     configures the Service Broker and exports the certificate as a single action. When
     you run the stored procedure, specify the FQDN of the database replica server, the
     name of the database replicas database, and specify a location for the export of
     the certificate file.

     Run the following query to configure the required details on the database replica
     server, and to export the certificate for the database replica server: EXEC
     sp_BgbConfigSSBForReplicaDB '<Replica SQL Server FQDN>', '<Replica Database

     Name>', '<Certificate Backup File Path>'

       ７ Note

       When the database replica server isn't on the default instance of SQL Server,
       also specify the instance name with the replica database name. In the example
       command, replace <Replica Database Name> with <Instance name>\<Replica
       Database Name> .

     After you export the certificate from the database replica server, place a copy of
     the certificate on the primary site database server.

   3. Use SQL Server Management Studio to connect to the primary site database. After
     you connect to the primary sites database, run a query to import the certificate
     and specify the Service Broker port that's in use on the database replica server, the
     FQDN of the database replica server, and name of the database replicas database.
     This action configures the primary sites database to use the Service Broker to
     communicate to the database of the database replica server.

     Run the following query to import the certificate from the database replica server
     and specify the required details: EXEC sp_BgbConfigSSBForRemoteService 'REPLICA',
     '<SQL Service Broker Port>', '<Certificate File Path>', '<Replica SQL Server

     FQDN>', '<Replica Database Name>'

<!-- p.1035 -->

        ７ Note

        When the database replica server isn't on the default instance of SQL Server,
        also specify the instance name with the replica database name. In the example
        command, replace <Replica Database Name> with <Instance name>\<Replica
        Database Name> .

   4. On the site database server, run the following command to export the certificate
     for the site database server: EXEC sp_BgbCreateAndBackupSQLCert '<Certificate
     Backup File Path>'

     After you export the certificate from the site database server, place a copy of the
     certificate on the database replica server.

   5. Use SQL Server Management Studio to connect to the replica server database.
     After you connect to the replica server database, run a query to import the
     certificate and specify the site code of the primary site and the Service Broker port
     that's in use on the site database server. This action configures the database
     replica server to use the Service Broker to communicate to the database of the
     primary site.

     Run the following query to import the certificate from the site database server:
      EXEC sp_BgbConfigSSBForRemoteService '<Site Code>', '<SQL Service Broker
     Port>', '<Certificate File Path>'

A few minutes after you complete the configuration of the site database and the
database replica database, the notification manager at the primary site sets up the
Service Broker conversation for client notification from the primary site database to the
database replica.

Supplemental script for other database replicas on a
single SQL Server
When you use the script from step 4 to configure a self-signed certificate for the
database replica server on a SQL Server that already has a database replica you plan to
continue using, use a modified version of the original script. The following modifications
prevent the script from deleting an existing certificate on the server, and create
subsequent certificates with unique friendly names. Edit the original script as follows:

     Comment out each line between the script entries # Delete existing cert if one
     exists and # Create the new cert . Add a pound sign ( # ) as the first character of

<!-- p.1036 -->

     each applicable line.

     For each subsequent database replica you use this script to configure, update the
     friendly name for the certificate. Edit the line $enrollment.CertificateFriendlyName
     = "ConfigMgr SQL Server Identification Certificate" and replace ConfigMgr SQL

     Server Identification Certificate with a new name. For example, ConfigMgr SQL

     Server Identification Certificate1 .

Manage database replica configurations
When you use a database replica at a site, use the information in the following sections
to supplement the process of uninstalling a database replica, uninstalling a site that uses
a database replica, or moving the site database to a new installation of SQL Server.
When delete publications, use the guidance for deleting transactional replication for the
version of SQL Server that you use for the database replica. For more information, see
Delete a Publication.

  ７ Note

  After you restore a site database that was configured for database replicas, before
  you can use the database replicas, reconfigure each database replica and recreate
  both the publications and subscriptions.

Uninstall a database replica
When you use a database replica for a management point, you might need to uninstall
it and then reconfigure it for use. For example, remove database replicas before you
update Configuration Manager to the latest version. After the site update completes,
restore the database replica for use.

Use the following steps to uninstall a database replica.

   1. In the Administration workspace of the Configuration Manager console, expand
     Site Configuration, then select Servers and Site System Roles. In the details pane,
     select the site system server that hosts the management point that uses the
     database replica you will uninstall.

   2. In the Site System Roles pane, select the Management point role. In the ribbon,
     on the Site Role tab, select Properties.

<!-- p.1037 -->

   3. Switch to the Management Point Database tab. Select Use the site database to
     configure the management point to use the site database instead of the database
     replica. Select OK to save the configuration.

   4. Use SQL Server Management Studio to do the following tasks:

           Delete the publication for the database replica from the site server database.

           Delete the subscription for the database replica from the database replica
           server.

           Delete the replica database from the database replica server.

           Disable publishing and distribution on the site database server. To disable
           publishing and distribution, right-click the Replication folder and select
           Disable Publishing and Distribution.

After you delete the publication, subscription, the replica database, and disable
publishing on the site database server, the database replica is uninstalled.

Uninstall a site server that publishes a database replica
Before you uninstall a site that publishes a database replica, use the following steps to
clean up the publication and any subscriptions.

   1. Use SQL Server Management Studio to delete the database replica publication
     from the site server database.

   2. Use SQL Server Management Studio to delete the database replica subscription
     from each remote SQL Server that hosts a database replica for this site.

   3. Uninstall the site.

Move a site server database that publishes a database
replica
When you move the site database to a new computer, use the following steps:

   1. Use SQL Server Management Studio to delete the publication for the database
     replica from the site server database.

   2. Use SQL Server Management Studio to delete the subscription for the database
     replica from each database replica server for this site.

<!-- p.1038 -->

   3. Move the database to the new SQL Server computer. For more information, see
     Modify the site database configuration.

   4. Recreate the publication for the database replica on the site database server. For
     more information, see Step 1 - Configure the site database server to Publish the
     database replica.

   5. Recreate the subscriptions for the database replica on each database replica server.
     For more information, see Step 2 - Configuring the database replica server.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1039 -->

Site components for Configuration
Manager
Article • 03/28/2024

Applies to: Configuration Manager (current branch)

For each Configuration Manager site, you can configure site components to modify the
behavior of site system roles and site status reporting. Site component configurations
apply to a site, and to each instance of an applicable site system role at the site.

In the Configuration Manager console, go to the Administration workspace, expand Site
Configuration, and select the Sites node. Select a site. In the Settings group of the
ribbon, choose Configure Site Components. Select one of the following options:

      Software distribution
      Software update point
      OS deployment
      Management point
      Status reporting
      Email notification
      Collection membership evaluation

About site components
Most options for the various site components are self-explanatory when viewed in the
Configuration Manager console. However, the following details can help explain some of
the more complex configurations, or direct you to other content.

  ７ Note

  The available options for some components vary whether you select the central
  administration site, a primary site, or a secondary site. Some components are not
  available at all for certain types of sites.

Software distribution

Content distribution settings

<!-- p.1040 -->

On the General tab, specify settings that modify how the site server transfers content to
its distribution points. When you increase the values you use for concurrent distribution
settings, content distribution can use more network bandwidth.

  ７ Note

  Don't increase Maximum number of packages 3 (default) in concurrent distribution
  settings when the content are distributed to CMG CDP.

Pull distribution point
For more information, see Use a pull-distribution point.

Network access account
For more information, see Network access account.

Automate software distribution site component with PowerShell
To programmatically view and configure the Software distribution site component, use
the following PowerShell cmdlets:

     Get-CMSoftwareDistributionComponent
     Set-CMSoftwareDistributionComponent

Software update point
For more information, see Install a software update point.

Automate software update point site component with PowerShell

To programmatically view and configure the Software update point site component, use
the following PowerShell cmdlets:

     Get-CMSoftwareUpdatePointComponent
     Set-CMSoftwareUpdatePointComponent

OS deployment
For more information, see Specify the drive for offline OS image servicing.
