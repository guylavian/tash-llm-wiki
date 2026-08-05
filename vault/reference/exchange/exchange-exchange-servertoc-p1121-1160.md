---
title: "Exchange Server — pages 1121-1160"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1121-1160
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1121-1160
family: exchange
documentKind: "doc"
abstract: "2. In the list of groups, click the distribution group that you want to view or change, and then click Edit . 3. On the group properties page, click one of the following sections to view or change properties. General Ownership Membership Membership approval Delivery management M"
---

# Exchange Server — pages 1121-1160

<!-- p.1121 -->

   2. In the list of groups, click the distribution group that you want to view or change, and
     then click Edit   .

   3. On the group properties page, click one of the following sections to view or change
     properties.

           General

           Ownership

           Membership

           Membership approval

           Delivery management

           Message approval

           Email options

           MailTip

           Group delegation

General
Use this section to view or change basic information about the group.

     * Display name: This name appears in the address book, on the To: line when email is sent
     to this group, and in the Groups list. The display name is required and should be user-
     friendly so people recognize what it is. It also has to be unique in your domain.

     If you've implemented a group naming policy, the display name has to conform to the
     naming format defined by the policy.

     * Alias: This is the portion of the email address that appears to the left of the at (@)
     symbol. If you change the alias, the primary SMTP address for the group will also be
     changed, and contain the new alias. Also, the email address with the previous alias will be
     kept as a proxy address for the group.

     Description: Use this box to describe the group so people know what the purpose of the
     group is. This description appears in the address book and in the Details pane in the EAC.

     Hide this group from address lists: Select this check box if you don't want users to see
     this group in the address book. To send email to this group, a sender has to type the
     group's alias or email address on the To: or Cc: lines.

<!-- p.1122 -->

         Tip

        Consider hiding security groups because they're typically used to assign permissions
        to group members and not to send email.

     Organizational unit: This read-only box displays the organizational unit (OU) that
     contains the distribution group. You have to use Active Directory Users and Computers to
     move the group to a different OU.

Ownership
Use this section to assign group owners. The group owner can add members to the group,
approve or reject requests to join or leave the group, and approve or reject messages sent to
the group. By default, the person who creates a group is the owner. All groups must have at
least one owner.

You can add owners by clicking Add      . You can remove an owner by selecting the owner and
then clicking Remove       .

Membership
Use this section to add or remove members. Group owners don't have to be members of the
group. Under Members, you can add members by clicking Add           . You can remove a member
by selecting a user in the member list and then clicking Remove     .

Membership approval
Use this section to specify whether approval is required for users to join or leave the group.

     Choose whether owner approval is required to join the group: Select one of the
     following settings:

        Open: Anyone can join this group without being approved by the group owners

        Closed: Members can be added only by the group owners. All requests to join will
        be rejected automatically

        Owner Approval: All requests are approved or rejected by the group owners: If you
        select this option, the group owner or owners receive an email requesting approval to
        join the group.

     Choose whether the group is open to leave: Select one of the following settings:

<!-- p.1123 -->

           Open: Anyone can leave this group without being approved by the group owners

           Closed: Members can be removed only by the group owners. All requests to leave
           will be rejected automatically

Delivery management
Use this section to manage who can send email to this group.

     Only senders inside my organization: Select this option to allow only senders in your
     organization to send messages to the group. This means that if someone outside of your
     organization sends an email message to this group, it will be rejected. This is the default
     setting.

     Senders inside and outside of my organization: Select this option to allow anyone to
     send messages to the group.

     You can further limit who can send messages to the group by allowing only specific
     senders to send messages to this group. Click Add       and then select one or more
     recipients. If you add senders to this list, they are the only ones who can send mail to the
     group. Mail sent by anyone not in the list will be rejected.

     To remove a person or a group from the list, select them in the list and then click Remove
       .

  ） Important

  If you've configured the group to allow only senders inside your organization to send
  messages to the group, email sent from a mail contact will be rejected, even if they are
  added to this list.

Message approval

Use this section to set options for moderating the group. Moderators approve or reject
messages sent to the group before they reach the group members.

     Messages sent to this group have to be approved by a moderator: This check box isn't
     selected by default. If you select this check box, incoming messages are reviewed by the
     group moderators before delivery. Group moderators can approve or reject incoming
     messages.

<!-- p.1124 -->

     Group moderators: To add group moderators, click Add          . To remove a moderator,
     select the moderator, and then click Remove       . If you've selected "Messages sent to this
     group have to be approved by a moderator" and you don't select a moderator, messages
     to the group are sent to the group owners for approval.

     Senders who don't require message approval: To add people or groups that can bypass
     moderation for this group, click Add     . To remove a person or a group, select the item,
     and then click Remove      .

     Select moderation notifications: Use this section to set how users are notified about
     message approval.

        Notify all senders when their messages aren't approved: This is the default setting.
        Notify all senders, inside and outside your organization, when their message isn't
        approved.

        Notify senders in your organization when their messages aren't approved: When you
        select this option, only people or groups in your organization are notified when a
        message that they sent to the group isn't approved by a moderator.

        Don't notify anyone when a message isn't approved: When you select this option,
        notifications aren't sent to message senders whose messages aren't approved by the
        group moderators.

Email options
Use this section to view or change the email addresses associated with the group. This includes
the group's primary SMTP addresses and any associated proxy addresses. The primary SMTP
address (also known as the reply address) is displayed in bold text in the address list, with the
uppercase SMTP value in the Type column.

     Add: Click Add      to add a new email address for this mailbox. Select one of following
     address types:

        SMTP: This is the default address type. Click this button and then type the new SMTP
        address in the * Email address box.

        Custom address type: Click this button and type one of the supported non-SMTP
        email address types in the * Email address box.

           ７ Note

           With the exception of X.400 addresses, Exchange doesn't validate custom
           addresses for correct formatting. You must make sure that the custom address

<!-- p.1125 -->

           you specify complies with the format requirements for that address type.

     Edit: To change an email address associated with the group, select it in the list, and then
     click Edit   .

     Remove: To delete an email address associated with the group, select it in the list, and
     then click Remove     .

     Automatically update email addresses based on the email address policy applied to this
     recipient: Select this check box to have the recipient's email addresses automatically
     updated based on changes made to email address policies in your organization. This box
     is selected by default.

MailTip

Use this section to add a MailTip to alert users of potential issues if they send a message to this
group. A MailTip is text that's displayed in the InfoBar when this group is added to the To, Cc,
or Bcc lines of a new email message. For example, you could add a MailTip to large groups to
warn potential senders that their message will be sent to lots of people.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Group delegation
Use this section to assign permissions to a user (called a delegate) to allow them to send
messages as the group or send messages on behalf of the group. You can assign the following
permissions:

     Send As: This permission allows the delegate to send messages as the group. After this
     permission is assigned, the delegate has the option to add the group to the From line to
     indicate that the message was sent by the group.

     Send on Behalf Of: This permission also allows a delegate to send messages on behalf of
     the group. After this permission is assigned, the delegate has the option to add the group
     in the From line. The message will appear to be sent by the group and will say that it was
     sent by the delegate on behalf of the group.

<!-- p.1126 -->

To assign permissions to delegates, click Add under the appropriate permission to display the
Select Recipient page, which displays a list of all recipients in your Exchange organization that
can be assigned the permission. Select the recipients you want, add them to the list, and then
click OK. You can also search for a specific recipient by typing the recipient's name in the
search box and then clicking Search.

Use the Exchange Management Shell to change distribution
group properties
Use the Get-DistributionGroup and Set-DistributionGroup cmdlets to view and change
properties for distribution groups. Advantages of using the Exchange Management Shell are
the ability to change the properties that aren't available in the EAC and to change properties
for multiple groups. For information about which parameters correspond to distribution group
properties, see the following topics:

     Get-DistributionGroup

     Set-DistributionGroup

Here are some examples of using the Exchange Management Shell to change distribution
group properties.

This example changes the primary SMTP address (also called the reply address) for the Seattle
Employees distribution group from employees@contoso.com to sea.employees@contoso.com.
Also, the previous reply address will be kept as a proxy address.

  PowerShell

  Set-DistributionGroup "Seattle Employees" -EmailAddresses
  SMTP:sea.employees@contoso.com,smtp:employees@contoso.com

This example limits the maximum message size that can be sent to all distribution groups in
the organization to 10 megabytes (MB).

  PowerShell

  Get-DistributionGroup -ResultSize unlimited -Filter "RecipientTypeDetails -eq
  'MailUniversalDistributionGroup'" | Set-DistributionGroup -MaxReceiveSize 10MB

This example enables moderation for the distribution group Customer Support and sets the
moderator to Amy. In addition, this moderated distribution group will notify senders who send
mail from within the organization if their messages aren't approved.

<!-- p.1127 -->

  PowerShell

  Set-DistributionGroup -Identity "Customer Support" -ModeratedBy "Amy" -
  ModerationEnabled $true -SendModerationNotifications 'Internal'

This example changes the user-created distribution group Dog Lovers to require the group
manager to approve users' requests to join the group. In addition, by using the
BypassSecurityGroupManagerCheck parameter, the group manager will not be notified that a
change was made to the distribution group's settings.

  PowerShell

  Set-DistributionGroup -Identity "Dog Lovers" -MemberJoinRestriction
  'ApprovalRequired' -BypassSecurityGroupManagerCheck

How do you know this worked?
To verify that you've successfully changed properties for a distribution group, do the following:

     In the EAC, select the group and then click Edit    to view the property or feature that
     you changed. Depending on the property that you changed, it might be displayed in the
     Details pane for the selected group.

     In the Exchange Management Shell, use the Get-DistributionGroup cmdlet to verify the
     changes. One advantage of using the Exchange Management Shell is that you can view
     multiple properties for multiple groups. In the example above where the recipient limit
     was changed, run the following command to verify the new value.

        PowerShell

        Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
        'UserMailbox'" | Format-List Name,RecipientLimits

     For the example above where the message limits were changed, run this command.

        PowerShell

        Get-Mailbox -OrganizationalUnit "Marketing" | Format-List
        Name,IssueWarningQuota,ProhibitSendQuota,ProhibitSendReceiveQuota,UseDatabase
        QuotaDefaults

<!-- p.1128 -->

Manage mail-enabled security groups in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019       Subscription Edition

You can use mail-enabled security groups to distribute messages as well as grant access
permissions to resources in Exchange and Active Directory. You can create, modify, and remove
mail-enabled security groups in the Exchange admin center (EAC) or in the Exchange
Management Shell. For more information about mail-enabled security groups, see Recipients.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Distribution groups" entry in the
      Recipients Permissions topic.

      For more information about accessing and using the EAC, see Exchange admin center in
      Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      If you add users to or remove users from a mail-enabled security group, the users need to
      log out and log in for the permission changes to take effect.

      For mail-enabled security groups, users can't add or remove themselves from the group,
      nor can they send requests to the group owners to join or leave the group. A group
      owner needs to manually add and remove group members from a mail-enabled security
      group.

      If a mail-enabled security group contains members that aren't mail-enabled, a non-
      delivery report (also known as an NDR or bounce message) is returned for those non-
      mail-enabled members when you send a message to the group. To prevent NDRs, you
      can expand the group members in the To field of the message before you send the
      message (only the mail-enabled members of the group will appear).

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

<!-- p.1129 -->

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server .

Create mail-enabled security groups
   When you create groups in the EAC, the value of the Display name property is used for
   the value of the unseen Name property (the unique identifier for the group object in the
   forest). Because the value of Name has a maximum length of 64 characters, the value of
   Display name also has a maximum length of 64 characters when you create groups in the
   EAC.

   When you create groups in the Exchange Management Shell, the Name parameter is
   required, the value must be unique, and the value has a maximum length of 64
   characters. The DisplayName parameter is optional (the value of Name is used if you
   don't use it), the value isn't required to be unique, and the value has a maximum length
   of 256 characters.

   When you create groups in the EAC, the groups are automatically configured to only
   accept messages from authenticated (internal) senders. When you create groups in the
   Exchange Management Shell, you can use the RequireSenderAuthenticationEnabled
   parameter with the value $false so the group can accept messages from authenticated
   an unauthenticated (internal and external) senders. After you create the group, you can
   use the EAC or the Exchange Management Shell to change this setting.

Use the EAC to create a mail-enabled security group
 1. In the EAC, go to Recipients > Groups.

 2. Click New    and then select Security group in the drop down list that appears.

<!-- p.1130 -->

3. On the New security group page that opens, configure these settings (values marked
  with an * are required):

       * Display name: This value should help users immediately recognize what the group
       is used for. This name appears in the global address list, on the To: line when email
       is sent to this group, and in the Groups list in the EAC. The maximum length in the
       EAC is 64 characters, and the value must be unique.

          ７ Note

          If a group naming policy is applied, you need to follow the naming constraints
          that are enforced for your organization. For more information, see Create a
          Distribution Group Naming Policy. If you want to override your organization's
          group naming policy, see Override a Distribution Group Naming Policy.

       * Alias: This value is used to generate the primary email address (<alias>@
       <domain>). This value can contain letters, numbers and the characters !, #, $, %, &, ',
       *, +, -, /, =, ?, ^, _, `, {, |, } and ~. Periods (.) are allowed, but each period must be
       surrounded by other valid characters (for example, help.desk). Unicode characters
       from U+00A1 to U+00FF are also allowed, but are mapped to best-fit US-ASCII text
       characters in the primary email address (for example, U+00F6 (ö) is changed to oe).
       The alias can't exceed 64 characters and must be unique in the forest. When a user
       types the alias on the To: line of an email message, it resolves to the group's display
       name.

       Notes: Use this box to describe the purpose of the group. This description appears
       in the global address list and in the details pane in the EAC.

<!-- p.1131 -->

Organizational unit: The default location in Active Directory depends on the
recipient scope that's configured:

  If the recipient scope is the Active Directory forest, the default location is the
  Users container in the domain where the computer that's running the EAC is
  located.

  If the recipient scope is a specific domain, the default location is the Users
  container in that domain.

  If the recipient scope is a specific organizational unit (OU), the default location is
  that OU.

To select a different OU, click Browse. The Select an organizational unit dialog box
that opens shows all of the available OUs in the forest that are within the specified
recipient scope. Select the desired OU, and then click OK.

* Owners: By default, the person who creates the group is the owner. All groups
must have at least one owner. Group owners can:

  Modify the properties of the group

  Add or remove group members

  Delete the group

  Approve messages sent to the group (if moderation is enabled)

To add owners, click Add    . In the Select Owners dialog that appears, select one or
more owners, click Add, and then click OK.

To remove owners, select the owner in the list, and then click Remove       .

Members

To add members to the group, click Add       . In the Select Members dialog that
appears, select one or more members, click Add, and then click OK.

To remove members, select the member in the list, and then click Remove            .

Add group owners as members: When this check box is selected, you don't need to
manually include group owners in the list of members. If you don't want the group
owners to be members of the group, clear this check box.

Owner approval is required: For mail-enabled security groups, user requests to join
the group aren't sent to the group owners, regardless of the state of this check box

<!-- p.1132 -->

           (selected or not selected). A group owner needs to manually add and remove group
           members from a mail-enabled security group.

     When you've finished, click Save.

Use the Exchange Management Shell to create a mail-enabled
security group
To create a mail-enabled security group, use this syntax:

  PowerShell

  New-DistributionGroup -Type Security -Name <UniqueName> [-IgnoreNamingPolicy] [-
  Alias <Alias>] [-DisplayName "<DisplayName>"] [-Notes "<Description>"] [-
  OrganizationalUnit <OU>] [-ManagedBy "<owner1>","<owner2>"...] [-Members "
  <member1>","<member2>"...] [-CopyOwnerToMember] [-MemberJoinRestriction <Closed |
  ApprovalRequired>] [-RequireSenderAuthenticationEnabled <$true | $false>]

This example creates a security group with these settings:

     Name: File Server Managers. This value is also used for the display name because we
     aren't using the DisplayName parameter. If a group naming policy is applied, you can use
     the IgnoreNamingPolicy switch to override the policy.

     Alias: fsadmin. If we didn't use the Alias parameter, the value of the Name parameter
     would be used, with spaces removed (FileServerManagers in this example).

     Description: None, because we aren't using the Notes parameter.

     Organizational Unit: The default location that's specified by the recipient scope, because
     we aren't using the OrganizationalUnit parameter.

     Owners: The user account that's creating the group is the only owner, because we aren't
     using the ManagedBy parameter.

     Members: Bishamon Tamura and Valeria Barrios. Because we're using the
     CopyOwnerToMember switch, the group owner is also a member.

     User requests to join the group: For mail-enabled security groups, user requests to join
     the group aren't sent to the group owners, regardless of the MemberJoinRestriction
     parameter value ( ApprovalRequired or Closed ). A group owner needs to manually add
     and remove group members from a mail-enabled security group.

     Accept messages from external senders: No, because we're aren't using the
     RequireSenderAuthenticationEnabled parameter, and the default value is $true .

<!-- p.1133 -->

  PowerShell

  New-DistributionGroup -Type Security -Name "File Server Managers" -Alias fsadmin -
  Members "Bishamon Tamura","Valeria Barrios" -CopyOwnerToMember

For detailed syntax and parameter information, see New-DistributionGroup.

How do you know this worked?
To verify that you've successfully created a mail-enabled security group, do any of these steps:

     In the EAC, go to Recipients > Groups. Verify that the group is listed, and the Group Type
     value is Security group.

     In the Exchange Management Shell, run this command and verify that the group is listed:

        PowerShell

        Get-DistributionGroup -Filter "RecipientType -eq
        'MailUniversalSecurityGroup'"

     In the Exchange Management Shell, replace <GroupIdentity> with the identity of the
     group (for example, name, alias, or email address), and run this command to verify the
     property values:

        PowerShell

        Get-DistributionGroup -Identity <GroupIdentity> | Format-List

View or modify mail-enabled security groups
     When you modify groups in the EAC, the maximum length for the Display name property
     is now 256 characters, and the value doesn't need to be unique. This value no longer
     affects the value of the unseen Name property (the unique identifier for the group object
     in the forest). You can't use the EAC to modify the Name value of an existing group.

     When you modify groups in the Exchange Management Shell, the maximum length for
     the Name parameter value is still 64 characters, and the value must be unique. The
     maximum length for the DisplayName parameter value is still 256 characters, and the
     value doesn't need to be unique.

Use the EAC to view or modify a mail-enabled security group

<!-- p.1134 -->

1. In the EAC, go to Recipients > Groups.

2. In the list of groups, find the mail-enabled security group that you want to view or
  modify. You can:

       Scroll through the list of groups.

       Click Search     and enter part of the group's name, email address, or alias.

       Click More options        > Advanced search to find the group.

       Click the Group Type column header to sort the groups by Security group.

       Once you've found the mail-enabled security group that you want to modify, select
       it, and then click Edit    .

3. On the Edit Security Group page that opens, click one of the tabs to view or change the
  settings of the group:

       General

       Ownership

       Membership

       Membership approval

       Delivery management

       Message approval

       Email options

       MailTip

       Group delegation

<!-- p.1135 -->

     When you're finished, click Save or Cancel.

General
Use this tab to view or change basic information about the group.

     Display name: This value should help users immediately recognize what the group is used
     for. This name appears in the global address list, on the To: line when email is sent to this
     group, and in the Groups list in the EAC. The maximum length is 256 characters, and the
     value doesn't need to be unique.

     Alias: This value is used to generate the primary email address (<alias>@ <domain>).
     This value can contain letters, numbers and the characters !, #, $, %, &, ', *, +, -, /, =, ?, ^,
     _, `, {, |, } and ~. Periods (.) are allowed, but each period must be surrounded by other valid
     characters (for example, help.desk). Unicode characters from U+00A1 to U+00FF are also
     allowed, but are mapped to best-fit US-ASCII text characters in the primary email address
     (for example, U+00F6 (ö) is changed to oe). The alias can't exceed 64 characters and must
     be unique in the forest. When a user types the alias on the To: line of an email message, it
     resolves to the group's display name.

     When you change the alias value, the previous primary email address is kept as a proxy
     address for the group.

     Notes: Use this box to describe the purpose of the group. This description appears in the
     global address list and in the details pane in the EAC.

     Hide this group from address lists: Select this check box if you don't want users to see
     the group in the global address list. If this check box is selected, a sender has to know
     and type the group's alias or email address to send messages to the group.

     Organizational unit: This read-only box displays the location of the group object in Active
     Directory. You need to use Active Directory Users and Computers to move the group to a
     different OU.

Ownership
Use this section to assign group owners. All groups must have at least one owner. Group
owners can:

     Modify the properties of the group

     Add or remove group members

     Delete the group

<!-- p.1136 -->

     Approve member depart or join requests (if available)

     Approve messages sent to the group (if moderation is enabled)

To add owners, click Add    . In the Select Owners dialog that appears, select one or more
owners, click Add, and then click OK.

To remove owners, select the owner in the list, and then click Remove     .

Membership
Use this tab to add or remove group members. Group owners aren't required to be members
of the group.

To add members to the group, click Add       . In the Select Members dialog that opens, select
one or more members, click Add, and then click OK.

To remove members, select the member in the list, and then click Remove       .

Membership approval

For mail-enabled security groups, user requests to join the group aren't sent to the group
owners, regardless of the state of the Owner approval is required check box (selected or not
selected). A group owner needs to manually add or remove group members from a mail-
enabled security group.

Delivery management

Use this tab to control who's allowed to send messages to the group.

     Only senders inside my organization: The group only accepts messages from
     authenticated (internal) senders. This is the default setting.

     Senders inside and outside of my organization: The group accepts messages from
     authenticated and unauthenticated (internal and external) senders.

     Restrict the internal senders who can send messages to the group by clicking Add        . In
     the Select Allowed Senders dialog that appears, select one or more senders, click Add,
     and then click OK. Only the specified senders can send messages to the group.

     To remove internal senders that are allowed to send messages to the group, select the
     sender in the list, and then click Remove    .

<!-- p.1137 -->

  ） Important

  Mail contacts are always considered unauthenticated (external) senders. If you select Only
  senders inside my organization and add the mail contact to the list of approved internal
  senders, messages sent to the group by the mail contact will be rejected.

Message approval

Use this tab to configure the moderation settings for messages that are sent to the group.

     Messages sent to this group have to be approved by a moderator: This check box isn't
     selected by default. If you select this check box, messages that are sent to the group must
     be approved by the specified moderators before they're delivered to the group members.
     When you select this option, you can configure these additional settings:

        Group moderators: For mail-enabled security groups, the group owners aren't
        automatically used as moderators. You need to specify at least one moderator here
        when moderation is enabled.

        To add moderators, click Add    . In the Select Group Moderators dialog that appears,
        select one or more moderators (which can include any of the group owners), click Add,
        and then click OK.

        To remove moderators, select the moderator in the list, and then click Remove      .

        Senders who don't require message approval: To configure senders who can bypass
        moderation for the group (send messages directly to the group members), click Add
          . In the Select Senders dialog that appears, select one or more senders, click Add,
        and then click OK.

        To remove senders, select the sender in the list, and then click Remove   .

        You don't need to include moderators in the list of senders who bypass moderation.
        Messages that are sent to the group by a moderator aren't moderated.

        Select moderation notifications: This setting configures how message senders are
        notified when their messages aren't approved by a moderator:

        Notify all senders when their messages aren't approved: Authenticated and
        unauthenticated (internal and external) senders are notified when their messages
        aren't approved by a group moderator. This is the default value.

<!-- p.1138 -->

        Notify senders in your organization when their messages aren't approved: Only
        authenticated (internal) senders are notified when their messages aren't approved by a
        group moderator.

        Don't notify anyone when a message isn't approved: Senders aren't notified when
        their messages aren't approved by a group moderator.

Email options
Use this tab to view or change the email addresses that are configured for the group.

     Email address: By default, you use this setting to add additional email addresses for the
     group (also known as proxy addresses).

     By default, the primary email address (also known as the Reply To or reply address) is
     configured by the email address policy that's applied to the group. For more information
     about email address policies, see Email address policies in Exchange Server. The primary
     email address that's shown here is bold, and has the uppercase SMTP value in the Type
     column.

     To manually specify the group's primary email address here, you need to clear the check
     box Automatically update email addresses based on the email address policy applied to
     this recipient. Note that clearing this check box prevents automatic updates to the email
     addresses of the group by email address policies.

        To add a new email address for the group, click Add    . In the New email address
        page that opens, select one of these options:

        Email address type: Select SMTP. In the Email address box, type the email address (for
        example, helpdesk@contoso.com). The domain must be an accepted domain that's
        configured for your organization. For more information, see Accepted domains in
        Exchange Server.

        On the previous page, if you left Automatically update email addresses based on the
        email address policy applied to this recipient check box selected, the email address is
        added to the group as a proxy address (there's no Make this the reply address check
        box on this page).

        On the previous page, if you cleared the Automatically update email addresses based
        on the email address policy applied to this recipient check box, you can select Make
        this the reply address. This setting adds the new email address as the primary email
        address, and the previous primary email address is kept as a proxy address. If you

<!-- p.1139 -->

        don't select Make this the reply address, the email address is added as a proxy
        address, and the primary email address is unaffected.

        Email address type: Select Enter a custom address type. Type the custom email
        address type (for example, X400). In the Email address box, type the custom email
        address.

     Note: With the exception of X.400 addresses, Exchange doesn't validate custom email
     addresses for correct formatting. You need to make sure that the custom email address
     complies with the format requirements for that address type.

     When you're finished, click OK.

        To modify an existing email address for the group, select it in the list, and then click
        Edit   . Note that you can't change the email address type, just the email address.

        To remove an existing email address from the group, select it in the list, and then click
        Remove      . Note that you can't remove the primary email address.

MailTip
Use this tab to add a custom MailTip for the group. MailTips alert users to potential issues
before they send a message to the group. For more information about MailTips, see Configure
Custom MailTips for Recipients.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Group delegation
Use this tab to assign permissions to the group for a user (called a delegate).

     Send As: The specified users can send messages that appear to be sent by the group. The
     actual sender isn't revealed, and replies to these messages are delivered to the group.

     Send on Behalf: The specified users can send on behalf of the group. Although messages
     send on behalf of the group clearly show the sender in the From line (<Sender> on behalf
     of <Group>), replies to these messages are delivered to the group, not the sender.

To add delegates, click Add     for the appropriate permission. In the resulting dialog that
appears, select one or more delegates, click Add, and then click OK.

<!-- p.1140 -->

After you assign one of these permissions, the delegate can select the group for the From line
in Outlook or Outlook on the web (formerly known as Outlook Web App).

To remove delegates, select the delegate in the appropriate list, and then click Remove       .

Use the Exchange Management Shell to modify a mail-
enabled security group
You use the Set-DistributionGroup cmdlet to modify mail-enabled security groups. Here are
some interesting settings that you can configure using the Set-DistributionGroup cmdlet that
aren't available in the EAC or on the New-DistributionGroup cmdlet:

     Configure values for the CustomAttribute1 through CustomAttribute15 properties (the
     CustomAttribute1 through CustomAttribute15 parameters).

     Configure MailTips in different languages (the MailTipTranslations parameter).

     Configure the maximum message size that can be sent to or sent from the group (the
     MaxReceiveSize and MaxSendSize parameters).

     Instead of specifying the internal recipients who are allowed to send messages to the
     group, you can specify the internal recipients who aren't allowed to send messages to the
     group (the RejectMessagesFromSendersOrMembers parameter).

For detailed syntax and parameter information, see Set-DistributionGroup.

This example configures the value DoNotMigrate for the CustomAttribute5 property of the
group named Experimental Project.

  PowerShell

  Set-DistributionGroup -Identity "Experimental Project" -CustomAttribute5
  DoNotMigrate

This example adds the Spanish translation for the existing English MailTip, "Please allow 4
business days for a response to messages sent to this group" that's configured on the mail-
enabled security group events@contoso.com.

  PowerShell

  Set-DistributionGroup -Identity events@contoso.com -MailTipTranslations
  @{Add="ES:Espere 4 días hábiles para responder a los mensajes enviados a este
  grupo."}

<!-- p.1141 -->

How do you know this worked?
To verify that you've successfully modified a mail-enabled security group, do any of these
steps:

        In the EAC, go to Recipients > Groups > select the mail-enabled security group (the
        Group Type value is Security group) > click Edit   and verify the property values.

        In the Exchange Management Shell, replace <GroupIdentity> with the identity of the
        group (for example, name, alias, or email address), and run this command to verify the
        property values:

          PowerShell

          Get-DistributionGroup -Identity <GroupIdentity> | Format-List

Use the Exchange Management Shell to view mail-enabled
security groups
You use the Get-DistributionGroup cmdlet to view mail-enabled security groups.

This example returns a summary list of all security groups in the organization.

  PowerShell

  Get-DistributionGroup -ResultSize unlimited -Filter "RecipientTypeDetails -eq
  'MailUniversalSecurityGroup'"

This example returns detailed information for the mail-enabled security group named Help
Desk.

  PowerShell

  Get-DistributionGroup -Identity "Help Desk" | Format-List

For detailed syntax and parameter information, see Get-DistributionGroup.

Remove mail-enabled security groups

Use the EAC to remove a mail-enabled security group
   1. In the EAC, go to Recipients > Groups.

<!-- p.1142 -->

   2. In the list of groups, find the security group that you want to remove. You can:

            Scroll through the list of groups.

            Click Search    and enter part of the group's name, email address, or alias.

            Click More options      > Advanced search to find the group.

            Click the Group Type column header to sort the groups by Security group.

     Once you've found the security group that you want to remove, select it, click Delete      ,
     and then click Yes in the warning message that appears.

Use the Exchange Management Shell to remove a mail-
enabled security group
To remove a mail-enabled security group, use this syntax:

  PowerShell

  Remove-DistributionGroup -Identity <GroupIdentity>

This example removes the mail-enabled security group that has the alias value contractors.

  PowerShell

  Remove-DistributionGroup -Identity contractors

How do you know this worked?
To verify that you've successfully removed a mail-enabled security group, do any of these
steps:

     In the EAC, go to Recipients > Groups, and verify that the group isn't listed. Note that
     you might need to click Refresh      .

     In the Exchange Management Shell, run this command and verify that the group isn't
     listed:

         PowerShell

         Get-DistributionGroup -Filter "RecipientType -eq
         'MailUniversalSecurityGroup'"

<!-- p.1143 -->

     In the Exchange Management Shell, replace <GroupIdentity> with the identity of the
     group (for example, name, alias, or email address), and run this command to verify that
     the group isn't returned:

        PowerShell

        Get-DistributionGroup -Identity <GroupIdentity> | Format-List

     In the Exchange Management Shell, run this command and verify that the group is listed:

        PowerShell

        Get-Group -Filter "RecipientTypeDetails -eq 'UniversalSecurityGroup'"

Mail-enable or mail-disable existing security
groups
To mail-enable an existing universal security group that's not already mail-enabled, or to mail-
disable an existing mail-enabled security group, you can't use the EAC. You can only use the
Exchange Management Shell.

Use the Exchange Management Shell to mail-enable an
existing security group
To mail-enable an existing universal security group, use this syntax:

  PowerShell

  Enable-DistributionGroup -Identity <GroupIdentity> [-Alias <Alias>] [-DisplayName
  <DisplayName>] [-PrimarySMTPAddress <EmailAddress>]

This example mail-enables the existing universal security group named Help Desk with the
following settings:

     Alias: hdesk. If we didn't use the Alias parameter, the value of the Name parameter would
     be used, with spaces removed (HelpDesk in this example).

     Display name: Because we aren't using the DisplayName parameter, the group's existing
     Name property value is used for the display name.

     Primary email address: Because we're using the Alias parameter, the group's primary
     email address is <alias>@ <domain>, where <domain> is specified by the email address

<!-- p.1144 -->

     policy that applies to the group. If we specified a value for the PrimarySMTPAddress
     parameter, the EmailAddressPolicyEnabled property would be set to the value $false ,
     which means the email addresses of the group aren't automatically updated by email
     address policies.

  PowerShell

  Enable-DistributionGroup -Identity "Help Desk" -Alias hdesk

After you mail-enable the security group, the group will be visible to all other *-
DistributionGroup cmdlets.

For detailed syntax and parameter information, see Enable-DistributionGroup.

How do you know this worked?

To verify that you've successfully mail-enabled an existing security group, do any of these
steps:

     In the EAC, go to Recipients > Groups. Verify that the group is listed, and the Group Type
     value is Security group. Note that you might need to click Refresh       if the EAC was
     already open.

     In the Exchange Management Shell, run this command and verify that the group is listed:

         PowerShell

         Get-DistributionGroup -Filter "RecipientType -eq
         'MailUniversalSecurityGroup'"

     In the Exchange Management Shell, replace <GroupIdentity> with the identity of the
     group (for example, name, alias, or email address), and run this command to verify the
     property values:

         PowerShell

         Get-DistributionGroup -Identity <GroupIdentity> | Format-List

Use the Exchange Management Shell to mail-disable an
existing mail-enabled security group
To mail-disable an existing mail-enabled universal security group, use this syntax:

<!-- p.1145 -->

  PowerShell

  Disable-DistributionGroup -Identity <GroupIdentity> [-IgnoreDefaultScope]

This example mail-disables the mail-enabled security group named Human Resources.

  PowerShell

  Disable-DistributionGroup -Identity "Human Resources"

Notes:

     If the distribution group isn't visible to you because of a restricted recipient scope, you'll
     need to use the IgnoreDefaultScope switch to see all groups in the Active Directory forest.
     But, when you use this switch, you'll need to identify the group by its distinguished name
     (DN). For example, "CN=<Group Name>,CN=North America,CN=Users,DC=contoso,DC=com" .

     After you mail-disable the security group, the group will be invisible to all *-
     DistributionGroup cmdlets except Enable-DistributionGroup.

For detailed syntax and parameter information, see Disable-DistributionGroup.

How do you know this worked?
To verify that you've successfully mail-disabled an existing mail-enabled universal security
group, do any of these steps:

     In the EAC, go to Recipients > Groups, and verify that the group isn't listed. Note that
     you might need to click Refresh      if the EAC was already open.

     In the Exchange Management Shell, run this command and verify that the group isn't
     listed:

         PowerShell

         Get-DistributionGroup -Filter "RecipientType -eq
         'MailUniversalSecurityGroup'"

     In the Exchange Management Shell, replace <GroupIdentity> with the name of the group,
     and run this command to verify that the group isn't returned:

         PowerShell

<!-- p.1146 -->

  Get-DistributionGroup -Identity <GroupIdentity> | Format-List

In the Exchange Management Shell, run this command and verify that the group is listed:

  PowerShell

  Get-Group -Filter "RecipientTypeDetails -eq 'UniversalSecurityGroup'"

<!-- p.1147 -->

Manage dynamic distribution groups
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Dynamic distribution groups are mail-enabled Active Directory group objects that are created
to expedite the mass sending of email messages and other information within a Microsoft
Exchange organization.

Unlike regular distribution groups that contain a defined set of members, the membership list
for dynamic distribution groups is calculated each time a message is sent to the group, based
on the filters and conditions that you define. When an email message is sent to a dynamic
distribution group, it's delivered to all recipients in the organization that match the criteria
defined for that group.

  ） Important

  A dynamic distribution group includes any recipient in Active Directory with attribute
  values that match its filter. If a recipient's properties are modified to match the filter, the
  recipient could inadvertently become a group member and start receiving messages that
  are sent to the group. Well-defined, consistent account provisioning processes will reduce
  the chances of this issue occurring.

What do you need to know before you begin?
      Estimated time to complete: 2 to 5 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Dynamic distribution groups"
      entry in the Recipients Permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.1148 -->

Create a dynamic distribution group

Use the EAC to create a dynamic distribution group
 1. In the EAC, navigate to Recipients > Groups > New > Dynamic distribution group.

 2. On the New dynamic distribution group page, complete the following boxes:

        * Display name: Use this box to type the display name. This name appears in the
        shared address book, on the To: line when email is sent to this group, and in the
        Groups list in the EAC. The display name is required and should be user-friendly so
        people recognize what it is. It also must be unique in the forest.

     ７ Note

     Group naming policy isn't applied to dynamic distribution groups.

        * Alias: Use this box to type the name of the alias for the group. The alias cannot
        exceed 64 characters and must be unique in the forest. When a user types the alias
        in the To: line of an email message, it resolves to the group's display name.

        Description: Use this box to describe the group so people know what the purpose
        of the group is. This description appears in the shared address book.

        Organizational unit: You can select an organizational unit (OU) other than the
        default (which is the recipient scope). If the recipient scope is set to the forest, the
        default value is set to the Users container in the Active Directory domain that
        contains the computer on which the EAC is running. If the recipient scope is set to a
        specific domain, the Users container in that domain is selected by default. If the
        recipient scope is set to a specific OU, that OU is selected by default.

        To select a different OU, click Browse. The dialog box displays all OUs in the forest
        that are within the specified scope. Select the OU you want, and then click OK.

        Owner: An owner for a dynamic distribution group is optional. You can add owners
        by clicking Browse and then selecting users from the list.

 3. Use the Members section to specify the types of recipients for the group and set up rules
   that will determine membership. Select one of the following boxes:

        All recipient types: Choose this option to send messages that meet the criteria
        defined for this group to all recipient types.

<!-- p.1149 -->

       Only the following recipient types: Messages that meet the criteria defined for this
       group will be sent to one or more of the following recipient types:

       Users with Exchange mailboxes: Select this check box if you want to include users
       that have Exchange mailboxes. Users that have Exchange mailboxes are those that
       have a user domain account and a mailbox in the Exchange organization.

       Users with external email addresses: Select this check box if you want to include
       users that have external email addresses. Users that have external email accounts
       have user domain accounts in Active Directory, but use email accounts that are
       external to the organization. This enables them to be included in the global address
       list (GAL) and added to distribution lists.

       Resource mailboxes: Select this check box if you want to include Exchange resource
       mailboxes. Resource mailboxes allow you to administer company resources through
       a mailbox, such as a conference room or a company vehicle.

       Contacts with external email addresses: Select this check box if you want to include
       contacts that have external email addresses. Contacts that have external email
       addresses don't have user domain accounts in Active Directory, but the external
       email address is available in the GAL.

       Mail-enabled groups: Select this check box if you want to include security groups or
       distribution groups that have been mail-enabled. Mail-enabled groups are similar to
       distribution groups. Email messages that are sent to a mail-enabled group account
       will be delivered to several recipients.

4. Click Add a rule to define the criteria for membership in this group.

5. Select one of the following recipient attributes from the drop-down list and provide a
  value. If the value for the selected attribute matches that value you define, the recipient
  receives a message sent to this group.

                                                                                  ﾉ   Expand table

   Attribute                                Send message to a recipient if...

   Recipient container                      The recipient object resides in the specified domain or
                                            OU.

   State or province                        The specified value matches the recipient's State or
                                            province property.

   Company                                  The specified value matches the recipient's Company
                                            property.

<!-- p.1150 -->

   Attribute                                Send message to a recipient if...

   Department                               The specified value matches the recipient's
                                            Department property.

   Custom attributeN (where N is a number   The specified value matches the recipient's
   from 1 to 15)                            CustomAttributeN property.

    ） Important

    The values that you enter for the selected attribute must exactly match those that
    appear in the recipient's properties. For example, if you enter Washington for State
    or province, but the value for the recipient's property is WA, the condition will not
    be met. Also, text-based values that you specify aren't case-sensitive. For example, if
    you specify Contoso for the Company attribute, messages will be sent to a recipient
    if this value is contoso.

6. In the Specify words or phrases window, type the value in the text box. Click Add and
  then click OK.

7. To add another rule to define the criteria for membership, click Add a rule under the
  previous rule that you created.

    ） Important

    If you add multiple rules to define membership, a recipient must meet the criteria of
    each rule to receive a message sent to the group. In other words, each rule is
    connected with the Boolean operator AND.

8. When you've finished, click Save to create the dynamic distribution group.

    ７ Note

    If you want to specify rules for attributes other than the ones available in the EAC,
    you must use the Exchange Management Shell to create a dynamic distribution
    group. Keep in mind that the filter and condition settings for dynamic distribution
    groups that have custom recipient filters can be managed only by using the
    Exchange Management Shell. For an example of how to create a dynamic
    distribution group with a custom query, see the next section on using the Exchange
    Management Shell to create a dynamic distribution group.

<!-- p.1151 -->

Use the Exchange Management Shell to create a dynamic
distribution group

  ７ Note

  If you do not specify an OU in your cmdlets, the default OU scope will be the local OU (the
  OU in which the dynamic distribution group is being created). With the New-
  DynamicDistributionGroup cmdlet, use the RecipientContainer parameter to specify an

  OU.

This example creates the dynamic distribution group "Mailbox Users DDG" that contains only
mailbox users.

  PowerShell

  New-DynamicDistributionGroup -IncludedRecipients MailboxUsers -Name "Mailbox Users
  DDG" -RecipientContainer Users

This example creates a dynamic distribution group with a custom recipient filter. The dynamic
distribution group contains all mailbox users on a server called Server1.

  PowerShell

  New-DynamicDistributionGroup -Name "Mailbox Users on Server1" -RecipientContainer
  Users -RecipientFilter "(RecipientTypeDetails -eq 'UserMailbox') -and (ServerName
  -eq 'Server1')"

This example creates a dynamic distribution group with a custom recipient filter. The dynamic
distribution group contains all mailbox users that have a value of "FullTimeEmployee" in the
CustomAttribute10 property.

  PowerShell

  New-DynamicDistributionGroup -Name "Full Time Employees" -RecipientFilter "
  (RecipientTypeDetails -eq 'UserMailbox') -and (CustomAttribute10 -eq
  'FullTimeEmployee')"

For detailed syntax and parameter information, see New-DynamicDistributionGroup.

How do you know this worked?
To verify that you've successfully created a dynamic distribution group, do one of the following:

<!-- p.1152 -->

     In the EAC, navigate to Recipients > Groups. The new dynamic distribution group is
     displayed in the group list. Under Group Type, the type is Dynamic distribution group.

     In the Exchange Management Shell, run the following command to display information
     about the new dynamic distribution group.

       PowerShell

        Get-DynamicDistributionGroup | Format-List
        Name,RecipientTypeDetails,RecipientFilter,PrimarySmtpAddress

Change dynamic distribution group properties

Use the EAC to change dynamic distribution group properties
   1. In the EAC, navigate to Recipients > Groups.

   2. In the list of groups, click the dynamic distribution group that you want to view or
     change, and then click Edit    .

   3. On the group's properties page, click one of the following sections to view or change
     properties.

           General

           Ownership

           Membership

           Delivery management

           Message approval

           Email options

           MailTip

           Group delegation

General

Use this section to view or change basic information about the group.

<!-- p.1153 -->

     * Display name: This name appears in the address book, on the To: line when email is sent
     to this group, and in the Groups list. The display name is required and should be user-
     friendly so people recognize what it is. It also has to be unique in your domain.

     * Alias: This is the portion of the email address that appears to the left of the at (@)
     symbol. If you change the alias, the primary SMTP address for the group will also be
     changed, and contain the new alias. Also, the email address with the previous alias will be
     kept as a proxy address for the group.

     Description: Use this box to describe the group so people know what the purpose of the
     group is. This description appears in the address book and in the Details pane in the EAC.

     Hide this group from address lists: Select this check box if you don't want users to see
     this group in the address book. To send email to this group, a sender has to type the
     group's alias or email address on the To: or Cc: lines.

     Organizational unit: This read-only box displays the organizational unit (OU) that
     contains the dynamic distribution group. You have to use Active Directory Users and
     Computers to move the group to a different OU.

Ownership
Use this section to assign a group owner. A dynamic distribution group can have only one
owner. The group owner appears on the Managed by tab of the object in Active Directory
Users and Computers.

You can add owners by clicking Browse and selecting the owner from the list. To remove the
owner, click Clear (X) and then click Save.

Membership

Use this section to change the criteria used to determine membership of the group. You can
delete or change existing membership rules and add new rules. For procedures that tell you
how to do this, see Use the EAC to create a dynamic distribution group in the procedures for
configuring membership when you use the EAC to create a new dynamic distribution group.

Delivery management

Use this section to manage who can send email to this group.

     Only senders inside my organization: Select this option to allow only senders in your
     organization to send messages to the group. This means that if someone outside your

<!-- p.1154 -->

     organization sends an email message to this group, it is rejected. This is the default
     setting.

     Senders inside and outside of my organization: Select this option to allow anyone to
     send messages to the group.

     You can further limit who can send messages to the group by allowing only specific
     senders to send messages to this group. Click Add       and then select one or more
     recipients. If you add senders to this list, they are the only ones who can send mail to the
     group. Mail sent by anyone not in the list will be rejected.

     To remove a person or a group from the list, select them in the list and then click Remove
       .

       ） Important

       If you've configured the group to allow only senders inside your organization to
       send messages to the group, email sent from a mail contact is rejected, even if
       they're added to this list.

Message approval

Use this section to set options for moderating the group. Moderators approve or reject
messages sent to the group before they reach the group members.

     Messages sent to this group have to be approved by a moderator: This check box isn't
     selected by default. If you select this check box, incoming messages are reviewed by the
     group moderators before delivery. Group moderators can approve or reject incoming
     messages.

     Group moderators: To add group moderators, click Add           . To remove a moderator,
     select the moderator, and then click Remove      . If you've selected "Messages sent to this
     group have to be approved by a moderator" and you don't select a moderator, messages
     to the group are sent to the group owners for approval.

     Senders who don't require message approval: To add people or groups that can bypass
     moderation for this group, click Add     . To remove a person or a group, select the item,
     and then click Remove      .

     Select moderation notifications: Use this section to set how users are notified about
     message approval.

<!-- p.1155 -->

        Notify all senders when their messages aren't approved: This is the default setting.
        Notify all senders, inside and outside your organization, when their message isn't
        approved.

        Notify senders in your organization only when their messages aren't approved:
        When you select this option, only people or groups in your organization are notified
        when a message that they sent to the group isn't approved by a moderator.

        Don't notify anyone when a message isn't approved: When you select this option,
        notifications aren't sent to message senders whose messages aren't approved by the
        group moderators.

Email options

Use this section to view or change the email addresses associated with the group. This includes
the group's primary SMTP addresses and any associated proxy addresses. The primary SMTP
address (also known as the reply address) is displayed in bold text in the address list, with the
uppercase SMTP value in the Type column.

     Add: Click Add        to add a new email address for this mailbox. Select one of following
     address types:

        SMTP: This is the default address type. Click this button and then type the new SMTP
        address in the * Email address box.

           ７ Note

           To make the new address the primary SMTP address for the group, select the
           Make this the reply address check box.

        Custom address type: Click this button and type one of the supported non-SMTP
        email address types in the * Email address box.

           ７ Note

           With the exception of X.400 addresses, Exchange doesn't validate custom
           addresses for proper formatting. You must make sure that the custom address
           you specify complies with the format requirements for that address type.

     Edit: To change an email address associated with the group, select it from the list, and
     then click Edit   .

<!-- p.1156 -->

        ７ Note

        To make an existing address the primary SMTP address for the group, select the
        Make this the reply address check box.

     Remove: To delete an email address associated with the group, select it from the list, and
     then click Remove     .

     Automatically update email addresses based on the email address policy applied to this
     recipient: Select this check box to have the recipient's email addresses automatically
     updated based on changes made to email address policies in your organization. This box
     is selected by default.

MailTip

Use this section to add a MailTip to alert users of potential issues before they send a message
to this group. A MailTip is text that's displayed in the InfoBar when this group is added to the
To, Cc, or Bcc lines of a new email message. For example, you could add a MailTip to large
groups to warn potential senders that their message will be sent to lots of people.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Group delegation
Use this section to assign permissions to a user (called a delegate) to allow them to send
messages as the group or send messages on behalf of the group. You can assign the following
permissions:

     Send As: This permission allows the delegate to send messages as the group. After this
     permission is assigned, the delegate has the option to add the group to the From line to
     indicate that the message was sent by the group.

     Send on Behalf Of: This permission also allows a delegate to send messages on behalf of
     the group. After this permission is assigned, the delegate has the option to add the group
     on the From line. The message will appear to be sent by the group and will say that it was
     sent by the delegate on behalf of the group.

<!-- p.1157 -->

To assign permissions to delegates, click Add under the appropriate permission to display the
Select Recipient page, which displays a list of all recipients in your Exchange organization that
can be assigned the permission. Select the recipients you want, add them to the list, and then
click OK. You can also search for a specific recipient by typing the recipient's name in the
search box and then clicking Search.

Use the Exchange Management Shell to change dynamic
distribution group properties
Use the Get-DynamicDistributionGroup and Set-DynamicDistributionGroup cmdlets to view
and change properties for dynamic distribution groups. Advantages of using the Exchange
Management Shell are the ability to change the properties that aren't available in the EAC and
change properties for multiple groups. For information about what parameters correspond to
distribution group properties, see the following topics:

     Get-DynamicDistributionGroup

     Set-DynamicDistributionGroup

Here are some examples of using the Exchange Management Shell to change dynamic
distribution group properties.

This example changes the following parameters for all dynamic distribution groups in the
organization:

     Hide all dynamic distribution groups from the address book

     Set the maximum message size that can be sent to the group to 5MB

     Enable moderation

     Assign the administrator as the group moderator

  PowerShell

  Get-DynamicDistributionGroup -ResultSize unlimited | Set-DynamicDistributionGroup
  -HiddenFromAddressListsEnabled $true -MaxReceiveSize 5MB -ModerationEnabled $true
  -ModeratedBy administrator

This example adds the proxy SMTP email address, Seattle.Employees@contoso.com, to the All
Employees group.

  PowerShell

<!-- p.1158 -->

  Set-DynamicDistributionGroup -Identity "All Employees" -EmailAddresses
  SMTP:All.Employees@contoso.com, smtp:Seattle.Employees@contoso.com

How do you know this worked?
To verify that you've successfully changed properties for a dynamic distribution group, do the
following:

     In the EAC, select the group and then click Edit   to view the property or feature that
     you changed. Depending on the property that you changed, it might be displayed in the
     Details pane for the selected group.

     In the Exchange Management Shell, use the Get-DynamicDistributionGroup cmdlet to
     verify the changes. One advantage of using the Exchange Management Shell is that you
     can view multiple properties for multiple groups. In the first example, you would run the
     following command to verify the new values.

       PowerShell

        Get-DynamicDistributionGroup -ResultSize unlimited | Format-List
        Name,HiddenFromAddressListsEnabled,MaxReceiveSize,ModerationEnabled,Moderated
        By

     For the example above where the message limits were changed, run this command.

       PowerShell

        Get-Mailbox -OrganizationalUnit "Marketing" | Format-List
        Name,IssueWarningQuota,ProhibitSendQuota,ProhibitSendReceiveQuota,UseDatabase
        QuotaDefaults

<!-- p.1159 -->

View members of a dynamic distribution
group
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

Dynamic distribution groups are distribution groups whose membership is based on specific
recipient filters rather than a defined set of recipients. For more information, see Manage
dynamic distribution groups.

You can't use the Exchange admin center (EAC) to view the members of a dynamic distribution
group. You can only use the Exchange Management Shell.

What do you need to know before you begin?
     Estimated time to complete: 2 minutes.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Dynamic distribution groups"
     entry in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to view the
members of a dynamic distribution group
To view the members of a dynamic distribution group, use the following syntax:

  PowerShell

  $<VariableName> = Get-DynamicDistributionGroup -Identity
  <DynamicDistributionGroupIdentity>

<!-- p.1160 -->

  Get-Recipient -RecipientPreviewFilter ($<VariableName>.RecipientFilter) [-
  OrganizationalUnit ($<VariableName>.RecipientContainer)]

     <DynamicDistributionGroupIdentity> is the name, alias, or email address of the dynamic

     distribution group.
     The OrganizationalUnit parameter is required only if you used the RecipientContainer
     parameter in the filter for the dynamic distribution group to specify an OU or container
     that's different than where the dynamic distribution group object resides (typically, the
     Users container). It's OK to include the OrganizationalUnit parameter even if it isn't
     required.

This example returns the list of members for the dynamic distribution group named Full Time
Employees. The first command stores the dynamic distribution group object in the variable
$FTE . The second command uses the Get-Recipient cmdlet to list the recipients that match the

criteria defined for the dynamic distribution group.

  PowerShell

  $FTE = Get-DynamicDistributionGroup -Identity "Full Time Employees"

  Get-Recipient -RecipientPreviewFilter ($FTE.RecipientFilter)

This example returns the members of the dynamic distribution group named Project X that
exists in the Users container, but uses the OU named ContosoProjects in the filter for the
group.

  PowerShell

  $ProjectX = Get-DynamicDistributionGroup -Identity "Project X"

  Get-Recipient -RecipientPreviewFilter ($ProjectX.RecipientFilter) -
  OrganizationalUnit ($ProjectX.RecipientContainer)

For detailed syntax and parameter information, see Get-DynamicDistributionGroup and Get-
Recipient.
