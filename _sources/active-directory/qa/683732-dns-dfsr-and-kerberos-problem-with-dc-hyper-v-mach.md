---
title: "DNS, DFSR and Kerberos problem with DC Hyper-V machine after merge checkpoints to parent disk."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/683732/dns-dfsr-and-kerberos-problem-with-dc-hyper-v-mach
question_id: 683732
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# DNS, DFSR and Kerberos problem with DC Hyper-V machine after merge checkpoints to parent disk.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/683732/dns-dfsr-and-kerberos-problem-with-dc-hyper-v-mach (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there.  

For some reason my backup solution couldn't delete checkpoints after running schedule backup. They couldn't be deleted even from PS. So, stopped the VM and exported it. Then, inspected the HDD to view the chain to the parent HDD and run powershell script to merge the checkpoint chain. All run well and after that, created a new VM and appended the main VHDX HDD. Started the server and the problems started. I have DC1 AND DC2. The problem started in DC1. The only way to access file share is trought IP. Created a new user in DC1 and doesn't appear on DC2. Don't know where to start diagnose the problem. I hope someone could help me and understand my english. #bshwjt

## Answer (community) — community member

*upvotes: 1 · updated: 2022-01-10*

Hello MauroSoares,  

Thank you for your question and reaching out.  

I can understand you are facing with AD after merged checkpoint.  

- 	Download AD replication health status tool from Microsoft to see which AD components or services are Healthy or not.  

https://www.microsoft.com/en-in/download/details.aspx?id=30005  

- 	As you  have created new VM then I will suggest you to get MAC and IP of previous VM and bind it to this newly created VM then attach VM  the Disk.  

- 	Please verify DC1’s  IP and DNS IP should be identical as it was before and disable firewall or Antivirus on both DC1 and DC2.  

- 	Please also check Date and Time should be synced and does not skew.  

If above steps does not help and issue still persists then If your DC2 is primary DC and Holds FSMO roles, then I would suggest to Demote DC1 and Re-Format and Promote it again to avoid any further effect to other working DC2.  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-01-06*

dc1 domain controller and all members must use the ip address of DC listed for DNS and no others such as router or public DNS, so remove the router address and do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service.  

The dcdiag did not complete, you could try again with  

Dcdiag /v /c /d /e /s:dc1 >C:\dcdiag.log  

Dcdiag /v /c /d /e /s:dc2 >C:\dcdiag.log

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-06*

Didn't run NTDSUTIL command line since isn't needed on WS2019.  

The GUI methods should work fine.  

What DC appears healthier? DC1 or DC2? I'm confused.  

DC1 and it appears to be the role holder which is good. The event logs did not get cleared either. That and the remnants of the two nonexistent domain controllers junk up the logs which doesn't help either.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
