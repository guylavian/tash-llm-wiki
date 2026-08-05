---
title: "Windows Server 2016 Domain Controller Promotion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/550251/windows-server-2016-domain-controller-promotion
question_id: 550251
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Windows Server 2016 Domain Controller Promotion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/550251/windows-server-2016-domain-controller-promotion (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Greetings.  

We have an Active Directory environment with couple of Windows Server 2008 R2 Domain Controllers.  

We want to introduce\add Windows Server 2016 in the environment & promote it as a Domain Controller\DNS.  

Can anyone please guide us with steps required to perform before promoting windows Server 2016 server as a Domain Controller\DNS?  

Also will there be any impact with existing applications in the environment once we promote windows Server 2016 as a DC\DNS & remove windows server 2008 DCs from environment? (We will point all apps\servers to New DNS servers)  

Thanks Much.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-14*

Hello Raja,    

The operation is very straight forward and if the health of the domain controllers is ok, the process should be seamless for the experience of your environment.    

-  Health check of existing domain server:Use dcdiag and repadmin to check on the health status and AD replication status on your DCs.    

-  install new server 2016 on new machine    

-  join with existing domain    

-  install active directory services on 2016 server (after this, you may decide to run manually adprep /schemaprep and adprep /domainprep on the WS 2016 to have more visibility and control over the FFL and DFL upgrade)    

-  run dcpromo to configure as additional domain controller (this would also elevate the FFL and DFL in case you haven't done it manually)    

-  make it GC     

-  transfer FSMO roles and PDC    

-  run health check    

-  decommission old if all the checks and replication is correct.     

You can find some useful guides here: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers    

Hope this helps you,    

Best regards,

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-09-13*

Hi, adding to DSPatrick, if your domain is older, created pre 2008R2, you might need to migrate FRS to DFS for the SYSVOL.   

Except that it's pretty straightforward with the Add Role feature. If you want to be sure start the wizard, and the prereq will be listed if you have some to do.   

For the impact, usually it's transparent, but just be sure your AD is healthy, like DSPatrick state.   

Thanks
