---
title: "Beyond post installation task WSUS & SCCM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100121/beyond-post-installation-task-wsus-sccm
question_id: 100121
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Beyond post installation task WSUS & SCCM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100121/beyond-post-installation-task-wsus-sccm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi to all  

It may be a question out of place but what if the Wsus of a SCCM does not leave it in the post installation task or if on the contrary the post installation task is executed and configured.   

Will the SCCM have problems to handle the patches to synchronize them or should it not have any problems at all?  

Is there any Microsoft support document that talks about this particular part (post installation task)?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2020-09-20*

WSUS post installation tasks is mandatory and this task will create the database (SUSDB),  directories, pool in IIS,import the publisher info such as windows,office,SQL etc and other important tasks for ConfigMgr to recognize that, WSUS is ready to be used for synchronization with Microsoft.  

If WSUS is not configured after its role installation, you cannot ConfigMgr for any patching activities because the SUP role will fail to install because it has dependencies on WSUS configuration.  

Regards,  

Eswar  

www.eskonr.com

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-09-20*

There are two possibilities here for what you are referring to. The first is exactly as Eswar described and is the post-installation configuration process.  

The second is the configuration wizard which launches after the post-installation tasks or the first time you launch the WSUS admin console; this wizard configured things like the products, classifications, etc. You should not complete this wizard but should cancel it.
