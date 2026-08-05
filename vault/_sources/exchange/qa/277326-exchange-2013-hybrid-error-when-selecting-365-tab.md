---
title: "Exchange 2013 Hybrid error when selecting 365 tab on ECP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/277326/exchange-2013-hybrid-error-when-selecting-365-tab
question_id: 277326
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange 2013 Hybrid error when selecting 365 tab on ECP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/277326/exchange-2013-hybrid-error-when-selecting-365-tab (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all  

Hope you can help.   

We have Exchange 2013 and I've run the hybrid the migration wizard with no errors at all.  

My next step was to try to migrate a mailbox in ECP selecting the Office 365 tab and this is where I am stuck.  

I see the following error...  

login.microsoftonline.com refused to connect.  

If I use a private browsing window then it prompts for a login and I pop in the main 365 admin account, I then get the same error.  

I have ensured that all accounts I use have the Organization Management and Recipient Management role. I have confirmed that the MRSProxy service is on.  

Really not sure what to do next to resolve this and would really appricate any help you can offer.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Fantastic, thank you so much. Turned out our remote endpoint was wrong but fixed that and all looks great now.
