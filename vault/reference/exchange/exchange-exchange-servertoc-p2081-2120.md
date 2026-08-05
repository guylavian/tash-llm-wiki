---
title: "Exchange Server — pages 2081-2120"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2081-2120
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2081-2120
family: exchange
documentKind: "doc"
abstract: "PowerShell Disable-MailPublicFolder -Identity \"\\Marketing\\Reports\" For detailed syntax and parameter information, see Disable-MailPublicFolder. Allow anonymous users to send email to a mail- enabled public folder You can use either Outlook or the Exchange Management Shell to set"
---

# Exchange Server — pages 2081-2120

<!-- p.2081 -->

  PowerShell

  Disable-MailPublicFolder -Identity "\Marketing\Reports"

For detailed syntax and parameter information, see Disable-MailPublicFolder.

Allow anonymous users to send email to a mail-
enabled public folder
You can use either Outlook or the Exchange Management Shell to set permissions on a public
folder's Anonymous account. You can't use the EAC to set permissions on the Anonymous
account.

Use Outlook to set permissions for the Anonymous account

   1. Open Outlook using an account that's been granted Owner permissions on the email-
     enabled public folder you want anonymous users to send mail to.

   2. Navigate to Public folders - <user's name>.

   3. Navigate to the public folder you want to change.

   4. Right-click on the public folder, click Properties and then select the Permissions tab.

   5. Select the Anonymous account, select Create items under Write, and then click OK.

Use the Exchange Management Shell to set permissions for the Anonymous account

This example sets the CreateItems permission for the Anonymous account on the "Customer
Feedback" mail-enabled public folder.

  PowerShell

  Add-PublicFolderClientPermission "\Customer Feedback" -AccessRights CreateItems -
  User Anonymous

For detailed syntax and parameter information, see Add-PublicFolderClientPermission.

<!-- p.2082 -->

View statistics for public folders and public
folder items
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

You can use the Exchange Management Shell to retrieve statistics about a public folder, such as
the display name, creation time, last user modified time, and item size. You can use this
information to make decisions about deleting or retaining public folders.

  ７ Note

  While you can view some of the quota and usage information in the Exchange admin
  center (EAC), this information is incomplete, and we recommend that you use the
  Exchange Management Shell to view public folder statistics. To view quota and usage
  information for public folders by navigating to Public Folders > Edit     > Mailbox usage.

For additional management tasks related to public folders, see Public Folder Procedures in
Exchange Online.

What do you need to know before you begin?
     Estimated time to complete: 1 minute.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Public folders" entry in the
     Sharing and collaboration permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to retrieve
public folder statistics

<!-- p.2083 -->

This example returns the statistics for the public folder Marketing with a piped command to
format the list.

  PowerShell

  Get-PublicFolderStatistics -Identity \Marketing | Format-List

  ７ Note

  The value for the Identity parameter must include the path to the public folder. For
  example, if the public folder Marketing existed under the parent folder Business, you
  would provide the following value: \Business\Marketing

For detailed syntax and parameter information, see Get-PublicFolderStatistics.

Note that some parameters and settings might be available only in Exchange Online or only in
Exchange Server.

Use the Exchange Management Shell to view
statistics for public folder items
You can view the following information about items within a public folder:

     Type of item

     Subject

     Last user modification time

     Creation time

     Attachments

     Message size

This example returns default statistics for all items in the public folder Pamphlets under the
path \Marketing\2013. Default information includes item identity, creation time, and subject.

  PowerShell

  Get-PublicFolderItemStatistics -Identity "\Marketing\2013\Pamphlets"

<!-- p.2084 -->

This example returns additional information about the items within the public folder
Pamphlets, such as subject, last modification time, creation time, attachments, message size,
and the type of item. It also includes a piped command to format the list.

  PowerShell

  Get-PublicFolderItemStatistics -Identity "\Marketing\2010\Pamphlets" | Format-List

For detailed syntax and parameter information, see Get-PublicFolderItemStatistics.

Note that some parameters and settings might be available only in Exchange Online or only in
Exchange Server.

Use the Exchange Management Shell to export the
output of the Get-PublicFolderItemStatistics
cmdlet to a .csv file
This example exports the output of the cmdlet to the PFItemStats.csv file that includes the
following information for all items within the public folder \Marketing\Reports:

     Subject of the message ( Subject )

     Date and time that the item was last modified ( LastModificationTime )

     Whether the item has attachments ( HasAttachments )

     Type of item ( ItemType)

     Size of the item ( MessageSize )

  PowerShell

  Get-PublicFolderItemStatistics -Identity "\Marketing\Reports" | Select
  Subject,LastModificationTime,HasAttachments,ItemType,MessageSize | Export-CSV
  C:\PFItemStats.csv

For detailed syntax and parameter information, see Get-PublicFolderItemStatistics.

<!-- p.2085 -->

Shared mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

A shared mailbox is a mailbox that multiple users can use to read and send email messages.
Shared mailboxes can also be used to provide a common calendar, allowing multiple users to
schedule and view vacation time or work shifts.

Why set up a shared mailbox?

      Provides a generic email address (for example, info@contoso.com or
      sales@contoso.com), that customers can use to inquire about your company.

      Allows departments that provide centralized services to employees (for example, help
      desk, human resources, or printing services), to respond to employee questions.

      Allows multiple users to monitor and reply to email sent to an email address (for example,
      an address used specifically by the help desk).

What are shared mailboxes?
A shared mailbox is a type of user mailbox that doesn't have its own username and password.
As a result, users can't log into them directly. To access a shared mailbox, users must first be
granted Send As or Full Access permissions to the mailbox. Once that's done, users sign into
their own mailboxes and then access the shared mailbox by adding it to their Outlook profile.
In Exchange 2003 and earlier, shared mailboxes were just a regular mailbox to which an
administrator could grant delegate access. Beginning in Exchange 2007, shared mailboxes
became their own recipient type:

      RecipientType: UserMailbox

      RecipientTypeDetails: SharedMailbox

In previous version of Exchange, creating a shared mailbox was a multi-step process in which
you had to use the Exchange Management Shell to complete some of the tasks. In Exchange
2013 and later, you can use the Exchange admin center (EAC) to create a shared mailbox in one
step. For details, see Create shared mailboxes in the Exchange admin center. In fact, the EAC
has a feature area devoted entirely to shared mailboxes. Just navigate to Recipients > Shared
mailboxes to view all the management tasks for shared mailboxes.

You can use the following permissions with a shared mailbox.

<!-- p.2086 -->

     Full Access: The Full Access permission lets a user log into the shared mailbox and act as
     the owner of that mailbox. While logged in, the user can create calendar items; read, view,
     delete, and change email messages; create tasks and calendar contacts. However, a user
     with Full Access permission can't send email from the shared mailbox unless they also
     have Send As or Send on Behalf permission.

     Send As: The Send As permission lets a user impersonate the shared mailbox when
     sending mail. For example, if Kweku logs into the shared mailbox Marketing Department
     and sends an email, it will look like the Marketing Department sent the email.

     Send on Behalf: The Send on Behalf permission lets a user send email on behalf of the
     shared mailbox. For example, if John logs into the shared mailbox Reception Building 32
     and sends an email, it look like the mail was sent by "John on behalf of Reception
     Building 32". You can't use the EAC to grant Send on Behalf permissions, you must use
     Set-Mailbox cmdlet with the GrantSendonBehalf parameter.

  ７ Note

  A shared mailbox is not designed for direct logon. The user account for the shared
  mailbox itself should stay in a Disabled (or "disconnected") state.

Converting shared mailboxes
In previous versions of Exchange, you could use a regular mailbox as a delegated mailbox. If
you have delegated mailboxes, you can use the Exchange Management Shell to convert those
delegate mailboxes to shared mailboxes. For details, see Convert a mailbox in Exchange Server.

<!-- p.2087 -->

Create shared mailboxes in the Exchange
admin center
Article • 04/30/2025

APPLIES TO:        2016       2019   Subscription Edition

If your organization uses a hybrid Exchange environment, you should use the on-premises
Exchange admin center (EAC) to create and manage shared mailboxes. The Exchange admin
center (EAC) is the single unified management console that allows for managing both your on-
premises and Exchange Online organizations and allows you to connect and configure features
for both organizations. For more information, see Hybrid management in Exchange hybrid
deployments.

Use the EAC to create a shared mailbox
For information on limitations, automapping, and getting your users set up, see Create a
shared mailbox.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "User mailboxes" entry in the Recipients Permissions
topic.

   1. Go to Recipients > Shared > Add      .

   2. Fill-in the required fields:

            Display name

            Email address

   3. To grant Full Access or Send As permissions, click Add   , and then select the users you
      want to grant permissions to. You can use the CTRL key to select multiple users. Confused
      about which permission to use? See Which permissions should you use? later in this topic.

         ７ Note

         The Full Access permission allows a user to open the mailbox as well as create and
         modify items in it. The Send As permission allows anyone other than the mailbox
         owner to send email from this shared mailbox. Both permissions are required for
         successful shared mailbox operation.

   4. Click Save to save your changes and create the shared mailbox.

<!-- p.2088 -->

Use the EAC to edit shared mailbox delegation
   1. Go to Recipients > Shared > Edit    .

   2. Click Mailbox delegation

   3. To grant or remove Full Access and Send As permissions, click Add    or Remove         and
     then select the users you want to grant permissions to.

        ７ Note

        The Full Access permission allows a user to open the mailbox as well as create and
        modify items in it. The Send As permission allows anyone other than the mailbox
        owner to send email from this shared mailbox. Both permissions are required for
        successful shared mailbox operation.

   4. Click Save to save your changes.

Use the Exchange Management Shell to create a
shared mailbox
This example creates the shared mailbox Sales Department and grants Full Access and Send on
Behalf permissions for the security group MarketingSG. Users who are members of the security
group will be granted the permissions to the mailbox.

  ７ Note

  This example assumes that you've already created the security group MarketingSG and
  that security group is mail-enabled. See Manage mail-enabled security groups in
  Exchange Server.

  PowerShell

  New-Mailbox -Shared -Name "Sales Department" -DisplayName "Sales Department" -
  Alias Sales | Set-Mailbox -GrantSendOnBehalfTo MarketingSG | Add-MailboxPermission
  -User MarketingSG -AccessRights FullAccess -InheritanceType All

For detailed syntax and parameter information, see New-Mailbox.

Which permissions should you use?

<!-- p.2089 -->

You can use the following permissions with a shared mailbox.

     Full Access: The Full Access permission lets a user log into the shared mailbox and act as
     the owner of that mailbox. While logged in, the user can create calendar items; read, view,
     delete, and change email messages; create tasks and calendar contacts. However, a user
     with Full Access permission can't send email from the shared mailbox unless they also
     have Send As or Send on Behalf permission.

     Send As: The Send As permission lets a user impersonate the shared mailbox when
     sending mail. For example, if Kweku logs into the shared mailbox Marketing Department
     and sends an email, it will look like the Marketing Department sent the email.

     Send on Behalf: The Send on Behalf permission lets a user send email on behalf of the
     shared mailbox. For example, if John logs into the shared mailbox Reception Building 32
     and sends an email, it look like the mail was sent by "John on behalf of Reception
     Building 32". You can't use the EAC to grant Send on Behalf permissions, you must use
     Set-Mailbox cmdlet with the GrantSendonBehalf parameter.

More information
For information about keyboard shortcuts that may apply to the procedures in this topic, see
Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.2090 -->

Email addresses and address books in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019        Subscription Edition

Exchange uses address books to organize and store email address information for recipients in
the organization. The topics that will help you learn about and configure email addresses and
address books in Exchange Server are described in the following table.

                                                                                                ﾉ   Expand table

 Key               Description                                                                  Topic
 terminology

 Address book      The global address list (GAL) is the master list of all recipients in your   Address book
 policies          Exchange organization. Address book policies (ABPs) provide a                policies in
                   simpler mechanism for GAL segmentation in organizations that                 Exchange Server
                   require multiple GALs. An ABP defines a GAL, an offline address
                   book (OAB), a room list, and one or more address lists. You can then
                   assign the ABP to users.

 Address lists     An address list is a subset of a GAL. Each address list is a dynamic         Address lists in
                   collection of one or more types recipients. You can use address lists        Exchange Server
                   to help users find the recipients and resources that they need.

 Details           Details templates control the appearance of recipient properties that        Details
 templates         are displayed in address lists in Outlook.                                   Templates

 Email address     Email address policies are the rules that create email addresses for         Email address
 policies          Exchange recipients.                                                         policies in
                                                                                                Exchange Server

 Hierarchical      The hierarchical address book (HAB) presents recipients in the GAL           Hierarchical
 address books     by using your organization's unique business structure (for example,         Address Books
                   seniority or management hierarchy), which provides an efficient
                   method for locating internal recipients.

 Offline           An offline address book (OAB) is a collection of address lists that can      Offline address
 address books     be downloaded and used in Outlook by users that are disconnected             books in
                   from the Exchange organization.                                              Exchange Server

<!-- p.2091 -->

Email address policies in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Email address policies define the rules that create email addresses for recipients in your
Exchange organization. Email address policies in Exchange Server 2016 and Exchange Server
2019 are basically unchanged from Exchange Server 2010.

The SMTP domains that are available to use in email address policies are defined by the
accepted domains that are configured in the Exchange organization (specifically, authoritative
domains and internal relay domains). For more information about accepted domains, see
Accepted domains in Exchange Server.

The basic components of an email address policy are:

      Email address templates: Define the email address format for the recipients (for example
      <firstname>@contoso.com or <lastname>.<firstname>@contoso.com ).

      Recipient filter: Specifies the recipients whose email addresses are configured by the
      policy.

      Priority: Specifies the order to apply the email address policies (important if a recipient is
      identified by more than one policy).

To configure email address policies, see Procedures for email address policies in Exchange
Server.

Email address templates
An email address template contains the address type and the address format. An email
address policy can contain multiple email address templates. One template must define the
primary (reply) SMTP email address, and there can be only one primary SMTP email address
defined in the policy (it's the Reply-To: email address for recipients). Other email address
templates in the policy define the additional or proxy addresses for recipients.

Address types
Although you'll primarily use SMTP email addresses in email address policies, other email
address types are available. The valid address type values are:

      SMTP

<!-- p.2092 -->

     GWISE: Novell GroupWise. By default, looks for the missing
     %ExchangeInstallPath%Mailbox\address\gwise\amd64\gwxpxgen.dll file to validate the

     email address format.

     NOTES: Lotus Notes. By default, uses the included
     %ExchangeInstallPath%Mailbox\address\notes\amd64\ntspxgen.dll file to validate the

     email address format.

     X400: By default, uses the included
     %ExchangeInstallPath%Mailbox\address\notes\amd64\x400prox.dll file to validate the

     email address format.

Notes:

     In the Exchange Management Shell, the value SMTP specifies the primary email address,
     and the value smtp specifies additional (proxy) addresses.

     In the EAC, only the Make this format the reply email address check box controls
     whether the email address is the primary address or a proxy address. It doesn't matter
     whether you type SMTP or smtp in the Enter a custom address type field. However, in the
     list of email address templates in the policy, the EAC shows the value SMTP (bold and
     uppercase) for the primary address, and smtp (not bold and lowercase) for proxy
     addresses.

     The types of email addresses that you can configure in a email address policy are limited
     compared to those you can configure on individual recipients.

     All non-SMTP email addresses are considered custom address types. Exchange doesn't
     provide unique dialog boxes or property pages for X.400, Novell GroupWise, or Lotus
     Notes email address types. Non-SMTP email addresses require the appropriate .dll files.

Address formats
An SMTP email address uses the syntax chris@contoso.com , where the value chris is the local
part of the email address, and the value contoso.com is the SMTP domain (also known as the
address space or name space). The available SMTP domain values are determined by the
accepted domains that are configured for your organization.

You can use email address policies to assign multiple SMTP email addresses to recipients by
using different combinations of the local part and domain values. However, only one SMTP
email address in a policy can be configured as the primary address.

<!-- p.2093 -->

All SMTP email address formats in the Exchange Management Shell, or custom SMTP email
address formats in the EAC require you to use variables to define the local part of the email
address. These variables are described in the following table:

                                                                                              ﾉ   Expand table

 Variable   Value

 %d         Display name

 %g         Given name (first name)

 %i         Middle initial

 %m         Exchange alias

 %rxy       Replace all occurrences of x with y

 %rxx       Remove all occurrences of x

 %s         Surname (last name)

 %ng        The first n letters of the first name. For example, %2g uses the first two letters of the first name.

 %ns        The first n letters of the last name. For example, %2s uses the first two letters of the last name.

In addition to variables, you can also use US ASCII text characters that are allowed in Exchange
email addresses (for example, periods ( . ) or underscores ( _ ). Note that each period needs to
be surrounded by other valid characters (for example %g.%s ).

In the EAC, you can selected from a short list of precanned SMTP email address formats. These
address formats are described in the following table, where the example user is named
Elizabeth Brunner, and the domain is contoso.com:

                                                                                              ﾉ   Expand table

 Example                                          Exchange Management Shell equivalent

 <alias>@contoso.com                              %m@contoso.com

 elizabeth.brunner@contoso.com                    %g.%s@contoso.com

 ebrunner@contoso.com                             %1g%s@contoso.com

 elizabethb@contoso.com                           %g%1s@contoso.com

 brunner.elizabeth@contoso.com                    %s.%g@contoso.com

 belizabeth@contoso.com                           %1s%g@contoso.com

<!-- p.2094 -->

 Example                                     Exchange Management Shell equivalent

 brunnere@contoso.com                        %s%1g@contoso.com

Recipient filters for email address policies
Recipient filters identify the recipients that the email address policy applies to. There are two
basic options: precanned recipient filters and custom recipient filters. These are basically the
same recipient filtering options that are used by dynamic distribution groups and address
books. The following table summarizes the differences between the two filtering methods.

                                                                                       ﾉ     Expand table

 Recipient     User interface       Filterable recipient properties       Filter operators
 filtering
 method

 Precanned     Exchange admin       Limited to:                           Property values require an
 recipient     center (EAC) and           Recipient type (All recipient   exact match. Wildcards and
 filters       the Exchange               types or any combination        partial matches aren't
               Management Shell           of user mailboxes, resource     supported. For example,
                                          mailboxes, mail contacts,       "Sales" doesn't match the
                                          mail users, and groups)         value "Sales and Marketing".
                                          Company                         Multiple values of the same
                                          Custom Attribute 1 to 15        property always use the or
                                          State or Province               operator. For example,
                                          Department                      "Department equals Sales or
                                                                          Department equals
                                                                          Marketing".

                                                                          Multiple properties always use
                                                                          the and operator. For example,
                                                                          "Department equals Sales and
                                                                          Company equals Contoso".

 Custom        Exchange             You can use virtually any available   You use OPATH filter syntax to
 recipient     Management Shell     recipient attributes.                 specify any available Windows
 filters       only                                                       PowerShell filter operators.
                                                                          Wildcards and partial matches
                                                                          are supported.

Notes:

     You can't used precanned filters and customized filters at the same time.

<!-- p.2095 -->

      The recipient's location in Active Directory (the organizational unit or container) is
      available in both precanned and custom recipient filters.

      If you create an email address policy in the Exchange Management Shell that uses custom
      recipient filters, you can't edit the recipient filters in the EAC.

      You can prevent individual recipients from being affected by email address policies. For
      example:

         In the EAC, in the properties of the recipient, on the Email address tab, clear the check
         box: Automatically update email addresses based on the email address policy
         applied to this recipient.

         In the Exchange Management Shell, set the EmailAddressPolicyEnabled parameter to
         the value $false on the recipient management cmdlet (for example, Set-Mailbox or
         Set-DistributionGroup).

Priority of email address policies
If a recipient is identified by multiple email address policies, the recipient's email addresses are
only configured by the first email address policy that's evaluated. You configure the order that
the policies are evaluated by using the priority of the policy. A lower priority number indicates
a higher priority, higher priority policies are evaluated first, and the default email address policy
is always evaluated last. You assign a higher priority (lower number) to policies that use the
most specific or restrictive recipient filters.

Here are some other issues to consider:

      A recipient can only be affected by one email address policy. After the recipient is
      matched by the filtering properties of the policy, all other policies are ignored.

      All email address policies, including policies that have never been applied, are evaluated
      based on priority. For example, if you have a priority 1 policy and a priority 2 policy that
      both identity a recipient, the match in the first policy prevents the second policy from

<!-- p.2096 -->

      updating the recipient's email addresses, even if the first policy has never been applied to
      the recipient.

Default email address policy
Exchange setup creates a default email address policy that applies email addresses to all
recipients in your organization. The properties of the default email address policy are described
in the following list:

      Name: Default Policy

      Priority: Lowest (all other email address policies are evaluated before the default policy).

      Email address format

           Type: SMTP (primary email address)

           Domain: <alias>@<ADForestRootFQDN> . This domain value is used because it's the first
           accepted domain in the Exchange organization.

      Apply to: All recipient types.

You can't delete the default email address policy, and you can't designate another policy as the
default. You can modify some properties of the default policy, but the modification options are
limited:

      You can't filter recipients by type or properties (applies to all recipient types).

      You can't change the name or priority of the policy.

      You can fully customize the email address templates in the policy (modify, add, or remove
      templates). For more information, see Modify email address policies.

Apply email address policies
After you create or modify an email address policy in the EAC or the Exchange Management
Shell, the policy needs to be applied to the affected recipients.

If the updates affect a large number of recipients (our recommendation is more than 3000),
you should use the Exchange Management Shell to apply the updates to the affected
recipients. For more information, see Apply email address policies to recipients.

<!-- p.2097 -->

Procedures for email address policies in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

Email address policies assign email addresses to recipients in your Exchange organization. You
use the Exchange admin center (EAC) or the Exchange Management Shell to configure email
address policies in Exchange Server.

For more information about email address policies, see Email address policies in Exchange
Server.

What do you need to know before begin?
      Estimated time to complete each procedure: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Email address policies" entry in
      the Email addresses and address books in Exchange Server topic.

      The procedures in this topic primarily focus on SMTP email addresses in email address
      policies, but other address types are available. For more information, see Address types.

      Before you can use an SMTP domain in an email address policy, you need to configure
      the domain as an accepted domain (specifically, an authoritative domain or internal relay
      domain). For more information, see Accepted domains in Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forum at: Exchange
  Server .

Create email address policies

<!-- p.2098 -->

After you create an email address policy, you need to apply the policy to recipients. For more
information, see the Apply email address policies to recipients section in this topic.

Use the EAC to create email address policies
   1. In the EAC, go to Mail flow > Email address policies, and then click Add        .

   2. In New Email address policy windows that opens, configure the following settings:

           Policy name: Enter a unique, descriptive name for the policy.

           Email address format: Click Add (      ) to configure an email address template. After
           you add the first template to define the primary SMTP email address, you can add
           additional templates for proxy email addresses (SMTP or otherwise), or you can click
           Edit (   ) to modify an existing template. For details about the settings that are
           available, see the Email address format window in the EAC section in this topic.

           You can also click Remove ( ) to delete existing templates.

     Notes:

           The first SMTP email address template that you create here defines the primary
           (Reply-To:) SMTP email address. This template has the Type value SMTP (bold and
           uppercase), while other SMTP templates for proxy addresses have the Type value
           smtp (not bold and lowercase).

           You can't delete the email address template that defines the primary SMTP email
           address in the policy. Instead, you can add or modify another template, configure it
           to as the primary email address, and then delete the original template.

           Run this policy in this sequence with other policies: The value that you can select
           here depends on how many other email address policies you've manually created.
           For example, for the first email address policy that you create, the only available
           value is 1. If you create another policy, you can select 1 or 2. Remember, the first
           email address policy that identifies a recipient configures the recipient's email
           addresses. All other policies are ignored, even if the first policy is unapplied and
           can't configure the recipient's email addresses.

           For details about the recipient filters that are available here, see the Recipient filters
           in the EAC section in this topic.

   3. When you're finished, click Save. You'll receive a warning message that tells you to click
     Apply in the details pane to apply the policy to recipients. For more information, see the
     Apply email address policies to recipients section in this topic.

<!-- p.2099 -->

Use the Exchange Management Shell to create email address
policies
An email address policy in the Exchange Management Shell requires a recipient filter, and one
or more email address templates. For details about recipient filters, see the Recipient filters in
the Exchange Management Shell section in this topic.

Email address templates use the syntax <Type>:<AddressFormat> :

      <Type> : A valid email address type as described in Address types. For example, SMTP for

     the primary email address, and smtp for proxy addresses.

      <AddressFormat> : For SMTP email addresses, a domain or subdomain that's configured as

     accepted domain (authoritative or internal relay), and valid variables and ASCII text
     characters as described in Address formats. For example: <alias>@contoso.com requires
     the value %m@contoso.com , and <firstname>.<lastname>@contoso.com requires the value
      %g.%s@contoso.com .

To create an email address policy, use the following syntax:

  PowerShell

  New-EmailAddressPolicy -Name "<Policy Name>" <Precanned recipient filter | Custom
  recipient filter> [-RecipientContainer <OrganizationalUnit>] [-Priority
  <AllowedInteger>] -EnabledEmailAddressTemplates "SMTP:
  <PrimaryEmailAddressFormat>","smtp:<ProxyEmailAddress1>","smtp:
  <ProxyEmailAddress2>"...

This example creates an email address policy with a precanned recipient filter:

     Name: Southeast Offices

     Precanned recipient filter: All users with mailboxes where the State or province value is
     GA, AL, or LA (Georgia, Alabama, or Louisiana).

     Primary SMTP email address: <last name>.<first two letters of the first
     name>@contoso.com

     Additional proxy email addresses: <last name>.<first two letters of the first
     name>@contoso.net

     Priority: n+1, where n is the number of manually created email address policies that
     already exist (we didn't use the Priority parameter, and the default value is n+1).
     Remember, the first email address policy that identifies a recipient configures the

<!-- p.2100 -->

     recipient's email addresses. All other policies are ignored, even if the first policy is
     unapplied and can't configure the recipient's email addresses.

  PowerShell

  New-EmailAddressPolicy -Name "Southeast Offices" -IncludedRecipients MailboxUsers
  -ConditionalStateorProvince "GA","AL","LA" -EnabledEmailAddressTemplates
  "SMTP:%s%2g@southeast.contoso.com","smtp:%s%2g@southeast.contoso.net"

This example creates an email address policy with a custom recipient filter:

     Name: Northwest Executives

     Custom recipient filter: All users with mailboxes where the Title value contains Director
     or Manager, and the State or province value is WA, OR, or ID (Washington, Oregon, or
     Idaho).

     Primary SMTP email address: <first two letters of the first name><last
     name>@contoso.com

     Additional proxy email addresses: None

     Priority: 2

  PowerShell

  New-EmailAddressPolicy -Name "Northwest Executives" -RecipientFilter "
  (RecipientType -eq 'UserMailbox') -and (Title -like '*Director*' -or Title -like
  '*Manager*') -and (StateOrProvince -eq 'WA' -or StateOrProvince -eq 'OR' -or
  StateOrProvince -eq 'ID')" -EnabledEmailAddressTemplates "SMTP:%2g%s@contoso.com"
  -Priority 2

Notes:

     Typically, you use the EnabledEmailAddressTemplates parameter to define the primary
     SMTP email address and one or more proxy addresses (SMTP or otherwise). However, if
     you're only going to define the primary SMTP email address and no additional proxy
     addresses, you can use the EnabledPrimarySMTPAddressTemplate parameter instead. This
     parameter doesn't require the SMTP: prefix, and you can't use this parameter with the
     EnabledEmailAddressTemplates parameter.

     The EnabledEmailAddressTemplates parameter requires at least one template with the
     <Type> value SMTP (to define the primary SMTP email address). After that, if you don't

     include a <Type> prefix for a template, the value smtp (an SMTP proxy address) is
     assumed.

<!-- p.2101 -->

For detailed syntax and parameter information, see New-EmailAddressPolicy.

How do you know this worked?
To verify that you've successfully created an email address policy, use either of the following
procedures:

     In the EAC, go to Mail flow > Email address policies, verify that the policy is listed, and
     the details are correct. Select the policy and click Edit (   ) to view details that aren't
     displayed in the list view.

     In the Exchange Management Shell, run the following command to verify the property
     values:

        PowerShell

        Get-EmailAddressPolicy | Format-List
        Name,Priority,Enabled*,RecipientFilterType,RecipientContainer,RecipientFilter
        ,IncludedRecipients,Conditional*

Modify email address policies
     For the default email address policy, you can't modify the name, priority, or recipient filter
     settings. You can only modify the email address templates.

     After you modify an email address policy, you need to apply the policy to recipients. For
     more information, see the Apply email address policies to recipients section in this topic.

     If you created an email address policy in the Exchange Management Shell that uses a
     custom recipient filter, you can't modify the recipient filter in the EAC. You need to use
     the Exchange Management Shell.

     You can't use the EAC or the Exchange Management Shell to replace a custom recipient
     filter with a precanned recipient filter or vice-versa in an existing email address policy.

<!-- p.2102 -->

Modify email address policies in the EAC
The same settings are available as when you created the policy, although the settings are now
located on separate tabs.

   1. In the EAC, go to Mail flow > Email address policies, select the policy from the list, and
     then click Edit (      ).

   2. Configure the settings on the following tabs:

           General

           Policy name: A unique, descriptive name for the policy.

           Run this policy in this sequence with other policies: Remember, the first email
           address policy that identifies a recipient configures the recipient's email addresses.
           All other policies are ignored, even if the first policy is unapplied and can't configure
           the recipient's email addresses.

           Email address format: For details about the settings that are available when you
           click Add (      ) or Edit (   ), see the Email address format window in the EAC section
           in this topic.

           You can also click Remove ( ) to delete existing email address templates.

     Notes:

           The Type value SMTP (bold and uppercase) indicates the primary SMTP email
           address, and the value smtp (not bold and lowercase) indicates a proxy address.

           You can't delete the email address template that defines the primary SMTP email
           address in the policy. Instead, you can add or modify another template, configure it
           to define the primary email address, and then delete the original template.

           Apply to: For details about the recipient filters that are available here, see the
           Recipient filters in the EAC section in this topic.

           Note: Even if you configured a custom recipient filter in the Exchange Management
           Shell, you can still select Preview recipients the policy applies to here.

   3. When you're finished, click Save. You'll receive a warning message that tells you to click
     Apply in the details pane to apply the policy to recipients. For more information, see the
     Apply email address policies to recipients section in this topic.

<!-- p.2103 -->

Modify email address policies in the Exchange Management
Shell
The same basic settings are available as when you created the policy. For more information,
see the Use the Exchange Management Shell to create email address policies section in this
topic.

To modify an existing email address template, use the following syntax:

  PowerShell

  Set-EmailAddressPolicy -Identity <EmailAdressPolicyIdentity> [-Name <Name>]
  [<Precanned recipient filter | Custom recipient filter>] [-RecipientContainer
  <OrganizationalUnit>] [-Priority <AllowedInteger>] [-EnabledEmailAddressTemplates
  <"Type1:AddressFormat1","Type2:AddressFormat2"...] [-DisabledEmailAddressTemplates
  <"Type1:AddressFormat1","Type2:AddressFormat2"... | $null>]

When you modify the Conditional parameter values, you can use the following syntax to add or
remove values without affecting other existing values: @{Add="<Value1>","<Value2>"...;
Remove="<Value1>","<Value2>"...} .

This example modifies the existing email address policy named Southeast Executives by adding
the State or province value TX (Texas) to the precanned recipient filter.

  PowerShell

  Set-EmailAddressPolicy -Identity "Southeast Executives" -
  ConditionalStateOrProvince @{Add="TX"}

The DisabledEmailAddressTemplates parameter specifies inactive email address templates that
are no longer used in the policy, and uses the same syntax as the
EnabledEmailAddressTemplates parameter (except that DisabledEmailAddressTemplates can't
contain a primary SMTP email address). Typically, this property is only populated if you've
migrated from a previous version of Exchange. However, if a domain is specified in this
property, you can't remove the corresponding accepted domain.

This example clears the disabled email address templates from the email address policy named
Contoso Executives.

  PowerShell

  Set-EmailAddressPolicy -Identity "Contoso Executives" -
  DisabledEmailAddressTemplates $null

<!-- p.2104 -->

For detailed syntax and parameter information, see Set-EmailAddressPolicy.

How do you know this worked?
To verify that you've successfully modified an email address policy, use either of the following
procedures:

     In the EAC, go to Mail flow > Email address policies, and verify the properties are correct.
     Select the policy and click Edit (   ) to view properties that aren't displayed in the list view.

     In the Exchange Management Shell, run the following command to verify the property
     values:

        PowerShell

        Get-EmailAddressPolicy | Format-List
        Name,Priority,*Template*,RecipientFilterType,RecipientContainer,RecipientFilt
        er,IncludedRecipientsConditional*

Apply email address policies to recipients
After you create or modify an email address policy in the EAC or the Exchange Management
Shell, you need to apply the policy to the affected recipients.

     If the policy affects more than 3000 recipients, we recommend that you use the Exchange
     Management Shell. The recipient updates will take a long time, and will prevent you from
     using the EAC session until the updates are finished.

     If the policy affects less than 3000 recipients, it's OK to use the EAC.

Use the EAC to apply email address policies to recipients
   1. In the EAC, go to Mail flow > Email address policies.

   2. Select the email address policy that you want to apply (a policy that has the Status value
     Unapplied).

   3. In the details pane, click Apply.

<!-- p.2105 -->

   4. After you click Apply, a warning message that appears. Click Yes to apply the policy by
     using the EAC. A progress bar allows you to monitor the recipient update process. When
     updates are complete, click Close.

Use the Exchange Management Shell to apply email address
policies to recipients
To apply an email address policy to recipients, use the following syntax:

  PowerShell

  Update-EmailAddressPolicy -Identity <EmailAddressPolicyIdentity> [-
  FixMissingAlias] -[UpdateSecondaryAddressesOnly]

This example applies the email address policy named Northwest Executives.

  PowerShell

<!-- p.2106 -->

  Update-EmailAddressPolicy -Identity "Northwest Executives"

For detailed syntax and parameter information, see Update-EmailAddressPolicy.

How do you know this worked?
To verify that you've successfully applied an email address policy, use either of the following
procedures:

     In the EAC, go to Mail flow > Email address policies, and verify that the Status value of
     the policy is Applied.

     In the Exchange Management Shell, run the following command to verify the
     RecipientFilterApplied property has the value True :

        PowerShell

        Get-EmailAddressPolicy | Format-Table -Auto Name,RecipientFilterApplied

Remove email address policies
     You can't delete the default email address policy.

     If the policy affects more than 3000 recipients, we recommend that you use the Exchange
     Management Shell to remove the policy. The recipient updates will take a long time, and
     will prevent you from using the EAC session until the updates are finished. If removing the
     policy affects less than 3000 recipients, it's OK to use the EAC.

Use the EAC to remove email address policies
   1. In the EAC, go to Mail flow > Email address policies.

   2. Select the email address policy that you want to delete, and then click Remove     .

   3. Click Yes in the warning message that appears. A progress bar allows you to monitor the
     recipient update process. When updates are complete, click Close.

Use the Exchange Management Shell to remove email address
policies
To remove an email address policy, use the following syntax:

<!-- p.2107 -->

  PowerShell

  Remove-EmailAddressPolicy -Identity <EmailAddressPolicyIdentity>

This example removes the email address policy named Southeast Offices.

  PowerShell

  Remove-EmailAddressPolicy -Identity "Southeast Offices"

For detailed syntax and parameter information, see Remove-EmailAddressPolicy.

How do you know this worked?
To verify that you've successfully removed an email address policy, use either of the following
procedures:

     In the EAC, go to Mail flow > Email address policies, and verify that the policy is no
     longer listed.

     In the Exchange Management Shell, run the following command to verify that the email
     address policy isn't listed:

        PowerShell

        Get-EmailAddressPolicy

Reference

Email address format window in the EAC
As you create or modify an email address policy in the EAC, in the Email address format
section, an Email address format window appears when you click Add (          ) or Edit (   ). The
following settings are available in this window:

     Precanned SMTP email addresses:

        Select an accepted domain: Select an accepted domain (authoritative domain or
        internal relay domain) from the drop down list. Note that if you've configured an
        accepted domain for a domain and all subdomains (for example, *.contoso.com ), only
        the root domain ( contoso.com ) is available in the drop down list.

<!-- p.2108 -->

        Or

        Specify a custom domain name for the email address: Select this option when you
        need to enter a subdomain of a *.<domain> accepted domain. For example, if
         *.contoso.com is configured as an authoritative domain, you can type eu.contoso.com

        in this field.

        And then:

        Email address format: Select one of the available email address templates from the
        list.

     Custom SMTP or non-SMTP email addresses:

        Click More options and then select Enter a custom address type.

        Enter a custom address type: If this is the first email address template that you're
        configuring in the policy, type SMTP, and then continue to the Email address
        parameters field to define the primary SMTP email address format.

        After you've configured a template in the policy to define the primary SMTP email
        address, you can type SMTP or another address type value to configure email address
        templates for additional proxy addresses. For more information about the type values
        that you can use, see Address types.

        Email address parameters: For SMTP email addresses, this value contains:

        Valid variables and ASCII text characters as described in Address formats.

        A domain or subdomain that's configured as an accepted domain (authoritative or
        internal relay).

        An example value is %3g.%s@contoso.com for <first three letters of the first
        name>.<last name> @contoso.com.

     Make this format the reply email address: The first email address template in a policy is
     automatically configured as the primary (reply) email address (you can't uncheck the
     check box). When you add additional templates to the policy, you can select this check
     box to define the primary email address.

Recipient filters in the EAC
When you create or modify email address policies in the EAC, the following recipient filter
settings are available:

<!-- p.2109 -->

Specify the types of recipients this email address policy will apply to:

  All recipient types

  Or

  Only the following recipient types: Select one or more of the following values:

       Users with Exchange mailboxes

       Mail users with external email addresses

       Resource mailboxes

       Mail contacts with external email addresses

       Mail-enabled groups

Create rules to further define the recipients that this email address policy applies to:

   1. Click Add rule and select one of the recipient properties from the drop down list:

         Recipient container (container or organization unit)

         State or province

         Company

         Department

         Custom attribute 1 to 15

   2. Enter a value for the property you selected:

         If you selected Recipient container, a Select an organizational unit dialog box
         appears that allows you to select the container or OU in Active Directory.

         For other recipient properties, a Specify words or phrases dialog appears that
         allows you to add, edit and remove text values.

         Property values require an exact match. Wildcards and partial matches aren't
         supported. For example, the value "Sales" doesn't match "Sales and Marketing".

         Multiple values of the same property use the or operator. For example,
         "Department equals Sales or Department equals Marketing"

   3. After you've selected a property and value, click Add rule.

<!-- p.2110 -->

         4. Repeat the previous steps to configure more filters. Note that multiple properties
           use the and operator. For example, "Department equals Sales and Company equals
           Contoso".

           Preview recipients the policy applies to: When you click this setting, a Preview
           dialog appears that shows you the recipients that are identified by the filters you
           configured.

Notes:

     You can't configure any recipient filter settings in the default email address policy (All
     recipient types is selected).

     If you configure too many recipient filter rules, you can restrict the policy to the point
     where it doesn't contain any recipients.

Recipient filters in the Exchange Management Shell
In the Exchange Management Shell, you can specify precanned recipient filters, or custom
recipient filters, but not both at the same time.

     Precanned recipient filters:

         Uses the required IncludedRecipient parameter with the AllRecipients value or one or
         more of the following values: MailboxUsers , MailContacts , MailGroups , MailUsers , or
         Resources . You can specify multiple values separated by commas.

         You can also use any of the optional Conditional filter parameters:
         ConditionalCompany, ConditionalCustomAttribute[1to15], ConditionalDepartment, and
         ConditionalStateOrProvince.

         You specify multiple values for a Conditional parameter by using the syntax "
         <Value1>","<Value2>"... . Multiple values of the same property implies the or operator.

         For example, "Department equals Sales or Marketing or Finance".

     Custom recipient filters: Uses the required RecipientFilter parameter with an OPATH filter.

         The basic OPATH filter syntax is "<Property1> -<Operator> '<Value1>' <Property2> -
         <Operator> '<Value2>'..." .

         Double quotation marks " " are required around the whole OPATH filter. Although the
         filter is a string (not a system block), you can also use braces { } , but only if the filter
         doesn't contain variables that require expansion..

<!-- p.2111 -->

        Hyphens ( - ) are required before all operators. Here are some of the most frequently
        used operators:

         and , or , and not .

         eq and ne (equals and does not equal; not case-sensitive).

         lt and gt (less than and greater than).

         like and notlike (string contains and does not contain; requires at least one wildcard

        in the string. For example, "Department -like 'Sales*'" .

        Use parentheses to group <Property> -<Operator> '<Value>' statements together in
        complex filters. For example, "(Department -like 'Sales*' -or Department -like
        'Marketing*') -and (Company -eq 'Contoso' -or Company -eq 'Fabrikam')" . Exchange

        stores the filter in the RecipientFilter property with each individual statement enclosed
        in parentheses, but you don't need to enter them that way.

        For more information, see Additional OPATH syntax information.

        After you use the New-EmailAddressPolicy cmdlet to create a policy that uses custom
        recipient filters, you can't modify the recipient filters in the EAC. You need to use the
        Set-EmailAddressPolicy cmdlet with the RecipientFilter parameter in the Exchange
        Management Shell.

Note: The RecipientContainer (organizational unit) recipient filter parameter is available to both
precanned recipient filters and custom recipient filters.

<!-- p.2112 -->

Offline address books in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016      2019      Subscription Edition

An offline address book (OAB) is a local copy of an address list collection. OABs are used for
address book queries by Outlook clients that are configured in cached Exchange mode. OABs
are the only option for Outlook clients that are disconnected from the Exchange server, but
they're also queried first by connected Outlook clients as a way to help reduce the workload on
Exchange servers. You can configure which address lists are included in an OAB, access to
specific OABs, how frequently the OABs are generated, and where the OABs are distributed
from.

By default, a new installation of Exchange creates an OAB named Default Offline Address Book
on the server. This OAB is also the default OAB, which means it's the OAB that's used by
mailboxes and mailbox databases that don't have an OAB assigned to them.

OABs in Exchange 2013 and later are improved over OABs in Exchange 2010. These changes
were introduced in Exchange 2013:

        Only web-based distribution is supported (public folder distribution is no longer
        available). Web-based distribution allows:

          Support for more concurrent downloads by client computers.

          Reduced bandwidth usage.

          More control over the OAB distribution points.

        Only OAB version 4 is supported. This version of the OAB is Unicode, and allows clients to
        receive differential updates, instead of always using full downloads. All versions of
        Outlook that are supported by Exchange fully support OAB version 4.

        A mailbox assistant (not the Microsoft Exchange System Attendant service) is the process
        that's responsible for generating OABs. This allows OAB generation to run or pause based
        on the workload of the server (workload management).

        OAB generation occurs in a designated arbitration mailbox (not on a designated OAB
        generation server). These mailboxes can use database availability groups (DAGs) to help
        prevent a single point of failure for OAB generation and downloads.

For OAB procedures, see Procedures for offline address books in Exchange Server.

To learn more about address lists, see Address lists in Exchange Server.

<!-- p.2113 -->

OAB generation
OAB generation is controlled by the mailbox assistant named OABGeneratorAssistant that runs
under the Microsoft Exchange Mailbox Assistants service. OAB generation occurs in a
designated arbitration mailbox that has the OrganizationCapabilityOABGen value for the
PersistedCapability property. An arbitration mailbox with this capability is also known as an
organization mailbox.

By default, OABs are generated every 8 hours. To change the OAB generation schedule, see
Change the offline address book generation schedule in Exchange Server. To manually update
an OAB, see Use the Exchange Management Shell to update offline address books.

The arbitration mailbox named SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c} is the
first organization mailbox in your organization. By default, this organization mailbox is
responsible for generating all OABs (the first OAB named Default Offline Address Book, and
any new OABs that you create).

You can create additional organization mailboxes to generate OABs. Exchange Server contains
the improvements to OAB generation that were introduced in Exchange 2013 Cumulative
Update 7 (CU7):

     You can configure multiple OABs to be generated by the same organization mailbox, but
     you can't configure an OAB to be generated by more than one organization mailbox. If
     you configured an OAB with multiple organization mailboxes, each copy of the OAB had a
     different unique identifier. So, a full OAB download was required whenever a client was
     proxied to a different organization mailbox location.

     You can configure an OAB to allow a read-only copy (also known as a shadow copy) to be
     distributed to all organization mailboxes in the organization (also known as shadow
     distribution). All copies of the OAB have the same unique identifier, so full a OAB
     download isn't required when a client is proxied to a different organization mailbox
     location.

     Typically, shadow copies are only required in multi-site Exchange organizations. You
     configure an organization mailbox in each site, and you configure shadow distribution for
     an OAB to help prevent cross-site OAB download requests by clients (likely over slow
     WAN links). To create additional organization mailboxes, see Use the Exchange
     Management Shell to create organization mailboxes.

     Shadow distribution is described in detail in the next section.

To find all organization mailboxes, and the organization mailbox that's defined for an OAB, see
Use the Exchange Management Shell to find organization mailboxes.

<!-- p.2114 -->

The OAB files are generated and stored in the designated organization mailbox, so the
destination for OAB download requests is the Mailbox server that holds the active copy of the
organization mailbox. The OAB files are copied from the organization mailbox to
%ExchangeInstallPath%ClientAccess\OAB\<OAB GUID> for retrieval by clients. Clients never

connect directly to this backend location. Client requests for the OAB are proxied by the Client
Access (frontend) services on a Mailbox server to this backend location.

OAB distribution
By default, Outlook clients are configured to download the OAB every 24 hours, or users can
initiate a manual download from Outlook at any time.

OAB distribution to clients depends on Internet Information Services (IIS) virtual directories and
the Autodiscover service. The IIS virtual directory that's used for client access to OABs is
located in the default web site in the Client Access (frontend) services on the Mailbox server,
and is named OAB (Default Web Site). This virtual directory is automatically created when you
install Exchange, and is configured to service internal clients at the URL
https://<ServerName>/oab (for example, https://mailbox01.contoso.com/oab ). You'll need to

manually configure the external URL that's used to distribute OABs to external clients. For more
information, see Step 4: Configure external URLs in Configure mail flow and client access on
Exchange servers.

In the properties of the OAB, you can configure the OAB virtual directories that are available to
distribute the OAB to clients. The default setting restricts OAB distribution to the OAB virtual
directories on the server that holds the OAB's organization mailbox. However, the Client Access
services on any Mailbox server can proxy incoming OAB download requests to the correct
location. Therefore, we recommend that you configure all OAB virtual directories to accept
requests to download the OAB. For instructions, see Use the Exchange Management Shell to
configure any virtual directory in the organization to accept download requests for the OAB.

The Autodiscover service advertises the OAB URLs that you've configured. Autodiscover is
supported by all versions of Outlook and virtually all mobile devices that are currently by
Exchange. Here's a summary of the OAB distribution process:

   1. Outlook receives the OAB URL from Autodiscover, and connects to the Client Access
     (frontend) services on a Mailbox server.

   2. The Client Access services on the Mailbox server that accepted the connection performs
     these steps:

      a. Queries Active Directory to find the organization mailbox that's responsible for
        generating the user's OAB (the default OAB, the OAB that's specified for the mailbox

<!-- p.2115 -->

        database, or the OAB that's specified for the mailbox).

     b. Queries Active Directory again to find the mailbox database that hosts the
        organization mailbox for the OAB, and the Mailbox server that currently holds the
        active copy of the database.

      c. Proxies the OAB download request to the identified Mailbox server.

     d. Retrieves the OAB files from the backend location
        %ExchangeInstallPath%ClientAccess\OAB\<GUID> and proxies them back to the client.

If a shadow copy of the OAB exists in an organization mailbox in the local Active Directory site
(the site where the user is connecting from), then a local Mailbox server is used to download
the OAB. However, synchronization of the shadow copy between organization mailboxes is
performed on-demand. Here's how it works:

   1. Let's say the organization mailbox doesn't have a suitable shadow copy of the OAB. This
     can be caused by the following conditions:

           A client has never requested a download of the shadow copy.

           The shadow copy is out of date. Shadow copies are aware when an updated copy of
           the parent OAB has been generated and published (manually, or by the default 8
           hour OAB generation schedule). The affected Mailbox servers will stop distributing
           the outdated shadow copy to clients.

   2. The first client tries to download the shadow copy will receive error 0x80190194
     (BG_E_HTTP_ERROR_404) in Outlook. This will trigger a full copy of the OAB from the parent

     to the shadow copy. The following events are reported:

           Event ID: 102

           Source: MSExchange OABRequestHandler

           Description: The OABRequestHandler has begun downloading the OAB <GUID> from

           the server <Server>.

           Event ID: 103

           Source: MSExchange OABRequestHandler

           Description: The OABRequestHandler has finished downloading the OAB <GUID>.

   3. The OABRequestHandler will make up to three immediate attempts to copy the OAB files
     from the Mailbox server that holds the parent OAB generation mailbox. If all three

<!-- p.2116 -->

     attempts fail, the OABRequestHandler will retry the copy after one hour. The following
     events are reported:

           Event ID: 104

           Source: MSExchange OABRequestHandler

           Description: Download of the OAB <GUID> failed. The job will be re-submitted.

          The error was: BG_ERROR_CONTEXT=BE_ERROR_CONTEXT_REMOTE_FILE; error
          code=0x80190194

           Event ID: 105

           Source: MSExchange OABRequestHandler

           Description: Download of the OAB <GUID> has failed too many times. The job will

          not be resubmitted for the next hour.

  4. If the OAB is configured for shadow distribution, but there's no organization mailbox in
     the local Active Directory site (the site where the user is connecting from), the Client
     Access services will proxy the OAB download request back to the Mailbox server that
     holds the organization mailbox for the parent OAB.

Conditions that cause a full OAB download
The improvements to OABs typically require clients to download OAB updates, not the full and
complete OAB. However, full OAB downloads are sometimes required. For example:

     The Changes.oab files are greater than or equal to half the size of the full OAB files.
     Outlook compares the total size of the compressed Changes.oab files that are required to
     update the OAB to the total size of the compressed full OAB files on the server.

     There's no OAB on your computer (for example, during the initial setup of Outlook).

     A differential file is missing on the server. Missing differential files can be caused by the
     following conditions:

        You haven't used Outlook to connect to your Exchange mailbox in more than 30 days
        (by default, the differential files are stored on the server for 30 days).

        The server couldn't generate the differential file for a day that's required to update
        your local copy of the OAB.

<!-- p.2117 -->

     A more recent version of the OAB is available on the server (for example, your mailbox
     was upgraded from Exchange 2010, and your local copy of the OAB is version 3).

     Applying changes to the OAB failed. For example, differential files are corrupted on the
     server (the server crashed during differential file generation).

     The OAB is not present on your computer (for example, you manually deleted one or
     more local OAB files).

     A previous full download failed, so Outlook has to start over.

     You initiated a manual download of the full OAB.

OAB planning and deployment
Whether you use a single OAB or multiple OABs, consider the following factors as you plan and
implement your OAB strategy:

     Th size of each OAB in your organization. OAB sizes can vary from a few megabytes to
     hundreds of megabytes. The following factors can affect the size of the OAB:

        The usage of certificates in your organization. The more public key infrastructure (PKI)
        certificates, the larger the OAB. PKI certificates range from 1 kilobyte (KB) to 3 KB.
        They're the single largest contributor to the OAB size.

        The number of mail recipients in your organization.

        The number of groups in your organization.

        User information that your organization adds to each recipient object. For example,
        some organizations configure full address and contact details for each user.

     The number of OAB downloads.

     The number and frequency of parent distinguished name changes for recipient objects in
     Active Directory.

     SMTP address mismatches.

     The overall number of changes that you make to Active Directory.

     Recipients that you've hidden in Active Directory by using methods outside of Exchange
     will be visible in OABs (for example, by using the Windows security descriptor). To
     effectively hide recipients in OABs, configure the Hide from address lists property for the
     recipient in the Exchange admin center (EAC) or the HiddenFromAddressListsEnabled

<!-- p.2118 -->

     parameter in the corresponding recipient management cmdlet in the Exchange
     Management Shell. For more information, see Hide recipients from address lists. Or, you
     can create an address list that doesn't include the hidden recipients, assign the address
     list to the OAB, and assign the OAB to users (directly or by making the OAB the default).
     For more information about creating address lists, see Create address lists.

Move OAB generation to another server
In Exchange 2010, moving OAB generation to another server required you to specify a different
generation server in the properties of the OAB. But in Exchange 2013, Exchange 2016 and
Exchange 2019, OAB generation occurs in a designed organization mailbox, not on a
designated server. To move OAB generation to another server, you need to move the
organization mailbox. For example:

     Move the existing organization mailbox to a different Exchange 2013, Exchange 2016, or
     Exchange 2019 server (you can't move the organization mailbox to an Exchange 2010
     server).

     Configure the OAB to use an existing organization mailbox on a different server. For more
     information, see Use the Exchange Management Shell to change the organization
     mailbox that's responsible for generating an offline address book.

     Create a new organization mailbox on a different server, and configure the OAB to use
     that organization mailbox. For more information, see Use the Exchange Management
     Shell to create organization mailboxes.

Remember, you can configure multiple OABs to use the same organization mailbox, but you
can't configure an OAB to use more than one organization mailbox. If you need multiple copies
of the OAB in different locations (typically, in different Active Directory sites), verify that an
organization mailbox is exists in the site, and enable shadow distribution for the OAB. For more
information, see Use the Exchange Management Shell to enable shadow distribution for offline
address books.

<!-- p.2119 -->

Procedures for offline address books in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

An offline address book (OAB) in Exchange Server allows Outlook users in cached Exchange
mode to access address list and global address list information while they're disconnected
from the server. For more information, see Offline address books in Exchange Server.

Here's a list of OAB procedures that are covered in this topic:

      Use the Exchange Management Shell to view offline address books

      Use the Exchange Management Shell to create offline address books

      Use the Exchange Management Shell to modify offline address books:

         Use the Exchange Management Shell to configure the default offline address book

         Use the Exchange Management Shell to add and remove address lists from offline
         address books

         Use the Exchange Management Shell to change the organization mailbox that's
         responsible for generating an offline address book

         Use the Exchange Management Shell to configure any virtual directory in the
         organization to accept download requests for the OAB

         Use the Exchange Management Shell to enable shadow distribution for offline address
         books

      Use the Exchange Management Shell to update offline address books

      Use the Exchange Management Shell to remove offline address books

      Use the Exchange Management Shell to find organization mailboxes

      Use the Exchange Management Shell to create organization mailboxes

      Assign offline address books to mailbox databases

      Use the Exchange Management Shell to assign offline address books to mailboxes

To change the OAB generation schedule, see Change the offline address book generation
schedule in Exchange Server.

<!-- p.2120 -->

What do you need to know before you begin?
     Estimated time to complete each procedure: 5 minutes

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Offline address books" entry in
     the Email address and address book permissions topic.

     You can't do most of these procedures in the Exchange admin center (EAC). You need to
     use the Exchange Management Shell. To learn how to open the Exchange Management
     Shell in your on-premises Exchange organization, see Open the Exchange Management
     Shell. For more information about the EAC, see Exchange admin center in Exchange
     Server.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online     , or Exchange Online Protection .

Use the Exchange Management Shell to view
offline address books
To view OABs, use the following syntax:

  PowerShell

  Get-OfflineAddressBook [-Identity <OABIdentity>]

This example returns a summary list of all OABs in your organization.

  PowerShell

  Get-OfflineAddressBook

This example returns detailed information about the OAB named Default Offline Address Book.

  PowerShell
