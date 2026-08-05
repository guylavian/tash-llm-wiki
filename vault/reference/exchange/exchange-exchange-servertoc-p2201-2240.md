---
title: "Exchange Server — pages 2201-2240"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2201-2240
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2201-2240
family: exchange
documentKind: "doc"
abstract: "Manage In-Place Archives in Exchange Server Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition In-Place Archiving helps you regain control of your organization's messaging data by eliminating the need for personal store (.pst) files and allowing you to meet your org"
---

# Exchange Server — pages 2201-2240

<!-- p.2201 -->

Manage In-Place Archives in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

In-Place Archiving helps you regain control of your organization's messaging data by
eliminating the need for personal store (.pst) files and allowing you to meet your organization's
message retention and eDiscovery requirements. With archiving enabled, users can store
messages in an archive mailbox, which is accessible by using Microsoft Outlook and Outlook
on the web.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place Archive" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      The procedures in this topic apply to on-premises archive mailboxes. For information
      about archive mailboxes in Exchange Online, see Enable archive mailboxes in the
      compliance portal.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      It's not supported to have a user's primary mailbox reside on a version of Exchange that's
      older than the user's archive. If the user's primary mailbox is still on Exchange 2010 or
      Exchange 2013, you need to move it to Exchange 2016 or Exchange 2019 at the same
      time you move the archive mailbox to Exchange 2016 or Exchange 2019.

Enable an archive mailbox
You can use the Exchange admin center or the Exchange Management Shell to enable archive
mailboxes for users that already have a primary mailbox.

Use the EAC to enable an archive mailbox
   1. Go to Recipients > Mailboxes.

   2. Select a mailbox.

<!-- p.2202 -->

   3. In the details pane, under In-Place Archive, click Enable.

     Note: You can also bulk-enable archives by selecting multiple mailboxes (use the Shift or
     Ctrl keys). After selecting multiple mailboxes, in the details pane, click More options.
     Then, under Archive click Enable.

   4. On the Create In-Place Archive page, click OK to have Exchange automatically select a
     mailbox database for the archive or click Browse to specify one.

Use the Exchange Management Shell to enable an archive
mailbox
This example enables the archive mailbox for Tony Smith.

  PowerShell

  Enable-Mailbox "Tony Smith" -Archive

This example retrieves mailboxes in database DB01 that don't have an on-premises or cloud-
based archive enabled and don't have a name starting with DiscoverySearchMailbox. It pipes
the results to the Enable-Mailbox cmdlet to enable the archive for all mailboxes on mailbox
database DB01.

  PowerShell

  Get-Mailbox -Database DB01 -Filter "ArchiveGuid -Eq `$null -AND ArchiveDomain -eq
  `$null -AND Name -NotLike 'DiscoverySearchMailbox*'" | Enable-Mailbox -Archive

How do you know that you've enabled an archive mailbox?
To verify that you've successfully enabled an on-premises archive for an existing mailbox, do
one of the following:

     In the EAC, go to Recipients > Mailboxes, and then select the mailbox from the list. In the
     details pane, under In-Place Archive, confirm that it is set to Enabled. Click View details
     to view archive properties, including archive status and the mailbox database in which it is
     created.

     In the Exchange Management Shell, run the following command to display information
     about the new archive.

        PowerShell

<!-- p.2203 -->

        Get-Mailbox <MailboxIdentity> | Format-List Name,*Archive*

     In the Exchange Management Shell, use the Test-ArchiveConnectivity cmdlet to test
     connectivity to the archive. For an example of how to test archive connectivity, see the
     Examples section in the topic, Test-ArchiveConnectivity.

Enable an archive mailbox when you create a new
mailbox
You can also enable an archive mailbox when you first create a new mailbox for a user.

Use the EAC to enable an archive mailbox when you create a
new mailbox
   1. Go to Recipients > Mailboxes.

   2. Click New > User mailbox.

   3. On the New user mailbox page, in the Alias box, type an alias for the user.

     Note: If you leave this box blank, the value you type in the User logon name box is used
     for the alias.

   4. Select one of the following options:

           Existing user that isn't mail-enabled: Click this button and then click Browse to
           open the Select User - Entire Forest dialog box. This dialog box displays a list of
           Active Directory user accounts in the forest that aren't mail-enabled or don't have
           Exchange mailboxes. Select the user account you want to mail-enable, and then click
           OK. If you select this option, you don't have to provide user account information
           because this information already exists in Active Directory.

           New user: Click this button to create a new user account in Active Directory and
           create a mailbox for the user. If you select this option, you'll have to provide the
           required user account information.

   5. Click More options to configure the following settings.

           Mailbox database: Click Browse to select a mailbox database in which to store the
           mailbox. If you don't select a database, Exchange will automatically assign one.

<!-- p.2204 -->

           Archive: Select this check box to create an archive mailbox for the mailbox. If you
           create an archive mailbox, mailbox items will be moved automatically from the
           primary mailbox to the archive, based on the default retention policy settings or
           those you define.

     Click Browse to select a database to store the archive mailbox.

   6. When you're finished, click Save to create the mailbox and its archive.

Use the Exchange Management Shell to enable an archive
mailbox when you create a new mailbox
This example creates the user named Chris Ashton in Active Directory, creates the mailbox on
mailbox database DB01, and enables and creates an archive mailbox on DB01. To set the initial
value of the password, this example creates a variable ($password), prompts you to enter a
password, and assigns that password to the variable as a SecureString object.

  PowerShell

  $password = Read-Host "Enter password" -AsSecureString

  PowerShell

  New-Mailbox -UserPrincipalName cashton@contoso.com -Alias cashton -Database "DB01"
  -Archive -Name "Chris Ashton" -OrganizationalUnit Users -Password $password -
  FirstName Chris -LastName Ashton

How do you know that you've enabled an archive mailbox
when you created a new mailbox?
To verify that you've successfully created a user mailbox with an on-premises archive, do one of
the following:

     In the EAC, go to Recipients > Mailboxes, and then select the new user mailbox from the
     list. In the details pane, under In-Place Archive, confirm that it is set to Enabled. Click
     View details to view archive properties, including archive status and the mailbox database
     in which it is created.

     In the Exchange Management Shell, run the following command to display information
     about the new user mailbox and archive.

        PowerShell

<!-- p.2205 -->

          Get-Mailbox <Name> | Format-List
          Name,RecipientTypeDetails,PrimarySmtpAddress,*Archive*

        In the Exchange Management Shell, use the Test-ArchiveConnectivity cmdlet to test
        connectivity to the archive. For an example of how to test archive connectivity, see the
        Examples section in Test-ArchiveConnectivity.

Disable an archive mailbox
You may want to disable a user's archive for troubleshooting purposes or compliance-related
reasons. If you disable an archive mailbox, all information in the archive will be kept in the
mailbox database until the mailbox retention time expires and the archive is permanently
deleted. By default, Exchange keeps deleted mailboxes, including archive mailboxes, for 30
days.

Use the EAC to disable an archive mailbox
   1. Go to Recipients > Mailboxes.

   2. Select a mailbox.

   3. In the details pane, under In-Place Archive, click Disable.

        Note: You can also bulk-disable archives by selecting multiple mailboxes (use the Shift or
        Ctrl keys). After selecting multiple mailboxes, in the details pane, click More options.
        Then, under Archive click Disable.

Use the Exchange Management Shell to disable an archive
mailbox
This example disables the archive mailbox for Chris Ashton's mailbox. It doesn't disable the
user's primary mailbox.

  PowerShell

  Disable-Mailbox "Chris Ashton" -Archive

How do you know this worked?
To verify that you have successfully disabled an archive mailbox, do the following:

<!-- p.2206 -->

     In the EAC, select the mailbox. In the details pane, check its archive status under In-Place
     Archive.

     In the Exchange Management Shell, run the following command to check the archive
     properties for the mailbox user.

        PowerShell

        Get-Mailbox "Chris Ashton" | Format-List *Archive*

If the archive is disabled, the following values are returned for archive-related properties.

                                                                                    ﾉ   Expand table

 Property                                                         Value

 ArchiveDatabase (for on-premises archives)                       <blank>

 ArchiveState                                                     None

 DisabledArchiveDatabase (for on-premises archives)               <name of mailbox database>

 DisabledArchiveGuid                                              <GUID of disabled archive>

Re-enable an archive mailbox
When you disable an archive mailbox, it becomes disconnected. A disconnected archive
mailbox is retained in the mailbox database for a specified amount of time. By default,
Exchange retains disconnected archive mailboxes for 30 days. Within 30 days of disabling an
archive mailbox, you can reconnect it to the user's primary mailbox by re-enabling the archive.
In this case, the original contents of the archive mailbox are restored. However after 30 days of
disabling a mailbox, the contents of the original archive mailbox are permanently deleted
(purged from the mailbox database) and can't be recovered. So if you re-enable the archive
more than 30 days after disabling it, a new archive mailbox is created when you re-enable it.

Use the EAC to re-enable an archive mailbox
   1. Go to Recipients > Mailboxes.

   2. Select the mailbox.

   3. In the details pane, under In-Place Archive, click Enable

   4. On the Create in-place archive page, click OK.

<!-- p.2207 -->

     You can have Exchange automatically select a mailbox database for the re-enabled
     archive mailbox or you can click Browse to specify one.

Use the Exchange Management Shell to re-enable an archive
mailbox
Use the Enable-Mailbox -Archive command to re-enable an archive mailbox. For example:

  PowerShell

  Enable-Mailbox "Chris Ashton" -Archive

How do you know this worked?
To verify that you have successfully connected a disabled archive mailbox to the user's primary
mailbox, run the following command to retrieve the mailbox user's archive properties, and
verify the values returned for the ArchiveGuid and ArchiveDatabase properties.

  PowerShell

  Get-Mailbox "Chris Ashton" | Format-List *Archive*

As previously stated, if you re-enable an archive mailbox within 30 days of disabling it, the user
will be able to access the original contents of their archive mailbox. If you re-enable the archive
more than 30 days after disabling it, the new archive mailbox will be empty the first time the
user accesses it.

<!-- p.2208 -->

In-Place Hold and Litigation Hold in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

When a reasonable expectation of litigation exists, organizations are required to preserve
electronically stored information (ESI), including email that's relevant to the case. This
expectation often exists before the specifics of the case are known, and preservation is often
broad. Organizations may need to preserve all email related to a specific topic or all email for
certain individuals. Depending on the organization's electronic discovery (eDiscovery) practices,
the following measures can be adopted to preserve email:

      End users may be asked to preserve email by not deleting any messages. However, users
      can still delete email knowingly or inadvertently.

      Automated deletion mechanisms such as messaging records management (MRM) may be
      suspended. This could result in large volumes of email cluttering the user mailbox, and
      thus impacting user productivity. Suspending automated deletion also doesn't prevent
      users from manually deleting email.

      Some organizations copy or move email to an archive to make sure it isn't deleted,
      altered, or tampered with. This increases costs due to the manual efforts required to copy
      or move messages to an archive, or third-party products used to collect and store email
      outside Exchange.

Failure to preserve email can expose an organization to legal and financial risks such as scrutiny
of the organization's records retention and discovery processes, adverse legal judgments,
sanctions, or fines.

Litigation Hold and In-Place Hold
There are two types of holds available in Exchange Server: Litigation Hold and In-Place Hold.
Litigation Hold uses the LitigationHoldEnabled property of a mailbox. When Litigation Hold is
enabled, all mailbox all items are placed on hold. In contrast, you can use an In-Place Hold to
preserve only those items that meet that the criteria of a search query that you define by using
the In-Place eDiscovery tool. You can place multiple In-Place Holds on a mailbox, but Litigation
Hold is either enabled or disabled for a mailbox. For both types of holds, you can also specify
the duration period to hold items. The duration is calculated from the date a mailbox item is
received or created. If a duration isn't set, items are held indefinitely or until the hold is
removed. If you remove a Litigation Hold from a mailbox, but one or more In-Place Holds are

<!-- p.2209 -->

still placed on the mailbox, items matching the In-Place Hold criteria are held for the period
specified in the hold settings.

You can use In-Place Hold to place a user on multiple holds. When a user is placed on multiple
holds, the search queries from any query-based hold are combined (with OR operators). In this
case, the maximum number of keywords in all query-based holds placed on a mailbox is 500. If
there are more than 500 keywords, then all content in the mailbox is placed on hold (not just
that content that matches the search criteria). All content is held until the total number of
keywords is reduced to 500 or less.

When you move a mailbox that's on Litigation Hold in Exchange 2010 or Exchange 2013 to a
Mailbox server in Exchange 2016, the Litigation Hold setting continues to apply, ensuring that
compliance requirements are met during and after the move.

  ） Important

  When you put a mailbox on Litigation Hold or In-Place Hold, the hold is placed on both
  the primary and the archive mailbox.

For more information when to use each type of hold, see Place all mailboxes on hold.

Hold goals and features
You can use Litigation Hold and In-Place Hold to accomplish the following goals:

     Place user mailboxes on hold and preserve mailbox items immutably.

     Preserve items indefinitely or for a specific duration.

     Preserve mailbox items deleted by users or automatic processes such as MRM.

     Preserve messages that are forwarded to another mailbox.

     Use query-based In-Place Hold to search for and retain items matching specified criteria
     (you can also place all items hold by including all mailbox content when you create the
     hold)

     Place a user on multiple holds for different cases or investigations.

     Keep holds transparent from the user by not having to suspend MRM.

     Use In-Place eDiscovery to search for items that are preserved by being placed on hold

<!-- p.2210 -->

If you're upgrading from Exchange Server 2010, the notion of legal hold is to hold all mailbox
data for a user indefinitely or until when hold is removed. In Exchange 2016, In-Place Hold
introduced a different model that allows you to specify the following parameters:

     Query-based hold: With Litigation Hold, all items in a mailbox are preserved. However, an
     In-Place Hold allows you to specify which items to hold by using search query parameters
     such as keywords, senders and recipients, start and end dates, and also specify the
     message types such as email messages, calendar items, and Skype for Business
     conversations that you want to place on hold. After you create a query-based In-Place
     Hold, all existing and future mailbox items (including messages received at a later date)
     that match the query parameters are preserved. Litigation Hold doesn't support query-
     based holds.

     Hold duration: In both Litigation Hold and In-Place Hold, you can specify how long to
     hold items. You can either specify an infinite hold duration or a time-based hold duration.
     The duration is calculated from the date a mailbox item is received or created. For
     example, if your organization requires that all mailbox items be preserved for 7 years, you
     can create a time-based hold. So if a mailbox is placed on hold and the hold duration is
     set to 7 years, and an item in the mailbox is permanently deleted after 2 years from the
     date it was received, it's held for an 5 years before being purged from the mailbox
     database.

        Tip

       You can use a time-based hold together with a retention policy to make sure items
       are preserved for a specified duration and then permanently removed from
       Exchange after the retention age and the hold duration expire.

Placing a mailbox on hold
The Legal Hold management role is required to place a mailbox on Litigation Hold or In-Place
Hold. But to create a query-based In-Place Hold, you must also be assigned the Mailbox Search
role. Users that have been added to the Discovery Management role-based access control
(RBAC) role group (or assigned the Legal Hold and Mailbox Search roles) can place users hold
and create a query-based In-Place Hold. To learn how to add members to the Discovery
Management role group, see Assign eDiscovery permissions in Exchange Server.

You can place a mailbox Litigation Hold on the Recipients page in the Exchange admin center
or by using the Set-Mailbox -LitigationHoldEnabled $true command in the Exchange
Management Shell.

<!-- p.2211 -->

The In-Place Hold functionality is integrated with In-Place eDiscovery searches. You can place a
mailbox on In-Place Hold by using the In-Place eDiscovery & Hold wizard in the EAC or the
New-MailboxSearch cmdlet in the Exchange Management Shell. To learn how, see:

     Place a mailbox on Litigation Hold

     Create or remove an In-Place Hold

  ７ Note

  If you use Exchange Online Archiving to provision a cloud-based archive for your on-
  premises mailboxes, you must manage In-Place Holds from your on-premises Exchange
  Server organization. Hold settings are automatically propagated to the cloud-based
  archive using DirSync.

Many organizations require that users be informed when they're placed on hold. Additionally,
when a mailbox is on hold, any retention policies applicable to the mailbox user don't need to
be suspended. Because messages continue to be deleted as expected, users may not notice
they're on hold. If your organization requires that users on hold be informed, you can add a
notification message to the mailbox user's by populating the Retention Comment property
and using the RetentionUrl property to link to a web page for more information. Outlook 2010
and later versions display the retention comment and URL in the backstage area, which is
located on the Files ribbon. You can use the Set-Mailbox cmdlet to add these properties.

Holds and the Recoverable Items folder
Litigation Hold and In-Place Hold use the Recoverable Items folder to preserve items. The
Recoverable Items folder is hidden from the default view of Outlook, Outlook on the web, and
other email clients. To learn more about the Recoverable Items folder, see Recoverable Items
folder in Exchange Server.

By default, when a user deletes a message from a folder other than the Deleted Items folder,
the message is moved to the Deleted Items folder. When a user soft deletes an item (by
pressing SHIFT+DELETE) or deletes an item from the Deleted Items folder, the message is
moved to the Recoverable Items folder, thereby disappearing from the user's view.

Items in the Recoverable Items folder are retained for the deleted item retention period
configured on the user's mailbox database. By default, the deleted item retention period is set
to 14 days for mailbox databases.

The Recoverable Items folder contains the following subfolders used to store deleted items in
various sites and facilitate Litigation Hold and In-Place Hold:

<!-- p.2212 -->

     Deletions: Items removed from the Deleted Items folder or soft-deleted from other
     folders are moved to the Deletions subfolder and are visible to the user when using the
     Recover Deleted Items feature in Outlook and Outlook on the web. By default, items
     reside in this folder until the deleted item retention period configured for the mailbox
     database or the mailbox expires.

     Purges: When a user deletes an item from the Recoverable Items folder (by using the
     Recover Deleted Items tool in Outlook and Outlook on the web, the item is moved to the
     Purges folder. Items that exceed the deleted item retention period configured on the
     mailbox database or the mailbox are also moved to the Purges folder. Items in this folder
     aren't visible to users if they use the Recover Deleted Items tool. When the mailbox
     assistant processes the mailbox, items in the Purges folder are purged from the mailbox
     database. When you place the mailbox user on Litigation Hold, the mailbox assistant
     doesn't purge items in this folder.

     DiscoveryHolds: If a user is put on an In-Place Hold, deleted items are moved to this
     folder. When the mailbox assistant processes the mailbox, it evaluates messages in this
     folder. Items that match the In-Place Hold query are retained until the hold period
     specified in the query. If no hold period is specified, items are held indefinitely or until the
     user is removed from the hold. However, if you put a user who was already on an In-Place
     Hold on Litigation Hold, the Litigation Hold takes preference. Therefore, deleted items are
     moved to the Purges folder instead.

     Versions: When a user is put on In-Place Hold or Litigation Hold, mailbox items must be
     protected from tampering or modification by the user or a process. This is done by using
     a copy-on-write process. When a user or a process changes specific properties of a
     mailbox item, a copy of the original item is saved in the Versions folder before the change
     is committed. This process is repeated for subsequent changes. Items captured in the
     Versions folder are also indexed and returned in In-Place eDiscovery searches. After the
     hold is removed, copies in the Versions folder are removed by the Managed Folder
     Assistant.

Properties that trigger copy-on-write

                                                                                   ﾉ   Expand table

 Item type                            Properties that trigger copy-on-write

 Messages (IPM.Note*)                 Subject
 Posts (IPM.Post*)                    Body
                                      Attachments
                                      Senders/Recipients
                                      Sent/Received Dates

<!-- p.2213 -->

 Item type                             Properties that trigger copy-on-write

 Items other than messages and posts   Any change to a visible property, except the following:
                                             Item location (when an item is moved between folders)
                                             Item status change (read or unread)
                                             Changes to retention tag applied to an item

 Items in the default folder Drafts    None (items in the Drafts folder are exempt from copy on write)

  ） Important

  Copy-on-write is disabled for calendar items in the organizer's mailbox when meeting
  responses are received from attendees and the tracking information for the meeting is
  updated. For calendar items and items that have a reminder set, copy-on-write is disabled
  for the ReminderTime and ReminderSignalTime properties. Changes to these properties
  are not captured by copy-on-write. Changes to RSS feeds aren't captured by copy-on-
  write.

Although the DiscoveryHolds, Purges, and Versions folders aren't visible to the user, all items in
the Recoverable Items folder are discoverable by using In-Place eDiscovery. After a mailbox
user is removed from In-Place Hold or Litigation Hold, items in the DiscoveryHolds, Purges, and
Versions folders are purged by the Managed Folder Assistant.

If a mailbox isn't placed on Litigation Hold or In-Place Hold, items in the Purges folder are
permanently deleted from the Recoverable Items folder on a first in, first out basis when the
item has resided in the folder for longer than the deleted item retention period.

Holds and mailbox quotas
Items in the Recoverable Items folder aren't calculated toward the user's mailbox quota. In
Exchange, the Recoverable Items folder has its own quota. For Exchange, the default values for
the RecoverableItemsWarningQuota and RecoverableItemsQuota mailbox properties are set to
20 GB and 30 GB respectively. To modify these values for a mailbox database for Exchange
Server, use the Set-MailboxDatabase cmdlet. To modify them for individual mailboxes, use the
Set-Mailbox cmdlet.

When a user's Recoverable Items folder exceeds the warning quota for recoverable items (as
specified by the RecoverableItemsWarningQuota parameter), an event is logged in the
Application event log of the Mailbox server. When the folder exceeds the quota for recoverable
items (as specified by the RecoverableItemsQuota parameter), users won't be able to empty the
Deleted Items folder or permanently delete mailbox items. Also copy-on-write won't be able to

<!-- p.2214 -->

create copies of modified items. Therefore, it's critical that you monitor Recoverable Items
quotas for mailbox users placed on In-Place Hold.

Holds and email forwarding
Users with mailboxes on Exchange Server can use Outlook and Outlook on the web to set up
email forwarding for their mailbox. Email forwarding lets users configure their mailbox to
forward email messages sent to their mailbox to another mailbox located inside or outside of
their organization. Administrators can also set up mail flow rules (also known as transport
rules) to forward messages to another mailbox. In both cases, email forwarding can be
configured so that any message sent to the original mailbox isn't copied to that mailbox and is
only sent to the forwarding address.

If a mailbox is on hold, additional steps are taken. During the delivery process, the hold
settings for the mailbox are checked. If the message meets the hold criteria for the mailbox, a
copy of the message is saved to the Inbox folder. That means you can use In-Place eDiscovery
to search the original mailbox to find messages that were forwarded to another mailbox.

Preserving archived Skype for Business content
Exchange 2016 and Exchange 2019, Skype for Business, and SharePoint 2016 provide an
integrated preservation and eDiscovery experience that allows you to preserve and search for
items across the different data stores. Exchange 2016 and 2019 allow you to archive Skype for
Business content in Exchange, removing the requirement of having a separate SQL Server
database to store archived Lync content. The integrated hold and eDiscovery capability in
SharePoint 2016 allows you to preserve and search data across all stores from a single console.

When you place an Exchange Server mailbox on In-Place Hold or Litigation Hold, Skype for
Business content (such as instant messaging conversations and files shared in an online
meeting) are archived in the mailbox. If you search the mailbox using In-Place eDiscovery, any
archived Skype for Business content matching the search query is also returned in search
results. You can also restrict the search to Skype for Business content archived in the mailbox.

To enable archiving of Skype for Business content in Exchange Server mailboxes, you must
configure Skype for Business Server 2015 integration with Exchange Server. For details, see the
following topics:

     Planning for Archiving

     Deploying Archiving

<!-- p.2215 -->

Deleting a mailbox on hold
If you delete a user account that has a mailbox, the Exchange Information store will eventually
detect that the mailbox is no longer connected to a user account and mark that mailbox for
deletion, even if the mailbox is on hold. If you want to preserve the mailbox, you have to do
the following:

   1. Instead of deleting the user account, disable the user account.

   2. Change the properties of the mailbox to restrict the use and access to the mailbox. For
     example, set send and receive quotas equal to 1, block who can send messages to the
     mailbox, and restrict who can access the mailbox.

   3. Retain the mailbox until all data has been removed or until preserving the data is no
     longer required.

Migrating mailboxes on hold from Exchange
Server to Microsoft 365 or Office 365
If you have an Exchange hybrid deployment, the following conditions are true when you move
(onboard) an on-premises Exchange Server mailbox to Exchange Online in Microsoft 365 or
Office 365:

     If the on-premises mailbox is on Litigation Hold or In-Place Hold, the hold settings are
     preserved after the mailbox is moved to Exchange Online.

     If the on-premises mailbox is on Litigation Hold or In-Place Hold, any content in the
     Recoverable Items folder is moved to the Exchange Online mailbox.

Hold settings and content in the Recoverable Items folder are also preserved when you move
(offboard) an Exchange Online mailbox to your on-premises Exchange Server organization.

   Tip

  For Exchange Server, an Exchange hybrid deployment is the recommended way to migrate
  on-premises mailboxes to Microsoft 365 or Office 365.

<!-- p.2216 -->

Create or remove an In-Place Hold
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

An In-Place Hold preserves all mailbox and public folder content, including deleted items and
original versions of modified items. All such items can be returned in an In-Place eDiscovery
search. When you place an In-Place Hold on a user's mailbox, the contents in the
corresponding archive mailbox (if it's enabled) are also placed on hold and returned in a
eDiscovery search.

When you create an In-Place Hold, you can place all items in the source mailbox or public
folder on hold or you can hold only the items that meet the search criteria specified for the
hold. Similarly, you can hold items indefinitely or for a specific amount of time. For more
information about In-Place Holds, see In-Place Hold and Litigation Hold in Exchange Server.

You can create In-Place holds in the Exchange admin center (EAC) or in the Exchange
Management Shell.

Before you begin
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place Hold" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      Depending on your Active Directory topology and replication latency, it may take up to
      an hour for an In-Place Hold to take effect.

      As previously explained, when you place an In-Place Hold on a user's mailbox, the content
      in the user's archive mailbox is also placed on hold.

      You can only search or place holds on all public folders in your organization. You can't
      specify individual public folders.

      See the More information section for a description of the In-Place Hold workflow process.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

Create an In-Place Hold

Use the EAC to create an In-Place Hold

<!-- p.2217 -->

1. Go to Compliance management > In-Place eDiscovery & Hold, and then click New            .

2. In the New In-Place eDiscovery & Hold window, on the Name and description page,
  type a name for the hold and an optional description, and then click Next.

3. On the Mailboxes and Public folders page, select the content sources to search:

       To exclude mailboxes from the hold (and place a hold on public folders only), click
       Don't search any mailboxes.

       To include specific mailboxes in the search, click Specify mailboxes to search, and
       then add the mailboxes that you want to search.

       To place public folders on hold, click Search all public folders.

    ） Important

    You can't select the Search all mailboxes option when creating an In-Place Hold. To
    create an In-Place Hold, you must select the specific mailboxes you want to place on
    hold.

4. On the Search query page, complete the following fields, and then click Next.

<!-- p.2218 -->

          Include all content: Select this option to place all content in selected sources on
          hold.

          Filter based on criteria: Select this option to specify search criteria, including
          keywords, start and end dates, sender and recipient addresses, and message types.

       ） Important

       If a user is placed on multiple In-Place Holds, the search queries from any query-
       based hold are combined (with OR operators). In this case, the maximum number of
       keywords in all query-based holds placed on a mailbox is 500. If there are more than
       500 keywords, then all content in the mailbox is placed on hold (not just that content
       that matches the search criteria). All content is held until the total number of
       keywords is reduced to 500 or less.

  5. On the In-Place Hold settings page, click the Place content matching the search query
     in selected sources on hold check box and then select one of the following options:

          Hold indefinitely: Place items returned by the search on an indefinite hold. Items on
          hold will be preserved until you change the hold duration, remove the mailbox (or
          public folders) from the search, or remove the search.

          Specify number of days to hold items relative to their received date: Hold items
          for a specific period. For example, you can use this option if your organization
          requires that all messages be retained for at least seven years. You can use a time-
          based In-Place Hold along with a retention policy to make sure items are
          permanently deleted in seven years.

  6. Click Finish to create the In-Place Hold.

Use the Exchange Management Shell to create an In-Place
Hold
This example creates an In-Place Hold named Hold-CaseId012 and adds the mailbox
joe@contoso.com to the hold.

  ） Important

  If you don't specify additional search parameters for an In-Place Hold, all items in the
  specified source mailboxes are placed on hold. If you don't specify the ItemHoldPeriod

<!-- p.2219 -->

  parameter, items are placed on hold indefinitely or until the mailbox is either removed
  from hold or the hold is deleted.

  PowerShell

  New-MailboxSearch "Hold-CaseId012" -SourceMailboxes "joe@contoso.com" -
  InPlaceHoldEnabled $true

This example places an In-Place Hold on all public folders in the organization, and holds
content for 7 years. The hold doesn't include any mailboxes.

  PowerShell

  New-MailboxSearch -Name "Hold for Public Folders" -AllPublicFolderSources $true -
  AllSourceMailboxes $false -ItemHoldPeriod 2555 -InPlaceHoldEnabled $true

For detailed syntax and parameter information, see New-MailboxSearch.

How do you know this worked?
To verify that you have successfully created the In-Place Hold, do one of the following:

     Use the EAC to verify that the In-Place Hold is listed in the list view of the In-Place
     eDiscovery & Hold page.

     Use the Get-MailboxSearch cmdlet to retrieve the mailbox search and check the hold
     properties. For example, the following command displays the hold properties for the
     search named Hold-CaseId012:

        PowerShell

        Get-MailboxSearch "Hold-CaseId012" | Format-List
        InPlaceHoldEnabled,ItemHoldPeriod,InPlaceHoldIdentity

     Use the Get-Mailbox cmdlet to display In-Place Hold information for specific user
     mailboxes or public folder mailboxes. For example, the following command displays the
     GUID for the In-Place Hold:

        PowerShell

        Get-Mailbox "joe@contoso.com" | Format-List InPlaceHolds

<!-- p.2220 -->

     This example will display the In-Place Hold GUID for all public folder mailboxes in the
     organization.

        PowerShell

        Get-Mailbox -PublicFolder | Format-List Name,InPlaceHolds

Remove an In-Place Hold
In Exchange Server, eDiscovery searches are used to hold and search for content in on content
sources. You can't remove an In-Place eDiscovery search that's used to place content sources
on hold. You must first remove the In-Place Hold by clearing the Place content matching the
search query in selected sources on hold check box on the In-Place Hold page or by setting
the InPlaceHoldEnabled parameter to $false in the Exchange Management Shell. Alternatively,
you can remove mailboxes and public folders from an In-Place Hold by changing the value of
the SourceMailboxes or AllPublicFolderSources parameters specified in the search.

Use the EAC to remove an In-Place Hold
   1. Go to Compliance management > In-Place eDiscovery & Hold.

   2. In the list view, select the In-Place Hold you want to remove, and then click Edit   .

   3. In In-Place eDiscovery & Hold properties, on the In-Place Hold page, clear the Place
     content matching the search query in selected sources on hold check box, and then
     click Save.

   4. Select the In-Place Hold again from the list view and then click Delete   .

   5. In warning, click Yes to remove the search.

Use the Exchange Management Shell to remove an In-Place
Hold
This example first disables In-Place Hold named Hold-CaseId012 and then removes the
mailbox search.

  PowerShell

  Set-MailboxSearch "Hold-CaseId012" -InPlaceHoldEnabled $false; Remove-
  MailboxSearch "Hold-CaseId012"

<!-- p.2221 -->

For detailed syntax and parameter information, see Set-Mailboxsearch.

How do you know this worked?
To verify that you have successfully removed an In-Place Hold, do one of the following:

     Use the EAC to verify that the In-Place Hold doesn't appear in the list view of the In-Place
     eDiscovery & Hold tab.

     Use the Get-MailboxSearch cmdlet to retrieve all mailbox searches and check that the
     search you removed is no longer listed.

More information
How does In-Place Hold work?: If a mailbox or public folder is not on hold, an item is moved
to the Deletions subfolder in the Recoverable Items folder when it's permanently deleted (Shift
+ Delete) or deleted from the Deleted Items folder. A deletion policy (how long items are set to
be retained) also moves items to the Deletions subfolder when the retention period expires.
When a user purges an item in the Recoverable Items folder or when the deleted item
retention period expires for an item, the item is moved to the Purges subfolder and marked for
permanent deletion. It will be then be purged from Exchange the next time the mailbox is
processed by the Managed Folder Assistant (MFA).

When an In-Place Hold is placed on a mailbox or public folder, purged items are not moved to
the Purges subfolder but are instead moved to the DiscoveryHolds subfolder and are preserved
for the hold duration specified by the In-Place Hold. The hold duration is calculated from the
original date an item was received or created, and defines how long items in the
DiscoveryHolds subfolder are held. When the hold duration expires for an item in the
DiscoveryHolds subfolder, the item it is marked for permanent deletion and will be purged
from Exchange the next time the mailbox or public folder is processed by the MFA. If an
indefinite hold is placed on a mailbox or public folder, items will never be purged from the
DiscoveryHolds subfolder.

The following illustration shows the subfolders in the Recoverable Items folders and the hold
workflow process.

<!-- p.2222 -->

７ Note

If a mailbox is place on Litigation Hold, purged items are moved to the Purges subfolder
and preserved for the hold duration configured for the Litigation Hold.

<!-- p.2223 -->

Place a mailbox on Litigation Hold
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Place a mailbox on Litigation Hold to preserve all mailbox content, including deleted items and
original versions of modified items. When you place a mailbox on Litigation Hold, the user's
archive mailbox (if it's enabled) is also placed on hold. Deleted and modified items are
preserved for a specified period or until you remove the mailbox from Litigation Hold. All such
mailbox items are returned in an In-Place eDiscovery in Exchange Server search.

Before you begin
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "In-Place Hold" entry in the
      Messaging policy and compliance permissions in Exchange Server topic.

      The Litigation Hold setting may take up to 60 minutes to take effect.

      Litigation Hold preserves items in the Recoverable Items folder in the user's mailbox. The
      default size for this folder is 30 GB. Depending on number and size of items deleted or
      modified, the size of the Recoverable Items folder of the mailbox may increase quickly.
      The Recoverable Items folder is configured with a high quota by default. We recommend
      that you monitor mailboxes that are placed on Litigation Hold on a weekly basis to ensure
      they don't reach the limits of the Recoverable Items quotas.

      As previously explained, when you place a user's mailbox on Litigation Hold, the user's
      archive mailbox is also placed on hold.

      Litigation Hold preserves deleted items and also preserves original versions of modified
      items until the hold is removed. You can optionally specify a hold duration, which
      preserves a mailbox item for the specified duration period. If you specify a hold duration
      period, it's calculated from the date a message is received or a mailbox item is created.

      See the More information section for a description of the Litigation Hold workflow
      process.

Use the EAC to place a mailbox on Litigation Hold
   1. Go to Recipients > Mailboxes.

<!-- p.2224 -->

   2. In the list of user mailboxes, click the mailbox that you want to place on Litigation Hold,
     and then click Edit    .

   3. On the mailbox properties page, click Mailbox features.

   4. Under Litigation hold: Disabled, click Enable to place the mailbox on Litigation Hold.

   5. On the Litigation Hold page, enter the following optional information:

           Litigation hold duration (days): Use this box to specify how long mailbox items are
           held when the mailbox is placed on Litigation Hold. The duration is calculated from
           the date a mailbox item is received or created. If you leave this box blank, items are
           held indefinitely or until the hold is removed. Use days to specify the duration.

           Note*: Use this box to inform the user their mailbox is on Litigation Hold. The note
           will appear on the File tab in Outlook 2010 or later.

           URL*: Use this box to direct the user to a website for more information about
           Litigation Hold. This URL appears on the File tab Outlook 2010 or later.

     *If you leave the Note and URL values blank, the user isn't notified that you placed a

     litigation hold on their mailbox.

   6. Click Save on the Litigation Hold page, and then click Save on the mailbox properties
     page.

Use the Exchange Management Shell to place a
mailbox on Litigation Hold indefinitely
This example places the mailbox bsuneja@contoso.com on Litigation Hold. Items in the
mailbox are held indefinitely or until the hold is removed.

  PowerShell

  Set-Mailbox bsuneja@contoso.com -LitigationHoldEnabled $true

  ７ Note

  When you place a mailbox on Litigation Hold indefinitely (by not specifying a duration
  period), the value for the LitigationHoldDuration property mailbox is set to Unlimited .

<!-- p.2225 -->

Use the Exchange Management Shell to place a
mailbox on Litigation Hold and preserve items for
a specified duration
This example places the mailbox bsuneja@contoso.com on Litigation Hold and preserves items
for 2555 days (approximately 7 years).

  PowerShell

  Set-Mailbox bsuneja@contoso.com -LitigationHoldEnabled $true -
  LitigationHoldDuration 2555

Use the Exchange Management Shell to place all
mailboxes on Litigation Hold
Your organization may require that all mailbox data be preserved.

This example places all user mailboxes in the organization on Litigation Hold and sets the hold
duration for one year (365 days).

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -LitigationHoldEnabled $true -LitigationHoldDuration 365

The example uses the Get-Mailbox cmdlet to retrieve all mailboxes in the organization,
specifies a recipient filter to include all user mailboxes, and then pipes the list of mailboxes to
the Set-Mailbox cmdlet to enable the Litigation Hold and set the hold duration.

To place all user mailboxes on an indefinite hold, run the previous command but don't include
the LitigationHoldDuration parameter.

See the More information section for examples of using other recipient properties in a filter to
include or exclude one or more mailboxes.

Use the Exchange Management Shell to remove a
mailbox from Litigation Hold
This example removes the mailbox bsuneja@contoso.com from Litigation Hold.

<!-- p.2226 -->

  PowerShell

  Set-Mailbox bsuneja@contoso.com -LitigationHoldEnabled $false

How do you know this worked?
To verify that you have successfully placed a mailbox on Litigation Hold, do the one of the
following:

     In the EAC:

          1. Go to Recipients > Mailboxes.

          2. In the list of user mailboxes, click the mailbox that you want to verify Litigation Hold
             settings for, and then click Edit   .

          3. On the mailbox properties page, click Mailbox features.

          4. Under Litigation hold, verify that hold is enabled.

          5. Click View details to verify when the mailbox was placed on Litigation Hold and by
             whom. You can also verify or change the values in the optional Litigation hold
             duration (days), Note, and URL boxes.

     In the Exchange Management Shell, run one of the following commands:

          PowerShell

          Get-Mailbox <name of mailbox> | Format-List LitigationHold*

     or

          PowerShell

          Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq
          'UserMailbox'" | Format-List Name,LitigationHold*

     If a mailbox is placed on Litigation Hold indefinitely, the value for the
     LitigationHoldDuration property mailbox is set to Unlimited .

More information

<!-- p.2227 -->

How does Litigation Hold work? In the normal deleted item workflow, a mailbox item is
moved to the Deletions subfolder in the Recoverable Items folder when a user
permanently deletes it (Shift + Delete) or deletes it from the Deleted Items folder. A
deletion policy (which is a retention tag configured with a Delete retention action) also
moves items to the Deletions subfolder when the retention period expires. When a user
purges an item in the Recoverable Items folder or when the deleted item retention period
expires for an item, it's moved to the Purges subfolder in the Recoverable Items folder
and marked for permanent deletion. It will be purged from Exchange the next time the
mailbox is processed by the Managed Folder Assistant (MFA).

When a mailbox is placed on Litigation Hold, items in the Purges subfolder are preserved
for the hold duration specified by the Litigation Hold. The hold duration is calculated
from the original date an item was received or created, and defines how long items in the
Purges subfolder are held. When the hold duration expires for an item in the Purges
subfolder, the item is marked for permanent deletion and will be purged from Exchange
the next time the mailbox is processed by the MFA. If an indefinite hold is placed on a
mailbox, items will never be purged from the Purges subfolder.

The following illustration shows the subfolders in the Recoverable Items folders and the
hold workflow process.

  ７ Note

  If an In-Place Hold is placed on a mailbox, purged items are moved from the
  Deletions subfolder to the DiscoveryHolds subfolder and are preserved for the hold
  duration for the In-Place Hold.

<!-- p.2228 -->

If your organization requires that all mailbox data has to preserved for a specific period of
time, consider the following before you place all mailboxes in an organization on
Litigation Hold.

   When you use the previous command to place a hold on all mailboxes in an
   organization (or a subset of mailboxes matching a specified recipient filter) only
   mailboxes that exist at the time that you run the command are placed on hold. If you
   create new mailboxes later, you have to run the command again to place the new
   mailboxes on hold. If you create new mailboxes often, you can run the command as a
   scheduled task as frequently as required.

   Placing all mailboxes on Litigation Hold can significantly impact mailbox sizes. In an
   Exchange 2016 or Exchange 2019 organization, plan for adequate storage to meet
   your organization's preservation requirements.

   The Recoverable Items folder has its own storage limit, so items in the folder don't
   count towards the mailbox storage limit. As previously explained, preserving mailbox
   data for a long period of time will result in growth of the Recoverable Items folder in a
   user's mailbox and archive. We recommend that you periodically monitor the size of
   this folder by using the Get-MailboxFolderStatistics cmdlet to ensure it doesn't reach
   the limit. For more information, see:

      Get-MailboxFolderStatistics

      Clean up or delete items from the Recoverable Items folder.

The previous command to place a hold on all mailboxes uses a recipient filter that returns
all user mailboxes. You can use other recipient properties to return a list of specific
mailboxes that you can then pipe to the Set-Mailbox cmdlet to place a Litigation Hold on
those mailboxes.

Here are some examples of using the Get-Mailbox and Get-Recipient cmdlets to return a
subset of mailboxes based on common user or mailbox properties. These examples
assume that relevant mailbox properties (such as CustomAttributeN or Department) have
been populated.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'CustomAttribute15 -eq "OneYearLitigationHold"'

  PowerShell

<!-- p.2229 -->

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'Department -eq "HR"'

  PowerShell

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'PostalCode -eq "98052"'

  PowerShell

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'StateOrProvince -eq "WA"'

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -ne
  'DiscoveryMailbox'"

You can use other user mailbox properties in a filter to include or exclude mailboxes. For
details, see Filterable Properties for the -Filter Parameter.

<!-- p.2230 -->

Place all mailboxes on hold
Article • 04/30/2025

APPLIES TO:          2016       2019       Subscription Edition

Your organization may require all mailbox data to be preserved for a specific period. You can
use Litigation Hold or In-Place Hold to meet this requirement. After you place a mailbox on
Litigation Hold or In-Place Hold, mailbox items that are modified or that are permanently
deleted are preserved in the Recoverable Items folder for the duration specified by the hold.
For more information, see In-Place Hold and Litigation Hold in Exchange Server.

Before you place all mailboxes in an organization on Litigation Hold or In-Place Hold, consider
the following:

      When you place mailboxes on hold, content in a user's archive mailbox (if it's enabled) is
      also placed on hold.

      Placing all mailboxes in an organization on hold can significantly impact mailbox sizes. In
      an Exchange Server deployment, plan for adequate storage to meet your organization's
      preservation requirements.

      Preserving mailbox data for a long duration will result in growth of the Recoverable Items
      folder in a user's primary mailbox and archive mailbox. The Recoverable Items folder has
      its own storage limit, so items in the folder don't count towards the mailbox storage limit.
      In Exchange Server, the default storage limit for the Recoverable Items folder is 30 GB. We
      recommend that you periodically monitor the size of this folder to ensure it doesn't reach
      the limit. For more information, see Recoverable Items folder in Exchange Server.

Choosing between Litigation Hold and In-Place
Hold
Here are some factors to consider when deciding the hold feature you should use to place all
mailboxes in your organization on hold.

                                                                                          ﾉ   Expand table

 If you want to...     Use Litigation Hold                  Use In-Place Hold

 Use the EAC           Yes                                  Yes

                       For setting a Litigation Hold, the   However, you can't select more than 500 source
                       EAC is best suited for quick one-    mailboxes in the EAC. For details, see Create or
                       off actions on a few mailboxes. We   remove an In-Place Hold.

<!-- p.2231 -->

If you want to...    Use Litigation Hold                     Use In-Place Hold

                     recommend using the Exchange
                     Management Shell for placing a
                     Litigation Hold for all users in your
                     organization. For details, see Place
                     a mailbox on Litigation Hold.

Use the Exchange     Yes                                     Yes
Management
Shell

Place more than      Yes                                     Yes; use multiple In-Place Holds
10,000 mailboxes
on hold              Litigation Hold is a mailbox            You can use distribution groups to specify a
                     property. You can place all             maximum of 10,000 mailboxes in a single In-
                     mailboxes in an organization on         Place Hold. To place additional mailboxes on
                     hold by using the Set-Mailbox           hold, you must create additional In-Place Holds.
                     cmdlet.                                 This will result in additional management
                                                             overhead. Using Litigation Hold placing large
                                                             numbers of mailboxes on hold is simpler.

Place many           Yes                                     Yes
different
mailboxes on         Litigation Hold is a mailbox            If you're placing individual holds on thousands
hold for different   property. You can place each            of mailboxes, we recommend using Litigation
periods.             mailbox (or sets of mailboxes) on       Hold. However, if you're creating holds for
                     hold for a different duration.          specific events that involve multiple users (such
                                                             as a legal case), use a single in-Place hold for
                     See the More information section        the group of users.
                     for examples of using recipient
                     properties in a filter so you can       It's not recommended to create separate In-
                     place a Litigation Hold on a subset     Place Holds for each mailbox as this will create
                     of mailboxes.                           many In-Place Hold queries. This will be more
                                                             difficult to manage than Litigation Holds. A
                                                             large number of In-Place Hold objects may also
                                                             result in slow performance in the EAC when
                                                             refreshing, creating, or modifying In-Place
                                                             eDiscovery or In-Place Hold objects.

Automatically        No                                      No
place new
mailboxes on         You have to place a new mailbox         You have to add a new mailbox to an existing
hold                 on Litigation Hold after it's           In-Place Hold, even if you specified a
                     created. You can schedule the           distribution group when you created the In-
                     command or script to run as             Place Hold. You can also schedule the
                     frequently as required to achieve       command or script to run as frequently as
                     the same effect.                        required to achieve the same effect. We
                                                             recommend that the script check if an existing
                                                             In-Place Hold has already reached the 10,000

<!-- p.2232 -->

 If you want to...   Use Litigation Hold             Use In-Place Hold

                                                     mailbox limit, and then create a new In-Place
                                                     Hold if required.

Place all mailboxes on Litigation Hold
You can easily and quickly place all mailboxes on hold indefinitely or for a specified hold
duration using the Exchange Management Shell. This command places all mailboxes on hold
with a hold duration of 2555 days (approximately 7 years).

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -LitigationHoldEnabled $true -LitigationHoldDuration 2555

The example uses the Get-Mailbox cmdlet and a recipient filter to retrieve all user mailboxes in
the organization, and then pipes the list of mailboxes to the Set-Mailbox cmdlet to enable the
Litigation Hold and specify a hold duration. For more information, see Place a mailbox on
Litigation Hold.

Place all mailboxes on In-Place Hold
You can use the EAC to select up to 500 mailboxes and place them on hold. For details, see
Create or remove an In-Place Hold.

To place more than 500 users on In-Place Hold, use the Exchange Management Shell. For
details, see New-MailboxSearch.

   Tip

  In hybrid environments, you can use the inactive mailbox feature in Exchange Online to
  retain mailboxes without consuming a license or requiring an account for the mailbox. The
  inactive mailbox feature requires an "Exchange Online Plan 2, Office 365 Enterprise E3 and
  E5 subscriptions" license. If you have an Exchange Online Plan 1 license, you need to
  assign a separate "Exchange Online Archiving" license to the mailbox. For more
  information, see Inactive mailbox.

More information

<!-- p.2233 -->

When you place all mailboxes in your organization on hold, only the mailboxes that exist
at the time you run the command are placed on hold. If you create new mailboxes later,
run the command again to place them on hold. If you frequently create new mailboxes,
you can run the command as a scheduled task as frequently as required.

Placing mailboxes on hold preserves data by preventing items in the Recoverable Items
folder from being deleted until the specified hold duration for an item expires. If a hold is
configured to hold items indefinitely, items won't be purged from a mailbox. Also, when a
mailbox is on hold the original version of a message is saved before it's modified.
Combine Litigation Hold or In-Place Hold with a Retention Policy, which can automatically
delete messages (and move them into the Recoverable Items folder) after a specified
period, to meet your organization's email retention requirements. See Retention tags and
retention policies in Exchange Server for details.

The Exchange Management Shell command used in this topic to place a Litigation Hold
on all mailboxes uses a recipient filter that returns all user mailboxes. You can use other
recipient properties to return a list of specific mailboxes that you can then pipe to the
Set-Mailbox cmdlet to place a Litigation Hold on those mailboxes.

Here are some examples of using the Get-Mailbox and Get-Recipient cmdlets to return a
subset of mailboxes based on common user or mailbox properties. These examples
assume that relevant mailbox properties (such as CustomAttributeN or Department) have
been populated.

  PowerShell

  Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'CustomAttribute15 -eq "OneYearLitigationHold"'

  PowerShell

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'Department -eq "HR"'

  PowerShell

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'PostalCode -eq "98052"'

  PowerShell

  Get-Recipient -RecipientTypeDetails UserMailbox -ResultSize unlimited -Filter
  'StateOrProvince -eq "WA"'

<!-- p.2234 -->

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -ne
  'DiscoveryMailbox'"

You can use other user mailbox properties in a filter to include or exclude mailboxes. For
details, see Filterable Properties for the -Filter Parameter.

<!-- p.2235 -->

Preserve Bcc and expanded distribution
group recipients for eDiscovery
Article • 04/30/2025

APPLIES TO:         2016       2019       Subscription Edition

In-Place Hold and Litigation Hold allow you to preserve mailbox content to meet regulatory
compliance and eDiscovery requirements. Information about recipients directly addressed in
the To and Cc fields of a message is included in all messages by default, but your organization
requires the ability to search for and reproduce details about all recipients of a message. This
includes:

      Recipients addressed using the Bcc field of a message: Bcc recipients are stored in the
      message in the sender's mailbox, but not included in headers of the message delivered to
      recipients.

      Expanded distribution group recipients: Recipients who receive the message because
      they're members of a distribution group to which the message was addressed, either in
      the To, Cc or Bcc fields.

Exchange 2016 and Exchange 2019 preserve information about Bcc and expanded distribution
group recipients. You can search for this information by using an In-Place eDiscovery search.

How Bcc recipients and expanded distribution
group recipients are preserved
As stated earlier, information about Bcc'ed recipients is stored with the message in the sender's
mailbox. This information is indexed and available to In-Place eDiscovery and Hold.

Information about expanded distribution group recipients is stored with the message after you
place a mailbox on In-Place Hold or Litigation Hold. Distribution group membership is
determined at the time the message is sent. The expanded recipients list stored with the
message isn't impacted by changes to membership of the group after the message is sent.

                                                                                 ﾉ   Expand table

 Information           Is stored in...          Is stored by default?           Is accessible to...
 about...

 To and Cc             Message properties       Yes                             Sender, recipients,
 recipients            in the sender and                                        and compliance
                       recipients' mailboxes.                                   officers

<!-- p.2236 -->

 Information          Is stored in...         Is stored by default?                      Is accessible to...
 about...

 Bcc recipients       Message property in     Yes                                        Sender and
                      the sender's mailbox.                                              compliance
                                                                                         officers

 Expanded             Message properties      No. Expanded distribution group            Compliance
 distribution group   in the sender's         recipient information is stored after a    officers
 recipients           mailbox.                mailbox is placed on In-Place Hold or
                                              Litigation Hold.

Searching for messages sent to Bcc and expanded
distribution group recipients
When searching for messages sent to a recipient, eDiscovery search results now include
messages sent to a distribution group that the recipient is a member of. The following table
shows the scenarios where messages sent to Bcc and expanded distribution group recipients
are returned in eDiscovery searches.

Scenario 1: John is a member of the US-Sales distribution group. This table shows eDiscovery
search results when Bob sends a message to John directly or indirectly via a distribution group.

                                                                                          ﾉ   Expand table

 When you search Bob's mailbox for                  And the message is sent        Results include
 messages sent...                                   with...                        message?

 To:John                                            John on TO                     Yes

 To:John                                            US-Sales on TO                 Yes

 To:US-Sales                                        US-Sales on TO                 Yes

 Cc:John                                            John on CC                     Yes

 Cc:John                                            US-Sales on CC                 Yes

 Cc:US-Sales                                        US-Sales on CC                 Yes

Scenario 2: Bob sends an email to John (To/Cc) and Jack (Bcc directly, or indirectly via a
distribution group). The table below shows eDiscovery search results.

                                                                                          ﾉ   Expand table

<!-- p.2237 -->

 When you     For messages sent...    Results       Notes
 search...                            include
                                      message?

 Bob's        To/Cc:John              Yes           Presents an indication that Jack was Bcc'ed.
 mailbox

 Bob's        Bcc:Jack                Yes           Presents an indication that Jack was Bcc'ed.
 mailbox

 Bob's        Bcc:Jack (via           Yes           List of members of the Bcc'ed distribution group,
 mailbox      distribution group)                   expanded when the message was sent, is visible
                                                    in eDiscovery search preview, export and logs.

 John's       To/Cc:John              Yes           No indication of Bcc recipients.
 mailbox

 John's       Bcc:Jack (directly or   No            Bcc information isn't stored in the message
 mailbox      via distribution                      delivered to recipients. You must search the
              group)                                sender's mailbox.

 Jack's       To/Cc:John (directly    Yes           To/Cc information is included in message
 mailbox      or via distribution                   delivered to all recipients.
              group)

 Jack's       Bcc:Jack (directly or   No            Bcc information isn't stored in the message
 mailbox      via distribution                      delivered to recipients. You must search the
              group)                                sender's mailbox.

Frequently asked questions
Q. When and where is Bcc recipient information stored?

A. Bcc recipient information is preserved by default in the original message in sender's mailbox.
If the Bcc recipient is a distribution group, distribution group membership is only expanded if
the sender's mailbox is on hold.

Q. When and where is the list of expanded distribution group recipients stored?

A. Group membership is expanded at the time the message is sent. The list of expanded
distribution group members is stored in the original message in the sender's mailbox. The
sender's mailbox must be on In-Place Hold or Litigation Hold.

Q. Can the To/Cc recipients see which recipients were Bcc'ed?

A. No. This information isn't included in message headers, and isn't visible to To/Cc recipients.
The sender can see the Bcc field stored in the original message stored in their mailbox.

<!-- p.2238 -->

Compliance officers can see this information when searching the sender's mailbox.

Q. How can I ensure expanded distribution group recipients are always preserved?

A. To ensure expanded distribution group members are always preserved with a message, Place
all mailboxes on hold.

Q. Which types of groups are supported?

A. Distribution groups, mail-enabled security groups, and dynamic distribution groups are
supported.

Q. Is there a limit on the number of distribution group recipients that are expanded and
stored in the message?

A. Up to 10,000 members of a distribution group is preserved.

Q. Are nested distribution groups supported?

A. Yes, 25 levels of nested distribution groups are expanded.

Q. Where is the Bcc and expanded distribution group recipient information visible?

A. Bcc and expanded distribution group recipients information is visible to Compliance officers
when performing an eDiscovery search. Bcc and expanded distribution group recipients are
included in search results copied to a Discovery mailbox or exported to a PST file and in the
eDiscovery log included in search results. Bcc recipient information is also available in search
preview.

Q. What happens if a member of a distribution group is hidden from the organization's
global address list (GAL)?

A. There's no impact. If recipients are hidden from the GAL, they're still included in the list of
recipients for the expanded distribution group.

<!-- p.2239 -->

In-Place eDiscovery in Exchange Server
07/16/2025

APPLIES TO:      2016      2019      Subscription Edition

If your organization adheres to legal discovery requirements (related to organizational policy,
compliance, or lawsuits), In-Place eDiscovery in Exchange Server can help you perform
discovery searches for relevant content within mailboxes.

  ） Important

  In-Place eDiscovery is a powerful feature that allows a user with the correct permissions to
  potentially gain access to all messaging records stored throughout the Exchange Server
  organization. It's important to control and monitor discovery activities, including addition
  of members to the Discovery Management role group, assignment of the Mailbox Search
  management role, and assignment of mailbox access permission to discovery mailboxes.

How In-Place eDiscovery works
In-Place eDiscovery uses the content indexes created by Exchange Search. Role Based Access
Control (RBAC) provides the Discovery Management role group to delegate discovery tasks to
non-technical personnel, without the need to provide elevated privileges that may allow a user
to make any operational changes to Exchange configuration. The Exchange admin center (EAC)
provides an easy-to-use search interface for non-technical personnel such as legal and
compliance officers, records managers, and human resources professionals.

Authorized users can perform an In-Place eDiscovery search by selecting the mailboxes, and
then specifying search criteria such as keywords, start and end dates, sender and recipient
addresses, and message types. After the search is complete, authorized users can then select
one of the following actions:

     Estimate search results - This option returns an estimate of the total size and number of
     items that will be returned by the search based on the criteria you specified.

     Preview search results - This option provides a preview of the results. Messages returned
     from each mailbox searched are displayed.

     Copy search results - This option lets you copy messages to a discovery mailbox.

     Export search results - After search results are copied to a discovery mailbox, you can
     export them to a PST file.

<!-- p.2240 -->

In-Place eDiscovery uses Keyword Query Language (KQL). Users familiar with KQL can construct
powerful search queries to search content indexes. For more information about KQL, see
Keyword Query Language syntax reference.

In-Place eDiscovery permissions
For authorized users to perform In-Place eDiscovery searches, you need to add them to the
Discovery Management role group. This role group consists of two management roles: the
Mailbox Search Role, which allows a user to perform an In-Place eDiscovery search, and the
Legal Hold Role, which allows a user to place a mailbox on In-Place Hold and Litigation Hold.

By default, permissions to perform In-Place eDiscovery-related tasks aren't assigned to any
user or Exchange administrators. Exchange administrators who are members of the
Organization Management role group can add users to the Discovery Management role group
and create custom role groups to narrow the scope of a discovery manager to a subset of
users. To learn more about adding users to the Discovery Management role group, see Assign
eDiscovery permissions in Exchange Server.

  ） Important

  If a user isn't added to the Discovery Management role group or isn't assigned the
  Mailbox Search role, the In-Place eDiscovery & Hold user interface isn't displayed in the
  EAC, and the In-Place eDiscovery (*MailboxSearch) cmdlets aren't available in the
  Exchange Management Shell.
