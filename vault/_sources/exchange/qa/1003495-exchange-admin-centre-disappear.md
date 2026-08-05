---
title: "Exchange Admin Centre disappear"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003495/exchange-admin-centre-disappear
question_id: 1003495
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Admin Centre disappear

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003495/exchange-admin-centre-disappear (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I would like to ask if anyone has encountered a similar problem.    

In our Exchange Hybrid, when I want to create a new o365 account (as for example according to the instructions from https://www.alitajran.com/create-office-365-mailbox-exchange-hybrid/ ), "Office 365 Mailbox" is not in the menu (in figures)    

    

thx for little help

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-13*

Hi @Matej Čech      

According to the screenshot you shared above, your issue seems to be related to RBAC, take a reference at the link here: RBAC hides the Office 365 Mailbox creation link    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

It’s all based around one missing role entry. To see that link you need access to the Get-RemoteDomain command. Members of Recipient Management do not have this.    

```
New-ManagementRole -Parent "View-Only Configuration" -Name "Office 365 Provisioning Link"  
Get-ManagementRoleEntry "Office 365 Provisioning Link\*" | Where { $_.Name -NotLike "Get-RemoteDomain" } | Remove-ManagementRoleEntry  
New-ManagementRoleAssignment -Role "Office 365 Provisioning Link" -SecurityGroup "Recipient Management"
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
