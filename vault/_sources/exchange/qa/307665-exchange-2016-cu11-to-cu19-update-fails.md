---
title: "Exchange 2016 cu11 to cu19 update fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/307665/exchange-2016-cu11-to-cu19-update-fails
question_id: 307665
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 cu11 to cu19 update fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/307665/exchange-2016-cu11-to-cu19-update-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

following the 0day reports on exchange, I had to update Exchange 2016   CU11 to a newer CU in order to the install the patch  

I choose to update to CU19  

once all prerequisites were fulfilled, the update started.   

However, it failed & quits at the start of the configuration phase  'Admin Tools Configuration'  

[03/10/2021 09:25:24.0892] [1] Processing component 'Admin Tools Configuration' (Configuring the server.).  

with the following error:  

[03/10/2021 09:25:25.0515] [1] The following 1 error(s) occurred during task execution:  

[03/10/2021 09:25:25.0517] [1] 0.  ErrorRecord: Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Destination'. Specified method is not supported.  

exchange is now offline.  and has been since 5 days.  

I opened a case with Microsoft Support, but there is no progress  

-  Internet search has not revealed much information. A few report similar errors but without a solution.  

One post at https://social.technet.microsoft.com/Forums/en-US/785b904a-0424-4db1-8d6d-4d4afeb1597f/installing-management-tools?forum=exchangesvradmin) point to this command:  

Copy-Item -Path ($RoleInstallPath+"Bin\mmc.exe.config") -Destination (Split-Path (where.exe mmc)) -Force  

 where.exe mmc returns an array of 2 locations system32 and syswow64  

Suggestions, help, solutions are very very welcome  

glenn

## Answer (community) — community member

*upvotes: 1 · updated: 2023-03-19*

mmc.exe  issue still present in CU23   

thanks 2021'glenn

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-19*

I have the same issue before and I have found that if I find the location of the file that is the source of the trusted installer and use the depracted way of acquisition and changing the ability to make changes or access the file itself may help solve the problem by allowing permission to evaluate how to proceed. I'm not an expert at this but I have face the same issue and had to resort to the old way of permissions and sharing and location and so on and so forth then no longer is kept up by Microsoft. I hope this makes some sense but certain files in certain setups especially with x86 syswow system 32 system 64 all in one have presented certain challenges that have answered sometimes completely outside of the box and resorting to older methods of principle and acquisition and ownership and rights and user groups. I will look into those types of solutions although to depracted l find them very useful. A out of the box suggestion.
