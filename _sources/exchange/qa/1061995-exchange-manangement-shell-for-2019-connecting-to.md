---
title: "Exchange Manangement Shell for 2019 Connecting to an Exchange 2016 Mailbox Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1061995/exchange-manangement-shell-for-2019-connecting-to
question_id: 1061995
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Manangement Shell for 2019 Connecting to an Exchange 2016 Mailbox Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1061995/exchange-manangement-shell-for-2019-connecting-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

GOod Morning,     

We are in the process of upgrading our on-premises Exchange to EX2019 from EX2016.     

I use a jump box to connect to Exchange management products.  I recently upgraded this server to W2019, removed EX2016 and installed EX2019.     

This server only has Exchange Management tools, does not hold any maillboxes or any other roles.  The EX2016 mailbox servers are still up and running and will be until we complete the cut over.    

When I go to the Exchange 2019 folder in start menu, and launch Exchange Management shell, it still connects to one of the current EX2016 mailbox servers.  I would of thought it would of connected an EX2019 mailbox server.  I can run Connnect-Server -Server ex2019Server.domain.com, but it still defaults to the EX2016 mailbox server at each launch.  Is there a way to make sure when I launch EX2019 Management Shell it defaults to connect to an EX2019 Mailbox server.     

Thank You

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-02*

Kyle-Xu,     

Thank you for the response.      

We will utilize the command lines for now to connect to the EX2019 from my proxy server.     

Thank You

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-25*

```
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http:///PowerShell/ -Authentication Kerberos -Credential $UserCredential
```

Set the ServerFQDN to the 2019 server    

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-servers-using-remote-powershell?view=exchange-ps
