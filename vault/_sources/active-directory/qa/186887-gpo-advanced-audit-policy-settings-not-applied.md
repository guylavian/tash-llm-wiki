---
title: "GPO Advanced Audit Policy Settings Not Applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186887/gpo-advanced-audit-policy-settings-not-applied
question_id: 186887
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO Advanced Audit Policy Settings Not Applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186887/gpo-advanced-audit-policy-settings-not-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I would like to know why my changes to Advanced Audit Policy Configuration in a GPO attached to an OU are not being applied to member servers (running windows server 2016)? I have done everything to check what's going on but I always see local group policy as the wining policy for this setting, but all other changes are successfully applied on the local GP.  

-  running the command `auditpol.exe /get /category:*` shows me totally different settings than what I have in my GPO  

-  also checked the results of this command `gpresult /H c:\gpresults.html` and shows me that for advanced auditing the local policy is winning  

-  for some reason my advanced audit changes are not showing under the settings tab when clicking on the GPO in the group policy management  

-  I did also enable `Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings`

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-04*

Hi,  

Check if there is a WMI or group filter set on the GPO.  

run the following command to get more details about all GPO settings and filters applied on the server.  

```
gpresult /H c:\gpresult.html
```

Please don't forget to mark this reply as answer if it help you to fix your issue
