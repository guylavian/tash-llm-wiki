---
title: "Welcome — pages 881-904"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0881-0904
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0881-0904
family: sccm
documentKind: "doc"
abstract: "8. From an elevated Windows PowerShell prompt, run the following script to initiate the WSUS Cleanup wizard: PowerShell [reflection.assembly]::LoadWithPartialName(\"Microsoft.UpdateServices.Administrati on\") | out-null $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]:"
---

# Welcome — pages 881-904

<!-- p.881 -->

 8. From an elevated Windows PowerShell prompt, run the following script to initiate the WSUS
   Cleanup wizard:

     PowerShell

     [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administrati
     on") | out-null
     $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer();
     $cleanupScope = new-object Microsoft.UpdateServices.Administration.CleanupScope;
     $cleanupScope.DeclineSupersededUpdates = $true
     $cleanupScope.DeclineExpiredUpdates = $true
     $cleanupScope.CleanupObsoleteUpdates = $true
     $cleanupScope.CompressUpdates = $true
     $cleanupScope.CleanupObsoleteComputers = $true
     $cleanupScope.CleanupUnneededContentFiles = $true
     $cleanupManager = $wsus.GetCleanupManager();
     $cleanupManager.PerformCleanup($cleanupScope);

 9. From an elevated Windows PowerShell prompt, run the following script to perform a
   cleanup of declined updates:

     PowerShell

     [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administrati
     on")
     $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer();
     $wsus.GetUpdates() | Where {$_.IsDeclined -eq $true} | ForEach-Object
     {$wsus.DeleteUpdate($_.Id.UpdateId.ToString()); Write-Host $_.Title removed }

10. Shrink the SUSDB files.

11. Shrink the SUSDB database.

12. Reindex and update statistics on SUSDB.

    a. To reindex SUSDB, run the following SQL script:

        SQL

        EXEC sp_MSforeachtable @command1="SET QUOTED_IDENTIFIER ON;ALTER INDEX ALL ON
        ? REBUILD;"

    b. To update statistics, run the following SQL script:

        SQL

<!-- p.882 -->

          Exec sp_msforeachtable "UPDATE STATISTICS ? WITH FULLSCAN, COLUMNS"

Maintain the WSUS database (SUSDB) automatically
The following PowerShell script replicates the manual steps. When the script is executed, a
SUSDB-Maintenance.log file will be created and opened.

  ） Important

  Ensure that any scheduled synchronizations are disabled, either in Configuration Manager (if
  used) or on standalone WSUS servers.

 PowerShell

 <# SUSDB-Maintenance

 Requirements
 * WID must be local.
 * Remote connections for SQL now supported, choose [S] Change SQL Server from menu to
 set the SQL Server.
 * WSUS Console must be installed local.
 * No longer requires SQL Server PowerShell Module - uses native .NET SqlClient.

 This script will present the following menu options for performing SUSDB Maintenance.
 SUSDB-Maintenance.log will be created and opened when the script is run.

 [S] Change SQL Server, currently set to
 [A] Update Count
 [1] Update spDeleteUpdate procedure
 [2] Shrink Files
 [3] Shrink Database
 [4] Reindex and Update Statistics
 [5] Cleanup Sync History
 [6] Cleanup Superseded Updates Older than x Days
 [7] Cleanup Obsolete Updates
 [8] WSUS Cleanup Wizard
 [9] Cleanup Declined
 [10] Shrink Files
 [11] Shrink Database
 [12] Reindex and Update Statistics
 [RA] Run all above steps sequentially

 Sample scripts are not supported under any Microsoft standard support program or
 service. Sample scripts are provided AS IS without warranty of any kind.
 Microsoft further disclaims all implied warranties including, without limitation, any
 implied warranties of merchantability or of fitness for a particular purpose.
 The entire risk arising out of the use or performance of the sample script and
 documentation remains with you.

<!-- p.883 -->

In no event shall Microsoft, its authors, or anyone else involved in the creation,
production, or delivery of the scripts be liable for any damages whatsoever
(including, without limitation, damages for loss of business profits, business
interruption, loss of business information, or other pecuniary loss) arising out of
the use
of or inability to use the sample script or documentation, even if Microsoft has been
advised of the possibility of such damages.

#>

#Global Variables
$Global:LogFile = $null
$Global:SQLoutput = $null
$Global:Spaceused = $null
$Global:progresspreference = 'SilentlyContinue'
$Global:DaysSupersededNotDeclined = 30

$ErrorActionPreference = "Stop"

try {
    $SQLsetup = (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Update
Services\Server\Setup' -Name SqlServerName).SqlServerName
}
catch {
    $global:LocalSQLInstance = "SQL Server or WID NOT Found"
}

if ($SQLsetup -contains "MICROSOFT##WID" ) {
    $global:LocalSQLInstance = '\\.\pipe\MICROSOFT##WID\tsql\query'
}
elseif ($null -ne $SQLsetup) {
    $global:LocalSQLInstance = $SQLsetup
}
else {
    $global:LocalSQLInstance = "SQL Server or WID NOT Found"
}

#Region SQL_Queries
$spDeleteUpdate = "USE SUSDB
GO

/****** Object: StoredProcedure [dbo].[spDeleteUpdate]     Script Date: 11/2/2020
8:55:02 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[spDeleteUpdate]
    @localUpdateID int
AS
SET NOCOUNT ON
 Begin TRANSACTION

<!-- p.884 -->

SAVE TRANSACTION DeleteUpdate
DECLARE @retcode INT
DECLARE @revisionID INT
DECLARE @revisionList TABLE(RevisionID INT PRIMARY KEY)
INSERT INTO @revisionList (RevisionID)
     SELECT r.RevisionID FROM dbo.tbRevision r
         WHERE r.LocalUpdateID = @localUpdateID
IF EXISTS (SELECT b.RevisionID FROM dbo.tbBundleDependency b WHERE b.BundledRevisionID
IN (SELECT RevisionID FROM @revisionList))
   OR EXISTS (SELECT p.RevisionID FROM dbo.tbPrerequisiteDependency p WHERE
p.PrerequisiteRevisionID IN (SELECT RevisionID FROM @revisionList))
 Begin
     RAISERROR('spDeleteUpdate got error: cannot delete update as it is still
referenced by other update(s)', 16, -1)
     ROLLBACK TRANSACTION DeleteUpdate
     COMMIT TRANSACTION
     RETURN(1)
 End
INSERT INTO @revisionList (RevisionID)
     SELECT DISTINCT b.BundledRevisionID FROM dbo.tbBundleDependency b
         INNER JOIN dbo.tbRevision r ON r.RevisionID = b.RevisionID
         INNER JOIN dbo.tbProperty p ON p.RevisionID = b.BundledRevisionID
         WHERE r.LocalUpdateID = @localUpdateID
              AND p.ExplicitlyDeployable = 0
IF EXISTS (SELECT IsLocallyPublished FROM dbo.tbUpdate WHERE LocalUpdateID =
@localUpdateID AND IsLocallyPublished = 1)
 Begin
     INSERT INTO @revisionList (RevisionID)
         SELECT DISTINCT pd.PrerequisiteRevisionID FROM dbo.tbPrerequisiteDependency pd
              INNER JOIN dbo.tbUpdate u ON pd.PrerequisiteLocalUpdateID =
u.LocalUpdateID
              INNER JOIN dbo.tbProperty p ON pd.PrerequisiteRevisionID = p.RevisionID
              WHERE u.IsLocallyPublished = 1 AND p.UpdateType = 'Category'
 End
DECLARE #cur CURSOR LOCAL FAST_FORWARD FOR
     SELECT t.RevisionID FROM @revisionList t ORDER BY t.RevisionID DESC
OPEN #cur
FETCH #cur INTO @revisionID
WHILE (@@ERROR=0 AND @@FETCH_STATUS=0)
 Begin
     IF EXISTS (SELECT b.RevisionID FROM dbo.tbBundleDependency b WHERE
b.BundledRevisionID = @revisionID
                     AND b.RevisionID NOT IN (SELECT RevisionID FROM @revisionList))
        OR EXISTS (SELECT p.RevisionID FROM dbo.tbPrerequisiteDependency p WHERE
p.PrerequisiteRevisionID = @revisionID
                        AND p.RevisionID NOT IN (SELECT RevisionID FROM @revisionList))
      Begin
         DELETE FROM @revisionList WHERE RevisionID = @revisionID
         IF (@@ERROR <> 0)
          Begin
              RAISERROR('Deleting disqualified revision from temp table failed', 16, -1)
              GOTO Error
          End
      End
     FETCH NEXT FROM #cur INTO @revisionID

<!-- p.885 -->

 End
IF (@@ERROR <> 0)
 Begin
     RAISERROR('Fetching a cursor to value a revision', 16, -1)
     GOTO Error
 End
CLOSE #cur
DEALLOCATE #cur
DECLARE #cur CURSOR LOCAL FAST_FORWARD FOR
     SELECT t.RevisionID FROM @revisionList t ORDER BY t.RevisionID DESC
OPEN #cur
FETCH #cur INTO @revisionID
WHILE (@@ERROR=0 AND @@FETCH_STATUS=0)
 Begin
     EXEC @retcode = dbo.spDeleteRevision @revisionID
     IF @@ERROR <> 0 OR @retcode <> 0
      Begin
         RAISERROR('spDeleteUpdate got error from spDeleteRevision', 16, -1)
         GOTO Error
      End
     FETCH NEXT FROM #cur INTO @revisionID
 End
IF (@@ERROR <> 0)
 Begin
     RAISERROR('Fetching a cursor to delete a revision', 16, -1)
     GOTO Error
 End
CLOSE #cur
DEALLOCATE #cur
COMMIT TRANSACTION
RETURN(0)
Error:
     CLOSE #cur
     DEALLOCATE #cur
     IF (@@TRANCOUNT > 0)
      Begin
         ROLLBACK TRANSACTION DeleteUpdate
         COMMIT TRANSACTION
      End
     RETURN(1)
GO"

$DB = "Use SUSDB
GO
 "

$Reindex = $DB + 'EXEC sp_MSforeachtable @command1="SET QUOTED_IDENTIFIER ON;ALTER
INDEX ALL ON ? REBUILD;"'

$UpdateStatistics = $DB + 'Exec sp_msforeachtable "UPDATE STATISTICS ? WITH FULLSCAN,
COLUMNS"'

$CleanupSyncHistory = "USE SUSDB;
DELETE FROM tbEventInstance WHERE EventNamespaceID = '2' AND EVENTID IN ('381', '382',
'384', '386', '387', '389');"

<!-- p.886 -->

$UpdateCount = "use SUSDB;
GO

DECLARE @numberOfMatch INT
DECLARE @tmpTable TABLE (
    name VARCHAR(25)
)
INSERT INTO @tmpTable
EXEC spGetObsoleteUpdatesToCleanup
SELECT @numberOfMatch = @@ROWCOUNT
select
(Select count (*) from vwMinimalUpdate ) 'Total Updates',
(Select count (*) from vwMinimalUpdate where declined=0) as 'Live Updates',
(Select count (*) from vwMinimalUpdate where IsSuperseded =1) as 'Superseded',
(Select count (*) from vwMinimalUpdate where IsSuperseded =1 and declined=0) as
'Superseded but not declined',
(Select count (*) from vwMinimalUpdate where declined=1) as 'Declined',
(Select count (*) from vwMinimalUpdate where IsSuperseded =1 and declined=1)
'Superseded and Declined',
(select Count(*) From @tmpTable ) 'Obsolete Updates Needed to be cleaned'"

$Shrinkfile = "USE SUSDB;
GO
DBCC SHRINKFILE (SUSDB, 0);
GO"

$ShrinkDatabase = "
USE SUSDB;
GO
DBCC SHRINKDATABASE (SUSDB, 0);
GO"

$CleanupSupersededUpdates = "DECLARE @thresholdDays INT =
$Global:DaysSupersededNotDeclined    -- Specify the number of days between today and
the release date for which the superseded updates must not be declined. This should
match configuration of supersedence rules in SUP component properties, if ConfigMgr is
being used with WSUS.
DECLARE @testRun BIT = 0           -- Set this to 1 to test without declining anything.
-- There shouldn't be any need to modify anything after this line.
DECLARE @uid UNIQUEIDENTIFIER
DECLARE @title NVARCHAR(500)
DECLARE @date DATETIME
DECLARE @userName NVARCHAR(100) = SYSTEM_USER
DECLARE @count INT = 0
DECLARE DU CURSOR FOR
        SELECT MU.UpdateID, U.DefaultTitle, U.CreationDate FROM vwMinimalUpdate MU
        JOIN PUBLIC_VIEWS.vUpdate U ON MU.UpdateID = U.UpdateId
        WHERE MU.IsSuperseded = 1 AND MU.Declined = 0 AND MU.IsLatestRevision = 1
        AND MU.CreationDate < DATEADD(dd,-@thresholdDays,GETDATE())
        ORDER BY MU.CreationDate
PRINT 'Declining superseded updates older than ' + CONVERT(NVARCHAR(5),
@thresholdDays) + ' days.' + CHAR(10)
OPEN DU
FETCH NEXT FROM DU INTO @uid, @title, @date

<!-- p.887 -->

WHILE (@@FETCH_STATUS > - 1)
 Begin
       SET @count = @count + 1
       PRINT 'Declining update ' + CONVERT(NVARCHAR(50), @uid) + ' (Creation Date ' +
CONVERT(NVARCHAR(50), @date) + ') - ' + @title + ' ...'
       IF @testRun = 0
              EXEC spDeclineUpdate @updateID = @uid, @adminName = @userName,
@failIfReplica = 1
       FETCH NEXT FROM DU INTO @uid, @title, @date
 End
CLOSE DU
DEALLOCATE DU
PRINT CHAR(10) + 'Attempted to decline ' + CONVERT(NVARCHAR(10), @count) + '
updates.'"

$CleanupObsoleteUpdates = "DECLARE @var1 INT
DECLARE @msg nvarchar(100)
CREATE TABLE #results (Col1 INT)
        INSERT INTO #results(Col1) EXEC spGetObsoleteUpdatesToCleanup
DECLARE WC Cursor
        FOR
        SELECT Col1 FROM #results
OPEN WC
        FETCH NEXT FROM WC
        INTO @var1
        WHILE (@@FETCH_STATUS > -1)
         Begin SET @msg = 'Deleting' + CONVERT(varchar(10), @var1)
        RAISERROR(@msg,0,1) WITH NOWAIT EXEC spDeleteUpdate @localUpdateID=@var1
        FETCH NEXT FROM WC INTO @var1 End
CLOSE WC
        DEALLOCATE WC

       DROP TABLE #results"

$Spaceused = "USE SUSDB;
SELECT
    name,
       size * 8/1024 'Size (MB)'
FROM sys.database_files;"
#EndRegion SQL_Queries

Function Write-log {

    ############################
    #Write-Log in CMTrace Format
    ############################

    PARAM(
        [String]$Message,
        [String]$Path = $LogFile,
        [int]$severity,
        [string]$component
    )

    $TimeZoneBias = Get-WmiObject -Query "Select Bias from Win32_TimeZone"

<!-- p.888 -->

    $Date = Get-Date -Format "HH:mm:ss.fff"
    $Date2 = Get-Date -Format "MM-dd-yyyy"

    "<![LOG[$Message]LOG]!><time=$([char]34)$date$($TimeZoneBias.bias)$([char]34)
date=$([char]34)$date2$([char]34) component=$([char]34)$component$([char]34)
context=$([char]34)$([char]34) type=$([char]34)$severity$([char]34)
thread=$([char]34)$([char]34) file=$([char]34)$([char]34)>" | Out-File -FilePath $Path
-Append -NoClobber -Encoding default

    #Write-Log -Message "Starting installation" -severity 1 -component "Installation"
    #Write-Log -Message "Something went wrong" -severity 2 -component "Installation"
    #Write-Log -Message "BIG Error Message" -severity 3 -component "Installation"

}

function Write-Color([String[]]$Text, [ConsoleColor[]]$Color) {
    for ($i = 0; $i -lt $Text.Length; $i++) {
        Write-Host $Text[$i] -Foreground $Color[$i] -NoNewline
    }
    Write-Host
}

function Invoke-CustomSqlCommand {
    <#
    .SYNOPSIS
    Executes SQL commands without requiring SQL Server PowerShell module

    .PARAMETER ServerInstance
    SQL Server instance name (can be pipe name for WID)

    .PARAMETER Query
    SQL query to execute

    .PARAMETER Database
    Database name (optional)

    .PARAMETER OutputResults
    Return results as objects (default: $true)
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$ServerInstance,

        [Parameter(Mandatory = $true)]
        [string]$Query,

        [Parameter(Mandatory = $false)]
        [string]$Database,

        [Parameter(Mandatory = $false)]
        [bool]$OutputResults = $true
    )

    $startTime = Get-Date
    $infoMessages = @()

<!-- p.889 -->

    try {
        # Build connection string
        if ($ServerInstance -like '*pipe*') {
            # WID connection
            $connectionString = "Server=np:$ServerInstance;Database=SUSDB;Integrated
Security=True;TrustServerCertificate=True;"
        }
        else {
            # Regular SQL Server connection
            if ($Database) {
                $connectionString =
"Server=$ServerInstance;Database=$Database;Integrated
Security=True;TrustServerCertificate=True;"
            }
            else {
                $connectionString = "Server=$ServerInstance;Integrated
Security=True;TrustServerCertificate=True;"
            }
        }

       # Create connection
       $connection = New-Object System.Data.SqlClient.SqlConnection
       $connection.ConnectionString = $connectionString

       # Add event handler for info messages (PRINT statements, etc.)
       $connection.add_InfoMessage({
           param($sender, $event)
           $script:infoMessages += $event.Message
       })

       $connection.FireInfoMessageEventOnUserErrors = $true
       $connection.Open()

        # Split query by GO statements (batch separator)
        $batches = $Query -split '\r?\nGO\r?\n|\r?\nGO$|^GO\r?\n' | Where-Object {
$_.Trim() -ne '' }

       $allResults = @()
       $lastResultSet = $null

       foreach ($batch in $batches) {
           $trimmedBatch = $batch.Trim()
           if ($trimmedBatch -eq '' -or $trimmedBatch -eq 'GO') {
               continue
           }

            # Create command
            $command = $connection.CreateCommand()
            $command.CommandText = $trimmedBatch
            $command.CommandTimeout = 0 # No timeout

            # Execute and capture results
            $reader = $command.ExecuteReader()

<!-- p.890 -->

            # Read all result sets from this batch
            do {
                $dataTable = New-Object System.Data.DataTable
                $dataTable.Load($reader)

                if ($dataTable.Rows.Count -gt 0) {
                    $allResults += $dataTable
                    $lastResultSet = $dataTable
                }
            } while (!$reader.IsClosed)

            $reader.Close()
       }

       # Calculate execution time
       $endTime = Get-Date
       $executionTime = ($endTime - $startTime).TotalMilliseconds

       # Create return object with statistics
       $result = [PSCustomObject]@{
           Results = $lastResultSet
           ExecutionTime = $executionTime
           RowsAffected = if ($lastResultSet) { $lastResultSet.Rows.Count } else { 0
}
            InfoMessages = $infoMessages
       }

       return $result
    }
    catch {
        Write-Error "SQL Error: $($_.Exception.Message)"
        throw
    }
    finally {
        if ($connection.State -eq 'Open') {
            $connection.Close()
        }
    }
}

function UpdateCount {

    Write-log -Message "--> Begin Update Count" -severity 1 -component "Update Count"
    Write-log -Message "Update Count" -severity 1 -component "Update Count"

    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$UpdateCount

    if ($result.Results -and $result.Results.Rows.Count -gt 0) {
        $SQLoutput = $result.Results.Rows[0]

        Write-log -Message ("Total execution time for Update Count.........:" +
($result.ExecutionTime / 1000) + " seconds")
        Write-log -Message ("Total Updates " + $SQLoutput.'Total Updates') -severity
1 -component "Update Count"

<!-- p.891 -->

        Write-log -Message ("Live Updates " + $SQLoutput.'Live Updates') -severity 1
-component "Update Count"
        Write-log -Message ("Superseded " + $SQLoutput.'Superseded') -severity 1 -
component "Update Count"
        Write-log -Message ("Superseded but not declined " + $SQLoutput.'Superseded
but not declined') -severity 1 -component "Update Count"
        Write-log -Message ("Declined " + $SQLoutput.'Declined') -severity 1 -
component "Update Count"
        Write-log -Message ("Superseded and Declined " + $SQLoutput.'Superseded and
Declined') -severity 1 -component "Update Count"
        Write-log -Message ("Obsolete Updates Needed to be cleaned " +
$SQLoutput.'Obsolete Updates Needed to be cleaned') -severity 1 -component "Update
Count"
    }
    else {
        Write-log -Message "No results returned from Update Count query" -severity 2
-component "Update Count"
    }

    Write-log -Message "--> End Update Count" -severity 1 -component "Update Count"
}

function Update_spDeleteUpdate_Procedure {

    Write-log -Message "--> Begin update spDeleteUpdate procedure" -severity 1 -
component "Update spDeleteUpdate"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$spDeleteUpdate
    Write-log -Message ("Total execution time.........:" + ($result.ExecutionTime /
1000) + " seconds") -severity 1 -component "Update spDeleteUpdate"
    Write-log -Message "SQL Output is $($result.Results)" -severity 1 -component
"Update spDeleteUpdate"
    Write-log -Message "--> End update spDeleteUpdate procedure" -severity 1 -
component "Update spDeleteUpdate"
}

function ShrinkFile {

    Write-log -Message "--> Begin shrink file" -severity 1 -component "Shrink File"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Spaceused
    $SQLoutput = $result.Results
    Write-log -Message ("Total execution time for checking Space Used.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink File"

    if ($SQLoutput -and $SQLoutput.Rows.Count -gt 1) {
        Write-log -Message ($SQLoutput.Rows[1].name + " " + $SQLoutput.Rows[1]."Size
(MB)" + " MB") -severity 1 -component "Shrink Files"
    }

    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Shrinkfile
    Write-log -Message ("Total execution time for Shrinking File.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink File"

<!-- p.892 -->

    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Spaceused
    $SQLoutput = $result.Results
    Write-log -Message ("Total execution time for checking Space Used.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink File"

    if ($SQLoutput -and $SQLoutput.Rows.Count -gt 1) {
        Write-log -Message ($SQLoutput.Rows[1].name + " " + $SQLoutput.Rows[1]."Size
(MB)" + " MB") -severity 1 -component "Shrink File"
    }

    Write-log -Message "--> End shrink file" -severity 1 -component "Shrink File"
}

function ShrinkDatabase {

    Write-log -Message "--> Begin shrink database" -severity 1 -component "Shrink
Database"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Spaceused
    $SQLoutput = $result.Results
    Write-log -Message ("Total execution time for checking Space Used.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink Database"

    if ($SQLoutput -and $SQLoutput.Rows.Count -gt 0) {
        Write-log -Message ($SQLoutput.Rows[0].name + " " + $SQLoutput.Rows[0]."Size
(MB)" + " MB") -severity 1 -component "Shrink Database"
    }

    Write-log -Message "--> Begin shrink database" -severity 1 -component "Shrink
Database"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$ShrinkDatabase
    Write-log -Message ("Total execution time for Shrinking Database.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink Database"

    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Spaceused
    $SQLoutput = $result.Results
    Write-log -Message ("Total execution time for checking Space Used.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Shrink Database"

    if ($SQLoutput -and $SQLoutput.Rows.Count -gt 0) {
        Write-log -Message ($SQLoutput.Rows[0].name + " " + $SQLoutput.Rows[0]."Size
(MB)" + " MB") -severity 1 -component "Shrink Database"
    }

    Write-log -Message "--> End shrink database" -severity 1 -component "Shrink
Database"
}

function ReindexStatistics {

    Write-log -Message "--> Begin reindex and update statistics" -severity 1 -
component "IndexStats"

<!-- p.893 -->

    Write-log -Message "Reindexing" -severity 1 -component "IndexStats"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$Reindex
    Write-log -Message ("Total execution time for Reindex.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "IndexStats"

    Write-log -Message "Now Updating Statistics" -severity 1 -component "IndexStats"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$UpdateStatistics
    Write-log -Message ("Total execution time for Updating Statistics.........:" +
($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "IndexStats"
    Write-log -Message "--> End reindex and update statistics" -severity 1 -component
"IndexStats"

}

function CleanUpSyncHistory {

    Write-log -Message "--> Begin cleanup sync history" -severity 1 -component
"Cleanup Sync History"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$CleanupSyncHistory
    Write-log -Message ("Total execution time for Cleaning up Sync History.........:"
+ ($result.ExecutionTime / 1000) + " seconds") -severity 1 -component "Cleanup Sync
History"
    Write-log -Message "--> End cleanup sync history" -severity 1 -component "Cleanup
Sync History"
}

function CleanupSupersedUpdates {
    Write-log -Message "--> Begin cleanup superseded updates" -severity 1 -component
"Cleanup Superseded Updates"
    Write-log -Message "Days specified: $Global:DaysSupersededNotDeclined" -severity
1 -component "Cleanup Superseded Updates"

    $CleanupSupersededUpdates = "DECLARE @thresholdDays INT =
$Global:DaysSupersededNotDeclined   -- Specify the number of days between today and
the release date for which the superseded updates must not be declined. This should
match configuration of supersedence rules in SUP component properties, if ConfigMgr is
being used with WSUS.
DECLARE @testRun BIT = 0          -- Set this to 1 to test without declining anything.
-- There shouldn't be any need to modify anything after this line.
DECLARE @uid UNIQUEIDENTIFIER
DECLARE @title NVARCHAR(500)
DECLARE @date DATETIME
DECLARE @userName NVARCHAR(100) = SYSTEM_USER
DECLARE @count INT = 0
DECLARE DU CURSOR FOR
       SELECT MU.UpdateID, U.DefaultTitle, U.CreationDate FROM vwMinimalUpdate MU
       JOIN PUBLIC_VIEWS.vUpdate U ON MU.UpdateID = U.UpdateId
       WHERE MU.IsSuperseded = 1 AND MU.Declined = 0 AND MU.IsLatestRevision = 1
       AND MU.CreationDate < DATEADD(dd,-@thresholdDays,GETDATE())
       ORDER BY MU.CreationDate
PRINT 'Declining superseded updates older than ' + CONVERT(NVARCHAR(5),
@thresholdDays) + ' days.' + CHAR(10)

<!-- p.894 -->

OPEN DU
FETCH NEXT FROM DU INTO @uid, @title, @date
WHILE (@@FETCH_STATUS > - 1)
 Begin
        SET @count = @count + 1
        PRINT 'Declining update ' + CONVERT(NVARCHAR(50), @uid) + ' (Creation Date ' +
CONVERT(NVARCHAR(50), @date) + ') - ' + @title + ' ...'
        IF @testRun = 0
               EXEC spDeclineUpdate @updateID = @uid, @adminName = @userName,
@failIfReplica = 1
        FETCH NEXT FROM DU INTO @uid, @title, @date
 End
CLOSE DU
DEALLOCATE DU
PRINT CHAR(10) + 'Attempted to decline ' + CONVERT(NVARCHAR(10), @count) + '
updates.'"

    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$CleanupSupersededUpdates -Database "SUSDB"
    Write-log -Message ("Total execution time for Cleaning up Superseded
Updates.........:" + ($result.ExecutionTime / 1000) + " seconds") -severity 1 -
component "Cleanup Superseded Updates"
    Write-log -Message "SQL Output is $($result.Results)" -severity 1 -component
"Cleanup Superseded Updates"
    Write-log -Message "--> End cleanup superseded updates" -severity 1 -component
"Cleanup Superseded Updates"
}

function CleanupObsoleteUpdates {

    Write-log -Message "--> Begin cleanup obsolete updates" -severity 1 -component
"Cleanup Obsolete Updates"
    $result = Invoke-CustomSqlCommand -ServerInstance $LocalSQLInstance -Query
$CleanupObsoleteUpdates -Database "SUSDB"
    Write-log -Message ("Total execution time for Cleaning up Obsolete
Updates.........:" + ($result.ExecutionTime / 1000) + " seconds") -severity 1 -
component "Cleanup Obsolete Updates"
    Write-log -Message "--> End cleanup obsolete updates" -severity 1 -component
"Cleanup Obsolete Updates"
}

function WSUSCleanUpWizard {

    Write-log -Message "--> Begin WSUS cleanup wizard" -severity 1 -component "WSUS
Cleanup Wizard"

[reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration")
| Out-Null
    $CleanUpWizard = {

[reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration")
| Out-Null
        $wsus =
[Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer();

<!-- p.895 -->

        $cleanupScope = New-Object
Microsoft.UpdateServices.Administration.CleanupScope;
        $cleanupScope.DeclineSupersededUpdates = $true
        $cleanupScope.DeclineExpiredUpdates = $true
        $cleanupScope.CleanupObsoleteUpdates = $true
        $cleanupScope.CompressUpdates = $true
        $cleanupScope.CleanupObsoleteComputers = $true
        $cleanupScope.CleanupUnneededContentFiles = $true
        $cleanupManager = $wsus.GetCleanupManager();
        $cleanupManager.PerformCleanup($cleanupScope);
    }

    $RunCleanUpWizard = Invoke-Command -ScriptBlock $CleanUpWizard

    Write-log -Message ("Disk Space Freed " + $RunCleanUpWizard.DiskSpaceFreed + "
MB") -severity 1 -component "WSUS Cleanup Wizard"
    Write-log -Message ("Expired Updates Declined " +
$RunCleanUpWizard.ExpiredUpdatesDeclined) -severity 1 -component "WSUS Cleanup Wizard"
    Write-log -Message ("Obsolete Computers Deleted " +
$RunCleanUpWizard.ObsoleteComputersDeleted) -severity 1 -component "WSUS Cleanup
Wizard"
    Write-log -Message ("Obsolete Updates Deleted " +
$RunCleanUpWizard.ObsoleteUpdatesDeleted) -severity 1 -component "WSUS Cleanup Wizard"
    Write-log -Message ("Superseded Updates Declined " +
$RunCleanUpWizard.SupersededUpdatesDeclined) -severity 1 -component "WSUS Cleanup
Wizard"
    Write-log -Message ("Updates Compressed " + $RunCleanUpWizard.UpdatesCompressed)
-severity 1 -component "WSUS Cleanup Wizard"
    Write-log -Message "--> End WSUS cleanup wizard" -severity 1 -component "WSUS
Cleanup Wizard"
}

function CleanUpDeclined {

    Write-log -Message "--> Begin cleanup declined" -severity 1 -component "Cleanup
Declined"

    # Load WSUS administration assembly
    [void]
[Reflection.Assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration")

    # Connect to WSUS
    $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer()

    # Attempt to delete all declined updates, but skip those that are referenced
    $wsus.GetUpdates() |
        Where-Object { $_.IsDeclined -eq $true } |
        ForEach-Object {
            try {
                # Use the UpdateId GUID directly (no ToString() needed)
                $wsus.DeleteUpdate($_.Id.UpdateId)
                Write-log -Message "Removed: $($_.Title)" -severity 1 -component
"Cleanup Declined"
            }
            catch {

<!-- p.896 -->

                Write-log -Message "Skipped: $($_.Title)" -severity 2 -component
"Cleanup Declined"
            }
        }

    Write-log -Message "--> End cleanup declined" -severity 1 -component "Cleanup
Declined"
}

function ChangeSQL {
    Write-log -Message "--> Begin change SQL" -severity 1 -component "Change SQL"
    $global:LocalSQLInstance = Read-Host -Prompt 'Enter the name of the SQL Server'
    Write-log -Message "--> SQL Server changed to $LocalSQLInstance" -severity 1 -
component "Change SQL"
    Write-log -Message "--> End change SQL" -severity 1 -component "Change SQL"
}
function Show-Menu {
    Write-log -Message "--> Begin Show Menu" -severity 1 -component "Show Menu"
    Clear-Host
    Write-Host "================ $Title ================" -BackgroundColor Black -
ForegroundColor Yellow

     #Write-Color -Text "[S] ", "Change SQL Server, currently set to $LocalSQLInstance"
-Color Yellow, Cyan
     Write-Color -Text "[S] ", "Change SQL Server, currently set to ",
$LocalSQLInstance -Color Yellow, Cyan, Green
     Write-Color -Text "[A] ", "Update Count" -Color Yellow, Cyan
     Write-Color -Text "[1] ", "Update spDeleteUpdate procedure" -Color Yellow, Cyan
#https://docs.microsoft.com/en-US/troubleshoot/mem/configmgr/spdeleteupdate-slow-
performance
     Write-Color -Text "[2] ", "Shrink Files" -Color Yellow, Cyan
     Write-Color -Text "[3] ", "Shrink Database" -Color Yellow, Cyan
     Write-Color -Text "[4] ", "Reindex and Update Statistics" -Color Yellow, Cyan
     Write-Color -Text "[5] ", "Cleanup Sync History" -Color Yellow, Cyan
     Write-Color -Text "[6] ", "Cleanup Superseded Updates Older than x Days" -Color
Yellow, Cyan
     Write-Color -Text "[7] ", "Cleanup Obsolete Updates" -Color Yellow, Cyan
     Write-Color -Text "[8] ", "WSUS Cleanup Wizard" -Color Yellow, Cyan
     Write-Color -Text "[9] ", "Cleanup Declined" -Color Yellow, Cyan
     Write-Color -Text "[10] ", "Shrink Files" -Color Yellow, Cyan
     Write-Color -Text "[11] ", "Shrink Database" -Color Yellow, Cyan
     Write-Color -Text "[12] ", "Reindex and Update Statistics" -Color Yellow, Cyan {
{} }
     Write-Color -Text "[RA] ", "Run all above steps sequentially" -Color Yellow, Cyan
     Write-Host
     Write-Color -Text "[Q] ", "Quit" -Color Yellow, Cyan
     Write-Host

}

#Region Initialize
#Check if running as admin
$admin = ([Security.Principal.WindowsIdentity]::GetCurrent().Groups -contains 'S-1-5-
32-544')
if ($admin -ne 'True') {

<!-- p.897 -->

    Write-Host "`nMust run PowerShell as administrator.`n" -ForegroundColor Yellow
    Exit
}
else {
    #Region LogCheck
    $ScriptLocation = Get-Location
    $LogFile = "$ScriptLocation\SUSDB-Maintenance.log"
    If ( -not (Test-Path -Path $LogFile -PathType Leaf)) {
        try {
            $null = New-Item -ItemType File -Path $LogFile -Force -ErrorAction Stop
            Write-Host "The file [$LogFile] has been created."
            Invoke-Expression $LogFile
        }
        catch {
            throw $_.Exception.Message
        }
    }
    else {
        Write-Host "Log file [$LogFile] already existed."
        Invoke-Expression $LogFile
    }
    #EndRegion LogCheck

    Write-Host "Script initialized - using native .NET SqlClient (no SQL module
required)" -ForegroundColor Green

}
#EndRegion Initialize

#Region ShowMenu
do {
    Show-Menu -Title 'SUSDB Maintenance'
    $selection = Read-Host "Please make a selection"
    switch ($selection) {
        'S' {
            #Change SQL Server
            ChangeSQL

       }'A' {
           #Update Count
           UpdateCount

        }'1' {
            #Update spDeleteUpdate procedure --> https://docs.microsoft.com/en-
US/troubleshoot/mem/configmgr/spdeleteupdate-slow-performance
            Update_spDeleteUpdate_Procedure

       }'2' {
           #Shrink Files
           ShrinkFile
       }'3' {
           #Shrink Database
           ShrinkDatabase

       }'4' {

<!-- p.898 -->

            #Reindex and Update Statistics
            ReindexStatistics

       }'5' {
           #Cleanup Sync History
           CleanUpSyncHistory

        }'6' {
            #Cleanup Superseded Updates
            Write-Host "Specify the number of days between today and the release date
for which the superseded updates must not be declined.`nThis should match
configuration of supersedence rules in SUP component properties, if ConfigMgr is being
used with WSUS.`n"
            $Global:DaysSupersededNotDeclined = Read-Host -Prompt 'Days '

            if ($Global:DaysSupersededNotDeclined -gt 0 -and
$Global:DaysSupersededNotDeclined -le 99) {
                Write-log -Message "Number of days entered :
$Global:DaysSupersededNotDeclined , proceeding with cleaning up superseded updates." -
severity 1 -component "Cleanup Superseded Updates"
                CleanupSupersedUpdates
            }
            else {
                Write-Host "`nInvalid entry, must be between 1-99.`n" -ForegroundColor
Red
                Write-log -Message "Number of days entered
[$Global:DaysSupersededNotDeclined] is invalid, must be between 1-99." -severity 3 -
component "Cleanup Superseded Updates"
            }

       }'7' {
           #Cleanup Obsolete Updates
           CleanupObsoleteUpdates

       }'8' {
           #WSUS Cleanup Wizard
           WSUSCleanUpWizard

       }'9' {
           #Cleanup Declined
           CleanUpDeclined

       }'10' {
           #Shrink File
           ShrinkFile
       }'11' {
           #Shrink Database
           ShrinkDatabase

       }'12' {
           #Reindex and Update Statistics
           ReindexStatistics

       }'RA' {

<!-- p.899 -->

            Write-log -Message "--> Begin run all" -severity 1 -component "Run All"

            Write-Host "Specify the number of days between today and the release date
for which the superseded updates must not be declined.`nThis should match
configuration of supersedence rules in SUP component properties, if ConfigMgr is being
used with WSUS.`n"
            $Global:DaysSupersededNotDeclined = Read-Host -Prompt 'Days '

            if ($Global:DaysSupersededNotDeclined -gt 0 -and
$Global:DaysSupersededNotDeclined -le 99) {
                Write-log -Message "Number of days entered :
$Global:DaysSupersededNotDeclined , proceeding with cleaning up superseded updates." -
severity 1 -component "Run All"
            }
            else {
                Write-Host "`nInvalid entry, must be between 1-99.`n" -ForegroundColor
Red
                Write-log -Message "Number of days entered
[$Global:DaysSupersededNotDeclined] is invalid, must be between 1-99." -severity 3 -
component "Run All"
                Exit
            }

            UpdateCount
            Update_spDeleteUpdate_Procedure
            ShrinkFile
            ShrinkDatabase
            ReindexStatistics
            CleanUpSyncHistory
            CleanupSupersedUpdates
            CleanupObsoleteUpdates
            WSUSCleanUpWizard
            CleanUpDeclined
            ShrinkFile
            ShrinkDatabase
            ReindexStatistics
            UpdateCount
            Write-log -Message "--> End run all" -severity 1 -component "Run All"

        }'q' {
            Write-Host
            Write-Host "Have a nice day!`n" -ForegroundColor Yellow
        }
        default {
            Write-Host
            Write-Host "You didn't make a valid selection.`n" -ForegroundColor Red
        }
    }

    Pause
}
until ($selection -eq 'q')
#EndRegion ShowMenu

<!-- p.900 -->

Last updated on 05/23/2026

<!-- p.901 -->

WSUS synchronization fails with
SoapException
This article helps you fix an issue where Windows Server Update Services (WSUS)
synchronization fails because of a decommissioned endpoint.

Original product version: WSUS - All versions, Windows Server 2016, Windows Server 2012 R2,
Windows Server 2012
Original KB number: 4482416

Symptoms
WSUS synchronization fails, and you receive the following error message:

  SoapException: Fault occurred
  at
  System.Web.Services.Protocols.SoapHttpClientProtocol.ReadResponse(SoapClientMessage
  message, WebResponse response, Stream responseStream, Boolean asyncCall)
  at System.Web.Services.Protocols.SoapHttpClientProtocol.Invoke(String methodName,
  Object[] parameters)
  at
  Microsoft.UpdateServices.ServerSyncWebServices.ServerSync.ServerSyncProxy.GetUpdateD
  ata(Cookie cookie, UpdateIdentity[] updateIds)
  at
  Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.WebserviceGetUpdateData(Up
  dateIdentity[] updateIds, List`1 allMetadata, List`1 allFileUrls, Boolean isForConfig)
  at
  Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.GetUpdateDataInChunksAndI
  mport(List`1 neededUpdates, List`1 allMetadata, List`1 allFileUrls, Boolean isConfigData)
  at Microsoft.UpdateServices.ServerSync.Cat

Additionally, an error message that resembles the following is logged in the WSUS log file
( %ProgramFiles%\Update Services\LogFiles\SoftwareDistribution.log ) on the WSUS server:

 Output

<!-- p.902 -->

<Date> <Time> Error WsusService.25 SoapUtilities.LogException USS ThrowException:
Actor =
https://fe2.update.microsoft.com/v6/ServerSyncWebService/ServerSyncWebService.asmx,
Method = "http://www.microsoft.com/SoftwareDistribution/GetUpdateData", ID=<ID>,
ErrorCode=InternalServerError, Message=
   at Microsoft.UpdateServices.Internal.SoapUtilities.LogException(SoapException e)
   at Microsoft.UpdateServices.Internal.WebServiceCommunicationHelper.
ProcessWebServiceProxyException(SoapHttpClientProtocol& webServiceObject, Exception
exceptionInfo)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.WebserviceGetUpdateData(Up
dateIdentity[] updateIds, List\1 allMetadata, List\1 allFileUrls, List\`1&
updatesWithSecureFileData, Boolean isForConfig)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.GetUpdateDataInChunksAndIm
port(List\1 neededUpdates, List\1 allMetadata, List\1 allFileUrls, Boolean
isConfigData)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.GetAndSaveUpdateMetadata(L
ist\1 updates)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.ExecuteSyncProtocol(Boolea
n allowRedirect)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.CatalogSyncThreadProcess()
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext
executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,
ContextCallback callback, Object state, Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,
ContextCallback callback, Object state)
   at System.Threading.ThreadHelper.ThreadStart()
<Date> <Time> Error WsusService.25 SoapUtilities.LogException USS ThrowException:
Actor =
https://fe2.update.microsoft.com/v6/ServerSyncWebService/ServerSyncWebService.asmx,
Method = "http://www.microsoft.com/SoftwareDistribution/GetUpdateData", ID=\<ID>,
ErrorCode=InternalServerError, Message=
   at Microsoft.UpdateServices.Internal.SoapUtilities.LogException(SoapException e)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.ExecuteSyncProtocol(Boolea
n allowRedirect)
   at
Microsoft.UpdateServices.ServerSync.CatalogSyncAgentCore.CatalogSyncThreadProcess()
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext
executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,
ContextCallback callback, Object state, Boolean preserveSyncCtx)
   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,
ContextCallback callback, Object state)
   at System.Threading.ThreadHelper.ThreadStart()

Cause

<!-- p.903 -->

This issue occurs if the WSUS servers are configured to use the old synchronization endpoint,
https://fe2.update.microsoft.com/v6 . This endpoint was fully decommissioned and is no

longer reachable after July 8, 2019.

Resolution
To fix the issue, change the synchronization endpoint in WSUS configuration to
https://sws.update.microsoft.com .

To do this, follow these steps on the topmost WSUS server that connects directly to Microsoft
Update, such as the root WSUS server in a WSUS hierarchy:

   1. Close all WSUS consoles.

   2. At an elevated PowerShell command prompt, run the following PowerShell scripts.

        ７ Note

        Don't run the scripts on a WSUS server that's not the topmost server. If the server
        isn't connected to the Internet, synchronization may fail.

     For WSUS version 3.x:

       PowerShell

       [void]
       [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administr
       ation")
       $server =
       [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer()
       $config = $server.GetConfiguration()
       # Check current settings before you change them
       $config.MUUrl
       $config.RedirectorChangeNumber
       # Update the settings if MUUrl is https://fe2.update.microsoft.com/v6
       $config.MUUrl = "https://sws.update.microsoft.com"
       $config.RedirectorChangeNumber = 4002
       $config.Save();
       iisreset
       Restart-Service *Wsus* -v

     WSUS servers that are running Windows Server 2008 (without the latest update) or earlier
     versions may be using the https://update.microsoft.com/v6 or
     https://www.update.microsoft.com synchronization endpoints. Because these versions of

<!-- p.904 -->

     Windows don't support SHA256 certificate authentication, use the following settings in
     the PowerShell scripts:

       PowerShell

       $config.MUUrl = " https://sws1.update.microsoft.com"
       $config.RedirectorChangeNumber = 3011

     For WSUS on Windows Server 2012 and later versions:

       PowerShell

       $server = Get-WsusServer
       $config = $server.GetConfiguration()
       # Check current settings before you change them
       $config.MUUrl
       $config.RedirectorChangeNumber
       # Update the settings if MUUrl is https://fe2.update.microsoft.com/v6
       $config.MUUrl = "https://sws.update.microsoft.com"
       $config.RedirectorChangeNumber = 4002
       $config.Save()
       iisreset
       Restart-Service *Wsus* -v

  3. Verify that WSUS synchronization succeeds.

More information
For more information about how to run PowerShell scripts, see What is PowerShell?.

Last updated on 03/30/2026
