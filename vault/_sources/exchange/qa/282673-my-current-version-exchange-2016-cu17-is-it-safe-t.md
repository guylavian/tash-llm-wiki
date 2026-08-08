---
title: "My Current Version Exchange 2016(CU17) is it Safe to Upgrade CU19?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282673/my-current-version-exchange-2016-cu17-is-it-safe-t
question_id: 282673
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# My Current Version Exchange 2016(CU17) is it Safe to Upgrade CU19?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282673/my-current-version-exchange-2016-cu17-is-it-safe-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

My Current Version of Exchange 2016 is running in (CU17) is it Safe to Upgrade CU19?  

i have a Standalone Exchange Server.   

no test lab in my end.  

Any impact on CU19? Are can i wait for CU20? any customers review for CU19?  

Please advise

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

Hello Andy and Zhengqilou  

My Current Infra is Running 20GB Exchange2016(CU17)(Single Server)  

ADs:-  

Primary AD :-  

Secondary AD:-  

Child Domain:-  

CDC01  

CDC02  

RODC:-  

RODC1  

RODC2  

Total Mailboxes  

User Mailbox:- 119  

SharedMailbox:- 153  

Two DBs:  

DB01 (Main DB)  

DB02(Archive)  

If i want to test Upcoming Exchange CUs. i have to restore All the above servers?  

or   

any one Primary AD and Exchange Controller is enough to do the test  

Please advise

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-23*

Hi @SathishkumarSingh-0068 ,    

Yes you could upgrade to CU19 directly. It is recommended that users should always use the latest version, but since installing the CU would be a full setup, I would carefully consider Andy's suggestion.     

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
