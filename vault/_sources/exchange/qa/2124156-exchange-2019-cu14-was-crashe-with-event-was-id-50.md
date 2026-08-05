---
title: "Exchange 2019 CU14 was crashe with event WAS ID 5011"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2124156/exchange-2019-cu14-was-crashe-with-event-was-id-50
question_id: 2124156
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU14 was crashe with event WAS ID 5011

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2124156/exchange-2019-cu14-was-crashe-with-event-was-id-50 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a proble with Exchange 2019 CU14, which is accompanied by  event ID 5011, it means that IIS pools (MAPI, OWA, RPC, EWS etc) were crashed, of course, this is only a consequence, we cannot understand the cause yet. But there is a suspicion that the reason is in the backup driver. We have cyberprotect installed (https://cyberprotect.ru/products/backup/). After removing the agents, the problem went away. 

I saw the same cases, but we don`t have problemes with resource utilization:  

https://learn.microsoft.com/en-us/answers/questions/727386/exchange-2019-was-id-5011  

https://www.exchangeitup.net/2017/02/exchange-2016-100-cpu-and-event-id-5011.html

Has anyone encountered a similar problem?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-29*

Hi @Иван Кордяк,

Welcome to the Microsoft Q&A platform!

Event ID 5011 typically indicates that the IIS application pool for Exchange has crashed. This can be caused by a variety of factors, including third-party software conflicts such as backup agents.

Based on your description, removing the Cyber​​Protect backup agent seems to resolve the issue, which suggests they may be the culprit. This is consistent with other reports where third-party software, particularly backup or antivirus solutions, has caused similar issues.

Here are a few steps you can take to further investigate and potentially resolve the issue:

-  Even though you mentioned that there is no issue with resource utilization, it is still worth monitoring CPU, memory, and disk usage at the time of the crash. Tools such as Performance Monitor or Process Explorer can help with this.

-  Look for any related events in Event Viewer, especially at the time of the crash. Events 15004-15007 in the Application log may provide additional clues.

-  As a temporary measure, you can try to recycle the affected application pool from IIS Manager. This can sometimes help stabilize the service.

-  If the issue persists, make sure your Exchange Server OAuth certificate is not expired, as this can also cause the application pool to crash.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
