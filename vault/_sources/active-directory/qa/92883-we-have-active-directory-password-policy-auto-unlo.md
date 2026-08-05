---
title: "We have active directory password policy auto-UNLOCK configured but some users are locked for days"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/92883/we-have-active-directory-password-policy-auto-unlo
question_id: 92883
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# We have active directory password policy auto-UNLOCK configured but some users are locked for days

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/92883/we-have-active-directory-password-policy-auto-unlo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts, as the title mentions, We have an Active Directory password policy for all users that auto-UNLOCKS the user account after a half an hour. It's working for 99% of users, However a small handful of users have been locked for days, sometimes weeks who have this policy. Is there some reason, some scenario where they will not  be unlocked or do we have some weird issue going on?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-14*

To narrow down the issue , we may need to find out what caused the lockout firstly.

Usually, for troubleshooting account lockout issue, we should follow the general troubleshooting steps below. For your reference :

First of all,looking for event 4740 on the domain controller is , and the computer source can be found through this event (each domain controller needs to confirm whether there is this event ); if not, need to enable the account management audit policy for the domain controller. , In [Computer Configuration \ Windows Settings \ Security Settings \ Local Policies \ Audit Policy \ Audit account management]  

  

Then, find the 4625 event on the client computer source and check the process of the locked account. If there is no 4625 event on the computer source, you need to enable the following audit events if the events:  

Best Regards,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-13*

Hi,  

To know the source IP of lockout ,you have to enable the setting: Audit account logon through a GPO on all members machines and domain controllers.  

You can refer to the following link if you want generate automatically a event for each  account lockout:  

how-to-trace-and-diagnose-account-lockout-in-ad.html  

Please don't forget to mark this reply as answer if it help you to fixe your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-11*

have you checked event logs to see if those user accounts are subject to continuing consecutive failed logon attempts?  

the auto-unlock timer will be reset if the failed attempts continue, and unlock will never occur...

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-11*

Apparently some of the complaints are coming from users failing LDAP authentication, are those not auto unlocked automatically perhaps ?
