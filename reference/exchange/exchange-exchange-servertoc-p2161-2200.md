---
title: "Exchange Server — pages 2161-2200"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2161-2200
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2161-2200
family: exchange
documentKind: "doc"
abstract: "APBs take effect when a user connects to the Client Access (frontend) services on a Mailbox server. If you change an ABP, the updated APB takes effect when a user restarts or reconnects their client app, or you restart the Mailbox server (specifically, the Microsoft Exchange RPC"
---

# Exchange Server — pages 2161-2200

<!-- p.2161 -->

APBs take effect when a user connects to the Client Access (frontend) services on a Mailbox
server. If you change an ABP, the updated APB takes effect when a user restarts or reconnects
their client app, or you restart the Mailbox server (specifically, the Microsoft Exchange RPC
Client Access service in the backend services).

Address Book Policy Routing agent
In an Exchange organization that doesn't use ABPs, the following things occur when a user
creates an email message in Outlook or Outlook on the web and sends the message to another
recipient in the organization:

   1. The email address resolves to the user's display name. For example, if you type
     sardor@contoso.com in the To field, the SMTP email address resolves to Sarah Dorsey.

   2. After the name resolves, you can view the recipient's contact card by double-clicking on
     the user's name. The contact card shows the recipient's contact information, such as
     office and phone number.

If you're using ABPs, and you don't want the users in the ABPs to view each other's potentially
private information, you can turn on the Address Book Policy Routing agent. The ABP Routing
agent is a Transport agent that controls how recipients are resolved in your organization. When
the ABP Routing agent is installed and configured, users that are assigned to different GALs by
different ABPs can't view each other's contact cards (they appear as external recipients to each
other).

<!-- p.2162 -->

For details about how to turn on the ABP Routing agent, see Use the Exchange Management
Shell to install and configure the Address Book Policy Routing Agent.

ABP example
In the following diagram, Fabrikam and Tailspin Toys share the same Exchange organization
and the same CEO. The CEO is the only employee common to both companies.

The suggested configuration includes three ABPs:

     One ABP is assigned to Fabrikam employees. The GAL and address lists in the ABP include
     Fabrikam employees and the CEO.

     One ABP is assigned to Tailspin Toys employees. The GAL and address lists in the ABP
     include Tailspin Toys employees and the CEO.

     One ABP is assigned to only the CEO. The (default) GAL and address lists in the ABP
     include all employees (Fabrikam, Tailspin Toys, and the CEO).

Based on this configuration, the ABPs help to enforce these requirements:

     The users in Tailspin Toys can only see Tailspin Toys employees and the CEO when they
     browse the GAL.

     The users in Fabrikam can only see Fabrikam employees and the CEO when they browse
     the GAL.

<!-- p.2163 -->

The CEO can see all Fabrikam and Tailspin Toys employees when she browses the GAL.

Users who view the CEO's group membership can see only groups that belong to their
company. They can't see groups that belong to the other company.

<!-- p.2164 -->

Scenario: Deploying address book policies
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

The scenarios in this topic describe the deployment solutions for address book policies (ABPs)
in three of the most common organization types where multiple entities (companies,
government agencies, school classrooms, etc.) share a common Exchange environment. In all
scenarios, a recipient filter divides recipients into separate virtual organizations, which then
defines the ABPs that are applied to users in those virtual organizations. For more information
recipient filters and virtual organizations, see the Considerations and best practices for address
book policies section later in this topic.

For more information about ABPs, see Address book policies in Exchange Server. For ABP
procedures, see Procedures for address book policies in Exchange Server.

Scenario 1: Two separate companies in one
Exchange organization
This scenario applies to companies or divisions that share the same Exchange environment, but
have no common employees or management. In addition, the divisions have no special
security or privacy concerns.

In this scenario, Contoso and Humongous Insurance are two separate companies that share the
same Exchange environment. An ABP for each company lets employees in one company see
only members of the same company in the global address list (GAL) in Outlook and Outlook on
the web (formerly known as Outlook Web App). All distribution groups belong to one company
or the other, and no distribution group contains members from both companies.

<!-- p.2165 -->

The GAL, offline address book (OAB), room list, and address lists that are required inn the ABPs
for this scenario are described in the this table:

                                                                               ﾉ   Expand table

 ABP element                       Contoso                   Humongous Insurance

 Global address list               GAL_CON                   GAL_HI

 Offline address book              OAB_CON                   OAB_HI

 Room list                         AL_CON_Rooms              AL_HI_Rooms

 Address Lists                     AL_CON_Groups             AL_HI_Groups
                                   AL_CON_Users              AL_HI_Users
                                   AL_CON_Contacts           AL_HI_Contacts

Scenario 2: Two companies sharing a CEO in one
Exchange organization
This scenario applies to companies or divisions that share Exchange environment, and the only
employees in common are in upper management.

In this scenario, Fabrikam and Tailspin Toys are separate companies in the same Exchange
environment that share the same CEO, who is the only person in common between the two
companies. This scenario uses three ABPs that have the following requirements:

     Employees in one company can only see recipients in their company when they browse
     the GAL, and employees in both companies can see the CEO in the GAL and in

<!-- p.2166 -->

     distribution groups.

     The CEO can see all recipients in both companies, is able to create distribution groups
     that span both companies, and the groups are visible in each company's GAL. However,
     group members only see other members from their respective company (group members
     from the other company are hidden).

     Employees who look at the CEO's group membership will only see groups in their
     company. They won't see groups in the other company.

     Each company has a distribution group named Senior Leadership that includes the
     management of that company and the CEO.

     The names of the three ABPs are: ABP_FAB, ABP_TAIL, and ABP_CEO.

The GAL, OAB, room list, and address lists that are required in the ABPs for this scenario are
described in the this table:

                                                                                 ﾉ   Expand table

 ABP element             Fabrikam            Tailspin Toys         CEO

 Name                    ABP_FAB             AB_TAIL               ABP_CEO

 Global address list     GAL_FAB             GAL_TAIL              Default Global Address Book

 Offline address book    OAB_FAB             OAB_TAIL              Default Offline Address Book

<!-- p.2167 -->

 ABP element             Fabrikam                Tailspin Toys       CEO

 Room address list       AL_FAB_Rooms            AL_TAIL_Rooms       All Rooms

 Address lists           AL_FAB_Users_DGs        AL_TAIL_Users_DGs   AL_FAB_Users_DGs
                         AL_FAB_Contacts         AL_TAIL_Contacts    AL_FAB_Contacts
                                                                     AL_TAIL_Users_DGs
                                                                     AL_TAIL_Contacts

For a complete walkthrough of creating the required elements for this scenario, see the
Detailed deployment steps for Scenario 2: Two companies sharing a CEO in one Exchange
organization section at the end of this topic.

Scenario 3: Education
This scenario is applicable to schools or universities where a division of class rooms is
necessary to ensure the privacy of the students, and has the following requirements:

     Students in each class can only see other students in their class, their teacher, and the
     principal.

     Teachers can only see students in their own classes.

     Teachers can see the principal and all other teachers.

     Distribution groups are created for the parents and faculty that are associated with each
     class.

The GAL, OAB, room list, and address lists that are required in the ABPs for this scenario are
described in the this table:

<!-- p.2168 -->

                                                                                          ﾉ   Expand table

 ABP            Students_ClassA         Teachers_ClassA                                   Principal
 element

 Global         GAL_StudentsClassA      GAL_TeachersClassA                                GAL_Everyone
 address
 list

 Offline        OAB_StudentsClassA      OAB_TeachersClassA                                Default Offline
 address                                                                                  Address Book
 book

 Room           AL_BlankRoom            AL_BlankRoom                                      All Rooms
 address
 list

 Address        AL_ClassAAL_Principal   AL_ClassAAL_AllTeachersAL_AllGroupsAL_Principal   AL_ClassA
 Lists                                                                                    AL_ClassB
                                                                                          AL_AllTeachers
                                                                                          AL_AllStudents
                                                                                          AL_AllGroups

Considerations and best practices for address book
policies
These are the important issues to consider when you use ABPs in your organization:

         You can't use hierarchical address books (HABs) and ABPs simultaneously. To learn more,
         see Understanding Hierarchical Address Books.

         A user that's assigned an ABP needs to exist in the GAL that's specified for the ABP.

         If you create ABPs in your organization and don't assign an ABP to some users, those
         recipients can see all address lists.

         To divide recipients into virtual organizations, we recommend using the
         CustomAttribute1 to CustomAttribute15 attributes on recipients. These attributes work
         better than the other pre-canned conditional attributes such as Company, Department,
         or StateOrProvince because:

            Not all recipient types support the Company, Department or StateOrProvince
            attributes (for example, distribution groups, dynamic distribution groups, and mail-
            enabled public folders).

<!-- p.2169 -->

   The CustomAttribute1 to CustomAttribute15 attributes aren't configurable by users on
   their own mailboxes, and are entirely under the control of administrators.

   Even recipient types that support the Company, Department or StateOrProvince
   attributes require different cmdlets to configure them.

   For example, to configure values for Company, Department or StateOrProvince on
   mailboxes, mail users, or mail contacts, you can't use the Set-Mailbox, Set-MailUser, or
   Set-MailContact cmdlets. Instead, you need to use the Set-User and Set-Contact
   cmdlets. In contrast, the CustomAttribute1 to CustomAttribute15 parameters are
   available on the corresponding Set-* cmdlets for all recipient types.

   For more information about recipient filtering, see Recipient filtering on Edge
   Transport servers.

Client applications that access Active Directory directly through LDAP will bypass the logic
that's built into ABPs.

At a minimum, the GAL that's specified in an ABP must contain all address lists (including
the room address list) that are specified in the ABP (it's OK if the ABP contains additional
address lists). Don't create a GAL that contains fewer recipients than the address lists in
the same ABP.

We recommend against creating distribution groups that cross virtual organization
boundaries. Groups that contain members of multiple virtual organizations lead to these
issues:

   A group member will see the email addresses of all group members if they request a
   delivery receipt or a read receipt when they send a message to the distribution group.

   Encrypted messages that are sent to the distribution group can cause issues when
   some group members don't have valid digital IDs. For example, suppose a distribution
   group contains three members from Agency A, and two members from Agency B.
   Furthermore, one of the members from Agency A and two of the members in Agency
   B have invalid digital IDs. If a member from Agency A sends an encrypted messages to
   the distribution group, they'll receive a warning that there are three recipients without
   valid digital IDs. However, only the email address for the member in Agency A will
   appear in the warning message.

   ABPs don't apply to all users or processes that use the Get-Group cmdlet, so these
   users will see all members of any group that they have access to.

   Because if this issue, we recommend that you prevent users from managing their own
   groups in Outlook or Outlook on the web. To do this, remove the

<!-- p.2170 -->

        MyDistributionGroupMembership RBAC role assignment from the users. For more
        information, see Manage role assignment policies.

        If you allow users to use Outlook or Outlook on the web to manage groups, visibility to
        the full group membership list must be OK for the group owners.

     All ABPs must contain a room address list. However, if your organization doesn't use
     room address lists, you can create an empty room address list.

     Note: The room list that's required for an ABP is an address list that specifies rooms
     (contains the filter RecipientDisplayType -eq 'ConferenceRoomMailbox' ). It's not a room
     finder distribution group that you create with the RoomList switch on the New-
     DistributionGroup or Set-DistributionGroup cmdlets. For more information, see Create
     and manage room mailboxes.

     Deploying ABPs doesn't prevent users in one virtual organization from sending email to
     users in another virtual organization. If you want to prevent users from sending email
     across virtual organizations, we recommend that you create a mail flow rule (also known
     as a transport rule) that looks for messages sent between the recipients. For example, to
     prevent Contoso users from receiving messages from Fabrikam users and vice-versa, but
     still allow Fabrikam's senior leadership team to send messages to Contoso users, you can
     create the following mail flow rule in the Exchange Management Shell:

       PowerShell

       New-TransportRule -Name "Ethical Wall: Contoso-Fabrikam" -BetweenMemberOf1
       "AllFabrikamEmployees" -BetweenMemberOf2 "AllContosoEmployees" -DeleteMessage
       -ExceptIfFrom seniorleadership@fabrikam.com

     For more information about mail flow rules, see Mail flow rules in Exchange Server.

     To configure a feature that's similar to address book policies in the Skype for Business or
     Lync client, you can set the msRTCSIP-GroupingID attribute for specific users. For details,
     see PartitionByOU Replaced with msRTCSIP-GroupingID.

Detailed deployment steps for Scenario 2: Two
companies sharing a CEO in one Exchange
organization
This section walks you through the deployment steps for Scenario 2: Two companies sharing a
CEO in one Exchange organization. If you recall, Fabrikam and Tailspin Toys are separate
companies that share the same CEO.

<!-- p.2171 -->

To learn how to open the Exchange Management Shell in your on-premises Exchange
organization, see Open the Exchange Management Shell.

Step 1: Install and configure the Address Book Policy Routing
Agent
The ABP Routing Agent makes users that are assigned different GALs appear as external
recipients to each other. For detailed instructions, see Use the Exchange Management Shell to
install and configure the Address Book Policy Routing Agent.

Step 2: Define your virtual organizations
In this scenario, the CustomAttribute15 attribute defines the virtual organizations: the value
FAB for Fabrikam recipients, the value TAIL for Tailspin Toys recipients, and the value CEO for

the CEO, which is required so Fabrikam and Tailspin users can see the CEO. If you don't include
the CEO in the Fabrikam and Tailspin Toys virtual organizations, the CEO can see everyone, but
no one can see the CEO. For more information about recipient filtering, see Recipient filtering
on Edge Transport servers.

To set the CustomAttribute15 attribute value for the Fabrikam and Tailspin Toys mailboxes,
distribution groups, dynamic distribution groups, mail contacts, and mail users, use the
following syntax:

  PowerShell

  $<VariableName> = Get-<RecipientType> -ResultSize Unlimited | where
  PrimarySMTPAddress -match <fabrikam.com | tailspintoys.com>
  $<VariableName> | foreach {Set-<RecipientType> -Identity ($_.GUID).ToString() -
  CustomAttribute15 <FAB | TAIL>

Notes:

     Using the recipient's GUID value for the Identity parameter can help avoid collisions if
     there are similar usernames in both organizations (for example, julia@fabrikam.com and
     julia@contoso.com).

     The valid <RecipientType> values for the cmdlet names are Mailbox, DistributionGroup,
     DynamicDistributionGroup, MailContact, and MailUser. You need to configure the
     CustomAttribute15 attribute value for each recipient type separately.

This example sets the value FAB for the CustomAttribute15 attribute on all Fabrikam
mailboxes.

<!-- p.2172 -->

  PowerShell

  $FAB_MBX = Get-Mailbox -ResultSize Unlimited | where PrimarySMTPAddress -match
  fabrikam.com
  $FAB_MBX | foreach {Set-Mailbox -Identity ($_.GUID).ToString() -CustomAttribute15
  FAB}

Step 3: Create the required elements for the address book
policies

Create address lists

This organization requires four custom address lists:

     AL_FAB_Users_DGs

     AL_FAB_Contacts

     AL_TAIL_Users_DGs

     AL_TAIL_Contacts

This example creates the address list named AL_FAB_Users_DGs that contains all Fabrikam
users, distribution groups, and dynamic distribution groups and the CEO.

  PowerShell

  New-AddressList -Name "AL_FAB_Users_DGs" -RecipientFilter "((RecipientType -eq
  'UserMailbox') -or (RecipientType -eq 'MailUniversalDistributionGroup') -or
  (RecipientType -eq 'DynamicDistributionGroup')) -and (CustomAttribute15 -eq 'FAB')
  -or (CustomAttribute15 -eq 'CEO')"

This example creates the address list named AL_FAB_Contacts that contains all Fabrikam mail
contacts.

  PowerShell

  New-AddressList -Name "AL_FAB_Contacts" -RecipientFilter "(RecipientType -eq
  'MailContact') -and (CustomAttribute15 -eq 'FAB')"

This example creates the address list named AL_TAIL_Users_DGs that contains all Tailspin Toys
users, distribution groups, and dynamic distribution groups and the CEO.

  PowerShell

<!-- p.2173 -->

  New-AddressList -Name "AL_TAIL_Users_DGs" -RecipientFilter "((RecipientType -eq
  'UserMailbox') -or (RecipientType -eq 'MailUniversalDistributionGroup') -or
  (RecipientType -eq 'DynamicDistributionGroup')) -and (CustomAttribute15 -eq
  'TAIL') -or (CustomAttribute15 -eq 'CEO')"

This example creates the address list named AL_TAIL_Contacts that contains all Tailspin Toys
mail contacts.

  PowerShell

  New-AddressList -Name "AL_TAIL_Contacts" -RecipientFilter "(RecipientType -eq
  'MailContact') -and (CustomAttribute15 -eq 'TAIL')"

For more information, see Create address lists.

Create room lists
This organization requires two custom room lists:

     AL_FAB_Rooms

     AL_TAIL_Rooms

This example creates the room list named AL_FAB_Rooms for Fabrikam room mailboxes.

  PowerShell

  New-AddressList -Name AL_FAB_Rooms -RecipientFilter "(Alias -ne $null) -and
  (CustomAttribute15 -eq 'FAB') -and (RecipientDisplayType -eq
  'ConferenceRoomMailbox') -or (RecipientDisplayType -eq
  'SyncedConferenceRoomMailbox')"

This example creates a room list named AL_TAIL_Rooms for Tailspin Toys room mailboxes.

  PowerShell

  New-AddressList -Name AL_TAIL_Rooms -RecipientFilter "(Alias -ne $null) -and
  (CustomAttribute15 -eq 'TAIL') -and (RecipientDisplayType -eq
  'ConferenceRoomMailbox') -or (RecipientDisplayType -eq
  'SyncedConferenceRoomMailbox')"

Note: This example creates a blank room list named AL_BlankRoom if the organization doesn't
have any room mailboxes (an ABP requires a room list, even if it's empty):

<!-- p.2174 -->

New-AddressList -Name AL_BlankRoom -RecipientFilter "(Alias -ne $null) -and
((RecipientDisplayType -eq 'ConferenceRoomMailbox') -or (RecipientDisplayType -eq

'SyncedConferenceRoomMailbox'))"

For more information about creating address lists, see Create address lists.

Create GALs

This organization requires two custom GALs:

     GAL_FAB

     GAL_TAIL

This example creates the GAL named GAL_FAB for Fabrikam that includes all Fabrikam
recipients and allows the Fabrikam users to see the CEO.

  PowerShell

  New-GlobalAddressList -Name "GAL_FAB" -RecipientFilter "(CustomAttribute15 -eq
  'FAB') -or (CustomAttribute15 -eq 'CEO')"

This example creates the GAL named GAL_TAIL for Tailspin Toys that includes all Tailspin Toys
recipients and allows the Tailspin Toys users to see the CEO.

  PowerShell

  New-GlobalAddressList -Name "GAL_TAIL" -RecipientFilter "(CustomAttribute15 -eq
  'TAIL') -or (CustomAttribute15 -eq 'CEO')"

Note: Don't use a GAL in an ABP that contains recipients that are missing from address lists in
the ABP. The combination of all address lists must match the recipients in the GAL.

For more information, see Use the Exchange Management Shell to create global address lists.

Create OABs
This organization requires two custom GALs:

     OAB_FAB

     OAB_TAIL

This example creates the OAB named OAB_FAB for Fabrikam that includes the Fabrikam GAL.

<!-- p.2175 -->

  PowerShell

  New-OfflineAddressBook -Name "OAB_FAB" -AddressLists "GAL_FAB"

This example creates the OAB named OAB_TAIL for Tailspin Toys that includes the Tailspin Toys
GAL.

  PowerShell

  New-OfflineAddressBook -Name "OAB_TAIL" -AddressLists "GAL_TAIL"

Note: If you want users to see all recipients in the virtual organization, make sure that you
include the GAL in OAB. Otherwise, you can reduce the download size of the OAB by specifying
a reduced list of address lists that are included in the OAB.

For more information, see Use the Exchange Management Shell to create offline address
books.

Step 4: Create the address book policies
This organization requires three ABPs:

                                                                                  ﾉ    Expand table

 ABP element             Fabrikam             Tailspin Toys         CEO

 Name                    ABP_FAB              ABP_TAIL              ABP_CEO

 Global address list     GAL_FAB              GAL_TAIL              Default Global Address Book

 Offline address book    OAB_FAB              OAB_TAIL              Default Offline Address Book

 Room address list       AL_FAB_Rooms         AL_TAIL_Rooms         All Rooms

 Address lists           AL_FAB_Users_DGs     AL_TAIL_Users_DGs     AL_FAB_Users_DGs
                         AL_FAB_Contacts      AL_TAIL_Contacts      AL_FAB_Contacts
                                                                    AL_TAIL_Users_DGs
                                                                    AL_TAIL_Contacts

This example creates the ABP named ABP_FAB that contains the GAL, OAB, room list and
address lists for Fabrikam.

  PowerShell

  New-AddressBookPolicy -Name "ABP_FAB" -AddressLists
  "AL_FAB_Users_DGs","AL_FAB_Contacts" -OfflineAddressBook "\OAB_FAB" -

<!-- p.2176 -->

  GlobalAddressList "\GAL_FAB" -RoomList "\AL_FAB_Rooms"

This example creates the ABP named ABP_TAIL that contains the GAL, OAB, room list and
address lists for Tailspin Toys.

  PowerShell

  New-AddressBookPolicy -Name "ABP_TAIL" -AddressLists
  "AL_TAIL_Users_DGs","AL_TAIL_Contacts" -OfflineAddressBook "\OAB_TAIL" -
  GlobalAddressList "\GAL_TAIL" -RoomList "\AL_TAIL_Rooms"

This example creates the ABP named ABP_CEO that contains the GAL, OAB, room list and
address lists for the CEO.

  PowerShell

  New-AddressBookPolicy -Name "ABP_CEO" -AddressLists
  "AL_FAB_Users_DGs","AL_FAB_Contacts","AL_TAIL_Users_DGs","AL_TAIL_Contacts" -
  OfflineAddressBook "\Default Offline Address Book" -GlobalAddressList "\Default
  Global Address List" -RoomList "\All Rooms"

For more information, see Procedures for address book policies in Exchange Server.

Step 5: Assign the address book policies to mailboxes
This example assigns the ABP named ABP_FAB to all Fabrikam mailboxes.

  PowerShell

  $Fab = Get-Mailbox -ResultSize unlimited -Filter "CustomAttribute15 -eq 'FAB'";
  $Fab | foreach {Set-Mailbox -Identity $_.Identity -AddressBookPolicy 'ABP_FAB'}

This example assigns the ABP named ABP_TAIL to all Tailspin Toys mailboxes.

  PowerShell

  $Tail = Get-Mailbox -ResultSize unlimited -Filter "CustomAttribute15 -eq 'TAIL'";
  $Tail | foreach {Set-Mailbox -Identity $_.Identity -AddressBookPolicy 'ABP_TAIL'}

This example assigns the ABP named ABP_CEO to the CEO named Gabriela Laureano.

  PowerShell

  Set-Mailbox -Identity "Gabriela Laureano" -AddressBookPolicy "ABP_CEO"

<!-- p.2177 -->

Note: If the user is already connected to Outlook or Outlook on the web when the ABP is
applied to their mailbox, they'll need to close and restart their client application before they
can see the new address lists and GAL.

For more information, see Assign address book policies to mailboxes.

Other considerations
After you create or modify an address list or GAL, you need to update the membership.

If the address list contains a large number of recipients (our recommendation is more than
3000), you should use the Exchange Management Shell to update the address list (not the
Exchange admin center). For more information, see Update address lists.

To update a GAL, you always need to use the Exchange Management Shell. For more
information, see Use the Exchange Management Shell to update global address lists.

<!-- p.2178 -->

Procedures for address book policies in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Address book policies (ABPs) allow you to segment users into specific groups to give them
customized global address lists (GALs) in Outlook and Outlook on the web (formerly known as
Outlook Web App). For more information about ABPs, see Address book policies in Exchange
Server.

Note: Implementing an ABP is a multi-step process that requires planning. For more
information, see Scenario: Deploying address book policies in Exchange Server.

What do you need to know before you begin?
      Estimated time to complete each procedure: Less than 5 minutes.

      You can assign ABPs to mailboxes in the Exchange admin center (EAC), but all other ABP
      procedures require the Exchange Management Shell. For more information about
      accessing and using the EAC, see Exchange admin center in Exchange Server. To learn
      how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Address book policies" entry in
      the Email address and address book permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

      Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
      Server   , Exchange Online   , or Exchange Online Protection   .

Use the Exchange Management Shell to view
address book policies
To view ABPs, use this syntax:

  PowerShell

<!-- p.2179 -->

  Get-AddressBookPolicy [-Identity <ABPIdentity>]

This example returns a summary list of all ABPs in the organization:

  PowerShell

  Get-AddressBookPolicy

This example returns detailed information for the ABP named All Fabrikam ABP.

  PowerShell

  Get-AddressBookPolicy -Identity "All Fabrikam ABP" | Format-List

For detailed syntax and parameter information, see Get-AddressBookPolicy.

Use the Exchange Management Shell to create
address book policies
An ABP requires one global address list (GAL), one offline address book (OAB), one room list,
and one or more address lists. To view the available objects, use the Get-GlobalAddressList,
Get-OfflineAddressBook, and Get-AddressList cmdlets.

Note: The room list that's required for an ABP is an address list that specifies rooms (contains
the filter RecipientDisplayType -eq 'ConferenceRoomMailbox' ). It's not a room finder
distribution group that you create with the RoomList switch on the New-DistributionGroup or
Set-DistributionGroup cmdlets.

To create an ABP, use this syntax:

  PowerShell

  New-AddressBookPolicy -Name "<Unique Name>" -GlobalAddressList "<GAL>" -
  OfflineAddressBook "<OAB>" -RoomList "<RoomList>" -AddressLists "<AddressList1>","
  <AddressList2>"...

This example creates an ABP named All Fabrikam ABP with these settings:

     GAL: All Fabrikam

     OAB: Fabrikam-All-OAB

<!-- p.2180 -->

     Room list: All Fabrikam Rooms

     Address lists: All Fabrikam Mailboxes, All Fabrikam DLs, and All Fabrikam Contacts

  PowerShell

  New-AddressBookPolicy -Name "All Fabrikam ABP" -GlobalAddressList "\All Fabrikam"
  -OfflineAddressBook \Fabrikam-All-OAB -RoomList "\All Fabrikam Rooms" -
  AddressLists "\All Fabrikam Mailboxes","\All Fabrikam DLs","\All Fabrikam
  Contacts"

For detailed syntax and parameter information, see New-AddressBookPolicy.

How do you know this worked?
To verify that you've successfully created an ABP, use either of these procedures:

     Run this command in the Exchange Management Shell to verify that the ABP is listed:

        PowerShell

        Get-AddressBookPolicy

     Replace <ABPIdentity> with the name of the ABP, and run this command in the Exchange
     Management Shell to verify the property values:

        PowerShell

        Get-AddressBookPolicy -Identity "<ABPIdentity>" | Format-List

Use the Exchange Management Shell to modify
address book policies
You use the Set-AddressBookPolicy cmdlet to modify an existing ABP. The settings are
identical to the settings that are available when you create an ABP.

     The Name, GlobalAddressList, OfflineAddressBook, and RoomList parameters all take single
     values, so the value you specify replaces the existing value.

     This example modifies the ABP named "All Fabrikam ABP" by replacing the OAB with the
     specified OAB.

        PowerShell

<!-- p.2181 -->

       Set-AddressBookPolicy -Identity "All Fabrikam ABP" -OfflineAddressBook
       \Fabrikam-OAB-2

     The AddressLists parameter takes multiple values, so you need to decide whether you
     want to replace the existing address lists in the ABP, or add and remove address lists
     without affecting the other address lists in the ABP.

     This example replaces the existing address lists in the ABP named Government Agency A
     with the specified address lists.

       PowerShell

       Set-AddressBookPolicy -Identity "Government Agency A" -AddressLists
       "GovernmentAgencyA-Atlanta","GovernmentAgencyA-Moscow"

     To add address lists to an ABP, you need to specify the new address lists and any existing
     address lists that you want to keep.

     This example adds the address list named Contoso-Chicago to the ABP named ABP
     Contoso, which is already configured to use the address list named Contoso-Seattle.

       PowerShell

       Set-AddressBookPolicy -Identity "ABP Contoso" -AddressLists "Contoso-
       Chicago","Contoso-Seattle"

     To remove address lists from an ABP, you need to specify the existing address lists that
     you want to keep, and omit the address lists that you want to remove.

     For example, the ABP named ABP Fabrikam uses the address lists named Fabrikam-HR
     and Fabrikam-Finance. To remove the Fabrikam-HR address list, specify only the
     Fabrikam-Finance address list.

       PowerShell

       Set-AddressBookPolicy -Identity "ABP Fabrikam" -AddressLists Fabrikam-Finance

For detailed syntax and parameter information, see Set-AddressBookPolicy.

How do you know this worked?
To verify that you've successfully modify an ABP, replace <ABPIdentity> with the name of the
ABP, and run this command in the Exchange Management Shell to verify the property values:

<!-- p.2182 -->

  PowerShell

  Get-AddressBookPolicy -Identity "<ABPIdentity>" | Format-List

Use the Exchange Management Shell to remove
address book policies
     You can't remove an ABP if it's assigned to a mailbox. To see if an ABP is assigned to a
     mailbox, replace <ABPIdentity> with the name of the ABP, and run this command in the
     Exchange Management Shell to get the DistinguishedName value:

     Get-AddressBookPolicy -Identity <ABPIdentity> | Format-List DistinguishedName

     Then, use the DistinguishedName value of the ABP in this command to show all
     mailboxes where the ABP is assigned:

     Get-Mailbox -ResultSize unlimited -Filter "AddressBookPolicy -eq

     '<DistinguishedName>'"

     To remove ABP assignments from mailboxes, see the Assign address book policies to
     mailboxes section in this topic.

To remove an ABP, use this syntax:

  PowerShell

  Remove-AddressBookPolicy -Identity <ABPIdentity>

This example removes the ABP named ABP_TailspinToys.

  PowerShell

  Remove-AddressBookPolicy -Identity "ABP_TailspinToys"

For detailed syntax and parameter information, see Remove-AddressBookPolicy.

How do you know this worked?
To verify that you've successfully removed an ABP, use either of these procedures:

     Run this command in the Exchange Management Shell to verify that the ABP isn't listed:

<!-- p.2183 -->

     PowerShell

      Get-AddressBookPolicy

   Replace <ABPIdentity> with the name of the ABP, and run this command to confirm that
   an error is returned:

     PowerShell

      Get-AddressBookPolicy -Identity "<ABPIdentity>"

Assign address book policies to mailboxes
   Users aren't automatically assigned an ABP when you create mailboxes. If you don't
   assign an ABP to a mailbox, the GAL for your entire organization is visible to the user in
   Outlook and Outlook on the web.

   To identify your virtual organizations for ABPs, we recommend that you use the
   CustomAttribute1-15 attributes on mailboxes, contacts, and groups, because these
   attributes are the most widely available and manageable for all recipient types. For more
   information, see Scenario: Deploying address book policies in Exchange Server.

   The procedures to assign ABPs to mailboxes or remove the ABP assignments from
   mailboxes are the same:

      To assign ABPs to mailboxes, you select the ABP in EAC, or specify the ABP in the
      Exchange Management Shell.

      To remove the ABP assignments from mailboxes, you select the value [No Policy] in
      the EAC, or use the value $null in the Exchange Management Shell.

Use the Exchange admin center (EAC) to assign an ABP to a
single mailbox
 1. In the EAC, go to Recipients > Mailboxes.

 2. In the list of mailboxes, find the mailbox that you want to modify. You can:

        Scroll through the list of mailboxes.

        Click Search       and enter part of the user's name, email address, or alias.

        Click More options        > Advanced search to find the mailbox.

<!-- p.2184 -->

     Once you've found the mailbox that you want to modify, select it, and then click Edit   .

   3. On the mailbox properties page that opens, click Mailbox features.

   4. Click the drop-down arrow in Address book policy, and select the ADP that you want to
     apply.

     When you're finished, click Save.

Note: You can also assign an ABP when you create a user mailbox in the EAC by clicking More
options, and clicking the drop-down arrow in Address book policy.

Use the Exchange Management Shell to assign an address
book policy to a single mailbox
To assign an ABP to a mailbox, use this syntax:

  PowerShell

  Set-Mailbox -Identity <MailboxIdentity> -AddressBookPolicy <ABPIdentity> or $null

This example assigns the ABP named All Fabrikam to mailbox joe@fabrikam.com.

  PowerShell

<!-- p.2185 -->

  Set-Mailbox -Identity joe@fabrikam.com -AddressBookPolicy "All Fabrikam"

Note: You can also assign an ABP when you create a user mailbox with the New-Mailbox
cmdlet by using the AddressBookPolicy parameter. If you don't specify an ABP when you create
the mailbox, no ABP is assigned (the default value is blank or $null ).

For detailed syntax and parameter information, see Set-Mailbox.

Use the EAC to assign an address book policy to multiple
mailboxes
   1. In the EAC, go to Recipients > Mailboxes.

   2. In the list of mailboxes, find the mailboxes that you want to modify. For example:

      a. Click More options     > Advanced search.

     b. In the Advanced search window that opens, select Recipient types and verify the
        default value User mailbox.

      c. Click More options, and then click Add a condition.

     d. In the Select one drop-down box that appears, select the appropriate Custom
        attribute 1 to Custom attribute 15 values that defines your virtual organizations.

      e. In the Specify words or phrases dialog that appears, enter the value that you want to
        search for, and then click OK.

      f. Back on the Advanced search window, click OK. In the EAC at Recipients > Mailboxes,
        click More options     > Advanced search to find user mailboxes.

   3. In the list of mailboxes, select multiple mailboxes of the same type (for example, User)
     from the list. For example:

           Select a mailbox, hold down the Shift key, and select another mailbox that's farther
           down in the list.

           Hold down the CTRL key as you select each mailbox.

     After you select multiple mailboxes of the same type, the title of the details pane changes
     to Bulk Edit.

   4. In the details pane, scroll down and click More options, scroll down to Address Book
     Policy, and then click Update.

<!-- p.2186 -->

   5. In the Bulk assign address book policy window that opens, select the ABP by clicking the
     drop-down arrow in Select Address Book Policy, and then click Save.

Use the Exchange Management Shell to assign an address
book policy to multiple mailboxes
You can use the Get-Mailbox or Get-Content cmdlets to identify the user mailboxes that you
want to assign the ABP to. For example:

     Use the Filter parameter to create OPATH filters that identify the mailboxes. For more
     information, see Filterable Properties for the -Filter Parameter.

     Use a text file to specify the mailboxes. The text file contains one mailbox (email address,
     name, or other unique identifier) on each line like this:

       ebrunner@tailspintoys.com
       fapodaca@tailspintoys.com
       glaureano@tailspintoys.com
       hrim@tailspintoys.com

This example assigns the ABP named ABP_EngineeringDepartment to all user mailboxes where
the CustomAttribute11 attribute contains the value Engineering Department.

  PowerShell

  Get-Mailbox -Filter "RecipientType -eq 'UserMailbox' -and CustomAttribute11 -like
  '*Engineering Department'" | Set-Mailbox -AddressBookPolicy

<!-- p.2187 -->

  "ABP_EngineeringDepartment"

This example uses the text file C:\My Documents\Accounts.txt to assign the same ABP to the
specified user mailboxes.

  PowerShell

  Get-Content "C:\My Documents\Accounts.txt" | foreach {Set-Mailbox $_ -
  AddressBookPolicy "ABP_EngineeringDepartment"}

For detailed syntax and parameter information, see Get-Mailbox.

How do you know this worked?
To verify that you've successfully assigned an ABP to a mailbox, do any of these steps:

     In the EAC, go to Recipients > Mailboxes > select the mailbox > click Edit     > Mailbox
     features and verify the Address Book Policy value.

     In the Exchange Management Shell, replace <MailboxIdentity> with the identity of the
     mailbox (for example, name, alias, or email address), and run this command:

        PowerShell

<!-- p.2188 -->

         Get-Mailbox -Identity "<MailboxIdentity>" | Format-List AddressBookPolicy

     In the Exchange Management Shell, use the same filter that you used to identify the
     mailboxes. For example:

         PowerShell

         Get-Mailbox -Filter "RecipientType -eq 'UserMailbox' -and CustomAttribute11 -
         like '*Engineering Department'" | Format-Table -Auto
         Name,EmailAddress,AddressBookPolicy

     In the Exchange Management Shell, replace <ABPIdentity> with the name of the ABP, and
     run this command to get the DistinguishedName value:

         PowerShell

         Get-AddressBookPolicy -Identity <ABPIdentity> | Format-List DistinguishedName

     Then, use the DistinguishedName value of the ABP in this command to show all
     mailboxes where the ABP is assigned:

         PowerShell

         Get-Mailbox -ResultSize unlimited -Filter "AddressBookPolicy -eq
         '<DistinguishedName>'"

Use the Exchange Management Shell to install and
configure the Address Book Policy Routing Agent
Address Book Policy routing (ABP routing) controls how recipients are resolved in
organizations that use ABPs. When ABP routing is enabled, users that are assigned different
GALs appear as external recipients to each other.

ABP routing requires that you install and enable the Address Book Policy Routing Agent (ABP
Routing Agent) on all Mailbox servers in your organization, and enable ABP routing globally in
your organization. After you do this, it might take up to 30 minutes for messages to be
processed by the ABP Routing Agent.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Transport Agents" entry in the Mail flow permissions
topic.

<!-- p.2189 -->

Step 1: Install the ABP Routing agent
To install the ABP Routing Agent on the local Mailbox server, run this command on every
Mailbox server in the organization.

  PowerShell

  Install-TransportAgent -Name "ABP Routing Agent" -TransportAgentFactory
  "Microsoft.Exchange.Transport.Agent.AddressBookPolicyRoutingAgent.AddressBookPolic
  yRoutingAgentFactory" -AssemblyPath
  $env:ExchangeInstallPath\TransportRoles\agents\AddressBookPolicyRoutingAgent\Micro
  soft.Exchange.Transport.Agent.AddressBookPolicyRoutingAgent.dll

Note: You'll get a warning that the Transport service needs to be restarted for the changes to
take effect. But, don't restart the Transport service until you finish Step 2 (so you only have to
restart the Transport service once).

For detailed syntax and parameter information, see Install-TransportAgent.

Step 2: Enable the ABP Routing agent
To enable the ABP Routing Agent on the local Mailbox server, run this command on every
Mailbox server in the organization.

  PowerShell

  Enable-TransportAgent "ABP Routing Agent"

For detailed syntax and parameter information, see Enable-TransportAgent.

Step 3: Restart the Transport service
To restart the Transport service, run this command on every Mailbox server in the organization.

  PowerShell

  Restart-Service MSExchangeTransport

For detailed syntax and parameter information, see Get-TransportAgent.

Step 4: Enable ABP routing globally in the Exchange
organization

<!-- p.2190 -->

To enable ABP routing globally in the Exchange organization, run this command once on any
Mailbox server:

  PowerShell

  Set-TransportConfig -AddressBookPolicyRoutingEnabled $true

For detailed syntax and parameter information, see Set-TransportConfig.

Note: To disable ABP routing after you've enabled it, do these steps:

   1. Run this command once on any Mailbox server to globally disable ABP routing:

        PowerShell

        Set-TransportConfig -AddressBookPolicyRoutingEnabled $false

   2. Disable the ABP Routing Agent by running this command on every Mailbox server where
     the agent is installed:

        PowerShell

        Disable-TransportAgent "ABP Routing Agent"

   3. Run this command on every Mailbox server where the agent is installed:

        PowerShell

        Restart-Service MSExchangeTransport

How do you know this worked?
To verify that you've successfully installed and configured the ABP Routing Agent, use any of
these steps:

     Run this command on a Mailbox server to verify that ABP routing is enabled for the
     organization:

        PowerShell

        Get-TransportConfig | Format-List AddressBookPolicyRoutingEnabled

<!-- p.2191 -->

Run this command on every Mailbox server to verify that the ABP Routing Agent is
enabled:

  PowerShell

  Get-TransportAgent "ABP Routing Agent"

Have a user that's assigned an ABP send an email message to a user that's assigned a
different ABP, and verify that the sender's email address doesn't resolve to their display
name.

<!-- p.2192 -->

Messaging policy and compliance in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016         2019        Subscription Edition

Email has become a reliable and ubiquitous communication medium for information workers in
organizations of all sizes. Messaging stores and mailboxes have become repositories of
valuable data. It's important for organizations to formulate messaging policies that dictate the
fair use of their messaging systems, provide user guidelines for how to act on the policies, and
where required, provide details about the types of communication that may not be allowed.

Organizations must also create policies to manage email lifecycle, retain messages for the
length of time based on business, legal, and regulatory requirements, preserve email records
for litigation and investigation purposes, and be prepared to search and provide the required
email records to fulfill eDiscovery requests.

Messaging policy and compliance in Exchange
Server
The following table provides an overview of the messaging policy and compliance features in
Exchange 2016 and Exchange 2019 and includes links to topics that will help you learn about
and use these features.

                                                                                            ﾉ   Expand table

 Feature               Description                                                         Resources

 In-Place              In-Place Archiving helps you regain control of your                 In-Place Archiving
 Archiving             organization's messaging data by eliminating the need for           in Exchange Server
                       personal store (.pst) files and allowing users to store messages
                       in an archive mailbox accessible in Outlook 2010 and later and
                       Outlook on the web.

 In-Place Hold         When a reasonable expectation of litigation exists, organizations   In-Place Hold and
 and Litigation        are required to preserve electronically stored information,         Litigation Hold in
 Hold                  including email that's relevant to the case. In-Place Hold allows   Exchange Server
                       you to search and preserve messages matching query
                       parameters. Litigation Hold only allows you to place all items in
                       a mailbox on hold. For both types of holds, messages are
                       protected from permanent deletion, modification, and
                       tampering and can be preserved indefinitely or for a specified
                       period.

<!-- p.2193 -->

Feature            Description                                                           Resources

In-Place           In-Place eDiscovery allows you to search mailbox data across          In-Place eDiscovery
eDiscovery         your Exchange organization, preview search results, copy search       in Exchange Server
                   results to a Discovery mailbox, or export the results to a PST file

Administrator      Administrator audit logs enable you to keep a log of changes          Administrator audit
audit logging      made by administrators to Exchange server and organization            logging in
                   configuration and to Exchange recipients. You might use               Exchange Server
                   administrator audit logging as part of your change control
                   process or to track changes and access to configuration and
                   recipients for compliance purposes.

Mailbox audit      Because mailboxes can potentially contain sensitive, high             Mailbox audit
logging            business impact information and personally identifiable               logging in
                   information, it's important that you track who logs on to the         Exchange Server
                   mailboxes in your organization and what actions are taken. It's
                   especially important to track access to mailboxes by users other
                   than the mailbox owner (known as delegate users). Using
                   mailbox audit logging, you can log mailbox access by
                   administrators, delegates (including administrators with full
                   access permissions), and mailbox owners.

Data loss          Data loss prevention (DLP) in Exchange Server includes 80             Sensitive
prevention         sensitive information types that are ready for you to use in your     information types
                   DLP policies.                                                         in Exchange Server

Mail flow rules    Use mail flow rules to look for specific conditions in messages       Mail flow rule
(also known as     that pass through your organization and take action on them.          conditions and
transport rules)   You can use conditions and exceptions to define when a mail           exceptions
                   flow rule is applied, and then apply an action on messages when       (predicates) in
                   the conditions are met.                                               Exchange Server
                                                                                         Mail flow rule
                                                                                         actions in
                                                                                         Exchange Server

<!-- p.2194 -->

In-Place Archiving in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016      2019       Subscription Edition

In-Place Archiving in Exchange Server helps you regain control of your organization's
messaging data by eliminating the need for personal store (.pst) files and allowing users to
store messages in an archive mailbox. The archive mailbox is an additional mailbox that's
enabled for a user's primary mailbox. The archive mailbox is accessible in Outlook and Outlook
on the web (formerly known as Outlook Web App). Users can view an archive mailbox and
move or copy messages between their primary mailbox and their archive mailbox.

You can provision a user's archive mailbox on the same mailbox database as the user's primary
mailbox, a different mailbox database on the same Mailbox server, or on a mailbox database
on a different Mailbox server in the same Active Directory site. In Exchange hybrid
deployments, you can also provision a cloud-based archive mailbox for primary mailboxes
located in your on-premises organization.

Client access to archive mailboxes
The following table lists the client applications that can be used to access archive mailboxes.

                                                                                        ﾉ   Expand table

 Client                Access to archive mailbox?

 Outlook for Mac for   Yes. Users can copy or move items from their primary mailbox to their archive
 Office 365            mailbox, and can also use retention policies to move items to the archive.
 Outlook 2016 for      Outlook doesn't create a local copy of the archive mailbox on a user's computer,
 Mac or later          even if it's configured to use Cached Exchange Mode. Users can access an archive
                       mailbox in online mode only.
 Microsoft 365 Apps
 for enterprise

 Outlook 2013 or
 later

 Outlook on the
 web

 Exchange              No
 ActiveSync

  ７ Note

<!-- p.2195 -->

          In-Place Archiving is a premium feature and requires an Exchange Enterprise client
          access license (CAL). For details about how to license Exchange, see Exchange
          licensing FAQs   .
          For details about the versions of Outlook that are required to access an archive
          mailbox, see Outlook license requirements for Exchange features      .

Moving messages to the archive mailbox
There are several ways to move messages from a user's primary mailbox to their archive
mailbox:

     Move or copy messages manually: Users can manually move or copy messages from
     their primary mailbox or a .pst file to their archive mailbox. The archive mailbox appears
     as another mailbox Outlook and Outlook on the web or like a mounted .pst file in
     Outlook.

     Move or copy messages using Inbox rules: Users can create Inbox rules in Outlook to
     automatically move messages to a folder in their archive mailbox.

     Move messages using retention policies: You can use retention policies to automatically
     move messages to the archive mailbox. Users can also apply personal tags to move
     messages to their archive mailbox. For details about archive and retention policies, see
     the next section in this topic.

     Import messages from .pst files: In Exchange Server, you can use a mailbox import
     request to import messages from a .pst file to a user's archive or primary mailbox. For
     details, see Mailbox imports and exports in Exchange Server.

Archiving and retention policies
In Exchange Server, you can apply archive policies to a mailbox to automatically move
messages from a user's primary mailbox to the archive mailbox after a specified period. Archive
policies are implemented by creating retention tags that use the Move to Archive retention
action.

Messages are moved to a folder in the archive mailbox that has the same name as the source
folder in the primary mailbox. If a folder with the same name doesn't exist in the archive
mailbox, it's created when the Managed Folder Assistant moves a message. Re-creating the
same folder hierarchy in the archive mailbox allows users to find messages easily.

<!-- p.2196 -->

To learn more about retention policies, retention tags, and the Move to Archive retention
action, see Retention tags and retention policies in Exchange Server.

Default MRM policy
Exchange Server Setup creates a default archive and retention policy named Default MRM
Policy. This policy contains retention tags that have the Move to Archive action, as shown in
the following table.

                                                                                         ﾉ   Expand table

 Retention tag         Tag type        Description
 name

 Default 2 year        Default (DPT)   Messages are automatically moved to the archive mailbox after
 move to archive                       two years. Applies to items in the entire mailbox that don't have a
                                       retention tag applied explicitly or inherited from the folder.

 Personal 1 year       Personal        Messages are automatically moved to the archive mailbox after
 move to archive                       one year.

 Personal 5 year       Personal        Messages are automatically moved to the archive mailbox after
 move to archive                       five years.

 Personal never        Personal        Messages are never moved to the archive mailbox.
 move to archive

 Recoverable Items     Recoverable     Messages are moved from the Recoverable Items folder in the
 14 days move to       Items Folder    user's primary mailbox to the Recoverable Items folder in the
 archive                               archive mailbox. Users attempting to recover deleted items in their
                                       archive mailbox must use the Recover Deleted Items tool in the
                                       archive mailbox.

If you enable an In-Place Archive for a mailbox user and the mailbox doesn't already have a
retention policy assigned, the default archive and retention policy is automatically assigned.
After the Managed Folder Assistant processes the mailbox, these tags become available to the
user, who can then tag folders or messages to be moved to the archive mailbox. By default,
email messages from the entire mailbox are moved to the archive after two years.

Before provisioning archive mailboxes for your users, we recommend that you inform them
about the archive policies that will be applied to their mailbox and provide subsequent training
or documentation to meet their needs. This should include details about the following:

     Functionality available within the archive, and the default archive retention policies.

     Information about when messages are automatically moved to the archive.

<!-- p.2197 -->

     Information about the folder hierarchy created in the archive mailbox.

     How to apply personal tags (displayed in the Archive policy menu in Outlook and Outlook
     on the web).

  ７ Note

  If you apply a retention policy to users who have an archive mailbox, the retention policy
  replaces the default MRM policy. You can create one or more retention tags with the
  Move to Archive action, and then link the tags to the retention policy. You can also add
  the default Move to Archive tags (which are created by Setup and linked to the Default
  MRM Policy) to any retention policies you create.

Archive quotas
Archive mailboxes are designed so that users can store historical messaging data outside their
primary mailbox. Often, users use .pst files due to low mailbox storage quotas and the
restrictions imposed when these quotas are exceeded. For example, users can be prevented
from sending messages when their mailbox size exceeds the Prohibit send quota. Similarly,
users can be prevented from sending and receiving messages when their mailbox size exceeds
the Prohibit send and receive quota.

To eliminate the need for .pst files, you can provide an archive mailbox with storage limits that
meet the user's requirements. However, you may still want to retain some control of the
storage quotas and growth of archive mailboxes to help monitor costs and expansion.

To help with this control, you can configure archive mailboxes with an archive warning quota
and an archive quota. When an archive mailbox exceeds the specified archive warning quota, a
warning event is logged in the Application event log. When an archive mailbox exceeds the
specified archive quota, messages are no longer moved to the archive, a warning event is
logged in the Application event log, and a quota message is sent to the mailbox user. By
default, in Exchange Server, the archive warning quota is set to 90 GB and the archive quota is
set to 100 GB.

The following table lists the events logged and warning messages sent when the archive
warning quota and archive quota are met.

                                                                                 ﾉ   Expand table

<!-- p.2198 -->

 Quota      Event   Type      Source                        Category    Message
            ID

 Archive    10022   Warning   MSExchangeMailboxAssistants   Managed     The archive mailbox
 warning                                                    Folder      '<Display Name>:<GUID>:
 quota                                                      Assistant   <Mailbox Database>:<Server
                                                                        FQDN>' exceeded the archive
                                                                        warning quota '<Archive
                                                                        warning quota>'. Archive
                                                                        mailbox size is '<Size>'
                                                                        bytes.

 Archive    8537    Warning   MSExchangeIS                  General     The archive mailbox for
 quota                                                                  <Legacy DN> has exceeded
                                                                        the maximum archive mailbox
                                                                        size. You can't copy or
                                                                        move items into the archive
                                                                        mailbox. All message
                                                                        retention actions that move
                                                                        items to the archive
                                                                        mailbox will fail, and the
                                                                        primary mailbox may contain
                                                                        items with expired
                                                                        retention tags until the
                                                                        archive mailbox is within
                                                                        the maximum size limit. The
                                                                        mailbox owner should be
                                                                        notified about the
                                                                        condition of the archive
                                                                        mailbox.

In-Place Archiving and other Exchange features
This section explains the functionality between In-Place Archiving and various Exchange
features:

     Exchange Search: The ability to quickly search messages becomes even more critical with
     archive mailboxes. For Exchange Search, there's no difference between the primary and
     archive mailbox. Content in both mailboxes is indexed. Because the archive mailbox isn't
     cached on a user's computer (even when using Outlook in Cached Exchange Mode),
     search results for the archive are always provided by Exchange Search. When searching
     the entire mailbox in Outlook, search results include the users' primary and archive
     mailbox.

<!-- p.2199 -->

     In-Place eDiscovery: When a discovery manager performs an In-Place eDiscovery search,
     users' archive mailboxes are also searched. There's no option to exclude archive
     mailboxes when creating a discovery search from the Exchange admin center (EAC). When
     using the Exchange Management Shell to create a discovery search, you can exclude the
     archive by using the DoNotIncludeArchive switch. For details, see New-MailboxSearch. To
     learn more, see In-Place eDiscovery in Exchange Server.

     In-Place Hold and Litigation Hold: When you put a mailbox on In-Place Hold or
     Litigation Hold, the hold is placed on both the primary and the archive mailbox. To learn
     more, see In-Place Hold and Litigation Hold in Exchange Server.

     Recoverable Items folder: The archive mailbox contains its own Recoverable Items folder
     and is subject to the same Recoverable Items folder quotas as the primary mailbox. To
     learn more about recoverable items, see Recoverable Items folder in Exchange Server.

     Archiving Skype for Business content in Exchange: You can archive instant messaging
     conversations and shared online meeting documents in the user's primary mailbox. The
     mailbox must reside on an Exchange Mailbox server and you must have Skype for
     Business Server 2015 deployed in your organization.

Managing archive mailboxes
In Exchange Server, creating and managing archive mailboxes is integrated with common
mailbox management tasks. For step by step procedures, see Manage In-Place Archives in
Exchange Server.

     Creating an archive mailbox: You can enable an archive mailbox for an existing mailbox
     or you can create an archive mailbox when creating a new mailbox.

     Moving an archive mailbox: You can move a user's archive mailbox to another mailbox
     database on the same Mailbox server or to another server, independent of the primary
     mailbox. To move a user's archive mailbox, you must create a mailbox move request. For
     details, see Manage on-premises mailbox moves in Exchange Server.

     Disabling an archive mailbox: You may want to disable a user's archive mailbox for
     troubleshooting purposes or if you're moving the primary mailbox to a version of
     Exchange that doesn't support In-Place Archiving. Disabling an archive is similar to
     disabling a primary mailbox. In on-premises deployments, a disabled archive mailbox is
     retained in the mailbox database until the deleted mailbox retention period for that
     database is reached. During this period, you can reconnect the same disabled archive
     mailbox to a user's primary mailbox. When the deleted mailbox retention period is
     reached, the disconnected archive mailbox is purged from the mailbox database.

<!-- p.2200 -->

Retrieving mailbox statistics and folder statistics: You can retrieve mailbox statistics and
mailbox folder statistics for a user's archive mailbox by using the Archive switch with the
Get-MailboxStatistics and Get-MailboxFolderStatistics cmdlets.

Test archive connectivity: In Exchange Server, you can use the Test-ArchiveConnectivity
cmdlet to test connectivity to a specified user's on-premises or cloud-based archive
mailbox.
