---
title: "Microsoft Active Directory Tiering and Microsoft Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5956052/microsoft-active-directory-tiering-and-microsoft-e
question_id: 5956052
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Active Directory Tiering and Microsoft Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5956052/microsoft-active-directory-tiering-and-microsoft-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I noticed misleading information on Microsoft Learn - AD DS Tier Model

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/tier-model

Microsoft Exchange is complicated system on AD DS Tiering

-  As default installation of Microsoft Exchange Server/System is by default Tier-0-Level service, because of different AD permissions.

-  Second installation of Microsoft Exchange Server/System requires splitting to install service on Tier-1-Level.  

https://learn.microsoft.com/fi-fi/exchange/permissions/split-permissions/split-permissions#active-directory-split-permissions

By reading AD DS Tier Model text reader could make weakenings to the AD-Forest/-Domain without notifying Microsoft Exchange risks.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2026-07-24*

Yep - I'd agree that your concern is reasonable. The current AD DS tiering article discusses administrative tiers in general terms, but it does not mention Exchange Server's unique security implications. Historically, Exchange has been an exception because its default installation grants the Exchange Trusted Subsystem and related security principals extensive permissions in Active Directory. As a result, a compromised Exchange server can potentially be leveraged to compromise the forest, which is why many organizations have historically treated Exchange servers as Tier 0 assets unless Exchange split permissions has been implemented.

That stated, there are a couple of nuances. Microsoft's traditional ESAE/administrative tier model has largely been superseded by the Enterprise Access Model, and newer guidance focuses on control planes rather than strict Tier 0/1/2 classifications. Also, Exchange Server Subscription Edition and recent supported versions have evolved over time, so stating categorically that "Exchange is Tier 0" without qualification could be challenged. It is more accurate to say that a default Exchange deployment has privileges that place it in the Tier 0 security boundary, whereas Exchange configured with Active Directory split permissions reduces those administrative dependencies, although organizations should still evaluate their own risk model.

If you plan to submit feedback through the Microsoft Learn page (via the Suggest a fix option), you might consider the following:

The current AD DS Tier Model article could benefit from additional guidance regarding Microsoft Exchange Server. A default Exchange Server deployment introduces Active Directory permissions (for example, Exchange Trusted Subsystem) that effectively place Exchange within the Tier 0 security boundary. Readers may incorrectly conclude that Exchange servers can be managed as Tier 1 systems, potentially weakening the security of the Active Directory forest. Consider adding a note that default Exchange deployments require Tier 0 consideration, and reference Exchange split permissions as an option to reduce Active Directory administrative dependencies where appropriate. See: https://learn.microsoft.com/exchange/permissions/split-permissions/split-permissions

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
