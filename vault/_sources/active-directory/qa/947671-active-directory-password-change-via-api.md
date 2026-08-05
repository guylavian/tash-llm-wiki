---
title: "Active Directory Password Change Via API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/947671/active-directory-password-change-via-api
question_id: 947671
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Password Change Via API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/947671/active-directory-password-change-via-api (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,    

I am trying to develop API for manipulate Active directory password change via api call, I connecting to LDAP server via SSL connection but i am unable to change the password due to following issue     

{"lde_message":"0000001F: SvcErr: DSID-031A125F, problem 5003 (WILL_NOT_PERFORM), data 0\n\u0000","lde_dn":null}

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-30*

Hi @Ashan Jayasundara      

Have a look at this article which contains the details of the requirements to set a users password using LDAP - https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/6e803168-f140-4d23-b2d3-c3a8ab5917d2    

From the quick testing I've completed, while article states there are different error codes for each failed validation, it seems they are all result in an WILL_NOT_PERFORM error, with the exception of the following:    

-  Password Complexity - Error: CONSTRAINT_ATT_TYPE - Extended Error Text: Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain    

-  User doesn't have Reset Password permission - Error: INSUFF_ACCESS_RIGHTS, Extended Error Text: The user has insufficient access rights, Access is denied.    

Requirements to set the password for LDAPS:    

-  Password value must be unicode encoded    

-  The password must be surrounded by quotations "<password>"    

-  The modifier must be replace to force password reset    

Requirements to set the password for LDAP:    

-  Password value must be unicode encoded    

-  The password must be surrounded by quotations "<password>"    

-  The modifier must be replace to force password reset    

-  Session Option LDAP_OPT_ENCRYPT must be set    

Gary.
