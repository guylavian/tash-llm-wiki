---
title: "Hybrid Exchange - Outlook Password prompt if not in VPN or LAN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1112047/hybrid-exchange-outlook-password-prompt-if-not-in
question_id: 1112047
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid Exchange - Outlook Password prompt if not in VPN or LAN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1112047/hybrid-exchange-outlook-password-prompt-if-not-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears    

We have an on-premise Exchange 2016 environment with Microsoft hybridation  (AD connect services are ok).    

After hybridation our users (all with on-premise mailboxes) noticed that when opening Outlook from home (nor in VPN neither in LAN), Outlook asks them to put the password.    

We're using, in my case, Office 2021 but the problem occurs with 2019 too.    

I verified lots of thing but there's n way to get out of this issue.    

Already trying updating clients, clearing credentials cache, still same issue.    

Thank in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-05*

Update    

I added the first entry to the MSOl Exchange but the result is the same, Outlook keeps asking password    

Any suggestion?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-01*

Dear @Andy David - MVP  

I tried Resolution 1 with no luck.  

Do I have to try with Resolution 2?  

Disable MAPI using Exchange Online Powershell

Based on this article I noticed that on my MSOnline I miss the first link

PS C:\> Get-MsolServicePrincipal -AppPrincipalId 00000002-0000-0ff1-ce00-000000000000 | select -ExpandProperty ServicePrincipalNames

https://autodiscover.exoip.com/  

https://mail.exoip.com/  

00000002-0000-0ff1-ce00-000000000000/mail.exoip.com  

00000002-0000-0ff1-ce00-000000000000/autodiscover.M365x877334.mail.onmicrosoft.com  

00000002-0000-0ff1-ce00-000000000000/M365x877334.mail.onmicrosoft.com  

00000002-0000-0ff1-ce00-000000000000/autodiscover.exoip.com  

00000002-0000-0ff1-ce00-000000000000/exoip.com  

00000002-0000-0ff1-ce00-000000000000/autodiscover.exoip.local  

00000002-0000-0ff1-ce00-000000000000/exoip.local  

00000002-0000-0ff1-ce00-000000000000/outlook.office365.com  

00000002-0000-0ff1-ce00-000000000000/mail.office365.com  

00000002-0000-0ff1-ce00-000000000000/outlook.com  

00000002-0000-0ff1-ce00-000000000000/*.outlook.com  

00000002-0000-0ff1-ce00-000000000000  

https://ps.compliance.protection.outlook.com  

https://outlook-sdf.office.com/  

https://outlook-sdf.office365.com/  

https://outlook.office365.com:443/  

https://outlook.office.com/  

https://outlook.office365.com/  

https://outlook.com/  

https://ps.protection.outlook.com/  

https://outlook-tdf.office.com/  

https://outlook-tdf-2.office.com/  

https://ps.outlook.com

Is it needed? Al the others are the same.

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-01*

Most likely its the direct connect feature in outlook which is assuming you have a mailbox in Exchange Online.    

https://learn.microsoft.com/en-us/outlook/troubleshoot/profiles-and-accounts/unexpected-autodiscover-behavior    

This article shows how to change that behavior:     

Test it out and see with a few clients:    

https://medium.com/jj365/outlook-issue-with-direct-connect-to-office365-352dd29de65
