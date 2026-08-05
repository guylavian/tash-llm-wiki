---
title: "GPO with AMD windows 10 Devices Pin issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327656/gpo-with-amd-windows-10-devices-pin-issue
question_id: 327656
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO with AMD windows 10 Devices Pin issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327656/gpo-with-amd-windows-10-devices-pin-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have a Weird problem with few Laptop Computers powered by AMD Ryzen 3 the thing is all computers are joined domain controller and all setting working perfectly for PIN and fingerprint except for these machines and even the error message is different it says "This device doesn't meet your organization's requirements for Windows Hello" usually the error " something went wrong " its related to ADMX but the issues on AMD machines that nothing works whatever I did even I suspected its related to hardware but it didn't I have updated all windows update like other computers and all other policies are working fine disconnected and reconnected again to Domain I even installed fresh windows with all updates but still same error and yes without joining the domain Pin working fine can someone help in this matter? Thanks In Advance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi,  

and sorry for late reply   

yes i did gpupdate and all policies have been pulled   

check the below link where have screenshot of the report  

https://drive.google.com/drive/folders/1lkLITvRGnwYFZxkwe9hn6DkA6y85f9Hw?usp=sharing  

so i see the policies for windows hello has been applied but it didn't work only on these machines   

any thoughts or help about it

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-24*

Hi，  

To know the issue more clearly, you can check the result through the command /: gpresult /h report.html   

Confirm that if the GPO was applied or if any errors there.  

If possible , you can share a screenshot of the gpresult /h report.html here!(please hide the private information)  

Best Regards,
