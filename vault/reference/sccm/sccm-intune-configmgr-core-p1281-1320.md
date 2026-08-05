---
title: "Core infrastructure documentation — pages 1281-1320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1281-1320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1281-1320
family: sccm
documentKind: "doc"
abstract: "the service. By default this value is https://ConfigMgrService . Change the default to one of the following recommended formats: api://{tenantId}/{string} , for example, api://5e97358c-d99c-4558-af0c- de7774091dda/ConfigMgrService https://{verifiedCustomerDomain}/{string} , for"
---

# Core infrastructure documentation — pages 1281-1320

<!-- p.1281 -->

     the service. By default this value is https://ConfigMgrService . Change the default
     to one of the following recommended formats:
         api://{tenantId}/{string} , for example, api://5e97358c-d99c-4558-af0c-
        de7774091dda/ConfigMgrService

         https://{verifiedCustomerDomain}/{string} , for example,

         https://contoso.onmicrosoft.com/ConfigMgrService

     Secret Key validity period: choose either 1 year or 2 years from the drop-down list.
     One year is the default value.

        ７ Note

        You may see an option for Never, but Microsoft Entra no longer supports it. If
        you previously selected this option, the expiration date is now set for 99 years
        from the date you created it.

Select Sign in to authenticate to Azure as an administrative user. These credentials
aren't saved by Configuration Manager. This persona doesn't require permissions in
Configuration Manager, and doesn't need to be the same account that runs the Azure
Services Wizard. After successfully authenticating to Azure, the page shows the
Microsoft Entra tenant Name for reference.

Select OK to create the web app in Microsoft Entra ID and close the Create Server
Application dialog. This action returns to the Server app dialog.

  ７ Note

  If you have a Microsoft Entra Conditional Access policy defined and applies to All
  Cloud apps - you must exclude the created Server Application from this policy. For
  more information on how to exclude specific apps, see Microsoft Entra Conditional
  Access Documentation.

Native Client app
This app is the Microsoft Entra ID type Native, also referred to as a client app in
Configuration Manager.

Client App dialog

<!-- p.1282 -->

When you select Browse for the Native Client app on the App page of the Azure
Services Wizard, it opens the Client App dialog. It displays a list that shows the following
properties of any existing native apps:

     Tenant friendly name
     App friendly name
     Service Type

There are three actions you can take from the Client App dialog:

     To reuse an existing native app, select it from the list.
     Select Import to open the Import apps dialog.
     Select Create to open the Create Client Application dialog.

After you select, import or create a native app, choose OK to close the Client App
dialog. This action returns to the App page of the Azure Services Wizard.

Import apps dialog (client)

When you select Import from the Client App dialog, it opens the Import apps dialog.
This page lets you enter information about a Microsoft Entra native app that is already
created in the Azure portal. It imports metadata about that native app into
Configuration Manager. Specify the following information:

     Application Name: A friendly name for the app.
     Client ID: The Application (client) ID value of the app registration. The format is a
     standard GUID.

After entering the information, select Verify. Then select OK to close the Import apps
dialog. This action returns to the Client App dialog.

   Tip

  When you register the app in Microsoft Entra ID, you may need to manually specify
  the following Redirect URI: ms-appx-web://Microsoft.AAD.BrokerPlugin/<ClientID> .
  Specify the app's client ID GUID, for example: ms-appx-
  web://Microsoft.AAD.BrokerPlugin/a26a653e-17aa-43eb-ab36-0e36c7d29f49 .

Create Client Application dialog
When you select Create from the Client App dialog, it opens the Create Client
Application dialog. This page automates the creation of a native app in Microsoft Entra

<!-- p.1283 -->

ID. Specify the following information:

     Application Name: A friendly name for the app.
     Reply URL: This value isn't used by Configuration Manager, but required by
     Microsoft Entra ID. By default this value is https://ConfigMgrService .

Select Sign in to authenticate to Azure as an administrative user. These credentials
aren't saved by Configuration Manager. This persona doesn't require permissions in
Configuration Manager, and doesn't need to be the same account that runs the Azure
Services Wizard. After successfully authenticating to Azure, the page shows the
Microsoft Entra tenant Name for reference.

Select OK to create the native app in Microsoft Entra ID and close the Create Client
Application dialog. This action returns to the Client App dialog.

Configuration or Discovery
After specifying the web and native apps on the Apps page, the Azure Services Wizard
proceeds to either a Configuration or Discovery page, depending upon the service to
which you're connecting. The details of this page vary from service to service. For more
information, see one of the following articles:

     Cloud Management service, Discovery page: Configure Microsoft Entra user
     Discovery

     Log Analytics Connector service, Configuration page: Configure the connection to
     Log Analytics

     Microsoft Store for Business service, Configurations page: Configure Microsoft
     Store for Business synchronization

Finally, complete the Azure Services Wizard through the Summary, Progress, and
Completion pages. You've completed the configuration of an Azure service in
Configuration Manager. Repeat this process to configure other Azure services.

Update application settings
To allow your Configuration Manager clients to request an Microsoft Entra device token
and to enable the Reading directory data permissions, you need to update the web
server application settings.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Microsoft Entra tenants node.

<!-- p.1284 -->

   2. Select the Microsoft Entra tenant for the application you want to update.
   3. In the Applications section, select your Microsoft Entra web server application,
     then select Update Application Settings from the ribbon.
   4. When prompted for confirmation, select Yes to confirm you want to update the
     application with the latest settings.

Renew secret key
You need to renew the Microsoft Entra app's secret key before the end of its validity
period. If you let the key expire, Configuration Manager can't authenticate with
Microsoft Entra ID, which will cause your connected Azure services to stop working.

Starting in version 2006, the Configuration Manager console displays notifications for
the following circumstances:

     One or more Microsoft Entra app secret keys will expire soon
     One or more Microsoft Entra app secret keys have expired

To mitigate both cases, renew the secret key.

For more information on how to interact with these notifications, see Configuration
Manager console notifications.

  ７ Note

  You need to have at least the "Cloud Application Administrator" Microsoft Entra
  role assigned to be able to renew the key.

Renew key for created app
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Microsoft Entra tenants node.

   2. On the Details pane, select the Microsoft Entra tenant for the app.

   3. In the ribbon, select Renew Secret Key. Enter the credentials of either the app
     owner or a Microsoft Entra administrator.

Renew key for imported app
If you imported the Azure app in Configuration Manager, use the Azure portal to renew.
Note the new secret key and expiry date. Add this information on the Renew Secret Key

<!-- p.1285 -->

wizard.

  ７ Note

  Save the secret key before closing the Azure application properties Key page. This
  information is removed when you close the page.

Disable authentication
Starting in version 2010, you can disable Microsoft Entra authentication for tenants not
associated with users and devices. When you onboard Configuration Manager to
Microsoft Entra ID, it allows the site and clients to use modern authentication. Currently,
Microsoft Entra device authentication is enabled for all onboarded tenants, whether or
not it has devices. For example, you have a separate tenant with a subscription that you
use for compute resources to support a cloud management gateway. If there aren't
users or devices associated with the tenant, disable Microsoft Entra authentication.

   1. In the Configuration Manager console, go to the Administration workspace.

   2. Expand Cloud Services and select the Azure Services node.

   3. Select the target connection of type Cloud Management. In the ribbon, select
     Properties.

   4. Switch to the Applications tab.

   5. Select the option to Disable Microsoft Entra authentication for this tenant.

   6. Select OK to save and close the connection properties.

   Tip

  It can take up to 25 hours for this change to take effect on clients. For purposes of
  testing to speed up this change in behavior, use the following steps:

     1. Restart the sms_executive service on the site server.
     2. Restart the ccmexec service on the client.
     3. Trigger the client schedule to refresh the default management point. For
          example, use the send schedule tool: SendSchedule {00000000-0000-0000-
          0000-000000000023}

<!-- p.1286 -->

View the configuration of an Azure service
View the properties of an Azure service you've configured for use. In the Configuration
Manager console, go to the Administration workspace, expand Cloud Services, and
select Azure Services. Select the service you want to view or edit, and then select
Properties.

If you select a service and then choose Delete in the ribbon, this action deletes the
connection in Configuration Manager. It doesn't remove the app in Microsoft Entra ID.
Ask your Azure administrator to delete the app when it's no longer needed. Or run the
Azure Service Wizard to import the app.

Cloud management data flow
The following diagram is a conceptual data flow for the interaction between
Configuration Manager, Microsoft Entra ID, and connected cloud services. This specific
example uses the Cloud Management service, which includes a Windows 10 client, and
both server and client apps. The flows for other services are similar.

<!-- p.1287 -->

1. The Configuration Manager administrator imports or creates the client and server
  apps in Microsoft Entra ID.

2. Configuration Manager Microsoft Entra user discovery method runs. The site uses
  the Microsoft Entra server app token to query Microsoft Graph for user objects.

3. The site stores data about the user objects. For more information, see Microsoft
  Entra user Discovery.

4. The Configuration Manager client requests the Microsoft Entra user token. The
  client makes the claim using the application ID of the Microsoft Entra client app,
  and the server app as the audience. For more information, see Claims in Microsoft
  Entra Security Tokens.

5. The client authenticates with the site by presenting the Microsoft Entra token to
  the cloud management gateway and on-premises HTTPS-enabled management
  point.

<!-- p.1288 -->

For more detailed information, see Microsoft Entra authentication workflow.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1289 -->

Uninstall roles, sites, and hierarchies in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use this article as a guide to uninstall a Configuration Manager site system role, site, or
hierarchy. You can also remove the central administration site (CAS) from a hierarchy,
but keep the primary site.

Site system role
You might want to remove a role from a site system server for the following reasons:

      Broader infrastructure change, such as network or physical locations
      Decommission the underlying server
      Consolidate roles to reduce costs and complexity
      Reconfigure or redesigning the site roles
      Discontinue use of the feature that role supports

When you decide you need to remove a role, first consider your answers to the
following questions:

      Do you still need the role in the site? If so, does another site system already have
      the role?

      Are other site systems with this role properly sized to support your business
      requirements for performance and availability?

      Are all clients already reconfigured to use another role? Will you rely upon default
      client behaviors to fall back or discover another server?

Procedure to remove a site system role
Use the following procedure to remove a role:

   1. In the Configuration Manager console, go to the Administration workspace.
      Expand Site Configuration, and then select the Servers and Site System Roles
      node.

<!-- p.1290 -->

   2. Select the site system server with the role to remove. In the Site System Roles
     details pane, select the target role.

   3. In the ribbon, on the Site Role tab, in the Site Role group, select Remove Role.
     Confirm that you want to remove the role.

Additional information for specific roles
Some roles may have additional steps and considerations.

Software update point
After you remove the software update point, Configuration Manager updates the client
policy to remove the software update point from the list. When you remove the last
software update point at the site, the software update point list contains no software
update points. With no roles available, software updates management is essentially
disabled at the site.

When you have more than one software update point at a primary site, and you remove
the software update point that's the synchronization source, choose another software
update point at the site to be the new synchronization source.

Secondary site
Other than when you're decommissioning a hierarchy, the main reason to remove a
secondary site is because of a broader infrastructure change, such as network or
physical locations. Also review the reasons to choose a secondary site.

When you decide you need to remove a secondary site, first consider your answers to
the following questions:

     Did you remove all site system roles from the site server?

     Are any boundaries or boundary groups associated with the secondary site?
     Reconfigure boundaries before removing the site.

     Are any clients still at the location?

     Have you configured other content management options like peer caching?

Options to delete secondary sites

<!-- p.1291 -->

You can't move or reassign a secondary site to another primary site. When you remove a
secondary site from its direct parent site, choose whether to uninstall or delete it.

Uninstall the secondary site

Use this option to remove a functional secondary site that's accessible from the network.
This option uninstalls Configuration Manager from the secondary site server. It then
deletes all information about the site and its resources from the Configuration Manager
site.

If Configuration Manager installed SQL Server Express for the secondary site,
Configuration Manager uninstalls SQL Server Express as well. If you installed SQL Server
Express before you installed the secondary site, Configuration Manager doesn't uninstall
SQL Server Express.

Delete the secondary site

Use this option in the following situations:

        It failed to install

        After you uninstall it, the Configuration Manager console still shows the secondary
        site

        This option deletes all information about the site and its resources from the
        Configuration Manager hierarchy, but doesn't make any changes on the site server.

           Tip

          You also can use the Hierarchy Maintenance Tool with the /DELSITE option to
          delete a secondary site. For more information, see Hierarchy Maintenance
          Tool (Preinst.exe).

Prerequisites to delete a secondary site
The administrative user that runs Configuration Manager setup needs the following
security rights:

        Local Administrator rights on the secondary site server

        If the primary site database server is remote from the primary site server, local
        Administrator rights on the remote site database server for the primary site.

<!-- p.1292 -->

     Infrastructure Administrator or Full Administrator security role on the parent
     primary site

     Sysadmin rights on the secondary site database

Procedure to delete a secondary site
Use the following procedure to uninstall or delete a secondary site:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and then select the Sites node.

   2. Select the secondary site server that you want to remove. In the ribbon, on the
     Home tab, in the Site group, select Delete.

   3. On the General page, select whether to uninstall or delete the secondary site.

   4. Complete the wizard.

Primary site
You might want to uninstall a primary site from your hierarchy for the following reasons:

     Consolidate sites to reduce costs and complexity
     Reconfigure or redesign the sites of the hierarchy

Before you uninstall a child primary site that uses distributed views for its replication link
to the CAS, first turn off distributed views in your hierarchy. For more information, see
Uninstall a primary site that is configured with distributed views.

Plan to uninstall a primary site
Before you uninstall a primary site, review the following tasks:

     Review boundaries, boundary groups, and fallback relationships. If you assign
     clients to a new site, but don't change the boundaries, they may be considered
     roaming. For more information, see Define site boundaries and boundary groups.

     Make sure all active clients are reassigned to another primary site in the hierarchy.
     Otherwise clients will be unmanaged after you uninstall the site. For more
     information, see How to assign clients to a site.

        Review the list of site roles to make sure the new site provides the same level of
        service.

<!-- p.1293 -->

         Make sure that you've properly sized the other site systems with this role in the
         other site. They will need to support your business requirements for
         performance and availability with the additional clients.

         If this site has lots of clients, reassign them in stages. Monitor database
         replication as clients refresh full inventory and other site-specific data. If you
         manage software updates, clients will assign to a new software update point.
         This behavior causes a full scan for update compliance.

         Client reassignment may impact reports and queries that rely on inventory data,
         and state-based compliance. Consider temporarily adjusting any client cycles
         during the transition.

         Review all client assignment methods to make sure that none refers to this
         primary site.

     Check if any actively used objects in the hierarchy have static references to the site
     code. For example, collection queries, task sequences, or administrative scripts.

     If the hierarchy uses a fallback site for automatic site assignment, make sure it
     doesn't reference this primary site.

     Reconfigure any client installation methods that may reference a static site code.

     If this primary site has any site-specific cloud-attached services, make sure to
     remove them. If you still need the cloud resources, move them to another primary
     site in the hierarchy. Remove them from the primary site that you're going to
     uninstall, and add them to another primary site.

     If this primary site has any discovery methods for the hierarchy, move them to
     another site.

     Retire any site-based OS deployment media.

     Uninstall all site system roles from the site and the site server. For more
     information, see Uninstall site system roles. While this preparation step isn't
     required, it helps identify any additional dependencies before uninstalling the site.

     Uninstall any secondary sites under this primary site. For more information, see the
     Secondary site section.

Prerequisites to uninstall a primary site
The administrative user that runs Configuration Manager setup needs the following
security rights:

<!-- p.1294 -->

     Local Administrator rights on the CAS server

     If the CAS database server is remote from the site server, local Administrator rights
     on the remote site database server for the CAS.

     Sysadmin rights on the CAS site database

     Local Administrator rights on the primary site server

     If the primary site database server is remote from the primary site server, local
     Administrator rights on the remote site database server for the primary site.

     Infrastructure Administrator or Full Administrator security role on the CAS

Procedure to uninstall a primary site
You run Configuration Manager setup to uninstall a primary site that doesn't have an
associated secondary site. Use the following procedure to uninstall a primary site:

   Tip

  If the primary site server is no longer available, use the Hierarchy Maintenance Tool
  at the CAS to delete the primary site from the site database. For more information,
  see Hierarchy Maintenance Tool (Preinst.exe).

   1. Start Configuration Manager setup on the primary site server by using one of the
     following methods:

           On the Start menu, select Configuration Manager Setup.

           In the directory for the Configuration Manager installation media, open
           \SMSSETUP\BIN\X64\setup.exe . Make sure this version is the same as the site

           version.

           In the directory where Configuration Manager is installed, open
           \BIN\X64\setup.exe .

   2. Review the information on the Before You Begin page.

   3. On the Getting Started page, select Uninstall a Configuration Manager site.

       ） Important

<!-- p.1295 -->

        When a secondary site is attached to the primary site, you must remove the
        secondary site before you can uninstall the primary site.

   4. On the Uninstall the Configuration Manager Site page, both of the following
     options are enabled by default:

             Remove the site database from the primary site server
             Remove the Configuration Manager console

   5. Select Yes to confirm the uninstallation of the Configuration Manager primary site.

Uninstall a primary site that uses distributed views
   1. Before you uninstall a child primary site, turn off distributed views on each link in
     the hierarchy between the CAS and a primary site.

   2. After you turn off distributed views on each link, confirm that the data from the
     primary site finishes reinitializing at the CAS. To monitor the initialization of data,
     see Monitor replication.

   3. After the data successfully reinitializes with the CAS, you can uninstall the primary
     site.

   4. When the primary site is uninstalled, you can reconfigure distributed views on links
     from the CAS to other primary sites.

        ） Important

        If you uninstall the primary site before you turn off distributed views at each
        site, or before the data from the primary site successfully reinitializes at the
        CAS, data replication might fail.

Decommission a hierarchy
Some organizations have multiple hierarchies because of mergers, acquisitions, test
environments, or other business requirements. If you consolidate management to a
single hierarchy, this action can help reduce costs and complexity. Another reason to
decommission the hierarchy is that you're migrating to a cloud-only management
service such as Microsoft Intune, and are ready to remove your on-premises
infrastructure.

<!-- p.1296 -->

To decommission a hierarchy with multiple sites, the sequence of removal is important.
Start by uninstalling the sites at the bottom of the hierarchy and then move upward:

   1. Remove secondary sites attached to primary sites.
   2. Uninstall primary sites.
   3. After you uninstall all primary sites, you can uninstall the CAS.

For more information, see the following sections:

     Remove a secondary site
     Uninstall a primary site
     Uninstall the CAS

Uninstall the CAS
The final step to decommission a hierarchy is to uninstall the CAS. Run Configuration
Manager setup to uninstall the CAS that doesn't have child primary sites.

Prerequisites to uninstall the CAS

The administrative user who runs Configuration Manager setup needs the following
security rights:

     Local Administrator rights on the CAS server

     If the CAS database server is remote from the site server, local Administrator rights
     on the remote site database server for the CAS.

Procedure to uninstall the CAS
   1. Start Configuration Manager setup on the CAS server by using one of the following
     methods:

           On the Start menu, select Configuration Manager Setup.

           In the directory for the Configuration Manager installation media, open
            \SMSSETUP\BIN\X64\setup.exe . Make sure this version is the same as the site

           version.

           In the directory where Configuration Manager is installed, open
            \BIN\X64\setup.exe .

   2. Review the information on the Before You Begin page.

<!-- p.1297 -->

   3. On the Getting Started page, select Uninstall a Configuration Manager site.

        ） Important

        Remove all child primary sites before you can uninstall the CAS.

   4. On the Uninstall the Configuration Manager Site page, both of the following
     options are enabled by default:

           Remove the site database from the CAS server
           Remove the Configuration Manager console

   5. Select Yes to confirm the uninstallation of the Configuration Manager central
     administration site (CAS).

Remove the CAS
If the hierarchy consists of the CAS and a single child primary site, you can remove the
CAS. This action simplifies your Configuration Manager infrastructure to a single,
standalone primary site. It removes the complexities of site-to-site replication, and
focuses your management tasks to the single site.

For more information, see Remove the CAS.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1298 -->

Remove the central administration site
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If the hierarchy consists of the central administration site (CAS) and a single child
primary site, you can remove the CAS. This action simplifies your Configuration Manager
infrastructure to a single, standalone primary site. It removes the complexities of site-to-
site replication, and focuses your management tasks to the single site.

  ７ Note

  This feature was first introduced in version 2002 as a pre-release feature. Starting
  in version 2103, it's no longer a pre-release feature.

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Plan
      The hierarchy needs to consist of the CAS and a single child primary site. The
      primary site can have secondary sites. To remove other child primary sites from the
      hierarchy, review the planning steps and prerequisites to Uninstall a primary site.

      Make sure your child primary site meets the size and scale requirements for a
      stand-alone primary site.

      Make sure to upgrade all sites to the latest released version of Configuration
      Manager current branch.

      Move or retire any site roles at the CAS, except the service connection point and
      the software update point. Configuration Manager setup handles these two roles
      when you remove the CAS.

      The following roles are most common at the CAS, which you need to retire or
      move to the primary site:
         Asset Intelligence sync point
         Endpoint Protection point
         Reporting services point
         Data warehouse service point

<!-- p.1299 -->

  Turn off distributed views

  Configuration Manager automatically handles package source locations for built-in
  packages, like the Configuration Manager client. Review all other content source
  locations to make sure they aren't using a share on the CAS.

  Stop any active migration jobs and remove all configurations for migration. For
  more information, see Stop active migration from another hierarchy.

  If you have any custom status filter rules or alerts and subscriptions, recreate them
  on the child primary site. Starting in version 2107, also recreate any subscriptions
  for external notifications.

  If you use automatic deployment rules for software updates, recreate them on the
  child primary site.

  If you use Configuration Manager or System Center Updates Publisher to manage
  third-party software updates, export the WSUS signing certificate from the
  software update point on the CAS.
     Before you remove the CAS, wait for the deadlines of any required deployments
     of third-party software updates. Clients pre-download content for required
     deployments, and when you change the software update point, the content
     hash changes with local publishing of software updates. (This behavior doesn't
     impact other content types, only local publishing of third-party software
     updates.) If you remove the CAS with these required deployments still in-
     progress, they'll fail on clients with a hash mismatch error.

  Review any third-party software that might have a dependency on the CAS.

Prerequisites
  Configuration Manager version 2103 or later.

  The administrative user that runs Configuration Manager setup needs the
  following security rights:

     Local Administrator rights on the CAS server

     If the CAS database server is remote from the site server, local Administrator
     rights on the remote site database server for the CAS.

     Sysadmin rights on the CAS site database

     Local Administrator rights on the primary site server

<!-- p.1300 -->

        If the primary site database server is remote from the primary site server, local
        Administrator rights on the remote site database server for the primary site.

        Sysadmin rights on the primary site database

        Infrastructure Administrator or Full Administrator security role on the CAS and
        primary site

     Only one child primary site in the hierarchy. For more information, see Uninstall a
     primary site.

Process
   1. Start Configuration Manager setup on the CAS server by using one of the following
     methods:

           On the Start menu, select Configuration Manager Setup.

           In the directory for the Configuration Manager installation media, open
           \SMSSETUP\BIN\X64\setup.exe . Make sure this version is the same as the site

           version.

           In the directory where Configuration Manager is installed, open
           \BIN\X64\setup.exe .

   2. Review the information on the Before You Begin page.

   3. On the Getting Started page, select Perform site maintenance or reset this site.

   4. On the Site Maintenance page, select Remove central administration site.

   5. On the Reconfiguring Existing Site System Roles page:

           Service Connection Point: Enter the fully qualified domain name of the site
           system in the primary site to host this required role. For more information,
           see About the service connection point.

           Software Update Point: Select an existing software update point in the
           primary site. Setup configures this software update point to synchronize the
           same as the CAS configuration.

     Setup checks that the specified servers meet the prerequisites. Select Begin Install
     when you're ready to continue.

If setup comes across an issue, use the wizard to retry the process.

<!-- p.1301 -->

When setup is complete, it resets the primary site. For more information, see Run a site
reset.

Monitor and verify
Review the following logs during the setup process:

         C:\ConfigMgrSetup.log on the CAS server

         hman.log in the Configuration Manager logs directory on the primary site server

Use the Site Hierarchy node in the Monitoring workspace to visualize the changes to
the hierarchy. For example, the following graphic shows the before and after
comparison of the SHY CAS, HAW primary site, and VWT secondary site:

                                                                          ﾉ   Expand table

 Before                                         After

Post-setup tasks
After you remove the CAS, review the following steps as they apply to your
environment.

<!-- p.1302 -->

Manually remove the CAS server computer account from the primary site local
groups.

If you perform OS Deployment activities, these additional actions need to be
performed as the trusted root key has changed:

   Update OS deployment boot images to include the latest Configuration
   Manager binaries.

   Recreate OS deployment media.

If you enable Endpoint Analytics for devices uploaded to Microsoft Endpoint
Manager, in version 2107, re-enable this option.

If you connect Configuration Manager with Azure Monitor, you need to reset the
connection. The first step to resolve any issues is to renew the secret key. If that
doesn't resolve the issue, recreate the connection.

  ） Important

  The Log Analytics Connector was deprecated in November 2020. It's removed
  from Configuration Manager in version 2107. For more information, see
  Removed and deprecated features.

If you enable synchronization of Surface drivers, reconfigure this feature after you
remove the CAS. For more information, see Microsoft Surface drivers and firmware
updates.

If you manage third-party software updates:

   1. Export the WSUS signing certificate from the software update point on the
     CAS, if you haven't already.

   2. Before you create any new deployments, remove the update from any
     existing deployments and software update packages.

   3. To recover software update metadata into a usable state, resynchronize
     subscribed catalogs. You can also wait for Configuration Manager to
     automatically resynchronize.

   4. Start or wait for a normal software update sync process to update
     Configuration Manager with the current status from WSUS. Optionally, use
     SCUP or WSUS PowerShell cmdlets to delete and readd updates.

<!-- p.1303 -->

         5. Republish content for updates that you need to deploy.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1304 -->

Accounts used in Configuration
Manager
Article • 09/04/2024

Applies to: Configuration Manager (current branch)

Use the following information to identify the Windows groups, accounts, and SQL Server
objects that are used in Configuration Manager, how they're used, and any
requirements.

  ） Important

  If you are specifying an account in a remote domain or forest, be sure to specify the
  domain FQDN before the user name and not just the domain NetBIOS name. For
  example, specify Corp.Contoso.com\UserName instead of just Corp\UserName. This
  allows Configuration Manager to use Kerberos when the account is used to
  authenticate to the remote site system. Using the FQDN often fixes authentication
  failures resulting from recent hardening changes around NTLM in Windows
  monthly updates.

      Windows groups that Configuration Manager creates and uses
         Configuration Manager_CollectedFilesAccess
         Configuration Manager_DViewAccess
         Configuration Manager Remote Control Users
         SMS Admins
         SMS_SiteSystemToSiteServerConnection_MP_<sitecode>
         SMS_SiteSystemToSiteServerConnection_SMSProv_<sitecode>
         SMS_SiteSystemToSiteServerConnection_Stat_<sitecode>
         SMS_SiteToSiteConnection_<sitecode>

      Accounts that Configuration Manager uses
         Active Directory group discovery account
         Active Directory system discovery account
         Active Directory user discovery account
         Active Directory forest account
         Certificate registration point account
         Capture OS image account
         Client push installation account
         Enrollment point connection account

<!-- p.1305 -->

  Exchange Server connection account
  Management point connection account
  Multicast connection account
  Network access account
  Package access account
  Reporting services point account
  Remote tools permitted viewer accounts
  Site installation account
  Site system installation account
  Site system proxy server account
  SMTP server connection account
  Software update point connection account
  Source site account
  Source site database account
  Task sequence domain join account
  Task sequence network folder connection account
  Task sequence run as account

User objects that Configuration Manager uses in SQL
  smsdbuser_ReadOnly
  smsdbuser_ReadWrite
  smsdbuser_ReportSchema

Database roles that Configuration Manager uses in SQL
  smsdbrole_AITool
  smsdbrole_AIUS
  smsdbrole_CRP
  smsdbrole_CRPPfx
  smsdbrole_DMP
  smsdbrole_DmpConnector
  smsdbrole_DViewAccess
  smsdbrole_DWSS
  smsdbrole_EnrollSvr
  smsdbrole_extract
  smsdbrole_HMSUser
  smsdbrole_MCS
  smsdbrole_MP
  smsdbrole_MPMBAM
  smsdbrole_MPUserSvc
  smsdbrole_siteprovider
  smsdbrole_siteserver

<!-- p.1306 -->

         smsdbrole_SUP
         smsschm_users

Windows groups that Configuration Manager
creates and uses
Configuration Manager automatically creates, and in many cases, automatically
maintains, the following Windows groups:

  ７ Note

  When Configuration Manager creates a group on a computer that's a domain
  member, the group is a local security group. If the computer is a domain controller,
  the group is a domain local group. This type of group is shared among all domain
  controllers in the domain.

Configuration Manager_CollectedFilesAccess
Configuration Manager uses this group to grant access to view files collected by
software inventory.

For more information, see Introduction to software inventory.

Type and location for CollectedFilesAccess

This group is a local security group created on the primary site server.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Membership for CollectedFilesAccess

Configuration Manager automatically manages the group membership. Membership
includes administrative users that are granted the View Collected Files permission to the
Collection securable object from an assigned security role.

Permissions for CollectedFilesAccess
By default, this group has Read permission to the following folder on the site server:
C:\Program Files\Microsoft Configuration Manager\sinv.box\FileCol

<!-- p.1307 -->

Configuration Manager_DViewAccess
This group is a local security group that Configuration Manager creates on the site
database server or database replica server for a child primary site. The site creates it
when you use distributed views for database replication between sites in a hierarchy. It
contains the site server and SQL Server computer accounts of the central administration
site.

For more information, see Data transfers between sites.

Configuration Manager Remote Control Users
Configuration Manager remote tools use this group to store the accounts and groups
that you set up in the Permitted Viewers list. The site assigns this list to each client.

For more information, see Introduction to remote control.

Type and location for remote control users

This group is a local security group created on the Configuration Manager client when
the client receives a policy that enables remote tools.

After you disable remote tools for a client, this group isn't automatically removed.
Manually delete it after disabling remote tools.

Membership for remote control users
By default, there are no members in this group. When you add users to the Permitted
Viewers list, they're automatically added to this group.

Use the Permitted Viewers list to manage the membership of this group instead of
adding users or groups directly to this group.

In addition to being a permitted viewer, an administrative user must have Remote
Control permission for the Collection object. Assign this permission by using the
Remote Tools Operator security role.

Permissions for remote control users
By default, this group doesn't have permission to access any locations on the computer.
It's used only to hold the Permitted Viewers list.

<!-- p.1308 -->

SMS Admins
Configuration Manager uses this group to grant access to the SMS Provider through
WMI. Access to the SMS Provider is required to view and change objects in the
Configuration Manager console.

  ７ Note

  The role-based administration configuration of an administrative user determines
  which objects they can view and manage when using the Configuration Manager
  console.

For more information, see Plan for the SMS Provider.

Type and location for SMS Admins
This group is a local security group created on each computer that has an SMS Provider.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Membership for SMS Admins
Configuration Manager automatically manages the group membership. By default, each
administrative user in a hierarchy and the site server computer account are members of
the SMS Admins group on each SMS Provider computer in a site.

Permissions for SMS Admins

You can view the rights and permissions for the SMS Admins group in the WMI Control
MMC snap-in. By default, this group is granted Enable Account and Remote Enable in
the Root\SMS WMI namespace. Authenticated users have Execute Methods, Provider
Write, and Enable Account.

When you use a remote Configuration Manager console, configure Remote Activation
DCOM permissions on both the site server computer and the SMS Provider. Grant these
rights to the SMS Admins group. This action simplifies administration instead of
granting these rights directly to users or groups. For more information, see Configure
DCOM permissions for remote Configuration Manager consoles.

SMS_SiteSystemToSiteServerConnection_MP_<sitecode>

<!-- p.1309 -->

Management points that are remote from the site server use this group to connect to
the site database. This group provides management point access to the inbox folders on
the site server and the site database.

Type and location for SMS_SiteSystemToSiteServerConnection_MP
This group is a local security group created on each computer that has an SMS Provider.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Membership for SMS_SiteSystemToSiteServerConnection_MP

Configuration Manager automatically manages the group membership. By default,
membership includes the computer accounts of remote computers that have a
management point for the site.

Permissions for SMS_SiteSystemToSiteServerConnection_MP

By default, this group has Read, Read & execute, and List folder contents permission to
the following folder on the site server: C:\Program Files\Microsoft Configuration
Manager\inboxes . This group also has Write permission to subfolders below inboxes, to

which the management point writes client data.

SMS_SiteSystemToSiteServerConnection_SMSProv_<sitecode>
Remote SMS Provider computers use this group to connect to the site server.

Type and location for
SMS_SiteSystemToSiteServerConnection_SMSProv

This group is a local security group created on the site server.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Membership for SMS_SiteSystemToSiteServerConnection_SMSProv

Configuration Manager automatically manages the group membership. By default,
membership includes a computer account or a domain user account. It uses this account
to connect to the site server from each remote SMS Provider.

<!-- p.1310 -->

Permissions for SMS_SiteSystemToSiteServerConnection_SMSProv
By default, this group has Read, Read & execute, and List folder contents permission to
the following folder on the site server: C:\Program Files\Microsoft Configuration
Manager\inboxes . This group also has the Write and Modify permissions to subfolders

below the inboxes. The SMS Provider requires access to these folders.

This group also has Read permission to the subfolders on the site server below
C:\Program Files\Microsoft Configuration Manager\OSD\Bin .

It also has the following permissions to the subfolders below C:\Program
Files\Microsoft Configuration Manager\OSD\boot :

      Read
      Read & execute
      List folder contents
      Write
      Modify

SMS_SiteSystemToSiteServerConnection_Stat_<sitecode>
The file dispatch manager component on Configuration Manager remote site system
computers uses this group to connect to the site server.

Type and location for SMS_SiteSystemToSiteServerConnection_Stat

This group is a local security group created on the site server.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Membership for SMS_SiteSystemToSiteServerConnection_Stat
Configuration Manager automatically manages the group membership. By default,
membership includes the computer account or the domain user account. It uses this
account to connect to the site server from each remote site system that runs the file
dispatch manager.

Permissions for SMS_SiteSystemToSiteServerConnection_Stat

By default, this group has Read, Read & execute, and List folder contents permission to
the following folder and its subfolders on the site server: C:\Program Files\Microsoft

<!-- p.1311 -->

Configuration Manager\inboxes .

This group also has the Write and Modify permissions to the following folder on the
site server: C:\Program Files\Microsoft Configuration Manager\inboxes\statmgr.box .

SMS_SiteToSiteConnection_<sitecode>
Configuration Manager uses this group to enable file-based replication between sites in
a hierarchy. For each remote site that directly transfers files to this site, this group has
accounts set up as a File Replication Account.

Type and location for SMS_SiteToSiteConnection

This group is a local security group created on the site server.

Membership for SMS_SiteToSiteConnection
When you install a new site as a child of another site, Configuration Manager
automatically adds the computer account of the new site server to this group on the
parent site server. Configuration Manager also adds the parent site's computer account
to the group on the new site server. If you specify another account for file-based
transfers, add that account to this group on the destination site server.

When you uninstall a site, this group isn't automatically removed. Manually delete it
after uninstalling a site.

Permissions for SMS_SiteToSiteConnection

By default, this group has Full control to the following folder: C:\Program
Files\Microsoft Configuration Manager\inboxes\despoolr.box\receive .

Accounts that Configuration Manager uses
You can set up the following accounts for Configuration Manager.

   Tip

  Don't use the percentage character ( % ) in the password for accounts that you
  specify in the Configuration Manager console. The account will fail to authenticate.

<!-- p.1312 -->

Active Directory group discovery account
The site uses the Active Directory group discovery account to discover the following
objects from the locations in Active Directory Domain Services that you specify:

     Local, global, and universal security groups.
     The membership within these groups.
     The membership within distribution groups.
        Distribution groups aren't discovered as group resources.

This account can be a computer account of the site server that runs discovery, or a
Windows user account. It must have Read access permission to the Active Directory
locations that you specify for discovery.

For more information, see Active Directory group discovery.

Active Directory system discovery account
The site uses the Active Directory system discovery account to discover computers
from the locations in Active Directory Domain Services that you specify.

This account can be a computer account of the site server that runs discovery, or a
Windows user account. It must have Read access permission to the Active Directory
locations that you specify for discovery.

For more information, see Active Directory system discovery.

Active Directory user discovery account
The site uses the Active Directory user discovery account to discover user accounts
from the locations in Active Directory Domain Services that you specify.

This account can be a computer account of the site server that runs discovery, or a
Windows user account. It must have Read access permission to the Active Directory
locations that you specify for discovery.

For more information, see Active Directory user discovery.

Active Directory forest account
The site uses the Active Directory forest account to discover network infrastructure
from Active Directory forests. Central administration sites and primary sites also use it to
publish site data to Active Directory Domain Services for a forest.

<!-- p.1313 -->

  ７ Note

  Secondary sites always use the secondary site server computer account to publish
  to Active Directory.

To discover and publish to untrusted forests, the Active Directory forest account must be
a global account. If you don't use the computer account of the site server, you can select
only a global account.

This account must have Read permissions for each Active Directory forest where you
want to discover network infrastructure.

This account must have Full Control permissions to the System Management container
and all its child objects in each Active Directory forest where you want to publish site
data.

For more information, see Prepare Active Directory for site publishing.

For more information, see Active Directory forest discovery.

Certificate registration point account

  ２ Warning

  Starting in version 2203, the certificate registration point is no longer supported.
  For more information, see Frequently asked questions about resource access
  deprecation.

The certificate registration point uses the Certificate registration point account to
connect to the Configuration Manager database. It uses its computer account by
default, but you can configure a user account instead. When the certificate registration
point is in an untrusted domain from the site server, you must specify a user account.
This account requires only Read access to the site database because the state message
system handles write tasks.

For more information, see Introduction to certificate profiles.

Capture OS image account
When you capture an OS image, Configuration Manager uses the Capture OS image
account to access the folder where you store captured images. If you add the Capture

<!-- p.1314 -->

OS Image step to a task sequence, this account is required.

The account must have Read and Write permissions on the network share where you
store captured images.

If you change the password for the account in Windows, update the task sequence with
the new password. The Configuration Manager client receives the new password when it
next downloads the client policy.

If you need to use this account, create one domain user account. Grant it minimal
permissions to access the required network resources, and use it for all capture task
sequences.

  ） Important

  Don't assign interactive sign-in permissions to this account.

  Don't use the network access account for this account.

For more information, see Create a task sequence to capture an OS.

Client push installation account
When you deploy clients by using the client push installation method, the site uses the
Client push installation account to connect to computers and install the Configuration
Manager client software. If you don't specify this account, the site server tries to use its
computer account.

This account must be a member of the local Administrators group on the target client
computers. This account doesn't require Domain Admin rights.

You can specify more than one client push installation account. Configuration Manager
tries each one in turn until one succeeds.

   Tip

  If you have a large Active Directory environment and need to change this account,
  use the following process to more effectively coordinate this account update:

     1. Create a new account with a different name.
     2. Add the new account to the list of client push installation accounts in
        Configuration Manager.

<!-- p.1315 -->

     3. Allow sufficient time for Active Directory Domain Services to replicate the new
       account.
     4. Then remove the old account from Configuration Manager and Active
       Directory Domain Services.

  ） Important

  Use the domain or local group policy to assign the Windows user the right to Deny
  log on locally. As a member of the Administrators group, this account will have the
  right to sign in locally, which isn't needed. For better security, explicitly deny the
  right to this account. The deny right supersedes the allow right.

For more information, see Client push installation.

Enrollment point connection account
The enrollment point uses the Enrollment point connection account to connect to the
Configuration Manager site database. It uses its computer account by default, but you
can configure a user account instead. When the enrollment point is in an untrusted
domain from the site server, you must specify a user account. This account requires
Read and Write access to the site database.

For more information, see Install site system roles for on-premises MDM.

Exchange Server connection account
The site server uses the Exchange Server connection account to connect to the
specified Exchange Server. It uses this connection to find and manage mobile devices
that connect to the Exchange Server. This account requires Exchange PowerShell
cmdlets that provide the required permissions to the Exchange Server computer. For
more information about the cmdlets, see Install and configure the Exchange connector.

Management point connection account
The management point uses the Management point connection account to connect to
the Configuration Manager site database. It uses this connection to send and retrieve
information for clients. The management point uses its computer account by default,
but you can configure an alternate service account instead. When the management

<!-- p.1316 -->

point is in an untrusted domain from the site server, you must specify an alternate
service account.

  ７ Note

  For enhanced security posture it is recommended to leverage alternate service
  account rather than Computer account for ‘Management point connection
  account’.

Create the account as a low-right service account on the computer that runs Microsoft
SQL Server.

  ） Important

        Don't grant interactive sign-in rights to this account.
        If you are specifying an account in a remote domain or forest, be sure to
        specify the domain FQDN before the user name and not just the domain
        NetBIOS name. For example, specify Corp.Contoso.com\UserName instead of
        just Corp\UserName. This allows Configuration Manager to use Kerberos
        when the account is used to authenticate to the remote site system. Using the
        FQDN often fixes authentication failures resulting from recent hardening
        changes around NTLM in Windows monthly updates.

Multicast connection account
Multicast-enabled distribution points use the Multicast connection account to read
information from the site database. The server uses its computer account by default, but
you can configure a service account instead. When the site database is in an untrusted
forest, you must specify a service account. For example, if your data center has a
perimeter network in a forest other than the site server and site database, use this
account to read the multicast information from the site database.

If you need this account, create it as a low-right service account on the computer that
runs Microsoft SQL Server.

  ７ Note

<!-- p.1317 -->

  For enhanced security posture it is recommended to leverage service account
  rather than Computer account for ‘Multicast connection account’.

  ） Important

  Don't grant interactive sign-in rights to this service account.

For more information, see Use multicast to deploy Windows over the network.

Network access account
Client computers use the network access account when they can't use their local
computer account to access content on distribution points. It mostly applies to
workgroup clients and computers from untrusted domains. This account is also used
during OS deployment, when the computer that's installing the OS doesn't yet have a
computer account on the domain.

  ７ Note

  Managing clients in untrusted domains and cross-forest scenarios allows for
  multiple network access accounts.

  ） Important

  The network access account is never used as the security context to run programs,
  install software updates, or run task sequences. It's used only for accessing
  resources on the network.

A Configuration Manager client first tries to use its computer account to download the
content. If it fails, it then automatically tries the network access account.

If you configure the site for HTTPS or Enhanced HTTP, a workgroup or Microsoft Entra
joined client can securely access content from distribution points without the need for a
network access account. This behavior includes OS deployment scenarios with a task
sequence running from boot media, PXE, or the Software Center. For more information,
see Client to management point communication.

  ７ Note

<!-- p.1318 -->

  If you enable Enhanced HTTP to not require the network access account,
  distribution points need to be running currently supported versions of Windows
  Server or Windows 10/11.

Permissions for the network access account
Grant this account the minimum appropriate permissions for the content that the client
requires to access the software. The account must have the Access this computer from
the network right at the distribution point. You can configure up to 10 network access
accounts per site.

Create an account in any domain that provides the necessary access to resources. The
network access account must always include a domain name. Pass-through security isn't
supported for this account. If you have distribution points in multiple domains, create
the account in a trusted domain.

   Tip

  To avoid account lockouts, don't change the password on an existing network
  access account. Instead, create a new account and set up the new account in
  Configuration Manager. When sufficient time has passed for all clients to have
  received the new account details, remove the old account from the network shared
  folders and delete the account.

  ） Important

  Don't grant interactive sign-in rights to this account.

  Don't grant this account the right to join computers to the domain. If you must join
  computers to the domain during a task sequence, use the Task sequence domain
  join account.

Configure the network access account
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. Then select the site.

   2. On the Settings group of the ribbon, select Configure Site Components, and
     choose Software Distribution.

<!-- p.1319 -->

   3. Choose the Network access account tab. Set up one or more accounts, and then
     choose OK.

Actions that require the network access account

The network access account is still required for the following actions (including eHTTP &
PKI scenarios):

     Multicast. For more information, see Use multicast to deploy Windows over the
     network.

     Task sequence deployment option to Access content directly from a distribution
     point when needed by the running task sequence. For more information, see Task
     sequence deployment options.

     Apply the OS Image task sequence step option to Access content directly from
     the distribution point. This option is primarily for Windows Embedded scenarios
     with low disk space where caching content to the local disk is costly. For more
     information, see Access content directly from the distribution point.

     If downloading a package from a distribution point using HTTP/HTTPS fails, it has
     the ability to fall back to downloading the package using SMB from the package
     share on the distribution point. Downloading the package using SMB from the
     package share on the distribution point requires use of the network access
     account. This fallback behavior only occurs if the option Copy the content in this
     package to a package share on distribution points is enabled under the Data
     Access tab in the properties of a package. To retain this behavior, make sure that
     the network access account isn't disabled or removed. If this behavior is no longer
     desired, make sure the option Copy the content in this package to a package
     share on distribution points isn't enabled on any package.

     Request State Store task sequence step. If the task sequence can't communicate
     with the state migration point using the device's computer account, it falls back to
     using the network access account. For more information, see Request State Store.

     Task Sequence properties setting to Run another program first. This setting runs a
     package and program from a network share before the task sequence starts. For
     more information, see Task sequences properties: Advanced tab.

Package access account
A Package access account lets you set NTFS permissions to specify the users and user
groups that can access package content on distribution points. By default, Configuration

<!-- p.1320 -->

Manager grants access only to the generic access accounts User and Administrator. You
can control access to client computers by using other Windows accounts or groups.
Mobile devices always retrieve package content anonymously, so they don't use a
package access account.

By default, when Configuration Manager copies the content files to a distribution point,
it grants Read access to the local Users group and Full Control to the local
Administrators group. The actual permissions required depend on the package. If you
have clients in workgroups or in untrusted forests, those clients use the network access
account to access the package content. Make sure that the network access account has
permissions to the package by using the defined package access accounts.

Use accounts in a domain that can access the distribution points. If you create or modify
the account after you create the package, you must redistribute the package. Updating
the package doesn't change the NTFS permissions on the package.

You don't have to add the network access account as a package access account because
membership in the Users group adds it automatically. Restricting the package access
account to only the network access account doesn't prevent clients from accessing the
package.

Manage package access accounts

   1. In the Configuration Manager console, go to the Software Library workspace.

   2. In the Software Library workspace, determine the type of content for which you
     want to manage access accounts, and follow the steps provided:

           Application: Expand Application Management, choose Applications, and
           then select the application for which to manage access accounts.

           Package: Expand Application Management, choose Packages, and then
           select the package for which to manage access accounts.

           Software update deployment package: Expand Software Updates, choose
           Deployment Packages, and then select the deployment package for which to
           manage access accounts.

           Driver package: Expand Operating Systems, choose Driver Packages, and
           then select the driver package for which to manage access accounts.

           OS image: Expand Operating Systems, choose Operating System Images,
           and then select the operating system image for which to manage access
           accounts.
