---
title: "Additional ADFS to a farm with SPN error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/949951/additional-adfs-to-a-farm-with-spn-error
question_id: 949951
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Additional ADFS to a farm with SPN error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/949951/additional-adfs-to-a-farm-with-spn-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

well I have an ADFS Farm that is implemented between my on-premise and Azure VM (primary VM in the on-premise DC and 1st Additional in Azure as a VM)    

we have also additional domain controller in Azure, both VMs are working fine with no issues, we can authenticate as normal from both locations.    

now our issue that when we try to add a 2nd additional VM to the farm we are getting error for the SPN of the service account that we are currently using.     

tried to follow the below URLs but with no luck.    

https://social.msdn.microsoft.com/Forums/en-US/d7ddd8b5-7b60-4035-ba2d-5a7fe683c41a/error-while-adding-other-server-into-adfs-farm?forum=winserver8gen    

https://learn.microsoft.com/en-us/archive/blogs/joeleo/spn-and-user-namepassword-errors-when-trying-to-add-an-additional-ad-fs-server-with-a-group-managed-service-account    

please note: service account is in its default location and havent been moved or edited, all adfs servers are able to communicate over those ports (80, 443, 49443, 5985, 5986)    

thanks,

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-16*

There might be issues with the machines and the service name. You need to ensure that all machines have a different name and that their name IS NOT EQUAL to the name of the AD FS farm service.     

Anyhow, if that's name related, we can't really tell more without you sharing more info about your naming convention.
