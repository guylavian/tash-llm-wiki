---
title: "Hybrid Exchange - Migrated users unable to see on-prem room mailboxes/other shared mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236687/hybrid-exchange-migrated-users-unable-to-see-on-pr
question_id: 236687
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Hybrid Exchange - Migrated users unable to see on-prem room mailboxes/other shared mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236687/hybrid-exchange-migrated-users-unable-to-see-on-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Last week I completed a Hybrid Configuration setup between our on-prem Exchange 2016 servers and 365. I've migrated myself and a couple of other IT staff.    

I did a Full Hybrid Configuration using the Classic Hybrid Topology.    

So far everything appears to be working normally, however I no longer have access to any of the conference room calendars or mailboxes I had full access to pre-migration (all of which are still on-premises). Clicking on a conference room calendar in my Shared Calendars doesn't bring up anything at all (not even a blank calendar, it's like it doesn't even register that I clicked on it). I can click on on-prem calendars from user mailboxes and see their free/busy data, but not the room mailboxes.    

I found an article indicating that the default permission on these calendars is None and that I should change that to Free/Busy or one of its variants, but looking at the affected calendars they're already set to Reviewer (Full Details) so that isn't the issue.    

I looked at Organization - Sharing in the 365 EAC and it shows that sharing is enabled on the migration endpoint:    

    

Please advise.

## Answers

_No answers on this thread._
