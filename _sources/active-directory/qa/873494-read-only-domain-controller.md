---
title: "Read Only Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/873494/read-only-domain-controller
question_id: 873494
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Read Only Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/873494/read-only-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone    

I have a requirement to setup Read Only Domain Controller. I have never setup any domain controller earlier.    

i have two writable domain controllers DC1,DC2 which are 2019 OS. I need to setup a RODC in DMZ which is RODC1.  Please guide me.    

I came up with new windows 2019 server lets say RODC1.my all servers are hosted in azure.    

As per the below article i  will restrict RPC traffic to a specific port.    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/restrict-ad-rpc-traffic-to-specific-port    

On the new RODC1 i will modify the below registry values.    

Step1--> i will perform this.    

Registry key 1    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters    

Registry value: TCP/IP Port    

Value type: REG_DWORD Value data: 9985    

Registry key 2    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters    

Registry value: DCTcpipPort    

Value type: REG_DWORD Value data: 9986    

Step2-->    

https://blogs.technet.microsoft.com/askds/2009/07/16/configuring-dfsr-to-a-static-port-the-rest-of-the-story/    

dfsrdiag staticrpc /port:9987     

Do i need to execute the above  command on DC1,DC2,RODC1 or only on RODC1?    

Step3-->Since my RODC is in DMZ what ports do i need to allow so that this RODC can communicate with writeable Domain Controllers DC1 and DC2.    

Step4-->Install RODC i will follow the below article    

https://dailysysadmin.com/KB/Article/3947/how-to-create-a-windows-server-2019-rodc-or-read-only-domain-controller/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-03*

i am not clear on this  

Step2-->  

https://blogs.technet.microsoft.com/askds/2009/07/16/configuring-dfsr-to-a-static-port-the-rest-of-the-story/  

dfsrdiag staticrpc /port:9987  

Do i need to execute the above command on DC1,DC2,RODC1 or only on RODC1?
