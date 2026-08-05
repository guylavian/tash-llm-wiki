---
title: "Exchange Server — pages 2841-2880"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2841-2880
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2841-2880
family: exchange
documentKind: "doc"
abstract: "restored, the data files can then be moved into a recovery database, manually moved back to their original location, or mounted somewhere else in the Exchange organization using database portability. When you restore a database to an alternate location, the restored database is"
---

# Exchange Server — pages 2841-2880

<!-- p.2841 -->

           restored, the data files can then be moved into a recovery database, manually
           moved back to their original location, or mounted somewhere else in the Exchange
           organization using database portability. When you restore a database to an
           alternate location, the restored database is in a dirty shutdown state. After the
           restore process is complete, you need to manually put the database into a clean
           shutdown state using Eseutil.exe.

   9. On the Confirmation page, review the recovery settings, and then select Recover.

 10. On the Recovery Progress page, you can view the status and progress of the recovery
     operation.

 11. Select Close when the recovery operation is complete.

How do you know you successfully restore a
backup of Exchange using Windows Server
Backup?
The Recovery Progress page indicates whether or not the recovery process completed
successfully. To further verify you successfully restored the data, do any of the following steps:

     Examine the target directory of the backup and verify the restored data exists.
     On the server where you ran Windows Server Backup, verify the job completed
     successfully by viewing the backup logs.
     Open Event Viewer and verify a restore completion event was logged in the Application
     event log.

<!-- p.2842 -->

Recover Exchange servers
ﾃ   Summarize this article for me

APPLIES TO:         2016            2019   Subscription Edition

You can recover a lost Exchange server by using the /Mode:RecoverServer switch in unattended
mode (from the command line) of Exchange Setup. Since most Exchange server settings are
stored in Active Directory, the Setup.exe /Mode:RecoverServer command uses that information
during the installation of Exchange on a new server with the same name.

Recovering a lost Exchange server is often accomplished by using new hardware. However, you
can also use an existing server that doesn't already have Exchange installed on it.

This topic shows you how to recover a lost Exchange server that isn't a member of a database
availability group (DAG). For detailed steps about how to recover a server that was a member
of a DAG, see Recover a database availability group member server.

Looking for other management tasks related to backing up and restoring data? Check out
Backup, restore, and disaster recovery.

What do you need to know before you begin?
     Estimated time to complete: 20 minutes

     The account that you'll use to do the server recovery requires the following permissions:

        Domain Admins security group membership.

        Exchange Organization Management role group membership.

     If Exchange is installed in a location other than the default location of
     %ProgramFiles%\Microsoft\Exchange Server\V15, you must include the /TargetDir:<Path>
     switch in the Setup.exe /Mode:RecoverServer command to specify the location of the
     Exchange program (binary) files. If you don't use the /TargetDir switch, the Exchange files
     will be installed in the default location when you recover the Exchange server.

     To find the install location of Exchange on the lost Exchange server, do the following
     steps:

        1. Open ADSIEDIT.MSC or LDP.EXE.

        2. Go to CN=ExServerName,CN=Servers,CN=First Administrative
            Group,CN=Administrative Groups,CN=ExOrg Name,CN=Microsoft
            Exchange,CN=Services,CN=Configuration,DC=DomainName,CN=Com

<!-- p.2843 -->

      3. Right-click the Exchange server object, and then click Properties.

      4. Find the msExchInstallPath attribute. This attribute stores the current installation
         path.

   If you do not have the installation media for the Cumulative Update (CU) version that was
   installed on the server being recovered, you can use the latest available CU. Once the
   recovery is successful, the AdminDisplayVersion and msExchVersion attribute for the
   recovered server will show the build number of older CU but this is only cosmetic. You
   can either run Setup in Upgrade mode using the latest CU, or wait for and upgrade to the
   next CU release, which will correct this.

   The target server must use the same version of Windows Server as the lost server. For
   example, you can't recover a lost Exchange 2016 server that was running Windows 2012
   R2 on a new server that's running Windows 2016, or vice-versa.

   The same disk drive letters that were used for mounted databases on the lost server must
   also exist on the target server.

   The target server should have the same general performance characteristics and hardware
   configuration as the lost server.

   The /Mode:RecoverServer switch assigns a self-signed certificate to all Exchange Services
   that require SSL/TLS. If the server previously used an SSL/TLS certificate that was issued
   by a different certification authority, you'll need to re-import the certificate and configure
   the services to use the certificate. Otherwise, users will get a certificate prompt when they
   try to connect (for example, in Outlook).

  Tip

 Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
 Server | Management.

Recover a Lost Exchange Server
 1. Reset the computer account for the lost server. For detailed steps, see Reset a Computer
   Account.

 2. Install the proper operating system and name the new server with the same name as the
   lost server. Recovery won't succeed if the target Windows server doesn't have the same
   name as the lost Exchange server.

 3. Join the server to the same domain as the lost server.

<!-- p.2844 -->

4. Install the necessary prerequisites and operating system components on the target server.
  For details, see Exchange Server system requirements.

5. On the target server, open File Explorer, right-click on the Exchange ISO image file that
  you downloaded, and then select Mount. Note the virtual DVD drive letter that's
  assigned.

6. Open a Windows Command Prompt window. For example:

       Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then press
       OK.

       Press Start. In the Search box, type Command Prompt, then in the list of results,
       select Command Prompt.

7. In the Command Prompt window, use the following syntax:

    ７ Note

          The previous /IAcceptExchangeServerLicenseTerms switch will not work starting
          with the Exchange Server 2016 and Exchange Server 2019 September 2021
          Cumulative Updates (CUs). You now must use either
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and
          scripted installs.

          The examples below use the
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you to
          change the switch to /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

    Console

    <Virtual DVD drive letter>:\Setup.exe
    /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:RecoverServer
    [/TargetDir:<Path>] [/DomainController:<ServerNameOrFQDN>]
    [/DoNotStartTransport] [/EnableErrorReporting]

  This example uses the Exchange installation files on drive E: to install Exchange in the
  default location (%ProgramFiles%\Microsoft\Exchange Server\V15) and recover the
  Exchange server.

    PowerShell

<!-- p.2845 -->

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
       /Mode:RecoverServer

     This is the same example, but a custom location for the Exchange program files is
     required to match the location on the lost server.

       PowerShell

       E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
       /Mode:RecoverServer /TargetDir:"D:\Program Files\Exchange"

     For more information about the optional switches, see Use unattended mode in Exchange
     Setup.

   8. After Setup has completed, but before you put the recovered server into production,
     reconfigure any custom settings that were previously present on the server, and then
     restart the server.

How do you know this worked?
The successful completion of Setup will be the primary indicator that the recovery was
successful. To further verify that you've successfully recovered a lost server, open the Windows
Services tool (services.msc) and verify that the Microsoft Exchange services have been installed
and are running.

Possible issues with the Scripting Agent
If you previously enabled the Scripting Agent in your Exchange organization, the recovery
process might fail. The error will look like this:

  Console

  "Initialization failed: '"Scripting Agent initialization failed: "File is not
  found: 'C:\Program Files\Microsoft\Exchange
  Server\V15\Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml'.""' --->
  Microsoft.Exchange.Provisioning.ProvisioningException: "Scripting Agent
  initialization failed: "File is not found: 'C:\Program Files\Microsoft\Exchange
  Server\V15\Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml'."" --->
  System.IO.FileNotFoundException: "File is not found: 'C:\Program
  Files\Microsoft\Exchange
  Server\V15\Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml'."

If you have other Exchange servers in your organization, you'll need to:

<!-- p.2846 -->

      1. Disable the Scripting Agent in the Exchange Management Shell on an existing server:

          PowerShell

          Disable-CmdletExtensionAgent -Identity "Scripting Agent"

      2. Run Exchange Setup in recovery mode as described earlier in this topic.

      3. Enable the Scripting Agent in the Exchange Management Shell after the Exchange server
        recovery is complete:

          PowerShell

          Enable-CmdletExtensionAgent -Identity "Scripting Agent"

If the recovered Exchange server is the only Exchange server in your organization, you'll need
to:

      1. Rename the file
        %ExchangeInstallPath%Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml.sample to
        %ExchangeInstallPath%Bin\CmdletExtensionAgents\ScriptingAgentConfig.xml.

        The default value of %ExchangeInstallationPath% is %ProgramFiles%\Microsoft\Exchange
        Server\V15, but the actual value is wherever you installed Exchange on the server.

      2. Re-run Exchange Setup in recovery mode as described earlier in this topic.

 Last updated on 02/13/2026

<!-- p.2847 -->

Recover a database availability group
member server in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

If a Mailbox server that's a member of a database availability group (DAG) is lost or fails, and is
unrecoverable and needs replacement, you can run a server recovery operation.

Microsoft Exchange Server Setup includes the switch /m:RecoverServer that can be used to run
the server recovery operation. Running Setup with the /m:RecoverServer switch causes Setup to
read the server's configuration information from Active Directory for a server with the same
name as the server from which you're running Setup.

After the server's configuration information is gathered from Active Directory, the original
Exchange files and services are then installed on the server, and the roles and settings that
were stored in Active Directory are then applied to the server.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
      Estimated time to complete: 30 minutes

      You need to be assigned permissions before you can do this procedure or procedures. To
      see what permissions you need, see the "Mailbox database copies" entry in the High
      availability and site resilience permissions topic.

      If Exchange is installed in a location other than the default location, you must use the
      /TargetDir Setup switch to specify the location of the Exchange program files. If you don't
      use the /TargetDir switch, the Exchange program files will be installed in the default
      location (%programfiles%\Microsoft\Exchange Server\V15).

      To determine the install location, follow these steps:

          1. Open ADSIEDIT.MSC or LDP.EXE.

          2. Navigate to the following location: CN=ExServerName,CN=Servers,CN=First
            Administrative Group,CN=Administrative Groups,CN=ExOrg Name,CN=Microsoft
            Exchange,CN=Services,CN=Configuration,DC=DomainName,CN=Com

          3. Right-click the Exchange server object, and then click Properties.

<!-- p.2848 -->

      4. Locate the msExchInstallPath attribute. This attribute stores the current installation
         path.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

Use Setup /m:RecoverServer to recover a server
 1. Retrieve any replay lag or truncation lag settings for any mailbox database copies that
   exist on the server being recovered by using the Get-MailboxDatabase cmdlet:

      PowerShell

      Get-MailboxDatabase DB1 | Format-List *lag*

 2. Remove any mailbox database copies that exist on the server being recovered by using
   the Remove-MailboxDatabaseCopy cmdlet:

      PowerShell

      Remove-MailboxDatabaseCopy DB1\MBX1

 3. Remove the failed server's configuration from the DAG by using the Remove-
   DatabaseAvailabilityGroupServer cmdlet:

      PowerShell

      Remove-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX1

      ７ Note

      If the DAG member being removed is offline and can't be brought online, you must
      add the -ConfigurationOnly parameter to the preceding command. If you use the -
      ConfigurationOnly switch, you must also manually evict the node from the cluster.

<!-- p.2849 -->

4. Reset the server's computer account in Active Directory. For detailed steps, see Reset a
  Computer Account.

5. Open a Command Prompt window. Using the original Setup media, run the following
  command:

    ７ Note

          Starting with the Exchange Server 2016 and Exchange Server 2019 September
          2021 Cumulative Updates (CUs) you now must use either
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

          Next example below use the
          /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you to
          change the switch to /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

    Console

     Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
     /m:RecoverServer

6. When the Setup recovery process is complete, add the recovered server to the DAG by
  using the Add-DatabaseAvailabilityGroupServer cmdlet:

    PowerShell

     Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX1

7. After the server has been added back to the DAG, you can reconfigure mailbox database
  copies by using the Add-MailboxDatabaseCopy cmdlet. If any of the database copies
  being added previously had replay lag or truncation lag times greater than 0, you can use
  the ReplayLagTime and TruncationLagTime parameters of the Add-MailboxDatabaseCopy
  cmdlet to reconfigure those settings:

    PowerShell

     Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX1
     Add-MailboxDatabaseCopy -Identity DB2 -MailboxServer MBX1 -ReplayLagTime
     3.00:00:00
     Add-MailboxDatabaseCopy -Identity DB3 -MailboxServer MBX1 -ReplayLagTime
     3.00:00:00 -TruncationLagTime 3.00:00:00

<!-- p.2850 -->

  ７ Note

  You will need to reconfigure the Virtual Directories on the recovered server and re-create
  any customizations you might have made. You might also need to perform additional
  recovery steps depending on your configuration. See Deploy the ASA credential to
  another Exchange server running Client Access services.

  You need to import the AD FS signing certificate. See Step 1: Review the certificate
  requirements for AD FS.

How do you know this fix worked?
To verify that you've successfully recovered the DAG member, use the following method:

     In the Exchange Management Shell, run the following command to verify the health and
     status of the recovered DAG member.

       PowerShell

       Test-ReplicationHealth <ServerName>

       PowerShell

       Get-MailboxDatabaseCopyStatus -Server <ServerName>

     All of the replication health tests should pass successfully, and the status of databases
     and their content indexes should be healthy.

<!-- p.2851 -->

Recovery databases in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019   Subscription Edition

A recovery database (RDB) is a special kind of mailbox database that allows you to mount a
restored mailbox database and extract data from the restored database as part of a recovery
operation. You can use the New-MailboxRestoreRequest cmdlet to extract data from an RDB.
After extraction, the data can be exported to a folder or merged into an existing mailbox. RDBs
enable you to recover data from a backup or copy of a database without disturbing user access
to current data.

Microsoft Exchange Server supports the ability to restore data directly to a recovery database.
Mounting the recovered data as a recovery database allows the administrator to restore
individual mailboxes or individual items in a mailbox. Restoring to a recovery database can be
accomplished in two ways:

      If a recovery database already exists, the application can dismount the database, restore
      the data onto the recovery database and log files, and then remount the database.

      The database and log files can be restored to any disk location. Exchange analyzes the
      restored data and replays the transaction logs to bring the databases up to date, and
      then a recovery database can be configured to point to already recovered database files.

Difference between a mailbox database and a
recovery database
RDBs are different from standard mailbox databases in several respects:

      An RDB is created by using the Exchange Management Shell.

      Mail can't be sent to or from an RDB. All client protocol access to an RDB (including
      SMTP, POP3, and IMAP4) is blocked. This design prevents using an RDB to insert mail into
      or remove mail from the messaging system.

      Client MAPI access using Microsoft Outlook or Outlook on the web is blocked. MAPI
      access is supported for an RDB, but only by recovery tools and applications. Both the
      mailbox GUID and the database GUID must be specified when using MAPI to log into a
      mailbox in an RDB.

      Mailboxes in an RDB can't be connected to user accounts. To allow a user to access the
      data in a mailbox in an RDB, the mailbox must be merged into an existing mailbox, or
      exported to a folder.

<!-- p.2852 -->

       System and mailbox management policies aren't applied. This design prevents items in an
       RDB from being deleted by the system during the recovery process.

       Online maintenance isn't performed for RDBs.

       Circular logging can't be enabled for RDBs.

       Only one RDB can be mounted at any time on a Mailbox server. The use of an RDB
       doesn't count against the database limit per Mailbox server.

       You can't create mailbox database copies of an RDB.

       An RDB can be used as a target for restore operations, but not backup operations.

       A recovered database mounted as an RDB isn't tied to the original mailbox in any way.

Using a recovery database
Before you can use an RDB, there are certain requirements that must be met. An RDB can be
used for Exchange 2016 and later mailbox databases only. Mailbox databases from previous
versions of Exchange aren't supported. In addition, the target mailbox used for data merges
and extraction must be in the same Active Directory forest as the database mounted in the
RDB.

An RDB can be used to recover data in several situations, such as:

       Same server dial tone recovery: You can perform a recovery from an RDB after the
       original database has been restored from backup, as part of a dial tone recovery
       operation.

       Alternate server dial tone recovery: You can use an alternate server to host the dial tone
       database, and then later recover data from an RDB after the original database has been
       restored from backup.

       Mailbox recovery: You can recover an individual mailbox from backup when the deleted
       mailbox retention period has elapsed. You then extract data from the restored mailbox
       and copy it to a target folder or merge it with another mailbox.

       Specific item recovery: You can restore from backup data that has been deleted or
       purged from a mailbox.

  ７ Note

<!-- p.2853 -->

  Folder access control lists (ACLs) aren't preserved when recovering content into an active
  mailbox. Because the recovery process typically involves recovering mailbox data and
  merging the content back into the original database, there should be no need to recover
  or copy ACLs.

An RDB is designed for mailbox database recovery under the following conditions and
scenarios:

     The logical information about the original database and the mailboxes in that database
     remains intact and unchanged in Active Directory.

     You need to recover a single mailbox or a single database. Recovery scenarios include:

        Recovering or repairing a database while a dial tone database is in use, with the goal of
        merging the two databases.

        Recovering a database on a server other than the original server for that database. If
        needed, you can then merge the recovered data back to the original server.

        Recovering deleted items that users previously deleted from their mailbox, after the
        deleted item retention period has expired.

RDBs are generally not designed for scenarios in which you have to restore entire servers, when
you have to restore multiple databases, or when you're in an emergency situation that requires
changing or rebuilding your Active Directory topology.

For detailed steps about how to create an RDB, see Create a recovery database. For detailed
steps about how to use an RDB, see Restore data using a recovery database.

<!-- p.2854 -->

Create a recovery database in Exchange
Server
07/23/2025

APPLIES TO:      2016     2019      Subscription Edition

You can use the Exchange Management Shell to create a recovery database, a special kind of
mailbox database that's used to mount and extract data from the restored database as part of
a recovery operation. After you create a recovery database, you can move a recovered or
restored mailbox database into the recovery database, and then use the New-
MailboxRestoreRequest cmdlet to extract data from the recovered database. After extraction,
the data can then be exported to a folder or merged into an existing mailbox. Using recovery
databases, you can recover data from a backup or copy of a database without disrupting user
access to current data.

Looking for other management tasks related to recovery databases? Check out Recovery
databases.

What do you need to know before you begin?
     Estimated time to complete this task: 1 minute

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
     Recipients Permissionstopic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to create a
recovery database
This example creates the recovery database RDB1 on the Mailbox server MBX2.

<!-- p.2855 -->

  PowerShell

  New-MailboxDatabase -Recovery -Name RDB1 -Server MBX2

This example creates the recovery database RDB2 on the Mailbox server MBX1 using a custom
path for the database file and log folder.

  PowerShell

  New-MailboxDatabase -Recovery -Name RDB2 -Server MBX1 -EdbFilePath
  "C:\Recovery\RDB2\RDB2.EDB" -LogFolderPath "C:\Recovery\RDB2"

For detailed syntax and parameter information, see New-MailboxDatabase.

How do you know this worked?
To verify that you've successfully created a recovery database, do the following:

     In the Exchange Management Shell, run the following command to display configuration
     information for the recovery database.

        PowerShell

        Get-MailboxDatabase <RecoveryDatabaseName> | Format-List

Other Tasks
After you create a recovery database, you may also want to restore data using a recovery
database. For detailed steps, see Restore data using a recovery database.

<!-- p.2856 -->

Restore data using a recovery database in
Exchange Server
Article • 04/30/2025

APPLIES TO:         2016      2019      Subscription Edition

A recovery database (RDB) is a special kind of mailbox database that allows you to mount and
extract data from a restored mailbox database as part of a recovery operation. RDBs allow you
to recover data from a backup or copy of a database without disrupting user access to current
data.

After you create an RDB, you can restore a mailbox database into the RDB by using a backup
application or by copying a database and its log files into the RDB folder structure. Then you
can use the New-MailboxRestoreRequest cmdlet to extract data from the recovered database.
Once extracted, the data can then be exported to a folder or merged into an existing mailbox.

For additional management tasks related to RDBs, see Recovery databases.

What do you need to know before you begin?
        Estimated time to complete this task: 1 minute, plus the time it takes to put the database
        into a clean shutdown state and to extract the data.

        You need to be assigned permissions before you can perform this procedure or
        procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
        Recipients Permissions topic.

        Some backup applications have the ability to restore Exchange data directly to a recovery
        database. Windows Server Backup can restore only file-level backups to a recovery
        database. It cannot be used to restore application-level backups to a recovery database.

        The database and log files containing the recovered data must be restored or copied into
        the RDB folder structure.

        The database must be in a clean shutdown state. Because an RDB is an alternate restore
        location for all databases, all restored databases will be in a dirty shutdown state. You
        must use Eseutil /R to put restored databases into a clean shutdown state.

Use the Exchange Management Shell to recover
data using a recovery database

<!-- p.2857 -->

1. Copy a recovered database and its log files, or restore a database and it log files, to the
  location you will use for your recovery database.

2. Use Eseutil to bring that database into a clean shutdown state. In the following example,
  EXX is the log generation prefix for the database (for example, E00, E01, E02, and so on).

    PowerShell

     Eseutil /R EXX /l <RDBLogFilePath> /d <RDBEdbFolder>

  The following example illustrates a log generation prefix of E01 and a recovery database
  and log file path of E:\Databases\RDB1:

    PowerShell

     Eseutil /R E01 /l E:\Databases\RDB1 /d E:\Databases\RDB1

3. Create a recovery database. Give the recovery database a unique name, but use the name
  and path of the database file for the EdbFilePath parameter, and the location of the
  recovered log files for the LogFolderPath parameter.

    PowerShell

     New-MailboxDatabase -Recovery -Name <RDBName> -Server <ServerName> -
     EdbFilePath <RDBPathandFileName> -LogFolderPath <LogFilePath>

  The following example illustrates creating a recovery database that will be used to recover
  DB1.edb and its log files, which are located at E:\Databases\RDB1.

    PowerShell

     New-MailboxDatabase -Recovery -Name <RDBName> -Server <ServerName> -
     EdbFilePath "E:\Databases\RDB1\DB1.EDB" -LogFolderPath "E:\Databases\RDB1"

4. Restart the Microsoft Exchange Information Store service:

    PowerShell

     Restart-Service MSExchangeIS

5. Mount the recovery database:

    PowerShell

<!-- p.2858 -->

      Mount-database <RDBName>

 6. Verify that the mounted database contains the mailbox(es) you want to restore:

     PowerShell

      Get-MailboxStatistics -Database <RDBName> | Format-Table
      DisplayName,MailboxGUID -AutoSize

 7. Use the New-MailboxRestoreRequest cmdlet to restore a mailbox or items from the
   recovery database to a production mailbox.

   The following example restores the source mailbox that has the MailboxGUID 1d20855f-
   fd54-4681-98e6-e249f7326ddd on mailbox database DB1 to the target mailbox with the
   alias Morris.

     PowerShell

      New-MailboxRestoreRequest -SourceDatabase DB1 -SourceStoreMailbox 1d20855f-
      fd54-4681-98e6-e249f7326ddd -TargetMailbox Morris

   The following example restores the content of the source mailbox that has the display
   name Morris Cornejo on mailbox database DB1 to the archive mailbox for
   Morris@contoso.com.

     PowerShell

      New-MaiboxRestoreRequest -SourceDatabase DB1 -SourceStoreMailbox "Morris
      Cornejo" -TargetMailbox Morris@contoso.com -TargetIsArchive

 8. Periodically check the status of the Mailbox restore request using Get-
   MailboxRestoreRequest.

   Once the restore has a status of Completed, remove the restore request using Remove-
   MailboxRestoreRequest. For example:

     PowerShell

      Get-MailboxRestoreRequest -Status Completed | Remove-MailboxRestoreRequest

How do you know this worked?

<!-- p.2859 -->

To verify that you have successfully recovered the mailbox data, open the target mailbox using
Outlook or Outlook Web App and verify that the recovered data is present.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online     , or Exchange Online Protection .

<!-- p.2860 -->

Move a mailbox database using database
portability in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016       2019       Subscription Edition

Database portability can help reduce overall recovery times for some failure scenarios. By using
database portability, reliability is improved by removing several error-prone, manual steps from
the recovery processes. Note that Mailbox databases from previous versions of Exchange can't
be moved to a Mailbox server running Exchange 2016 or Exchange 2019.

  ７ Note

  When using database portability to recover a mailbox database, the operating system
  version and the Exchange Server version on the source and target Exchange servers must
  be the same. For example, if an Exchange 2016 mailbox database was previously mounted
  on a server running Windows Server 2016, database portability will only work when
  migrating the database to a server also running Windows Server 2016 and Exchange 2016.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes, plus the time it takes to restore the data, move
      the database files, and wait for Active Directory replication to complete.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
      Recipients Permissions topic.

      You can't use the EAC to move user mailboxes to a recovered or dial tone database using
      database portability.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online           , or Exchange Online Protection .

Use the Exchange Management Shell to move user
mailboxes to a recovered or dial tone database

<!-- p.2861 -->

using database portability
 1. Verify that the database to be moved is in a clean shutdown state. If the database isn't in
   a clean shutdown state, perform a soft recovery.

     ７ Note

     When you perform a soft recovery, any uncommitted log files are committed to the
     database. If you don't have all of the required log files, you can't complete the soft
     recovery process. Proceed to step 2.

   To commit all uncommitted log files to the database, from a command prompt, run the
   following command.

     PowerShell

      ESEUTIL /R <Enn>

     ７ Note

     <E nn> specifies the log file prefix for the database into which you intend to replay
     the log files. The log file prefix specified by <E nn> is a required parameter for
     Eseutil /r.

 2. Create a database on a server using the following syntax:

     PowerShell

      New-MailboxDatabase -Name <DatabaseName> -Server <ServerName> -EdbFilePath
      <DatabaseFileNameandPath> -LogFolderPath <LogFilesPath>

 3. Set the This database can be over written by restore attribute using the following syntax:

     PowerShell

      Set-MailboxDatabase <DatabaseName> -AllowFileRestore $true

 4. Move the original database files (.edb file, log files, and Exchange Search catalog) to the
   database folder you specified when you created the new database above.

 5. Mount the database using the following syntax:

<!-- p.2862 -->

       PowerShell

        Mount-Database <DatabaseName>

   6. After the database is mounted, modify the user account settings with the Set-Mailbox
     cmdlet so that the account points to the mailbox on the new mailbox server. To move all
     of the users from the old database to the new database, use the following syntax.

       PowerShell

        Get-Mailbox -Database <SourceDatabase> |where {$_.ObjectClass -NotMatch
        '(SystemAttendantMailbox|ExOleDbSystemMailbox)'}| Set-Mailbox -Database
        <TargetDatabase>

   7. Trigger delivery of any messages remaining in queues using the following syntax.

       PowerShell

        Get-Queue <QueueName> | Retry-Queue -Resubmit $true

After Active Directory replication is complete, all users can access their mailboxes on the new
Exchange server. Most clients are redirected via Autodiscover. Outlook on the web users are
also automatically redirected.

How do you know this worked?
To verify that you've successfully moved a mailbox, do the following:

     Open the mailbox using Outlook on the web.

     Open the mailbox using Microsoft Outlook.

<!-- p.2863 -->

Dial tone portability in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Dial tone portability is a feature of Exchange Server 2016 and Exchange Server 2019 that
provides a limited business continuity solution for failures that affect a mailbox database, a
server, or an entire site. A temporary mailbox maintains users' ability to send email, and this
mailbox can be on the same Exchange Mailbox server or on any other Exchange Mailbox server
in your organization, provided they contain databases with the same database schema version.
This allows an alternative server to host the mailboxes of users who were previously on a server
that is no longer available. Clients that support Autodiscover are automatically redirected to
the new server without having to manually update the user's desktop profile. After the user's
original mailbox data has been restored, an administrator can merge a user's recovered
mailbox and the user's dial tone mailbox into a single, up-to-date mailbox.

The process for using dial tone portability is called a dial tone recovery. A dial tone recovery
involves creating an empty database on a Mailbox server to replace a failed database. This
empty database, referred to as a dial tone database, allows users to send and receive email
messages while the failed database is recovered.

There are three options for performing a dial tone recovery:

      Dial tone recovery on the server with the failed database: If the server hosting the failed
      database is still functional, we recommend that you perform a dial tone recovery on that
      server. This means less downtime because you don't need to move database files
      between servers. In addition, you won't need to reconfigure messaging profiles for clients
      that don't support Autodiscover.

      Dial tone recovery using an alternate server for the dial tone database: If a server fails
      and needs to be rebuilt, the most efficient way to give users basic mail functionality is to
      create a dial tone database on another server, and use database portability to move the
      users' mailbox configuration to that new server. Because this process involves moving the
      dial tone database back to the original (recovered) server, this option adds more time to
      the overall recovery process. In addition, this process is more complex than performing a
      dial tone recovery on the original server. When performing this process, the server
      hosting the dial tone database must have sufficient resources to support the added load
      of the additional users. In addition, if the users' client doesn't support Autodiscover, their
      messaging profile will need to be reconfigured to point to the dial tone server.

      Dial tone recovery using and staying on an alternate server for the dial tone database:
      This is similar to the preceding option, except that you don't revert back to the original
      server. We recommend this option for situations in which it isn't possible or feasible to

<!-- p.2864 -->

     recover the failed server. In this scenario, users typically remain on an alternate server
     after the recovery operation has completed. When performing this process, the server
     hosting the dial tone database must have sufficient resources to support the added load
     of the additional users. In addition, if the users' client doesn't support Autodiscover, their
     messaging profile will need to be reconfigured to point to the dial tone server.

All three options follow the same basic steps:

   1. Create an empty dial tone database to replace the failed database.

     This new database will allow users who had mailboxes on the failed database to send and
     receive new messages. Dial tone portability allows you to point a user to a different
     database without moving the mailbox. If you created the dial tone database on a different
     server than the server that housed the failed database, you need to move the mailbox
     configuration to that new server.

   2. Restore the old database.

     Use the backup and recovery software you typically use to restore the failed database. If
     there is no backup of the failed database, recover the failed database using other means
     if possible. If you're using the same server for dial tone recovery, you need to restore the
     database to a recovery database (RDB).

   3. Swap the dial tone database with the restored database.

     After the failed database is restored, swap it with the dial tone database. This gives the
     users the ability to send and receive email and access all the data in the restored
     database. If users were moved to a dial tone database on another server, you need to
     move the mailbox configuration back to the original server.

   4. Merge the databases.

     To get the data from the dial tone database into the restored database, you merge the
     data using the New-MailboxRestoreRequest cmdlet.

For detailed steps about how to perform a dial tone recovery, see Perform a dial tone recovery.

<!-- p.2865 -->

Perform dial tone recovery in Exchange
Server
07/23/2025

APPLIES TO:       2016       2019      Subscription Edition

The process for using dial tone portability is known as a dial tone recovery, which involves
creating an empty database on a Mailbox server to replace a failed database. To learn more,
see Dial tone portability.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes, plus the time it takes to restore and move the
     data.

     Your organization needs to have less than the maximum number of allowed databases to
     create a new dial tone database:
        Exchange Standard Edition: The maximum is five databases per server.
        Exchange Enterprise Edition: This maximum is 100 databases per server.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Mailbox recovery" entry in the
     Recipients Permissions article.

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to perform a
dial tone recovery on a single server

  ７ Note

<!-- p.2866 -->

You can't use the Exchange admin center (EAC) to perform a dial tone recovery on a single
server.

1. Make sure that any existing files for the database being recovered are preserved in case
   they're needed later for further recovery operations.

2. Use the New-MailboxDatabase cmdlet to create a dial tone database, as shown in this
   example.

     PowerShell

     New-MailboxDatabase -Name DTDB1 -EdbFilePath D:\DialTone\DTDB1.EDB

3. Use the Set-Mailbox cmdlet to rehome the user mailboxes hosted on the database being
   recovered, as shown in this example.

     PowerShell

     Get-Mailbox -Database DB1 | Set-Mailbox -Database DTDB1

4. Use the Mount-Database cmdlet to mount the database so client computers can access
   the database and send and receive messages, as shown in this example.

     PowerShell

     Mount-Database -Identity DTDB1

5. Create a recovery database (RDB) and restore or copy the database and log files
   containing the data you want to recover into the RDB. For detailed steps, see Create a
   recovery database.

6. After the data is copied to the RDB, but before mounting the restored database, copy any
   log files from the failed database to the RDB log folder to play against the restored
   database.

7. Mount the RDB, and then use the Dismount-Database cmdlet to dismount it, as shown in
   this example.

     PowerShell

     Mount-Database -Identity RDB1
     Dismount-Database -Identity RDB1

<!-- p.2867 -->

 8. After the RDB is dismounted, move the current database and log files within the RDB
   folder to a safe location. This step prepares for swapping the recovered database with the
   dial tone database.

 9. Dismount the dial tone database, as shown in this example. Users experience an
   interruption in service when you dismount this database.

     PowerShell

      Dismount-Database -Identity DTDB1

10. Move the database and log files from the dial tone database folder into the RDB folder.

11. Move the database and log files from the safe location containing the recovered database
   into the dial tone database folder, and then mount the database, as shown in this
   example.

     PowerShell

      Mount-Database -Identity DTDB1

   This ends the service interruption for users. They can access their original production
   database and send and receive messages.

12. Mount the RDB, as shown in this example.

     PowerShell

      Mount-Database -Identity RDB1

13. Use the Get-Mailbox and New-MailboxRestoreRequest cmdlets to export the data from
   the RDB and import it into the recovered database, as shown in this example. This step
   imports all the messages sent and received using the dial tone database into the
   production database.

     PowerShell

      $mailboxes = Get-Mailbox -Database DTDB1

     PowerShell

      $mailboxes | %{ New-MailboxRestoreRequest -SourceStoreMailbox $_.ExchangeGuid
      -SourceDatabase RDB1 -TargetMailbox $_ }

<!-- p.2868 -->

 14. After the restore operation is complete, you can dismount and remove the RDB, as shown
     in this example.

       PowerShell

        Dismount-Database -Identity RDB1
        Remove-MailboxDatabase -Identity RDB1

For detailed syntax and parameter information, see the following articles:

     New-MailboxDatabase

     Get-Mailbox

     Set-Mailbox

     Mount-Database

     Dismount-Database

     Remove-MailboxDatabase

How do you know you successfully performed a
dial tone recovery?
To verify you successfully performed a dial tone recovery, do the following steps:

     Open the mailbox using Outlook on the web.
     Open the mailbox using Microsoft Outlook.

<!-- p.2869 -->

Managed availability
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Ensuring that users have a good email experience has always been the primary objective for
messaging system administrators. In your Exchange Server organization, all aspects of the
system must be actively monitored and any detected issues must be resolved quickly. To
achieve this, a feature called Managed Availability provides built-in monitoring and recovery
actions that preserve the end-user experience.

Managed Availability
Managed availability, also known as Active Monitoring, or Local Active Monitoring, is the
integration of built-in monitoring and recovery actions with the Exchange high availability
platform. It's designed to detect and recover from problems as soon as they occur and are
discovered by the system. Unlike previous external monitoring solutions and techniques for
Exchange, managed availability doesn't try to identify or communicate the root cause of an
issue. It's instead focused on recovery aspects that address three key areas of the user
experience:

      Availability: Can users access the service?

      Latency: How is the experience for users?

      Errors: Are users able to accomplish what they want?

Managed availability provides a native health monitoring and recovery solution. It moves away
from monitoring individual separate slices of the system to monitoring the end-to-end user
experience, and protecting the end user's experience through recovery-oriented actions.

Managed availability is an internal process that runs on every Exchange server. It polls and
analyzes hundreds of health metrics every second. If something is found to be wrong, most of
the time it will be fixed automatically. But there will always be issues that managed availability
won't be able to fix on its own. In those cases, managed availability will escalate the issue to an
administrator with event logging.

Managed availability is implemented in the form of two services:

      Exchange Health Manager Service (MSExchangeHMHost.exe): This is a controller
      process used to manage worker processes. It's used to build, execute, and start and stop
      the worker process, as needed. It's also used to recover the worker process in case that
      process fails, to prevent the worker process from being a single point of failure.

<!-- p.2870 -->

     Exchange Health Manager Worker process (MSExchangeHMWorker.exe): This is the
     worker process responsible for performing run-time tasks within the managed availability
     framework.

Managed availability uses persistent storage to perform its functions:

     XML files in the \bin\Monitoring\config folder are used to store configuration settings for
     some of the probe and monitor work items.

     Active Directory is used to store global overrides.

     The Windows registry is used to store run-time data, such as bookmarks, and local
     (server-specific) overrides.

     The Windows crimson channel event log infrastructure is used to store the work item
     results.

     Health mailboxes are used for probe activity. Multiple health mailboxes will be created on
     each mailbox database that exists on the server.

Managed Availability Components
As illustrated in the following drawing, managed availability includes three main asynchronous
components that are constantly doing work.

Managed Availability Components

Probes

The first component is called a Probe. Probes are responsible for taking measurements on the
server and collecting data.

<!-- p.2871 -->

There are three primary categories of probes: recurrent probes, notifications, and checks.
Recurrent probes are synthetic transactions performed by the system to test the end-to-end
user experience. Checks are the infrastructure that performs the collection of performance
data, including user traffic. Checks also measure the collected data against thresholds that are
set to determine spikes in user failures, which enable the checks infrastructure to become
aware when users are experiencing issues. Finally, the notification logic enables the system to
take action immediately, based on a critical event, and without having to wait for the results of
the data collected by a probe. These are typically exceptions or conditions that can be detected
and recognized without a large sample set.

Recurrent probes run every few minutes and evaluate some aspect of service health. These
probes might transmit an email via Exchange ActiveSync to a monitoring mailbox, they might
connect to an RPC endpoint, or they might verify Client Access-to-Mailbox connectivity.

All probes are defined on Health Manager service startup in the
Microsoft.Exchange.ActiveMonitoring\ProbeDefinition crimson channel. Each probe definition
has many properties, but the most relevant properties are:

     Name The name of the probe, which begins with a SampleMask of the probe's monitor.

     TypeName The code object type of the probe that contains the probe's logic.

     ServiceName The name of the health set that contains this probe.

     TargetResource The object the probe is validating. This is appended to the name of the
     probe when it is executed to become a probe result ResultName

     RecurrenceIntervalSeconds How often the probe executes.

     TimeoutSeconds How long the probe will wait before failing.

There are hundreds of recurrent probes. Many of these probes are per-database, so as the
number of databases increases, so does the number of probes. Most probes are defined in
code and are therefore not directly discoverable.

The basics of a recurrent probe are as follows: start every RecurrenceIntervalSeconds and check
(or probe) some aspect of health. If the component is healthy, the probe passes and writes an
informational event to the Microsoft.Exchange.ActiveMonitoring\ProbeResult channel with a
ResultType of 3. If the check fails or times out, the probe fails and writes an error event to the
same channel. A ResultType of 4 means the check failed and a ResultType of 1 means that it
timed out. Many probes will rerun if they time out, up to the value of the MaxRetryAttempts
property.

  ７ Note

<!-- p.2872 -->

  The ProbeResult crimson channel can get very busy with hundreds of probes running
  every few minutes and logging an event, so there can be a real impact on the
  performance of your Exchange server if you try expensive queries against the event logs in
  a production environment.

Notifications are probes that are not run by the health manager framework, but by some other
service on the server. These services perform their own monitoring, and then feed their data
into the Managed Availability framework by directly writing probe results. You won't see these
probes in the ProbeDefinition channel, as this channel only describes probes that will be run by
the Managed Availability framework. For example, the ServerOneCopyMonitor Monitor is
triggered by probe results written by the MSExchangeDAGMgmt service. This service performs
its own monitoring, determines whether there is a problem, and logs a probe result. Most
notification probes have the capability to log both a red event that turns the monitor unhealthy
and a green event that makes the monitor healthy again.

Checks are probes that only log events when a performance counter passes above or below a
defined threshold. They are really a special case of notification probes, as there is a service
monitoring the performance counters on the server and logging events to the ProbeResult
channel when the configured threshold is met.

To find the counter and threshold that is considered unhealthy, you can look at the monitor for
this check. Monitors of the type
Microsoft.Office.Datacenter.ActiveMonitoring.OverallConsecutiveSampleValueAboveThresholdMo
nitor or
Microsoft.Office.Datacenter.ActiveMonitoring.OverallConsecutiveSampleValueBelowThresholdMon
itor mean that the probe they watch is a check probe

Monitor

The results of the measurements collected by probes flow into the second component, the
Monitor. The monitor contains all of the business logic used by the system on the data
collected. Similar to a pattern recognition engine, the monitor looks for the various different
patterns on all the collected measurements, and then it decides whether something is
considered healthy.

Monitors query the data to determine if action needs to be taken based on a predefined rule
set. Depending on the rule or the nature of the issue, a monitor can either initiate a responder
or escalate the issue to a human via an event log entry. In addition, monitors define how much
time after a failure that a responder is executed, and the workflow of the recovery action.
Monitors have various states. From a system state perspective, monitors have two states:

<!-- p.2873 -->

     Healthy: The monitor is operating properly and all collected metrics are within normal
     operating parameters.

     Unhealthy: The monitor isn't healthy and has either initiated recovery through a
     responder or notified an administrator through escalation.

From an administrative perspective, monitors have additional states that appear in the
Exchange Management Shell:

     Degraded: When a monitor is in an unhealthy state from 0 through 60 seconds, it's
     considered Degraded. If a monitor is unhealthy for more than 60 seconds, it is considered
     Unhealthy.

     Disabled: The monitor has been explicitly disabled by an administrator.

     Unavailable: The Exchange Health service periodically queries each monitor for its state. If
     it doesn't get a response to the query, the monitor state becomes Unavailable.

     Repairing: An administrator sets the Repairing state to indicate to the system that
     corrective action is in process by a human, which allows the system and humans to
     differentiate between other failures that may occur at the same time corrective action is
     being taken (such as a database copy reseed operation).

Every monitor has a SampleMask property in its definition. As the monitor executes, it looks for
events in the ProbeResult channel that have a ResultName that matches the monitor's
SampleMask. These events could be from recurrent probes, notifications, or checks. If the
monitor's thresholds are achieved, it becomes Unhealthy. From the monitor's perspective, all
three probe types are the same as they each log to the ProbeResult channel.

Its worth noting that a single probe failure doesn't necessarily indicate that something is wrong
with the server. It's the design of monitors to correctly identify when there's a real problem that
needs fixing. This is why many monitors have thresholds of multiple probe failures before
becoming Unhealthy. Even then, many of these problems can be fixed automatically by
responders, so the best place to look for problems that require manual intervention is in the
Microsoft.Exchange.ManagedAvailability\Monitoring crimson channel. This will include the
most recent probe error.

Responders

Finally, there are Responders, which are responsible for recovery and escalation actions. As their
name implies, responders execute some sort of response to an alert that was generated by a
monitor. When something is unhealthy, the first action is to attempt to recover that
component. This could include multi-stage recovery actions; for example, the first attempt may
be to restart the application pool, the second may be to restart the service, the third attempt

<!-- p.2874 -->

may be to restart the server, and the subsequent attempt may be to take the server offline so
that it no longer accepts traffic. If the recovery actions are unsuccessful, the system escalates
the issue to a human through event log notifications.

Responders take various recovery actions, such as resetting an application worker pool or
restarting a server. There are several types of responders:

     Restart Responder Terminates and restarts a service.

     Reset AppPool Responder Stops and restarts an application pool in Internet Information
     Services (IIS).

     Failover Responder Initiates a database or server failover.

     Bugcheck Responder Initiates a bugcheck of the server, thereby causing a server reboot.

     Offline Responder Takes a protocol on a server out of service (rejects client requests).

     Online Responder Places a protocol on a server back into production (accepts client
     requests).

     Escalate Responder Escalates the issue to an administrator via event logging.

In addition to the above listed responders, some components also have specialized responders
that are unique to their component.

All responders include throttling behavior, that provides a built-in sequencing mechanism for
controlling responder actions. The throttling behavior is designed to ensure that the system
isn't compromised or made worse as a result of responder recovery actions. All responders are
throttled in some fashion. When throttling occurs, the responder recovery action may be
skipped or delayed, depending on the responder action. For example, when the Bugcheck
Responder is throttled, its action is skipped, and not delayed.

Health Sets
From a reporting perspective, managed availability has two views of health, one internal and
one external.

The internal view uses health sets. Each component in Exchange Server (for example, Outlook
on the web, Exchange ActiveSync, the Information Store service, content indexing, transport
services, etc.) is monitored by managed availability using probes, monitors, and responders. A
group of probes, monitors, and responders for a given component is called a health set. A
health set is a group of probes, monitors, and responders that determine if that component is
healthy. The current state of a health set (for example, whether it is healthy or unhealthy) is

<!-- p.2875 -->

determined by using the state of the health set's monitors. If all of a health set's monitors are
healthy, then the health set is in a healthy state. If any monitor is not in a healthy state, then
the health set state will be determined by its least healthy monitor.

For detailed steps to view server health or health sets state, see Manage health sets and server
health.

Health Groups
The external view of managed availability is composed of health groups. Health groups are
exposed to System Center Operations Manager 2012 R2.

There are four primary health groups:

     Customer Touch Points Components that affect real-time user interactions, such as
     protocols, or the Information Store.

     Service Components Components without direct, real-time user interactions, such as the
     Microsoft Exchange Mailbox Replication service, or the offline address book generation
     process (OABGen).

     Server Components The physical resources of the server, such as disk space, memory,
     and networking.

     Dependency Availability The server's ability to access necessary dependencies, such as
     Active Directory, DNS, and so on.

When the Exchange Management Pack is installed, System Center Operations Manager (SCOM)
acts as a health portal for viewing information related to the Exchange environment. The SCOM
dashboard includes three views of Exchange server health:

     Active Alerts Escalation Responders write events to the Windows event log that are
     consumed by the monitor within SCOM. These appear as alerts in the Active Alerts view.

     Organization Health A rollup summary of the overall health of the Exchange organization
     health is displayed in this view. These rollups include displaying health for individual
     database availability groups, and health within specific Active Directory sites.

     Server Health Related health sets are combined into health groups and summarized in
     this view.

Overrides

<!-- p.2876 -->

Overrides provide an administrator with the ability to configure some aspects of the managed
availability probes, monitors, and responders. Overrides can be used to fine tune some of the
thresholds used by managed availability. They can also be used to enable emergency actions
for unexpected events that may require configuration settings that are different from the out-
of-box defaults.

Overrides can be created and applied to a single server (this is known as a server override), or
they can be applied to a group of servers (this is known as a global override). Server override
configuration data is stored in the Windows registry on the server on which the override is
applied. Global override configuration data is stored in Active Directory.

Overrides can be configured to last indefinitely, or they can be configured for a specific
duration. In addition, global overrides can be configured to apply to all servers, or only servers
running a specific version of Exchange.

When you configure an override, it won't take effect immediately. The Microsoft Exchange
Health Manager service checks for updated configuration data every 10 minutes. In addition,
global overrides will be dependent on Active Directory replication latency.

For detailed steps to view or configure server or global overrides, see Configure managed
availability overrides.

Management Tasks and Cmdlets
There are three primary operational tasks that administrators will typically do with respect to
managed availability:

     Extracting or viewing system health

     Viewing health sets, and details about probes, monitors and responders

     Managing overrides

The two primary management tools for managed availability are the Windows Event Log and
the Exchange Management Shell. Managed availability logs a large amount of information in
the Exchange ActiveMonitoring and ManagedAvailability crimson channel event logs, such as:

     Probe, monitor, and responder definitions, which are logged in the respective *Definition
     event logs.

     Probe, monitor, and responder results, which are logged in the respective *Results event
     logs.

<!-- p.2877 -->

     Details about responder recovery actions, including when the recovery action is started,
     and it's considered complete (whether successful or not), which are logged in the
     RecoveryActionResults event log.

There are 12 cmdlets used for managed availability, which are described in the following table.

                                                                                          ﾉ     Expand table

 Cmdlet                       Description

 Get-ServerHealth             Used to get raw server health information, such as health sets and their
                              current state (healthy or unhealthy), health set monitors, server
                              components, target resources for probes, and timestamps related to probe
                              or monitor start or stop times, and state transition times.

 Get-HealthReport             Used to get a summary health view that includes health sets and their
                              current state.

 Get-MonitoringItemIdentity   Used to view the probes, monitors, and responders associated with a
                              specific health set.

 Get-MonitoringItemHelp       Used to view descriptions about some of the properties of probes,
                              monitors, and responders.

 Add-                         Used to create a local, server-specific override of a probe, monitor, or
 ServerMonitoringOverride     responder.

 Get-                         Used to view a list of local overrides on the specified server.
 ServerMonitoringOverride

 Remove-                      Used to remove a local override from a specific server.
 ServerMonitoringOverride

 Add-                         Used to create a global override for a group of servers.
 GlobalMonitoringOverride

 Get-                         Used to view a list of global overrides configured in the organization.
 GlobalMonitoringOverride

 Remove-                      Used to remove a global override.
 GlobalMonitoringOverride

 Set-ServerComponentState     Used to configure the state of one or more server components.

 Get-ServerComponentState     Used to view the state of one or more server components.

<!-- p.2878 -->

Manage health sets and server health in
Exchange Server
07/23/2025

APPLIES TO:       2016      2019      Subscription Edition

You can use the built-in health reporting cmdlets to perform a variety of tasks related to
managed availability, such as:

      Viewing the health of a server or group of servers

      Viewing a list of health sets

      Viewing a list of probes, monitors, and responders associated with a particular health set

      View a list of monitors and their current health

For more information about health reporting and managed availability, see Managed
availability.

What do you need to know before you begin?
      Estimated time to complete each procedure: 2 minutes

      The procedures in this topic require the Exchange Management Shell. For more
      information, see Open the Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the Exchange Management Shell to view
server health
You can use the Exchange Management Shell to get a summary of the health of an Exchange
server.

<!-- p.2879 -->

Run either of the following commands to view the health sets and health information on an
Exchange server:

  PowerShell

  Get-HealthReport -Identity <ServerName>

  PowerShell

  Get-ServerHealth -Identity <ServerName> | Format-Table
  Server,CurrentHealthSetState,Name,HealthSetName,AlertValue,HealthGroupName -Auto

Run any of the following commands to view the health sets on an Exchange server or database
availability group:

  PowerShell

  Get-ExchangeServer | Get-HealthReport -RollupGroup

  PowerShell

  Get-ExchangeServer | Get-HealthReport -RollupGroup -HealthSetName <HealthSet>

  PowerShell

  (Get-DatabaseAvailabilityGroup <DAGName>).Servers | Get-HealthReport -RollupGroup

For detailed syntax and parameter information, see Get-HealthReport.

Use the Exchange Management Shell to view a list
of health sets
A health set is a group of monitors, probes and responders for a component that determine
whether the component is healthy or unhealthy.

Run the following command to view the health sets on an Exchange server:

  PowerShell

  Get-HealthReport -Server <ServerName>

For detailed syntax and parameter information, see Get-HealthReport.

<!-- p.2880 -->

Use the Exchange Management Shell to view the
probes, monitors and responders for a health set
You can use the Exchange Management Shell to view the list of probes, monitors, and
responders associated with a health set on an Exchange server.

Run the following command to view the probes, monitors and responders associated with a
health set on an Exchange server:

  PowerShell

  Get-MonitoringItemIdentity -Server <ServerName> -Identity <HealthSetName> |
  Format-Table Identity,ItemType,Name -Auto

For detailed syntax and parameter information, see Get-MonitoringItemIdentity.

Use the Exchange Management Shell to View a List
of Monitors and Their Current Health
The health of a monitor is reported by using the "worst of" monitors in the health set. You can
view the details of a health set to see which monitors are healthy and which ones are
unhealthy.

Run the following command to view a list of the monitors and their current health on an
Exchange server:

  PowerShell

  Get-ServerHealth -HealthSet <HealthSetName> -Server <ServerName> | Format-Table
  Name, AlertValue -Auto

For detailed syntax and parameter information, see Get-ServerHealth.
