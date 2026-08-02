---
title: "How to make LDAP Server integrity to Require signing when promoting DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188153/how-to-make-ldap-server-integrity-to-require-signi
question_id: 2188153
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# How to make LDAP Server integrity to Require signing when promoting DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188153/how-to-make-ldap-server-integrity-to-require-signi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I have observed that after installing ADDS role and promoting it to domain controller. the ldapserverintegrity is setting to none. 

Therefore the default domain controller policy (GPO) is setting it to None.

I don't want to update manually for the GPO. 

Is there any option to set to 'Require Signing' by default when we promoting DC or any powershell command to update directly the GPO 'default domain controller policy'.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-02*

Thanks for your update.

The solution which provides is updating it manually in Group Policy. 

My question was is there any solution which I can update the same policy using powershell cmdlet or any other way?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-02*

Hello Adrien TRANI,

Thank you for posting on the Microsoft Community Forums.

Do you mean in the last sentence of your text that you want to set all LDAP Server integrity to "signature required"? If you choose to update or promote the GPO, all LDAP Server integrity will be changed. If that's what you want and you just can't find a way to do it, I've got a screenshot below to show you how to set it up. 

Kind regards

Neuvi Jiang

============================================

If the answer is helpful, please click "Accept Answer" and vote for it.
