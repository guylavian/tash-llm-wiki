---
title: "Unable to open Active Directory in Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190380/unable-to-open-active-directory-in-domain-controll
question_id: 2190380
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Unable to open Active Directory in Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190380/unable-to-open-active-directory-in-domain-controll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am having a trouble opening active directory users and computers from my domain controller. 

When I try to open, it gives me an error message as:

"Naming information cannot be locates because: The specified domain either does not exist or could not be contacted. Contact your system administrator to verify if your domain is properly configured and is currently online.

I have tried restarting the AD services and reboot but still same.

Please advise if what can be done to solve this as this is the only DC that we have other than the secondary which is not working properly as well with the replication. 

Regards,

PA

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-20*

Not that it Reallyyyy matters but how many DC's do you have?

It sounds like you either are not connected to the source network or something really went wrong in your DNS.
