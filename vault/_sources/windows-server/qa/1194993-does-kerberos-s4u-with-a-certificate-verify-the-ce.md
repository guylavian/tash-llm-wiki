---
title: "Does Kerberos S4U with a certificate verify the certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194993/does-kerberos-s4u-with-a-certificate-verify-the-ce
question_id: 1194993
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Does Kerberos S4U with a certificate verify the certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194993/does-kerberos-s4u-with-a-certificate-verify-the-ce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are attempting verify an Active Directory machine account, using Kerberos S4U with a Certificate.

The client sends the public part of a provisioned certificate to a remote server. The server then attempts to locate the machine account using Kerberos S4U with the public certificate.

All this works as expected.

However, in addition to performing the MS-RCMP to get the account, it was expected that the domain controller would also verify the basic certificate properties, such as expiration, and revocation. However, this seems not to be the case.

Can you confirm if this is the case, and if not, is there a recommendation as to how to verify the certificate?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-03*

Hello there,

Replication between domain controllers will still take place over RPC, even after installing SSL certificates. The payload is encrypted, but not with SSL.

If you use SMTP replication, that replication can be encrypted with the domain controller's SSL certificate.

But domain-joined Windows clients already have SASL signing and sealing and Kerberos, which is already encrypted and is pretty secure. So they'll just keep using that.

Smart card clients make use of the domain controller's SSL certificate when Strict KDC Validation is turned on. It's just an extra measure of protection for smart card clients to be able to verify that the KDC that they're talking to is legitimate.

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-03*

Hello,

Thank you for posting in our Q&A forum.

Kerberos S4U allows the domain controller to verify the computer's mapping, strong mapping and weak mapping. The rest are managed by CAs.

As for verifying certificate attributes, certificate expiration is checked by the computer during self-test, and certificate revocation is checked by the computer when it goes to the CA.

Hope above information can help you.
