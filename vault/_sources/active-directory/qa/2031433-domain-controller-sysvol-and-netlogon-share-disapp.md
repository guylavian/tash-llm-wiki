---
title: "Domain Controller Sysvol and Netlogon share disappear when DFSR service is started"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2031433/domain-controller-sysvol-and-netlogon-share-disapp
question_id: 2031433
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controller Sysvol and Netlogon share disappear when DFSR service is started

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2031433/domain-controller-sysvol-and-netlogon-share-disapp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We recently moved away from our MSP who had originally setup our entire windows AD network. Unfortunately out migration away from them, was not done with their support as the relationship went south when we told them we were leaving. Anyhow, we went ahead an moved the FSMO roles to our on prem server, a Win 2016 server, and things seemed to be doing well until we attempted to migrate the Sysvol from FRS to DFSR based on recommendations and plans to move to Win 2019 or 2022 in the near future. Now, the migration says that it's at the "eliminated" stage, and won't allow rollback to 0, which I understand is the expected behavior. However, when we run the DFSR service, the sysvol and netlogon share drop off immediately. I have tried rebuilding them, but nothing appears to get copied into the new directories after renaming them except a few top level folders. I have been forced to turn off the DFSR service, and use the registry key "sysvolready" set to 1, to keep the share online. Almost all dcdiag /v test pass, and things appear semi stable, but I know this is a critical issue that needs to be resolved. I have tried all I can think of, but wasn't sure on the next steps. I do have full backups and system state, as well as copies of the sysvol directory and other backups. I also do have a 2019 server in I could look to promote to DC, but I didn't think that was a good idea at this point, as I didn't want to have two servers with same issue. I should have noted that the remaining DC is the only DC in the domain, we only have one domain. Also, most of our users are Entra only joined devices, so I don't know if the current state of the ADDS will impact them, but we do have an on prem file server, and a few other servers. Lastly, I can post any requested test that will help. Thank you for taking your time to help, it's greatly appreciated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-02*

Hello

Thank you for posting in Q&A forum

no matter FRS and DFSR, they all depend on the SYSVOL share

I think that you didn't make sure all the domain controllers get ready at the same status before you go to next stage.

in the final stage. these settings can't rollback. DC will shut down the FRS forever and will turn off the SYSVOL and NETLOGON share, but because the DC is not at the same status, DFSR can success share the SYSVOL and NETLOGON folder.

also, the DC is depending on the netlogon service too, the NETLOGON folder can share will affect the NETLOGON service and effect the DC.

you can try below link to see if it can help you for solve the issue, and also you can rollback from your backup

Troubleshoot missing SYSVOL and Netlogon shares for Distributed File System (DFS) Replication - Windows Server | Microsoft Learn

The good thing is you have the backup. And also, you want to upgrade the system to windows server 2022.

here is my advice:

-  restore a DC which have all the fsmo role. and this dc is in a closed network environment.

-  change FRS to DFSR, because here only have one dc so it won't take you long time

-  clean the DC metadata at the PDC, (if we have A B C three DC, and A is PDC, then we should clean BC)

-  Promote DC which version is windows server 2022 name and IP is same with B or C

-  after all the DC is back to domain again, move FSMO roles to DC B

-  A DC demote and join promote by windows server 2022machine

-  turn the internet on and turn the old environment off.

in this step, you can fix your FSR error and migrate together within a most short time.

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2024-09-01*

Hi,

What is the status of the replication, did you followed the official guidelines from Microsoft as you have not listed what doc or recommendations you followed to migrate the FRS to DFSR?

Please check the Eliminated stage procedure and verify each step whether you have followed please print this doc and check the steps it seems you might have missed some steps - https://techcommunity.microsoft.com/t5/storage-at-microsoft/sysvol-migration-series-part-5-8211-migrating-to-the-8216/ba-p/423516

Also provide the event logs and replsum status from the DC.

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
