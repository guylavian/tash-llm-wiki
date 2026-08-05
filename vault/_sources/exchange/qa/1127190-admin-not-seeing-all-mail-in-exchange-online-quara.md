---
title: "Admin not seeing all mail in Exchange Online Quarantine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1127190/admin-not-seeing-all-mail-in-exchange-online-quara
question_id: 1127190
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Admin not seeing all mail in Exchange Online Quarantine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1127190/admin-not-seeing-all-mail-in-exchange-online-quara (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our Exchange quarantine I can see all of the quarantined messages as a global admin, a co-worker with security admin role sees most of the quarantine (he sees phish, spam, malware) but he only sees the malware ones that are from the Anti-malware policy, he does not see the ones tagged as malware by the safe-attachments policy. What role or group does he need to be in to see these?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-14*

Hi @Rod MacPherson   ,    

The Quarantine Administrator role group in Email & collaboration roles in the Microsoft 365 Defender portal ,you could reach this link directly: Permissions - Microsoft 365 security    

In addition ,you also need to be members of the Hygiene Management role group in Exchange Online to do quarantine procedures in Exchange Online PowerShell.    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-13*

I don't see a quarantine admin role in either Exchange Admin Center portal nor in Azure AD portal.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-13*

I would add the account to the Quarantine Admin role as well and test that. They have made some changes recently around these perms    

https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/quarantine-admin-manage-messages-files?view=o365-worldwide
