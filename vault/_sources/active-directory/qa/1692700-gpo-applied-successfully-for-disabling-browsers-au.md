---
title: "GPO applied successfully for disabling browsers auto updates still its not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1692700/gpo-applied-successfully-for-disabling-browsers-au
question_id: 1692700
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO applied successfully for disabling browsers auto updates still its not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1692700/gpo-applied-successfully-for-disabling-browsers-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,  

 I am applying GPO to disabling browsers auto updates in Windows 2012 Server, it got applied successfully, It got working in multiple environment.   

But its not disabling the browsers auto update in one particular environment even though GPO applied successfully. We have no idea how to fix it. Below are the GPO which we are applying to disable. Could someone help me to fix this issue   

I am looking forward to hearing from you.  

   Select Default Domain Policy and Edit the GPO and Browse to Computer Configuration>Preferences>Windows Settings>Registry.

1)      Chrome

a)      Create new registry with the below values :

        Hive: HKEY_LOCAL_MACHINE

        Key Path: SOFTWARE\WOW6432Node\Policies\Google\Update

        Value Name: AutoUpdateCheckPeriodMinutes

        Value type: REG_DWORD

        Value Data: 0 (Select Decimal)

b)       Create new registry with the below values:

        Hive: HKEY_LOCAL_MACHINE

        Key Path: SOFTWARE\WOW6432Node\Policies\Google\Update

        Value Name: UpdateDefault

        Value type: REG_DWORD

        Value Data: 0 (Select Decimal)  

2)      Firefox       

a)      Create new registry with the below values:

        Hive: HKEY_LOCAL_MACHINE

        Key Path: SOFTWARE\Policies\Mozilla\Firefox

        Value Name: DisableAppUpdate

        Value type: REG_DWORD

        Value Data: 1 (Select Decimal)  

 3)     Microsoft Edge

 a)      Create new registry with the below values:

        Hive: HKEY_LOCAL_MACHINE

        Key Path: SOFTWARE\Policies\Microsoft\EdgeUpdate

        Value Name: UpdateDefault

        Value type: REG_DWORD

        Value Data: 0 (Select Decimal)

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-07*

Hello Jimmy Afflick,  

Thank you for posting in Q&A forum.  

1.Does the problem occur on all the domain machines in this one particular environment? Or only one or some domain machines?  

2.Do all the three browsers still auto update on the domain machines in this one particular environment? Or only one or two browsers still auto update?

Please check the group policy apply result on one problematic machine, for checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".  

If you can see all the gpresult information on this problematic machine, you can check if the registry data you mentioned is changed manually on this machine.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
