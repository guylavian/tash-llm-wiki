---
title: "ldap issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2720385/ldap-issue
question_id: 2720385
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ldap issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2720385/ldap-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we are trying to get humhum and LDAP to work within our AD environment.  Our current environment is a mixed domain and forest of windows 2008r2 and windows 2012r2. 

basically what we are trying to do is have our users be allowed access into this webpage for training using their network name and password.

The issue that we are seeing is

Status: Error! (Message: 0x50 (Other (e.g., implementation specific) error; 80090304: LdapErr: DSID-0C0903A8, comment: AcceptSecurityContext error, data 20ee, v1db1): CN=LDAP,OU=Users-Undefined,OU=ouUSS-Departments,DC=---,DC=local)

the LDAP account is a domain admin account with all rights to the server

The LDAP is on a member server named netmon using port 389

We are using an LDAP instance named ldap1 with the following account named ldap,

ldap [netmon.---.local:389]

     cn=ldap1,dc=---,dc=local

         cn=lostandfound

         cn=ntds quotas

         cn=roles

I have added the cn=users container and with the user cn=ldap, msds-useraccountdisabled = false

In reading some articles and watching youtube, it states that i must export information from my DC and import it to this location, but when i do it will not import

using ldp i can bind with the local account but still can't get any users to populate

res = ldap_simple_bind_s(ld, 'CN=ldap,CN=users,CN=ldap1,DC=---,DC=local', <unavailable>); // v.3  

Authenticated as: 'CN=ldap,CN=users,CN=ldap1,DC=---,DC=local'.

## Answers

_No answers on this thread._
