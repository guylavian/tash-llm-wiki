---
title: "Free/Busy no available in Exchange 2016/2019 conexisting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/256113/free-busy-no-available-in-exchange-2016-2019-conex
question_id: 256113
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Free/Busy no available in Exchange 2016/2019 conexisting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/256113/free-busy-no-available-in-exchange-2016-2019-conex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

installed Exchange 2019 into the same org as existing Exchange 2016.  Moving mailboxes and all seems to be fine except Exchange 2016 Outlook user can't see free/busy for Exchange 2019 user.  Outlook shows "No Information".  I opened a case with MS support.  The engineer said I need add a registry to enable TLS 1.2 client on all Exchange 2016 servers and a couple for .Net 4.0.  But the MS engineer I worked with for migration never mentioned that.  And I couldn't find any MS KB for Exchange 2019 migration showing that as required.    

Any idea?  

Thanks,  

Chris

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-02-02*

I would follow this doc and enable it on the 2016 side:  

https://tkolber.medium.com/exchange-2019-free-busy-issue-with-exchange-2013-2016-ca902ca543a8  

I suspect alot of documentation and support needs to be updated, so thats probably why it wasnt mentioned.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-03*

Hi @Yellow Tiger  ,    

I've seen a similar issue but in Exchange 2013/2019 coexistence which was finally resolved by enabling TLS 1.2 support on 2013. See link below:    

Users still on Exchange 2013 cannot see Exchange 2019 users free/busy info    

Note:The hyperlinks of the Exchange server TLS guidance mentioned in the answer have been changed, you may click the links below instead:    

Exchange Server TLS guidance Part 2: Enabling TLS 1.2 and Identifying Clients Not Using It    

Exchange Server TLS guidance Part 3: Turning Off TLS 1.0/1.1    

As mentioned in the discussion in that thread and also indicated in the official blog below, Exchange Server 2019 only uses TLS 1.2 out of the box, and removes legacy ciphers and hashing algorithms.     

Exchange Server 2019 Now Available    

Given this, I'd suggest preparing your Exchange Server 2016 by following the post in this blog, that is, upgrading to at least CU8 or CU9(if you need to disable TLS1.0 and TLS1.1) and installing the newest version of .NET and associated patches supported by your CU. Afterwards, refer to the blog shared by Andy or the "Exchange Server TLS guidance Part 2" mentioned earlier to enble TLS 1.2 on Exchange 2016.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
