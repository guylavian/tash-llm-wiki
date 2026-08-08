---
title: "Is it supported to replace the last exchange server 2010 with exchange management tools 2019?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2244063/is-it-supported-to-replace-the-last-exchange-serve
question_id: 2244063
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Is it supported to replace the last exchange server 2010 with exchange management tools 2019?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2244063/is-it-supported-to-replace-the-last-exchange-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm currently replacing a on-prem exchange environment, wondering if it's supported to replace the last Exchange Server 2010 with Exchange Management Tools 2019?

All mailboxes exist in office365, no mailbox is on-prem anymore, the move was performed with a hybrid exchange connector setup.

Currently I'm planning on shutting down the last Exchange Server 2010 as its beyond eol and planning to fully move to Exchange Online, some smtp configuration is still needed but it's the only thing that currently remains.

Am i going to stumble onto any issues considering the move was done from exchange 2010, will some attributes not be available if newer attributes have appeared in newer exchange versions?

Assuming Exchange Management Tools 2019 can be installed and supported by the current configuration, do I need to uninstall the Hybrid configuration that was put in place to perform the on-prem > cloud migration? 

Through research, removing the hybrid configuration will disable following:

-  Cross-premises availability: Allows you to see a user's free/busy information while scheduling a meeting, regardless of their mailbox premises.

Does the cross-premises functionality matter when the mailbox is sat in exchange online? Assuming I also schedule a meeting in Teams, will i still see availability status after removing the hybrid configuration?

Note: Currently we plan to maintain our local AD infrastructure, which means we will still run a Entra ID connector/sync.

Thanks in advance :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-08*

Hi @Qivra  , You cannot jump directly to Exchange 2019 if Exchange 2010 is still present. Hence, the double-hop (Exchange 2010 → 2016 → 2019) is essential.  

Microsoft now supports installing Exchange 2019 Management Tools only (starting with CU12 or later) in environments where directory synchronization (Entra ID / Azure AD Connect) is used and no mailboxes remain on-premises.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-08*

Hi @Qivra,

Welcome to Q&A!

You can safely replace your Exchange 2010 server with just the Exchange 2019 Management Tools (no full Exchange server needed). Since all mailboxes are already in Exchange Online and you're keeping Azure AD Connect running, here's what you need to know:

1.Exchange 2019 Management Tools** will work fine for managing Exchange Online recipients through your on-prem AD. This is Microsoft's officially supported method when keeping AD sync.

2.Don't remove the hybrid configuration yet** - you'll need it temporarily during the 2010→2019 transition to maintain attribute synchronization. Remove it only after:
All Exchange 2010 servers are decommissioned
Exchange 2019 management tools are installed and tested
You've confirmed no mail flow relies on hybrid connectors

3.Free/busy will keep working** after removing hybrid because:
Teams/Exchange Online use cloud-based availability data
Azure AD Connect syncs enough basic user data for scheduling
The only thing you'll lose is free/busy lookups between separate hybrid organizations

4.SMTP needs** can be handled by:
A simple SMTP relay service (like IIS or hMailServer)
Exchange Online mail flow connectors
Or keep the lightweight 2019 management server if you need full Exchange SMTP features

The key is to do this in order: (1) Install 2019 tools, (2) Migrate any remaining 2010-specific configs, (3) Decommission 2010, (4) Then decide whether to keep/demolish hybrid config.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in our [documentation]](https://aka.ms/msftqanotifications)) to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-04*

There is no path from 2010 to 2019, so you would prob need to Run the Forest prep steps individually then for 2016, then 2019. Havent tested that however. 

2010 would have to be completely gone. 

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/install-management-tools?view=exchserver-2019

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-04*

IF you are syncing then you need to keep at least once Exchange Server on prem for mgmt:

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange#why-you-may-not-want-to-decommission-exchange-servers-from-on-premises

Alternatively, look at:

https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools
