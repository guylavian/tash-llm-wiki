---
title: "Active Directory: Audit Who Logged into a Computer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1110237/active-directory-audit-who-logged-into-a-computer
question_id: 1110237
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory: Audit Who Logged into a Computer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1110237/active-directory-audit-who-logged-into-a-computer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we upgraded our AD Servers and we are missing some important event logs. Old AD Servers had in EventViewer "4625(F): An account failed to log on." with device hostname, but this audit log is missing on our new AD. I set up new AD like old one with help of "auditpol /get /category:*".      

Can somebody help ?    

Thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-15*

Hello SchwandtnerBoris-0763,

Thank you for your reply.

1.Please check whether the AD replication is OK.

2.Have you configured "Audit Logon Events – Success and Failure"?

GPO: Default Domain Controller Policy

Legacy audit policy:  

Computer Configuration\Windows settings\security settings\local policies\audit policy  

Audit Logon Events – Success and Failure

Or use advanced audit policies (advanced audit policies will overwrite all legacy audit policies by default):  

Computer Configuration\Windows settings\security settings\Advanced Audit Policy Configuration  

Logon/Logoff:  

Audit Logon – Success and Failure  

Audit Logoff – Success and Failure  

Audit Account Lockout – Success and Failure

If so, you can try to log on the DC using one incorrect domain account and check if there is any event 4625.

Tip: There is only auditing Success result for the default Audit Logoff settings on DC.  

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-01*

Hello DaisyZhou-MSFT,    

thank you for your reply.    

Our upgrade process was done by adding a new AD servers to domain, and then promote that servers to Domain Controllers. After testing DHCP, DNS .... and rest of the services, we shut down old AD servers (but keep them in case of troubles).     

Everything seems working fine except for audit logs.     

This log is when test user has correcly setup"Log on to:"    

    

When i delete "Log on to" computer from user i no longer see in logs hostname. I see IP address but that's now enough.    

    

Thank you for your time    

Boris Schwandtner

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-01*

Hello SchwandtnerBoris-0763,    

Thank you for posting in our Q&A forum.    

Based on the description "we upgraded our AD Servers", how did you upgrade the AD servers? In-place upgrade the operating system of the AD server or add new server to the same domain and then promote this server to Domain Controller?    

If you performed In-place upgrade the operating system of the AD server, the logs should not be missing, here is a similar thread for your references.    

https://learn.microsoft.com/en-us/answers/questions/1000078/security-event-log-id4740-amp-4767-appear-and-then.html    

If you added new server to the same domain and then promote this server to Domain Controller, I find not all the logs on old server will replicate to new server.    

For example:    

There is no event ID 4625 On old AD server.    

    

There are 4 event ID 4625 On new AD server.    

    

There are 24347 entries for Security logs on old AD server.    

    

There are 13271 entries for Security logs on old AD server.    

    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
