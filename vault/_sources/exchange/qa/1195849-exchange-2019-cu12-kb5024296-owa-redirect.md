---
title: "Exchange 2019, CU12,KB5024296 - OWA redirect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195849/exchange-2019-cu12-kb5024296-owa-redirect
question_id: 1195849
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
---
# Exchange 2019, CU12,KB5024296 - OWA redirect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195849/exchange-2019-cu12-kb5024296-owa-redirect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After installing CU12 and update KB5024296 users are after login forwared to our homepage.
The OWA url is like https://mail.ourcompany.nl/owa. The login screen is shown.  

When the user login is succesfull the  redirect is to https://ourcompany.nl.
We didn't change the exchange configuration and before its wordked fine.
Where can I find the redirect reason?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-04*

Hi @Marc Looren / MHL Solutions ,

I updated KB5024296 in my environment, and the URL of OWA did not redirect, so it should not be the update of SU that caused this issue.  

Please check the OWA virtual directory settings in EAC and http redirection in IIS for any changes.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
