---
title: "Exchange Server — pages 121-160"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0121-0160
family: exchange
documentKind: "doc"
abstract: "For more information about the CSV file requirements for local move requests, see CSV Files for Mailbox Migration. ７ Note All mailboxes that are specified in the CSV file will be migrated, even if they are outside of the RBAC scope (for example, an OU) that gives the admin permi"
---

# Exchange Server — pages 121-160

<!-- p.121 -->

For more information about the CSV file requirements for local move requests, see CSV Files
for Mailbox Migration.

  ７ Note

  All mailboxes that are specified in the CSV file will be migrated, even if they are outside of
  the RBAC scope (for example, an OU) that gives the admin permissions to migrate
  mailboxes.

To create a migration batch, use this syntax:

  PowerShell

  New-MigrationBatch -Local [-AutoStart] [-AutoComplete] -Name "
  <MigrationBatchName>" -CSVData
  ([System.IO.File]::ReadAllBytes('<PathAndFileName>')) [<-ArchiveOnly | -
  PrimaryOnly>] [-TargetDatabases "<MailboxDatabase1>","<MailboxDatabase1>"... [-
  TargetArchiveDatabases "<MailboxDatabase1>","<MailboxDatabase1>"...] [-Priority
  <PriorityValue>] [-BadItemLimit <Value>] [-AcceptLargeDataLoss]

This example creates a migration batch with these settings:

     CSV file that specifies the mailboxes to move:
     C:\Users\Administrator\Desktop\LocalMove 01.csv. If you only want to move the primary
     mailbox, use the PrimaryOnly switch, or the MailboxType value PrimaryOnly in the CSV
     file. If you only want to move the archive mailbox, use the ArchiveOnly switch, or the
     MailboxType value ArchiveOnly in the CSV file.

     Batch name: LocalMove 01.

     Target database: MBX DB02. If we don't use the TargetDatabase parameter, and the
     primary mailbox databases aren't specified in the CSV file, the automatic distribution logic
     in Exchange randomly selects databases in the Active Directory site.

     Target database for archive mailboxes: MBX DB02. Because we aren't using the
     ArchiveTargetDatabase parameter (in the command or the CSV file), the archive mailbox
     database is moved to the same database as the primary mailbox.

     If we use the ArchiveOnly switch (in the command or CSV file) without using the
     ArchiveTargetDatabase parameter (in the command or CSV file), the automatic
     distribution logic in Exchange will randomly select databases in the Active Directory site.

     When to start the migration: Immediately, because we're using the AutoStart switch. If
     we don't use this switch, we need to use the Start-MigrationBatch cmdlet to start the

<!-- p.122 -->

     migration batch after it's created.

     When to complete the migration: After the mailboxes complete their initial
     synchronization, because we're using the AutoComplete switch. If we don't use this switch,
     we need to use the Complete-MigrationBatch cmdlet to start the migration batch after
     it's created

     Priority: Normal , because we aren't using the Priority parameter.

     Bad item limit: 10 (the default value in the Exchange Management Shell is 0). Because the
     value is less than 51, we don't need to use the AcceptLargeDataLoss switch.

  PowerShell

  New-MigrationBatch -Local -AutoStart -AutoComplete -Name "LocalMove 01" -CSVData
  ([System.IO.File]::ReadAllBytes("C:\Users\Administrator\Desktop\LocalMove
  01.csv")) -TargetDatabases "MBX DB02" -BadItemLimit 10

How do you know this worked?
To verify that you've successfully created a local move request, do any of these steps:

     In the EAC, go to Recipients > Migration and verify the status of the move request (note
     that you might need to click Refresh        ). You can select the move request, and see more
     information in the details pane, or by clicking Edit     .

     In the EAC, go to Recipients > Migration and click Status For All Batches.

     Check the notification message. The sender is Microsoft Outlook. When the move request
     is complete, you'll get a message with the subject Migration batch <MigrationBatchName>
     has completed successfully .

     In the EAC, click the notification viewer     to view the status of the request.

     In the Exchange Management Shell, replace <MailboxIdentity> with the name, email
     address, or alias of the mailbox, and run this command to verify the basic property values:

        PowerShell

        Get-MoveRequest -Identity <MailboxIdentity> | Format-List
        DisplayName,Alias,Status,*database*

     In the Exchange Management Shell, replace <BatchName> with the batch name value of
     the move request, and run this command to verify the basic property values:

<!-- p.123 -->

        PowerShell

        Get-MoveRequest -BatchName <BatchName> | Format-List
        DisplayName,Alias,Status,*database*

     Note: If you created the move request in the EAC, the batch name value is
      MigrationService:<BatchNameValueFromTheEAC> .

     If you created the move request in the EAC, replace <BatchName> with the batch name
     value you specified, and run this command in the Exchange Management Shell to verify
     summary information about all mailboxes in the move:

        PowerShell

        Get-MigrationUserStatistics -BatchId <BatchName>

     If you created the move request in the EAC, replace <EmailAddress> with the email
     address of the moved mailbox, and run this command to see detailed information about
     the specified mailbox:

        PowerShell

        Get-MigrationUserStatistics -Identity <EmailAddress> | Format-List

For more information, see Get-MigrationUserStatistics.

Display migration batches
For an example of how to use the Exchange Management Shell to display a migration batch,
see Example 2 in Get-MigrationBatch.

Create a cross-forest move using a .csv batch file
This example configures the migration endpoint, and then creates a cross-forest batch move
from the source forest to the target forest using a .csv file.

  PowerShell

  New-MigrationEndpoint -Name Fabrikam -ExchangeRemote -Autodiscover -EmailAddress
  tonysmith@fabrikam.com -Credentials (Get-Credential fabrikam\tonysmith)
  $csvData=
  [System.IO.File]::ReadAllBytes("C:\Users\Administrator\Desktop\batch.csv")

<!-- p.124 -->

  New-MigrationBatch -CSVData $csvData -Timezone "Pacific Standard Time" -Name
  FabrikamMerger -SourceEndpoint Fabrikam -TargetDeliveryDomain "mail.contoso.com"

For more information about preparing your forest for cross-forest moves, see the following
topics:

     Prepare mailboxes for cross-forest move requests

     Prepare Mailboxes for Cross-Forest Moves Using Sample Code

     Prepare mailboxes for cross-forest moves using the Exchange Management Shell

For detailed syntax and parameter information, see New-MigrationBatch and New-
MoveRequest.

How do you know this worked?
To verify that you have successfully completed your migration, do the following:

     From the Exchange Management Shell, run the following command to retrieve mailbox
     move information.

          PowerShell

          Get-MigrationUserStatistics -Identity BatchName -Status | Format-List

For more information, see Get-MigrationUserStatistics.

<!-- p.125 -->

Prepare mailboxes for cross-forest move
requests in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Mailbox moves and mailbox migrations in Exchange 2016 and Exchange 2019 from one forest
to another require that you prepare the destination forest, which is made easier by Exchange
tools and cmdlets. Exchange 2016 supports mailbox moves and migrations using the Exchange
Management Shell, specifically the New-MoveRequest and New-MigrationBatch cmdlets. You
can also move the mailbox in the Exchange admin center (EAC).

To move an Exchange mailbox from a source forest to the target Exchange 2016 or Exchange
2019 target forest, the target forest needs to contain a valid mail user (also known as a mail-
enabled user) with a specified set of Active Directory attributes.

      In Exchange 2016, you can move an Exchange 2010, Exchange 2013, or Exchange 2016
      mailbox from a source Exchange forest to a target Exchange 2016 forest. If there's at least
      one Exchange 2016 Mailbox server in the target forest, the forest is considered an
      Exchange 2016 forest.

      In Exchange 2019, you can move an Exchange 2013, Exchange 2016, or Exchange 2019
      mailbox from a source Exchange forest to a target Exchange 2019 forest. If there's at least
      one Exchange 2019 Mailbox server in the target forest, the forest is considered an
      Exchange 2019 forest.

To prepare for the mailbox move, you need to create mail users (also known as mail-enabled
users) with the required Active Directory attributes in the target forest. There are two
recommended approaches for creating mail users with the necessary attributes:

      If you deployed Identity Lifecycle Manager (ILM) for cross-forest global address list (GAL)
      synchronization, we recommend that you use Microsoft Identity Manager 2016 Service
      Pack 1. We've created sample code that you can use to learn how to customize ILM to
      synchronize the source mailbox user and target mail user.

      For more information, including how to download the sample code, see Prepare
      mailboxes for cross-forest moves using sample code.

      If you created the target mail user using an Active Directory tool other than ILM or
      Microsoft Identity Integration Server (MIIS), use the Update-Recipient cmdlet with the
      Identity parameter to generate the LegacyExchangeDN attribute for the target mail user.
      We've created a sample PowerShell script that reads from and writes to Active Directory
      and calls the Update-Recipient cmdlet.

<!-- p.126 -->

      For more information about using the sample script, see Prepare mailboxes for cross-
      forest moves using the Exchange Management Shell.

After creating the target mail user, you can then run the New-MoveRequest or the New-
MigrationBatch cmdlets to move the mailbox to the target Exchange 2016 or Exchange 2019
forest.

For more information about remote move requests, see the following topics:

      New-MigrationBatch

      New-MoveRequest

The remainder of this topic describes the mail user Active Directory attributes that are required
for a mailbox move. These attributes are configured for you when you use either the code or
the script to prepare for the mailbox move. However, you can manually copy these attributes
using an Active Directory editor.

Active Directory user attributes required for a
mailbox move
To support a remote mailbox move, the mail user object in the target Exchange forest must
have the Active Directory attributes that are described in this section:

      Mandatory attributes

      Optional attributes

      Linked attributes

      Linked user attributes

      Resource mailbox attributes

      Additional attributes

Mandatory attributes
The following table lists the minimum set of attributes that need to be configured in ILM on
the target mail user for the New-MoveRequest cmdlet to function correctly.

Mail user attributes

                                                                                ﾉ   Expand table

<!-- p.127 -->

Active Directory attribute   Action

displayName                  Copy the corresponding attribute of the source mailbox or generate a
                             new value.

Mail                         Directly copy the corresponding attribute of the source mailbox.

mailNickname                 Copy the corresponding attribute of the source mailbox or generate a
                             new value.

msExchArchiveGUID and        Directly copy the corresponding attribute of the source mailbox.
msExchArchiveName

msExchMailboxGUID            Directly copy the corresponding attribute of the source mailbox.

msExchRecipientDisplayType   -2147483642 decimal (equivalent to 0x80000006 hex).

msExchRecipientTypeDetails   128 decimal (0x80 hex).

msExchUserCulture            Directly copy the corresponding attribute of the source mailbox.

msExchVersion                44220983382016 (decimal).

cn                           Copy the corresponding attribute of the source mailbox or generate a
                             new value.

proxyAddresses               Copy source mailbox's proxyAddresses attribute. Additionally, copy
                             source mailbox's LegacyExchangeDN as an X500 address in the
                             proxyAddresses attribute of the target mail user.
                             Note: The proxyAddresses of the source mailbox user must contain an
                             SMTP address that matches the authoritative domain of the target
                             forest. This allows the New-MoveRequest cmdlet to correctly select the
                             targetAddress of the source mail-enabled user (converted from the
                             source mailbox user after the mailbox move request is complete) to
                             ensure that mail routing is still functional.

sAMAccountName               Copy the corresponding attribute of the source mailbox or generate a
                             new value.
                             Ensure that the value is unique within the target forest domain that the
                             target mail user belongs to.

targetAddress                Set to an SMTP address in the proxyAddresses attribute of the source
                             mailbox.
                             This SMTP address must belong to the authoritative domain of the
                             source forest.

userAccountControl           Constant: 514 (equivalent to 0x202, ACCOUNTDISABLE |
                             NORMAL_ACCOUNT).

userPrincipalName            Copy the corresponding attribute of the source mailbox or generate a
                             new value. Because the mail user is logon disabled, this
                             userPrincipalName isn't used.

<!-- p.128 -->

Optional attributes
The following attributes aren't required for the New-MoveRequest cmdlet to function
correctly; however, synchronizing them provides a better end-to-end user experience after
moving the mailbox. Because the GAL in the target forest displays this target mail user, you
should set the following GAL-related attributes.

GAL-related attributes

                                                                                         ﾉ   Expand table

 Mail user's Active Directory attribute   Action

 c                                        Directly copy the corresponding attribute of the source mailbox.

 co                                       Directly copy the corresponding attribute of the source mailbox.

 countryCode                              Directly copy the corresponding attribute of the source mailbox.

 company                                  Directly copy the corresponding attribute of the source mailbox.

 department                               Directly copy the corresponding attribute of the source mailbox.

 facsimileTelephoneNumber                 Directly copy the corresponding attribute of the source mailbox.

 givenName                                Directly copy the corresponding attribute of the source mailbox.

 homePhone                                Directly copy the corresponding attribute of the source mailbox.

 info                                     Directly copy the corresponding attribute of the source mailbox.

 initials                                 Directly copy the corresponding attribute of the source mailbox.

 l                                        Directly copy the corresponding attribute of the source mailbox.

 mobile                                   Directly copy the corresponding attribute of the source mailbox.

 msExchAssistantName                      Directly copy the corresponding attribute of the source mailbox.

 msExchHideFromAddressLists               Directly copy the corresponding attribute of the source mailbox.

 otherHomePhone                           Directly copy the corresponding attribute of the source mailbox.

 otherTelephone                           Directly copy the corresponding attribute of the source mailbox.

 pager                                    Directly copy the corresponding attribute of the source mailbox.

 physicalDeliveryOfficeName               Directly copy the corresponding attribute of the source mailbox.

 postalCode                               Directly copy the corresponding attribute of the source mailbox.

<!-- p.129 -->

 Mail user's Active Directory attribute   Action

 sn                                       Directly copy the corresponding attribute of the source mailbox.

 st                                       Directly copy the corresponding attribute of the source mailbox.

 streetAddress                            Directly copy the corresponding attribute of the source mailbox.

 telephoneAssistant                       Directly copy the corresponding attribute of the source mailbox.

 telephoneNumber                          Directly copy the corresponding attribute of the source mailbox.

 title                                    Directly copy the corresponding attribute of the source mailbox.

Linked attributes
A linked attribute is an Active Directory attribute that references other Active Directory objects
in the local forest. You can't directly copy the linked attribute values from a mailbox in the
source forest to a mail user in the target forest. Instead, you do the following steps:

      1. Find the Active Directory objects in the source forest that the source mailbox attribute
         refers to.

      2. Find the corresponding Active Directory objects in the target forest.

      3. Set the target mail user's attribute to refer to the Active Directory objects in the target
         forest.

Linked attributes

                                                                                          ﾉ    Expand table

 Mail user's Active Directory   Action
 attribute

 altRecipient                   Correspond to the source mailbox's altRecipient attribute.

 deliverAndRedirect             Directly copy the corresponding attribute of the source mailbox. This
                                attribute is a Boolean value that should be set along with altRecipient.

 Manager (and its backlinks)    Correspond to the source mailbox's manager attribute.

 MemberOf (backlinks)           This is the backlink of group member attribute.

 publicDelegates (and its       Correspond to the source mailbox's publicDelegates attribute.
 backlinks)

<!-- p.130 -->

Linked user attributes
If you want to move a mailbox to an Exchange resource forest, the mailbox in the resource
forest is considered a linked mailbox. In this scenario, you need to create a linked mail user in
the (target) resource forest. To create a linked mail user, you need to set the attributes shown
in the following table.

Linked mail user attributes

                                                                                     ﾉ   Expand table

 Active Directory attribute    Action

 msExchMasterAccountHistory    Directly copy the corresponding attribute of the source mailbox.

 msExchMasterAccountSid        If the source mailbox has msExchMasterAccountSid, copy it. Otherwise,
                               copy the source mailbox's objectSid.

 msExchRecipientDisplayType    Constant:-1073741818 decimal (equivalent to *unsigned* 0xC0000006 ).

  ７ Note

  A linked mailbox can only be created if there's a forest trust between the source forest and
  target forest.

If the source object is disabled and the msExchMasterAccountSid attribute is set to self
(resource mailbox, shared mailbox), don't stamp anything on the target user.

If the source object is disabled and the msExchMasterAccountSid attribute isn't set, the
mailbox is invalid.

If the source object is enabled and the msExchMasterAccountSid attribute is set, the mailbox is
invalid.

Resource mailbox attributes
If you want to move a resource mailbox to an Exchange forest, you need to set the attributes
shown in the following table on the target mail user.

Resource mailbox attributes

                                                                                     ﾉ   Expand table

<!-- p.131 -->

 Mail user's Active Directory          Action
 attribute

 msExchRecipientDisplayType            If the source mailbox is a conference room: Constant: -2147481850
                                       decimal (equivalent to *unsigned* 0x80000706 ).
                                       If the source mailbox is an equipment mailbox: Constant:
                                       -2147481594 decimal (equivalent to *unsigned* 0x80000806 ).

 msExchResourceCapacity                Directly copy the corresponding attribute of the source mailbox.

 msExchResourceDisplay                 Directly copy the corresponding attribute of the source mailbox.

 msExchResourceMetaData                Directly copy the corresponding attribute of the source mailbox.

 msExchResourceSearchProperties        Directly copy the corresponding attribute of the source mailbox.

Additional attributes
Resource mailbox attributes

                                                                                        ﾉ   Expand table

 Mail User's Active Directory attributes             Description

 comment                                             Directly copy the corresponding attribute of the
                                                     source mailbox.

 deletedItemFlags                                    Directly copy the corresponding attribute of the
                                                     source mailbox.

 delivContLength                                     Directly copy the corresponding attribute of the
                                                     source mailbox.

 departmentNumber                                    Directly copy the corresponding attribute of the
                                                     source mailbox.

 description                                         Directly copy the corresponding attribute of the
                                                     source mailbox.

 division                                            Directly copy the corresponding attribute of the
                                                     source mailbox.

 employeeID                                          Directly copy the corresponding attribute of the
                                                     source mailbox.

 employeeNumber                                      Directly copy the corresponding attribute of the
                                                     source mailbox.

 employeeType                                        Directly copy the corresponding attribute of the

<!-- p.132 -->

Mail User's Active Directory attributes   Description

                                          source mailbox.

extensionAttribute1-15                    Directly copy the corresponding attribute of the
                                          source mailbox.

homePostalAddress                         Directly copy the corresponding attribute of the
                                          source mailbox.

internationalISDNNumber                   Directly copy the corresponding attribute of the
                                          source mailbox.

ipPhone                                   Directly copy the corresponding attribute of the
                                          source mailbox.

language                                  Directly copy the corresponding attribute of the
                                          source mailbox.

lmPwdHistory                              Directly copy the corresponding attribute of the
                                          source mailbox.

localeID                                  Directly copy the corresponding attribute of the
                                          source mailbox.

mAPIRecipient                             Directly copy the corresponding attribute of the
                                          source mailbox.

middleName                                Directly copy the corresponding attribute of the
                                          source mailbox.

msDS-PhoneticCompanyName                  Directly copy the corresponding attribute of the
                                          source mailbox.

msDS-PhoneticDepartment                   Directly copy the corresponding attribute of the
                                          source mailbox.

msDS-PhoneticDisplayName                  Directly copy the corresponding attribute of the
                                          source mailbox.

msDS-PhoneticFirstName                    Directly copy the corresponding attribute of the
                                          source mailbox.

msDS-PhoneticLastName                     Directly copy the corresponding attribute of the
                                          source mailbox.

msExchBlockedSendersHash                  Directly copy the corresponding attribute of the
                                          source mailbox.

msExchELCExpirySuspensionEnd              Directly copy the corresponding attribute of the
                                          source mailbox.

<!-- p.133 -->

Mail User's Active Directory attributes      Description

msExchELCExpirySuspensionStart               Directly copy the corresponding attribute of the
                                             source mailbox.

msExchELCMailboxFlags                        Directly copy the corresponding attribute of the
                                             source mailbox.

msExchExternalOOFOptions                     Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMessageHygieneFlags                    Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMessageHygieneSCLDeleteThreshold       Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMessageHygieneSCLJunkThreshold         Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMessageHygieneSCLQuarantineThreshold   Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMessageHygieneSCLRejectThreshold       Directly copy the corresponding attribute of the
                                             source mailbox.

msExchMDBRulesQuota                          Directly copy the corresponding attribute of the
                                             source mailbox.

msExchPoliciesExcluded                       Directly copy the corresponding attribute of the
                                             source mailbox.

msExchSafeRecipientsHash                     Directly copy the corresponding attribute of the
                                             source mailbox.

msExchSafeSendersHash                        Directly copy the corresponding attribute of the
                                             source mailbox.

msExchUMSpokenName                           Directly copy the corresponding attribute of the
                                             source mailbox.

otherFacsimileTelephoneNumber                Directly copy the corresponding attribute of the
                                             source mailbox.

otherIpPhone                                 Directly copy the corresponding attribute of the
                                             source mailbox.

otherMobile                                  Directly copy the corresponding attribute of the
                                             source mailbox.

otherPager                                   Directly copy the corresponding attribute of the
                                             source mailbox.

<!-- p.134 -->

Mail User's Active Directory attributes   Description

preferredDeliveryMethod                   Directly copy the corresponding attribute of the
                                          source mailbox.

personalPager                             Directly copy the corresponding attribute of the
                                          source mailbox.

personalTitle                             Directly copy the corresponding attribute of the
                                          source mailbox.

photo                                     Directly copy the corresponding attribute of the
                                          source mailbox.

pOPCharacterSet                           Directly copy the corresponding attribute of the
                                          source mailbox.

pOPContentFormat                          Directly copy the corresponding attribute of the
                                          source mailbox.

postalAddress                             Directly copy the corresponding attribute of the
                                          source mailbox.

postOfficeBox                             Directly copy the corresponding attribute of the
                                          source mailbox.

primaryInternationalISDNNumber            Directly copy the corresponding attribute of the
                                          source mailbox.

primaryTelexNumber                        Directly copy the corresponding attribute of the
                                          source mailbox.

showInAdvancedViewOnly                    Directly copy the corresponding attribute of the
                                          source mailbox.

street                                    Directly copy the corresponding attribute of the
                                          source mailbox.

terminalServer                            Directly copy the corresponding attribute of the
                                          source mailbox.

textEncodedORAddress                      Directly copy the corresponding attribute of the
                                          source mailbox.

thumbnailLogo                             Directly copy the corresponding attribute of the
                                          source mailbox.

thumbnailPhoto                            Directly copy the corresponding attribute of the
                                          source mailbox.

url                                       Directly copy the corresponding attribute of the
                                          source mailbox.

<!-- p.135 -->

Mail User's Active Directory attributes   Description

userCert                                  Directly copy the corresponding attribute of the
                                          source mailbox.

userCertificate                           Directly copy the corresponding attribute of the
                                          source mailbox.

userSMIMECertificate                      Directly copy the corresponding attribute of the
                                          source mailbox.

wWWHomePage                               Directly copy the corresponding attribute of the
                                          source mailbox.

<!-- p.136 -->

Prepare mailboxes for cross-forest moves
using the Exchange Management Shell
Article • 04/30/2025

APPLIES TO:            2016   2019   Subscription Edition

Exchange Server supports mailbox moves and migrations using the Exchange Management
Shell New-MoveRequest and New-MigrationBatch cmdlets. You can also move the mailbox in
the Exchange admin center (EAC).

      In Exchange 2016, you can move an Exchange 2010, Exchange 2013, or Exchange 2016
      mailbox from a source Exchange forest to a target Exchange 2016 forest.

      In Exchange 2019, you can move an Exchange 2013, Exchange 2016, or Exchange 2019
      mailbox from a source Exchange forest to a target Exchange 2019 forest.

To run the New-MoveRequest and New-MigrationBatch cmdlets, a mail user must exist in the
target Exchange forest, and the mail user must have a minimum set of required Active
Directory attributes.

The sample Exchange PowerShell script described in this topic supports this task by
synchronizing mailbox users from an Exchange source forest to Exchange target forests as mail
users (also known as mail-enabled users). The script copies the Active Directory attributes of
the mailbox users in the source forest to the target forest, and then uses the Update-Recipient
cmdlet to turn the target objects into mail users.

For more information about using and writing scripts, see About Scripts. For more information
about preparing for cross-forest moves, see Prepare mailboxes for cross-forest move requests.

Looking for other management tasks related to remote move requests? Check out Manage on-
premises mailbox moves in Exchange Server.

What do you need to know before you begin?
      Locate the Prepare-MoveRequest.ps1 script in %ExchangeInstallPath%Scripts. By default,
      %ExchangeInstallPath% is C:\Program Files\Microsoft\Exchange Server\V15\ (note the
      trailing '\').

      To run the sample script, you need the following:

         An Exchange source forest (where the mailbox currently resides).

<!-- p.137 -->

           For Exchange 2016 target forests, the source mailbox can be in Exchange 2010,
           Exchange 2013, or Exchange 2016.

           For Exchange 2019 target forests, the source mailbox can be in Exchange 2013,
           Exchange 2016, or Exchange 2019.

        A target forest with Exchange 2016 or Exchange 2019 installed (where the mailbox will
        be moved to).

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the Prepare-MoveRequest.ps1 script to prepare
mailboxes for cross-forest moves
Run the script from the Exchange Management Shell on a Mailbox server in the target
Exchange 2016 or Exchange 2019 forest. The script copies the mailbox attributes from the
source forest.

To assign a specific authentication credential for the remote forest domain controller, you must
first run the Windows PowerShell Get-Credential cmdlet and store the user input in a
temporary variable. When you run the Get-Credential cmdlet, the cmdlet asks for the user
name and password of the account used during authentication with the remote forest domain
controller. You can then use the temporary variable in the Prepare-MoveRequest.ps1 script. For
more information about the Get-Credential cmdlet, see Get-Credential.

  ７ Note

  Make sure that you use two separate credentials for the local forest and the remote forest
  when calling this script.

   1. Run the following commands to get the local forest and remote forest credentials.

        PowerShell

        $LocalCredentials = Get-Credential

        PowerShell

<!-- p.138 -->

            $RemoteCredentials = Get-Credential

   2. Run the following commands to pass the credential information to the
      LocalForestCredential and RemoteForestCredential parameters in the Prepare-
      MoveRequest.ps1 script.

            PowerShell

            Prepare-MoveRequest.ps1 -Identity JohnSmith@Fabrikan.com -
            RemoteForestDomainController DC001.Fabrikam.com -RemoteForestCredential
            $RemoteCredentials -LocalForestDomainController DC001.Contoso.com -
            LocalForestCredential $LocalCredentials

Parameter set of the script
The following table describes the parameter set for the script.

                                                                                       ﾉ   Expand table

 Parameter                      Required   Description

 Identity                       Required   The Identity parameter uniquely identifies a mailbox in the
                                           source forest. Identity can be any of the following values:
                                           Common name (CN), Alias, proxyAddress property,
                                           objectGuid property, or DisplayName property

 RemoteForestCredential         Required   The RemoteForestCredential parameter specifies the
                                           administrator who has permissions to copy data from the
                                           source forest Active Directory.

 RemoteForestDomainController   Required   The RemoteForestDomainController parameter specifies a
                                           domain controller in the source forest where the mailbox
                                           resides.

 DisableEmailAddressPolicy      Optional   The DisableEmailAddressPolicy parameter specifies whether
                                           the Email Address Policy (EAP) should be disabled when
                                           creating a MailUser object in the target forest.
                                           When you specify this parameter, the EAP in the target
                                           forest won't be applied.
                                           Note: When you specify this parameter, the MailUser object
                                           won't have e-mail address mapping in the local forest
                                           domain stamped. This is usually stamped by the EAP.

 LinkedMailUser                 Optional   The LinkedMailUser switch specifies whether to create a
                                           linked MailUser in the local forest for the mailbox user in
                                           the remote forest.

<!-- p.139 -->

Parameter                     Required   Description

                                         If the switch is provided, the script creates a target MailUser
                                         object linked to the source mailbox. If the switch is omitted,
                                         the script creates a regular target MailUser object.

LocalForestCredential         Optional   The LocalForestCredential parameter specifies the
                                         administrator with permissions to write data to the target
                                         forest Active Directory.
                                         We recommend that you explicitly specify this parameter to
                                         avoid Active Directory permission issues.
                                         If the remote forest and the local forest have a trusted
                                         relationship configured, don't use a user account from the
                                         remote forest as the local forest credential, even though the
                                         remote user account may have permission to modify Active
                                         Directory in the local forest.

LocalForestDomainController   Optional   The LocalForestDomainController parameter specifies a
                                         domain controller in the target forest where the mail user
                                         will be created.
                                         We recommend that you specify this parameter to avoid
                                         possible domain controller replication delay issues in the
                                         local forest that could occur if a random domain controller
                                         is selected.

MailboxDeliveryDomain         Optional   The MailboxDeliveryDomain parameter specifies an
                                         authoritative domain of the source forest so that the script
                                         can select the correct source mailbox user's proxyAddress
                                         property as the target mail user's targetAddress property.
                                         By default, the primary SMTP address of the source mailbox
                                         user is set as the targetAddress property of the target mail
                                         user.

OverWriteLocalObject          Optional   The OverWriteLocalObject parameter is used for users
                                         created by the Active Directory Migration Tool. The
                                         properties are copied from the existing mail contact to the
                                         newly created mail user. However, after this copy, the script
                                         also copies the properties from the source forest user to the
                                         newly created mail user.

TargetMailUserOU              Optional   The TargetMailuserOU parameter specifies the
                                         organizational unit (OU) under which the target mail user
                                         will be created.

UseLocalObject                Optional   The UseLocalObject parameter specifies whether to convert
                                         the existing local object to the required target mail user if
                                         the script detects an object in the local forest that conflicts
                                         with the to-be-created mail user.

<!-- p.140 -->

Examples
This section contains several examples of how you can use the Prepare-MoveRequest.ps1
script.

Example: Single linked mail user
This example provisions a single linked mail user in the local forest, when there is forest trust
between the remote forest and local forest.

   1. Run the following commands to get the local forest and remote forest credentials.

          PowerShell

          $LocalCredentials = Get-Credential

          PowerShell

          $RemoteCredentials = Get-Credential

   2. Run the following command to pass the credential information to the
      LocalForestCredential and RemoteForestCredential parameters in the Prepare-
      MoveRequest.ps1 script.

          PowerShell

          Prepare-MoveRequest.ps1 -Identity JamesAlvord@Contoso.com -
          RemoteForestDomainController DC001.Fabrikam.com -RemoteForestCredential
          $RemoteCredentials -LocalForestDomainController DC001.Contoso.com -
          LocalForestCredential $LocalCredentials -LinkedMailUser

Example: Pipelining
This example supports pipelining if you supply a list of mailbox identities.

   1. Run the following command.

          PowerShell

          $UserCredentials = Get-Credential

   2. Run the following command to pass the credential information to the
      RemoteForestCredential parameter in the Prepare-MoveRequest.ps1 script.

<!-- p.141 -->

           PowerShell

           "IanP@Contoso.com", "JoeAn@Contoso.com" | Prepare-MoveRequest.ps1 -
           RemoteForestDomainController DC001.Fabrikam.com -RemoteForestCredential
           $UserCredentials

Example: Use a .csv file to bulk-create mail users
You can generate a .csv file containing a list of mailbox identities from the source forest, which
allows you to pipe the content of this file into the script to bulk-create the target mail users.

For example, the content of the .csv file can be:

  PowerShell

  Identity
  Ian@contoso.com
  John@contoso.com
  Cindy@contoso.com

This example calls a .csv file to bulk create the target mail users.

   1. Run the following command to get the remote forest credentials.

           PowerShell

           $UserCredentials = Get-Credential

   2. Run the following command to pass the credential information to the
     RemoteForestCredential parameter in the Prepare-MoveRequest.ps1 script.

           PowerShell

           Import-Csv Test.csv | Prepare-MoveRequest.ps1 -RemoteForestDomainController
           DC001.Fabrikam.com -RemoteForestCredential $UserCredentials

Script behavior per target object
This section describes how the script performs in relation to several scenarios for target
objects.

Duplicate target mail-enabled object

<!-- p.142 -->

When the script attempts to create a target mail user from the source mailbox user, and it
detects a duplicate local mail-enabled object, it uses the following logic:

     If the source mailbox user's masterAccountSid attribute equals any target object's
     objectSid or masterAccountSid attribute:

        If the target object isn't mail-enabled, the script returns an error because the script
        doesn't support converting an object that isn't mail-enabled to a mail user.

        If the target object is mail-enabled, the target object is a duplicate.

     If an address in the source mailbox user's proxyAddress properties (smtp/x500 only)
     equals an address in a target object's proxyAddress properties (smtp/x500 only), the
     target object is a duplicate.

The script prompts the user about the duplicate objects.

If the target mail-enabled object is a mail user or mail contact, which is most likely created by a
cross-forest global address list (GAL) synchronization deployment, you can run the script again
with the UseLocalObject parameter to use the target mail-enabled object for mailbox migration.

Mail user
If the target object is a mail user, the script copies the following attributes from the source
mailbox user to the target mail user:

     msExchMailboxGUID

     msExchArchiveGUID

     msExchArchiveName

If the LinkedMailUser parameter is set, the script copies the source objectSid /
masterAccountSid attribute.

Mail contact
If the target object is a mail contact, the script deletes the existing contact and copies all its
attributes to a new mail user. The script also copies the following attributes from the source
mailbox user:

     msExchMailboxGUID

     msExchArchiveGUID

<!-- p.143 -->

     msExchArchiveName

     sAMAccountName

     userAccountControl (set to 514; equivalent to 0x202, ACCOUNTDISABLE | NORMAL_ACCOUNT )

     userPrincipalName

If the LinkedMailUser parameter is set, the script copies the source objectSid /
masterAccountSid attribute.

LegacyExchangeDN attribute
When the Update-Recipient cmdlet is called to convert the target object into a mail user, a
new LegacyExchangeDN attribute is generated for the target mail user. The script copies the
LegacyExchangeDN attribute of the target mail user as an x500 address to the proxyAddress
properties of the source mailbox user.

<!-- p.144 -->

Enable the MRS Proxy endpoint in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

The Mailbox Replication Service (MRS) has a proxy endpoint that's required for cross-forest
mailbox moves and remote move migrations between your on-premises Exchange
organization and Microsoft 365 or Office 365. You need to enable the MRS proxy endpoint in
the Exchange Web Services (EWS) virtual directory settings on Exchange 2016 or Exchange
2019 Mailbox servers.

Where you enable the MRS Proxy endpoint depends on the type and direction of the mailbox
move:

      Cross-forest enterprise moves: For cross-forest moves that are initiated from the target
      forest (known as a pull move type), you need to enable the MRS Proxy endpoint on
      Mailbox servers in the source forest. For cross-forest moves that are initiated from the
      source forest (known as a push move type), you need to enable the MRS Proxy endpoint
      on Mailbox servers in the target forest.

      Remote move migrations between an on-premises Exchange organization and
      Microsoft 365 or Office 365. For both onboarding and offboarding remote move
      migrations, you need to enable the MRS Proxy endpoint on Mailbox servers in your on-
      premises Exchange organization.

      Staged migrations between an on-premises Exchange organization and Microsoft 365
      or Office 365: For staged migration into M365, you need to enable the MRS Proxy
      endpoint on Mailbox servers in your on-premises Exchange organization. For more
      information on Staged migration, see Perform a staged migration of email in Exchange
      Online.

      Cutover migrations between an on-premises Exchange organization and Microsoft 365
      or Office 365: For Cutover migration into M365, you need to enable the MRS Proxy
      endpoint on Mailbox servers in your on-premises Exchange organization. For more
      information on Cutover migration, see Migrate email to Exchange Online using the
      Exchange cutover method.

Note: If you use the Exchange admin center (EAC) to move mailboxes, cross-forest moves and
onboarding remote move migrations are pull move types, because you initiate the request
from the target environment. Offboarding remote move migrations are push move types
because you initiate the request from the source environment.

<!-- p.145 -->

What do you need to know before you begin?
   Estimated time to complete: 2 minutes per server.

   You need to be assigned permissions before you can perform this procedure or
   procedures. To see what permissions you need, see the "Exchange Web Services
   permissions" section in the Clients and mobile devices permissions topic.

   If you've deployed multiple Mailbox servers in your Exchange organization, you should
   enable the MRS Proxy endpoint on each Mailbox server. If you add additional Mailbox
   servers, be sure to enable the MRS Proxy endpoint on the new servers. Cross-forest
   moves and remote move migrations can fail if the MRS Proxy endpoint isn't enabled on
   all Mailbox servers.

   If you don't perform cross-forest moves or remote move migrations, keep MRS Proxy
   endpoints disabled on Mailbox servers to reduce the attack surface of your organization.

   Exchange Online requires Windows authentication for the MRS proxy endpoint in the
   Exchange Web Services (EWS) virtual directories.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

Use the EAC to enable the MRS Proxy endpoint
 1. In the EAC, go to Servers > Virtual Directories.

 2. Select the EWS virtual directory that you want to configure.

         You can use the Select server drop-down list to filter the Exchange servers by name.

         To only display EWS virtual directories, select EWS in the Select type drop-down list.

   After you've selected the EWS virtual directory that you want to configure, click Edit   .

<!-- p.146 -->

   3. On the properties page that opens, on the General tab, select the Enable MRS Proxy
     endpoint check box, and then click Save.

Use the Exchange Management Shell to enable the
MRS Proxy endpoint
To enable the MRS Proxy endpoint, use this syntax:

  PowerShell

  Set-WebServicesVirtualDirectory -Identity "[<Server>\]EWS (Default Web Site)" -
  MRSProxyEnabled $true

This example enables the MRS Proxy endpoint of the EWS virtual directories on the Mailbox
server named EXCH-SRV-01.

  PowerShell

<!-- p.147 -->

  Set-WebServicesVirtualDirectory -Identity "EXCH-SRV-01\EWS (Default Web Site)" -
  MRSProxyEnabled $true

This example enables the MRS Proxy endpoint of the EWS virtual directories on all Mailbox
servers in your Exchange organization.

  PowerShell

  Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled
  $true

For detailed syntax and parameter information, see Set-WebServicesVirtualDirectory.

How do you know this worked?
To verify that you've successfully enabled the MRS Proxy endpoint, do any of these steps:

     In the EAC, go to Servers > Virtual Directories > select the EWS virtual directory, and
     verify in the details pane that the MRS Proxy endpoint is enabled.

     Run this command in the Exchange Management Shell, and verify that the
     MRSProxyEnabled property for the EWS virtual directory has the value True :

        PowerShell

        Get-WebServicesVirtualDirectory | Format-Table -Auto Identity,MRSProxyEnabled

     Use the Test-MigrationServerAvailability cmdlet in the Exchange Management Shell to
     test communication with the remote servers that hosts the mailboxes that you want to
     move (or the servers in your on-premises Exchange organization for offboarding remote
     move migrations from Microsoft 365 or Office 365).

<!-- p.148 -->

Replace <EmailAddress> with the email address of one of the mailboxes that you want to
move, and run this command in the Exchange Management Shell:

  PowerShell

  Test-MigrationServerAvailability -ExchangeRemoteMove -Autodiscover -
  EmailAddress <EmailAddress> -Credentials (Get-Credential)

To run this command successfully, the MRS Proxy endpoint must be enabled.

For detailed syntax and parameter information, see Test-MigrationServerAvailability.

<!-- p.149 -->

Re-create missing arbitration mailboxes
Article • 04/30/2025

APPLIES TO:        2016      2019       Subscription Edition

Exchange 2016 CU8 or later contains seven special system mailboxes known as arbitration
mailboxes. Arbitration mailboxes are used for storing different types of system data and for
managing messaging approval workflow. The following table lists each type of arbitration
mailbox and their responsibilities.

                                                                                  ﾉ    Expand table

 Arbitration mailbox Name           Display      Persisted          Function
                                    name         capabilities

 FederatedEmail.4c1f4d8b-8179-      Microsoft    none               This mailbox stores data used
 4148-93bf-00a95fa1e042             Exchange                        to maintain federation between
                                    Federation                      different Exchange
                                    Mailbox                         organizations. This includes
                                                                    Rights Management Services,
                                                                    cross-premises mail-flow
                                                                    monitoring probes and
                                                                    responses, notifications, online
                                                                    archives, messaging records
                                                                    management, and cross-
                                                                    premises free/busy information.

 Migration.8f3e7716-2011-43e4-      Microsoft    Management         Stores data for the Exchange
 96b1-aba62d229136                  Exchange                        migration service to use when
                                    Migration                       moving mailboxes in batches.

 SystemMailbox{1f05a927-XXXX-       Microsoft    none               This mailbox is provisioned for
 XXXX-XXXX-XXXXXXXXXXXX}            Exchange                        use by the Exchange approval
 (for example,                      Approval                        framework for recipient
 SystemMailbox{1f05a927-9350-       Assistant                       moderation and auto group
 4efe-a823-5529c2d64109}; most                                      approval requests.
 of the mailbox name is unique to
 your organization)

 SystemMailbox{bb558c35-97f1-       Microsoft    ClientExtensions   This is known as an
 4cb9-8ff7-d53741dc928c}            Exchange     GMGen              organization mailbox. It is used
                                                                    for creating offline address
                                                 MailRouting        books (OABs). To load-balance
                                                                    OAB generation across your
                                                 MessageTracking
                                                                    organization, including across
                                                 OABGen             geographically separate sites,
                                                                    you can create additional
                                                 PstProvider        organization mailboxes.

<!-- p.150 -->

 Arbitration mailbox Name          Display     Persisted           Function
                                   name        capabilities

                                               UMGrammar

                                               UMGrammarReady
                                               (Exchange 2016
                                               only)

 SystemMailbox{e0dc1c29-89c3-      Microsoft   UMDataStorage       Discovery system mailbox.
 4034-b678-e6c29d823ed9}           Exchange                        Provisioned for use by the e-
                                                                   Discovery feature, which is used
                                                                   by compliance officers to locate
                                                                   messages that match specified
                                                                   selection criteria. This mailbox is
                                                                   also used by Unified Messaging
                                                                   in Exchange 2016 for storing
                                                                   UM console attending files and
                                                                   other information.

 SystemMailbox{D0E409A0-AF9B-      Microsoft   none                Used for temporarily storing
 4720-92FE-AAC869B0D201}           Exchange                        encrypted mails so that external
 (Exchange 2016 CU8 and later)                                     users may read it in OWA.

 SystemMailbox{2CE34405-31BE-      Microsoft   none                This mailbox contain relevancy
 455D-89D7-A7C7DA7A0DAA}           Exchange                        features of each shard in an
 (Exchange 2016 CU8 and later)                                     organization.

If you need to re-create one of more of these arbitration mailboxes, use the instructions in this
article.

What do you need to know before you begin?
      Estimated time to complete: 10 minutes per procedure.

      You need to be assigned permissions before you can perform these procedures. To see
      what permissions you need, see the "Recipient Provisioning Permissions" section in the
      Recipients Permissions topic.

      To run Setup.exe /PrepareAD , your account needs to be a member of the Enterprise
      Admins security group.

      The computer that you use to run Setup.exe /PrepareAD requires access to Setup.exe in
      the Exchange installation files:

           1. Use your most recently downloaded copy of the Exchange ISO image file, or
             download an updated copy from Updates for Exchange Server.

<!-- p.151 -->

        2. In File Explorer, right-click on the Exchange ISO image file and then select Mount.
              Note the virtual DVD drive letter that's assigned.
        3. Open a Windows Command Prompt window. For example:
                Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then
                press OK.
                Press Start. In the Search box, type Command Prompt, then in the list of results,
                select Command Prompt.

     For more information about opening the Exchange Management Shell, see Open the
     Exchange Management Shell.

     For more information about running Exchange Setup in unattended mode, see Use
     unattended mode in Exchange Setup.

  ７ Note

        The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
        the September 2021 Cumulative Updates (CUs). You now must use either
        /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
        /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
        installs.

        The examples below use the /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
        switch. It's up to you to change the switch to
        /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

Re-create an arbitration mailbox
Use the following instructions to re-create a particular type of arbitration mailbox.

Re-create the Microsoft Exchange Federation Mailbox
To re-create the arbitration mailbox FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042,
run the following commands:

   1. If the mailbox is missing, run the following command from a Windows Command Prompt
     window:

        dos

<!-- p.152 -->

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

       dos

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

  2. In the Exchange Management Shell, run the following command:

       PowerShell

       Enable-Mailbox -Identity "FederatedEmail.4c1f4d8b-8179-4148-93bf-
       00a95fa1e042" -Arbitration

Re-create the Microsoft Exchange Migration mailbox
To re-create the arbitration mailbox Migration.8f3e7716-2011-43e4-96b1-aba62d229136, run
the following commands:

  1. If the mailbox is missing, run the following command from a Windows Command Prompt
     window:

       dos

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

       dos

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

  2. In the Exchange Management shell, run the following command:

       PowerShell

       Enable-Mailbox -Identity "Migration.8f3e7716-2011-43e4-96b1-aba62d229136" -
       Arbitration

<!-- p.153 -->

  3. In the Exchange Management Shell, set the Persisted Capabilities
     (msExchCapabilityIdentifiers) for the mailbox by running the following command:

       PowerShell

       Set-Mailbox -Identity "Migration.8f3e7716-2011-43e4-96b1-aba62d229136" -
       Arbitration -Management $true -Force

Re-create the Microsoft Exchange Approval Assistant mailbox
To re-create the arbitration mailbox SystemMailbox{1f05a927-XXXX-XXXX-XXXX-
XXXXXXXXXXXX}, run the following commands:

  1. If the mailbox is missing, run the following command from a Windows Command Prompt
     window:

       dos

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

       dos

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

  2. In the Exchange Management Shell, run the following command:

       PowerShell

       Get-User -ResultSize Unlimited | where {$_.Name -like
       "SystemMailbox{1f05a927*"} | Enable-Mailbox -Arbitration

Re-create the Microsoft Exchange organization mailbox for
OABs
To re-create the arbitration mailbox SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c},
run the following commands:

  1. If the mailbox is missing, run the following command from a Windows Command Prompt
     window:

<!-- p.154 -->

       dos

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

       dos

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

  2. In the Exchange Management Shell, run the following command:

       PowerShell

       Enable-Mailbox -Identity "SystemMailbox{bb558c35-97f1-4cb9-8ff7-
       d53741dc928c}" -Arbitration

  3. In the Exchange Management Shell, set the Persisted Capabilities
     (msExchCapabilityIdentifiers) for the mailbox by running the following command:

       PowerShell

       Get-Mailbox "SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}" -
       Arbitration | Set-Mailbox -Arbitration -UMGrammar $true -OABGen $true -GMGen
       $true -ClientExtensions $true -MessageTracking $true -PstProvider $true -
       MaxSendSize 1GB -Force

  4. In the Exchange Management Shell, add the required capabilities to the mailbox by
     running the following commands:

       PowerShell

       $OABMBX = Get-Mailbox "SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}" -
       Arbitration; Set-ADUser $OABMBX.SamAccountName -Add
       @{"msExchCapabilityIdentifiers"="40","42","43","44","47","51","52","46"}

Re-create the Microsoft Exchange Discovery system mailbox
To re-create the arbitration mailbox SystemMailbox{e0dc1c29-89c3-4034-b678-
e6c29d823ed9}, run the following commands:

  1. If the mailbox is missing, run the following command from a Windows Command Prompt
     window:

<!-- p.155 -->

       dos

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

       dos

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

  2. In the Exchange Management shell, run the following command:

       PowerShell

       Enable-Mailbox -Identity "SystemMailbox{e0dc1c29-89c3-4034-b678-
       e6c29d823ed9}" -Arbitration

  3. In the Exchange Management Shell, set the Persisted Capabilities
     (msExchCapabilityIdentifiers) for the mailbox by running the following command:

       PowerShell

       Set-Mailbox -Identity "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}" -
       Arbitration -UMDataStorage $true -Force

Re-create the Microsoft Exchange 2016 CU8 and later system
mailboxes
To re-create the arbitration mailbox SystemMailbox{D0E409A0-AF9B-4720-92FE-
AAC869B0D201} and SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}, run the
following commands:

  1. If the mailboxes are missing, run the following command from a Windows Command
     Prompt window:

       dos

       <Virtual DVD drive letter>:\Setup.exe
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

     For example:

<!-- p.156 -->

        dos

        E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

   2. In the Exchange Management shell, run the following command:

        PowerShell

        Enable-Mailbox -Identity "SystemMailbox{D0E409A0-AF9B-4720-92FE-
        AAC869B0D201}" -Arbitration
        Enable-Mailbox -Identity "SystemMailbox{2CE34405-31BE-455D-89D7-
        A7C7DA7A0DAA}" -Arbitration

   3. In the Exchange Management Shell, configure some mailbox properties and set the
     Persisted Capabilities (msExchCapabilityIdentifiers) for the mailbox by running the
     following command:

        PowerShell

        Set-Mailbox -Identity 'SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}' -
        Arbitration -DisplayName 'Microsoft Exchange' -
        RequireSenderAuthenticationEnabled $false -UseDatabaseQuotaDefaults $false -
        SCLDeleteEnabled $false -SCLJunkEnabled $false -SCLQuarantineEnabled $false -
        SCLRejectEnabled $false -HiddenFromAddressListsEnabled $true -Force

        $ShardMBX = Get-Mailbox -Identity 'SystemMailbox{2CE34405-31BE-455D-89D7-
        A7C7DA7A0DAA}' -Arbitration
        Set-ADUser $ShardMBX.SamAccountName -Add @{ msExchCapabilityIdentifiers = 66
        }

How do you know this worked?
To verify that you've successfully re-created the arbitration mailbox, set the search scope to
search the entire Active Directory forest, and then use the Get-Mailbox cmdlet with the
Arbitration switch to retrieve system mailboxes.

  PowerShell

  Set-ADServerSettings -ViewEntireForest $true; Get-Mailbox -Arbitration | Format-
  Table Name,DisplayName

View the results of the command to verify that appropriate system mailbox, either by Name or
Display Name from the above table, has been re-created.

<!-- p.157 -->

 Tip

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
Server .

<!-- p.158 -->

Managed Store in Exchange Server
Article • 04/30/2025

APPLIES TO:           2016   2019     Subscription Edition

The Managed Store is the name for the Information Store (also known as the Store) processes
in Exchange Server 2016 and Exchange Server 2019. Introduced in Exchange Server 2013, the
Managed Store uses a controller/worker process model that provides storage process isolation
and faster database failover. The Managed Store also uses a static database caching
mechanism that replaces the dynamic buffer algorithm in previous versions of Exchange.

The multi-process model that's used by the Managed Store consists of the following processes
on the Mailbox server:

      A single store service controller process for the whole Exchange server
      (Microsoft.Exchange.Store.Service.exe, also known as MSExchangeIS).

      One worker process for each mounted database (Microsoft.Exchange.Store.Worker.exe).
      When a database is mounted, a new worker process is instantiated that services only that
      database. When a database is dismounted, the worker process for that database is
      terminated.

For example, if you have 40 mailbox databases mounted on a Mailbox server, there will be 41
processes running for the Managed Store: one for each database, and one for the store service
process controller. The store process controller monitors the health of all store worker
processes on the server. A forcible or unexpected termination the
Microsoft.Exchange.Store.Service.exe causes an immediate failover of all active database copies
on the server.

The Managed Store is also tightly integrated with the Microsoft Exchange Replication service
(MSExchangeRepl.exe) and Active Manager. The controller process, worker processes, and
Replication service work together to provide greater availability and reliability as described in
the following list:

      Microsoft Exchange Replication service process (MSExchangeRepl.exe):

         Responsible for issuing mount and dismount operations to the Store.

         Initiates recovery action on storage or database failures reported by the Store, the
         Extensible Storage Engine (ESE), and Managed Availability responders.

         Detects unexpected database failures.

         Provides the administrative interface for management tasks.

<!-- p.159 -->

     Store service process/controller (Microsoft.Exchange.Store.Service.exe):

        Manages each worker process lifetime based on the mount and dismount operations
        received from the Replication service.

        Handles incoming requests from the Windows Service Control Manager.

        Logs failure items when store worker process problems detected (for example, hang or
        unexpected exit).

        Terminates store worker processes in response failover event.

     Store worker process (Microsoft.Exchange.Store.Worker.exe)

        Responsible for executing RPC operations for mailboxes on a database.

        RPC endpoint instance within worker process is the database GUID.

        Provides database cache for a database.

Static database caching algorithm
The Managed Store uses a simple and straightforward algorithm for determining database
cache as compared to dynamic buffer allocation that was used in the previous versions of
Exchange. The memory that's allocated for each database cache (that is, each store worker
process) is based on number of local database copies and configured value of the
MaximumActiveDatabases parameter on the Set-MailboxServer cmdlet (the default value is
$null or blank). If the value of MaximumActiveDatabases is greater than number of current
database copies, then the cache calculation is based on the number of database copies.

The static algorithm allocates memory for the ESE cache of each store worker process based on
the amount of physical RAM that's installed in the server. This is referred to the Max Cache
Target of the database. 25% of total server memory is allocated to the ESE cache, and is
referred to as the Server Cache Size Target.

  ７ Note

  You can override the Server Cache Size Target, and therefore the amount of memory
  allocated to the Store for ESE cache by using msExchESEParamCacheSizeMax attribute of the
  InformationStore object in Active Directory (the value configured is the number of 32 KB
  pages to allocate across all store processes).

<!-- p.160 -->

A static amount of this cache is allocated to active and passive copies. The store worker
process is allocated the Max Cache Target only when servicing an active database copy. Passive
database copies are allocated 20 percent of the Max Cache Target. The remainder is reserved
by the Store, and allocated to the worker process if the database transitions from passive to
active.

Max Cache Target is calculated only at Store startup. Therefore, if you add or remove databases
or database copies, you must restart the Store controller service (MSExchangeIS) so that the
cache can be adjusted accordingly. If the service isn't restarted, new databases will have a
smaller cache size target than databases that existed before the last service startup. In this
scenario, the sum of database cache size targets will likely exceed the Server Cache Size Target
until MSExchangeIS is restarted.

Example database cache calculations
Here are example database caching calculations that are based on a Mailbox server's memory
and database configuration.

Example 1
Mailbox server configuration:

      48 GB of memory

      Two active databases and two passive databases

      MaximumActiveDatabases parameter: not configured

The amount of database cache is 3 GB for each active database copy worker process and 0.6
GB for each passive database copy worker process. Here's how these values are calculated:

      Server Cache Size Target: 25% of the amount of memory: 48 GB * 0.25 = 12 GB.

      Database Max Cache Target: Divide the Server Cache Size Target by the total number of
      active and passive databases: 12 GB / 4 databases = 3 GB.

      Memory used for passive database copies: 20% of the Database Max Cache Target: 3 GB
      * 0.20 = 0.6 GB.

Of the 12 GB of memory that's assigned to the Server Cache Size Target:

      7.2 GB will be in use by database worker processes.
