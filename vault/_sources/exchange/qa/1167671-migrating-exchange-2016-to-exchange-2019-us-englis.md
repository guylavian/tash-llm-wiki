---
title: "Migrating Exchange 2016 to Exchange 2019 US English Only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167671/migrating-exchange-2016-to-exchange-2019-us-englis
question_id: 1167671
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrating Exchange 2016 to Exchange 2019 US English Only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167671/migrating-exchange-2016-to-exchange-2019-us-englis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in need to migrate Exchange 2016 with Unified Messaging and multiple languages to Exchange 2019 with US English only language due to compliance issues. I read that Unified Messaging is no longer a part of 2019 correct? If this is true this is good because I do not need it. However, I wanted to ask if there is a way to install Exchange 2019 in US-English only meaning no other languages at all. Please advise. Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-06*

Hi @Oscar Gonzalez  ,

There are no switches in the official documentation that can be selected to install language packs, except for UM language packs for Exchange 2016.

However, this switch is no longer needed in Exchange 2019.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-04*

I dont know of any supported way to remove the client language packs:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deployment-ref/language-support?view=exchserver-2019

But yes, UM is not in 2019:

https://learn.microsoft.com/en-us/exchange/new-features/discontinued-features?view=exchserver-2019#discontinued-features-from-exchange-2016-to-exchange-2019
