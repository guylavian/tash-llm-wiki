---
title: "Issue seizing fsmo role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66721/issue-seizing-fsmo-role
question_id: 66721
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Issue seizing fsmo role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66721/issue-seizing-fsmo-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All  

I'm trying to transfer fsmo role from a 2008 sbs to 2012 r2 server but having some issue transferring the PDC and RID master roles. The others (schema master, naming master and infrstructure master) were trasnfered successfully.  

i ran ntdsuil.exe and seize the PDC and RID and it says 'transferred successful - seizure not required'  

However 'netdom query fsmo' shows it's still on the sbs 2008.   

Now this is where its get even more complicated. When you open AD user and computer and check operations master on the 2012 server it shows the PDC and RID master as the 2012 server but on the 2008 sbs it still shows the server 2008 as the operation master for PDC and RID and does not allow it to be change there either as it list its own self as the server to change to.  

Any solution will be appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-14*

Hi,  

Thank you for posting in our forum.  

Because the log you upload needs some time to analyze, I will update it as soon as I finish the analysis.  

Thank you for your understanding and support  

Best wishes  

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-14*

EjzNIORlXstLv-nvypwMUX4B_eDoFiqBB8D0O-MmC8s2Fg

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-14*

Sounds like some things are broken. Please run;  

-  Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log  

-  repadmin /showrepl >C:\repl.txt  

-  ipconfig /all > C:\dc1.txt  

-  ipconfig /all > C:\dc2.txt  

then put unzipped text files up on OneDrive and share a link.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-14*

They are both on premise vms running on same host. It not a migration from onprem to cloud or vice versa so not like any ports being blocked by firewall. however just to give it a try i disable local firewall on both dc and still same issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-14*

Sounds like some ports may be blocked between the networks. I'd check the required ports are flowing     

https://support.microsoft.com/en-us/help/179442/how-to-configure-a-firewall-for-domains-and-trusts  

https://www.microsoft.com/en-us/download/details.aspx?id=24009  

--please don't forget to Accept as answer if the reply is helpful--
