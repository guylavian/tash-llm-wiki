---
title: "Two similar DLP policies were created in Exchange and Security complaince using US PII template. DLP from Security & complaince seems to be workingbut not the one created in exchange admin center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/409219/two-similar-dlp-policies-were-created-in-exchange
question_id: 409219
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Two similar DLP policies were created in Exchange and Security complaince using US PII template. DLP from Security & complaince seems to be workingbut not the one created in exchange admin center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/409219/two-similar-dlp-policies-were-created-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There are two similar DLP policies were created in EAC and in Security & Compliance using US PII template. The difference between these two is the action. The one created in EOP has action to reject the emails and in the Security portal it has just to notify the user. Just to let you know that the DLP policy is set to exchange only in S&C.  

We tested and found that the policy in security and compliance is working as expected but the one created in EAC as a transport rule does not trigger.  

what is the difference between these two and does security & compliance has priority on the one created in EAC?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-26*

@Ajaz Khan      

Here are detailed information about it: How DLP in the Security & Compliance Center works with DLP and mail flow rules in the Exchange admin center    

    

I think the policy that you created in Security & Compliance has synced to Exchange online, and working from Exchange online side.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
