---
title: "AD - passwords expire after 40-ish days despite GPO set to 365 days"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194989/ad-passwords-expire-after-40-ish-days-despite-gpo
question_id: 2194989
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# AD - passwords expire after 40-ish days despite GPO set to 365 days

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194989/ad-passwords-expire-after-40-ish-days-despite-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there!

We recently set our password expiry to 365 days using the Default Domain Policy GPO. I had all users change their passwords at the same time. Now, 5 weeks or so in, all users are receiving notifications their passwords are about to expire, which is clearly too early based on the 365 days set in the GPO.

Things I've looked into:

-  I have checked with gpresult /R and the policy is being applied to our workstations.

-  I have checked the pwdLastSet attribute on some of the users in question, and it's 19/03/24 or similar. It's currently 25/04/24, and passwords are supposedly expiring in 4 days. That would be similar of a maxAge of about 40, give or take.

-  I have checked all other GPOs, and there are none that set anything password related.

-  after some googling I saw there is also a registry entry controlling the password age. I've checked on our DC and it was set to 30 days. My understanding is the GPO would take precedent. Still, I have now set this to 365, just in case.

-  there is only one DC, so this is not a sync issue.

Question:

What else, other than GPOs, might control password maxAge in an AD, and how can I debug this?

Thanks for your help!

## Answers

_No answers on this thread._
