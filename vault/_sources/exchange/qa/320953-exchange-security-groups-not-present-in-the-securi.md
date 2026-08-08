---
title: "Exchange Security Groups not present in the Security of organizational units and on users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320953/exchange-security-groups-not-present-in-the-securi
question_id: 320953
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Security Groups not present in the Security of organizational units and on users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320953/exchange-security-groups-not-present-in-the-securi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Goodmorning everyone,  

I have implemented a coexistence between an Exchange 2010 and an Exchange 2016.  

In doing the move on the DB of 2016 I have an error extended on several users related to the homeMDB permissions  

Error: MigrationPermanentException: Active Directory property 'homeMDB' is not writable to recipient  

The prepareAD did not give me any errors during the installation phase of Exchange 2016  

I have checked the versions from ADSI and they are all up to date.  

The Exchange Security groups all exist, also because an Exchange 2010 is already present in the environment  

However, I realized that they are not present in the OU and user security  

Some users, I was able to move them, as they had the correct ACLs and did not have active inheritance  

By adding Exchange Trusted Subsystem, on individual user objects, I am able to make the move  

I wanted to restore the permissions upstream, to act in propagation on everyone  

Would it be enough to re-run Setup / PrepareAD?  

Are there other solutions to be adopted?  

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-18*

Running PrepareAD wont fix it if inheritance is blocked. I would just through those steps and fix:  

https://support.microsoft.com/en-us/topic/-active-directory-property-%E2%80%8E-homemdb%E2%80%8E-isn-t-writeable-on-recipient-error-when-moving-a-mailbox-to-office-365-5f6d0a0a-d09e-93cb-395e-f19d609e5ba4
