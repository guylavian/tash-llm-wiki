---
title: "Remove old Exchange OWA versions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327205/remove-old-exchange-owa-versions
question_id: 327205
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Remove old Exchange OWA versions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327205/remove-old-exchange-owa-versions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

We have 2 Exchange 2016 servers which have been running for more than 2 years now.  

We have applied several CU during this period and now we can see that significative amont of disk space is used by old OWA versions (in %ExchangeInstallPath%ClientAccess\Owa and %ExchangeInstallPath%ClientAccess\Owa\prem).  

How can I safely remove theses old versions ?  

Thank you.  

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

Hi @Joyce Shen - MSFT  ,    

Next reboot is planned next saturday night.    

I'll give you my feedback on next monday.    

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

OK. Surprized about MS Exchange Team has never address this behavior.  

I moved all folder which not correspond to our current servers version to another folder.  

Wait and see until our Exchange servers next reboot.  

Thank you.  

regards,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-23*

No there isnt  ;)  

If you look at the first article, you can see it references an old Technet forum question that I answered  :)   

https://social.technet.microsoft.com/Forums/en-US/f3731694-ae4a-47d8-b921-a61e47c2b757/remove-old-owa-files-after-cumulative-updates?forum=Exch2016GD  

I have always been of the opinion to just leave the old files there, but if you want to remove them, move them to another location first leaving the current ones and test :)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

Hi Andy and thank you for your answer.  

I've already seen these articles, but I'm not convinced about them as they are not Microsoft issued.  

Is there really not any official article about this context ?  

Regards,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-23*

I never do, but give it a try. Don't delete them just yet, move to another directory and test that everything still works. If no issues, remove them!  

https://webbanshee.net/remove-old-owa-versions/  

https://www.alitajran.com/remove-old-exchange-owa-files-to-free-up-disk-space/
