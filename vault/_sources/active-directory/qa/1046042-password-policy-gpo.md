---
title: "Password policy GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1046042/password-policy-gpo
question_id: 1046042
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Password policy GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1046042/password-policy-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to enable GPO password security in order users could change change their password every 120 days.    

In GPO I configured :    

Max password age 120 days    

Minimum password age 1 days    

Min owd length 8 charaters    

Compexity Enabled    

Linked to the group users.    

Seems okay everything, but it shows that users must change not after 120 days, but 42 days. Could you help me in this issue?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-10-19*

Hello DiasDT-8403,    

Thank you for posting in our Q&A forum.    

For domain password policy, we must configure domain password policy within the "Default Domain Policy" group policy object, the password policy will take effect.    

If we configure domain password policy in other custom group policy object instead of the "Default Domain Policy", it will not take effect.    

Please check you configured domain password policy within the "Default Domain Policy" group policy object.    

Also, please check whether you configured FGPP in your domain. Because if you have configured FGPP, the FGPP will have a higher priority than domain password policy.    

For more information about FGPP, please read the link below.    

Step-by-Step: Enabling and Using Fine-Grained Password Policies in AD    

https://blogs.technet.microsoft.com/canitpro/2013/05/29/step-by-step-enabling-and-using-fine-grained-password-policies-in-ad/    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
