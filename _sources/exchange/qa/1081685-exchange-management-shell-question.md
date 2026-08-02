---
title: "Exchange management shell question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1081685/exchange-management-shell-question
question_id: 1081685
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
---
# Exchange management shell question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1081685/exchange-management-shell-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I need an exchange management shell script to give all users with full access on mailboxes 'reviewer' accessrights on the 'Inbox' of the corresponding folder.    

For now I've created this for my testcase:    

 $mailboxes = Get-Mailbox -identity gp -ResultSize Unlimited -Filter ('RecipientTypeDetails -eq "UserMailbox"')    

 foreach ($mailbox in $mailboxes)     

 {     

$Permissions =    

Get-MailboxPermission -Identity $mailbox.alias -ResultSize Unlimited |     

?{($.IsInherited -eq $false) -and     

($.User -ne "NT AUTHORITY\SELF") -and     

($_.AccessRights -like "FullAccess")} | select Identity, User, AccessRights     

foreach ($Permission in $Permissions) {    

```
Add-MailboxFolderPermission -Identity "$($mailbox.Alias):\Inbox" -User $Permission.user -AccessRights Reviewer  
Add-MailboxFolderPermission -Identity "$($mailbox.Alias):\Postvak IN" -User $Permission.user -AccessRights Reviewer
```

}    

}    

This works in Exchange Online Powershell, but it fails on the on premise exchange 2016 server with the following error:    

Cannot convert the "domain\username" value of type "Microsoft.Exchange.Configuration.Tasks.SecurityPrincipalIdParameter" to type "Microsoft.Exchange.Management.StoreTasks.MailboxFolderUserIdParameter"    

I believe this may be due to an incorrect loop.    

Can someone help me with this?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-10*

@Gerwin Persoon       

This issue is caused by the $Permission.user show in the domain/user format on Exchange on-premises.     

    

You need to change it to one of format below:    

     

Such as:    

```
$Permission.user.RawIdentity.split('\')[1].tostring()
```

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
