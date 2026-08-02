---
title: "Windows Active Directory setup in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1660121/windows-active-directory-setup-in-azure
question_id: 1660121
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Windows Active Directory setup in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1660121/windows-active-directory-setup-in-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I plan to setup a Windows Active Directory (AD) using VMs (1 for PDC and 1 for BDC) in the Azure cloud environment and it should sync the AD in the on-prem via the established site-to-site IPsec VPN link. What are the pros and cons? Which is better in terms of cost considering the same setup with Microsoft Entra ID?

Thanks,

Archimedes

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-25*

Hello

This can be a very large topic and a difficult question to just answer shortly, but ill give you some summary at least. :)

Entra ID have a lot of more integration with all O365 and Azure services, and is managed by Microsoft with all the resilience you get from that. There are a lot of built-in services you can use to manage your identity's trough Entra ID. Things as MFA is very easy to manage as its just an integrated service, easier mobile managment and much more.

Active Directory of course have more native integration with most application running inside the Windows OS (although Entra ID is constantly evolving in that area, with Entra joined devices and so on). Most customer cases i have been working with have hybrid environment and also an on-premise active directory domain.

Some fundamentals compared between the two

https://learn.microsoft.com/en-us/entra/fundamentals/compare  

Entra Connect

You can also sync your Active Directory accounts from on-premise to Entra ID to create hybrid identity's, these users will exist in both Entra ID and Active Directory for giving you the integration on both services and a more pleasant user experience in hybrid environments.  

https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect  

There might be even more things to consider of course.

If your setting up the Domain Controllers in Azure as a redundancy for domain joined servers in Azure, this might be a big argument why its definitely the right approach. setting up two additional VM:s is of course adding some costs to your environment.   

Entra ID is "free" in its basic form, but a lot of features needs licenses for users.  

Using Entra Connect to sync users from on-premise also "forces" you to manage does users in the on-premise active directory.  

Since this is a large topic, feel free to ask additional questions :)  

Hope this is helpful and remember shared knowledge is the best knowledge 😊

Best Regards,

Timmy Malmgren

If the Answer is helpful, please click "Accept Answer" and upvote it as it helps others to find what they are looking for faster!
