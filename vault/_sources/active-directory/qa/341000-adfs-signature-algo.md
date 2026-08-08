---
title: "adfs signature algo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341000/adfs-signature-algo
question_id: 341000
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# adfs signature algo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341000/adfs-signature-algo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A third party app was set to sha256 in the relying party trust. It worked fine until one day. The support had us change it back to sha1, which worked. The app provider later restarted their service after which sha256 worked again, that is, for sometime.   

One thing that was observed when it didn't work was the saml response doesn't have a full response in the sense attributes are not sent over. We have applications that don't have any issues with sha256 but this particular one. Adfs is 3.0.   

The vendor thinks its the adfs not sending over full saml response. But the same setting worked when initially set up and also after a service restart on their end. Any insight into where the problem may lie? Could saml request be a possible factor?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-03*

If you want to check if your rules are issuing the proper claims in your token, I recommend you to use the Claim-X Ray test relying party trust.   

Configure it as you configured your other applications and check if you are sending the right stuff.
