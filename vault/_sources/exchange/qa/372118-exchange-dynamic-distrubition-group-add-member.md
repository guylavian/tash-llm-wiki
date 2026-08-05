---
title: "Exchange Dynamic Distrubition Group Add Member"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/372118/exchange-dynamic-distrubition-group-add-member
question_id: 372118
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Dynamic Distrubition Group Add Member

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/372118/exchange-dynamic-distrubition-group-add-member (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have 1 dynamic distribution group and wants to add  1 static user and  1 static distribution group to that dynamic distribution group.  

I didnt find corrent powershell key. Could some one help me ?  

Best Ragards.  

Yakup

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-26*

You don't "add" members to a Dynamic DG, you adjust the recipient filter to include whichever objects you care about. For example, you can use the following to "add" an object with a specific Name value or specific email address:  

```
New-DynamicDistributionGroup -RecipientFilter "Name -eq 'DG' -or PrimarySmtpAddress -eq '******@domain.com'" -Name test -WhatIf
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-27*

Hi @Yakup Akpınar  ,    

Great to see that you've got useful information from michev's reply. You can click "Accept Answer" under his post to close this up and also make answer searching easier for others who encounter a similar issue. Thanks for your understanding.    

In addition, below is the official document about how to manage Dynamic Distribution groups, hopefully you can find it helpful:    

Manage dynamic distribution groups    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
