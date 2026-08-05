---
title: "Error  HRESULT: 0x80070040 when i triy to modfiy GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/634938/error-hresult-0x80070040-when-i-triy-to-modfiy-gpo
question_id: 634938
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Error  HRESULT: 0x80070040 when i triy to modfiy GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/634938/error-hresult-0x80070040-when-i-triy-to-modfiy-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have 2 DCs win2k2016  an am facing this issue on both when i try to modify GPO,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-22*

Hello @Tabir Ali       

Usually is just a matter of network readiness while loading the GPOs to the client during boot.     

Try changing the next policy: Path "Computer Configuration/Admin Templates/System/Logon". Set the  "Always wait for the network at computer startup and logon" to Enabled    

If that doesn't resolve it I would recommend review the next Forum thread where different troubleshooting approaches have been suggested and the issue resolved     

https://social.technet.microsoft.com/Forums/windowsserver/en-US/dce1c1f3-63ea-4896-903b-660b20e3cd56/group-policy-not-applying-on-all-computers-other-serious-group-policy-problems?forum=winserverGP    

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
