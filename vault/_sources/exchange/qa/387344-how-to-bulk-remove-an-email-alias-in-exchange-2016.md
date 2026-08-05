---
title: "how to bulk remove an email alias in Exchange 2016?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387344/how-to-bulk-remove-an-email-alias-in-exchange-2016
question_id: 387344
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# how to bulk remove an email alias in Exchange 2016?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387344/how-to-bulk-remove-an-email-alias-in-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys/gals,    

How would should I go about removing an email address alias for all of my mailboxes?     

Currently mailboxes have the following:     

SMTP:user1@mathieu.company  .com    

smtp:user1@mathieu.company  .mail.onmicrosoft.com    

smtp:user1@xyz  .com (I want to remove this alias)    

X400    

x400    

x500    

Thanks,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-10*

Hi @Safs-3080,    

Based on my research and test, the following scripts can be used to bulk remove a secondary smtp email address.     

You can copy and paste the below code in Notepad, save it as a.ps1 file and give it a name such as "Remove-SMTP.ps1", put it in a folder like C:\scripts, then you would be able to bulk remove all SMTP addresses with the domain xyz.com by running the script. Before running the script, it's suggested to add "-WhatIf" after "Set-Mailbox $Mailbox -EmailAddresses @{remove = $_ } " to take a look at what will happen.    

```
Start-Transcript -Path C:\temp\Remove-SMTP-Address.log -Append  
$Mailboxes = Get-Mailbox -ResultSize Unlimited  
   
foreach ($Mailbox in $Mailboxes) {  
  
        $Mailbox.EmailAddresses | Where-Object { $_.AddressString -like "*@xyz.com" } | ForEach-Object {  
   
        Set-Mailbox $Mailbox -EmailAddresses @{remove = $_ }   
   
        Write-Host "Removing $_ from $Mailbox Mailbox" -ForegroundColor Green  
    }  
}  
Stop-Transcript
```

    

    

For more details, hopefully you can find the article below helpful:    

Bulk remove secondary SMTP address with PowerShell    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
