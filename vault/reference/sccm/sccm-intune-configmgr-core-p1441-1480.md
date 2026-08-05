---
title: "Core infrastructure documentation — pages 1441-1480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1441-1480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1441-1480
family: sccm
documentKind: "doc"
abstract: "2001 STATE_TOPICTYPE_EP_CLIENT_DEPLOYMENT ﾉ Expand table State message ID State message description 1 Endpoint Protection unmanaged 2 Endpoint Protection waiting for install 3 Endpoint Protection managed 4 Endpoint Protection installation failed 5 Endpoint Protection reboot pend"
---

# Core infrastructure documentation — pages 1441-1480

<!-- p.1441 -->

2001 STATE_TOPICTYPE_EP_CLIENT_DEPLOYMENT

                                                                      ﾉ   Expand table

State message ID        State message description

1                       Endpoint Protection unmanaged

2                       Endpoint Protection waiting for install

3                       Endpoint Protection managed

4                       Endpoint Protection installation failed

5                       Endpoint Protection reboot pending

6                       Endpoint Protection not supported

7                       Endpoint Protection co-managed

2002 STATE_TOPICTYPE_EP_CLIENT_POLICYAPPLICATION

                                                                      ﾉ   Expand table

State message ID   State message description

1                  Endpoint Protection policy application succeeded

2                  Endpoint Protection policy application failed

2003 STATE_TOPICTYPE_CLIENT_ACTION

                                                                      ﾉ   Expand table

State message ID               State message description

1                              Not applicable

2                              Failed

3                              Succeeded

Wake-up proxy

2100 STATE_TOPICTYPE_WP_CLIENT_DEPLOYMENT

<!-- p.1442 -->

                                                                          ﾉ   Expand table

 State message ID             State message description

 1                            Wake-up proxy isn't installed

 2                            Wake-up proxy is waiting for installation

 3                            Wake-up proxy is installed

 4                            Wake-up proxy installation failed

 5                            Wake-up proxy is waiting for reboot

 6                            Wake-up proxy isn't supported on this OS

 7                            Wake-up proxy server opt-out

 8                            Wake-up proxy uninstall failed

 9                            Wake-up proxy runtime not supported

Mobile device management
The following topic types have no state IDs:

                                                                          ﾉ   Expand table

 Topic type     Description

 2200           STATE_TOPICTYPE_FDM

 2201           STATE_TOPICTYPE_CCM_CERT_BINDING

 2202           STATE_TOPICTYPE_SERVER_STATISTIC

 4000           STATE_TOPICTYPE_MDM_DEVICE_PROPERTY

 4002           STATE_TOPICTYPE_MDM_CLIENT_IDENITITY

 4003           STATE_TOPICTYPE_MDM_APPLICATION_REQUEST

 4004           STATE_TOPICTYPE_MDM_APPLICATION_STATE

 4005           STATE_TOPICTYPE_MDM_LICENSE_DEVICE_RELATION

 4006           STATE_TOPICTYPE_MDM_LICENSE_KEYS

 4007           STATE_TOPICTYPE_MDM_POLICY_ASSIGNMENT

<!-- p.1443 -->

Topic type     Description

4008           STATE_TOPICTYPE_MDM_ANDROID_COUNT

4009           STATE_TOPICTYPE_MDM_SLK_STATUS

4010           STATE_TOPICTYPE_MDM_USER_COMPANY_TERM_ACCEPTANCE

4022           STATE_TOPICTYPE_MDM_DEP_SYNCNOW_STATUS

4023           STATE_TOPICTYPE_MDM_MAM_STORE_APP_SYNC

3000 STATE_TOPICTYPE_DM_WNS_CHANNEL

                                                                             ﾉ   Expand table

State message ID             State message description

0                            Windows Push Notification service channel set

Resource access

5000 STATE_TOPICTYPE_CERTIFICATE_ENROLLMENT

                                                                             ﾉ   Expand table

State message ID                    State message description

1                                   Challenge issued

2                                   Challenge issue failed

3                                   Request creation failed

4                                   Request submit failed

5                                   Challenge validation succeeded

6                                   Challenge validation failed

7                                   Issue failed

8                                   Issue pending

9                                   Issued

10                                  Response processing failed

<!-- p.1444 -->

State message ID   State message description

11                 Response pending

12                 Enrollment succeeded

13                 Enrollment not needed

14                 Revoked

15                 Removed from collection

16                 Renew verified

17                 Install failed

18                 Installed

19                 Delete failed

20                 Deleted

21                 Renewal requested

5001 STATE_TOPICTYPE_CERTIFICATE_CRP

                                                    ﾉ   Expand table

State message ID   State message description

1                  Challenge issued

2                  Challenge issue failed

3                  Request creation failed

4                  Request submit failed

5                  Challenge validation succeeded

6                  Challenge validation failed

7                  Issue failed

8                  Issue pending

9                  Issued

10                 Response processing failed

11                 Response pending

<!-- p.1445 -->

 State message ID                  State message description

 12                                Enrollment succeeded

 13                                Enrollment not needed

 14                                Revoked

 15                                Removed from collection

 16                                Renew verified

 17                                Install failed

 18                                Installed

 19                                Delete failed

 20                                Deleted

 21                                Renewal requested

5200 STATE_TOPICTYPE_RESOURCE_ACCESS_STATUS

                                                                     ﾉ   Expand table

 State message ID                  State message description

 1                                 Status pin set up succeeded

 2                                 Status pin set up failed

 3                                 Status pin set up not supported

 4                                 Status pin set up in progress

Remote applications
The following topic types have no state IDs:

                                                                     ﾉ   Expand table

 Topic type     Description

 6000           STATE_TOPICTYPE_REMOTEAPP_SUBSCRIPTION_STATUS

 6001           STATE_TOPICTYPE_REMOTEAPP_SUBSCRIPTION_SYNC_STATUS

<!-- p.1446 -->

 Topic type     Description

 6002           STATE_TOPICTYPE_REMOTEAPP_AUTHCOOKIES_SYNC_STATUS

 6003           STATE_TOPICTYPE_REMOTEAPPLICATIONS_SYNC_STATUS

 6004           STATE_TOPICTYPE_REMOTEAPP_LOCK_RESULT

Compliance settings
The following topic types have no state IDs:

                                                                    ﾉ   Expand table

 Topic type         Description

 7000               STATE_TOPICTYPE_USER_COMPANY_TERM_ACCEPTANCE

7001 STATE_TOPICTYPE_PFX_CERTIFICATE

                                                                    ﾉ   Expand table

 State message ID                  State message description

 1                                 Challenge issued

 2                                 Challenge issue failed

 3                                 Request creation failed

 4                                 Request submit failed

 5                                 Challenge validation succeeded

 6                                 Challenge validation failed

 7                                 Issue failed

 8                                 Issue pending

 9                                 Issued

 10                                Response processing failed

 11                                Response pending

 12                                Enrollment succeeded

<!-- p.1447 -->

State message ID      State message description

13                    Enrollment not needed

14                    Revoked

15                    Removed from collection

16                    Renew verified

17                    Install failed

18                    Installed

19                    Delete failed

20                    Deleted

21                    Renewal requested

7010
STATE_TOPICTYPE_CONDITIONAL_ACCESS_COMPLIANCE

                                                           ﾉ   Expand table

State message ID   State message description

1                  Compliance success

2                  Compliance fail at MP

3                  Compliance fail at the client

4                  Compliance fail at Intune

5                  Compliance fail at Microsoft Entra ID

6                  Compliance comgmt Intune

Peer caching

7200
STATE_TOPICTYPE_SUPER_PEER_UPDATE_CACHE_MAP

                                                           ﾉ   Expand table

<!-- p.1448 -->

 State message ID                     State message description

 1                                    Peer Cache Source added

 2                                    Peer Cache Source removed

7201 STATE_TOPICTYPE_SUPER_PEER_UPDATE_CONFIG

                                                                       ﾉ   Expand table

 State message ID                   State message description

 1                                  Peer Cache Source deactivated

 2                                  Peer Cache Source is active

7202 STATE_TOPICTYPE_DOWNLOAD_AGGREGATE_DATA

                                                                       ﾉ   Expand table

 State message ID                  State message description

 1                                 Download aggregate data upload

7203
STATE_TOPICTYPE_PEERSOURCE_REQ_REJECTION_STATS

                                                                       ﾉ   Expand table

 State message ID                  State message description

 1                                 Peer source rejection data upload

Proxy
The following topic types have no state IDs:

                                                                       ﾉ   Expand table

 Topic type          Description

 7300                STATE_TOPICTYPE_PROXY_TRAFFIC

<!-- p.1449 -->

 Topic type          Description

 7301                STATE_TOPICTYPE_PROXY_CONNECTION

 7302                STATE_TOPICTYPE_SRS_USAGE_DATA

 7303                STATE_TOPICTYPE_PROXY_TRAFFIC_IDENTITY

Health attestation

8001 STATE_TOPICTYPE_HAS_REPORT

                                                                        ﾉ   Expand table

 State message ID                  State message description

 1                                 Health attestation is supported

 2                                 Health attestation isn't supported

Client actions
The following topic types have no state IDs:

                                                                        ﾉ   Expand table

 Topic type      Description

 8002            STATE_TOPICTYPE_DEVICE_CLIENT_EDPLOG

 8003            STATE_TOPICTYPE_ENABLE_LOSTMODE

 8004            STATE_TOPICTYPE_DISABLE_LOSTMODE

 8005            STATE_TOPICTYPE_LOCATE_DEVICE

 8006            STATE_TOPICTYPE_REBOOT_DEVICE

 8007            STATE_TOPICTYPE_LOGOUTUSER

 8008            STATE_TOPICTYPE_USERSLIST

 8009            STATE_TOPICTYPE_DELETEUSER

 8010            STATE_TOPICTYPE_CLEANPCRETAININGUSERDATA

<!-- p.1450 -->

 Topic type       Description

 8011             STATE_TOPICTYPE_CLEANPCWITHOUTRETAININGUSERDATA

 8012             STATE_TOPICTYPE_SETDEVICENAME

 9000             STATE_TOPICTYPE_BOOK_CI_COMPLIANCE

 9001             STATE_TOPICTYPE_BOOK_CI_ENFORCEMENT

Next steps
Description of state messaging in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1451 -->

Unicode and ASCII support in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager creates most objects by using Unicode characters. However,
several objects only support ASCII characters, or they have other limitations.

Objects that use ASCII characters
When you create the following objects, Configuration Manager only supports the ASCII
character set:

      Site code

      All site system server computer names

      The following Configuration Manager accounts:

        ７ Note

        These accounts support ASCII characters, and RUS characters on a site that
        runs in Russian.

         Client push installation account

         Management point database connect account

         Network access account

         Package access account

         Standard sender account

         Site system installation account

         Software update point connection account

         Software update point proxy server account

           ７ Note

<!-- p.1452 -->

       The accounts that you specify for role-based administration support
       Unicode.

       The reporting services point account supports Unicode, with the exception
       of RUS characters.

  Fully qualified domain name (FQDN) for site servers and site systems

  Installation path for Configuration Manager

  SQL Server instance name

  The path for the following site system roles:

    Enrollment point

    Enrollment proxy point

    Reporting services point

    State migration point

  The path for the following folders:

    The folder that stores client state migration data

    The folder that contains the Configuration Manager reports

    The folder that stores the Configuration Manager backup

    The folder that stores the installation source files for site setup

    The folder that stores the prerequisite downloads for use by setup

  The path for the following objects:

    IIS website

    Virtual application installation path

    Virtual application name

  Boot media ISO file names

  Custom property names

Other limitations

<!-- p.1453 -->

The following limitations are for supported character sets and language versions:

     Configuration Manager doesn't support changing the locale of the site server
     computer.

     An enterprise certificate authority (CA) doesn't support client computer names that
     use double-byte character sets (DBCS). The client computer names that you can
     use are restricted by the PKI limitation of the IA5 character set. Configuration
     Manager doesn't support CA names or subject name values that use DBCS.

Objects that aren't localized
The Configuration Manager database supports Unicode for most objects that it stores.
When possible, it displays this information in the OS language that matches the locale
of a computer. For the client interface or Configuration Manager console to display
information in the computer's OS language, the computer's locale must match a client
or server language that you install at a site.

Several Configuration Manager objects don't support Unicode. They're stored in the
database by using ASCII, or they have other language limitations. This information is
always displayed by using the ASCII character set, or in the language that was in use
when you created the object.

Next steps
Language packs in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1454 -->

Management insights in Configuration
Manager
Article • 06/20/2024

Applies to: Configuration Manager (current branch)

Management insights in Configuration Manager provide information about the current
state of your environment. The information is based on analysis of data from the site
database. Insights help you to better understand your environment and take action
based on the insight.

Review management insights
To view the insights, your account needs the Read permission on the Site object.

   1. In the Configuration Manager console, go to the Administration workspace,
      expand Management Insights, and select All Insights.

        ７ Note

        When you select the Management Insights node, it shows the Management
        insights dashboard.

   2. Open the management insights group name you want to review.

   3. In the ribbon, select Show Insights.

The following four tabs are available for review:

      All Rules: Gives the complete list of insights for the chosen group.

      Complete: Lists insights where no action is needed.

      In Progress: Shows insights where some, but not all, prerequisites are complete.

      Action Needed: This tab lists insights that need you to take action. Select More
      Details to show specific items where action is needed.

The Prerequisites pane lists any required items needed to run the selected insight.

For example, the following screenshot shows an example of the All Rules tab for the
Cloud Services group:

<!-- p.1455 -->

To see the details, select an insight, and then select More Details.

Operations
The site reevaluates the applicability of the management insights on a weekly schedule.
To manually reevaluate an insight, right-click the insight, and select Re-evaluate.

The log file for management insights is SMS_DataEngine.log on the site server.

Some insights let you take action. Select an insight, select More Details, and then if
available select Take action. Depending upon the insight, this action has one of the
following behaviors:

     Automatically navigate in the console to the node where you can take further
     action. For example, if the management insight recommends changing a client
     setting, taking action navigates to the Client Settings node. Then take further
     action by modifying the default or a custom client settings object.

     Navigate to a filtered view based on a query. For example, taking action on the
     empty collections insight shows just these collections in the list of collections. Then
     take further action, such as deleting a collection or modifying its membership
     rules.

Management insights dashboard

<!-- p.1456 -->

Select the Management Insights node to display a graphical dashboard. This dashboard
displays an overview of the insight states, which makes it easier for you to show your
progress.

Use the following filters at the top of the dashboard to refine the view:

     Show Completed
     Optional
     Recommended
     Critical

The dashboard includes the following tiles:

     Management insights index: Tracks overall progress on management insights. The
     index is a weighted average. Critical insights are worth the most. This index gives
     the least weight to optional insights.

     Management insights groups: Shows percent of insights in each group, honoring
     the filters. Select a group to drill down to the specific insights in this group.

     Management insights priority: Shows percent of insights by priority, honoring the
     filters.

     Top 10 applicable insight rules: A table of insights including priority and state. Use
     the Filter field at the top of the table to match strings in any of the available
     columns. The dashboard sorts the table in the following order:
        Status: Action Needed, Completed, Unknown
        Priority: Critical, Recommended, Optional
        Last Changed: older dates on top

<!-- p.1457 -->

                                                                                   

Groups and insights
Insights are organized into the following management insight groups:

     Applications
     Cloud services
     Collections
     Configuration Manager Assessment
     Deprecated and unsupported features
     Optimize for remote workers
     Proactive maintenance
     Security
     Simplified management
     Software Center
     Software updates
     Windows 10

  ７ Note

  Your site may not show all of the following groups and insights. Some insights
  don't appear when you've already configured the site for the recommendation.

<!-- p.1458 -->

Applications
Insights for your application management.

     Applications without deployments or references: Lists the applications in your
     environment that don't have active deployments or references. References include
     dependencies, task sequences, and virtual environments. This insight helps you
     find and delete unused applications to simplify the list of applications displayed in
     the console. For more information, see Deploy applications.

Cloud services
Helps you integrate with many cloud services, which enable modern management of
your devices.

     Assess co-management readiness: Helps you understand what steps are needed
     to enable co-management. This insight has prerequisites. For more information,
     see Co-management overview.

     Devices not uploaded to Microsoft Entra ID: This insight lists devices that the site
     hasn't uploaded to Microsoft Entra ID because you haven't configured it for HTTPS.
     Configure Enhanced HTTP, or enable at least one management point for HTTPS. If
     you already configured the site for HTTPS communication, this insight doesn't
     appear.

     Enable cloud management gateway: The cloud management gateway (CMG)
     provides a simple way to manage Configuration Manager clients over the internet.
     By deploying the CMG as a cloud service in Microsoft Azure, you can continue to
     manage and serve content to clients that roam onto the internet. With CMG, you
     don't need any additional on-premises infrastructure exposed to the internet. For
     more information, see Overview of CMG.

     Enable devices to be Microsoft Entra hybrid joined: Microsoft Entra joined devices
     allow users to sign in with their domain credentials, and make sure devices meet
     the organization's security and compliance standards. For more information, see
     Microsoft Entra hybrid identity design considerations.

     Sites that don't have proper HTTPS configuration: This insight lists sites in your
     hierarchy that aren't properly configured for HTTPS. This configuration prevents
     the site from synchronizing collection membership results to Microsoft Entra
     groups. It may cause Microsoft Entra ID Sync to not upload all devices.
     Management of these clients may not function properly. Configure Enhanced

<!-- p.1459 -->

     HTTP, or enable at least one management point for HTTPS. If you already
     configured the site for HTTPS communication, this insight doesn't appear.

     Update clients to the latest Windows 10 version: Windows 10, version 1709 or
     above improves and modernizes the computing experience of your users. For
     more information, see Stay current with Windows as a service.

Collections
Insights that help simplify management by cleaning up and reconfiguring collections.

     Empty Collections: Lists collections in your environment that have no members.
     For more information, see How to manage collections.

     Collections with no query rules and no direct members: To simplify the list of
     collections in your hierarchy, delete these collections.

     Collections with the same re-evaluation start time: These collections have the
     same re-evaluation time as other collections. Modify the re-evaluation time so they
     don't conflict.

     Collections with query time over 5 minutes: Review the query rules for this
     collection. Consider modifying or deleting the collection.

     The following insights include configurations that potentially cause unnecessary
     load on the site. Review these collections, then either delete them, or disable
     collection rule evaluation:

        Collections with no query rules and incremental updates enabled

        Collections with no query rules and enabled for any schedule

        Collections with no query rules and schedule full evaluation selected

  ７ Note

  For more information on managing collections and collection evaluation, see the
  following articles:

       Best practices for collections
       Collection evaluation
       How to view collection evaluation

<!-- p.1460 -->

Configuration Manager Assessment
This group is courtesy of Microsoft Premier Field Engineering. These insights are a
sample of the many more checks that Microsoft Premier provides in the Services Hub.

     Active Directory Security Group Discovery is configured to run too frequently:
     You typically don't need to configure Active Directory Security Group Discovery to
     occur more frequently than every three hours. A more frequent configuration can
     have a negative performance impact on Active Directory, the network, and
     Configuration Manager. Enable incremental synchronization instead of using a full
     sync schedule. For more information, see Active Directory group discovery.

     Active Directory System Discovery is configured to run too frequently: You
     typically don't need to configure Active Directory System Discovery to occur more
     frequently than every three hours. A more frequent configuration can have a
     negative performance impact on Active Directory, the network, and Configuration
     Manager. Enable incremental synchronization instead of using a full sync schedule.
     For more information, see Active Directory system discovery.

     Active Directory User Discovery is configured to run too frequently: You typically
     don't need to configure Active Directory User Discovery to occur more frequently
     than every three hours. A more frequent configuration can have a negative
     performance impact on Active Directory, the network, and Configuration Manager.
     Enable incremental synchronization instead of using a full sync schedule. For more
     information, see Active Directory user discovery.

     Collections limited to All Systems or All Users: Review any collections that use the
     All Systems or All Users collections as the limiting collection. Configuration
     Manager updates the membership of these default collections with data from the
     Active Directory discovery methods. This data may not be valid information for
     Configuration Manager clients.

     Heartbeat Discovery is disabled: Heartbeat discovery requires that you install the
     Configuration Manager client on devices. It's the only discovery method that
     clients start. All other methods occur on site servers. Heartbeat discovery is
     essential to keep client activity status current. It makes sure that the site doesn't
     accidentally age out the resource records from the site database. For more
     information, see Heartbeat discovery.

     Long running collection queries enabled for incremental updates: Collections
     with a last incremental refresh time higher than 30 seconds use site server and
     database resources, which could potentially impact overall Configuration Manager
     performance. For more information, see Best practices for collections.

<!-- p.1461 -->

     Reduce the number of applications and packages on distribution points:
     Microsoft officially supports a combined total of up to 10,000 packages and
     applications on a distribution point. Exceeding this total can lead to operational
     problems. For more information, see Size and scale numbers - distribution point.

     Secondary site installation issues: The installation status of some secondary sites
     is Pending or Failed. These states mean that you started the install but it didn't
     complete successfully. Until the secondary site install finishes, clients may not
     communicate properly with the primary site. Check the Monitoring workspace, and
     retry the installation. For more information, see Retry installation of a failed update.

     Update all sites to the same version: Use the same version of Configuration
     Manager in a hierarchy. This configuration makes sure all sites provide the same
     functionality. Sites of different versions in the same hierarchy introduce
     interoperability scenarios. Later versions of Configuration Manager include new
     features and resolve known issues. For more information, see Interoperability
     between different versions.

For more information on these insights, see Remediation steps for Configuration
Manager management insights.

   Tip

  If you're already a customer of Microsoft Unified or Microsoft Premier, sign in to
  the Services Hub     for additional on-demand assessments.

  For more information about Microsoft Services, see Support Solutions        .

Deprecated and unsupported features
(Introduced in version 2203)

The following management insights are about features you may be using which have
been deprecated or are no longer supported. These features may be removed from the
product in a future release.

     Site system roles associated with deprecated or removed features: This insight
     checks for installed site system roles for deprecated features that will be removed
     in a future release.
     Check if the site uses the asset intelligence sync point role: This insight checks for
     installation of the asset intelligence synchronization point role.

<!-- p.1462 -->

     Configuration Manager client for macOS end of support: This insight lists the
     clients running macOS. Support for the Configuration Manager client for macOS
     and Mac client management ends on December 31, 2022.
     Certificate registration point is no longer supported: This insight checks for
     installation of the certificate registration point site system role. This feature is no
     longer supported as of March 2022. Configuration Manager versions released
     before March 2022 will still be able to install and use certificate registration points.
     Company resource access policies are no longer supported: This insight checks
     for company resource access policies. These features are no longer supported as of
     March 2022. Company resource access includes email, certificate, VPN, Wi-Fi, and
     Windows Hello for Business profiles. Configuration Manager versions released
     before March 2022 will still be able to use company resource access policies.
     Microsoft Store for Business deprecated: This insight checks for the presence of
     Microsoft Store for Business connector. This feature has been deprecated as of
     Nov 2021.

Operating system deployment
The following management insights help you manage the policy size of task sequences.
When the size of the task sequence policy exceeds 32 MB, the client fails to process the
large policy. The client then fails to run the task sequence deployment.

     Large task sequences may contribute to exceeding maximum policy size: If you
     deploy these task sequences, clients may not be able to process the large policy
     objects. Reduce the size of the task sequence policy to prevent potential policy
     processing issues.

     Total policy size for task sequences exceeds policy limit: Clients can't process the
     policy for these task sequences because it's too large. Reduce the size of the task
     sequence policy to allow the deployment to run on clients.

For more information, see Reduce the size of task sequence policy.

This group also includes the following insight:

     Unused boot images: Boot images not referenced for PXE boot or task sequence
     use. For more information, see Manage boot images.

Optimize for remote workers
Starting in version 2006, the following insights help you create better experiences for
remote workers and reduce load on your infrastructure:

<!-- p.1463 -->

     Configure VPN connected clients to prefer cloud based content sources: To
     reduce traffic on the VPN, enable the boundary group option to Prefer cloud
     based sources over on-premises sources. This option allows clients to download
     content from the internet instead of distribution points across the VPN. For more
     information, see Boundary group options.

     Define VPN boundary groups: Create a VPN boundary and associate it to a
     boundary group. Associate VPN-specific site systems to the group, and configure
     the settings for your environment. This insight checks for at least one boundary
     group with at least one VPN boundary in it. From the properties of this insight,
     select Review Actions to go to the Boundary Groups node. For more information,
     see VPN boundary type.

     Disable peer to peer content sharing for VPN connected clients: To prevent
     unnecessary peer-to-peer traffic that likely doesn't benefit the remote clients,
     disable the boundary group option to Allow peer downloads in this boundary
     group. For more information, see Boundary group options.

Proactive maintenance
The insights in this group highlight potential configuration issues to avoid through
upkeep of Configuration Manager objects.

     Boundary groups with no assigned site systems: Without assigned site systems,
     boundary groups can only be used for site assignment. For more information, see
     Configure boundary groups.

     Boundary groups with no members: Boundary groups aren't applicable for site
     assignment or content lookup if they don't have any members. For more
     information, see Configure boundary groups.

     Distribution points not serving content to clients: Distribution points that haven't
     served content to clients in the past 30 days. This data is based on reports from
     clients of their download history. For more information, see Install and configure
     distribution points.

     Enable WSUS Cleanup: Verifies that you've enabled the option to run WSUS
     cleanup on the properties of the software update point component. This option
     helps to improve WSUS performance. For more information, see Software update
     maintenance.

     Unused configuration items: Configuration items that aren't part of a
     configuration baseline and are older than 30 days. For more information, see

<!-- p.1464 -->

     Create configuration baselines.

     Update Microsoft .NET Framework on site systems: Starting in version 2107,
     Configuration Manager requires Microsoft .NET Framework version 4.6.2 for site
     servers, specific site systems, clients, and the console. Before you run setup to
     install or update the site, first update .NET and restart the system. If possible in
     your environment, install the latest version of .NET version 4.8. For more
     information, Site and site system prerequisites.

     Update servers running Windows Server 2012 and 2012 R2: Detects servers that
     are running Windows Server 2012 or 2012 R2 operating systems. The support
     lifecycle for these operating systems ended on October 9, 2023. For more
     information, see the Product lifecycle.

     Upgrade peer cache sources to the latest version of the Configuration Manager
     client: Identify clients that serve as a peer cache source but haven't upgraded from
     a pre-1806 client version. Pre-1806 clients can't be used as a peer cache source for
     clients that run version 1806 or later. Select Take action to open a device view that
     displays the list of clients.

   Tip

  In version 2006, the insight for Unused boot images moved to the new OS
  deployment group.

Security
Insights for improving the security of your infrastructure and devices.

     NTLM fallback is enabled: This insight detects if you enabled the less secure NTLM
     authentication fallback method for the site. When using the client push method of
     installing the Configuration Manager client, the site can require Kerberos mutual
     authentication. This enhancement helps to secure the communication between the
     server and the client. For more information, see How to install clients with client
     push.

     Unsupported antimalware client versions: More than 10% of clients are running
     versions of System Center Endpoint Protection that aren't supported. For more
     information, see Endpoint Protection.

     Update clients running Windows 7 and Windows Server 2008: The rule shows
     clients running Windows 7, Windows Server 2008 (non-Azure), and Windows

<!-- p.1465 -->

     Server 2008 R2 (non-Azure) that are no longer receiving security updates. For more
     information about updates for these operating systems, see Extended Security
     Updates (ESU)   .

Simplified management
Insights that help you simplify the day-to-day management of your environment.

     Connect the site to the Microsoft cloud for Configuration Manager updates: This
     insight makes sure your Configuration Manager service connection point has
     connected to the Microsoft cloud within the past seven days. This connection is to
     download content for regular updates. Review DMPDownloader.log and hman.log.
     For more information, see Internet access requirements.

     Non-CB Client Versions: Lists all clients whose versions aren't a current branch (CB)
     build. For more information, see Upgrade clients.

     Update clients to a supported Windows 10 version: This insight reports on clients
     that are running a version of Windows 10 that's no longer supported.

Software Center
Insights for managing Software Center.

     Direct users to Software Center instead of Application Catalog: Check if users
     have installed or requested applications from the application catalog in the last 14
     days. The primary functionality of application catalog is now included in Software
     Center. Support for the application catalog roles ended with version 1910. For
     more information, see Deprecated features.

     Use the new version of Software Center: The previous version of Software Center
     is no longer supported. Set up clients to use the new Software Center by enabling
     the client setting Use new Software Center in the Computer Agent group. For
     more information, see About client settings.

Software updates
     Client settings aren't configured to allow clients to download delta content:
     Some software updates synchronized in your environment include delta content.
     Enable the client setting, Allow clients to download delta content when available.
     If you don't enable this setting, when you deploy these updates, client will

<!-- p.1466 -->

     unnecessarily download more content than they require. For more information, see
     Client settings - Software updates.

     Enable the software updates product category 'Windows 10, version 1903 and
     later': There's a new software updates product category for Windows 10, version
     1903 and later. If you synchronize Windows 10 updates, and have Windows 10,
     version 1903 or later clients, select the Windows 10, version 1903 and later
     product category in the software update point component properties. For more
     information, seeConfigure classifications and products to synchronize.

     Configure software update points to use TLS/SSL: Detects if your software update
     points are configured to use TLS/SSL. Configuring Windows Server Update Services
     (WSUS) servers and their corresponding software update points (SUPs) to use
     TLS/SSL may reduce the ability of a potential attacker to remotely compromise a
     client and elevate privileges. This rule was added in Configuration Manager version
     2107.

Windows 10
Insights related to the deployment and servicing of Windows 10. The Windows 10
management insight group is only available when more than half of clients are running
Windows 7, Windows 8, or Windows 8.1.

     Configure Windows diagnostic data and commercial ID key: To use data from
     Desktop Analytics, configure devices with a Commercial ID key and enable
     collection of diagnostic data. Set Windows 10 devices to Enhanced (Limited) level
     or higher.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1467 -->

Community hub and GitHub
Article • 10/31/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in March 2023, this feature of Configuration Manager is being removed. All
  future versions, starting with 2303 will not have the Community hub node in the
  admin console. The Community hub node in older versions will be redirected to
  deprecated features.

The IT Admin community has developed a wealth of knowledge over the years. Rather
than reinventing items like Scripts and Reports from scratch, we've built a Community
hub in Configuration Manager where IT Admins can share with each other. By
leveraging the work of others, you can save hours of work. The Community hub fosters
creativity by building on others work and having other people build on yours. GitHub
already has industry-wide processes and tools built for sharing. Now, the Community
hub can leverage those tools directly in the Configuration Manager console as
foundational pieces for driving this new community.

About Community hub
Community hub supports the following objects:

      CMPivot queries
      Applications
      Task sequences
      Configuration items
      Configuration baselines, including child configuration items
         Baselines with software updates or version-specific references aren't supported
      PowerShell Scripts
      Reports
      Power BI report templates
         For information about sharing and using Power BI report templates with
         Community hub, see Integrate with Power BI Report Server.
      Console extensions are available for download, but contributions are currently
      limited

<!-- p.1468 -->

    Content for console extensions isn't hosted by Microsoft. Currently, the source
    download location displays in the verbose SmsAdminUi.log for the console that
    initiates the download.

What's new
  Support for downloading signed console extensions and limited contribution,
  added in July 2021
  Filter content when using search, added in June 2021
  Support for configuration baselines including child configuration items, added in
  March 2021
  Support for Power BI reports, added in February 2021

Prerequisites
  The device running the Configuration Manager console used to access the
  Community hub needs the following items:
    .NET Framework version 4.6 or later
       .NET Framework version 4.6.2 or later is required starting in Configuration
       Manager 2010
       Starting in version 2107, the console requires .NET version 4.6.2, and version
       4.8 is recommended. For more information, see Install the Configuration
       Manager console.
    A supported version of Windows 10 or later
       Windows Server isn't supported before version 2010, so the Configuration
       Manager console needs to be installed on a supported Windows client
       device separate from the site server.
       Starting in version 2010, install the Microsoft Edge WebView2 console
       extension to support Windows Server.

  The administration service in Configuration Manager needs to be set up and
  functional.

  If your organization restricts network communication with the internet using a
  firewall or proxy device, you need to allow the Configuration Manager console to
  access internet endpoints. For more information, see Internet access requirements.

  A GitHub account is only required to contribute and share content from the Your
  hub page. If you don't wish to share, you can use contributions from others
  without having a GitHub account, For more information, see Contribute to
  Community hub.

<!-- p.1469 -->

        ） Important

        Configuration Manager versions 2006 and earlier won't be able to sign in to
        GitHub. Configuration Manager version 2010 or later with the WebView2
        console extension installed is required for sign in.

Permissions
      To import a script: Create permission for SMS_Scripts class.
      To import a report: Full Administrator security role.
      Starting in version 2010, Full Administrators can opt in the hierarchy for
      unreviewed content via hierarchy settings. Lower hierarchy administrators can't opt
      in the hierarchy for unreviewed hub items. For more information, see the
      Categorize Community hub content section.

Most built-in security roles will have access to the Community hub node:

                                                                           ﾉ   Expand table

 Role name                View the hub    Contribute hub content     Download hub content

 Remote Tools Operator    No              N/A                        N/A

 Read Only Analyst        Yes             No                         No

 All other roles          Yes             Yes                        Yes

Use the Community hub
   1. Go to the Community hub node in the Community workspace.
   2. Select an item to download.
   3. You'll need appropriate permissions in your Configuration Manager site to
      download objects from the hub and import them into the site.

            To import a script: Create permission for SMS_Scripts class.
            To import a report: Full Administrator security role.

   4. Downloaded reports are deployed to a report folder called hub on the reporting
      services point. Downloaded scripts can be seen in the Run Scripts node. Typically,
      downloaded items are placed in the console node for which they're used.
   5. View all items downloaded from the hub by your organization by selecting Your
      downloads from the Community hub node.

<!-- p.1470 -->

                                                                                        

Filter Community hub content when searching
You can filter content in the Community hub when using search. The following filters are
available to use when searching:

                                                                            ﾉ   Expand table

 Filter name            Example search                             Uses a like filter

 Type                   type:report                                Yes

 Curated                curated:false                              No

 User                   user:<GitHubUserName>                      No

 Organization           org:<GitHubOrganizationName>               No

 Name                   name:test_report                           Yes

 Description            desc:description                           Yes

When filtering Community hub items in search:

        The filtering on some items is done using like so you don't need to know the
        exact name of an item you are trying to find. For instance, using type:task would
        return task sequences.
        You can't use the same filter twice in a search. For instance, using type:report and
        type:extension would only return reports since the second filter gets ignored.

<!-- p.1471 -->

     Search filtering respects the hierarchy setting for displaying Community hub
     content categories.
         If your hierarchy is set to Display Microsoft and curated community content,
         then curated:false is ignored.
         If your hierarchy is set to Display Microsoft content, then the curated: filter is
         ignored.
     Starting in version 2203, the console displays a list of search filters you can use in
     Community hub.

Direct links to Community hub items
(Introduced in version 2006)

You can navigate to and reference items in the Configuration Manager console
Community hub node with a direct link. Collaborate with your colleagues easily by
sharing direct links to Community hub items. These deep links are currently only for
items in the Community hub node of the console.

Prerequisites for direct links:

     Configuration Manager console version 2006 or later

Share an item:

   1. Go the item in the hub and select Share.
   2. Paste the copied link and share it with others.

Open a shared link:

   1. Open the link from a machine that has the Configuration Manager console
     installed.
   2. Select Launch the Community hub when prompted.
   3. The console opens directly to the script in the Community hub node.

<!-- p.1472 -->

Categorize Community hub content
(Introduced in version 2010)

Starting in Configuration Manager version 2010, Community hub content is grouped
into a Microsoft, curated, or unreviewed category to allow admins to choose the types
of content their environment displays. Admins can choose from the different categories
of content that are provided in the Community hub to match their risk profile and their
willingness to share and use content from those outside Microsoft and outside their
own company. Only Full Administrators can opt in the hierarchy for unreviewed content
via hierarchy settings.

Community hub content has three categories for content sources:

     Microsoft curated: Content provided by Microsoft
     Community curated: Content provided by the community that gets reviewed by
     Microsoft
     Community unreviewed: General content from the community that doesn't get
     reviewed by Microsoft

Admins can choose the types of content their environment displays from the following
options:

     Display Microsoft content: Selecting this option means that only content created
     by Microsoft will be shown in the Community hub. This content has had some
     basic testing and scanning validation to confirm no malware and inappropriate
     text.
     Display Microsoft and curated community content: Show curated content from
     both Microsoft and community partners with basic level of review. Selecting this
     option means that only content that has been curated will be shown. The curation

<!-- p.1473 -->

     process includes basic review to confirm that the content doesn’t have malware
     and inappropriate text, but hasn’t necessarily been tested. It will include content
     from the community, not just from Microsoft.
     Display all content including unreviewed content: Selecting this option means
     that all content is shown. This option includes unreviewed open-source type
     samples from the community, meaning that the content hasn’t necessarily been
     reviewed at all. It's provided as-is as open-source type sample content. Doing your
     own inspection and testing before using is highly encouraged, which is good
     practice on any content, but especially this class of content.

Since the content is open-source style content, admins should always review what is
provided before consuming it. The new curation process is intended to vet the material
to make sure there aren't obvious quality or compliance issues, but it will be somewhat
of a cursory review. All content stored within GitHub and accessed from the Community
hub isn’t supported by Microsoft. Microsoft doesn’t validate content collected from or
shared by the general community. For more information, see GitHub Terms of Service
and GitHub Privacy Statement .

Select the content categories to display in Community
hub for the environment
   1. In the Configuration Manager console, go to Administration > Overview > Site
     Configuration > Sites.
   2. Select the top-level site in your hierarchy and select Hierarchy Settings from the
     ribbon.
   3. On the General tab, change the Community hub setting to Display Microsoft
     content.
   4. Select Ok when you're finished changing the hierarchy setting.
   5. Open the Community hub node in the Community workspace.
   6. Ensure that only Microsoft content is displayed and available for download.
   7. Go back to Hierarchy Settings and select another option such as Display all
     content, including unreviewed content.
   8. Confirm that only the type of content is displayed and able to be downloaded
     from the Community hub, that matches the corresponding hierarchy setting
     category.

<!-- p.1474 -->

Install the WebView2 console extension
(Introduced in version 2010)

The Microsoft Edge WebView2 console extension enables the full functionality for
Community hub. If WebView2 isn't installed, a banner is shown when you navigate to
the Community hub node. The WebView2 console extension:

     Displays the Community hub on Windows Server operating systems
     Enables sign in for GitHub
        GitHub sign-in is needed for contributing to Community hub but not for
        downloading items.

  ） Important

       When you upgrade to Configuration Manager 2107, you will be prompted to
       install the WebView2 console extension again.
       Configuration Manager versions 2006 and earlier can’t sign into GitHub but
       can still download items. Using Community hub on Windows Server requires
       the WebView2 console extension and Configuration Manager version 2010 or
       later.

Follow the instructions below to enable the full functionality of Community hub:

   1. In the upper-right corner of the console, select the bell icon to display
     Configuration Manager console notifications.

   2. The notification will say New custom console extensions are available.

   3. Select the link Install custom console extensions to launch the install.

<!-- p.1475 -->

   4. When the install completes, select Close to restart the console.

   5. Confirm that you can view the Community hub node from the machine running
     the Windows Server operating system.

           You may also notice that a new folder
           AdminConsole\bin\Microsoft.WebView2.FixedVersionRuntime.<version>.x86

           was created.
           The files are automatically downloaded from
           https://developer.microsoft.com/en-us/microsoft-
           edge/webview2/#download-section with the other redistributable files.

   Tip

  Starting in Configuration Manager version 2103, you can also install the WebView2
  extension from the Console Extensions node. For more information, see Install an
  extension on a local console.

Known issues

Community hub doesn't load
The Community hub may not load, or load after a long delay if the WebView2 console
extension hasn't been installed. For more information about installing console
extensions, see the Install the WebView2 console extension and Managing console
extensions (starting in version 2103).

<!-- p.1476 -->

Unhandled exception occurs when loading Community
hub
In certain circumstances, you may encounter the following exception when loading
Community hub:

Could not load type 'System.Runtime.InteropServices.Architecture' from assembly
'mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'.

Workaround: To work around this issue, update the .NET Framework to version 4.7.1 or
later for the machine running the Configuration Manager console.

Unable to access Community hub node when running
console as a different user
If you're signed in as a user with lower rights and choose Run as a different user to open
the Configuration Manager console, you may not be able to access the Community hub
node.

Downloaded reports don't get removed from your
downloads page
If you delete a downloaded report from the Monitoring > Reports node, the report isn't
deleted from the Community hub > Your downloads page and you're unable to
download the report again.

Unable to download baseline that contains a previously
downloaded configuration item
If you previously downloaded a configuration item from Community hub using
Configuration Manager 2010, you may receive an error when downloading a baseline
after upgrading to Configuration Manager version 2103. A download error can occur
when the baseline contains an updated version of the configuration item you previously
downloaded with Configuration Manager 2010.

Workaround: To work around this issue, delete the configuration item you previously
downloaded, then download the baseline with the new version of the configuration
item.

<!-- p.1477 -->

Unable to sign in when single sign on with multifactor
authentication is used
When single sign on with multifactor authentication is used, you may not be able to sign
in for the following features when using Configuration Manager 2103 and earlier:

     Community hub
     Community hub from CMPivot
     Custom tabs in Software Center that load a website that's subject to conditional
     access policies

Next steps
Contribute to the Configuration Manager Community hub

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1478 -->

Contribute to the Community hub
Article • 10/31/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in March 2023, this feature of Configuration Manager is being removed. All
  future versions, starting with 2303 will not have the Community hub node in the
  admin console. The Community hub node in older versions will be redirected to
  deprecated features.

Community hub fosters creativity by building on others work and having other people
build on yours. GitHub already has industry-wide processes and tools built for sharing.
Now, the Community hub can leverage those tools directly in the Configuration
Manager console as foundational pieces for driving this new community. You can share
the following objects for use by others in the Configuration Manager community:

      CMPivot queries
      Applications
      Task sequences
      Configuration items
      Configuration baselines, including child configuration items
         Baselines with software updates or version-specific references aren't supported
      PowerShell Scripts
      Reports
      Power BI report templates
         For information about sharing and using Power BI report templates with
         Community hub, see Integrate with Power BI Report Server.
      Console extensions are available for download, but contributions are currently
      limited
         Content for console extensions isn't hosted by Microsoft. Currently, the source
         download location displays in the verbose SmsAdminUi.log for the console that
         initiates the download.

Prerequisites
      All Community hub prerequisites and permissions
      Configuration Manager version 2010 or later

<!-- p.1479 -->

      Install the Microsoft Edge WebView2 extension for the Configuration Manager
      console.
      A GitHub       account
         A GitHub account is only required to contribute and share content from the
         Your hub page.
         If you don't already have a GitHub account, you can create one before you join.
         If you don't wish to share, you can use contributions from others without having
         a GitHub account.

  ） Important

  Configuration Manager versions 2006 and earlier can’t sign into GitHub but can still
  download items. Using Community hub on Windows Server requires the WebView2
  console extension and Configuration Manager version 2010 or later.

Most built-in security roles will have access to the Community hub node:

                                                                         ﾉ   Expand table

 Role name                 View the hub   Contribute hub content   Download hub content

 Remote Tools Operator     No             N/A                      N/A

 Read Only Analyst         Yes            No                       No

 All other roles           Yes            Yes                      Yes

Join the Community hub to contribute content
   1. Go to the Community hub node in the Community workspace.

   2. Select Your hub and you'll be prompted to sign into GitHub. If you don't have an
      account, you'll be redirected to GitHub where you can create one. A GitHub
      account is only required to contribute and share content from the Your hub page.

   3. Once you've signed into GitHub, select the Join button to join the Community hub.

<!-- p.1480 -->

   4. After joining, you'll see your membership request is pending. Your account needs
     approval by the Configuration Manager Content Curation team. Approvals are
     done once a day, so it may take up to one business day for your approval to be
     granted.

   5. Once you're granted access, you'll get an email from GitHub. Open the link in the
     email to accept the invitation.

       ） Important

       You must accept the invitation sent in the email otherwise you won't be able
       to contribute content.

Contribute content
Once you've accepted the invitation, you can contribute content.

   1. Go to Community > Community hub > Your hub.

   2. Select Add an Item to open the Contribute item wizard.

   3. Specify the Type of object you want to share from the drop-down menu. The
     following object types are available:

          CMPivot queries
          Applications
          Task sequences
          Configuration items
          Configuration baselines, including child configuration items
             Baselines with software updates or version-specific references aren't
             supported
          PowerShell Scripts
          Reports
          Power BI report templates
