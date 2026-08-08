---
title: "Exchange Server — pages 2561-2600"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2561-2600
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2561-2600
family: exchange
documentKind: "doc"
abstract: "The Exchange Management Shell names for the conditions listed here are parameters that require the TransportRule cmdlet. Learn more about the cmdlet at New-TransportRule. Learn more about property types for these conditions at Mail flow rule conditions and exceptions (predicates"
---

# Exchange Server — pages 2561-2600

<!-- p.2561 -->

The Exchange Management Shell names for the conditions listed here are parameters that
require the TransportRule cmdlet.

     Learn more about the cmdlet at New-TransportRule.
     Learn more about property types for these conditions at Mail flow rule conditions and
     exceptions (predicates) in Exchange Server.

Supported executable file types for mail flow rule
inspection
The transport agent uses true type detection by inspecting file properties rather than merely
the file extensions. This detection helps to prevent hackers from bypassing your rule by
renaming a file extension. The following table lists the executable file types supported by these
conditions. If a file is found that isn't listed here, the AttachmentIsUnsupported condition is
triggered.

                                                                                     ﾉ     Expand table

 Type of file                                                                       Native extension

 32-bit Windows executable file with a dynamic link library extension.              .dll

 Self-extracting executable program file.                                           .exe

 Uninstallation executable file.                                                    .exe

 Program shortcut file.                                                             .exe

 32-bit Windows executable file.                                                    .exe

 Microsoft Visio XML drawing file.                                                  .vxd

 OS/2 operating system file.                                                        .os2

 16-bit Windows executable file.                                                    .w16

 Disk-operating system file.                                                        .dos

 European Institute for Computer Antivirus Research standard antivirus test file.   .com

 Windows program information file.                                                  .pif

 Windows executable program file.                                                   .exe

  ） Important

<!-- p.2562 -->

  .rar (self-extracting archive files created with the WinRAR archiver), .jar (Java archive

  files), and .obj (compiled source code, 3D object, or sequence files) files are not
  considered to be executable file types. To block these files, you can use mail flow rules
  that look for files with these extensions as described earlier in this article.

Extending the number of supported file types
The supported file types listed in this topic can be revised at any time using IFilter integration.
For more information, see Register IFilters Filter Packs in Exchange Server.

The file types you add using this process become supported file types and no longer trigger
the AttachmentIsUnsupported condition.

Data loss prevention policies and attachment mail
flow rules
To help you manage important business information in email, you can include any of the
attachment-related conditions along with the rules of a data loss prevention (DLP) policy. For
example, you might want to allow messages with passport numbers to be sent but only if the
passport numbers are in a password-protected attachment. To accomplish this, do the
following steps:

     Create a DLP policy that inspects mail for passport-related sensitive information. Learn
     more at Data loss prevention in Exchange Server.
     Add the Any attachment is password protected exception in the Except if... mail flow rule
     area.
     Define an action to take on mail that contains passport numbers that aren't in the
     protected file.

DLP policies and attachment-related conditions can help you enforce your business needs by
defining those needs as mail flow rule conditions, exceptions, and actions. When you include
the sensitive information inspection in a DLP policy, any attachments to messages are scanned
for that information only. However, attachment-related conditions such as size or file type
aren't included until you add the conditions listed in this topic. DLP isn't available with all
versions of Exchange; learn more at Data loss prevention.

<!-- p.2563 -->

Recoverable Items folder in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016      2019   Subscription Edition

To protect from accidental or malicious deletion and to facilitate discovery efforts commonly
undertaken before or during litigation or investigations, Exchange Server and Exchange Online
use the Recoverable Items folder. The Recoverable Items folder replaces the feature that was
known as the dumpster in earlier versions of Exchange. The following Exchange features use the
Recoverable Items folder:

      Deleted item retention

      Single item recovery

      In-Place Hold

      Litigation Hold

      Mailbox audit logging

      Calendar logging

Terminology
Knowledge of the following terms will help you understand the content in this topic.

Delete

  Describes when an item is deleted from any folder and placed in the Deleted Items default
  folder.

Soft delete

  Describes when an item is deleted from the Deleted Items default folder and placed in the
  Recoverable Items folder. Also describes when an Outlook user deletes an item by pressing
  Shift+Delete, which bypasses the Deleted Items folder and places the item directly in the
  Recoverable Items folder.

Hard delete

<!-- p.2564 -->

  Describes when an item is marked to be purged from the mailbox database. This is also
  known as a store hard delete.

Recoverable Items folder
Each user mailbox is divided into two subtrees: the IPM (interpersonal messaging) subtree,
which contains the normal, visible folders such as Inbox, Calendar, and Sent Items and the non-
IPM subtree, which contains internal data, preferences, and other operational data about the
mailbox. The Recoverable Items folder resides in the non-IPM subtree of each mailbox. This
subtree isn't visible to users using Outlook, Outlook on the web, or other email clients.

This architectural change provides the following key benefits:

     When a mailbox is moved to another mailbox database, the Recoverable Items folder
     moves with it.

     The Recoverable Items folder is indexed by Exchange Search and can be discovered by
     using In-Place eDiscovery.

     The Recoverable Items folder has its own storage quota.

     Exchange can prevent data from being purged from the Recoverable Items folder.

     Exchange can track edits of certain content.

The Recoverable Items folder contains the following subfolders:

     Deletions: This subfolder contains all items deleted from the Deleted Items folder. (In
     Outlook, a user can soft delete an item by pressing Shift+Delete.) This subfolder is
     exposed to users through the Recover Deleted Items feature in Outlook and Outlook on
     the web.

     Versions: If In-Place Hold or Litigation Hold is enabled, this subfolder contains the original
     and modified copies of the deleted items. This folder isn't visible to end users.

     Purges: If either Litigation Hold or single item recovery is enabled, this subfolder contains
     all items that are hard deleted. This folder isn't visible to end users.

     Audits: If mailbox audit logging is enabled for a mailbox, this subfolder contains the audit
     log entries. To learn more about mailbox audit logging, see Mailbox audit logging in
     Exchange Server.

     DiscoveryHolds: If In-Place Hold is enabled, this subfolder contains all items that meet
     the hold query parameters and are hard deleted.

<!-- p.2565 -->

     Calendar Logging: This subfolder contains calendar changes that occur within a mailbox.
     This folder isn't available to users.

The following illustration shows the subfolders in the Recoverable Items folders. It also shows
the deleted item retention, single item recovery, and hold workflow processes that are
described in the following sections.

Deleted item retention
An item is considered to be soft deleted in the following cases:

     A user deletes an item or empties all items from the Deleted Items folder.

     A user presses Shift+Delete to delete an item from any other mailbox folder.

Soft-deleted items are moved to the Deletions subfolder of the Recoverable Items folder. This
provides an additional layer of protection so users can recover deleted items without requiring
Help desk intervention. Users can use the Recover Deleted Items feature in Outlook or Outlook
on the web to recover a deleted item. Users can also use this feature to permanently delete an
item. For more information, see:

     Recover deleted items in Outlook for Windows

     Recover deleted items or email messages in Outlook on the web

Items remain in the Deletions subfolder until the deleted item retention period is reached. The
default deleted item retention period for a mailbox database is 14 days. You can modify this
period for a mailbox database or for a specific mailbox. In addition to a deleted item retention

<!-- p.2566 -->

period, the Recoverable Items folder is also subject to quotas. To learn more, see Recoverable
Items mailbox quotas later in this topic.

When the deleted item retention period expires, the item is completely removed from
Exchange Server.

The Don't permanently delete items until the database is backed up setting can affect this
behavior. If this setting is not enabled (default), only the deleted item retention period is
considered to remove items from the Deletions subfolder. If this setting is enabled and the
deleted item retention period is reached, items are not deleted until after the mailbox database
on which the mailbox is located has been backed up.

For more information about these settings and how to modify them, see Configure Deleted
Item retention and Recoverable Items quotas.

Single item recovery
If an item is removed from the Deletions subfolder, either by a user purging the item by using
the Recover Deleted Items feature or by an automated process such as the Managed Folder
Assistant (retention tag set to permanently delete for example), the item can't be recovered by
the user. In previous versions of Exchange, recovering these items required the administrator to
restore the mailbox database or a mailbox from backup copies. This process generally delayed
recovery by minutes or hours, depending on the backup mechanism used.

In Exchange Server, you can use single item recovery to recover items without using backup
media to restore the mailbox databases. This results in considerably shorter recovery periods. If
single item recovery is enabled for a mailbox, any item removed from the Deletions subfolder
before the deleted item retention period is moved to the Purges subfolder. When the
Managed Folder Assistant processes the Recoverable Items folder for a mailbox that has single
item recovery enabled, any item in the Purges subfolder isn't purged if the deleted item
retention period hasn't expired for that item.

The following table lists the contents of and actions that can be performed in the Recoverable
Items folder if single item recovery is enabled.

Recoverable Items folder and single item recovery

                                                                                  ﾉ   Expand table

<!-- p.2567 -->

 State of    Recoverable      Recoverable       Users can       Managed Folder Assistant
 single      Items folder     Items folder      purge items     automatically purges items from
 item        contains soft-   contains hard-    from the        the Recoverable Items folder
 recovery    deleted items    deleted items     Recoverable
                                                Items folder

 Enabled     Yes              Yes               No              Yes. By default, all items are
                                                                purged after 14 days, with the
                                                                exception of calendar items, which
                                                                are purged after 120 days.

 Disabled    Yes              No                Yes             Yes. By default, all items are
                                                                purged after 14 days, with the
                                                                exception of calendar items, which
                                                                are purged after 120 days. If the
                                                                Recoverable Items warning quota
                                                                is reached before the deleted item
                                                                retention period elapses, messages
                                                                are deleted in first in, first out
                                                                (FIFO) order.

In Exchange Server, single item recovery isn't enabled by default for new mailboxes or
mailboxes moved from a previous version of Exchange. You need to use the Exchange
Management Shell to enable single item recovery for a mailbox, and then configure or modify
the deleted item retention period. For details about how to perform a single item recovery, see
Recover deleted messages in a user's mailbox.

In-Place Hold and Litigation Hold
In Exchange Server and Exchange Online, discovery managers can use In-Place eDiscovery with
delegated Discovery Management role group permissions to perform eDiscovery searches of
mailbox content. In Exchange Server and Exchange Online, you can use In-Place Hold to
preserve mailbox items that match query parameters and protect the items from deletion by
users or automated processes. You can also use Litigation Hold to preserve all items in user
mailboxes and protect the items from deletion by users or automated processes.

Putting a mailbox on In-Place Hold or Litigation Hold stops the Managed Folder Assistant from
automatically purging messages from the DiscoveryHolds, Deletions, and Purges subfolders.
Additionally, copy-on-write page protection is also enabled for the mailbox. Copy-on-write
page protection creates a copy of the original item before any modifications are written to the
Exchange store. After the mailbox is removed from hold, the Managed Folder Assistant
resumes automated purging.

  ７ Note

<!-- p.2568 -->

  If you put a mailbox on both In-Place Hold and Litigation Hold, Litigation Hold takes
  preference because this puts the entire mailbox on hold.

The following table lists the contents of and actions that can be performed in the Recoverable
Items folder if Litigation Hold is enabled.

Recoverable Items folder and holds

                                                                                    ﾉ   Expand table

 State of    Recoverable        Recoverable Items     Users can purge      Managed Folder
 hold        Items folder       folder contains       items from the       Assistant automatically
             contains soft-     modified and hard-    Recoverable Items    purges items from the
             deleted items      deleted items         folder               Recoverable Items
                                                                           folder

 Enabled     Yes                Yes                   No                   No

 Disabled    Yes                No                    Yes                  Yes

To learn more about In-Place eDiscovery, In-Place Hold, and Litigation Hold, see the following
topics:

     In-Place eDiscovery in Exchange Server

     In-Place Hold and Litigation Hold in Exchange Server

Copy-on-write page protection and modified items
If a user who is placed on In-Place Hold or Litigation Hold modifies specific properties of a
mailbox item, a copy of the original mailbox item is created before the changed item is written.
The original copy is saved in the Versions subfolder. This process is known as copy-on-write
page protection. Copy-on-write page protection applies to items residing in any mailbox folder.
The Versions subfolder isn't visible to users.

The following table lists the message properties that trigger copy-on-write page protection.

Properties that trigger copy-on-write page protection

                                                                                    ﾉ   Expand table

 Item type                        Properties that trigger copy-on-write page protection

 Messages (IPM.Note*)             Subject
 Posts (IPM.Post*)                      Body

<!-- p.2569 -->

 Item type                            Properties that trigger copy-on-write page protection

                                           Attachments
                                           Senders and recipients
                                           Sent and received dates

 Items other than messages and        Any change to a visible property, except the following:
 posts                                      Item location (when an item is moved between folders)
                                           Item status change (read or unread)
                                           Changes to a retention tag applied to an item

 Items in the Drafts default folder   None. Items in the Drafts folder are exempt from copy-on-write page
                                      protection.

  ） Important

  Copy-on-write page protection doesn't save a version of the meeting when a meeting
  organizer receives responses from attendees and the meeting's tracking information is
  updated. Also, changes to RSS feeds aren't captured by copy-on-write page protection.

When a mailbox is no longer on In-Place Hold or litigation hold, copies of modified items
stored in the Versions folder are removed.

Recoverable Items mailbox quotas
When an item is moved to the Recoverable Items folder, its size is deducted from the mailbox
quota and added to the size of the Recoverable Items folder. In Exchange Server, mailbox
databases have a configurable Recoverable Items warning quota (soft limit) of 20 GB and a
Recoverable Items quota ( hard limit) of 30 GB. By default, these limits are inherited by all
mailboxes in the database. However, you can configure individual mailboxes with different
quotas. To learn more, see Configure Deleted Item retention and Recoverable Items quotas.

In Exchange Online, the default limits for the Recoverable Items quota are the same as
Exchange Server: a soft limit of 20 GB and a hard limit of 30 GB. However, the quotas for the
Recoverable Items folder are automatically increased to 90 GB and 100 GB, respectively, when
you place a mailbox on Litigation Hold or In-Place Hold.

When the Recoverable Items folder for a mailbox reaches the Recoverable Items quota, no
more items can be stored in the folder. This impacts mailbox functionality in the following
ways:

        Mailbox users can't delete items.

<!-- p.2570 -->

     The Managed Folder Assistant can't delete items based on retention tag or managed
     folder settings.

     For mailboxes that have single item recovery, In-Place Hold or Litigation Hold enabled,
     the copy-on-write page protection process can't maintain versions of items edited by the
     user.

     For mailboxes that have mailbox audit logging enabled, no mailbox audit log entries can
     be saved in the Audits subfolder.

For mailboxes that aren't placed on In-Place Hold or Litigation Hold, the Managed Folder
Assistant automatically purges items from the Recoverable Items folder when the deleted item
retention period expires. If the folder reaches the Recoverable Items warning quota, the
assistant automatically purges items in first-in-first-out order.

When the Recoverable Items folder reaches the soft and hard limit defaults, you are notified by
means of the event log and a Microsoft System Center Operations Manager alert. This alert
fires when the Recoverable Items folder first reaches the soft and hard limit defaults, and then
once daily afterward.

The following table lists the events logged when the Recoverable Items folder reaches the soft
and hard limit defaults.

Recoverable Items quota warnings and errors

                                                                                     ﾉ   Expand table

 Event   Type      Source                         Message
 ID

 10024   Warning   MSExchangeIS Mailbox Store     The mailbox for <mailbox user> (<GUID>) has
                                                  exceeded the Recoverable Items Warning Quota.
                                                  Please remove items from Recoverable Items or
                                                  increase the Recoverable Items Warning Quota and
                                                  Recoverable Items Quota. If the Recoverable Items
                                                  Quota is exceeded, the user will be unable to delete
                                                  items from the mailbox.

 10023   Error     MSExchangeIS Mailbox Store     The mailbox for <mailbox user> (<GUID>) has
                                                  exceeded the maximum Recoverable Items Quota.
                                                  Items cannot be deleted from this mailbox. The
                                                  mailbox owner should be notified about the
                                                  condition of the mailbox as soon as possible. Please
                                                  remove items from Recoverable Items or increase
                                                  the Recoverable Items Quota to restore functionality.

<!-- p.2571 -->

 Event    Type      Source                        Message
 ID

 10023    Warning   MSExchangeMailboxAssistants   The mailbox: <mailbox user> Recoverable Items size
                                                  has exceeded the warning quota limit. Items were
                                                  deleted from Recoverable Items folders to prevent
                                                  mailbox outage. Recoverable Items Warning Quota:
                                                  20 GB (21,474,836,480 bytes) Original Recoverable
                                                  Items size: 21475005311 Current Recoverable Items
                                                  size: 21474823820 Folder stats: - Folders processed:
                                                  RecoverableItemsRoot, RecoverableItemsVersions,
                                                  RecoverableItemsPurges, RecoverableItemsDeletions
                                                  - Original folder sizes: 21391661934, 55190914,
                                                  1987247, 26157788 (item counts: 276828, 400, 84,
                                                  646) - Current folder sizes: 21391480443, 55190914,
                                                  1987247, 26157788 (item counts: 276817, 400, 84,
                                                  646)

If the mailbox is placed on In-Place Hold or Litigation Hold, copy-on-write page protection
can't maintain versions of modified items. To maintain versions of modified items, you need to
reduce the size of the Recoverable Items folder. You can use the Search-Mailbox cmdlet to
copy messages from the Recoverable Items folder of a mailbox to a discovery mailbox, and
then delete the items from the mailbox. Alternatively, you can also raise the Recoverable Items
quota for the mailbox. For details, see Clean up or delete items from the Recoverable Items
folder.

More information
     Copy-on-write is only enabled when a mailbox is on In-Place Hold or Litigation Hold.

     If users need to recover deleted items from the Recoverable Items folder, point them to
     the following topics:

          Restore deleted items in Outlook for Windows

          Recover deleted items or email in Outlook on the web

<!-- p.2572 -->

Clean up or delete items from the
Recoverable Items folder
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The Recoverable Items folder (known in earlier versions of Exchange as the dumpster) exists to
protect from accidental or malicious deletions and to facilitate discovery efforts commonly
undertaken before or during litigation or investigations.

How you clean up a user's Recoverable Items folder depends on whether the mailbox is placed
on In-Place Hold or Litigation Hold, or had single item recovery enabled:

      If a mailbox isn't placed on In-Place Hold or Litigation Hold or doesn't have single item
      recovery enabled, you can simply delete items from the Recoverable Items folder. After
      items are deleted, you can't use single item recovery to recover them.

      If the mailbox is placed on In-Place Hold or Litigation Hold or has single item recovery
      enabled, you'll want to preserve the mailbox data until the hold is removed or single item
      recovery is disabled. In this case, you need to perform more detailed steps to clean up the
      Recoverable Items folder.

To learn more about In-Place Hold and Litigation Hold, see In-Place Hold and Litigation Hold in
Exchange Server. To learn more about single item recovery, see "Single Item Recovery" in
Recoverable Items folder in Exchange Server.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Delete mailbox content" entry in
      the Messaging policy and compliance permissions in Exchange Server topic.

      Because incorrectly cleaning up the Recoverable Items folder can result in data loss, it's
      important that you're familiar with the Recoverable Items folder and the impact of
      removing its contents. Before performing this procedure, we recommend that you review
      the information in Recoverable Items folder in Exchange Server.

      You can't use the Exchange admin center (EAC) to perform these procedures. You must
      use the Exchange Management Shell. To learn how to open the Exchange Management
      Shell in your on-premises Exchange organization, see Open the Exchange Management
      Shell.

<!-- p.2573 -->

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server   ,
Exchange Online, or Exchange Online Protection   .

Use the Exchange Management Shell to delete
items from the Recoverable Items folder for
mailboxes that aren't placed on hold or don't have
single item recovery enabled
This example permanently deletes items from the user Gurinder Singh's Recoverable Items
folder and also copies the items to the GurinderSingh-RecoverableItems folder in the Discovery
Search Mailbox (a discovery mailbox created by Exchange Setup).

  PowerShell

  Search-Mailbox -Identity "Gurinder Singh" -SearchDumpsterOnly -TargetMailbox
  "Discovery Search Mailbox" -TargetFolder "GurinderSingh-RecoverableItems" -
  DeleteContent

  ７ Note

  To delete items from the mailbox without copying them to another mailbox, use the
  preceding command without the TargetMailbox and TargetFolder parameters.

For detailed syntax and parameter information, see Search-Mailbox.

Use the Exchange Management Shell to clean up
the Recoverable Items folder for mailboxes that are
placed on hold or have single item recovery
enabled
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Delete mailbox content" entry in the Messaging policy
and compliance permissions in Exchange Server topic.

<!-- p.2574 -->

If a mailbox reaches its Recoverable Items quota, we recommend that you raise the quota and
not delete items from the folder. You can also monitor events in the Application log related to
the Recoverable Items warning quota and take necessary actions such as raising the quota or
investigating the growth of the Recoverable Items folder for mailboxes that reach the warning
quota.

If storage constraints or similar issues prevent you from raising the Recoverable Items quota,
we recommend that you first copy data from the user's Recoverable Items folder to another
mailbox before you delete messages. If you're deleting items due to storage constraints on one
volume, you can copy items to a mailbox located on a volume that has adequate storage.

This procedure copies items from Gurinder Singh's Recoverable Items folder to the
GurinderSingh-RecoverableItems folder in the Discovery Search Mailbox. Before you copy and
delete items from the Recoverable Items folder, you should first perform several steps to make
sure items aren't deleted from the Recoverable Items folder. After you copy items to a
discovery or backup mailbox and clean up the folder, you can revert to the mailbox's previous
settings.

   1. Retrieve the following quota settings. Be sure to note the values so you can revert to
     these settings after cleaning up the Recoverable Items folder:

            RecoverableItemsQuota

            RecoverableItemsWarningQuota

            ProhibitSendQuota

            ProhibitSendReceiveQuota

            UseDatabaseQuotaDefaults

            RetainDeletedItemsFor

            UseDatabaseRetentionDefaults

         ７ Note

         If the UseDatabaseQuotaDefaults parameter is set to $true , the previous quota
         settings aren't applied. The corresponding quota settings configured on the mailbox
         database are applied, even if individual mailbox settings are populated.

         PowerShell

         Get-Mailbox "Gurinder Singh" | Format-List

<!-- p.2575 -->

     *Quota*,RetainDeletedItemsFor,UseDatabaseRetentionDefaults

2. Retrieve the mailbox access settings for the mailbox. Be sure to note these settings for
  later.

    PowerShell

     Get-CASMailbox "Gurinder Singh" | Format-List EwsEnabled, ActiveSyncEnabled,
     MAPIEnabled, OWAEnabled, ImapEnabled, PopEnabled

3. Retrieve the current size of the Recoverable Items folder. Note the size so you can raise
  the quotas in Step 6.

    PowerShell

     Get-MailboxFolderStatistics "Gurinder Singh" -FolderScope RecoverableItems |
     Format-List Name,FolderAndSubfolderSize

4. Disable client access to the mailbox to make sure no changes can be made to mailbox
  data for the duration of this procedure.

    PowerShell

     Set-CASMailbox "Gurinder Singh" -EwsEnabled $false -ActiveSyncEnabled $false
     -MAPIEnabled $false -OWAEnabled $false -ImapEnabled $false -PopEnabled $false

5. To make sure no items are deleted from the Recoverable Items folder, increase the
  Recoverable Items quota, increase the Recoverable Items warning quota, and set the
  deleted item retention period to a value higher than the current size of the user's
  Recoverable Items folder. This is particularly important for preserving messages for
  mailboxes placed on In-Place Hold or Litigation Hold. We recommend raising these
  settings to twice their current size.

    PowerShell

     Set-Mailbox "Gurinder Singh" -RecoverableItemsQuota 50Gb -
     RecoverableItemsWarningQuota 50Gb -RetainDeletedItemsFor 3650 -
     ProhibitSendQuota 50Gb -ProhibitSendReceiveQuota 50Gb -
     UseDatabaseQuotaDefaults $false -UseDatabaseRetentionDefaults $false

6. Stop the Microsoft Exchange Mailbox Assistants service and prevent it from starting on
  the Mailbox server by running the following commands:

    PowerShell

<!-- p.2576 -->

    Stop-Service MSExchangeMailboxAssistants; Set-Service
    MSExchangeMailboxAssistants -StartupType Disabled

  The effect of this command is to stop the Managed Folder Assistant on the Mailbox
  server.

    ） Important

    If the mailbox resides on a mailbox database in a database availability group (DAG),
    you must disable the Managed Folder Assistant on each DAG member that hosts a
    copy of the database. If the database fails over to another server, this prevents the
    Managed Folder Assistant on that server from deleting mailbox data.

7. Disable single item recovery and remove the mailbox from Litigation Hold.

    PowerShell

    Set-Mailbox "Gurinder Singh" -SingleItemRecoveryEnabled $false -
    LitigationHoldEnabled $false

    ） Important

    After you run this command, it may take up to one hour to disable single item
    recovery or Litigation Hold. We recommend that you perform the next step only
    after this period has elapsed.

8. Copy items from the Recoverable Items folder to a folder in the Discovery Search Mailbox
  and delete the contents from the source mailbox.

    PowerShell

    Search-Mailbox -Identity "Gurinder Singh" -SearchDumpsterOnly -TargetMailbox
    "Discovery Search Mailbox" -TargetFolder "GurinderSingh-RecoverableItems" -
    DeleteContent

  If you need to delete only messages that match specified conditions, use the SearchQuery
  parameter to specify the conditions. This example deletes messages that have the string
  "Your bank statement" in the Subject field.

    PowerShell

<!-- p.2577 -->

      Search-Mailbox -Identity "Gurinder Singh" -SearchQuery "Subject:'Your bank
      statement'" -SearchDumpsterOnly -TargetMailbox "Discovery Search Mailbox" -
      TargetFolder "GurinderSingh-RecoverableItems" -DeleteContent

      ７ Note

      It isn't required to copy items to the Discovery Search Mailbox. You can copy
      messages to any mailbox. However, to prevent access to potentially sensitive
      mailbox data, we recommend copying messages to a mailbox that has access
      restricted to authorized records managers. By default, access to the default Discovery
      Search Mailbox is restricted to members of the Discovery Management role group.
      For details, see In-Place eDiscovery in Exchange Server.

 9. If the mailbox was placed on Litigation Hold or had single item recovery enabled earlier,
   enable these features again.

      PowerShell

      Set-Mailbox "Gurinder Singh" -SingleItemRecoveryEnabled $true -
      LitigationHoldEnabled $true

      ） Important

      After you run this command, it may take up to one hour to enable single item
      recovery or Litigation Hold. We recommend that you enable the Managed Folder
      Assistant and allow client access (Steps 11 and 12) only after this period has elapsed.

10. Revert the following quotas to the values noted in Step 1:

         RecoverableItemsQuota

         RecoverableItemsWarningQuota

         ProhibitSendQuota

         ProhibitSendReceiveQuota

         UseDatabaseQuotaDefaults

         RetainDeletedItemsFor

         UseDatabaseRetentionDefaults

<!-- p.2578 -->

     In this example, the mailbox is removed from retention hold, the deleted item retention
     period is reset to the default value of 14 days, and the Recoverable Items quota is
     configured to use the same value as the mailbox database. If the values you noted in Step
     1 are different, you must use the preceding parameters to specify each value and set the
     UseDatabaseQuotaDefaults parameter to $false . If the RetainDeletedItemsFor and
     UseDatabaseRetentionDefaults parameters were previously set to a different value, you
     must also revert them to the values noted in Step 1.

       PowerShell

       Set-Mailbox "Gurinder Singh" -RetentionHoldEnabled $false -
       RetainDeletedItemsFor 14 -RecoverableItemsQuota unlimited -
       UseDatabaseQuotaDefaults $true

 11. Configure the Microsoft Exchange Mailbox Assistants service to start automatically and
     start it on the Mailbox server by running the following commands:

       PowerShell

       Set-Service MSExchangeMailboxAssistants -StartupType Automatic; Start-Service
       MSExchangeMailboxAssistants

 12. Enable client access to the mailbox by running the following command:

       PowerShell

       Set-CASMailbox -ActiveSyncEnabled $true -EwsEnabled $true -MAPIEnabled $true
       -OWAEnabled $true -ImapEnabled $true -PopEnabled $true

For detailed syntax and parameter information, see the following topics:

     Get-Mailbox

     Get-CASMailbox

     Get-MailboxFolderStatistics

     Set-CASMailbox

     Set-Mailbox

     Search-Mailbox

How do you know this worked?

<!-- p.2579 -->

To verify that you have successfully cleaned up the Recoverable Items folder of a mailbox, use
Get-MailboxFolderStatistics cmdlet the check the size of the Recoverable Items folder.

This example retrieves the size of the Recoverable Items folder and its subfolders and an item
count in the folder and each subfolder.

  PowerShell

  Get-MailboxFolderStatistics -Identity "Gurinder Singh" -FolderScope
  RecoverableItems | Format-Table
  Name,FolderAndSubfolderSize,ItemsInFolderAndSubfolders -Auto

<!-- p.2580 -->

S/MIME for message signing and
encryption
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

As an administrator in Exchange Server, you can enable Secure/Multipurpose Internet Mail
Extensions (S/MIME) for your organization. S/MIME is a widely accepted method (more
precisely, a protocol) for sending digitally signed and encrypted messages. S/MIME allows you
to encrypt emails and digitally sign them. When you use S/MIME, it helps the people who
receive the message by:

      Ensuring that the message in their inbox is the exact message that started with the
      sender.

      Ensuring that the message came from the specific sender and not from someone
      pretending to be the sender.

To do this, S/MIME provides for cryptographic security services such as authentication,
message integrity, and non-repudiation of origin (using digital signatures). S/MIME also helps
enhance privacy and data security (using encryption) for electronic messaging.

S/MIME requires a certificate and publishing infrastructure that is often used in business-to-
business and business-to-consumer situations. The user controls the cryptographic keys in
S/MIME and can choose whether to use them for each message they send. Email programs
such as Outlook search a trusted root certificate authority location to perform digital signing
and verification of the signature.

For a more complete background about the history and architecture of S/MIME in the context
of email, see Understanding S/MIME.

Supported scenarios and technical considerations
for S/MIME
You can set up S/MIME to work with any of the following end points:

      Outlook 2010 or later

      Outlook on the web (formerly known as Outlook Web App)

      Exchange ActiveSync (EAS)

<!-- p.2581 -->

The steps that you follow to set up S/MIME with each of these endpoints are slightly different.
Generally, you need to complete these steps:

   1. Install a Windows-based Certification Authority and set up a public key infrastructure to
     issue S/MIME certificates. Certificates issued by third-party certificate providers are
     supported. For details, see Server Certificate Deployment Overview.

   2. Publish the user certificate in an on-premises Active Directory Domain Services (AD DS)
     account in the UserSMIMECertificate and/or UserCertificate attributes. Your AD DS
     needs to be located on computers at a physical location that you control and not at a
     remote facility or cloud-based service somewhere on the Internet. For more information
     about AD DS, see Active Directory Domain Services Overview.

   3. Set up a virtual certificate collection in order to validate S/MIME. This information is used
     by Outlook on the web when validating the signature of an email and ensuring that it was
     signed by a trusted certificate.

   4. Set up the Outlook or EAS end point to use S/MIME.

Set up S/MIME with Outlook on the web
Setting up S/MIME with Outlook on the web involves these key steps:

   1. S/MIME settings for Outlook on the web in Exchange Server.

   2. Set up Virtual Certificate Collection to Validate S/MIME

For information about how to send an S/MIME encrypted message in Outlook on the web, see
Encrypt messages by using S/MIME in Outlook on the web           .

Related message encryption technologies
A variety of encryption technologies work together to provide protection for messages at rest
and in transit. S/MIME can work simultaneously with the following technologies but isn't
dependent on them:

     Transport Layer Security (TLS): Encrypts the tunnel or the route between email servers in
     order to help prevent snooping and eavesdropping, and encrypts the connection
     between email clients and servers.

        ７ Note

<!-- p.2582 -->

  Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
  protocol that's used to encrypt data sent between computer systems. They're so
  closely related that the terms "SSL" and "TLS" (without versions) are often used
  interchangeably. Because of this similarity, references to "SSL" in Exchange topics,
  the Exchange admin center, and the Exchange Management Shell have often been
  used to encompass both the SSL and TLS protocols. Typically, "SSL" refers to the
  actual SSL protocol only when a version is also provided (for example, SSL 3.0). To
  find out why you should disable the SSL protocol and switch to TLS, check out
  Protecting you against the SSL 3.0 vulnerability .

BitLocker: Encrypts the data on a hard drive in a datacenter so that if someone gets
unauthorized access, they can't read it. For more information, see BitLocker: How to
deploy on Windows Server 2012 and later

<!-- p.2583 -->

S/MIME settings for Outlook on the web in
Exchange Server
As an Exchange administrator, you can set up Outlook on the web (OWA) to allow sending and
receiving S/MIME-protected messages. Use the Get-SmimeConfig and Set-SmimeConfig cmdlets
to view and manage this feature in the Exchange Management Shell. To open the Exchange
Management Shell, see Open the Exchange Management Shell.

For detailed syntax and parameter information, see Get-SmimeConfig and Set-SmimeConfig.

Make sure that you already have configured the S/MIME prerequisites as outlined in the article
S/MIME for message signing and encryption.

  ７ Note

  A complete list of browsers that support S/MIME is available in the Exchange Server
  supportability matrix.

Configure policies to install the S/MIME extensions in
Web Browsers
S/MIME in Outlook on the web in the Chromium-based Microsoft Edge or in Google Chrome
requires specific policy settings that are configured by an admin. Specifically, you need to set and
configure the policy named ExtensionInstallForcelist to install the Microsoft S/MIME extension in
the browser. The policy value for the OWA S/MIME extension is:
maafgiompdekodanheihhgilkjchcakm;https://outlook.office.com/owa/SmimeCrxUpdate.ashx .

Applying this policy requires domain-joined computers, so using S/MIME in Chrome effectively
requires domain-joined computers.

To ensure that the correct S/MIME extension is fetched for update, it's important to also add the
following ExtensionSettings:

Registry path:
SOFTWARE\Policies\Microsoft\Edge\ExtensionSettings\maafgiompdekodanheihhgilkjchcakm Value

type: DWORD Value name: override_update_url Value data: 1

<!-- p.2584 -->

To elaborate, maafgiompdekodanheihhgilkjchcakm is the extension id for S/MIME managed
extension.

Install the S/MIME Control in Web Browsers
The policy is a prerequisite for using S/MIME in Outlook on the web. It doesn't replace the
S/MIME control that's installed by users. Users are prompted to download and install the S/MIME
control in Outlook on the web during their first use of S/MIME. Or, users can proactively go to
S/MIME in their Outlook on the web settings to get the download link for the control.

Ensure your admin hasn't configured NativeMessagingUserLevelHosts policy to be disabled. This
is to ensure communication is established with S/MIME control.

In case your organization has configured the Browser with a NativeMessagingBlocklist policy, you
must make sure to allowlist the S/MIME control there. Your admin can use the
NativeMessagingAllowlist policy to allow the Microsoft S/MIME Control. The value for the
Microsoft S/MIME Control is: com.microsoft.outlook.smime.chromenativeapp .

Allow the S/MIME Interaction with your OWA Domain
To allow the S/MIME to interact with your OWA Domain, the users are being asked to configure
your OWA Domain once after clicking on an email with S/MIME Content. The user sees a yellow
Mailtip with a link, which guides to the S/MIME Extension Options Page, on which they can add
your OWA Domain to be allowed.

 Last updated on 04/29/2026

<!-- p.2585 -->

High availability and site resilience in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

You can protect your Exchange Server mailbox databases and the data they contain by
configuring your Exchange servers and databases for high availability and site resilience.
Exchange Server minimizes the cost and complexity of deploying a highly available and
resilient messaging solution while providing high levels of service and data availability and
support for very large mailboxes.

Exchange Server enables customers of all sizes and in all segments to economically deploy a
messaging continuity service in their organization by building on the native replication
capabilities and high availability architecture introduced in Exchange 2010. For a list of changes
since Exchange 2010, see Changes to high availability and site resilience over previous versions.

Key terminology
The following key terms are important to understand high availability or site resilience:

Active Manager

  An internal Exchange component which runs inside the Microsoft Exchange Replication
  service that's responsible for failure monitoring and corrective action through failover
  within a database availability group (DAG).

AutoDatabaseMountDial

  A property setting of a Mailbox server that determines whether a passive database copy
  will automatically mount as the new active copy, based on the number of log files missing
  by the copy being mounted.

Continuous replication - block mode

  In block mode, as each update is written to the active database copy's active log buffer, it's
  also shipped to a log buffer on each of the passive mailbox copies in block mode. When
  the log buffer is full, each database copy builds, inspects, and creates the next log file in
  the generation sequence.

Continuous replication - file mode

<!-- p.2586 -->

  In file mode, closed transaction log files are pushed from the active database copy to one
  or more passive database copies.

Database availability group

  A group of up to 16 Exchange servers that hosts a set of replicated databases.

Database mobility

  The ability of an Exchange Server mailbox database to be replicated to and mounted on
  other Exchange servers.

Datacenter

  Typically this refers to an Active Directory site; however, it can also refer to a physical site.
  In the context of this documentation, datacenter equals Active Directory site.

Datacenter Activation Coordination mode

  A property of the DAG setting that, when enabled, forces the Microsoft Exchange
  Replication service to acquire permission to mount databases at startup.

Disaster recovery

  Any process used to manually recover from a failure. This can be a failure that affects a
  single item, or it can be a failure that affects an entire physical location.

Exchange third-party replication API

  An Exchange-provided API that enables use of third-party synchronous replication for a
  DAG instead of continuous replication.

High availability

  A solution that provides service availability, data availability, and automatic recovery from
  failures that affect the service or data (such as a network, storage, or server failure).

Incremental deployment

  The ability to deploy high availability and site resilience after Exchange Server is installed.

<!-- p.2587 -->

Lagged mailbox database copy

  A passive mailbox database copy that has a log replay lag time greater than zero.

Mailbox database copy

  A mailbox database (.edb file and logs), which is either active or passive.

Mailbox resiliency

  The name of a unified high availability and site resilience solution in Exchange Server.

Managed availability

  A set of internal processes made up of probes, monitors, and responders that incorporate
  monitoring and high availability across all server roles and all protocols.

*over (pronounced "star over")

  Short for switchovers and failovers. A switchover is a manual activation of one or more
  database copies. A failover is an automatic activation of one or more database copies after
  a failure.

Safety Net

  Formerly known as transport dumpster, this is a feature of the transport service that stores
  a copy of all messages for X days. The default setting is 2 days.

Shadow redundancy

  A transport server feature that provides redundancy for messages for the entire time
  they're in transit.

Site resilience

  A configuration that extends the messaging infrastructure to multiple Active Directory sites
  to provide operational continuity for the messaging system in the event of a failure
  affecting one of the sites.

Database availability groups

<!-- p.2588 -->

A DAG is the base component of the high availability and site resilience framework built into
Exchange Server. A DAG is a group of up to 16 Exchange servers that hosts a set of databases
and provides automatic, database-level recovery from failures that affect individual databases,
networks, or servers. Any server in a DAG can host a copy of a mailbox database from any
other server in the DAG. When a server is added to a DAG, it works with the other servers in the
DAG to provide automatic recovery from failures that affect mailbox databases, such as a disk
failure or server failure. For more information about DAGs, see Database availability groups.

Mailbox database copies
The high availability and site resilience features used first introduced in Exchange 2010 are
used in Exchange Server to create and maintain database copies. Exchange Server also
leverages the concept of database mobility, which is Exchange-managed database-level
failovers.

Database mobility disconnects databases from servers and adds support for up to 16 copies of
a single database. It also provides a native experience for creating copies of a database.

Setting a database copy as the active mailbox database is known as a switchover. When a
failure affecting a database or access to a database occurs and a new database becomes the
active copy, this process is known as a failover. This process also refers to a server failure in
which one or more servers bring online the databases previously online on the failed server.
When either a switchover or failover occurs, other Exchange servers become aware of the
switchover almost immediately and redirect client and messaging traffic to the new active
database.

For example, if an active database in a DAG fails because of an underlying storage failure,
Active Manager will automatically recover by failing over to a database copy on another server
in the DAG. In Exchange Server, managed availability provides behaviors to recover from loss of
protocol access to a database, including recycling application worker pools, restarting services
and servers, and initiating database failovers.

For more information about mailbox database copies, see Mailbox database copies.

Active Manager
Exchange Server leverages Active Manager to manage the database and database copy health,
status, continuous replication, and other aspects of high availability. For more information
about Active Manager, see Active Manager.

Site resilience

<!-- p.2589 -->

In Exchange 2010, you could deploy a DAG across two datacenters and host the witness in a
third datacenter and enable failover for the Mailbox server role for either datacenter. But you
didn't get failover for the solution itself because the namespace still needed to be manually
changed for the non-Mailbox server roles.

In Exchange 2016 and Exchange 2019, the namespace doesn't need to move with the DAG.
Exchange leverages fault tolerance built into the namespace through multiple IP addresses,
load balancing (and if need be, the ability to take servers in and out of service). Modern HTTP
clients work with this redundancy automatically. The HTTP stack can accept multiple IP
addresses for a fully qualified domain name (FQDN), and if the first IP address it tries fails hard
(that is, it can't connect), it will try the next IP address in the list. In a soft failure (connection is
lost after the session is established, perhaps due to an intermittent failure in the service where,
for example, a device is dropping packets and needs to be taken out of service), the user might
need to refresh their browser.

This means the namespace is no longer a single point of failure as it was in Exchange 2010. In
Exchange 2010, perhaps the biggest single point of failure in the messaging system is the
FQDN that you give to users because it tells the user where to go. In the Exchange 2010
paradigm, changing where that FQDN goes isn't easy because you have to change DNS, and
then handle DNS latency, which in some parts of the world is challenging. And you have name
caches in browsers that are typically about 30 minutes or more that also have to be handled.

In Exchange Server, clients have more than one place to go. Almost all the client access
protocols in Exchange Server are HTTP based. Examples include Outlook, EAS, EWS, Outlook on
the web, and EAC). All supported HTTP clients have the ability to use multiple IP addresses,
thereby providing failover on the client side. You can configure DNS to hand multiple IP
addresses to a client during name resolution. The client asks for mail.contoso.com and gets
back two IP addresses, or four IP addresses, for example. However many IP addresses the client
gets back will be used reliably by the client. This makes the client a lot better off because if one
of the IP addresses fails, the client has one or more alternative IP addresses to try to connect
to. If a client tries one and it fails, it waits about 20 seconds and then tries the next one in the
list. Thus, if you lose the VIP for the Client Access service array, recovery for the clients happens
automatically, and in about 21 seconds.

The benefits include the following:

      In Exchange Server, if you lose the load balancer in your primary site, you simply turn it
      off (or maybe turn off the VIP) and repair or replace it. Clients that aren't already using
      the VIP in the secondary datacenter will automatically fail over to the secondary VIP
      without any change of namespace, and without any change in DNS. Not only does that
      mean you no longer have to perform a switchover, but it also means that all of the time
      normally associated with a datacenter switchover recovery isn't spent. In Exchange 2010,

<!-- p.2590 -->

      you had to handle DNS latency (hence, the recommendation to set the Time to Live (TTL)
      to 5 minutes, and the introduction of the failback URL). In Exchange 2016 and Exchange
      2019, you don't need to do that because you get fast failover (20 seconds) of the
      namespace between VIPs (datacenters).

      Because you can fail over the namespace between datacenters, all that's needed to
      achieve a datacenter failover is a mechanism for failover of the Mailbox server role across
      datacenters. To get automatic failover for the DAG, you simply architect a solution where
      the DAG is evenly split between two datacenters, and then place the witness server in a
      third location so that it can be arbitrated by DAG members in either datacenter,
      regardless of the state of the network between the datacenters that contain the DAG
      members. If you only have two datacenters and a third physical location isn't available,
      you can place the witness server on a Microsoft Azure virtual machine. See Using a
      Microsoft Azure VM as a DAG witness server for more information.

      In this scenario, the administrator's efforts are geared toward simply fixing the problem,
      and not spent restoring service. You simply fix the thing that failed; while service has been
      running and data integrity has been maintained. The urgency and stress level you feel
      when fixing a broken device is nothing like the urgency and stress you feel when you're
      working to restore service. It's better for the end user, and less stressful for the
      administrator.

You can allow failover to occur without having to perform switchbacks (sometimes mistakenly
referred to as failbacks). If you lose servers in your primary datacenter, resulting in a 20 second
interruption for clients, you might not even care about failing back. At this point, your primary
concern would be fixing the core issue (for example, replacing the failed load balancer). After
it's back online and functioning, some clients will start using it, and other clients might remain
operational through the second datacenter.

Exchange Server also provides functionality that enables administrators to deal with
intermittent failures. An intermittent failure is where, for example, the initial TCP connection can
be made, but nothing happens afterward. An intermittent failure requires some sort of extra
administrative action to be taken because it might be the result of a replacement device being
put into service. While this repair process is occurring, the device might be powered on and
accepting some requests, but not really ready to service clients until the necessary
configuration steps are performed. In this scenario, the administrator can perform a namespace
switchover by simply removing the VIP for the device being replaced from DNS. Then during
that service period, no clients will be trying to connect to it. After the replacement process has
completed, the administrator can add the VIP back to DNS, and clients will eventually start
using it.

<!-- p.2591 -->

For details about planning and deploying site resilience, see Plan for high availability and site
resilience and Deploying high availability and site resilience.

Third-party replication API
Exchange Server includes a third-party replication API that enables organizations to use third-
party synchronous replication solutions instead of the built-in continuous replication feature.
Microsoft supports third-party solutions that use this API, provided that the solution provides
the necessary functionality to replace all native continuous replication functionality that's
disabled as a result of using the API. Solutions are supported only when the API is used within
a DAG to manage and activate mailbox database copies. Use of the API outside of these
boundaries isn't supported. In addition, the solution must meet the applicable Windows
hardware support requirements. (Test validation isn't required for support.)

When deploying a solution that uses the built-in third-party replication API, be aware that the
solution vendor is responsible for primary support of the solution. Microsoft supports
Exchange data for both replicated and non-replicated solutions. Solutions that use data
replication must adhere to the Microsoft support policy for data replication. In addition,
solutions that utilize the Windows Failover Cluster resource model must meet Windows cluster
supportability requirements as described in Microsoft Knowledge Base article 943984, The
Microsoft Support Policy for Windows Server 2008 or Windows Server 2008 R2 Failover
Clusters    or The Microsoft Support Policy for Windows Server 2012 Failover Clusters              .

Microsoft's backup and restore support policy for deployments that use third-party replication
API-based solutions is the same as for native continuous replication deployments.

If you're a partner seeking information about the third-party API, contact your Microsoft
representative.

High availability and site resilience documentation
The following table contains links to topics that will help you learn about and manage DAGs,
mailbox database copies, and backup and restore for Exchange Server.

                                                                                         ﾉ   Expand table

 Topic                            Description

 Database availability groups     Learn about DAGs, Active Manager, Datacenter Activation Coordination
                                  (DAC) mode, and mailbox database copies.

 Plan for high availability and   Learn about the general, hardware, network, software, witness server, and

<!-- p.2592 -->

Topic                           Description

site resilience                 other requirements and best practices for DAGs.

Deploying high availability     Explore an example deployment scenario for deploying and configuring
and site resilience             DAGs.

Managing high availability      Learn about DAG management tasks, switchovers and failovers, and
and site resilience             maintenance mode.

Monitor database availability   Learn about the built-in cmdlets and scripts for monitoring DAGs and
groups                          database copies.

Backup, restore, and disaster   Learn about backing up and restoring Exchange databases, recovery
recovery                        databases, and server recovery.

<!-- p.2593 -->

Changes to high availability and site
resilience over previous versions of
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

Exchange Server 2013 and later uses DAGs and mailbox database copies (along with other
features such as single item recovery, retention policies, and lagged database copies) to
provide high availability, site resilience, and Exchange native data protection. The high
availability platform, Exchange Information Store, and Extensible Storage Engine (ESE) have all
been enhanced since Exchange 2010 to provide availability and less complex management, and
to reduce costs. These enhancements include:

      Reduction in IOPS: This enables you to use larger disks in terms of capacity and IOPS as
      efficiently as possible.

      Managed availability: With managed availability, internal monitoring and recovery-
      oriented features are tightly integrated to help prevent failures, proactively restore
      services, and start server failovers automatically or alert administrators to take action. The
      focus is on monitoring and managing the end-user experience rather than just server and
      component uptime to help keep the service continuously available.

      Managed Store: The Managed Store is the name of the rewritten Information Store
      processes in Exchange 2013 or later. The Managed Store is written in C# and tightly
      integrated with the Microsoft Exchange Replication service (MSExchangeRepl.exe) to
      provide higher availability through improved resiliency.

      Support for multiple databases per disk: Enhancements enable you to support multiple
      databases (mixtures of active and passive copies) on the same disk, thereby using larger
      disks in terms of capacity and IOPS as efficiently as possible.

      AutoReseed: Automatic reseeding capability enables you to quickly restore database
      redundancy after disk failure. If a disk fails, the database copy stored on that disk is
      copied from the active database copy to a spare disk on the same server. If multiple
      database copies were stored on the failed disk, they can all be automatically reseeded on
      a spare disk. This enables faster reseeds, as the active databases are likely to be on
      multiple servers and the data is copied in parallel.

      Automatic recovery from storage failures: This feature continues the innovation that was
      introduced in Exchange 2010 to allow the system to recover from failures that affect
      resiliency or redundancy. Exchange now includes more recovery behaviors for long I/O

<!-- p.2594 -->

     times, excessive memory consumption by MSExchangeRepl.exe, and severe cases where
     the system is in such a bad state that threads can't be scheduled.

     Lagged copy enhancements: Lagged copies can now care for themselves to a certain
     extent using automatic log play down. Lagged copies will automatically play down log
     files in various situations, such as page patching and low disk space scenarios. If the
     system detects that page patching is required for a lagged copy, the logs will be
     automatically replayed into the lagged copy to do page patching. Lagged copies will also
     invoke this auto replay feature when a low disk space threshold has been reached, and
     when the lagged copy has been detected as the only available copy for a specific period
     of time. In addition, lagged copies can use Safety Net, making recovery or activation
     much easier.

     Single copy alert enhancements: The single copy alert introduced in Exchange 2010 is no
     longer a separate scheduled script. It's now integrated into the managed availability
     components within the system and is a native function within Exchange.

     DAG network auto-configuration: DAG networks can be automatically configured by the
     system based on configuration settings. In addition to manual configuration options,
     DAGs can also distinguish between MAPI and replication networks and configure DAG
     networks automatically.

Reduction in IOPS
In Exchange 2010, passive database copies have a low checkpoint depth, that is required for
fast failover. In addition, the passive copy does aggressive pre-reading of data to keep up with
a 5 megabyte (MB) checkpoint depth. As a result of using a low checkpoint depth and doing
these aggressive pre-read operations, IOPS for a passive database copy is equal to IOPS for an
active copy in Exchange 2010.

In Exchange 2013 or later, the system can provide fast failover while using a high checkpoint
depth on the passive copy (100 MB). Because passive copies have 100-MB checkpoint depth,
they've been de-tuned to no longer be so aggressive. As a result of increasing the checkpoint
depth and de-tuning the aggressive pre-reads, IOPS for a passive copy are about 50 percent of
the active copy IOPS.

Having a higher checkpoint depth on the passive copy also results in other changes. On
failover in Exchange 2010, the database cache is flushed as the database is converted from a
passive copy to an active copy. Starting in Exchange 2013, ESE logging was rewritten so that
the cache is persisted through the transition from passive to active. Because ESE doesn't need
to flush the cache, you get fast failover.

<!-- p.2595 -->

One other change was made to the background database maintenance (BDM) process. BDM
now processes around 1-2 MB per second per copy.

As a result of these changes, Exchange now provides a significant reduction in IOPS over
Exchange 2010.

Managed Availability
Managed Availability is the integration of built-in, active monitoring, and the Exchange high
availability platform. With Managed Availability, the system can make a determination on when
to fail over a database based on service health. Managed Availability is an internal
infrastructure that's deployed in the Client Access (frontend) services and backend services on
Mailbox servers. Managed Availability includes three main asynchronous components that are
constantly doing work:

   1. The first component is the probe engine, that is responsible for taking measurements on
     the server and collecting data. The results of those measurements flow into the second
     component, the monitor.

   2. The monitor contains all of the business logic used by the system based on what is
     considered healthy on the data collected. Similar to a pattern recognition engine, the
     monitor looks for the various different patterns on all the collected measurements, and
     then it decides whether something is considered healthy.

   3. Finally, there's the responder engine, that is responsible for recovery actions.

When something is unhealthy, the first action is to attempt to recover that component. This
could include multi-stage recovery actions; for example:

   1. Restart the application pool.

   2. Restart the service.

   3. Restart the server.

   4. Take the server offline so that it no longer accepts traffic.

If the recovery actions are unsuccessful, the system escalates the issue to a human through
event log notifications.

Managed availability is implemented in the form of two services:

     Exchange Health Manager Service (MSExchangeHMHost.exe): This is a controller
     process that's used to manage worker processes. It's used to build, execute, and start and

<!-- p.2596 -->

     stop the worker process as needed. It's also used to recover the worker process in case
     that process crashes, to prevent the worker process from being a single point of failure.

     Exchange Health Manager Worker process (MSExchangeHMWorker.exe): This is the
     worker process that's responsible for doing the runtime tasks.

Managed availability uses persistent storage to do its functions:

     XML configuration files are used to initialize the work item definitions during startup of
     the worker process.

     The registry is used to store runtime data, such as bookmarks.

     The crimson channel event log infrastructure is used to store the work item results.

For more information about managed availability, see Managed availability.

Managed Store
Exchange 2010 and earlier versions support running a single instance of the Information Store
process (Store.exe) on the Mailbox server role. This single Store instance hosts all databases on
the server: active, passive, lagged, and recovery. In these Exchange architectures, there's little, if
any, isolation between the different databases hosted on a Mailbox server. An issue with a
single mailbox database has the potential to negatively affect all other databases, and crashes
resulting from a mailbox corruption can affect service for all users whose databases are hosted
on that server.

Another challenge with a single Store instance is the lack of processor scalability with the
Extensible Storage Engine (ESE). ESE scales well to 8-12 processor cores, but beyond that,
cross-processor communication and cache synchronization issues lead to negative
performance. Given today's servers with 16+ core systems available, this would impose the
administrative challenge of managing the affinity of 8-12 cores for ESE and using the other
cores for non-Store processes (for example, Assistants, Search Foundation, Managed
Availability, and so on). Moreover, the previous architecture restricted scale-up for the Store
process.

The Store.exe process has evolved considerably throughout the years as Exchange Server itself
evolved, but as a single process, ultimately its scalability is limited, and it represents a single
point of failure. Because of these limits, Store.exe was removed in Exchange 2013 and replaced
by the Managed Store.

For more information, see Managed Store.

<!-- p.2597 -->

Multiple databases per volume
Although the storage improvements in Exchange are designed primarily for just a bunch of
disks (JBOD) configurations, they're available for use by all supported storage configurations.
One such feature is the ability to host multiple databases on the same volume. This feature is
about Exchange optimizing for large disks. These optimizations result in a much more efficient
use of large disks in terms of capacity, IOPS, and reseed times, and they're meant to address
the challenges associated with running in a JBOD storage configuration:

     Database sizes must be manageable.

     Reseed operations must be fast and reliable.

     Although storage capacity is increasing, IOPS aren't.

     Disks hosting passive database copies are underutilized in terms of IOPS.

     Lagged copies have asymmetric storage requirements.

     Limited agility exists to recover from low disk space conditions.

The trend of increasing storage capacity continues. For example, the Exchange best practice
guideline for maximum database size (2 terabytes) on an 8-terabyte drive means you would
waste more than 5 terabytes of disk space.

A solution would be to grow the databases larger, but that inhibits manageability because it
might introduce long reseed times (including operationally unmanageable reseed times) and
compromised reliability of copying that amount of data over the network.

In addition, in the Exchange 2010 model, the disk storing a passive copy is underutilized in
terms of IOPS. In the case of a lagged passive copy, not only is the disk underutilized in terms
of IOPS, but it's also asymmetric in terms of its size, relative to the disks used to store the
active and non-lagged passive copies.

Exchange 2013 and later has been optimized to use large disks (8 terabytes) in a JBOD
configuration more efficiently. With multiple databases per disk, you can now have the same
size disks storing multiple database copies, including lagged copies. The goal is to drive the
distribution of users across the number of volumes that exist, providing you with a symmetric
design where during normal operations each DAG member hosts a combination of active,
passive, and optional lagged copies on the same volumes.

An example of a configuration that uses multiple databases per volume is illustrated below.

Configuration that uses multiple databases per volume

<!-- p.2598 -->

The configuration in the diagram provides a symmetrical design. All four servers have the same
four databases all hosted on a single disk per server. The key is that the number of copies of
each database that you have should be equal to the number of database copies per disk.

In the configuration in the diagram, there are four copies of each database: one active copy,
two passive copies, and one lagged copy. Because there are four copies of each database, the
proper configuration is one that has four copies per volume.

In addition, activation preference is configured so that it's balanced across the DAG and across
each server. For example:

     The active copy will have an activation preference value of 1.

     The first passive copy will have an activation preference value of 2.

     The second passive copy will have an activation preference value of 3.

     The lagged copy will have an activation preference value of 4.

In addition to having a better distribution of users across the existing volumes, another benefit
of using multiple databases per disk is a reduction in the amount of time to restore data
protection for failures that require a reseed (for example, disk failure).

As a database gets bigger, reseeding the database takes longer. For example, a 2-terabyte
database could take 23 hours to reseed, whereas an 8-terabyte database could take as long as
93 hours (almost 4 days). Both seeds would occur at about 20 MB per second. This generally
means that a very large database can't be seeded within an operationally reasonable amount
of time.

In the case of a single database copy per disk scenario, the seeding operation is effectively
source-bound, because it's always seeding the disk from a single source.

<!-- p.2599 -->

By dividing the volume into multiple database copies, and by having the active copy of the
passive databases on a specified volume stored on separate DAG members, the system is no
longer source bound in the context of reseeding the disk. When a failed disk is replaced, it can
be reseeded from multiple sources. This allows the system to reseed and restore data
protection for these databases in a much shorter amount of time.

When you use multiple databases per volume, we recommend that you follow these best
practices and requirements:

     A single logical disk partition per physical disk must be used. Don't create multiple
     partitions on the disk. Each database copy and its companion files (such as transaction
     logs and content index) should be hosted in a unique directory on the single partition.

     The number of database copies configured per volume should be equal to the number of
     copies of each database. For example, if you have four copies of your databases, you
     should use four database copies per volume.

     Database copies should have the same neighbors. (For example, they should all share the
     same disk on each server.)

     Activation preference across the DAG should be balanced, such that each database copy
     on a specified disk has a unique activation preference value.

AutoReseed
Automatic reseed (also known as AutoReseed) is the replacement for what is normally an
administrator-driven action in response to a disk failure, database corruption event, or other
issue that requires a reseed of a database copy. AutoReseed is designed to automatically
restore database redundancy after a disk failure by using spare disks that have been
provisioned on the system.

For more information, see AutoReseed. For detailed steps to configure AutoReseed, see
Configure AutoReseed for a database availability group.

Automatic recovery from storage failures
Automatic recovery from storage failures allows the system to recover from failures that affect
resiliency or redundancy. In addition to the bugcheck behaviors introduced in Exchange 2010,
Exchange now includes additional recovery behaviors for long I/O times, excessive memory
consumption by the Microsoft Exchange Replication service (MSExchangeRepl.exe), and severe
cases where threads can't be scheduled.

<!-- p.2600 -->

Even in JBOD environments, storage array controllers can have issues, such as crashing or
hanging. The following table lists features that provide hung I/O detection and recovery
features that provide enhanced resilience.

                                                                                             ﾉ    Expand table

 Name                Check                             Action                                       Threshold

 ESE Database        ESE checks for outstanding I/Os   Generates a failure item in the              240
 Hung IO                                               crimson channel to restart the server        seconds
 Detection

 Failure Item        Ensures failure items can be      Replication service heartbeats               30 seconds
 Channel             written to and read from          crimson channel and restart server
 Heartbeat           crimson channel                   on failures

 System Disk         Verifies server's system disk     Periodically sends unbuffered I/O to         120
 Heartbeat           state                             system disk; restarts server on              seconds
                                                       heartbeat time out

Exchange 2013 and later enhances server and storage resilience by including behaviors for
other serious conditions. These conditions and behaviors are described in the following table.

                                                                                             ﾉ    Expand table

 Name               Check                              Action                                     Threshold

 System bad         No threads, including non-         Restart the server                         302 seconds
 state              managed threads, can be
                    scheduled

 Long I/O times     I/O operation latency              Restart the server                         41 seconds
                    measurements

 Replication        Measure the working set of         1: Log event 4395 in the crimson           4 gigabyte
 service memory     MSExchangeRepl.exe                 channel with a service termination         (GB)
 use                                                   request
                                                       2: Initiate termination of
                                                       MSExchangeRepl.exe
                                                       3: If service termination fails, restart
                                                       the server

 System Event       Check for Event 129 in System      Restart the server                         When event
 129 (Bus reset)    event log                                                                     occurs

 Cluster database   Global Update Manager              Restart the server                         When event
 hang               updates are blocked                                                           occurs
