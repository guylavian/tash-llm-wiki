---
title: "ADFS 2019 | Multiple ADFS providers, proofup page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165844/adfs-2019-multiple-adfs-providers-proofup-page
question_id: 1165844
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2019 | Multiple ADFS providers, proofup page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165844/adfs-2019-multiple-adfs-providers-proofup-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our environment we need to offer two different MFA providers for employees (Thales) and students (Azure MFA). The selection based on groupmembership is working, but we ran into an issue with Azure MFA for students.

When students does not have a method enrolled in Azure, they need to ProofUp using the https://aka.ms/mfasetup page. But students needs to sign-in to this page, student is being redirected to ADFS and MFA is being forced by AdditionalAuthenticationRules. Is it possible to exclude proofup page from MFA?

If Azure is being used to enforce MFA (Conditional Access Policies), the page is being excluded from MFA. So it seems to possible?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-31*

If you are enforcing MFA on the RP which it sounds like you are, then you cannot exclude that 1 page on the ADFS side. You would need to stop enforcing it there and use something like conditional access in AAD to apply that MFA. Another option is to use TAP https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-temporary-access-pass. This code would be used against Azure AD directly and would allow them to register for Azure MFA.
