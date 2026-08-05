---
title: "Exchange and ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/788441/exchange-and-adfs
question_id: 788441
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange and ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/788441/exchange-and-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I have Exchange 2016 hybrid with federated domain and 2 ADFS + 2 WAP servers .  

I want to extend the whole setup to DR site , How can i do DR for ADFS and WAP servers?  

what are the required setup for ADFS and DR in DR site and the changes required on Exchange servers?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-14*

So ADFS Farm can be extended through multiple AD sites?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-29*

By "security process" you mean authentication I suppose? PTA offers a way to keep the authentication on-premises without having to maintain an AD FS infrastructure: https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-pta

If you want to stay with AD FS, you can add multiple AD FS and WAP server to a farm. We do publish some guidance on how to install a part on that in Azure to increase your availability, you might want to have a look there:  

-  Deploying Active Directory Federation Services in Azure  

-  High availability cross-geographic AD FS deployment in Azure with Azure Traffic Manager

You might also want to consider monitoring the AD FS servers with Azure AD Connect Health agents: https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-health-adfs.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-28*

Please find answers:

-    Federation with all office 365 workload

- 

-    ADFS 2016

- 

-    According security regulation , The security process should happen in Onprmise

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-28*

Please specify the following:  

-  Do you federate Exchange and ADFS directly for OWA, or do you have an Exchange Online environment and your AD FS to for all Office 365 workload, not only Exchange.  

Federation with all office 365 workload  

-  What version of AD FS are you using?  

ADFS 2016  

-  Is there any reason why you want to still use AD FS as opposed as other authentication methods which do not have the same challenges in terms of high availability?  

According security regulation , The security process should happen in Onprmise
