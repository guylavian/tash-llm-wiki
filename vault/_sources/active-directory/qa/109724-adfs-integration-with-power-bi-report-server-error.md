---
title: "ADFS integration with Power BI Report Server Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/109724/adfs-integration-with-power-bi-report-server-error
question_id: 109724
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS integration with Power BI Report Server Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/109724/adfs-integration-with-power-bi-report-server-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi everyone,    

I'm trying to setup a adfs login later with MFA on my Powerbi report server which will be access internally    

I've seen this article and follow the steps: https://learn.microsoft.com/en-us/power-bi/report-server/connect-adfs-wap-report-server    

Ive finished the guide and tried to access the site. but got an error. some of the screenshot is below    

hope you can help me    

Report Server Configuration    

    

when tried to access the URL configure on the external. I encounter an error

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-01*

The problem might be that the client communicates with the ADFS server not over the WAP server. Is this the case? Also, the SPN is invalid. It should be http/ndsg-infra-pbi.ndsginfra.com not http://.
