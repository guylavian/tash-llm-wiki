---
title: "Domain controller issues with updates KB5019964 & KB5021654"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1118593/domain-controller-issues-with-updates-kb5019964-kb
question_id: 1118593
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller issues with updates KB5019964 & KB5021654

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1118593/domain-controller-issues-with-updates-kb5019964-kb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a situation in which we have software that runs on Server 2003 (3 servers total), and we are still in a years-long planning phase to migrate to a more modern solution that would allow us to ditch Server 2003 for good.    

We installed the November 2022 cumulative update (KB5019964) a few weeks ago on one of our domain controllers (running Server 2016).  We soon found out that this broke the connections to file shares on the 2003 servers for any computer that was authenticating through this domain controller.  When rolling back that update didn't resolve the issue, we found a workaround to apply the following registry edits.  This allowed those file shares to start working again without the November updates installed.    

```
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Kdc]  
"KrbtgtFullPacSignature"=dword:00000000  
"ApplyDefaultDomainPolicy"=dword:00000000  
  
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters]  
"RequireSeal"=dword:00000000
```

On November 17, an out-of-band update (KB5021654) was release. Our understanding is that this is supposed to resolve the issue with the file shares.    

We have reinstalled the cumulative update along with this OOB update on this domain controller, and it is still causing the same issues with file shares on our 2003 servers for any computers authenticated through thid DC. For now, we've rolled back the updates again.  Can anyone provide suggestions to move forward with these updates while keeping the file shares for Server 2003 intact?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-06*

You may still need RC4 encryption    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
