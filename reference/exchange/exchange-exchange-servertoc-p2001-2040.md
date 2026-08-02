---
title: "Exchange Server — pages 2001-2040"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2001-2040
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2001-2040
family: exchange
documentKind: "doc"
abstract: "On the Exchange 2010 server, run the following command to lock the public folders for finalization. PowerShell Set-OrganizationConfig -PublicFoldersLockedForMigration:$true For detailed syntax and parameter information, see Set-OrganizationConfig. If your organization has multip"
---

# Exchange Server — pages 2001-2040

<!-- p.2001 -->

On the Exchange 2010 server, run the following command to lock the public folders for
finalization.

  PowerShell

  Set-OrganizationConfig -PublicFoldersLockedForMigration:$true

For detailed syntax and parameter information, see Set-OrganizationConfig.

If your organization has multiple public folder databases, you'll need to wait until public folder
replication is complete to confirm that all public folder databases have picked up the
PublicFoldersLockedForMigration property value and any pending changes users recently made

to folders have converged across the organization. This may take several hours.

Step 7: Finalize the public folder migration
(downtime required)
First, run the following cmdlet to change the Exchange 2016 deployment type to Remote:

  PowerShell

  Set-OrganizationConfig -PublicFoldersEnabled Remote

Once that is done, you can complete the public folder migration by running the following
command:

  PowerShell

  Complete-MigrationBatch PFMigration

Or, in EAC, you can complete the migration by clicking Complete this migration batch.

When you complete the migration, Exchange will perform a final synchronization between the
Exchange 2010 server and Exchange 2016. If the final synchronization is successful, the public
folders on the Exchange 2016 server will be unlocked and the status of the migration batch will
change to Completing, and then Completed. It is common for the migration batch to take a few
hours before its status changes from Synced to Completing, at which point the final
synchronization will begin.

  ７ Note

<!-- p.2002 -->

  If for any reason the migration batch file does not finalize (the
  PublicFolderMigrationComplete property value is False ) restart the Information Store (IS) on
  the Exchange 2010 server.

Step 8: Test and unlock the public folder migration
After you finalize the public folder migration, you should run the following test to make sure that
the migration was successful. This allows you to test the migrated public folder hierarchy before
you switch to using Exchange 2016 public folders.

   1. In PowerShell, run the following command to assign some test mailboxes to use any newly
     migrated public folder mailbox as the default public folder mailbox.

       PowerShell

       Set-Mailbox -Identity <Test User> -DefaultPublicFolderMailbox <Public Folder
       Mailbox Identity>

   2. Log on to Outlook 2007 or later with the test user identified in the previous step, and then
     perform the following public folder tests:

           View the hierarchy.

           Check permissions.

           Create and delete public folders.

           Post content to and delete content from a public folder.

   3. If you run into any issues, see Roll back the migration later in this topic. If the public folder
     content and hierarchy is acceptable and functions as expected, run the following command
     to unlock the public folders for all other users.

       PowerShell

       Get-Mailbox -PublicFolder | Set-Mailbox -PublicFolder -
       IsExcludedFromServingHierarchy $false

        ） Important

<!-- p.2003 -->

        Don't use the IsExcludedFromServingHierarchy parameter after initial migration
        validation is complete as this parameter is used by the automated load-balancing
        service for Exchange.

   4. On the Exchange 2010 server, run the following command to indicate that the public folder
     migration is complete:

       PowerShell

       Set-OrganizationConfig -PublicFolderMigrationComplete:$true

   5. After you've verified that the migration is complete, on the Exchange 2016 server, run the
     following command:

       PowerShell

       Set-OrganizationConfig -PublicFoldersEnabled Local

   6. Finally, if you want external senders to send mail to the migrated mail-enabled public
     folders, the Anonymous user needs to be granted at least the Create Items permission. If
     you don't do this, external senders will receive a delivery failure notification and the
     messages won't be delivered to the migrated mail-enabled public folder.

     You can use the Exchange Management Shell or Outlook to set the permissions on the
     Anonymous user. To read more about how to set permissions on the Anonymous user, see
     Mail-enable or mail-disable a public folder.

How do I know this worked?
In Step 2: Prepare for the migration, you were instructed to take snapshots of the public folder
structure, statistics, and permissions before the migration began. The following steps will help
verify that your public folder migration was successful by taking the same snapshots after the
migration is complete. You can then compare the data in both files to verify success.

   1. Run the following command to take a snapshot of the new folder structure.

       PowerShell

       Get-PublicFolder -Recurse | Export-CliXML C:\PFMigration\Cloud_PFStructure.xml

<!-- p.2004 -->

   2. Run the following command to take a snapshot of the public folder statistics such as item
     count, size, and owner.

       PowerShell

       Get-PublicFolderStatistics -ResultSize Unlimited | Export-CliXML
       C:\PFMigration\Cloud_PFStatistics.xml

   3. Run the following command to take a snapshot of the permissions.

       PowerShell

       Get-PublicFolder -Recurse | Get-PublicFolderClientPermission | Select-Object
       Identity,User -ExpandProperty AccessRights | Export-CliXML
       C:\PFMigration\Cloud_PFPerms.xml

Remove public folder databases from the Exchange
2010 servers
After the migration is complete, and you have verified that your Exchange 2016 or Exchange 2019
public folders are working as expected, you should remove the public folder databases on the
Exchange 2010 servers.

For details about how to remove public folder databases from Exchange 2010 servers, see
Remove Public Folder Databases.

Roll back the migration
If you run into issues with the migration and need to reactivate your Exchange 2010 public
folders, perform the following steps.

  Ｕ Caution

  If you roll your migration back to the Exchange 2010 servers, you will lose any email that was
  sent to mail-enabled public folders or content that was posted to public folders in Exchange
  2016 or Exchange 2019 after the migration. To save this content, you need to export the
  public folder content to a .pst file and then import it to the Exchange 2010 public folders
  when the rollback is complete.

<!-- p.2005 -->

  1. On the Exchange 2010 server, run the following command to unlock the migrated public
     folders. This process may take several hours.

       PowerShell

       Set-OrganizationConfig -PublicFoldersLockedForMigration $false

  2. On the Exchange 2016 server, run the following commands to remove the public folder
     mailboxes.

       PowerShell

       Get-Mailbox -PublicFolder | Where {$_.IsRootPublicFolderMailbox -eq $false} |
       Remove-Mailbox -PublicFolder -Force -Permanent $true -Confirm:$false

       PowerShell

       Get-Mailbox -PublicFolder | Remove-Mailbox -PublicFolder -Force -Permanent $true
       -Confirm:$false

  3. On the Exchange 2010 server, run the following command to set the
     PublicFolderMigrationComplete property value to False .

       PowerShell

       Set-OrganizationConfig -PublicFolderMigrationComplete $false

  4. On the Exchange 2016 server, run the following command to remove the public folder
     mailboxes.

       PowerShell

       Set-OrganizationConfig -PublicFoldersEnabled Remote -RemotePublicFolderMailboxes
       <ProxyMailbox1>,<ProxyMailbox2>,...,<ProxyMailboxN>

     For more information about the remote Public Folder mailboxes you must use with this
     command, see Configure legacy public folders where user mailboxes are on Exchange 2013
     servers.

Last updated on 06/03/2026

<!-- p.2006 -->

Use batch migration to migrate Exchange
Server public folders to Exchange Online
APPLIES TO:      2016      2019      Subscription Edition

  ７ Note

  The native migration method supports maximum of 100 target public folder mailboxes in
  Exchange Online (although up to 1000 can be created post migration), with each public
  folder mailbox of up to maximum capacity of 100GB. 5 TB is the maximum recommended
  size that can be migrated to Exchange Online, as per our best practices to fill up each target
  public folder mailbox with up to 50% of capacity.

  ７ Note

  The article lists steps to migrate public folders from on-premises to Exchange Online. Note
  that there are no native tools to migrate/move public folders from Exchange Online to
  Exchange on-premises.

Migrating your Exchange Server public folders to Exchange Online requires Exchange Server 2013
CU15 or later, or Exchange Server 2016 CU4 or later, to be running in your on-premises
environment. All versions of Exchange Server 2019 are supported for batch migrations of public
folders. As a best practice, install latest Cumulative Update & Security Update before starting the
migration. Please check this article for information about latest updates for Exchange server.

For instructions on migrating Exchange Server 2010 public folders to Exchange Online, see Use
batch migration to migrate legacy public folders to Exchange Online.

What do you need to know before you begin?
     We strongly recommend you review FAQ: Public folders before you attempt a migration.

     When you upgrade to Exchange Server 2013 CU15 or later, or to Exchange Server 2016 CU4
     or later, you must also prepare Active Directory or your public folder migration will fail. This
     Active Directory preparation ensures that all relevant PowerShell cmdlets and parameters

<!-- p.2007 -->

are available to you for preparing for and running the migration. See Prepare Active
Directory and domains for more information.

In Exchange Online, you need to be a member of the Organization Management role group.
This role group is different from the permissions assigned to you when you subscribe to
Exchange Online. For details about how to enable the Organization Management role
group, see Manage role groups.

In Exchange Server, you need to be a member of the Organization Management or Server
Management RBAC role groups. For details, see Add Members to a Role Group.

Before you begin the public folder migration, if any single public folder in your organization
is larger than 25 GB, we recommend that you delete content from that folder to make it
smaller, or divide the public folder's content into multiple, smaller public folders. The 25 GB
limit cited here only applies to the public folder and not to any child or sub-folders the
folder in question may have. If neither option is feasible, we recommend that you do not
move your public folders to Exchange Online. See Exchange Online Limits for more
information.

  ７ Note

  If your current public folder quotas in Exchange Online are less than 25 GB, you can use
  the Set-OrganizationConfig cmdlet to increase them with the
  DefaultPublicFolderIssueWarningQuota and DefaultPublicFolderProhibitPostQuota
  parameters.

In Exchange Online, you can create a maximum of 1000 public folder mailboxes. However, a
maximum of 100 public folder mailboxes is supported for migration from Exchange Server.

If you intend to migrate users to Microsoft 365, you should complete your user migration
prior to migrating your public folders. For more information, see Ways to migrate multiple
email accounts to Microsoft 365.

MRS Proxy needs to be enabled on at least one Exchange server, a server that is also
hosting public folder mailboxes. See Enable the MRS Proxy endpoint for remote moves for
details.

To perform the migration procedures in this article, you can't use the Exchange admin
center (EAC). Instead, you need to use the Exchange Management Shell on your Exchange

<!-- p.2008 -->

   servers. In Exchange Online, you need to use Exchange Online PowerShell. For more
   information, see Connect to Exchange Online PowerShell.

   Skipping the migration of deleted items and deleted folders from Exchange Server to
   Exchange Online is supported. For more information, see the Exchange Team blog post
   about modern public folder migrations without dumpster data .

   You must use a single migration batch to migrate all of your public folder data. Exchange
   allows creating only one migration batch for public folders migration. If you attempt to
   create more than one public folder migration batch simultaneously, the result will be an
   error. Also note that once the migration batch has a status of "Completed," no more data
   can be copied over from the source environment.

   We recommend that you don't use Outlook's PST export feature to migrate public folders to
   Exchange Online. Public folder mailbox growth in Exchange Online is managed using an
   auto-split feature that splits the public folder mailbox when it exceeds size quotas. Auto-
   split can't handle the sudden growth of public folder mailboxes when you use PST export to
   migrate your public folders, and you may have to wait for up to two weeks for auto-split to
   move the data from the primary mailbox. We recommend that instead you use the cmdlet-
   based instructions in this article to migrate your public folders. If you still decide to migrate
   public folders using PST export, see Migrate Public Folders to Microsoft 365 by using
   Outlook PST export later in this article.

   Verify if the DefaultPublicFolderAgeLimit is configured on the organization level ( Get-
   OrganizationConfig | Format-List DefaultPublicFolderAgeLimit ) or if you have any

   AgeLimit ( Get-PublicFolder <FolderPath> | Format-List AgeLimit ) configured for the
   individual Public Folders, so that automatic deletions of the content to be prevented.

   Before you begin, read this article in its entirety. For some steps there is downtime required.
   During this downtime, public folders won't be accessible by anyone. Also review the list of
   known issues. Also, read best practices for public folder migration     to plan your migration.

  Tip

 Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server
 | Management.

Step 1: Download the migration scripts

<!-- p.2009 -->

 1. Download all scripts from Exchange Server Public Folders Migration Scripts      and Exchange
    Server Public Folders to Microsoft 365 Pre-Migration Scripts    .

 2. Save the scripts to the local computer on which you'll be running PowerShell. For example,
    C:\PFScripts. Make sure all scripts are saved in the same location.

    The scripts and files you're downloading are:

          SourceSideValidations.ps1 : Source Side Validation script scans the public folders at

          source and reports issues found along with actions required to fix the issues. You'll run
          this script on the Exchange server on-premises.

          Sync-ModernMailPublicFolders.ps1 This script synchronizes mail-enabled public folder

          objects between your Exchange on-premises environment and Microsoft 365. You'll
          run this script on an on-premises Exchange server.

          Export-ModernPublicFolderStatistics.ps1 This script creates the folder name-to-

          folder size and deleted item size mapping file. You'll run this script on an on-premises
          Exchange server.

          ModernPublicFolderToMailboxMapGenerator.ps1 This script creates the public folder-to-

          mailbox mapping file by using the output from the Export-
          ModernPublicFolderStatistics.ps1 script. You'll run this script on an on-premises
          Exchange server.

          SetMailPublicFolderExternalAddress.ps1 This script updates the

          ExternalEmailAddress of mail-enabled public folders in your on-premises environment

          to that of their Exchange Online counterparts, so that emails addressed to your mail-
          enabled public folders post-migration are properly routed to Exchange Online. You
          need to run this script on an on-premises Exchange server.

Step 2: Prepare for the migration

 ７ Note

 We strongly recommend running the Source Side Validation          script from an on-premises
 Exchange Mailbox server. The script will scan and report issues that are known to cause
 migration to be slow, along with guidance to fix these issues. The script will perform all the
 following prerequisites.

<!-- p.2010 -->

Perform all prerequisite steps in the following sections before you begin the public folder
migration.

General prerequisite steps
For your migration to be successful, you should:

     Make sure that there are no orphaned public folder mail objects in Active Directory. These
     are objects in Active Directory without a corresponding Exchange object.

     Confirm that the SMTP email addresses configured for public folders in Active Directory
     match the SMTP email addresses on the Exchange objects.

     Confirm that there are no duplicate public folder objects in Active Directory. This is
     necessary to avoid having two or more Active Directory objects that are pointing to the
     same mail-enabled public folder.

Prerequisite steps in the on-premises Exchange 2013, Exchange
2016, or Exchange 2019 server environment
In Exchange Management Shell (on-premises) perform the following steps:

   1. Once your migration is complete, it takes some time for DNS caches across the Internet to
     direct messages to your mail-enabled public folders in their new location in Exchange
     Online. You can ensure that your newly migrated mail-enabled public folders receive
     messages during this DNS transition period by creating an accepted domain with a well-
     known name. To do this, run the following command in your Exchange on-premises
     environment. In this example, target domain is your Exchange Online domain, for which a
     send connector has already been configured by the Hybrid Configuration Wizard.

       PowerShell

       New-AcceptedDomain -Name
       PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 -DomainName <target
       domain> -DomainType InternalRelay

     Example:

       PowerShell

       New-AcceptedDomain -Name
       PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 -DomainName

<!-- p.2011 -->

    "contoso.mail.onmicrosoft.com" -DomainType InternalRelay

  If the accepted domain already exists in your on-premises environment, rename it to
  PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 and leave the other

  attributes intact.

  To check if the accepted domain is already present in your on-premises environment, run
  the following:

    PowerShell

    Get-AcceptedDomain | Where {$_.DomainName -eq "<target domain>"}

  To rename the accepted domain to
  PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 , run the following:

    PowerShell

    Get-AcceptedDomain | Where {$_.DomainName -eq "<target domain>"} | Set-
    AcceptedDomain -Name PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99

    ７ Note

    If you're expecting your mail-enabled public folders in Exchange Online to receive
    external email from the internet, you need to disable Directory Based Edge Blocking
    (DBEB). For more information, see Use Directory-Based Edge Blocking to reject
    messages sent to invalid recipients in Exchange Online.

2. If the name of a public folder contains a backslash \ or a forward slash /, it may not get
  migrated to its designated mailbox during the migration process. Before you migrate,
  rename any such folders to remove these characters.

  a. To locate public folders that have a backslash in the name, run the following command:

    PowerShell

    Get-PublicFolder -Recurse -ResultSize Unlimited | Where {$_.Name -like "*\*" -or
    $_.Name -like "*/*"} | Format-List Name, Identity, EntryId

  b. If any public folders are returned, you can rename them by running the following
  command:

<!-- p.2012 -->

    PowerShell

    Set-PublicFolder -Identity "<public folder EntryId>" -Name "<new public folder
    name>"

3. (This step is required only if you're re-doing a previous migration attempt for some reason.
  If this is not the case, skip to the next step.) Run the following cmdlets to confirm there isn't
  a record of a previous, successful migration in your organization. If there is, you need to set
  that value to $false .

  Before changing the values, please confirm that the previous migration attempt can be
  discarded so that you don't accidentally perform a second migration.

  a. Run the following command to check for any previous migrations, and the status of those
  migrations:

    PowerShell

    Get-OrganizationConfig | Format-List
    PublicFolderMailboxesLockedForNewConnections,
    PublicFolderMailboxesMigrationComplete

  b. If any of the above is returned with a value set to $true , make them $false by running:

    PowerShell

    Set-OrganizationConfig -PublicFolderMailboxesLockedForNewConnections:$false -
    PublicFolderMailboxesMigrationComplete:$false

4. For the purpose of verifying the success of the migration upon its completion, we
  recommend that you run the following commands on all appropriate Exchange 2016 or
  Exchange 2019 servers. This will take snapshots of your current public folder deployment
  that you can later use to compare with your newly migrated public folders.

    ７ Note

    Depending on the size of your Exchange organization, it could take some time for
    these commands to run.

       Run the following command to take a snapshot of the original source folder structure.

         PowerShell

<!-- p.2013 -->

         Get-PublicFolder -Recurse -ResultSize Unlimited | Export-CliXML
         OnPrem_PFStructure.xml

       Run the following command to take a snapshot of public folder statistics such as item
       count, size, and owner.

         PowerShell

         Get-PublicFolderStatistics -ResultSize Unlimited | Export-CliXML
         OnPrem_PFStatistics.xml

       Run the following command to take a snapshot of public folder permissions.

         PowerShell

         Get-PublicFolder -Recurse -ResultSize Unlimited | Get-
         PublicFolderClientPermission | Select-Object Identity,User,AccessRights -
         ExpandProperty AccessRights | Export-CliXML OnPrem_PFPerms.xml

       Run the following command to take a snapshot of your mail-enabled public folders:

         PowerShell

         Get-MailPublicFolder -ResultSize Unlimited | Export-CliXML OnPrem_MEPF.xml

       Save the files generated from the preceding commands in a safe place in order to
       make a comparison at the end of the migration.

5. If you're using Microsoft Entra Connect (Microsoft Entra Connect) to synchronize your on-
  premises directories with Microsoft Entra ID, you need to do the following (if you aren't
  using Microsoft Entra Connect, you can skip this step):

  a. On an on-premises computer, open Microsoft Entra Connect, and then select Configure.

  b. On the Additional tasks screen, select Customize synchronization options, and then
     click Next.

   c. On the Connect to Microsoft Entra ID screen, enter the appropriate credentials, and then
     click Next. Once connected, keep clicking Next until you're on the Optional Features
     screen.

  d. Make sure that Exchange Mail Public Folders is not selected. If it isn't selected, you can
     continue to the next section, Prerequisite steps in Exchange Online. If it is selected, click to

<!-- p.2014 -->

        clear the check box, and then click Next. Unchecking this option removes mail enabled
        public folders synced to Entra. You may get a warning message, if there are more than
        500 MEPF objects being removed from Entra. Follow the steps in this article to allow
        deletion of MEPF objects in case of this warning.

          ７ Note

          If you don't see Exchange Mail Public Folders as an option on the Optional
          Features screen, you can exit Microsoft Entra Connect and proceed to the next
          section, Prerequisite steps in Exchange Online.

     e. After you have cleared the Exchange Mail Public Folders selection, keep clicking Next
        until you're on the Ready to configure screen, and then click Configure.

Prerequisite steps in Exchange Online
In Exchange Online PowerShell, do the following steps:

   1. Make sure there are no existing public folder migration requests. If there are, clear them or
     your own migration request will fail. This step is only required if you think there may be an
     existing migration request in the pipeline (one that has failed or that you wish to abort).

     The following example will discover any existing batch migration requests:

       PowerShell

       Get-MigrationBatch | ?{$_.MigrationType.ToString() -eq "PublicFolder"}

     The following example removes any existing public folder batch migration requests:

       PowerShell

       Remove-MigrationBatch <name of migration batch> -Confirm:$false

   2. Make sure there aren't any existing public folders or public folder mailboxes in Exchange
     Online. If you do discover public folders in Exchange Online after following the steps below,
     it's important to determine why they're there and who in your organization started a public
     folder hierarchy before you begin removing any public folders and public folder mailboxes.

     a. In Exchange Online PowerShell, run the following command to see if any public folders
     mailboxes exist:

<!-- p.2015 -->

    PowerShell

    Get-Mailbox -PublicFolder

  b. If the command doesn't return any public folder mailboxes, continue to Step 3: Generate
  the .csv files. If the command does return any public folders mailboxes, run the following
  command to see if any public folders exist:

    PowerShell

    Get-PublicFolder -Recurse

3. If you do have any public folders in Exchange Online, run the following PowerShell
  command to remove them (after confirming that they aren't needed). Make sure that you've
  saved any information within these public folders before deleting them, because all
  information will be permanently deleted when you remove the public folders.

    PowerShell

    Get-MailPublicFolder -ResultSize Unlimited | where {$_.EntryId -ne $null}|
    Disable-MailPublicFolder -Confirm:$false
    Get-PublicFolder -GetChildren \ -ResultSize Unlimited | Remove-PublicFolder -
    Recurse -Confirm:$false

4. After the public folders are removed, run the following commands to remove all public
  folder mailboxes:

    PowerShell

    $hierarchyMailboxGuid = $(Get-
    OrganizationConfig).RootPublicFolderMailbox.HierarchyMailboxGuid
    Get-Mailbox -PublicFolder | Where-Object {$_.ExchangeGuid -ne
    $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force
    Get-Mailbox -PublicFolder | Where-Object {$_.ExchangeGuid -eq
    $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force
    Get-Mailbox -PublicFolder -SoftDeletedMailbox | % {Remove-Mailbox -PublicFolder
    $_.PrimarySmtpAddress -PermanentlyDelete:$true -force -Confirm:$false}
    $soft=Get-Mailbox -PublicFolder -SoftDeletedMailbox; foreach ($mbx in $soft){if
    ($mbx.Name -like "*CNF:*" -or $mbx.identity -like "*CNF:*") {Remove-Mailbox -
    PublicFolder        $mbx.ExchangeGUID.GUID -
    RemoveCNFPublicFolderMailboxPermanently -Force -Confirm:$false}}

  Repeat the above command block for couple of times, at interval of 5-10 minutes to ensure
  the SoftDeletedMailboxes are cleared up and there are no CNF objects left behind.

<!-- p.2016 -->

           ７ Note

           The above command block may return error like "The operation couldn't be performed
           because object <MailboxName> couldn't be found on", which can be safely ignored
           because of AD replication latency.

   5. Run following command again to ensure there are no SoftDeleted or CNF mailboxes left
     behind.

           PowerShell

           Get-Mailbox -PublicFolder -SoftDeletedMailbox

     If you see list of soft deleted mailboxes, repeat the command block from step 4, else
     proceed to the next step

Step 3: Generate the .csv files
Use the previously downloaded scripts to generate the .csv files that will be used in the
migration.

   1. From the Exchange Management Shell (on-premises), run the Export-
     ModernPublicFolderStatistics.ps1 script to create the folder name-to-folder size mapping

     file. You must have local administrator permissions to run this script. The resulting file
     contains three columns: FolderName, FolderSize, and DeletedItemSize. The values for the
     FolderSize and DeletedItemSize columns are displayed in bytes. For example,
     \PublicFolder01,10240, 100 means the public folder in the root of your hierarchy named
     PublicFolder01 is 10240 bytes (10 KB) in size and there are 100 bytes of recoverable items in
     it.

           PowerShell

           .\Export-ModernPublicFolderStatistics.ps1 <Folder-to-size map path>

     Example:

           PowerShell

           .\Export-ModernPublicFolderStatistics.ps1 stats.csv

<!-- p.2017 -->

2. Run the ModernPublicFolderToMailboxMapGenerator.ps1 script to create a .csv file that maps
  source public folders to public folder mailboxes in your Exchange Online destination. This
  file is used to calculate the correct number of public folder mailboxes in Exchange Online.

  The file generated by ModernPublicFolderToMailboxMapGenerator.ps1 won't contain the
  name of every public folder in your organization. It contains references to the parent folders
  of larger folder trees, or the names of folders which themselves are significantly large. You
  can think of this file as an "exception" file used to make sure certain folder trees and larger
  folders get placed into specific public folder mailboxes. It's normal to not see every one of
  your public folders in this file. Child folders of any folder listed in this mapping file will also
  be migrated to the same public folder mailbox as their parent folder (unless explicitly
  mentioned on another line within the mapping file that directs them to a different public
  folder mailbox).

    PowerShell

    .\ModernPublicFolderToMailboxMapGenerator.ps1 <Maximum mailbox size in bytes>
    <Maximum mailbox recoverable item size in bytes><Folder-to-size map path><Folder-
    to-mailbox map path>

        Maximum mailbox size in bytes is the maximum amount of data you want to migrate

       into any single public folder mailbox in Exchange Online. The maximum size of this
       field is currently 100 GB, but we recommend you use a smaller size, such as 50% of
       maximum size, to allow for future growth.

        Maximum mailbox recoverable items size in bytes is the recoverable items quota on

       your Exchange Online mailboxes. The maximum size of public folder mailboxes In
       Exchange Online is currently 100 GB. We recommend setting RecoverableItemsQuota
       to 15 GB or less.

        Folder-to-size map path is the file path of the .csv file you created when you ran the

        Export-ModernPublicFolderStatistics.ps1 script.

        Folder-to-mailbox map path is the file path of the folder-to-mailbox .csv file that

       you're creating in this step. If you only specify a file name, the file is generated in the
       current PowerShell directory on the local computer.

  Example:

    PowerShell

<!-- p.2018 -->

       .\ModernPublicFolderToMailboxMapGenerator.ps1 -MailboxSize 50GB -
       MailboxRecoverableItemSize 1GB -ImportFile .\stats.csv -ExportFile map.csv

        ７ Note

        The map.csv generated by the script uses generic names for the target public folder
        mailboxes that will be created in EXO during the next step (for example, Mailbox1 and
        Mailbox2). We encourage you to change the public folder mailbox names in the
        map.csv to suit your organization's naming policies. Also, if your on-premises
        organization already has mailboxes that match the generic names, you should edit the
        map.csv and provide unique names for the target public folder mailboxes in Exchange
        Online. Use Notepad or a similar editor to edit the TargetMailbox names in the
        map.csv.

        ７ Note

        We don't support the migration of public folders to Exchange Online when there are
        more than 100 unique public folder mailboxes in Exchange Online. During migration,
        you can have up to 100 public folder mailboxes enabled.

Step 4: Create the public folder mailboxes in
Exchange Online
Next, in Exchange Online PowerShell, create the target public folder mailboxes that contain your
migrated public folders.

Run the following script to create the target public folder mailboxes. The script creates a target
mailbox for each mailbox in the .csv file that you generated previously in Step 3: Generate the .csv
files, when you ran the ModernPublicFoldertoMailboxMapGenerator.ps1 script.

 PowerShell

 $mappings = Import-Csv <Folder-to-mailbox map path>
 $primaryMailboxName = ($mappings | Where-Object FolderPath -eq "\" ).TargetMailbox;
 New-Mailbox -HoldForMigration:$true -PublicFolder -
 IsExcludedFromServingHierarchy:$false $primaryMailboxName
 ($mappings | Where-Object TargetMailbox -ne $primaryMailboxName).TargetMailbox |
 Sort-Object -unique | ForEach-Object { New-Mailbox -PublicFolder -
 IsExcludedFromServingHierarchy:$false $_ }

<!-- p.2019 -->

Folder-to-mailbox map path is the file path of the folder-to-mailbox.csv file that was generated

by the ModernPublicFoldertoMailboxMapGenerator.ps1 script in Step 3: Generate the .csv files.

Step 5: Start the migration request
A number of commands now need to be run both in your Exchange Server on-premises
environment and in Exchange Online.

   1. From any of your Exchange 2016 or Exchange 2019 servers hosting public folder mailboxes,
     execute the following script. This script synchronizes mail-enabled public folders from your
     local Active Directory to Exchange Online. Make sure that you have downloaded the latest
     version of this script and that you're running it from Exchange Management Shell.

       PowerShell

       .\Sync-ModernMailPublicFolders.ps1 -CsvSummaryFile:sync_summary.csv

           CsvSummaryFile is the file path to where you want your log file of synchronization

          operations and errors located. The log will be in .csv format.

       ７ Note

       Use Sync MEPF Script troubleshooting if you see any errors during the Sync-
       ModernMailPublicFolders.ps1 script.

   2. In Exchange Online PowerShell, pass the credential of a user who has administrator
     permissions in the Exchange 2013, Exchange 2016, or Exchange 2019 on-premises
     environment into the variable $Source_Credential . The migration request that you run in
     Exchange Online will use this credential to gain access to your on-premises Exchange
     servers to copy the public folder content over to Exchange Online.

       PowerShell

       $Source_Credential = Get-Credential <source_domain>\
       <PublicFolder_Administrator_Account>

   3. In Exchange Online PowerShell, pass the Internet routable fully qualified domain name of
     your Exchange Mailbox Replication Service (MRS) into the variable $Source_RemoteServer .
     The migration request that you run in Exchange Online will use this remote server to copy
     the public folder content to Exchange Online.

<!-- p.2020 -->

    PowerShell

    $Source_RemoteServer = "<MRS proxy endpoint server>"

4. On your on-premises Exchange server, open the Exchange Management Shell and find the
  GUID of the primary hierarchy mailbox with the following command:

    PowerShell

    (Get-OrganizationConfig).RootPublicFolderMailbox.HierarchyMailboxGuid.GUID

  Note the output of this command. You'll need it in the next step. For example:

    91edc6dd-478a-497c-8731-b0b793f5a986

    ７ Note

    The public folder mailbox GUID mentioned in the previous command must be obtained
    from the on-premises server; if it is obtained from Exchange Online, the migration
    batch will fail with transient error.

5. In Exchange Online PowerShell, run the following commands to create the public folder
  migration endpoint and the public folder migration request:

    PowerShell

    $bytes = [System.IO.File]::ReadAllBytes('folder_mapping.csv')
    $PfEndpoint = New-MigrationEndpoint -PublicFolder -Name PublicFolderEndpoint -
    RemoteServer $Source_RemoteServer -Credentials $Source_Credential
    New-MigrationBatch -Name PublicFolderMigration -CSVData $bytes -SourceEndpoint
    $PfEndpoint.Identity -SourcePfPrimaryMailboxGuid <guid you noted from previous
    step> -NotificationEmails <email addresses for migration notifications>

  Where folder_mapping.csv is the map file that was generated in Step 3: Generate the .csv
  files and HierarchyMailboxGUID is the output you noted in the previous step. Be sure to
  provide the full file path to folder_mapping.csv . If the map file was moved for any reason,
  be sure to use the new location.

  Separate multiple email addresses with commas.

    ７ Note

<!-- p.2021 -->

    You may notice the above command failing with the error "Cannot find a recipient that
    has mailbox GUID" with the GUID mentioned of public folder mailbox in EXO. This can
    happen because of AD replication latency. In such case, wait for an hour and retry the
    command again.

6. Finally, start the migration using the following command in Exchange Online PowerShell:

    PowerShell

    Start-MigrationBatch PublicFolderMigration

  While batch migrations need to be created using the New-MigrationBatch cmdlet in
  Exchange Online PowerShell, the progress and completion of the migration can be viewed
  and managed in the EAC or by running the Get-MigrationBatch cmdlet. The New-
  MigrationBatch cmdlet initiates a mailbox migration request for each public folder mailbox,

  and you can view the status of these requests using the mailbox migration page.

  To go to the mailbox migration page:

  a. Log on to Exchange Online and open the EAC.

  b. Navigate to Recipients, and then select Migration.

  c. Select the migration request that was just created and then, on the Details pane, select
     View Details.

  Before moving on to Step 6: Lock down the public folders on the Exchange on-premises
  server, verify that all data has been copied and that there are no errors in the migration.
  Once you have confirmed that the batch has moved to the state of Synced, run the
  commands mentioned in Step 2: Prepare for the migration, in the final step under
  Prerequisite steps in the Exchange Server on-premises environment, to take a snapshot of
  the public folders on-premises.

  Once these commands have run, you can proceed to the next step. Note that these
  commands could take a while to complete depending on the number of folders you have.
  The migration process synchronizes the data from the source (on-premises) environment
  once every 24 hours.

  You can use the following cmdlets to monitor your migration:

       Get-PublicFolderMailboxMigrationRequest

<!-- p.2022 -->

            Get-PublicFolderMailboxMigrationRequestStatistics

            Get-MigrationBatch

Step 6: Lock down the public folders on the Exchange
on-premises server (public folder downtime required)
Until this point in the migration process, users have been able to access your on-premises public
folders. The following steps will now log off users off from Exchange Server public folders and
then lock the folders as the migration process completes its final synchronization. Users won't be
able to access public folders during this time, and any messages sent to these mail-enabled
public folders will be queued and remain undelivered until the public folder migration is
complete.

  ７ Note

  The final sync might take a substantial amount of time, depending on the changes made to
  the source environment, the size of the public folder deployment, server capacity, and so on.
  If the folder hierarchy had many corrupt ACLs that were not cleaned up before the
  migration, there might be a significant delay in completion. It is recommended that you plan
  for a minimum of 48 hours of downtime for the final sync to complete.

Ensure the migration batch and individual migration requests have successfully synced.

Run the following command in EXO PowerShell for more information:

Get-MigrationBatch |?{$_.MigrationType -like "*PublicFolder*"} | ft *last*sync*

Get-PublicFolderMailboxMigrationRequest | Get-PublicFolderMailboxMigrationRequestStatistics

|ft targetmailbox,*last*sync*

The LastSyncedDate (on migration batch) and LastSuccessfulSyncTimestamp (on individual jobs)
should be within the last 7 days. If the date is too far in the past, such as more than a month ago,
you might want to review public folder migration requests and ensure that all the requests were
synced recently.

At this point, we recommend rerunning the following script to ensure that any new mail-enabled
public folders are synchronized with Exchange Online:

 PowerShell

<!-- p.2023 -->

  .\Sync-ModernMailPublicFolders.ps1 -CsvSummaryFile:sync_summary.csv

After you have confirmed that the batch and all migration requests have successfully synced, in
your on-premises environment, run the following command to lock the Exchange Server public
folders for finalization.

  PowerShell

  Set-OrganizationConfig -PublicFolderMailboxesLockedForNewConnections $true

  ７ Note

  If you aren't able to access the -PublicFolderMailboxesLockedForNewConnections parameter,
  it could be because your Active Directory was not prepared during the CU upgrade, as we
  advised above in What do you need to know before you begin? See Prepare Active Directory
  and domains for more information. Also note that any users who need access to public
  folders should be migrated first, before you migrate the public folders themselves.

If your organization has public folder mailboxes on multiple Exchange servers, you'll need to wait
until Active Directory replication is complete. Once complete, you can confirm that all public
folder mailboxes have picked up the PublicFolderMailboxesLockedForNewConnections flag, and
that any pending changes users recently made to their public folders have converged across the
organization. All of this could take several hours.

Run the following command in your on-premises environment to ensure that public folders are
locked:

  PowerShell

  Get-PublicFolder \

The expected result if public folders are locked is:

Couldn't find the public folder mailbox. + CategoryInfo : NotSpecified: (:) [Get-

PublicFolder], ObjectNotFoundException

Step 7: Finalize the public folder migration (public
folder downtime required)

<!-- p.2024 -->

You need to check the following items before you can complete your public folder migration:

  1. Confirm that there are no other public folder mailbox moves or public folder moves going
     on in your on-premises Exchange environment. To do this, use the Get-MoveRequest and
     Get-PublicFolderMoveRequest cmdlets to list any existing public folder moves. If there are
     any moves in progress, or in the Completed state, remove them.

  2. If your environment has multiple active directory domains, ensure the steps in No active
     public folder mailboxes were found" error and migration batch fails at Complete-
     MigrationBatch command are followed before initiating completing.

  3. To complete the public folder migration, run the following command in Exchange Online
     PowerShell:

       PowerShell

       Complete-MigrationBatch PublicFolderMigration

       ） Important

       After a migration batch is completed, no additional data can be synchronized from the
       on-premises Exchange servers and Exchange Online.

     When you run Complete-MigrationBatch PublicFolderMigration , Exchange will perform a
     final synchronization between your Exchange on-premises organization and Exchange
     Online. During this period, the status of the migration batch will change from Synced to
     Completing, and then finally to Completed. If the final synchronization is successful, the
     public folders in Exchange Online will be unlocked. However, it is strongly recommended
     that you complete Step 8 and Step 9 of this article before you open up public folders to
     your users.

     It's common for the status of migration batch to remain on Synced for a few hours before it
     switches to Completing. For migrations involving a large number of target mailboxes, it's
     normal to see the status remain in the Synced state for more than 24 hours, provided none
     of the underlying public folder migration requests have failed or were quarantined.

Step 8: Test and unlock public folders in
Exchange Online

<!-- p.2025 -->

Once the public folder migration is complete, take the following steps to test the success of the
migration, and to officially verify its completion. These final tasks allow you to test the migrated
public folder hierarchy before you permanently switch your organization to Exchange Online
public folders.

   1. In Exchange Online PowerShell, configure some test user mailboxes to use one of your
     newly migrated public folder mailboxes as their default public folder mailbox:

       PowerShell

       Set-Mailbox -Identity <test user> -DefaultPublicFolderMailbox <public folder
       mailbox identity>

     Make sure that your test users have necessary permissions to create public folders.

   2. Log on to Outlook with the test user you designated in the previous step, and then perform
     the following public folder tests. Note that it may take 15 to 30 minutes for changes to take
     effect. Once Outlook is aware of the changes, it might prompt you to restart a couple of
     times.

     a. View the hierarchy.

     b. Check permissions.

     c. Create some public folders and then delete them.

     d. Post content to, and delete content from, a public folder.

     If you run into any issues and determine you aren't ready to switch your organization's
     public folders entirely to Exchange Online, see Roll back a public folder migration from
     Exchange Server to Exchange Online.

   3. Run the following command in Exchange Online PowerShell to unlock your public folders in
     Exchange Online. After you run the command, it may take approximately 15 to 30 minutes
     for the changes to take effect. Once Outlook is aware of the changes, it might prompt your
     users to restart Outlook a couple of times.

       PowerShell

       Set-OrganizationConfig -RemotePublicFolderMailboxes $Null -PublicFoldersEnabled
       Local

<!-- p.2026 -->

Step 9: Finalize the migration on-premises
To enable emails to mail-enabled public folders on-premises, perform the following steps:

   1. Run the following command in your on-premises environment, to take a backup of the
     emails in the queue that were sent to your mail-enabled public folders. This backup can be
     used in scenarios where email delivery to mail-enabled public folders failed for any reason:

       PowerShell

       $Server=Get-TransportService;ForEach ($t in $server) {Get-Message -Server $t -
       ResultSize Unlimited| ?{$_.Recipients -like "*PF.InTransit*"} | ForEach-Object
       {Suspend-Message $_.Identity -Confirm:$False;
       $Temp="C:\ExportFolder\"+$_.InternetMessageID+".eml"; $Temp=$Temp.Replace("
       <","_"); $Temp=$Temp.Replace(">","_"); Export-Message $_.Identity |
       AssembleMessage -Path $Temp;Resume-message $_.Identity -Confirm:$false}}

   2. In your on-premises environment, run the following script to make sure all emails to mail-
     enabled public folders are correctly routed to Exchange Online. The script will stamp mail-
     enabled public folders with an ExternalEmailAddress that points them to their Exchange
     Online counterparts:

       PowerShell

       .\SetMailPublicFolderExternalAddress.ps1 -ExecutionSummaryFile:mepf_summary.csv

   3. If your testing is successful, in your on-premises environment, run the following command
     to indicate that the public folder migration is complete:

       PowerShell

       Set-OrganizationConfig -PublicFolderMailboxesMigrationComplete:$true -
       PublicFoldersEnabled Remote

How do I know this worked?
In Step 2: Prepare for the migration, you took snapshots of your on-premises public folder
structure, statistics, and permissions. The following steps will help you verify your public folder
migration was successful by taking the same snapshots in Exchange Online post-migration.
Compare the data in both files to verify success.

<!-- p.2027 -->

 1. In Exchange Online PowerShell, run the following command to take a snapshot of the new
    folder structure:

     PowerShell

     Get-PublicFolder -Recurse -ResultSize Unlimited | Export-CliXML
     Cloud_PFStructure.xml

 2. In Exchange Online PowerShell, run the following command to take a snapshot of the public
    folder statistics, including item count, size, and owner:

     PowerShell

     Get-PublicFolder -Recurse -ResultSize Unlimited | Get-PublicFolderStatistics |
     Export-CliXML Cloud_PFStatistics.xml

 3. In Exchange Online PowerShell, run the following command to take a snapshot of the
    permissions:

     PowerShell

     Get-PublicFolder -Recurse -ResultSize Unlimited | Get-
     PublicFolderClientPermission | Select-Object Identity,User,AccessRights | Export-
     CliXML Cloud_PFPerms.xml

 4. Exchange Online PowerShell, run the following command to take a snapshot of the mail-
    enabled public folders:

     PowerShell

     Get-MailPublicFolder -ResultSize Unlimited | Export-CliXML Cloud_MEPF.xml

 ７ Note

 Post-migration, if external emails fail mail-enabled public folders in Exchange Online with a
 5.7.13 or 5.4.1 error, ensure that the public folder has CreateItems permission enabled for
 anonymous users and Domain Based Edge Blocking (DBEB) is disabled for the email
 domain configured on the public folder.

Known issues

<!-- p.2028 -->

The following are common public folder migration issues that you may encounter in your
organization.

     We don't support the migration of public folders to Exchange Online when there are more
     than 100 unique public folder mailboxes in Exchange Online.

     Permissions for the root public folder and the EFORMS REGISTRY folder won't be migrated
     to Exchange Online, and you'll have to manually apply them in Exchange Online. To do this,
     run the following command in your Exchange Online PowerShell. Run the command once
     for each permission entry that is present on-premises but missing in Exchange Online:

       PowerShell

       Add-PublicFolderClientPermission "\" -User <user> -AccessRights <access rights>
       Add-PublicFolderClientPermission "\NON_IPM_SUBTREE\EFORMS REGISTRY" -User <user>
       -AccessRights <access rights>

     There is a known issue where some public folder migrations will fail if some public folder
     mailboxes are not serving the public folder hierarchy. This means the
     IsExcludedFromServingHierarchy parameter on one or more mailboxes is set to $true . To

     avoid this, set all mailboxes in Exchange Online to serve the hierarchy.

     Send As and Send on Behalf permissions don't get migrated to Exchange Online. If this
     happens with your migration, use the following commands in your on-premises
     environment to note who has these permissions.

     To see which public folders have Send As permissions on-premises:

       PowerShell

       Get-MailPublicFolder | Get-ADPermission | ?{$_.ExtendedRights -like "*Send-As*"}

     To see which public folders have Send on Behalf permissions on-premises:

       PowerShell

       Get-MailPublicFolder | ?{$_.GrantSendOnBehalfTo -ne "$null"} | Format-Table
       name,GrantSendOnBehalfTo

     To add Send As permission to a mail-enabled public folder in Exchange Online, in Exchange
     Online PowerShell type:

<!-- p.2029 -->

 PowerShell

 Add-RecipientPermission -Identity <mail-enabled public folder primary SMTP
 address> -Trustee <name of user to be assigned permission> -AccessRights SendAs

Example:

 PowerShell

 Add-RecipientPermission -Identity send1 -Trustee Exo1 -AccessRights SendAs

To add Send on Behalf permission to a mail-enabled public folder in Exchange Online, in
Exchange Online PowerShell type:

 PowerShell

 Set-MailPublicFolder -Identity <name of public folder> -GrantSendOnBehalfTo <user
 or comma-separated list of users>

Example:

 PowerShell

 Set-MailPublicFolder send2 -GrantSendOnBehalfTo exo1,exo2

Having more than 10,000 folders under the "\NON_IPM_SUBTREE\DUMPSTER_ROOT" folder
can cause the migration to fail. Therefore, check the
"\NON_IPM_SUBTREE\DUMPSTER_ROOT" folder to see if there are more than 10,000 folders
directly under it (immediate children). You can use the following command to find the
number of public folders in this location:

 PowerShell

 (Get-PublicFolder -GetChildren "\NON_IPM_SUBTREE\DUMPSTER_ROOT").Count

Exchange Online doesn't support more than 10,000 subfolders, which is why migrations of
more than 10,000 folders will fail. We are currently developing a script to unblock such
configurations. In the meantime, we suggest waiting to migrate your public folders.

Migration jobs aren't making progress or are stalled. This can happen if there are too many
jobs running in parallel, causing jobs to fail with intermittent errors. You can reduce the
number of concurrent jobs by modifying MaxConcurrentMigrations and

<!-- p.2030 -->

     MaxConcurrentIncrementalSyncs to a smaller number. Use the following example to set these

     values:

       PowerShell

       Set-MigrationEndpoint <PublicFolderEndpoint> -MaxConcurrentMigrations 30 -
       MaxConcurrentIncrementalSyncs 20 -SkipVerification

     Migration jobs fail with the error "Error: Dumpster of the Dumpster folder." If you see this
     error, it should be resolved if you stop the batch and then restart it.

     Migration jobs fail with the error "Request was quarantined because of the following error:
     The given key wasn't present in the dictionary." This happens when a corrupt item is present
     in a folder which migration jobs can't copy. To work around this:

        1. Stop the migration batch.

        2. Identify the folder containing the bad item. The migration report should include
           references to the folder that was being copied when the error occurred.

        3. In your on-premises environment, move the affected folder to the primary public
           folder mailbox. You can use the New-PublicFolderMoveRequest cmdlet to move folders.

        4. Wait for the folder move to complete. After it is complete, remove the move request.
           Finally, re-start the migration batch.

Remove public folder mailboxes from your Exchange
on-premises environment
After the migration is complete and you have verified that your public folders in Exchange Online
are working as expected and contain all expected data, you can remove your on-premises public
folder mailboxes.

Be aware that this step is irreversible, because once public folder mailboxes are deleted, they
can't be recovered. Therefore we strongly recommend that, in addition to validating the success
of your migration, that you also monitor your Exchange Online public folders for a few weeks
before removing the on-premises public folder mailboxes.

Migrate Public Folders to Exchange Online by using
Outlook PST export

<!-- p.2031 -->

We recommend that you don't use Outlook's PST export feature to migrate public folders to
Exchange Online if your on-premises public folder hierarchy is greater than 30 GB. Exchange
Online public folder mailbox growth is managed using an auto-split feature that splits the public
folder mailbox when it exceeds size quotas. Auto-split can't handle the sudden growth of public
folder mailboxes when you use PST export to migrate your public folders and you may have to
wait for up to two weeks for auto-split to move the data from the primary mailbox. In addition,
consider the following before using Outlook PST to export public folders to Exchange Online:

     Public folder permissions will be lost during this process. Capture the current permissions
     before migration and manually add them back once the migration is completed.

     If you use complex permissions or have many folders to migrate, we recommend that you
     use the cmdlet method for migration.

     Any item and folder changes made to the source public folders during the PST export
     migration will be lost. Therefore, we recommend that you use the cmdlet method if this
     export and import process will take a long time to complete.

If you still want to migrate your public folders by using PST files, follow these steps to ensure a
successful migration.

   1. Use the instructions in Step 1: Download the migration scripts to download the migration
     scripts. You only need to download the PublicFolderToMailboxMapGenerator.ps1 file.

   2. Follow step number 2 of Step 3: Generate the .csv files to create the public folder-to-
     mailbox mapping file. This file is used to calculate the correct number of public folder
     mailboxes in Exchange Online.

   3. Create the public folder mailboxes that you'll need based on the mapping file. For more
     information, see Use the EAC to create a public folder mailbox.

   4. Use the New-PublicFolder cmdlet to create the top-most public folder in each of the public
     folder mailboxes by using the Mailbox parameter.

   5. Export and import the PST files using Outlook.

   6. Set the permissions on the public folders using the EAC. For more information, follow Step
     3: Assign permissions to the public folder in the Set up public folders in a new organization
     article.

  Ｕ Caution

<!-- p.2032 -->

  If you've already started a PST migration and have run into an issue where the primary
  mailbox is full, you have two options for recovering the PST migration:

  The first option is to wait for the auto-split to move the data from the primary mailbox. This
  may take up to two weeks. However, all the public folders in a completely filled public folder
  mailbox won't be able to receive new content until the auto-split completes.

  Option two is to create a public folder mailbox in Exchange Server and then use the New-
  PublicFolder cmdlet with the Mailbox parameter to create the remaining public folders in
  the secondary public folder mailbox.

Troubleshoot public folder migrations
Select the following button for common issues during public folder migration:

 Run Tests: Troubleshoot public folder migration

A flyout page opens in the Microsoft 365 admin center, log in with your tenant admin account,
and select appropriate option.

Last updated on 06/03/2026

<!-- p.2033 -->

Remove public folder deployment from
Exchange Server 2013 or later
Article • 04/30/2025

APPLIES TO:          2016   2019     Subscription Edition

After you've migrated all the on-premises users and public folders to Exchange Online, you
need to remove the on-premises public folders deployment. Performing a clean removal of the
on-premises public folder deployment is critical as an improper removal can lead to issues like
orphaned Mail Enabled Public Folders (MEPFs) and blocked SMTP addresses in Microsoft
Entra ID or Exchange Online.

This article lists the steps to safely remove public folders and related data from an on-premises
deployment of Exchange Server 2013 or later versions.

Prerequisites
Before you begin, make sure that:

      You've migrated the on-premises public folders to Exchange Online.

      There are no users on-premises or in Exchange Online that are connecting to or using
      public folders deployed on-premises.

      On-premises public folder mailboxes are backed up before removal.

      All the following steps must be performed from Exchange Management Shell with the
      admin account that has necessary roles assigned.

Disable public folder access on users
   1. Run the following command to disable system public folder mailbox assignment on the
      users:

        PowerShell

        Set-OrganizationConfig -PublicFoldersEnabled None

   2. Then, run the following command to remove any admin-assigned public folder mailbox
      on the users:

        PowerShell

<!-- p.2034 -->

         Set-ADServerSettings -ViewEntireForest:$true
         Get-Mailbox -ResultSize unlimited | where {$_.DefaultPublicFolderMailbox -ne
         $Null} | Set-Mailbox -DefaultPublicFolderMailbox $Null

  3. Allow up to an hour for AD replication and the changes to take effect. Then, run the
       following command to ensure there's no public folder mailbox assignment present on the
       users:

         PowerShell

         Set-ADServerSettings -ViewEntireForest:$true
         Get-Mailbox -ResultSize unlimited |?{$_.DefaultPublicFolderMailbox -ne $Null
         -OR $_.EffectivePublicFolderMailbox -ne $Null}

Clean-up mail enabled public folders
Use the Exchange Management Shell to run the PowerShell commands listed in these steps.

  1. Back up the MEPF details. Mail Enabled Public folders don't hold any data themselves but
       are objects in Active Directory that are linked to public folder that hosts the actual data.
       Run:

  PowerShell

  Set-ADServerSettings -ViewEntireForest:$true
  Get-MailPublicFolder -ResultSize Unlimited| Export-Clixml MEPF.XML

  2. Disable MEPFs.

Run the following command:

  PowerShell

  Set-ADServerSettings -ViewEntireForest:$true
  Get-MailPublicFolder -ResultSize Unlimited | Disable-MailPublicFolder

  3. Verify that no MEPFs are listed. You also might verify that there's no more object of type
       "PublicFolder" in any of the Microsoft Exchange System Objects OUs in your on-premises
       AD.

Run:

<!-- p.2035 -->

  PowerShell

  Get-MailPublicFolder

  4. Verify the Exchange Mail Public Folders checkbox is cleared from the Microsoft Entra
     Connect tool.

  5. Perform the Microsoft Entra Connect Sync.

Remove the public folder mailboxes
The following command locks the public folders for user connections and indicates public
folder migration has been completed in the environment:

  PowerShell

  Set-OrganizationConfig -PublicFolderMailboxesLockedForNewConnections $true -
  PublicFolderMailboxesMigrationComplete $true

  2. Remove secondary hierarchy PF mailboxes.

  PowerShell

<!-- p.2036 -->

Set-ADServerSettings -ViewEntireForest:$true

Get-Mailbox -PublicFolder -ResultSize Unlimited |?{$_.IsRootPublicFolderMailbox -
ne "True"} | Remove-Mailbox -PublicFolder

2. Remove the primary hierarchy PF mailbox:

PowerShell

Get-Mailbox -PublicFolder |?{$_.IsRootPublicFolderMailbox -eq "True"} | Remove-
Mailbox -PublicFolder

<!-- p.2037 -->

Roll back a public folder migration from
Exchange Server to Exchange Online
Article • 04/30/2025

APPLIES TO:          2016   2019      Subscription Edition

If you run into issues with your public folder migration to Exchange Online, or for any other
reason need to reactivate your Exchange Server public folders, perform the following steps:

Roll back the migration
If you roll back your migration, you will lose any content that was added to public folders in
Exchange Online post-migration, either through clients or via email for mail-enabled public
folders. To save this content, you can export the post-migration public folder content to a .pst
file, which can then be imported into the on-premises public folders when the rollback is
complete.

   1. In your Exchange on-premises environment, run the following command to unlock your
      Exchange Server public folders:

        PowerShell

        Set-OrganizationConfig -PublicFolderMailboxesLockedForNewConnections:$false -
        PublicFolderMailboxesMigrationComplete:$false -PublicFoldersEnabled Local

        ７ Note

        The unlocking may take several hours.

   2. In your Exchange on-premises environment, revert the ExternalEmailAddress of any mail-
      enabled public folder that was updated by SetMailPublicFolderExternalAddress.ps1 (the
      script used in Step 8: Test and unlock public folders in Exchange Online of Use batch
      migration to migrate Exchange Server public folders to Exchange Online). You can refer to
      the summary file created by the script to identify the ones that were modified, or use the
      OnPrem_MEPF.xml file generated earlier in the same batch migration process to get the
      original properties for all mail-enabled public folders.

   3. In Exchange Online PowerShell, run the following commands to remove all Exchange
      Online public folders and mailboxes:

        PowerShell

<!-- p.2038 -->

    Get-MailPublicFolder -ResultSize Unlimited | where {$_.EntryId -ne $null}|
    Disable-MailPublicFolder -Confirm:$false
    Get-PublicFolder -GetChildren \ -ResultSize Unlimited | Remove-PublicFolder -
    Recurse -Confirm:$false
    $hierarchyMailboxGuid = $(Get-
    OrganizationConfig).RootPublicFolderMailbox.HierarchyMailboxGuid
    Get-Mailbox -PublicFolder | Where-Object {$_.ExchangeGuid -ne
    $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force
    Get-Mailbox -PublicFolder | Where-Object {$_.ExchangeGuid -eq
    $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force
    Get-Mailbox -PublicFolder -SoftDeletedMailbox | Remove-Mailbox -PublicFolder
    -PermanentlyDelete:$true -Force

4. Run the following command in your Exchange Online environment to redirect public
  folder traffic back to on-premises (Exchange Server):

    PowerShell

    Set-OrganizationConfig -PublicFoldersEnabled Remote

5. See Configure Exchange 2013 public folders for a hybrid deployment for instructions on
  reconfiguring access to your on-premises public folders, so that your Exchange Online
  users can access them.

<!-- p.2039 -->

Use batch migration to migrate legacy
public folders to Microsoft 365

  ７ Note

  Public folder migrations from Exchange Server 2010 and older versions to Exchange Online
  (Public folders and Microsoft 365 Groups) will be blocked starting October 1st, 2025.
  Organizations currently using Exchange Server 2010, or older versions are who are planning
  to migrate public folders to Exchange Online (Public Folders and Microsoft 365 Groups)
  using Microsoft native migration tools will be impacted by this change. Customers migrating
  public folders from Exchange Server 2010 and older to Exchange Online should complete
  their public folder migration by 1st October 2025. Please check this announcement for more
  details.

Summary: Use these procedures to move your Exchange 2010 public folders to Microsoft 365.

This article describes how to migrate your public folders in a cutover or staged migration from
Update Rollup 8 for Exchange Server 2010 Service Pack 3 (SP3) to Microsoft 365 and Exchange
Online.

This article refers to the Exchange 2010 SP3 RU8 server as the legacy Exchange server. Also, the
steps in this article apply to both Exchange Online and Microsoft 365. The terms might be used
interchangeably in this article.

We recommend that you don't use Outlook's PST export feature to migrate public folders to
Exchange Online. Microsoft 365 and Exchange Online public folder mailbox growth is managed
using an auto-split feature that splits the public folder mailbox when it exceeds size quotas.
Auto-split can't handle the sudden growth of public folder mailboxes when you use PST export to
migrate your public folders and you might have to wait for up to two weeks for auto-split to
move the data from the primary mailbox. We recommend that you use the cmdlet-based
instructions in this document to migrate public folders to Exchange Online. However, if you elect
to migrate public folders using PST export, see the Migrate Public Folders to Microsoft 365 by
using Outlook PST export section later in this article.

You do the migration using the *-MigrationBatch cmdlets, in addition to the following
PowerShell scripts:

<!-- p.2040 -->

     SourceSideValidations.ps1 : Source Side Validation script scans the public folders at source

     and reports issues found along with action to fix the issues. You run this script on the legacy
     on-premises Exchange server.

     Export-PublicFolderStatistics.ps1 : This script creates the folder name-to-folder size

     mapping file. You run this script on the legacy Exchange server.

     PublicFolderToMailboxMapGenerator.ps1 : This script creates the public folder-to-mailbox

     mapping file by using the output from the Export-PublicFolderStatistics.ps1 script. You
     run this script on the legacy Exchange server.

     Create-PublicFolderMailboxesForMigration.ps1 : This script creates the target public folder

     mailboxes for the migration. In addition, this script calculates the number of mailboxes
     necessary to handle the estimated user load, based on the guidelines for the number of
     user logons per public folder mailbox recommended in Limits for Public Folders.

     Sync-MailPublicFolders.ps1 : This script synchronizes mail-enabled public folder objects

     between your local Exchange deployment and Microsoft 365. You run this script on the
     legacy Exchange server.

Step 1: Download the migration scripts provides details about where to download these scripts.
Make sure all scripts are downloaded to the same location.

What versions of Exchange are supported for migrating
public folders to Microsoft 365 and Exchange Online?
Exchange supports moving your public folders to Microsoft 365 and Exchange Online from the
following legacy versions of Exchange Server:

     Exchange 2010 SP3 RU8 or later

If you need to move your public folders to Exchange Online but your on-premises servers aren't
running the minimum support versions of Exchange 2010, we strongly recommend that you
upgrade your on-premises servers and use batch migration, which is the only supported public
folder migration method.

You can't migrate public folders directly from Exchange 2003 or Exchange 2007. If you're running
Exchange 2007 or earlier in your organization, you need to move all public folder databases and
replicas to Exchange 2010 SP3 RU8 or later. No public folder replicas can remain on Exchange
