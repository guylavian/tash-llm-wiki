---
title: "Exchange Server — pages 41-80"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0041-0080
family: exchange
documentKind: "doc"
abstract: "design also means that there is no longer a public folder database. Public folder replication now uses the continuous replication model. High availability for the hierarchy and content mailboxes is provided by the database availability group (DAG). With this design, we're moving"
---

# Exchange Server — pages 41-80

<!-- p.41 -->

     design also means that there is no longer a public folder database. Public folder
     replication now uses the continuous replication model. High availability for the hierarchy
     and content mailboxes is provided by the database availability group (DAG). With this
     design, we're moving away from a multi-master replication model to a single-master
     replication model. For more information, see Public folders.

     Shared mailboxes: In previous versions of Exchange, creating a shared mailbox was a
     multi-step process in which you had to use the Exchange Management Shell to set the
     delegate permissions. Now you can create a shared mailbox in one step via the Exchange
     admin center (EAC). In the EAC, go to Recipients > Shared to create a shared mailbox.
     Shared mailboxes are a recipient type so you can easily search for your shared mailboxes
     in either the EAC or by using the Exchange Management Shell. For more information, see
     Shared mailboxes.

Integration with SharePoint and Skype for Business
Exchange 2016 offers greater integration with SharePoint and Skype for Business. Benefits of
this enhanced integration include:

     Skype for Business Server 2015 can archive content in Exchange 2016 and use Exchange
     2016 as a contact store.

     Discovery Managers can perform In-Place eDiscovery and Hold searches across
     SharePoint, Exchange, and Skype for Business data.

For more information, see Plan Exchange 2016 integration with SharePoint and Skype for
Business.

Clients

Outlook on the web (formerly Outlook Web App)
Outlook Web App is now known as Outlook on the web, which continues to let users access
their Exchange mailbox from almost any web browser.

  ７ Note

  Supported Web browsers for Outlook on the web in Exchange 2016 are Microsoft Edge,
  Internet Explorer 11, and the most recent versions of Mozilla Firefox, Google Chrome, and
  Apple Safari.

<!-- p.42 -->

In Exchange 2016, the former Outlook Web App user interface is updated and optimized for
tablets and smart phones, in addition to desktop and laptop computers. New Exchange 2016
features include:

     Platform-specific experiences for phones for both iOS and Android.

     Premium Android experience using Chrome on devices running Android version 4.2 or
     later.

     Apps for Outlook which allow users and administrators to extend the capabilities of
     Outlook on the web.

     Email improvements, including a new single-line view of the Inbox with an optimized
     reading pane, archiving, emojis, and the ability to undo mailbox actions like deleting a
     message or moving a message.

     Contact linking the ability for users to add contacts from their LinkedIn accounts.

     Calendar has an updated look and new features, including email reminders for Calendar
     events, ability to propose a new time in meeting invitations, improved search, and
     birthday calendars.

     Search suggestions and refiners for an improved search experience that helps users find
     the information they want, faster. Search suggestions try to anticipate what the user's
     looking for and returns results that might be what the user is looking for. Search refiners
     will help a user more easily find the information they're looking for by providing
     contextually-aware filters. Filters might include date ranges, related senders, and so on.

     Themes Exchange 2016 provides over 50 built-in themes.

     Options for individual mailboxes have been overhauled.

     Link preview which enables users to paste a link into messages, and Outlook on the web
     automatically generates a rich preview to give recipients a peek into the contents of the
     destination. This works with video links as well.

     Inline video player saves the user time by keeping them in the context of their
     conversations. An inline preview of a video automatically appears after inserting a video
     URL.

     Link preview which enables users to paste a link into messages, and Outlook on the web
     automatically generates a rich preview to give recipients a peek into the contents of the
     destination. This works with video links as well.

<!-- p.43 -->

        Pins and Flags which allow users to keep essential emails at the top of their inbox (Pins)
        and mark others for follow-up (Flags). Pins are now folder specific, great for anyone who
        uses folders to organize their email. Quickly find and manage flagged items with inbox
        filters or the new Task module, accessible from the app launcher.

        Performance improvements in a number of areas across Outlook on the web, including
        creating calendar events, composing, loading messages in the reading pane, popouts,
        search, startup, and switching folders.

        New Outlook on the web action pane that allows you to quickly click those actions you
        most commonly use such as New, Reply all, and Delete. A few new actions have been
        added as well including Archive, Sweep, and Undo.

Offline Outlook on the web
Internet Explorer 11 and Windows Store apps using JavaScript support the Application Cache
API (or AppCache) as defined in the HTML5 specification, which allows you to create offline
web applications. AppCache enables webpages to cache (or save) resources locally, including
images, script libraries, style sheets, and so on. In addition, AppCache allows URLs to be served
from cached content using standard Uniform Resource Identifier (URI) notation. The following
is a list of the browsers that support AppCache:

        Microsoft Edge

        Internet Explorer 11 or later versions

        Google Chrome 44 or later versions

        Mozilla Firefox 39 or later versions

        Apple Safari 8 or later (only on OS X/iOS) versions

MAPI over HTTP
MAPI over HTTP is now the default protocol that Outlook uses to communicate with Exchange.
MAPI over HTTP improves the reliability and stability of the Outlook and Exchange connections
by moving the transport layer to the industry-standard HTTP model. This allows a higher level
of visibility of transport errors and enhanced recoverability. Additional functionality includes
support for an explicit pause-and-resume function, which enables supported clients to change
networks or resume from hibernation while maintaining the same server context.

Note: MAPI over HTTP isn't enabled in organizations where the following conditions are both
true:

<!-- p.44 -->

     You're installing Exchange 2016 in an organization that already has Exchange 2013 servers
     installed.

     MAPI over HTTP wasn't enabled in Exchange 2013.

While MAPI over HTTP is now the default communication protocol between Outlook and
Exchange, clients that don't support it will fall back to Outlook Anywhere (RPC over HTTP). RPC
(RPC over TCP) is no longer supported.

For more information, see MAPI over HTTP in Exchange 2016.

Document collaboration

Exchange 2016, along with SharePoint Server 2016, enables Outlook on the web users to link to
and share documents that are stored in OneDrive for Business in an on-premises SharePoint
server instead of attaching files to messages. Users in an on-premises environment can
collaborate on files in the same manner that's used in Microsoft 365 or Office 365.

For more information about SharePoint Server 2016, see New and improved features in
SharePoint Server 2016.

When an Exchange 2016 user receives a Word, Excel, or PowerPoint file in an email attachment,
and the file is stored in OneDrive for Business or on-premises SharePoint, the user will now
have the option of viewing and editing that file in Outlook on the web alongside the message.
To do this, you'll need a separate computer in your on-premises organization that's running
Office Online Server. For more information, see Install Office Online Server in an Exchange 2016
organization.

Exchange 2016 also brings the following improvements to document collaboration:

     Saving files to OneDrive for Business.

     Uploading a file to OneDrive for Business.

     Most Recently Used lists populated with both local and online files.

Batch mailbox moves
Exchange 2016 makes use of batch moves. The move architecture is built on top of MRS
(Mailbox Replication service) moves with enhanced management capability. The batch move
architecture features the following enhancements:

     Ability to move multiple mailboxes in large batches.

     Email notification during move with reporting.

<!-- p.45 -->

     Automatic retry and automatic prioritization of moves.

     Primary and personal archive mailboxes can be moved together or separately.

     Option for manual move request finalization, which allows you to review a move before
     you complete it.

     Periodic incremental syncs to migrate the changes.

For more information, see Manage on-premises mailbox moves in Exchange 2016.

High availability and site resilience
The high availability model of the mailbox component has not changed significantly since
Exchange 2010. The unit of high availability is still the database availability group (DAG). The
DAG still uses Windows Server failover clustering. Continuous replication still supports both file
mode and block mode replication. However, there have been some improvements. Failover
times have been reduced as a result of transaction log code improvements and deeper
checkpoint on the passive databases. The Exchange Store service has been re-written in
managed code. Now, each database runs under its own process, which isolates store issues to
a single database.

Exchange 2016 uses DAGs and mailbox database copies, along with other features such as
single item recovery, retention policies, and lagged database copies, to provide high
availability, site resilience, and Exchange native data protection. The high availability platform,
the Exchange Information Store and the Extensible Storage Engine (ESE), have all been
enhanced to provide greater availability, easier management, and to reduce costs. These
enhancements include:

     Managed availability: With managed availability, internal monitoring and recovery-
     oriented features are tightly integrated to help prevent failures, proactively restore
     services, and initiate server failovers automatically or alert administrators to take action.
     The focus is on monitoring and managing the end user experience rather than just server
     and component uptime to help keep the service continuously available.

     Managed Store: See the Managed Store section.

     Support for multiple databases per disk: Exchange 2016 includes enhancements that
     enable you to support multiple databases (mixtures of active and passive copies) on the
     same disk, thereby leveraging larger disks in terms of capacity and IOPS as efficiently as
     possible.

     Automatic reseed: Enables you to quickly restore database redundancy after disk failure.
     If a disk fails, the database copy stored on that disk is copied from the active database

<!-- p.46 -->

     copy to a spare disk on the same server. If multiple database copies were stored on the
     failed disk, they can all be automatically re-seeded on a spare disk. This enables faster
     reseeds, as the active databases are likely to be on multiple servers and the data is copied
     in parallel.

     Automatic recovery from storage failures: This feature continues the innovation that was
     introduced in Exchange 2010 to allow the system to recover from failures that affect
     resiliency or redundancy. In addition to the Exchange 2010 bugcheck behaviors, Exchange
     2016 includes additional recovery behaviors for long I/O times, excessive memory
     consumption by MSExchangeRepl.exe , and severe cases where the system is in such a bad
     state that threads can't be scheduled.

     Lagged copy enhancements: Lagged copies can now use automatic log play down to
     care for themselves (to a certain extent). Lagged copies will automatically play down log
     files in a variety of situations, such as single page restore and low disk space scenarios. If
     the system detects that page patching is required for a lagged copy, the logs will be
     automatically replayed into the lagged copy. Lagged copies will also invoke this auto
     replay feature when a low disk space threshold has been reached, and when the lagged
     copy has been detected as the only available copy for a specific period of time. In
     addition, lagged copies can leverage Safety Net, making recovery or activation much
     easier. Safety Net is improved functionality in Exchange 2016 based on the transport
     dumpster of Exchange 2010.

     Single copy alert enhancements: The single copy alert that was introduced in Exchange
     2010 is no longer a separate scheduled script. It's now integrated into the managed
     availability components within the system and is a native function within Exchange.

     DAG network auto-configuration: DAGs networks can be automatically configured by the
     system based on configuration settings. In addition to manual configuration options,
     DAGs can also distinguish between MAPI and Replication networks and configure DAG
     networks automatically.

For more information about these features, see High availability and site resilience and
Changes to high availability and site resilience over previous versions.

Managed Store

In Exchange 2016, Managed Store is the name of the Information Store processes,
Microsoft.Exchange.Store.Service.exe and Microsoft.Exchange.Store.Worker.exe . The new

Managed Store is written in C# and is tightly integrated with the Microsoft Exchange
Replication service ( MSExchangeRepl.exe ) to provide higher availability through improved

<!-- p.47 -->

resiliency. In addition, the Managed Store allows more granular management of resource
consumption, and has improved diagnostics for faster root cause analysis.

The Managed Store works with the Microsoft Exchange Replication service to manage mailbox
databases, which continue to use the Extensible Storage Engine (ESE) database engine.
Exchange 2016 includes significant changes to the mailbox database schema that provide
many optimizations over previous versions of Exchange. The Microsoft Exchange Replication
service is also responsible for all service availability related to Mailbox servers. These
architectural changes enable faster database failover and better physical disk failure handling.

The Managed Store uses the same search platform as SharePoint Server 2016 to provide more
robust indexing and searching when compared to Microsoft Search engine that was used in
previous versions of Exchange.

For more information, see High availability and site resilience.

Exchange workload management
An Exchange workload is an Exchange server feature, protocol, or service that has been
explicitly defined for the purposes of Exchange system resource management. Each Exchange
workload consumes system resources such as CPU, mailbox database operations, or Active
Directory requests to execute user requests or run background work. Examples of Exchange
workloads include Outlook on the web, Exchange ActiveSync, mailbox migration, and mailbox
assistants.

There are two ways to manage Exchange workloads in Exchange 2016:

     Monitor the health of system resources: Managing workloads based on the health of
     system resources.

     Control how resources are consumed by individual users: Controlling how resources are
     consumed by individual users was possible in Exchange 2010 (user throttling), and this
     capability has been expanded for Exchange 2016.

For more information about these features, see User workload management in Exchange 2016.

<!-- p.48 -->

What's discontinued in Exchange Server SE
06/16/2025

APPLIES TO:      2016      2019      Subscription Edition

   Tip

  Looking for what's discontinued in Exchange Server 2019? See What's discontinued in
  Exchange Server 2019.

This topic discusses the components, features, and functionality that's been removed,
discontinued, or replaced in Exchange Server Subscription Edition (SE).

Discontinued features from Exchange 2019 to
Exchange SE
This section lists the Exchange 2019 features that are no longer available in Exchange SE.

Exchange Server Subscription Edition (SE) RTM is code equivalent to Exchange Server 2019
CU15, except for the following changes:

     The License agreement, an RTF file shown only in the GUI version of Setup, is different
     The product name changed from Microsoft Exchange Server 2019 to Microsoft Exchange
     Server Subscription Edition
     The build number

New changes are introduced starting with the Exchange Server SE Cumulative Update (CU) 1.

Discontinued features from Exchange 2016 to
Exchange SE
This section lists the Exchange 2016 features that are no longer available in Exchange SE.

Architecture

                                                                               ﾉ   Expand table

<!-- p.49 -->

 Feature             Comments and mitigation

 Unified             Unified Messaging has been removed from Exchange SE. We recommend that
 Messaging (UM)      Exchange SE organizations transition to Skype for Business Cloud Voice Mail.

Discontinued features from Exchange 2013 to
Exchange SE
This section lists the Exchange 2013 features that are no longer available in Exchange SE.

Architecture

                                                                                           ﾉ   Expand table

 Feature          Comments and mitigation

 Unified          Unified Messaging has been removed from Exchange SE. We recommend that Exchange
 Messaging        SE organizations transition to Skype for Business Cloud Voice Mail.
 (UM)

 Client Access    Client Access services that run on the Mailbox server role replaced the Client Access
 server role      server role. The Mailbox server role now performs all functionality that was previously
                  included with the Client Access server role. For more information about the new Mailbox
                  server role, see Exchange Server architecture.

 MAPI/CDO         The MAPI/CDO library was replaced by Exchange Web Services (EWS), Exchange
 library          ActiveSync (EAS), and Representational State Transfer (REST) APIs. If an application uses
                  the MAPI/CDO library, it needs to move to EWS or EAS to communicate with Exchange
                  SE.

De-emphasized features in Exchange SE
The following features are being de-emphasized in Exchange SE and may not be included in
future versions of Exchange.

      Third-party replication APIs

      RPC over HTTP

      Database availability group (DAG) support for failover cluster administrative access points

<!-- p.50 -->

What's discontinued in Exchange Server
2019
06/16/2025

APPLIES TO:       2016     2019       Subscription Edition

   Tip

  Looking for what's discontinued in Exchange Server 2016? See What's discontinued in
  Exchange Server 2016.

This topic discusses the components, features, and functionality that's been removed,
discontinued, or replaced in Exchange 2019.

Discontinued features from Exchange 2016 to
Exchange 2019
This section lists the Exchange 2016 features that are no longer available in Exchange 2019.

Architecture

                                                                                      ﾉ   Expand table

 Feature           Comments and mitigation

 Unified           Unified Messaging has been removed from Exchange 2019. We recommend that
 Messaging (UM)    Exchange 2019 organizations transition to Skype for Business Cloud Voice Mail.

Discontinued features from Exchange 2013 to
Exchange 2019
This section lists the Exchange 2013 features that are no longer available in Exchange 2019.

Architecture

                                                                                      ﾉ   Expand table

<!-- p.51 -->

 Feature         Comments and mitigation

 Unified         Unified Messaging has been removed from Exchange 2019. We recommend that
 Messaging       Exchange 2019 organizations transition to Skype for Business Cloud Voice Mail.
 (UM)

 Client Access   Client Access services that run on the Mailbox server role replaced the Client Access
 server role     server role. The Mailbox server role now performs all functionality that was previously
                 included with the Client Access server role. For more information about the new Mailbox
                 server role, see Exchange Server architecture.

 MAPI/CDO        The MAPI/CDO library was replaced by Exchange Web Services (EWS), Exchange
 library         ActiveSync (EAS), and Representational State Transfer (REST) APIs. If an application uses
                 the MAPI/CDO library, it needs to move to EWS or EAS to communicate with Exchange
                 2019.

De-emphasized features in Exchange 2019
The following features are being de-emphasized in Exchange 2019 and may not be included in
future versions of Exchange.

      Third-party replication APIs

      RPC over HTTP

      Database availability group (DAG) support for failover cluster administrative access points

<!-- p.52 -->

What's discontinued in Exchange Server
2016
Article • 05/09/2025

APPLIES TO:        2016      2019        Subscription Edition

   Tip

  Looking for what's discontinued in Exchange Server 2019? See What's discontinued in
  Exchange Server 2019.

This topic discusses the components, features, or functionality that have been removed,
discontinued, or replaced in Exchange 2016.

Discontinued features from Exchange 2013 to
Exchange 2016
This section lists the Exchange 2013 features that are no longer available in Exchange 2016.

Architecture

                                                                                          ﾉ   Expand table

 Feature         Comments and mitigation

 Client Access   The Client Access server role has been replaced by Client Access services that run on the
 server role     Mailbox server role. The Mailbox server role now performs all functionality that was
                 previously included with the Client Access server role. For more information about the
                 new Mailbox server role, see Exchange Server architecture.

 MAPI/CDO        The MAPI/CDO library has been replaced by Exchange Web Services (EWS), Exchange
 library         ActiveSync (EAS), and Representational State Transfer (REST)* APIs. If an application uses
                 the MAPI/CDO library, it needs to move to EWS, EAS, or the REST APIs to communicate
                 with Exchange 2016.

* REST APIs will be included in a future release of Exchange 2016.

De-emphasized features in Exchange 2016
The following features are being de-emphasized in Exchange 2016 and may not be included in
future versions of Exchange.

<!-- p.53 -->

         Third-party replication APIs

         RPC over HTTP

         Database Availability Group support for failover cluster administrative access points

Discontinued features from Exchange 2010 to
Exchange 2016
This section lists the Exchange 2010 features that are no longer available in Exchange 2016.

Architecture

                                                                                             ﾉ   Expand table

    Feature         Comments and mitigation

    Hub Transport   The Hub Transport server role has been replaced by Transport services which run on the
    server role     Mailbox server role. The Mailbox server role includes the Microsoft Exchange Transport,
                    Microsoft Exchange Mailbox Transport Delivery, the Microsoft Exchange Mailbox
                    Transport Submission, and the Microsoft Exchange Frontend Transport service. For more
                    information, see Mail flow and the transport pipeline.

    Unified         The Unified Messaging server role has been replaced by Unified Messaging services
    Messaging       which run on the Mailbox and Client Access server roles. The Mailbox server role
    server role     includes the Microsoft Exchange Unified Messaging service and the Client Access server
                    role includes the Microsoft Exchange Unified Messaging Call Router service. For more
                    information, see Voice Architecture Changes.

    MAPI/CDO        The MAPI/CDO library has been replaced by Exchange Web Services (EWS), Exchange
    library         ActiveSync (EAS), and Representational State Transfer (REST)* APIs. If an application uses
                    the MAPI/CDO library, it needs to move to EWS, EAS, or the REST APIs to communicate
                    with Exchange 2016.

*
    REST APIs will be included in a future release of Exchange 2016.

Management interfaces

                                                                                             ﾉ   Expand table

<!-- p.54 -->

Feature                     Comments and mitigation

Exchange Management         The Exchange Management Console and the Exchange Control Panel have
Console and Exchange        been replaced by the Exchange admin center (EAC). EAC uses the same virtual
Control Panel               directory (/ecp) as the Exchange Control Panel. For more information, see
                            Exchange admin center in Exchange Server.

Client access

                                                                                           ﾉ   Expand table

Feature           Comments and mitigation

Outlook 2003 is   To connect Microsoft Outlook to Exchange 2016, the use of the Autodiscover service is
not supported     required. However, Microsoft Outlook 2003 doesn't support the use of the
                  Autodiscover service.

RPC/TCP access    In Exchange 2016, Microsoft Outlook clients can connect using Outlook Anywhere
for Outlook       (RPC/HTTP) or MAPI over HTTP Outlook 2013 Service Pack 1 and later. If you have
clients           Outlook clients in your organization, using Outlook Anywhere and/or MAPI over HTTP
                  is required. For more information, see Outlook Anywhere and MAPI over HTTP in
                  Exchange Server.

Outlook Web App and Outlook

                                                                                           ﾉ   Expand table

Feature           Comments and mitigation

Spell check       Outlook Web App no longer has built-in spell check services. Instead, it uses the spell
                  check features in your Web browsers.

Customizable      Outlook Web App no longer has customizable filtered views and no longer supports
filters           saving filtered views to Favorites. Customizable filters have been replaced by fixed filters
                  that can be used to view all messages, unread messages, messages sent to the user, or
                  flagged messages.

Message flags     The ability to set a custom date on a message flag isn't available in Outlook Web App.
                  You can use Outlook to set custom dates.

Chat contact      The chat contact list that appeared in the folder list in Outlook Web App for Exchange
list              2010 is no longer available.

Search folders    The ability for users to use Search folders isn't currently available in Outlook Web App.

Web Parts         Outlook on the web no longer includes support for Web Parts. Customers will need to
                  develop replacement functionality to meet this need in their environments.

<!-- p.55 -->

Mail flow

                                                                                       ﾉ   Expand table

Feature          Comments and mitigation

Linked           The ability to link a Send connector to a Receive connector has been removed.
connectors       Specifically, the LinkedReceiveConnector parameter has been removed from New-
                 SendConnector and Set-SendConnector.

Antispam and antimalware

                                                                                       ﾉ   Expand table

Feature              Comments and mitigation

Antispam agent       In Exchange 2010, when you enabled the antispam agents on a Hub Transport
management in        server, you could manage the antispam agents in the Exchange Management
the EMC              Console (EMC). In Exchange 2016, when you enable the antispam agents on a
                     Mailbox server, you can't manage the agents using the EAC. You can only use the
                     Exchange Management Shell. For information about how to enable the antispam
                     agents on a Mailbox server, see Enable antispam functionality on Mailbox servers.

Connection           In Exchange 2010, when you enabled the antispam agents on a Hub Transport
Filtering agent on   server, the Attachment Filter agent was the only antispam agent that wasn't
Hub Transport        available. In Exchange 2016, when you enable the antispam agents on a Mailbox
servers              server, the Attachment Filter agent and the Connection Filtering agent aren't
                     available. The Connection Filtering agent provides IP Allow List and IP Block List
                     capabilities. For information about how to enable the antispam agents on a Mailbox
                     server, see Enable antispam functionality on Mailbox servers.
                     Note: The only way to enable the Connection Filtering agent is to install an Edge
                     Transport server in the perimeter network. For more information, see Edge Transport
                     servers.

Messaging policy and compliance

                                                                                       ﾉ   Expand table

Feature        Comments and mitigation

Managed        In Exchange 2010, you use managed folders for messaging retention management (MRM).
Folders        In Exchange 2016, managed folders aren't supported. You must use retention policies for
               MRM.
               Note: Cmdlets related to managed folders are still available. You can create managed
               folders, managed content settings and managed folder mailbox policies, and apply a

<!-- p.56 -->

Feature       Comments and mitigation

              managed folder mailbox policy to a user, but the MRM assistant skips processing of
              mailboxes that have a managed folder mailbox policy applied.

Port          In Exchange 2010, you use the Port Managed Folder wizard to create retention tags based
Managed       on managed folder and managed content settings. In Exchange 2016, the Exchange admin
Folder        center doesn't include this functionality. You can use the New-RetentionPolicyTag cmdlet
wizard        with the ManagedFolderToUpgrade parameter to create a retention tag based on a
              managed folder.

Unified Messaging and voice mail

                                                                                        ﾉ   Expand table

Feature               Comments and mitigation

Directory lookups     In Exchange 2010, Outlook Voice Access users can use speech inputs using
using Automatic       Automatic Speech Recognition (ASR) to search for users listed in the directory.
Speech Recognition    Speech inputs could be also used in Outlook Voice Access to navigate menus,
(ASR)                 messages, and other options. However, even if an Outlook Voice Access user is
                      able to use speech inputs, they have to use the telephone key pad to enter their
                      PIN, and navigate personal options.
                      In Exchange 2016, authenticated and non-authenticated Outlook Voice Access
                      users can't search for users in the directory using speech inputs or ASR in any
                      language. However, callers that call into an auto attendant can use speech inputs
                      in multiple languages to navigate auto attendant menus and search for users in the
                      directory.

Mailbox database copies

                                                                                        ﾉ   Expand table

Feature                     Comments and mitigation

Update-                     Content index catalog seeding is no longer possible over the replication
MailboxDatabaseCopy         network; it can only be done over a MAPI network. This is true even when
Update Mailbox Database     you use the -Network parameter in the Update-MailboxDatabaseCopy
Copy wizard                 cmdlet.

<!-- p.57 -->

Updates for Exchange Server
APPLIES TO:        2016    2019      Subscription Edition

Exchange Server uses a delivery model of 1-2 Cumulative Updates (CUs) per year that address
issues reported to Microsoft by customers and discovered independently by Microsoft. CUs can
also include features and functionality, or introduce the deprecation of legacy features that are
being removed from the product. Critical product updates are used to address a Microsoft-
released security bulletin or changes in time zone definitions. Critical product updates are
released as needed and can typically be applied to the latest CU and the immediately previous
CU.

Exchange Server SE
To get the latest version of Exchange SE, download and install Exchange Server SE RTM . Each
CU is a full installation of Exchange that includes all updates and changes from previous CUs.
When installing a new Exchange server using the latest released CU, you don't need to install
Exchange RTM or any previously released CU.

The following table contains links to Exchange Team blog posts ("What's New" information) for
this and other Exchange SE CUs.

                                                                                   ﾉ   Expand table

 Version                                  Blog post

 Exchange SE RTM                          Exchange Server SE RTM

For information about the new features you'll get when you upgrade to Exchange 2019 from
previous versions of Exchange, see What's new in Exchange Server.

Exchange Server 2019
To get the latest version of Exchange 2019, download and install Cumulative Update 15 for
Exchange Server 2019 . Each CU is a full installation of Exchange that includes all updates and
changes from previous CUs. When installing a new Exchange server using the latest released CU,
you don't need to install Exchange RTM or any previously released CU.

<!-- p.58 -->

The following table contains links to Exchange Team blog posts ("What's New" information) for
this and other Exchange 2019 CUs.

                                                                                      ﾉ   Expand table

 Version                   Blog post

 Exchange 2019 CU15        Released: 2025 H1 Cumulative Updates for Exchange Server

 Exchange 2019 CU14        Released: 2024 H1 Cumulative Updates for Exchange Server

 Exchange 2019 CU13        Released: 2023 H1 Cumulative Updates for Exchange Server

 Exchange 2019 CU12        Released: 2022 H1 Cumulative Updates for Exchange Server

 Exchange 2019 CU11        Released: September 2021 Quarterly Exchange Updates

 Exchange 2019 CU10        Released: June 2021 Quarterly Exchange Updates

 Exchange 2019 CU9         Released: March 2021 Quarterly Exchange Updates

 Exchange 2019 CU8         Released: December 2020 Quarterly Exchange Updates

 Exchange 2019 CU7         Released: September 2020 Quarterly Exchange Updates

 Exchange 2019 CU6         Released: June 2020 Quarterly Exchange Updates

 Exchange 2019 CU5         Released: March 2020 Quarterly Exchange Updates

 Exchange 2019 CU4         Released: December 2019 Quarterly Exchange Updates

 Exchange 2019 CU3         Released: September 2019 Quarterly Exchange Updates

 Exchange 2019 CU2         Released: June 2019 Quarterly Exchange Updates

 Exchange 2019 CU1         Released: February 2019 Quarterly Exchange Updates

 Exchange 2019 RTM         Exchange Server 2019 Now Available

For information about the new features you'll get when you upgrade to Exchange 2019 from
previous versions of Exchange, see What's new in Exchange Server.

Exchange Server 2016
To get the latest version of Exchange 2016, download and install Cumulative Update 23 for
Exchange Server 2016 . Because each CU is a full installation of Exchange that includes updates
and changes from all previous CUs, you don't need to install any previous CUs or Exchange 2016
RTM first.

<!-- p.59 -->

The following table contains links to Exchange Team blog posts ("What's New" information) for
this and other Exchange 2016 CUs.

                                                                                   ﾉ   Expand table

 Version                Blog post

 Exchange 2016 CU23     Released: 2022 H1 Cumulative Updates for Exchange Server

 Exchange 2016 CU22     Released: September 2021 Quarterly Exchange Updates

 Exchange 2016 CU21     Released: June 2021 Quarterly Exchange Updates

 Exchange 2016 CU20     Released: March 2021 Quarterly Exchange Updates

 Exchange 2016 CU19     Released: December 2020 Quarterly Exchange Updates

 Exchange 2016 CU18     Released: September 2020 Quarterly Exchange Updates

 Exchange 2016 CU17     Released: June 2020 Quarterly Exchange Updates

 Exchange 2016 CU16     Released: March 2020 Quarterly Exchange Updates

 Exchange 2016 CU15     Released: December 2019 Quarterly Exchange Updates

 Exchange 2016 CU14     Released: September 2019 Quarterly Exchange Updates

 Exchange 2016 CU13     Released: June 2019 Quarterly Exchange Updates

 Exchange 2016 CU12     Released: February 2019 Quarterly Exchange Updates

 Exchange 2016 CU11     Released: October 2018 Quarterly Exchange Updates

 Exchange 2016 CU10     Released: June 2018 Quarterly Exchange Updates

 Exchange 2016 CU9      Released: March 2018 Quarterly Exchange Updates

 Exchange 2016 CU8      Released: December 2017 Quarterly Exchange Updates

 Exchange 2016 CU7      Released: September 2017 Quarterly Exchange Updates

 Exchange 2016 CU6      Released: June 2017 Quarterly Exchange Updates

 Exchange 2016 CU5      Released: March 2017 Quarterly Exchange Updates

 Exchange 2016 CU4      Released: December 2016 Quarterly Exchange Updates

 Exchange 2016 CU3      Released: September 2016 Quarterly Exchange Updates

 Exchange 2016 CU2      Released: June 2016 Quarterly Exchange Updates

 Exchange 2016 CU1      Released: March 2016 Quarterly Exchange Updates

<!-- p.60 -->

 Version                     Blog post

 Exchange 2016 RTM           Exchange Server 2016: Forged in the cloud. Now available on-premises

For information about the new features you'll get when you upgrade to Exchange 2016 from
previous versions of Exchange, see What's new in Exchange Server.

     To upgrade to the latest CU after you've downloaded it, see Upgrade Exchange to the latest
     Cumulative Update.
     For downloads and updates for other versions of Exchange, see Exchange Server build
     numbers and release dates.

Last updated on 07/14/2026

<!-- p.61 -->

Feature availability for Exchange Server
APPLIES TO:        2016      2019        Subscription Edition

The following table lists the major Exchange Server features available across different supported
versions (certain caveats apply--see the footnotes for further information--this table may change
without notice).

                                                                                        ﾉ    Expand table

 Feature                  Description                    Exchange      Exchange      Exchange Server
                                                         Server 2013   Server 2016   2019 /
                                                                                     Subscription
                                                                                     Edition

 Anti-spam and anti-      Built-in anti-spam and anti-   Yes           Yes           Yes
 malware protection       malware protection

                          Customize anti-spam and        Yesvia        Yesvia        Yesvia PowerShell
                                                         PowerShell    PowerShell
                          anti-malware policies

                          Quarantine - administrator     Yes           Yes           Yes
                          management

                          Quarantine - end-user self-    Yes           Yes           Yes
                          management

 Clients and mobile       Outlook for Windows and        Yes           Yes           Yes
 devices                  Mac¹

                          Outlook on the web¹            Yes           Yes           Yes

                          Outlook for iOS and            Yes           Yes           Yes
                          Android¹

                          Outlook add-ins and            Yes           Yes           Yes
                          Outlook MAPI²

                          Web Parts                      Yes           Yes           Yes

                          Exchange ActiveSync            Yes           Yes           Yes

                          SMTP, POP and IMAP             Yes           Yes           Yes

                          EWS application support        Yes           Yes           Yes

<!-- p.62 -->

Feature                 Description                    Exchange      Exchange      Exchange Server
                                                       Server 2013   Server 2016   2019 /
                                                                                   Subscription
                                                                                   Edition

Exchange Online         Exchange admin center          Yes           Yes           Yes
setup and               access
administration

                        Remote Windows PowerShell      Yes           Yes           Yes
                        access

                        ActiveSync policies for        Yes           Yes           Yes
                        mobile devices

                        Usage reporting                Yes           Yes           Yes

High availability and   Database availability groups   Yes           Yes           Yes
business continuity

                        Deleted mailbox and deleted    Yes           Yes           Yes
                        item recovery

                        Single item recovery           Yes           Yes           Yes

Interoperability,       Skype for Business presence    Yes           Yes           Yes
connectivity, and       in OWA and Outlook
compatibility

                        SharePoint interoperability    Yes           Yes           Yes

                        EWS connectivity and SMTP      Yes           Yes           Yes
                        relay support

Mail flow               Hybrid email and custom        Yes           Yes           Yes
                        routing of outbound mail

                        Secure messaging with a        Yes           Yes           Yes
                        trusted partner

                        Conditional mail routing and   Yes           Yes           Yes
                        adding to an inbound safe
                        list

Message policy and      Cloud-based archiving of       Yes           Yes           Yes
compliance              on-premises mailboxes³

                        Messaging Records              Yes           Yes           Yes
                        Management (MRM) and
                        Journaling

<!-- p.63 -->

Feature        Description                     Exchange      Exchange      Exchange Server
                                               Server 2013   Server 2016   2019 /
                                                                           Subscription
                                                                           Edition

               Manual retention policies,      Yes           Yes           Yes
               labels, and tags

               Encryption of data at rest      Yes           Yes           Yes
               (BitLocker)⁴

               IRM using Azure Information     Yes           Yes           Yes
               Protection

               IRM using Windows Server        Yes           Yes           Yes
               AD RMS⁵

               S/MIME                          Yes           Yes           Yes

               In-Place Hold and Litigation    Yes           Yes           Yes
               Hold

               In-Place eDiscovery             Yes           Yes           Yes

               Transport rules⁷                Yes           Yes           Yes

               Data loss prevention9,10        Yes           Yes           Yes

Permissions    Role-based permissions, role    Yes           Yes           Yes
               groups, and assignment
               policies

Planning and   Hybrid deployment support       Yes           Yes           Yes
deployment     IMAP, cutover, and staged
               migration support

Recipients     Capacity alerts, Inbox rules,   Yes           Yes           Yes
               and Mail Tips

               Clutter                         No            No            No

               Delegate access                 Yes           Yes           Yes

               Connected accounts              Yes           Yes           Yes

               Inactive mailboxes              No            No            No

               Offline address book and        Yes           Yes           Yes
               policies

               Hierarchical address book       Yes           Yes           Yes

<!-- p.64 -->

 Feature                Description                    Exchange      Exchange      Exchange Server
                                                       Server 2013   Server 2016   2019 /
                                                                                   Subscription
                                                                                   Edition

                        Address lists and global       Yes           Yes           Yes
                        address list

                        Universal contact card,        Yes           Yes           Yes
                        contact linking with social
                        networks and external
                        contacts

                        Out-of-office replies,         Yes           Yes           Yes
                        conference room
                        management, and resource
                        mailboxes

                        Calendar sharing               Yes           Yes           Yes

 Reporting features     Message trace                  Yes           No            Yes
 and troubleshooting
 tools

                        Auditing reports               Yes           Yes           Yes

                        Unified Messaging reports      Yes           Yes           Yes

 Sharing and            Federated sharing (including   Yes           Yes           Yes
 collaboration          calendar publishing)

                        Site mailboxes¹⁰               Yes           Yes           Yes

                        Public folders                 Yes           Yes           Yes

 Voice message          Voice mail                     Yes¹¹         No            No
 services

                        Integration between voice      Yes¹¹         No            No
                        mail and third-party FAX

                        Third-party voice mail         Yes¹¹         No            No
                        interoperability and Skype
                        for Business integration

¹ The table indicates if the client works with the server. It doesn't mean the clients are included in
the purchase of these servers.

² Some third-party web parts and add-ins may not be available.

<!-- p.65 -->

³ Requires an Exchange Online Archiving subscription for each on-premises mailbox user that has
a cloud-based archive.

⁴ BitLocker drive encryption is supported for Exchange Server, but an administrator needs to
enable the feature.

⁵ Windows Server AD RMS is an on-premises server that must be purchased and managed
separately in order to enable the supported IRM features.

⁶ Supported for on-premises customers running Exchange Server 2013 or later who purchase
Azure Information Protection. Microsoft Purview Message Encryption requires on-premises
customers to route email through Exchange Online, either by using the Built-in security add-on
for on-premises mailboxes, or by establishing hybrid mail flow.

⁷ Transport rules are made up of flexible criteria, which allow you to define conditions and
exceptions, and actions to take based on the criteria.

⁸ For Exchange 2013, DLP requires an Exchange Enterprise Client Access License (CAL).

⁹ Customers running Exchange Server 2013 or later need to download and install the latest
cumulative update (CU) or the immediately previous CU, to access Document Fingerprinting and
Policy Tips in OWA and OWA for Devices.

¹⁰ SharePoint Server must be deployed in the on-premises Exchange organization.

¹¹ Cloud Voicemail works with Exchange Online and Exchange 2019. See Plan Cloud Voicemail
service for on-premises users - Skype for Business Hybrid | Microsoft Docs.

For information regarding Exchange Online, go to Exchange Online Service Description.

 Last updated on 05/29/2026

<!-- p.66 -->

Exchange Server build numbers and
release dates
APPLIES TO:      2016       2019      Subscription Edition

  ） Important

  Exchange Server 2016 and 2019 are out of support         .

  Customers who enrolled in the Extended Security Update (ESU) program            are eligible to
  receive the December 2025 (and later) security updates for Exchange Server 2016 and 2019.

  If you are not part of the ESU program, migrate to Exchange Server Subscription Edition (SE)
  to keep receiving the latest security updates.

  If you have already purchased the ESU and need information on accessing the latest security
  updates, please contact us by sending an email to
  ExchangeandSfBServerESUInquiry@service.microsoft.com .

You can use the information in this article to verify the versions of Microsoft Exchange Server in
your organization.

This article is organized in sections that correspond to the major releases of Exchange. Each
section lists build numbers for each Service Pack (SP), Cumulative Update (CU), Security Update
(SU), Hotfix Update (HU), or Update Rollup (RU) of the specific Exchange release.

Links for the available downloads are also included.

   Tip

  Releases are listed from the latest release to the earliest release.

  Starting in the March 2021 Security Update (SU), we also include build numbers for Security
  Updates.

  RTM stands for "release to manufacturing" (the first version of the product).

View Exchange Server build numbers

<!-- p.67 -->

This section describes the various methods you can use to view the build numbers of Exchange
servers. The following examples are all run on the same Exchange server.

Option 1 (recommended)
Run the Exchange HealthChecker script    , and check Build Number and Exchange IU or Security
Hotfix Detected in the Exchange Information* section as shown in the following example output:

 PowerShell

 Exchange Information
 --------------------
         Name: MBX01.contoso.com
         Generation Time: 09/22/2025 11:23:45
         Version: Exchange 2019 CU15 Sep25HU
         Build Number: 15.02.1748.037
         Latest Install Time (SU/CU): 08/15/2025 10:24:08
         Exchange IU or Security Hotfix Detected.
                 Interim Update for Exchange Server 2019 Cumulative Update 15
 (KB5066372)
         Server Role: Mailbox
 ...

Option 2
Run the following Get-Command command in the Exchange Management Shell:

 PowerShell

 [PS] C:\Windows\system32>Get-Command Exsetup.exe | ForEach-Object {$_.FileVersionInfo}

 ProductVersion   FileVersion          FileName
 --------------   -----------          --------
 15.02.1748.037   15.02.1748.037       C:\Program Files\Microsoft\Exchange
 Server\V15\bin\ExSetup.exe

The result shows Exchange 2019 CU15 Sep25HU (15.02.1748.037) .

Option 3
This option shows the Cumulative Update (CU) status only. It doesn't show installed Security
Updates (SUs) or Hotfix Updates (HUs). To confirm the SU or HU status, use option 1 or option 2.

Run the following Get-ExchangeServer command in the Exchange Management Shell:

<!-- p.68 -->

 PowerShell

 [PS] C:\Windows\system32>Get-ExchangeServer | Format-List
 Name,Edition,AdminDisplayVersion

 Name                : MBX01
 Edition             : Enterprise
 AdminDisplayVersion : Version 15.2 (Build 1748.10)

The result shows Exchange 2019 CU15 (15.2.1748.10) , but doesn't show the installed Sep25HU
(15.2.1748.37) .

Exchange Server SE
The table in this section provides build numbers and general release dates for each version of
Microsoft Exchange Server SE.

                                                                                  ﾉ   Expand table

 Product name                             Release date           Build number      Build number
                                                                 (short format)    (long format)

  Exchange Server SE RTM May26HU          May 7, 2026             15.2.2562.41    15.02.2562.041

  Exchange Server SE RTM Feb26SU          February 10, 2026       15.2.2562.37    15.02.2562.037

  Exchange Server SE RTM Dec25SU          December 9, 2025        15.2.2562.35    15.02.2562.035

  Exchange Server SE RTM Oct25SU          October 14, 2025        15.2.2562.29    15.02.2562.029

  Exchange Server SE RTM Sep25HU          September 8, 2025       15.2.2562.27    15.02.2562.027

  Exchange Server SE RTM Aug25SU          August 12, 2025         15.2.2562.20    15.02.2562.020

 Exchange Server SE RTM                   July 1, 2025            15.2.2562.17    15.02.2562.017

Exchange Server 2019
The table in this section provides build numbers and general release dates for each version of
Microsoft Exchange Server 2019.

                                                                                  ﾉ   Expand table

<!-- p.69 -->

Product name                           Release date        Build number     Build number
                                                           (short format)   (long format)

 Exchange Server 2019 CU15 Feb26SU     February 10, 2026    15.2.1748.43    15.02.1748.043

 Exchange Server 2019 CU15 Dec25SU     December 9, 2025     15.2.1748.42    15.02.1748.042

 Exchange Server 2019 CU15 Oct25SU     October 14, 2025     15.2.1748.39    15.02.1748.039

 Exchange Server 2019 CU15 Sep25HU     September 8, 2025    15.2.1748.37    15.02.1748.037

 Exchange Server 2019 CU15 Aug25SU     August 12, 2025      15.2.1748.36    15.02.1748.036

 Exchange Server 2019 CU15 May25HU     May 29, 2025         15.2.1748.26    15.02.1748.026

 Exchange Server 2019 CU15 Apr25HU     April 18, 2025       15.2.1748.24    15.02.1748.024

Exchange Server 2019 CU15 (2025H1)     February 10, 2025    15.2.1748.10    15.02.1748.010

 Exchange Server 2019 CU14 Feb26SU     February 10, 2026    15.2.1544.39    15.02.1544.039

 Exchange Server 2019 CU14 Dec25SU     December 9, 2025     15.2.1544.37    15.02.1544.037

 Exchange Server 2019 CU14 Oct25SU     October 14, 2025     15.2.1544.36    15.02.1544.036

 Exchange Server 2019 CU14 Sep25HU     September 8, 2025    15.2.1544.34    15.02.1544.034

 Exchange Server 2019 CU14 Aug25SU     August 12, 2025      15.2.1544.33    15.02.1544.033

 Exchange Server 2019 CU14 May25HU     May 29, 2025         15.2.1544.27    15.02.1544.027

 Exchange Server 2019 CU14 Apr25HU     April 18, 2025       15.2.1544.25    15.02.1544.025

 Exchange Server 2019 CU14 Nov24SUv2   November 27, 2024    15.2.1544.14    15.02.1544.014

 Exchange Server 2019 CU14 Nov24SU     November 12, 2024    15.2.1544.13    15.02.1544.013

 Exchange Server 2019 CU14 Apr24HU     April 23, 2024       15.2.1544.11    15.02.1544.011

 Exchange Server 2019 CU14 Mar24SU     March 12, 2024       15.2.1544.9     15.02.1544.009

Exchange Server 2019 CU14 (2024H1)     February 13, 2024    15.2.1544.4     15.02.1544.004

 Exchange Server 2019 CU13 Nov24SUv2   November 27, 2024    15.2.1258.39    15.02.1258.039

 Exchange Server 2019 CU13 Nov24SU     November 12, 2024    15.2.1258.38    15.02.1258.038

 Exchange Server 2019 CU13 Apr24HU     April 23, 2024       15.2.1258.34    15.02.1258.034

 Exchange Server 2019 CU13 Mar24SU     March 12, 2024       15.2.1258.32    15.02.1258.032

 Exchange Server 2019 CU13 Nov23SU     November 14, 2023    15.2.1258.28    15.02.1258.028

 Exchange Server 2019 CU13 Oct23SU     October 10, 2023     15.2.1258.27    15.02.1258.027

<!-- p.70 -->

Product name                           Release date        Build number     Build number
                                                           (short format)   (long format)

 Exchange Server 2019 CU13 Aug23SUv2   August 15, 2023      15.2.1258.25    15.02.1258.025

 Exchange Server 2019 CU13 Aug23SU     August 8, 2023       15.2.1258.23    15.02.1258.023

 Exchange Server 2019 CU13 Jun23SU     June 13, 2023        15.2.1258.16    15.02.1258.016

Exchange Server 2019 CU13 (2023H1)     May 3, 2023          15.2.1258.12    15.02.1258.012

 Exchange Server 2019 CU12 Nov23SU     November 14, 2023    15.2.1118.40    15.02.1118.040

 Exchange Server 2019 CU12 Oct23SU     October 10, 2023     15.2.1118.39    15.02.1118.039

 Exchange Server 2019 CU12 Aug23SUv2   August 15, 2023      15.2.1118.37    15.02.1118.037

 Exchange Server 2019 CU12 Aug23SU     August 8, 2023       15.2.1118.36    15.02.1118.036

 Exchange Server 2019 CU12 Jun23SU     June 13, 2023        15.2.1118.30    15.02.1118.030

 Exchange Server 2019 CU12 Mar23SU     March 14, 2023       15.2.1118.26    15.02.1118.026

 Exchange Server 2019 CU12 Feb23SU     February 14, 2023    15.2.1118.25    15.02.1118.025

 Exchange Server 2019 CU12 Jan23SU     January 10, 2023     15.2.1118.21    15.02.1118.021

 Exchange Server 2019 CU12 Nov22SU     November 8, 2022     15.2.1118.20    15.02.1118.020

 Exchange Server 2019 CU12 Oct22SU     October 11, 2022     15.2.1118.15    15.02.1118.015

 Exchange Server 2019 CU12 Aug22SU     August 9, 2022       15.2.1118.12    15.02.1118.012

 Exchange Server 2019 CU12 May22SU     May 10, 2022         15.2.1118.9     15.02.1118.009

Exchange Server 2019 CU12 (2022H1)     April 20, 2022       15.2.1118.7     15.02.1118.007

 Exchange Server 2019 CU11 Mar23SU     March 14, 2023       15.2.986.42     15.02.0986.042

 Exchange Server 2019 CU11 Feb23SU     February 14, 2023    15.2.986.41     15.02.0986.041

 Exchange Server 2019 CU11 Jan23SU     January 10, 2023     15.2.986.37     15.02.0986.037

 Exchange Server 2019 CU11 Nov22SU     November 8, 2022     15.2.986.36     15.02.0986.036

 Exchange Server 2019 CU11 Oct22SU     October 11, 2022     15.2.986.30     15.02.0986.030

 Exchange Server 2019 CU11 Aug22SU     August 9, 2022       15.2.986.29     15.02.0986.029

 Exchange Server 2019 CU11 May22SU     May 10, 2022         15.2.986.26     15.02.0986.026

 Exchange Server 2019 CU11 Mar22SU     March 8, 2022        15.2.986.22     15.02.0986.022

 Exchange Server 2019 CU11 Jan22SU     January 11, 2022     15.2.986.15     15.02.0986.015

<!-- p.71 -->

Product name                         Release date         Build number     Build number
                                                          (short format)   (long format)

 Exchange Server 2019 CU11 Nov21SU   November 9, 2021      15.2.986.14     15.02.0986.014

 Exchange Server 2019 CU11 Oct21SU   October 12, 2021       15.2.986.9     15.02.0986.009

Exchange Server 2019 CU11            September 28, 2021     15.2.986.5     15.02.0986.005

 Exchange Server 2019 CU10 Mar22SU   March 8, 2022         15.2.922.27     15.02.0922.027

 Exchange Server 2019 CU10 Jan22SU   January 11, 2022      15.2.922.20     15.02.0922.020

 Exchange Server 2019 CU10 Nov21SU   November 9, 2021      15.2.922.19     15.02.0922.019

 Exchange Server 2019 CU10 Oct21SU   October 12, 2021      15.2.922.14     15.02.0922.014

 Exchange Server 2019 CU10 Jul21SU   July 13, 2021         15.2.922.13     15.02.0922.013

Exchange Server 2019 CU10            June 29, 2021          15.2.922.7     15.02.0922.007

 Exchange Server 2019 CU9 Jul21SU    July 13, 2021         15.2.858.15     15.02.0858.015

 Exchange Server 2019 CU9 May21SU    May 11, 2021          15.2.858.12     15.02.0858.012

 Exchange Server 2019 CU9 Apr21SU    April 13, 2021        15.2.858.10     15.02.0858.010

Exchange Server 2019 CU9             March 16, 2021         15.2.858.5     15.02.0858.005

 Exchange Server 2019 CU8 May21SU    May 11, 2021          15.2.792.15     15.02.0792.015

 Exchange Server 2019 CU8 Apr21SU    April 13, 2021        15.2.792.13     15.02.0792.013

 Exchange Server 2019 CU8 Mar21SU    March 2, 2021         15.2.792.10     15.02.0792.010

Exchange Server 2019 CU8             December 15, 2020      15.2.792.3     15.02.0792.003

 Exchange Server 2019 CU7 Mar21SU    March 2, 2021         15.2.721.13     15.02.0721.013

Exchange Server 2019 CU7             September 15, 2020     15.2.721.2     15.02.0721.002

 Exchange Server 2019 CU6 Mar21SU    March 2, 2021         15.2.659.12     15.02.0659.012

Exchange Server 2019 CU6             June 16, 2020          15.2.659.4     15.02.0659.004

 Exchange Server 2019 CU5 Mar21SU    March 2, 2021          15.2.595.8     15.02.0595.008

Exchange Server 2019 CU5             March 17, 2020         15.2.595.3     15.02.0595.003

 Exchange Server 2019 CU4 Mar21SU    March 2, 2021         15.2.529.13     15.02.0529.013

Exchange Server 2019 CU4             December 17, 2019      15.2.529.5     15.02.0529.005

 Exchange Server 2019 CU3 Mar21SU    March 2, 2021         15.2.464.15     15.02.0464.015

<!-- p.72 -->

 Product name                                Release date         Build number         Build number
                                                                  (short format)       (long format)

 Exchange Server 2019 CU3                    September 17, 2019     15.2.464.5         15.02.0464.005

  Exchange Server 2019 CU2 Mar21SU           March 2, 2021          15.2.397.11        15.02.0397.011

 Exchange Server 2019 CU2                    June 18, 2019          15.2.397.3         15.02.0397.003

  Exchange Server 2019 CU1 Mar21SU           March 2, 2021          15.2.330.11        15.02.0330.011

 Exchange Server 2019 CU1                    February 12, 2019      15.2.330.5         15.02.0330.005

  Exchange Server 2019 RTM Mar21SU           March 2, 2021          15.2.221.18        15.02.0221.018

 Exchange Server 2019 RTM                    October 22, 2018       15.2.221.12        15.02.0221.012

 Exchange Server 2019 Preview                July 24, 2018          15.2.196.0         15.02.0196.000

Exchange Server 2016
The table in this section provides build numbers and general release dates for each version of
Microsoft Exchange Server 2016.

                                                                                   ﾉ    Expand table

 Product name                                Release date          Build number        Build number
                                                                  (short format)       (long format)

  Exchange Server 2016 CU23 Feb26SU          February 10, 2026     15.1.2507.66        15.01.2507.066

  Exchange Server 2016 CU23 Dec25SU          December 9, 2025      15.1.2507.63        15.01.2507.063

  Exchange Server 2016 CU23 Oct25SU          October 14, 2025      15.1.2507.61        15.01.2507.061

  Exchange Server 2016 CU23 Sep25HU          September 8, 2025     15.1.2507.59        15.01.2507.059

  Exchange Server 2016 CU23 Aug25SU          August 12, 2025       15.1.2507.58        15.01.2507.058

  Exchange Server 2016 CU23 May25HU          May 29, 2025          15.1.2507.57        15.01.2507.057

  Exchange Server 2016 CU23 Apr25HU          April 18, 2025        15.1.2507.55        15.01.2507.055

  Exchange Server 2016 CU23 Nov24SUv2        November 27, 2024     15.1.2507.44        15.01.2507.044

  Exchange Server 2016 CU23 Nov24SU          November 12, 2024     15.1.2507.43        15.01.2507.043

  Exchange Server 2016 CU23 Apr24HU          April 23, 2024        15.1.2507.39        15.01.2507.039

  Exchange Server 2016 CU23 Mar24SU          March 12, 2024        15.1.2507.37        15.01.2507.037

<!-- p.73 -->

Product name                           Release date         Build number     Build number
                                                            (short format)   (long format)

 Exchange Server 2016 CU23 Nov23SU     November 14, 2023     15.1.2507.35    15.01.2507.035

 Exchange Server 2016 CU23 Oct23SU     October 10, 2023      15.1.2507.34    15.01.2507.034

 Exchange Server 2016 CU23 Aug23SUv2   August 15, 2023       15.1.2507.32    15.01.2507.032

 Exchange Server 2016 CU23 Aug23SU     August 8, 2023        15.1.2507.31    15.01.2507.031

 Exchange Server 2016 CU23 Jun23SU     June 13, 2023         15.1.2507.27    15.01.2507.027

 Exchange Server 2016 CU23 Mar23SU     March 14, 2023        15.1.2507.23    15.01.2507.023

 Exchange Server 2016 CU23 Feb23SU     February 14, 2023     15.1.2507.21    15.01.2507.021

 Exchange Server 2016 CU23 Jan23SU     January 10, 2023      15.1.2507.17    15.01.2507.017

 Exchange Server 2016 CU23 Nov22SU     November 8, 2022      15.1.2507.16    15.01.2507.016

 Exchange Server 2016 CU23 Oct22SU     October 11, 2022      15.1.2507.13    15.01.2507.013

 Exchange Server 2016 CU23 Aug22SU     August 9, 2022        15.1.2507.12    15.01.2507.012

 Exchange Server 2016 CU23 May22SU     May 10, 2022          15.1.2507.9     15.01.2507.009

Exchange Server 2016 CU23 (2022H1)     April 20, 2022        15.1.2507.6     15.01.2507.006

 Exchange Server 2016 CU22 Nov22SU     November 8, 2022      15.1.2375.37    15.01.2375.037

 Exchange Server 2016 CU22 Oct22SU     October 11, 2022      15.1.2375.32    15.01.2375.032

 Exchange Server 2016 CU22 Aug22SU     August 9, 2022        15.1.2375.31    15.01.2375.031

 Exchange Server 2016 CU22 May22SU     May 10, 2022          15.1.2375.28    15.01.2375.028

 Exchange Server 2016 CU22 Mar22SU     March 8, 2022         15.1.2375.24    15.01.2375.024

 Exchange Server 2016 CU22 Jan22SU     January 11, 2022      15.1.2375.18    15.01.2375.018

 Exchange Server 2016 CU22 Nov21SU     November 9, 2021      15.1.2375.17    15.01.2375.017

 Exchange Server 2016 CU22 Oct21SU     October 12, 2021      15.1.2375.12    15.01.2375.012

Exchange Server 2016 CU22              September 28, 2021    15.1.2375.7     15.01.2375.007

 Exchange Server 2016 CU21 Mar22SU     March 8, 2022         15.1.2308.27    15.01.2308.027

 Exchange Server 2016 CU21 Jan22SU     January 11, 2022      15.1.2308.21    15.01.2308.021

 Exchange Server 2016 CU21 Nov21SU     November 9, 2021      15.1.2308.20    15.01.2308.020

 Exchange Server 2016 CU21 Oct21SU     October 12, 2021      15.1.2308.15    15.01.2308.015

<!-- p.74 -->

Product name                         Release date         Build number     Build number
                                                          (short format)   (long format)

 Exchange Server 2016 CU21 Jul21SU   July 13, 2021         15.1.2308.14    15.01.2308.014

Exchange Server 2016 CU21            June 29, 2021         15.1.2308.8     15.01.2308.008

 Exchange Server 2016 CU20 Jul21SU   July 13, 2021         15.1.2242.12    15.01.2242.012

 Exchange Server 2016 CU20 May21SU   May 11, 2021          15.1.2242.10    15.01.2242.010

 Exchange Server 2016 CU20 Apr21SU   April 13, 2021        15.1.2242.8     15.01.2242.008

Exchange Server 2016 CU20            March 16, 2021        15.1.2242.4     15.01.2242.004

 Exchange Server 2016 CU19 May21SU   May 11, 2021          15.1.2176.14    15.01.2176.014

 Exchange Server 2016 CU19 Apr21SU   April 13, 2021        15.1.2176.12    15.01.2176.012

 Exchange Server 2016 CU19 Mar21SU   March 2, 2021         15.1.2176.9     15.01.2176.009

Exchange Server 2016 CU19            December 15, 2020     15.1.2176.2     15.01.2176.002

 Exchange Server 2016 CU18 Mar21SU   March 2, 2021         15.1.2106.13    15.01.2106.013

Exchange Server 2016 CU18            September 15, 2020    15.1.2106.2     15.01.2106.002

 Exchange Server 2016 CU17 Mar21SU   March 2, 2021         15.1.2044.13    15.01.2044.013

Exchange Server 2016 CU17            June 16, 2020         15.1.2044.4     15.01.2044.004

 Exchange Server 2016 CU16 Mar21SU   March 2, 2021         15.1.1979.8     15.01.1979.008

Exchange Server 2016 CU16            March 17, 2020        15.1.1979.3     15.01.1979.003

 Exchange Server 2016 CU15 Mar21SU   March 2, 2021         15.1.1913.12    15.01.1913.012

Exchange Server 2016 CU15            December 17, 2019     15.1.1913.5     15.01.1913.005

 Exchange Server 2016 CU14 Mar21SU   March 2, 2021         15.1.1847.12    15.01.1847.012

Exchange Server 2016 CU14            September 17, 2019    15.1.1847.3     15.01.1847.003

 Exchange Server 2016 CU13 Mar21SU   March 2, 2021         15.1.1779.8     15.01.1779.008

Exchange Server 2016 CU13            June 18, 2019         15.1.1779.2     15.01.1779.002

 Exchange Server 2016 CU12 Mar21SU   March 2, 2021         15.1.1713.10    15.01.1713.010

Exchange Server 2016 CU12            February 12, 2019     15.1.1713.5     15.01.1713.005

 Exchange Server 2016 CU11 Mar21SU   March 2, 2021         15.1.1591.18    15.01.1591.018

Exchange Server 2016 CU11            October 16, 2018      15.1.1591.10    15.01.1591.010

<!-- p.75 -->

 Product name                                Release date         Build number         Build number
                                                                  (short format)       (long format)

  Exchange Server 2016 CU10 Mar21SU          March 2, 2021         15.1.1531.12        15.01.1531.012

 Exchange Server 2016 CU10                   June 19, 2018          15.1.1531.3        15.01.1531.003

  Exchange Server 2016 CU9 Mar21SU           March 2, 2021         15.1.1466.16        15.01.1466.016

 Exchange Server 2016 CU9                    March 20, 2018         15.1.1466.3        15.01.1466.003

  Exchange Server 2016 CU8 Mar21SU           March 2, 2021         15.1.1415.10        15.01.1415.010

 Exchange Server 2016 CU8                    December 19, 2017      15.1.1415.2        15.01.1415.002

 Exchange Server 2016 CU7                    September 19, 2017    15.1.1261.35        15.01.1261.035

 Exchange Server 2016 CU6                    June 27, 2017         15.1.1034.26        15.01.1034.026

 Exchange Server 2016 CU5                    March 21, 2017         15.1.845.34        15.01.0845.034

 Exchange Server 2016 CU4                    December 13, 2016      15.1.669.32        15.01.0669.032

 Exchange Server 2016 CU3                    September 20, 2016     15.1.544.27        15.01.0544.027

 Exchange Server 2016 CU2                    June 21, 2016          15.1.466.34        15.01.0466.034

 Exchange Server 2016 CU1                    March 15, 2016         15.1.396.30        15.01.0396.030

 Exchange Server 2016 RTM                    October 1, 2015        15.1.225.42        15.01.0225.042

 Exchange Server 2016 Preview                July 22, 2015          15.1.225.16        15.01.0225.016

Exchange Server 2013
The table in this section provides build numbers and general release dates for each version of
Microsoft Exchange Server 2013.

                                                                                   ﾉ    Expand table

 Product name                               Release date          Build number         Build number
                                                                  (short format)       (long format)

  Exchange Server 2013 CU23 Mar23SU         March 14, 2023         15.0.1497.48        15.00.1497.048

  Exchange Server 2013 CU23 Feb23SU         February 14, 2023      15.0.1497.47        15.00.1497.047

  Exchange Server 2013 CU23 Jan23SU         January 10, 2023       15.0.1497.45        15.00.1497.045

  Exchange Server 2013 CU23 Nov22SU         November 8, 2022       15.0.1497.44        15.00.1497.044

<!-- p.76 -->

Product name                         Release date         Build number     Build number
                                                          (short format)   (long format)

 Exchange Server 2013 CU23 Oct22SU   October 11, 2022      15.0.1497.42    15.00.1497.042

 Exchange Server 2013 CU23 Aug22SU   August 9, 2022        15.0.1497.40    15.00.1497.040

 Exchange Server 2013 CU23 May22SU   May 10, 2022          15.0.1497.36    15.00.1497.036

 Exchange Server 2013 CU23 Mar22SU   March 8, 2022         15.0.1497.33    15.00.1497.033

 Exchange Server 2013 CU23 Jan22SU   January 11, 2022      15.0.1497.28    15.00.1497.028

 Exchange Server 2013 CU23 Nov21SU   November 9, 2021      15.0.1497.26    15.00.1497.026

 Exchange Server 2013 CU23 Oct21SU   October 12, 2021      15.0.1497.24    15.00.1497.024

 Exchange Server 2013 CU23 Jul21SU   July 13, 2021         15.0.1497.23    15.00.1497.023

 Exchange Server 2013 CU23 May21SU   May 11, 2021          15.0.1497.18    15.00.1497.018

 Exchange Server 2013 CU23 Apr21SU   April 13, 2021        15.0.1497.15    15.00.1497.015

 Exchange Server 2013 CU23 Mar21SU   March 2, 2021         15.0.1497.12    15.00.1497.012

Exchange Server 2013 CU23            June 18, 2019         15.0.1497.2     15.00.1497.002

 Exchange Server 2013 CU22 Mar21SU   March 2, 2021         15.0.1473.6     15.00.1473.006

Exchange Server 2013 CU22            February 12, 2019     15.0.1473.3     15.00.1473.003

 Exchange Server 2013 CU21 Mar21SU   March 2, 2021         15.0.1395.12    15.00.1395.012

Exchange Server 2013 CU21            June 19, 2018         15.0.1395.4     15.00.1395.004

Exchange Server 2013 CU20            March 20, 2018        15.0.1367.3     15.00.1367.003

Exchange Server 2013 CU19            December 19, 2017     15.0.1365.1     15.00.1365.001

Exchange Server 2013 CU18            September 19, 2017    15.0.1347.2     15.00.1347.002

Exchange Server 2013 CU17            June 27, 2017         15.0.1320.4     15.00.1320.004

Exchange Server 2013 CU16            March 21, 2017        15.0.1293.2     15.00.1293.002

Exchange Server 2013 CU15            December 13, 2016     15.0.1263.5     15.00.1263.005

Exchange Server 2013 CU14            September 20, 2016    15.0.1236.3     15.00.1236.003

Exchange Server 2013 CU13            June 21, 2016         15.0.1210.3     15.00.1210.003

Exchange Server 2013 CU12            March 15, 2016        15.0.1178.4     15.00.1178.004

Exchange Server 2013 CU11            December 15, 2015     15.0.1156.6     15.00.1156.006

<!-- p.77 -->

 Product name                                    Release date               Build number         Build number
                                                                            (short format)       (long format)

 Exchange Server 2013 CU10                       September 15, 2015          15.0.1130.7         15.00.1130.007

 Exchange Server 2013 CU9                        June 17, 2015               15.0.1104.5         15.00.1104.005

 Exchange Server 2013 CU8                        March 17, 2015              15.0.1076.9         15.00.1076.009

 Exchange Server 2013 CU7                        December 9, 2014            15.0.1044.25        15.00.1044.025

 Exchange Server 2013 CU6                        August 26, 2014             15.0.995.29         15.00.0995.029

 Exchange Server 2013 CU5                        May 27, 2014                15.0.913.22         15.00.0913.022

  Exchange Server 2013 SP1 Mar21SU               March 2, 2021               15.0.847.64         15.00.0847.064

 Exchange Server 2013 SP1                        February 25, 2014           15.0.847.32         15.00.0847.032

 Exchange Server 2013 CU3                        November 25, 2013           15.0.775.38         15.00.0775.038

 Exchange Server 2013 CU2                        July 9, 2013                15.0.712.24         15.00.0712.024

 Exchange Server 2013 CU1                        April 2, 2013               15.0.620.29         15.00.0620.029

 Exchange Server 2013 RTM                        December 3, 2012            15.0.516.32         15.00.0516.032

Exchange Server 2010
The tables in this section provide build numbers and general release dates for each version of
Microsoft Exchange Server 2010.

Exchange Server 2010 SP3 build numbers

                                                                                             ﾉ    Expand table

 Product name                                           Release date              Build          Build number
                                                                                 number          (long format)
                                                                                  (short
                                                                                 format)

 Update Rollup 32 for Exchange Server 2010 SP3          March 2, 2021           14.3.513.0       14.03.0513.000

 Update Rollup 31 for Exchange Server 2010 SP3          December 1, 2020        14.3.509.0       14.03.0509.000

 Update Rollup 30 for Exchange Server 2010 SP3          February 11, 2020       14.3.496.0       14.03.0496.000

 Update Rollup 29 for Exchange Server 2010 SP3          July 9, 2019            14.3.468.0       14.03.0468.000

<!-- p.78 -->

Product name                                      Release date          Build      Build number
                                                                      number       (long format)
                                                                       (short
                                                                      format)

Update Rollup 28 for Exchange Server 2010 SP3     June 7, 2019        14.3.461.1   14.03.0461.001

Update Rollup 27 for Exchange Server 2010 SP3     April 9, 2019       14.3.452.0   14.03.0452.000

Update Rollup 26 for Exchange Server 2010 SP3     February 12, 2019   14.3.442.0   14.03.0442.000

Update Rollup 25 for Exchange Server 2010 SP3     January 8, 2019     14.3.435.0   14.03.0435.000

Update Rollup 24 for Exchange Server 2010 SP3     September 5,        14.3.419.0   14.03.0419.000
                                                  2018

Update Rollup 23 for Exchange Server 2010 SP3     August 13, 2018     14.3.417.1   14.03.0417.001

Update Rollup 22 for Exchange Server 2010 SP3     June 19, 2018       14.3.411.0   14.03.0411.000

Update Rollup 21 for Exchange Server 2010 SP3     May 7, 2018         14.3.399.2   14.03.0399.002

Update Rollup 20 for Exchange Server 2010 SP3     March 5, 2018       14.3.389.1   14.03.0389.001

Update Rollup 19 for Exchange Server 2010 SP3     December 19,        14.3.382.0   14.03.0382.000
                                                  2017

Update Rollup 18 for Exchange Server 2010 SP3     July 11, 2017       14.3.361.1   14.03.0361.001

Update Rollup 17 for Exchange Server 2010 SP3     March 21, 2017      14.3.352.0   14.03.0352.000

Update Rollup 16 for Exchange Server 2010 SP3     December 13,        14.3.336.0   14.03.0336.000
                                                  2016

Update Rollup 15 for Exchange Server 2010 SP3     September 20,       14.3.319.2   14.03.0319.002
                                                  2016

Update Rollup 14 for Exchange Server 2010 SP3     June 21, 2016       14.3.301.0   14.03.0301.000

Update Rollup 13 for Exchange Server 2010 SP3     March 15, 2016      14.3.294.0   14.03.0294.000

Update Rollup 12 for Exchange Server 2010 SP3     December 15,        14.3.279.2   14.03.0279.002
                                                  2015

Update Rollup 11 for Exchange Server 2010 SP3     September 15,       14.3.266.2   14.03.0266.002
                                                  2015

Update Rollup 10 for Exchange Server 2010 SP3     June 17, 2015       14.3.248.2   14.03.0248.002

Update Rollup 9 for Exchange Server 2010 SP3      March 17, 2015      14.3.235.1   14.03.0235.001

Update Rollup 8 v2 for Exchange Server 2010 SP3   December 12,        14.3.224.2   14.03.0224.002
                                                  2014

<!-- p.79 -->

Product name                                        Release date             Build           Build number
                                                                           number            (long format)
                                                                             (short
                                                                            format)

Update Rollup 8 v1 for Exchange Server 2010 SP3     December 9, 2014       14.3.224.1        14.03.0224.001
(recalled )

Update Rollup 7 for Exchange Server 2010 SP3        August 26, 2014        14.3.210.2        14.03.0210.002

Update Rollup 6 for Exchange Server 2010 SP3        May 27, 2014           14.3.195.1        14.03.0195.001

Update Rollup 5 for Exchange Server 2010 SP3        February 24, 2014      14.3.181.6        14.03.0181.006

Update Rollup 4 for Exchange Server 2010 SP3        December 9, 2013       14.3.174.1        14.03.0174.001

Update Rollup 3 for Exchange Server 2010 SP3        November 25,           14.3.169.1        14.03.0169.001
                                                    2013

Update Rollup 2 for Exchange Server 2010 SP3        August 8, 2013         14.3.158.1        14.03.0158.001

Update Rollup 1 for Exchange Server 2010 SP3        May 29, 2013           14.3.146.0        14.03.0146.000

Exchange Server 2010 SP3                            February 12, 2013      14.3.123.4        14.03.0123.004

Build numbers for previous releases of Exchange Server 2010

                                                                                         ﾉ    Expand table

Product name                                      Release date          Build number         Build number
                                                                        (short format)       (long format)

Update Rollup 8 for Exchange Server 2010 SP2      December 9, 2013        14.2.390.3         14.02.0390.003

Update Rollup 7 for Exchange Server 2010 SP2      August 3, 2013          14.2.375.0         14.02.0375.000

Update Rollup 6 Exchange Server 2010 SP2          February 12, 2013       14.2.342.3         14.02.0342.003

Update Rollup 5 v2 for Exchange Server 2010 SP2   December 10, 2012      14.2.328.10         14.02.0328.010

Update Rollup 5 for Exchange Server 2010 SP2      November 13, 2012       14.3.328.5         14.03.0328.005

Update Rollup 4 v2 for Exchange Server 2010 SP2   October 9, 2012         14.2.318.4         14.02.0318.004

Update Rollup 4 for Exchange Server 2010 SP2      August 13, 2012         14.2.318.2         14.02.0318.002

Update Rollup 3 for Exchange Server 2010 SP2      May 29, 2012            14.2.309.2         14.02.0309.002

Update Rollup 2 for Exchange Server 2010 SP2      April 16, 2012          14.2.298.4         14.02.0298.004

Update Rollup 1 for Exchange Server 2010 SP2      February 13, 2012       14.2.283.3         14.02.0283.003

<!-- p.80 -->

 Product name                                      Release date        Build number     Build number
                                                                       (short format)   (long format)

 Exchange Server 2010 SP2                          December 4, 2011      14.2.247.5     14.02.0247.005

 Update Rollup 8 for Exchange Server 2010 SP1      December 10, 2012     14.1.438.0     14.01.0438.000

 Update Rollup 7 v3 for Exchange Server 2010 SP1   November 13, 2012     14.1.421.3     14.01.0421.003

 Update Rollup 7 v2 for Exchange Server 2010 SP1   October 10, 2012      14.1.421.2     14.01.0421.002

 Update Rollup 7 for Exchange Server 2010 SP1      August 8, 2012        14.1.421.0     14.01.0421.000

 Update Rollup 6 for Exchange Server 2010 SP1      October 27, 2011      14.1.355.2     14.01.0355.002

 Update Rollup 5 for Exchange Server 2010 SP1      August 23, 2011       14.1.339.1     14.01.0339.001

 Update Rollup 4 for Exchange Server 2010 SP1      July 27, 2011         14.1.323.6     14.01.0323.006

 Update Rollup 3 for Exchange Server 2010 SP1      April 6, 2011         14.1.289.7     14.01.0289.007

 Update Rollup 2 for Exchange Server 2010 SP1      December 9, 2010      14.1.270.1     14.01.0270.001

 Update Rollup 1 for Exchange Server 2010 SP1      October 4, 2010       14.1.255.2     14.01.0255.002

 Exchange Server 2010 SP1                          August 23, 2010      14.1.218.15     14.01.0218.015

 Update Rollup 5 for Exchange Server 2010          December 13, 2010     14.0.726.0     14.00.0726.000

 Update Rollup 4 for Exchange Server 2010          June 10, 2010         14.0.702.1     14.00.0702.001

 Update Rollup 3 for Exchange Server 2010          April 13, 2010        14.0.694.0     14.00.0694.000

 Update Rollup 2 for Exchange Server 2010          March 4, 2010         14.0.689.0     14.00.0689.000

 Update Rollup 1 for Exchange Server 2010          December 9, 2009      14.0.682.1     14.00.0682.001

 Exchange Server 2010 RTM                          November 9, 2009     14.0.639.21     14.00.0639.021

Exchange Server 2007
The tables in this section provide build numbers and general release dates for each version of
Microsoft Exchange Server 2007.

  ７ Note

  After you apply Exchange 2007 SP1 to an Exchange 2007 RTM Edge Transport server, the
  version information for the Edge Transport server isn't automatically updated in the
