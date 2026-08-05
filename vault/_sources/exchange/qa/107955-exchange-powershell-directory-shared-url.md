---
title: "Exchange powershell directory shared URL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/107955/exchange-powershell-directory-shared-url
question_id: 107955
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Exchange powershell directory shared URL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/107955/exchange-powershell-directory-shared-url (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have two exchange 2019 servers in DAG (like exch01.contoso.local and exch02.contoso.local). And I also have dns record like mail.contoso.com that points to those servers exactly  

I want to use https://mail.contoso.com/powershell URL in my scripts, but it looks like this URL is doen't work. When I tried to open it in browser, I've got 400 HTTP error  

At the same time, all the other directories (such as owa, ecp, autodiscover etc.) work well.  

https://exch01.contoso.local/powershell or https://exch02.contoso.local/powershell work well too.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-09-28*

@Alexander Burtsev       

Please use the following command to check your URL settings for PowerShell virtual directory:    

```
Get-PowerShellVirtualDirectory|fl identity,*url*
```

When you change to use mail.contoso.com, please make sure the InternalUrl or ExternalUrl is modified correctly. Additionally, in general we use http instead of https for PowerShell virtual directory. You can check the article provided by AndyDavid, test if http://mail.contoso.com/powershell works and can connect to Exchange successfully.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-25*

WHy do you want to connect to the Virtual directory like that?    

If you are trying to use remote powershell, then you need to connect like this:    

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-servers-using-remote-powershell?view=exchange-ps#connect-to-a-remote-exchange-server
