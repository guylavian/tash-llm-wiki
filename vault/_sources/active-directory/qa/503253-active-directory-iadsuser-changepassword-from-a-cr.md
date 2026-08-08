---
title: "Active Directory - IADsUser ChangePassword from a Cross Domain machine - 80070005"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/503253/active-directory-iadsuser-changepassword-from-a-cr
question_id: 503253
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory - IADsUser ChangePassword from a Cross Domain machine - 80070005

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/503253/active-directory-iadsuser-changepassword-from-a-cr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When changing the password for a domain user using the IADsUser::ChangePassword (binded using the domain user's credential) from a machine that is connected to another domain, I get HRESULT 0x80070005 error.  

All the required ports have been opened and User cannot change password flag is not enabled for the user in AD.  

When binding the IADsUser instance with domain administrator credentials, the ChangePassword function works fine in the same machine.  

Is this because of any security settings in AD or in the local machine ?

## Answers

_No answers on this thread._
