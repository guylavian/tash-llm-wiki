---
title: "Exchange Hybrid with Teams.  Calendar does not Sync with On Premise Mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1598474/exchange-hybrid-with-teams-calendar-does-not-sync
question_id: 1598474
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Hybrid with Teams.  Calendar does not Sync with On Premise Mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1598474/exchange-hybrid-with-teams-calendar-does-not-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have been having a heck of a time trying to get Teams Calendars to sync properly with our Exchange 2019 CU14 on premise server.  Here is a summary of our set up:
Exchange 2019 CU14 Classic Hybrid - All OAuth checks come back successfully
Azure AD Connect set up with Exchange Checkbox selected an password hash synchronization, all successfully synced with no errors.
I think the problem is when we assign a Teams license (Microsoft Business Basic) to a user, it creates an online Exchange mailbox for them.  When I run the Teams Calendar Tab test in Microsoft Connectivity Analyzer it seems like Teams is determining that the mailbox is hosted online.  

We want to keep all our mailboxes on premise right now so how can I disable this online mailbox or at least set the 365 account to point to the on premise mailbox?  I have been searching and searching and can't seem to find a solution.
One article I read says that running this autodiscover test should return the local autodiscover:
https://outlook.office365.com/autodiscover/autodiscover.json?Email=******@contoso.com&Protocol=EWS&RedirectCount=5
This is my result from that:

```
{"Protocol":"EWS","Url":"https://outlook.office365.com/EWS/Exchange.asmx"}
```

How can I get this once and for all to point to my on premise Exchange Server?  I'm sure it involves disabling the online mailbox but I can't seem to find a way to do that or at the very least tell 365 that the mailbox is on premise.
Thanks!
Christos

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-27*

Hi @Christos Georgakis  
It seems you did not have the users synced correctly to Entra ID (Azure AD), thus a duplicated online mailbox was created.

For more details please follow the guide in this link:

My user has a mailbox both on-premises and in Exchange Online. Help!

Once you removed the Exchange online mailbox, please follow this link:

Configuring Teams calendar access for Exchange on-premises mailboxes

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
