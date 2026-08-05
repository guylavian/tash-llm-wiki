---
title: "GPO Mapped Drive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168827/gpo-mapped-drive
question_id: 168827
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Mapped Drive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168827/gpo-mapped-drive (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I am not sure what is happening regarding a GPO that I have created in order to Map drives on different Domains.  

Basically, we have two domains which have a two way full trust relationship between them. We have a file server on Domain A which holds various files and Security groups. On Domain B I have a user that needs to access files and folders on Domain A. I have created a GPO on Domain B which basically points to a network share via a security group on Domain A.   

I have made the User in Domain B a member of the Security Group in Domain A.   

The GPO is applied BUT the share does not map successfully. However, I am able to map the same GPO drive manually while logged in as the user in Domain B so no problem with the network share. The GPO's I have created are Domain Local. I have tried the same with the Security Group as Global and Universal but still no joy.  

Can someone please help me - this is a real nightmare to troubleshoot.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-20*

Hi,  

Actually, i did a test in my lab too.  

The result is the same , i can map the shared folder from the trust relationship forest manually, but with not luck when using the GPP.  

I'm not sure why this is failed, but would do more research, if there are any updates , i would share here!  

Best Regards,
