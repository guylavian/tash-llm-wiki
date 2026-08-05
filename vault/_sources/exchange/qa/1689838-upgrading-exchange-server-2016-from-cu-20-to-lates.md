---
title: "Upgrading Exchange Server 2016 from CU 20 to latest CU that is in Hybrid."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689838/upgrading-exchange-server-2016-from-cu-20-to-lates
question_id: 1689838
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Upgrading Exchange Server 2016 from CU 20 to latest CU that is in Hybrid.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689838/upgrading-exchange-server-2016-from-cu-20-to-lates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have Exchange Server 2016 that is currently on CU 20 and I would like to upgrade it to the latest CU 23. We are in Hybrid and on prem is primarily used for SMTP relay and initial on boarding of users/mailboxes that are then migrated to O365. I am looking for upgrading on Prem exchange in hybrid mode process. There is lots of documentation but that relates to on prem only upgraded. Anything different that I would need to do for Hyrbid environment.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-31*

Nope, its really the same.

You are pretty far behind so its important to catch up ASAP.

first prep the forest: (You can skip this step if this is a single domain AD forest)

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019

Then run setup and upgrade to CU23:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019

Then upgrade to the lastest security updates:

https://techcommunity.microsoft.com/t5/exchange-team-blog/released-april-2024-exchange-server-hotfix-updates/ba-p/4120536

Then enable Exchange Extended Protection:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection?view=exchserver-2019
