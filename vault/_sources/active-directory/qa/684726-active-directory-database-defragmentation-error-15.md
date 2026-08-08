---
title: "Active Directory database defragmentation error -1526"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/684726/active-directory-database-defragmentation-error-15
question_id: 684726
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory database defragmentation error -1526

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/684726/active-directory-database-defragmentation-error-15 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have a corrupted Active Directory DB on a RODC.  

Performing the defragmentation, I get this error:  

Operation terminated with error -1526 (JET_errLVCorrupted, Corruption encountered in long-value tree)   

Do you have any idea on how to fix this error?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-12*

I was trying to avoid the demote, but this was the only solution.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-10*

Hello  

Thank you for your question and reaching out.  

I can understand you are facing the issue with AD Database defragmentation.  

The best solution will be Rebuild the Domain controller  

If you've more than one Domain controller you may try to rebuild the DC that is having problems and then re-promote it again.  

-  Remove active directory from the DC. You can do that formatting the hard drive, replacing the drive with a new one (backup the files that you need before formatting the drive). Normally this is done by using the dcpromo /forceremoval, but in corruption scenarios that shouldn't work. Just MAKE SURE that the DC and related Active Directory configuration IS OUT of the DC and is NEVER AGAIN related or CONNECTED to the same network where the ORIGINAL HEALTHY DCs are. Is very important to guarantee this step or you may end up in a complete forest corruption scenario. Perhaps formatting the drive is the best option here... Just in case :)  

-  The second step relates to seizing process. it's SEIZE ROLES, transfers are only possible when the DCs that have FSMO roles are online, but that’s not the case because we formatted the drive, right?  

If your "formatted" DC held any FSMO roles, you must seize them to another online DC. To identify if your “formatted” DC had any FSMO roles in it go to command prompt and type (first install support tools from your windows cd\Support directory):  

netdom query fsmo  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-06*

Hi,    

According to the KB, this error shows that Active Directory Replication doesn't work well.     

-  Perform offline defragmentation of the Active Directory database    

active-directory-replication-error-8451    

So that, I recommend you to check whether Active Directory replication works well by using "repadmin" command.    

And if something error message shows, please check based on the message.     

-  Repadmin    

cc770963(v=ws.11)    

I hope this information will be of use to you.    

Best Regards,    

Zaamasu

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-05*

Not much to go on but the simplest solution may be to demote, reboot, promo it again or just stand up a new one for replacement.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
