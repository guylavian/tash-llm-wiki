---
title: "Active Directory Deligated Access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5443868/active-directory-deligated-access
question_id: 5443868
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-unknown-routing-unknown-platform", "windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active Directory Deligated Access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5443868/active-directory-deligated-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to set a permission in AD for delegated access. I want the group to be able to download software with their own credentials on any computer in the domain without being a full domain admin.  

We're using a windows server 2019.  

Is this possible?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-07-10*

Hello Brannon. This isn't really the right forum for your question, I'd suggest posting in the Windows Server forums instead, specifically under the tag of Active Directory here: https://learn.microsoft.com/en-us/answers/tags/...

That said, what you're asking isn’t directly possible without local admin rights. If users need to install software on domain PCs without being domain admins, your best options are:

› Deploy approved MSI installers via Group Policy, so users can install without elevation.

› Or use a security group to grant local admin rights across machines via GPO.
