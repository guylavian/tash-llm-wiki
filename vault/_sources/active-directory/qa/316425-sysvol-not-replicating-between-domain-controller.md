---
title: "SYSVOL Not REplicating between Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316425/sysvol-not-replicating-between-domain-controller
question_id: 316425
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# SYSVOL Not REplicating between Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316425/sysvol-not-replicating-between-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts!!  

We have 3 Domain Controllers and one of them which is the old DC 2k12 will be subject for decommission.  The 2 is DC 2k16 which the new one and currently thr FSMO holder. Now we have some issue with sysvol replication, something that any of created changes from DC 2k16  is not replicating on the sysvol policies of DC 2k12 .   

My question now is :   

-  What will be the impact in the production of sysvol not replicated or not syncing in the old DC 2k12 ?   

-  Since we will be decommission the DC2k12 is it okay to ignore the issue with sysvol replication ?   

-  Is there an impact to DC2k12 decommission if we ignore the issue is sysvol ? or we should need to fix the issue to avoid any disruption during DC demotion?   

-  Sysvol Policies is not up to date in DC 2k12 but sysvol in 2 new DC 2k16 is same and up to date. is there any methods of procedure we can follow?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-17*

Hi,    

For your questions:    

As you mentioned above, sysvol not not syncing will cause the group policy issue .And the sysvol sync may caused by the ad replication or other issues.    

So before any more changes in the domain, it is suggested to fix the issue firstly.    

You can confirm if there are any ad replication problems or DC issues on each DC by command :    

Dcdiag /v >c:\dcdiag1.log        

Repadmin /showrepl >C:\repl.txt     

repadmin /showrepl * /csv (It will report the replication situation for all the DCs)    

If there are no issues for the ad replication ,you can try to fix the sysvol sync:    

For FRS : you may try to do "D2"on the 2012 DC.(Before this,remember to backup the sysvol folder for the 2016DC and 2012DC.) https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs    

For DFSR: You can try the non-authoritative synchronization on 2012 DC.((Before this, remember to backup the sysvol folder for the 2016DC and 2012DC.))    

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo    

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-04*

Hello,  

Since you are getting rid of the 2K12 you can always orphan it but if you or others else have created any policies on it they will be lost. Better to get replication working then gracefully remove it from the domain as mentioned previously by FafFan and DSPatrick.  

regards,  

Miguel  

https://www.falconitservices.com

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-16*

Yes, it must be fixed. If you're using older FRS you can follow along here.  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

or for DFSR follow along here.  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to Accept as answer if the reply is helpful--
