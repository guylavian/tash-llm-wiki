---
title: "User gets page not found after adfs modal dialog"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238828/user-gets-page-not-found-after-adfs-modal-dialog
question_id: 238828
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# User gets page not found after adfs modal dialog

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238828/user-gets-page-not-found-after-adfs-modal-dialog (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Using Oracle Fusion with ADFS on Windows Server 2016. The user authenticates using ADFS/SSO with no issue. When the user wants to create a spreadsheet they get a windows security dialog box stating EXCEL and then the fqdn of the adfs server. After the user enters his credentials a webpage cannot be found page is displayed.    

The only thing I can see is that the security dialog box states the fqdn of the server not the cname of the server. What I mean by that is, the fqdn of the server is something like svradfs.domain.com whereas our cname for adfs is adfs.domain.com. Could that be the issue?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-01-21*

The FQDN of the farm should be an A record not a CNAME. Cf: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/design/ad-fs-requirements#BKMK_7    

For Windows Integrated authentication to work inside the network and outside the network for a subset of endpoints exposed through the Web Application Proxy, you must use an A record (not CNAME) to point to the load balancers.    

That statement applies even if you don't have load balancers.
