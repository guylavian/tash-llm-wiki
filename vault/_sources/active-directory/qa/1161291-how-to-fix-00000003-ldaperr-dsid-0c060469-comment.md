---
title: "how to fix 00000003: LdapErr: DSID-0C060469, comment: Error decrypting ldap message, data 0, v1db1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161291/how-to-fix-00000003-ldaperr-dsid-0c060469-comment
question_id: 1161291
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# how to fix 00000003: LdapErr: DSID-0C060469, comment: Error decrypting ldap message, data 0, v1db1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161291/how-to-fix-00000003-ldaperr-dsid-0c060469-comment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

We have a unique setup that has worked in the past but when trying to recreate it keeps failing

We have created an AD LDS/ADAM instance on a dedicated Win 2008 R2 server then created account using ADSI Edit in that instance that match the accounts in a web based application "maximo" 

We can logon/bind with LDP with the account using port 636 with SSL and port 389

When we logon to maximo we get an error in the ADAM event log

Internal event: The LDAP server returned an error. 

Additional Data 

Error value:

00000003: LdapErr: DSID-0C060469, comment: Error decrypting ldap message, data 0, v1db1

I can't find a lot of info on what this error is.

Anybody else know what this error means?

Cheers

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Sorry for giving the shout out to the wrong user..... my mistake

Hey compdigit44 it was @BOURBITA Thameur that suggested that it was a cert issue.

Certs are issued from a 3rd party "entrust" and use a private key

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

In that case if does sound like a cert issue like R1prime 210 mentioned. What type of cert are you using? Local , 3rd party etc.... if local which CA template was used to create it?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Have you tried logging in with the non-secure LDAP port just for testing purposes?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-16*

Hi,

It seems a certificate problem. 

Check if root certificate is installed correctly on the server. 

Please don't forget to mark helpful reply as answer
