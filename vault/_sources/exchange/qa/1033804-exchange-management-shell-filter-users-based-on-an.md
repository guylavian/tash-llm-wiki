---
title: "Exchange Management Shell Filter users based on an existing attribute"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1033804/exchange-management-shell-filter-users-based-on-an
question_id: 1033804
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
---
# Exchange Management Shell Filter users based on an existing attribute

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1033804/exchange-management-shell-filter-users-based-on-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Exchange Management Shell I run these commands to try to set a couple of users remote powershell access to disabled:    

$DSA = Get-User -ResultSize Unlimited -Filter "(RecipientType -eq 'UserMailbox') -and (Title -like 'Sales Associate')"    

$DSA | foreach {Set-User -Identity $_ -RemotePowerShellEnabled $false}    

After I input the 2nd command, I get this response from the shell:    

cmdlet Set-User at command pipeline position 1    

Supply values for the following parameters:    

Identity:    

I am not sure what I am supposed to do. I got the instructions from control-remote-powershell-access-to-exchange-servers and it does not mention this part.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

@Chris Martinez       

Run command blow first, make sure it could find the correct users on your Exchange server:    

```
$DSA = Get-User -ResultSize Unlimited -Filter "(RecipientType -eq 'UserMailbox') -and (Title -like '*Sales Associate*')"  
$DSA
```

If there doesn't exist output, it means the filer that you used isn't correct. You need to modify the filter first.    

Here is an example in my lab:    

    

Please note, there exist * in the command. You also need to pay attention to the Space between the $_  and -RemotePowerShellEnabled.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
