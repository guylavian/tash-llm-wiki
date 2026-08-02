---
title: "using LDAPS query in powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/767092/using-ldaps-query-in-powershell
question_id: 767092
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# using LDAPS query in powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/767092/using-ldaps-query-in-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

We are using following powershell cmdlets to get user info.  

$AccountName = "Shashidhar.Joliholi"  

$Query = "(&(objectClass=user)(objectCategory=person)(samAccountName=$AccountName))"  

$UserInfo = Get-ADUser -LDAPFilter $Query  

We are planning to block LDAP and go with LDAPS in DCs. does it impact above powershell script. if yes, what modification need to be done on the powershell cmdlets to use LDAPS to get $UserInfo.   

can i use $UserInfo = Get-ADUser -LDAPFilter $Query -server dc.domain.com:636 ?  

Need your help!  

Thanks,  

Shashidhar Joliholi

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-11*

Out of interest how are you planning to block the use of LDAP and what changes are you planning to make so clients only connect on LDAPS/636?  

Gary.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-03-10*

Hi @shashidhar joliholi   ,    

No matter if you are using LDAP or LDAPS the query will always remain the same. The only difference is that the LDAP communication gets encrypted when using LDAPS.    

You don't need to change anything regarding the query.     

Hope I was able to answer your question.    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

Stoyan Chalakov
