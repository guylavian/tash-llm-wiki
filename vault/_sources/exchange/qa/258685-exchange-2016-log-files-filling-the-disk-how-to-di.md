---
title: "Exchange 2016 log files filling the disk. how to directly clean up , already run the Circular logging on a Database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/258685/exchange-2016-log-files-filling-the-disk-how-to-di
question_id: 258685
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 log files filling the disk. how to directly clean up , already run the Circular logging on a Database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/258685/exchange-2016-log-files-filling-the-disk-how-to-di (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 log files filling the disk. how to directly clean up , already run the Circular logging on a Database

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-16*

Hi   

i face other issue on exchange , the exchange B auto start at 4 days ago   

the event log is   

Cluster node 'EXG01A' was removed from the active failover cluster membership. The Cluster service on this node may have stopped. This could also be due to the node having lost communication with other active nodes in the failover cluster. Run the Validate a Configuration wizard to check your network configuration. If the condition persists, check for hardware or software errors related to the network adapters on this node. Also check for failures in any other network components to which the node is connected such as hubs, switches, or bridges  

then EXG01B have restart , have any advise on this

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-10*

is it keep 7 days log? , i already move the log to E drive

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

have some command can directly to clear log first.? like

$executionPolicy = Get-ExecutionPolicy  

if ($executionPolicy -ne 'RemoteSigned') {  

Set-Executionpolicy RemoteSigned -Force  

}

$days = 7  

$IISLogPath = "C:\inetpub\logs\LogFiles\"  

$ExchangeLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Logging\"  

$ETLLoggingPath = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\ETLTraces\"  

$ETLLoggingPath2 = "C:\Program Files\Microsoft\Exchange Server\V15\Bin\Search\Ceres\Diagnostics\Logs"

Function CleanLogfiles($TargetFolder)  

{  

Write-Host -ForegroundColor Yellow -BackgroundColor Black $TargetFolder

```
if (Test-Path $TargetFolder) {
    $Now = Get-Date
    $LastWrite = $Now.AddDays(-$days)
    $Files = Get-ChildItem $TargetFolder  -Recurse | Where-Object { $_.Extension -in '.log', '.blg', '.etl' -and $_.LastWriteTime -le $lastwrite } | Select-Object -ExpandProperty FullName  

    foreach ($File in $Files)
    {
        Write-Host "Deleting file $File" -ForegroundColor "yellow";
        try {
            Remove-Item $File -ErrorAction Stop
        }
        catch {
            Write-Warning -Message $_.Exception.Message
        }

    }
}
else {
    Write-Host "The folder $TargetFolder doesn't exist! Check the folder path!" -ForegroundColor "red"
}
```

}

CleanLogfiles($IISLogPath)  

CleanLogfiles($ExchangeLoggingPath)  

CleanLogfiles($ETLLoggingPath)  

CleanLogfiles($ETLLoggingPath2)

i checked my exist enviroment is not enable CircularLogging

and our side concern after dismount and mount database have any effect for users outlook happen

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-05*

Hi @Louis Ruth   ,    

Do you mean after you running the circular logging, the space is not reduced?    

Have you followed this article: Configure circular logging for a mailbox database to configure circular logging for a database?    

If you did all these but the circular logging is still no useless, you could try to disable and re-enable it on this database and then re-mount this database to try.    

Also if you have multiple databases, you should run circular logging on every of them like Troy said. You could share some more details about this problem so we can better troubleshooting for you.    

Here is a guidance about the enabling circular logging: Exchange 2016 (& 2013) Enable Circular Logging, hope it could help you.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
