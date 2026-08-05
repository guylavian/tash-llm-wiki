---
title: "Exchange Server — pages 1241-1280"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1241-1280
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1241-1280
family: exchange
documentKind: "doc"
abstract: "If you successfully purged the mailbox, the command won't return any results. If the mailbox wasn't purged, the command will return information about the mailbox. Use the Exchange Management Shell to find the disconnected mailbox type A disconnected mailbox can be either disable"
---

# Exchange Server — pages 1241-1280

<!-- p.1241 -->

     If you successfully purged the mailbox, the command won't return any results. If the
     mailbox wasn't purged, the command will return information about the mailbox.

Use the Exchange Management Shell to find the
disconnected mailbox type
A disconnected mailbox can be either disabled or soft-deleted. You need to specify the correct
type to permanently delete a disconnected mailbox. If you don't, the command will fail.

Replace <DisplayName> with the display name of the mailbox and run the following command
to determine whether a disconnected mailbox is disabled or soft-deleted:

  PowerShell

  $dbs = Get-MailboxDatabase
  $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
  {$_.DisplayName -eq "<DisplayName>"} | Format-List
  DisplayName,MailboxGuid,Database,DisconnectReason

The value for the DisconnectReason property will be either Disabled or SoftDeleted .

You can run the following commands to display the type for all disconnected mailboxes in your
organization:

  PowerShell

  $dbs = Get-MailboxDatabase
  $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
  {$_.DisconnectReason -ne $null} | Format-List
  DisplayName,MailboxGuid,Database,DisconnectReason

Use the Exchange Management Shell to
permanently delete a disconnected mailbox

  Ｕ Caution

  When you use the Remove-StoreMailbox cmdlet to permanently delete a disconnected
  mailbox, all its contents are purged from the mailbox database and the data loss is
  permanent.

<!-- p.1242 -->

This example permanently deletes the disabled mailbox with the GUID 2ab32ce3-fae1-4402-
9489-c67e3ae173d3 from mailbox database named MBD01.

  PowerShell

  Remove-StoreMailbox -Database MBD01 -Identity "2ab32ce3-fae1-4402-9489-
  c67e3ae173d3" -MailboxState Disabled

This example permanently deletes the soft-deleted mailbox for Dan Jump from mailbox
database named MBD01.

  PowerShell

  Remove-StoreMailbox -Database MBD01 -Identity "Dan Jump" -MailboxState SoftDeleted

This example permanently deletes all soft-deleted mailboxes from mailbox database named
MBD01.

  PowerShell

  Get-MailboxStatistics -Database MBD01 | where {$_.DisconnectReason -eq
  "SoftDeleted"} | ForEach {Remove-StoreMailbox -Database $_.Database -Identity
  $_.MailboxGuid -MailboxState SoftDeleted}

For detailed syntax and parameter information, see Remove-StoreMailbox and Get-
MailboxStatistics.

How do you know this worked?
To verify that you've permanently deleted a disconnected mailbox and that it was successfully
purged from the mailbox database, replace <DisplayName> with the display name of the
mailbox and run the following command:

  PowerShell

  $dbs = Get-MailboxDatabase
  $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
  {$_.DisplayName -eq "<DisplayName>"}

If you successfully purged the mailbox, the command won't return any results. If the mailbox
wasn't purged, the command will return information about the mailbox.

<!-- p.1243 -->

Custom attributes in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016    2019      Subscription Edition

Exchange Server includes 15 extension attributes that you can use to add information about a
recipient, such as an employee ID, organizational unit (OU), or some other custom value for
which there isn't an existing attribute.

In earlier versions of Exchange, if you wanted to store this information in Active Directory, you
had to create an attribute by extending the Active Directory schema. Schema extension
requires planning, procuring object identifiers (OIDs) for new attributes, and testing the
extension process in a test environment before you implement it in a production environment.
Exchange Server doesn't let you use schema extensions in recipient filters that are used by
address lists, e-mail address policies, and dynamic distribution groups.

The custom attributes available to Exchange Server are labeled in Active Directory as ms-Exch-
Extension-Attribute1 through ms-Exch-Extension-Attribute15. In the Exchange Management
Shell, the corresponding parameters are CustomAttribute1 through CustomAttribute15. These
attributes aren't used by any Exchange components. They can be used to store Active Directory
data without having to extend the Active Directory schema.

  ７ Note

  ms-Exch-Extension-Attribute-16 to ms-Exch-Extension-Attribute-45 are present in Active
  Directory, but aren't available in the Exchange admin center (EAC) or the Exchange
  Management Shell. Don't use non-Exchange tools to edit these attributes because they
  might be used for future Exchange features.

Advantages of custom attributes
There are several advantages to using custom attributes:

      You avoid extending the Active Directory schema.

      You don't have to do the work, because the attributes are created by Exchange Setup.

      You can use the EAC or the Exchange Management Shell to manage the attributes. You
      don't need to build custom controls or write scripts to populate and display these
      attributes.

<!-- p.1244 -->

     You can filter and reuse the attributes, as attributes are filterable properties that can be
     used in the Filter parameter with recipient cmdlets such as Get-Mailbox. They can also be
     used in the EAC and the Exchange Management Shell to create filters for e-mail address
     policies, address lists, and dynamic distribution groups.

Multivalued custom attributes
Starting with Exchange 2010 Service Pack 2 (SP2), five multivalued custom attributes were
added to Exchange to allow you to store additional information for mail recipients if the
traditional custom attributes didn't meet your needs. The ExtensionCustomAttribute1 to
ExtensionCustomAttribute5 parameters can hold up to 1,300 values each. You can specify
multiple values as a comma-delimited list. The following cmdlets support these new
parameters:

     Set-DistributionGroup

     Set-DynamicDistributionGroup

     Set-Mailbox

     Set-MailContact

     Set-MailPublicFolder

     Set-RemoteMailbox

For more information about multivalued properties, see Modifying multivalued properties.

Custom attribute examples
A common scenario in many Exchange deployments is that of creating an e-mail address policy
for all recipients in an OU. The OU isn't a filterable property that can be used in the
RecipientFilter parameter of an e-mail address policy or an address list.

  ７ Note

  Dynamic distribution groups have an additional parameter that you can use to restrict it to
  recipients in a particular OU or container.

If the recipients in a particular OU don't share any common properties that you can filter by,
such as department or location, you can populate one of the custom attributes with a common
value, as shown in this example.

<!-- p.1245 -->

  PowerShell

  Get-Mailbox -OrganizationalUnit Sales | Set-Mailbox -CustomAttribute1 "SalesOU"

With that done, now you can create an e-mail address policy for all recipients that have the
CustomAttribute1 property that equals SalesOU, as shown in this example.

  PowerShell

  New-EmailAddressPolicy -Name "Sales" -RecipientFilter "CustomAttribute1 -eq
  'SalesOU'" -EnabledEmailAddressTemplates "SMTP:%s%2g@sales.contoso.com"

Custom attribute example using the
ConditionalCustomAttributes parameter
When creating dynamic distribution groups, email address policies, or address lists, you don't
need to use the RecipeintFilter parameter to specify custom attributes. You can use the
ConditionalCustomAttribute1 to ConditionalCustomAttribute15 parameters instead.

This example creates a dynamic distribution group based on the recipients whose
CustomAttribute1 is set to SalesOU.

  PowerShell

  New-DynamicDistributionGroup -Name "Sales Users and Contacts" -IncludedRecipients
  "MailboxUsers,MailContacts" -ConditionalCustomAttribute1 "SalesOU"

  ７ Note

  You need to use the IncludedRecipients parameter if you use a Conditional parameter. In
  addition, you can't use Conditional parameters if you use the RecipientFilter parameter. If
  you want to include additional filters to create your dynamic distribution group, email
  address policies, or address lists, you should use the RecipientFilter parameter.

Custom attribute example using
ExtensionCustomAttributes parameter
In this example, the mailbox for Kweku will have ExtensionCustomAttribute1 updated to reflect
that he's enrolled in the following educational classes: MATH307, ECON202, and ENGL300.

<!-- p.1246 -->

  PowerShell

  Set-Mailbox -Identity Kweku -ExtensionCustomAttribute1 MATH307,ECON202,ENGL300

Next, a dynamic distribution group for all students enrolled MATH307 is created by using the
RecipientFilter parameter where ExtensionCustomAttribute1 is equal to MATH307. When using
the ExtentionCustomAttributes parameters, you can use the -eq operator instead of the -like
operator.

  PowerShell

  New-DynamicDistributionGroup -Name Students_MATH307 -RecipientFilter
  "ExtensionCustomAttribute1 -eq 'MATH307'"

In this example, Kweku's ExtensionCustomAttribute1 values are updated to reflect that he's
added the class ENGL210 and removed the class ECON202.

  PowerShell

  Set-Mailbox -Identity Kweku -ExtensionCustomAttribute1 @{Add="ENGL210";
  Remove="ECON202"}

<!-- p.1247 -->

Manage permissions for recipients
Article • 04/30/2025

APPLIES TO:        2016         2019     Subscription Edition

In Exchange Server, you can use the Exchange admin center (EAC) or the Exchange
Management Shell to assign permissions to a mailbox or group so that other users can access
the mailbox (the Full Access permission), or send email messages that appear to come from the
mailbox or group (the Send As or Send on Behalf permissions). The users that are assigned
these permissions on other mailboxes or groups are called delegates.

The permissions that you can assign to delegates for mailboxes and groups in Exchange Server
are described in the following table:

Note: Although you can use the Exchange Management Shell to assign some or all of these
permissions to other delegate types on other kinds of recipient objects, this topic focuses on
the delegate and recipient object types that produce useful results.

                                                                                         ﾉ   Expand table

 Permission    Description                       Recipient      Additional    Delegate       Additional
                                                 types in       recipient     types in       delegate
                                                 the EAC        types in      the EAC        types in the
                                                                PowerShell                   PowerShell

 Full Access   Allows the delegate to open       User           Arbitration   Mailboxes      User
               the mailbox, and view, add and    mailboxes      mailboxes     with user      accounts
               remove the contents of the        Linked         Discovery     accounts       that aren't
               mailbox. Doesn't allow the        mailboxes      mailboxes     Mail users     mail-
               delegate to send messages                                      with           enabled.
               from the mailbox.                 Resource                     accounts       Universal,
               If you assign the Full Access     mailboxes                                   global, and
               permission to a mailbox that's                                 Mail-          domain local
                                                 Shared                       enabled
               hidden from address lists, the                                                security
                                                 mailboxes                    security
               delegate won't be able to open                                                groups that
               the mailbox. By default,                                       groups         aren't mail-
               arbitration and discovery                                                     enabled.
               mailboxes are hidden from
               address lists.

               By default, the mailbox auto-
               mapping feature uses
               Autodiscover to automatically
               open the mailbox in the
               delegate's Outlook profile (in
               addition to their own mailbox).
               Note that auto-mapping will

<!-- p.1248 -->

Permission   Description                       Recipient      Additional   Delegate     Additional
                                               types in       recipient    types in     delegate
                                               the EAC        types in     the EAC      types in the
                                                              PowerShell                PowerShell

             only work for individual users
             granted the proper permissions
             and will not work for any kind
             of group. If you don't want
             mailboxes to be auto-mapped,
             you need to take one of the
             following actions:

                   Use the Add-
                   MailboxPermission
                   cmdlet in the Exchange
                   Management Shell to
                   assign the Full Access
                   permission with the -
                   AutoMapping $false
                   setting. For more
                   information, see the Use
                   the Exchange
                   Management Shell to
                   assign the Full Access
                   permission to mailboxes
                   section in this topic.
                   Assign the Full Access
                   permission to a (mail-
                   enabled) security group.
                   The mailbox won't open
                   in the Outlook profile of
                   each member.

Send As      Allows the delegate to send       User           n/a          Mailboxes    n/a
             messages as if they came          mailboxes                   with user
             directly from the mailbox or      Linked                      accounts
             group. There's no indication      mailboxes                   Mail users
             that the message was sent by                                  with
             the delegate.                     Resource                    accounts
             Doesn't allow the delegate to     mailboxes
             read the contents of the                                      Mail-
                                               Shared                      enabled
             mailbox.
                                               mailboxes                   security
             If you assign the Send As                                     groups
                                               Distribution
             permission to a mailbox that's
                                               groups
             hidden from address lists, the
             delegate won't be able to send    Dynamic
             messages from the mailbox.        distribution

<!-- p.1249 -->

Permission   Description                         Recipient      Additional   Delegate       Additional
                                                 types in       recipient    types in       delegate
                                                 the EAC        types in     the EAC        types in the
                                                                PowerShell                  PowerShell

                                                 groups

                                                 Mail-
                                                 enabled
                                                 security
                                                 groups

Send on      Allows the delegate to send         User           Shared       Mailboxes      n/a
Behalf       messages from the mailbox or        mailboxes      mailboxes    with user
             group. The From address of          Linked                      accounts
             these messages clearly shows        mailboxes                   Mail users
             that the message was sent by                                    with
             the delegate (" <Delegate> on       Resource                    accounts
             behalf of <MailboxOrGroup>").       mailboxes
             However, replies to these                                       Mail-
                                                 Distribution                enabled
             messages are sent to the
                                                 groups                      security
             mailbox or group, not to the
             delegate.                                                       groups
                                                 Dynamic
                                                 distribution                Distribution
             Doesn't allow the delegate to
                                                 groups                      groups
             read the contents of the
             mailbox.                            Mail-
                                                 enabled
             If you assign the Send on
                                                 security
             Behalf permission to a mailbox
                                                 groups
             that's hidden from address lists,
             the delegate won't be able to
             send messages from the
             mailbox.

 ７ Note

 If a user has both Send As and Send on Behalf permissions to a mailbox or group, the
 Send As permission is always used.|User mailboxes

What do you need to know before you begin?
    Estimated time to complete each procedure: 2 minutes.

    You need to be assigned permissions before you can perform the procedures in this topic.
    To see what permissions you need, see the "Recipient provisioning permissions" entry in
    the Recipients Permissions topic.

<!-- p.1250 -->

   To learn how to open the Exchange Management Shell in your on-premises Exchange
   organization, see Open the Exchange Management Shell.

   Procedures in this topic require specific permissions. See each procedure for its
   permissions information.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server .

Use the EAC to assign permissions to individual
mailboxes
 1. In the EAC, click Recipients in the feature pane. Depending on the type of mailbox that
   you want to assign permissions for, click on one of the following tabs:

         Mailboxes: User or linked mailboxes.

         Resources: Room or equipment mailboxes.

         Shared: Shared mailboxes.

 2. In the list of mailboxes, select the mailbox that you want to assign permissions for, and
   then click Edit   .

 3. On the mailbox properties page that opens, click Mailbox delegation and configure one
   or more of the following permissions:

         Send As: Messages sent by a delegate appear to come from the mailbox.

         Send on Behalf: Messages sent by a delegate have " <Delegate> on behalf of
         <Mailbox>" in the From address. Note that this permission isn't available in the EAC
         for shared mailboxes.

         Full Access: The delegate can open the mailbox and do anything except send
         messages.

   To assign permissions to delegates, click Add     under the appropriate permission. A
   dialog box appears that lists the users or groups that can have the permission assigned to

<!-- p.1251 -->

   them. Select the user or group from the list, and then click Add. Repeat this process as
   many times as necessary. You can also search for users or groups in the search box by
   typing all or part of the name, and then clicking Search    . When you're finished selecting
   delegates, click OK.

   To remove a permission from a delegate, select the delegate in the list under the
   appropriate permission, and then click Remove       .

 4. When you're finished, click Save.

Use the EAC to assign permissions to multiple
mailboxes at the same time
 1. In the EAC, navigate to Recipients > Mailboxes.

 2. Select the mailboxes that you want to assign permissions for. Use click + Shift key + click
   to select a range of mailboxes, or Ctrl key + click to select multiple individual mailboxes.
   The title of the details pane changes to Bulk Edit as shown in the following diagram.

   Note that the mailboxes that you select need to be the same type. For example, if you
   select both user mailboxes and linked mailboxes, you'll get a warning in the details pane
   that says bulk edit won't work.

 3. At the bottom of the details pane, click More options. Under the Mailbox Delegation
   option that appears, choose Add or Remove. Depending on your selection, do one of the

<!-- p.1252 -->

     following steps:

           Add: In the Bulk Add Delegation dialog box that appears, click Add       under the
           appropriate permission (Send As, Send on Behalf, or Full Access). When you're
           finished selecting users or groups to add as delegates, click Save.

           Remove: In the Bulk Remove Delegation dialog box that appears, click Add
           under the appropriate permission (Send As, Send on Behalf, or Full Access). When
           you're finished selecting users or groups to remove from the existing delegates,
           click Save.

Use the EAC to assign permissions to groups
   1. In the EAC, navigate to Recipients > Groups.

   2. In the list of groups, select the group that you want to assign permissions for, and then
     click Edit   .

   3. On the group properties page that opens, click Group delegation and configure one of
     the following permissions:

           Send As: Messages sent by a delegate appear to come from the group.

           Send on Behalf: Messages sent by a delegate have " <Delegate> on behalf of
           <Group>" in the From address.

   4. To assign permissions to delegates, click Add    under the appropriate permission. A
     dialog box appears that lists the users or groups that can have the permission assigned to
     them. Select the user or group from the list, and then click Add. Repeat this process as
     many times as necessary. You can also search for users or groups in the search box by
     typing all or part of the name, and then clicking Search    . When you're finished selecting
     delegates, click OK.

     To remove a permission from a delegate, select the delegate in the list under the
     appropriate permission, and then click Remove      .

   5. When you're finished, click Save.

Use the Exchange Management Shell to assign the
Full Access permission to mailboxes
You use the Add-MailboxPermission and Remove-MailboxPermission cmdlets to manage the
Full Access permission for mailboxes. These cmdlets use the same basic syntax:

<!-- p.1253 -->

  PowerShell

  Add-MailboxPermission -Identity <MailboxIdentity> -User <DelegateIdentity> -
  AccessRights FullAccess -InheritanceType All [-AutoMapping $false]

For more information, see Add-MailboxPermission.

  PowerShell

  Remove-MailboxPermission -Identity <MailboxIdentity> -User <DelegateIdentity> -
  AccessRights FullAccess -InheritanceType All

For more information, see Remove-MailboxPermission.

This example assigns the delegate Raymond Sam the Full Access permission to the mailbox of
Terry Adams.

  PowerShell

  Add-MailboxPermission -Identity "Terry Adams" -User raymonds -AccessRights
  FullAccess -InheritanceType All

This example assigns Esther Valle the Full Access permission to the organization's default
discovery search mailbox, and prevents the mailbox from automatically opening in Esther
Valle's Outlook.

  PowerShell

  Add-MailboxPermission -Identity "DiscoverySearchMailbox{D919BA05-46A6-415f-80AD-
  7E09334BB852}" -User estherv -AccessRights FullAccess -InheritanceType All -
  AutoMapping $false

This example assigns members of the Helpdesk mail-enabled security group the Full Access
permission to the shared mailbox named Helpdesk Tickets.

  PowerShell

  Add-MailboxPermission -Identity "Helpdesk Tickets" -User Helpdesk -AccessRights
  FullAccess -InheritanceType All

This example removes Full Access permission for Jim Hance from Ayla Kol's mailbox.

  PowerShell

<!-- p.1254 -->

  Remove-MailboxPermission -Identity ayla -User "Jim Hance" -AccessRights FullAccess
  -InheritanceType All

How do you know this worked?
To verify that you've successfully assigned or removed the Full Access permission for a delegate
on a mailbox, use either of the following procedures:

     In the properties of the mailbox in the EAC, verify the delegate is or isn't listed in Mailbox
     delegation > Full Access.

     Replace <MailboxIdentity> with the identity of the mailbox and run the following
     command in the Exchange Management Shell to verify that the delegate is or isn't listed..

         PowerShell

         Get-MailboxPermission <MailboxIdentity> | where {$_.AccessRights -like
         'Full*'} | Format-Table -Auto User,Deny,IsInherited,AccessRights

     For more information, see Get-MailboxPermission.

Use the Exchange Management Shell to assign the
Send As permission to mailboxes and groups
You use the Add-AdPermission and Remove-AdPermission cmdlets to manage the Send As
permission for mailboxes. These cmdlets use the same basic syntax:

  PowerShell

  <Add-AdPermission | Remove-AdPermission> -Identity <MailboxOrGroupNameOrDN> -User
  <DelegateIdentity> [-AccessRights ExtendedRight] -ExtendedRights "Send As"

For more information, see Add-AdPermission and Remove-AdPermission.

Notes:

     The Identity parameter requires you to use the Name or DistinguishedName (DN) value
     of the mailbox or group.
         Name: This value may or may not be the same as the display name. For example,
         Felipe Apodaca .

<!-- p.1255 -->

          DistinguishedName: This value always contains the Name value and uses Active
          Directory LDAP syntax. For example, CN=Felipe Apodaca,CN=Users,DC=contoso,DC=com .

     To find these values for a mailbox or group, you can use the Get-Recipient cmdlet, which
     accepts many different values for the Identity parameter. For example:

          PowerShell

          Get-Recipient -Identity helpdesk@contoso.com | Format-List
          Name,DistinguishedName

     The commands work with or without -AccessRights ExtendedRight , which is why it's
     shown as optional in the syntax.

This example assigns the Send As permission to the Helpdesk mail-enabled security group on
the shared mailbox named Helpdesk Support Team.

  PowerShell

  Add-ADPermission -Identity "Helpdesk Support Team" -User Helpdesk -ExtendedRights
  "Send As"

This example removes the Send As permission for the user Pilar Pinilla on the mailbox of James
Alvord.

  PowerShell

  Remove-ADPermission -Identity "James Alvord" -User pilarp -ExtendedRights "Send
  As"

How do you know this worked?
To verify that you've successfully assigned or removed the Send As permission for a delegate
on a mailbox or group, use either of the following procedures:

     In the properties of the mailbox or group in the EAC, verify the delegate is or isn't listed in
     Mailbox delegation > Send As or Group delegation > Send As.

     Replace <MailboxOrGroupNameOrDN> with the name or distinguished name of the
     mailbox or group and run the following command in the Exchange Management Shell to
     verify that the delegate is or isn't listed.

          PowerShell

<!-- p.1256 -->

        Get-ADPermission -Identity <MailboxOrGroupNameOrDN> | where
        {$_.ExtendedRights -like 'Send*'} | Format-Table -Auto
        User,Deny,ExtendedRights

     For more information, see Get-AdPermission.

Use the Exchange Management Shell to assign the
Send on Behalf permission to mailboxes and
groups
You use the GrantSendOnBehalfTo parameter on the various mailbox and group Set- cmdlets to
manage the Send on Behalf permission for mailboxes and groups:

     Set-Mailbox

     Set-DistributionGroup: Distribution groups and mail-enabled security groups.

     Set-DynamicDistributionGroup

The basic syntax for these cmdlets is:

  PowerShell

  <Cmdlet> -Identity <MailboxOrGroupIdentity> -GrantSendOnBehalfTo <Delegates>

The GrantSendOnBehalfTo parameter has the following options for delegate values:

     Replace existing delegates: <DelegateIdentity> or "<DelegateIdentity1>","
     <DelegateIdentity2>",...

     Add or remove delegates without affecting other delegates: @{Add="\<value1\>","\
     <value2\>"...; Remove="\<value1\>","\<value2\>"...}

     Remove all delegates: Use the value $null .

This example assigns the delegate Holly Holt the Send on Behalf permission to the mailbox of
Sean Chai.

  PowerShell

  Set-Mailbox -Identity seanc@contoso.com -GrantSendOnBehalfTo hollyh

<!-- p.1257 -->

This example adds the group tempassistants@contoso.com to the list of delegates that have
Send on Behalf permission to the Contoso Executives shared mailbox.

  PowerShell

  Set-Mailbox "Contoso Executives" -GrantSendOnBehalfTo
  @{Add="tempassistants@contoso.com"}

This example assigns the delegate Sara Davis the Send on Behalf permission to the Printer
Support distribution group.

  PowerShell

  Set-DistributionGroup -Identity printersupport@contoso.com -GrantSendOnBehalfTo
  sarad

This example removes the Send on Behalf permission that was assigned to the administrator
on the All Employees dynamic distribution group.

  PowerShell

  Set-DynamicDistributionGroup "All Employees" -GrantSendOnBehalfTo
  @{Remove="Administrator"}

How do you know this worked?
To verify that you've successfully assigned or removed the Send on Behalf permission for a
delegate on a mailbox or group, use either of the following procedures:

     In the properties of the mailbox or group in the EAC, verify the delegate is or isn't listed in
     Mailbox delegation > Send As or Group delegation > Send As.

     Replace <MailboxIdentity> or <GroupIdentity> with the identity of the mailbox or group
     and run the one of the following commands in the Exchange Management Shell to verify
     that the delegate is or isn't listed.

        Mailbox:

           PowerShell

           Get-Mailbox -Identity <MailboxIdentity> | Format-List GrantSendOnBehalfTo

        Group:

<!-- p.1258 -->

          PowerShell

          Get-DistributionGroup -Identity <GroupIdentity> | Format-List
          GrantSendOnBehalfTo

        Dynamic distribution group:

          PowerShell

          Get-DynamicDistributionGroup -Identity <GroupIdentity> | Format-List
          GrantSendOnBehalfTo

Next steps
For more information about how delegates can use the permissions that are assigned to them
on mailboxes and groups, see the following topics:

     Access another person's mailbox

     Open and use a shared mailbox in Outlook for Windows

     Open and use a shared mailbox in Outlook on the web

<!-- p.1259 -->

Mailbox moves in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

You use mailbox moves to move mailboxes to, from, and within your Exchange organization.
These are the basic types of mailbox moves that are available:

      Local mailbox moves: You move mailboxes from one mailbox database to another on
      Exchange servers within a single Active Directory forest. For instructions, see Manage on-
      premises mailbox moves in Exchange Server.

      Cross-forest mailbox moves: You move mailboxes to Exchange servers in a different
      Active Directory forest. You can initiate the move from the target forest where you want
      to move the mailboxes (known as a pull move type), or from the source forest that
      currently hosts the mailboxes (known as a push move type). For more information, see
      Prepare mailboxes for cross-forest move requests.

      Remote mailbox moves in hybrid deployments: In hybrid deployments between on-
      premises Exchange and Microsoft Office 365, you can move mailboxes from Exchange to
      Microsoft 365 or Office 365 (known as onboarding remote move migrations) and from
      Microsoft 365 or Office 365 to Exchange (know as offboarding remote move migrations).
      For more information, see Move mailboxes between on-premises and Exchange Online
      organizations in hybrid deployments.

  ７ Note

  For more information about migrating on-premises Exchange organizations to Microsoft
  365 or Office 365, see Ways to migrate multiple email accounts to Microsoft 365 or
  Office 365.

Mailbox moves in Exchange 2016 and Exchange 2019 use the batch move architecture that was
introduced in Exchange 2013. The batch move architecture gives you the ability to move
mailboxes in large batches. The enhanced management capabilities in the batch move
architecture includes:

      Email notification during move with reporting.

      Automatic retry and automatic prioritization of moves.

      Move primary and personal archive mailboxes together or separately.

<!-- p.1260 -->

     Option for manual move request finalization to let you review your move before
     completion.

     Periodic incremental syncs to update migration changes.

You can move mailboxes in the Exchange admin center (EAC), or by using the New-
MoveRequest or New-MigrationBatch cmdlets in the Exchange Management Shell.

Scenarios for local and cross-forest mailbox moves
These are some scenarios for local mailbox moves:

     Upgrade: When you upgrade from an earlier version of Exchange, you move mailboxes
     from the existing Exchange servers to an Exchange Mailbox server.

     Realignment: For example, you might want to move a mailbox to a database that has a
     larger mailbox size limit.

     Investigate an issue: If you need to investigate an issue with a mailbox, you can move
     that mailbox to a different server. For example, you can move all mailboxes that have high
     activity to another server.

     Corrupted mailboxes: If you encounter corrupted mailboxes, you can move the mailboxes
     to a different server or database. The corrupted messages won't be moved.

     Physical location changes: You can move mailboxes to a server in a different Active
     Directory site. For example, if a user moves to a different physical location, you can move
     that user's mailbox to a server closer to the new location.

These are some scenarios for cross-forest mailbox moves:

     Separation of administrative roles: You might want to separate Exchange administration
     from Active Directory user account administration. To do this, you can move mailboxes
     from a single forest into a resource forest scenario. In this scenario, the Exchange
     mailboxes reside in one forest and their associated Active Directory user accounts reside
     in a different forest.

     Outsourced email administration: You might want to outsource the administration of
     email and retain the administration of Active Directory user accounts. To do this, you can
     move mailboxes from a single forest into a resource forest scenario.

     Integrate email and user account administration: You might want to change from a
     separated or outsourced email administration model to a model where email and user
     accounts can be managed from within the same forest. To do this, you can move

<!-- p.1261 -->

     mailboxes from a resource forest scenario to a single forest. In this scenario, the Exchange
     mailboxes and Active Directory user accounts reside in the same forest.

CSV files for mailbox moves
One of the major benefits of the batch move architecture is the ability to use a comma-
separated value (CSV) to specify the mailboxes to move. The information that's required in the
CSV file depends on the type of move. For more information, see CSV Files for Mailbox
Migration.

Migration endpoints for cross-forest and remote
mailbox moves
You use migration endpoints for cross-forest mailbox moves, and remote mailbox moves
between Exchange and Microsoft 365 or Office 365 in hybrid deployments. You don't use
migration endpoints for local mailbox moves.

Migration endpoints specify the remote server information, source throttling settings, and the
required credentials for migrating the mailboxes.

     Cross-forest mailbox moves require an ExchangeRemoteMove migration endpoint.

     Onboarding mailbox move migrations in hybrid organizations (from Exchange to
     Microsoft 365 or Office 365) require an ExchangeRemoteMove migration endpoint as the
     source of the migration batch.

     Offboarding mailbox move migrations in hybrid organizations (from Microsoft 365 or
     Office 365 to Exchange) require an ExchangeRemoteMove migration endpoint as the
     target of the migration batch.

You can create migration endpoints in the EAC or by using the New-MigrationEndpoint cmdlet
in the Exchange Management Shell.

MRS Proxy endpoints for cross-forest and remote
mailbox moves
The Mailbox Replication Service Proxy (MRS Proxy) facilitates cross-forest mailbox moves and
remote move migrations. By default, the EWS virtual directories on Mailbox servers aren't
configured to accept incoming move requests, so you'll need to enable the MRS Proxy
endpoint.

<!-- p.1262 -->

     For cross-forest moves from the target forest (pull moves), you need to enable the MRS
     Proxy endpoint of the EWS virtual directories on Mailbox servers in the source forest.

     For cross-forest moves from the source forest (push moves), you need to enable the MRS
     Proxy endpoint of the EWS virtual directories on Mailbox servers in the target forest.

     For both onboarding and offboarding remote move migrations in hybrid deployments,
     you need to enable the MRS Proxy endpoint of the EWS virtual directories on Mailbox
     servers in the on-premises Exchange organization.

For more information, see Enable the MRS Proxy endpoint for remote moves.

<!-- p.1263 -->

Mailbox imports and exports in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Exchange Server uses the Microsoft Exchange Mailbox Replication service (MRS) to import .pst
files to mailboxes, and export mailboxes to .pst files. The advantages of using MRS instead of
Outlook to import and export mailboxes are:

      Import and export requests are asynchronous (you can import and export multiple .pst
      files at the same time).

      Imports and exports take advantage of the queuing and throttling that's provided by the
      MRS.

      You can import a .pst file directly to a user's archive mailbox.

      The source or destination .pst files can reside on any network share that's accessible by
      your Exchange servers.

This feature was introduced in Exchange 2010 Service Pack 1 (SP1). In Exchange 2010, the MRS
runs on Client Access servers. In Exchange 2013 or later, the MRS runs in the backend services
on Mailbox servers (not in the frontend Client Access services).

  ７ Note

  Mailbox imports and exports are available only in the Mailbox Import Export role, and by
  default, that role isn't assigned to a role group. To use these features, you need to add the
  Mailbox Import Export role to a role group that you belong to (for example, the
  Organization Management role group). For more information, see Add a role to a role
  group.

Reasons to import or export mailboxes
As an administrator, you might need to import .pst files to mailboxes or export mailboxes to
.pst files. For example:

      Compliance requirements: You can export a mailbox to a .pst file for legal discovery
      purposes. After the export is complete, you can import the .pst file to a mailbox that's
      specifically used for compliance purposes.

<!-- p.1264 -->

     Create a point-in-time snapshot of a mailbox: Suppose you're keeping a backup of an
     entire mailbox database for just a few mailboxes. By exporting those mailboxes to .pst
     files, you can eliminate the mailbox database backup.

     Get content out of .pst files and into mailboxes: Typically, Outlook users can save their
     email messages locally in .pst files. You can import users' .pst files to their primary
     mailboxes or archive mailboxes. This is an easy method for transferring email from a
     user's local computer to an Exchange server.

Considerations
Before you import .pst files to mailboxes, or export mailboxes to .pst files, consider these
issues:

     You need to use a UNC network share (\ <Server>\ <Share>\ or \
     <LocalServerName>\c$). The Exchange Trusted Subsystem security group requires
     permissions to the network share (Read for imports, Read/Write for exports). If the share
     doesn't have these permissions, you'll get errors when you try to import or export .pst
     files.

     We recommend that you don't try to import or export .pst files that are larger than 50
     gigabytes (GB), because 50 GB is the maximum .pst file size that's supported by current
     versions of Outlook. You can export mailboxes that are larger than 50 GB to .pst files by
     using multiple export requests that include or exclude specific folders, or by using a
     content filter.

     The operations may take several hours depending on the size of the .pst files or
     mailboxes, the available network bandwidth, and MRS throttling.

     You can't import .pst files to public folders.

Import .pst files to mailboxes
Here are some things to consider when you import .pst files to mailboxes:

     You can create new mailbox import requests in the EAC or the Exchange Management
     Shell. To view, modify, suspend, resume, or remove mailbox import requests, you need to
     use the Exchange Management Shell.

     You can import the .pst file to a different mailbox. For example, you can export data from
     john@contoso.com and import it to legaldiscovery@contoso.com.

<!-- p.1265 -->

     You can import the .pst file directly to the user's personal archive instead of their primary
     mailbox.

     By default, associated messages are imported if they exist in the .pst file. Associated
     messages are special messages that contain hidden data with information about rules,
     views, and forms. You can change this setting in the Exchange Management Shell (the
     AssociatedMessagesCopyOption parameter).

     By default, the Recoverable Items folder is imported if it exists in the .pst file. You can
     change this setting in the Exchange Management Shell (the ExcludeDumpster switch).

     In the Exchange Management Shell, you can include or exclude specific folders to import
     (the IncludeFolders, ExcludeFolders, or SourceRootFolder parameters).

     In the Exchange Management Shell, you can specify the destination folder for imported
     items in the target mailbox (the TargetRootFolder parameter).

     In the Exchange Management Shell, you can increase or decrease the priority value for
     mailbox import requests (the Priority parameter).

For mailbox import procedures, see Procedures for mailbox imports from .pst files in Exchange
Server.

Export mailboxes to .pst files
Here are some things to consider when you export mailboxes to .pst files:

     You can create new mailbox export requests in the EAC or the Exchange Management
     Shell. To view, modify, suspend, resume, or remove mailbox export requests, you need to
     use the Exchange Management Shell.

     You can export a mailbox or a user's archive mailbox to a .pst file.

     By default, associated messages are exported from the mailbox. Associated messages are
     special messages that contain hidden data with information about rules, views, and forms.
     You can change this setting in the Exchange Management Shell (the
     AssociatedMessagesCopyOption parameter).

     By default, the Recoverable Items folder is exported from the mailbox. You can change
     this setting in the Exchange Management Shell (the ExcludeDumpster switch).

     In the Exchange Management Shell, you can filter the messages to export from the
     mailbox (the ContentFilter parameter). You can filter by message content, attachment,

<!-- p.1266 -->

     senders, recipients, Inbox category, importance, message type, message size, and when
     the message was sent, received, or expired.

     In the Exchange Management Shell, you can include or exclude specific folders to export
     (the IncludeFolders, ExcludeFolders, or SourceRootFolder parameters).

     In the Exchange Management Shell, you can specify the destination folder for exported
     items in the target .pst file (the TargetRootFolder parameter).

     In the Exchange Management Shell, you can increase or decrease the priority value for
     mailbox export requests (the Priority parameter).

For mailbox export procedures, see Procedures for mailbox exports to .pst files in Exchange
Server.

<!-- p.1267 -->

Procedures for mailbox imports from .pst
files in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Mailbox import requests use the Microsoft Exchange Mailbox Replication service (MRS) to
import the contents of .pst files into mailboxes. For more information, see Mailbox imports and
exports in Exchange Server.

This topic shows you how to:

      Create mailbox import requests

      View mailbox import requests.

      Modify mailbox import requests that haven't completed.

      Suspend mailbox import requests that haven't completed or failed.

      Resume suspended or failed mailbox import requests

      Remove mailbox import requests.

What do you need to know before you begin?

  ） Important

  The procedures in this topic require the Mailbox Import Export role, which isn't assigned
  to any role groups by default. To assign the role to a role group that you belong to, see
  Add a role to a role group. Note that changes in permission require you to log off and
  log on for the changes to take effect.

      Estimated time to complete each procedure: 5 minutes

      You need to import the .pst files from a UNC network share (\ <Server>\ <Share>\ or \
      <LocalServerName>\c$). The Exchange Trusted Subsystem security group requires the
      Read permission to the network share. If the share doesn't have this permission, you'll get
      errors when you try to import .pst files to mailboxes.

      You can create mailbox import requests in the Exchange admin center (EAC) or in the
      Exchange Management Shell. All other procedures can only be done in the Exchange
      Management Shell. For more information about accessing and using the EAC, see

<!-- p.1268 -->

   Exchange admin center in Exchange Server. To learn how to open the Exchange
   Management Shell in your on-premises Exchange organization, see Open the Exchange
   Management Shell.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Create mailbox import requests

Use the EAC to create a mailbox import request
 1. In the EAC, go to Recipients > Mailboxes > click More options   , and select Import PST.

 2. The Import from a .pst wizard opens. On the first page, enter the UNC path and filename
   of the source .pst file.

<!-- p.1269 -->

  When you're finished, click Next.

3. On the next page, select the target mailbox, and then select one of these options:

       Import to this mailbox

       Import to this mailbox's archive

  When you're finished, click Next.

4. On the last page, configure one of these settings:

       Leave the Send email to the mailbox below when the .pst file has been exported
       check box selected. Click Browse to add or remove notification recipients.

       Clear the Send email to the mailbox below when the .pst file has been exported
       check box.

<!-- p.1270 -->

     When you're finished, click Finish.

Use the Exchange Management Shell to create a mailbox
import request
To create a mailbox import request, use this syntax:

  PowerShell

  New-MailboxImportRequest [-Name <UniqueName>] -FilePath <UNCPathToPST> -Mailbox
  <TargetMailboxIdentity> [-IsArchive] [-SourceRootFolder <PSTFolder>] [-
  TargetRootFolder <MailboxFolder>] [-IncludeFolders <MailboxFolder1>,
  <MailboxFolder2>...] [-ExcludeFolders <MailboxFolder1>,<MailboxFolder2>...] [-
  Priority <PriorityValue>]

This example creates a new mailbox import request with these settings:

     Mailbox import request name: The default value MailboxImport is used, because we
     aren't using the Name parameter. The unique identity of the mailbox import request is
     <MailboxIdentity>\MailboxImportX (X is either not present, or has the value 0 to 9).

     Source .pst file: \\SERVER01\PSTFiles\Archives\Vbarrios.pst

     Target mailbox: Valeria Barrios

     Content and folders: Content in all folder paths in the .pst file is replicated in the target
     mailbox. Content is merged under existing folders and new folders are created if they
     don't already exist.

     Priority: Normal , because we aren't using the Priority parameter.

  PowerShell

<!-- p.1271 -->

  New-MailboxImportRequest -FilePath \\SERVER01\PSTFiles\Archives\Vbarrios.pst -
  Mailbox "Valeria Barrios"

This example creates a new mailbox import request with these settings:

     Mailbox import request name: The custom name Kathleen Reiter Import is specified by
     the Name parameter. Specifying a custom name allows more than 10 mailbox import
     requests for the mailbox. The unique identity value of the mailbox import request is
     <MailboxIdentity>\<MailboxImportRequestName> (for example, kreiter\Kathleen Reiter

     Import ).

     Source .pst file: \\SERVER01\PSTFiles\Archives\Recovered.pst

     Target mailbox: The archive mailbox for Kathleen Reiter (Kathleen's primary mailbox alias
     is kreiter).

     Content and folders: Only content in the Inbox folder of the .pst file is imported
     (regardless of the localized name of the folder), and it's imported to the Recovered Files
     folder in the target mailbox.

     Priority: High

  PowerShell

  New-MailboxImportRequest -Name "Kathleen Reiter Import" -FilePath
  \\SERVER01\PSTFiles\Recovered.pst -Mailbox kreiter -IsArchive -IncludeFolders
  "#Inbox#" -TargetRootFolder "Recovered Files" -Priority High

For detailed syntax and parameter information, see New-MailboxImportRequest.

How do you know this worked?
To verify that you've successfully created a mailbox import request, do any of these steps:

     In the EAC, click the notification viewer   to view the status of the request.

     If you created the mailbox import request in the EAC, and selected the option to send
     notification email messages, check the notification messages. The sender is Microsoft
     Exchange. The first message has the subject Your Import PST request has been received .
     If the import request completed successfully, you'll receive another message with the
     subject Import PST has finished .

<!-- p.1272 -->

     Replace <MailboxIdentity> with the name, email address, or alias of the target mailbox,
     and run this command in the Exchange Management Shell to verify the basic property
     values:

        PowerShell

        Get-MailboxImportRequest -Mailbox "<MailboxIdentity>" | Format-List
        Name,FilePath,Mailbox,Status

     Replace <MailboxIdentity> and <MailboxImportRequestName> with the appropriate
     values, and run this command in the Exchange Management Shell to verify the details:

        PowerShell

        Get-MailboxImportRequestStatistics -Identity "<MailboxIdentity>\
        <MailboxImportRequestName>"

Use the Exchange Management Shell to view
mailbox import requests
By default, the Get-MailboxImportRequest cmdlet returns the name, target mailbox, and
status of mailbox import requests. If you pipeline the command to the Format-List cmdlet,
you'll only get a limited number of additional useful details:

     FilePath: The source .pst file.

     RequestGUID: The unique GUID value of the mailbox import request.

     RequestQueue: The mailbox database that the import request is being run on.

     BatchName: The optional batch name for the mailbox import request.

     Identity: The unique identity value of the mailbox import request (<MailboxIdentity>\
     <MailboxImportRequestName>).

By default, the Get-MailboxImportRequestStatistics cmdlet returns the name, status, alias of
the target mailbox, and the completion percentage of mailbox import requests. If you pipeline
the command to the Format-List cmdlet, you'll see detailed information about the mailbox
import request.

This example returns the summary list of all mailbox import requests.

  PowerShell

<!-- p.1273 -->

  Get-MailboxImportRequest

This example returns additional information for mailbox import requests to the mailbox Akia
Al-Zuhairi.

  PowerShell

  Get-MailboxImportRequest -Mailbox "Akia Al-Zuhairi" | Format-List

This example returns the summary list of in-progress mailbox import requests for mailboxes
that reside on the mailbox database named DB01.

  PowerShell

  Get-MailboxImportRequest -Status InProgress -Database DB01

This example returns the summary list of completed mailbox import requests in the batch
named Import DB01 PSTs.

  PowerShell

  Get-MailboxImportRequest -Status Completed -BatchName "Import DB01 PSTs"

For detailed syntax and parameter information, see Get-MailboxImportRequest.

To view detailed information about a mailbox import request, use this syntax:

  PowerShell

  Get-MailboxImportRequestStatistics -Identity <MailboxImportRequestIdentity> [-
  IncludeReport] | Format-List

Where <MailboxImportRequestIdentity> is the identity value of the mailbox import request
(<MailboxIdentity>\ <MailboxImportRequestName> or <RequestGUID>).

This example returns detailed information for the mailbox import request named
MailboxImport for Akia Al-Zuhairi's mailbox, including the log of actions in the Report
property.

  PowerShell

  Get-MailboxImportRequestStatistics -Identity "aal-zuhairi\MailboxImport" -
  IncludeReport | Format-List

<!-- p.1274 -->

For detailed syntax and parameter information, see Get-MailboxImportRequestStatistics.

Use the Exchange Management Shell to modify
mailbox import requests
You can modify mailbox import requests that haven't completed. You can't modify the
fundamental settings of an existing request (for example, the source .pst file, target mailbox,
the source content in the .pst file, or the destination in the target mailbox).

To modify a mailbox import request, use this syntax:

  PowerShell

  Set-MailboxImportRequest -Identity <MailboxIdentity>\<MailboxImportRequestName> [-
  BadItemLimit <value>] [-LargeItemLimit <value>] [-AcceptLargeDataLoss]

This example modifies the failed mailbox import request for the mailbox of Valeria Barrios to
accept up to five corrupted mailbox items.

  PowerShell

  Set-MailboxImportRequest -Identity "Valeria Barrios\MailboxImport" -BadItemLimit 5

For detailed syntax and parameter information, see Set-MailboxImportRequest.

Note: After you modify a suspended or failed mailbox import request, you need to resume it
by using the Resume-MailboxImportRequest cmdlet.

How do you know this worked?
To verify that you've successfully modified a mailbox import request, replace <MailboxIdentity>
and <MailboxImportRequestName> with the appropriate values, and run this command in the
Exchange Management Shell to verify the details:

  PowerShell

  Get-MailboxImportRequestStatistics -Identity "<MailboxIdentity>\
  <MailboxImportRequestName>" | Format-List

Use the Exchange Management Shell to suspend
mailbox import requests

<!-- p.1275 -->

You can suspend mailbox import requests that are in progress. You can't suspend completed or
failed mailbox import requests.

To suspend a mailbox import request, use this syntax:

  PowerShell

  Suspend-MailboxImportRequest -Identity <MailboxIdentity>\
  <MailboxImportRequestName> [-SuspendComment "<Descriptive Comment>"]

This example suspends the mailbox import request to Kathleen Reiter's mailbox that's named
Kathleen Reiter Import.

  PowerShell

  Suspend-MailboxImportRequest -Identity "kreiter@contoso.com\Kathleen Reiter
  Import"

This example suspends all in-progress mailbox import requests with the comment "OK to
resume after 10 P.M. on Monday 6/19"

  PowerShell

  Get-MailboxImportRequest -Status InProgress | Suspend-MailboxImportRequest -
  SuspendComment "OK to resume after 10 P.M. on Monday 6/19"

For detailed syntax and parameter information, see Suspend-MailboxImportRequest.

Notes:

     You can also use the New-MailboxImportRequest cmdlet with the Suspend switch to
     create a suspended mailbox import request.

     You use the Resume-MailboxImportRequest parameter to resume suspended mailbox
     import requests.

How do you know this worked?
To verify that you've successfully suspended a mailbox import request, do any of these steps:

     Replace <MailboxIdentity> with the name, email address, or alias of the target mailbox,
     run this command in the Exchange Management Shell, and verify that the Status property
     has the value Suspended :

<!-- p.1276 -->

        PowerShell

        Get-MailboxImportRequest -Mailbox "<MailboxIdentity>" | Format-List
        Name,FilePath,Mailbox,Status

     Run this command in the Exchange Management Shell, and verify that the suspended
     mailbox import request is listed:

        PowerShell

        Get-MailboxImportRequest -Status Suspended

Use the Exchange Management Shell to resume
mailbox import requests
You can resume suspended or failed mailbox import requests.

To resume a mailbox import request, use this syntax:

  PowerShell

  Resume-MailboxImportRequest -Identity <MailboxIdentity>\<MailboxImportRequestName>

This example resumes the failed mailbox import request for Valeria Barrios' mailbox.

  PowerShell

  Resume-MailboxImportRequest -Identity vbarrios\MailboxImport

This example resumes all suspended mailbox import requests.

  PowerShell

  Get-MailboxImportRequest -Status Suspended | Resume-MailboxImportRequest

For detailed syntax and parameter information, see Resume-MailboxImportRequest.

How do you know this worked?
To verify that you've successfully resumed a mailbox import request, replace <MailboxIdentity>
with the name, email address, or alias of the target mailbox, run this command in the Exchange
Management Shell, and verify that the Status property doesn't have the value Suspended :

<!-- p.1277 -->

  PowerShell

  Get-MailboxImportRequest -Mailbox <MailboxIdentity> | Format-List
  Name,FilePath,Mailbox,Status

Use the Exchange Management Shell to remove
mailbox import requests
You can remove fully or partially completed mailbox import requests.

     If you remove a partially completed mailbox import request, the request is removed from
     the MRS job queue. Any content that's already been imported from the .pst file isn't
     removed from the target mailbox.

     By default, completed mailbox import request are removed after 30 days (you can
     override this value with the CompletedRequestAgeLimit parameter), and failed requests
     aren't automatically removed. But, if you use the RequestExpiryInterval parameter when
     you create or modify a mailbox import request, these results are available:

        RequestExpiryInterval with a timespan value: Completed and failed requests are
        automatically removed after the specified timespan.

        RequestExpiryInterval with the value unlimited: Completed and failed requests aren't
        automatically removed.

This example removes the mailbox import request named MailboxImport for Akia Al-Zuhairi's
mailbox.

  PowerShell

  Remove-MailboxImportRequest -Identity "aal-zuhairi\MailboxImport"

This example removes all completed mailbox import requests.

  PowerShell

  Get-MailboxImportRequest -Status Completed | Remove-MailboxImportRequest

For detailed syntax and parameter information, see Remove-MailboxImportRequest.

How do you know this worked?

<!-- p.1278 -->

To verify that you've successfully removed a mailbox import request, replace <MailboxIdentity>
with the name, email address, or alias of the target mailbox, run this command in the Exchange
Management Shell, and verify that the mailbox import request isn't listed:

  PowerShell

  Get-MailboxImportRequest -Mailbox <MailboxIdentity> | Format-List
  Name,FilePath,Mailbox,Status

<!-- p.1279 -->

Procedures for mailbox exports to .pst files
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Mailbox export requests use the Microsoft Exchange Mailbox Replication service (MRS) to
export the contents of mailboxes to .pst files. For more information, see Mailbox imports and
exports in Exchange Server.

This topic shows you how to:

      Create mailbox export requests.

      View mailbox export requests.

      Modify mailbox export requests that haven't completed.

      Suspend mailbox export requests that haven't completed or failed.

      Resume suspended or failed mailbox export requests

      Remove mailbox export requests.

What do you need to know before you begin?

  ） Important

  The procedures in this topic require the Mailbox Import Export role, which isn't assigned
  to any role groups by default. To assign the role to a role group that you belong to, see
  Add a role to a role group. Note that changes in permission require you to log off and
  log on for the changes to take effect.

      Estimated time to complete each procedure: 5 minutes

      You need to export mailboxes to .pst files on a UNC network share (\ <Server>\ <Share>\
      or \ <LocalServerName>\c$). The Exchange Trusted Subsystem security group requires
      the Read/Write permission to the network share. If the share doesn't have this permission,
      you'll get errors when you try to export mailboxes to .pst files.

      You can create mailbox export requests in the Exchange admin center (EAC) or in the
      Exchange Management Shell. All other procedures can only be done in the Exchange
      Management Shell. For more information about accessing and using the EAC, see

<!-- p.1280 -->

   Exchange admin center in Exchange Server. To learn how to open the Exchange
   Management Shell in your on-premises Exchange organization, see Open the Exchange
   Management Shell.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Create mailbox export requests

Use the EAC to create a mailbox export request
 1. In the EAC, go to Recipients > Mailboxes > click More options      , and select Export to a
   PST file.

 2. The Export to a .pst file wizard opens. On the first page, select the source mailbox, and
   then select one of these options:

         Export only the contents of this mailbox
