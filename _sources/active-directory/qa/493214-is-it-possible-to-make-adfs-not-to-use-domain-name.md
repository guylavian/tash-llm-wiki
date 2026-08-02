---
title: "Is it possible to make ADFS not to use domain name to authenticate users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/493214/is-it-possible-to-make-adfs-not-to-use-domain-name
question_id: 493214
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Is it possible to make ADFS not to use domain name to authenticate users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/493214/is-it-possible-to-make-adfs-not-to-use-domain-name (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,    

Please help me.    

Is it possible to make ADFS not to use a domain name to authenticate users.    

UseCase:                    

-  Test1 user account is created in AD LDS and this server is joined with AD (soft.example.com ==10.10.10.11)    

-  ADFS is running on soft1.example.com ==10.10.10.12    

-  I have integrated ADFS with AD LDS for authentication using the below blog. (https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-to-authenticate-users-stored-in-ldap-directories)    

-  Whenever i perform IDP initiated login, I have to key in username/password on the ADFS screen as example\test1 and password if i only give test1 and password, ADFS is not allowing authenticate.    

-  how do i achieve this use-case without domain.    

Thanks.

## Answers

_No answers on this thread._
