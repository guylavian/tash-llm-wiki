---
title: "Upgrading a Server 2019 Domain Controller to 2025, Where's ADPREP?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2279846/upgrading-a-server-2019-domain-controller-to-2025
question_id: 2279846
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Upgrading a Server 2019 Domain Controller to 2025, Where's ADPREP?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2279846/upgrading-a-server-2019-domain-controller-to-2025 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a pair of windows 2019 servers I'm trying to upgrade to 2025 with an in-place install and the error is:

|Active Directory on this domain controller does not contain   

Windows Server 2025 ADPREP /FORESTPREP updates. See   

https://go.microsoft.com/fwlink/?LinkId=113955.|
| -------- |
|Active Directory on this domain controller does not contain Windows Server 2025 ADPREP /FORESTPREP updates. See https://go.microsoft.com/fwlink/?LinkId=113955.|

When I search for ADPREP, it is not found on either machine.  I've followed some guides on the web, but none of them are working.  The forest is at 2016 level so that's not the problem.

When I look under roles, Active Directory Domain Services is  installed correctly on both machines.  

I'm kinda stumped, any assistance would be helpful.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2025-05-29*

Refer to https://robertsmit.wordpress.com/2024/11/20/upgrading-to-windows-server-2025-a-step-by-step-guide-ws2025-winserv-azurearc/

On the ISO in the support folder there is the ADPREP folder that should be used to do the forest prep. This and only this ADprep should be used.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-30*

Another question, my PDC is an older server that does NOT have a TPM 2.0 module.  I can get one for $70 and install it if it's necessary to run 2025.

Do I need this before proceeding or can I bypass the TPM requirement?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-29*

thank you for that answer.

Does it matter if I'm doing the non-Primary Domain Controller first as a test to see how it goes?

What does adprep do to the forest?

Hate to see the install fail and me not be able to access anything.
