---
title: "LDAP: error code 12 - 00000057: LdapErr: DSID-0C090B19, comment: Error processing control, data 0, v4563]"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/761199/ldap-error-code-12-00000057-ldaperr-dsid-0c090b19
question_id: 761199
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP: error code 12 - 00000057: LdapErr: DSID-0C090B19, comment: Error processing control, data 0, v4563]

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/761199/ldap-error-code-12-00000057-ldaperr-dsid-0c090b19 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using LDAP protocol pagination to query users in AD group and get exception:  

```
LDAP: error code 12 - 00000057: LdapErr: DSID-0C090B19, comment: Error processing control, data 0, v4563]
```

I can find the meaning of LDAP: error code 12 - 00000057:  LDAP_UNAVAILABLE_CRITICAL_EXTENSION -->Indicates that the LDAP server was unable to satisfy a request because one or more critical extensions were not available. Either the server does not support the control or the control is not appropriate for the operation type.   

But this indicates a certain type of column error, I also need to locate the specific error, and I can't find any information to refer to what " LdapErr: DSID-0C090B19, comment: Error processing control, data 0, v4563" means. Is there any information that can help me locate the cause of the issue?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-08*

Hi    

Have at look at this answer which covers a similar question. https://learn.microsoft.com/en-us/answers/questions/570480/what-does-this-dsid-ldaperr-dsid-0c090aff-error-co.html    

As to the reason for the error, it could be that the server doesn't support the control but if the control is listed in the supported controls in the rootdse you should be good. Most likely reason for the error is that the control has the wrong parameter.    

Gary.
