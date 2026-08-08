---
title: "Exchange 2010 - 2016 hybrid setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126668/exchange-2010-2016-hybrid-setup
question_id: 126668
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 - 2016 hybrid setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126668/exchange-2010-2016-hybrid-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,   

i have a scenario where a customer still is running an Exchange2010 and they now want to migrate to Exchange online.  

There is no hybrid config yet.  

Can someone confirm my architecture :   

-  i install a new exchange 2016 next to the 2010 - mailboxes keep getting hosted on 2010  

-  i enable mrs endpoint proxy on the 2016 and load balance to the new 2016 server  

-  i run the hybrid config on this 2016 server  

-  i migrate the mailboxes that are hosted on ex2010 thru the ex2016 to O365   

thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-29*

Hi @Filip Soogen  ,    

i have a scenario where a customer still is running an Exchange2010 and they now want to migrate to Exchange online.    

By this, do you mean your customer are going to migrated to Exchange Online completely? If this is the case, as far as I know, you can go directly from Exchange 2010 to Exchange Online.     

If the customer still needs an on-premise Exchange server, considering that even if you run the Exchange 2010 in hybrid first, you'll need to run the HCW again in Exchange 2016 after it's introduced to update the hybrid configuration, so personally I would suggest moving to Exchange 2016 first, then run the HCW there.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-14*

that is exactly the reason why i want to deploy a 2016 next to the 2010 - to be in a supported environment...  

even if i run the hybrid wizard on the 2010 and move all mailboxes to O365 , i still have to upgrade the 2010 hybrid server to 2016 ...   

Don't know which path is the easiest ...

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-14*

That will work, yes.  

Note you can still just migrate directly from Exch 2010 even though support ran out yesterday.
