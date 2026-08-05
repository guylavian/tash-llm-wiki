---
title: "Exchange 2019 Pure On-Premise - Outlook Clients Receiving Modern Authentication Prompt"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182311/exchange-2019-pure-on-premise-outlook-clients-rece
question_id: 182311
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 Pure On-Premise - Outlook Clients Receiving Modern Authentication Prompt

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182311/exchange-2019-pure-on-premise-outlook-clients-rece (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Exchange 2019 environment that is purely on-premise (no hybrid). Users that have an archive mailbox (online archive) provisioned for their account erroneously receive the modern authentication prompt when launching Outlook. Users without an archive mailbox do not seem to get this prompt, and everything works as expected. This occurs with Office 2019 and Office 365 (and if memory serves me correctly 2016 as well).  

For domain-joined workstations I've been able to work around this by deploying the "ExcludeExplicitO365Endpoint" registry value, but need to solve this issue for Outlook on computers which I have no control over. For what it's worth Autodiscover is configured and working properly.  

Any insight into this long-standing issue would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

@jayuw  

You can also use group policy to apply change on all domain-joined computers, those two articles will be useful to you:

-    Unexpected Autodiscover behavior when you have registry settings under the \Autodiscover key

-    How to control Outlook AutoDiscover by using Group Policy

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-01*

I was actually going to suggest that you simply put that reg key in a file/web/Box Drive location that any user can get to and if they have issues, they click on it to add to the registry.
