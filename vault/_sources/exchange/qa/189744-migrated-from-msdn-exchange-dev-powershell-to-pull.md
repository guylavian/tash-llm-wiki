---
title: "[Migrated from MSDN Exchange Dev]  PowerShell to pull Full access from exchange account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189744/migrated-from-msdn-exchange-dev-powershell-to-pull
question_id: 189744
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]  PowerShell to pull Full access from exchange account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189744/migrated-from-msdn-exchange-dev-powershell-to-pull (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/a578f9a3-d42f-47e2-b612-f31654b5684a/powershell-to-pull-full-access-from-exchange-account?forum=exchangesvrdevelopment&prof=required  

I wrote this simple script to grab names and user ID's who have full access to a mailbox. It ran once, but now won't run again. Any help with syntax will be appreciated:  

$perm = get-mailboxpermission -identity [Mailboxname] | Where{$.User -like "U*" -and $.AccessRights -Like "FullAccess*"}  

 Foreach ($perm in $perms)  

{  

get-mailbox $perm.User | Select Name, Alias  

}  

If I look at the variable $perm.User, it is grabbing the user ID's I want, but for some reason the get-mailbox command is just returning nothing.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-08*

$perm.user will get results like "contoso\username", which cannot be identity of Get-Mailbox.    

Try the following commands please:    

```
$perms = get-mailboxpermission -identity user | Where{$_.User -like "U*" -and $_.AccessRights -Like "FullAccess*"}  
$perms | select @{Name="User";expression={(Get-Recipient $_.user.tostring()).displayname}} | foreach{  
get-mailbox $_.User  | Select Name, Alias  
}
```

Reference link: https://social.technet.microsoft.com/Forums/office/ru-RU/1a4c34a2-345a-45fc-88bd-87b020dd3d59/get-full-name-from-getmailboxpermission?forum=exchangesvrdevelopment    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
