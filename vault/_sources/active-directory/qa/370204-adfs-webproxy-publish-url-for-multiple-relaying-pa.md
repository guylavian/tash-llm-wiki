---
title: "ADFS Webproxy publish URL for multiple relaying parties"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/370204/adfs-webproxy-publish-url-for-multiple-relaying-pa
question_id: 370204
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Webproxy publish URL for multiple relaying parties

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/370204/adfs-webproxy-publish-url-for-multiple-relaying-pa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a application hosted on cloud which use ADFS webproxy for SSO login. Now one more application is published on cloud. How to use the same webproxy to redirect request to the second application

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-25*

When you use ADSF and WAP solely for the authentication of your SaaS, there are no specific URL to publish on the WAP. The default configuration is enough. You do not need additional configuration to authenticate to another SaaS. You just need to create the relying party trust in ADFS.
