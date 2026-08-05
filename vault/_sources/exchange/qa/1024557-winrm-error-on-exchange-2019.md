---
title: "WinRM error on Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1024557/winrm-error-on-exchange-2019
question_id: 1024557
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# WinRM error on Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1024557/winrm-error-on-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange 2019 DAG with 3 three servers and the issue I am facing is on Exchange Toolbox the error message popup every few time    

"Connecting to remote server failed with the following error message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that the computer is accessible over the network, and that a firewall exception for the WinRM service is enabled and allows access from this computer. By default, the WinRM firewall exception for public profiles limits access to remote computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic."    

while executing the winrm get winrm/config, the following result shows    

"Cannot create a WinRM listener on HTTPS because this machine does not have an appropriate certificate. To be used for SSL, a certificate must have a CN matching the hostname, be appropriate for Server Authentication, and not be expired, revoked, or self-signed."    

I just renewed my SSL certificate from Digicert and every thing is working fine from server and client side only the problem is certificate is not showing "Revocation check failed" not the valid status in EAC

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-28*

My mistake, in certificate details in EAC and status is showing "Revocation Check Failed". I already tried to download the .crl files and updated on the server but same problem.    

Any idea of WinRM issue, this issue is also related to this SSL certificate error?
