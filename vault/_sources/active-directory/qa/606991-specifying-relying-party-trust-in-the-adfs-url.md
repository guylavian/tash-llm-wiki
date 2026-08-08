---
title: "specifying relying party trust in the ADFS url"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/606991/specifying-relying-party-trust-in-the-adfs-url
question_id: 606991
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# specifying relying party trust in the ADFS url

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/606991/specifying-relying-party-trust-in-the-adfs-url (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have done this before but could not find the reference anymore. How can I construct the URL to launch the login page for a specific relying party trust for ADFS. e.g. https://adfs.domainname.com/relying_party_A.  

Thanks.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-28*

I think I found the answer.  

https://<host>:<port>/adfs/ls/IdpInitiatedSignOn.aspx?loginToRp=<partnerUrl>
