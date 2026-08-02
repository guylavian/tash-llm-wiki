---
title: "demoting 2008 R2 active directory domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/399359/demoting-2008-r2-active-directory-domain-controlle
question_id: 399359
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# demoting 2008 R2 active directory domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/399359/demoting-2008-r2-active-directory-domain-controlle (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning to demote 2(total 8 DC's) 2008 R2 domain controllers(virtual) and following are some notes:  

We don't have DNS hosted on AD (External, on Infoblox)  

Same with DHCP, on infoblox  

No FSMO roles on these 2  

These are not DFS name space servers  

Not ADFS, KMS or CA hosted on these  

We came across the following article for an impact analysis: https://social.technet.microsoft.com/wiki/contents/articles/50925.active-directory-checklist-for-decommissioning-a-domain-controller.aspx  

One of the action plans suggests to power off the domain controllers for 1 or 2 weeks to remediate any dependencies (after impact analysis) and then demote and decommission the server eventually.  

These 2 seemed to be the first domain controllers in the company.  

Based on your experience, do you see any issues with powering off dc's for 2 weeks? We won't remove the SRV records until they are decommissioned but powering the dc's off will create any slowness in authentication or something?  

We also have Linux servers using LDAP but I am not sure if they will have any impact.  

Please suggest if there are any precautions or steps to take care before we commence the decommission  

Thank you in advance!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-05-18*

Hi,  

Before doing any critical changes in domain, remember to back up the DCs.  

Check other DCs are working well through the following command.  

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps *   

If there are no errors, you can demote the 2 DCs one by one. Then you can keep them as the domain members in the domain or remove them from the domain.  

Or you can do as the mentioned above: Shut down the 2 DCs and monitor for one or two weeks.  

If everything works well, you can remove the 2 DCs safely.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-21*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-18*

Shouldn't be a problem to do this. In the end if the demotion is problematic you can remove from network then easily perform cleanup to remove them.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
