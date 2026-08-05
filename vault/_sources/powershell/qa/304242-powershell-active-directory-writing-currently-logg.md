---
title: "Powershell - Active Directory - Writing currently logged on user into computer description box"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304242/powershell-active-directory-writing-currently-logg
question_id: 304242
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Powershell - Active Directory - Writing currently logged on user into computer description box

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304242/powershell-active-directory-writing-currently-logg (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there, first post here :)     

I am wanting to write a script so that the last logged on user of a computer (more specifically, the Display Name) gets written into the computer Description of the computer that they are currently logged into.    

For example:    

Find the PC name    

On that PC, find the currently logged on user, and find the Display Name    

Then, on that PC, in the description in AD, write the Display Name of the currently logged in user    

    

I hope that made sense    

Many thanks    

Alex Rothwell

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-09*

Hi,    

Does this work for you？    

```
$server = 'W10GB54'  
$user = query user /server:$server |ForEach-Object {  
        ($_ -split '  '| Where-Object {$_}) -join ','} |   
        ConvertFrom-Csv | Select-Object -ExpandProperty USERNAME  
$displayname = Get-ADUser -Filter {Name -eq $user} -Properties DisplayName | Select-Object -ExpandProperty DisplayName  
Set-ADComputer -Identity $server -Description $displayname
```

Best Regards，    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
