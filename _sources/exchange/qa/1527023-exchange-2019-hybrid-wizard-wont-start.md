---
title: "Exchange 2019 hybrid wizard won't start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1527023/exchange-2019-hybrid-wizard-wont-start
question_id: 1527023
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 hybrid wizard won't start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1527023/exchange-2019-hybrid-wizard-wont-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I setup a new install of Exchange 2019 in lab.  I'm in the ECP and trying to launch the Hybrid wizard.  

It prompts for download in edge but then fails.

What is the fix for this?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-02-07*

OMG I figured it out.  

In lab I was just using the default Domain\Administrator account.    

Once I created a new account with the same rights it started right away.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-08*

OMG I figured it out.> In lab I was just using the default Domain\Administrator account.> Once I created a new account with the same rights it started right away.

Hi @ComputerHabit  ，  

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : ) 

[Exchange 2019 hybrid wizard won't start]  

Issue Symptom:  

When trying to launch the Hybrid wizard in a new install of Exchange 2019 in lab, it prompts for download in edge but then fails.  

Solution:  

“In lab I was just using the default Domain\Administrator account.
Once I created a new account with the same rights it started right away.”

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-07*

Sounds like firewall issues. Does that lab have access to the internet?
