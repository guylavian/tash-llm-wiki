---
title: "AD DC GPO to limit the number of password changes per 24 hours"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161439/ad-dc-gpo-to-limit-the-number-of-password-changes
question_id: 1161439
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# AD DC GPO to limit the number of password changes per 24 hours

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161439/ad-dc-gpo-to-limit-the-number-of-password-changes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I limit password-changing attempts in  the AD environment for AD users?

Example: One of the AD users changes his/her password one of day. He/She can change the password again on the same day, but we need to refuse 3rd attempt to password change. 

Can we perform the above matter on the on-prem active directory environment? 

I'm waiting for all of your support.

Thanks & Regards.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-17*

Hi,

Yes it's possible by forcing a minimum password age through password policy.

To create and apply a password policy you can use the default domain policy linked on domain level or FGPP:  

Minimum Passowrd age

Password Setting Objects (PSO): Explained

Fine-Grained Password Policy in Active Directory

Please don't forget to accept helpful answer in order to close the thread and help community to identify the correct answer
