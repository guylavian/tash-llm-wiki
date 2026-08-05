---
title: "Exchange 2016 Cu18 causing owa issue in Chrome, same site cookies preventing login."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/178432/exchange-2016-cu18-causing-owa-issue-in-chrome-sam
question_id: 178432
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Cu18 causing owa issue in Chrome, same site cookies preventing login.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/178432/exchange-2016-cu18-causing-owa-issue-in-chrome-sam (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, since installing CU 18 we have problems accessing owa in Chrome because of the same site cookie issue. I though this was resolved in CU16? All other browsers are working fine. I disable same site cookies in my Chrome borswer and it works fine in Chrome. We are only on prem at the moment, no cloud integration.  

Anybody else have this experience with CU18?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-30*

The issues fixed in CU16 are not for on-premise Exchange scenario.    

Just found a similar issue wiith CU17: https://www.reddit.com/r/exchangeserver/comments/iphn9a/cant_get_into_owa_after_cu17_update/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Please refer to official doc for Samesite cookie issue and wait for next fix: https://learn.microsoft.com/en-us/office365/troubleshoot/miscellaneous/chrome-behavior-affects-applications#recommendations    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
