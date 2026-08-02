---
title: "Restore of Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/464105/restore-of-active-directory
question_id: 464105
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Restore of Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/464105/restore-of-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All;  

I am running active directory in my network. There are two domain controller installed on windows server 2012 R2 standard x64. One domain controller is running as primary and other is secondary. A few days ago my secondary domain controller crashed and after that I recovered that domain controller using non-authoritative backup restore. But when I rebooted the server it was unable to login. The given error was "trust relationship between the workstation and the primary domain failed".  Please help how can I solve this problem so that my secondary domain controller could work properly.   

Thanks and Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-06*

Hi,    

Welcome to ask here!    

It will be better idea to remove the second DC from domain and then promote it again.    

Steps:    

Shut down the demoted server.    

On a healthy domain controller, clean up the metadata of the demoted domain controller. For more information, see Clean up Active Directory Domain Controller server metadata.    

If the incorrectly restored domain controller hosts operations master roles, transfer these roles to a healthy domain controller. For more information, see Transfer or seize FSMO roles in Active Directory Domain Services.    

Restart the demoted server.    

If you are required to, install Active Directory on the stand-alone server again.    

If the domain controller was previously a global catalog, configure the domain controller to be a global catalog.     

If the domain controller previously hosted operations master roles, transfer the operations master roles back to the domain controller.
