---
title: "Third party Kerberos Realms, and PAC-validation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2241592/third-party-kerberos-realms-and-pac-validation
question_id: 2241592
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Third party Kerberos Realms, and PAC-validation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2241592/third-party-kerberos-realms-and-pac-validation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For years we have helped customers manage Windows Servers and workstations, that log on via third party kerberos MIT-realm, but with the updates and PAC-validatoin requirements all interoperability with such realms seems broken. We help with both FreeIPA deployments (that do indeed add ms-pac) attributes to the tickets, and barebone MIT-deploymnets, that dosen't. Is there no longer any way to handle trust, or logon i such enviroments, se for example this link for the basic strategy:

https://blog.dan.drown.org/kerberos-for-windows-without-ad/

Any tips or pointers are deeply appreciated.

With FreeIPA deployments trust is indeed possible, but unable to logon or access windows resources, when a ticket is used with an uknown SID, that is I am able to access smb-shares on windows servers (or workstations), if I forcefully add SID from FreeIPA, to the filesystem. Without MS-PAC, tickets I cannot see anyway for inteoperability to work like it has for years. Any tips, pointers, or insights are deeply appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-01*

I know the purpose of the Privilege Attribute Certificate in the Microsoft-world. I also understand the importance of enforcing PAC-verification and signatures in the Microsoft-world, due to the serious security problems revealed over the past years.   

But all of our KDCs are MiT-kerberos, some that does not issue MS-PAC, and cannot trivially be configured to do so and using them without PAC (on a lonley workstation or terminal server) would not entail the same risk, as in a pure AD-environment. We also manage installations that use the RedHat-based FreeIPA-framework and these do add MS-PAC and SID-information to the ticket. Before the PAC-enforcement era, all of this coexisted beautifully - but we need to see how we can reestablish some interoperability.   

We are currently experimenting in an lab environment, to see if how far I am able to inter-opt with Microsoft 2025-servers either through a "one computer" AD and a trust relationship with the external kerberos realm, or some other mechanism. It is not an option to deploy a site-wide AD infrastructure along side our main infrastructure, so without some more progress - or for Microsoft clients/servers to accept tickets without PAC, they might have to be removed from the equation.   

I would assume that there are others in the same situation.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-01*

Hi Jostein-Skyfritt,

Thanks for your post. Generally speaking, the Privilege Attribute Certificate (PAC) Data Structure is used by authentication protocols that verify identities to transport authorization information, which controls access to resources. The Kerberos protocol [RFC4120] does not provide authorization. The Privilege Attribute Certificate (PAC) was created to provide this authorization data for Kerberos Protocol Extensions [MS-KILE]. Into the PAC structure [MS-KILE] encodes authorization information, which consists of group memberships, additional credential information, profile and policy information, and supporting security metadata.

Also, Kerberos PAC validation should use the generic pass-through mechanism ([MS-NRPC] section 3.2.4.1). The NETLOGON_TICKET_LOGON_INFO message ([MS-NRPC] section 2.2.1.4.19) MUST be sent to the domain controller (DC) for privilege attribute certificate (PAC) verification. The ticket verification algorithm MUST occur (section 3.2.5).

Reference. How to manage PAC Validation changes related to CVE-2024-26248 and CVE-2024-29056 - Microsoft Support

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-30*

I have come somewhat closer to solve parts of this problem in the freeIPA-case (which do ad SIDs and ms-pac to the kerberos tickets). Via the foreign principials ldap-container in active directory. 

But still a long way for fixing interaoperability, with the Microsoft world.
