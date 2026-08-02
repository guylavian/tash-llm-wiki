---
title: "Exchange Server — pages 2041-2080"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2041-2080
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2041-2080
family: exchange
documentKind: "doc"
abstract: "2007 or earlier. Additionally, mail destined for an Exchange 2013 or later public folder can't be routed through an Exchange 2003 or Exchange 2007 server. What do you need to know before you begin? The Exchange 2010 server needs to be running Exchange 2010 SP3 RU8 or later. In M"
---

# Exchange Server — pages 2041-2080

<!-- p.2041 -->

2007 or earlier. Additionally, mail destined for an Exchange 2013 or later public folder can't be
routed through an Exchange 2003 or Exchange 2007 server.

What do you need to know before you begin?
     The Exchange 2010 server needs to be running Exchange 2010 SP3 RU8 or later.

     In Microsoft 365 and Exchange Online, you need to be a member of the Organization
     Management role group. This role group is different from the permissions assigned to you
     when you first enrolled. For details about how to enable the Organization Management role
     group, see Manage role groups in Exchange Online.

     In Exchange 2010, you need to be a member of the Organization Management or Server
     Management RBAC role groups. For details, see Add Members to a Role Group.

     Before you begin the public folder migration, if any single public folder in your organization
     is larger than 25 GB, we recommend that you delete content from that folder to make it
     smaller. Or, we recommend that you divide the public folder's content into multiple, smaller
     public folders. The 25 GB limit cited here only applies to the public folder and not to any
     child or subfolders. If neither option is feasible, we recommend that you don't move your
     public folders to Exchange Online. For more information, see Exchange Online Limits.

         Tip

        If your current public folder quotas in Exchange Online are less than 25 GB, you can use
        the Set-OrganizationConfig cmdlet to increase them with the
        DefaultPublicFolderIssueWarningQuota and DefaultPublicFolderProhibitPostQuota

        parameters.

     If you use a firewall and access control lists (ACLs), ensure that the IP ranges used by
     Microsoft 365 in your region are permitted through your firewall.

     In Microsoft 365 and Exchange Online, you can create a maximum of 1,000 public folder
     mailboxes.

     Before you migrate your public folders, we recommend that you first move all user
     mailboxes to Microsoft 365 and Exchange Online. For details, see Ways to migrate multiple
     email accounts to Microsoft 365. However, you still need to keep in the on-premises
     environment the mailbox for PF admin performing migration or create new PF admin
     account and assign a mailbox hosted on the legacy Exchange server.

<!-- p.2042 -->

   Outlook Anywhere needs to be enabled on the legacy Exchange server. For details about
   enabling Outlook Anywhere on Exchange 2010 servers, see Enable Outlook Anywhere.

   You can't use the Exchange admin center (EAC) or the Exchange Management Console
   (EMC) to perform this procedure. On the legacy Exchange servers, you need to use the
   Exchange Management Shell. For Exchange Online, you need to use Exchange Online
   PowerShell. For more information, see Connect to Exchange Online PowerShell.

   You must use a single migration batch to migrate all of your public folder data. Exchange
   allows creating only one migration batch at a time. If you attempt to create more than one
   migration batch simultaneously, you get an error.

   Before you begin, we recommend that you read this article in its entirety as downtime is
   required for some steps.

   For information about keyboard shortcuts that might apply to the procedures in this article,
   see Keyboard shortcuts for the Exchange admin center.

   Verify if the DefaultPublicFolderAgeLimit is configured on the organization level ( Get-
   OrganizationConfig | Format-List DefaultPublicFolderAgeLimit ) or if you have any

   AgeLimit ( Get-PublicFolder <FolderPath> | Format-List AgeLimit ) configured for the
   individual Public Folders, so that automatic deletions of the content to be prevented.

  Tip

 Having problems? Ask for help in the Exchange Online forum at Exchange Online.

Step 1: Download the migration scripts
 1. Download all scripts and supporting files from Public Folders Migration Scripts .

 2. Save the scripts to the local computer where you intend to run PowerShell. For example,
   C:\PFScripts. Make sure all scripts are saved in the same location.

 3. Download the following file from Mail-enabled Public Folders - directory sync script      :

         Sync-MailPublicFolders.ps1

 4. Download the source side validation script from https://aka.ms/ssv2    .

 5. Save the scripts to the same location you did for step 2. For example, C:\PFScripts.

<!-- p.2043 -->

Step 2: Prepare for the migration
Perform the following prerequisite steps before you begin the migration.

  ７ Note

  We strongly recommend running the Source Side Validation script from an on-premises
  Exchange 2010 server with the Mailbox role installed. The script scans and reports issues that
  are known to cause migration to be slow, along with guidance to fix these issues. Use the
  examples described here    .

General prerequisite steps
     Make sure that there are no orphaned public folder mail objects in Active Directory,
     meaning objects in Active Directory without a corresponding Exchange object.
     Confirm that SMTP email address configured for public folders in Active Directory match the
     SMTP email addresses on the Exchange objects.
     Make sure that there are no duplicate public folder objects in Active Directory, to avoid a
     situation where two or more Active Directory objects are pointing to the same mail-enabled
     public folder.

Prerequisite steps on the legacy Exchange server

  ７ Note

  We strongly recommend running the Source Side Validation script from an on-premises
  Exchange 2010 server with the Mailbox role installed. The script scans and reports issues that
  are known to cause migration to be slow, along with guidance to fix these issues. Use the
  examples as documented here . The script does all the following prerequisites.

   1. On the legacy Exchange server, make sure that routing to the mail-enabled public folders in
     the cloud continues to work until all DNS caches over the internet are updated to point to
     the cloud DNS where your organization now resides. Run the following command to
     configure an accepted domain with a well-known name that properly routes email
     messages to the cloud domain.

       PowerShell

<!-- p.2044 -->

  New-AcceptedDomain -Name
  "PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99" -DomainName
  <target domain> -DomainType InternalRelay

Example:

  PowerShell

  New-AcceptedDomain -Name
  PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 -DomainName
  'contoso.mail.onmicrosoft.com' -DomainType InternalRelay

If the accepted domain already exists in your on-premises environment, rename it to
PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99 and leave the other
attributes intact.

To check if the accepted domain is already present in your on-premises environment, run
the following command:

  PowerShell

  Get-AcceptedDomain | Where {$_.DomainName -eq "<target domain>"}

To rename the accepted domain to
PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99, run the following
command:

  PowerShell

  Get-AcceptedDomain | Where {$_.DomainName -eq "<target domain>"} | Set-
  AcceptedDomain -Name PublicFolderDestination_78c0b207_5ad2_4fee_8cb9_f373175b3f99

If you're expecting your mail-enabled public folders in Exchange Online to receive external
emails from the Internet, you have to disable Directory Based Edge Blocking (DBEB) in
Microsoft 365. See Use Directory Based Edge Blocking to reject messages sent to invalid
recipients for more information.

If the name of a public folder contains a backslash ( \ ) or a forward slash ( / ), the public
folders might be created in the parent public folder when migration occurs. Before you
migrate, we recommend that you rename any public folders that have a backslash or a
forward slash in the name.

<!-- p.2045 -->

  In Exchange 2010, to locate public folders that have a backslash in the name, run the
  following command:

    PowerShell

    Get-PublicFolderStatistics -ResultSize Unlimited | Where {($_.Name -like "*\*") -
    or ($_.Name -like "*/*") } | Format-List Name,Identity

2. If any public folders are returned, you can rename them by running the following command:

    PowerShell

    Set-PublicFolder -Identity <public folder identity> -Name <new public folder
    name>

3. Make sure there isn't a previous record of a successful migration. If there is, you need to set
  that value to $false . Otherwise, the migration request will fail.

  The following example checks the public folder migration status.

    PowerShell

    Get-OrganizationConfig | Format-List
    PublicFoldersLockedforMigration,PublicFolderMigrationComplete

4. This step is required only if you're re-attempting a migration that failed previously.

  If the status of the PublicFoldersLockedforMigration or PublicFolderMigrationComplete
  properties is $true , run the following command to set the value to $false .

    PowerShell

    Set-OrganizationConfig -PublicFoldersLockedforMigration:$false -
    PublicFolderMigrationComplete:$false

    ） Important

    After resetting these properties, you need to wait for Exchange to detect the new
    settings. This result might take up to two hours to complete.

5. For verification purposes at the end of migration, we recommend that you first run the
  following Exchange Management Shell commands on the legacy Exchange server to take

<!-- p.2046 -->

  snapshots of your current public folder deployment.

  Run the following command to take a snapshot of the original source folder structure.

    PowerShell

    Get-PublicFolder -Recurse -ResultSize Unlimited | Export-CliXML
    C:\PFMigration\Legacy_PFStructure.xml

  Run the following command to take a snapshot of public folder statistics such as item
  count, size, and owner.

    PowerShell

    Get-PublicFolderStatistics -ResultSize Unlimited | Export-CliXML
    C:\PFMigration\Legacy_PFStatistics.xml

  Run the following command to take a snapshot of the permissions.

    PowerShell

    Get-PublicFolder -Recurse -ResultSize Unlimited | Get-
    PublicFolderClientPermission | Select-Object Identity,User -ExpandProperty
    AccessRights | Export-CliXML C:\PFMigration\Legacy_PFPerms.xml

  Save the information from the preceding commands for comparison at the end of the
  migration.

6. If you're using Microsoft Entra Connect (Microsoft Entra Connect) to synchronize your on-
  premises directories with Microsoft Entra ID, you need to do the following (if you aren't
  using Microsoft Entra Connect, you can skip this step):

  a. On an on-premises computer, open Microsoft Entra Connect, and then select Configure.

  b. On the Additional tasks screen, select Customize synchronization options, and then
     select Next.

   c. On the Connect to Microsoft Entra ID screen, enter the appropriate credentials, and then
     select Next. Once connected, keep selecting Next until you are on the Optional Features
     screen.

  d. Make sure that Exchange Mail Public Folders isn't selected. If it isn't selected, you can
     continue to the next section. If it's selected, clear the check box, and then select Next.

<!-- p.2047 -->

          ７ Note

          If you don't see Exchange Mail Public Folders as an option on the Optional
          Features screen, you can exit Microsoft Entra Connect and proceed to the next
          section.

   7. After you clear the Exchange Mail Public Folders selection, keep selecting Next until you're
     on the Ready to configure screen, and then select Configure.

For detailed syntax and parameter information, see the following articles:

     New-AcceptedDomain
     Get-PublicFolder
     Get-PublicFolderDatabase
     Set-PublicFolder
     Get-PublicFolderStatistics
     Get-PublicFolderClientPermission
     Get-OrganizationConfig
     Set-OrganizationConfig

Prerequisite steps in the cloud
   1. Make sure there are no existing public folder migration requests. If there are, clear them or
     your own migration request will fail. This step isn't required in all cases; it's only required if
     you think there might be an existing migration request in the pipeline.

       ） Important

       Before removing a migration request, it's important to understand why there was an
       existing one. The following commands determine when a previous request was made
       and helps you diagnose any problems that might have happened. You might need to
       communicate with other administrators in your organization to determine why the
       change was made.

     The following example discovers any existing batch migration requests:

       PowerShell

<!-- p.2048 -->

    $batch = Get-MigrationBatch | Where-Object {$_.MigrationType.ToString() -eq
    "PublicFolder"}

  The following example removes any existing public folder batch migration requests.

    PowerShell

    $batch | Remove-MigrationBatch -Confirm:$false

2. Confirm that no public folders or public folder mailboxes exist in the cloud.

    ） Important

    If you see public folders in the cloud, it's important to determine why they're there, and
    who started a public folder hierarchy before you remove the public folders and public
    folder mailboxes.

   a. In Exchange Online PowerShell, run the following command to see if any public folders
     mailboxes exist:

       PowerShell

       Get-Mailbox -PublicFolder

  b. If the command didn't return any public folder mailboxes, continue to Step 3: Generate
     the .csv files. If the command returned any public folders mailboxes, run the following
     command to see if any public folders exist:

       PowerShell

       Get-PublicFolder

   c. If you have any public folders in the cloud, run the following command in Exchange
     Online PowerShell to remove them. Make sure you saved any information that was in the
     cloud-based public folders.

       Ｕ Caution

<!-- p.2049 -->

          All information contained in the public folders is permanently deleted when you
          remove the public folders.

          PowerShell

          Get-MailPublicFolder | where {$_.EntryId -ne $null}| Disable-MailPublicFolder
          -Confirm:$false
          Get-PublicFolder -GetChildren \ | Remove-PublicFolder -Recurse -Confirm:$false

     d. After the public folders are removed, run the following commands to remove all public
        folder mailboxes.

          PowerShell

          $hierarchyMailboxGuid = $(Get-
          OrganizationConfig).RootPublicFolderMailbox.HierarchyMailboxGuid
          Get-Mailbox -PublicFolder:$true | Where-Object {$_.ExchangeGuid -ne
          $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false
          Get-Mailbox -PublicFolder:$true | Where-Object {$_.ExchangeGuid -eq
          $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false

For detailed syntax and parameter information, see the following articles:

     Get-MigrationBatch
     Get-PublicFolderMailboxMigrationRequest
     Remove-PublicFolderMailboxMigrationRequest
     Get-Mailbox
     Get-PublicFolder
     get-MailPublicFolder
     Disable-MailPublicFolder
     remove-PublicFolder
     Remove-Mailbox

Step 3: Generate the .csv files
   1. On the legacy Exchange server, run the Export-PublicFolderStatistics.ps1 script to create
     the folder name-to-folder size mapping file. A local administrator needs to run this script.
     The file contains two columns: FolderName and FolderSize. The FolderSize column is
     displayed in bytes. For example, \PublicFolder01,10000.

       PowerShell

<!-- p.2050 -->

    .\Export-PublicFolderStatistics.ps1       <Folder to size map path> <FQDN of source
    server>

       FQDN of source server equals the fully qualified domain name of the Mailbox server
       where the public folder hierarchy is hosted.

       Folder to size map path equals the file name and path on a network shared folder
       where you want the .csv file saved. Later in this article, you need to use the Exchange
       Online PowerShell to access this file. If you specify only the file name, the file is
       generated in the current PowerShell directory on the local computer.

       If necessary, remove any mail-enabled system folders from the script output before
       proceeding.

2. Run the PublicFolderToMailboxMapGenerator.ps1 script to create the public folder-to-
  mailbox mapping file. This file is used to calculate the correct number of public folder
  mailboxes in Exchange Online.

    PowerShell

    .\PublicFolderToMailboxMapGenerator.ps1 <Maximum mailbox size in bytes> <Folder
    to size map path> <Folder to mailbox map path>

       Before you run the script, use the following command to check the current public
       folder limits in your Exchange Online tenant. Then, note the current quota values for
       public folders.

         PowerShell

         Get-OrganizationConfig | Format-List *quota*

       In Exchange Online, the default value is 1.7 GB for
       DefaultPublicFolderIssueWarningQuota and 2 GB for
       DefaultPublicFolderProhibitPostQuota.

       Maximum mailbox size in bytes equals the maximum size that you want to set for the
       new public folder mailboxes. In Exchange Online, the maximum size of public folder
       mailboxes is 100 GB. We recommend that you use a setting of 75 GB so that each
       public folder mailbox has room to grow. Fewer public folder mailboxes mean fewer
       connections for the Outlook clients, which might help to avoid performance issues.
       The location is transparent for users, as they see the same hierarchy on the client side.

<!-- p.2051 -->

          Exchange Online has a default public folder "prohibit post" quota of 2 GB. If you have
          individual public folders that are larger than 2 GB, you can use any of the following
          options to fix this issue:

          Before you start the migration batch, increase the default public folder "prohibit post"
          quota by running the following command:

            PowerShell

            Set-OrganizationConfig -DefaultPublicFolderProhibitPostQuota <size value> -
            DefaultPublicFolderIssueWarningQuota <size value>

          Before you start the migration batch, delete public folder content to reduce the size of
          the content to 2 GB or less.

          Before you start the migration batch, split the public folder into multiple public folders
          that are each 2 GB or less.

            ７ Note

            If the public folder is larger than 30 GB, and if it isn't feasible to delete content or
            split it into multiple public folders, we recommend that you don't move your
            public folders to Exchange Online.

          Folder to size map path equals the file path of the .csv file that you created when you
          ran the Export-PublicFolderStatistics.ps1 script.

          Folder to mailbox map path equals the file name and path of the folder-to-mailbox .csv
          file that you create in this step. If you specify only the file name, the file is generated in
          the current PowerShell directory on the local computer.

 ７ Note

 After the scripts are run and the .csv files are generated, any new public folders or updates
 to existing public folders aren't collected.

Step 4: Create the public folder mailboxes in
Exchange Online

<!-- p.2052 -->

Run the following command to create the target public folder mailboxes. The script creates a
target mailbox for each mailbox in the .csv file that you generated previously in Step 3, by
running the PublicFoldertoMailboxMapGenerator.ps1 script.

 PowerShell

 .\Create-PublicFolderMailboxesForMigration.ps1 -FolderMappingCsv Mapping.csv -
 EstimatedNumberOfConcurrentUsers:<estimate>

Mapping.csv is the file generated by the PublicFoldertoMailboxMapGenerator.ps1 script in Step 3.
The estimated number of simultaneous user connections browsing a public folder hierarchy is
usually less than the total number of users in an organization.

  ７ Note

  Use Exchange Online PowerShell for running this script. For more information, see Connect
  to Exchange Online PowerShell.

Step 5: Start the migration request
   1. Perform the following steps on the Exchange server to fulfill the prerequisite for running the
     Sync-MailPublicFolders.ps1 script.

      a. Sign in with the account that has Enterprise administrator permissions.

     b. Install EXO PowerShell as described in Install and maintain the Exchange Online
        PowerShell module.

      c. Launch PowerShell in administrator mode.

     d. Run the following commands to start the synchronization:

          PowerShell

          Add-PSSnapin *exchange* | .\Sync-MailPublicFolders.ps1 -
          CsvSummaryFile:sync_summary.csv

      e. Once prompted, enter the credentials for your Microsoft 365 tenant administrator
        account.

<!-- p.2053 -->

2. On the legacy Exchange server, get the following information that's needed to run the
  migration request:

  a. Find the LegacyExchangeDN of the user's account who is a member of the Public Folder
     Administrator role. This account is the same user whose credentials you need in step 3 of
     this procedure.

       ７ Note

       The account used must be mailbox enabled in the on-premises Exchange Server.
       Create a new on-premises mailbox for the Public Folder Administrator account if
       one doesn't exist there.

       PowerShell

       Get-Mailbox <PublicFolder_Administrator_Account> | Select-Object
       LegacyExchangeDN

  b. Find the LegacyExchangeDN of any Mailbox server that has a public folder database.

       PowerShell

       Get-ExchangeServer <public folder server> | Select-Object -Expand
       ExchangeLegacyDN

   c. Find the FQDN of the Outlook Anywhere host name. If you have multiple instances of
     Outlook Anywhere, we recommend that you select the instance that is either closest to
     the migration endpoint or the one that is closest to the public folder replicas in the
     legacy Exchange organization. The following command finds all instances of Outlook
     Anywhere:

       PowerShell

       Get-OutlookAnywhere | Format-Table Identity,ExternalHostName

3. In Exchange Online PowerShell, run the following commands to pass the information that
  was returned in the previous step to variables that are used in the migration request.

  a. Pass the credential of a user who has administrative permissions on the legacy Exchange
     server into the variable $Source_Credential . The migration request that's run in Exchange

<!-- p.2054 -->

     Online uses this credential to gain access to your legacy Exchange servers to copy the
     content over.

      PowerShell

      $Source_Credential = Get-Credential
      <source_domain\PublicFolder_Administrator_Account>

  b. Use the ExchangeLegacyDN of the migration user on the legacy Exchange server that you
     found in step 2a and pass it into the variable $Source_RemoteMailboxLegacyDN .

      PowerShell

      $Source_RemoteMailboxLegacyDN = "<paste the value here>"

  c. Use the ExchangeLegacyDN of the public folder server that you found in step 2b above
     and pass it into the variable $Source_RemotePublicFolderServerLegacyDN .

      PowerShell

      $Source_RemotePublicFolderServerLegacyDN = "<paste the value here>"

  d. Use the External Host Name of Outlook Anywhere that you found in step 2c above and
     pass it into the variable $Source_OutlookAnywhereExternalHostName .

      PowerShell

      $Source_OutlookAnywhereExternalHostName = "<paste the value here>"

4. Finally, in Exchange Online PowerShell, run the following commands to create the migration
  request.

    ７ Note

    The authentication method in the following example needs to match your Outlook
    Anywhere settings. Otherwise, the command will fail.

    PowerShell

    $PfEndpoint = New-MigrationEndpoint -PublicFolder -Name PublicFolderEndpoint -
    RPCProxyServer $Source_OutlookAnywhereExternalHostName -Credentials
    $Source_Credential -SourceMailboxLegacyDN $Source_RemoteMailboxLegacyDN -

<!-- p.2055 -->

       PublicFolderDatabaseServerLegacyDN $Source_RemotePublicFolderServerLegacyDN -
       Authentication Basic
       $bytes = [System.IO.File]::ReadAllBytes('folder_mapping.csv')
       New-MigrationBatch -Name PublicFolderMigration -CSVData $bytes -SourceEndpoint
       $PfEndpoint.Identity -NotificationEmails <email addresses for migration
       notifications>

     Where folder_mapping.csv is the map file that was generated in Step 3: Generate the .csv
     files.

        ７ Note

        You might notice the above command failing with the error "Cannot find a recipient
        that has mailbox GUID" error, with the GUID mentioned of public folder mailbox in
        EXO. This issue can be caused by AD replication latency. Wait an hour and retry the
        command.

   5. Start the migration using the following command:

       PowerShell

       Start-MigrationBatch PublicFolderMigration

While batch migrations need to be created using the New-MigrationBatch cmdlet in the
Exchange Management Shell, the progress and completion of the migration can be viewed and
managed in the EAC. Because the New-MigrationBatch cmdlet initiates a mailbox migration
request for each public folder mailbox, you can view the status of these requests using the
mailbox migration page. You can get to the mailbox migration page, and create migration reports
that can be emailed to you, by doing the following:

   1. Log into Exchange Online and open the EAC.

   2. Navigate to Mailbox > Migration.

   3. Select the migration request that was just created, and then select View Details in the
     Details pane.

For detailed syntax and parameter information, see the following articles:

     Get-Mailbox

     Get-ExchangeServer

<!-- p.2056 -->

     Get-OutlookAnywhere

     New-MigrationBatch

     Get-PublicFolderDatabase

     Get-PublicFolderMailboxMigrationRequest

     Get-PublicFolderMailboxMigrationRequestStatistics

Step 6: Lock down the public folders on the
legacy Exchange server for final migration
(downtime required)
Up to this point in the migration, users can still access public folders. The next steps disconnect
users from the legacy public folders and lock the folders while the migration completes final
synchronization. Users can't access public folders during this process. Also, any mail sent to mail-
enabled public folders is queued and isn't delivered until the public folder migration is complete.

  ７ Note

  The final sync might take substantial amount of time, depending on the changes made on
  the source environment, size of public folder deployment, server capacity, etc. Not cleaning
  up a large number of corrupt ACLs in the folder hierarchy before starting migration can
  cause a significant delay. We recommend that you plan for a minimum of 48 hours of
  downtime for the final sync to complete.

Ensure the migration batch and individual migration requests have successfully synced.

Run the following commands in Exchange Online PowerShell to get the details:

 PowerShell

 Get-MigrationBatch | Where-Object {$_.MigrationType -like "*PublicFolder*"} | Format-
 Table *last*sync*

 Get-PublicFolderMailboxMigrationRequest | Get-
 PublicFolderMailboxMigrationRequestStatistics | Format-Table targetmailbox,*last*sync*

The LastSyncedDate (on migration batch) and LastSuccessfulSyncTimestamp (on individual jobs)
should be within last seven days. If it's too far off, like older than a month or so, you might want

<!-- p.2057 -->

to take a look at public folder migration requests and ensure all the requests were synced
recently.

Once you have confirmed the batch and all migration requests have successfully synced, on the
legacy Exchange server, run the following command to lock the legacy public folders for
finalization.

  PowerShell

  Set-OrganizationConfig -PublicFoldersLockedForMigration:$true

For detailed syntax and parameter information, see set-OrganizationConfig.

If your organization has multiple public folder databases, you need to wait until public folder
replication is complete to confirm that all public folder databases have picked up the
PublicFoldersLockedForMigration flag and any pending changes users recently made to folders

have converged across the organization. This processmight take several hours.

Step 7: Finalize the public folder migration
(downtime required)
To complete the public folder migration, run the following command:

  PowerShell

  Complete-MigrationBatch PublicFolderMigration

  ） Important

  After a migration batch is completed, no additional data can be synchornized from Exchange
  servers on-premises and Exchange Online.

When you complete the migration, Exchange performs a final synchronization between the
legacy Exchange server and Exchange Online. If the final synchronization is successful, the public
folders in Exchange Online are unlocked and the status of the migration batch changes to
Completed. It's common for the status of migration batch to remain on "Synced" for few hours
before it switches to Completing. For migrations involving large number of target mailboxes, it's
normal to see the status remain "Synced" state for more than 24 hours, provided none of
underlying public folder migration requests have failed or were quarantined.

<!-- p.2058 -->

If you configured a hybrid deployment between your on-premises Exchange servers and
Microsoft 365, you need to run the following command in Exchange Online PowerShell after
migration is complete:

 PowerShell

 Set-OrganizationConfig -RemotePublicFolderMailboxes $Null -PublicFoldersEnabled Local

Step 8: Test and unlock the public folder migration
After you finalize the public folder migration, you should run the following test to make sure that
the migration was successful. This allows you to test the migrated public folder hierarchy before
you switch to using public folders in the cloud.

   1. In Exchange Online PowerShell, assign some test mailboxes to use any newly migrated
     public folder mailbox as the default public folder mailbox.

       PowerShell

       Set-Mailbox -Identity <Test User> -DefaultPublicFolderMailbox <Public Folder
       Mailbox Identity>

   2. Sign in Outlook 2010 or later with the test user identified in the previous step, and then
     perform the following public folder tests:

           View the hierarchy.
           Check permissions.
           Create and delete public folders.
           Post content to and delete content from a public folder.

   3. If you run into any issues, see Roll back the migration later in this article. If the public folder
     content and hierarchy is acceptable and functions as expected, continue to the next step.

   4. On the legacy Exchange server, run the following command to indicate that the public
     folder migration is complete:

       PowerShell

       Set-OrganizationConfig -PublicFolderMigrationComplete:$true

<!-- p.2059 -->

   5. After you verify that migration is complete, run the following command in Exchange Online
     PowerShell to make sure that the PublicFoldersEnabled parameter on Set-
     OrganizationConfig is set to Local :

       PowerShell

       Set-OrganizationConfig -PublicFoldersEnabled Local

For detailed syntax and parameter information, see the following articles:

Set-Mailbox

Get-Mailbox

Set-OrganizationConfig

How do I know this worked?
In Step 2: Prepare for the migration, you were instructed to take snapshots of the public folder
structure, statistics, and permissions before the migration began. The following steps help verify
that your public folder migration was successful by taking the same snapshots after the migration
is complete. You can then compare the data in both files to verify success.

   1. In Exchange Online PowerShell, run the following command to take a snapshot of the new
     folder structure.

       PowerShell

       Get-PublicFolder -Recurse -ResultSize Unlimited | Export-CliXML
       C:\PFMigration\Cloud_PFStructure.xml

   2. In Exchange Online PowerShell, run the following command to take a snapshot of the public
     folder statistics such as item count, size, and owner.

       PowerShell

       Get-PublicFolderStatistics | Export-CliXML C:\PFMigration\Cloud_PFStatistics.xml

   3. In Exchange Online PowerShell, run the following command to take a snapshot of the
     permissions.

       PowerShell

<!-- p.2060 -->

       Get-PublicFolder -Recurse -ResultSize Unlimited | Get-
       PublicFolderClientPermission | Select-Object Identity,User -ExpandProperty
       AccessRights | Export-CliXML C:\PFMigration\Cloud_PFPerms.xml

Remove public folder databases from the legacy
Exchange servers
After the migration is complete, and you have verified that your Exchange Online public folders
are working as expected, you should remove the public folder databases on the legacy Exchange
servers.

  ） Important

  Since all of your mailboxes were migrated to Microsoft 365 before the public folder
  migration, we strongly recommend that you route the traffic through Microsoft 365
  (decentralized mail flow) instead of centralized mail flow through your on-premises
  environment. Choosing to keep mail flow centralized could cause delivery issues to your
  public folders, since you removed public folder mailbox databases from your on-premises
  organization.

     For details about how to remove public folder databases from Exchange 2010 servers, see
     Remove Public Folder Databases.

Roll back the migration
If you run into issues with the migration and need to reactivate your legacy Exchange public
folders, perform the following steps.

  Ｕ Caution

  If you roll your migration back to the legacy Exchange servers, you lose any email that was
  sent to mail-enabled public folders or content that was posted to public folders after the
  migration. To save this content, you need to export the public folder content to a .pst file
  and then import it to the legacy public folders when the rollback is complete.

   1. On the legacy Exchange server, run the following command to unlock the legacy Exchange
     public folders. This process might take several hours.

<!-- p.2061 -->

       PowerShell

       Set-OrganizationConfig -PublicFoldersLockedForMigration:$False

   2. In Exchange Online PowerShell, run the following commands to remove all Exchange Online
     public folders.

       PowerShell

       $hierarchyMailboxGuid = $(Get-
       OrganizationConfig).RootPublicFolderMailbox.HierarchyMailboxGuid
       Get-Mailbox -PublicFolder:$true | Where-Object {$_.ExchangeGuid -ne
       $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force
       Get-Mailbox -PublicFolder:$true | Where-Object {$_.ExchangeGuid -eq
       $hierarchyMailboxGuid} | Remove-Mailbox -PublicFolder -Confirm:$false -Force

   3. On the legacy Exchange server, run the following command to set the
     PublicFolderMigrationComplete flag to $false .

       PowerShell

       Set-OrganizationConfig -PublicFolderMigrationComplete:$False

Migrate Public Folders to Microsoft 365 by using
Outlook PST export
We recommend that you don't use Outlook's PST export feature to migrate public folders to the
cloud if your on-premises public folder hierarchy is greater than 30 GB. Microsoft 365 online
public folder mailbox growth is managed using an auto-split feature that splits the public folder
mailbox when it exceeds size quotas. Auto-split can't handle the sudden growth of public folder
mailboxes when you use PST export to migrate your public folders and you might have to wait
for up to two weeks for auto-split to move the data from the primary mailbox. In addition,
consider the following before using Outlook PST to export public folders to the cloud:

     Public folder permissions are lost during this process. Capture the current permissions
     before migration and manually add them back once the migration is completed.

     If you use complex permissions or have many folders to migrate, we recommend that you
     use the cmdlet method for migration.

     Any item and folder changes made to the source public folders during the PST export
     migration are lost. Therefore, we recommend that you use the cmdlet method if this export

<!-- p.2062 -->

     and import process takes a long time to complete.

If you still want to migrate your public folders by using PST files, follow these steps to ensure a
successful migration.

   1. Use the instructions in Step 1: Download the migration scripts to download the migration
     scripts. You only need to download the PublicFolderToMailboxMapGenerator.ps1 file.

   2. Follow step 2 of Step 3: Generate the .csv files to create the public folder-to-mailbox
     mapping file. This file is used to calculate the correct number of public folder mailboxes in
     Exchange Online.

   3. Create the public folder mailboxes that you need based on the mapping file. For more
     information, see Create a public folder mailbox.

   4. Use the New-PublicFolder cmdlet to create the top-most public folder in each of the public
     folder mailboxes by using the Mailbox parameter.

   5. Export and import the PST files using Outlook.

   6. Set the permissions on the public folders using the EAC. For more information, see Step 3:
     Assign permissions to the public folder.

  ） Important

  If you already started a PST migration and run into an issue where the primary mailbox is
  full, you have two options for recovering the PST migration:

        Wait for the auto-split to move the data from the primary mailbox. This process might
        take up to two weeks. However, all the public folders in a completely filled public folder
        mailbox can't receive new content until the auto-split completes.
        Create a public folder mailbox and then use the New-PublicFolder cmdlet with the
        Mailbox parameter to create the remaining public folders in the secondary public folder
        mailbox.

Troubleshoot public folder migrations
Select the following button for common issues during public folder migration:

 Run Tests: Troubleshoot public folder migration

<!-- p.2063 -->

A flyout page opens in the Microsoft 365 admin center, sign in with your tenant admin account
and select appropriate option.

Last updated on 06/11/2026

<!-- p.2064 -->

Migrate public folders from Exchange 2013
to Exchange 2016 or Exchange 2019
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

To migrate your Exchange 2013 public folders to Exchange 2016 or Exchange 2019, you need
to move all of your Exchange 2013 public folder mailboxes to an Exchange 2016 server or
Exchange 2019 server.

Before you move your public folder mailboxes, here are some things you should consider:

      Capacity: The size of your public folder mailboxes might vary significantly depending on
      how many public folders and public folder mailboxes you have. Make sure the target
      Exchange servers where you'll move your public folder mailboxes have enough storage
      capacity.

      Time: It might take a while to move your public folder mailboxes. The following items
      could impact how long it takes:

      Public folder mailbox size

      The number of public folder mailboxes

      Network bandwidth

The good news is that your public folders will remain available during the public folder mailbox
move. There's only a brief time window where the public folders might no be available (as the
move completes).

What do you need to know before you begin?
      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

<!-- p.2065 -->

Use the Exchange Management Shell to move
public folder mailboxes from Exchange 2013 to
Exchange 2016 or Exchange 2019
 1. Run the following command to get a list of all Exchange 2013 public folder mailboxes:

     PowerShell

     Get-ExchangeServer | Where {($_.AdminDisplayVersion -Like 'Version 15.0*') -
     And ($_.ServerRole -Like '*Mailbox*')} | Get-Mailbox -PublicFolder | Get-
     MailboxStatistics | Format-Table -Auto ServerName,DisplayName,TotalItemSize

 2. Use the following syntax to list all mailbox databases on all Exchange 2016 or Exchange
   2019 Mailbox servers:

     PowerShell

     Get-ExchangeServer | Where {($_.AdminDisplayVersion -like '<Version>') -and
     ($_.ServerRole -Like "*Mailbox*")} | Get-MailboxDatabase | Format-List
     Server,Name,EdbFilePath

   You can use the location information that's returned by this command to check the
   available free disk space for each mailbox database.

   This example returns the locations of all mailbox databases on all Exchange 2016 Mailbox
   servers.

     PowerShell

     Get-ExchangeServer | where {($_.AdminDisplayVersion -like 'Version 15.1*') -
     and ($_.ServerRole -Like '*Mailbox*')} | Get-MailboxDatabase | Format-List
     Server,Name,EdbFilePath

   This example returns the locations of all mailbox databases on all Exchange 2019 Mailbox
   servers.

     PowerShell

     Get-ExchangeServer | where {($_.AdminDisplayVersion -like 'Version 15.2*') -
     and ($_.ServerRole -Like '*Mailbox*')} | Get-MailboxDatabase | Format-List
     Server,Name,EdbFilePath

   This example returns the locations of all mailbox databases on all Exchange 2016 and
   Exchange 2019 Mailbox servers.

<!-- p.2066 -->

    PowerShell

    Get-ExchangeServer | where {(($_.AdminDisplayVersion -like 'Version 15.1*') -
    or ($_.AdminDisplayVersion -like 'Version 15.2*')) -and ($_.ServerRole -Like
    '*Mailbox*')} | Get-MailboxDatabase | Format-List Server,Name,EdbFilePath

3. Use the information from the previous steps to decide the target mailbox database
  and/or Mailbox server (if you have more than one) to move some or all of your public
  folder mailboxes to. For example, you might not want to move three large public folder
  mailboxes to a server with low available drive space.

  You can also decide whether you want to move all public folder mailboxes at once, all
  public folder mailboxes on a specific server, or a specific public folder mailbox.

  Choose the command that fits the kind of move you want to do. Be sure to replace the
  Exchange server names, database names, and public folder mailbox names with your own.

       Move all Exchange 2013 public folder mailboxes at once.

          PowerShell

          Get-ExchangeServer | Where {($_.AdminDisplayVersion -Like "Version
          15.0*") -And ($_.ServerRole -Like "*Mailbox*")} | Get-Mailbox -
          PublicFolder | New-MoveRequest -TargetDatabase Ex2016MbxDatabase

       Move all public folder mailboxes on a specific Exchange 2013 server at once.

          PowerShell

          Get-Mailbox -PublicFolder -Server Ex2013Mbx | New-MoveRequest -
          TargetDatabase Ex2016MbxDatabase

       Move a specific Exchange 2013 public folder mailbox.

          PowerShell

          New-MoveRequest "Sales Public Folder Mailbox" -TargetDatabase
          Ex2016MbxDatabase

4. To see the status of the move requests you created, run the following command:

    PowerShell

    Get-MoveRequest

<!-- p.2067 -->

     Depending on the size of the public folder mailboxes you're moving and your available
     network capacity, it could take several hours or days for the moves to complete.

     For a list of possible status values that can be returned, see the next section.

How do you know this worked?
To verify that you've successfully migrated all of your Exchange 2013 public folders to
Exchange 2016 or Exchange 2019, do the following steps:

     Check the status of the move requests you created by running the following command in
     the Exchange Management Shell on an Exchange 2016 or Exchange 2019 Mailbox server:

       PowerShell

        Get-MoveRequest

     The command will return each move request you created along with one of the following
     status values:

        Completed: The public folder mailbox was successfully moved to the target mailbox
        database.

        CompletedWithWarning: The public folder mailbox was moved to the target mailbox
        database, but one or more issues were encountered during the move. You can find
        more information by viewing the move report that was delivered to the Administrator
        mailbox.

        CompletionInProgress: The public folder mailbox move to the target mailbox database
        is in its final stages. Public folders hosted in this mailbox may be unavailable for a brief
        period of time while the move is finalized.

        InProgress: The public folder mailbox move to the target mailbox database is
        underway. Public folders hosted in this mailbox are available during this portion of the
        move.

        Failed: The public folder mailbox move failed for one or more reasons. You can find
        more information by viewing the move report that was delivered to the Administrator
        mailbox.

        Queued: The public folder mailbox move has been submitted but the move hasn't
        started yet.

<!-- p.2068 -->

  Retry: The migration service is currently having trouble proceeding with the job, but it
  has not given up, and will continue trying.

  AutoSuspended: The public folder mailbox move is ready to enter its final stages but
  won't proceed further until you manually resume the move.

  This option can be helpful if you want to choose the time a move will complete. You
  can automatically suspend a move when you create it by using the
  SuspendWhenReadyToComplete switch on the New-MoveRequest cmdlet. To resume
  the move when you're ready, use the Resume-MoveRequest cmdlet.

  Suspended: The public folder mailbox move has been manually suspended by
  Suspend-MoveRequest cmdlet and won't proceed until you manually resume the
  move. To resume the move when you're ready, use the Resume-MoveRequest cmdlet.

View the location of your public folder mailboxes after their move request has completed
by running the following command on an Exchange 2016 or Exchange 2019 server:

  PowerShell

  Get-Mailbox -PublicFolder | Get-MailboxStatistics | Format-Table
  ServerName,DisplayName,TotalItemSize

In the list public folder mailboxes that are returned, verify that they've each been moved
to an Exchange 2016 Mailbox server.

<!-- p.2069 -->

Set up public folders in a new organization
Article • 04/30/2025

APPLIES TO:         2016   2019       Subscription Edition

Public folders in Exchange are based on a mailbox architecture that allows public folders to
benefit from things such as the resiliency of a Database Availability Group (DAG) and other
mailbox features.

For limits in on-premises Exchange Server, see Limits for public folders.

For additional management tasks related to public folders in Exchange Server, see Public folder
procedures.

What do you need to know before you begin?
      Estimated time to complete this task: 30 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Public folders" entry in the
      Sharing and collaboration permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Step 1: Create the primary public folder mailbox
The primary public folder mailbox contains a writeable copy of the public folder hierarchy plus
content and is the first public folder mailbox that you create for your organization. Subsequent
public folder mailboxes will be secondary public folder mailboxes, which will contain a read-
only copy of the hierarchy plus content.

For detailed steps, see Create a public folder mailbox.

Step 2: Create your first public folder

<!-- p.2070 -->

For detailed steps, see Create a public folder.

Step 3: Assign permissions to the public folder
After you create the public folder, you'll need to assign the Owner permissions level so that at
least one user can access the public folder from the client and create subfolders. Any public
folders created after this one will inherit the permissions of the parent public folder.

   1. In the Exchange admin center (EAC), navigate to Public folders > Public folders.

   2. In the list view, select the public folder.

   3. In the details pane, under Folder permissions, click Manage.

   4. In Public Folder Permissions, click Add       .

   5. Click Browse to select a user.

   6. In the Permission level list, select a level. At least one user should be an Owner.

   7. Click Save.

   8. You can add multiple users by clicking Add        and assigning the appropriate permissions
     using the steps above. You can also customize the permission level by selecting or
     clearing the check boxes. When you edit a predefined permission level such as Owner,
     the permission level will change to Custom.

For information about how to use the Exchange Management Shell to assign permissions to a
public folder, see Add-PublicFolderClientPermission.

Step 4 (Optional): Mail-enable the public folder
If you want users to send mail to the public folder, you can mail-enable the public folder. This
step is optional. If you don't mail-enable the public folder, users can post messages to the
public folder by dragging into it items from Outlook.

   1. In the EAC, navigate to Public folders > Public folders.

   2. In the list view, select the public folder you want to mail-enable.

   3. In the details pane, under Mail settings - Disabled, click Enable.

     A warning displays asking if you're sure you want to enable mail for the public folder.
     Click Yes.

<!-- p.2071 -->

The public folder will be mail-enabled and the name of the public folder will become the alias
of the public folder. If you have multiple recipients with that name, the public folder's alias will
be appended with a number. For example, if you have a distribution group named SalesTeam
and you create a public folder named SalesTeam and then mail-enable it, the alias of that
public folder will be SalesTeam1.

For information about how to use the Exchange Management Shell to mail-enable a public
folder, see Enable-MailPublicFolder.

<!-- p.2072 -->

Create a public folder mailbox in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Before you can create a public folder in Exchange server, you must first create a public folder
mailbox. Public folder mailboxes contain the hierarchy information as well as the content for
public folders.

The first public folder mailbox that you create in the organization is the primary hierarchy
mailbox, which contains the only writable copy of the public folder hierarchy. Any additional
public folder mailboxes that you create are secondary hierarchy mailboxes, which contain a
read-only copy of the public folder hierarchy. You can create multiple public folder mailboxes
for load balancing.

  ７ Note

  For more information about the storage quotas and limits for public folders in on-
  premises Exchange, see Limits for public folders.

For additional management tasks related to public folders in Exchange Server, see Public folder
procedures.

What do you need to know before you begin?
      Estimated time to complete: less than 5 minutes.

      Public folders on Exchange 2010 servers can't exist in the same organization with
      Exchange 2016 or later public folders. If you try to create a public folder mailbox when
      you still have legacy public folders, you'll receive the error An existing Public Folder
      deployment has been detected. To migrate existing Public Folder data, create new
      Public Folder mailbox using -HoldForMigration switch.

      Before you can create public folders in Exchange Server 2016 or later, you need to
      migrate your Exchange 2010 public folders by following the steps in Use batch migration
      to migrate public folders from Exchange 2010 to Exchange 2016.

      To move your public folder mailboxes from Exchange 2013 to Exchange 2016 or Exchange
      2019, see Migrate public folders from Exchange 2013 to Exchange 2016 or Exchange
      2019.

<!-- p.2073 -->

     For more information about the Exchange admin center, see Exchange admin center in
     Exchange Server. To learn how to open the Exchange Management Shell in your on-
     premises Exchange organization, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Public folders" entry in the
     Sharing and collaboration permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to create a public folder mailbox
   1. In the EAC, go to Public folders > Public folder mailboxes, and then click Add   .

   2. In the New public folder mailbox page that opens, enter the following information:

           Name: Enter the name for the public folder mailbox.

           Organizational unit: Click Browse to select the location in Active Directory where
           the mailbox object is created.

           Mailbox database: Click Browse to select the mailbox database where the mailbox is
           created.

     When you're finished, click Save.

Use the Exchange Management Shell to create a
public folder mailbox
To create a public folder mailbox, use the following syntax:

  PowerShell

  New-Mailbox -PublicFolder -Name <Name>

<!-- p.2074 -->

This example creates the primary hierarchy public folder mailbox named Master Hierarchy,
because this is the first public folder mailbox in the organization (the value of the Name
parameter doesn't determine whether the mailbox is the primary hierarchy public folder
mailbox).

  PowerShell

  New-Mailbox -PublicFolder -Name "Master Hierarchy"

This example creates a secondary hierarchy public folder mailbox named Istanbul, because this
isn't the first public folder mailbox in the organization (the value of the Name parameter
doesn't determine whether the mailbox is a secondary hierarchy public folder mailbox).

  PowerShell

  New-Mailbox -PublicFolder -Name Istanbul

For detailed syntax and parameter information, see New-Mailbox.

How do you know this worked?
To verify that you've successfully created a public folder mailbox, do any of these steps:

     In the EAC, go to Public folders > Public folder mailboxes and verify the public folder
     mailbox is listed. The primary hierarchy public folder mailbox has the value Primary
     Hierarchy for the Contains property. All other public folder mailboxes have the value
     Secondary Hierarchy for the Contains property.

     In the Exchange Management Shell, run the following command to verify the mailbox is
     listed, and check the value of the IsRootPublicFolderMailbox property to see if the
     mailbox is the primary hierarchy public folder mailbox ( True ) or a secondary hierarchy
     public folder mailbox ( False ):

        PowerShell

        Get-Mailbox -PublicFolder | Format-Table -Auto
        Name,ServerName,Database,IsRootPublicFolderMailbox

     In the Exchange Management Shell, run the following commands to verify the primary
     hierarchy public folder mailbox:

        1. Run the following command:

<!-- p.2075 -->

    PowerShell

    Get-OrganizationConfig | Format-List RootPublicFolderMailbox

2. Use the GUID value returned by the first command with Get-Mailbox to confirm the
  mailbox name. You can copy the GUID value by right-clicking in the Exchange
  Management Shell window, selecting Mark, highlighting the GUID value, and then
  pressing ENTER.

    PowerShell

    Get-Mailbox -PublicFolder -Identity <GUID>

<!-- p.2076 -->

Create a public folder
07/22/2025

APPLIES TO:       2016      2019      Subscription Edition

Public folders are designed for shared access and provide an easy and effective way to collect,
organize, and share information with other people in your workgroup or organization.

By default, a public folder inherits the settings of its parent folder, including the permissions
settings.

For additional management tasks related to public folders, see Public folder procedures.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Public folders" entry in the
      Sharing and collaboration permissionstopic.

      You can't create a public folder unless you've first created a public folder mailbox. For
      more information about how to create a public folder mailbox, see Create a public folder
      mailbox.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to create a public folder
When using the EAC to create a public folder, you'll only be able to set the name and the path
of the public folder. To configure additional settings, you'll need to edit the public folder after
it's created.

   1. Navigate to Public folders > Public folders.

<!-- p.2077 -->

   2. If you want to create this public folder as a child of an existing public folder, click the
     existing public folder in the list view. If you want to create a top-level public folder, skip
     this step.

   3. Click Add     .

   4. In Public Folder, type the name of the public folder.

        ） Important

        Don't use a backslash () in the name when creating a public folder.

   5. In the Path box, verify the path to the public folder. If this isn't the desired path, click
     Cancel and follow Step 2 of this procedure.

   6. Click Save.

Use the Exchange Management Shell to create a
public folder
This example creates a public folder named Reports in the path Marketing\2016.

  PowerShell

  New-PublicFolder -Name Reports -Path \Marketing\2016

  ） Important

  Don't use a backslash () in the name when creating a public folder.

For detailed syntax and parameter information, see New-PublicFolder.

How do you know this worked?
To verify that you've successfully created a public folder, do the following:

     In the EAC, click Refresh to refresh the list of public folders. Your new public folder should
     be displayed in the list.

     In the Exchange Management Shell, run any of the following commands:

<!-- p.2078 -->

PowerShell

Get-PublicFolder -Identity \Marketing\2016\Reports | Format-List

PowerShell

Get-PublicFolder -Identity \Marketing\2016 -GetChildren

PowerShell

Get-PublicFolder -Recurse

<!-- p.2079 -->

Mail-enable or mail-disable a public folder
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Public folders are designed for shared access and provide an easy and effective way to collect,
organize, and share information with other people in your workgroup or organization. Mail-
enabling a public folder allows users to post to the public folder by sending an email message
to it. When a public folder is mail-enabled additional settings become available for the public
folder in the Exchange admin center (EAC), such as email addresses and mail quotas. In the
Exchange Management Shell, before a public folder is mail-enabled, you use the Set-
PublicFolder cmdlet to manage all of its settings. After the public folder is mail-enabled, you
use the Set-PublicFolder and the Set-MailPublicFolder cmdlets to manage the settings.

If you want users on the Internet to send mail to a mail-enabled public folder, you need to set
addition permissions using the Add-PublicFolderClientPermission cmdlet.

For additional management tasks related to managing public folders, see Public folder
procedures.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      To ensure that users on the Internet can send e-mail messages to a mail-enabled public
      folder, the public folder needs to have at least the CreateItems access right granted to the
      Anonymous account. If you want to learn how to do this, see Allow anonymous users to
      send email to a mail-enabled public folder later in this article.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Public folders" entry in the
      Sharing and collaboration permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

<!-- p.2080 -->

Use the EAC to mail-enable or mail-disable a public
folder
   1. Navigate to Public folders > Public folders.

   2. In the list view, select the public folder that you want to mail-enable or mail-disable.

   3. In the details pane, under Mail settings, click Enable or Disable.

   4. A warning box displays asking if you're sure you want to enable or disable email for the
     public folder. Click Yes to continue.

If you want external users to send mail to this public folder, make sure you follow the steps in
Allow anonymous users to send email to a mail-enabled public folder.

Use the Exchange Management Shell to mail-
enable a public folder
This example mail-enables the public folder Help Desk.

  PowerShell

  Enable-MailPublicFolder -Identity "\Help Desk"

This example mail-enables the public folder Reports under the Marketing public folder, but
hides the folder from address lists.

  PowerShell

  Enable-MailPublicFolder -Identity "\Marketing\Reports" -
  HiddenFromAddressListsEnabled $True

If you want external users to send mail to this public folder, make sure you follow the steps in
Allow anonymous users to send email to a mail-enabled public folder.

For detailed syntax and parameter information, see Enable-MailPublicFolder.

Use the Exchange Management Shell to mail-
disable a public folder
This example mail-disables the public folder Marketing\Reports.
