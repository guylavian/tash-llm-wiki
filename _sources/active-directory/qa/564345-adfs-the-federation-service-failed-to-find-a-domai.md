---
title: "ADFS The Federation Service failed to find a domain controller for the domain  EXAMPLE.LOCAL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/564345/adfs-the-federation-service-failed-to-find-a-domai
question_id: 564345
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS The Federation Service failed to find a domain controller for the domain  EXAMPLE.LOCAL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/564345/adfs-the-federation-service-failed-to-find-a-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to configure ADFS and am encountering an issue where ADFS is logging event ID 238 "The Federation Service failed to find a domain controller for the domain example.local"

This event is logged any time I attempt to test ADFS by using  

https://my-adfs-server/adfs/ls/idpinitiatedsignon.aspx? where it prompts me for AD credentials and then brings me to an error page:

An error occurred  

An error occurred. Contact your administrator for more information.  

Error details  

Activity ID: ba3a2f96-7798-4aa7-1000-0080010000c3  

Error time: Thu, 23 Sep 2021 19:17:46 GMT  

Cookie: enabled  

User agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47

From the ADFS server I am able to use nltest just fine:

C:\Users\myuser>nltest /dsgetdc:example.local  

DC: \DC-SERV.example.local  

Address: \10.200.1.11  

Dom Guid: f445d18a-5f41-4527-8a87-1a0f39e6e5fa  

Dom Name: example.local  

Forest Name: example.local  

Dc Site Name: NorthPole  

Our Site Name: NorthPole  

Flags: PDC GC DS LDAP KDC TIMESERV WRITABLE DNS_DC DNS_DOMAIN DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8 DS_9 DS_10 0x20000  

The command completed successfully

I made sure the ADFS service user has the 'Allowed to Authenticate' permission on both of our DCs.  

There is no firewall in between the ADFS server and the DC either.  

The ADFS server is definitely joined to our domain because I'm logging on to it with my domain user and it's listed in the correct AD container.

Any further insight into why ADFS acts like it cannot locate our DC?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-02*

Not sure... 238 is an AttributeStoreFindDCFailedError. Maybe there is something odd in some clains rules that are used to pull attributes from AD. Can you try to run something like LDP on the ADFS server (it comes with the AD DS server tools) and connect to the DC? That would validate that LDAP is also working.  

Are you picking an application when you are on this page? Does authentication work in SP-Initiated flow?  

I would recommend you configure and test the Claim X Ray app and trigger a WS-Fed authentication too. Just to validate that the type of flow and the rules aren't the culprit.  

https://adfshelp.microsoft.com/ClaimsXray/TokenRequest
