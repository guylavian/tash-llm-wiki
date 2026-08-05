---
title: "Should the custom health probe (/adfs/probe) on the Azure Application Gateway be configured to use HTTP or HTTPS?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841949/should-the-custom-health-probe-adfs-probe-on-the-a
question_id: 1841949
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-application-gateway", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
---
# Should the custom health probe (/adfs/probe) on the Azure Application Gateway be configured to use HTTP or HTTPS?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841949/should-the-custom-health-probe-adfs-probe-on-the-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are hosting an ADFS farm on Azure, including an external Application Gateway configured with two WAP servers in its backend pool. Currently, the health probe uses the HTTP protocol with the path `/adfs/probe`, as recommended by Microsoft. However, we are unable to associate the health probe with the backend setting, which is configured to use the HTTPS protocol. Should we change the health probe to use the HTTPS protocol to resolve this issue, and is this configuration supported by the Application Gateway?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-08-02*

@pavan b a  ,

Welcome to the Microsoft Q&A Platform. Thank you for reaching out & I hope you are doing well.

From your comment,

-  It is evident that that the backend's health page(/adfs/probe) is not responding to HTTPS (Port 443)

-  However, may I ask if the backend service as a whole is capable of responding over HTTPS

-  If not, 

-  Then there is no point is using a HTTPS BackendSettings

-  You can simply use a HTTP BackendSettings

-  If yes, 

-  Then can you share the document where Microsoft recommends the use of HTTP Protocol for health check up with Application Gateway?

-  Or is this a POC design

Cheers,

Kapil
