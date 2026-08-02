---
title: "ADFS Hybrid MFA client logon"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/731204/adfs-hybrid-mfa-client-logon
question_id: 731204
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Hybrid MFA client logon

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/731204/adfs-hybrid-mfa-client-logon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hiya,  

We have an hybrid enviroment. We use an ad connect server between on-prem and azure.  

Users of 365 products already use MFA for authentication.  

We are wanting all users when on premise to use MFA when logging on, this includes admin logging on servers.  

I read 2016 server & above supports the mfa adapter does mean if I set up mfa adfs as in the many articles on the internet, the server logon can be mfa or just apps when logged on.  

How does each individual server know weather to use mfa or traditional logon, or would this be based on user config.  

Would you enter email adress etc when logging in server.  

I see there is a staged roll out method does this apply to users or devices.  

Regards  

Do you have to register each server on network or point logon at azure.  

Or does the authication method configured on FS server apply to all devices on site

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-11*

@Michael Wright       

Thank you for reaching out to us. Reviewed your query, its not possible to have MFA triggered for users/admins when they login to client/servers while authentication ( at logon screen ).     

Azure MFA is possible/leveraged for accessing apps which are federated with Azure AD.     

If you want to have Azure MFA triggered while logging to servers, you can leverage NPS Extension with Azure AD. Refer to this article https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-nps-extension-rdg which provides steps on how to setup NPS extension with Azure AD using Remote Desktop Gateway.      

Regarding MFA Adapter, this is related to ADFS Server - the AD FS 2016 Azure MFA adapter integrates directly with Azure AD helps to have MFA for applications which are federated with ADFS.     

In the past we used to have On Premise MFA server which used to offer different capabilities which is depreciated now ( As of July 1, 2019, Microsoft no longer offers MFA Server for new deployments. New customers that want to require multi-factor authentication (MFA) during sign-in events should use cloud-based Azure AD Multi-Factor Authentication ).     

Reference: https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfaserver-windows    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-and-azure-mfa    

Let me know if you have any questions.
