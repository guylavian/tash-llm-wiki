---
title: "Hyper-V Hosted Domain Controllers Failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53944/hyper-v-hosted-domain-controllers-failing
question_id: 53944
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Hyper-V Hosted Domain Controllers Failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53944/hyper-v-hosted-domain-controllers-failing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm dealing with two domain controllers hosted in Hyper-V, each running Server 2008 R2. One is a primary and the other a secondary. Unfortunately I did not install them so I'll provide as much information as I can.  

Shortly after acquiring this client and assessing the server, the DC 1 (primary) failed to boot, throwing a stop c00002e2 error (device connected to this system is not functioning properly). Since DC 2 was still active, I troubleshot DC 1 for several weeks to no avail. I tried all ntdsutil and esentutl commands to try to rebuild what appeared to be a corrupt database with no luck.  

Fast forward several years (DC 1 has been out of commission this whole time) and DC 2 now finally decides to throw the same error and cease booting properly. Again, I tried all ntdsutil and esentutl commands I could find online, no luck. I find it surprising that so many people report success here.  

I'm now out of options and looking for any assistance at ALL. This network will not function well for long without a DC, as we have several services that rely on DC authentication. Where do I start troubleshooting this?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-06*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-31*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-07-28*

Sounds well beyond trouble shooting. You'll need to restore one of them from a recent backup. If it isn't the role holder then you can seize roles.      

https://support.microsoft.com/en-us/help/255504/using-ntdsutil-exe-to-transfer-or-seize-fsmo-roles-to-a-domain-control      

then perform cleanup.      

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup      

Then build a new replacement for the other one. It's always recommended to have at least two active domain controllers to maintain high availability and for disaster mitigation.    

 --please don't forget to Accept as answer if the reply is helpful--
