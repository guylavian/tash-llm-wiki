---
title: "Impact of MD5 Disable via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1222041/impact-of-md5-disable-via-gpo
question_id: 1222041
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Impact of MD5 Disable via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1222041/impact-of-md5-disable-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,
We are planning to disbaled the MD5 via GPO with following registry
HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Hashes\MD5 set `DWORD` value `Enabled` to `0`
Does that make any impact to windows machines in the term of Authentication or Any other things.
Please advise

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-13*

Hello Loganathan R,  

Thank you for posting in our Q&A forum.  

Q: Does that make any impact to windows machines in the term of Authentication or Any other things.  

A: Before disabling MD5 via GPO, you had better check whether you have any old application or programs or old Operating System to still use MD5, if so, then you cannot disable it.  

Hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou  

============================================   

If the Answer is helpful, please click "Accept Answer" and upvote it.
