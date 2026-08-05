---
title: "Exchange Server — pages 1041-1080"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1041-1080
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1041-1080
family: exchange
documentKind: "doc"
abstract: "When you're finished, click Save. Use the Exchange Management Shell to create mailboxes for existing user accounts To create a mailbox for an existing user account, use the following syntax: PowerShell Enable-Mailbox -Identity <Account> [-Alias <Alias>] [-DisplayName <DisplayNam"
---

# Exchange Server — pages 1041-1080

<!-- p.1041 -->

     When you're finished, click Save.

Use the Exchange Management Shell to create mailboxes for
existing user accounts
To create a mailbox for an existing user account, use the following syntax:

  PowerShell

  Enable-Mailbox -Identity <Account> [-Alias <Alias>] [-DisplayName <DisplayName>]
  [-Database <Database>]

This example creates a mailbox in the mailbox database named UsersMailboxDatabase for the
existing user named Kathleen Reiter, whose account name (user principal name) is
kreiter@contoso.com .

     Because we aren't using the Alias parameter, the alias value is kreiter .

     Because we aren't using the DisplayName parameter, the value of the name attribute in
     Active Directory is used as the display name.

  PowerShell

  Enable-Mailbox -Identity kreiter@contoso.com -Database UsersMailboxDatabase

This example finds all user accounts that aren't mail-enabled and that aren't system accounts
(the userPrincipalName attribute isn't blank), and then creates mailboxes for those accounts.

  PowerShell

  Get-User -RecipientTypeDetails User -Filter "UserPrincipalName -ne `$null" -
  ResultSize unlimited | Enable-Mailbox

For detailed syntax and parameter information, see Enable-Mailbox and Get-User.

How do you know that you've created mailboxes for existing
user accounts?
To verify that you've successfully created a mailbox for an existing user, use either of the
following procedures:

     In the EAC, go to Recipients > Mailboxes and verify the mailbox is displayed in the list.

<!-- p.1042 -->

In the Exchange Management Shell, replace <Name> with the name attribute of the user,
and run the following command:

  PowerShell

  Get-Mailbox -Identity <Name> | Format-List
  Name,DisplayName,Alias,PrimarySmtpAddress,Database

<!-- p.1043 -->

Manage user mailboxes
Article • 04/30/2025

APPLIES TO:         2016    2019     Subscription Edition

After you create a user mailbox, you can make changes and set additional properties by using
the EAC or the Exchange Management Shell.

You can also change properties for multiple user mailboxes at the same time. For more
information, see Use the EAC to bulk edit user mailboxes.

What do you need to know before you begin?
      Estimated time to complete each user mailbox task: 2 to 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Change user mailbox properties

Use the EAC to change user mailbox properties
   1. In the EAC, navigate to Recipients > Mailboxes.

   2. In the list of user mailboxes, click the mailbox that you want to change the properties for,
      and then click Edit   .

   3. On the mailbox properties page, click one of the following sections to view or change
      properties.

            General

            Mailbox Usage

<!-- p.1044 -->

          Contact Information

          Organization

          Email Address

          Mailbox Features

          Member Of

          MailTip

          Mailbox Delegation

General

Use the General section to view or change basic information about the user.

     First name, Initials, Last name

     * Name: This is the name that's listed in Active Directory. If you change this name, it can't
     exceed 64 characters.

     * Display name: This name appears in your organization's address book, on the To: and
     From: lines in email, and in the Mailbox list. This name can't contain empty spaces before
     or after the display name.

     * Alias: This specifies the email alias for the user. The user's alias is the portion of the
     email address on the left side of the at (@) symbol. It must be unique in the forest.

     * User logon name: This is the name that the user uses to sign in to their mailbox and to
     log on to the domain. Typically the user logon name consists of the user's alias on the left
     side of the @ symbol, and the domain name in which the user account resides on the
     right side of the @ symbol.

     Require password change on next logon: Select this check box if you want the user to
     reset their password the next time they sign in to their mailbox.

     Hide from address lists: Select this check box to prevent the recipient from appearing in
     the address book and other address lists that are defined in your Exchange organization.
     After you select this check box, users can still send messages to the recipient by using the
     email address.

Click More options to view or change these additional properties:

<!-- p.1045 -->

     Organizational unit: This read-only box displays the organizational unit (OU) that
     contains the user account. You have to use Active Directory Users and Computers to
     move the user account to a different OU.

     Mailbox database: This read-only box displays the name of the mailbox database that
     hosts the mailbox. To move the mailbox to a different database, select it in the mailbox
     list, and then click Move mailbox to another database in the Details pane.

     Custom attributes: This section displays the custom attributes defined for the user
     mailbox. To specify custom attribute values, click Edit. You can specify up to 15 custom
     attributes for the recipient.

Mailbox Usage

Use the Mailbox Usage section to view or change the mailbox storage quota and deleted item
retention settings for the mailbox. These settings are configured by default when the mailbox is
created. They use the values that are configured for the mailbox database and apply to all
mailboxes in that database. You can customize these settings for each mailbox instead of using
the mailbox database defaults.

     Last logon: This read-only box displays the last time that the user signed in to their
     mailbox.

     Mailbox usage: This area shows the total size of the mailbox and the percentage of the
     total mailbox quota that has been used.

  ７ Note

  To obtain the information that's displayed in the previous two boxes, the EAC queries the
  mailbox database that hosts the mailbox. If the EAC is unable to communicate with the
  Exchange store that contains the mailbox database, these boxes will be blank. A warning
  message is displayed if the user hasn't signed in to the mailbox for the first time.

Click More options to view or change the mailbox storage quota and the deleted item
retention settings for the mailbox.

     Storage quota settings: To customize these settings for the mailbox and not use the
     mailbox database defaults, click Customize the settings for this mailbox, type a new
     value, and then click Save.

     The value range for any of the storage quota settings is from 0 through 2047 gigabytes
     (GB).

<!-- p.1046 -->

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
     the mailbox database defaults, click Customize the settings for this mailbox, type a new
     value, and then click Save.

        Keep deleted items for (days): This box displays the length of time that deleted items
        are retained before they are permanently deleted and can't be recovered by the user.
        When the mailbox is created, this value is based on the deleted item retention settings
        configured for the mailbox database. By default, a mailbox database is configured to
        retain deleted items for 14 days. The value range for this property is from 0 through
        24855 days.

        Don't permanently delete items until the database is backed up: Select this check box
        to prevent mailboxes and email messages from being deleted until after the mailbox
        database on which the mailbox is located has been backed up.

Contact Information
Use the Contact Information section to view or change the user's contact information. The
information on this page is displayed in the address book. Click More options to display
additional boxes.

   Tip

  You can use the State/Province box to create recipient conditions for dynamic distribution
  groups, email address policies, or address lists.

Mailbox users can use Outlook or Outlook on the web (formerly known as Outlook Web App)
to view and change their own contact information. But they can't change the information in the

<!-- p.1047 -->

Notes and Web page boxes.

Organization
Use the Organization section to record detailed information about the user's role in the
organization. This information is displayed in the address book. Also, you can create a virtual
organization chart that is accessible from email clients such as Outlook.

     Title: Use this box to view or change the recipient's title.

     Department: Use this box to view or change the department in which the user works. You
     can use this box to create recipient conditions for dynamic distribution groups, email
     address policies, or address lists.

     Company: Use this box to view or change the company for which the user works. You can
     use this box to create recipient conditions for dynamic distribution groups, email address
     policies, or address lists.

     Manager: To add a manager, click Browse. In Select Manager, select a person, and then
     click OK.

     Direct reports: You can't modify this box. A direct report is a user who reports to a specific
     manager. If you've specified a manager for the user, that user appears as a direct report in
     the details of the manager's mailbox. For example, Kari manages Chris and Kate, so Kari's
     mailbox is specified in the Manager box of Chris's mailbox and Kate's mailbox, and Chris
     and Kate appear in the Direct reports box in the properties of Kari's mailbox.

Email Address

Use the Email Address section to view or change the email addresses associated with the user
mailbox. This includes the user's primary SMTP address and any associated proxy addresses.
The primary SMTP address (also known as the default reply address) is displayed in bold text in
the address list, with the uppercase SMTP value in the Type column.

     Add: Click Add      to add a new email address for this mailbox. Select one of following
     address types:

        SMTP: This is the default address type. Click this button and then type the new SMTP
        address in the * Email address box.

        EUM: An EUM (Exchange Unified Messaging) address is used by the Microsoft
        Exchange Unified Messaging service in Exchange 2016 to locate UM-enabled users
        within an Exchange organization. EUM addresses consist of the extension number and

<!-- p.1048 -->

        the UM dial plan for the UM-enabled user. Click this button and type the extension
        number in the Address/Extension box. Then click Browse and select a dial plan for the
        user. (Note: Unified Messaging is not available in Exchange 2019.)

        Custom address type: Click this button and type one of the supported non-SMTP
        email address types in the * Email address box.

            ７ Note

            With the exception of X.400 addresses, Exchange doesn't validate custom
            addresses for proper formatting. You must make sure that the custom address
            you specify complies with the format requirements for that address type.

        Make this the reply address: In Exchange Online, you can select this check box to
        make the new email address the primary SMTP address for the mailbox. This check box
        isn't available in the EAC in Exchange Server.

     Automatically update email addresses based on the email address policy applied to this
     recipient: Select this check box to have the recipient's email addresses automatically
     updated based on changes made to email address policies in your organization. This box
     is selected by default.

Mailbox Features
Use the Mailbox Features section to view or change the following mailbox features and
settings:

     Sharing policy: This box shows the sharing policy applied to the mailbox. A sharing policy
     controls how users in your organization can share calendar and contact information with
     users outside your Exchange organization. The Default Sharing Policy is assigned to
     mailboxes when they are created. To change the sharing policy that's assigned to the
     user, select a different one from the drop-down list.

     Role assignment policy: This box shows the role assignment policy assigned to the
     mailbox. The role assignment policy specifies the role-based access control (RBAC) roles
     that are assigned to the user and control what specific mailbox and distribution group
     configuration settings users can modify. To change the role assignment policy that's
     assigned to the user, select a different one from the drop-down list.

     Retention policy: This box shows the retention policy assigned to the mailbox. A
     retention policy is a group of retention tags that are applied to the user's mailbox. They
     allow you to control how long to keep items in users' mailboxes and define what action to

<!-- p.1049 -->

take on items that have reached a certain age. A retention policy isn't assigned to
mailboxes when they are created. To assign a retention policy to the user, select one from
the drop-down list.

Address book policy: This box shows the address book policy applied to the mailbox. An
address book policy allows you to segment users into specific groups to provide
customized views of the address book. To apply or change the address book policy
applied to the mailbox, select one from the drop-down list.

Unified Messaging (not available in Exchange 2019): This feature is disabled by default.
When you enable Unified Messaging (UM) in Exchange 2016, the user will be able to use
your organization's UM features and a default set of UM properties are applied to the
user. Click Enable to enable UM for the mailbox. For information about how to enable
UM, see Enable a User for Unified Messaging.

  ７ Note

  A UM dial plan and a UM mailbox policy must exist before you can enable UM.

Mobile Devices: Use this section to view and change the settings for Exchange
ActiveSync, which is enabled by default. Exchange ActiveSync enables access to an
Exchange mailbox from a mobile device. Click Disable Exchange ActiveSync to disable
this feature for the mailbox.

Outlook Web App: This feature is enabled by default. Outlook on the web enables access
to an Exchange mailbox from a web browser. Click Disable to disable Outlook on the web
for the mailbox. Click Edit details to add or change an Outlook on the web mailbox policy
for the mailbox.

IMAP: This feature is enabled by default. Click Disable to disable IMAP for the mailbox.

POP3: This feature is enabled by default. Click Disable to disable POP3 for the mailbox.

MAPI: This feature is enabled by default. MAPI enables access to an Exchange mailbox
from a MAPI client such as Outlook. Click Disable to disable MAPI for the mailbox.

Litigation hold: This feature is disabled by default. Litigation hold preserves deleted
mailbox items and records changes made to mailbox items. Deleted items and all
instances of changed items are returned in a discovery search. Click Enable to put the
mailbox on litigation hold. If the mailbox is on litigation hold, click Disable to remove the
litigation hold. Mailboxes on litigation hold are inactive mailboxes and can't be deleted.
To delete the mailbox, remove the litigation hold. If the mailbox is on litigation hold, click
Edit details to view and change the following litigation hold settings:

<!-- p.1050 -->

   Hold date: This read-only box indicates the date and time when the mailbox was put
   on litigation hold.

   Put on hold by: This read-only box indicates the user who put the mailbox on litigation
   hold.

   Note: Use this box to notify the user about the litigation hold, explain why the mailbox
   is on litigation hold, or provide additional guidance to the user, such as informing
   them that the litigation hold won't affect their day-to-day use of email.

   URL: Use this box to provide a URL to a website that provides information or guidance
   about the litigation hold on the mailbox.

     ７ Note

     The text from these boxes appears in the user's mailbox only if they are using
     Outlook 2010 or later versions. It doesn't appear in Outlook on the web or other
     email clients. To view the text from the Note and URL boxes in Outlook, click the
     File tab, and on the Info page, under Account Settings, you'll see the litigation
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

   Archive quota (GB): This box shows the total size of the archive mailbox. To change the
   size, type a new value in the box or select a value from the drop-down list.

   Issue warning at (GB): This box shows the maximum storage limit for the archive
   mailbox before a warning is issued to the user. If the archive mailbox size reaches or
   exceeds the value specified, Exchange sends a warning message to the user. To change
   this limit, type a new value in the box or select a value from the drop-down list.

Delivery Options: Use to forward email messages sent to the user to another recipient
and to set the maximum number of recipients that the user can send a message to. Click

<!-- p.1051 -->

View details to view and change these settings.

  Forwarding address: Select the Enable forwarding check box and then click Browse to
  display the Select Mail User and Mailbox page. Use this page to select a recipient to
  whom you want to forward all email messages that are sent to this mailbox.

  Deliver message to both forwarding address and mailbox: Select this check box so
  that messages will be delivered to both the forwarding address and the user's mailbox.

  Recipient limit: This setting controls the maximum number of recipients the user can
  send a message to. Select the Maximum recipients check box to limit the number of
  recipients allowed in the To:, Cc:, and Bcc: boxes of an email message and then specify
  the maximum number of recipients. For on-premises Exchange organizations, the
  recipient limit is unlimited.

Message Size Restrictions: These settings control the size of messages that the user can
send and receive. Click View details to view and change maximum size for sent and
received messages.

  Sent messages: To specify a maximum size for messages sent by this user, select the
  Maximum message size (KB) check box and type a value in the box. The message size
  must be between 0 and 2,097,151 KB. If the user sends a message larger than the
  specified size, the message will be returned to the user with a descriptive error
  message.

  Received messages: To specify a maximum size for messages received by this user,
  select the Maximum message size (KB) check box and type a value in the box. The
  message size must be between 0 and 2,097,151 KB. If the user receives a message
  larger than the specified size, the message will be returned to the sender with a
  descriptive error message.

Message Delivery Restrictions: These settings control who can send email messages to
this user. Click View details to view and change these restrictions.

  Accept messages from: Use this section to specify who can send messages to this
  user.

  All senders: Select this option to specify that the user can accept messages from all
  senders. This includes both senders in your Exchange organization and external
  senders. This option is selected by default. This option includes external users only if
  you clear the Require that all senders are authenticated check box. If you select this
  check box, messages from external users will be rejected.

<!-- p.1052 -->

        Only senders in the following list: Select this option to specify that the user can accept
        messages only from a specified set of senders in your Exchange organization. Click
        Add      to display the Select Recipients page, which displays a list of all recipients in
        your Exchange organization. Select the recipients you want, add them to the list, and
        then click OK. You can also search for a specific recipient by typing the recipient's
        name in the search box and then clicking Search        .

        Require that all senders are authenticated: Select this option to prevent anonymous
        users from sending messages to the user.

        Reject messages from: Use this section to block people from sending messages to this
        user.

        No senders: Select this option to specify that the mailbox won't reject messages from
        any senders in the Exchange organization. This option is selected by default.

        Senders in the following list: Select this option to specify that the mailbox will reject
        messages from a specified set of senders in your Exchange organization. Click Add
        to display the Select Recipients page, which displays a list of all recipients in your
        Exchange organization. Select the recipients you want, add them to the list, and then
        click OK. You can also search for a specific recipient by typing the recipient's name in
        the search box and then clicking Search      .

Member Of
Use the Member Of section to view a list of the distribution groups or security groups to which
this user belongs. You can't change membership information on this page. Note that the user
may match the criteria for one or more dynamic distribution groups in your organization.
However, dynamic distribution groups aren't displayed on this page because their membership
is calculated each time they are used.

MailTip

Use the MailTip section to add a MailTip to alert users of potential issues if they send a
message to this recipient. A MailTip is text that is displayed in the InfoBar when this recipient is
added to the To, Cc, or Bcc boxes of a new email message.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

<!-- p.1053 -->

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

To assign permissions to delegates, click Add     under the appropriate permission to display a
page that displays a list of all recipients in your Exchange organization that can be assigned the
permission. Select the recipients you want, add them to the list, and then click OK. You can also
search for a specific recipient by typing the recipient's name in the search box and then clicking
Search    .

Use the Exchange Management Shell to change user mailbox
properties
Use the Get-Mailbox and Set-Mailbox cmdlets to view and change properties for user
mailboxes. One advantage of using the Exchange Management Shell is the ability to change
the properties for multiple mailboxes. For information about what parameters correspond to
mailbox properties, see the following topics:

     Get-Mailbox

     Set-Mailbox

Here are some examples of using the Exchange Management Shell to change user mailbox
properties.

<!-- p.1054 -->

This example shows how to forward Pat Coleman's email messages to Sunil Koduri's
(sunilk@contoso.com) mailbox.

  PowerShell

  Set-Mailbox -Identity patc -DeliverToMailboxAndForward $true -ForwardingAddress
  sunilk@contoso.com

This example uses the Get-Mailbox command to find all user mailboxes in the organization,
and then uses the Set-Mailbox command to set the recipient limit to 500 recipients allowed in
the To:, Cc:, and Bcc: boxes of an email message.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -RecipientLimits 500

This example uses the Get-Mailbox command to find all the mailboxes in the Marketing
organizational unit, and then uses the Set-Mailbox command to configure these mailboxes.
The custom warning, prohibit send, and prohibit send and receive limits are set to 200
megabytes (MB), 250 MB, and 280 MB respectively, and the mailbox database's default limits
are ignored. This command can be used to configure a specific set of mailboxes to have larger
or smaller limits than other mailboxes in the organization.

  PowerShell

  Get-Mailbox -OrganizationalUnit "Marketing" | Set-Mailbox -IssueWarningQuota
  209715200 -ProhibitSendQuota 262144000 -ProhibitSendReceiveQuota 293601280 -
  UseDatabaseQuotaDefaults $false

This example uses the Get-Mailbox cmdlet to find all users in the Customer Service
department, and then uses the Set-Mailbox cmdlet to change the maximum message size for
sending messages to 2 MB.

  PowerShell

  Get-Mailbox -Filter "Department -eq 'Customer Service'" | Set-Mailbox -MaxSendSize
  2097152

This example sets the MailTip translation in French and Chinese.

  PowerShell

<!-- p.1055 -->

  Set-Mailbox john@contoso.com -MailTipTranslations ("FR: C'est la langue
  française", "CHT: 這是漢語語言")

How do you know this worked?
To verify that you've successfully changed properties for a user mailbox, do the following:

     In the EAC, select the mailbox and then click Edit    to view the property or feature that
     you changed. Depending on the property that you changed, it might be displayed in the
     Details pane for the selected mailbox.

     In the Exchange Management Shell, use the Get-Mailbox cmdlet to verify the changes.
     One advantage of using the Exchange Management Shell is that you can view multiple
     properties for multiple mailboxes. In the example above where the recipient limit was
     changed, run the following command to verify the new value.

        PowerShell

        Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
        'UserMailbox'" | Format-List Name,RecipientLimits

     For the example above where the message limits were changed, run this command.

        PowerShell

        Get-Mailbox -OrganizationalUnit "Marketing" | Format-List
        Name,IssueWarningQuota,ProhibitSendQuota,ProhibitSendReceiveQuota,UseDatabase
        QuotaDefaults

Bulk edit user mailboxes
You can use the EAC to change the properties for multiple user mailboxes. When you select
two or more user mailboxes from the mailbox list in the EAC, the properties that can be bulk
edited are displayed in the Details pane. When you change one of these properties, the change
is applied to all selected mailboxes.

Here's a list of the user mailbox properties and features that can be bulk edited. Note that not
all properties in each area are available to be changed.

     Contact Information: Change shared properties such as street, postal code, and city
     name.

<!-- p.1056 -->

    Organization: Change shared properties such as department name, company name, and
    the manager that the selected users report to.

    Custom attributes: Change or add values for custom attributes 1 - 15.

    Mailbox quota: Change the mailbox quota values and the retention period for deleted
    items.

    Email connectivity: Enable or disable Outlook on the web, POP3, IMAP, MAPI, and
    Exchange ActiveSync.

    Archive: Enable or disable the archive mailbox.

    Retention policy, role assignment policy, and sharing policy: Update the settings for
    each of these mailbox features.

    Move mailboxes to another database: Move the selected mailboxes to a different
    database.

    Delegate permissions: Assign permissions to users or groups that allow them to open or
    send messages from other mailboxes. You can assign Full, Send As and Send on Behalf
    permissions to users or groups. Check out Manage permissions for recipients for more
    details.

 ７ Note

 The estimated time to complete this task is 2 minutes, but may take longer if you change
 multiple properties or features.

Use the EAC to bulk edit user mailboxes
 1. In the EAC, navigate to Recipients > Mailboxes.

 2. In the list of mailboxes, select two or more mailboxes.

       Tip

      You can select multiple adjacent mailboxes by holding down the Shift key and
      clicking the first mailbox, and then clicking the last mailbox you want to edit. You can
      also select multiple non-adjacent mailboxes by holding down the Ctrl key and
      clicking each mailbox that you want to edit.

<!-- p.1057 -->

   3. In the Details pane, under Bulk Edit, select the mailbox properties or feature that you
     want to edit.

   4. Make the changes on the properties page and then save your changes.

How do you know this worked?
To verify that you've successfully bulk edited user mailboxes, do one of the following:

     In the EAC, select each of the mailboxes that you bulk edited and then click Edit      to
     view the property or feature that you changed.

     In the Exchange Management Shell, use the Get-Mailbox cmdlet to verify the changes.
     One advantage of using the Exchange Management Shell is that you can view multiple
     properties for multiple mailboxes. For example, say you used the bulk edit feature in the
     EAC to enable the archive mailbox and assign a retention policy to all users in your
     organization. To verify these changes, you could run the following command:

       PowerShell

        Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
        'UserMailbox'" | Format-List Name,ArchiveDatabase,RetentionPolicy

     For more information about the available parameters for the Get-Mailbox cmdlet, see
     Get-Mailbox.

<!-- p.1058 -->

Add/remove email addresses for a mailbox
Article • 04/30/2025

APPLIES TO:        2016      2019       Subscription Edition

You can use the EAC or the Exchange Management Shell to add or remove an email address for
a user mailbox. You can configure more than one email address for the same mailbox. The
additional addresses are called proxy addresses. A proxy address lets a user receive email that's
sent to a different email address. Any email message sent to the user's proxy address is
delivered to their primary email address, which is also known as the primary SMTP address or
the default reply address.

  ７ Note

  The procedures in this topic show how to add or remove email addresses for a user
  mailbox. You can use similar procedures to add or remove email addresses for other
  recipient types.

For additional management tasks related to managing recipients, see the "Recipients
documentation" table in Recipients.

What do you need to know before you begin?
      Estimated time to complete each procedure: 2 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online          , or Exchange Online Protection .

<!-- p.1059 -->

Add an email address to a user mailbox

Use the EAC to add an email address
   1. In the EAC, navigate to Recipients > Mailboxes.

   2. In the list of user mailboxes, click the mailbox that you want to add an email address to,
     and then click Edit   .

   3. On the mailbox properties page, click Email Address.

        ７ Note

        On the Email Address page, the primary SMTP address is displayed in bold text in
        the address list, with the uppercase SMTP value in the Type column.

   4. Click Add   , and then click SMTP to add an SMTP email address to this mailbox.

        ７ Note

        SMTP is the default email address type. You can also add Exchange Unified
        Messaging (EUM) addresses or custom addresses to a mailbox in Exchange 2016. For
        more information, see "Change user mailbox properties" in the Manage user
        mailboxes topic. (Note: Unified Messaging is not available in Exchange 2019.)

   5. Type the new SMTP address in the Email address box, and then click OK.

     The new address is displayed in the list of email addresses for the selected mailbox.

   6. Click Save to save the change.

Use the Exchange Management Shell to add an email address
The email addresses associated with a mailbox are contained in the EmailAddresses property
for the mailbox. Because it can contain more than one email address, the EmailAddresses
property is known as a multivalued property. The following examples show different ways to
modify a multivalued property.

This example shows how to add an SMTP address to the mailbox of Dan Jump.

  PowerShell

<!-- p.1060 -->

     Set-Mailbox "Dan Jump" -EmailAddresses @{add="dan.jump@northamerica.contoso.com"}

This example shows how to add multiple SMTP addresses to a mailbox.

  PowerShell

     Set-Mailbox "Dan Jump" -EmailAddresses
     @{add="dan.jump@northamerica.contoso.com","danj@tailspintoys.com"}

For more information about how to use this method of adding and removing values for
multivalued properties, see Modifying Multivalued Properties.

This example shows another way to add email addresses to a mailbox by specifying all
addresses associated with the mailbox. In this example, danj@tailspintoys.com is the new email
address that you want to add. The other two email addresses are existing addresses. The
address with the case-sensitive qualifier SMTP is the primary SMTP address. You have to include
all email addresses for the mailbox when you use this command syntax. If you don't, the
addresses specified in the command will overwrite the existing addresses.

  PowerShell

     Set-Mailbox "Dan Jump" -EmailAddresses
     "SMTP:dan.jump@contoso.com","dan.jump@northamerica.contoso.com","danj@tailspintoys
     .com"

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To verify that you've successfully added an email address to a mailbox, do one of the following:

       In the EAC, navigate to Recipients > Mailboxes, click the mailbox, and then click Edit   .

       On the mailbox properties page, click Email Address.

       In the list of email addresses for the mailbox, verify that the new email address is
       included.

Or

       Run the following command in the Exchange Management Shell.

         PowerShell

<!-- p.1061 -->

        Get-Mailbox <identity> | Format-List EmailAddresses

     Verify that the new email address is included in the results.

Remove an email address from a user mailbox

Use the EAC to remove an email address
   1. In the EAC, navigate to Recipients > Mailboxes.

   2. In the list of user mailboxes, click the mailbox that you want to remove an email address
     from, and then click Edit   .

   3. On the mailbox properties page, click Email Address.

   4. In the list of email addresses, select the address you want to remove, and then click
     Remove     .

   5. Click Save to save the change.

Use the Exchange Management Shell to remove an email
address
This example shows how to remove an email address from the mailbox of Janet Schorr.

  PowerShell

  Set-Mailbox "Janet Schorr" -EmailAddresses @{remove="janets@corp.contoso.com"}

This example shows how to remove multiple addresses from a mailbox.

  PowerShell

  Set-Mailbox "Janet Schorr" -EmailAddresses
  @{remove="janet.schorr@corp.contoso.com","janets@tailspintoys.com"}

For more information about how to use this method of adding and removing values for
multivalued properties, see Modifying Multivalued Properties.

You can also remove an email address by omitting it from the command to set email addresses
for a mailbox. For example, let's say Janet Schorr's mailbox has three email addresses:
janets@contoso.com (the primary SMTP address), janets@corp.contoso.com, and

<!-- p.1062 -->

janets@tailspintoys.com. To remove the address janets@corp.contoso.com, you would run the
following command.

  PowerShell

     Set-Mailbox "Janet Schorr" -EmailAddresses
     "SMTP:janets@contoso.com","janets@tailspintoys.com"

Because janets@corp.contoso.com was omitted in the previous command, it's removed from
the mailbox.

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To verify that you've successfully removed an email address from a mailbox, do one of the
following:

       In the EAC, navigate to Recipients > Mailboxes, click the mailbox, and then click Edit      .

       On the mailbox properties page, click Email Address.

       In the list of email addresses for the mailbox, verify that the email address isn't included.

Or

       Run the following command in the Exchange Management Shell.

         PowerShell

         Get-Mailbox <identity> | Format-List EmailAddresses

       Verify that the email address isn't included in the results.

Use the Exchange Management Shell to add email
addresses to multiple mailboxes
You can add a new email address to multiple mailboxes at one time by using the Exchange
Management Shell and a comma separated values (CSV) file.

This example imports data from C:\Users\Administrator\Desktop\AddEmailAddress.csv, which
has the following format.

  CSV

<!-- p.1063 -->

     Mailbox,NewEmailAddress
     Dan Jump,danj@northamerica.contoso.com
     David Pelton,davidp@northamerica.contoso.com
     Kim Akers,kima@northamerica.contoso.com
     Janet Schorr,janets@northamerica.contoso.com
     Jeffrey Zeng,jeffreyz@northamerica.contoso.com
     Spencer Low,spencerl@northamerica.contoso.com
     Toni Poe,tonip@northamerica.contoso.com
     ...

Run the following command to use the data in the CSV file to add the email address to each
mailbox specified in the CSV file.

  PowerShell

     Import-CSV "C:\Users\Administrator\Desktop\AddEmailAddress.csv" | foreach {Set-
     Mailbox $_.Mailbox -EmailAddresses @{add=$_.NewEmailAddress}}

  ７ Note

  The column names in the first row of this CSV file ( Mailbox,NewEmailAddress ) are arbitrary.
  Whatever you use for column names, make sure you use the same column names in the
  Exchange Management Shell command.

How do you know this worked?
To verify that you've successfully added an email address to multiple mailboxes, do one of the
following:

       In the EAC, navigate to Recipients > Mailboxes, click a mailbox that you added the
       address to, and then click Edit   .

       On the mailbox properties page, click Email Address.

       In the list of email addresses for the mailbox, verify that the new email address is
       included.

Or

       Run the following command in the Exchange Management Shell, using the same CSV file
       that you used to add the new email address.

         PowerShell

<!-- p.1064 -->

  Import-CSV "C:\Users\Administrator\Desktop\AddEmailAddress.csv" | foreach
  {Get-Mailbox $_.Mailbox | Format-List Name,EmailAddresses}

Verify that the new email address is included in the results for each mailbox.

<!-- p.1065 -->

Configure email forwarding for a mailbox
07/23/2025

APPLIES TO:       2016     2019       Subscription Edition

Email forwarding lets you to set up a mailbox to forward email messages sent to a user's
mailbox to another user's mailbox in or outside of your organization.

Use the Exchange admin center and the Exchange
Management Shell
You can use either the Exchange admin center (EAC) or Exchange Management Shell to set up
email forwarding.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Recipient Provisioning Permissions" entry in the
Recipients Permissions topic.

Use the Exchange admin center to set up email forwarding
   1. In the Exchange admin center, navigate to Recipients > Mailboxes.

   2. In the list of user mailboxes, click or tap the mailbox that you want to set up mail
     forwarding for, and then click or tap Edit    .

   3. On the mailbox properties page, click Mailbox Features.

   4. Under Mail Flow, select View details to view or change the setting for forwarding email
     messages.

     On this page, you can set the maximum number of recipients that the user can send a
     message to. The recipient limit is unlimited by default. If you want to specify a limit, click
     the Maximum recipients check box and then type the limit in the text box beneath the
     check box.

   5. Check the Enable forwarding check box, and then click or tap Browse.

   6. On the Select Recipient page, select a user you want to forward all email to. Select the
     Deliver message to both forwarding address and mailbox check box if you want both
     the recipient and the forwarding email address to get copies of the emails sent. Click or
     tap OK, and then click or tap Save.

<!-- p.1066 -->

  ７ Note

  What if you want to forward emails to an email address outside your organization? You
  can use the Exchange Management Shell to do this. See the following example in "Use the
  Exchange Management Shell to configure mail forwarding".

Use the Exchange Management Shell to set up mail
forwarding
Haven't used Exchange Management Shell much? Check out the Exchange Management Shell
topic to learn more. Take a look at the Get-Mailbox and Set-Mailbox topics for more details on
the cmdlets used here.

This example delivers email to the mailbox of Douglas Kohn and also forwards all mail sent to
Douglas Kohn to an external email address, douglaskohn.parents@fineartschool.net.

  PowerShell

  Set-Mailbox -Identity "Douglas Kohn" -DeliverToMailboxAndForward $true -
  ForwardingSMTPAddress "douglaskohn.parents@fineartschool.net"

This example forwards all email sent to the mailbox of Ken Sanchez, an employee of Contoso
Suites, to one of his coworkers, pilarp@contoso.com.

  PowerShell

  Set-Mailbox -Identity "Ken Sanchez" -ForwardingAddress "pilarp@contoso.com"

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To make sure that you've successfully set up email forwarding, do one of the following:

   1. In the Exchange admin center, go to Recipients > Mailboxes.

   2. In the list of user mailboxes, click or tap the mailbox that you configured email forwarding
     for, and then click Edit   .

   3. On the mailbox properties page, click or tap Mailbox Features.

   4. Under Mail Flow, click or tap View details to view the mail forwarding settings.

<!-- p.1067 -->

Or

Run the following command in the Exchange Management Shell.

  PowerShell

     Get-Mailbox <identity> | Format-List
     ForwardingSMTPAddress,DeliverToMailboxandForward

Make sure that the forwarding address is listed in the ForwardingSMTPAddress parameter. Also,
if the DeliverToMailboxAndForward parameter is set to $true , messages will be delivered to the
mailbox and to the forwarding address. If the parameter is set to $false , messages are
delivered only to the forwarding address.

End users
Check out the following topics on how to forward your email to another email address by
using Outlook and Outlook Web App.

       Forward email to another email account

       Manage email messages by using rules

Additional information
For information about keyboard shortcuts that may apply to the procedures in this topic, see
Keyboard shortcuts in the Exchange admin center.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.1068 -->

Configure message delivery restrictions for
a mailbox
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

You can use the EAC or the Exchange Management Shell to place restrictions on whether
messages are delivered to individual recipients. Message delivery restrictions are useful to
control who can send messages to users in your organization. For example, you can configure a
mailbox to accept or reject messages sent by specific users or to accept messages only from
users in your Exchange organization.

The message delivery restrictions covered in this topic apply to all recipient types. To learn
more about the different recipient types, see Recipients.

For additional management tasks related to recipients, see the following topics:

      Manage user mailboxes

      Manage distribution groups

      Manage dynamic distribution groups

      Manage mail users

      Manage mail contacts

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

<!-- p.1069 -->

Use the EAC to place message delivery restrictions
 1. In the EAC, navigate to Recipients > Mailboxes.

 2. In the list of user mailboxes, click the mailbox that you want to set up message delivery
   restrictions for, and then click Edit   .

 3. On the mailbox properties page, click Mailbox Features.

 4. Under Message Delivery Restrictions, click View details to view and change the following
   delivery restrictions:

        Accept messages from: Use this section to specify who can send messages to this
        user.

        All senders: This option specifies that the user can accept messages from all
        senders. This includes both senders in your Exchange organization and external
        senders. This is the default option. It includes external users only if you clear the
        Require that all senders are authenticated check box. If you select this check box,
        messages from external users will be rejected.

        Only senders in the following list: This option specifies that the user can accept
        messages only from a specified set of senders in your Exchange organization. Click
        Add      to display a list of all recipients in your Exchange organization. Select the
        recipients you want, add them to the list, and then click OK. You can also search for
        a specific recipient by typing the recipient's name in the search box and then
        clicking Search     .

        Require that all senders are authenticated: This option prevents anonymous users
        from sending messages to the user. This includes external users that are outside of
        your Exchange organization.

        Reject messages from: Use this section to block people from sending messages to
        this user.

        No senders: This option specifies that the mailbox won't reject messages from any
        senders in the Exchange organization. This is the default option.

        Senders in the following list: This option specifies that the mailbox will reject
        messages from a specified set of senders in your Exchange organization. Click Add
            to display a list of all recipients in your Exchange organization. Select the
        recipients you want, add them to the list, and then click OK. You can also search for
        a specific recipient by typing the recipient's name in the search box and then
        clicking Search     .

<!-- p.1070 -->

   5. Click OK to close the Message Delivery Restrictions page, and then click Save to save
     your changes.

Use the Exchange Management Shell to place
message delivery restrictions
The following examples show how to use the Exchange Management Shell to configure
message delivery restrictions for a mailbox. For other recipient types, use the corresponding
Set- cmdlet with the same parameters.

This example configures the mailbox of Robin Wood to accept messages only from the users
Lori Penor, Jeff Phillips, and members of the distribution group Legal Team 1.

  PowerShell

  Set-Mailbox -Identity "Robin Wood" -AcceptMessagesOnlyFrom "Lori Penor","Jeff
  Phillips" -AcceptMessagesOnlyFromDLMembers "Legal Team 1"

  ７ Note

  If you're configuring a mailbox to accept messages only from individual senders, you have
  to use the AcceptMessagesOnlyFrom parameter. If you're setting up a mailbox to accept
  messages only from senders that are members of a specific distribution group, use the
  AcceptMessagesOnlyFromDLMembers parameter.

This example adds the user named David Pelton to the list of users whose messages will be
accepted by the mailbox of Robin Wood.

  PowerShell

  Set-Mailbox -Identity "Robin Wood" -AcceptMessagesOnlyFrom @{add="David Pelton"}

This example configures the mailbox of Robin Wood to require all senders to be authenticated.
This means the mailbox will only accept messages sent by other users in your Exchange
organization.

  PowerShell

  Set-Mailbox -Identity "Robin Wood" -RequireSenderAuthenticationEnabled $true

<!-- p.1071 -->

This example configures the mailbox of Robin Wood to reject messages from the users Joe
Healy, Terry Adams, and members of the distribution group Legal Team 2.

  PowerShell

  Set-Mailbox -Identity "Robin Wood" -RejectMessagesFrom "Joe Healy","Terry Adams" -
  RejectMessagesFromDLMembers "Legal Team 2"

This example configures the mailbox of Robin Wood to also reject messages sent by members
of the group Legal Team 3.

  PowerShell

  Set-Mailbox -Identity "Robin Wood" -RejectMessagesFromDLMembers @{add="Legal Team
  3"}

  ７ Note

  If you're setting up a mailbox to reject messages from individual senders, you have to use
  the RejectMessagesFrom parameter. If you're setting up a mailbox to reject messages from
  senders that are members of a specific distribution group, use the
  RejectMessagesFromDLMembers parameter.

For detailed syntax and parameter information related to placing delivery restrictions for
different types of recipients, see the following topics:

     Set-DistributionGroup

     Set-DynamicDistributionGroup

     Set-Mailbox

     Set-MailContact

     Set-MailUser

How do you know this worked?
To verify that you've successfully placed message delivery restrictions for a user mailbox, do
one the following:

   1. In the EAC, navigate to Recipients > Mailboxes.

<!-- p.1072 -->

     2. In the list of user mailboxes, click the mailbox that you want to verify the message
       delivery restrictions for, and then click Edit   .

     3. On the mailbox properties page, click Mailbox Features.

     4. Under Message Delivery Restrictions, click View details to verify the delivery restrictions
       for the mailbox.

Or

Run the following command in the Exchange Management Shell.

  PowerShell

     Get-Mailbox <identity> | Format-List
     AcceptMessagesOnlyFrom,AcceptMessagesOnlyFromDLMembers,RejectMessagesFrom,RejectMe
     ssagesFromDLMembers,RequireSenderAuthenticationEnabled

<!-- p.1073 -->

Configure message size limits for a mailbox
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Message size limits control the size of messages that a user can send and receive. By default,
when a mailbox is created, there isn't a size limit for sent and received messages.

Keep in mind that there are other settings in an Exchange organization that determine the
maximum message size a mailbox can send and receive (for example, the maximum message
size configured on a Mailbox server). To learn more about the message size restrictions in
Exchange, including the types of message size limits, their scope, and the order of precedence,
see Message size and recipient limits in Exchange Server.

For additional management tasks related to user mailboxes, see Manage user mailboxes.

  ７ Note

  You can also control the size of messages sent and received by mail users and from shared
  mailboxes.

What do you need to know before you begin?
      Estimated time to complete: 2 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.1074 -->

Use the EAC to set message size limits
   1. In the EAC, navigate to Recipients > Mailboxes.

   2. In the list of user mailboxes, click the mailbox that you want to change the message size
     limits for, and then click Edit    .

   3. On the mailbox properties page, click Mailbox Features.

   4. Under Message Size Restrictions, click View details to view and change the following
     message size limits:

             Sent messages: To set a maximum size for messages sent by this user, select the
             Maximum message size (KB) check box and type a value in the box. The message
             size must be between 0 and 2,097,151 KB. If the user sends a message larger than
             the specified size, the message will be returned to the user with a descriptive error
             message.

             Received messages: To set a maximum size for messages received by this user,
             select the Maximum message size (KB) check box and type a value in the box. The
             message size must be between 0 and 2,097,151 KB. If the user receives a message
             larger than the specified size, the message will be returned to the sender with a
             descriptive error message.

   5. Click OK, and then click Save to save your changes.

Use the Exchange Management Shell to configure
message size limits
This example sets the maximum size for sent messages to 25 MB and the maximum size for
received messages to 35 MB for the mailbox of Debra Garcia.

  PowerShell

  Set-Mailbox -Identity "Debra Garcia" -MaxSendSize 25mb -MaxReceiveSize 35mb

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To verify that you've successfully set up message size limits for a mailbox, do one of the
following:

<!-- p.1075 -->

1. In the EAC, navigate to Recipients > Mailboxes.

2. In the list of user mailboxes, click the mailbox that you want to verify the message size
  limits for, and then click Edit   .

3. On the mailbox properties page, click Mailbox Features.

4. Under Message Size Restrictions, click View details to verify the message size limits for
  the mailbox.

  Or

  Run the following command in the Exchange Management Shell.

    PowerShell

       Get-Mailbox -Identity <Identity> | Format-List MaxSendSize,MaxReceiveSize

<!-- p.1076 -->

Configure storage quotas for a mailbox in
Exchange Server
Article • 04/30/2025 • Applies to: Exchange Server 2013, Exchange Server 2016, Exchange Server 2019

APPLIES TO:        2016      2019       Subscription Edition

   Tip

  This article applies to on-premises Exchange servers. The cloud version of this article is
  available at Increase or customize Exchange Online mailbox size.

You can use the Exchange admin center (EAC) or the Exchange Management Shell to customize
the mailbox storage quotas for specific mailboxes. Storage quotas let you control the size of
mailboxes and manage the growth of mailbox databases. When a mailbox reaches or exceeds a
specified storage quota, Exchange sends a descriptive notification to the mailbox owner.

Typically, you configure storage quotas on mailbox databases, because the quotas apply to all
existing and future mailboxes in the database. For more information, see Manage mailbox
databases in Exchange Server.

This article shows you how to customize storage settings for specific mailboxes that override
the storage settings from the mailbox database. For more management tasks related to user
mailboxes, see Manage user mailboxes.

What do you need to know before you begin?
     Estimated time to complete: 2 minutes.
     To open the Exchange admin center (EAC), see Exchange admin center in Exchange
     Server. To open the Exchange Management Shell, see Open the Exchange Management
     Shell.
     You need to be assigned permissions before you can perform these procedures. To see
     what permissions you need, see the "Recipient Provisioning Permissions" section in the
     Recipients Permissions article.
     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum .

<!-- p.1077 -->

Use the EAC to set storage quotas for a mailbox
 1. In the EAC, go to Recipients > Mailboxes tab.

 2. On the Mailboxes tab, select the mailbox that you want to modify, and then select
   Edit.

 3. On the mailbox properties page that opens, select the Mailbox usage tab, and then select
   More options to show the mailbox quota settings.

 4. On the Mailbox usage tab, select Customize the quota settings for this mailbox, and
   then configure the following settings:

           Issue a warning at (GB): At this mailbox size, the user receives a descriptive warning
           message.

             ７ Note

             The warning message isn't sent unless the Issue a warning value is at least 50%
             of the Prohibit send value. For example, if the Prohibit send value is 800 MB,
             the Issue warning value must be at least 400 MB. Otherwise, the warning
             message isn't sent.

           Prohibit send at (GB): At this mailbox size, Exchange prevents the user from sending
           new messages from the mailbox and displays a descriptive error message.

           Prohibit send and receive at (GB): At this mailbox size, Exchange prevents the user
           from sending messages from the mailbox and doesn't deliver new messages to the
           mailbox. Any messages sent to the mailbox are returned to the sender in a
           descriptive nondelivery report (also known as an NDR or bounce message).

   Valid values for these quotas are:

           0 through 2,047 gigabytes (GB).
           The value unlimited.

   When you're finished on the Mailbox usage tab, select Save.

Use the EAC to set storage quotas for many
mailboxes
 1. In the EAC, go to Recipients > Mailboxes tab.

<!-- p.1078 -->

 2. On the Mailboxes tab, do one of the following steps:

        Press and hold the CTRL key, and then individually select the mailboxes to modify.
        To select a continuous range of mailboxes, select a mailbox, press and hold the
        SHIFT key, and then select another mailbox farther down in the list.

 3. In the details pane, select Update in the Mailbox quota section.

 4. On the Bulk edit mailbox quota page that opens, configure the following settings:

        Issue a warning at (GB)
        Prohibit send at (GB)
        Prohibit send and receive at (GB)

   When you're finished on the Bulk edit mailbox quota page, select Save.

      Tip

     Although the Customize the quota settings for this mailbox isn't available on the
     Bulk edit mailbox quota page, entering a value for one of the quotas automatically
     selects the setting.

Use the Exchange Management Shell to configure
storage quotas for a mailbox

<!-- p.1079 -->

To configure storage quotas for an individual mailbox, use the following syntax:

  PowerShell

  Set-Mailbox -Identity "<MailboxIdentity>" -UseDatabaseQuotaDefaults $false -
  IssueWarningQuota <ValueInMBorGB> -ProhibitSendQuota <ValueInMBorGB> -
  ProhibitSendReceiveQuota <ValueInMBorGB>

     <MailboxIdentity> is any value that uniquely identifies the mailbox. For example, name,
     distinguished name (DN), alias, user principal name (UPN), or email address. Quotation
     marks are required for values that contain spaces.
     The value $false for the UseDatabaseQuotaDefaults parameter is required so the custom
     storage quotas override the mailbox database defaults.

This example sets the specified quotas for Joe Healy's mailbox.

  PowerShell

  Set-Mailbox -Identity "Joe Healy" -UseDatabaseQuotaDefaults $false -
  IssueWarningQuota 24.5GB -ProhibitSendQuota 24.75GB -ProhibitSendReceiveQuota 25GB

This example sets the specified quotas for Ayla Kol's mailbox.

  PowerShell

  Set-Mailbox -Identity "Ayla Kol" -UseDatabaseQuotaDefaults $false -
  IssueWarningQuota 900MB -ProhibitSendQuota 950MB -ProhibitSendReceiveQuota 1GB

For detailed syntax and parameter information, see Set-Mailbox.

Use the Exchange Management Shell to configure
storage quotas for many mailboxes
To configure storage quotas for many mailboxes at the same time, you have the following
options:

     Filter mailboxes based on an existing attribute: This method assumes the target
     mailboxes all share a unique filterable attribute. Some attributes (for example, Title,
     Department, address information, and telephone number) are available only from the
     Get-User cmdlet. Other attributes (for example, CustomAttribute1 to CustomAttribute15)
     are available only from the Get-Mailbox cmdlet.
     Use a list of specific mailboxes: After you generate the list of specific mailboxes, you can
     use that list to configure the mailbox storage quotas.

<!-- p.1080 -->

Filter mailboxes based on an existing attribute

   Tip

  If you're using the Get-User cmdlet to identify the target mailboxes, be sure to use an
  identity property that's available and acceptable to the Get-User and Set-Mailbox cmdlets
  that don't require quotation marks around the values (for example, UserPrincipalName).

To configure storage quotas for any number of mailboxes based on an existing attribute, use
the following syntax:

  PowerShell

  $<VariableName> = <Get-Mailbox | Get-User> -ResultSize unlimited -Filter <Filter>

  $<VariableName> | foreach {Set-Mailbox -Identity $_.UserPrincipalName -
  UseDatabaseQuotaDefaults $false -IssueWarningQuota <ValueInMBorGB> -
  ProhibitSendQuota <ValueInMBorGB> -ProhibitSendReceiveQuota <ValueInMBorGB>}

This example configures storage quotas for all user mailboxes where the associated user's Title
attribute contains the value "Sales Associate".

  PowerShell

  $SA = Get-User -ResultSize unlimited -Filter "(RecipientType -eq 'UserMailbox') -
  and (Title -like 'Sales Associate*')"

  $SA | foreach {Set-Mailbox -Identity $_.UserPrincipalName -
  UseDatabaseQuotaDefaults $false -IssueWarningQuota 24.5GB -ProhibitSendQuota
  24.75GB -ProhibitSendReceiveQuota 25GB}

Use a list of specific mailboxes
To configure storage quotas for a list of specific mailboxes, use the following syntax:

  PowerShell

  $<VariableName> = Get-Content <text file>

  $<VariableName> | foreach {Set-Mailbox -Identity $_ -UseDatabaseQuotaDefaults
  $false -IssueWarningQuota <ValueInMBorGB> -ProhibitSendQuota <ValueInMBorGB> -
  ProhibitSendReceiveQuota <ValueInMBorGB>}
