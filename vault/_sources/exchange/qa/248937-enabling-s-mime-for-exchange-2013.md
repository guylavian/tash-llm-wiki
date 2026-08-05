---
title: "Enabling S/MIME for Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/248937/enabling-s-mime-for-exchange-2013
question_id: 248937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Enabling S/MIME for Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/248937/enabling-s-mime-for-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Please share the S/MIME step by step procedure for installation on exchange 2013 server. we are trying to encrypt the emails to external recipients and would like to know the changes required on the exchange server, CISCO and recipient end.  

Exchange--CISCO--Internet  

Thanks  

Priya

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-29*

Hi,Priya.

Here is a Microsoft document on this topic for your reference: S/MIME for message signing and encryption in Exchange Server  

According to it, the general steps are:

1.Install a Windows-based Certification Authority and set up a public key infrastructure to issue S/MIME certificates. Certificates issued by third-party certificate providers are also supported. For details, see Active Directory Certificate Services Overview.

2.Publish the user certificate in an on-premises AD DS account in the UserSMIMECertificate and/or UserCertificate attributes.

3.Set up a virtual certificate collection in order to validate S/MIME. This information is used by OWA when validating the signature of an email and ensuring that it was signed by a trusted certificate.

4.Set up the Outlook or EAS end point to use S/MIME.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
