---
title: "SPLA Exchange SPLA SAL Licensing Basic Licence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/250550/spla-exchange-spla-sal-licensing-basic-licence
question_id: 250550
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# SPLA Exchange SPLA SAL Licensing Basic Licence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/250550/spla-exchange-spla-sal-licensing-basic-licence (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am working for a service provider which offers hosted exchange.
We offer Exchange Server Hosted Exchange Standard SALs and now we want to offer Exchange Server Hosted Exchange Basic SAL.

The features for Basic SAL are self-explanatory	

> Outlook Web Access features that enable: E-Discovery, Exchange anti-spam, and Multi-Mailbox Search; Messaging and personal folder access; Internet mail protocol (SMTP, POP, IMAP) and Web browser access via any client; Personal Mail Folders, Address List, Calendar and Tasks (not shared with other users); Support for a single, second level domain for a single user or user organization; and Global Address List

But now I want to configure that in my hosted exchange.
We use Exchange Server 2016 and I deactivated a few features in the outlook web-app restrictions and via Powershell.
I also deactivated several features under mailbox functions by a testuser. All functions except Outlook on the web.

PowerShell said this, but I miss "Exchange Server 2016 Basic CAL" there.

> Get-ExchangeServerAccessLicense
> 
> ProductName          LicenseName                             UnitLabel TabulationMethod
> -----------          -----------                             --------- ----------------
> Exchange Server 2016 Exchange Server 2016 Standard Edition   Server    Net
> Exchange Server 2016 Exchange Server 2016 Enterprise Edition Server    Net
> Exchange Server 2016 Exchange Server 2016 Standard CAL       CAL       Net
> Exchange Server 2016 Exchange Server 2016 Enterprise CAL     CAL       Ne

How can I configure it right to be compliant in the future if someone by a basic license?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-01*

Hi @xiffus1987  ，    

PowerShell said this, but I miss "Exchange Server 2016 Basic CAL" there.    

According to this official link, the Get-ExchangeServerAccessLicense cmdlet returns a collection of these license names:    

-  Exchange Server Standard CAL    

-  Exchange Server Enterprise CAL    

-  Exchange Server Standard Edition    

-  Exchange Server Enterprise Edition    

So per my understanding, it's expected that the Basic SAL is not included in the results returned.    

Then when it comes to the question you asked, would you please  elaborate it a bit more so that we can understand better about the situation? From your description, are you currently using the Basic SAL in your environment and are trying to configure the OWA features? What exactly you wanted to configure and what you mean by "All functions except Outlook on the web"? More additional information would be appreciated.    

Furthermore, considering that the the issue sounds relevant to the licensing, personally I'd recommend also contacting Microsoft licensing support as they would be more familiar with license related questions and might provide more information about this.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
