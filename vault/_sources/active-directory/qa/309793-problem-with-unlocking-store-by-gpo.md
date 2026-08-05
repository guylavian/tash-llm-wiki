---
title: "Problem with unlocking STORE by GPO."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309793/problem-with-unlocking-store-by-gpo
question_id: 309793
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problem with unlocking STORE by GPO.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309793/problem-with-unlocking-store-by-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. I have a problem unlocking Microsoft Store from a domain controller. In GPO, I set the Default Domain Policy to Computer Configuration - Policies - Administrative Templates - Windows Components / Store - Disable all apps from Windows Store: Enabled. And in User Configuration - Policies - Administrative Templates - Windows Components / Store - Disable all apps from Windows Store: Enabled. I run gpupdate / force on the client and the Microsoft Store is still blocked by the administrator. Domain controllers work in the forest on Windows Server 2016, Windows Server 2012 R2, and computers connecting to the domain on Windows 10 Pro. Where and how should I look for the cause of the problem?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-12*

Hi,    

Based on my research ,if you want to use the windows store in the computer, the policy: Disable all apps from Windows Store should be configured to Enabled    

In your gpresult output , the policy was set the disabled , so the store was still blocked by the policy.    

Check the gpresult and find the GPO on which you disabled the policy ,and change it to enabled.    

    

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

This is the result of using gpresult /H.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Both options in local settings are set to disabled. Of course, in the native Polish language.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-11*

As a start I would run `rsop.msc` or `gpresult /h c:\gpresult.htm` on the client to verify whether there is possibly yet another GPO that overwrites the settings.  

Besides, when you set these two settings to "enabled" like you described, you actually disable the STORE. However, your screenshot shows the correct settings to enable the STORE...  

best regards  

Oliver
