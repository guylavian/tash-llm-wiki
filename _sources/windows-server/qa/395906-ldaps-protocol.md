---
title: "LDAPS protocol."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/395906/ldaps-protocol
question_id: 395906
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAPS protocol.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/395906/ldaps-protocol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!  

  After enabling LDAPS in the domain (DCs), should I define any GPO rules to tell the clients computers to only use LDAPS? Or is that automatic? I am asking because we are planning to block LDAP protocol traffic on the firewall between networks segments.  

Hope I was clear enough.  

Thanks.  

Doria

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-17*

Hi,  

LDAPS is automatically enabled when you install an Enterprise Root CA on a Domain Controller. If you install the AD-CS role and specify the type of setup as “Enterprise” on a DC, all DCs in the forest will automatically be configured to accept LDAPS.  

https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.asp  

If you want to secure the connection, you may consider configuring the server to reject Simple Authentication and Security Layer (SASL) LDAP binds that do not request signing (integrity verification) or to reject LDAP simple binds that are performed on a clear text (non-SSL/TLS-encrypted) connection. Policies for your reference:  

Policy Setting: "Domain controller: LDAP server channel binding token requirements"  

Policy Setting: "Domain controller: LDAP server signing requirements"  

https://support.microsoft.com/en-us/topic/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows-ef185fb8-00f7-167d-744c-f299a66fc00a  

Best Regards,
