---
title: "Does the ADFS EnableRelayStateForIdpInitiatedSignOn setting have any impact on existing Relying Party Trusts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/680038/does-the-adfs-enablerelaystateforidpinitiatedsigno
question_id: 680038
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Does the ADFS EnableRelayStateForIdpInitiatedSignOn setting have any impact on existing Relying Party Trusts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/680038/does-the-adfs-enablerelaystateforidpinitiatedsigno (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to update the ADFS configuration and set EnableRelayStateForIdpInitiatedSignOn to 'true'.  

`Set-ADFSProperties -RelaystateForIdpInitiatedSignonEnabled $True`  

I am unsure from the documentation whether this will impact any of our existing configurations, Relying Party Trusts and user authentications or whether enabling this setting could break what is already setup.  

I would imagine that enabling the RelayState would only then take effect if the RelayState URL is provided, otherwise ADFS operating as normal without it.  

I don't really have an easy way to test this behaviour

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-01-11*

Well, this just tells ADFS not to discard the RelayState. So it won't impect applications not using the SAML relay state feature...
