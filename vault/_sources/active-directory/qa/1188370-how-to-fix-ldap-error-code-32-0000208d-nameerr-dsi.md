---
title: "How to fix LDAP: error code 32 - 0000208D: NameErr: DSID-0310023C, problem 2001"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188370/how-to-fix-ldap-error-code-32-0000208d-nameerr-dsi
question_id: 1188370
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# How to fix LDAP: error code 32 - 0000208D: NameErr: DSID-0310023C, problem 2001

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188370/how-to-fix-ldap-error-code-32-0000208d-nameerr-dsi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am getting error message as below while creating group using ldapContext :   

javax.naming.NameNotFoundException: [LDAP: error code 32 - 0000208D: NameErr: DSID-0310023C, problem 2001 (NO_OBJECT), data 0, best match of: "FQDN" like ou=testou,dc=test,dc=test  

the same is working for create Users operation on the same DC.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-13*

Hi 

LDAP: error code 32 - this is the LDAP error code which means the object doesn't exist 

0x208D is the corresponding windows error code (8333) Directory object not found

The Distinguished Name value you passed to the LDAP function doesn't exist, you will need to create any sub OU\CN before you can create any objects in the sub path.

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-13*

Double-check the Fully Qualified Domain Name on the LDAP side, including the prefixes (cn, ou, etc.), and ensure that it matches your directory configuration within JIRA.
