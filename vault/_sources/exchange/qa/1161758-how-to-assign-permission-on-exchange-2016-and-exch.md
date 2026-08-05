---
title: "How to assign permission on exchange 2016 and exchange online for security group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161758/how-to-assign-permission-on-exchange-2016-and-exch
question_id: 1161758
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to assign permission on exchange 2016 and exchange online for security group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161758/how-to-assign-permission-on-exchange-2016-and-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have created an security group and added all of the members and I would like to assign this security group in Exchange 2016 and Exchange online as admin for exchange

When I click on "Org Management"  I don't see the new security group I only see users

Can someone please let me know if i can assign AD security group in exchange 2016 and exchange online

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-19*

You can do this in Azure. Create a new PIM eligible security group and add to the Exchange Admin Azure Role:

[https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/groups-assign-member-owner

On-prem, you can add the universal security group directly  to the Exchange Org Management group using ADUC

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-19*

Hi @lalajee  ,

You could not assign permissions to security groups, only to users. Here is a similar case: Admin Roles to Security Groups

Administrator documentation reference: About admin roles in the Microsoft 365 admin center

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Also, I want to avoid potential security and compliance risks. I recommend upgrading to Microsoft 365 E3, which includes Microsoft 365 Apps and all the familiar applications such as Word, Excel, PowerPoint, and Outlook.
