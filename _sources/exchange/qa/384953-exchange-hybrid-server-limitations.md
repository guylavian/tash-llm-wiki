---
title: "Exchange Hybrid Server Limitations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384953/exchange-hybrid-server-limitations
question_id: 384953
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid Server Limitations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384953/exchange-hybrid-server-limitations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

What are the Exchange hybrid server license limitations? Can we host few mailboxes on the server? Can we off-board mailboxes to on-premises server? Is there any Microsoft article mentioning these ?  

Regards,  

Mr.POP

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-07*

Hi,    

1 What limitation do you mean?    

2 yes    

3 yes For example, https://techgenix.com/off-boarding-email-office-365-exchange-2013-part1/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-06*

You can not move any mailboxes to a server running the free hybrid license if that is what you are asking:  

https://practical365.com/how-to-licence-exchange-hybrid-servers/  

If you are running Exchange Server 2010, 2013, 2016 or 2019 then you already have Exchange Hybrid capabilities built in to your Exchange Servers today.  

It’s important to note that when you add Exchange Hybrid servers to your Exchange 2003/2007 organization you cannot move any mailboxes to the servers if you wish to qualify for a “free” Exchange Hybrid licence. That means you can’t (for example) stage mailboxes from Exchange 2003 to Exchange 2010 first, before moving them to Office 365.
