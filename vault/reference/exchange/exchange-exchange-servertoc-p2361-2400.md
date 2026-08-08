---
title: "Exchange Server — pages 2361-2400"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2361-2400
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2361-2400
family: exchange
documentKind: "doc"
abstract: "To disable admin audit logging, use the following command. PowerShell Set-AdminAuditLogConfig -AdminAuditLogEnabled $false Enable admin audit logging To enable admin audit logging, use the following command. PowerShell Set-AdminAuditLogConfig -AdminAuditLogEnabled $true View adm"
---

# Exchange Server — pages 2361-2400

<!-- p.2361 -->

To disable admin audit logging, use the following command.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogEnabled $false

Enable admin audit logging
To enable admin audit logging, use the following command.

  PowerShell

  Set-AdminAuditLogConfig -AdminAuditLogEnabled $true

View admin audit logging settings
To view the admin audit logging settings that you've configured for your organization, use the
following command.

  PowerShell

  Get-AdminAuditLogConfig

<!-- p.2362 -->

Mailbox audit logging in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Because mailboxes can contain sensitive, high business impact (HBI) information and
personally identifiable information (PII), it's important that you track who logs on to the
mailboxes in your organization and what actions are taken. It's especially important to track
access to mailboxes by users other than the mailbox owner. These users are referred to as
delegate users.

By using mailbox audit logging, you can log mailbox access by mailbox owners, delegates
(including administrators with full access permissions to mailboxes), and administrators.

When you enable audit logging for a mailbox, you can specify which user actions (for example,
accessing, moving, or deleting a message) will be logged for a logon type (administrator,
delegate user, or owner). Audit log entries also include important information such as the client
IP address, host name, and process or client used to access the mailbox. For items that are
moved, the entry includes the name of the destination folder.

Mailbox audit logs
Mailbox audit logs are generated for each mailbox that has mailbox audit logging enabled. Log
entries are stored in the Recoverable Items folder in the audited mailbox, in the Audits
subfolder. This ensures that all audit log entries are available from a single location, regardless
of which client access method was used to access the mailbox or which server or computer an
administrator uses to access the mailbox audit log. If you move a mailbox to another Mailbox
server, the mailbox audit logs for that mailbox are also moved because they're located in the
mailbox.

By default, mailbox audit log entries are retained in the mailbox for 90 days and then deleted.
You can modify this retention period by using the AuditLogAgeLimit parameter with the Set-
Mailbox cmdlet. If a mailbox is on In-Place Hold or Litigation Hold, audit log entries are only
retained until the audit log retention period for the mailbox is reached. To retain audit log
entries longer, you have to increase the retention period by changing the value for the
AuditLogAgeLimit parameter. You can also export audit log entries before the retention period
is reached. For more information, see:

      Export Mailbox Audit Logs

      Create a Mailbox Audit Log Search

<!-- p.2363 -->

Enabling mailbox audit logging
Mailbox audit logging is enabled per mailbox. Use the Set-Mailbox cmdlet to enable or disable
mailbox audit logging. For details, see Enable or disable mailbox audit logging for a mailbox.

When you enable mailbox audit logging for a mailbox, access to the mailbox and certain
administrator and delegate actions are logged by default. To log actions taken by the mailbox
owner, you must specify which owner actions should be audited.

Mailbox actions logged by mailbox audit logging
The following table lists the actions logged by mailbox audit logging, including the logon types
for which the action can be logged. Note that an administrator who has been assigned the Full
Access permission to a user's mailbox is considered a delegate user.

If you no longer require certain types of mailbox actions to be audited, you should modify the
mailbox's audit logging configuration to disable those actions. Existing log entries aren't
purged until the age limit for audit log entries is reached.

                                                                                      ﾉ     Expand table

 Action                Description                                           Admin   Delegate     Owner

 Copy                  An item is copied to another folder.                  Yes     No           No

 Create                An item is created in the Calendar, Contacts,         Yes1    Yes1         Yes
                       Notes, or Tasks folder in the mailbox; for example,
                       a new meeting request is created. Note that
                       message or folder creation isn't audited.

 FolderBind            A mailbox folder is accessed.                         Yes1    Yes2         No

 HardDelete            An item is deleted permanently from the               Yes1    Yes1         Yes
                       Recoverable Items folder.

 MailboxLogin          The user signed in to their mailbox.                  No      No           Yes3

 MessageBind           An item is accessed in the reading pane or            Yes     No           No
                       opened.

 Move                  An item is moved to another folder.                   Yes1    Yes          Yes

 MoveToDeletedItems    An item is moved to the Deleted Items folder.         Yes1    Yes          Yes

 SendAs                A message is sent using Send As permissions.          Yes1    Yes1         No

<!-- p.2364 -->

    Action                Description                                         Admin   Delegate   Owner

    SendOnBehalf          A message is sent using Send on Behalf              Yes1    Yes        No
                          permissions.

    SoftDelete            An item is deleted from the Deleted Items folder.   Yes1    Yes1       Yes

    Update                An item's properties are updated.                   Yes1    Yes1       Yes

1
    Audited by default if auditing is enabled for a mailbox.

2
    Entries for folder bind actions performed by delegates are consolidated. One log entry is
generated for individual folder access within a time span of 24 hours.

3 Auditing for owner logins to a mailbox works only for POP3, IMAP4, or OAuth logins. It

doesn't work for NTLM or Kerberos logins to the mailbox.

Searching the mailbox audit log
You can use the following methods to search mailbox audit log entries:

        Synchronously search a single mailbox: You can use the Search-MailboxAuditLog cmdlet
        to synchronously search mailbox audit log entries for a single mailbox. The cmdlet
        displays search results in the Exchange Management Shell window. For details, see Search
        Mailbox Audit Log for a Mailbox.

        Asynchronously search one or more mailboxes: You can create a mailbox audit log
        search to asynchronously search mailbox audit logs for one or more mailboxes, and then
        have the search results sent to a specified email address. The search results are sent as an
        XML attachment. To create the search, use the New-MailboxAuditLogSearch cmdlet. For
        details, see Create a Mailbox Audit Log Search.

        Use auditing reports in the Exchange admin center (EAC): You can use the Auditing tab
        in the EAC to run a non-owner mailbox access report (contains entries for admin and
        delete actions) or export non-owner entries from the mailbox audit log. For details, see:

             Run a non-owner mailbox access report

             Export Mailbox Audit Logs

Mailbox audit log entries
The following table describes the fields logged in a mailbox audit log entry.

<!-- p.2365 -->

                                                                             ﾉ   Expand table

Field                Populated with

Operation            One of the following actions:
                     Copy
                     Create
                     FolderBind
                     HardDelete
                     MailboxLogin
                     MessageBind
                     Move
                     MoveToDeletedItems
                     SendAs
                     SendOnBehalf
                     SoftDelete
                     Update

OperationResult      One of the following results:
                     Failed
                     PartiallySucceeded
                     Succeeded

LogonType            Logon type of the user who performed the operation. Logon types
                     include:
                     Owner
                     Delegate
                     Admin

DestFolderId         Destination folder GUID for move operations.

DestFolderPathName   Destination folder path for move operations.

FolderId             Folder GUID.

FolderPathName       Folder path.

ClientInfoString     Details that identify which client or Exchange component performed the
                     operation.

ClientIPAddress      Client computer IP address.

ClientMachineName    Client computer name.

ClientProcessName    Name of the client application process.

ClientVersion        Client application version.

InternalLogonType    The type of internal user (a person in your organization) who performed
                     the operation. The possible values for this field are the same ones as the
                     LogonType field.

<!-- p.2366 -->

Field                          Populated with

MailboxOwnerUPN                Mailbox owner user principal name (UPN).

MailboxOwnerSid                Mailbox owner security identifier (SID).

DestMailboxOwnerUPN            Destination mailbox owner UPN, logged for cross-mailbox operations.

DestMailboxOwnerSid            Destination mailbox owner SID, logged for cross-mailbox operations.

DestMailboxOwnerGuid           Destination mailbox owner GUID.

CrossMailboxOperation          Information about whether the operation logged is a cross-mailbox
                               operation (for example, copying or moving messages between
                               mailboxes).

LogonUserDisplayName           Display name of user who is logged on.

DelegateUserDisplayName        Delegate user display name.

LogonUserSid                   SID of user who is logged on.

SourceItems                    ItemID of mailbox items on which the logged action is performed (for
                               example, move or delete). For operations performed on a number of
                               items, this field is returned as a collection of items.

SourceFolders                  Source folder GUID.

ItemId                         Item ID.

ItemSubject                    Item subject.

MailboxGuid                    Mailbox GUID.

MailboxResolvedOwnerName       Mailbox user resolved name in the format DOMAIN\ SamAccountName.

LastAccessed                   Time when the operation was performed.

Identity                       Audit log entry ID.

More information
    Administrator access to mailboxes: Mailboxes are considered to be accessed by an
    administrator only in the following scenarios:

         In-Place eDiscovery is used to search a mailbox.

         The New-MailboxExportRequest cmdlet is used to export a mailbox.

<!-- p.2367 -->

  Microsoft Exchange Server MAPI Client and Collaboration Data Objects      is used to
  access the mailbox.

Bypassing mailbox auditing logging: Mailbox access by authorized automated processes
such as accounts used by third-party tools or accounts used for lawful monitoring can
create a large number of mailbox audit log entries and may not be of interest to your
organization. You can configure such accounts to bypass mailbox audit logging. For
details, see Bypass a User Account From Mailbox Audit Logging.

Logging mailbox owner actions: For mailboxes such as the Discovery Search Mailbox,
which may contain more sensitive information, consider enabling mailbox audit logging
for mailbox owner actions such as message deletion.

<!-- p.2368 -->

Enable or disable mailbox audit logging for
a mailbox in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

With mailbox audit logging in Exchange Server, you can track logons to a mailbox as well as
what actions are taken while the user is logged on. When you enable mailbox audit logging for
a mailbox, some actions performed by administrators and delegates are logged by default.
None of the actions performed by the mailbox owner are logged by default. To learn more
about mailbox audit logging and what actions can be logged, see Mailbox audit logging in
Exchange Server.

  Ｕ Caution

  Auditing of mailbox owner actions can generate a large number of mailbox audit log
  entries and is therefore disabled by default. We recommend that you only enable auditing
  of specific owner actions needed to meet business or compliance requirements.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox audit logging" entry in
      the Messaging policy and compliance permissions in Exchange Server topic.

      Entries in the mailbox audit log are retained for 90 days, by default. See the More
      information section change how long entries are retained.

      You can't use the Exchange admin center (EAC) to enable or disable mailbox audit
      logging. You have to use the Exchange Management Shell. To learn how to open the
      Exchange Management Shell in your on-premises Exchange organization, see Open the
      Exchange Management Shell.

      An administrator who has been assigned the Full Access permission to a user's mailbox is
      considered a delegate user.

      Mailboxes are considered to be accessed by an administrator only in the following
      scenarios:

         In-Place eDiscovery is used to search a mailbox.

<!-- p.2369 -->

        The New-MailboxExportRequest cmdlet is used to export a mailbox.

        Microsoft Exchange Server MAPI Editor is used to access the mailbox.

Enable or disable mailbox audit logging
You can use the Exchange Management Shell to enable or disable mailbox audit logging for a
mailbox. This enables or disables logging of all operations specified for administrator,
delegates, and the mailbox owner.

This example enables mailbox audit logging for Ben Smith's mailbox.

  PowerShell

  Set-Mailbox -Identity "Ben Smith" -AuditEnabled $true

This example enables mailbox audit logging for all user mailboxes in your organization.

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Select PrimarySmtpAddress | ForEach {Set-Mailbox -Identity $_.PrimarySmtpAddress
  -AuditEnabled $true}

This example disables mailbox audit logging for Ben Smith's mailbox.

  PowerShell

  Set-Mailbox -Identity "Ben Smith" -AuditEnabled $false

For detailed syntax and parameter information, see Set-Mailbox.

Configure mailbox audit logging settings for
administrator, delegate, and owner access
When mailbox audit logging is enabled for a mailbox, only the administrator, delegate, and
owner actions specified in the audit logging configuration for the mailbox are logged.

This example specifies that the MessageBind and FolderBind actions performed by
administrators will be logged for Ben Smith's mailbox.

  PowerShell

<!-- p.2370 -->

  Set-Mailbox -Identity "Ben Smith" -AuditAdmin MessageBind,FolderBind -AuditEnabled
  $true

This example specifies that the SendAs or SendOnBehalf actions performed by delegate users
will be logged for Ben Smith's mailbox.

  PowerShell

  Set-Mailbox -Identity "Ben Smith" -AuditDelegate SendAs,SendOnBehalf -AuditEnabled
  $true

This example specifies that the HardDelete action performed by the mailbox owner will be
logged for Ben Smith's mailbox.

  PowerShell

  Set-Mailbox -Identity "Ben Smith" -AuditOwner HardDelete -AuditEnabled $true

For detailed syntax and parameter information, see Set-Mailbox.

How do you know this worked?
To verify that you have successfully enabled mailbox audit logging for a mailbox and specified
the correct logging settings for administrator, delegate, or owner access, use the Get-Mailbox
cmdlet to retrieve the mailbox audit logging settings for that mailbox.

This example retrieves Ben Smith's mailbox settings and pipes the specified audit settings,
including the audit log age limit, to the Format-List cmdlet.

  PowerShell

  Get-Mailbox "Ben Smith" | Format-List Audit*

A value of True for the AuditEnabled property verifies that audit logging is enabled.

This example retrieves the auditing settings for all user mailboxes in your organization.

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Format-List Name,Audit*

<!-- p.2371 -->

More information
The actions that are audited for each type of user may not all be displayed when you run the
Get-Mailbox cmdlet. But you can run the following commands to display all the audited
actions for a specific user logon type.

  PowerShell

  Get-Mailbox <identity of mailbox> | Select-Object -ExpandProperty AuditAdmin

  PowerShell

  Get-Mailbox <identity of mailbox> | Select-Object -ExpandProperty AuditDelegate

  PowerShell

  Get-Mailbox <identity of mailbox> | Select-Object -ExpandProperty AuditOwner

By default, entries in the mailbox audit log are kept for 90 days. When an entry is older than 90
days, it's deleted. You can use the Set-Mailbox cmdlet to change this setting so items are kept
for a longer (or shorter) period of time.

This example increases the age limit for mailbox audit log entries in Pilar Pinilla's mailbox to
180 days.

  PowerShell

  Set-Mailbox -Identity "Pilar Pinilla" -AuditLogAgeLimit 180

This example decreases the age limit for mailbox audit log entries for all user mailboxes in your
organization to 60 days.

  PowerShell

  Get-Mailbox -ResultSize Unlimited -Filter "RecipientTypeDetails -eq 'UserMailbox'"
  | Set-Mailbox -AuditLogAgeLimit 60

<!-- p.2372 -->

Run a non-owner mailbox access report
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

The Non-Owner Mailbox Access Report in the Exchange admin center (EAC) lists the
mailboxes that are accessed by someone other than the person who owns the mailbox. When a
non-owner accesses a mailbox, Exchange logs information about this action. Exchange stores
this mailbox audit log as an email message in a hidden folder in the audited mailbox. The
report displays entries from this log as search results and includes any mailboxes accessed by a
non-owner, who accessed each mailbox and when, the actions performed by non-owners, and
whether or not the actions were successful.

Exchange logs specific actions by non-owners, which includes administrators and users who are
assigned permissions to a mailbox (who are called delegated users). You can also narrow the
search to users inside or outside your organization. By default, Exchange retains entries in the
mailbox audit log for 90 days.

You enable mailbox audit logging in the Exchange Management Shell.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes.

     To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
     Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox audit logging" entry in
     the Messaging policy and compliance permissions in Exchange Server article.

     For information about keyboard shortcuts that apply to the procedures in this article, see
     Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

<!-- p.2373 -->

Step 1: Use the Exchange Management Shell to
enable mailbox audit logging
You have to enable mailbox audit logging for each mailbox that you want to include in a non-
owner mailbox access report. If you don't enable mailbox audit logging, you won't get any
results when you run a report.

To enable mailbox audit logging for a single mailbox, run the following command in the
Exchange Management Shell:

  PowerShell

  Set-Mailbox <Identity> -AuditEnabled $true

For example, to enable mailbox auditing for a user named Florence Flipo, run the following
command.

  PowerShell

  Set-Mailbox "Florence Flipo" -AuditEnabled $true

To enable mailbox auditing for all user mailboxes in your organization, run the following
commands:

  PowerShell

  $UserMailboxes = Get-mailbox -Filter "RecipientTypeDetails -eq 'UserMailbox'"

  PowerShell

  $UserMailboxes | ForEach {Set-Mailbox $_.Identity -AuditEnabled $true}

How do you know this worked?
Run the following command to verify that you successfully configured mailbox audit logging.

  PowerShell

  Get-Mailbox | Format-List Name,AuditEnabled

A value of True for the AuditEnabled property verifies that audit logging is enabled.

<!-- p.2374 -->

Step 2: Use the EAC to run a non-owner mailbox
access report
   1. In the EAC, navigate to Compliance Management > Auditing.

   2. Select Run a non-owner mailbox access report.

     By default, Exchange runs the report for non-owner access to any mailboxes in the
     organization over the past two weeks. Audit logging was enabled for the mailboxes listed
     in the search results.

   3. To view non-owner access for a specific mailbox, select the mailbox from the list of
     mailboxes. View the search results in the details pane.

Notes:

     Want to narrow the search results? Select the start date, end date, or both, and select
     specific mailboxes to search. Select Search to rerun the report.

     You can also specify that you want to search for the non-owner access type, also called
     the logon type. Here are your options:

         All non-owners: Search for access by administrators and delegated users inside your
         organization. Also includes access user outside of your organization.

         External users: Search for access by users outside of your organization.

         Administrators and delegated users: Search for access by administrators and
         delegated users inside your organization.

         Administrators: Search for access by administrators in your organization.

How do you know this worked?
To verify that you've successfully run a non-owner mailbox access report, check the search
results pane. The results pane displays the mailboxes that you ran the report for, whether an
individual user or a group of mailboxes. If there are no results for a specific mailbox, it's
possible there was no non-owner access or there was no non-owner access in the specified
date range. As we previously recommended, be sure to verify that you enabled audit logging
for the mailboxes you want to search for access by non-owners.

What gets logged in the mailbox audit log?

<!-- p.2375 -->

When you run a non-owner mailbox access report, the EAC search results display entries from
the mailbox audit log. Each report entry contains this information:

     Who accessed the mailbox and when.

     The actions performed by the non-owner.

     The affected message and its folder location.

     Whether the action was successful

The following table describes the types of actions logged, and whether these actions are
logged by default for access by administrators and for access by delegated users. If you want
to track actions that aren't logged by default, you have to use the Exchange Management Shell
to enable logging of those actions.

                                                                                   ﾉ     Expand table

 Action          Description                                            Administrators    Delegated
                                                                                          users

 Update          A message was changed.                                 Yes               Yes

 Copy            A message was copied to another folder.                No                No

 Move            A message was moved to another folder.                 Yes               No

 Move To         A message was moved to the Deleted Items folder.       Yes               No
 Deleted Items

 Soft-delete     A message was deleted from the Deleted Items folder.   Yes               Yes

 Hard-delete     A message was purged from the Recoverable Items        Yes               Yes
                 folder.

 FolderBind      A mailbox folder was accessed.                         Yes               No

 Send as         A message was sent using SendAs permission. This       Yes               Yes
                 means another user sent the message as though it
                 came from the mailbox owner.

 Send on         A message was sent using SendOnBehalf permission.      Yes               No
 behalf of       This means another user sent the message on behalf
                 of the mailbox owner. The message indicates to the
                 recipient who the message was sent on behalf of and
                 who actually sent the message.

 MessageBind     A message was viewed in the preview pane or opened.    No                No

<!-- p.2376 -->

Data loss prevention in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Data loss prevention (DLP) is important in Exchange Server because business critical email
communication often includes sensitive data. DLP features make managing sensitive data in
email messages easier than ever before by balancing compliance requirements without
unnecessarily hindering the productivity of workers. For a conceptual overview of DLP, watch
the following video.
https://learn-video.azurefd.net/vod/player?id=da03be8a-9f33-4a2b-a1d0-
2a31f81550ab&locale=en-us&embedUrl=%2Fexchange%2Fpolicy-and-
compliance%2Fdata-loss-prevention%2Fdata-loss-prevention

DLP policies are simple packages that are collections of mail flow rules (also known as
transport rules) that contain specific conditions, actions, and exceptions that filter messages
and attachments based on their content. You can create a DLP policy, yet choose to not
activate it. This allows you to test your policies without affecting mail flow. For more
information, see Test a mail flow rule.

DLP policies can use the full power of mail flow rules to detect and then act on messages in
transit. For example, a mail flow rule can perform deep content analysis through keyword
matches, dictionary matches, text pattern matches through regular expressions, and other
content examination techniques to detect content that violates your organization's DLP
policies. Document fingerprinting is also available to help you detect sensitive information in
standard forms. For more information, see the following topics:

      Document fingerprinting

      Mail flow rules in Exchange Server

      Integrating classification rules with mail flow rules

In addition to the customizable DLP policies themselves, you can also inform email senders
when they're about to violate one of your policies, even before they send a message that
contains sensitive information. You do this by configuring Policy Tips. Policy Tips present a brief
note about the possible policy violations in Outlook 2013 or later, Outlook on the web
(formerly known as Outlook Web App), and Outlook on the web for devices. For more
information, see Policy Tips.

Notes:

      DLP is a premium feature that requires an Exchange Enterprise Client Access License
      (CAL). For more information about CALs and server licensing, see Exchange licensing

<!-- p.2377 -->

     FAQs    .

     In hybrid environments where some mailboxes are in on-premises Exchange and some
     are in Exchange Online, DLP policies are only applied in Exchange Online. Messages that
     are sent between on-premises users don't have DLP policies applied, because the
     messages don't leave the on-premises environment.

Looking for management tasks related to Data Loss Prevention? See DLP Procedures.

Establish policies to protect sensitive data
The data loss prevention features can help you identify and monitor many categories of
sensitive information that you have defined within the conditions of your policies, such as
private identification numbers or credit card numbers. You have the option of defining your
own custom policies and mail flow rules, or you can use the DLP policy templates that are
included in Exchange to get started quickly. A policy template is a model that includes a range
of conditions, rules, and actions that you can choose from to create and save an actual DLP
policy that will help you inspect messages. For more information about the included policy
templates, see DLP Policy Templates Supplied in Exchange.

There are three different methods that you can use to implement DLP:

     Apply an out-of-the-box template supplied in Exchange: The quickest way to start using
     DLP policies is to create and implement a new policy by using a template. This saves you
     the effort of building a new set of rules from nothing. You need to know what type of
     data you want to check for or which compliance regulation you're attempting to address.
     You also need to know your organization's expectations for processing this data. For
     more information, see DLP Policy Templates Supplied in Exchange and Create a DLP Policy
     From a Template.

     Import a pre-built policy file from outside your organization: You can import policies
     that were created by independent software vendors. In this way, you can extend the DLP
     solution to meet your business requirements. For more information, see Define Your Own
     DLP Templates and Information Types and Import a DLP Policy From a File.

     Create a custom policy without any pre-existing conditions: Your enterprise may have its
     own requirements for monitoring certain types of data that's known to exist within a
     messaging system. You can create a custom policy entirely on your own to find and act
     on your own unique message data. You need to know the requirements and constraints
     of the environment where the DLP policy will be enforced to create effective custom
     policies. For more information, see Create a Custom DLP Policy.

<!-- p.2378 -->

After you add a policy, you can review and change its rules, deactivate the policy, or remove it
completely. For more information, see Manage DLP Policies.

Sensitive information types in DLP policies
When you create or change DLP policies, you can include rules that look for sensitive
information. The sensitive information types that are listed in the topic Sensitive information
types in Exchange Server are available for you to use in your policies. You can customize the
conditions within a policy, such as how many times something has to be found before an
action is taken, or the action to take. For more information about creating DLP policies see,
Create a Custom DLP Policy. For more information about mail flow rules, see Mail flow rules in
Exchange Server.

To make it easy for you to use rules that look for sensitive information, Exchange comes with
policy templates that already include some of the sensitive information types. You can't add
conditions for all of the sensitive information types, because the templates are designed to
help you focus on the most common types of compliance-related data within your
organization. For more information about the pre-built templates, see DLP Policy Templates
Supplied in Exchange.

You can create many DLP policies for your organization, and enable them all so that many
different types of information are looked for. You can also create a DLP policy that isn't based
on an existing template. To create such a policy, see Create a Custom DLP Policy. For more
information about the available sensitive information types, see Sensitive information types in
Exchange Server.

Detecting sensitive form data with Document
Fingerprinting
Exchange lets you use Document Fingerprinting to easily create a sensitive information type
that's based on a standard form.

Policy Tips notify users about sensitive content
expectations
You can use Policy Tip notification messages to inform email senders about possible
compliance issues while they are composing an email message. When you configure a Policy
Tip in a DLP policy, the notification message will only show up if something in the sender's

<!-- p.2379 -->

email message matches the conditions described in your policy. Policy Tips are similar to
MailTips that were introduced in Exchange 2010. For more information, see Policy Tips.

Detecting sensitive information along with
traditional message classification
A key factor in the strength of a DLP solution is the ability to correctly identify confidential or
sensitive content that may be unique to your organization, regulatory needs, geography, or
other business needs. The Exchange DLP architecture uses deep content analysis coupled with
detection criteria that you establish through rules in your DLP policies. Helping to prevent data
loss in Exchange requires you to configure the appropriate set of sensitive information rules
that provide a high degree of protection while minimizing disruptions to mail flow that are
caused by false positives and negatives. These types of rules (referred to throughout the DLP
information as sensitive information detection) function within the framework of mail flow rules
to enable DLP capabilities. To learn more about these features, see Integrating sensitive
information rules with mail flow rules.

You can still apply traditional message classifications to messages, and you can combine these
classifications with sensitive information detection. You can use these features together within
a single DLP policy, or operate them independently (concurrently). To learn more about the
traditional Exchange 2010 message classifications, see Understanding Message Classifications.

Information about DLP-processed messages
To see information about messages that contain DLP policy detections in your environment,
see View DLP policy detection reports and Create incident reports for DLP policy detections.
Data related to DLP detections is highly integrated in the delivery reports.

For more information
     Messaging policy and compliance in Exchange Server

     DLP Procedures

     View DLP policy detection reports)

     Document Fingerprinting

<!-- p.2380 -->

Sensitive information types in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016     2019      Subscription Edition

Data loss prevention (DLP) includes 80 sensitive information types that are ready for you to use in your DLP policies. This topic lists all of these
sensitive information types and shows what a DLP policy looks for when it detects each type. A sensitive information type is defined by a pattern
that can be identified by a regular expression or a function. In addition, corroborative evidence such as keywords and checksums can be used to
identify a sensitive information type. Confidence level and proximity are also used in the evaluation process.

ABA Routing Number
Format: Nine digits that may be in a formatted or unformatted pattern.

Pattern:

Formatted:

      Four digits beginning with 0, 1, 2, 3, 6, 7, or 8

      A hyphen

      Four digits

      A hyphen

      A digit

Unformatted: Nine consecutive digits beginning with 0, 1, 2, 3, 6, 7, or 8

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_aba_routing finds content that matches the pattern.

      A keyword from Keyword_ABA_Routing is found.

  <!-- ABA Routing Number -->
  <Entity id="cb353f78-2b72-4c3c-8827-92ebe4f69fdf" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_aba_routing" />
          <Match idRef="Keyword_ABA_Routing" />
        </Pattern>
   </Entity>

Keywords:

                                                                                                                                       ﾉ   Expand table

 Keyword_ABA_Routing

 aba
 aba #
 aba routing #
 aba routing number
 aba#
 abarouting#
 aba number
 abaroutingnumber
 american bank association routing #
 american bank association routing number
 americanbankassociationrouting#
 americanbankassociationroutingnumber
 bank routing number
 bank routing#

<!-- p.2381 -->

 Keyword_ABA_Routing

 bank routing number
 routing transit number
 RTN

Argentina National Identity (DNI) Number
Format: Eight digits separated by periods

Pattern: Eight digits:

       Two digits

       A period

       Three digits

       A period

       Three digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The regular expression Regex_argentina_national_id finds content that matches the pattern.

       A keyword from Keyword_argentina_national_id is found.

  <!-- Argentina National Identity (DNI) Number -->
  <Entity id="eefbb00e-8282-433c-8620-8f1da3bffdb2" recommendedConfidence="75" patternsProximity="300">
     <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_argentina_national_id"/>
        <Match idRef="Keyword_argentina_national_id"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_argentina_national_id

 Argentina National Identity number
 Identity
 Identification National Identity Card
 DNI
 NIC National Registry of Persons
 Documento Nacional de Identidad
 Registro Nacional de las Personas
 Identidad
 Identificación

Australia Bank Account Number
Format: 6-10 digits with or without a bank state branch number

Pattern: Account number is 6-10 digits. Australia bank state branch number:

       Three digits

       A hyphen

       Three digits

<!-- p.2382 -->

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_australia_bank_account_number finds content that matches the pattern..

     A keyword from Keyword_australia_bank_account_number is found.

     The regular expression Regex_australia_bank_account_number_bsb finds content that matches the pattern.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_australia_bank_account_number finds content that matches the pattern..

     A keyword from Keyword_australia_bank_account_number is found.

  <!-- Australia Bank Account Number -->
  <Entity id="74a54de9-2a30-4aa0-a8aa-3d9327fc07c7" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_australia_bank_account_number" />
          <Match idRef="Keyword_australia_bank_account_number" />
          <Match idRef="Regex_australia_bank_account_number_bsb" />
    </Pattern>
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_australia_bank_account_number" />
          <Match idRef="Keyword_australia_bank_account_number" />
    </Pattern>
   </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_australia_bank_account_number

 swift bank code
 correspondent bank
 base currency
 usa account
 holder address
 bank address
 information account
 fund transfers
 bank charges
 bank details
 banking information
 full names
 idea

Australia Driver's License Number
Format: Nine letters and digits

Pattern: Nine letters and digits:

     Two digits or letters (not case sensitive)

     Two digits

     Five digits or letters (not case sensitive)

     OR

     1-2 optional letters (not case sensitive)

     4-9 digits

     OR

<!-- p.2383 -->

      Nine digits or letters (not case sensitive)

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_australia_drivers_license_number finds content that matches the pattern.

      A keyword from Keyword_australia_drivers_license_number is found.

      No keyword from Keyword_australia_drivers_license_number_exclusions is found.

  <!-- Australia Drivers License Number -->
  <Entity id="1cbbc8f5-9216-4392-9eb5-5ac2298d1356" patternsProximity="300" recommendedConfidence="75">
     <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_australia_drivers_license_number" />
          <Match idRef="Keyword_australia_drivers_license_number" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_australia_drivers_license_number_exclusions" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_australia_drivers_license_number                            Keyword_australia_drivers_license_number_exclusions

 international driving permits                                       aaa
 australian automobile association                                   DriverLicense
 Sydney nsw                                                          DriverLicenses
 international driving permit                                        Driver License
 DriverLicence                                                       Driver Licenses
 DriverLicences                                                      DriversLicense
 Driver Lic                                                          DriversLicenses
 Driver Licence                                                      Drivers License
 Driver Licences                                                     Drivers Licenses
 DriversLic                                                          Driver'License
 DriversLicence                                                      Driver'Licenses
 DriversLicences                                                     Driver' License
 Drivers Lic                                                         Driver' Licenses
 Drivers Lics                                                        Driver'sLicense
 Drivers Licence                                                     Driver'sLicenses
 Drivers Licences                                                    Driver's License
 Driver'Lic                                                          Driver's Licenses
 Driver'Lics                                                         DriverLicense#
 Driver'Licence                                                      DriverLicenses#
 Driver'Licences                                                     Driver License#
 Driver' Lic                                                         Driver Licenses#
 Driver' Lics                                                        DriversLicense#
 Driver' Licence                                                     DriversLicenses#
 Driver' Licences                                                    Drivers License#
 Driver'sLic                                                         Drivers Licenses#
 Driver'sLics                                                        Driver'License#
 Driver'sLicence                                                     Driver'Licenses#
 Driver'sLicences                                                    Driver' License#
 Driver's Lic                                                        Driver' Licenses#
 Driver's Lics                                                       Driver'sLicense#
 Driver's Licence                                                    Driver'sLicenses#
 Driver's Licences                                                   Driver's License#
 DriverLic#                                                          Driver's Licenses#
 DriverLics#
 DriverLicence#
 DriverLicences#
 Driver Lic#
 Driver Lics#
 Driver Licence#
 Driver Licences#
 DriversLic#

<!-- p.2384 -->

 Keyword_australia_drivers_license_number                            Keyword_australia_drivers_license_number_exclusions

 DriversLics#
 DriversLicence#
 DriversLicences#
 Drivers Lic#
 Drivers Lics#
 Drivers Licence#
 Drivers Licences#
 Driver'Lic#
 Driver'Lics#
 Driver'Licence#
 Driver'Licences#
 Driver' Lic#
 Driver' Lics#
 Driver' Licence#
 Driver' Licences#
 Driver'sLic#
 Driver'sLics#
 Driver'sLicence#
 Driver'sLicences#
 Driver's Lic#
 Driver's Lics#
 Driver's Licence#
 Driver's Licences#

Australia Medical Account Number
Format: 10-11 digits

Pattern: 10-11 digits:

      First digit is in the range 2-6

      Ninth digit is a check digit

      Tenth digit is the issue digit

      Eleventh digit (optional) is the individual number

Checksum: Yes

Definition:

A DLP policy is 95% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_australian_medical_account_number finds content that matches the pattern.

      A keyword from Keyword_Australia_Medical_Account_Number is found.

      The checksum passes.

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_australian_medical_account_number finds content that matches the pattern.

      The checksum passes.

  <!-- Australia Medical Account Number -->
  <Entity id="104a99a0-3d3b-4542-a40d-ab0b9e1efe63" recommendedConfidence="85" patternsProximity="300">
      <Pattern confidenceLevel="95">
       <IdMatch idRef="Func_australian_medical_account_number"/>
       <Any minMatches="1">
       <Match idRef="Keyword_Australia_Medical_Account_Number"/>
       </Any>
    </Pattern>
  <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_australian_medical_account_number"/>
       <Any minMatches="0" maxMatches="0">
    <Match idRef="Keyword_Australia_Medical_Account_Number"/>
       </Any>

<!-- p.2385 -->

    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_Australia_Medical_Account_Number

 bank account details
 medicare payments
 mortgage account
 bank payments
 information branch
 credit card loan
 department of human services
 local service
 medicare

Australia Passport Number
Format: A letter followed by seven digits

Pattern: A letter (not case sensitive) followed by seven digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_australia_passport_number finds content that matches the pattern.

      A keyword from Keyword_passport or Keyword_australia_passport_number is found.

  <!-- Australia Passport Number -->
  <Entity id="29869db6-602d-4853-ab93-3484f905df50" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_australia_passport_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_passport" />
            <Match idRef="Keyword_australia_passport_number" />
          </Any>
     </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_passport                                     Keyword_australia_passport_number

 Passport Number                                      passport
 Passport No                                          passport details
 Passport #                                           immigration and citizenship
 Passport#                                            commonwealth of australia
 PassportID                                           department of immigration
 Passportno                                           residential address
 passportnumber                                       department of immigration and citizenship
 パスポート                                                visa
 パスポート番号                                              national identity card
 パスポートのNum                                            passport number
 パスポート ＃                                              travel document
 Numéro de passeport                                  issuing authority
 Passeport n °
 Passeport Non
 Passeport #
 Passeport#

<!-- p.2386 -->

 Keyword_passport                                       Keyword_australia_passport_number

 PasseportNon
 Passeportn °

Australia Tax File Number
Format: 8-9 digits

Pattern: 8-9 digits typically presented with spaces as follows:

     Three digits

     An optional space

     Three digits

     An optional space

     2-3 digits where the last digit is a check digit

Checksum: Yes

Definition:

A DLP policy is 95% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_australian_tax_file_number finds content that matches the pattern.

     A keyword from Keyword_Australia_Tax_File_Number is found.

     No keyword from Keyword_number_exclusions is found.

     The checksum passes.

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_australian_tax_file_number finds content that matches the pattern.

     No keyword from Keyword_Australia_Tax_File_Number or Keyword_number_exclusions is found.

     The checksum passes.

  <!-- Australia Tax File Number -->
  <Entity id="e29bc95f-ff70-4a37-aa01-04d17360a4c5" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="95">
          <IdMatch idRef="Func_australian_tax_file_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_Australia_Tax_File_Number" />
          </Any>
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_number_exclusions" />
          </Any>
    </Pattern>
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_australian_tax_file_number" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_Australia_Tax_File_Number" />
            <Match idRef="Keyword_number_exclusions" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_Australia_Tax_File_Number                                                   Keyword_number_exclusions

 australian business number                                                          00000000
 marginal tax rate                                                                   11111111

<!-- p.2387 -->

 Keyword_Australia_Tax_File_Number                                                   Keyword_number_exclusions

 medicare levy                                                                       22222222
 portfolio number                                                                    33333333
 service veterans                                                                    44444444
 withholding tax                                                                     55555555
 individual tax return                                                               66666666
 tax file number                                                                     77777777
                                                                                     88888888
                                                                                     99999999
                                                                                     000000000
                                                                                     111111111
                                                                                     222222222
                                                                                     333333333
                                                                                     444444444
                                                                                     555555555
                                                                                     666666666
                                                                                     777777777
                                                                                     888888888
                                                                                     999999999
                                                                                     0000000000
                                                                                     1111111111
                                                                                     2222222222
                                                                                     3333333333
                                                                                     4444444444
                                                                                     5555555555
                                                                                     6666666666
                                                                                     7777777777
                                                                                     8888888888
                                                                                     9999999999

Belgium National Number
Format: 11 digits plus delimiters

Pattern: 11 digits plus delimiters:

     Six digits and two periods in the format YY.MM.DD for date of birth

     A hyphen

     Three sequential digits (odd for males, even for females)

     A period

     Two digits that are a check digit

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_belgium_national_number finds content that matches the pattern.

     A keyword from Keyword_belgium_national_number is found.

     The checksum passes.

  <!-- Belgium National Number -->
    <Entity id="fb969c9e-0fd1-4b18-8091-a2123c5e6a54" recommendedConfidence="75" patternsProximity="300">
     <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_belgium_national_number"/>
       <Match idRef="Keyword_belgium_national_number"/>
    </Pattern>
  </Entity>

Keywords:

<!-- p.2388 -->

                                                                                                                                ﾉ   Expand table

 Keyword_belgium_national_number

 Identity
 Registration
 Identification
 ID
 Identiteitskaart
 Registratie nummer
 Identificatie nummer
 Identiteit
 Registratie
 Identificatie
 Carte d'identité
 numéro d'immatriculation
 numéro d'identification
 identité
 inscription
 Identifikation
 Identifizierung
 Identifikationsnummer
 Personalausweis
 Registrierung
 Registrationsnummer

Brazil Legal Entity Number (CNPJ)
Format: 14 digits that include a registration number, branch number, and check digits, plus delimiters

Pattern: 14 digits, plus delimiters:

      Two digits

      A period

      Three digits

      A period

      Three digits (these first eight digits are the registration number)

      A forward slash

      Four-digit branch number

      A hyphen

      Two digits that are check digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_brazil_cnpj finds content that matches the pattern.

      A keyword from Keyword_brazil_cnpj is found.

      The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_brazil_cnpj finds content that matches the pattern.

      The checksum passes.

  <!-- Brazil Legal Entity Number (CNPJ) -->
  <Entity id="9b58b5cd-5e90-4df6-b34f-1ebcc88ceae4" recommendedConfidence="85" patternsProximity="300">
     <Pattern confidenceLevel="85">

<!-- p.2389 -->

       <IdMatch idRef="Func_brazil_cnpj"/>
       <Match idRef="Keyword_brazil_cnpj"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_brazil_cnpj"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_brazil_cnpj

 CNPJ
 CNPJ/MF
 CNPJ-MF
 National Registry of Legal Entities
 Taxpayers Registry
 Legal entity
 Legal entities
 Registration Status
 Business
 Company
 CNPJ
 Cadastro Nacional da Pessoa Jurídica
 Cadastro Geral de Contribuintes
 CGC
 Pessoa jurídica
 Pessoas jurídicas
 Situação cadastral
 Inscrição
 Empresa

Brazil CPF Number
Format: 11 digits that include a check digit and can be formatted or unformatted

Pattern:

Formatted:

     Three digits

     A period

     Three digits

     A period

     Three digits

     A hyphen

     Two digits which are check digits

Unformatted: 11 digits where the last two digits are check digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_brazil_cpf finds content that matches the pattern.

     A keyword from Keyword_brazil_cpf is found.

     The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

<!-- p.2390 -->

      The function Func_brazil_cpf finds content that matches the pattern.

      The checksum passes.

  <!-- Brazil CPF Number -->
  <Entity id="78e09124-f2c3-4656-b32a-c1a132cd2711" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_brazil_cpf"/>
       <Match idRef="Keyword_brazil_cpf"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_brazil_cpf"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_brazil_cpf

 CPF
 Identification
 Registration
 Revenue
 Cadastro de Pessoas Físicas
 Imposto
 Identificação
 Inscrição
 Receita

Brazil National ID Card (RG)
Format:

      Registro Geral (old format): Nine digits plus delimiters

      Registro de Identidade (RIC) (new format): 11 digits plus a hyphen

Pattern:

Registro Geral (old format):

      Two digits

      A period

      Three digits

      A period

      Three digits

      A hyphen

      One digit which is a check digit

Registro de Identidade (RIC) (new format)

      10 digits

      A hyphen

      One digit which is a check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

<!-- p.2391 -->

       The function Func_brazil_rg finds content that matches the pattern.

       A keyword from Keyword_brazil_rg is found.

       The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The function Func_brazil_rg finds content that matches the pattern.

       The checksum passes.

  <!-- Brazil National ID Card (RG) -->
  <Entity id="486de900-db70-41b3-a886-abdf25af119c" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_brazil_rg"/>
       <Match idRef="Keyword_brazil_rg"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_brazil_rg"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_brazil_rg

 National ID
 Registration
 Cédula de identidade
 Registro Geral
 RG
 Registro de Identidade
 RIC
 Número de registo
 Registro

Canada Bank Account Number
Format: Seven or twelve digits

Pattern: A Canada Bank Account Number is seven or twelve digits. A Canada bank account transit number is:

       Five digits

       A hyphen

       Three digits

       OR

       A zero "0"

       Eight digits

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The regular expression Regex_canada_bank_account_number finds content that matches the pattern.

       A keyword from Keyword_canada_bank_account_number is found.

       The regular expression Regex_canada_bank_account_transit_number finds content that matches the pattern.

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

<!-- p.2392 -->

     The regular expression Regex_canada_bank_account_number finds content that matches the pattern.

     A keyword from Keyword_canada_bank_account_number is found.

  <!-- Canada Bank Account Number -->
  <Entity id="552e814c-cb50-4d94-bbaa-bb1d1ffb34de" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_canada_bank_account_number" />
          <Match idRef="Keyword_canada_bank_account_number" />
          <Match idRef="Regex_canada_bank_account_transit_number" />
     </Pattern>
     <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_canada_bank_account_number" />
          <Match idRef="Keyword_canada_bank_account_number" />
     </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_canada_bank_account_number

 canada savings bonds
 canada revenue agency
 canadian financial institution
 direct deposit form
 canadian citizen
 legal representative
 notary public
 commissioner for oaths
 child care benefit
 universal child care
 canada child tax benefit
 income tax benefit
 harmonized sales tax
 social insurance number
 income tax refund
 child tax benefit
 territorial payments
 institution number
 deposit request
 banking information
 direct deposit

Canada Driver's License Number
Format: Varies by province

Pattern: Various patterns covering Alberta, British Columbia, Manitoba, New Brunswick, Newfoundland/Labrador, Nova Scotia, Ontario, Prince
Edward Island, Quebec, and Saskatchewan

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_[province_name]_drivers_license_number finds content that matches the pattern.

     A keyword from Keyword_[province_name]_drivers_license_name is found.

     A keyword from Keyword_canada_drivers_license is found.

  <!-- Canada Driver's License Number -->
      <Entity id="37186abb-8e48-4800-ad3c-e3d1610b3db0" patternsProximity="300" recommendedConfidence="75">
        <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_alberta_drivers_license_number" />

<!-- p.2393 -->

           <Match idRef="Keyword_alberta_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_british_columbia_drivers_license_number" />
           <Match idRef="Keyword_british_columbia_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_manitoba_drivers_license_number" />
           <Match idRef="Keyword_manitoba_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_new_brunswick_drivers_license_number" />
           <Match idRef="Keyword_new_brunswick_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_newfoundland_labrador_drivers_license_number" />
           <Match idRef="Keyword_newfoundland_labrador_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_nova_scotia_drivers_license_number" />
           <Match idRef="Keyword_nova_scotia_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_ontario_drivers_license_number" />
           <Match idRef="Keyword_ontario_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_prince_edward_island_drivers_license_number" />
           <Match idRef="Keyword_prince_edward_island_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_quebec_drivers_license_number" />
           <Match idRef="Keyword_quebec_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
         <Pattern confidenceLevel="75">
           <IdMatch idRef="Func_saskatchewan_drivers_license_number" />
           <Match idRef="Keyword_saskatchewan_drivers_license_name" />
           <Match idRef="Keyword_canada_drivers_license" />
         </Pattern>
       </Entity>

Keywords:

                                                                                                                    ﾉ   Expand table

 Keyword_[province_name]_drivers_license_name                                      Keyword_canada_drivers_license

 The province abbreviation, for example AB                                         DL
 The province name, for example Alberta                                            DLS
                                                                                   CDL
                                                                                   CDLS
                                                                                   DriverLic
                                                                                   DriverLics
                                                                                   DriverLicense
                                                                                   DriverLicenses
                                                                                   DriverLicence
                                                                                   DriverLicences
                                                                                   Driver Lic
                                                                                   Driver Lics
                                                                                   Driver License
                                                                                   Driver Licenses
                                                                                   Driver Licence
                                                                                   Driver Licences
                                                                                   DriversLic
                                                                                   DriversLics
                                                                                   DriversLicence
                                                                                   DriversLicences
                                                                                   DriversLicense
                                                                                   DriversLicenses

<!-- p.2394 -->

Keyword_[province_name]_drivers_license_name   Keyword_canada_drivers_license

                                               Drivers Lic
                                               Drivers Lics
                                               Drivers License
                                               Drivers Licenses
                                               Drivers Licence
                                               Drivers Licences
                                               Driver'Lic
                                               Driver'Lics
                                               Driver'License
                                               Driver'Licenses
                                               Driver'Licence
                                               Driver'Licences
                                               Driver' Lic
                                               Driver' Lics
                                               Driver' License
                                               Driver' Licenses
                                               Driver' Licence
                                               Driver' Licences
                                               Driver'sLic
                                               Driver'sLics
                                               Driver'sLicense
                                               Driver'sLicenses
                                               Driver'sLicence
                                               Driver'sLicences
                                               Driver's Lic
                                               Driver's Lics
                                               Driver's License
                                               Driver's Licenses
                                               Driver's Licence
                                               Driver's Licences
                                               Permis de Conduire
                                               id
                                               ids
                                               idcard number
                                               idcard numbers
                                               idcard #
                                               idcard #s
                                               idcard card
                                               idcard cards
                                               idcard
                                               identification number
                                               identification numbers
                                               identification #
                                               identification #s
                                               identification card
                                               identification cards
                                               identification
                                               DL#
                                               DLS#
                                               CDL#
                                               CDLS#
                                               DriverLic#
                                               DriverLics#
                                               DriverLicense#
                                               DriverLicenses#
                                               DriverLicence#
                                               DriverLicences#
                                               Driver Lic#
                                               Driver Lics#
                                               Driver License#
                                               Driver Licenses#
                                               Driver License#
                                               Driver Licences#
                                               DriversLic#
                                               DriversLics#
                                               DriversLicense#
                                               DriversLicenses#
                                               DriversLicence#
                                               DriversLicences#
                                               Drivers Lic#
                                               Drivers Lics#
                                               Drivers License#
                                               Drivers Licenses#

<!-- p.2395 -->

 Keyword_[province_name]_drivers_license_name                                              Keyword_canada_drivers_license

                                                                                           Drivers Licence#
                                                                                           Drivers Licences#
                                                                                           Driver'Lic#
                                                                                           Driver'Lics#
                                                                                           Driver'License#
                                                                                           Driver'Licenses#
                                                                                           Driver'Licence#
                                                                                           Driver'Licences#
                                                                                           Driver' Lic#
                                                                                           Driver' Lics#
                                                                                           Driver' License#
                                                                                           Driver' Licenses#
                                                                                           Driver' Licence#
                                                                                           Driver' Licences#
                                                                                           Driver'sLic#
                                                                                           Driver'sLics#
                                                                                           Driver'sLicense#
                                                                                           Driver'sLicenses#
                                                                                           Driver'sLicence#
                                                                                           Driver'sLicences#
                                                                                           Driver's Lic#
                                                                                           Driver's Lics#
                                                                                           Driver's License#
                                                                                           Driver's Licenses#
                                                                                           Driver's Licence#
                                                                                           Driver's Licences#
                                                                                           Permis de Conduire#
                                                                                           ID#
                                                                                           IDs#
                                                                                           idcard card#
                                                                                           idcard cards#
                                                                                           idcard#
                                                                                           identification card#
                                                                                           identification cards#
                                                                                           identification#

Canada Health Service Number
Format: 10 digits

Pattern: 10 digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_canada_health_service_number finds content that matches the pattern.

     A keyword from Keyword_canada_health_service_number is found.

  <!-- Canada Health Service Number -->
  <Entity id="59c0bf39-7fab-482c-af25-00faa4384c94" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_canada_health_service_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_canada_health_service_number" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

<!-- p.2396 -->

 Keyword_canada_health_service_number

 personal health number
 patient information
 health services
 speciality services
 automobile accident
 patient hospital
 psychiatrist
 workers compensation
 disability

Canada Passport Number
Format: Two uppercase letters followed by six digits

Pattern: Two uppercase letters followed by six digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_canada_passport_number finds content that matches the pattern.

      A keyword from Keyword_canada_passport_number or Keyword_passport is found.

  <!-- Canada Passport Number -->
  <Entity id="14d0db8b-498a-43ed-9fca-f6097ae687eb" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_canada_passport_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_canada_passport_number" />
            <Match idRef="Keyword_passport" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_canada_passport_number                                                                Keyword_passport

 canadian citizenship                                                                          Passport Number
 canadian passport                                                                             Passport No
 passport application                                                                          Passport #
 passport photos                                                                               Passport#
 certified translator                                                                          PassportID
 canadian citizens                                                                             Passportno
 processing times                                                                              passportnumber
 renewal application                                                                           パスポート
                                                                                               パスポート番号
                                                                                               パスポートのNum
                                                                                               パスポート＃
                                                                                               Numéro de passeport
                                                                                               Passeport n °
                                                                                               Passeport Non
                                                                                               Passeport #
                                                                                               Passeport#
                                                                                               PasseportNon
                                                                                               Passeportn °

Canada Personal Health Identification Number (PHIN)
Format: Nine digits

<!-- p.2397 -->

Pattern: Nine digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_canada_phin finds content that matches the pattern.

      At least two keywords from Keyword_canada_phin or Keyword_canada_provinces are found..

  <!-- Canada PHIN -->
  <Entity id="722e12ac-c89a-4ec8-a1b7-fea3469f89db" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_canada_phin" />
          <Any minMatches="2">
            <Match idRef="Keyword_canada_phin" />
            <Match idRef="Keyword_canada_provinces" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_canada_phin                                                   Keyword_canada_provinces

 social insurance number                                               Nunavut
 health information act                                                Quebec
 income tax information                                                Northwest Territories
 manitoba health                                                       Ontario
 health registration                                                   British Columbia
 prescription purchases                                                Alberta
 benefit eligibility                                                   Saskatchewan
 personal health                                                       Manitoba
 power of attorney                                                     Yukon
 registration number                                                   Newfoundland and Labrador
 personal health number                                                New Brunswick
 practitioner referral                                                 Nova Scotia
 wellness professional                                                 Prince Edward Island
 patient referral                                                      Canada
 health and wellness

Canada Social Insurance Number
Format: Nine digits with optional hyphens or spaces

Pattern:

Formatted:

      Three digits

      A hyphen or space

      Three digits

      A hyphen or space

      Three digits

Unformatted: Nine digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

<!-- p.2398 -->

        The function Func_canadian_sin finds content that matches the pattern.

        At least two of any combinations of the following:

          A keyword from Keyword_sin is found.

          A keyword from Keyword_sin_collaborative is found.

          The function Func_eu_date finds a date in the right date format.

        The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

        The function Func_unformatted_canadian_sin finds content that matches the pattern.

        A keyword from Keyword_sin is found.

        The checksum passes.

  <!-- Canada Social Insurance Number -->
  <Entity id="a2f29c85-ecb8-4514-a610-364790c0773e" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_canadian_sin" />
          <Any minMatches="2">
            <Match idRef="Keyword_sin" />
            <Match idRef="Keyword_sin_collaborative" />
            <Match idRef="Func_eu_date" />
          </Any>
    </Pattern>
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_unformatted_canadian_sin" />
          <Match idRef="Keyword_sin" />
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_sin                                                                    Keyword_sin_collaborative

 sin                                                                            driver's license
 social insurance                                                               drivers license
 numero d'assurance sociale                                                     driver's licence
 sins                                                                           drivers licence
 ssn                                                                            DOB
 ssns                                                                           Birthdate
 social security                                                                Birthday
 numero d'assurance social                                                      Date of Birth
 national identification number
 national id
 sin#
 soc ins
 social ins

Chile Identity Card Number
Format: 7-8 digits plus delimiters a check digit or letter

Pattern: 7-8 digits plus delimiters:

        1-2 digits

        A period

        Three digits

        A period

<!-- p.2399 -->

      Three digits

      A dash

      One digit or letter (not case sensitive) which is a check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_chile_id_card finds content that matches the pattern.

      A keyword from Keyword_chile_id_card is found.

      The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_chile_id_card finds content that matches the pattern.

      The checksum passes.

  <!-- Chile Identity Card Number -->
  <Entity id="4e979794-49a0-407e-a0b9-2c536937b925" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_chile_id_card"/>
       <Match idRef="Keyword_chile_id_card"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_chile_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_chile_id_card

 National Identification Number
 Identity card
 ID
 Identification
 Rol Único Nacional
 RUN
 Rol Único Tributario
 RUT
 Cédula de Identidad
 Número De Identificación Nacional
 Tarjeta de identificación
 Identificación

China Resident Identity Card (PRC) Number
Format: 18 digits

Pattern: 18 digits:

      Six digits which are an address code

      Eight digits in the form YYYYMMDD, which are the date of birth

      Three digits that are an order code

      One digit that is a check digit

Checksum: Yes

<!-- p.2400 -->

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_china_resident_id finds content that matches the pattern.

      A keyword from Keyword_china_resident_id is found.

      The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_china_resident_id finds content that matches the pattern.

      The checksum passes.

  <!-- China Resident Identity Card (PRC) Number -->
  <Entity id="c92daa86-2d16-4871-901f-816b3f554fc1" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_china_resident_id"/>
       <Match idRef="Keyword_china_resident_id"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_china_resident_id"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_china_resident_id

 Resident Identity Card
 PRC
 National Identification Card
 身份证
 居民 身份证
 居民身份证
 鉴定
 身分證
 居民 身份證
 鑑定

Credit Card Number
Format: 14 digits that can be formatted or unformatted (dddddddddddddd) and must pass the Luhn test.

Pattern: Very complex and robust pattern that detects cards from all major brands worldwide, including Visa, MasterCard, Discover Card, JCB,
American Express, gift cards, and diner cards.

Checksum: Yes, the Luhn checksum

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_credit_card finds content that matches the pattern.

      One of the following is true:

         A keyword from Keyword_cc_verification is found.

         A keyword from Keyword_cc_name is found.

         The function Func_expiration_date finds a date in the right date format.

      The checksum passes.
