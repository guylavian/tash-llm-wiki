---
title: "Domain controller - SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/852682/domain-controller-server-is-not-responding-or-is-n
question_id: 852682
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller - SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/852682/domain-controller-server-is-not-responding-or-is-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

We have domain controllers in 6 different sites, All the domain controllers were running in windows server 2008 OS, As a part of domain controllers upgrade project, we have deployed new domain controllers in windows server 2016 OS.  

Later we noticed the FRS is used for SYSVOL and NETLOGON replication. At present we have mixed up environment, 3 AD sites were running up with the domain controllers in windows server 2016 OS and other 3 sites were running up with the domain controllers in windows server 2008 OS. Now i think before to proceed further with domain controller upgradation, FRS to DFS migration has to be taken care. So i started working on the prerequisites for migration from FRS to DFS  

One of the prerequisites is failing with the  error message when we execute the below mentioned command  

Command executed : Dcdiag /e /test:sysvolcheck /test:advertising  

Error message  :  

Testing server: Site6\NEWSERVER Starting test: Advertising Warning: DsGetDcName returned information for \server1.test.local, when we were trying to reach NEWSERVER. SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE. ......................... NEWSERVER failed test Advertising Starting test: SysVolCheck ......................... NEWSERVER passed test SysVolCheck  

I have manually logged in to the newly deployed domain controller "NEWSERVER" and executed the command net share in the command prompt, i found that SYSVOL and NETLOGON shared were missing.  

Please share your thoughts to fix this issue.

## Answer (community) — community member

*upvotes: 2 · updated: 2022-05-18*

Hello NithyanandhamSingaravadivelu    

I would recommend to ensure the below IP settings on each domain controller:    

-  Each DC / DNS server points to its private IP address as primary DNS server and other internal DNS servers as secondary ones    

-  Each DC has just one IP address and one network adapter is enabled (disable unused NICs).    

-  If multiple NICs (enabled and disabled) are present on server, make sure the active NIC is on top in NIC binding.    

-  Contact your ISP and get valid DNS IPs from them and add it in to the forwarders, Do not set public DNS server in TCP/IP setting of DC.    

Once you are done with above, run "ipconfig /flushdns & ipconfig /registerdns", restart DNS and NETLOGON service on each DC.    

->>I suspect that the SYSVOL and NETLOGON shares are missing on dc2008R2, Open CMD> run "net share" command to confirm the same.    

If the both shares are missing on new DC then you need perform the D2 & D4, also known as authorative & non-authorative restore.    

How to force authoritative and non-authoritative synchronization for DFSR-replicated sysvol replication    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization    

Steps:    

-  First perform D4 on healthy DC (dc2008) then go for D2 on problem DC (dc2016).    

Follow this KB article- Using the BurFlags registry key to reinitialize File Replication Service replica sets: http://support.microsoft.com/kb/290762    

If still issue reoccurs, follow how to rebuild the SYSVOL tree and its content in a domain.    

http://support.microsoft.com/kb/315457/    

-------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-17*

You can work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares    

Also an FYI; The prerequisite before introducing the first 2016 domain controller: domain functional level needs to be 2003 or higher. FRS is still possible but DFSR is recommended.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
