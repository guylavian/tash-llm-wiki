---
title: "Hybrid Exchange 365 User Name Change"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374156/hybrid-exchange-365-user-name-change
question_id: 1374156
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Hybrid Exchange 365 User Name Change

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374156/hybrid-exchange-365-user-name-change (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We migrate our on-premises mailboxes to exchange online. we have a hybrid deployment. We need to change a user's name. I made the change in on-premises EAC and AD. I allowed it to synch.  I connected to powershell online and ran Connect-msolservice.  I then ran Set-MsolUserPrincipalName -UserPrincipalName oldname@.onmicrosoft.com - UserPrincipalName newname@.onmicrosoft.com

I received that I do not have permissions to run the command.

Is the command correct? Do I use the email address instead? 

Set-MsolUserPrincipalName -UserPrincipalName ******@company.com - UserPrincipalName ******@company.com

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-22*

Hi @mara2021  

If this user is synced from on-premises to Azure AD, you may need to change his UPN in on-premises AD then let it be synced to Azure AD.

Besides, can you find this user with Get-MsolUser -UserPrincipalName ******@.onmicrosoft.com?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
