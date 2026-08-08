---
title: "Hybrid Azure AD Join ADFS claims rule to only allow windows 10 versions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/346079/hybrid-azure-ad-join-adfs-claims-rule-to-only-allo
question_id: 346079
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Hybrid Azure AD Join ADFS claims rule to only allow windows 10 versions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/346079/hybrid-azure-ad-join-adfs-claims-rule-to-only-allo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am testing the deployment of Hybrid Azure AD Join in a federated domain to 32k users. We want to limit the rollout to only Windows 10 version 1909 (latest) and later. I know that we can use the Controlled Validation option that Microsoft describes by deleting the SCP in AD and applying the registry values. Our issue with the GPO option is that we have found that users on VPN are not always receiving GPO adn is not a reliable method. AS an alternative, is it possible to modify the ADFS claims rules to only allow version 1909 and above and control access that way?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-06*

The GPO I am referring to the one Microsoft recommends for Controlled Validation hybrid-azuread-join-control    

Windows 10 will look at the registry first before looking in AD for the SCP.    

The reason we want to limit the version is that there are older version of Windows 10 that are in the environment. 1803 and below do not remove the  Azure AD registration automatically so there is a manual process that we want to avoid. We ar ein ten middle of a hardware refresh and only want the latest to apply.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-06*

Those rules are used only for the registration phase. Once the device has registered into Azure AD, it no longer contacts ADFS.  

So I am not sure how a GPO would be relevant in this scheme (unless you mean a GPO with a WMI filter tha would apply only to 1909 and higher?).  

That said, you could control the issuance of the token you need for registration (and add conditions...). But the point would be very limited. And if the machine cannot get a token from ADFS, they will fallback into Synchronized Mode (so they would end up being registered anyways as long as the respective computer is in scope of the synchronization).  

I am curious to know why it matters anyways. What is the issue with lower Windows 10 version being Hybrid Azure AD Joined?
