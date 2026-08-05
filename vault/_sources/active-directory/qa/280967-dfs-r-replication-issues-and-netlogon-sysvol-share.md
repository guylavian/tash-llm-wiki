---
title: "DFS-R replication issues and netlogon/sysvol shares missing on second and third DCs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/280967/dfs-r-replication-issues-and-netlogon-sysvol-share
question_id: 280967
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# DFS-R replication issues and netlogon/sysvol shares missing on second and third DCs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/280967/dfs-r-replication-issues-and-netlogon-sysvol-share (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!    

My question is about decommissioning a domain controller, which led me to discover DFS Replication issues.    

I was in the process of decommissioning one of our Domain Controllers two weeks ago when I received the following message during the step to remove the DNS: "No other domain controller could be contacted, but other domain controller objects are in the directory...":    

    

I then decided to proceed anyway, and at the step to remove DNS, I could not continue without selecting the option "Remove this DNS zone (this is the last DNS server that hosts the zone)", which is not the case for us:    

    

This led me to believe that there was an issue with DNS, but after further investigation, this does not seem to be the case. This domain controller is able to communicate with other DCs based on their DNS name, and according to the output of the command "repadmin /showrepl", it is replicating to our second domain controller.    

Here is some information regarding our goal and our current domain controllers:    

End goal: Resolve DFS-R issues then make Second DC primary. Decommission First DC entirely.    

First DC (Local): Needs to be decommissioned    

Second DC (Local): Needs to become primary DC    

Third DC (RODC - Azure): Secondary RODC, remains the same    

Each DC was joined in order (First, Second, Third) and I would like to decommission the first one as it had an issue with Windows licensing that I could not "recover" from. Without getting too much into the details, the DC was deployed with a trial license/image of Windows, and we could not use our Volume license to activate it without removing the AD role.    

After a bit of digging, I have found that the NETLOGON and Sysvol directories on the Second DC and Third DC were not shared. They are present, but when I use the command "net use" on either DCs, the shares don't appear. On the First DC, however, the folders are shared. This seems to be causing DFS Replication issues on our Domain Controllers.    

For example:    

First DC    

Event log error 4012: "This server has been disconnected from other partners for x days"     

Second DC    

Event log error 5002: "The DFS Replication service encountered an error communicating with partner NTX-SRV-DC-01 for replication group Domain System Volume."    

Event log error 4612: "The DFS Replication service initialized SYSVOL at local path Z:\SYSVOL\domain and is waiting to perform initial replication."    

Third DC    

Event log error #5002: "The DFS Replication service encountered an error communicating with partner NTX-SRV-DC-01 for replication group Domain System Volume."    

Event log error #4612: "The DFS Replication service initialized SYSVOL at local path Z:\SYSVOL\domain and is waiting to perform initial replication."    

I have found a procedure online (https://www.checkyourlogs.net/how-to-fix-missing-sysvol-and-netlogon-share-and-replication-issues-on-new-domain-controller-at-azure/) that says that changing a value in the registry (SysvolReady) would share the NETLOGON and Sysvol directories, but I am not sure if that would fix our problem. What would be the steps to take to identify the problem and fix this kind of replication issue? I simply want to make sure that I'm not implementing a fix for something that doesn't need fixing.    

Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-24*

You'll need to fix the missing sysvol / netlogon before moving roles off and decommissioning the only healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-22*

Hello @Vincent Desroches  ,    

Thank you for posting here.    

Based on the description above, I understand:    

-  You have three DCs in the domain now.    

-  Netlogon folder and SYSVOL folder was shared on the first DC.    

-  Netlogon folder and SYSVOL folder on the Second DC and Third DC were not shared.     

Would you please confirm the following information:    

-  Are all three DCs also DNS servers?    

-  How do you set Preferred DNS server on the three DCs?    

-  The first DC has been disconnected from the second and third DC for x days, is that right？    

-  Is NTX-SRV-DC-01 the first DC name?    

Best Regards,    

Daisy Zhou

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-19*

This one may help. You'll need to correct this before moving roles off and decommissioning the only healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

--please don't forget to Accept as answer if the reply is helpful--
