---
title: "Exchange 2016 - OWA using outdated and vulnerable components"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1531209/exchange-2016-owa-using-outdated-and-vulnerable-co
question_id: 1531209
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 - OWA using outdated and vulnerable components

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1531209/exchange-2016-owa-using-outdated-and-vulnerable-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am using on-premise Microsoft Exchange 2016 with web client - OWA. Recently, our internal PT team has flagged that we are using oudated and vulnerable components : jQuery v1.7.2 and jQuery UI v1.8.21 (jquery.owa.bundle.mouse.js) and also using insecure ciphers - AES with CBC (msrcrypto-aes.js).  

Will like to check if there will be any security patching or upgrade to address these?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-14*

Hi @J L  ，

Will like to check if there will be any security patching or upgrade to address these?
I've tried searching a lot but seems that currently there's no official document about the components you mentioned above concerning Exchange 2016.   

However, regarding the outdated jQuery library, I found the official article below states that it was indeed a known issue for Exchange 2019, and the resolution is to install CU14 for Exchange 2019：  

Exchange Server 2019 Setup installs outdated JQuery library  

When it comes to your situation (Exchange 2016), since there's no more official information available, from the perspective of Exchange, I'd recommend just making sure your Exchange servers are updated to the latest CU+SUs (CU23+Nov23SU as to today) and run the Exchange Server Health Checker to check if any additional steps are needed.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
