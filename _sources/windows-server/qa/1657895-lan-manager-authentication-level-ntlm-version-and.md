---
title: "LAN manager authentication level (NTLM) version and GPO problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657895/lan-manager-authentication-level-ntlm-version-and
question_id: 1657895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# LAN manager authentication level (NTLM) version and GPO problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657895/lan-manager-authentication-level-ntlm-version-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

My company running 1 AD forest and a few number of DCs.100 User PC.

Domain functional level 2016, DCs are 2016 or 2019. Clients are at least Win10.

Our audit found some NTLM v1 traffic (event id 4624) and suggest to disable it.

I check our DC GPO and the [Network security:LAN Manager authentication level]  setting is:

Send NTLMv2 response only/refuse LM

But I check the GPO for users and the [Network security:LAN Manager authentication level]  setting is:

Send NTLM response only

Is it the client sending NTLM v1 request?

Can I simply change the client GPO to Send NTLMv2 response only/refuse LM to stop the NTLM V1 traffic and no impact to users PC?

Please advise~thanks,have a nice day.

related KB here:

https://support.microsoft.com/en-us/topic/client-service-and-program-issues-can-occur-if-you-change-security-settings-and-user-rights-assignments-0cb6901b-dcbf-d1a9-e9ea-f1b49a56d53a

## Answers

_No answers on this thread._
