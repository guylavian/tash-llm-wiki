---
title: "DC1 and DC2 sysvol not availbale"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/616929/dc1-and-dc2-sysvol-not-availbale
question_id: 616929
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# DC1 and DC2 sysvol not availbale

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/616929/dc1-and-dc2-sysvol-not-availbale (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

Our AD is composed by 2 DCs.     

On both DC, SYSVOL is not replication.  I already tried many things but even in ADSI.msc I cannot find Domain system volume in DFSR-LocalSettings and the information inside    

     

DCDiag is normal     

 repadmin /replsummary no error    

The issue is only related to Sysvol replicatation.    

thanks in advance for your help.    

Lucas

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-08*

SYSVOL and Netlogon shares are present and shared. The problem is the DFS Replication this is not working on my 2 DCs  

Completely different than you described above. You can simply perform a non authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-08*

Hi there,    

SYSVOL and Netlogon shares aren't shared on a domain controller. The following symptoms or conditions may also occur:    

The sysvol folder is empty.    

The affected domain controller was recently promoted.    

The environment contains domain controllers running versions of Windows earlier than Windows Server 2012 R2.    

DFS Replication is used to replicate the SYSVOL Share replicated folder.    

An upstream domain controller's DFS Replication service is in an error state.    

You can try the below troubleshooting methods    

How to troubleshoot missing SYSVOL and Netlogon shares https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

-------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-05*

Maybe you mean you have nothing at all? If so you can follow along here to rebuild from scratch    

https://gist.github.com/RavuAlHemio/00e51d3ea64731be9d43b01eda18734f    

--please don't forget to `upvote` and  if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-05*

Not much to go on but if you're using older FRS you can follow along here.  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

or for DFSR follow along here.  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
