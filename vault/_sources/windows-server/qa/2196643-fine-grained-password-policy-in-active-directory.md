---
title: "Fine-grained Password policy in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196643/fine-grained-password-policy-in-active-directory
question_id: 2196643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Fine-grained Password policy in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196643/fine-grained-password-policy-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to set a different Password Policy for some users in my Active Directory environment.

I go to "Active Directory Administrative Center \ Domain (Local ) \ System \ Password Settings Container "

Is this equivalent as to a GPO? But GPOs are linked to OUs but "Password Setting Container" is linked to AD Security groups?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-15*

Hello Paul Austin1,  

Thank you for posting in Microsoft Community forum.  

Is this equivalent as to a GPO? But GPOs are linked to OUs but "Password Setting Container" is linked to AD Security groups?

A: Yes, this is similar to GPO, but password policy within Default Domain Policy, it applies to all the machines in the domain. FGPP (Fine grained Password Policy) applies to domain users or domain groups, and FGPP takes precedence over domain password policy.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
