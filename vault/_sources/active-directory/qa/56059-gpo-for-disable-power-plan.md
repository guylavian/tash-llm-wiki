---
title: "GPO for disable power plan"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56059/gpo-for-disable-power-plan
question_id: 56059
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GPO for disable power plan

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56059/gpo-for-disable-power-plan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

 I have a service account that used to login to several workstations across multiple sites.  These workstations display are need to stay on. But because of our GPO, it's going to the sleep mode.   

Without finding these devices and excluded from the GPO.  

Can we apply the setting for this service account to force not to sleep? Or any better solution?  

As

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-02*

Hi Guys,  

  As i said i already have the GPO with these settings. But i need to exclude number of devices using the service account?   

As

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-31*

Hi,  

You can disable the sleep mode by creating a GPO, this would be the easiest option.  

How to set up Power Management by Group Policy in Windows 7 and higher    

https://community.spiceworks.com/how_to/50798-how-to-set-up-power-management-by-group-policy-in-windows-7-and-higher  

Best regards,    

Leon
