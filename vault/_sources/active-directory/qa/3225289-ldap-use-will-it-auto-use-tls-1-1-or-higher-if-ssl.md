---
title: "LDAP use - will it auto use TLS 1.1 or higher if SSL is disabled on servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3225289/ldap-use-will-it-auto-use-tls-1-1-or-higher-if-ssl
question_id: 3225289
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# LDAP use - will it auto use TLS 1.1 or higher if SSL is disabled on servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3225289/ldap-use-will-it-auto-use-tls-1-1-or-higher-if-ssl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The remote service accepts connections encrypted using SSL 2.0 and/or SSL 3.0. These versions of SSL are affected by several cryptographic flaws, including:  

-  An insecure padding scheme with CBC ciphers.  

-  Insecure session renegotiation and resumption schemes.  

An attacker can exploit these flaws to conduct man-in-the-middle attacks or to decrypt communications between the affected service and clients.  

Although SSL/TLS has a secure means for choosing the highest supported version of the protocol (so that these versions will be used only if the client or server support nothing better), many web browsers implement this in an unsafe way that allows an attacker
 to downgrade a connection (such as in POODLE). Therefore, it is recommended that these protocols be disabled entirely.  

NIST has determined that SSL 3.0 is no longer acceptable for secure communications. As of the date of enforcement found in PCI DSS v3.1, any version of SSL will not meet the PCI SSC's definition of 'strong cryptography'.

Consult the application's documentation to disable SSL 2.0 and 3.0.  

Use TLS 1.1 (with approved cipher suites) or higher instead.

## Answer (community) — community member

*upvotes: 0 · updated: 2019-08-06*

Hi intel96

Greetings! I am Vijay, an Independent Advisor. Try posting this question to Technet forum @

Windows IT Pro Technet Forum - 	https://social.technet.microsoft.com/Forums/win...

Do let me know if you have any more question or require further help.
