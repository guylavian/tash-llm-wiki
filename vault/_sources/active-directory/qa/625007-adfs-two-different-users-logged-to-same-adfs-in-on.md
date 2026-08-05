---
title: "ADFS - two different users logged to same ADFS in one browser window"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/625007/adfs-two-different-users-logged-to-same-adfs-in-on
question_id: 625007
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - two different users logged to same ADFS in one browser window

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/625007/adfs-two-different-users-logged-to-same-adfs-in-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can I have 2 identities from one domain logged in to one browser window? E.g. a separate ADFS for external and internal users? One user will be employee and another external worker, which have account in the same domain.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-14*

The short answer is you cannot have two different users authenticated at the same time if they are both using the same ADFS farm. ADFS kepts a bunch of cookies (especially the MSISAuth cookie) that attest that you have already been authenticated. And if you log off and that the application you signed in already is configured properly for signout flow, then you will out from the 1st identity.   

The long answer is that yo might be able to make it work, but at the expense of other features such as SSO. You could disable SSO cookies but you will always be prompted. And you will likely not be able to use the signout features of your apps.  

There are other situations where it might be doable but we would need more info. Such as version of ADFS, federation protocols you are expecting to use during those sessions, if the user is authenticated against the AD claim provider trust or another one, the nature of the relation between the two accounts (are they the same personna?)...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-12*

Hi Radje,    

Yes you can have 2 identities from one domain logged in to one browser window.    

When you create trust connection/s from one domain(forest) to another, users have the option to sign in different domain/s than their home domain (The domain that host their account/s).    

The "Authenticated Users" group on each computer allow users from trusted domain to be authenticated and logon to computer.    

You can also configure Alternate Login ID https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configuring-alternate-login-id    

--------    

--If the reply is helpful, please Upvote and Accept it as an answer--
