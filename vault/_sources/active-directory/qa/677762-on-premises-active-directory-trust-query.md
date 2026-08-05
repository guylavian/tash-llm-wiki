---
title: "On Premises Active Directory Trust Query"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/677762/on-premises-active-directory-trust-query
question_id: 677762
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# On Premises Active Directory Trust Query

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/677762/on-premises-active-directory-trust-query (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please consider this On Premises Active Directory AD Trust Scenario:  

Server Resources exists in NEWDOM.NET Domain (Trusting Domain) i.e Resource Domain.  

Users exist in OLDDOM.ORG Domain. (Trusted Domain) i.e User Domain.  

Users from OLDDOM.ORG need to access resources in NEWDOM.NET.  

The above 2 Domains exist across different Forests.  

A Forest Wide INCOMING trust exists in OLDDOM.ORG domain with selective auth.  

A Forest Wide OUtgoing Trust exists in NEWDOM.NET  

Domain COntrollers are running Windows Server 2016.  

Requirement 1 # GMSA account from OLDDOM.ORG needs to be set up to be used on servers in NEWDOM.NET Domain. GSMA needs to be defined on hosts group in OLDDOM.ORG which will contain computer objects from NEWDOM.NET.  

Query: How to add computer objects from NEWDOM.NET in the AD Group of OLDDOM.ORG cross-forest domain.  

Incase this is not achievable without building bidirectional trust then please let me know.  

Please suggest an alternate method to meet this requirement.  

Requirement 2# We are not setting up the GMSA account directly in the resource NEWDOM.NET domain because the account needs to access shares in OLDDOM.ORG Domain. We think accessing the resources from OLDDOM.ORG IN NETDOM.NET will not be possible with the existing trusts or until we setup Bidirectional Trusts. Kindly Confirm me with your expertise.  

Please suggest an alternate method to meet this requirement.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-30*

Hello MicroTechie,    

Thank you for your question and reaching out.    

I can understand you have questions regarding gMSA account and to access resources from other domains in AD having trust relationship between two AD domains.    

Ans 1 : Please note that gMSA having scope of Domain Wide, The gMSA principal needs to be a group in the same domain, but as long as the group is type Domain Local, you can add computers from the other domain as members to that group, and they are then able to retrieve the password successfully.    

https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/getting-started-with-group-managed-service-accounts    

Ans 2: Create the Domain local group in the domain where you want to grant users access to a resource. Then simply add your users to the group to access the resources of other domain.    

Hope this answers your question  :)    

-----------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
