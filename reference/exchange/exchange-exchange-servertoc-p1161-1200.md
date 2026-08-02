---
title: "Exchange Server — pages 1161-1200"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1161-1200
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1161-1200
family: exchange
documentKind: "doc"
abstract: "Manage mail contacts Article • 04/30/2025 APPLIES TO: 2016 2019 Subscription Edition Mail contacts are essentially contacts for people outside your Exchange or organization. Each mail contact has an external email address. For more information about mail contacts, see Recipients"
---

# Exchange Server — pages 1161-1200

<!-- p.1161 -->

Manage mail contacts
Article • 04/30/2025

APPLIES TO:          2016      2019       Subscription Edition

Mail contacts are essentially contacts for people outside your Exchange or organization. Each
mail contact has an external email address. For more information about mail contacts, see
Recipients.

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
  Server , Exchange Online            , or Exchange Online Protection .

Create a mail contact

Use the EAC to create a mail contact
   1. In the EAC, navigate to Recipients > Contacts.

   2. Click New        > Mail contact.

   3. Complete the following boxes on the New mail contact page:

              First name: Use this box to type the contact's first name.

              Initials: Use this box to type the contact's initials.

<!-- p.1162 -->

           Last name: Use this box to type the contact's last name.

           * Display name: Use this box to type a display name for the contact. This is the
           name that's listed in the contacts list in the EAC and in your organization's address
           book. By default, this box is populated with the names you enter in the First name,
           Initials, and Last name boxes. If you didn't use those boxes, you must still type a
           name in this box because it's required. The name can't exceed 64 characters.

           * Name: Use this box to type a name for the contact. This is the name that's listed in
           the directory service. Like the display name, this box is populated by default with the
           names you enter in the First name, Initials, and Last name boxes. If you didn't use
           those boxes, you must still type a name in this box because it's required. The name
           can't exceed 64 characters.

           * Alias: Use this box to type an alias (64 characters or less) for the contact. This box
           is required.

           * External email address: Use this box to type the outside email account of the
           contact. This box is required. Email sent to this contact is forwarded to this email
           address.

           Organizational unit: You can select an organizational unit (OU) other than the
           default, which is the recipient scope. If the recipient scope is set to the forest, the
           default value is set to the Users container in the domain that contains the computer
           on which the EAC is running. If the recipient scope is set to a specific domain, the
           Users container in that domain is selected by default. If the recipient scope is set to
           a specific OU, that OU is selected by default.

           To select a different OU, click Browse. The dialog box displays all OUs in the forest
           that are within the specified scope. Select the OU you want, and then click OK.

   4. When you've finished, click Save.

Use the Exchange Management Shell to create a mail contact
This example creates a mail contact for Debra Garcia in Exchange Server 2016.

  PowerShell

  New-MailContact -Name "Debra Garcia" -ExternalEmailAddress
  dgarcia@tailspintoys.com -OrganizationalUnit Users

This example mail-enables an existing contact named Karen Toh in Exchange Server 2016.

<!-- p.1163 -->

  PowerShell

  Enable-MailContact -Identity "Karen Toh" -ExternalEmailAddress
  ktoh@tailspintoys.com

How do you know this worked?
To verify that you've successfully created a mail contact, do one of the following:

     In the EAC, navigate to Recipients > Contacts. The new mail contact is displayed in the
     contact list. Under Contact Type, the type is Mail contact.

     In the Exchange Management Shell, run the following command to display information
     about the new mail contact.

        PowerShell

        Get-MailContact <Name> | Format-List
        Name,RecipientTypeDetails,ExternalEmailAddress

Change mail contact properties

Use the EAC to change mail contact properties
   1. In the EAC, navigate to Recipients > Contacts.

   2. In the list of mail contacts and mail users, click the mail contact that you want to change
     the properties for, and then click Edit   .

   3. On the mail contact properties page, click one of the following sections to view or change
     properties.

           General

           Contact Information

           Organization

           Email Options

           MailTip

General

<!-- p.1164 -->

Use the General section to view or change basic information about the mail contact.

     First name, Initials, Last name

     * Name: This is the name that's listed in Active Directory. If you change this name, it can't
     exceed 64 characters.

     * Display name: This name appears in your organization's address book, on the To and
     From lines in email, and in the Mailbox list. This name can't contain empty spaces before
     or after the display name.

     * Alias: This is the mail contact's alias. If you change it, it must be unique in the
     organization and must be 64 characters or less.

     * External email address: This is mail contact's primary SMTP address and their outside
     email account. Email sent to this contact is forwarded to this email address.

     Click More options to display the OU that contains the mail contact account. You have to
     use Active Directory Users and Computers to move the contact to a different OU.

Contact Information
Use the Contact Information section to view or change the recipient's contact information,
such as mailing address and telephone numbers. This information is displayed in the address
book.

Organization
Use the Organization section to record detailed information about the mail contact's role in
the organization. This information is displayed in the address book. Also, you can create a
virtual organization chart that's accessible from email clients such as Outlook.

     Title: Use this box to view or change the contact's title.

     Department: Use this box to view or change the department in which the contact works.
     You can use this box to create recipient conditions for dynamic distribution groups and
     address lists.

     Company: Use this box to view or change the company for which the contact works. You
     can also use this box to create recipient conditions for dynamic distribution groups.

     Manager: To add a manager, click Browse. In Select Manager, select a person, and then
     click OK.

<!-- p.1165 -->

     Direct reports: You can't modify this box. A direct report is a recipient who reports to a
     specific manager. If you've specified a manager for the recipient, that recipient appears as
     a direct report in the details of the manager's mailbox. For example, Toby manages Ann
     and Spencer, who are mail contacts, so Toby is specified in the Manager box in the
     organization properties for Ann and Spencer, and Ann and Spencer appear in the Direct
     reports box in the properties of Toby's mailbox.

Email Options
Use the Email Options section to add or remove proxy addresses for the mail contact or edit
existing proxy addresses. The mail contact's primary SMTP address is also displayed in this
section, but you can't change it. To change it, you have to change the contact's external email
address in the General section.

MailTip

Use the MailTip section to add a MailTip to alert users of potential issues before they send a
message to this recipient. A MailTip is text that's displayed in the InfoBar when this recipient is
added to the To, Cc, or Bcc lines of a new email message.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Use the Exchange Management Shell to change mail contact
properties
Properties for a mail contact are stored in both Active Directory and Exchange. In general, use
the Get-Contact and Set-Contact cmdlets to view and change organization and contact
information properties. Use the Get-MailContact and Set-MailContact cmdlets to view or
change mail-related properties, such as email addresses, the MailTip, custom attributes, and
whether the contact is hidden from address lists.

For more information, see the following topics:

     Get-Contact

     Set-Contact

     Get-MailContact

<!-- p.1166 -->

     Set-MailContact

Here are some examples of using the Exchange Management Shell to change mail contact
properties.

This example configures the Title, Department, Company, and Manager properties for the mail
contact Kai Axford.

  PowerShell

  Set-Contact "Kai Axford" -Title Consultant -Department "Public Relations" -Company
  Fabrikam -Manager "Karen Toh"

This example sets the CustomAttribute1 property to a value of PartTime for all mail contacts
and hides them from the organization's address book.

  PowerShell

  Get-MailContact | Set-MailContact -CustomAttribute1 PartTime -
  HiddenFromAddressListsEnabled $true

This example sets the CustomAttribute15 property to a value of TemporaryEmployee for all
mail contacts in the Public Relations department.

  PowerShell

  Get-Contact -Filter "Department -eq 'Public Relations'" | Set-MailContact -
  CustomAttribute15 TemporaryEmployee

How do you know this worked?
To verify that you've successfully changed properties for a mail contact, do the following:

     In the EAC, select the mail contact, and then click Edit   to view the property that you
     changed.

     In the Exchange Management Shell, use the Get-Contact and Get-MailContact cmdlets to
     verify the changes. One advantage of using the Exchange Management Shell is that you
     can view multiple properties for multiple mail contacts. In the example above where all
     mail contacts had the CustomAttribute1 property set to PartTime and were hidden from
     the address book, run the following command to verify the changes.

        PowerShell

<!-- p.1167 -->

        Get-MailContact | Format-List
        Name,CustomAttribute1,HiddenFromAddressListsEnabled

     In the example above where the CustomAttribute15 was set for all mail contacts in the
     Public Relations department, run the following command to verify the changes.

        PowerShell

        Get-Contact -Filter "Department -eq 'Public Relations'" | Get-MailContact |
        Format-List Name,CustomAttribute15

Bulk edit mail contacts
You can use the EAC to change selected properties for multiple mail contacts. When you select
two or more mail contacts from the contacts list in the EAC, the properties that can be bulk
edited are displayed in the Details pane. When you change one of these properties, the change
is applied to all selected recipients.

When you bulk edit mail contacts, you can change the following property areas:

     Contact Information: Change shared properties such as street, postal code, and city
     name.

     Organization: Change shared properties such as department name, company name, and
     the manager that the selected mail contacts or mail users report to.

Use the EAC to bulk edit mail contacts
   1. In the EAC, navigate to Recipients > Contacts.

   2. In the list of contacts, select two or more mail contacts. You can't bulk edit a combination
     of mail contacts and mail users.

         Tip

        You can select multiple adjacent mail contacts by holding down the Shift key and
        clicking the first mail contact, and then clicking the last mail contact you want to edit.
        You can also select multiple mail contacts by holding down the Ctrl key and clicking
        each one that you want to edit.

<!-- p.1168 -->

   3. In the Details pane, under Bulk Edit, click Update under Contact Information or
     Organization.

   4. Make the changes on the properties page and then save your changes.

How do you know this worked?
To verify that you've successfully bulk edited mail contacts, do one of the following:

     In the EAC, select each of the mail contacts that you bulk edited, and then click Edit   to
     view the properties that you changed.

     In the Exchange Management Shell, use the Get-Contact cmdlet to verify the changes.
     For example, say you used the bulk edit feature in the EAC to change the manager and
     the office for all mail contacts from a vendor company named A. Datum Corporation. To
     verify these changes, you could run the following command in the Exchange
     Management Shell.

        PowerShell

        Get-Contact -ResultSize unlimited -Filter "Company -eq 'Adatum'" | Format-
        List Name,Office,Manager

<!-- p.1169 -->

Manage mail users
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Mail users are similar to mail contacts. Both have external email addresses and both contain
information about people outside your Exchange organization that can be displayed in the
shared address book and other address lists. However, unlike a mail contact, a mail user has
logon credentials in your Exchange organization and can access resources. For more
information, see Recipients.

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

Create a mail user

Use the EAC to create a mail user
   1. In the EAC, navigate to Recipients > Contacts > New > Mail user.

   2. On the New mail user page, in the * Alias box, type the alias for the mail user. The alias
      can't exceed 64 characters and must be unique in the forest. This is required.

   3. Do one of the following to specify the email address type for the mail user:

<!-- p.1170 -->

       To specify an SMTP email address for the mail user's external email address, click
       SMTP.

    ７ Note

    Exchange validates SMTP addresses for correct formatting. If your entry is
    inconsistent with the SMTP format, an error message will be displayed when you
    click Save to create the mail user.

       To specify a custom address type, click the option button and then type the custom
       address type. For example, you can specify an X.500, GroupWise, or Lotus Notes
       address.

4. In the * External email address box, type the mail user's external email address. Email
  sent to this mail user is forwarded to this email address. This is required.

5. Select one of the following options:

       Existing user: Select to mail-enable an existing user.

       Click Browse to open the Select User - Entire Forest dialog box. This dialog box
       displays a list of user accounts in the organization that aren't mail-enabled or don't
       have mailboxes. Select the user account you want to mail-enable, and then click OK.
       If you select this option, you don't have to provide user account information
       because this information already exists in Active Directory.

       New user: Select to create a new user account in Active Directory and mail-enable
       the user. If you select this option, you'll have to provide the required user account
       information.

6. If you selected New User in Step 5, complete the following information on the New mail
  user page. Otherwise skip to Step 7.

       First name: Type the first name of the mail user.

       Initials: Type the initials of the mail user.

       Last name: Type the last name of the mail user.

       * Display name: Use this box to type a display name for the user. This is the name
       that's listed in the contacts list in the EAC and in your organization's address book.
       By default, this box is populated with the names you enter in the First name, Initials,
       and Last name boxes. If you didn't use those boxes, you must still type a name in
       this box because it's required. The name can't exceed 64 characters.

<!-- p.1171 -->

           * Name: Use this box to type a name for the mail user. This is the name that's listed
           in the directory service. This box is also populated with the names you enter in the
           First name, Initials, and Last name boxes. If you didn't use those boxes, you must
           still type a name because this is required. This name also can't exceed 64 characters.

           Organizational unit: You can select an organizational unit (OU) other than the
           default (which is the recipient scope). If the recipient scope is set to the forest, the
           default value is set to the Users container in the domain that contains the computer
           on which the EAC is running. If the recipient scope is set to a specific domain, the
           Users container in that domain is selected by default. If the recipient scope is set to
           a specific OU, that OU is selected by default.

           To select a different OU, click Browse. The dialog box displays all OUs in the forest
           that are within the specified scope. Select the OU you want, and then click OK.

           * User logon name: Type the name that the mail user will use to log on to the
           domain. The user logon name consists of a username on the left side of the at (@)
           symbol and a suffix on the right side. Typically, the suffix is the domain name the
           user account resides in.

           * New Password: Type the password that the mail user must use to log on to the
           domain. Make sure that the password you supply complies with the password
           length, complexity, and history requirements of the domain you're creating the user
           account in.

           * Confirm password: Use this box to confirm the password that you typed in the
           Password box.

           Require password change on next logon: Select this check box if you want mail
           users to reset the password when they first log on to the domain.

           If you select this check box, at first logon, the new mail user will be prompted with a
           dialog box in which to change the password. The mail user won't be allowed to
           perform any tasks until the password is changed successfully.

   7. When you've finished, click Save to create the mail user.

Use the Exchange Management Shell to create a mail user
This example creates a mail-enabled user account for Jeffrey Zeng in Exchange Server 2016
with the following details:

     The name and display name is Jeffrey Zeng.
     The alias is jeffreyz.

<!-- p.1172 -->

     The external email address is jzeng@tailspintoys.com .
     The first name is Jeffrey and the last name is Zeng.
     The logon name is jeffreyz@contoso.com .
     You're prompted to enter the password.
     The mail user will be created in the default OU. To specify a different OU, you can use the
     OrganizationalUnit parameter.

  PowerShell

  New-MailUser -Name "Jeffrey Zeng" -Alias jeffreyz -ExternalEmailAddress
  jzeng@tailspintoys.com -FirstName Jeffrey -LastName Zeng -UserPrincipalName
  jeffreyz@contoso.com -Password (Read-Host "Enter password" -AsSecureString)

For detailed syntax and parameter information, see New-MailUser.

How do you know that you've created a mail user?
To verify that you've successfully created a mail user, do one of the following:

     In the EAC, navigate to Recipients > Contacts. The new mail user is displayed in the list of
     contacts. Under Contact Type, the type is Mail user.

     In the Exchange Management Shell, run the following command to display information
     about the new mail user.

        PowerShell

        Get-MailUser <Name> | Format-List
        Name,RecipientTypeDetails,ExternalEmailAddress

Change mail user properties
After you create a mail user, you can make changes and set additional properties by using the
EAC or the Exchange Management Shell.

You can also change properties for multiple user mailboxes at the same time. For more
information, see Use the EAC to bulk edit mail users.

The estimated time to complete this task will vary based on the number of properties you want
to view or change.

Use the EAC to change user mailbox properties

<!-- p.1173 -->

   1. In the EAC, navigate to Recipients > Contacts.

   2. In the list of contacts, click the mail user that you want to change the properties for, and
     then click Edit   .

   3. On the mail user properties page, click one of the following sections to view or change
     properties.

           General
           Contact Information
           Organization
           Email Addresses
           Mail Flow Settings
           Member Of
           MailTip

General

Use the General section to view or change basic information about the mail user.

     First name, Initials, Last name

     * Name: This is the name that's listed in Active Directory. If you change this name, it can't
     exceed 64 characters.

     * Display name: This name appears in your organization's address book, on the To: and
     From: lines in email, and in the list of contacts in the EAC. This name can't contain empty
     spaces before or after the display name.

     * User logon name: This is the name that the user uses to log on to the domain.

     Hide from address lists: Select this check box to prevent the mail user from appearing in
     the address book and other address lists that are defined in your Exchange organization.
     After you select this check box, users can still send messages to the recipient by using the
     email address.

     Require password change on next logon: Select this check box if you want the user to
     reset their password the next time they log on to the domain.

Click More options to view or change these additional properties:

     Organizational unit: This read-only box displays the organizational unit (OU) that
     contains the mail user account. You have to use Active Directory Users and Computers to
     move the account to a different OU.

<!-- p.1174 -->

     Custom attributes: This section displays the custom attributes defined for the mail user.
     To specify custom attribute values, click Edit     . You can specify up to 15 custom
     attributes for the recipient.

Contact Information
Use the Contact Information section to view or change the user's contact information. The
information on this page is displayed in the address book. Click More options to display
additional boxes.

   Tip

  You can use the State/Province box to create recipient conditions for dynamic distribution
  groups, email address policies, or address lists.

Organization
Use the Organization section to record detailed information about the user's role in the
organization. This information is displayed in the address book. Also, you can create a virtual
organization chart that's accessible from email clients such as Outlook.

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
     the details of the manager's mailbox. For example, Kari manages Chris and Kate, so Kari is
     specified in the Manager box for Chris and Kate, and Chris and Kate appear in the Direct
     reports box in the properties of Kari's account.

Email Addresses

<!-- p.1175 -->

Use the Email Addresses section to view or change the email addresses associated with the
mail user. This includes the mail user's primary SMTP address, their external email address, and
any associated proxy addresses. The primary SMTP address (also known as the default reply
address) is displayed in bold text in the address list, with the uppercase SMTP value in the Type
column. By default, after the mail user is created, the primary SMTP address and the external
email address are the same.

     Add: Click Add     to add a new email address for this mailbox. Select one of following
     address types:

        SMTP: This is the default address type. Click this button and then type the new SMTP
        address in the * Email address box.

        Custom address type: Click this button and type one of the supported non-SMTP
        email address types in the * Email address box.

        Note: With the exception of X.400 addresses, Exchange doesn't validate custom
        addresses for correct formatting. You must make sure that the custom address you
        specify complies with the format requirements for that address type.

     Set the external email address: Use this box to change the mail user's external address.
     Email sent to this mail user is forwarded to this email address.

     Automatically update email addresses based on the email address policy applied to this
     recipient: Select this check box to have the recipient's email addresses automatically
     updated based on changes made to email address policies in your organization. This box
     is selected by default.

Mail Flow Settings

Use the Mail Flow Settings section to view or change the following settings:

     Message Size Restrictions: These settings control the size of messages that the mail user
     can send and receive. Click View details to view and change maximum size for sent and
     received messages.

        Sent messages: To specify a maximum size for messages sent by this user, select the
        Maximum message size (KB) check box and type a value in the box. The message size
        must be between 0 and 2,097,151 KB. If the user sends a message larger than the
        specified size, the message will be returned to the user with a descriptive error
        message.

        Received messages: To specify a maximum size for messages received by this user,
        select the Maximum message size (KB) check box and type a value in the box. The

<!-- p.1176 -->

        message size must be between 0 and 2,097,151 KB. If the user receives a message
        larger than the specified size, the message will be returned to the sender with a
        descriptive error message.

     Message Delivery Restrictions: These settings control who can send email messages to
     this mail user. Click View details to view and change these restrictions.

        Accept messages from: Use this section to specify who can send messages to this
        user.

        All senders: Select this option to specify that the user can accept messages from all
        senders. This includes both senders in your Exchange organization and external
        senders. This option is selected by default. This option includes external users only if
        you clear the Require that all senders are authenticated check box. If you select this
        check box, messages from external users will be rejected.

        Only senders in the following list: Select this option to specify that the user can accept
        messages only from a specified set of senders in your Exchange organization. Click
        Add     to display the Select Recipients page, which displays a list of all recipients in
        your Exchange organization. Select the recipients you want, add them to the list, and
        then click OK. You can also search for a specific recipient by typing the recipient's
        name in the search box and then clicking Search       .

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

<!-- p.1177 -->

may match the criteria for one or more dynamic distribution groups in your organization.
However, dynamic distribution groups aren't displayed on this page because their membership
is calculated each time they're used.

MailTip
Use the MailTip section to add a MailTip to alert users of potential issues before they send a
message to this recipient. A MailTip is text that's displayed in the InfoBar when this recipient is
added to the To, Cc, or Bcc lines of a new email message.

  ７ Note

  MailTips can include HTML tags, but scripts aren't allowed. The length of a custom MailTip
  can't exceed 175 displayed characters. HTML tags aren't counted in the limit.

Use the Exchange Management Shell to change mail user
properties
Properties for a mail user are stored in both Active Directory and Exchange. In general, use the
Get-User and Set-User cmdlets to view and change organization and contact information
properties. Use the Get-MailUser and Set-MailUser cmdlets to view or change mail-related
properties, such email addresses, the MailTip, custom attributes, and whether the mail user is
hidden from address lists.

Use the Get-MailUser and Set-MailUser cmdlets to view and change properties for mail users.
For information, see the following topics:

     Get-User
     Set-User
     Get-MailUser
     Set-MailUser

Here are some examples of using the Exchange Management Shell to change mail user
properties.

This example sets the external email address for Pilar Pinilla.

  PowerShell

  Set-MailUser "Pilar Pinilla" -ExternalEmailAddress pilarp@tailspintoys.com

<!-- p.1178 -->

This example hides all mail users from the organization's address book.

  PowerShell

  Get-MailUser | Set-MailUser -HiddenFromAddressListsEnabled $true

This example sets the Company property for all mail users to Contoso.

  PowerShell

  Get-User -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'mailuser'" |
  Set-User -Company Contoso

This example sets the CustomAttribute1 property to a value of ContosoEmployee for all mail
users that have a value of Contoso in the Company property.

  PowerShell

  Get-User -ResultSize unlimited -Filter "(RecipientTypeDetails -eq 'mailuser') -and
  (Company -eq 'Contoso')" | Set-MailUser -CustomAttribute1 ContosoEmployee

For detailed syntax and parameter information, see Set-MailUser.

How do you know that you've changed properties for mail
users?
To verify that you've successfully changed properties for mail users, do the following:

     In the EAC, select the mail user and then click Edit   to view the property that you
     changed.

     In the Exchange Management Shell, use the Get-User and Get-MailUser cmdlets to verify
     the changes. One advantage of using the Exchange Management Shell is that you can
     view multiple properties for multiple mail contacts.

        PowerShell

        Get-MailUser | Format-List Name,CustomAttribute1

     In the example above where the Company property was set to Contoso for all mail
     contacts, run the following command to verify the changes:

        PowerShell

<!-- p.1179 -->

        Get-User -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'mailuser'"
        | Format-List Name,Company

     In the example above where all mail users had the CustomAttribute1 property set to
     ContosoEmployee, run the following command to verify the changes.

        PowerShell

        Get-MailUser | Format-List Name,CustomAttribute1

Bulk edit mail users
You can also use the EAC to change selected properties for multiple mail users. When you
select two or more mail users from the contacts list in the EAC, the properties that can be bulk
edited are displayed in the Details pane. When you change one of these properties, the change
is applied to all selected recipients.

When you bulk edit mail users, you can change the following property areas:

     Contact Information: Change shared properties such as street, postal code, and city
     name.

     Organization: Change shared properties such as department name, company name, and
     the manager that the selected mail contacts or mail users report to.

Use the EAC to bulk edit mail users
   1. In the EAC, navigate to Recipients > Contacts.

   2. In the list of contacts, select two or more mail users. You can't bulk edit a combination of
     mail contacts and mail users.

     Note: You can select multiple adjacent mail users by holding down the Shift key and
     clicking the first mail user, and then clicking the last mail user you want to edit. You can
     also select multiple mail users by holding down the Ctrl key and clicking each one that
     you want to edit.

   3. In the Details pane, under Bulk Edit, click Update under Contact Information or
     Organization.

   4. Make the changes on the properties page and then save your changes.

<!-- p.1180 -->

How do you know this worked?
To verify that you've successfully bulk edited mail users, do one of the following:

     In the EAC, select each of the mail users that you bulk edited and then click Edit   to
     view the properties that you changed.

     In the Exchange Management Shell, use the Get-User cmdlet to verify the changes. For
     example, say you used the bulk edit feature in the EAC to change the manager and the
     office for all mail users from a vendor company named A. Datum Corporation. To verify
     these changes, you could run the following command in the Exchange Management
     Shell:

        PowerShell

        Get-User -ResultSize unlimited -Filter "(RecipientTypeDetails -eq 'mailuser')
        -and (Company -eq 'Adatum')" | Format-List Name,Office,Manager

<!-- p.1181 -->

Create and manage room mailboxes in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019      Subscription Edition

   Tip

  This article applies to on-premises Exchange servers. The cloud version of this article is
  available at Manage resource mailboxes in Exchange Online.

A room mailbox is one of the available resource mailbox types in Exchange. Unlike equipment
mailboxes, room mailboxes are assigned to a physical location, such as a conference room, an
auditorium, or a training room. Users can easily reserve these rooms by including the room
mailbox in meeting requests.

A room list is a special distribution group that contains only room mailboxes. Room lists help
organize hundreds of room mailboxes or room mailboxes by building. To create and manage
room lists, see the Create room lists section later in this article.

You can use the Exchange admin center (EAC), the Exchange Management Shell, and Outlook
on the web (formerly known as Outlook Web App or OWA) to manage room mailboxes. You
can create room lists only in the Exchange Management Shell.

To allow users to manage the calendar in a room mailbox (for example, an executive assistant
who needs to rearrange meetings), use the instructions in Manage permissions for recipients.
After a user gets permission to access the room mailbox, they can open the mailbox using the
instructions in Open and use a shared mailbox in Outlook for Windows .

   Tip

  Never set a room mailbox as the organizer of a meeting. Include room mailboxes only in
  the Attendee or Location fields in the meeting request.

  Instead of using a room mailbox like a team calendar, consider using the Exchange shared
  calendar feature.

To learn more about the types of recipients in Exchange, see Recipients.

What do you need to know before you begin?

<!-- p.1182 -->

     Estimated time to complete: 5 minutes.
     To open the Exchange admin center (EAC), see Exchange admin center in Exchange
     Server. To open the Exchange Management Shell, see Open the Exchange Management
     Shell.
     You need to be assigned permissions before you can perform these procedures. To see
     what permissions you need, see the "Recipient Provisioning Permissions" section in the
     Recipients Permissions article.
     If you're running Exchange Server in a hybrid scenario, be sure to create room mailboxes
     in the appropriate place. Create room mailboxes for your on-premises organization in
     Exchange Server, and create room mailboxes for your cloud organization in Exchange
     Online.
     We don't recommend using Full Access permissions to manage the room mailbox
     calendar. Instead, share the room calendar with the user who needs to manage meetings.
     After the user accepts the sharing invitation, they can manage meetings in the room
     calendar. If the room calendar is shared with Delegate permissions, the user also receives
     copies of all meeting requests sent to the room mailbox in their own mailbox.
     Sharing a room mailbox calendar doesn't prevent the calendar from having the Accept or
     decline booking requests automatically setting enabled. If the room calendar is shared
     with Accept or decline booking requests automatically enabled, meeting requests are
     accepted by default. But users with Editor or Delegate permissions to the room calendar
     can change the response.
     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum .

Use the EAC to create room mailboxes
To create a room mailbox in the EAC, do the following steps:

   1. In the EAC, go to Recipients > Resources tab.

   2. On the Resources tab, select      New > Room mailbox.

   3. On the New room mailbox page that opens, configure the following settings:

              Room name: Enter a unique, descriptive name. This value is required and it can't
              exceed 64 characters.

<!-- p.1183 -->

        Tip

       Although other properties are available to describe the details of the room (for
       example, Location and Capacity), consider summarizing the important details in the
       Name value using a consistent naming convention. Users can easily see the details in
       the room name when they select the room mailbox from the address book.

          Alias: A unique value that's use on the left side of the @ symbol in the email
          address. This value is required.
          Organizational unit: Select Browse to specify the location in Active Directory where
          the room mailbox object is created.
          Location, Phone, Capacity: Use these fields to enter details about the room.
          However, as explained earlier, you can include some or all of this information in the
          room name so users can see it.
          Select More options to reveal the following settings:
             Mailbox database: Select Browse to specify the mailbox database where the
             room mailbox is created.
             Address book policy: Select the ABP that includes the room mailbox. ABPs
             contain a global address list (GAL), an offline address book (OAB), a room list (not
             a room list distribution group), and a set of address lists. To learn more, see
             Address book policies in Exchange Server.

   4. When you're finished on the New room mailbox page, select Save to create the room
     mailbox.

After you create a room mailbox, you can Change how a room mailbox handles meeting
requests (including whether it responds automatically or someone needs to decide what to
do). By default, the room mailbox has the following settings:

     Automatically accept or decline meeting requests (depending on whether the requests
     conflict with any existing meetings on the calendar).
     Allow recurring meetings.
     Allow meetings up to 24 hours long up to 180 days from today (and decline longer
     meeting requests).

To change other mailbox settings, go to the Change other room mailbox properties section.

Use the Exchange Management Shell to create room
mailboxes
To create a room mailbox in the Exchange Management Shell, use the following syntax:

<!-- p.1184 -->

  PowerShell

  New-Mailbox -Room -Name "<UniqueDescriptiveName>" [-Alias <AliasValue>] [-Database
  <DatabaseIdentity>]
   [-DisplayName <String>] [-EnableRoomMailboxAccount $true] [-OrganizationalUnit
  <OrganizationalUnitIdentity>] [-PrimarySmtpAddress <SmtpAddress>] [-
  ResetPasswordOnNextLogon <Boolean>] [-RoomMailboxPassword <SecureString>] [-
  UserPrincipalName <UPN>]

     By default, accounts associated with room mailboxes are disabled. The
     EnableRoomMailboxAccount and RoomMailboxPassword parameters are required to
     enable the room mailbox account and set its password for features like the Skype for
     Business Room System or Microsoft Teams Rooms.
     You can't use the UserPrincipalName parameter with the EnableRoomMailboxAccount and
     RoomMailboxPassword parameters.

This example creates a room mailbox named Conference Room 6. Because we aren't using the
Alias, DisplayName, PrimarySmtpAddress, or UserPrincipalName parameters, the following
values are based on the Name parameter value:

     Alias: ConferenceRoom6. If you specify an Alias value without using the
     PrimarySmtpAddress or UserPrincipalName parameters, the Alias value is used on the left
     side of the '@' symbol.
     DisplayName: Conference Room 6
     PrimarySmtpAddress: Alias and domain values from the email address policy. If the policy
     doesn't specify an alias, the value ConferenceRoom6 is used if you don't use the Alias
     parameter.
     UserPrincipalName: ConferenceRoom6@<default Active directory domain> if you don't use
     the Alias parameter.

  PowerShell

  New-Mailbox -Room -Name "Conference Room 6"

This example creates a room mailbox named Training Room A with an enabled user account.
The RoomMailboxPassword parameter value prompts you to enter the password. The value you
enter in the User name box in the Windows PowerShell credential request dialog is
meaningless; only the Password value matters.

  PowerShell

  New-Mailbox -Room -Name "Training Room A" -UserPrincipalName traina@contoso.com -
  Alias traina -EnableRoomMailboxAccount $true -RoomMailboxPassword (Get-

<!-- p.1185 -->

  Credential).password

For detailed syntax and parameter information, see New-Mailbox.

How do you know you successfully created a room mailbox?
To verify that you successfully created a room mailbox, do either of the following steps:

     EAC: Go to Recipients > Resources tab. On the Resources tab, verify the room mailbox is
     listed. Select the mailbox, and then select   Edit to view the mailbox properties.

     Exchange Management Shell: To display information about the mailbox, replace
     <RoomMailboxIdentity> with the name, alias, user principal name (UPN), or email address
     of the mailbox, and then run the following command:

       PowerShell

        Get-Mailbox -Identity <RoomMailboxIdentity> | Format-List

Change how a room mailbox handles meeting
requests
You can use the EAC, Outlook on the web options for the room mailbox, or the Exchange
Management Shell to change how a room mailbox handles meeting requests.

All settings are available on the Set-CalendarProcessing cmdlet in the Exchange Management
Shell, but the following settings are available in Outlook on the web and not in the EAC:

     Turn off reminders
     Allow conflicts
        Allow up to this number of individual conflicts
        Allow up to this percentage of individual conflicts
     These users can schedule automatically if the resource is available and can submit a
     request for owner approval if the resource is unavailable

Use the EAC to change how a room mailbox handles meeting
requests
   1. In the Exchange admin center, navigate to Recipients > Resources.

   2. On the Resources tab, select the room mailbox, and then select      Edit.

<!-- p.1186 -->

3. On the room mailbox properties page that opens, the following tabs are specific to how
  the room mailbox handles meeting requests:

       Booking Delegates tab:
          Booking requests section: Select one of the following values:
             Use customized settings to accept or decline booking requests: This is the
             default value.
             Accept or decline booking requests automatically: Meeting requests are
             automatically accepted. Meeting requests are automatically declined in the
             following scenarios:
                A scheduling conflict with an existing reservation.
                The meeting request violates the scheduling limits of the room (for
                example, the meeting is too long).
             Select delegates who can accept or decline booking requests: One of the
             people you add to the Delegates box is responsible for accepting or declining
             meeting requests that are sent to the room mailbox. If you assign multiple
             delegates, only one needs to act on a meeting request.

       Booking Options tab: The following settings are available:

          Allow repeating meetings: Allows or prevents recurring meetings for the room.
          By default, this setting is selected, so recurring meetings are allowed.

          Allow scheduling only during working hours: Accepts or declines meeting
          requests that aren't during the working hours defined for the room mailbox. By
          default, this setting isn't selected, so meeting requests are allowed outside the
          working hours. By default, working hours are 8:00 A.M. to 5:00 P.M. Monday
          through Friday. You can set the working hours on a mailbox in the following
          locations:
             Outlook on the web in Settings > Options > Calendar > Personalization >
             Calendar appearance > Show work week as and Set your working hours.
             The WorkDays, WorkingHoursEndTime, WorkingHoursStartTime, and
             WorkingHoursTimeZone parameters on the Set-MailboxCalendarConfiguration
             cmdlet in the Exchange Management Shell.

          Always decline if the end date is beyond this limit: Controls the behavior of
          recurring meetings that extend beyond the date specified by the Maximum
          booking lead time (days) value:
             Selected: Recurring meeting requests are automatically declined if the
             meetings start on or before the Maximum booking lead time (days) date, and
             the meetings extend beyond the Maximum booking lead time (days) date.
             This is the default setting.

<!-- p.1187 -->

                Not selected: Recurring meeting requests are automatically accepted if the
                meetings start on or before Maximum booking lead time (days) date.
                However, any meetings that extend beyond the Maximum booking lead time
                (days) date are automatically removed (no meetings can extend beyond that
                date).

             Maximum booking lead time (days): Specifies the maximum number of days in
             advance that the room can be booked. A valid value is an integer between 0
             (today) and 1080 days. The default value is 180 days.

             Maximum duration (hours): Specifies the maximum duration that the room can
             be reserved in a meeting request. A valid value is from 0 (unlimited) to 35,791,394
             hours. The default value is 24 hours.

             This value applies to the length of each individual meeting in a recurring meeting
             request.

             If you want the meeting organizer to receive a reply, enter the text below: This
             text is used in a reply message sent to users who send meeting requests to
             reserve the room.

   4. When you're finished on the room mailbox properties page, select Save.

Use Outlook on the web options for the room mailbox to
change how the mailbox handles meeting requests
Users with Full Access permission to a room mailbox can use Open another mailbox in
Outlook on the web to change the scheduling settings of a room mailbox.

   1. In your Outlook on the web, select your account in the top right corner, and then select
     Open another mailbox.
   2. In the Open another mailbox dialog that opens, enter some or all of the room mailbox
     name, select Search directory, select the mailbox in the results, and then select Open.
   3. In the room mailbox in Outlook on the web, go to Settings > Options > Calendar >
     Resource scheduling.
   4. On the Resource scheduling settings page, configure the settings as described in the
     following subsections.

Scheduling options
The following settings are available in the Scheduling options section of the Resource
scheduling settings page in Outlook on the web for a room mailbox:

<!-- p.1188 -->

Automatically process meeting requests and cancellations: Meeting requests are
automatically accepted. By default, this setting is selected. Otherwise, a resource delegate
manually accepts or declines meeting requests.

Turn off reminders: Disables reminders in the room mailbox calendar. Meeting organizers
and attendees can still receive reminders.

By default, this setting isn't selected.

Maximum number of days in advance resources can be booked: A valid value is an
integer between 0 (today) and 1080 days. The default value is 180 days.
   Always decline if the end date is beyond this limit: Controls the behavior of recurring
   meetings that extend beyond the date specified by the Maximum number of days in
   advance resources can be booked value:
      Selected: Recurring meeting requests are automatically declined if the meetings
      start on or before the Maximum number of days in advance resources can be
      booked date, and the meetings extend beyond the Maximum number of days in
      advance resources can be booked date. This is the default setting.
      Not selected: Recurring meeting requests are automatically accepted if the
      meetings start on or before Maximum number of days in advance resources can
      be booked date. However, any meetings that extend beyond the Maximum
      number of days in advance resources can be booked date are automatically
      removed (no meetings can extend beyond that date).

Limit meeting duration and Maximum allowed minutes: Specifies the maximum duration
that the room can be reserved in a meeting request. A valid value is from 0 (unlimited) to
1440 minutes (24 hours). The default value is 1440 minutes.

This value applies to the length of each individual meeting in a recurring meeting request.

Allow scheduling only during working hours: Accepts or declines meeting requests that
aren't during the working hours defined for the room mailbox. By default, this setting isn't
selected, so meeting requests are allowed outside the working hours. By default, working
hours are 8:00 A.M. to 5:00 P.M. Monday through Friday. You can set the working hours
on a mailbox in Outlook on the web (formerly known as Outlook Web App or OWA) in
Settings > Options > Calendar > Personalization > Calendar appearance > Show work
week as and Set your working hours.

Allow repeating meetings: Allows or prevents recurring meetings for the room. By
default, this setting is selected, so recurring meetings are allowed.

Allow conflicts: Allow or prevent conflicting meeting requests (also known as double
booking). By default, this setting isn't selected.

<!-- p.1189 -->

     If recurring meetings are allowed on the room mailbox, this setting applies only to
     recurring meetings. Don't use Add rooms to include the room in the meeting request.
     Instead, include the room as a Required attendee in the meeting request.

        Allow up to this number of individual conflicts: When conflicts are allowed, this
        setting specifies the maximum number of conflicts for recurring meeting requests. A
        valid value is from 0 to 2147483647. The default value is 0.
           The value 0 means recurring meeting requests are denied if there are any conflicting
           reservations.
           A numerical value means recurring meeting requests are denied if the request
           conflicts with any existing reservations more than the specified number of times.

        Allow up to this percentage of individual conflicts: When conflicts are allowed, this
        setting specifies the maximum percentage of meeting conflicts for new recurring
        meeting requests. A valid value is from 0 to 100. The default value is 0.
           The value 0 means recurring meeting requests are denied if there are any conflicting
           reservations.
           A numerical value means recurring meeting requests are denied if the request
           conflicts with any existing reservations more than the specified percentage. For
           example, this setting is 10% and a recurring meeting request has 20 individual
           meetings:
           Allowed if there's a conflict two or less of the individual meetings.
           Denied if there's a conflict with three or more of the individual meetings.

Scheduling permissions

The following settings are available in the Scheduling permissions section of the Resource
scheduling settings page in Outlook on the web for a room mailbox:

     These people can schedule automatically if the resource is available: Select one of the
     following values:
        Everyone: Anyone can automatically reserve the room. If the room isn't available, the
        meeting request is automatically declined. This is the default value.
        Specific people and groups: Only the specified users and groups can automatically
        reserve the room. If the room isn't available, the meeting request is automatically
        declined. Meetings requests from other users or groups are automatically declined.
        Selecting this value without specifying the users or groups is equivalent to selecting
        Everyone.

     These users can submit a request for owner approval if the resource is available: Select
     one of the following values:

<!-- p.1190 -->

        Everyone: Anyone can request to reserve the room, but the request must be approved
        by a resource delegate (the Select delegates who can accept or decline booking
        requests setting in the EAC). If the room isn't available, the meeting request is
        automatically declined.

        Specific people and groups: Only the specified users and groups can request to
        reserve the room, but a resource delegate must approve the meeting request. If the
        room isn't available, the meeting request is automatically declined. Meetings requests
        from other users and groups are automatically declined.

        Selecting this value without specifying the users or groups is equivalent to selecting
        Everyone. By default, this value is selected, but no users or groups are selected.

     These users can schedule automatically if the resource is available and can submit a
     request for owner approval if the resource is unavailable: Select one of the following
     values:

        Everyone: Anyone can automatically reserve the room. If the room isn't available, the
        meeting request must be approved by a resource delegate (the Select delegates who
        can accept or decline booking requests setting in the EAC).

        Specific people and groups: Only the specified users and groups can request to
        reserve the room. If the room isn't available, a resource delegate must accept the
        meeting request. Meetings requests from other users and groups are automatically
        declined.

        Selecting this value without specifying the users or groups is equivalent to selecting
        Everyone. By default, this value is selected, but no users or groups are selected.

Response message
Select Add additional text to be included in responses to event invitations and enter the text
in the box.

Change other room mailbox properties
After you create a room mailbox, you can make changes and set other properties by using the
EAC or the Exchange Management Shell.

Use the EAC to change room mailbox properties
   1. In the EAC, go to Recipients > Resources.

<!-- p.1191 -->

   2. On the Resources tab, select the room mailbox, and then select    Edit.

   3. On the room mailbox properties page that opens, several tabs are available:

     The following tabs contain specific settings for room mailboxes:

           General
           Contact information
           Booking delegates and Booking options (previously described)

     The remaining tabs contain identical settings to user mailboxes. These tabs and settings
     are described in the user mailbox article:

           Email address
           MailTip
           Mailbox delegation

General tab in room mailbox properties
The following settings are available on the General tab of the mailbox properties for a room
mailbox:

     Room name: The maximum value is 64 characters.

        Tip

       Although other properties are available to describe the details of the room (for
       example, Location and Capacity), consider summarizing the important details in the
       Name value using a consistent naming convention. Users can easily see the details in
       the room name when they select the room mailbox from the address book.

     Email address: You can change this value on the Email Address tab.

     Capacity: Enter the maximum number of people who can safely occupy the room.

Select More options to view or change these other properties that appear:

     Organizational unit: The organizational unit (OU) that contains the account for the room
     mailbox. You can use Active Directory Users and Computers to move the account to a
     different OU.

     Mailbox database: The mailbox database that hosts the room mailbox. You can use
     recipients > Migration in the EAC to move the mailbox to a different database.

<!-- p.1192 -->

     Alias: When you change this value, the primary email address of the room mailbox is
     automatically updated if the mailbox is subject to email address policies.

     Hide from address lists: Select this setting to prevent the room mailbox from appearing
     in the global address lists and other address lists in your Exchange organization. If you
     select this setting, users can still send meeting requests using the email address.

     Department: Specify the department that the room is associated with. You can use this
     value to create recipient conditions for dynamic distribution groups and address lists.

     Company: Specify the company the room is associated with. You can use this value to
     create recipient conditions for dynamic distribution groups and address lists.

     Address book policy: Select the ABP that includes the room mailbox. ABPs contain a
     global address list (GAL), an offline address book (OAB), a room list (not a room list
     distribution group), and a set of address lists. To learn more, see Address book policies in
     Exchange Server.

     Custom attributes: Select      Edit to specify values for Custom Attribute 1 to Custom
     Attribute 15 on the mailbox. You can use this value to create recipient conditions for
     dynamic distribution groups and address lists.

Contact information tab in room mailbox properties
The following settings are available on the General tab of the mailbox properties for a room
mailbox:

     Location
     Phone
     Street
     City
     State/Province
     ZIP/Postal code
     Country/Region
     Notes

   Tip

  You can use the State/Province box to create recipient conditions for dynamic distribution
  groups, email address policies, or address lists.

<!-- p.1193 -->

Use the Exchange Management Shell to change room mailbox
properties
To view and change room mailbox properties, use the following cmdlets in the Exchange
Management Shell:

     Get-User and Set-User: View and set general properties such as location, department, and
     company names.
     Get-Mailbox and Set-Mailbox: View and set mailbox properties, such as email addresses
     and the mailbox database.
     Get-CalendarProcessing and Set-CalendarProcessing: View and set booking options and
     delegates.

Here are some examples of using the Exchange Management Shell to change room mailbox
properties.

This example changes the display name, the primary SMTP address (also called the default
reply address), and the room capacity. The previous primary SMTP address is kept as a proxy
address on the mailbox.

  PowerShell

  Set-Mailbox "Conf Room 123" -DisplayName "Conf Room 31/123 (12)" -EmailAddresses
  SMTP:Rm33.123@contoso.com,smtp:rm123@contoso.com -ResourceCapacity 12

This example configures room mailboxes to allow booking requests to be scheduled only
during working hours and sets a maximum duration of 9 hours.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'RoomMailbox'"
  | Set-CalendarProcessing -ScheduleOnlyDuringWorkHours $true -
  MaximumDurationInMinutes 540

This example uses the Get-User cmdlet to find all private conference room mailboxes, and then
uses the Set-CalendarProcessing cmdlet to send booking requests to a delegate named Robin
Wood to accept or decline.

  PowerShell

  Get-User -ResultSize unlimited -Filter "(RecipientTypeDetails -eq 'RoomMailbox') -
  and (DisplayName -like 'Private*')" | Set-CalendarProcessing -AllBookInPolicy
  $false -AllRequestInPolicy $true -ResourceDelegates "Robin Wood"

<!-- p.1194 -->

How do you know you successfully changed the room
mailbox properties?
To verify that you successfully changed the properties for a room mailbox, either of the
following steps:

     EAC: Go to Recipients > Resources tab. On the Resources tab, Select the mailbox, and
     then select        Edit to view the mailbox properties.

     Exchange Management Shell:
        To display information about the mailbox, replace <RoomMailboxIdentity> with the
        name, alias, user principal name (UPN), or email address of the mailbox, and then run
        the following commands:

        PowerShell

        Get-Mailbox -Identity <roomMailboxIdentity> | Format-List

        Get-CalendarProcessing -Identity <RoomMailboxIdentity> | Format-List

        Run the following command to identify the room mailboxes that can only be
        scheduled during working hours:

           PowerShell

           Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
           'RoomMailbox'" | Get-CalendarProcessing | Format-List
           Identity,ScheduleOnlyDuringWorkHours

Create room lists
Room lists are special distribution groups that contain only room mailboxes. Room mailboxes
are useful for organizing conference rooms by building.

Use the Exchange Management Shell to create a room list

   Tip

  You can create room lists in the Exchange Management Shell only. You can't create room
  lists in the EAC.

To create a room list, use the following syntax:

<!-- p.1195 -->

  PowerShell

  New-DistributionGroup -RoomList -Name <Name> [-Alias <Alias>] [-DisplayName "
  <DisplayName>"] [-PrimarySmtpAddress <EmailAddress>]

This example creates a room list named Building 32 Conference Rooms. Because we aren't
using the Alias, DisplayName, or PrimarySmtpAddress parameters, the following values are
based on the Name parameter value:

     Alias: Building32ConferenceRooms
     DisplayName: Building 32 Conference Rooms
     PrimarySmtpAddress: : Alias and domain values from the email policy. If the policy doesn't
     specify an alias, the value Building32ConferenceRooms is used.

  PowerShell

  New-DistributionGroup -RoomList -Name "Building 32 Conference Rooms"

For detailed syntax and parameter information, see New-DistributionGroup.

Use the Exchange Management Shell to add rooms to room
lists

   Tip

  You can add room mailboxes to room lists in the EAC or in PowerShell. For EAC
  instructions, see Use the EAC to change distribution group properties.

To add room mailboxes to a room list, use the following syntax:

  PowerShell

  Add-DistributionGroupMember -Identity <RoomListIdentity> -Member
  <RoomMailboxIdentity>

This example adds conference room 3223 to the building 32 room list.

  PowerShell

  Add-DistributionGroupMember -Identity "Building 32 Conference Rooms" -Member
  confroom3223@contoso.com

<!-- p.1196 -->

For detailed syntax and parameter information, see Add-DistributionGroupMember.

Use the Exchange Management Shell to convert a distribution
group to a room list

   Tip

  You can convert distribution groups to room lists in the Exchange Management Shell only.
  You can't convert distribution groups to room lists in the EAC.

If you previously created regular distribution groups that contain room mailboxes, you can
convert them to room lists by using the following syntax:

  PowerShell

  Set-DistributionGroup -Identity <GroupIdentity> -RoomList

This example converts the specified distribution group to a room list.

  PowerShell

  Set-DistributionGroup -Identity "Building 34 Conference Rooms" -RoomList

For detailed syntax and parameter information, see Set-DistributionGroup.

How do you know you successfully created, updated, or
converted a room list?
To verify you successfully created, updated, or converted a room list, do any of the following
steps:

     In the Exchange Management Shell, run the following commands to return all room lists
     and their members:

         PowerShell

         $RL = Get-DistributionGroup -ResultSize Unlimited -RecipientTypeDetails
         RoomList

         $RL | foreach {Get-DistributionGroup -Identity $_.Identity | Format-Table
         Name,DisplayName,PrimarySmtpAddress; Get-DistributionGroupMember -Identity
         $_.Identity}

<!-- p.1197 -->

In the Exchange Management Shell, replace <RoomListIdentity> with the Name, Alias, or
Email address of the room list, and then run the following commands to verify the details
of the room list and the room list members:

  PowerShell

  Get-DistributionGroup -Identity <RoomListIdentity> | Format-List

  Get-DistributionGroupMember -Identity <RoomListIdentity>

<!-- p.1198 -->

Manage equipment mailboxes in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016      2019    Subscription Edition

   Tip

  This article applies to on-premises Exchange servers. The cloud version of this article is
  available at Manage resource mailboxes in Exchange Online.

An equipment mailbox is one of the available resource mailbox types in Exchange. Unlike room
mailboxes, equipment mailboxes aren't assigned to a physical location, such as a portable
computer, projector, microphone, or a company car. Users can easily reserve equipment by
including the equipment mailbox in meeting requests.

You can use the Exchange admin center (EAC), the Exchange Management Shell, and Outlook
on the web (formerly known as Outlook Web App or OWA) to manage equipment mailboxes.

To allow users to manage the calendar in an equipment mailbox (for example, an executive
assistant who needs to rearrange reservations), use the instructions in Manage permissions for
recipients. After a user gets permission to access the equipment mailbox, they can open the
mailbox using the instructions in Open and use a shared mailbox in Outlook for Windows         .

   Tip

  Never set an equipment mailbox as the organizer of a meeting. Include equipment
  mailboxes only in the Attendee or Location fields in the meeting request.

To learn more about the types of recipients in Exchange, see Recipients.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.
      To open the Exchange admin center (EAC), see Exchange admin center in Exchange
      Server. To open the Exchange Management Shell, see Open the Exchange Management
      Shell.
      You need to be assigned permissions before you can perform this procedure or
      procedures. See the "Recipient Provisioning Permissions" section in the Recipients
      Permissions article.

<!-- p.1199 -->

     If you're running Exchange Server in a hybrid scenario, be sure to create equipment
     mailboxes in the appropriate place. Create equipment mailboxes for your on-premises
     organization in Exchange Server, and create equipment mailboxes for your cloud
     organization in Exchange Online.
     We don't recommend using Full Access permissions to manage the equipment mailbox
     calendar. Instead, share the equipment calendar with the user who needs to manage
     meetings. After the user accepts the sharing invitation, they can manage meetings in the
     equipment calendar. If the equipment calendar is shared with Delegate permissions, the
     user also receives copies of all meeting requests sent to the equipment mailbox in their
     own mailbox.
     Sharing an equipment mailbox calendar doesn't prevent the calendar from having the
     Accept or decline booking requests automatically setting enabled. If the equipment
     calendar is shared with Accept or decline booking requests automatically enabled,
     meeting requests are accepted by default. But users with Editor or Delegate permissions
     to the equipment calendar can change the response.
     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum .

Create an equipment mailbox

Use the EAC to create equipment mailboxes
To create an equipment mailbox in the EAC, do the following steps:

   1. In the EAC, go to Recipients > Resources tab.

   2. On the Resources tab, select   New > Equipment mailbox.

   3. On the New equipment mailbox page that opens, configure the following settings:

          Equipment name: Enter a unique, descriptive name. This value is required and it
          can't exceed 64 characters.

        Tip

<!-- p.1200 -->

           Although other properties are available to describe the details of the equipment (for
           example, Location and Capacity), consider summarizing the important details in the
           Name value using a consistent naming convention. Users can easily see the details in
           the equipment name when they select the equipment mailbox from the address
           book.

              Alias: A unique value that's use on the left side of the @ symbol in the email
              address. This value is required.
              Organizational unit: Select Browse to specify the location in Active Directory where
              the equipment mailbox object is created.
              Select More options to reveal the following settings:
                   Mailbox database: Select Browse to specify the mailbox database where the
                   equipment mailbox is created.
                   Address book policy: Select the ABP that includes the equipment mailbox. ABPs
                   contain a global address list (GAL), an offline address book (OAB), a room list (not
                   a room list distribution group), and a set of address lists. To learn more, see
                   Address book policies in Exchange Server.

   4. When you're finished on the New equipment mailbox page, select Save to create the
     equipment mailbox.

After you create an equipment mailbox, you can Change how an equipment mailbox handles
meeting requests (including whether it responds automatically or someone needs to decide
what to do). By default, the equipment mailbox has the following settings:

     Automatically accept or decline meeting requests (depending on whether the requests
     conflict with any existing meetings on the calendar).
     Allow recurring meetings.
     Allow meetings up to 24 hours long up to 180 days from today (and decline longer
     meeting requests).

To change other mailbox settings, go to the Change other equipment mailbox properties
section.

Use the Exchange Management Shell to create equipment
mailboxes
To create an equipment mailbox in the Exchange Management Shell, use the following syntax:

  PowerShell
