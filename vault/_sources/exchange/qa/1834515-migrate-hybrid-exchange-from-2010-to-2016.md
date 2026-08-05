---
title: "Migrate Hybrid Exchange from 2010 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1834515/migrate-hybrid-exchange-from-2010-to-2016
question_id: 1834515
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migrate Hybrid Exchange from 2010 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1834515/migrate-hybrid-exchange-from-2010-to-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am currently in the process of planning our Exchange migration from Exchange 2010 to Exchange 2016..

We use Exchange in a hybrid configuration. I am looking for some advice.

We do not have any public folders.

We have a single on prem domain and forest.

All mailboxes are hosted in Exchange Online.

We have some distribution groups and contacts on the exchange server.

We have a single Exchange 2010 server. We used to have two, but one was decommissioned some time ago.

Any and all advice / replies will be greatly appreciated. Thanks.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-24*

Hi, my answer above still applies. :) 

There is really no such thing as a "hybrid server", so when you are running the wizard again, point to the new 2016 server as the hybrid endpoint  :)  

You cant do an inplace upgrade to 2016 Exch, so you will need to bring up a new one. or simply use the existing Exch Server you are using to relay SMTP messages and point to that if its already at Exchange 2016 or above.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-24*

I'm sorry I didn't explain my current setup adequately. I have two Exchange Instants running in my environment. One is the regular Exchange server, which currently relays SMTP messages, creates contacts, and manages the old distribution lists. The second instance is the hybrid server, which has Exchange 2010 installed with the mailbox role installed. We no longer need the mailbox role because we migrated the mailboxes to Office 365.

We plan to decommission the regular exchange server and upgrade the hybrid server to Exchange 2016. What do you think about this scenario? 

Any advice/replies will be greatly appreciated.

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-23*

Before migrating from Exchange 2010 to Exchange 2016, several things to consider.

1.       Install the new server with Exchange Server 2016

2.       Install the required certificates

3.       Verify that send and receive connectors are configured and tested

4.       Update the URLs of virtual directories

5.       Move your distribution groups and contacts

When everything is done, you can decommission and uninstall Exchange 2010.

You can also refer this guide. 

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-22*

This should be pretty easy then

Bring up the 2016/2019 server.

Ensure you have a trusted 3rd party certificate on the new server:

https://learn.microsoft.com/en-us/exchange/certificate-requirements

Ensure you have the necessary FW ports open between the new and Exchange online ( Mimic the existing setup)

Run the Hybrid Wizard and point to the new server as the endpoints.

Create a new new custom receive connectors on the new server if they exist on the old.

Ensure the new server is set as a source server in all the send connectors. Remove the old server and verify mail flow.

Move the arbitration mailboxes from the 2010 server to 2016

https://www.alitajran.com/move-arbitration-mailboxes-in-exchange-server/

If all looks good, uninstall the 2010 server.
