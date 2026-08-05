---
title: "ldap_bind: Invalid credentials (49) additional info: 80090308: LdapErr: DSID-0C09050F, comment: AcceptSecurityContext error, data 52e, v4f7c"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191592/ldap-bind-invalid-credentials-49-additional-info-8
question_id: 2191592
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ldap_bind: Invalid credentials (49) additional info: 80090308: LdapErr: DSID-0C09050F, comment: AcceptSecurityContext error, data 52e, v4f7c

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191592/ldap-bind-invalid-credentials-49-additional-info-8 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two forests - each forest has one DC i.e. DC - prod.com and test.com respectively. I've set up a transitive trust between the forest. I'm able to login into DC test.com using the username and password of DC prod.com in RDP. But I'm not able to do the ldapsearch through the same username and password of DC prod.com into DC test.com.

ldapsearch -vx -L -H ldaps://192.19..:636 -D '**@prod.com' -w '' -b "DC=test,DC=com" -s sub "(cn=*)"

I'm getting this error

ldap_bind: Invalid credentials (49) additional info: 80090308: LdapErr: DSID-0C09050F, comment: AcceptSecurityContext error, data 52e, v4f7c

Further more, I'm able to do the LDAP search through the respective DC account.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-24*

Hello Sagar Rana1,  

Thank you for posting in Microsoft Community forum. 

 Here are two similar threads for your references. You can troubleshoot the issue using the possible solution in the two threads.  

openldap - ldap_bind: Invalid Credentials (49) - Stack Overflow

authentication - ldapsearch: Invalid credentials - Stack Overflow

If it does not work above, please check if you can do the same search using built-in LDP.exe tool on Domain Controller.  

Another threads for your reference.  

Unable to bind or log into LDAP using specific credentials - Microsoft Q&A  

If ldapsearch is a non-Microsoft tool?  

I hope the information above is helpful. 

If you have any question or concern, please feel free to let us know. 

Best Regards, 

Daisy Zhou
