---
title: "Count total items with Exchange 2016 Inbox and Send Items for all users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327308/count-total-items-with-exchange-2016-inbox-and-sen
question_id: 327308
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Count total items with Exchange 2016 Inbox and Send Items for all users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327308/count-total-items-with-exchange-2016-inbox-and-sen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are looking for a way to count / list total number of  items with all users Mailboxes specific to Inbox & Sent Items. The output should list only the total item count for the entire organization and no need to display per user  (we already prepared  a report per user inbox / sent items folders with Getmailboxfolderstatistics)  

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-23*

Hi,  

Please try using the below command and see if that gives the required output.  

[Int] $intInbox = $intSent = 0  

Get-Mailbox -ResultSize Unlimited | Get-MailboxFolderStatistics -FolderScope Inbox | Where {$_.Name -match “Inbox”} | Select ItemsinFolderandSubfolders | ForEach {$intInbox++}  

Get-Mailbox -ResultSize Unlimited | Get-MailboxFolderStatistics -FolderScope "Sent Items" | Where {$_.Name -match “Sent Items”} | Select ItemsinFolderandSubfolders | ForEach {$intSent++}  

Write-Host "Organization Inbox Items:  ",$intInbox  

Write-Host "Organization Sent Items:  ",$intSent  

Or alternatively, you can export the inbox items and sent items of all mailboxes into a CSV and use Excel to get the overall count which might be simpler.  

Get-Mailbox -ResultSize Unlimited | Get-MailboxFolderStatistics -FolderScope Inbox | Where {$_.Name -match “Inbox”} | Sort-Object DisplayName, ItemsinFolderandSubfolders -Descending | Export-csv c:\temp\MailboxItemCountInbox.csv  

Get-Mailbox -ResultSize Unlimited | Get-MailboxFolderStatistics -FolderScope "Sent Items" | Where {$_.Name -match “Sent Items”} | Sort-Object DisplayName, ItemsinFolderandSubfolders -Descending | Export-csv c:\temp\MailboxItemCountSentItems.csv  

If the above suggestion helps, please click on "Accept Answer" and upvote it. Thanks for understanding.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

Thank You All. We used below one to get the total Inbox & Sent Items at organization level

(Inbox)  

$mailboxes = @(Get-Mailbox -ResultSize Unlimited)  

[Int] $inboxstats = 0  

foreach ($mailbox in $mailboxes)  

{  

$inboxItems = Get-MailboxFolderStatistics $mailbox -FolderScope Inbox | Where {$.FolderPath -eq "/Inbox" -and $.FolderType -eq "Inbox"}  

$inboxstats += $inboxItems.ItemsinFolderandSubfolders  

}  

Write-Host "Organization Inbox Items: $inboxstats" -ForegroundColor DarkGreen

(Sent Items)  

$mailboxes = @(Get-Mailbox -ResultSize Unlimited)  

[Int] $sentitemsstats = 0  

foreach ($mailbox in $mailboxes)  

{  

$sentItems = Get-MailboxFolderStatistics $mailbox -FolderScope SentItems | Where {$.FolderPath -eq "/Sent Items" -and $.FolderType -eq "SentItems"}  

$sentitemsstats += $sentItems.ItemsinFolderandSubfolders  

}  

Write-Host "Organization Sent Items: $sentitemsstats" -ForegroundColor DarkGreen

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

@LMS       

If you want to know the amount of maisl sent and received over a period of time, you can use script below:    

```
$From = "3/1/2021"  
$To = "3/24/2021"  
  
$intSent = 0  
$intRec = 0  
  
$Mailboxes = Get-Mailbox -ResultSize unlimited  | where {$_.RecipientTypeDetails -eq "UserMailbox"}  
  
foreach ($Mailbox in $Mailboxes){  
Get-TransportService | Get-MessageTrackingLog -Sender $Mailbox.PrimarySmtpAddress -ResultSize Unlimited -Start $From -End $To | ForEach {  
    If ($_.EventId -eq "RECEIVE" -and $_.Source -eq "SMTP") {  
        $intSent ++  
    }  
}  
  
Get-TransportService | Get-MessageTrackingLog -Recipients $Mailbox.PrimarySmtpAddress -ResultSize Unlimited -Start $From -End $To | ForEach {  
    If ($_.EventId -eq "DELIVER") {  
        $intRec ++  
    }  
}  
}  
  
Write-Host "Total Sent:"$intSent  
Write-Host "Total Receive:"$intRec
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
