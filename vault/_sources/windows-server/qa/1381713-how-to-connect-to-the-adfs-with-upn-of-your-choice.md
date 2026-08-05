---
title: "How to connect to the adfs with upn of your choice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1381713/how-to-connect-to-the-adfs-with-upn-of-your-choice
question_id: 1381713
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to connect to the adfs with upn of your choice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1381713/how-to-connect-to-the-adfs-with-upn-of-your-choice (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have an ADFS server that works perfectly well to authenticate users who have a PC in the corporate domain.

On a PC that is not in the domain, you must authenticate manually (normal). 

I have a first upn for which I can log in as ******@domaine.fr

On the other hand I have a second upn for which you have to use DOMAIN username to make it work. 

Is it possible to set the adfs to connect with the upn (******@domaine2.fr) for this second upn?

Thanks for your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-23*

You can change the UPN for each Active Directory Users and Computers user. Next, in the Authentication Policies of ADFS, you can edit the Global Primary Authentication Policy, so configure the allowed UPN suffixes for authentication. You should include domaine2.fr in the list.
