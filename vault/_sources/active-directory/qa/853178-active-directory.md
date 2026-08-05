---
title: "Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/853178/active-directory
question_id: 853178
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/853178/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to apply new passwords requirement to an OU. This new password policy is to force password renewal every 60 days. Now I know I cant apply a new password policy to an OU, but I am reading something about creating a "Shadow Group" so I can apply the new password policy but all the post I have read step through this process vaguely. Can anyone point me in the direction to creating and applying a password policy to an OU??  

Thanks ahead!!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-25*

Hello  

Thank you for your question and reaching out. I can understand you are  having query related  to password policy for OU.  

This will not work. Password policies MUST be set on domain level, on OU it has no effect for domain logged on users.  

Therefore you can use FGPP, required is Windows server 2008 or higher.  

http://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx  

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-17*

Password policies in Active Directory can be defined only in the Default Domain Policy and it is applied at the root level of the domain.    

That being said, it's possible to create another type of password policies and it's called "Fine-Grained Password Policy" or FGPP.    

This policy can only be set on a user or a Domain Global Group.    

AFAIK, it's not possible to apply a password policy on a OU.    

Here is a good start on FGPP    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt    

hth
