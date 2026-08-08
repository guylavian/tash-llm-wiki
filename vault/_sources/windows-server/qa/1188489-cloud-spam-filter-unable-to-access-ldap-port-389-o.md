---
title: "Cloud SPAM filter unable to access LDAP port 389 on Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188489/cloud-spam-filter-unable-to-access-ldap-port-389-o
question_id: 1188489
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Cloud SPAM filter unable to access LDAP port 389 on Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188489/cloud-spam-filter-unable-to-access-ldap-port-389-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Cloud SPAM filter service is unable to access LDAP port 389 on Domain Controller (Server 2012 R2). 

Using a windows AD account credentials to establish connection. 

My SonicWall firewall is not blocking ports 389 or 636 and I also have these ports allowed on the server's local firewall via Symantec EP. 

In Group Policy, I also have "Domain controller: LDAP server signing requirements" set to None. I made this change based on a recommendation by SonicWall help.

When I try to telnet to port 389 inside or outside of domain using Putty, I get "Network error: Software caused connection abort".  I have no trouble telnet-ing to port 636.

Please advise as I want Cloud SPAM service to sync LDAP users.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-14*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to

It looks that you have already allowed from your  SonicWall  firewall. However from your Windows Server or PC try to disable or uninstall Symantec EP and Disable local Windows firewall for  temporary purpose.

--If the reply is helpful, please Upvote and Accept as answer--
