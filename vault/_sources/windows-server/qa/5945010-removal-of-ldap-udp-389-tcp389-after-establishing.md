---
title: "Removal of LDAP(UDP 389/TCP389) after establishing AD Trust between domains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5945010/removal-of-ldap-udp-389-tcp389-after-establishing
question_id: 5945010
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Removal of LDAP(UDP 389/TCP389) after establishing AD Trust between domains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5945010/removal-of-ldap-udp-389-tcp389-after-establishing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently succeeded in creating a Forest Trust between two domains.

However, we've come across a security problem, and would like to eliminate UDP 389 and TCP 389 permanently. 

Is it possible to remove LDAP (maybe change it to LDAPS? or another possible way) from a trust??? 

I've looked past cases quite a lot, but could not  find anything.!

I would like to know if it is possible and if it is, if there are any past cases.

Thank you in advance for your help.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-07-13*

Hello,

Thank you for your question. In a supported Active Directory forest trust configuration, LDAP over TCP/389 (and UDP/389 where applicable) remains part of the communication required by domain controllers. Microsoft does not support configuring an Active Directory trust to use LDAPS (TCP/636) as a replacement for the standard LDAP ports, nor is there a supported option to establish a forest trust that operates exclusively over LDAPS.

If the requirement is driven by a security policy, the recommended approach is to identify the specific traffic that must be protected and apply the appropriate security controls, such as SMB signing, LDAP signing, LDAP channel binding, or IPsec between domain controllers, rather than blocking the LDAP ports required for trust operations. Permanently blocking TCP/389 or UDP/389 between trusted forests may result in authentication, trust validation, or directory service functionality failing.
