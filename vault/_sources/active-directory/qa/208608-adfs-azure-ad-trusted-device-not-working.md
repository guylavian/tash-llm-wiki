---
title: "ADFS + Azure AD Trusted Device not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208608/adfs-azure-ad-trusted-device-not-working
question_id: 208608
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS + Azure AD Trusted Device not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208608/adfs-azure-ad-trusted-device-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We have a Windows Server 2016 ADFS farm setup with 2 ADFS and 2 ADFS proxy servers. The farm itself is working fine and everything has been running as expected. The farm was setup in a new Windows Server 2016 AD environment so there are no legacy objects for other ADFS farms or anything.    

I am trying to get trusted devices up and running on our ADFS environment using device writeback to make all Azure AD joined devices trusted on the ADFS environment (primarily to get PSSO on these devices when connecting through the ADFS proxy).    

I followed the steps as outlined in https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-device-based-conditional-access-on-premises.    

So far all the objects have been created as far as I can tell using adsiedit and ADUC. Device Writeback is also enabled successfully and I have our devices as objects in the registered devices container in ADUC (including attributes such as displayname, msDS-IsCompliant, msDS-IsManaged which seem to reflect their state in Azure AD/Intune correctly.     

The device registration page shows everything is enabled and green. I do however receive a lot of errors in the Device Registration Service eventlog (mostly Event ID 144) but somehow I only see the description "The description for Event ID 144 from source Device Registration Service cannot be found." which isn't very helpfull.    

According to the guide from Microsoft:     

**    

> "For easiest evaluation, sign on to AD FS using a test application that shows a list of claims. You will be able to see new claims including isManaged, isCompliant, and trusttype. If you enable Microsoft Passport for work, you will also see the prt claim."    

**     

Because of this I would expect to at least see the IsManaged, IsCompliant and trusttype claims when trying to log in to an application. I have created a test application which shows all the claims but I don't see the above claims at all. There is no difference between using a "trusted" and "untrusted" device or different browsers.    

Before I can even test PSSO correctly I assume I need to see these claims first before anything else. I tried to search for related problems already but I can't seem to find anything related to this specific problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-04*

Hello,  

Thank you for your answer. Even when using IE or Edge Legacy mode I do not see the claims as described by the documentation. The only claims I see are:   

-  http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn  

-  http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod  

-  http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationinstant  

I would expect to find the claims IsManaged, IsCompliant and trusttype as well.  

Also I cannot find any official documentation on this only being possible using IE or Edge Legacy mode.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-02*

Device authentication with browsers in that context will only work with IE and Legacy mode of Edge.
