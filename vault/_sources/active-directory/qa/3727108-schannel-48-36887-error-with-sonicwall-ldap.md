---
title: "Schannel 48 36887 error with SonicWall ldap"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3727108/schannel-48-36887-error-with-sonicwall-ldap
question_id: 3727108
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Schannel 48 36887 error with SonicWall ldap

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3727108/schannel-48-36887-error-with-sonicwall-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I don't know how many people are having the SChannel 48 36887 error.

I was and found out that my Sonicwall Firewall was trying to communicate with my Windows 2008 R2 DC.

I found the standard error in the system event log and went digging for the last 3 weeks through the different logs and finally found a series of log entries in the Application and Service,
 Directory Service.

 The entries are:

Internal event: An LDAP over Secure Sockets Layer (SSL) connection could not be established with a client.   

Client network address:  

10.16.0.1:54399   

Protocol:  

TCP   

Additional Data   

Error value:  

2148074277 The certificate chain was issued by an authority that is not trusted.   

Internal ID:  

c050725

Internal event: The LDAP server returned an error.   

Additional Data   

Error value:  

00000003: LdapErr: DSID-0C060469, comment: Error decrypting ldap message, data 0, v1db1

Internal event: An LDAP client connection was closed because of an error.   

Client IP:  

10.16.0.1:54399   

Additional Data   

Error value:  

3 The system cannot find the path specified.   

Internal ID:  

c060463

Internal event: An LDAP over Secure Sockets Layer (SSL) connection could not be established with a client.   

Client network address:  

10.16.0.1:54398   

Protocol:  

TCP   

Additional Data   

Error value:  

2148074277 The certificate chain was issued by an authority that is not trusted.   

Internal ID:  

c050725

This coincided with the time of the error 48.

I went up to my firewall and disabled the ldap query and the error has stopped.

I am thinking that it is because the firewall has a self generated certificate.

I hope that this may help someone who is having a similar issue.

## Answers

_No answers on this thread._
