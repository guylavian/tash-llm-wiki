---
title: "Exchange 2013 ECP cannot search recent message tracking log"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/124384/exchange-2013-ecp-cannot-search-recent-message-tra
question_id: 124384
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 ECP cannot search recent message tracking log

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/124384/exchange-2013-ecp-cannot-search-recent-message-tra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello EE,  

Here is the thing: if I try to run message tracking log in Exchange admin center, the log can only display the messages sent to Sept, the messages sent in Oct won't be tracked. While if I use Exchange management shell to run Get-MessageTrackingLog cmdlet, the log includes the messages sent in Oct. What's wrong with the ECP?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-14*

Hi Lucas,  

Appreciate for your detailed info. My customer has closed the case so I cannot provide further info.   

"delivery report uses the EAC to perform a directed search on the mail tracking log", so the mail tracking log is different from the message tracking log? If so, where is the mail tracking log stored?   

Thanks,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-13*

To make it clear, what's the difference from message tracking log in EAC and Get-MessageTrackingLog cmdlet in Exchange management shell?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-13*

Check this link helps you - run-a-message-trace-and-view-results
