---
title: "Exchange Powershell Script for Exporting message tracking advice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1393048/exchange-powershell-script-for-exporting-message-t
question_id: 1393048
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Powershell Script for Exporting message tracking advice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1393048/exchange-powershell-script-for-exporting-message-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i need to apply for the following to Multiple E-mail addresses/DL lists could anyone assist basically what i am trying to acheive is

Message trace, Message tracking for all Distribution Groups

i need to apply for the following to Multiple E-mail addresses/DL lists could anyone assist

$endDate = Get-Date  

$startDate = (Get-Date).AddMonths(-6)  

$sent = Get-MessageTrackingLog -resultsize unlimited -eventid send -Start $startDate -End $endDate -Sender "******@domainname.com"

$received = Get-MessageTrackingLog -resultsize unlimited -eventid receive -Start $startDate -End $endDate -Recipients "******@domainnme.com"  

$results = $send + $receive  

$results | Export-Csv -Path "filepath" -NoTypeInformation

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-16*

Hi @MTS,

Please have a check if the following script works for you:

```
$endDate = Get-Date

$startDate = (Get-Date).AddMonths(-6)

$DGlist = @("******@contoso.com", "******@contoso.com","******@contoso.com")

$results = @()

foreach ($DG in $DGlist) {
    $sent = Get-MessageTrackingLog -resultsize unlimited -eventid send -Start $startDate -End $endDate -Sender $DG | select MessageID,Sender,@{Name='Recipients';Expression={[string]::join(",", ($_.Recipients))}},MessageSubject
    $received = Get-MessageTrackingLog -resultsize unlimited -eventid receive -source SMTP -Start $startDate -End $endDate -Recipients $DG | select MessageID,Sender,@{Name='Recipients';Expression={[string]::join(",", ($_.Recipients))}},MessageSubject
    if ($sent.Count -eq 0 -and $received.Count -eq 0) {
        Write-Host "No messages sent or received for distribution group $DG"
    } 
    else {
        $results += $sent + $received
    }

}
$results | Export-Csv -Path "C:\temp\DG_usage.csv" -NoTypeInformation
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
