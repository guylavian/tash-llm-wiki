---
title: "Exchange Server — pages 2121-2160"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2121-2160
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2121-2160
family: exchange
documentKind: "doc"
abstract: "Get-OfflineAddressBook -Identity \"Default Offline Address Book\" | Format-List This example returns values for the specified properties on all OABs in your organization. PowerShell Get-OfflineAddressBook | Format-List Name,GUID,AddressLists,GeneratingMailbox,IsDefault,VirtualDire"
---

# Exchange Server — pages 2121-2160

<!-- p.2121 -->

  Get-OfflineAddressBook -Identity "Default Offline Address Book" | Format-List

This example returns values for the specified properties on all OABs in your organization.

  PowerShell

  Get-OfflineAddressBook | Format-List
  Name,GUID,AddressLists,GeneratingMailbox,IsDefault,VirtualDirectories,GlobalWebDis
  tributionEnabled,ShadowMailboxDistributionEnabled

For detailed syntax and parameter information, see Get-OfflineAddressBook.

Use the Exchange Management Shell to create
offline address books
If you've created multiple address lists, you can use OABs to make the address lists available to
users when they're offline.

To create new offline address books, use the following syntax:

  PowerShell

  New-OfflineAddressBook -Name "<Name>" -AddressLists "
  <GlobalAddressListOrAddressList1>","<GlobalAddressListOrAddressList2>,..." [-
  GlobalWebDistributionEnabled $true] [-GeneratingMailbox
  <OrganizationMailboxIdentity>] [-IsDefault $true] [-
  ShadowMailboxDistributionEnabled $true]

This example creates a new OAB named Contoso Executives OAB with the following properties:

     The Default Global Address List and Contoso Executives Address List are included in the
     OAB.

     All OAB virtual directories in the organization can accept requests to download the OAB.

     The organization mailbox that's responsible for generating the OAB is
     SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c} (we didn't use the

     GeneratingMailbox parameter to specify a different organization mailbox).

     The OAB isn't used by mailboxes and mailbox databases that don't have an OAB specified
     (we didn't use the IsDefault parameter with the value $true ).

<!-- p.2122 -->

     Shadow distribution for the OAB is disabled (read-only copies of the OAB aren't copied to
     all other organization mailboxes, because we didn't use the
     ShadowMailboxDistributionEnabled parameter with the value $true ).

  PowerShell

  New-OfflineAddressBook -Name "Contoso Executives OAB" -AddressLists "Default
  Global Address List","Contoso Executives Address List" -
  GlobalWebDistributionEnabled $true

For detailed syntax and parameter information, see New-OfflineAddressBook.

How do you know this worked?
To verify that you've successfully created the OAB, run the following command to verify the
property values:

  PowerShell

  Get-OfflineAddressBook | Format-List
  Name,AddressLists,GeneratingMailbox,IsDefault,VirtualDirectories,GlobalWebDistribu
  tionEnabled

Use the Exchange Management Shell to modify
offline address books
To modify OABs, use the following syntax:

  PowerShell

  Set-OfflineAddressBook -Identity "<OABIdentity>" [-Name <Name>] [-AddressLists "
  <GlobalAddressListOrAddressList1>","<GlobalAddressListOrAddressList2>,..."] [-
  VirtualDirectories $null] [-GlobalWebDistributionEnabled $true] [-
  GeneratingMailbox <OrganizationMailboxIdentity>] [-IsDefault $true] [-
  ShadowMailboxDistributionEnabled <$true | $false>]

For detailed syntax and parameter information, see Set-OfflineAddressBook.

Use the Exchange Management Shell to configure the default
offline address book

<!-- p.2123 -->

By default, the automatically created OAB named Default Offline Address Book is the default
OAB. The default OAB is used by:

     Mailboxes in mailbox databases where the database has no OAB assigned (by default, all
     databases)

     Mailboxes without an address book policy (ABP) assigned, or where the assigned ABP
     policy has no OAB defined (by default, there are no ABPs).

     Mailboxes without an OAB assigned (by default, all mailboxes)

This example configures the OAB named Contoso Executives OAB to be the default OAB.

  PowerShell

  Set-OfflineAddressBook -Identity "Contoso Executives OAB" -IsDefault $true

Use the Exchange Management Shell to add and remove
address lists from offline address books
When you modify the address lists that are configured in an OAB, the values that you specify
will replace any address lists in the OAB. To add address lists to the OAB, specify the current
address lists plus the ones you want to add. To remove address lists from the OAB, specify the
current address lists minus the ones you want to remove.

In this example, the OAB named Marketing OAB is already configured with Address List 1 and
Address List 2. To keep those address lists and add Address List 3, run the following command:

  PowerShell

  Set-OfflineAddressBook -Identity "Marketing OAB" -Address Lists "Address
  List1","Address List 2","Address List 3"

Similarly, to keep the OAB configured with Address List 1 and Address 2, but remove Address
List 3, run the following command:

  PowerShell

  Set-OfflineAddressBook -Identity "Marketing OAB" -AddressLists "Address List
  1","Address List 2"

<!-- p.2124 -->

Use the Exchange Management Shell to change the
organization mailbox that's responsible for generating an
offline address book
Typically, you only need to configure multiple organization mailboxes if you have Exchange
servers in different Active Directory sites. You can configure multiple OABs to use the same
organization mailbox, but you can't configure an OAB to use more than one organization
mailbox. If you need multiple copies of the OAB in different locations, enable shadow
distribution for the OAB. For more information, see the Use the Exchange Management Shell to
enable shadow distribution for offline address books section in this topic.

This example changes the organization mailbox that's responsible for generating the OAB
named Default Offline Address Book.

  PowerShell

  Set-OfflineAddressBook -Identity "Default Offline Address Book" -GeneratingMailbox
  OABGen2

Note: To configure an arbitration mailbox that you can use as an organization mailbox, see the
Use the Exchange Management Shell to create organization mailboxes section in this topic.

Use the Exchange Management Shell to configure any virtual
directory in the organization to accept download requests for
the OAB
The Client Access (frontend) services on any Mailbox server can proxy the OAB download
request to the correct location. The OAB files are downloaded from the backend location
%ExchangeInstallPath%ClientAccess\OAB\<OAB GUID> on the Mailbox server that holds the active

copy of the OAB's designated organization mailbox (or from the server that holds a shadow
copy of the OAB).

This example modifies the OAB named Default Offline Address Book to allow any virtual
directory in the organization to accept requests to download the OAB.

   1. Run the following command:

        PowerShell

        Set-OfflineAddressBook -Identity "Default Offline Address Book" -
        VirtualDirectories $null

<!-- p.2125 -->

   2. Run the following command:

        PowerShell

        Set-OfflineAddressBook -Identity "Default Offline Address Book" -
        GlobalWebDistributionEnabled $true

Use the Exchange Management Shell to enable shadow
distribution for offline address books
Before you enable shadow distribution to distribute a read-only copy of the OAB to
organization mailboxes in different Active Directory sites, verify that an organization mailbox
exists in each site. To create organization mailboxes, see the Use the Exchange Management
Shell to create organization mailboxes section in this topic.

This example enables shadow distribution for the OAB named Contoso Executives OAB.

  PowerShell

  Set-OfflineAddressBook -Identity "Contoso Executives OAB" -
  ShadowMailboxDistributionEnabled $true

How do you know this worked?
To verify that you've successfully modified the OAB, run the following command to verify the
property values:

  PowerShell

  Get-OfflineAddressBook | Format-List
  Name,AddressLists,GeneratingMailbox,IsDefault,VirtualDirectories,GlobalWebDistribu
  tionEnabled,

Use the Exchange Management Shell to update
offline address books
Changes in an OAB aren't available to users until the scheduled OAB generation (by default,
every 8 hours). If you don't want to wait, you can use the procedures in this topic to
immediately update an OAB.

<!-- p.2126 -->

To change the OAB generation schedule, see Change the offline address book generation
schedule in Exchange Server.

To update an OAB, use the following syntax:

  PowerShell

  Update-OfflineAddressBook -Identity <OABIdentity>

This example updates the OAB named Default Offline Address Book.

  PowerShell

  Update-OfflineAddressBook -Identity "Default Offline Address Book"

This example updates all OABs.

  PowerShell

  Get-OfflineAddressBook | Update-OfflineAddressBook

For detailed syntax and parameter information, see Update-OfflineAddressBook.

Use the Exchange Management Shell to remove
offline address books
To remove OABs, use the following syntax:

  PowerShell

  Remove-OfflineAddressBook -Identity <OABIdentity>

This example removes the OAB named Contoso Executives OAB.

  PowerShell

  Remove-OfflineAddressBook -Identity "Contoso Executives OAB"

Note: If the removed OAB is the default OAB, you need to create or configure another OAB as
the default (the IsDefault parameter value is $true ).

How do you know this worked?

<!-- p.2127 -->

To verify that you've successfully removed the OAB, run the following command to verify that
the OAB is gone.

  PowerShell

  Get-OfflineAddressBook

Use the Exchange Management Shell to find
organization mailboxes
Only organization mailboxes can generate OABs. An organization mailbox is an arbitration
mailbox that has the OrganizationCapabilityOABGen value in the PersistedCapability property.
To find the organization mailboxes in your organization, run the following command:

  PowerShell

  Get-Mailbox -Arbitration | where {$_.PersistedCapabilities -like "*OAB*"} |
  Format-List Name,ServerName,PersistedCapabilities

To find the organization mailbox that's used to generate an OAB, run the following command:

  PowerShell

  Get-OfflineAddressBook | Format-List Name,AddressLists,GeneratingMailbox,IsDefault

Use the Exchange Management Shell to create
organization mailboxes
Typically, you only need to create multiple arbitration mailboxes in multi-site Exchange
organizations. You can have an organization mailbox in each site, and you can configure
shadow distribution for an OAB (so a read only copy of the OAB is stored in all organization
mailboxes). For more information, see Use the Exchange Management Shell to enable shadow
distribution for offline address books.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Recipient Provisioning Permissions" section in the
Recipients Permissions topic.

   1. Create an arbitration mailbox by using the following syntax:

        PowerShell

<!-- p.2128 -->

        New-Mailbox -Arbitration -Name <UniqueName> -UserPrincipalName <UPN> [-
        Database <DBIdentity>] [-Alias <Alias>] [-DisplayName "<DisplayName>"]

     This example creates a new arbitration mailbox named OAB Gen 2, with the UPN (account
     name) oabgen2@contoso.com, in the default database.

        PowerShell

        New-Mailbox -Arbitration -Name "OAB Gen 2" -UserPrincipalName
        oabgen2@contoso.com

   2. Turn the arbitration mailbox into an organization mailbox by using the following syntax:

        PowerShell

        Set-Mailbox -Identity <MailboxIdentity> -Arbitration -OABGen $true -
        MaxSendSize 1GB

     This example turns the OAB Gen 2 arbitration mailbox into an organization mailbox.

        PowerShell

        Set-Mailbox -Identity "OAB Gen 2" -Arbitration -OABGen $true -MaxSendSize 1GB

   3. To activate the OAB generation capabilities of the new organization mailbox, run Update-
     OfflineAddressBook for any OAB in the organization. For example:

        PowerShell

        Update-OfflineAddressBook -Identity "Default Offline Address Book"

How do you know this worked?
To verify that you've successfully created an organization mailbox, run the following command
and verify the mailbox is returned:

  PowerShell

  Get-Mailbox -Arbitration | where {$_.PersistedCapabilities -like "*OAB*"} |
  Format-List Name,ServerName,PersistedCapabilities

<!-- p.2129 -->

Assign offline address books to mailbox databases
When you assign an OAB to a mailbox database, all mailboxes in the databases will use that
OAB instead of the default OAB, unless the mailbox has an OAB assigned. By default, no OAB is
assigned to a mailbox database.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Mailbox databases" entry in the Recipients
Permissions topic.

Use the EAC to assign an offline address book to a mailbox
database
   1. Open the EAC, and go to Servers > Databases. Select the database from the list, and then
     click Edit (    ).

   2. The Mailbox Database window opens. Click the Client settings tab, and then click Browse
     next to Offline address book.

<!-- p.2130 -->

   3. In the Select Offline Address Book window that opens, select the OAB from the list, and
     click OK.

   4. Back in the Mailbox Database window, click Save.

Use the Exchange Management Shell to assign an offline
address book to a mailbox database
Use the following syntax:

  PowerShell

  Set-MailboxDatabase -Identity <DatabaseIdentity> -OfflineAddressBook <OABIdentity>

This example assigns the OAB named Contoso Executives OAB to the mailbox database named
MBX DB02.

  PowerShell

  Set-MailboxDatabase -Identity "MBX DB02" -OfflineAddressBook "Contoso Executives
  OAB"

How do you know this worked?
To verify that you've successfully assigned an OAB to a mailbox database, use either of the
following procedures:

<!-- p.2131 -->

     In the EAC, go to Servers > Databases. Select the database from the list, and then click
     Edit (    ). In the Mailbox database window opens, click the Client settings tab, and verify
     that the OAB is listed in Offline address book.

     In the Exchange Management Shell, run the following command:

        PowerShell

        Get-MailboxDatabase | Format-Table -Auto Name,OfflineAddressBook

Use the Exchange Management Shell to assign
offline address books to mailboxes
When you assign an OAB to a mailbox, the default OAB and the OAB that's assigned to the
mailbox database (if any) aren't used by the mailbox. By default, no OAB is assigned to a
mailbox.

Note: If the mailbox has an address book policy (ABP) assigned, and the ABP has an OAB
defined, the OAB that's directly assigned to the mailbox will take precedence over the ABP. For
more information ABPs, see Address book policies in Exchange Server.

You need to be assigned permissions before you can perform this procedure or procedures. To
see what permissions you need, see the "Recipient Provisioning Permissions" section in the
Recipients Permissions topic.

To assign an OAB to a mailbox, use the following syntax:

  PowerShell

  Set-Mailbox -Identity <MailboxIdentity> -OfflineAddressBook <OABIdentity>

This example assigns the OAB named Contoso Executives to the mailbox laura@contoso.com.

  PowerShell

  Set-Mailbox -Identity laura@contoso.com -OfflineAddressBook "Contoso Executives
  OAB"

This example assigns the OAB named Contoso US to a filtered list of mailboxes.

  PowerShell

<!-- p.2132 -->

  $USContoso = Get-User -ResultSize Unlimited -Filter "RecipientType -eq
  'UserMailbox' -and Company -eq 'Contoso' -and CountryOrRegion -eq 'US'";
  $USContoso | foreach {Set-Mailbox $_.Identity -OfflineAddressBook "Contoso United
  States"}

How do you know this worked?
To verify that you've successfully assigned an OAB to a mailbox, replace <MailboxIdentity> with
the identity of the mailbox, and run the following command:

  PowerShell

  Get-Mailbox -Identity "<MailboxIdentity>" | Format-Table -Auto
  Name,OfflineAddressBook

<!-- p.2133 -->

Address lists in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

An address list is a collection of mail-enabled recipient objects from Active Directory. Address
lists are based on recipient filters, and are basically unchanged from Exchange 2010. You can
filter by recipient type (for example, mailboxes and mail contacts), recipient properties (for
example, Company or State or Province), or both. Address lists aren't static; they're updated
dynamically. When you create or modify recipients in your organization, they're automatically
added to the appropriate address lists. These are the different types of address lists that are
available:

      Global address lists (GALs): The built-in GAL that's automatically created by Exchange
      includes every mail-enabled object in the Active Directory forest. You can create
      additional GALs to separate users by organization or location, but a user can only see and
      use one GAL.

      Address lists: Address lists are subsets of recipients that are grouped together in one list,
      which makes them easier to find by users. Exchange comes with several built-in address
      lists, and you can create more based on you organization's needs.

      Offline address books (OABs): OABs contain address lists and GALs. OABs are used by
      Outlook clients in cached Exchange mode to provide local access to address lists and
      GALs for recipient look-ups. For more information, see Offline address books in Exchange
      Server.

Users in your organization use address lists and the GAL to find recipients for email messages.
Here's an example of what address lists look like in Outlook 2016:

<!-- p.2134 -->

For procedures related to address lists, see Procedures for address lists in Exchange Server.

Recipient filters for address lists
Recipient filters identify the recipients that are included in address lists and GALs. There are two
basic options: precanned recipient filters and custom recipient filters. These are basically the
same recipient filtering options that are used by dynamic distribution groups and email
address policies. The following table summarizes the differences between the two filtering
methods.

                                                                                    ﾉ      Expand table

 Recipient     User interface         Filterable recipient properties   Filter operators
 filtering
 method

 Precanned     Address lists:         Limited to:                       Property values require an
 recipient     Exchange admin               Recipient type (All         exact match. Wildcards and
 filters       center (EAC) and the         recipient types or any      partial matches aren't
               Exchange                     combination of user         supported. For example,
               Management Shell             mailboxes, resource         "Sales" doesn't match the
                                            mailboxes, mail contacts,   value "Sales and Marketing".
               GALs: Exchange               mail users, and groups)     Multiple values of the same
               Management Shell             Company                     property always use the or
               only                         Custom Attribute 1 to 15    operator. For example,
                                            Department                  "Department equals Sales or

<!-- p.2135 -->

 Recipient     User interface          Filterable recipient properties       Filter operators
 filtering
 method

                                             State or Province               Department equals
                                                                             Marketing".

                                                                             Multiple properties always use
                                                                             the and operator. For
                                                                             example, "Department equals
                                                                             Sales and Company equals
                                                                             Contoso".

 Custom        Exchange                You can use virtually any             You use OPATH filter syntax to
 recipient     Management Shell        available recipient attributes. For   specify any available Windows
 filters       only                    more information, see Filterable      PowerShell filter operators.
                                       Properties for the -RecipientFilter   Wildcards and partial matches
                                       Parameter.                            are supported.

Notes:

      You can't used precanned filters and customized filters at the same time.

      The recipient's location in Active Directory (the organizational unit or container) is
      available in both precanned and custom recipient filters.

      If an address list uses custom recipient filters instead of precanned filters, you can see the
      address list in the EAC, but you can't modify or remove it by using the EAC.

      You can hide recipients from all address lists and GALs. For more information, see Hide
      recipients from address lists.

Global address lists
By default, a new installation of Exchange Server creates an GAL named Default Global Address
List that's the primary repository of all recipients in the Exchange organization. Typically, most
organizations have only one GAL, because users can only see and use one GAL in Outlook and
Outlook on the web (formerly known as Outlook Web App). You might need to create multiple
GALs if you want to prevent groups of recipients from seeing each other (for example, you
single Exchange organization contains two separate companies). If you plan on creating
additional GALs, consider the following issues:

      You can only use the Exchange Management Shell to create, modify, remove, and update
      GALs.

<!-- p.2136 -->

         The GAL that users see in Outlook and Outlook on the web is named Global Address List,
         even though the default GAL is named Default Global Address List, and any new GALs
         that you create will require a unique name (users can't tell which GAL that they're using
         by name).

         Users can only see a GAL that they belong to (the recipient filter of the GAL includes
         them). If a user belongs to multiple GALs, they'll still see only one GAL based on the
         following conditions:

           The user needs permissions to view the GAL. You assign user permissions to GALs by
           using address book policies (ABPs). For more information, see Address book policies in
           Exchange Server.

           If a user is still eligible to see multiple GALs, only the largest GAL is used (the GAL that
           contains the most recipients).

           Each GAL needs a corresponding offline address book (OAB) that includes the GAL. To
           create OABs, see Use the Exchange Management Shell to create offline address books.

Default address lists
By default, Exchange comes with five built-in address lists and one GAL. These address lists are
described in the following table. Note that by default, system-related mailboxes like arbitration
mailboxes and public folder mailboxes are hidden from address lists.

                                                                                         ﾉ     Expand table

 Name             Type      Description                  Recipient filter used

 All Contacts     Address   Includes all mail contacts   "Alias -ne $null -and (ObjectCategory -like
                  list      in the organization. To      'person' -and ObjectClass -eq 'contact')"
                            learn more about mail
                            contacts, see Recipients.

 All              Address   Includes all distribution    "Alias -ne $null -and ObjectCategory -like
 Distribution     list      groups and mail-enabled      'group'"
 Lists                      security groups in the
                            organization. To learn
                            more about mail-
                            enabled groups, see
                            Recipients.

 All Rooms        Address   Includes all room            "Alias -ne $null -and (RecipientDisplayType -eq
                  list      mailboxes. Equipment         'ConferenceRoomMailbox' -or RecipientDisplayType
                            mailboxes aren't             -eq 'SyncedConferenceRoomMailbox')"
                            included. To learn more

<!-- p.2137 -->

 Name           Type      Description                  Recipient filter used

                          about room and
                          equipment (resource)
                          mailboxes, see
                          Recipients.

 All Users      Address   Includes all user            "((Alias -ne $null) -and (((((((ObjectCategory -
                list      mailboxes, linked            like 'person') -and (ObjectClass -eq 'user') -and
                          mailboxes, remote            (-not(Database -ne $null)) -and (-
                          mailboxes (Microsoft 365     not(ServerLegacyDN -ne $null)))) -or
                          or Office 365 mailboxes),    (((ObjectCategory -like 'person') -and
                          shared mailboxes, room       (ObjectClass -eq 'user') -and (((Database -ne
                          mailboxes, equipment         $null) -or (ServerLegacyDN -ne $null))))))) -and
                          mailboxes, and mail          (-not(RecipientTypeDetailsValue -eq
                          users in the organization.   'GroupMailbox')))))"
                          To learn more about
                          these recipient types, see
                          Recipients.

 Default        GAL       Includes all mail-enabled    "((Alias -ne $null) -and (((ObjectClass -eq
 Global                   recipient objects in the     'user') -or (ObjectClass -eq 'contact') -or
 Address List             organization (users,         (ObjectClass -eq 'msExchSystemMailbox') -or
                          contacts, groups,            (ObjectClass -eq 'msExchDynamicDistributionList')
                          dynamic distribution         -or (ObjectClass -eq 'group') -or (ObjectClass -
                          groups, and public           eq 'publicFolder'))))"
                          folders.

 Public         Address   Includes all mail-enabled    "Alias -ne $null -and ObjectCategory -like
 Folders        list      public folders in your       'publicFolder'"
                          organization. Access
                          permissions determine
                          who can view and use
                          public folders. For more
                          information about public
                          folders, see Public
                          folders.

Custom address lists
An Exchange organization might contain thousands of recipients, so the built-in address lists
could become quite large. To prevent this, you can create custom address lists to help users
find what they're looking for.

For example, consider a company that has two large divisions in one Exchange organization:

     Fourth Coffee, which imports and sells coffee beans.

<!-- p.2138 -->

         Contoso, Ltd, which underwrites insurance policies.

For most day-to-day activities, employees at Fourth Coffee don't communicate with employees
at Contoso, Ltd. Therefore, to make it easier for employees to find recipients who exist only in
their division, you can create two new custom address lists: one for Fourth Coffee and one for
Contoso, Ltd. However, if an employee is unsure about where recipient exists, they can search
in the GAL, which contains all recipients from both divisions.

You can also create address lists under other address lists. For example, you can create an
address list that contains all recipients in Manchester, and you can create another address list
under Manchester named Sales that contains only sales people in the Manchester office. You
can also move address lists back to the root, or under other address lists after you've created
them. For more information, see Use the Exchange Management Shell to move address lists.

Best practices for creating additional address lists
Although address lists are useful tools for users, poorly planned address lists can cause
frustration. To make sure that your address lists are practical for users, consider the following
best practices:

         Address lists should make it easier for users to find recipients.

         Avoid creating so many address lists that users can't tell which list to use.

         Use a naming convention and location hierarchy for your address lists so users can
         immediately tell what the list is for (which recipients are included in the list). If you have
         difficulty naming your address lists, create fewer lists and remind users that they can find
         anyone in your organization by using the GAL.

For detailed instructions about creating address lists in Exchange Server, see Create address
lists.

Update address lists
After you create or modify an address list, you need to update the membership.

If the address list contains a large number of recipients (our recommendation is more than
3000), you should use the Exchange Management Shell to update the address list (not the
EAC). For more information, see Update address lists.

To update a GAL, you always need to use the Exchange Management Shell. For more
information, see Use the Exchange Management Shell to update global address lists.

<!-- p.2139 -->

Procedures for address lists in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016        2019     Subscription Edition

Address lists and global address lists (GALs) are collections of mail-enabled recipient objects
from Active Directory. You can create or modify GALs, and update using the tools available in
the Exchange admin center (EAC) and the Exchange Management Shell. For more information,
see Address lists in Exchange Server.

These are the address list and GAL procedures that you'll find in this topic:

      Global address list procedures

         Use the Exchange Management Shell to update global address lists

         Use the Exchange Management Shell to view members of global address lists

         Use the Exchange Management Shell to create global address lists

         Use the Exchange Management Shell to modify global address lists

         Use the Exchange Management Shell to remove global address lists

      Address list procedures

         Update address lists

         View the members of address lists

         Create address lists

         Modify address lists

         Use the Exchange Management Shell to move address lists

         Remove address lists

         Hide recipients from address lists

Recipient filters in the EAC

Recipient filters in the Exchange Management Shell

What do you need to know before you begin?

<!-- p.2140 -->

     Estimated time to complete each procedure: 5 minutes.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Address lists" entry in the Email
     address and address book permissions topic.

     You can do some of the procedures in this topic by using the EAC. For more information
     about the EAC, see Exchange admin center in Exchange Server. Some procedures require
     the Exchange Management Shell. To learn how to open the Exchange Management Shell
     in your on-premises Exchange organization, see Open the Exchange Management Shell.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online     , or Exchange Online Protection .

Global address list procedures
All procedures for modifying or updating a GAL require the Exchange Management Shell.

Use the Exchange Management Shell to update global
address lists
After you create or modify a GAL, you need to update its membership. Updating a GAL only
starts the update process. It may take several hours for the GAL update to be completed.

To update a GAL, use the following syntax:

  PowerShell

  Update-GlobalAddressList -Identity <GALIdentity>

This example updates the GAL named Contoso GAL.

  PowerShell

  Update-AddressList -Identity "Contoso GAL"

This example updates all GALs in the organization that require updates.

<!-- p.2141 -->

  PowerShell

  Get-GlobalAddressList | where {$_.RecipientFilterApplied -eq $false} | Update-
  GlobalAddressList

For detailed syntax and parameter information, see Update-GlobalAddressList.

How do you know this worked?
To verify that you've successfully updated the GAL, replace <GALIdentity> with the name of the
address list, and run the following command to verify that the RecipientFilterApplied property
value is present:

  PowerShell

  Get-AddressList -Identity <GALIdentity> | Format-Table -Auto
  Name,RecipientFilterApplied

Use the Exchange Management Shell to view members of
global address lists
     Technically, this procedure returns all recipients (including hidden recipients) that match
     the recipient filters for the GAL. The recipients that are actually visible in the GAL have the
     HiddenFromAddressListsEnabled property value False .

     If the GAL isn't up to date (the RecipientFilterApplied property has the value False ), you
     should update the GAL before you view the members. For more information, see the
     previous section.

To view the members of a GAL, use the following syntax:

  PowerShell

  $GAL = Get-GlobalAddressList -Identity <GALIdentity>; Get-Recipient -ResultSize
  unlimited -RecipientPreviewFilter $GAL.RecipientFilter | select
  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled

This example returns the members of the GAL named Humongous Insurance.

  PowerShell

  $GAL = Get-GlobalAddressList -Identity "Humongous Insurance"; Get-Recipient -
  ResultSize unlimited -RecipientPreviewFilter $GAL.RecipientFilter | select

<!-- p.2142 -->

  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled

This example exports the results to the file C:\My Documents\Humongous Insurance
Export.csv.

  PowerShell

  $GAL = Get-GlobalAddressList -Identity "Humongous Insurance"; Get-Recipient -
  ResultSize unlimited -RecipientPreviewFilter $GAL.RecipientFilter | select
  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled | Export-Csv -
  NoTypeInformation -Path "C:\My Documents\Humongous Insurance Export.csv"

Use the Exchange Management Shell to create global address
lists
For more information about the requirements and implications of having multiple GALs in your
organization, see Global address lists.

For details about recipient filters in the Exchange Management Shell, see the Recipient filters in
the Exchange Management Shell section in this topic.

To create a GAL, use the following syntax:

  PowerShell

  New-GlobalAddressList -Name "<GAL Name>" [<Precanned recipient filter | Custom
  recipient filter>]

This example creates a GAL with a precanned recipient filter:

     Name: Contoso GAL

     Precanned recipient filter: All recipient types where the Company value is Contoso.

  PowerShell

  New-GlobalAddressList -Name "Contoso GAL" -IncludedRecipients AllRecipients -
  ConditionalCompany Contoso

This example creates a GAL with a custom recipient filter:

     Name: Agency A GAL

     Custom recipient filter: All recipient types where the CustomAttribute15 property
     contains the value AgencyA.

<!-- p.2143 -->

  PowerShell

  New-GlobalAddressList -Name "Agency A GAL" -RecipientFilter "CustomAttribute15 -
  like '*AgencyA*'"

For detailed syntax and parameter information, see New-GlobalAddressList.

How do you know this worked?
To verify that you've successfully created a GAL, use either of the following procedures:

     In the EAC, go to Organization > Address lists, select the address list, and click Edit (   )
     to view the details.

     In the Exchange Management Shell, replace <GAL Name> with the name of the GAL, and
     run the following command to verify the property values:

        PowerShell

        Get-GlobalAddressList -Identity "<GAL Name>" | Format-List
        Name,RecipientFilterType,RecipientContainer,RecipientFilter,IncludedRecipient
        s,Conditional*

Use the Exchange Management Shell to modify global
address lists
     The same settings are available as when you created the GAL. For more information, see
     the previous section.

     After you modify the GAL, you need to update its membership. For more information, see
     the Use the Exchange Management Shell to update global address lists section in this
     topic.

     You can't replace a custom recipient filter with a precanned recipient filter or vice-versa in
     an existing GAL.

To modify a GAL, use the following syntax:

  PowerShell

  Set-GlobalAddressList -Identity <GALIdentity>] [-Name <Name>] [<Precanned
  recipient filter | Custom recipient filter>] [-RecipientContainer
  <OrganizationalUnit>]

<!-- p.2144 -->

When you modify the Conditional parameter values, you can use the following syntax to add or
remove values without affecting other existing values: @{Add="<Value1>","<Value2>"...;
Remove="<Value1>","<Value2>"...} .

This example modifies the existing GAL named Contoso GAL by adding the Company value
Fabrikam to the precanned recipient filter.

  PowerShell

  Set-GlobalAddressList -Identity "Contoso GAL" -ConditionalCompany
  @{Add="Fabrikam"}

For detailed syntax and parameter information, see Set-GlobalAddressList.

How do you know this worked?
To verify that you've successfully modified a GAL, use either of the following procedures:

     In the EAC, go to Organization > Address lists, select the address list, and click Edit (   )
     to view the details.

     In the Exchange Management Shell, replace <GAL Name> with the name of the GAL, and
     run the following command to verify the property values:

        PowerShell

        Get-GlobalAddressList -Identity "<GAL Name>" | Format-List
        Name,RecipientFilterType,RecipientContainer,RecipientFilter,IncludedRecipient
        s,Conditional*

Use the Exchange Management Shell to remove global
address lists
     You can't remove the GAL named Default Offline Address Book, which is the GAL that's
     automatically created by Exchange, and the only GAL that has the
     IsDefaultGlobalAddressList property value True .

     You can't remove a GAL that's defined in an offline address book (OAB). To modify the
     address lists that are defined in an OAB, see Use the Exchange Management Shell to add
     and remove address lists from offline address books.

To remove a GAL, use the following syntax:

<!-- p.2145 -->

  PowerShell

  Remove-GlobalAddressList -Identity <GALIdentity>

This example removes the address list named Agency A GAL.

  PowerShell

  Remove-GlobalAddressList -Identity "Agency A GAL"

For detailed syntax and parameter information, see Remove-GlobalAddressList.

How do you know this worked?
To verify that you've successfully removed a GAL, use either of the following procedures:

     In the EAC, go to Organization > Address lists, and verify that the GAL is no longer listed.

     In the Exchange Management Shell, run the following command to verify that the GAL
     isn't listed:

        PowerShell

        Get-GlobalAddressList

Address list procedures

Update address lists
After you create or modify an address list in the EAC or the Exchange Management Shell, you
need to update the membership of the address list.

     If the address list contains more than 3000 recipients, we recommend that you use the
     Exchange Management Shell to update the address list. Updating the membership of the
     address list will take a long time, and will prevent you from using the EAC session until
     the address list is fully updated.

     If the address list contains fewer than 3000 recipients, it's OK to use the EAC.

Use the EAC to update address lists

<!-- p.2146 -->

   1. In the EAC, go to Organization > Address lists, and select the address list that you want
     to update.

           If the address list needs to be updated, you'll see a Not up to date section with an
           Update link in the details pane. Click Update.

           If the address list is already up to date, you'll see This address list is up to date in
           the details pane.

   2. After you click Update, a warning message that appears. Click Yes to update the address
     list by using the EAC. A progress bar allows you to monitor the update process. When the
     update is complete, click Close.

Use the Exchange Management Shell to update address lists

To update an address list, use the following syntax:

  PowerShell

  Update-AddressList -Identity [<AddressListIdentity>]

This example updates the address list named Northwest Executives.

  PowerShell

  Update-AddressList -Identity "Northwest Executives"

This example updates the address list named Sales that's located under the address list named
North America.

  PowerShell

  Update-AddressList "North America\Sales"

This example updates all address lists in the organization that require updates.

  PowerShell

  Get-AddressList | where {$_.RecipientFilterApplied -eq $false} | Update-
  AddressList

For detailed syntax and parameter information, see Update-AddressList.

<!-- p.2147 -->

How do you know this worked?
To verify that you've successfully updated an address list, use either of the following
procedures:

     In the EAC, go to Organization > Address lists, select the address list, and verify that you
     see This address list is up to date (instead of Not up to date with an Update link) in the
     details pane.

     In the Exchange Management Shell, replace <AddressListIdentity> with the name of the
     address list, and run the following command to verify the RecipientFilterApplied property
     value:

        PowerShell

        Get-AddressList -Identity <AddressListIdentity> | Format-Table -Auto
        Name,RecipientFilterApplied

View the members of address lists
If the address list isn't up to date, you should update the address list before you view the
members. For more information, see the previous section.

Use the EAC to view the members of address lists

   1. In the EAC, go to Organization > Address lists, and select the address list, and then click
     Edit (    ).

   2. Click Preview recipients the address list includes.

Use the Exchange Management Shell to view members of address lists
     Technically, this procedure returns all recipients (including hidden recipients) that match
     the recipient filters for the address list. The recipients that are actually visible in the
     address list have the HiddenFromAddressListsEnabled property value False .

To view the members of an address list, use the following syntax:

  PowerShell

  $AL = Get-AddressList -Identity <AddressListIdentity>; Get-Recipient -ResultSize
  unlimited -RecipientPreviewFilter $AL.RecipientFilter | select
  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled

<!-- p.2148 -->

This example returns the members of the address list named Southeast Offices.

  PowerShell

  $AL = Get-AddressList -Identity "Southeast Offices"; Get-Recipient -ResultSize
  unlimited -RecipientPreviewFilter $AL.RecipientFilter | select
  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled

This example exports the results to the file C:\My Documents\Southeast Offices Export.csv.

  PowerShell

  $AL = Get-AddressList -Identity "Southeast Offices"; Get-Recipient -ResultSize
  unlimited -RecipientPreviewFilter $AL.RecipientFilter | select
  Name,PrimarySmtpAddress,HiddenFromAddressListsEnabled | Export-Csv -
  NoTypeInformation -Path "C:\My Documents\Southeast Offices Export.csv"

Create address lists
You can create address lists by using the EAC or the Exchange Management Shell. In the EAC,
when you create an address list, you're required to include a recipient filter that's based on the
recipient type (specific types or all recipients). In the Exchange Management Shell, you aren't
required to include a recipient filter that's based on recipient type.

Use the EAC to create address lists

   1. In the EAC, go to Organization > Address lists, and then click New (     ).

   2. In the Address list windows that opens, configure the following settings:

           Name: Enter a unique, descriptive name for the address list.

           Address list path: You can create the address list in the root (" ****", also known as
           All Address Lists), or you can create the address list under an existing address list. To
           create the address list under an existing address list, click Browse, select the address
           list in the picker window, and then click OK.

           For details about the recipient filters and preview options that are available here, see
           the Recipient filters in the EAC section in this topic.

   3. When you're finished, click Save. You'll receive a warning message that tells you to click
     Update in the details pane to update the membership of the address list. For more
     information, see the Update address lists section in this topic.

<!-- p.2149 -->

Use the Exchange Management Shell to create address lists
You can create address lists with or without recipient filters. For details about recipient filters in
the Exchange Management Shell, see the Recipient filters in the Exchange Management Shell
section in this topic.

To create an address list, use the following syntax:

  PowerShell

  New-AddressList -Name "<Address List Name>" [-Container <ExistingAddressListPath>]
  [<Precanned recipient filter | Custom recipient filter>] [-RecipientContainer
  <OrganizationalUnit>]

This example creates an address list with a precanned recipient filter:

     Name: Southeast Offices

     Location: Under the root (" \ ", also known as All Address Lists) because we didn't use the
     Container parameter, and the default value is " \ ".

     Precanned recipient filter: All users with mailboxes where the State or province value is
     GA, AL, or LA (Georgia, Alabama, or Louisiana).

  PowerShell

  New-AddressList -Name "Southeast Offices" -IncludedRecipients MailboxUsers -
  ConditionalStateorProvince "GA","AL","LA"

This example creates an address list with a custom recipient filter:

     Name: Northwest Executives

     Location: Under the existing address list named North America.

     Custom recipient filter: All users with mailboxes where the Title value contains Director
     or Manager, and the State or province value is WA, OR, or ID (Washington, Oregon, or
     Idaho).

  PowerShell

  New-AddressList -Name "Northwest Executives" -Container "\North America"-
  RecipientFilter "(RecipientType -eq 'UserMailbox') -and (Title -like '*Director*'
  -or Title -like '*Manager*') -and (StateOrProvince -eq 'WA' -or StateOrProvince -
  eq 'OR' -or StateOrProvince -eq 'ID')"

<!-- p.2150 -->

For detailed syntax and parameter information, see New-AddressList.

How do you know this worked?
To verify that you've successfully created an address list, use either of the following procedures:

     In the EAC, go to Organization > Address lists, select the address list, and click Edit (      )
     to view the details.

     In the Exchange Management Shell, replace [<AddressListPath>] <AddressListName> with
     the name and (optionally) location of the address list, and run the following command to
     verify the property values:

        PowerShell

        Get-AddressList -Identity "[<AddressListPath>\]<AddressListName>" | Format-
        List
        Name,RecipientFilterType,RecipientContainer,RecipientFilter,IncludedRecipient
        s,Conditional*

Modify address lists
     If you created an address list with no recipient filters or a custom recipient filter in the
     Exchange Management Shell, you can't modify the address list in the EAC. You need to
     use the Exchange Management Shell.

     After you modify an address list, you need to update its membership. For more
     information, see the Update address lists section in this topic.

     You can't replace a custom recipient filter with a precanned recipient filter or vice-versa in
     an existing address list.

     You can change the location of an address list by using the Move-AddressList cmdlet in
     the Exchange Management Shell. For more information, see the Use the Exchange
     Management Shell to move address lists section in this topic.

Modify address lists in the EAC

   1. In the EAC, go to Organization > Address lists, select the address list, and then click Edit (
        ).

   2. In Address list windows that opens, configure the following settings:

             Display name: Enter a unique, descriptive name for the address list.

<!-- p.2151 -->

           For details about the recipient filters and preview options that are available here, see
           the Recipient filters in the EAC section in this topic.

   3. When you're finished, click Save. You'll receive a warning message that tells you to click
     Update in the details pane to update the membership of the address list. For more
     information, see the Update address lists section in this topic.

Modify address lists in the Exchange Management Shell
     The same basic settings are available as when you created the address list. For more
     information, see the Use the Exchange Management Shell to create address lists section
     in this topic.

     You can't use this procedure to move an address list. For more information, see the Use
     the Exchange Management Shell to move address lists section in this topic.

To modify an existing address list, use the following syntax:

  PowerShell

  Set-AddressList -Identity <AddressListIdentity> [-Name <Name>] [<Precanned
  recipient filter | Custom recipient filter>] [-RecipientContainer
  <OrganizationalUnit>]

When you modify the Conditional parameter values, you can use the following syntax to add or
remove values without affecting other existing values: @{Add="<Value1>","<Value2>"...;
Remove="<Value1>","<Value2>"...} .

This example modifies the existing address list named Southeast Offices by adding the State or
province value TX (Texas) to the precanned recipient filter.

  PowerShell

  Set-AddressList -Identity "Southeast Offices" -ConditionalStateOrProvince
  @{Add="TX"}

For detailed syntax and parameter information, see Set-AddressList.

How do you know this worked?
To verify that you've successfully modified an address list, use either of the following
procedures:

<!-- p.2152 -->

     In the EAC, go to Organization > Address lists, select the address list, and click Edit (      )
     to view the details.

     In the Exchange Management Shell, replace <AddressListIdentity> with the path\name of
     the address list, and run the following command to verify the property values:

        PowerShell

        Get-AddressList -Identity "<AddressListIdentity>" | Format-List
        Name,RecipientFilterType,RecipientContainer,RecipientFilter,IncludedRecipient
        s,Conditional*

Use the Exchange Management Shell to move address lists
You can select the location of an address list when you create an address list in the EAC or the
Exchange Management Shell. But, you can only move an existing address list by using the
Move-AddressList cmdlet in the Exchange Management Shell. If the source address list
contains child address lists under it, the address list hierarchy is moved to the target location
that you specify.

To move an address list, use the following syntax:

  PowerShell

  Move-AddressList -Identity "<AddressListIdentity>" -Target "<AddressListIdentity
  or \>"

This example moves the address list named Southeast Offices from the root (" \ ", also known
as All Address Lists) to the address list named North America.

  PowerShell

  Move-AddressList -Identity "Southeast Offices" -Target "North America"

For detailed syntax and parameter information, see Move-AddressList.

How do you know this worked?
To verify that you've successfully modified an address list, use either of the following
procedures:

     In the EAC, go to Organization > Address lists, select the address list, and click Edit (      )
     to view the details.

<!-- p.2153 -->

     In the Exchange Management Shell, replace <AddressListIdentity> with the path\name of
     the address list, and run the following command to verify the property values:

        PowerShell

        Get-AddressList -Identity "<AddressListIdentity>" | Format-List
        Name,RecipientFilterType,RecipientContainer,RecipientFilter,IncludedRecipient
        s,Conditional*

Remove address lists
If the address list contains more than 3000 recipients, we recommend that you use the
Exchange Management Shell to remove the address list. Removing the address list will take a
long time, and will prevent you from using the EAC session until the address list is fully
removed. If the address list contains less than 3000 recipients, it's OK to use the EAC to remove
the address list.

     You can't remove an address list that's defined in an offline address book (OAB). To
     modify the address lists that are defined in an OAB, see Use the Exchange Management
     Shell to add and remove address lists from offline address books.

     You can't remove an address list that contains child address lists (you'll receive an error).
     You first need to do one of the following steps:

         Use the EAC to remove the parent and all child address lists at the same time.

         Use the Exchange Management Shell to move all child address lists to another location
         by using the Move-AddressList cmdlet.

Use the EAC to remove address lists
   1. In the EAC, go to Organization > Address lists.

   2. Select the address list or lists that you want to remove, and then click Remove ( ). You
     can select multiple address lists by pressing the CTRL key while selecting each list.

   3. Click Yes in the warning message that appears. A progress bar allows you to monitor the
     removal process. When the removal is complete, click Close.

Use the Exchange Management Shell to remove address lists

To remove an address list, use the following syntax:

<!-- p.2154 -->

  PowerShell

  Remove-AddressList -Identity "[<AddressListPath>\]<AddressListName>" [-Recursive]

This example removes the address list named Southeast Offices and all its children from under
the North America address list.

  PowerShell

  Remove-AddressList -Identity "North America\Southeast Offices" -Recursive

For detailed syntax and parameter information, see Remove-AddressList.

How do you know this worked?

To verify that you've successfully removed an address list, use either of the following
procedures:

     In the EAC, go to Organization > Address lists, and verify that the address list is no
     longer listed.

     In the Exchange Management Shell, run the following command to verify that the address
     list isn't listed:

        PowerShell

        Get-AddressList

Hide recipients from address lists
Hiding a recipient from address lists doesn't prevent the recipient from receiving email
messages; it prevents users from finding the recipient in address lists. The recipient is hidden
from all address lists and GALs (effectively, they're exceptions to the recipient filters in all
address lists). If you want to selectively include the recipient in some address lists but not
others, you need to adjust the recipient filters in the address lists to include or exclude the
recipient.

Hiding a mailbox from address lists also prevents Outlook from finding the mailbox in GAL
when you create a new profile, or add an additional mailbox to an existing profile. To add the
hidden mailbox in Outlook, you can temporarily make the mailbox visible in address lists,
configure Outlook, and then hide the mailbox from address lists again.

<!-- p.2155 -->

Use the EAC to hide recipients from address lists
   1. In the EAC, go to one of the following locations based on the recipient type:

           Recipients > Mailboxes: User mailboxes, linked mailboxes, and remote mailboxes.

           Recipients > Groups: Distribution groups, mail-enabled security groups, and
           dynamic distribution groups.

           Recipients > Resources: Room and equipment mailboxes.

           Recipients > Contacts: Mail users and mail contacts.

           Recipients > Shared: Shared mailboxes.

           Public folders > Public folders: Mail-enabled public folders.

   2. Select the recipient that you want to hide from address lists, and then click Edit (   ).

   3. The recipient properties window opens. What you do next depends on the recipient type:

           Mailboxes, Contacts and Shared: On the General tab, select Hide from address
           lists.

           Groups: On the General tab, select Hide this group from address lists.

           Resources: On the General tab, click More options, and then select Hide from
           address lists.

           Public folders: On the General mail properties tab, select Hide from Exchange
           address list.

     When you're finished, click Save.

Use the Exchange Management Shell to hide recipients from
address lists
To hide a recipient from address lists, use the following syntax:

  PowerShell

  Set-<RecipientType> -Identity <RecipientIdentity> -HiddenFromAddressListsEnabled
  $true

<RecipientType> is one of these values:

<!-- p.2156 -->

     DistributionGroup

     DynamicDistributionGroup

     Mailbox

     MailContact

     MailPublicFolder

     MailUser

     RemoteMailbox

This example hides the distribution group named Internal Affairs from address lists.

  PowerShell

  Set-DistributionGroup -Identity "Internal Affairs" -HiddenFromAddressListsEnabled
  $true

This example hides the mailbox michelle@contoso.com from address lists.

  PowerShell

  Set-Mailbox -Identity michelle@contoso.com -HiddenFromAddressListsEnabled $true

Notes:

     To make the recipient visible in address lists again, use the value $false for the
     HiddenFromAddressListsEnabled parameter.

     By default, arbitration mailboxes and public folder mailboxes are hidden from address
     lists. If you use the Set-Mailbox cmdlet to change this or any other setting for arbitration
     or public folder mailboxes, you need to include the Arbitration or PublicFolder switches.

How do you know this worked?
You can verify that you've successfully hidden a recipient from address lists by using any of the
following procedures:

     In the EAC, select the recipient, click Edit (   ) and verify the hide from address lists setting
     is selected.

<!-- p.2157 -->

     In the Exchange Management Shell, run the following command and verify the recipient is
     listed:

        PowerShell

        Get-Recipient -ResultSize unlimited -Filter "HiddenFromAddressListsEnabled -
        eq `$true"

     Open the GAL in Outlook or Outlook on the web (formerly known as Outlook Web App),
     and verify the recipient isn't visible.

Recipient filters in the EAC
When you create or modify address lists in the EAC, the following recipient filter settings are
available:

     Types of recipients to include

        All recipients

        Or

        Only the following recipient types: Select one or more of the following values:

        Users with Exchange mailboxes

        Mail users with external email addresses

        Resource mailboxes

        Mail contacts with external email addresses

        Mail-enabled groups

     Create rules to further define the recipients

   1. Click Add rule and select one of the recipient properties from the drop down list:

             Recipient container (container or organization unit)

             State or province

             Company

             Department

             Custom attribute 1 to 15

<!-- p.2158 -->

   2. Enter a value for the property you selected:

           If you selected Recipient container, a Select an organizational unit dialog box
           appears that allows you to select the container or OU in Active Directory.

           For other recipient properties, a Specify words or phrases dialog appears that
           allows you to add, edit and remove text values.

           Property values require an exact match. Wildcards and partial matches aren't
           supported. For example, the value "Sales" doesn't match "Sales and Marketing".

           Multiple values of the same property use the or operator. For example, "Department
           equals Sales or Department equals Marketing"

   3. After you've selected a property and value, click Add rule.

   4. Repeat the previous steps to configure more filters. Note that multiple properties use the
     and operator. For example, "Department equals Sales and Company equals Contoso".

     Preview recipients the address list includes: When you click this setting, a Preview dialog
     appears that shows you the recipients that are identified by the filters you configured.

Recipient filters in the Exchange Management Shell
In the Exchange Management Shell, you can specify precanned recipient filters, or custom
recipient filters, but not both at the same time.

     Precanned recipient filters

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

<!-- p.2159 -->

        Double quotation marks " " are required around the whole OPATH filter. Although the
        filter is a string (not a system block), you can also use braces { } , but only if the filter
        doesn't contain variables that require expansion..

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

        After you use the New-AddressList cmdlet to create an address list that uses custom
        recipient filters, you can't modify the address list in the EAC. You need to use the Set-
        AddressList cmdlet with the RecipientFilter parameter in the Exchange Management
        Shell.

Note: The RecipientContainer (organizational unit) recipient filter parameter is available to both
precanned recipient filters and custom recipient filters.

<!-- p.2160 -->

Address book policies in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016    2019      Subscription Edition

Address book policies (ABPs) lets administrators segment users into specific groups to provide
customized views of the organization's global address list (GAL). The goal of an ABP is to
provide a simpler mechanism for GAL segmentation (also known as GAL segregation) in on-
premises organizations that require multiple GALs.

An ABP contains these elements:

      One GAL. For more information about GALs, see Global address lists.

      One offline address book (OAB). For more information about OABs, see Offline address
      books in Exchange Server.

      One room list. Note that this room list is a custom address list that specifies rooms
      (contains the filter RecipientDisplayType -eq 'ConferenceRoomMailbox' ). It's not a room
      finder that you create with the RoomList switch on the New-DistributionGroup or Set-
      DistributionGroup cmdlet. For more information, see Create and manage room
      mailboxes.

      One or more address lists. For more information about address lists, see Custom address
      lists.

For procedures involving ABPs, see Procedures for address book policies in Exchange Server.

Notes:

      ABPs create only a virtual separation of users from a directory perspective, not a legal
      separation.

      Implementing an ABP is a multi-step process that requires planning. For more
      information, see Scenario: Deploying address book policies in Exchange Server.

How ABPs work
The following diagram shows how ABPs work. The user is assigned Address Book Policy A that
contains a subset of address lists that are available in the organization. When the ABP is
created and assigned to the user, the ABP becomes the scope of the address lists that the user
is able to view.
