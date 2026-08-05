---
title: "Exchange Server — pages 1201-1240"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1201-1240
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1201-1240
family: exchange
documentKind: "doc"
abstract: "New-Mailbox -Equipment -Name \"<UniqueDescriptiveName>\" [-Alias <AliasValue>] [- Database <DatabaseIdentity>] [-DisplayName <String>] [-OrganizationalUnit <OrganizationalUnitIdentity>] [- PrimarySmtpAddress <SmtpAddress>] [-ResetPasswordOnNextLogon <Boolean>] [- UserPrincipalName"
---

# Exchange Server — pages 1201-1240

<!-- p.1201 -->

  New-Mailbox -Equipment -Name "<UniqueDescriptiveName>" [-Alias <AliasValue>] [-
  Database <DatabaseIdentity>]
   [-DisplayName <String>] [-OrganizationalUnit <OrganizationalUnitIdentity>] [-
  PrimarySmtpAddress <SmtpAddress>] [-ResetPasswordOnNextLogon <Boolean>] [-
  UserPrincipalName <UPN>]

This example creates an equipment mailbox named Car 02. Because we aren't using the Alias,
DisplayName, PrimarySmtpAddress, or UserPrincipalName parameters, the following values are
based on the Name parameter value:

     Alias: Car02. If you specify an Alias value without using the PrimarySmtpAddress or
     UserPrincipalName parameters, the Alias value is used on the left side of the '@' symbol.
     DisplayName: Car 02
     PrimarySmtpAddress: Alias and domain values from the email address policy. If the policy
     doesn't specify an alias, the value Car02 is used if you don't use the Alias parameter.
     UserPrincipalName: Car02@<default Active directory domain> if you don't use the Alias
     parameter.

  PowerShell

  New-Mailbox -Equipment -Name "Car 02"

For detailed syntax and parameter information, see New-Mailbox.

How do you know you successfully created an equipment
mailbox?
To verify that you successfully created an equipment mailbox, do either of the following steps:

     EAC: Go to Recipients > Resources tab. On the Resources tab, verify the equipment
     mailbox is listed. Select the mailbox, and then select   Edit to view the mailbox
     properties.

     Exchange Management Shell: To display information about the mailbox, replace
     <EquipmentMailboxIdentity> with the name, alias, user principal name (UPN), or email
     address of the mailbox, and then run the following command :

        PowerShell

        Get-Mailbox -Identity <EquipmentMailboxIdentity> | Format-List

<!-- p.1202 -->

Change how an equipment mailbox handles
meeting requests
You can use the EAC, Outlook on the web options for the equipment mailbox, or the Exchange
Management Shell to change how an equipment mailbox handles meeting requests.

All settings are available on the Set-CalendarProcessing cmdlet in the Exchange Management
Shell, but the following settings are available in Outlook on the web and not in the EAC:

     Turn off reminders
     Allow conflicts
        Allow up to this number of individual conflicts
        Allow up to this percentage of individual conflicts
     These users can schedule automatically if the resource is available and can submit a
     request for owner approval if the resource is unavailable

Use the EAC to change how an equipment mailbox handles
meeting requests
   1. In the Exchange admin center, navigate to Recipients > Resources.

   2. On the Resources tab, select the equipment mailbox, and then select      Edit.

   3. On the equipment mailbox properties page that opens, the following tabs are specific to
     how the equipment mailbox handles meeting requests:

          Booking Delegates tab:
             Booking requests section: Select one of the following values:
                Use customized settings to accept or decline booking requests: This is the
                default value.
                Accept or decline booking requests automatically: Meeting requests are
                automatically accepted. Meeting requests are automatically declined in the
                following scenarios:
                   A scheduling conflict with an existing reservation.
                   The meeting request violates the scheduling limits of the equipment (for
                   example, the meeting is too long).
                Select delegates who can accept or decline booking requests: One of the
                people you add to the Delegates box is responsible for accepting or declining
                meeting requests that are sent to the equipment mailbox. If you assign
                multiple delegates, only one needs to act on a meeting request.

          Booking Options tab: The following settings are available:

<!-- p.1203 -->

Allow repeating meetings: Allows or prevents recurring meetings for the
equipment. By default, this setting is selected, so recurring meetings are allowed.

Allow scheduling only during working hours: Accepts or declines meeting
requests that aren't during the working hours defined for the equipment mailbox.
By default, this setting isn't selected, so meeting requests are allowed outside the
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
  Not selected: Recurring meeting requests are automatically accepted if the
  meetings start on or before Maximum booking lead time (days) date.
  However, any meetings that extend beyond the Maximum booking lead time
  (days) date are automatically removed (no meetings can extend beyond that
  date).

Maximum booking lead time (days): Specifies the maximum number of days in
advance that the equipment can be booked. A valid value is an integer between 0
(today) and 1080 days. The default value is 180 days.

Maximum duration (hours): Specifies the maximum duration that the equipment
can be reserved in a meeting request. A valid value is from 0 (unlimited) to
35,791,394 hours. The default value is 24 hours.

This value applies to the length of each individual meeting in a recurring meeting
request.

If you want the meeting organizer to receive a reply, enter the text below: This
text is used in a reply message sent to users who send meeting requests to
reserve the equipment.

<!-- p.1204 -->

   4. When you're finished on the equipment mailbox properties page, select Save.

Use Outlook on the web options for the equipment mailbox
to change how the mailbox handles meeting requests
Users with Full Access permission to an equipment mailbox can use Open another mailbox in
Outlook on the web to change the scheduling settings of an equipment mailbox.

   1. In your Outlook on the web, select your account in the top right corner, and then select
     Open another mailbox.
   2. In the Open another mailbox dialog that opens, enter some or all of the equipment
     mailbox name, select Search directory, select the mailbox in the results, and then select
     Open.
   3. In the equipment mailbox in Outlook on the web, go to Settings > Options > Calendar >
     Resource scheduling.
   4. On the Resource scheduling settings page, configure the settings as described in the
     following subsections.

Scheduling options
The following settings are available in the Scheduling options section of the Resource
scheduling settings page in Outlook on the web for an equipment mailbox:

     Automatically process meeting requests and cancellations: Meeting requests are
     automatically accepted. By default, this setting is selected. Otherwise, a resource delegate
     manually accepts or declines meeting requests.

     Turn off reminders: Disables reminders in the equipment mailbox calendar. Meeting
     organizers and attendees can still receive reminders.

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

<!-- p.1205 -->

      Not selected: Recurring meeting requests are automatically accepted if the
      meetings start on or before Maximum number of days in advance resources can
      be booked date. However, any meetings that extend beyond the Maximum
      number of days in advance resources can be booked date are automatically
      removed (no meetings can extend beyond that date).

Limit meeting duration and Maximum allowed minutes: Specifies the maximum duration
that the equipment can be reserved in a meeting request. A valid value is from 0
(unlimited) to 1440 minutes (24 hours). The default value is 1440 minutes.

This value applies to the length of each individual meeting in a recurring meeting request.

Allow scheduling only during working hours: Accepts or declines meeting requests that
aren't during the working hours defined for the equipment mailbox. By default, this
setting isn't selected, so meeting requests are allowed outside the working hours. By
default, working hours are 8:00 A.M. to 5:00 P.M. Monday through Friday. You can set the
working hours on a mailbox in Outlook on the web (formerly known as Outlook Web App
or OWA) in Settings > Options > Calendar > Personalization > Calendar appearance >
Show work week as and Set your working hours.

Allow repeating meetings: Allows or prevents recurring meetings for the equipment. By
default, this setting is selected, so recurring meetings are allowed.

Allow conflicts: Allow or prevent conflicting meeting requests (also known as double
booking). By default, this setting isn't selected.

If recurring meetings are allowed on the equipment mailbox, this setting applies only to
recurring meetings. Don't use Add rooms to include the equipment in the meeting
request. Instead, include the equipment as a Required attendee in the meeting request.

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

<!-- p.1206 -->

           A numerical value means recurring meeting requests are denied if the request
           conflicts with any existing reservations more than the specified percentage. For
           example, this setting is 10% and a recurring meeting request has 20 individual
           meetings:
           Allowed if there's a conflict two or less of the individual meetings.
           Denied if there's a conflict with three or more of the individual meetings.

Scheduling Permissions
The following settings are available in the Scheduling permissions section of the Resource
scheduling settings page in Outlook on the web for an equipment mailbox:

     These people can schedule automatically if the resource is available: Select one of the
     following values:
        Everyone: Anyone can automatically reserve the equipment. If the equipment isn't
        available, the meeting request is automatically declined. This is the default value.
        Specific people and groups: Only the specified users and groups can automatically
        reserve the equipment. If the equipment isn't available, the meeting request is
        automatically declined. Meetings requests from other users or groups are
        automatically declined. Selecting this value without specifying the users or groups is
        equivalent to selecting Everyone.

     These users can submit a request for owner approval if the resource is available: Select
     one of the following values:

        Everyone: Anyone can request to reserve the equipment, but the request must be
        approved by a resource delegate (the Select delegates who can accept or decline
        booking requests setting in the EAC). If the equipment isn't available, the meeting
        request is automatically declined.

        Specific people and groups: Only the specified users and groups can request to
        reserve the equipment, but a resource delegate must approve the meeting request. If
        the equipment isn't available, the meeting request is automatically declined. Meetings
        requests from other users and groups are automatically declined.

        Selecting this value without specifying the users or groups is equivalent to selecting
        Everyone. By default, this value is selected, but no users or groups are selected.

     These users can schedule automatically if the resource is available and can submit a
     request for owner approval if the resource is unavailable: Select one of the following
     values:

<!-- p.1207 -->

        Everyone: Anyone can automatically reserve the equipment. If the equipment isn't
        available, the meeting request must be approved by a resource delegate (the Select
        delegates who can accept or decline booking requests setting in the EAC).

        Specific people and groups: Only the specified users and groups can request to
        reserve the equipment. If the equipment isn't available, a resource delegate must
        accept the meeting request. Meetings requests from other users and groups are
        automatically declined.

        Selecting this value without specifying the users or groups is equivalent to selecting
        Everyone. By default, this value is selected, but no users or groups are selected.

Response message
Select Add additional text to be included in responses to event invitations and enter the text
in the box.

Change other equipment mailbox properties
After you create an equipment mailbox, you can make changes and set other properties by
using the EAC or the Exchange Management Shell.

Use the EAC to change equipment mailbox
properties
   1. In the EAC, go to Recipients > Resources.

   2. On the Resources tab, select the equipment mailbox, and then select       Edit.

   3. On the equipment mailbox properties page that opens, several tabs are available:

     The following tabs contain specific settings for equipment mailboxes:

              General
              Contact information
              Booking delegates and Booking options (previously described)

     The remaining tabs contain identical settings to user mailboxes. These tabs and settings
     are described in the user mailbox article:

              Email address
              MailTip

<!-- p.1208 -->

          Mailbox delegation

General tab in equipment mailbox properties
The following settings are available on the General tab of the mailbox properties for an
equipment mailbox:

     Equipment name: The maximum value is 64 characters.

        Tip

       Although other properties are available to describe the details of the equipment (for
       example, Location and Capacity), consider summarizing the important details in the
       Name value using a consistent naming convention. Users can easily see the details in
       the equipment name when they select the equipment mailbox from the address
       book.

     Email address: You can change this value on the Email Address tab.

     Capacity

Select More options to view or change these other properties that appear:

     Organizational unit: The organizational unit (OU) that contains the account for the
     equipment mailbox. You can use Active Directory Users and Computers to move the
     account to a different OU.

     Mailbox database: The mailbox database that hosts the equipment mailbox. You can use
     recipients > Migration in the EAC to move the mailbox to a different database.

     Alias: When you change this value, the primary email address of the equipment mailbox is
     automatically updated if the mailbox is subject to email address policies.

     Hide from address lists: Select this setting to prevent the equipment mailbox from
     appearing in the global address lists and other address lists in your Exchange
     organization. If you select this setting, users can still send meeting requests using the
     email address.

     Department: Specify the department that the equipment is associated with. You can use
     this value to create recipient conditions for dynamic distribution groups and address lists.

     Company: Specify the company the equipment is associated with. You can use this value
     to create recipient conditions for dynamic distribution groups and address lists.

<!-- p.1209 -->

     Address book policy: Select the ABP that includes the equipment mailbox. ABPs contain a
     global address list (GAL), an offline address book (OAB), a room list (not a room list
     distribution group), and a set of address lists. To learn more, see Address book policies in
     Exchange Server.

     Custom attributes: Select      Edit to specify values for Custom Attribute 1 to Custom
     Attribute 15 on the mailbox. You can use this value to create recipient conditions for
     dynamic distribution groups and address lists.

Contact information tab in equipment mailbox properties
The following settings are available on the General tab of the mailbox properties for an
equipment mailbox:

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

Use the Exchange Management Shell to change equipment
mailbox properties
To view and change equipment mailbox properties, use the following cmdlets in the Exchange
Management Shell:

     Get-User and Set-User: View and set general properties such as location, department, and
     company names.
     Get-Mailbox and Set-Mailbox: View and set mailbox properties, such as email addresses
     and the mailbox database.
     Get-CalendarProcessing and Set-CalendarProcessing: View and set booking options and
     delegates.

<!-- p.1210 -->

Here are some examples of using the Exchange Management Shell to change equipment
mailbox properties.

This example changes the display name and primary SMTP address (also called the default
reply address). The previous primary SMTP address is kept as a proxy address on the mailbox.

  PowerShell

  Set-Mailbox "Van 01" -DisplayName "Van 01 - 13 passenger" -EmailAddresses
  SMTP:van01@contoso.com,smtp:01van@contoso.com -ResourceCapacity 13

This example configures equipment mailboxes to allow booking requests to be scheduled only
during working hours and sets a maximum duration of 9 hours.

  PowerShell

  Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq 'RoomMailbox'"
  | Set-CalendarProcessing -ScheduleOnlyDuringWorkHours $true -
  MaximumDurationInMinutes 540

This example uses the Get-User cmdlet to find all restricted equipment mailboxes, and then
uses the Set-CalendarProcessing cmdlet to send booking requests to a delegate named Robin
Wood to accept or decline.

  PowerShell

  Get-User -ResultSize unlimited -Filter "(RecipientTypeDetails -eq 'RoomMailbox') -
  and (DisplayName -like 'Restricted*')" | Set-CalendarProcessing -AllBookInPolicy
  $false -AllRequestInPolicy $true -ResourceDelegates "Robin Wood"

How do you know you successfully changed the equipment
mailbox properties?
To verify that you successfully changed the properties for an equipment mailbox, either of the
following steps:

     EAC: Go to Recipients > Resources tab. On the Resources tab, Select the mailbox, and
     then select      Edit to view the mailbox properties.

     Exchange Management Shell:
        To display information about the mailbox, replace <EquipmentMailboxIdentity> with
        the name, alias, user principal name (UPN), or email address of the mailbox, and then
        run the following commands:

<!-- p.1211 -->

PowerShell

Get-Mailbox -Identity <EquipmentMailboxIdentity> | Format-List

Get-CalendarProcessing -Identity <EquipmentMailboxIdentity> | Format-List

Run the following command to identify the equipment mailboxes that can only be
scheduled during working hours:

   PowerShell

   Get-Mailbox -ResultSize unlimited -Filter "RecipientTypeDetails -eq
   'EquipmentMailbox'" | Get-CalendarProcessing | Format-List
   Identity,ScheduleOnlyDuringWorkHours

<!-- p.1212 -->

Disconnected mailboxes in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

Each Microsoft Exchange mailbox consists of an Active Directory user account and the mailbox
data stored in the Exchange mailbox database. All configuration data for a mailbox is stored in
the Exchange attributes of the Active Directory user object. The mailbox database contains the
mail data that's in the mailbox associated with the user account. The following figure shows the
components of a mailbox.

Mailbox components

A disconnected mailbox is a mailbox object in the mailbox database that isn't associated with an
Active Directory user account. There are two types of disconnected mailboxes:

      Disabled mailboxes: When a mailbox is disabled or deleted in the Exchange admin center
      (EAC) or using the Disable-Mailbox or Remove-Mailbox cmdlet in the Exchange
      Management Shell, Exchange retains the deleted mailbox in the mailbox database, and
      switches the mailbox to a disabled state. This is why mailboxes that are either disabled or
      deleted are referred to as disabled mailboxes. The difference is that when you disable a
      mailbox, the Exchange attributes are removed from the corresponding Active Directory
      user account, but the user account is retained. When you delete a mailbox, both the
      Exchange attributes and the Active Directory user account are deleted.

      Disabled and deleted mailboxes are retained in the mailbox database until the deleted
      mailbox retention period expires, which is 30 days by default. After the retention period
      expires, the mailbox is permanently deleted (also called purged). If a mailbox is deleted

<!-- p.1213 -->

     using the Remove-Mailbox cmdlet, it's also retained for the duration of the retention
     period.

       ） Important

       If a mailbox is deleted using the Remove-Mailbox cmdlet and either the Permanent
       or StoreMailboxIdentity parameter, it will be immediately deleted from the mailbox
       database.

     To identify the disabled mailboxes in your organization, run the following commands in
     the Exchange Management Shell:

       PowerShell

       $dbs = Get-MailboxDatabase
       $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
       {$_.DisconnectReason -eq "Disabled"} | Format-Table
       DisplayName,Database,DisconnectDate

     Soft-deleted mailboxes: When a mailbox is moved to a different mailbox database,
     Exchange doesn't fully delete the mailbox from the source mailbox database when the
     move is complete. Instead, the mailbox in the source mailbox database is switched to a
     soft-deleted state. Like disabled mailboxes, soft-deleted mailboxes are retained in the
     source database either until the deleted mailbox retention period expires or until the
     Remove-StoreMailbox cmdlet is used to purge the mailbox.

     Run the following commands to identify soft-deleted mailboxes in your organization.

       PowerShell

       $dbs = Get-MailboxDatabase
       $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
       {$_.DisconnectReason -eq "SoftDeleted"} | Format-Table
       DisplayName,Database,DisconnectDate

Working with disabled mailboxes
You can perform several operations on a disabled mailbox before it's purged from the mailbox
database:

     Reconnect it to the same user account.
     Connect it to a different user account that isn't mail-enabled, which means the user
     account doesn't have a mailbox.

<!-- p.1214 -->

     Restore it to a user account that has an existing mailbox. For example, if a user whose
     mailbox was deleted has a new mailbox, you can restore the user's disabled mailbox to
     their new mailbox.
     Permanently delete it from the Exchange mailbox database.

Connecting or restoring a disabled mailbox
Here are scenarios in which you may want to connect or restore a disabled mailbox before the
mailbox retention period expires or before it's permanently deleted:

     You disabled a mailbox and now want to reconnect the mailbox to the same Active
     Directory user account.

     You deleted a mailbox by using the EAC or the Remove-Mailbox cmdlet and now want to
     reconnect the mailbox to a different Active Directory user account.

     You deleted a mailbox and now want to restore the mailbox to an existing mailbox. For
     example, if a user whose mailbox was deleted has a new mailbox, you can restore the
     user's disabled mailbox to their new mailbox.

     You want to convert a user mailbox to a linked mailbox associated with a user account
     that's external to the forest in which your Exchange organization exists. The resource
     forest scenario is an example of when you would want to associate a mailbox with an
     external account. In this scenario, user objects in the Exchange forest have mailboxes, but
     the user objects are disabled for logon. You must associate a mailbox in the Exchange
     forest with a user account in the external account forest.

There are two ways you can reconnect or restore a disabled mailbox. The first method is to use
the EAC or the Connect-Mailbox cmdlet to connect a disabled mailbox to a user account. For
procedures to reconnect disabled mailboxes, see Connect a disabled mailbox.

The second method uses the New-MailboxRestoreRequest cmdlet to merge the contents of
the disabled mailbox with an existing mailbox. This cmdlet uses the Mailbox Replication Service
(MRS) to restore the mailbox. For procedures to restore disabled mailboxes, see Connect or
restore a deleted mailbox.

Permanently deleting a disabled mailbox
As stated previously, Exchange retains disabled mailboxes in the mailbox database based on
the deleted mailbox retention settings configured for that mailbox database. After the specified
retention period, a disabled mailbox is purged from the Exchange mailbox database. You can
also permanently delete a disabled mailbox and all its message content from the mailbox
database by using the Remove-StoreMailbox cmdlet. After a disabled mailbox is automatically

<!-- p.1215 -->

purged or permanently deleted by an administrator, the data loss is permanent and the
mailbox can't be recovered.

For more information, see Permanently delete a mailbox.

Working with disabled archive mailboxes
Archive mailboxes become disconnected when they're disabled. Similar to a disabled primary
mailbox, a disconnected archive mailbox can be connected by using the Connect-Mailbox
cmdlet with the Archive parameter.

The primary mailbox and the archive mailbox share the same legacy distinguished name (DN),
so you must connect the archive mailbox to the same user mailbox that it was previously
connected to. You can't connect the archive mailbox to a different user mailbox.

You can perform two operations on a disconnected archive mailbox:

     Connect it to an existing primary mailbox: Like a disconnected primary mailbox, a
     disconnected archive mailbox is retained in the mailbox database until the deleted
     mailbox retention period expires, which is 30 days by default. During this time, you can
     recover the archive mailbox by reconnecting it to the same user account that it was
     connected to before it was disabled.

       ７ Note

       If you disable an archive mailbox for a user mailbox and then enable an archive
       mailbox for that same user, that user mailbox will get a new archive mailbox. While
       you can use the Connect-Mailbox cmdlet to connect a primary mailbox to a user,
       you must use the Enable-Mailbox cmdlet to connect a disabled archive mailbox to
       an existing mailbox.

     For more information, see Manage In-Place Archives in Exchange Server.

     Permanently delete it from the Exchange mailbox database: Exchange retains
     disconnected archive mailboxes based on the deleted mailbox retention settings
     configured for the mailbox database. The default retention period is 30 days. After the
     specified mailbox retention period, a disconnected archive mailbox is purged from the
     Exchange mailbox database.

     Like a disabled primary mailbox, you can permanently delete a disabled archive mailbox
     at any time by using the Remove-StoreMailbox cmdlet. For more information, see
     Permanently delete a mailbox.

<!-- p.1216 -->

Working with soft-deleted mailboxes
A soft-deleted mailbox is created when a mailbox is moved from one Exchange mailbox
database to any other mailbox database. Exchange doesn't fully delete the mailbox from the
source database after a move in case an error occurs during the move that causes the mailbox
on the destination database to fail. You can always restore the source mailbox and try again.
Exchange will retain the soft-deleted mailbox for the duration of the mailbox retention period.

You can perform two operations on a soft-deleted mailbox:

     Restore it to an existing mailbox.

     Permanently delete it from the Exchange mailbox database.

The procedures for restoring and permanently deleting a soft-deleted mailbox are similar to
those for a disabled mailbox. For more information, see the following topics:

     Connect or restore a deleted mailbox

     Permanently delete a mailbox

Summary of working with disconnected mailboxes
The following table summarizes the information about disconnected mailboxes, including how
the mailbox was disconnected, what happens to the corresponding Active Directory user
account when a mailbox is disconnected, and the options and tools you have to connect or
restore disconnected mailboxes.

                                                                                 ﾉ   Expand table

 How mailbox was     Value of             Is Active      Connect or    Tools
 disabled            DisconnectReason     Directory      restore
                     property             user account   options
                                          retained?

 The EAC:            Disabled             Yes            Connect to    The EAC: Recipients >
 Recipients >                                            same user     Mailboxes > Connect a
 Mailboxes >                                             account       Mailbox
 Disable
                                                                       The Exchange
 The Exchange                                                          Management Shell:
 Management Shell:                                                     Connect-Mailbox cmdlet
 Disable-Mailbox
 cmdlet

<!-- p.1217 -->

 How mailbox was     Value of            Is Active      Connect or     Tools
 disabled            DisconnectReason    Directory      restore
                     property            user account   options
                                         retained?

 The EAC:            Disabled            No             Connect to     The EAC: Recipients >
 Recipients >                                           a different    Mailboxes > Connect a
 Mailboxes >                                            user           Mailbox
 Delete                                                 account
                                                                       The Exchange
 The Exchange                                           Restore to a   Management Shell:
 Management Shell:                                      different
 Remove-Mailbox                                         mailbox                Connect-Mailbox
 cmdlet                                                                        cmdlet
                                                                               Enable-Mailbox
                                                                               cmdlet
                                                                               New-
                                                                               MailboxRestore
                                                                               cmdlet

 Moved to a          SoftDeleted         Yes            Connect to     The EAC: Recipients >
 different mailbox                                      a different    Mailboxes > Connect a
 database                                               user           Mailbox
                                                        account
                                                                       The Exchange
                                                        Restore to a   Management Shell:
                                                        different
                                                        mailbox                Connect-Mailbox
                                                                               cmdlet
                                                                               Enable-Mailbox
                                                                               cmdlet
                                                                               New-
                                                                               MailboxRestore
                                                                               cmdlet

Disconnected mailbox documentation
The following table contains links to topics that will help you manage disconnected mailboxes.
This includes managing disconnected user mailboxes, linked mailboxes, resource mailboxes,
and shared mailboxes.

                                                                                 ﾉ   Expand table

<!-- p.1218 -->

Topic                            Description

Disable or delete a mailbox in   Learn how to disable or delete mailboxes.
Exchange Server

Connect a disabled mailbox       Learn how to connect a disabled mailbox to an existing user account.

Connect or restore a deleted     Learn how to connect a deleted mailbox to a user account or restore the
mailbox                          contents of a deleted mailbox to an existing mailbox.

Manage Mailbox Restore           Learn how to manage mailbox restore requests using the Exchange
Requests                         Management Shell.

Permanently delete a mailbox     Learn how to permanently delete a mailbox.

<!-- p.1219 -->

Disable or delete a mailbox in Exchange
Server
10/09/2025

APPLIES TO:     2016      2019      Subscription Edition

In Exchange Server, you can use the Exchange admin center (EAC) or the Exchange
Management Shell to disable or delete mailboxes. Disabled or deleted mailboxes are also
known as disconnected mailboxes. For more information about disconnected mailboxes, see
Disconnected mailboxes.

  ７ Note

  If you need to delete a mailbox in Microsoft 365 or Office 365, see Delete or Restore User
  Mailboxes in Exchange Online.

What do you need to know before you begin?
     Estimated time to complete each procedure: 2 minutes.

     For more information about accessing and using the EAC, see Exchange admin center in
     Exchange Server. To learn how to open the Exchange Management Shell in your on-
     premises Exchange organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Recipient Provisioning
     Permissions" section in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Disable mailboxes

<!-- p.1220 -->

When you disable a mailbox, all Exchange attributes are removed from the associated user
account in Active Directory. The disconnected mailbox is hidden and marked for removal. The
disconnected mailbox is permanently deleted (purged) based on the MailboxRetention
property value for the mailbox database (the default value is 30 days). Before the mailbox is
purged, you can reconnect it to a new or existing user account that doesn't already have an
associated mailbox. For more information, see Connect a disabled mailbox.

  ７ Note

  Disabling a mailbox that has an associated archive marks both the primary and archive
  mailboxes for removal. To only mark the archive mailbox for removal without affecting the
  primary mailbox, see Disable an archive mailbox.

Use the EAC to disable a mailbox
   1. In the EAC, go to Recipients, and click the tab for the type of mailbox that you want to
     disable:

           Mailboxes for user mailboxes and linked mailboxes.

           Shared for shared mailboxes.

   2. Find and select the mailbox that you want to disable. For example:

           Scroll through the list. You can also click the column headers to sort the mailboxes.

           Click Search and enter the text to filter the list of mailboxes.

           Select multiple mailboxes by selecting a mailbox, holding the Shift key, and selecting
           a mailbox farther down in the list, or by holding down the CTRL key as you select
           each mailbox.

   3. After you've selected the mailbox or mailboxes that you want to disable, click More       ,
     select Disable, and then click Yes in the warning message that appears.

Use the Exchange Management Shell to disable a mailbox
To disable a mailbox, use this syntax:

  PowerShell

  Disable-Mailbox <MailboxIdentity> [-Arbitration] [-Archive] [-PublicFolder] [-
  RemoteArchive]

<!-- p.1221 -->

This example disables the user mailbox that has the alias value danj.

  PowerShell

  Disable-Mailbox danj

This example disables the room mailbox named Conf Room 31/1234 (12).

  PowerShell

  Disable-Mailbox "Conf Room 31/1234 (12)"

This example disables the shared mailbox that has the email address
sharedmbx@contoso.com.

  PowerShell

  Disable-Mailbox sharedmbx@contoso.com

For detailed syntax and parameter information, see Disable-Mailbox.

How do you know this worked?
To verify that you've successfully disabled a mailbox, do any of these steps:

     In the EAC, click Recipients, go to the appropriate tab for the type of mailbox that you
     disabled, and verify that the mailbox is no longer listed. Note that you might need to click
     Refresh     .

     In Active Directory Users and Computers, right-click the user account whose mailbox you
     disabled, and then click Properties. On the General tab, verify that the E-mail field is
     blank.

     In the Exchange Management Shell, replace <DisplayName> with the user's display name,
     and run the following commands to verify the DisconnectReason property value is
     Disabled (which indicates the mailbox has been marked for removal):

        PowerShell

        $dbs = Get-MailboxDatabase
        $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
        {$_.DisplayName -eq "<DisplayName>"} | Format-List
        DisconnectReason,DisconnectDate

<!-- p.1222 -->

     Notes
        The DisconnectReason property doesn't distinguish between disabled and deleted
        mailboxes (the value for both is Disabled ). The presence of the associated user
        account indicates whether the mailbox was disabled.
        When you delete a mailbox, the value of the DisconnectReason property is also
        Disabled , but the corresponding Active Directory user account is also deleted.

        If the command returns no results, replace <DatabaseName> with the name of the
        mailbox database where the disconnected mailbox resides, and run this command to
        synchronize the mailbox state for all disconnected mailboxes on the database:

       PowerShell

           Get-MailboxStatistics -Database "<DatabaseName>" | foreach {Update-
       StoreMailboxState -Database $_.Database > -Identity $_.MailboxGuid -
       Confirm:$false}

     Then, run the previous command, which should now return results.
        In the Exchange Management Shell, replace <UserIdentity> with the name or user
        principal name of the user (for example, user@contoso.com), and run this command to
        verify that the RecipientType property value is User , not UserMailbox .

       PowerShell

          Get-User -Identity <UserIdentity>

Delete mailboxes
When you delete a mailbox, the mailbox is disconnected from the associated user account, and
the account is removed from Active Directory. The disconnected mailbox is hidden and marked
for removal. The disconnected mailbox is permanently deleted (purged) based on the
MailboxRetention property value for the mailbox database (the default value is 30 days).
Before the mailbox is purged, you can reconnect it to a new or existing user account that
doesn't already have an associated mailbox. For more information, see Connect or restore a
deleted mailbox.

  ７ Note

  Deleting a mailbox that has an associated archive marks both the primary and archive
  mailboxes for removal. To only mark the archive mailbox for removal without affecting the
  primary mailbox, see Disable an archive mailbox.

<!-- p.1223 -->

Use the EAC to delete a mailbox
   1. In the EAC, go to the location for the type of mailbox that you want to delete:

           Recipients > Mailboxes for user mailboxes and linked mailboxes.

           Recipients > Resources for room and equipment mailboxes.

           Recipients > Shared for shared mailboxes.

           Public folders > Public folder mailboxes for public folder mailboxes.

   2. Find and select the mailbox that you want to disable. For example:

           Scroll through the list. You can also click the column headers to sort the mailboxes.

           Click Search and enter the text to filter the list of mailboxes.

           Select multiple mailboxes by selecting a mailbox, holding the Shift key, and selecting
           a mailbox farther down in the list, or by holding down the CTRL key as you select
           each mailbox.

   3. After you've selected the mailbox or mailboxes that you want to delete, click Delete     ,
     and then click Yes in the warning message that appears.

Use the Exchange Management Shell to delete a mailbox
To delete a mailbox, use this syntax:

  PowerShell

  Remove-Mailbox <MailboxIdentity> [-Arbitration] [-PublicFolder]

This example deletes the mailbox that has the email address pilarp@contoso.com.

  PowerShell

  Remove-Mailbox pilarp@contoso.com

This example deletes the equipment mailbox named Fleet Van (16).

  PowerShell

  Remove-Mailbox "Fleet Van (16)"

<!-- p.1224 -->

This example deletes the mailbox that has the alias value corpprint.

  PowerShell

  Remove-Mailbox corpprint

For detailed syntax and parameter information, see Remove-Mailbox.

  ７ Note

  If you use the Remove-Mailbox cmdlet with the Permanent switch, the mailbox is
  immediately purged and isn't recoverable. For more information, see Permanently delete
  a mailbox.

How do you know this worked?
To verify that you've successfully deleted a mailbox, do any of these steps:

     In the EAC, click Recipients, go to the appropriate tab for the type of mailbox that you
     deleted, and verify that the mailbox is no longer listed. Note that you might need to click
     Refresh     .

     In Active Directory Users and Computers, verify that the associated account is no longer
     listed. Note that mailbox types other than user and linked mailboxes also have associated
     user accounts that are disabled (for example, room, equipment, arbitration, shared, and
     public folder mailboxes).

     In the Exchange Management Shell replace <DisplayName> with the user's display name,
     and run the following commands to verify the DisconnectReason property value is
     Disabled (which indicates the mailbox has been marked for removal):

        PowerShell

        $dbs = Get-MailboxDatabase
        $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
        {$_.DisplayName -eq "<DisplayName>"} | Format-List
        DisconnectReason,DisconnectDate

     Notes:

        The DisconnectReason property doesn't distinguish between disabled and deleted
        mailboxes (the value for both is Disabled ). The absence of the associated user account
        indicates whether the mailbox was deleted.

<!-- p.1225 -->

        If the command returns no results, replace <DatabaseName> with the name of the
        mailbox database where the disconnected mailbox resides, and run the following
        command to synchronize the mailbox state for all disconnected mailboxes on the
        database:

          PowerShell

           Get-MailboxStatistics -Database "<DatabaseName>" | foreach {Update-
           StoreMailboxState -Database $_.Database -Identity $_.MailboxGuid -
           Confirm:$false}

        Then, run the previous command, which should now return results.

        In the Exchange Management Shell, replace <UserIdentity> with the name or user
        principal name of the user (for example, user@contoso.com), and run this command to
        verify that the user can't be found.

          PowerShell

             Get-User <UserIdentity>

More information
When you delete the Active Directory user account that's associated with a mailbox, Exchange
will detect that the mailbox is no longer connected to a user account, and will mark the
mailbox for removal, even if the mailbox has been placed on Litigation Hold or In-Place Hold.
To retain the mailbox, do these steps:

     Instead of deleting the user account, disable the user account.

     Change the properties of the mailbox to restrict its use and who has access to the
     mailbox. For example, set send and receive quotas equal to 1 , block who can send
     messages to the mailbox, and restrict who has access to the mailbox.

     Retain the mailbox until all data has been expunged, or until preserving the data is no
     longer required.

Disabling a user account in Active Directory, for example, keeps the associated mailbox active
but prevents the user from signing in with their credentials. This means that existing mailbox
configurations - such as inbox rules or email forwarding - will continue to function.

If you need to disable or remove inbox rules from the mailbox, use the Disable-InboxRule or
Remove-InboxRule cmdlets. To manage email forwarding on a mailbox - for example, to

<!-- p.1226 -->

disable an existing forwarding configuration - refer to the steps in the Configure email
forwarding for a mailbox documentation.

For more information, see In-Place Hold and Litigation Hold in Exchange Server.

<!-- p.1227 -->

Connect a disabled mailbox in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

When you disable a mailbox, Exchange retains the mailbox in the mailbox database and
switches the mailbox to a disabled state. The Exchange attributes are also removed from the
corresponding Active Directory user account, but the user account is retained. The mailbox is
retained until the deleted mailbox retention period expires, which is 30 days by default, before
it's then deleted permanently (or purged) from the mailbox database.

Until a disabled mailbox is permanently deleted from the Exchange mailbox database, you can
use the EAC or the Exchange Management Shell to reconnect it to the original Active Directory
user account.

To learn more about disconnected mailboxes and perform other related management tasks,
see the following topics:

      Disconnected mailboxes

      Disable or delete a mailbox in Exchange Server

      Connect or restore a deleted mailbox

      Permanently delete a mailbox

What do you need to know before you begin?
      Estimated time to complete: 2 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      Run the Get-User cmdlet in theExchange Management Shell to verify that the Active
      Directory user account that you want to connect the disabled mailbox to exists and that it
      isn't already associated with another mailbox. To connect a disabled mailbox to a user
      account, the account must exist and the value for the RecipientType property has to be
      User , which indicates that the account isn't already mailbox-enabled.

      You can also verify this information in Active Directory Users and Computers.

<!-- p.1228 -->

     Replace <DisplayName> with the display name of the mailbox, and run the following
     commands in the Exchange Management Shell to verify that the disabled mailbox that
     you want to connect to a user account exists and isn't a soft-deleted mailbox.

       PowerShell

       $dbs = Get-MailboxDatabase
       $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
       {$_.DisplayName -eq "<DisplayName>"} | Format-List
       DisplayName,Database,DisconnectReason

     To be able to connect a disabled mailbox, the mailbox has to exist in the mailbox
     database and the value for the DisconnectReason property has to be Disabled . If the
     mailbox has been purged from the database, the command won't return any results.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Recipient Provisioning
     Permissions" section in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to connect a disabled mailbox
The following procedure shows how to connect a disabled user mailbox. You can also
reconnect disabled linked mailboxes and disabled shared mailboxes to the corresponding user
account.

  1. In the EAC, navigate to Recipients > Mailboxes.

  2. Click More     , and then click Connect a mailbox.

     A list of mailboxes that are disconnected on the selected Exchange server in your
     Exchange organization will be displayed.

       ７ Note

<!-- p.1229 -->

        This list of disconnected mailboxes includes disabled mailboxes, deleted mailboxes,
        and soft-deleted mailboxes.

   3. Click the disabled mailbox that you want to reconnect, and then click Connect.

   4. In the window that asks if you're sure that you want to reconnect the mailbox, click Yes.

     Exchange will reconnect the disabled mailbox to the corresponding user account.

Use the Exchange Management Shell to connect a
disabled mailbox or personal archive
Use the Connect-Mailbox cmdlet in the Exchange Management Shell to connect a user
account to a disabled mailbox. You have to specify the type of mailbox that you're connecting.
The following examples show the syntax for reconnecting user, linked, shared, and archive
mailboxes.

This example connects a user mailbox. The Identity parameter specifies the disconnected
mailbox in the Exchange database. The User parameter specifies the Active Directory user
account to reconnect the mailbox to.

  PowerShell

  Connect-Mailbox -Identity "Jeffrey Zeng" -Database MBXDB01 -User "Jeffrey Zeng"

This example connects a linked mailbox. The Identity parameter specifies the disconnected
mailbox in the Exchange database. The LinkedMasterAccount parameter specifies the Active
Directory user account in the account forest that you want to reconnect the mailbox to. The
Alias parameter specifies the alias, which is the portion of the email address on the left side of
the at (@) symbol, for the reconnected mailbox.

  PowerShell

  Connect-Mailbox -Identity "Kai Axford" -Database MBXDB02 -LinkedDomainController
  FabrikamDC01 -LinkedMasterAccount kai.axford@fabrikam.com -Alias kaia

This example connects a shared mailbox.

  PowerShell

  Connect-Mailbox -Identity "Corporate Shared Mailbox" -Database "Mailbox Database
  03" -User "Corporate Shared Mailbox" -Alias corpshared -Shared

<!-- p.1230 -->

  ７ Note

  If you don't include the Alias parameter when you run the Connect-Mailbox cmdlet, the
  value specified in the User or LinkedMasterAccount parameter is used to create the email
  address alias for the reconnected mailbox.

This example connects a personal archive to the primary mailbox using the mailbox GUID
stored in mailbox database DB01.

  PowerShell

  Enable-Mailbox -Identity "Megan Bown" -ArchiveGUID "95352f8b-e5aa-496f-ac7f-
  ce93357d7b0c" -ArchiveDatabase "DB01" -Archive

If you do not know the name of the personal archive, you can view it in the Exchange
Management Shell by running the following command. This example returns all personal
archive mailboxes in mailbox database DB01.

  PowerShell

  Get-MailboxDatabase "DB01" | Get-MailboxStatistics | Where {($_.DisconnectDate -ne
  $null) -and ($_.IsArchiveMailbox -eq $true)} | Format-Table
  DisplayName,MailboxGuid -AutoSize

  ７ Note

  You can connect a personal archive mailbox to any primary mailbox you wish, even if it is
  not the original owner's mailbox. Use the AllowLegacyDNMismatch parameter to allow the
  connection of the archive mailbox to a different primary mailbox.

For detailed syntax and parameter information, see Connect-Mailbox.

How do you know this worked?
To verify that you've successfully connected a disabled mailbox to a user account, do one of
the following:

     In the EAC, click Recipients, navigate to the appropriate page for the mailbox type that
     you reconnected, click Refresh   , and verify that the mailbox is listed.

<!-- p.1231 -->

In Active Directory Users and Computers, right-click the user account whose mailbox you
disabled, and then click Properties. On the General tab, notice that the E-mail box is
populated with the email address for the reconnected mailbox.

In theExchange Management Shell,replace <Identity> with the name of the user account
and run the following command:

  PowerShell

  Get-User "<Identity>"

The UserMailbox value for the RecipientType property indicates that the user account and
the mailbox are connected. You can also run the Get-Mailbox cmdlet to verify that the
mailbox exists.

<!-- p.1232 -->

Connect or restore a deleted mailbox in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

When you delete a mailbox, Exchange retains the mailbox in the mailbox database and
switches the mailbox to a disabled state. The associated Active Directory user account is also
deleted. The mailbox is retained until the deleted mailbox retention period expires, which is 30
days by default, and then it's permanently deleted (or purged) from the mailbox database.

Until a deleted mailbox is permanently deleted from the Exchange mailbox database, you can
use the EAC or the Exchange Management Shell to connect it to an Active Directory user
account. You can also use the Exchange Management Shell to restore the contents of the
deleted mailbox to an existing mailbox.

To learn more about disconnected mailboxes and perform other related management tasks,
see the following topics:

      Disconnected mailboxes

      Disable or delete a mailbox in Exchange Server

      Connect a disabled mailbox

      Permanently delete a mailbox

What do you need to know before you begin?
      Estimated time to complete: 2 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      Create a new user account in Active Directory to connect the deleted mailbox to. Or use
      the Get-User cmdlet in the Exchange Management Shell to verify that the Active Directory
      user account that you want to connect the deleted mailbox to exists and that it isn't
      already associated with another mailbox. To connect a deleted mailbox to a user account,
      the account must exist and the value for the RecipientType property has to be User , which
      indicates that the account isn't already mailbox-enabled.

      For on-premises Exchange organizations, you can also verify this information in Active
      Directory Users and Computers.

<!-- p.1233 -->

       ） Important

       When you connect deleted linked mailboxes, resource mailboxes, or shared
       mailboxes, the Active Directory user account that you're connecting the mailbox to
       must be disabled.

     To verify that the deleted mailbox that you want to connect a user account to exists in the
     mailbox database and isn't a soft-deleted mailbox, run the following command:

       PowerShell

        Get-MailboxDatabase | foreach {Get-MailboxStatistics -Database $_.name} |
        where {$_.DisplayName -eq "<display name>"} | Format-List
        DisplayName,Database,DisconnectReason

     The deleted mailbox has to exist in the mailbox database and the value for the
     DisconnectReason property has to be Disabled . If the mailbox has been purged from the
     database, the command won't return any results.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Recipient Provisioning
     Permissions" section in the Recipients Permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

     Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
     Server   , Exchange Online   , or Exchange Online Protection      .

Connect a deleted mailbox
When you connect a deleted mailbox, you associate the mailbox with a user account that isn't
mail-enabled, which means that it doesn't have an existing mailbox. To connect a deleted
mailbox to a user account that has a mailbox, you have to restore the deleted mailbox. For
more information, see Restore a deleted mailbox later in this topic.

Use the EAC to connect a deleted mailbox
The following procedure shows how to connect a deleted user mailbox to a user account. You
can also use this procedure to connect linked mailboxes, resource mailboxes, and shared
mailboxes that have been deleted to a user account.

<!-- p.1234 -->

   1. In the EAC, go to Recipients > Mailboxes.

   2. Click More    , and then click Connect a mailbox.

     A list of mailboxes that are disconnected on the selected Exchange server in your
     Exchange organization will be displayed.

        ７ Note

        This list of disconnected mailboxes includes disabled mailboxes, deleted mailboxes,
        and soft-deleted mailboxes.

   3. Click the deleted mailbox that you want to connect a user to, and then click Connect.

   4. In the window that asks if you're sure that you want to connect the mailbox, click Yes.

     A list of user accounts that aren't mail-enabled is displayed.

   5. Click the user that you want to connect the deleted mailbox to, and then click OK.

     Exchange will connect the deleted mailbox to the user account that you selected.

Use the Exchange Management Shell to connect a deleted
mailbox
Use the Connect-Mailbox cmdlet in the Exchange Management Shell to connect a deleted
mailbox to a user account that isn't mail enabled. You have to specify the type of mailbox that
you're connecting. The following examples show the syntax for reconnecting user, linked,
room, equipment, and shared mailboxes. In all examples, the optional Alias parameter is used
to specify the email alias, which is the portion of the email address on the left side of the at (@)
symbol. If you don't include the Alias parameter, the value specified in the User or
LinkedMasterAccount parameter is used to create the alias for the email address for the
reconnected mailbox.

  ７ Note

  As previously stated, when you connect linked, resource, or shared mailboxes, the Active
  Directory user account that you're linking the mailbox to must be disabled.

This example connects a deleted user mailbox to a user account that isn't mail enabled. The
Identity parameter specifies the display name of the deleted mailbox retained in the mailbox

<!-- p.1235 -->

database named MBXDB01. The User parameter specifies the Active Directory user account to
connect the mailbox to.

  PowerShell

  Connect-Mailbox -Identity "Paul Cannon" -Database MBXDB01 -User "Robin Wood" -
  Alias robinw

  ７ Note

  You can also use the values for the LegacyDN or MailboxGuid properties to identify the
  deleted mailbox.

This example connects a linked mailbox. The Identity parameter specifies the deleted mailbox
on the mailbox database named MBXDB02. The LinkedMasterAccount parameter specifies the
Active Directory user account in the account forest that you want to connect the mailbox to.
The LinkedDomainController parameter specifies a domain controller in the account forest.

  PowerShell

  Connect-Mailbox -Identity "Temp User" -Database MBXDB02 -LinkedDomainController
  FabrikamDC01 -LinkedMasterAccount danpark@fabrikam.com -Alias dpark

This example connects a room mailbox.

  PowerShell

  Connect-Mailbox -Identity "rm2121" -Database "MBXResourceDB" -User "Conference
  Room 2121" -Alias ConfRm2121 -Room

This example connects an equipment mailbox.

  PowerShell

  Connect-Mailbox -Identity "MotorPool01" -Database "MBXResourceDB" -User "Van01 (12
  passengers)" -Alias van01 -Equipment

This example connects a shared mailbox.

  PowerShell

  Connect-Mailbox -Identity "Printer Support" -Database MBXDB01 -User "Corp Printer
  Support" -Alias corpprint -Shared

<!-- p.1236 -->

  ７ Note

  You can also use the LegacyDN or MailboxGuid values to identify the deleted mailbox.

For detailed syntax and parameter information, see Connect-Mailbox.

How do you know this worked?
To verify that you've successfully connected a deleted mailbox to a user account, do one of the
following steps:

     In the EAC, click Recipients, go to the appropriate page for the mailbox type that you
     connected, click Refresh     , and verify that the mailbox is listed.

     In Active Directory Users and Computers, right-click the user account that you connected
     to the mailbox, and then click Properties. On the General tab, notice that the E-mail box
     is populated with the email address for the connected mailbox.

     In the Exchange Management Shell, run the following command.

          PowerShell

          Get-User <identity>

     The UserMailbox value for the RecipientType property indicates that the user account and
     the mailbox are connected. You can also run the Get-Mailbox <identity> command to
     verify that the mailbox was connected.

Restore a deleted mailbox
You can use the Exchange Management Shell to restore a deleted mailbox to an existing
mailbox using the New-MailboxRestoreRequest cmdlet. When you restore a deleted mailbox,
its contents are copied to an existing mailbox, which is referred to as the target mailbox. After a
deleted mailbox is restored, it's still retained in the mailbox database until it's permanently
deleted by an administrator or purged after the deleted mailbox retention period expires.

After a mailbox restore request is successfully completed, it's retained for 30 days, by default,
before it's removed. You can remove the mailbox sooner by using the Remove-StoreMailbox
cmdlet.

  ７ Note

<!-- p.1237 -->

  You can't use the EAC to restore a deleted mailbox.

Use the Exchange Management Shell to restore a deleted
mailbox
To create a mailbox restore request, you have to use the display name, legacy distinguished
name (DN), or mailbox GUID of the deleted mailbox. Use the Get-MailboxStatistics cmdlet to
display the values of the DisplayName , MailboxGuid , and LegacyDN properties for the deleted
mailbox that you want to restore. For example, run the following commands to return this
information for all disabled and deleted mailboxes in your organization.

  PowerShell

  $dbs = Get-MailboxDatabase
  $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
  {$_.DisconnectReason -eq "Disabled"} | Format-Table
  DisplayName,MailboxGuid,Database,DisconnectDate

This example restores the deleted mailbox, which is identified by the SourceStoreMailbox
parameter and is located on the MBXDB01 mailbox database, to the target mailbox Debra
Garcia. The AllowLegacyDNMismatch parameter is used so the source mailbox can be restored
to a different mailbox, one that doesn't have the same legacy DN value.

  PowerShell

  New-MailboxRestoreRequest -SourceStoreMailbox e4890ee7-79a2-4f94-9569-91e61eac372b
  -SourceDatabase MBXDB01 -TargetMailbox "Debra Garcia" -AllowLegacyDNMismatch

This example restores Pilar Pinilla's deleted archive mailbox to her current archive mailbox. The
AllowLegacyDNMismatch parameter isn't necessary because a primary mailbox and its
corresponding archive mailbox have the same legacy DN.

  PowerShell

  New-MailboxRestoreRequest -SourceStoreMailbox "Personal Archive - Pilar Pinilla" -
  SourceDatabase "MDB01" -TargetMailbox pilarp@contoso.com -TargetIsArchive

For detailed syntax and parameter information, see New-MailboxRestoreRequest.

How do you know this worked?

<!-- p.1238 -->

To verify that you've successfully restored a deleted mailbox to the target mailbox, run the Get-
MailboxRestoreRequest cmdlet to display information about the restore request. If the restore
request was successfully created, the Status property will have a value of Queued , InProgress ,
or Completed . After the restore request is completed, the contents from the deleted mailbox
will appear in the target mailbox.

For more information, see:

     Manage Mailbox Restore Requests

     Get-MailboxRestoreRequest

     Get-MailboxRestoreRequestStatistics

<!-- p.1239 -->

Permanently delete a mailbox in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

When you permanently delete active mailboxes and disconnected mailboxes, all mailbox
contents are purged from the Exchange mailbox database, and the data loss is permanent.
When you permanently delete an active mailbox, the associated Active Directory user account
is also deleted.

An alternative to permanently deleting a mailbox is to disconnect it. After you disconnect a
mailbox, by default, Exchange retains the data in the mailbox database for 30 days. This gives
you the opportunity to reconnect or restore a mailbox before it's purged from the database.

To learn more about disconnected mailboxes and perform other related management tasks in
Exchange, see the following topics:

      Disconnected mailboxes

      Disable or delete a mailbox in Exchange Server

      Connect a disabled mailbox

      Connect or restore a deleted mailbox

  ７ Note

  You can't use the Exchange admin center (EAC) to permanently delete an active mailbox or
  a disconnected mailbox.

What do you need to know before you begin?
      Estimated time to complete: 2 minutes.

      The procedures in this topic require the Exchange Management Shell. For more
      information, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Recipient Provisioning
      Permissions" section in the Recipients Permissions topic.

<!-- p.1240 -->

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Use the Exchange Management Shell to
permanently delete an active mailbox
If you don't include the Permanent parameter when you delete a mailbox, the deleted mailbox
is retained in the mailbox database for 30 days (by default) before it's permanently deleted.

Run the following command to permanently delete an active mailbox and the associated Active
Directory user account:

  PowerShell

  Remove-Mailbox -Identity <Identity> -Permanent $true

For detailed syntax and parameter information, see Remove-Mailbox.

How do you know this worked?
To verify that you've permanently deleted an active mailbox, do the following:

   1. Verify that the mailbox is no longer listed in the Exchange admin center (EAC).

   2. Verify that the associated user account is no longer listed in Active Directory Users and
     Computers.

   3. Replace <DisplayName> with the display name of the mailbox and run the following
     commands in the Exchange Management Shell to verify that the mailbox was successfully
     purged from the Exchange mailbox database:

        PowerShell

        $dbs = Get-MailboxDatabase
        $dbs | foreach {Get-MailboxStatistics -Database $_.DistinguishedName} | where
        {$_.DisplayName -eq "<DisplayName>"}
