---
title: "Exchange Server — pages 1961-2000"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1961-2000
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1961-2000
family: exchange
documentKind: "doc"
abstract: "IsHierarchyReady: This parameter indicates whether the public folder mailbox is ready to serve the public folder hierarchy to users. It's set to $True only after the entire hierarchy has been synced to the public folder mailbox. If the parameter is set to $False, users won't use"
---

# Exchange Server — pages 1961-2000

<!-- p.1961 -->

        IsHierarchyReady: This parameter indicates whether the public folder mailbox is ready
        to serve the public folder hierarchy to users. It's set to $True only after the entire
        hierarchy has been synced to the public folder mailbox. If the parameter is set to
        $False, users won't use it to access the hierarchy. However, if you set the
        DefaultPublicFolderMailbox property on a user mailbox to a specific public folder
        mailbox, the user will still access the specified public folder mailbox even if the
        IsHierarchyReady parameter is set to $False .

        IsExcludedFromServingHierarchy: This parameter prevents users from accessing the
        public folder hierarchy on the specified public folder mailbox. For load-balancing
        purposes, users are equally distributed across public folder mailboxes by default. When
        this parameter is set on a public folder mailbox, that mailbox isn't included in this
        automatic load balancing and won't be accessed by users to retrieve the public folder
        hierarchy. However, if you set the DefaultPublicFolderMailbox property on a user
        mailbox to a specific public folder mailbox, the user will still access the specified public
        folder mailbox even if the IsExcludedFromServingHierarchy parameter is set for that
        public folder mailbox.

A secondary hierarchy mailbox will serve only public folder hierarchy information to users if it's
specified explicitly on the users' mailboxes using the DefaultPublicFolderMailbox property, or if
the following conditions are met:

     The IsHierarchyReady property on the public folder mailbox is set to $True .

     The IsExcludedFromServingHierarchy property on the public folder mailbox is set to
      $False .

Public folder hierarchy
The public folder hierarchy contains the folders' properties and organizational information,
including tree structure. Each public folder mailbox contains a copy of the public folder
hierarchy. There's only one writeable copy of the hierarchy, which is in the primary public folder
mailbox. For a specific folder, the hierarchy information is used to identify the following:

     Permissions on the folder

     The folder's position in the public folder tree, including its parent and child folders

  ７ Note

  The hierarchy doesn't store information about email addresses for mail-enabled public
  folders. The email addresses are stored on the directory object in Active Directory.

<!-- p.1962 -->

Hierarchy synchronization
The public folder hierarchy synchronization process uses Incremental Change Synchronization
(ICS), which provides a mechanism to monitor and synchronize changes to an Exchange store
hierarchy or content. The changes include creating, modifying, and deleting folders and
messages. When users are connected to and using content mailboxes, synchronization occurs
every 15 minutes. If no users are connected to content mailbox, synchronization will be
triggered less often (every 24 hours).If a write operation such as a creating a folder is
performed on the primary hierarchy, synchronization is triggered immediately (synchronously)
to the content mailbox.

  ） Important

  Because there's only one writeable copy of the hierarchy, folder creation is proxied to the
  hierarchy mailbox by the content mailbox users are connected to.

In a large organization, when you create a new public folder mailbox, the hierarchy must
synchronize to that public folder before users can connect to it. Otherwise, users may see an
incomplete public folder structure when connecting with Outlook. To allow time for this
synchronization to occur without users attempting to connect to the new public folder mailbox,
set the IsExcludedFromServingHierarchy parameter on the New-Mailbox cmdlet when creating
the public folder mailbox. This parameter prevents users from connecting to the newly created
public folder mailbox. When synchronization is complete, run the Set-Mailbox cmdlet with the
IsExcludedFromServingHierarchy parameter set to false , indicating that the public folder
mailbox is ready to be connected to. You can use also the Get-PublicFolderMailboxDiagnostics
cmdlet to view the sync status by the SyncInfo and the AssistantInfo properties.

For more information, see Create a public folder.

Public folder content
Public folder content can include email messages, posts, documents, and eForms. The content
is stored in the public folder mailbox but isn't replicated across multiple public folders
mailboxes. All users access the same public folder mailbox for the same set of content.
Although a full text search of public folder content is available, public folder content isn't
searchable across public folders and the content isn't indexed by Exchange Search.

  ７ Note

  Outlook on the web is supported, but with limitations. You can add and remove public
  folders to your Favorites through Outlook, and then perform item-level operations such as

<!-- p.1963 -->

  creating, editing, deleting posts, and replying to posts through Outlook on the web.
  However, you can't create or delete public folders from Outlook on the web. Also, only
  Mail, Post, Calendar, and Contact public folders can be added to the Favorites list in
  Outlook on the web.

Migrate public folders
     You can migrate public folders in the following scenarios:

     From Exchange 2010 to Exchange 2016 or to Exchange Online.

     From Exchange 2016 or later to Exchange Online.

If you already have Exchange 2010 SP3 public folders in your organization prior to installing
Exchange 2016, you must migrate those public folders to Exchange 2016. To do this, use the
PublicFolderMigrationRequst cmdlets. For more information, see Use batch migration to
migrate Exchange 2010 public folders to Exchange 2016. If your organization is moving to
Exchange Online, you can migrate your public folders to the cloud and upgrade them at the
same time. For details, see Use batch migration to migrate legacy public folders to Microsoft
365, Office 365, and Exchange Online and Use batch migration to migrate Exchange Server
public folders to Exchange Online.

Due to the changes in how public folders are stored, Exchange 2010 mailboxes are unable to
access the public folder hierarchy on Exchange 2016 or on Exchange Online. However, user
mailboxes on Exchange 2016 can connect to Exchange 2010 public folders. Exchange 2016
public folders and legacy public folders can't exist in your Exchange organization
simultaneously. This effectively means that there's no coexistence between versions. Migrating
public folders to Exchange Server 2016 or Exchange Online is currently a one-time cutover
process.

For this reason, we recommend that prior to migrating your Exchange 2010 public folders, you
should first migrate your Exchange 2010 mailboxes to Exchange 2016 or Exchange Online. For
more information about migrating mailboxes, see Mailbox moves in Exchange Server, Migrate
email using the Exchange cutover method, and Perform a staged migration of email to
Microsoft 365 or Office 365.

Public folder moves
You can move public folders to a different public folder mailbox, and you can move public
folder mailboxes to different mailbox databases. To move public folders to different public
folder mailboxes, use the PublicFolderMoveRequest set of cmdlets. Subfolders under the

<!-- p.1964 -->

public folder that's being moved won't be moved by default. If you want to move a branch of
public folders, you can use the Move-PublicFolderBranch.ps1 script that's installed by default
with Exchange. For more information, see Move a Public Folder to a different Public Folder
Mailbox.

In addition to moving public folders, you can move public folder mailboxes to different
mailbox databases by using the MoveRequest set of cmdlets. This is the same set of cmdlets
that are used for moving regular mailboxes. For more information, see Move a public folder
mailbox to a different mailbox database.

PublicFolderMoveRequest cmdlets and the MoveRequest cmdlets use the Mailbox Replication
Service to move public folders asynchronously. That means that the cmdlet doesn't do the
actual work and, during most of the move, the public folder and public folder mailboxes will
still be available to users. Because the Mailbox Replication Service performs mailbox moves,
import and export requests, and public folder move requests, it's important to consider
throttling and workload management.

Public folder quotas
By default, new public folder mailboxes automatically inherit the size limits of the mailbox
database. As a result, to accurately evaluate the current storage quota status for the public
folder mailbox using the Get-Mailbox cmdlet, you first need to review the value of the
UseDatabaseQuotaDefaults property:

     If the value is True , the per-mailbox settings are ignored and the mailbox database limits
     are used.

     If the value is False , the per-mailbox settings are used.

If the UseDatabaseQuotaDefaults property is True and the ProhibitSendQuota,
ProhibitSendReceiveQuota, and IssueWarningQuota properties are unlimited , the mailbox size
isn't really unlimited. Instead, you need to use the Get-MailboxDatabase cmdlet and review the
corresponding mailbox database storage limits to find out what the limits for the mailbox are.
The default mailbox database quota limits are:

     IssueWarningQuota: 1.9 GB

     ProhibitSendQuota: 2 GB

     ProhibitSendReceiveQuota: 2.3 GB

To find the mailbox database quotas, run the Get-MailboxDatabase cmdlet.

<!-- p.1965 -->

To set the quotas on a public folder mailbox, use the Set-OrganizationConfig cmdlet with the
DefaultPublicFolderIssueWarningQuota and DefaultPublicFolderProhibitPostQuota parameters.

Disaster recovery
Public folders are built on mailbox infrastructure and use the same mechanisms for availability
and redundancy. Every public folder mailbox can have multiple redundant copies with
automatic failover, just like regular mailboxes. To learn more, see Plan for high availability and
site resilience.

In addition to the overall disaster recovery scenario, you can also restore public folders in the
following situations:

      Soft-deleted public folder restore: The public folder was deleted but is still within the
      retention period.

      Soft-deleted public folder mailbox restore: The public folder mailbox was deleted and is
      still within the mailbox retention period.

      Public folder mailbox restore from a recovery database: You can recover an individual
      public folder mailbox from backup when the deleted mailbox retention period has
      elapsed. You then extract data from the restored mailbox and copy it to a target folder or
      merge it with another mailbox.

In all of these situations, the public folder or public folder mailbox is recoverable by using the
MailboxRestoreRequest cmdlets.

For more information, see Restore public folders and public folder mailboxes from failed
moves.

<!-- p.1966 -->

FAQ about public folder migration
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

This article contains frequently asked questions about public folder migrations.

FAQs and more information
To learn more about public folders, see Public folders.

For more information on public folder migrations, see:

      Use batch migration to migrate Exchange 2010 public folders to Exchange 2016
      Migrate public folders from Exchange 2013 to Exchange 2016 or Exchange 2019
      Use batch migration to migrate legacy public folders to Microsoft 365, Office 365, or
      Exchange Online
      Use batch migration to migrate Exchange Server public folders to Exchange Online
      Use batch migration to migrate Exchange Server public folders to Microsoft 365 Groups

What are the supported public folder migration scenarios?
The following list details the available options for migrating public folders to Exchange or
Exchange Online.

      Exchange 2010 public folders (SP3 RU8 or later) can be migrated to Exchange 2016,
      Exchange Online, or Microsoft 365 groups.

      Exchange 2013 public folders (CU15 or later) can be migrated to Exchange 2016,
      Exchange 2019, Exchange Online, or Microsoft 365 groups.

      Exchange 2016 public folders (CU4 or later) can be migrated to Exchange Online or
      Microsoft 365 groups.

      Exchange 2019 public folders can be migrated to Exchange Online or Microsoft 365
      groups.

Currently only migrations to Exchange 2016 or Exchange 2019 in the same Active Directory
forest are supported. The cross forest migration of public folders from Exchange 2013,
Exchange 2016 or Exchange 2019 to another Exchange On-Premises organization is not
supported.

<!-- p.1967 -->

After migration to Exchange 2016, what happens to the
hierarchy on the source Exchange 2010 servers?
During the finalization stage in migration, a lock is placed on the source server to make it
inaccessible to users. This lock remains in place to prevent users from accessing the source
public folders after migration completes. Although you can release this lock, we don't
recommend doing so because the changes can't be synced to Exchange 2016.

When you migrate public folders, what happens to existing
public folder rules?
Public folder rules are migrated along with the data and are kept as public folder rules. They
aren't converted to mailbox rules.

What happens if hierarchy changes are performed on the
source after the initial .csv file was generated? How would
these reflect on the destination?
The .csv file is used to determine the mapping between the source hierarchy and the
destination mailbox. It contains only the top-level folders. Child folders under the top-level
folders are automatically migrated. Therefore, if a new child folder is added, it's migrated
during the process. If a new top-level folder is created, it will be created in the mailbox that
contains the writable copy of the hierarchy.

For the migration of a geo-distributed hierarchy, how can I
make sure that the public folders are created in the location
nearest to the target users?
As part of the migration process, a .csv file is generated (using the
publicfoldertomailboxmapgenerator.ps1 script). This file contains the folder-to-mailbox

mapping for the new hierarchy. You can use this .csv file to create public folder mailboxes in
the appropriate geographic location and modify the file to place the required folders in the
appropriate mailbox so they are near the target users.

The input .csv file can be generated by running the script AggregatePFData.ps1 , located in the
directory < Exchange Installation Directory>\V15\Scripts. Run the script as follows:

  PowerShell

<!-- p.1968 -->

  .\AggregatePFData.ps1 | Select-Object -property @{Name="FolderName"; Expression =
  {$_.Identity}}, @{Name="FolderSize"; Expression =
  {$_.TotalItemSize.Value.ToBytes()}} | Export-CSV -Path <Path followed by the name
  of the CSV>

Do existing public folder permissions migrate?
Yes, permissions automatically migrate at the folder level with the data. You don't have to
perform this step separately.

Are public folders going away?
No. Public folders are great for Outlook integration, simple sharing scenarios, and for allowing
large audiences to access the same data.

Which clients support public folders?
The currently supported Outlook clients for Exchange Server can access public folders.
However, users with mailboxes on Exchange 2016 servers can't connect to Exchange 2010
public folders using Exchange Web Services (EWS) clients (for example, Outlook 2016 for Mac).
We recommend that you migrate Exchange 2010 public folders to Exchange 2016 to maintain
access for those users.

Can public folders be accessed using smart phones
or mobile phones?
Public folder access works from Outlook for Windows desktop and Outlook for Mac. However,
smart phone client apps including Outlook for Android or Outlook for iOS do not support
connecting to public folders.

If you would like to have functionality similar to public folders with content accessible on
mobile devices, consult Learn about Microsoft 365 Groups       for an alternative.

Are there any limitations in the clients?
Outlook on the web (formerly known as Outlook Web App) is supported, but with some
limitations. You can add and remove public folders to your Favorites (if they are Mail, Post,
Calendar, or Contact public folders) and perform item level operations, such as creating,

<!-- p.1969 -->

editing, deleting posts, and replying to posts. But, you can't do the following in Outlook on the
web:

       Create or delete public folders

       Drag-and-drop content

       Access public folders located on servers running previous versions of Exchange

  ７ Note

  You can only create public folder rules that contain the element reply using a specific
  template in mail-enabled public folders. It is possible that pre-existing rules containing
  reply using a specific template will continue to work on non-mail-enabled public folders,
  but on those folders you cannot create new rules with this template element, or edit
  existing rules with this element.

In a hybrid scenario, Outlook on the web isn't supported for cross-premises public folders.
Users must be in the same location as the public folders to access them with Outlook on the
web. Outlook 2016 for Mac users can access public folders in a hybrid scenario if the following
conditions are true:

       You've followed the procedures at Hybrid Deployment procedures.

       The April 2016 update for Outlook 2016 for Mac has been installed on all clients.

How can I store a very large hierarchy in a public
folder mailbox?
For more information about public folder storage limits, see Limits for public folders.

How can I view the hierarchy public folder
mailbox?
Run the following command:

  PowerShell

  Get-OrganizationConfig | Format-List RootPublicFolderMailbox

For detailed syntax and parameter information, see Get-OrganizationConfig.

<!-- p.1970 -->

How can I create content mailboxes for public
folders using Exchange Management Shell
cmdlets?
Run the following command to create the first master hierarchy public folder mailbox and the
secondary hierarchy mailboxes.

  PowerShell

  New-Mailbox -PublicFolder -Name <name of public folder>

For more detail, see Create a public folder.

In Exchange 2010 there was an option for each
mailbox database to specify its public folder
database. How does this work now?
There's no longer a database-level setting. Instead, Exchange has a mailbox-level ability to
specify the public folder mailbox, but by default Exchange auto-calculates the per-user
hierarchy mailbox.

How are public folder metric tools being used in
Exchange?
You can use Get-PublicFolderStatistics and Get-PublicFolderItemStatistics cmdlets to get public
folder metrics data. This same solution hase been available since Exchange 2010, so nothing
has changed here. Public folders don't require additional reporting add-ons.

Can public folders distinguish between internal
versus third-party access to public folders?
Starting in Exchange 2013, public folder permissions are managed by using role-based access
control (RBAC); access control lists (ACLs) no longer used. You can use Get-
PublicFolderStatistics and Get-PublicFolderItemStatistics cmdlets to keep track of accounts that
are performing administrative tasks and then audit access accordingly. To learn more about
RBAC, see Understanding Role Based Access Control.

<!-- p.1971 -->

Does mailbox audit logging work against public
folders?
No. Not at this time.

If you would like to have functionality similar to public folders with audit logging, consult Learn
about Microsoft 365 Groups      for an alternative.

What are the limits on public folders? What are the
recommendations?
For more information about public folder limits, see Limits for public folders.

What are the recommendations for splitting public
folder mailboxes? Should they stay on the same
database?
In previous versions of Exchange, you could split public folders across public folder databases.
You can decide whether to split the content of a public folder mailbox to a mailbox on the
same mailbox database or a different database. Typically, a split is recommended to be on a
separate database, because you want to balance storage and I\O.

Can you set retention policies on public folders?
Just like in previous versions of Exchange, you can set retention limits on items. For details, see
Limits for public folders.

Can you specify which users can use a specific
public folder mailbox?
In Exchange 2010, you could specify which users had access to specific public folders. In
Exchange 2013 or later, you can set the default public folder mailbox per user. To do so, run the
Set-Mailbox cmdlet with the DefaultPublicFolderMailbox parameter. For example:

  PowerShell

  Set-Mailbox -Identity kweku@contoso.com -DefaultPublicFolderMailbox

<!-- p.1972 -->

  "PF_Administration"

If the master hierarchy goes down, what's the user
impact?
If the master hierarchy public folder mailbox goes down, users can view but not write to public
folders. To help prevent the hierarchy from going down, we recommend that you include your
public folders in a database availability group (DAG). To learn about DAGs, see Database
availability groups.

Can you change which public folder mailbox is the
master hierarchy mailbox?
No. If you try to change the master hierarchy mailbox, you'll receive an error.

Do public folders have full text searching
capabilities?
Yes, full text search has been available for public folders since Exchange 2013. However, you
can't search across multiple public folders.

<!-- p.1973 -->

Limits for public folders in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016        2019   Subscription Edition

In Exchange Server, public folders are based on a mailbox architecture that benefits from the
resiliency of a Database Availability Group (DAG) and other mailbox enhancements. However,
there are limits and performance considerations that you should take into account.

Limits
The following table lists the limits for public folders in on-premises Exchange Server. Unless the
limits are stated as recommended, the values listed in this table are the supported limits for
public folders.

  ） Important

  Looking for Exchange Online limits for Microsoft 365 or Office 365? See Exchange Online
  Limits.

                                                                                        ﾉ   Expand table

 Item              Limits             Notes

 Total number of   1,000              1,000 is the limit for Exchange Server 2016 CU2 or later.
 public folder                        Although you can create more than 1,000 public folder
 mailboxes                            mailboxes, it isn't officially supported. See Create a public folder
                                      mailbox.

 Total public      1,000,000          Although you can create more than 1,000,000 public folders, it
 folders in                           isn't officially supported. For any deployment of 100,000 or more
 hierarchy                            public folders, we recommend reading Considerations when
                                      deploying public folders.

 Subfolders        10,000             Although you can create more than 1,000 subfolders under a
 under the                            parent folder, it isn't recommended. The limit can be enforced
 parent folder                        with the FolderHierarchyChildrenCountReceiveQuota parameter
                                      on the Set-Mailbox cmdlet.

 Folder depth      300                The folder depth is the number levels of nested folders that can
                                      exist in one branch of a public folder tree. The limit can be
                                      enforced with the FolderHierarchyDepthReceiveQuota parameter
                                      on the Set-Mailbox cmdlet.

<!-- p.1974 -->

Item             Limits                 Notes

Maximum          1 million              The limit can be enforced with the
messages per                            MailboxMessagesPerFolderCountRecieveQuota parameter on the
public folder                           Set-Mailbox cmdlet.

Maximum          10 GB                  This limit doesn't include subfolders beneath a single folder. See
individual                              Configure storage quotas for a mailbox.
public folder
size

Public folder    100 GB                 Although public folder mailbox size can exceed 100 GB, it isn't
mailbox size                            officially supported. See Configure storage quotas for a mailbox.

Number of user   2,000 concurrent       We recommend that you configure your hierarchy so that you've
logons per       user logons            no more than 2,000 users per public folder mailbox. For
public folder                           example, if you have 20,000 users, you should have 10 public
mailbox                                 folder mailboxes.

Moved item       14 days                Use the DefaultPublicFolderMovedItemRetention parameter on
retention        recommended            the Set-OrganizationConfig cmdlet.

Age limit        We recommend           These settings can be set at the following levels:
                 that you set this as
                 the same default       Organizational level: Use the DefaultPublicFolderAgeLimit
                 that you use for       parameter on the Set-OrganizationConfig cmdlet.
                 regular mailboxes.
                                        Folder level: Use the AgeLimit parameter on the Set-PublicFolder
                                        cmdlet.

Deleted item     We recommend           These settings can be set at the following levels:
retention        that you set this as
                 the same default       Organizational level: Use the
                 that you use for       DefaultPublicFolderMovedItemRetention parameter on the Set-
                 regular mailboxes.     OrganizationConfig cmdlet.

                                        Mailbox level: Use the RetainDeletedItemsFor on the Set-Mailbox
                                        cmdlet.

                                        Folder level: Use the RetainDeleteItemsFor parameter on the Set-
                                        PublicFolder cmdlet.

Maximum          500,000                This is the maximum number of public folders you can move to
number of                               Exchange from Exchange 2010 in a single migration. Although
public folders                          you can attempt to migrate more than 500,000 folders, it isn't
that can be                             officially supported. For details on migrating public folders, see
migrated from                           Use batch migration to migrate public folders from Exchange
Exchange 2010                           2010 to Exchange 2016.
to Exchange
2016

<!-- p.1975 -->

<!-- p.1976 -->

Considerations when deploying Exchange
public folders
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Although there are many advantages to using Exchange public folders, there are some things
to consider before implementing them in your organization.

Deployment considerations for public folders
This article contains factors to consider before you deploy public folders in your organization,
especially if you plan to have a large number of public folders. Exchange Server supports up to
one million public folders.

      Activity in a public folder directly impacts the load that's placed on the public folder
      mailbox where the folder is located. To avoid client connectivity issues, such as high
      latency or the inability to access a public folder, we recommend you do the following:

         Don't let public folder mailboxes exceed 50% of the mailbox size limit. If this happens
         consider using the Split-PublicFolderMailbox.ps1 script located in C:\Program
         Files\Microsoft\Exchange Server\V15\Scripts folder on the Exchange server to move
         some public folders to a new public folder mailbox.

         Consider moving heavily used public folders to a dedicated public folder mailbox.

         Exclude heavily used public folders from serving public folder hierarchy. You can do
         this by setting the IsExcludedFromServingHierarchy property on the public folder
         mailbox using the Set-Mailbox cmdlet.

         For large organizations with many public folders, consider adding additional public
         folder mailboxes to distribute the load of servicing public folder hierarchy requests.

      Place the primary public folder mailbox in a DAG to improve availability of the mailbox.
      The primary public folder mailbox is the authoritative copy of the public folder hierarchy.

      Place secondary public folder mailboxes in a DAG or back up the mailboxes frequently.

      Place public folder mailboxes in the geographical location that's nearest the users that
      will access the public folder content in them.

      Improve public folder hierarchy access times by using the DefaultPublicFolderMailbox
      property on the users' mailboxes to specify a public folder mailbox close to them. This will

<!-- p.1977 -->

prevent those users from retrieving the public folder hierarchy from a public folder
mailbox in other geographical locations.

In deployments with more than 50 secondary public folder mailboxes, we recommend
that you don't store public folder content in the primary public folder mailbox. This
dedicates the primary public folder mailbox to synchronizing the hierarchy with the
secondary public folder mailboxes.

Exchange 2016 doesn't support public folder databases. As a result, Outlook on the web
users won't be able to access Exchange 2010 public folders. Exchange 2016 users can
access Exchange 2010 public folders with Outlook or Outlook for Mac.

Outlook on the web is supported, but with limitations. You can add and remove public
folders from your Favorites and perform item-level operations such as creating, editing,
deleting posts, and replying to posts. However, you can't create or delete public folders
from Outlook on the web. Also, only Mail, Post, Calendar, and Contact public folders can
be added to the Favorites list in Outlook on the web.

Although a full text search of public folder content is available, public folder content isn't
searchable across public folders, and the content isn't indexed by Exchange Search.

You must use Outlook 2010 or later to access public folders on Exchange servers.

Retention policies aren't supported for public folder mailboxes.

<!-- p.1978 -->

Migrate your public folders to Microsoft
365 Groups
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

This article provides a comparison of public folders and Microsoft 365 Groups, and how one or
the other might be the best solution for your organization. Public folders have been around as
long as Exchange, whereas Groups were introduced more recently. If you want to migrate some
or all of your public folders to Groups, this article describes how the process works, and
provides links to the articles that walk you through the process, step by step.

What are public folders?
Public folders contain different kinds of data and are organized in a hierarchical structure.

Public folders aren't recommended for the following situations:

      Archiving data: Users with mailbox limits sometimes use public folders instead of
      mailboxes to archive data. This practice isn't recommended because it affects storage in
      public folders and undermines the goal of mailbox limits.

      Document sharing and collaboration: Public folders don't provide document
      management features, such as versioning, controlled check-in and check-out
      functionality, and automatic notifications of content changes.

What are Microsoft 365 Groups?
Microsoft 365 groups let you choose a set of people who you wish to collaborate with, and
then easily set up a collection of resources for those people to share. You don't have to worry
about manually assigning permissions to those resources, because adding members to your
group automatically gives the members the permissions they need to access the tools and
resources your group provides. Groups are also the new and improved experience for those
tasks that were previously handled by distribution lists and shared mailboxes.

For the full Groups story, see Learn about Microsoft 365 Groups     .

Should you migrate your public folders to
Microsoft 365 Groups?

<!-- p.1979 -->

Microsoft 365 Groups is the latest collaboration offering from Microsoft, which means there are
many reasons why they would be a preferable solution over public folders, a much older
technology. In Outlook, for example, Groups can replace mail-enabled public folders
altogether. Compiling a list of every scenario in which Microsoft 365 Groups works better than
public folders is impossible, but here are the highlights:

     Collaboration over email: Groups in Outlook has a dedicated Conversations space that
     stores all the emails and lets users collaborate over them. The group can even be set up
     to receive messages from people outside the group or organization. If you're currently
     using mail-enabled public folders to store project-related discussions, for example, or
     purchase orders that need to be viewed by a team of people, using groups would be an
     improvement. Groups are also better for situations when you simply want to broadcast
     information to a set of users.

     Collaboration over documents: In Outlook, Groups has a dedicated Files tab that displays
     all files from the group's SharePoint team site, and from mail attachments. You get one
     view of all the files, so you don't have to go searching for them like you would in public
     folders. Co-authoring also becomes easier. If you're using public folders for storing files
     meant to be consumed by multiple people, consider migrating to Groups.

     Shared calendar: Upon creation, every group gets a shared calendar (see Calendar
     sharing in Microsoft 365    . Any member of the group can create events on that calendar.
     When you favorite a group, that group's calendar can be displayed alongside your
     personal calendar. You can also subscribe to a group's events, in which case events
     created in that group appear in your personal calendar. If you're using public folders to
     host calendars for your team, such as a schedule or a timetable, Groups would be an
     improved experience.

     Simplified permissions: When you assign users to a group, they immediately get the
     permissions they need, whereas with public folders you need to manually assign the
     proper permissions. Members can be added as "owners" or "members." Owners have full
     rights in the group, including the ability to perform group management tasks. Members
     can also create content and edit files like owners, but they can't delete content that they
     haven't created. If the public folders' permissions model is too overwhelming for you and
     you want something simple and quick, Microsoft 365 Groups is the way to go.

     Mobile and Web presence: Public folders can't be accessed through mobile devices and
     have a limited set of functionalities on the Web. Microsoft 365 Groups, on the other hand,
     is accessible through Outlook mobile apps and has a richer set of features on the Web. If
     your team is on the move and requires mobile access, then you should be using Microsoft
     365 Groups.

<!-- p.1980 -->

     Access to a wide range of Microsoft 365 or Office 365 apps: When you create a group,
     you unlock access to a wide range of applications from the Microsoft 365 or Office 365
     suite. You get a SharePoint team site for storing files and a plan on Planner to track your
     tasks. Microsoft 365 Groups is the membership service that combines elements of the
     entire Microsoft 365 or Office 365 suite.

While Microsoft 365 Groups offers many advantages, you should be aware of a major
difference that you'll notice after leaving the public folders experience. This difference is
primarily:

     Granular permission roles: While public folders have various permission roles, Microsoft
     365 Groups only provides two: owner and member.

Before you move to Groups, it's also a good idea to make note of the various limits that come
with creating and maintaining groups. For more information, see How do I manage my groups?
in Learn about Microsoft 365 Groups       .

Migrating public folders to Microsoft 365 Groups
If you decide to switch to Microsoft 365 Groups, you can use a process known as batch
migration to move your email and calendar content from your existing public folders to
Groups. The specific steps for running a batch migration depend on which version of Exchange
currently hosts your public folder hierarchy. At the end of this article, you'll find links to
instructions that walk you through the batch migration process.

As a prerequisite to migrating public folders from Exchange to Microsoft 365 groups, you must
ensure that the Exchange Mail Public Folder option in the Microsoft Entra Connect tool is not
checked. If this option is - by any chance - checked, then uncheck it before you start migration
of the public folders. By default, this option is unchecked.

  ７ Note

  When you finish migrating a mail-enabled public folder to a particular group in Microsoft
  365 or Office 365, all the emails addressed to the public folder will at that point be
  received by the group.

Key benefits of batch migrations are:

     Mailbox Replication Service (MRS)-based migration: The migration process uses
     migration batch cmdlets. Migration to multiple groups can be triggered together in a
     single migration batch. There are also scripts available to help in the migration process.

<!-- p.1981 -->

     Supports mail and calendar public folders: Copied emails and posts will appear as in
     Groups as group conversations, and copied calendar items will be visible in group
     calendars. Other public folder types, such as tasks and contacts, are currently not
     supported for this migration.

     On-premises public folders can be migrated directly to Microsoft 365 Groups: This
     migration doesn't require you to first move your public folders to Microsoft 365 or Office
     365 and then move to Groups. The MRS data copy cmdlets read the public folder data
     directly from your on-premises environment and then copy the data to Microsoft 365
     Groups. Exchange public folders will require an MRS Proxy-based endpoint.

     Not an "all or nothing" migration: You get to choose specific public folders to migrate to
     Groups, and only those chosen public folders get migrated.

     One-shot data copy: Batch migrations are designed to be a one-time data copy from
     source public folders to target groups, without the complexities of incremental
     synchronization and finalization.

     Merges public folder data with existing data in a group: The data copy will merge the
     public folder content with the existing group's content, if any. If there's a need for
     incremental data copy, you can run the data copy as many times as you need to copy
     incremental data to the group.

Overview of batch migrations
The following steps outline the overall process of migrating your public folder content to
Microsoft 365 Groups in a batch migration.

   1. Select source: Choose the public folders that you want to migrate. You can choose any
     folder containing mail or calendar content.

   2. Create target: Create corresponding groups for your folders, with the desired
     configurations, such as members, privacy settings, and data classification.

   3. Copy data: Use the migration batch cmdlets to copy data from public folders to Groups.

   4. Lock source: Lock the public folders once you've verified the data in Groups.

   5. Cutover: Copy any new data that has been created between Steps 3 and 4.

Your public folders and their corresponding groups will remain online for your users during the
Select source and Copy data steps. After the Copy data step, you can evaluate whether or not
to proceed with the rest of the migration, based on the Groups experience, and whether or not
it suits your users and your organization. You can roll back your migration and resume using

<!-- p.1982 -->

public folders at that point. If you do proceed with the migration, after the Cutover step
completes, you can delete the original public folders. Even post-migration, it's possible to roll
back to public folders, provided you've saved your backup files from the migration process and
you haven't deleted your original public folders.

Batch migration prerequisites and step-by-step instructions
The following prerequisites are required in your Exchange environment before you can run a
batch migration. The specific prerequisites depend on which version of Exchange you're
currently running.

   1. If your public folders are on-premises, your servers need to be running one of the
     following versions:

           Exchange 2010 SP3 RU8 or later

           Exchange 2013 CU15 or later s

           Exchange 2016 CU4 or later

           Exchange 2019

   2. If your public folders are on-premises, you must have an Exchange Hybrid environment
     set up. For more information, see Exchange Server Hybrid Deployments.

Migration instructions
Click one of the following links for step-by-step instructions on running a batch migration.

     Use batch migration to migrate your Exchange Online public folders to Microsoft 365
     Groups

     Use batch migration to migrate your Exchange 2013 public folders to Microsoft 365
     Groups

     Use batch migration to migrate your Exchange 2010 public folders to Microsoft 365
     Groups

<!-- p.1983 -->

Public folder procedures in Microsoft
Exchange
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Use one or more of the procedures listed below to get your public folder infrastructure up and
running, and to perform other necessary tasks for managing public folders.

Set up public folders in a new organization

Configure legacy on-premises public folders for a hybrid deployment

Configure modern on-premises public folders for a hybrid deployment

Use batch migration to migrate Exchange 2010 public folders to Exchange 2016

Use batch migration to migrate legacy public folders to Microsoft 365 or Office 365 and
Exchange Online

Use batch migration to migrate Exchange Server public folders to Exchange Online

Migrate public folders from Exchange 2013 to Exchange 2016 or Exchange 2019

Configure legacy public folders where user mailboxes are on Exchange 2016 servers

Create a public folder mailbox

Create a public folder

Using favorite public folders in Outlook on the web

Mail-enable or mail-disable a public folder

Update the public folder hierarchy

Remove a public folder

Move a public folder mailbox to a different mailbox database

Move a public folder to a different public folder mailbox

Restore public folders and public folder mailboxes from failed moves

View statistics for public folders and public folder items

<!-- p.1984 -->

Configure legacy on-premises public folders
for a hybrid deployment of Exchange Server
APPLIES TO:      2016      2019      Subscription Edition

In a hybrid deployment, your users can be in Exchange Online, on-premises Exchange, or both,
and your public folders are either in Exchange Online or on-premises Exchange. Public folders
can only reside in one place, so you must decide where they belong. They can't be in both
locations. Public folder mailboxes are synchronized to Exchange Online by the Directory
Synchronization service. However, mail-enabled public folders aren't synchronized across
premises.

This article describes how to synchronize mail-enabled public folders when your users are in
Microsoft 365 and your public folder are in Exchange 2010 SP3 or later. However, a cloud user
who isn't represented by a MailUser object on-premises Exchange (local to the target public
folder hierarchy) can't access legacy or on-premises Exchange public folders.

  ７ Note

  This topic refers to the Exchange 2010 SP3 or later servers as the legacy Exchange server.

You use the following scripts to sync your mail-enabled public folders. The scripts are initiated by
a Windows task that runs in the on-premises environment:

     Sync-MailPublicFolders.ps1 : This script synchronizes mail-enabled public folder objects

     from your local on-premises Exchange deployment with Exchange Online. It uses the local
     on-premises Exchange deployment as authoritative to determine what changes need to be
     applied to Exchange Online. The script creates, update, or delete mail-enabled public folder
     objects in the cloud based on what exists in the local on-premises Exchange deployment.

When you complete this procedure, your on-premises and cloud users can access the same on-
premises public folder infrastructure.

What hybrid versions of Exchange work with
public folders?

<!-- p.1985 -->

The following table describes the supported version and location combinations of user mailboxes
and public folders. "Hybrid not applicable" is still a supported scenario, but isn't considered a
hybrid scenario because both the public folders and the users are residing in the same location.

                                                                                    ﾉ   Expand table

 Scenario                          On-premises             On-premises Exchange    Exchange Online
                                   Exchange 2010 User      2016/2019 User          User Mailbox
                                   Mailbox                 Mailbox

 On-premises Exchange 2010         Hybrid not applicable   Hybrid not applicable   Supported
 Public Folders

 On-premises Exchange 2013,        Hybrid not applicable   Hybrid not applicable   Supported
 Exchange 2016, or Exchange 2019
 Public Folders

 Exchange Online Public Folders    Not supported           Supported               Hybrid not
                                                                                   applicable

A hybrid configuration with Exchange 2003 public folders isn't supported. If you're running
Exchange 2003 in your organization, you must move all public folder databases and replicas to
Exchange 2010 SP3 or later. No public folder replicas can remain on Exchange 2003.

Step 1: What do you need to know before you begin?
     These instructions assume that you have used the Hybrid Configuration Wizard to configure
     and synchronize your on-premises and Exchange Online environments and that the DNS
     records used for most users' Autodiscover references an on-premises end-point. For more
     information, see Hybrid Configuration Wizard.

     These instructions assume that Outlook Anywhere is enabled and functional on the on-
     premises legacy Exchange servers. For information on how to enable Outlook Anywhere, see
     Outlook Anywhere.

     Implementing legacy public folder coexistence for a hybrid deployment of Exchange with
     the cloud might require you to fix conflicts during the import procedure. Conflicts can
     happen due to non-routable email address assigned to mail enabled public folders, conflicts
     with other users and groups in Exchange Online, and other attributes.

     These instructions assume your Exchange Online organization has been upgraded to a
     version that supports public folders.

<!-- p.1986 -->

   In Exchange Online, you must be a member of the Organization Management role group.
   This role group is different from the permissions assigned to you when you subscribe to
   Exchange Online. For details about how to enable the Organization Management role
   group, see Manage role groups.

   In Exchange 2010, you must be a member of the Organization Management or Server
   Management Role Based Access Control (RBAC) role groups. For details, see Add Members
   to a Role Group.

   In order to access public folders cross-premises, users must upgrade their Outlook clients to
   the November 2012 or later Outlook public update.

      To download the November 2012 Outlook update for Outlook 2010, see Update for
      Microsoft Outlook 2010 (KB2687623) 32-Bit Edition      .

      To download the November 2012 Outlook update for Outlook 2007, see Update for
      Microsoft Office Outlook 2007 (KB2687404)       and download in preferred language.

   Outlook 2016 for Mac and Outlook for Mac for Microsoft 365 are supported for cross-
   premises public folders if the following conditions are true:
      The April 2016 update for Outlook 2016 for Mac is installed.
      Exchange 2016 CU2 or later.
      Exchange 2013 CU14 or later.

   After you have followed the instructions in this article to configure your on-premises public
   folders for a hybrid deployment, users who are external to your organization won't be able
   to send messages to your on-premises public folders unless you take additional steps. For
   example:
      Set the accepted domain for the public folders to Internal Relay. For more information,
      see Manage accepted domains in Exchange Online.
      Disable Directory Based Edge Blocking (DBEB). For more information, see Use Directory
      Based Edge Blocking to Reject Messages Sent to Invalid Recipients.

   In hybrid mode, Exchange Online users can't access public folders using Outlook on the web
   (formerly known as Outlook Web App).

Step 2: Make remote public folders discoverable
 1. If your public folders are on Exchange 2010 servers, you must install Client Access services
   on all mailbox servers that have a public folder database. This enables the Exchange

<!-- p.1987 -->

  RpcClientAccess service to run, which enables all clients to access public folders. For more
  information, see Install Exchange Server 2010.

    ７ Note

    This server doesn't have to be part of the Client Access load balancing. For more
    information, see Understanding Load Balancing in Exchange 2010.

2. Create an empty mailbox database on each public folder server.

  For Exchange 2010, run the following command in the Exchange Management Shell. This
  command excludes the mailbox database from the mailbox provisioning load balancer. This
  action prevents new mailboxes from automatically being added to this database.

    PowerShell

    New-MailboxDatabase -Server <PFServerName_with_CASRole> -Name <NewMDBforPFs> -
    IsExcludedFromProvisioning $true

  For Exchange 2007, run the following command in the Exchange Management Shell:

    PowerShell

    New-MailboxDatabase -StorageGroup "<PFServerName>\StorageGroup>" -Name
    <NewMDBforPFs>

    ７ Note

    We recommend that the only mailbox that you add to this database is the proxy
    mailbox that you'll create in the next step. No other mailboxes should be created on
    this mailbox database.

3. Create a proxy mailbox within the new mailbox database, and hide the mailbox from the
  address book. The SMTP address of this mailbox is returned by AutoDiscover as the
  DefaultPublicFolderMailbox SMTP. By resolving this SMTP address the client can reach the
  legacy exchange server for public folder access.

    PowerShell

    New-Mailbox -Name <PFMailbox1> -Database <NewMDBforPFs>

<!-- p.1988 -->

       PowerShell

       Set-Mailbox -Identity <PFMailbox1> -HiddenFromAddressListsEnabled $true

   4. For Exchange 2010, enable Autodiscover to return the proxy public folder mailboxes.

       PowerShell

       Set-MailboxDatabase <NewMDBforPFs> -RPCClientAccessServer
       <PFServerName_with_CASRole>

   5. Repeat the preceding steps for every public folder server in your organization.

Step 3: Download the scripts
   1. Download the following file from Mail-enabled Public Folders - directory sync script   :

           Sync-MailPublicFolders.ps1

   2. Save the files to the local computer where you're running PowerShell. For example,
     C:\PFScripts.

Step 4: Configure directory synchronization
The Directory Synchronization service doesn't synchronize mail-enabled public folders. Running
the following script will synchronize the mail-enabled public folders across premises. You need to
recreate special permissions assigned to mail-enabled public folders in the cloud since cross-
premise permission aren't supported in Hybrid Deployment scenarios.

  ７ Note

  Synchronized mail-enabled public folders will appear as mail contact objects for mail flow
  purposes and will not be viewable in the Exchange admin center. See the Get-
  MailPublicFolder command. To recreate the SendAs permissions in the cloud, use the Add-
  RecipientPermission command.

   1. On the legacy Exchange server, run the following command to synchronize mail-enabled
     public folders from your local on-premises Active Directory to the cloud.

       PowerShell

<!-- p.1989 -->

       Sync-MailPublicFolders.ps1 -Credential (Get-Credential) -
       CsvSummaryFile:sync_summary.csv

     Where Credential is your cloud username and password, and CsvSummaryFile is the path to
     where you would like to log synchronization operations and errors, in .csv format.

  ７ Note

  Before running the script, we recommend that you first simulate the actions that the script
  would take in your environment by running it as previously described with the -WhatIf
  parameter. We also recommend that you run this script daily to synchronize your mail-
  enabled public folders.

Step 5: Configure Exchange Online users to access on-
premises public folders
The final step in this procedure is to configure the Exchange Online organization and to allow
access to the legacy on-premises public folders.

You point to all of the proxy public folder mailboxes that you created in Step 2: Make remote
public folders discoverable to enable theExchange Online organization to access the on-premises
public folders.

Run the following command in Exchange Online PowerShell. To learn how to use Windows
PowerShell to connect to Exchange Online, see Connect to Exchange Online PowerShell.

 PowerShell

 Set-OrganizationConfig -PublicFoldersEnabled Remote -RemotePublicFolderMailboxes
 PFMailbox1,PFMailbox2,PFMailbox3

You must wait until Active Directory synchronization has completed to see the changes. This
process can take up to 3 hours to complete. If you don't want to wait for the recurring
synchronizations that occur every three hours, you can force directory synchronization at any
time. For detailed steps to force directory synchronization, see Microsoft Entra Connect Sync:
Scheduler. Exchange Online randomly selects one of the public folder mailboxes that's supplied
in this command.

  ） Important

<!-- p.1990 -->

  A cloud user who isn't represented by a MailUser object on-premises (local to the target
  public folder hierarchy) won't be able to access legacy, Exchange 2016, or Exchange 2019
  on-premises public folders. See the Knowledge Base article Exchange Online users can't
  access legacy on-premises public folders for a solution.

How do I know this procedure worked?
Using a cloud user account, open Outlook and do the following public folder tests:

     View the hierarchy.
     Check permissions
     Create and delete public folders.
     Post content to and delete content from a public folder.

Last updated on 06/03/2026

<!-- p.1991 -->

Use batch migration to migrate Exchange
2010 public folders to Exchange 2016 or
Exchange 2019
APPLIES TO:      2016      2019      Subscription Edition

Migrate your public folders from Exchange Server 2010 SP3 RU8 to Exchange Server 2016or
Exchange 2019 within the same forest.

We refer to the Exchange 2010 SP3 RU8 or later server as the legacy Exchange server.

You'll perform the migration by using the *MigrationBatch cmdlets, and the
*PublicFolderMigrationRequest cmdlets for troubleshooting. In addition, you'll use the following
PowerShell scripts:

      Export-PublicFolderStatistics.ps1 : This script creates the folder name-to-folder size

     mapping file.

      PublicFolderToMailboxMapGenerator.ps1 : This script creates the public folder-to-mailbox

     mapping file.

      Create-PublicFolderMailboxesForMigration.ps1 : This script creates the target public folder

     mailboxes for the migration. In addition, this script calculates the number of mailboxes
     necessary to handle the estimated user load, based on the guidelines for the number of
     user logons per public folder mailbox recommended in Limits for public folders.

The Step 1: Download the migration scripts section provides details about where to download
these scripts. Be sure to download all scripts to the same location.

For additional management tasks related to public folders, see Public folder procedures.

What migration pathways are supported for Exchange
Server versions?
Exchange supports moving your public folders from the following legacy versions of Exchange
Server:

     Exchange 2010 SP3 RU8 or later

<!-- p.1992 -->

What do you need to know before you begin?
    Before you begin, we recommend that you read this topic in its entirety as downtime is
    required for some steps.

    The Exchange 2010 server needs to be running Exchange 2010 SP3 RU8 or later.

    The maximum number of public folders that can be migrated to Exchange 2016 in a single
    migration is 500,000.

    In Exchange 2016, you need to be a member of the Organization Management role group.
    For details about how to enable the Organization Management role group, see Manage role
    groups.

    In Exchange 2010, you need to be a member of the Organization Management or Server
    Management RBAC role groups. For details, see Add Members to a Role Group.

    Before you migrate, you should consider the Limits for public folders.

    Before you migrate, move all user mailboxes to Exchange 2016, because users with
    Exchange 2010 mailboxes will not have access to public folders on Exchange 2016. For
    details, see Mailbox moves in Exchange Server.

    After the migration is complete, if you want external senders to send mail to the migrated
    mail-enabled public folders, the Anonymous user needs to be granted at least the Create
    Items permission. If you don't do this, external senders will receive a delivery failure
    notification and the messages won't be delivered to the migrated mail-enabled public
    folder. To read more about how to set permissions on the Anonymous user, see Mail-enable
    or mail-disable a public folder.

    You must use a single migration batch to migrate all of your public folder data. Exchange
    allows creating only one migration batch at a time. If you attempt to create more than one
    migration batch simultaneously, the result will be an error.

    For information about keyboard shortcuts that may apply to the procedures in this topic,
    see Keyboard shortcuts in the Exchange admin center.

 ） Important

 Before you begin your migration, make sure you migrate your arbitration mailbox to the
 target Exchange server. Otherwise, your migration batch will hang in the Starting state. To

<!-- p.1993 -->

  identify your migration arbitration mailbox, run the following cmdlet:
  Get-Mailbox -Arbitration -Identity Migration.*

Step 1: Download the migration scripts
   1. Download all scripts and supporting files from Public Folders Migration Scripts .

   2. Save the scripts to the local computer on which you'll be running PowerShell. For example,
     C:\PFScripts. Make sure all scripts are saved in the same location.

Step 2: Prepare for the migration
Perform the following prerequisite steps before you begin the migration.

Prerequisite steps on the Exchange 2010 server
   1. For verification purposes at the end of migration, we recommend that you first run the
     following commands on the Exchange 2010 server to take snapshots of your current public
     folder deployment:

          Run the following command to take a snapshot of the original source folder structure:

            PowerShell

            Get-PublicFolder -Recurse | Export-CliXML
            C:\PFMigration\Legacy_PFStructure.xml

          Run the following command to take a snapshot of public folder statistics such as item
          count, size, and owner:

            PowerShell

            Get-PublicFolderStatistics | Export-CliXML
            C:\PFMigration\Legacy_PFStatistics.xml

          Run the following command to take a snapshot of the permissions:

            PowerShell

            Get-PublicFolder -Recurse | Get-PublicFolderClientPermission | Select-Object
            Identity,User -ExpandProperty AccessRights | Export-CliXML
            C:\PFMigration\Legacy_PFPerms.xml

<!-- p.1994 -->

2. If the name of a public folder contains a backslash ( \ ), migration will create the migrated
  public folders in the parent public folder. Before you migrate, we recommend that you
  rename any public folders that have a backslash in the name.

  To locate public folders in Exchange 2010 that have a backslash in the name, run the
  following command:

    PowerShell

    Get-PublicFolderStatistics -ResultSize Unlimited | Where {($_.Name -like "*\*") -
    or ($_.Name -like "*/*") } | Format-List Name, Identity

  If any public folders are returned, you can rename them by running the following command:

    PowerShell

    Set-PublicFolder -Identity <public folder identity> -Name <new public folder
    name>

3. Make sure there isn't a record of a previously successful migration by running the following
  command:

    PowerShell

    Get-OrganizationConfig | Format-List PublicFoldersLockedforMigration,
    PublicFolderMigrationComplete

  A previously successful migration will set the PublicFoldersLockedforMigration or
  PublicFolderMigrationComplete properties to the value True , which will cause your new
  migration request to fail.

  If the property values are True , run the following command to change them to False :

    PowerShell

    Set-OrganizationConfig -PublicFoldersLockedforMigration $false -
    PublicFolderMigrationComplete $false

    ７ Note

    After resetting these properties, you need to wait for Exchange to detect the new
    settings. This may take up to two hours to complete.

<!-- p.1995 -->

For detailed syntax and parameter information, see the following topics:

     Get-PublicFolder

     Get-PublicFolderDatabase

     Set-PublicFolder

     Get-PublicFolderStatistics

     Get-PublicFolderClientPermission

     Get-OrganizationConfig

     Set-OrganizationConfig

Prerequisite steps on the Exchange 2016 server
   1. Make sure there are no existing public folder migration requests. If there are, clear them or
     your own migration request will fail. This step isn't required in all cases; it's only required if
     you think there may be an existing migration request in the pipeline.

       ） Important

       Before removing a migration request, it is important to understand why there was an
       existing one. Running the following commands will determine when a previous request
       was made and help you diagnose any problems that may have occurred. You may need
       to communicate with other administrators in your organization to determine why the
       change was made.

          Run the following command to discover any existing batch migration requests:

            PowerShell

            $batch = Get-MigrationBatch | ?{$_.MigrationType.ToString() -eq
            "PublicFolder"}

          Run the following command to remove any existing public folder batch migration
          requests.

            PowerShell

<!-- p.1996 -->

            $batch | Remove-MigrationBatch -Confirm:$false

   2. Make sure no public folders or public folder mailboxes exist on the Exchange 2016 servers
     by running the following command:

       PowerShell

       Get-Mailbox -PublicFolder

     If the command didn't return any public folder mailboxes, continue to Step 3: Generate the
     .csv files. If the command returned any public folders, run the following command to see if
     any public folders exist:

       PowerShell

       Get-PublicFolder

     If you have any public folders, run the following commands to remove them. Make sure
     you've saved any information that was in the public folders.

       ７ Note

       All information contained in the public folders will be permanently deleted when you
       remove them.

       PowerShell

       Get-Mailbox -PublicFolder | Where {$_.IsRootPublicFolderMailbox -eq $false} |
       Remove-Mailbox -PublicFolder -Force -Confirm:$false

       PowerShell

       Get-Mailbox -PublicFolder | Remove-Mailbox -PublicFolder -Force -Confirm:$false

For detailed syntax and parameter information, see the following topics:

     Get-MigrationBatch

     Get-Mailbox

     Get-PublicFolder

<!-- p.1997 -->

   Get-MailPublicFolder

   Disable-MailPublicFolder

   Remove-PublicFolder

   Remove-Mailbox

Step 3: Generate the .csv files
 1. On the Exchange 2010 server, run the Export-PublicFolderStatistics.ps1 script to create
   the folder name-to-folder size mapping file. This script needs to be run by a local
   administrator. The file will contain two columns: FolderName and FolderSize. The values for
   the FolderSize column will be displayed in bytes. For example, \PublicFolder01,10000.

     PowerShell

     .\Export-PublicFolderStatistics.ps1 <Folder to size map path> <FQDN of source
     server>

        FQDN of source server equals the fully qualified domain name of the Mailbox server
        where the public folder hierarchy is hosted.

        Folder to size map path equals the file name and path on a local or network shared
        folder where you want the .csv file saved. Later in this topic, you'll need to access this
        file from the Exchange 2016 server. If you specify only the file name, the file will be
        generated in the current PowerShell directory on the local computer.

   Example 1

   The following example exports the public folder statistics to a file named PFStats.csv in the
   same folder from which the script is executed:

     PowerShell

     .\Export-PublicFolderStatistics.ps1 -ExportFile PFStats.csv -PublicFolderServer
     bat2exch1

   Example 2

   The following example exports the public folder statistics to a file named PFStats.csv in the
   network shared folder named Data on server Exch2:

<!-- p.1998 -->

       PowerShell

       .\Export-PublicFolderStatistics.ps1 -ExportFile \\Exch2\data\PFStats.csv -
       PublicFolderServer exch1

   2. Run the PublicFolderToMailboxMapGenerator.ps1 script to create the public folder-to-
     mailbox mapping file. This file is used to calculate the correct number of public folder
     mailboxes on the Exchange 2016 server.

       ７ Note

       If the name of a public folder contains a backslash ****, the public folders will be
       created in the parent public folder. We recommend that you review the .csv file and
       edit any names that contain a backslash.

       PowerShell

       .\PublicFolderToMailboxMapGenerator.ps1 <Maximum mailbox size in bytes> <Folder
       to size map path> <Folder to mailbox map path>

          Maximum mailbox size in bytes equals the maximum size you want to set for the new
          public folder mailboxes. When specifying this setting, be sure to allow for expansion so
          the public folder mailbox has room to grow.

          Folder to size map path equals the full file path of the .csv file you created when
          running the Export-PublicFolderStatistics.ps1 script.

          Folder to mailbox map path equals the file name and path of the folder-to-mailbox .csv
          file that you'll create with this step. If you specify only the file name, the file will be
          generated in the current PowerShell directory on the local computer.

Step 4: Create the public folder mailboxes in
Exchange 2016
Run the following command to create the target public folder mailboxes. The script will create a
target mailbox for each mailbox in the .csv file that you generated previously in Step 3 by running
the PublicFoldertoMailboxMapGenerator.ps1 script.

 PowerShell

<!-- p.1999 -->

 .\Create-PublicFolderMailboxesForMigration.ps1 -FolderMappingCsv Mapping.csv -
 EstimatedNumberOfConcurrentUsers:<estimate>

Mapping.csv is the file generated by the PublicFoldertoMailboxMapGenerator.ps1 script in Step 3.
The estimated number of simultaneous user connections browsing a public folder hierarchy is
usually less than the total number of users in an organization.

Step 5: Start the migration request
After you create the batch migration request in the Exchange Management Shell, you can view
the requests and manage them in the Exchange admin center (EAC).

   1. On the Exchange 2016 server, run the following command:

       PowerShell

       New-MigrationBatch -Name PFMigration -SourcePublicFolderDatabase (Get-
       PublicFolderDatabase -Server <Source server name>) -CSVData
       ([System.IO.File]::ReadAllBytes('<Folder to mailbox map path>')) -
       NotificationEmails <email addresses for migration notifications>

     The NotificationEmails parameter is optional.

   2. Start the migration in the EAC or in the Exchange Management Shell.

           In the Exchange Management Shell, run the following command:

            PowerShell

            Start-MigrationBatch PFMigration

           In the EAC:

           a. Log into Exchange Online and open the EAC.

           b. Go to Recipients > Migration.

           c. Select the migration batch you just created, and then click the start button.

           In the EAC, the Status column will show the initial batch status as Created. The status
           changes to Syncing during migration. When the migration request is complete, the
           status will be Synced. You can double-click a batch to view the status of individual
           mailboxes within the batch. Mailbox jobs begin with a status of Queued. When the job

<!-- p.2000 -->

           begins the status is Syncing, and once InitialSync is complete, the status will show
           Synced.

You can view and manage the progress and completion of the migration in the Recipients >
Migration tab in the EAC.

Because the New-MigrationBatch cmdlet initiates a mailbox migration request for each public
folder mailbox, you can view the status of these requests using the mailbox migration page in the
EAC, and you can create migration reports that can be emailed to you.

   1. Log into Exchange Online and open the EAC.

   2. Go to Recipients > Migration.

   3. Select the migration request that you just created and then click View Details in the Details
     pane.

For detailed syntax and parameter information, see the following topics:

     New-MigrationBatch

     Get-PublicFolderDatabase

     Get-PublicFolderMailboxMigrationRequest

     Get-PublicFolderMailboxMigrationRequestStatistics

Step 6: Lock down the public folders on the Exchange
2010 server for final migration (downtime required)
Until this point in the migration, users have been able to access public folders. The next steps will
log users off from the Exchange 2010 public folders and lock the folders while the migration
completes its final synchronization. Users won't be able to access public folders during this
process. Also, any mail sent to mail-enabled public folders will be queued and won't be delivered
until the public folder migration is complete.

Before you run the PublicFoldersLockedForMigration command as described below, make sure
that all jobs are in the Synced state. You can do this by running the Get-
PublicFolderMailboxMigrationRequest command. Continue with this step only after you've verified

that all jobs are in the Synced state.
