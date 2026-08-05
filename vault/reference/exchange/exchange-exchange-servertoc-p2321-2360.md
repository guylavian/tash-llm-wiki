---
title: "Exchange Server — pages 2321-2360"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2321-2360
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2321-2360
family: exchange
documentKind: "doc"
abstract: "Create a retention policy in Exchange Server Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition Learn how to use retention policies to manage an email lifecycle in Exchange 2016 and Exchange 2019. Retention policies are applied by creating retention tags, adding the"
---

# Exchange Server — pages 2321-2360

<!-- p.2321 -->

Create a retention policy in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Learn how to use retention policies to manage an email lifecycle in Exchange 2016 and
Exchange 2019. Retention policies are applied by creating retention tags, adding them to a
retention policy, and applying the policy to mailbox users.

What do you need to know before you begin?
      Estimated time to complete this task: 30 minutes.

      Procedures in this topic require specific permissions. See each procedure for its
      permissions information.

      Mailboxes to which you apply retention policies must reside on servers running Exchange
      Server 2010 or later.

Step 1: Create a retention tag
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Messaging records management" entry in the
Messaging policy and compliance permissions in Exchange Server topic.

Use the Exchange admin center (EAC) to create a retention tag

   1. Go to Compliance management > Retention tags, and click Add          .

   2. Select one of the following options:

            Applied automatically to entire mailbox (default): Creates a default policy tag
            (DPT). You can use DPTs to create a default deletion policy and a default archive
            policy, which applies to all items in the mailbox.

              ７ Note

              You can't use the EAC to create a DPT to delete voice mail items. For details
              about how to create a DPT to delete voice mail items, see the Exchange
              Management Shell example below.

<!-- p.2322 -->

       Applied automatically to a default folder: Creates a retention policy tag (RPT) for a
       default folder such as Inbox or Deleted Items.

          ７ Note

          You can only create RPTs with the Delete and allow recovery or Permanently
          delete actions.

       Applied by users to items and folders (personal): Creates personal tags. These tags
       allow Outlook and Outlook on the web users to apply archive or deletion settings to
       a message or folders that are different from the settings applied to the parent folder
       or the entire mailbox.

3. The New retention tag page title and options vary depending on the type of tag you
  select. Complete the following fields:

       Name: Enter a name for the retention tag. Retention tag names are displayed to
       users in Outlook and Outlook on the web along with the retention period.

       Apply this tag to the following default folder: Available only if you selected this
       option in Step 2.

       Retention action: Select one of the following actions to take after the item reaches
       its retention period:

       Delete and Allow Recovery: Deletes items but allow users to recover them using the
       Recover Deleted Items option in Outlook or Outlook on the web. Items are retained
       until the deleted item retention period configured for the mailbox database or the
       mailbox user is reached.

       Permanently Delete: Permanently deletes the item from the mailbox database.

          ） Important

          Mailboxes or items subject to In-Place Hold or litigation hold will be retained
          and returned in In-Place eDiscovery searches. To learn more, see In-Place Hold
          and Litigation Hold in Exchange Server.

       Move to Archive: Available only if you're creating a DPT or a personal tag. Select
       this action to move items to the user's In-Place Archive.

       Retention period: Select one of the following options:

<!-- p.2323 -->

            Never: Specifies that items should never be deleted or moved to the archive.

            When the item reaches the following age (in days): Specifies the number of days to
            retain items before they're moved or deleted. The retention age for all supported
            items except Calendar and Tasks is calculated from the date an item is received or
            created. Retention age for Calendar and Tasks items is calculated from the end date.

            Comment: Optional field used for administrative notes or comments. The field isn't
            displayed to users.

Use the Exchange Management Shell to create a retention tag

Use the New-RetentionPolicyTag cmdlet to create a retention tag. Different options available
in the cmdlet allow you to create different types of retention tags. Use the Type parameter to
create a DPT ( All ), RPT (specify a default folder type, such as Inbox ) or a personal tag
( Personal ).

This example creates a DPT to delete all messages in the mailbox after 7 years (2,556 days).

  PowerShell

  New-RetentionPolicyTag -Name "DPT-Corp-Delete" -Type All -AgeLimitForRetention
  2556 -RetentionAction DeleteAndAllowRecovery

This example creates a DPT to move all messages to the In-Place Archive in 2 years (730 days).

  PowerShell

  New-RetentionPolicyTag -Name "DPT-Corp-Move" -Type All -AgeLimitForRetention 730 -
  RetentionAction MoveToArchive

This example creates a DPT to delete voice mail messages after 20 days.

  PowerShell

  New-RetentionPolicyTag -Name "DPT-Corp-Voicemail" -Type All -MessageClass
  Voicemail -AgeLimitForRetention 20 -RetentionAction DeleteAndAllowRecovery

This example creates a RPT to permanently delete messages in the Junk EMail folder after 30
days.

  PowerShell

  New-RetentionPolicyTag -Name "RPT-Corp-JunkMail" -Type JunkEmail -

<!-- p.2324 -->

  AgeLimitForRetention 30 -RetentionAction PermanentlyDelete

This example creates a personal tag to never delete a message.

  PowerShell

  New-RetentionPolicyTag -Name "Never Delete" -Type Personal -RetentionAction
  DeleteAndAllowRecovery -RetentionEnabled $false

Step 2: Create a retention policy
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Messaging records management" entry in the
Messaging policy and compliance permissions in Exchange Server topic.

Use the EAC to create a retention policy

   1. Go to Compliance management > Retention policies, and click Add         .

   2. In New Retention Policy, complete the following fields:

           Name: Enter a name for the retention policy.

           Retention tags: Click Add     to select the tags you want to add to this retention
           policy.

           A retention policy can contain the following tags:

               One DPT with the Move to Archive action

               One DPT with the Delete and Allow Recovery or Permanently Delete actions

               One DPT for voice mail messages with the Delete and Allow Recovery or
               Permanently Delete actions

               One RPT per default folder such as Inbox to delete items

               Any number of personal tags

               ７ Note

               Although you can add any number of personal tags to a retention policy,
               having many personal tags with different retention settings can confuse users.
               We recommend linking no more than ten personal tags to a retention policy.

<!-- p.2325 -->

     You can create a retention policy without adding any retention tags to it, but items in the
     mailbox to which the policy is applied won't be moved or deleted. You can also add and
     remove retention tags from a retention policy after you create it.

Use the Exchange Management Shell to create a retention
policy
This example creates the retention policy RetentionPolicy-Corp and uses the
RetentionPolicyTagLinks parameter to associate five tags to the policy.

  PowerShell

  New-RetentionPolicy "RetentionPolicy-Corp" -RetentionPolicyTagLinks "DPT-Corp-
  Delete","DPT-Corp-Move","DPT-Corp-Voicemail","RPT-Corp-JunkMail","Never Delete"

For detailed syntax and parameter information, see New-RetentionPolicy.

Step 3: Apply a retention policy to mailbox users
After you create a retention policy, you must apply it to mailbox users. You can apply different
retention policies to different set of users. For detailed instructions, see Apply a retention
policy to mailboxes in Exchange Server.

How do you know this task worked?
After you create retention tags, add them to a retention policy, and apply the policy to a
mailbox user, the next time the MRM mailbox assistant processes the mailbox, messages are
moved or deleted based on settings you configured in the retention tags.

To verify that you have applied the retention policy, do the following:

   1. Run the following Exchange Management Shell command to run the MRM assistant
     manually against a single mailbox.

        PowerShell

        Start-ManagedFolderAssistant -Identity <mailbox identity>

   2. Log on to the mailbox using Outlook or Outlook on the web and verify that messages are
     deleted or moved to an archive in accordance with the policy configuration.

<!-- p.2326 -->

Retention tags and retention policies in
Exchange Server
04/30/2025

APPLIES TO:      2016      2019      Subscription Edition

Messaging records management (MRM) helps organizations to manage email lifecycle and
reduce legal risks associated with email and other communications. MRM makes it easier to
keep messages needed to comply with company policy, government regulations, or legal
needs, and to remove content that has no legal or business value.

Messaging records management strategy
MRM in Exchange Server is accomplished by using retention tags and retention policies. Before
discussing the details about each of these retention features, let's learn how the features are
used in the overall MRM strategy:

     Assigning retention policy tags (RPTs) to default folders, such as the Inbox and Deleted
     Items.

     Applying default policy tags (DPTs) to mailboxes to manage the retention of all untagged
     items.

     Allowing the user to assign personal tags to custom folders and individual items.

     Separating MRM functionality from users' Inbox management and filing habits. Users
     aren't required to file messages in managed folders based on retention requirements.
     Individual messages can have a different retention tag than the one applied to the folder
     in which they're located.

The following figure illustrates the tasks involved in implementing this strategy.

<!-- p.2327 -->

<!-- p.2328 -->

Retention tags
As you can see, retention tags are used to apply retention settings to folders and individual
items such as email messages and voice mail. These settings specify how long a message
remains in a mailbox and the action to take when the message reaches the specified retention
age. When a message reaches its retention age, it's moved to the user's In-Place Archive or
deleted.

Retention tags allow users to tag their own mailbox folders and individual items for retention.
Users no longer have to file items in managed folders provisioned by an administrator based
on message retention requirements.

<!-- p.2329 -->

Types of retention tags
Retention tags are classified into the following three types based on who can apply them and
where in a mailbox they can be applied.

                                                                                        ﾉ   Expand table

 Type of      Applied...                    Applied by...   Available     Details
 retention                                                  actions...
 tag

 Default      Automatically to entire       Administrator   Move to       Users can't change DPTs
 policy tag   mailbox                                       archive       applied to a mailbox.
 (DPT)        A DPT applies to                              Delete and
              untagged items, which are                     allow
              mailbox items that don't                      recovery
              have a retention tag
              applied directly or by                        Permanently
              inheritance from the                          delete
              folder.

 Retention    Automatically to a default    Administrator   Delete and    Users can't change the RPT
 policy tag   folder                                        allow         applied to a default folder.
 (RPT)        Default folders are folders                   recovery
              created automatically in                      Permanently
              all mailboxes, for example:                   delete
              Inbox, Deleted Items, and
              Sent Items. See the list of
              supported default folders
              in Default folders that
              support Retention Policy
              Tags.

 Personal     Manually to items and         Users           Move to       Personal tags allow your users
 tag          folders                                       archive       to determine how long an item
              Users can automate                            Delete and    should be retained. For
              tagging by using Inbox                        allow         example, the mailbox can have
              rules to either move a                        recovery      a DPT to delete items in seven
              message to a folder that                                    years, but a user can create an
              has a particular tag or to                    Permanently   exception for items such as
              apply a personal tag to                       delete        newsletters and automated
              the message.                                                notifications by applying a
                                                                          personal tag to delete them in
                                                                          three days.

More about personal tags

<!-- p.2330 -->

Personal tags are available to Outlook and Outlook on the web users as part of their retention
policy. In Outlook and Outlook on the web, personal tags with the Move to Archive action
appear as Archive Policy, and personal tags with the Delete and Allow Recovery or
Permanently Delete actions appear as Retention Policy, as shown here:

Users can apply personal tags to folders they create or to individual items. Messages that have
a personal tag applied are always processed based on the personal tag's settings. Users can
apply a personal tag to a message so that it's moved or deleted sooner or later than the
settings specified in the DPT or RPTs applied to that user's mailbox. You can also create
personal tags with retention disabled. This allows users to tag items so they're never moved to
an archive or never expire.

  ７ Note

  Users can apply archive policies to default folders, user-created folders or subfolders, and
  individual items. Users can apply a retention policy to user-created folders or subfolders

<!-- p.2331 -->

  and individual items (including subfolders and items in a default folder), but not to default
  folders.

Users can also use the Exchange admin center (EAC) to select additional personal tags that
aren't linked to their retention policy. The selected tags then become available in Outlook and
Outlook on the web. To enable users to select additional tags from the EAC, you must add the
MyRetentionPolicies Role to the user's role assignment policy. To learn more about role
assignment policies for users, see Understanding Management Role Assignment Policies. If you
allow users to select additional personal tags, all personal tags in your Exchange organization
become available to them.

  ７ Note

  Personal tags are a premium feature. Mailboxes with policies that contain these tags (or as
  a result of users adding the tags to their mailbox) require an Exchange Enterprise client
  access license (CAL).

Retention age
When you enable a retention tag, you must specify a retention age for the tag. This age
indicates the number of days to retain a message after it arrives in the user's mailbox.

The retention age for non-recurring items (such as email messages) is calculated differently
than items that have an end date or recurring items (such as meetings and tasks). To learn how
retention age is calculated for different types of items, see How retention age is calculated in
Exchange Server.

You can also create retention tags with retention disabled or disable tags after they're created.
Because messages that have a disabled tag applied aren't processed, no retention action is
taken. As a result, users can use a disabled personal tag as a Never Move tag or a Never
Delete tag to override a DPT or RPT that would otherwise apply to the message.

Retention actions
When creating or configuring a retention tag, you can select one of the following retention
actions to be taken when an item reaches its retention age:

                                                                                 ﾉ   Expand table

<!-- p.2332 -->

 Retention         Action taken...                          Except...
 action

 Move to           Moves the message to the user's          If the user doesn't have an archive mailbox, no
 archive           archive mailbox                          action is taken.
                   Only available for DPTs and personal
                   tags

                   For details about archiving, see In-
                   Place Archiving in Exchange Server.

 Delete and        Emulates the behavior when the user      If you've set the deleted item retention period
 allow             empties the Deleted Items folder.        to zero days, items are permanently deleted. For
 recovery:         Items are moved to the Recoverable       details, see Configure Deleted Item retention
                   Items folder in Exchange Server in       and Recoverable Items quotas.
                   the mailbox and preserved until the
                   deleted item retention period.

                   Provides the user a second chance to
                   recover the item using the Recover
                   Deleted Items dialog box in Outlook
                   or Outlook on the web

 Permanently       Permanently deletes messages.            If mailbox is placed on In-Place Hold and
 delete            You can't recover messages after         Litigation Hold in Exchange Server or Litigation
                   they're permanently deleted.             Hold, items are preserved in the Recoverable
                                                            Items folder based on hold parameters. In-Place
                                                            eDiscovery in Exchange Server will still return
                                                            these items in search results.

 Mark as past      Marks a message as expired. In           N. A.
 retention limit   Outlook, and Outlook on the web,
                   expired items are displayed with the
                   notification stating 'This item has
                   expired' and 'This item will expire in
                   0 days'.

  ７ Note

  Default Policy tag (DPT) with Move to Archive action always overwrites the Retention
  Policy tag (RPT) or the Personal tag (PT), when the age limit for retention of DPT is lower
  than RPT or PT.

For details about how to create retention tags, see Create a retention policy in Exchange
Server.

<!-- p.2333 -->

Retention policies
To apply one or more retention tags to a mailbox, you need to add them to a retention policy
and then apply the policy to mailboxes. A mailbox can't have more than one retention policy.
Retention tags can be linked to or unlinked from a retention policy at any time, and the
changes automatically take effect for all mailboxes that have the policy applied.

A retention policy can have the following retention tags:

                                                                                        ﾉ   Expand table

 Retention tag type   Tags in a policy

 Default policy tag   One DPT with the Move to archive action
 (DPT)
                      One DPT with the Delete and allow Recovery or Permanently delete actions

                      One DPT for voice mail messages with the Delete and allow recovery or
                      Permanently delete action

 Retention policy     One RPT for each supported default folder
 tags (RPTs)          Note: You can't link more than one RPT for a particular default folder (such as
                      Deleted Items) to the same retention policy.

 Personal tags        Any number of personal tags
                      Note: Many personal tags in a policy can confuse users. We recommend adding no
                      more than 10 personal tags to a retention policy.

  ７ Note

  Although a retention policy doesn't need to have any retention tags linked to it, we don't
  recommend using this scenario. If mailboxes with retention policies don't have retention
  tags linked to them, this may cause mailbox items to never expire.

A retention policy can contain both archive tags (tags that move items to the personal archive
mailbox) and deletion tags (tags that delete items). A mailbox item can also have both types of
tags applied. Archive mailboxes don't have a separate retention policy. The same retention
policy is applied to the primary and archive mailbox.

When planning to create retention policies, you must consider whether they'll include both
archive and deletion tags. As mentioned earlier, a retention policy can have one DPT that uses
the Move to archive action and one DPT that uses either the Delete and allow recovery or
Permanently delete action. The DPT with the Move to archive action must have a lower
retention age than the DPT with a deletion action. For example, you can use a DPT with the
Move to archive action to move items to the archive mailbox in two years, and a DPT with a

<!-- p.2334 -->

deletion action to remove items from the mailbox in seven years. Items in both primary and
archive mailboxes will be deleted after seven years.

Default retention policy
Exchange Setup creates the retention policy Default MRM Policy. The policy is applied
automatically if you create an archive for the new user and don't specify a retention policy

You can modify tags included in the Default MRM Policy, for example by changing the
retention age or retention action, disable a tag or modify the policy by adding or removing
tags from it. The updated policy is applied to mailboxes the next time they're processed by the
Managed Folder Assistant (MFA).

For more details, including a list of retention tags linked to the policy, see Default Retention
Policy.

Managed Folder Assistant
The Managed Folder Assistant, a mailbox assistant that runs on Mailbox servers, processes
mailboxes that have a retention policy applied.

The Managed Folder Assistant applies the retention policy by inspecting items in the mailbox
and determining whether they're subject to retention. It then stamps items subject to retention
with the appropriate retention tags and takes the specified retention action on items past their
retention age.

The Managed Folder Assistant is a throttle-based assistant. Throttle-based assistants are always
running and don't need to be scheduled. The system resources they can consume are throttled.
You can configure the Managed Folder Assistant to process all mailboxes on a Mailbox server
within a certain period (known as a work cycle). Additionally, at a specified interval (known as
the work cycle checkpoint), the assistant refreshes the list of mailboxes to be processed. During
the refresh, the assistant adds newly created or moved mailboxes to the queue. It also
reprioritizes existing mailboxes that haven't been processed successfully due to failures and
moves them higher in the queue so they can be processed during the same work cycle.

You can also use the Start-ManagedFolderAssistant cmdlet to manually trigger the assistant to
process a specified mailbox. To learn more, see Configure and run the Managed Folder
Assistant in Exchange Server.

  ７ Note

<!-- p.2335 -->

  The Managed Folder Assistant doesn't take any action on messages that aren't subject to
  retention, specified by disabling the retention tag. You can also disable a retention tag to
  temporarily suspend items with that tag from being processed.

Moving items between folders
A mailbox item moved from one folder to another inherits any tags applied to the folder to
which it's moved. If an item is moved to a folder that doesn't have a tag assigned, the DPT is
applied to it. If the item has a tag explicitly assigned to it, the tag always takes precedence over
any folder-level tags or the default tag.

Applying a retention tag to a folder in the archive
When the user applies a personal tag to a folder in the archive, if a folder with the same name
exists in the primary mailbox and has a different tag, the tag on that folder in the archive
changes to match the one in the primary mailbox. This is by design to avoid any confusion
about items in a folder in the archive having a different expiry behavior than the same folder in
the user's primary mailbox. For example, the user has a folder named Project Contoso in the
primary mailbox with a Delete - 3 years tag and a Project Contoso folder also exists in the
archive mailbox. If the user applies a Delete - 1 year personal tag to delete items in the folder
after 1 year. When the mailbox is processed again, the folder reverts to the Delete - 3 Years tag.

Removing or deleting a retention tag from a retention policy
When a retention tag is removed from the retention policy applied to a mailbox, the tag is no
longer available to the user and can't be applied to items in the mailbox.

Existing items that have been stamped with that tag continue to be processed by the Managed
Folder Assistant based on those settings and any retention action specified in the tag is applied
to those messages.

However, if you delete the tag, the tag definition stored in Active Directory is removed. This
causes the Managed Folder Assistant to process all items in a mailbox and restamp the ones
that have the removed tag applied. Depending on the number of mailboxes and messages, this
process may significantly consume resources on all Mailbox servers that contain mailboxes with
retention policies that include the removed tag.

  ） Important

<!-- p.2336 -->

  If a retention tag is removed from a retention policy, any existing mailbox items with the
  tag applied will continue to expire based on the tag's settings. To prevent the tag's
  settings from being applied to any items, you should delete the tag. Deleting a tag
  removes it from any retention policies where it's included.

Disabling a retention tag
If you disable a retention tag, the Managed Folder Assistant ignores items that have that tag
applied. Items that have a retention tag for which retention is disabled are either never moved
or never deleted, depending on the specified retention action. Because these items are still
considered tagged items, the DPT doesn't apply to them. For example, if you want to
troubleshoot retention tag settings, you can temporarily disable a retention tag to stop the
Managed Folder Assistant from processing messages with that tag.

  ７ Note

  The retention period for a disabled retention tag is displayed to the user as Never. If a
  user tags an item believing it will never be deleted, enabling the tag later may result in
  unintentional deletion of items the user didn't want to delete. The same is true for tags
  with the Move to archive action.

Retention hold
When users are temporarily away from work and don't have access to their email, retention
settings can be applied to new messages before they return to work or access their email.
Depending on the retention policy, messages may be deleted or moved to the user's personal
archive. You can temporarily suspend retention policies from processing a mailbox for a
specified period by placing the mailbox on retention hold. When you place a mailbox on
retention hold, you can also specify a retention comment that informs the mailbox user (or
another user authorized to access the mailbox) about the retention hold, including when the
hold is scheduled to begin and end. Retention comments are displayed in supported Outlook
clients. You can also localize the retention hold comment in the user's preferred language.

  ７ Note

  Placing a mailbox on retention hold doesn't affect how mailbox storage quotas are
  processed. Depending on the mailbox usage and applicable mailbox quotas, consider
  temporarily increasing the mailbox storage quota for users when they're on vacation or

<!-- p.2337 -->

  don't have access to email for an extended period. For more information about mailbox
  storage quotas, see Configure storage quotas for a mailbox.

During long absences from work, users may accrue a large amount of email. Depending on the
volume of email and the length of absence, it may take these users several weeks to sort
through their messages. In these cases, consider the additional time it may take the users to
catch up on their mail before removing them from retention hold.

If your organization has never implemented MRM, and your users aren't familiar with its
features, you can also use retention holds during the initial warm-up and training phase of your
MRM deployment. You can create and deploy retention policies and educate users about the
policies without the risk of having items moved or deleted before users can tag them. A few
days before the warm-up and training period ends, you should remind users of the warm-up
deadline. After the deadline, you can remove the retention hold from user mailboxes, allowing
the Managed Folder Assistant to process mailbox items and take the specified retention action.

If you are using Exchange hybrid, note the following behavior: When a retention hold is
configured in Microsoft 365, the GUID for this hold is written to the msExchUserHoldPolicies
attribute of the user object to which the hold applies. This attribute is then synchronized back
to the on-premises Active Directory. When MFA processes the mailbox for elements that can
be purged, it encounters the msExchUserHoldPolicies attribute. However, it cannot retrieve the
details of the configured hold because they are not available within the Exchange Server on-
premises organization. To prevent the deletion of data that might need to be preserved, MFA
skips purging these items from the DiscoveryHolds folder in the mailbox. Over time, this folder
becomes full and causes the Recoverable Items folder to reach its quota. You can find steps to
resolve this behavior and configuration recommendations in Recoverable Items folder not
emptied for mailbox on litigation or retention hold support article.

<!-- p.2338 -->

Apply a retention policy to mailboxes in
Exchange Server
Article • 04/30/2025

APPLIES TO:         2016       2019   Subscription Edition

You can use retention policies to group one or more retention tags and apply them to
mailboxes to enforce message retention settings. A mailbox can't have more than one
retention policy.

  Ｕ Caution

  Messages are expired based on settings defined in the retention tags linked to the policy.
  These settings include actions such moving messages to the archive or permanently
  deleting them. Before applying a retention policy to one or more mailboxes, we
  recommended that you test the policy and inspect each retention tag associated with it.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Applying retention policies" entry
      in the Messaging policy and compliance permissions in Exchange Server topic.

Use the Exchange admin center to apply a
retention policy to a single mailbox
   1. Go to Recipients > Mailboxes.

   2. In the list view, select the mailbox to which you want to apply the retention policy, and
      then click Edit      .

   3. In User Mailbox, click Mailbox features.

   4. In the Retention policy list, select the policy you want to apply to the mailbox, and then
      click Save.

<!-- p.2339 -->

Use the Exchange admin center to apply a
retention policy to multiple mailboxes
   1. Go to Recipients > Mailboxes.

   2. In the list view, use the Shift or Ctrl keys to select multiple mailboxes.

   3. In the details pane, click More options.

   4. Under Retention Policy, click Update.

   5. In Bulk Assign Retention Policy, select the retention policy you want to apply to the
     mailboxes, and then click Save.

Use the Exchange Management Shell to apply a
retention policy to a single mailbox
This example applies the retention policy RP-Finance to Morris's mailbox.

  PowerShell

  Set-Mailbox "Morris" -RetentionPolicy "RP-Finance"

For detailed syntax and parameter information, see Set-Mailbox.

Use the Exchange Management Shell to apply a
retention policy to multiple mailboxes
This example applies the new retention policy New-Retention-Policy to all mailboxes that have
the old policy Old-Retention-Policy.

  PowerShell

  $OldPolicy=(Get-RetentionPolicy "Old-Retention-Policy").distinguishedName
  Get-Mailbox -Filter "RetentionPolicy -eq '$OldPolicy'" -Resultsize Unlimited |
  Set-Mailbox -RetentionPolicy "New-Retention-Policy"

This example applies the retention policy RetentionPolicy-Corp to all mailboxes in the
Exchange organization.

  PowerShell

<!-- p.2340 -->

  Get-Mailbox -ResultSize unlimited | Set-Mailbox -RetentionPolicy "RetentionPolicy-
  Corp"
  ```PowerShell

  This example applies the retention policy RetentionPolicy-Finance to all mailboxes
  in the Finance organizational unit.

  ```PowerShell
  Get-Mailbox -OrganizationalUnit "Finance" -ResultSize Unlimited | Set-Mailbox -
  RetentionPolicy "RetentionPolicy-Finance"

For detailed syntax and parameter information, see Get-Mailbox and Set-Mailbox.

How do you know this worked?
To verify that you have applied the retention policy, run the Get-Mailbox cmdlet to retrieve the
retention policy for the mailbox or mailboxes.

This example retrieves the retention policy for Morris's mailbox.

  PowerShell

  Get-Mailbox Morris | Select RetentionPolicy

This command retrieves all mailboxes that have the retention policy RP-Finance applied.

  PowerShell

  Get-Mailbox -ResultSize unlimited | Where-Object {$_.RetentionPolicy -eq "RP-
  Finance"} | Format-Table Name,RetentionPolicy -Auto

<!-- p.2341 -->

Configure and run the Managed Folder
Assistant in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

The Managed Folder Assistant (MFA) is an Exchange Mailbox Assistant that applies and
processes the message retention settings that are configured in retention policies.

As in Exchange 2013, the Managed Folder Assistant in Exchange 2016 and Exchange 2019 is a
throttle-based assistant that's always running. The MFA doesn't need to be scheduled, and the
system resources that are consumed by the MFA can be throttled. You can configure the
Managed Folder Assistant to process all mailboxes on a Mailbox server within a certain time
period that's known as a work cycle. By default, the work cycle for the MFA is one day (all
mailboxes on the server are processed by the MFA every day).

You can also force the MFA to immediately process a specified mailbox.

What do you need to know before you begin?
      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      Although the ManagedFolderAssistantSchedule parameter is available in Exchange Server,
      it doesn't work on Exchange 2016 or Exchange 2019 servers. It's only used for coexistence
      with previous versions of Exchange.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Messaging records
      management" entry in the Messaging policy and compliance permissions in Exchange
      Server topic.

Configure the Managed Folder Assistant
Configuring the interval for when the MFA processes mailboxes is a two-step process:

   1. Configure the work cycle for the MFA.

   2. Apply the new work cycle value for the MFA.

<!-- p.2342 -->

Step 1: Use the Exchange Management Shell to configure the
work cycle for the Managed Folder Assistant
To configure the work cycle for the MFA, use this syntax:

  PowerShell

  New-SettingOverride -Name "<UniqueOverrideName>" -Component TimeBasedAssistants -
  Section ELCAssistant -Parameters @("WorkCycle=<Timespan>") -Reason "
  <DescriptiveReason>" [-Server <ServerName>]

Notes:

     To specify a <TimeSpan> value, use the syntax d.hh:mm:ss , where d = days, hh = hours,
     mm = minutes, and ss = seconds.

     To configure the same work cycle for the MFA on all Exchange 2016 and Exchange 2019
     Mailbox servers in the Active Directory forest, don't use the Server parameter.

     To configure the work cycle for the MFA on a specific Exchange 2016 and Exchange 2019
     Mailbox server, use the Server parameter and the name (not the fully qualified domain
     name or FQDN) of the server. This method is useful when you need to specify different
     work cycle values for the MFA on different Exchange servers.

This example configures the work cycle for the MFA to two days (the MFA processes mailboxes
every two days). Because we aren't using the Server parameter, the setting is applied to all
Exchange 2016 and Exchange 2019 Mailbox servers in the organization.

     Setting override name: "MFA WorkCycle Override" (must be unique)

     WorkCycle: 2.00:00:00 (2 days; note the value 2 also works)

     Override reason: Process mailboxes every 2 days

  PowerShell

  New-SettingOverride -Name "MFA WorkCycle Override" -Component TimeBasedAssistants
  -Section ELCAssistant -Parameters @("WorkCycle=2.00:00:00") -Reason "Process
  mailboxes every 2 days"

This example specifies the same 2 day work cycle for the MFA, but only on the server named
Mailbox01.

  PowerShell

<!-- p.2343 -->

  New-SettingOverride -Name "Mailbox01 MFA WorkCycle Override" -Component
  TimeBasedAssistants -Section ELCAssistant -Parameters @("WorkCycle=2.00:00:00") -
  Reason "Process mailboxes every 2 days" -Server Mailbox01

Step 2: Use the Exchange Management Shell to apply the new
the work cycle value for the Managed Folder Assistant
To apply the new the work cycle value for the MFA, use this syntax:

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh [-Server <ServerName>]

Notes:

     If you didn't use the Server parameter in Step 1, don't use it here. If you used the Server
     parameter in Step 1, use the same server name here.

     If you delete the custom work cycle value for the MFA by using the Remove-
     SettingOverride cmdlet, you still need to run this command to change the work cycle
     back to the default value of one day.

This example applies the new work cycle value for the MFA on all Exchange 2016 and Exchange
2019 Mailbox servers in the organization.

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh

This example applies the new work cycle value for the MFA on the server named Mailbox01.

  PowerShell

  Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
  Component VariantConfiguration -Argument Refresh -Server Mailbox01

How do you know this worked?
To verify that you've successfully configured the work cycle for the Managed Folder Assistant
on one or more servers, replace <ServerName> with the name of the server (not the FQDN),

<!-- p.2344 -->

and run the following command to verify the value of the WorkCycle property:

  PowerShell

  [xml]$diag=Get-ExchangeDiagnosticInfo -Server <ServerName> -Process
  MSExchangeMailboxAssistants -Component VariantConfiguration -Argument
  "Config,Component=TimeBasedAssistants"
  $diag.Diagnostics.Components.VariantConfiguration.Configuration.TimeBasedAssistant
  s.ElcAssistant

Use the Exchange Management Shell to start the
Managed Folder Assistant on a specific mailbox
To trigger the MFA to immediately process a mailbox, use this syntax:

  PowerShell

  Start-ManagedFolderAssistant -Identity <MailboxIdentity>

This example triggers the Managed Folder Assistant to immediately process Morris Cornejo's
mailbox.

  PowerShell

  Start-ManagedFolderAssistant -Identity morris.cornejo@contoso.com

For detailed syntax and parameter information, see Start-ManagedFolderAssistant.

<!-- p.2345 -->

How to use administrator audit logging in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

You can use administrator audit logging in Exchange Server to log when a user or administrator
makes a change in your organization. By keeping a log of the changes, you can trace changes
to the person who made the change, augment your change logs with detailed records of the
change as it was implemented, comply with regulatory requirements and requests for
discovery, and more.

By default, administrator audit logging is enabled in new installations of Exchange Server.

What gets audited
Cmdlets that are run directly in the Exchange Management Shell are audited. In addition,
operations performed using the Exchange admin center (EAC) are also logged because those
operations run cmdlets in the background.

Cmdlets, regardless of where they're run, are audited if a cmdlet is on the cmdlet auditing list
and one or more parameters on that cmdlet are on the parameter auditing list. Audit logging is
intended to show what actions have been taken to modify objects in an Exchange organization
rather than what objects have been viewed.

Notes:

      A cmdlet might not be logged if an error occurs before the cmdlet calls the Admin Audit
      Log cmdlet extension agent. If an error occurs after the Admin Audit Log agent is called,
      the cmdlet is logged along with the associated error. For more information, see the
      Admin Audit Log agent section later in this topic.

      Changes to the audit log configuration are refreshed every 60 minutes on computers that
      have the Exchange Management Shell open at the time a configuration change is made. If
      you want to apply the changes immediately, close and then open the Exchange
      Management Shell again on each computer.

      A command may take up to 15 minutes after it's run to appear in audit log search results.
      This is because audit log entries must be indexed before they can be searched. If a
      command doesn't appear in the administrator audit log, wait a few minutes and run the
      search again.

<!-- p.2346 -->

Admin audit logging configuration
By default, when admin audit logging is enabled, a log entry is created every time any cmdlet is
run. If you don't want to audit every cmdlet that's run, you can configure audit logging to audit
only the cmdlets and parameters you're interested in. You configure audit logging with the Set-
AdminAuditLogConfig cmdlet. The parameters referenced in the following sections are used
with this cmdlet.

  ） Important

  Changes to the administrator audit log configuration are always logged, regardless of
  whether the Set-AdminAuditLogConfig cmdlet is included in the list of cmdlets being
  audited or whether audit logging is enabled or disabled.

When a command is run, Exchange inspects the cmdlet that was used. If the cmdlet that was
run matches any of the cmdlets provided with the AdminAuditLogCmdlets parameter, Exchange
then checks the parameters specified in the AdminAuditLogParameters parameter. If at least
one or more parameters from the parameters list are matched, Exchange logs the cmdlet that
was run. The following sections contain more information about each aspect of the audit
logging configuration.

For more information about managing audit logging configuration, see Manage administrator
audit logging.

Cmdlets
You can control which cmdlets are audited by providing a list of cmdlets, and their parameters,
that you want to log. When you configure audit logging, you can specify to audit every cmdlet,
or you can specify the cmdlets you want to audit by using the AdminAuditLogCmdlets
parameter. You can specify full cmdlet names, such as New-Mailbox, or you can specify partial
cmdlet names and enclose those names in wildcard characters, such as an asterisk ( * ). For
example, if you want to log when any cmdlet that contains the string Transport runs, you can
specify a value of *Transport* . You can use a mix of full cmdlet names and partial cmdlet
names at the same time to tailor the audit logging configuration to your needs.

To audit all cmdlets, specify only the wildcard character (*). This is the default setting.

Parameters
In addition to specifying which cmdlets you want to log, you can also indicate that cmdlets
should only be logged if certain parameters on those cmdlets are used. Use the

<!-- p.2347 -->

AdminAuditLogParameters parameter to specify which parameters should be logged. As with
cmdlets, you can specify full parameter names, such as Database , or partial parameter names
enclosed in wildcard characters ( * ), such as *Address* , or a combination of both.

To audit all parameters, specify only the wildcard character (*). This is the default setting.

Admin audit log age limit
By default, admin audit logging is configured to store audit log entries for 90 days. After 90
days, the audit log entry is deleted. You can change the audit log age limit using the
AdminAuditLogAgeLimit parameter. For example, to change the age limit to 180 days, use the
command Set-AdminAuditLogConfig -AdminAuditLogAgeLimit 180 . You can also specify the
number of days, hours, minutes, and seconds that audit log entries should be kept. To specify a
value, use the format dd.hh:mm:ss where the following applies:

     dd: The number of days to keep the audit log entry.

     hh: The number of hours to keep the audit log entry.

     mm: The number of minutes to keep the audit log entry.

     ss: The number of seconds to keep the audit log entry.

You need to specify multiple years by using the dd field. For example, 365 days equals one
year; 730 days equals two years; 913 days equals two years and six months. For example, to set
the audit log age limit to two years and six months, use the value 913 .

Notes:

     You can set the admin audit log age limit to a value that's less than the current age limit.
     If you do this, any audit log entry whose age exceeds the new age limit is deleted.

     If you set the age limit to 0, Exchange deletes all the entries in the audit log.

     We recommend that you assign permissions to configure the audit log age limit only to
     highly trusted users.

Verbose logging
By default, the admin audit log records only the cmdlet name, cmdlet parameters (and values
specified), the object that was modified, who ran the cmdlet, when the cmdlet was run, and on
what server the cmdlet was run. The admin audit log doesn't log what properties were
modified on the object. If you want the admin audit log to also include the properties of the
object that were modified, you can enable verbose logging by setting the LogLevel parameter

<!-- p.2348 -->

to Verbose . When you enable verbose logging, in addition to the information logged by
default, the properties modified on an object, including their old and new values, are included
in the admin audit log.

Test cmdlets
Cmdlets that begin with the verb Test aren't logged by default. You can indicate that Test
cmdlets should be logged by setting the TestCmdletLoggingEnabled parameter to $true .
Although you can enable logging of test cmdlets, we recommend that you do this only for
short periods of time because test cmdlets can produce a large number of audit log entries.

Admin audit log
Each time a cmdlet is logged, an admin audit log entry is created. The audit log entries are
stored in the admin audit log, which is stored in a hidden, dedicated arbitration mailbox that
can only be accessed by using the EAC, the Search-AdminAuditLog cmdlet, or the New-
AdminAuditLogSearch cmdlet. The following sections provide information about:

     What's included in the admin audit log.

     Reports available on the EAC Auditing page.

     Admin audit log search cmdlets.

Audit log contents
Each audit log entry contains the information described in the following table. The audit log
contains one or more audit log entries. The number of audit log entries is controlled by the
audit log age limit specified using the Set-AdminAuditLogConfig -AdminAuditLogAgeLimit
command. Any audit log entry that exceeds the age limit is deleted.

Audit log entry fields

                                                                                        ﾉ   Expand table

 Field               Description

 RunspaceId          This field is used internally by Exchange.

 ObjectModified      This field contains the object that was modified by the cmdlet specified in the
                     CmdletName field.

<!-- p.2349 -->

 Field                Description

 CmdletName           This field contains the name of the cmdlet that was run by the user in the Caller
                      field.

 CmdletParameters     This field contains the parameters that were specified when the cmdlet in the
                      CmdletName field was run. Also stored in this field, but not visible in the default
                      output, is the value specified with the parameter, if any.

 ModifiedProperties   This field contains the properties that were modified on the object in the
                      ObjectModified field. Also stored in this field, but not visible in the default output,
                      are the old value of the property and the new value that was stored.
                      Important: This field is only populated if the LogLevel parameter on the Set-
                      AdminAuditLogConfig cmdlet is set to verbose .

 Caller               This field contains the user account of the user who ran the cmdlet in the
                      CmdletName field.

 Succeeded            This field specifies whether the cmdlet in the CmdletName field ran successfully. The
                      value is either True or False .

 Error                This field contains the error message generated if the cmdlet in the CmdletName
                      field failed to complete successfully.

 RunDate              This field contains the date and time when the cmdlet in the CmdletName field was
                      run. The date and time are stored in Coordinated Universal Time (UTC) format.

 OriginatingServer    This field indicates the server on which the cmdlet specified in the CmdletName field
                      was run.

 Identity             This field is used internally by Exchange.

 IsValid              This field is used internally by Exchange.

 ObjectState          This field is used internally by Exchange.

EAC auditing reports
The Auditing page in the EAC has several reports that provide information about various types
of compliance and administrative configuration changes. The following reports provide
information about configuration changes in your organization:

     Administrator role group report: This report enables you to search for changes to
     management role groups that you specify within a specified timeframe. The results that
     are returned include the role groups that have been changed, who changed them and
     when, and what changes were made. A maximum of 3,000 entries can be returned. If your
     search might return more than 3,000 entries, use the Administrator audit log report or
     the Search-AdminAuditLog cmdlet.

<!-- p.2350 -->

     Admin audit log report: This report enables you to view entries in the admin audit log
     recorded within a specified time frame. You can also export admin audit log entries to a
     XML file and then send the file via email to a recipient you specify. For more information
     about the contents of the XML file, see Administrator audit log structure.

For information about how to use these reports, see Search the role group changes or
administrator audit logs.

Search-AdminAuditLog cmdlet
When you run the Search-AdminAuditLog cmdlet, all the audit log entries that match your
search criteria are returned. You can specify the following search criteria:

     Cmdlets: Specifies the cmdlets you want to search for in the admin audit log.

     Parameters: Specifies the parameters, separated by commas, you want to search for in
     the admin audit log. You can only search for parameters if you specify a cmdlet to search
     for.

     End date: Scopes the admin audit log results to log entries that occurred on or before the
     specified date.

     Start date: Scopes the admin audit log results to log entries that occurred on or after the
     specified date.

     Object IDs: Specifies that only admin audit log entries that contain the specified changed
     objects should be returned

     User IDs: Specifies that only the admin audit log entries that contain the specified IDs of
     the user who ran the cmdlet should be returned.

     Successful completion: Specifies whether only admin audit log entries that indicated a
     success or failure should be returned.

Each audit log entry contains the information described in the table in Audit log contents. By
default, only the first 1,000 log entries that match the search criteria are returned. However,
you can override this default and return more or fewer entries using the ResultSize parameter.
You can specify a value of Unlimited with the ResultSize parameter to return all log entries that
match the specified criteria.

For information about how to use the Search-AdminAuditLog cmdlet, see Search the role
group changes or administrator audit logs.

New-AdminAuditLogSearch cmdlet

<!-- p.2351 -->

The New-AdminAuditLogSearch cmdlet searches the admin audit log just like the Search-
AdminAuditLog cmdlet. However, instead of displaying the results of the search in the
Exchange Management Shell, the New-AdminAuditLogSearch cmdlet performs the search and
then sends the results to a recipient you specify via an email message. The results are included
as an XML attachment to the email message.

You can use the same search criteria with the New-AdminAuditLogSearch cmdlet that's used
on the Search-AdminAuditLog cmdlet. For a list of the search criteria, see Search-
AdminAuditLog cmdlet.

After you run the New-AdminAuditLogSearch cmdlet, Exchange may take up to 15 minutes to
deliver the report to the specified recipient. The XML file attached report can be a maximum of
10 MB. The XML file contains the same information described in the table in Audit log contents.
For more information about the structure of the XML file, see Administrator audit log structure.

  ７ Note

  Outlook Web App doesn't allow you to open XML attachments by default. You can either
  configure Exchange to allow XML attachments to be viewed using Outlook Web App, or
  you can use another email client, such as Microsoft Outlook, to view the attachment. For
  information about how to configure Outlook Web App to allow you to view an XML
  attachment, see View or configure Outlook on the web virtual directories in Exchange
  Server.

For information about how to use the New-AdminAuditLogSearch cmdlet, see Search the role
group changes or administrator audit logs.

Manual admin audit log entries
In addition to logging Exchange cmdlets when they're run, Exchange Server enables you to
manually write log entries to the audit log. Exchange Server supports this using the Write-
AdminAuditLog cmdlet. Situations where you might want to add a manual log entry include
the following:

     Custom script entry and exit

     Change control information

     Maintenance start and end times

With the Write-AdminAuditLog cmdlet, you specify a string of text to include in the audit log
using the Comment parameter. The Comment parameter accepts an alphanumeric string up to

<!-- p.2352 -->

500 characters. Included in the manual audit log entry along with the comment string is all of
the same information captured when an Exchange cmdlet is logged. For a description of each
field included in the audit log, see the table in Audit log contents.

You can retrieve manual audit log entries the same way as any other log entry, using the EAC
Auditing page or using the Search-AdminAuditLog or New-AdminAuditLogSearch cmdlets.

To view the contents of the Comment parameter on the Write-AdminAuditLog cmdlet in a
manual audit log entry, see Search the role group changes or administrator audit logs.

Active Directory replication
Administrator audit logging relies on Active Directory replication to replicate the configuration
settings you specify to the domain controllers in your organization. Depending on your
replication settings, the changes you make may not be immediately applied to all servers
running Exchange in your organization.

Admin Audit Log agent
The Admin Audit Log built-in cmdlet extension agent performs admin audit logging of cmdlet
operations in Exchange Server. This agent reads the audit log configuration and then performs
an evaluation of each cmdlet run in your organization. If the criteria you've specified in the
admin audit log configuration matches the cmdlet that's being run, the agent generates an
audit log entry.

The Admin Audit Log agent is enabled by default, which is required for admin audit logging to
function. It can't be disabled, and its priority can't be changed. For more information about
cmdlet extension agents, see Cmdlet Extension Agents.

<!-- p.2353 -->

Administrator audit log structure in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

Administrator audit logs contain a record of all the cmdlets and parameters that have been run
in the Exchange Management Shell and by the Exchange admin center (EAC). They're created
on-demand when you run the admin audit log report in the EAC, or when you run the New-
AdminAuditLogSearch cmdlet in the Exchange Management Shell. For more information
about audit logs, see Administrator audit logging in Exchange Server.

Audit log XML tags and attributes
The audit logs are XML files and can contain multiple audit log entries. The following table
describes each XML tag and its associated attributes.

                                                                                         ﾉ   Expand table

 Element                  Attribute          Description

 <?xml version="1.0"      N/A                This is the XML document declaration tag. It's included in
 encoding="utf-8"?>                          every audit log XML file and contains the XML version
                                             number and the character encoding value.

 SearchResults            N/A                This tag contains all the audit log entries in the XML file.
                                             The Event tag is a child of this tag.
                                             There is only one SearchResults tag per XML file.

 Event                                       This tag contains the audit log entry for an individual
                                             cmdlet. This tag contains the Caller , Cmdlet ,
                                             ObjectModified , RunDate , Succeeded , Error , and
                                             OriginatingServer attributes. The CmdletParameters and
                                             ModifiedProperties tags are children of this tag.
                                             There is one Event tag per audit log entry.

                          Caller             This attribute contains the user account of the user who
                                             ran the cmdlet in the Cmdlet attribute.

                          Cmdlet             This attribute contains the name of the cmdlet that was
                                             run by the user in the Caller attribute.

                          ObjectModified     This attribute contains the object that was modified by the
                                             cmdlet specified in the Cmdlet attribute. The

<!-- p.2354 -->

Element              Attribute           Description

                                         ModifiedProperties tag shows which properties were
                                         modified on this object.

                     RunDate             This attribute contains the date and time when the cmdlet
                                         in the Cmdlet attribute was run.

                     Succeeded           This attribute specifies whether the cmdlet in the Cmdlet
                                         attribute ran successfully. The value is either True or
                                         False .

                     Error               This attribute contains the error message generated if the
                                         cmdlet in the Cmdlet attribute failed to complete
                                         successfully. If no error was encountered, the value is set
                                         to None .

                     OriginatingServer   This attribute contains the server on which the cmdlet
                                         specified in the Cmdlet attribute was run.

CmdletParameters     N/A                 This tag contains all of the parameters specified when the
                                         cmdlet was run. The Parameter tag is a child of this tag.
                                         There is one CmdletParameters tag per Event tag.

Parameter                                This tag contains an individual parameter that was
                                         specified when the cmdlet was run. This tag contains the
                                         Name and Value attributes.
                                         There can be multiple Parameter tags per
                                         CmdletParameters tag.

                     Name                This attribute contains the name of the parameter that was
                                         specified on the cmdlet that was run.

                     Value               This attribute contains the value that was provided on the
                                         parameter specified in the Name attribute.

ModifiedProperties   N/A                 This tag contains all of the properties that were modified
                                         by the cmdlet that was run. The Property tag is a child of
                                         this tag.
                                         There is one ModifiedProperties tag per Event tag.
                                         Important: This tag is only populated if the LogLevel
                                         parameter on the Set-AdminAuditLogConfig cmdlet is set
                                         to Verbose .

Property                                 This tag contains an individual property that was specified
                                         when the cmdlet was run. This tag contains the Name ,
                                         OldValue , and NewValue attributes.
                                         There can be multiple Property tags per
                                         ModifiedProperties tag.

<!-- p.2355 -->

 Element                Attribute          Description

                        Name               This attribute contains the name of the property that was
                                           modified when the cmdlet was run.

                        OldValue           This attribute contains the value that was contained in the
                                           property specified in the Name attribute before it was
                                           changed.

                        NewValue           This attribute contains the value that the property in the
                                           Name attribute was changed to.

Example of an admin audit log entry
The following is an example of a typical log entry in the admin audit log.

  XML

  <?xml version="1.0" encoding="utf-8"?>
  <SearchResults>
    <Event Caller="corp.e16.contoso.com/Users/Administrator" Cmdlet="Set-Mailbox"
  ObjectModified="corp.e16.contoso.com/Users/david" RunDate="2015-10-18T15:48:15-
  07:00" Succeeded="true" Error="None" OriginatingServer="WIN8MBX (15.01.0396.030)">
      <CmdletParameters>
        <Parameter Name="Identity" Value="david" />
        <Parameter Name="ProhibitSendReceiveQuota" Value="10 GB (10,737,418,240
  bytes)" />
      </CmdletParameters>
      <ModifiedProperties>
        <Property Name="ProhibitSendReceiveQuota" OldValue="35 GB (37,580,963,840
  bytes)" NewValue="10 GB (10,737,418,240 bytes)" />
      </ModifiedProperties>
    </Event>
  </SearchResults>

Based on the information in this log entry, we know the following occurred:

     On 10/18/2017 at 3:48 P.M. Pacific Daylight Time (UTC-7), the user Administrator ran the
     cmdlet Set-Mailbox.

     The two following parameters were provided when the Set-Mailbox cmdlet was run:

        Identity with a value of david

        ProhibitSendReceiveQuota with a value of 10GB

     The ProhibitSendReceiveQuota property on the object david was modified with a new
     value of 10GB , which replaced the old value of 35GB .

<!-- p.2356 -->

  ７ Note

  The modified properties are saved to the audit log because the LogLevel parameter
  on the Set-AdminAuditLogConfig cmdlet was set to Verbose in this example.

The operation completed successfully without any errors.

<!-- p.2357 -->

Manage administrator audit logging in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Administrator audit logging in Exchange Server enables you to create a log entry each time a
specified cmdlet is run. Log entries provide you with information about what cmdlet was run,
which parameters were used, who ran the cmdlet, and what objects were affected. For more
information about administrator audit logging, see Administrator audit logging in Exchange
Server.

What do you need to know before you begin?
      Estimated time to complete each procedure: less than 5 minutes

      You can only use PowerShell to perform this procedure. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Administrator audit logging"
      entry in the Exchange infrastructure and PowerShell permissions topic.

      Admin audit logging relies on Active Directory replication to replicate the configuration
      settings you specify to the domain controllers in your organization. Depending on your
      replication settings, the changes you make may not be immediately applied to all
      Exchange 2016 and Exchange 2019 servers in your organization.

      Changes to the audit log configuration are refreshed every 60 minutes on computers that
      have the Exchange Management Shell open at the time a configuration change is made. If
      you want to apply the changes immediately, close and then open the Exchange
      Management Shell again on each computer.

      A command may take up to 15 minutes after it's run to appear in audit log search results.
      This is because audit log entries must be indexed before they can be searched. If a
      command doesn't appear in the administrator audit log, wait a few minutes and run the
      search again.

Specify the cmdlets to be audited

<!-- p.2358 -->

By default, audit logging creates a log entry for every cmdlet that's run. If you're enabling audit
logging for the first time and want this behavior, you don't have to change the cmdlet audit
list. If you've previously specified cmdlets to audit and now want to audit all cmdlets, you can
audit all cmdlets by specifying the asterisk (*) wildcard character with the
AdminAuditLogCmdlets parameter on the Set-AdminAuditLogConfig cmdlet, as shown in the
following command.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogCmdlets *

You can specify which cmdlets to audit by providing a list of cmdlets using the
AdminAuditLogCmdlets parameter. When you provide the list of cmdlets to audit, you can
provide single cmdlets, cmdlets with the asterisk (*) wildcard characters, or a mix of both. Each
entry in the list is separated by commas. The following values are all valid:

      New-Mailbox

      *TransportRule

      *Management*

      Set-Transport*

This example audits the cmdlets specified in the preceding list.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogCmdlets New-Mailbox, *TransportRule,
  *Management*, Set-Transport*

For detailed syntax and parameter information, see Set-AdminAuditLogConfig.

Specify the parameters to be audited
By default, audit logging creates a log entry for every cmdlet that's run, regardless of the
parameters specified. If you're enabling audit logging for the first time and want this behavior,
you don't have to change the parameter audit list. If you've previously specified parameters to
audit and now want to audit all parameters, you can do so by specifying the asterisk (*)
wildcard character with the AdminAuditLogParameters parameter on the Set-
AdminAuditLogConfig cmdlet, as shown in the following command.

  PowerShell

<!-- p.2359 -->

  Set-AdminAuditLogConfig -AdminAuditLogParameters *

You can specify which parameters you want to audit by using the AdminAuditLogParameters
parameter. When you provide the list of parameters to audit, you can provide single
parameters, parameters with the asterisk (*) wildcard characters, or a mix of both. Each entry in
the list is separated by commas. The following values are all valid:

      Database

      *Address*

      Custom*

      *Region

  ７ Note

  For an audit log entry to be created when a command is run, the command must include
  at least one or more parameters that exist on at least one or more cmdlets specified with
  the AdminAuditLogCmdlets parameter.

This example audits the parameters specified in the preceding list.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogParameters Database, *Address*, Custom*,
  *Region

For detailed syntax and parameter information, see Set-AdminAuditLogConfig.

Specify the admin audit log age limit
The audit log age limit determines how long audit log entries will be retained. When a log
entry exceeds the age limit, it's deleted. The default is 90 days.

You can specifiy the age limit in days. Or you can specify the number of days, hours, minutes,
and seconds that audit log entries should be kept. To specify a value more specific than days,
use the format dd.hh.mm:ss where the following applies:

     dd: Number of days to keep the audit log entry

     hh: Number of hours to keep the audit log entry

<!-- p.2360 -->

     mm: Number of minutes to keep the audit log entry

     ss: Number of seconds to keep the audit log entry

  Ｕ Caution

  You can set the audit log age limit to a value that's less than the current age limit. If you
  do this, any audit log entry whose age exceeds the new age limit will be deleted. > If you
  set the age limit to 0, Exchange deletes all the entries in the audit log. > We recommend
  that you assign permissions to configure the audit log age limit only to highly trusted
  users.

This example specifies an age limit of two years and six months.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogAgeLimit 913

For detailed syntax and parameter information, see Set-AdminAuditLogConfig.

Enable or disable logging of Test cmdlets
Cmdlets that start with the verb Test aren't logged by default. This is because Test cmdlets can
generate a significant amount of data in a short time. Only enable the logging of Test cmdlets
for short periods of time.

This command enables the logging of Test cmdlets.

  PowerShell

  Set-AdminAuditLogConfig -TestCmdletLoggingEnabled $true

This command disables the logging of Test cmdlets.

  PowerShell

  Set-AdminAuditLogConfig -TestCmdletLoggingEnabled $false

For detailed syntax and parameter information, see Set-AdminAuditLogConfig.

Disable admin audit logging
