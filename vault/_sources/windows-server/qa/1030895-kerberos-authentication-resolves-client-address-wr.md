---
title: "kerberos authentication resolves client address wrong"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1030895/kerberos-authentication-resolves-client-address-wr
question_id: 1030895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# kerberos authentication resolves client address wrong

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1030895/kerberos-authentication-resolves-client-address-wr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two domain controllers. windows server 2019    

In event viewer I am seeing event 4768    

A kerberos authenication ticket TGT was requested.    

The "Client Address" is resolving incorrectly. It is showing the ip of our adfs server, not the client ip.    

This is causing problems with other software. Its not happening for all users but for alot of them.    

Some entries in event viewer show the client address resolving to the proper client ip address.    

I have already restarted, restarted the kerberos authenication service.    

What is the resolution?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

Turning off the ADFS stops these events from being on our domain controllers and the problem stops. However, I don't feel like the client address should be resolved to the ip address of the adfs server.

A Kerberos authentication ticket (TGT) was requested.

Account Information:  

Account Name: ****PROTECTED***  

Supplied Realm Name: ****PROTECTED***  

User ID: ****PROTECTED***

Service Information:  

Service Name: krbtgt  

Service ID: ****PROTECTED***\krbtgt

Network Information:  

Client Address: ::ffff:ip address of ADFS Server  

Client Port: 57764

Additional Information:  

Ticket Options: 0x40810010  

Result Code: 0x0  

Ticket Encryption Type: 0x12  

Pre-Authentication Type: 2

Certificate Information:  

Certificate Issuer Name:  

Certificate Serial Number:  

Certificate Thumbprint:

Certificate information is only provided if a certificate was used for pre-authentication.

Pre-authentication types, ticket options, encryption types and result codes are defined in RFC 4120.
