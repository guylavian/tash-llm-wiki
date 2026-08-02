---
title: "QID70003 is reported for 2012 R2 Domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/83025/qid70003-is-reported-for-2012-r2-domain-controller
question_id: 83025
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# QID70003 is reported for 2012 R2 Domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/83025/qid70003-is-reported-for-2012-r2-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

QID70003 Null Session/Password NetBIOS Access is being reported in Domain controllers ,  

Anyone please suggest is this really a vulnerability or not applicable for Windows 2012 R2

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-02*

Hello @SHANMUGAMSWAMINATHAN-5167,

Thank you for posting here.

We can check if "Anonymous Logon" is the member of "Pre-Windows 2000 Compatible Access" built-in domain group or if "Anonymous Logon" is under Security tab of "Pre-Windows 2000 Compatible Access" built-in domain group.  

If so, we can try to remove it to see if it helps.

Here is a similar case we can refer to.

Qualys showing "Null Session/Password NetBIOS Access" on DCs - Not Sure How/If this can be fixed.  

https://social.technet.microsoft.com/Forums/en-US/6bf6e366-8be2-4cfd-a5ec-3be4396a6f6d/qualys-showing-quotnull-sessionpassword-netbios-accessquot-on-dcs-not-sure-howif-this-can-be?forum=winserverDS

If it does not work,

1.Would you please tell us what you are doing then QID70003 is reported for 2012 R2 Domain controllers?

2.Did you scan DC using one vulnerability scan tool?

Best Regards,  

Daisy Zhou
