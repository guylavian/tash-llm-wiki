---
title: "GPO Method to Push DNS Settings to All PCs in a Domain Environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1666183/gpo-method-to-push-dns-settings-to-all-pcs-in-a-do
question_id: 1666183
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# GPO Method to Push DNS Settings to All PCs in a Domain Environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1666183/gpo-method-to-push-dns-settings-to-all-pcs-in-a-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently facing a challenging task regarding setting DNS configurations for all PCs. I aim to push DNS entries to ensure that all the machines use the correct DNS servers for domain resolution using Group Policy Object.

Methods that were already checked :

Using the Group Policy settings in "Computer Configuration > Administrative Templates > Network > DNS Client > DNS servers". Set it to "Enable" and add IP Address list. Problem here was that, it was only supported on Windows XP. The changes were not reflected on Windows 10 PC's when we tried.

Setting up Group Policy Object present in "Computer Configuration → Policies → Windows Settings → Security Settings → Network List Manager Policies". As mentioned in the link (https://learn.microsoft.com/en-us/answers/questions/1279987/changing-primary-and-secondary-dns-via-gpo). The options informed in this link was not present.

I have already found methods of doing this using a PowerShell and a bat script, but wanted to confirm if such options are available in GPO itself that I may have missed.

Thank you for your assistance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-16*

Hello,

 

Thank you for posting in Q&A forum.

Yes, currently this DNS entry in GPO settings only supports limited OS, it's more recommended to apply the DNS setting by PowerShell or Netsh command.

Sorry for the inconvenience caused and hope this answer help you well.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-14*

Use https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-dnsclient#dns_nameserver

To implement, follow https://learn.microsoft.com/en-us/windows/client-management/understanding-admx-backed-policies

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
