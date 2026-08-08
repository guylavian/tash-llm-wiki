---
title: "Exchange Server 2019 Need Help Blocking Display Name Spoofing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1086621/exchange-server-2019-need-help-blocking-display-na
question_id: 1086621
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server 2019 Need Help Blocking Display Name Spoofing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1086621/exchange-server-2019-need-help-blocking-display-na (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a rule that I was hoping would block display name spoofing.  These are emails that come from outside the organization, but have an internal user's display name.  Unfortunately, my rule doesn't seem to work, and I wanted to see if anyone had an idea on why.    

    

I also tried another rule, and it didn't work either.    

    

Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-14*

Hi @Michael Adams  ,    

I found the answer.    

Great to know that you've already thought of a solution and really appreciate it for your sharing!    

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others." and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, I would make a brief summary of this thread:    

[Exchange Server 2019 Need Help Blocking Display Name Spoofing]    

Issue Symptom:    

Create a rule to block Display Name Spoofing: These emails come from outside the organization but have an internal user's display name.    

The Solution:    

Set the conditions for the rule to:” A message header matches” and then for the field enter "FROM" and then person's name for the match.    

    

You could click the "Accept Answer" button for this summary to close this thread, and this can make it easier for other community members to see the useful information when reading this thread.     

Thanks!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-13*

I found the answer.  Set the condition to "A message header matches" and then for the field enter "FROM" and then then person's name for the match.
