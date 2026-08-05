---
title: "Found dcdiag error in One Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1117619/found-dcdiag-error-in-one-domain-controller
question_id: 1117619
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Found dcdiag error in One Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1117619/found-dcdiag-error-in-one-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have an environment where I have 2 Domain Controllers in DC site and 2 Domain Controllers in DR site. I have Microsoft Exchange as my email solutions but which is placed only for DC site. Now, I want to implement exchange in my DR site. So, when I run exchange setup, I got an error of LDAP search. I checked the exchangesetup log and found the following error:    

[12/05/2022 11:06:56.0082] [0] [ERROR] An Active Directory error 0x51 occurred when trying to check the suitability of server 'DR2.test.local'. Error: 'Active directory response: The LDAP server is unavailable.'    

[12/05/2022 11:06:56.0082] [0] [ERROR] The LDAP server is unavailable.    

After got the error then I checked status in my DR2 server. I went to DR2 server and ran dcdiag from command prompt. After that, I got the following error:    

Starting test: NCSecDesc    

         Ldap search capability attribute search failed on server DR2, return value = 81  

I checked the required ports and all are okay. I checked replication status and global catalog status, It's also okay. Now, I need your suggestion. Please suggest me how I can resolve it. Thanks in Advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hi,    

Thank you for posting your query.    

There are multiple workarounds to these issues:    

Ignore all these errors when running DCDIAG.    

To stop the event log-related errors, enable the built-in incoming firewall rules on DCs so that the event logs can be accessed remotely:    

Remote Event Log Management (NP-In)    

Remote Event Log Management (RPC)    

Remote Event Log Management (RPC-EPMAP)    

This can be done through the "Windows Firewall with Advanced Security" snap-in (WF.MSC), using the firewall group policy (Computer Configuration\ Policies\ Windows Settings\ Security Settings\ Windows Firewall with Advanced Security), or by using NETSH.EXE ADVFIREWALL.    

Go to this link for your reference and other troubleshooting procedures https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcdiag-commands-running-errors    

https://support.microsoft.com/en-us/topic/fix-the-connectivity-test-that-is-run-by-the-dcdiag-exe-tool-fails-together-with-error-code-0x621-766ed248-5a6c-bf63-5f53-932c120bddd6    

-------------------------------------------------------------------------------------------------------------------------------    

If the answer is helpful kindly click "Accept as Answer" and up vote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-06*

Hi @Md. Rubiat Haque   ,    

Please check the below,    

-  Required firewall rules are allowed between the DC's and between Exchange & DC    

-  Check by disabling AV if any    

-  Try enabling GC on DR site DC and check    

-  run repadmin /replsum /errorsonly and check for replication errors between DC's    

-  Not sure which version of Exchange, but you can try running PrepareAD command first and if it completes successfully, then try installing Exchange setup using unattended mode and with /DomainController switch by specifying the primary DC    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/unattended-installs?view=exchserver-2019    

If the above suggestion helps, please click on "Accept Answer" and upvote it
