---
title: "Replace adfs certificate error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387526/replace-adfs-certificate-error
question_id: 387526
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Replace adfs certificate error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387526/replace-adfs-certificate-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I use the command to modify the adfs certificate    

`    Set-AdfsAlternateTlsClientBinding -Thumbprint  “”    `    

But there is an error as shown below    

What is the problem and how to solve it

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-05-09*

Make sure you run the command from an elevated PowerShell prompt. When you have multiple servers, the cmdLet Set-AdfsAlternateTlsClientBinding tries to reach out all servers of the farm to change their TLS bindings.  

If that fails make sure of the following:  

-  That WinRM is configured on both nodes (run WINRM QC on both nodes)  

-  That the network config and WinRM config allow those servers to talk to each others  

-  That you are using a domain account which is a member of the local adminsitrators group on all ADFS servers.
