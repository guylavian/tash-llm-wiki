---
title: "Exchange Server — pages 1081-1120"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1081-1120
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1081-1120
family: exchange
documentKind: "doc"
abstract: "The following example uses the text file C:\\My Documents\\MBQuotas.txt to identify the mailboxes by the associated UPNs. The text file must contain one mailbox on each line as follows: akol@contoso.com tjohnston@contoso.com kakers@contoso.com After you populate the text file with"
---

# Exchange Server — pages 1081-1120

<!-- p.1081 -->

The following example uses the text file C:\My Documents\MBQuotas.txt to identify the
mailboxes by the associated UPNs. The text file must contain one mailbox on each line as
follows:

  akol@contoso.com
  tjohnston@contoso.com

  kakers@contoso.com

After you populate the text file with the mailboxes you want to update, run the following
commands:

  PowerShell

  $MBQ = Get-Content "C:\My Documents\MBQuotas.txt"

  $MBQ | foreach {Set-Mailbox -Identity $_ -UseDatabaseQuotaDefaults $false -
  IssueWarningQuota 900MB -ProhibitSendQuota 950MB -ProhibitSendReceiveQuota 1GB}

How do you successfully set the storage quotas for
a mailbox?
To verify you successfully set the storage quotas for a mailbox, do either of the following
procedures:

     Exchange admin center:

           1. In the EAC, go to Recipients > Mailboxes tab.
           2. On the Mailboxes tab, select the mailbox that you want to modify, and then select
                  Edit.
           3. On the mailbox properties page that opens, select the Mailbox usage tab, and then
              select More options to show the mailbox quota settings.

     Verify Customize the quota settings for this mailbox is selected, and verify the quota
     values.

     Exchange Management Shell: Replace <MailboxIdentity> with the name, email address
     or alias of the mailbox, and then run the following command:

           PowerShell

           Get-Mailbox <MailboxIdentity> | Format-List
           UseDatabaseQuotaDefaults,IssueWarningQuota,ProhibitSendQuota,ProhibitSendRece

<!-- p.1082 -->

iveQuota

<!-- p.1083 -->

Configure Deleted Item retention and
Recoverable Items quotas in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016       2019   Subscription Edition

When a user deletes items from the Deleted Items default folder by using the Delete,
Shift+Delete, or Empty Deleted Items Folder actions, the items are moved to the Recoverable
Items\Deletions folder. The duration that deleted items remain in this folder is based on the
deleted item retention settings configured for the mailbox database or the mailbox. By default,
a mailbox database is configured to retain deleted items for 14 days, and the recoverable items
warning quota and recoverable items quota are set to 20 gigabytes (GB) and 30 GB
respectively.

  ７ Note

  Before the retention time for deleted items elapses,Outlook and Outlook on the web users
  can recover deleted items by using the Recover Deleted Items feature. To learn more
  about these features, see the "Recover deleted items" topic for Outlook for Windows      or
  Outlook on the web      .

You can use the Exchange Management Shell to configure deleted item retention settings and
recoverable items quotas for a mailbox or mailbox database. Deleted item retention settings
are ignored when a mailbox is placed on In-Place Hold or litigation hold.

To learn more about deleted item retention, the Recoverable Items folder, In-Place Hold, and
litigation hold, see Recoverable Items folder in Exchange Server.

What do you need to know before you begin?
      Estimated time to completion: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Messaging records
      management" entry in the Messaging policy and compliance permissions in Exchange
      Server topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

<!-- p.1084 -->

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Configure deleted item retention for a mailbox
Use the Exchange admin center (EAC) to configure deleted item retention for a mailbox

  1. Navigate to Recipients > Mailboxes.

  2. In the list view, select a mailbox, and then click Edit   .

  3. On the mailbox property page, click Mailbox usage, click More options, and then select
     one of the following:

          Use the default retention settings from the mailbox database: Use the deleted
          item retention setting that's configured for the mailbox database.

          Customize the settings for this mailbox: Configure deleted item retention settings
          for the mailbox.

          *Keep deleted items for (days): Displays the length of time that deleted items are
          retained before they're permanently deleted and can't be recovered by the user.
          When the mailbox is created, this value is based on the deleted item retention
          settings configured for the mailbox database. By default, a mailbox database is
          configured to retain deleted items for 14 days. The value range for this property is
          from 0 through 24,855 days.

          Don't permanently delete items until the database is backed up: Check this box to
          prevent mailboxes and email messages from being deleted until after the mailbox
          database on which the mailbox is located has been backed up.

<!-- p.1085 -->

Configure deleted item retention for a mailbox
database
Use the Exchange admin center (EAC) to configure deleted item retention for a mailbox
database

  1. Navigate to Servers > Databases.

  2. In the list view, select a mailbox database, and then click Edit   .

  3. On the mailbox database property page, click Limits, and then select one of the following:

           *Keep deleted items for (days): Displays the length of time that deleted items are
           retained before they're permanently deleted and can't be recovered by the user.
           When a mailbox is created, this value is based on the deleted item retention settings
           configured for the mailbox database. By default, a mailbox database is configured to

<!-- p.1086 -->

           retain deleted items for 14 days. The value range for this property is from 0 through
           24,855 days.

           Don't permanently delete items until the database is backed up: Check this box to
           prevent mailboxes and email messages from being deleted until after the mailbox
           database on which the mailbox is located has been backed up.

Use the Exchange Management Shell to configure deleted
item retention for a mailbox
This example configures April Stewart's mailbox to retain deleted items for 30 days and until
after the mailbox database on which the mailbox is located has been backed up.

  PowerShell

  Set-Mailbox -Identity - "April Stewart" -RetainDeletedItemsFor 30 -
  RetainDeletedItemsUntilBackup $true

For detailed syntax and parameter information, see Set-Mailbox.

Use the Exchange Management Shell to configure
recoverable items quotas for a mailbox

  ７ Note

  You can't use the EAC to configure recoverable items quotas for a mailbox.

This example configures a recoverable items warning quota of 12 GB and a recoverable items
quota of 15 GB for April Stewart's mailbox.

  PowerShell

  Set-Mailbox -Identity "April Stewart" -RecoverableItemsWarningQuota 12GB -
  RecoverableItemsQuota 15GB -UseDatabaseQuotaDefaults $false

  ７ Note

<!-- p.1087 -->

  To configure a mailbox to use different recoverable items quotas than the mailbox
  database in which it resides, you must set the UseDatabaseQuotaDefaults parameter to
  $false .

For detailed syntax and parameter information, see Set-Mailbox.

Use the Exchange Management Shell to configure
deleted item retention for a mailbox database

  ７ Note

  You can't use the EAC to configure deleted item retention for a mailbox database.

This example configures a deleted item retention period of 10 days for the mailbox database
MDB2 and the setting to retain deleted items until the mailbox database has been backed up.

  PowerShell

  Set-MailboxDatabase -Identity MDB2 -DeletedItemRetention 10 -
  RetainDeletedItemsUntilBackup $true

For detailed syntax and parameter information, see Set-MailboxDatabase.

Use the Exchange Management Shell to configure
recoverable items quotas for a mailbox database

  ７ Note

  You can't use the EAC to configure recoverable items quotas for a mailbox database

This example configures a recoverable items warning quota of 15 GB and a recoverable items
quota of 20 GB on mailbox database MDB2.

  PowerShell

  Set-MailboxDatabase -Identity MDB2 -RecoverableItemsWarningQuota 15GB -
  RecoverableItemsQuota 20GB

For detailed syntax and parameter information, see Set-MailboxDatabase.

<!-- p.1088 -->

<!-- p.1089 -->

Convert a mailbox in Exchange Server
07/23/2025

APPLIES TO:      2016     2019      Subscription Edition

In Exchange Server 2013 or later, converting a mailbox from one type of mailbox to another is
mostly unchanged from the experience in Exchange 2010. You still need to use the Set-Mailbox
cmdlet in the Exchange Management Shell to do the conversion.

You can convert the following mailboxes to a different type:

     User mailbox to room or equipment mailbox

     User mailbox to shared mailbox

     Shared mailbox to user mailbox

     Shared mailbox to room or equipment mailbox

     Room or equipment mailbox to user mailbox

     Room or equipment mailbox to shared mailbox

  ７ Note

  If your organization uses a hybrid Exchange environment, you need to manage your
  mailboxes by using the on-premises Exchange management tools. To convert a mailbox in
  a hybrid environment, you might need to move the mailbox back to on-premises
  Exchange, convert the mailbox type, and then move it back to Microsoft 365 or Office 365.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes.

     Room, equipment, and shared mailboxes have associated user accounts in Active
     Directory, but the accounts are disabled. When you convert one of these mailbox types to
     a regular (user) mailbox, you need to specify a password that satisfies the length and
     complexity requirements for your organization.

     Overwriting an existing password requires the Reset Password role, which isn't assigned
     to any role groups by default. To assign the role to a role group that you belong to, see
     Add a role to a role group. Note that changes in permission require you to log off and log
     on for the changes to take effect.

<!-- p.1090 -->

     When you convert a regular (user) mailbox to a room, equipment, or shared mailbox, the
     associated account is disabled.

     For room mailboxes, you can enable the associated user account, which also requires you
     to specify a password (which requires the Reset Password role). You need to enable the
     room mailbox user account for features like the Skype for Business Room System.

     To learn how to open the Exchange Management Shell in your on-premises Exchange
     organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Recipient Provisioning
     Permissions" section in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to convert a
mailbox
To convert a mailbox to a different type, use this syntax:

  PowerShell

  Set-Mailbox -Identity <MailboxIdentity> -Type <Regular | Room | Equipment |
  Shared> [-Password (Read-Host "Enter password" -AsSecureString)] [-
  EnableRoomMailboxAccount <$true | $false>] [-RoomMailboxPassword (ConvertTo-
  SecureString -String '<Password>' -AsPlainText -Force)] [-ResetPasswordOnNextLogon
  <$true | $false>]

This example converts the shared mailbox named Marketing Dept 01 to a user mailbox. You're
prompted to enter the password, and the user is required to change their password the next
time they log in to the mailbox.

  PowerShell

  Set-Mailbox -Identity "Marketing Dept 01" -Type Regular -Password (Read-Host

<!-- p.1091 -->

  "Enter password" -AsSecureString) -ResetPasswordOnNextLogon $true

This example converts the user mailbox named Conference Room 01 to a room mailbox.

  PowerShell

  Set-Mailbox -Identity "Conference Room 01" -Type Room

This is the same example, but the user account for the room mailbox is enabled, and the
password is P@ssw0rd25

  PowerShell

  Set-Mailbox -Identity "Conference Room 01" -Type Room -EnableRoomMailboxAccount
  $true -RoomMailboxPassword (ConvertTo-SecureString -String 'P@ssw0rd25' -
  AsPlainText -Force)

Note: Even when you convert a user mailbox with a known password to a room mailbox, you
still need to use the RoomMailboxPassword parameter to specify a password.

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To verify that you've successfully converted a mailbox, replace <MailboxIdentity> with the
name, alias, or email address of the mailbox, and run this command in the Exchange
Management Shell to verify the property values:

  PowerShell

  Get-Mailbox -Identity <MailboxIdentity> | Format-List
  Name,RecipientTypeDetails,UserPrincipalName,AccountDisabled

For detailed syntax and parameter information, see Get-Mailbox.

<!-- p.1092 -->

Enable or disable single item recovery for a
mailbox
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

You can use the Exchange Management Shell to enable or disable single item recovery on a
mailbox. In Exchange Server, single item recovery is disabled when a mailbox is created. If
single item recovery is enabled, messages that are purged (hard-deleted) by the user are
retained in the Recoverable Items folder of the mailbox until the deleted item retention period
expires. This lets an administrator recover messages purged by the user before the deleted
item retention period expires.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Retention and legal holds" entry
      in the Recipients Permissions topic.

      You can't use the Exchange admin center (EAC) to enable or disable single item recovery.

      In Exchange Server, the mailbox uses the deleted item retention settings of the mailbox
      database, by default. The deleted item retention period for a mailbox database is set to
      14 days, but you can override the default by configuring this setting on a per-mailbox
      basis. For details, see Configure Deleted Item retention and Recoverable Items quotas.

Enable single item recovery
This example enables single item recovery for the mailbox of April Summers.

  PowerShell

  Set-Mailbox -Identity "April Summers" -SingleItemRecoveryEnabled $true

This example enables single item recovery for the mailbox of Pilar Pinilla and sets the number
of days that deleted items are retained to 30 days.

  PowerShell

  Set-Mailbox -Identity "Pilar Pinilla" -SingleItemRecoveryEnabled $true -
  RetainDeletedItemsFor 30

<!-- p.1093 -->

This example enables single item recovery for all user mailboxes in the organization.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -SingleItemRecoveryEnabled $true

This example enables single item recovery for all user mailboxes in the organization and sets
the number of days that deleted items are retained to 30 days

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -SingleItemRecoveryEnabled $true -RetainDeletedItemsFor 30

For detailed syntax and parameter information, see Set-Mailbox.

Disable single item recovery
You might need to disable single item recovery for a user's mailbox. For example, before you
can use Search-Mailbox -DeleteContent to permanently delete content from a mailbox, you
have to disable single item recovery. For more information, see Search for and delete messages
in Exchange Server.

This example disables single item recovery for the mailbox of Ayla Kol.

  PowerShell

  Set-Mailbox -Identity "Ayla Kol" -SingleItemRecoveryEnabled $false

How do you know this worked?
To verify that you've enabled single item recovery for a mailbox and display the value for how
long deleted items will be retained (in days), run the following command.

  PowerShell

  Get-Mailbox <Name> | Format-List SingleItemRecoveryEnabled,RetainDeletedItemsFor

You can use this same command to verify that single item recovery is disabled for a mailbox.

<!-- p.1094 -->

More information
  To learn more about single item recovery, see Recoverable Items folder in Exchange
  Server. To recover messages purged by the user before the deleted item retention period
  expires, see Recover deleted messages in a user's mailbox .

  If a mailbox is placed on In-Place Hold or Litigation Hold, messages in the Recoverable
  Items folder are retained until the hold duration expires. If the hold duration is unlimited,
  then items are retained until the hold is removed or the hold duration is changed.

<!-- p.1095 -->

Recover deleted messages in a user's
mailbox in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Administrators can search for items that are purged (hard-deleted) by a user by using the
Recover Deleted Items feature in Outlook or Outlook on the web. They can also search for
items deleted by an automated process, such as the retention policy assigned to user
mailboxes. In these situations, the purged items can't be recovered by a user. But
administrators can recover purged messages if the deleted item retention period for the item
hasn't expired.

  ７ Note

  In addition to using this procedure to search for and recover deleted items, you can also
  use this procedure to search for items residing in other folders in the mailbox and to
  delete items from the source mailbox (also known as search and purge).

What you need to know before you begin?
      Procedures in this topic require specific permissions. See each procedure for its
      permissions information.

      Single item recovery should be enabled for a mailbox before the item you want to recover
      is deleted. In Exchange Server, single item recovery is disabled when a mailbox is created.
      For more information, see Enable or disable single item recovery for a mailbox.

      To search for and recover items, you need the following information:

         Source mailbox: The mailbox being searched.

         Target mailbox: The discovery mailbox in which messages will be recovered. Exchange
         Server Setup creates a default discovery mailbox. In Exchange Online, a discovery
         mailbox is also created by default. If required, you can create additional discovery
         mailboxes. For details, see Create a Discovery Mailbox.

           ７ Note

           When using the Search-Mailbox cmdlet, you can also specify a target mailbox
           that isn't a discovery mailbox. However, you can't specify the same mailbox as the

<!-- p.1096 -->

           source and target mailbox.

        Search criteria: Criteria include sender or recipient, or keywords (words or phrases) in
        the message.

Step 1: Search for and recover missing items
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "In-Place eDiscovery" entry in the Messaging policy
and compliance permissions in Exchange Server topic.

  ７ Note

  You can use In-Place eDiscovery in the Exchange admin center (EAC) to search for missing
  items. However, when using the EAC, you can't restrict the search to the Recoverable Items
  folder. All messages matching your search parameters will be returned even if they're not
  deleted. After they're recovered to the specified discovery mailbox, you may need to
  review the search results and remove unnecessary messages before recovering the
  remaining messages to the user's mailbox or exporting them to a .pst file. For details
  about how to use the EAC to perform an In-Place eDiscovery search, see Create an In-
  Place eDiscovery search in Exchange Server.

The first step in the recovery process is to search for messages in the source mailbox. Use one
of the following methods to search a user mailbox and copy messages to a discovery mailbox.

Use the Exchange Management Shell to search for messages
  PowerShell

  Get-RecoverableItems -Identity laura@contoso.com -SubjectContains "FY17
  Accounting" -FilterItemType IPM.Note -FilterStartTime "2/1/2018 12:00:00 AM" -
  FilterEndTime "2/5/2018 11:59:59 PM"

This example returns all of the available recoverable deleted messages with the specified
subject in the mailbox laura@contoso.com for the specified date/time range.

   Tip

  Use the Get-RecoverableItems cmdlet to create a search query to find an Outlook item.
  Once you have a list of results you can use properties like last modified date, item type,

<!-- p.1097 -->

  etc. to narrow the amount of items restored or to restore a specific item.

For detailed syntax and parameter information, see Get-RecoverableItems.

How do you know this worked?
To verify that you have successfully searched the messages you want to recover, log on to the
discovery mailbox you selected as the target mailbox and review the search results.

Step 2: Restore recovered items
You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "In-Place eDiscovery" entry in the Messaging policy
and compliance permissions in Exchange Server topic.

  ７ Note

  You can't use the EAC to restore recovered items.

After messages have been recovered to a discovery mailbox, you can restore them to the user's
mailbox by using the Search-Mailbox cmdlet. In Exchange Server, you can also use the New-
MailboxExportRequest and New-MailboxImportRequest cmdlets to export the messages to
or import the messages from a .pst file.

Use the Exchange Management Shell to restore messages
  PowerShell

  $mailboxes = Import-CSV "C:\My Documents\RestoreMessage.csv"; $mailboxes | foreach
  {Restore-RecoverableItems -Identity $_.SMTPAddress -SubjectContains Project X" -
  SourceFolder DeletedItems -FilterItemType IPM.Note}

This example restores the deleted email message "Project X" for the mailboxes that are
specified in the comma-separated value (CSV) file C:\My Documents\RestoreMessage.csv. The
CSV file uses the header value SMTPAddress, and contains the email address of each mailbox
on a separate line like this:

SMTPAddress

chris@contoso.com

<!-- p.1098 -->

michelle@contoso.com

laura@contoso.com

julia@contoso.com

The first command reads the CSV file to the variable named $mailboxes. The second command
restores the specified message from the Deleted Items folder in those mailboxes.

For detailed syntax and parameter information, see Restore-RecoverableItems.

How do you know this worked?

To verify that you have successfully recovered messages to the user's mailbox, have the user
review messages in the target folder you specified in the above command.

Use the Exchange Management Shell to export and import
messages from a .pst file
In Exchange Server, you can export contents from a mailbox to a .pst file and import the
contents of a .pst file to a mailbox. To learn more about mailbox import and export, see
Mailbox imports and exports in Exchange Server. You can't perform this task in Exchange
Online.

This example uses the following settings to export messages from the folder April Stewart
Recovery in the Discovery Search Mailbox to a .pst file:

     Mailbox: Discovery Search Mailbox

     Source folder: April Stewart Recovery

     ContentFilter: April travel plans

     PST file path: \MYSERVER\HelpDeskPst\AprilStewartRecovery.pst

  PowerShell

  New-MailboxExportRequest -Mailbox "Discovery Search Mailbox" -SourceRootFolder
  "April Stewart Recovery" -ContentFilter "Subject -eq 'April travel plans'" -
  FilePath \\MYSERVER\HelpDeskPst\AprilStewartRecovery.pst

For detailed syntax and parameter information, see New-MailboxExportRequest.

This example uses the following settings to import messages from a .pst file to the folder
Recovered By Helpdesk in April Stewart's mailbox:

<!-- p.1099 -->

     Mailbox: April Stewart

     Target folder: Recovered By Helpdesk

     PST file path: \MYSERVER\HelpDeskPst\AprilStewartRecovery.pst

  PowerShell

  New-MailboxImportRequest -Mailbox "April Stewart" -TargetRootFolder "Recovered By
  Helpdesk" -FilePath \\MYSERVER\HelpDeskPst\AprilStewartRecovery.pst

For detailed syntax and parameter information, see New-MailboxImportRequest.

How do you know this worked?

To verify that you have successfully exported messages to a .pst file, use Outlook to open the
.pst file and inspect its contents. To verify that you have successfully imported messages from
the .pst file, have the user inspect the contents of the target folder you specified in the above
command.

More information
     The ability to recover deleted items is enabled by single item recovery, which lets an
     administrator recover a message that's been purged by a user or by retention policy as
     long as the deleted item retention period hasn't expired for that item. To learn more
     about single item recovery, see Recoverable Items folder in Exchange Server.

     In Exchange Server, a mailbox database is configured to retain deleted items for 14 days,
     by default. You can configure deleted item retention settings for a mailbox or mailbox
     database. For more information, see:
        Configure Deleted Item retention and Recoverable Items quotas

     Users can recover a deleted item if it hasn't been purged and if the deleted item retention
     period for that item hasn't expired. If users need to recover deleted items from the
     Recoverable Items folder, point them to the following topics:

        Recover deleted items in Outlook for Windows

        Recover deleted items or email in Outlook on the web

     This topic shows you how to use the Search-Mailbox cmdlet to search for and recover
     missing items. If you use this cmdlet, you can search only one mailbox at a time. If you
     want to search multiple mailboxes at the same time, you can use In-Place eDiscovery in

<!-- p.1100 -->

     Exchange Server in the Exchange admin center (EAC) or the New-ComplianceSearch
     cmdlet in Windows PowerShell.

     In addition to using this procedure to search for and recover deleted items, you can also
     use a similar procedure to search for items in user mailboxes and then delete those items
     from the source mailbox. For more information, see Search for and delete messages in
     Exchange Server.

Related article
Are you using Exchange Online? See Recover deleted messages in a user's mailbox in Exchange
Online.

<!-- p.1101 -->

Manage linked mailboxes in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Linked mailboxes may be necessary for organizations that deploy Exchange in a resource forest.
The resource forest scenario lets an organization centralize Exchange in a single forest, while
allowing access to the Exchange organization with user accounts that are located in one or
more trusted forests (called account forests). The user account that accesses the linked mailbox
doesn't exist in the forest where Exchange is deployed. Therefore, a disabled user account that
exists in the same forest as Exchange is created and associated with the corresponding linked
mailbox.

The following figure illustrates the relationship between the linked user account used to access
the linked mailbox (located in the account forest) and the disabled user account in the
Exchange resource forest that's associated with the linked mailbox.

Linked mailboxes

  ７ Note

  A trust between the Exchange forest and at least one account forest must be set up before
  you can create linked mailboxes. At a minimum, you must set up a one-way, outgoing
  trust so that the Exchange forest trusts the account forest. For more information, see
  Learn more about setting up a forest trust to support linked mailboxes.

What do you need to know before you begin?

<!-- p.1102 -->

   Estimated time to complete: 2 to 5 minutes.

   You need to be assigned permissions before you can perform this procedure or
   procedures. To see what permissions you need, see the "Recipient Provisioning
   Permissions" section in the Recipients Permissions topic.

   A user account (called the linked master account) must exist in the account forest before
   you can create a linked mailbox. This is because the linked mailbox is associated with a
   user in the account forest.

   If you've configured a one-way outgoing trust where the Exchange forest trusts the
   account forest, you'll need administrator credentials in the account forest to create a
   linked mailbox.

   To create a linked mailbox without being prompted for administrator credentials in the
   account forest, you have to create a two-way trust, or create another one-way outgoing
   trust where the account forest also trusts the Exchange forest. This step also requires
   administrator credentials in the account forest.

   You can complete this procedure in the Exchange admin center (EAC) or use the Exchange
   Management Shell.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online        , or Exchange Online Protection .

Create a linked mailbox

Use the EAC to create a linked mailbox
 1. In the EAC, navigate to Recipients > Mailboxes.

 2. Click New > Linked mailbox.

 3. On the New linked mailbox page, in the Trusted forest or domain box, select the name
   of the account forest that contains the user account that you're creating the linked
   mailbox for. Click Next.

<!-- p.1103 -->

4. If your organization has configured a one-way outgoing trust where the Exchange forest
  trusts the account forest, you're prompted for administrator credentials in the account
  forest so that you can gain access to a domain controller in the trusted forest. Type the
  username and password for an administrator account in the account forest, and then click
  Next.

    ７ Note

    You won't be prompted for administrator credentials if you've created a two-way
    trust or have created another one-way outgoing trust where the account forest trusts
    the Exchange forest.

5. Complete the following boxes on the Select linked master account page.

       Linked domain controller: Select a domain controller in the account forest.
       Exchange will connect to this domain controller to retrieve the list of user accounts
       in the account forest so that you can select the linked master account.

       Linked master account: Click Browse, select a user account in the account forest,
       and then click OK. The new linked mailbox will be associated with this account.

6. Click Next and complete the following boxes on the Enter general information page.

       * Name: Use this box to type a name for the user. This is the name used as the
       display name in the EAC and your organization's address book, and the name that's
       listed in Active Directory. This name is required.

       Organizational unit: You can select an organizational unit (OU) other than the
       default (which is the recipient scope). If the recipient scope is set to the forest, the
       default value is set to the Users container in the Active Directory domain that
       contains the computer on which the EAC is running. If the recipient scope is set to a
       specific domain, the Users container in that domain is selected by default. If the
       recipient scope is set to a specific OU, that OU is selected by default.

       To select a different OU, click Browse. The dialog box displays all OUs in the
       Exchange forest that are within the specified scope. Select the OU you want, and
       then click OK.

       * User logon name: Use this box to type the user logon name, which is required to
       create a linked mailbox. Type the username here. This name will be used in the left
       portion of the email address for the linked mailbox if you don't specify an alias.

          ７ Note

<!-- p.1104 -->

            Because the user account that is created in the Exchange forest is disabled
            when you create a linked mailbox, the user doesn't use the user logon name to
            sign in to the linked mailbox. They sign in using their credentials from the
            account forest.

  7. Click More options to configure the following boxes. Otherwise, skip to Step 8 to save the
     new linked mailbox.

          Alias: Type the alias, which specifies the email alias for the linked mailbox. The user's
          alias is the portion of the email address on the left side of the at (@) symbol. It must
          be unique in the forest.

            ７ Note

            If you leave this box blank, the value from the username portion of the User
            Logon Name is used for the email alias.

          First name, Initials, Last name

          Mailbox database: Use this option to specify a mailbox database instead of allowing
          Exchange to choose a database for you. Click Browse to open the Select Mailbox
          Database dialog box. This dialog box lists all the mailbox databases in your
          Exchange organization. By default, the mailbox databases are sorted by name. You
          can also click the title of the corresponding column to sort the databases by server
          name or version. Select the mailbox database you want to use, and then click OK.

          Address book policy: Use this option to specify an address book policy (ABP) for the
          linked mailbox. An ABP contains a global address list (GAL), an offline address book
          (OAB), a room list, and a set of address lists. When assigned to users, an ABP
          provides them with access to a customized GAL in Outlook and Outlook on the web
          (formerly known as Outlook Web App). To learn more, see Address book policies in
          Exchange Server.

          In the drop-down list, select the policy that you want associated with this mailbox.

  8. When you're finished, click Save to create the new linked mailbox.

Use the Exchange Management Shell to create a linked
mailbox
This example creates a linked mailbox for Ayla Kol in the CONTOSO Exchange resource forest.
The FABRIKAM domain is in the account forest. The administrator account FABRIKAM

<!-- p.1105 -->

\administrator is used to access the linked domain controller.

  PowerShell

  New-Mailbox -Name "Ayla Kol" -LinkedDomainController "DC1_FABRIKAM" -
  LinkedMasterAccount " FABRIKAM\aylak" -OrganizationalUnit Users -UserPrincipalName
  aylak@contoso.com -LinkedCredential:(Get-Credential FABRIKAM\administrator)

For syntax and parameter information, see New-Mailbox.

How do you know this worked?
To verify that you've successfully created a linked mailbox, do one of the following:

     In the EAC, navigate to Recipients > Mailboxes. The new linked mailbox is displayed in
     the mailbox list. Under Mailbox Type, the type is Linked.

     In the Exchange Management Shell, run the following command to display information
     about the new linked mailbox.

        PowerShell

        Get-Mailbox <Name> | Format-List
        Name,RecipientTypeDetails,IsLinked,LinkedMasterAccount

Change linked mailbox properties
After you create a linked mailbox, you can make changes and set additional properties by
using the EAC or the Exchange Management Shell.

You can also change properties for multiple linked mailboxes at the same time. For more
information, see Bulk edit user mailboxes.

  ） Important

  The estimated time to complete this task will vary based on the number of properties you
  want to view or change.

Use the EAC to change linked mailbox properties
   1. In the EAC, navigate to Recipients > Mailboxes.

<!-- p.1106 -->

   2. In the list of mailboxes, click the linked mailbox that you want to change the properties
     for, and then click Edit   .

   3. On the mailbox properties page, click one of the following sections to view or change
     properties.

          General

          Mailbox Usage

          Email Address

          Mailbox Features

          Member Of

          MailTip

General
Use the General section to view or change basic information about the user.

     * Linked mailbox name: This is the name that's listed in Active Directory. If you change
     this name, it can't exceed 64 characters.

     * Display name: This name appears in your organization's address book, on the To: and
     From: lines in email, and in the Mailboxes list in the EAC. This name can't contain empty
     spaces before or after the display name.

     * User logon name: For user mailboxes, this is the name that the user uses to sign in to
     their mailbox and to log on to the domain. For linked mailboxes, the corresponding user
     account that is created in the Exchange forest when the linked mailbox was created is
     disabled. The user uses their credentials from the account forest to sign in to the linked
     mailbox.

     If you change this name, it must be unique in your organization.

     Linked master account: This read-only box displays the user (in the format
     domain\username format) from the account forest that is associated with the linked
     mailbox. To change the linked master account associated with the linked mailbox, you
     have to use the Set-Mailbox cmdlet in the Exchange Management Shell. If you change
     the linked master account, the user will have to use the credentials for the new linked
     master account to sign in to the linked mailbox. For the command syntax to change the
     linked master account, see Use the Exchange management Shell to change linked mailbox
     properties.

<!-- p.1107 -->

     Hide from address lists: Select this check box to prevent the linked mailbox from
     appearing in the address book and other address lists that are defined in your Exchange
     organization. After you select this check box, users can still send messages to this user by
     using the email address.

Click More options to view or change these additional properties:

     Organizational unit: This read-only box displays the organizational unit (OU) that
     contains the user account. You have to use Active Directory Users and Computers to
     move the user account to a different OU.

     Mailbox database: This read-only box displays the name of the mailbox database that
     hosts the mailbox. To move the mailbox to a different database, select it in the mailbox
     list, and then click Move mailbox to a different database in the Details pane.

     * Alias This specifies the email alias for the linked mailbox. The alias is the portion of the
     email address on the left side of the at (@) symbol. It must be unique in the forest.

     First name, Initials, Last name

     Custom attributes: This section displays the custom attributes defined for the linked
     mailbox. To specify custom attribute values, click Edit    . You can specify up to 15 custom
     attributes for the recipient.

Mailbox Usage

Use the Mailbox Usage section to view or change the mailbox storage quota and deleted item
retention settings for the linked mailbox. These settings are configured by default when the
linked mailbox is created. They use the values that are configured for the mailbox database and
apply to all mailboxes in that database. You can customize these settings for each mailbox
instead of using the mailbox database defaults.

     Last logon: This read-only box displays the last time that the user signed in to the
     mailbox.

     Mailbox usage: This area shows the total size of the mailbox and the percentage of the
     total mailbox quota that has been used.

  ７ Note

  To obtain the information that's displayed in the previous two boxes, the EAC queries the
  mailbox database that hosts the mailbox. If the EAC can't communicate with the Exchange

<!-- p.1108 -->

  store that contains the mailbox database, these boxes will be blank. A warning message is
  displayed if the user hasn't signed in to the mailbox for the first time.

Click More options to view or change the mailbox storage quota and the deleted item
retention settings for the mailbox.

     Storage quota settings: To customize these settings for the mailbox and not use the
     mailbox database defaults, click Customize settings for this mailbox, type a new value,
     and then click Save.

     The value range for any of the storage quota settings is from 0 through 2047 gigabytes
     (GB).

        Issue a warning at (GB): This box displays the maximum storage limit before a warning
        is issued to the user. If the mailbox size reaches or exceeds the value specified,
        Exchange sends a warning message to the user.

        Prohibit send at (GB): This box displays the prohibit send limit for the mailbox. If the
        mailbox size reaches or exceeds the specified limit, Exchange prevents the user from
        sending new messages and displays a descriptive error message.

        Prohibit send and receive at (GB): This box displays the prohibit send and receive limit
        for the mailbox. If the mailbox size reaches or exceeds the specified limit, Exchange
        prevents the mailbox user from sending new messages and won't deliver any new
        messages to the mailbox. Any messages sent to the mailbox are returned to the sender
        with a descriptive error message.

     Deleted item retention settings: To customize these settings for the mailbox and not use
     the mailbox database defaults, click Customize settings for this mailbox, type a new
     value, and then click Save.

        Keep deleted items for (days): This box displays the length of time that deleted items
        are retained before they're permanently deleted and can't be recovered by the user.
        When the mailbox is created, this length of time is based on the deleted item retention
        settings configured for the mailbox database. By default, a mailbox database is
        configured to retain deleted items for 14 days. The value range for this property is
        from 0 through 24855 days.

        Don't permanently delete items until the database is backed up: Select this check box
        to prevent mailboxes and email messages from being deleted until after the mailbox
        database on which the mailbox is located has been backed up.

Email Address

<!-- p.1109 -->

Use the Email address section to view or change the email addresses associated with the
linked mailbox. This includes the user's primary SMTP addresses and any associated proxy
addresses. The primary SMTP address (also known as the default reply address) is displayed in
bold text in the address list, with the uppercase SMTP value in the Type column.

     Add: Click Add      to add a new email address for this mailbox. Select one of following
     address types:

        SMTP: This is the default address type. Click this radio button and then type the new
        SMTP address in the * Email address box.

        EUM: An EUM (Exchange Unified Messaging) address is used by the Exchange Unified
        Messaging service in Exchange 2016 to locate UM-enabled users within an Exchange
        organization. EUM addresses consist of the extension number and the UM dial plan for
        the UM-enabled user. Click this radio button and type the extension number in the
        Address/Extension box. Then click Browse and select a dial plan for the user. (Note:
        Unified Messaging is not available in Exchange 2019.)

        Custom address type: Click this button and type one of the supported non-SMTP
        email address types in the * Email address box.

            ７ Note

            With the exception of X.400 addresses, Exchange doesn't validate custom
            addresses for proper formatting. You must make sure that the custom address
            you specify complies with the format requirements for that address type.

     Automatically update email addresses based on the email address policy applied to this
     recipient: Select this check box if you want the recipient's email addresses to be updated
     automatically when changes are made to email address policies in your organization. This
     box is selected by default.

Mailbox Features

Use the Mailbox Features section to view or change the following mailbox features and
settings:

     Sharing policy: This box shows the sharing policy applied to the mailbox. A sharing policy
     controls how users in your organization can share calendar and contact information with
     users outside your Exchange organization. The Default Sharing Policy is assigned to
     mailboxes when they are created. To change the sharing policy that's assigned to the
     user, select a different one from the drop-down list.

<!-- p.1110 -->

Role assignment policy: This box shows the role assignment policy assigned to the
mailbox. The role assignment policy specifies the role-based access control (RBAC) roles
that are assigned to the user and controls which mailbox and distribution group
configuration settings users can modify. To change the role assignment policy that's
assigned to the user, select a different one from the drop-down list.

Retention policy: This box shows the retention policy assigned to the mailbox. A
retention policy is a group of retention tags that are applied to the user's mailbox. The
tags allow you to control how long to keep items in users' mailboxes and define which
action to take on items that have reached a certain age. A retention policy isn't assigned
to mailboxes when they are created. To assign a retention policy to the user, select one
from the drop-down list.

Address Book policy: This box shows the address book policy applied to the mailbox. An
address book policy allows you to segment users into specific groups to provide
customized views of the address book. To apply or change the address book policy that's
applied to the mailbox, select one from the drop-down list.

Unified Messaging: This feature is disabled by default. When you enable Unified
Messaging (UM) in Exchange 2016, the user will be able to use your organization's UM
features and a default set of UM properties are applied to the user. Click Enable to enable
UM for the mailbox. For information about how to enable UM, see Enable a User for
Unified Messaging. (Note: Unified Messaging is not available in Exchange 2019.)

  ７ Note

  A UM dial plan and a UM mailbox policy must exist before you can enable UM.

Mobile Devices: Use this section to view and change the settings for Exchange
ActiveSync, which is enabled by default. Exchange ActiveSync enables access to an
Exchange mailbox from a mobile device. Click Disable Exchange ActiveSync to disable
this feature for the mailbox.

Outlook Web App: This feature is enabled by default. Outlook on the web provides
access to an Exchange mailbox via a web browser. Click Disable to disable Outlook on the
web for the mailbox. Click Edit details to add or change an Outlook on the web mailbox
policy for the mailbox.

IMAP: This feature is enabled by default. Click Disable to disable IMAP for the mailbox.

POP3: This feature is enabled by default. Click Disable to disable POP3 for the mailbox.

<!-- p.1111 -->

MAPI: This feature is enabled by default. MAPI enables access to an Exchange mailbox
from a MAPI client such as Outlook. Click Disable to disable MAPI for the mailbox.

Litigation hold: This feature is disabled by default. Litigation hold preserves deleted
mailbox items and records changes made to mailbox items. Deleted items and all
instances of changed items are returned in a discovery search. Click Enable to put the
mailbox on litigation hold. If the mailbox is on litigation hold, click Disable to remove the
litigation hold. If the mailbox is on litigation hold, click Edit details to view and change
the following litigation hold settings:

   Hold date: This read-only box indicates date and time when the mailbox was put on
   litigation hold.

   Put on hold by: This read-only box indicates the user who put the mailbox on litigation
   hold.

   Note: Use this box to notify the user about the litigation hold, explain why the mailbox
   is on litigation hold, or provide additional guidance to the user, such as informing
   them that the litigation hold won't affect their day-to-day use of email.

   URL: Use this box to provide a URL to a website that provides information or guidance
   about the litigation hold on the mailbox.

     ７ Note

     The text from these boxes appears in the user's mailbox only if they're using
     Outlook 2010 or later versions. It doesn't appear in Outlook on the web or other
     email clients. To view the text from the Note and URL boxes in Outlook, click the
     File tab and, on the Info page, under Account Settings, you'll see the litigation
     hold comment.

Archiving: If an archive mailbox doesn't exist for the user, this feature is disabled. To
enable an archive mailbox, click Enable. If the user has an archive mailbox, the size of the
archive mailbox and usage statistics are displayed. Click Edit details to view and change
the following archive mailbox settings:

   Status: This read-only box indicates whether an archive mailbox exists.

   Database: This read-only box shows the name of the mailbox database that hosts the
   archive mailbox.

   Name: Type the name of the archive mailbox in this box. This name is displayed under
   the folder list in Outlook or Outlook on the web.

<!-- p.1112 -->

  Quota usage: This read-only area shows the total size of the archive mailbox and the
  percentage of the total archive mailbox quota that has been used.

  Quota value (GB): This box shows the total size of the archive mailbox. To change the
  size, type a new value in the box or select a value from the drop-down list.

  Issue warning at (GB): This box shows the maximum storage limit for the archive
  mailbox before a warning is issued to the user. If the archive mailbox size reaches or
  exceeds the value specified, Exchange sends a warning message to the user. To change
  this limit, type a new value in the box or select a value from the drop-down list.

Delivery Options: Use Delivery Options to forward email messages sent to the user to
another recipient and to set the maximum number of recipients that the user can send a
message to. Click Edit details to view and change these settings.

  Forwarding address: Select the Enable forwarding check box and then click Browse to
  display the Select Mail User and Mailbox page. Use this page to select a recipient to
  whom you want to forward all email messages that are sent to this mailbox. Messages
  will be delivered to both the linked mailbox and the forwarding address.

  Recipient limit: This setting controls the maximum number of recipients the user can
  send a message to. Select the Maximum recipients check box to limit the number of
  recipients allowed on the To:, Cc:, and Bcc: lines of an email message, and then specify
  the maximum number of recipients.

     ７ Note

     For on-premises Exchange organizations, the recipient limit is unlimited. For
     Exchange Online organizations, the limit is 500 recipients.

Message Size Restrictions: These settings control the size of messages that the user can
send and receive. Click Edit details to view and change the maximum size for sent and
received messages.

  Sent messages: To specify a maximum size for messages sent by this user, select the
  Maximum message size (KB) check box and type a value in the box. The message size
  must be between 0 and 2,097,151 KB. If the user sends a message larger than the
  specified size, the message will be returned to the user with a descriptive error
  message.

  Received messages: To specify a maximum size for messages received by this user,
  select the Maximum message size (KB) check box and type a value in the box. The
  message size must be between 0 and 2,097,151 KB. If the user receives a message

<!-- p.1113 -->

        larger than the specified size, the message will be returned to the sender with a
        descriptive error message.

     Message Delivery Restrictions: These settings control who can send email messages to
     this user. Click Edit details to view and change these restrictions.

        Accept messages from: Use this section to specify who can send messages to this
        user.

        All senders: Select this option to specify that the user can accept messages from all
        senders. This includes both senders in your Exchange organization and external
        senders. This option is selected by default. This option includes external users only if
        you clear the Require that all senders are authenticated check box. If you select this
        check box, messages from external users will be rejected.

        Only senders in the following list: Select this option to specify that the user can accept
        messages only from a specified set of senders in your Exchange organization. Click
        Add to display the Select Recipients page, which displays a list of all recipients in your
        Exchange organization. Select the recipients you want, add them to the list, and then
        click OK. You can also search for a specific recipient by typing the recipient's name in
        the search box and then clicking Search.

        Require that all senders are authenticated: Select this option to prevent anonymous
        users from sending messages to the user.

        Reject messages from: Use this section to block people from sending messages to this
        user.

        No senders: Select this option to specify that the mailbox won't reject messages from
        any senders in the Exchange organization. This option is selected by default.

        Senders in the following list: Select this option to specify that the mailbox will reject
        messages from a specified set of senders in your Exchange organization. Click Add to
        display the Select Recipient page, which displays a list of all recipients in your
        Exchange organization. Select the recipients you want to reject messages from, add
        them to the list, and then click OK. You can also search for a specific recipient by
        typing the recipient's name in the search box and then clicking Search.

Member Of

Use the Member Of section to view a list of the distribution groups or security groups to which
this user belongs. You can't change membership information on this page. Note that the user
may match the criteria for one or more dynamic distribution groups in your organization.

<!-- p.1114 -->

However, dynamic distribution groups aren't displayed on this page because their membership
is calculated each time they're used.

MailTip

Use the MailTip section to add a MailTip to alert users of potential issues if they send a
message to this recipient. A MailTip is text that's displayed in the InfoBar when a recipient is
added to the To, Cc, or Bcc lines of a new email message.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Mailbox Delegation

Use the Mailbox Delegation section to assign permissions to other users (also called delegates)
to allow them to sign in to the user's mailbox or send messages on behalf of the user. You can
assign the following permissions:

     Send As: This permission allows users other than the mailbox owner to use the mailbox to
     send messages. After this permission is assigned to a delegate, any message that a
     delegate sends from this mailbox will appear as if it was sent by the mailbox owner.
     However, this permission doesn't allow a delegate to sign in to the user's mailbox.

     Send on Behalf Of: This permission also allows a delegate to use this mailbox to send
     messages. However, after this permission is assigned to a delegate, the From: address in
     any message sent by the delegate indicates that the message was sent by the delegate
     on behalf of the mailbox owner.

     Full Access: This permission allows a delegate to sign in to the user's mailbox and view
     the contents of the mailbox. However, after this permission is assigned to a delegate, the
     delegate can't send messages from the mailbox. To allow a delegate to send email from
     the user's mailbox, you still have to assign the delegate the Send As or the Send on Behalf
     Of permission.

To assign permissions to delegates, click Add under the appropriate permission to display the
Select Recipient page, which displays a list of all recipients in your Exchange organization that
can be assigned the permission. Select the recipients you want assign delegate permissions to,
add them to the list, and then click OK. You can also search for a specific recipient by typing
the recipient's name in the search box and then clicking Search.

<!-- p.1115 -->

Use the Exchange management Shell to change linked
mailbox properties
Use the Get-Mailbox and Set-Mailbox cmdlets to view and change properties for linked
mailboxes. One advantage of using the Exchange Management Shell is the ability to change
the properties for multiple linked mailboxes. For information about what parameters
correspond to mailbox properties, see the following topics:

     Get-Mailbox

     Set-Mailbox

Here are some examples of using the Exchange Management Shell to change linked mailbox
properties.

This example uses the Get-Mailbox command to find all the linked mailboxes in the
organization.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
  'LinkedMailbox'"

This example uses the Set-Mailbox command to limit the number of recipients allowed on the
To:, Cc:, and Bcc: lines of an email message to 500. This limit applies to all linked mailboxes in
the organization.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
  'LinkedMailbox'" | Set-Mailbox -RecipientLimits 500

This example changes the linked master account in the fabrikam.com account forest that is
associated with a linked mailbox in an Exchange forest.

  PowerShell

  Set-Mailbox -Identity "Ayla Kol" -LinkedDomainController DC1.fabrikam.com -
  LinkedMasterAccount "fabrikam\robinw" -LinkedCredential:(Get-Credential
  fabrikam\administrator)

How do you know this worked?
To verify that you have successfully changed properties for a linked mailbox, do the following:

<!-- p.1116 -->

In the EAC, select the linked mailbox and then click Edit to view the property or feature
that you changed. Depending on the property that you changed, it might be displayed in
the Details pane for the selected mailbox.

In the Exchange Management Shell, use the Get-Mailbox cmdlet to verify the changes.
One advantage of using the Exchange Management Shell is that you can view multiple
properties for multiple linked mailboxes. In the example above where the recipient limit
was changed, running the following command will verify the new value.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
  'LinkedMailbox'" | Format-List Name,RecipientLimits

For the example above where the linked master account was changed, run the following
command to verify the new value.

  PowerShell

  Get-Mailbox "Ayla Kol" | Format-List LinkedMasterAccount

<!-- p.1117 -->

Manage distribution groups
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

Use the Exchange admin center (EAC) or the Exchange Management Shell to create a new
distribution group in your Exchange organization or to mail-enable an existing group in Active
Directory.

There are two types of groups that can be used to distribute messages:

      Mail-enabled universal distribution groups (also called distribution groups) can be used
      only to distribute messages.

      Mail-enabled universal security groups (also called security groups) can be used to
      distribute messages as well as to grant access permissions to resources in Active
      Directory. For more information, see Manage mail-enabled security groups in Exchange
      Server.

It's important to note the terminology differences between Active Directory and Exchange. In
Active Directory, a distribution group refers to any group that doesn't have a security context,
whether it's mail-enabled or not. In contrast, in Exchange, all mail-enabled groups are referred
to as distribution groups, whether they have a security context or not.

  ７ Note

  You can create or mail-enable only universal distribution groups. To convert a domain-
  local or a global group to a universal group, you can use the Set-Group cmdlet using the
  Exchange Management Shell. You may have mail-enabled groups that were migrated from
  previous versions of Exchange that are not universal groups. You can use the EAC or the
  Exchange Management Shell to manage these groups

What do you need to know before you begin?
      Estimated time to complete: 2 to 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Distribution groups" entry in the
      Recipients Permissions topic.

      If your organization has configured a group naming policy, it's applied only to groups
      created by users. When you or other administrators use the EAC to create distribution

<!-- p.1118 -->

   groups, the group naming policy is ignored and isn't applied to the group name.
   However, if you use the Exchange Management Shell to create or rename a distribution
   group, the policy is applied unless you use the IgnoreNamingPolicy parameter to override
   the group naming policy. For more information, see:

      Create a Distribution Group Naming Policy

      Override the Distribution Group Naming Policy

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Create a distribution group

Use the EAC to create a distribution group
 1. In the EAC, navigate to Recipients > Groups.

 2. Click New    > Distribution group.

 3. On the New distribution group page, complete the following boxes:

         * Display name: Use this box to type the display name. This name appears in your
         organization's address book, on the To: line when email is sent to this group, and in
         the Groups list in the EAC. The display name is required and should be user-friendly
         so people recognize what it is. It also must be unique in the forest.

         * Alias: Use this box to type the name of the alias for the group. The alias can't
         exceed 64 characters and must be unique in the forest. When a user types the alias
         in the To: line of an email message, it resolves to the group's display name.

         Description: Use this box to describe the group so people know what the purpose
         of the group is. This description appears in the address book.

         Organizational unit: You can select an organizational unit (OU) other than the
         default (which is the recipient scope). If the recipient scope is set to the forest, the
         default value is set to the Users container in the Active Directory domain that
         contains the computer on which the EAC is running. If the recipient scope is set to a

<!-- p.1119 -->

         specific domain, the Users container in that domain is selected by default. If the
         recipient scope is set to a specific OU, that OU is selected by default.

         To select a different OU, click Browse. The dialog box displays all OUs in the forest
         that are within the specified scope. Select the OU you want, and then click OK.

         * Owners: By default, the person who creates a group is the owner. All groups must
         have at least one owner. You can add owners by clicking Add        .

         Members: Use this section to add members and to specify whether approval is
         required for people to join or leave the group.

         Group owners don't have to be members of the group. Use Add group owners as
         members to add or remove the owners as members.

         To add members to the group, click Add       . When you've finished adding members,
         click OK to return to the New distribution group page.

         Under Choose whether owner approval is required to join the group, specify
         whether approval is required for people to join the group. Select one of the
         following settings:

            Open: Anyone can join this group without being approved by the group
            owners: This is the default setting.

            Closed: Members can be added only by the group owners. All requests to join
            will be rejected automatically

         Owner Approval: All requests are manually approved or rejected by the group
         owners: If you select this option, the group owner or owners will receive an email
         message requesting approval to join the group.

         Under Choose whether the group is open to leave, specify whether approval is
         required for people to leave the group. Select one of the following settings:

         Open: Anyone can leave this group without being approved by the group owners:
         This is the default setting.

         Closed: Members can be removed only by the group owners. All requests to leave
         will be rejected automatically

4. When you've finished, click Save to create the distribution group.

７ Note

<!-- p.1120 -->

  By default, new distribution groups require that all senders be authenticated. This prevents
  external senders from sending messages to distribution groups. To configure a
  distribution group to accept messages from all senders, you must modify the message
  delivery restriction settings for that distribution group.

Use the Exchange Management Shell to create a distribution
group
This example creates a distribution group with an alias itadmin and the name IT
Administrators. The distribution group is created in the default OU, and anyone can join this
group without approval by the group owners.

  PowerShell

  New-DistributionGroup -Name "IT Administrators" -Alias itadmin -
  MemberJoinRestriction open

For more information about using the Exchange Management Shell to create distribution
groups, see New-DistributionGroup.

How do you know this worked?
To verify that you've successfully created a distribution group, do one of the following:

     In the EAC, navigate to Recipients > Groups. The new distribution group is displayed in
     the group list. Under Group Type, the type is Distribution group.

     In the Exchange Management Shell, run the following command to display information
     about the new distribution group.

        PowerShell

        Get-DistributionGroup <Name> | Format-List
        Name,RecipientTypeDetails,PrimarySmtpAddress

Change distribution group properties

Use the EAC to change distribution group properties
   1. In the EAC, navigate to Recipients > Groups.
