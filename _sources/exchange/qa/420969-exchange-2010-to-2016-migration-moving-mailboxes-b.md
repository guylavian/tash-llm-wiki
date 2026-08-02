---
title: "Exchange 2010 to 2016 migration - moving mailboxes back"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/420969/exchange-2010-to-2016-migration-moving-mailboxes-b
question_id: 420969
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 to 2016 migration - moving mailboxes back

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/420969/exchange-2010-to-2016-migration-moving-mailboxes-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

As per a previous post I have made I am starting a migration from Exchange 2010 to 2016 and am currently doing some testing.  

If I move a mailbox from 2010 to 2016 Outlook doesn't automatically register the change and it seems I have to restart  MSExchangeAutodiscoverAppPool   as per this article:  

https://support.microsoft.com/en-us/topic/outlook-logon-fails-after-mailbox-moves-from-exchange-2010-to-exchange-2013-or-exchange-2016-bd3f59ed-c521-4349-5c00-c49717b5e04d  

But I also need to test moving the mailboxes back to 2010 in case I need to for any reason, however unlikely.  

When I do this, the above fix doesn't work and I need to create a new email profile in Outlook.  

For one or two users this would not be a problem but when it is time to move the mailboxes for real there will be hundreds. As I said, moving back is probably unlikely but it would be good if we had a more central solution in case we needed it.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-04*

Hi @jarweb  ,    

Found the thread below which is about a similar situation. According to the discussion there, it seems that restarting MSExchangeAutodiscoverAppPool on both servers doesn't help either. So it's likely that currently educating the affected users to recreate their Ouutlook profile in case the issue occurs would be the only way to work this around.    

Move mailboxes back to Exchange 2010 from Exchange 2016 cu5    

"Recycled the autodisc. apppol och both Exchange 2010, no luck still same problem in Outlook clients"    

By the way, as indicated in the link you shared, when mailboxes are moved from Exchange 2010 to Exchange 2016, the Outlook client can remain disconnected for "up to 12 hours", which means, it may automatically get reconnected after wating for up to 12 hours. So I am assuming if possible, you may consider testing by giving it some time and see if this applies as well when a mailbox is moved back to Exchange 2010 from Exchange 2016. If it works, an alterternative could be moving the mailboxes back in non-working hours like weekends or holidays. But still, it's not recommended to move mailboxes back.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-03*

Well, going back is always different  :)   

If restarting the app pool (s) on the 2010 server as well doesnt work, I think you are probably stuck and will need to recreate the profile.
