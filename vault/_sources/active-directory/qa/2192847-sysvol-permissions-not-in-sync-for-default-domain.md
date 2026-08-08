---
title: "SYSVOL permissions not in sync for Default Domain Policy and Default Domain Controller Policy between 2012 R2 and 2022 DC's"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192847/sysvol-permissions-not-in-sync-for-default-domain
question_id: 2192847
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# SYSVOL permissions not in sync for Default Domain Policy and Default Domain Controller Policy between 2012 R2 and 2022 DC's

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192847/sysvol-permissions-not-in-sync-for-default-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all

I've just introduced two new 2022 DC's with the goal of demoting and retiring the old 2012 R2 DC's.  Am having an issue whereby I'm getting the error "The SYSVOL permissions for one or more GPOs on this domain controller are not in sync with the permissions for the GPOs on the baseline domain" in Group Policy Management.

The "Domain Admins" were duplicated on all my GPO's except for the Default Domain Policy and Default Domain Controllers Policy.  I found this link https://learn.microsoft.com/en-us/answers/questions/149354/the-sysvol-permissions-for-one-or-more-gpos-on-thi and applied the fixes to all my non-default policies and they all replicated OK.

I'm now battling with the Default Domain Policy and Default Domain Controllers Policy & the reason I think it's complaining is because the permissions on the SYSVOL/domain/policies are different between the 2022 and the 2012 R2 DC's:

Can I safely remove the additional "BUILTIN\Administrators:(RX,W,WDAC,WO)" from the 2012 R2 DC's SYSVOL/domain/policies/XYZ... folders or is there another solution I'm unaware of?

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-15*

Hi CraigShone,

Thank you for posting in the Microsoft Community Forums.

Your goal is to downgrade the old old domain control and retire the domain is it? 

How do you confirm that replication has been confirmed as normal? 

The extra "BUILTIN\Administrators" in the folder in the old server cannot be deleted, which is also a type of permission group. 

You don't need to worry about this error if you just want to demote the old server. The extra group "BUILTIN\Administrators" exists on the 2012 server. 

You can just downgrade and reclaim the old server normally. 

Best regards

Neuvi Jiang
