---
title: "how to reset sysvol folder to default settings. because all folders inside sysvol are malware-encrypted. and I don't need the old sysvol setup."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/909263/how-to-reset-sysvol-folder-to-default-settings-bec
question_id: 909263
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# how to reset sysvol folder to default settings. because all folders inside sysvol are malware-encrypted. and I don't need the old sysvol setup.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/909263/how-to-reset-sysvol-folder-to-default-settings-bec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have two domain controllers and all DC inside sysvol malware encrypted (dot play). how to reset sysvol folder to default settings?    

and i don't need the old sysvol setup.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-01*

Hi !!!    

Before performing the activity ensure you have clean environment ... ensure that malware / virus or worms are removed from your environment (workstations / servers, etc) using good antivirus solution ...     

The solution is as good as doing a DR with no DC's available (but you should have good backup of your DC as you have to restore it from the backup)    

You may try one thing which is risky but a good option to consider:    

-  Both your DC are corrupt. Decommission one of your DC (ensure the DC that is going to be decommissioned has no roles). If required size the roles to other DC.    

-  Re-name and remove the record of the DC from DNS, DHCP and AD.    

-  Ensure the old name and IP of the decommissioned DC is not available on your network (ping / nslookup).    

-  Stop the replication services or remove your second DC from the network temporarily.    

-  Build a new server and promote it as a DC (using backup / IFM).    

-  Size the roles and make the DC authoritative in your forest using the burflag or above steps shared.    

-  You may have to change the DNS on the client as the new DC as preferred and check on few server if the authentication is working ... using the command set l ... will give you the details for the server from which authentication happened.    

-  Run the environment for a week and if you find the environment good .. remove the second DC forcefully... if required perform ntdsutil option to remove the records and create another DC.    

If you require any information please let me know.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-30*

Hi,    

Hope this help you, kindly test the solution before executing it in production domain:    

DFS:    

https://www.techtarget.com/searchwindowsserver/tip/How-to-rebuild-the-SYSVOL-tree-when-none-exists-in-Active-Directory    

FRS:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-30*

You can give this a try.    

https://gist.github.com/RavuAlHemio/00e51d3ea64731be9d43b01eda18734f    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
