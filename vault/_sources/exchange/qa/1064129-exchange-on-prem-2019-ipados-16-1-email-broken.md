---
title: "Exchange On-Prem 2019 / iPadOS 16.1 eMail Broken"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1064129/exchange-on-prem-2019-ipados-16-1-email-broken
question_id: 1064129
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange On-Prem 2019 / iPadOS 16.1 eMail Broken

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1064129/exchange-on-prem-2019-ipados-16-1-email-broken (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I spent a couple of hours on the phone with an Apple Engineer, and we were able to find that 'something' in iPadOS 16.1 has broken syncing with on-premise Exchange Server 2019/on-premise AD, using the apple mail app and Outlook app. They are still looking into it, but they suggested that I also look here to see if maybe there is a security update in the iPadOS that we need to tweak Exchange for.     

What we were able to test out/prove:    

iPadOS on the same WIFI network and on 5G on <16.1 - mail works fine.    

iPadOS on same WIFI network and on 5G on 16.1 and 16.2 beta - mail doesn't work at all.     

Restoring iPad to factory doesn't fix it. It happens on MDM and non MDM connected iPads. These iPads were able to connect to mail fine prior to update.     

What logs can I look at on Exchange to prove out that Exchange is what is not allowing the iPads to connect?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-22*

Hi Everyone, in my case iPhones connect no problem but iPads are the issue. The mailbox does install properly in the iPad but is not stable, the synchronization never ends. I updates iPad to verision 17 and still same problem. Any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-28*

I think Fiddler's new version isn't looking at the dll. I had to create the 'Inspectors' folder manually. When I run Fiddler, it is only showing when I open a web browser, it's not showing any of the back end devices that are using Active Sync.     

The second issue I have is that there isn't any logging happening even after turning it on. The Exchange ActiveSync mailbox log couldn't be processed: Logs couldn't be retrieved for your mobile device. Make sure your mobile device is synchronizing with Exchange before you start logging again and try to retrieve the logs.    

I see your note says Exchange 2013. This doesn't help on 2019.
