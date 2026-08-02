---
title: "Unsigned LDAP Bind from NT AUTHORITY\\SYSTEM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166367/unsigned-ldap-bind-from-nt-authoritysystem
question_id: 1166367
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Unsigned LDAP Bind from NT AUTHORITY\SYSTEM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166367/unsigned-ldap-bind-from-nt-authoritysystem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am working to reject all unsigned LDAP binds on domain controllers per the recommendation from a security provider.

I have identified/patched all servers requesting unsigned LDAP binds except one which is the local host itself.

My question is: why would a domain controller be issuing unsigned LDAP binds to itself and if I start rejecting unsigned LDAP binds, what might break? How can I stop the localhost from requesting unsigned LDAP binds?

Event viewer output for reference. "LDAP Interface Events" log level set to 2.

bolded word = IP source

Event Viewer: Directory Service Event ID 2889

The following client performed a SASL (Negotiate/Kerberos/NTLM/Digest) LDAP bind without requesting signing (integrity verification), or performed a simple bind over a clear text (non-SSL/TLS-encrypted) LDAP connection. 

Client IP address: 

**linklocalipv6address:**52855

Identity the client attempted to authenticate as:

NT AUTHORITY\SYSTEM 

Binding Type:

0

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-22*

I'm having the same issue. It is either the fulllinklocalipv6 or [::1]. For identity I'm having the same "NT AUTHORITY\SYSTEM" or even Computer names (DOMAIN\PCNAME$).
What I was able to find so far is the DC itself does not use LDAP signing and it is also visible from its own ldapclientintegrity registry value 0. Also, when I run ADUC from the DC it triggers the event ID 2889. When the ldapclientintegrity is set to 1, ADUC does not trigger the 2889, but still have the SYSTEM and PCNAME$ entries. Curious if it will require a reboot to drop all "internal" connections and redo them with LDAP signing.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

Unsigned LDAP binds are generally used as a way to authenticate users or services to a given domain controller. In this case, it appears that the localhost is attempting to authenticate itself to the domain controller in order to access resources or services hosted on that machine.

If you start rejecting unsigned LDAP binds, it is possible that certain services may no longer be able to access the domain controller and may stop working. The localhost should be able to authenticate itself using a signed LDAP bind instead. To stop the localhost from requesting unsigned LDAP binds, you should configure the server to use a signed LDAP bind for authentication. This can be done by setting the LDAP_SIGNING option in the server’s configuration file. Additionally, you should ensure that the server’s DNS is configured correctly and that Kerberos authentication is set up correctly. Once all of these steps have been completed, the localhost should be able to authenticate itself correctly and should no longer attempt to use an unsigned LDAP bind.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

Unsigned LDAP binds are generally used as a way to authenticate users or services to a given domain controller. In this case, it appears that the localhost is attempting to authenticate itself to the domain controller in order to access resources or services hosted on that machine.

If you start rejecting unsigned LDAP binds, it is possible that certain services may no longer be able to access the domain controller and may stop working. The localhost should be able to authenticate itself using a signed LDAP bind instead. To stop the localhost from requesting unsigned LDAP binds, you should configure the server to use a signed LDAP bind for authentication. This can be done by setting the LDAP_SIGNING option in the server’s configuration file. Additionally, you should ensure that the server’s DNS is configured correctly and that Kerberos authentication is set up correctly. Once all of these steps have been completed, the localhost should be able to authenticate itself correctly and should no longer attempt to use an unsigned LDAP bind.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
