---
title: "How to create a Exchange Online Dynamic Distribution list for a AD Security group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1437721/how-to-create-a-exchange-online-dynamic-distributi
question_id: 1437721
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to create a Exchange Online Dynamic Distribution list for a AD Security group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1437721/how-to-create-a-exchange-online-dynamic-distributi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have Microsoft Hybrid Active Directory and so have created an On-Premise universal security group called 'All Sales' and we are going to add all sales reps from all locations to this group.

The issue is I've created a Dynamic Distribution list in Exchange Online but I can't map membership to be only users of the 'All Sales' group.

Please can you advise how this can be done as using PowerShell with the following filter doesn't work {-RecipientFilter "((MemberOfGroup -eq 'CN=All Sales,OU=Groups,DC=,DC=')}, I've also tried ObjectId but I suspect I'm doing something wrong.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-27*

Hi @Adrian Davies  ,

Welcome to our Q&A forum.

According to your description, the filter you are using seems correct, could you please share any error messages after running that?

Besides, you mentioned PowerShell cmdlet with ObjectId filter, does it like the below?

```
New-DynamicDistributionGroup -Name "All Sales DDG" -RecipientFilter {(MemberOfGroup -eq 'ObjectID_of_All_Sales_group')}
```

Based on my research, we can create Dynamic Distribution group with Custom rule in EAC, have you tried this method.

If you're sure that every step is fine, you'll need to wait hours for the membership synchronous.

Please feel free to let us know if any updates.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
