---
title: "Can I login our ldap user  in windows 10 without AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/340344/can-i-login-our-ldap-user-in-windows-10-without-ad
question_id: 340344
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Can I login our ldap user  in windows 10 without AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/340344/can-i-login-our-ldap-user-in-windows-10-without-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

Our company have 70% Linux users and 30% Windows10 users and Mac.   

We are using LDAP to login the Linux machines.  

To login the Windows machines, we don't have any centralized login (Like LDAP, AD).  

1.So, I just want to check the possibilities to login in Windows10 (pro and home edition) machines via LDAP users (without AD) and can you suggest any third party software for centralized user management for login the Windows, Linux and Mac machines.  

2.If we integrate the LDAP with AD, where have to create the user in common, whether it is LDAP or AD.  

-  can we integrate only windows machine like (pro, home edition) in windows 10 pro

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-03*

You tagged your message with the ADFS Active Directory Federation Services. With ADFS yes, you can use an LDAP directory as a source for authentication starting ADFS on Windows Server 2016. But it means the appications used by the users are trusting ADFS and not your LDAP directory for authentication.  

In other hand, if you are trying to do is to open a session on Windows, then first, this is the wrong tag (it is not an ADFS but an ADDS question) and second, you can't. You can implement a Kerberos Key Distribution Center in one of your Unix servers and do Kerberos authentcation. But not LDAP.  

Also, note that LDAP is not an authentication protocol. Even if your users sits in LDAP, it would make more sense to use an actual authentication protocol to authenticate them (such as Kerberos).
