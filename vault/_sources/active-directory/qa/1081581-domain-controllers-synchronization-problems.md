---
title: "Domain Controllers Synchronization Problems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1081581/domain-controllers-synchronization-problems
question_id: 1081581
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controllers Synchronization Problems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1081581/domain-controllers-synchronization-problems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have a closed network with 4 Domain Controllers (running Windows Server 2012 R2), DC1 DC2 DC3 DC4.    

By accident I have found that the baseline DC is the secondary DC DC2 and not the primary DC DC1 (DC2 is the PDC but DC1 is the master of all other FSMO rules).    

Furthermore, in the Group Policy Management DC1 has the "SYSVOL Permissions are not in sync" error,    

and DC3 & DC4 are Sysvol Inaccessible.    

The Permissions on the Sysvol Folders seem to be identical, there are no networking issues that might cause this,    

and all the repadmin commands ( /syncall, /kcc, etc) return successful.    

Are there any known solutions for this problem ? any checks I may run to better understand the problem ?    

Thank you for your help,    

David.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-11-09*

Hi David,    

first regarding the "failed test SystemLog". The dcdiag checks whether there are any Errors, related to Ad in the last 24 hours if I am not mistaken and reports the test as "failed" if there are such. I personally ignore the results of this speciffic tests or I go and check the Events from the System Log to ensure that there is nothing related to the problem there (this is also most probably the case when it comes to Sysvol replication).    

Now to the other test: "The Current DC is not in the domain controller's OU" That could be an issue or it could be ignored, depending on how your GPO infrastrcuture is built. In order to clarify this further, here a couple of things to check/:    

-  Is there any specific reason for the DC account not to be in the "Domain Controllers" OU in AD? If not, please makes sure the DC accounts are moved back to the OU. You also need to ensure that the Default Domain Controller GPO is applied to the OU.    

-  Is the "Default Domain Controllers" Group Policy linked to the OU, in which the DC3 and DC4 resides?    

-  What does the DFSR event log say on thosse 4x DCs?    

-  Does the output from dcdiag  report anything about the Sysvol (there is a Sysvol replication test)?    

-  Do you have warningss in the dcdiag output, something related to "userAccountControl" attribute?    

Thanks and regards,    

Stoyan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-11-09*

Hi David,    

You need first to differentiate between the common AD replication and the Sysvol Replication, which uses DFS-R to replicate the content of the sysvol. Repadmin will show you only the status of the AD replication and in your case it is OK, because the issue seems to be with the Sysvol replication most probably.    

You can get some more information about what is going on by running a dcdiag on the each DC. You can redirect the output of dcdiag to a text file like this:    

dcdiag /v >dcdiag.txt    

You can then check each individual test and the result of it to get the "big picture".    

Usually, if the sysvol isn't replicated by one of the DC, you can do a non-authoritative restore of the sysvol, using this guide:    

How to force authoritative and non-authoritative synchronization for DFSR-replicated sysvol replication    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization?WT.mc_id=EM-MVP-5002219    

This means you designate the DC with the issues as non-authoritative for the sysvol replica set and it pulls the content from another DC, which is authoritative. You just need to ensure that the one dc you are getting the syvol from has the correct content. Please read the article for more details.     

You can also get more details from the DFSR Event log on each domain controller, but as already mentioned, please do the dcdiag first to check on all the AD related details.     

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

Stoyan Chalakov
