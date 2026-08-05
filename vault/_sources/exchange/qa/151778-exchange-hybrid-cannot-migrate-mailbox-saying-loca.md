---
title: "Exchange Hybrid: cannot migrate Mailbox saying local ex server:  refused to connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/151778/exchange-hybrid-cannot-migrate-mailbox-saying-loca
question_id: 151778
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Hybrid: cannot migrate Mailbox saying local ex server:  refused to connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/151778/exchange-hybrid-cannot-migrate-mailbox-saying-loca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,   

I have been moving mailboxes to online exchange successfully in the past.   

In the morning, I was asked to move an old legacy mailbox to Exchange online, I just found out when I click on Move Mailbox: To exchange online, sign in to Office 365. It gave me a blank page saying: Ex01 (local ex server) refused to connect.   

Do you know why?   

Thanks  

ML

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-07*

A new build version of Exchange admin center has been released and the mailbox migration location has changed.    

Click on '' New Exchange Admin Center'' at the left menu list of exchange admin center then select migration

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-01*

The same problem here. Tried Edge, Chrome, Firefox, Opera - private/non private. Tried different network, and different device. Enabled pop ups and redirecting, allowed cookies for [.]office.net,[.]live.com,[*.]microsoftonline.com. The problem still persists.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-10*

I'm facing the exact same scenario and would love to find a fix.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-05*

Hi,  

Please provide us with the Exchange server version and the type of migration. Also, check whether any changes made on the network firewall to block incoming/outgoing communication between the Exchange server and Office365.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

@Namless Shelter       

to exchange online, sign in to Office 365. It gave me a blank page saying: Ex01 (local ex server) refused to connect.    

Where do you try to create this migration request? As far as I know, there doesn't exist a step to "sign into Office 365"    

I would suggest you try to rerun HCW to check whether there exists issue in your organization. Then, login Exchange online admin center , then check whether the migration endpoint exist.    

Here is an article about how to migrate mailbox in hybrid, it may be useful to you: Move mailboxes between on-premises and Exchange Online organizations in hybrid deployments    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
