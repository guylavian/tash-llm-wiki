---
title: "Test-ComputerSecureChannel -Repair fails after LDAPS enforcement (February 2021)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/379008/test-computersecurechannel-repair-fails-after-ldap
question_id: 379008
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Test-ComputerSecureChannel -Repair fails after LDAPS enforcement (February 2021)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/379008/test-computersecurechannel-repair-fails-after-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

after applying the latest patches to our DCs, that also included the enforement of LDAPS security fixes, a number of machines (Windows 10) broke their trust with the domain.  

I used to fix these issues via Test-ComputerSecureChannel -Repair or Reset-ComputerMachinePassword. The first one just failed as it "couldn't find the domain" and the second one worked, but the machine was failing the fix.  

I noticed the following client event during my tries:  

TimeCreated  : 30/04/2021 10:43:17  

ProviderName : Schannel  

Id           : 36884  

Message      : The certificate received from the remote server does not contain the expected name. It is therefore not possible to determine whether we are connecting to the correct  

               server. The server name we were expecting is DOMAIN.NAME. The TLS connection request has failed. The attached data contains the server certificate.

As it seems, those commands are now forced to use TLS to do their binding, and if there is no such SAN in the LDAPS certificates, this action fails.  

Takeaway:  

The LDAPS certificates must include the FQDN Domain Name (dns) which is nowhere to be found on the official documentation.  

https://support.microsoft.com/en-us/topic/how-to-manage-the-changes-in-netlogon-secure-channel-connections-associated-with-cve-2020-1472-f7e8cc17-0309-1d6a-304e-5ba73cd1a11e  

For the time being, what worked was a full unjoin, rejoin via WMI -which apparently does not use LDAPS binds, rather, only Netbios ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Opened a case with Microsoft and it seems that using this command is not a bullet-proof method of repairing trusts.  

The official method is to fully unjoin/rejoin the domain.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-30*

For complex issues you could also start a case here with product support.  

https://support.serviceshub.microsoft.com/supportforbusiness  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-30*

They do have it. This is issue is far more complicated than that.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-30*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to Accept as answer if the reply is helpful--
