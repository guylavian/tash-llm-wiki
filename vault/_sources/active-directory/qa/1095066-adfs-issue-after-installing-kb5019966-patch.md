---
title: "Adfs issue after installing KB5019966 patch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1095066/adfs-issue-after-installing-kb5019966-patch
question_id: 1095066
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Adfs issue after installing KB5019966 patch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1095066/adfs-issue-after-installing-kb5019966-patch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I am facing issue with my ADFS server after I installed the KB5019966 patch on my windows server 2016. Users are not able to authenticate via ADFS. I checked ADFS is working good using MS claims X-ray testing tool and also IDPinitiatedsignon is set true and working but still getting below error when trying to sign in    

Error details    

Activity ID: 8563c49f-fcb3-408a-ab86-4307b1182e95    

Relying party: Microsoft Office 365 Identity Platform    

Error time: Fri, 18 Nov 2022 08:44:18 GMT    

Cookie: enabled    

User agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42    

Kindly suggest any answers will uninstalling the KB resolves the issue. If yes then how can I make my server upto date with MS release KB patches.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Dear piaudonn,    

Thanks for your quick response. Issues seems resolved    

As checked internally, Microsoft has investigated a new known issue causing enterprise domain controllers to experience Kerberos sign-in failures and other authentication problems after installing the cumulative updates released during this month's Patch Tuesday.     

November 8, 2022—KB5019964 (OS Build 14393.5501) - Microsoft Support    

Microsoft has released optional out-of-band (OOB) updates to fix a known issue triggering Kerberos sign-in failures and other authentication problems on enterprise domain controllers. You do not need to install any update or make any changes to other servers or client devices in your environment to resolve this issue. The OOB updates released today are available only via the Micrsoft Update Catalog and will not be offered by windows updates. Please install KB5021654 patch on your windows server 2016 where you have installed the KB5019964 patch.     

November 17, 2022—KB5021654 (OS Build 14393.5502) Out-of-band - Microsoft Support
