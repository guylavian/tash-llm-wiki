---
title: "How to clear Exchange Logs without any impact for Exchange 2016 (CU19) C Drive Disk space increase fastly."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351164/how-to-clear-exchange-logs-without-any-impact-for
question_id: 351164
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to clear Exchange Logs without any impact for Exchange 2016 (CU19) C Drive Disk space increase fastly.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351164/how-to-clear-exchange-logs-without-any-impact-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support

I got the script for clearing logs. These are fine

is it safe to delete below the path of logs? after the backup completed?

Set execution policy if not set

$ExecutionPolicy = Get-ExecutionPolicy  

if ($ExecutionPolicy -ne "RemoteSigned") {  

Set-ExecutionPolicy RemoteSigned -Force  

}

Cleanup logs older than the set of days in numbers

$days = 2

Path of the logs that you like to cleanup

$IISLogPath = "C:\inetpub\logs\LogFiles\"  

$ExchangeLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Logging\"  

$ETLLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\ETLTraces\"  

$ETLLoggingPath2 = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\Logs\"  

$ExchangeLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\Logs\"

Clean the logs

Function CleanLogfiles($TargetFolder) {  

Write-Host -Debug -ForegroundColor Yellow -BackgroundColor Cyan $TargetFolder

```
if (Test-Path $TargetFolder) {
    $Now = Get-Date
    $LastWrite = $Now.AddDays(-$days)
    $Files = Get-ChildItem $TargetFolder -Recurse | Where-Object { $_.Name -like "*.log" -or $_.Name -like "*.blg" -or $_.Name -like "*.etl" } | Where-Object { $_.lastWriteTime -le "$lastwrite" } | Select-Object FullName
    foreach ($File in $Files) {
        $FullFileName = $File.FullName  
        Write-Host "Deleting file $FullFileName" -ForegroundColor "yellow"; 
        Remove-Item $FullFileName -ErrorAction SilentlyContinue | out-null
    }
}
Else {
    Write-Host "The folder $TargetFolder doesn't exist! Check the folder path!" -ForegroundColor "red"
}
```

}  

CleanLogfiles($IISLogPath)  

CleanLogfiles($ExchangeLoggingPath)  

CleanLogfiles($ETLLoggingPath)  

CleanLogfiles($ETLLoggingPath2)

But here i want mail notification like what are the files are deleted. those details to be sent by mail  

Please advise how to add this Mail notification part? in the existing script

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-12*

@Sathishkumar Singh      

Our forum does not support scripting on demand so far. If you need a script to complete a job, you may need to open a ticket to Microsoft which supported for it.    

About this existing script, you can modify those two places, then this script will generate and save a log:    

    

    

If you want to send it with email, you will need to writing another script to do it.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-08*

If anyone else want to have a read about the script. The original article with the script can be found in the below post:

https://www.alitajran.com/cleanup-logs-exchange-2013-2016-2019/

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-12*

yes, absolutely.   

The only logs you do not want to clear using a script are the Exchange database transaction logs.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

Thank you KyleXu

is it safe to cleanup below paths of logs?

$IISLogPath = "C:\inetpub\logs\LogFiles\"  

$ExchangeLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Logging\"  

$ETLLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\ETLTraces\"  

$ETLLoggingPath2 = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\Logs\"  

$ExchangeLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\Logs\"
