---
title: "Second Domain controller did not take over"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/689108/second-domain-controller-did-not-take-over
question_id: 689108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Second Domain controller did not take over

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/689108/second-domain-controller-did-not-take-over (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 domain controllers in different sites.  

Second one setup as a backup to the first. They replicate perfectly, both set as global catalogues, both have AD and DNS on them, also have DFS on too.  

All works brilliantly.... until......... the first domain controller failed. I'd have expected all computers to look over to the second one, which for the dns they did, but for the AD and DFS it just collapsed.  

I checked the second domain controller and active directory just would not load and so did DFS so namespace would not work or anything. I couldnt even load the active directory, it just kept looking for the primary domain controller.  

Primary is on server 2012 r2 and the secondary is on 2008 r2 (due to be upgraded)  

Any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-13*

Hello    

Thank you for your question and reaching out.    

I can understand you are facing with one of your DC after Primary goes down.    

In this scenario I would suggest you to check below steps toward to resolve the issue.    

-  Please verify they are BOTH Global Catalog Servers, you can check this in Active Directory Sites and services > NTDS > Properties, you will see a box that should be checked  and probably have to manually assign the second domain controller. Also, try to set DHCP to have both servers in the DNS entries.    

-   If there is any latent metadata from the DC you pulled off the network.  This support link will guide you through removing metadata from any domain controller that no longer exists in your network    

http://support.microsoft.com/kb/216498    

-  Check if the configuration in AD Sites and Services is correct and  also check  that clients are pointing to more than one DNS servers.    

-  The FSMO roles need to always be available, so if you're going keep power off Primary then  you need to take the time to migrate the roles to the other server.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

----------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-10*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
