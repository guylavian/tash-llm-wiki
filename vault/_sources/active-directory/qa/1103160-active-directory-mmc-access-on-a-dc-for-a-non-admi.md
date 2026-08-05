---
title: "Active Directory MMC Access on a DC for a non Admin users with Delegation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1103160/active-directory-mmc-access-on-a-dc-for-a-non-admi
question_id: 1103160
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory MMC Access on a DC for a non Admin users with Delegation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1103160/active-directory-mmc-access-on-a-dc-for-a-non-admi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm actually working on trying to remove a lot of users who were in the Domain Admin Group. We had all the support equip users inside this groupe but now i removed them.    

I made delegation for them on the active directory and everything works well with RSAT tools on their computers.    

But we have issues when they are working remotly with RSAT, everything is really slow and we cant find or explain why.    

So i give them only a remote access right on one DC for when they are on remote working.    

I Follow this link to do so : https://blog.geralexgr.com/windows/allow-non-admin-users-to-connect-through-rdp-on-domain-controller    

Now, they successfully connect on the DC but they just cant open the MMC like user & computer ADUC, they have a pop up to log with admin rights.    

I tried to check for an answer but can't find. If Someone can help it would be really nice.    

Have a good day

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-29*

Hello GUILLOUOlivier-5426,    

Thank you for posting in our Q&A forum.    

You can try to disable UAC on Domain Controller to see if it helps.    

    

Here is a similar thread with more discussion for your references.    

https://social.technet.microsoft.com/Forums/en-US/729179f4-fb17-4c87-860f-227463364ef8/can-you-allow-mmcaduc-snapin-for-a-domain-user-on-a-domain-controller    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

===============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
